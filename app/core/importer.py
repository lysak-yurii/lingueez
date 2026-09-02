# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Additional terms under AGPL-3.0 section 7 apply to this program; see the
# NOTICE file distributed with this source for details.
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Excel import pipeline, GUI-free.

The analysis phase classifies every spreadsheet row into add/update/skip
(with a reason and human-readable detail); the apply phase inserts/updates
through the DatabaseAdapter so sync keeps working. The caller (UI) lets the
user review the classification and deselect rows between the two phases.

Definitions and tags ride along in optional columns. Merging into a word that
already exists is deliberately non-destructive: a definition is written only
into a field the database left empty, and tags are added to whatever the word
already carries — an import never overwrites or removes what is already there.
"""
import logging
import os
import sqlite3

import numpy as np
import pandas as pd

from app.core.data_management import (
    build_word_index, check_duplicate_entry, normalize_language_pairs,
)
from app.core.db import get_active_db_path
from app.i18n import canonical_language

logger = logging.getLogger(__name__)

REQUIRED_HEADERS = ["Language1", "Language2", "Word1", "Word2"]
OPTIONAL_HEADERS = ["Status", "ID", "Definition", "Definition2", "Tags"]
# Columns worth putting in the template: the required four plus the extras a
# user actually fills in by hand (Status and ID are machine columns).
TEMPLATE_HEADERS = REQUIRED_HEADERS + ["Definition", "Definition2", "Tags"]
TAG_SEPARATOR = ","

ACTION_ADD = 'add'
ACTION_UPDATE = 'update'
ACTION_SKIP = 'skip'

_PY_LEVELS = {'error': logging.ERROR, 'warning': logging.WARNING}


def _noop_log(message, level='info'):
    logger.log(_PY_LEVELS.get(level, logging.INFO), message)


def create_import_template(path):
    """Write an .xlsx import template: the required headers plus example rows."""
    examples = [
        {"Language1": "English", "Language2": "German",
         "Word1": "house", "Word2": "Haus",
         "Definition": "a building people live in",
         "Definition2": "ein Gebäude, in dem Menschen wohnen",
         "Tags": "noun, home, A1"},
        {"Language1": "English", "Language2": "Ukrainian",
         "Word1": "dictionary", "Word2": "словник",
         "Definition": "a book listing words and their meanings",
         "Definition2": "книга зі словами та їх значеннями",
         "Tags": "noun, study"},
    ]
    pd.DataFrame(examples, columns=TEMPLATE_HEADERS).to_excel(path, index=False)


def read_excel_with_headers(file_path, log=_noop_log):
    """Read an Excel file, with or without a header row. Returns df or None."""
    all_headers = REQUIRED_HEADERS + OPTIONAL_HEADERS
    log(f"Reading Excel file: {file_path}", level='info')

    try:
        first_row = pd.read_excel(file_path, header=None, nrows=1).iloc[0].tolist()
    except Exception as exc:
        log(f"Error reading the first row: {exc}", level='error')
        return None

    first_row_lower = [str(cell).strip().lower() for cell in first_row]
    has_required = set(h.lower() for h in REQUIRED_HEADERS).issubset(set(first_row_lower))

    if has_required:
        log("Required headers detected — reading with headers.", level='info')
        df = pd.read_excel(file_path, header=0)
        for col in OPTIONAL_HEADERS:
            if col not in df.columns:
                df[col] = np.nan
        df = df[[c for c in all_headers if c in df.columns]]
    else:
        log("Required headers not found — reading without headers.", level='warning')
        df = pd.read_excel(file_path, header=None)
        if df.shape[1] < len(REQUIRED_HEADERS):
            log(f"Excel file has fewer than {len(REQUIRED_HEADERS)} columns.", level='error')
            return None
        df = df.iloc[:, :len(REQUIRED_HEADERS)]
        df.columns = REQUIRED_HEADERS
        for col in OPTIONAL_HEADERS:
            df[col] = np.nan

    df = df.reindex(columns=all_headers, fill_value=np.nan).reset_index(drop=True)
    return df


def _norm(value):
    """Normalized form of a cell for duplicate keys ('' for blank/NaN)."""
    if value is None:
        return ''
    try:
        if pd.isna(value):
            return ''
    except (TypeError, ValueError):
        pass
    return str(value).strip().lower()


def _text(value):
    """Trimmed cell text ('' for blank/NaN)."""
    if value is None:
        return ''
    try:
        if pd.isna(value):
            return ''
    except (TypeError, ValueError):
        pass
    text = str(value).strip()
    return '' if text.lower() == 'nan' else text


def parse_tags(value):
    """Tag names from one separated cell, de-duplicated case-insensitively."""
    names, seen = [], set()
    for part in _text(value).split(TAG_SEPARATOR):
        name = part.strip()
        if name and name.lower() not in seen:
            seen.add(name.lower())
            names.append(name)
    return names


def brings_extras(row):
    """True when importing this row actually writes a definition or a tag.

    For a new entry that is whatever the file supplies; for an existing one only
    what the merge found missing, so a row whose definitions and tags are all
    already stored does not count.
    """
    if row['action'] == ACTION_SKIP:
        return False
    if row['action'] == ACTION_ADD:
        return bool(row.get('Definition') or row.get('Definition2') or row.get('Tags'))
    patch = row.get('patch') or {}
    return bool(row.get('new_tags') or patch.get('Definition') or patch.get('Definition2'))


def _join_notes(notes):
    """'a, b and c' — the merge fragments as one readable phrase."""
    if not notes:
        return ""
    if len(notes) == 1:
        return notes[0]
    return ", ".join(notes[:-1]) + " and " + notes[-1]


def _added_detail(definition, definition2, tags):
    """Review-table detail for a brand-new entry, naming the extras it brings."""
    notes = []
    if definition:
        notes.append("definition 1")
    if definition2:
        notes.append("definition 2")
    if tags:
        notes.append("tags: " + ", ".join(tags))
    return "New entry." if not notes else f"New entry with {_join_notes(notes)}."


def _existing_entry(cursor, db_id):
    """Words, languages, definitions and tag names a stored entry already carries."""
    cursor.execute("SELECT Word1, Word2, Language1, Language2, Definition, Definition2 "
                   "FROM words WHERE ID = ?", (db_id,))
    found = cursor.fetchone() or ('', '', None, None, '', '')
    cursor.execute("""
        SELECT tags.tag_name FROM tags
        JOIN word_tags ON tags.tag_id = word_tags.tag_id
        WHERE word_tags.word_id = ?
    """, (db_id,))
    return {'Word1': found[0], 'Word2': found[1],
            'Language1': found[2], 'Language2': found[3],
            'Definition': found[4] or '', 'Definition2': found[5] or '',
            'tags': [row[0] for row in cursor.fetchall()]}


def _stored_as(stored, word1, word2):
    """' as "house – Haus"' when the database spells the pair differently.

    Matching is case-insensitive, so an existing word is found however the
    spreadsheet capitalizes it — and keeps the spelling it already has.
    """
    if (stored['Word1'] or '') == word1 and (stored['Word2'] or '') == word2:
        return ""
    return f" as \"{stored['Word1']} – {stored['Word2']}\""


def _plan_merge(stored, definition, definition2, tags):
    """Work out what an existing word is missing. Returns (patch, new_tags, notes).

    Non-destructive by design: a definition is proposed only for a field the
    database left empty, and only tags the word does not already have are
    listed. *notes* are short human-readable fragments for the review table.
    """
    have_tags = stored['tags']
    patch, notes = {}, []
    for column, label, incoming, current in (
            ('Definition', "definition 1", definition, stored['Definition']),
            ('Definition2', "definition 2", definition2, stored['Definition2'])):
        if incoming and not str(current).strip():
            patch[column] = incoming
            notes.append(label)

    known = {str(tag).lower() for tag in have_tags}
    new_tags = [tag for tag in tags if tag.lower() not in known]
    if new_tags:
        notes.append("tags: " + ", ".join(new_tags))
    return patch, new_tags, notes


def analyze_excel_import(file_path, settings, log=_noop_log, db_path=None):
    """Classify every spreadsheet row for user review.

    Returns ``{'rows': [...], 'counts': {'add', 'update', 'skip', 'total'}}``
    where each row dict carries: ``row`` (1-based data row in the file),
    ``Word1/Word2/Language1/Language2``, ``Definition/Definition2``, ``Tags``
    (list), ``action`` (ACTION_*), ``reason``, ``detail`` (human-readable
    explanation), ``ID`` (existing DB id for updates/duplicates) and
    ``existing`` (current DB languages for updates). Update rows additionally
    carry ``patch`` (columns to write) and ``new_tags`` (tags to attach).
    Returns None when the file could not be read.
    """
    db_path = db_path or get_active_db_path()
    placeholders_str = settings.get("excel_import_placeholders", "(  ),'',N/A,---,None,null, ")
    placeholders = set(p.strip().lower() for p in placeholders_str.split(',')) if placeholders_str else set()
    skip_placeholders = str(settings.get("excel_import_skip_placeholders", "True")) == 'True'
    skip_empty = str(settings.get("excel_import_skip_empty", "True")) == 'True'
    normalize_df = str(settings.get("excel_import_normalize", "True")) == 'True'

    df = read_excel_with_headers(file_path, log)
    if df is None:
        return None
    log(f"Excel file read successfully: {len(df)} data rows.", level='success')

    if normalize_df:
        df = normalize_language_pairs(df)
        log("Language pairs normalized to a consistent order.")
    else:
        log("Data normalization skipped as per settings.")

    rows = []
    seen_pairs = {}  # normalized (lang1, word1, lang2, word2) -> first file row

    with sqlite3.connect(os.path.abspath(db_path)) as conn:
        cursor = conn.cursor()
        word_index = build_word_index(cursor)

        for index, raw in df.iterrows():
            file_row = index + 1
            word1, word2 = raw.get('Word1'), raw.get('Word2')
            lang1, lang2 = raw.get('Language1'), raw.get('Language2')
            definition, definition2 = _text(raw.get('Definition')), _text(raw.get('Definition2'))
            tags = parse_tags(raw.get('Tags'))
            entry = {'row': file_row, 'Language1': lang1, 'Word1': word1,
                     'Language2': lang2, 'Word2': word2,
                     'Definition': definition, 'Definition2': definition2,
                     'Tags': tags, 'patch': None, 'new_tags': [],
                     'ID': None, 'existing': None,
                     'lang1_ok': True, 'lang2_ok': True, 'lang_ok': True}

            def skip(reason, detail, db_id=None):
                entry.update(action=ACTION_SKIP, reason=reason, detail=detail, ID=db_id)
                rows.append(entry)
                log(f"Row {file_row}: skipped — {detail}", level='warning')

            if skip_placeholders and any(
                    str(w).strip().lower() in placeholders for w in [word1, word2, lang1, lang2]):
                skip('placeholder', "Contains placeholder values.")
                continue

            if skip_empty and (pd.isna(word1) or pd.isna(word2)
                               or not str(word1).strip() or not str(word2).strip()):
                skip('empty', "Word 1 or Word 2 is empty.")
                continue

            word1 = str(word1).strip() if not pd.isna(word1) else None
            word2 = str(word2).strip() if not pd.isna(word2) else None
            lang1 = str(lang1).strip() if isinstance(lang1, str) else lang1
            lang2 = str(lang2).strip() if isinstance(lang2, str) else lang2

            # Map languages written in English or any bundled locale (e.g.
            # Ukrainian) to the canonical English name used for storage, dedup
            # matching and TTS. Unrecognized non-blank values are flagged but
            # kept exactly as written.
            canon1, canon2 = canonical_language(lang1), canonical_language(lang2)
            entry['lang1_ok'] = bool(canon1) or not str(lang1 or '').strip()
            entry['lang2_ok'] = bool(canon2) or not str(lang2 or '').strip()
            entry['lang_ok'] = entry['lang1_ok'] and entry['lang2_ok']
            # Captured before any reversed-duplicate swap below so the message
            # always names the right values.
            entry['unknown_langs'] = [lng for lng, ok in
                                      ((lang1, entry['lang1_ok']),
                                       (lang2, entry['lang2_ok'])) if not ok]
            lang1 = canon1 or lang1
            lang2 = canon2 or lang2
            entry.update(Word1=word1, Word2=word2, Language1=lang1, Language2=lang2)

            if word1 is None and word2 is None:
                skip('invalid', "No usable words in the row.")
                continue

            def note_unknown_lang(detail):
                """Append the unrecognized-language warning to *detail* and log it."""
                if entry['lang_ok']:
                    return detail
                names = ', '.join(str(u) for u in entry['unknown_langs'])
                log(f"Row {file_row}: unrecognized language '{names}' — "
                    "imported as written.", level='warning')
                return f"{detail} ⚠ Unrecognized language — imported as written."

            key = (_norm(lang1), _norm(word1), _norm(lang2), _norm(word2))
            reversed_key = (key[2], key[3], key[0], key[1])
            first_row = seen_pairs.get(key, seen_pairs.get(reversed_key))
            if first_row is not None:
                skip('file_duplicate', f"Duplicate of row {first_row} in this file.")
                continue
            seen_pairs[key] = file_row

            duplicate_status, db_id = check_duplicate_entry(
                cursor, word1, word2, lang1, lang2, index=word_index)
            if duplicate_status is None:
                entry.update(action=ACTION_ADD, reason='new',
                             detail=note_unknown_lang(_added_detail(definition,
                                                                   definition2, tags)))
                rows.append(entry)
                log(f"Row {file_row}: \"{word1} – {word2}\" not found — proposed "
                    "for addition.", level='new')
                continue

            # The stored row may hold the pair the other way round; line the
            # file's values up with it before comparing or writing anything.
            if duplicate_status.startswith('reversed'):
                word1, word2 = word2, word1
                lang1, lang2 = lang2, lang1
                definition, definition2 = definition2, definition

            stored = _existing_entry(cursor, db_id)
            patch, new_tags, notes = _plan_merge(stored, definition, definition2, tags)
            lang_conflict = duplicate_status in ('needs_update', 'reversed_needs_update')
            # The stored spelling wins, so name it whenever the file differs.
            stored_as = _stored_as(stored, word1, word2)

            if not lang_conflict and not patch and not new_tags:
                reversed_note = " in reversed order" if duplicate_status == 'reversed_duplicate' else ""
                skip('db_duplicate',
                     f"Already in the database{reversed_note}{stored_as}; "
                     "nothing new to add.", db_id)
                continue

            existing = None
            if lang_conflict:
                existing = {'Language1': stored['Language1'], 'Language2': stored['Language2']}
                patch['Language1'], patch['Language2'] = lang1, lang2
                detail = (f"Already in the database{stored_as} with languages "
                          f"'{stored['Language1']} – {stored['Language2']}'; "
                          f"will become '{lang1} – {lang2}'.")
                if notes:
                    detail += " Also adds " + _join_notes(notes) + "."
                reason = 'language_conflict'
            else:
                detail = (f"Already in the database{stored_as}; "
                          f"will add {_join_notes(notes)}.")
                reason = 'merge'

            entry.update(
                action=ACTION_UPDATE, reason=reason,
                detail=note_unknown_lang(detail),
                ID=db_id, existing=existing, patch=patch, new_tags=new_tags,
                Word1=word1, Word2=word2, Language1=lang1, Language2=lang2,
                Definition=definition, Definition2=definition2)
            rows.append(entry)
            log(f"Row {file_row}: \"{word1} – {word2}\" exists — proposed for "
                f"update ({_join_notes(notes) if notes else 'languages'}).",
                level='new')

    counts = {'add': 0, 'update': 0, 'skip': 0, 'unknown_lang': 0,
              'extras': 0, 'total': len(rows)}
    for row in rows:
        counts[row['action']] += 1
        if not row.get('lang_ok', True):
            counts['unknown_lang'] += 1
        if brings_extras(row):
            counts['extras'] += 1
    log(f"Analysis complete: {counts['add']} to add, {counts['update']} to update, "
        f"{counts['skip']} skipped out of {counts['total']} rows.", level='success')
    return {'rows': rows, 'counts': counts}


def _apply_tags(db_adapter, tag_links, log=_noop_log):
    """Attach collected tags, one adapter call per distinct tag name.

    *tag_links* maps a tag name to the word ids that should carry it. A tag that
    fails to attach is logged but does not fail the word itself — the row is in
    the database by then, and re-running the import will offer the tag again.
    """
    for tag_name, word_ids in tag_links.items():
        try:
            tagged, tag_failed = db_adapter.add_tag_to_words(word_ids, tag_name)
        except Exception as exc:
            log(f"Could not apply the tag \"{tag_name}\": {exc}", level='error')
            continue
        if tag_failed:
            log(f"Tag \"{tag_name}\" could not be applied to "
                f"{len(tag_failed)} item(s).", level='warning')
        elif tagged:
            log(f"Tagged {tagged} item(s) with \"{tag_name}\".")


def _collect_tags(tag_links, word_id, tags):
    for tag_name in tags or []:
        if word_id:
            tag_links.setdefault(tag_name, []).append(word_id)


def apply_additions(db_adapter, items_to_add, log=_noop_log, progress=None):
    """Insert the given rows with their definitions and tags.

    Returns (added_count, failed_items).
    """
    added, failed = 0, []
    tag_links = {}
    for done, item in enumerate(items_to_add, start=1):
        word_data = {
            'Language1': item['Language1'], 'Language2': item['Language2'],
            'Word1': item['Word1'], 'Word2': item['Word2'],
            'Definition': item.get('Definition') or None,
            'Definition2': item.get('Definition2') or None,
            'Status': 'New', 'Source': 'excel_import',
        }
        try:
            result = db_adapter.insert_word(word_data)
            if not result:
                log(f"Row {item.get('row', '?')}: could not add "
                    f"\"{item['Word1']} – {item['Word2']}\".", level='error')
        except Exception as exc:
            result = None
            log(f"Row {item.get('row', '?')}: insert failed: {exc}", level='error')
        if result:
            added += 1
            _collect_tags(tag_links,
                          result.get('ID') if isinstance(result, dict) else item.get('ID'),
                          item.get('Tags'))
        else:
            failed.append(item)
        if progress:
            progress(done, len(items_to_add))
    _apply_tags(db_adapter, tag_links, log)
    log(f"Added {added} of {len(items_to_add)} new items.",
        level='success' if not failed else 'warning')
    return added, failed


def apply_updates(db_adapter, items_to_update, log=_noop_log, progress=None):
    """Apply the merge planned for existing rows: languages, definitions, tags.

    Each item carries the ``patch`` and ``new_tags`` worked out during analysis;
    an item without a patch (an older caller) falls back to the languages alone.
    Returns (updated_count, failed_items).
    """
    updated, failed = 0, []
    tag_links = {}
    for done, item in enumerate(items_to_update, start=1):
        patch = item.get('patch')
        if patch is None:
            patch = {'Language1': item['Language1'], 'Language2': item['Language2']}
        new_tags = item.get('new_tags') or []
        try:
            # A tags-only merge has nothing to write to the words table.
            ok = bool(db_adapter.update_word(item['ID'], patch)) if patch else True
            if not ok:
                log(f"Row {item.get('row', '?')}: could not update entry ID {item['ID']}.",
                    level='error')
        except Exception as exc:
            ok = False
            log(f"Row {item.get('row', '?')}: update failed: {exc}", level='error')
        if ok:
            updated += 1
            _collect_tags(tag_links, item['ID'], new_tags)
        else:
            failed.append(item)
        if progress:
            progress(done, len(items_to_update))
    _apply_tags(db_adapter, tag_links, log)
    log(f"Updated {updated} of {len(items_to_update)} items.",
        level='success' if not failed else 'warning')
    return updated, failed

# NOTE: this module used to reset the SQLite AUTOINCREMENT sequence after an
# import. That recycles the IDs of deleted rows, which corrupts cloud sync
# (deletion records and soft-deleted cloud rows are keyed by ID) — so it was
# removed deliberately. Do not reintroduce it while sync exists.
