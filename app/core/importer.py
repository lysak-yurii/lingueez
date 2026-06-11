"""Excel import pipeline, GUI-free.

The analysis phase classifies every spreadsheet row into add/update/skip
(with a reason and human-readable detail); the apply phase inserts/updates
through the DatabaseAdapter so sync keeps working. The caller (UI) lets the
user review the classification and deselect rows between the two phases.
"""
import logging
import os
import sqlite3

import numpy as np
import pandas as pd

from app.core.data_management import check_duplicate_entry, normalize_language_pairs

logger = logging.getLogger(__name__)

REQUIRED_HEADERS = ["Language1", "Language2", "Word1", "Word2"]
OPTIONAL_HEADERS = ["Status", "ID"]

ACTION_ADD = 'add'
ACTION_UPDATE = 'update'
ACTION_SKIP = 'skip'

_PY_LEVELS = {'error': logging.ERROR, 'warning': logging.WARNING}


def _noop_log(message, level='info'):
    logger.log(_PY_LEVELS.get(level, logging.INFO), message)


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


def analyze_excel_import(file_path, settings, log=_noop_log, db_path='dictionary.db'):
    """Classify every spreadsheet row for user review.

    Returns ``{'rows': [...], 'counts': {'add', 'update', 'skip', 'total'}}``
    where each row dict carries: ``row`` (1-based data row in the file),
    ``Word1/Word2/Language1/Language2``, ``action`` (ACTION_*), ``reason``,
    ``detail`` (human-readable explanation), ``ID`` (existing DB id for
    updates/duplicates) and ``existing`` (current DB languages for updates).
    Returns None when the file could not be read.
    """
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

        for index, raw in df.iterrows():
            file_row = index + 1
            word1, word2 = raw.get('Word1'), raw.get('Word2')
            lang1, lang2 = raw.get('Language1'), raw.get('Language2')
            entry = {'row': file_row, 'Language1': lang1, 'Word1': word1,
                     'Language2': lang2, 'Word2': word2,
                     'ID': None, 'existing': None}

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
            entry.update(Word1=word1, Word2=word2, Language1=lang1, Language2=lang2)

            if word1 is None and word2 is None:
                skip('invalid', "No usable words in the row.")
                continue

            key = (_norm(lang1), _norm(word1), _norm(lang2), _norm(word2))
            reversed_key = (key[2], key[3], key[0], key[1])
            first_row = seen_pairs.get(key, seen_pairs.get(reversed_key))
            if first_row is not None:
                skip('file_duplicate', f"Duplicate of row {first_row} in this file.")
                continue
            seen_pairs[key] = file_row

            duplicate_status, db_id = check_duplicate_entry(cursor, word1, word2, lang1, lang2)
            if duplicate_status == 'exact_duplicate':
                skip('db_duplicate', f"Already in the database (ID {db_id}).", db_id)
            elif duplicate_status == 'reversed_duplicate':
                skip('db_duplicate', f"Already in the database in reversed order (ID {db_id}).", db_id)
            elif duplicate_status in ('needs_update', 'reversed_needs_update'):
                if duplicate_status == 'reversed_needs_update':
                    word1, word2 = word2, word1
                    lang1, lang2 = lang2, lang1
                cursor.execute("SELECT Language1, Language2 FROM words WHERE ID = ?", (db_id,))
                found = cursor.fetchone() or (None, None)
                existing = {'Language1': found[0], 'Language2': found[1]}
                entry.update(
                    action=ACTION_UPDATE, reason='language_conflict',
                    detail=f"Entry ID {db_id} exists with languages "
                           f"'{found[0]} – {found[1]}'; will become '{lang1} – {lang2}'.",
                    ID=db_id, existing=existing,
                    Word1=word1, Word2=word2, Language1=lang1, Language2=lang2)
                rows.append(entry)
                log(f"Row {file_row}: \"{word1} – {word2}\" exists with different "
                    "languages — proposed for update.", level='new')
            else:
                entry.update(action=ACTION_ADD, reason='new', detail="New entry.")
                rows.append(entry)
                log(f"Row {file_row}: \"{word1} – {word2}\" not found — proposed "
                    "for addition.", level='new')

    counts = {'add': 0, 'update': 0, 'skip': 0, 'total': len(rows)}
    for row in rows:
        counts[row['action']] += 1
    log(f"Analysis complete: {counts['add']} to add, {counts['update']} to update, "
        f"{counts['skip']} skipped out of {counts['total']} rows.", level='success')
    return {'rows': rows, 'counts': counts}


def apply_additions(db_adapter, items_to_add, log=_noop_log, progress=None):
    """Insert the given rows. Returns (added_count, failed_items)."""
    added, failed = 0, []
    for done, item in enumerate(items_to_add, start=1):
        word_data = {
            'Language1': item['Language1'], 'Language2': item['Language2'],
            'Word1': item['Word1'], 'Word2': item['Word2'],
            'Status': 'New', 'Source': 'excel_import',
        }
        try:
            ok = db_adapter.insert_word(word_data)
            if not ok:
                log(f"Row {item.get('row', '?')}: could not add "
                    f"\"{item['Word1']} – {item['Word2']}\".", level='error')
        except Exception as exc:
            ok = False
            log(f"Row {item.get('row', '?')}: insert failed: {exc}", level='error')
        if ok:
            added += 1
        else:
            failed.append(item)
        if progress:
            progress(done, len(items_to_add))
    log(f"Added {added} of {len(items_to_add)} new items.",
        level='success' if not failed else 'warning')
    return added, failed


def apply_updates(db_adapter, items_to_update, log=_noop_log, progress=None):
    """Update languages of existing rows. Returns (updated_count, failed_items)."""
    updated, failed = 0, []
    for done, item in enumerate(items_to_update, start=1):
        try:
            ok = db_adapter.update_word(item['ID'], {
                'Language1': item['Language1'], 'Language2': item['Language2']})
            if not ok:
                log(f"Row {item.get('row', '?')}: could not update entry ID {item['ID']}.",
                    level='error')
        except Exception as exc:
            ok = False
            log(f"Row {item.get('row', '?')}: update failed: {exc}", level='error')
        if ok:
            updated += 1
        else:
            failed.append(item)
        if progress:
            progress(done, len(items_to_update))
    log(f"Updated {updated} of {len(items_to_update)} items.",
        level='success' if not failed else 'warning')
    return updated, failed

# NOTE: this module used to reset the SQLite AUTOINCREMENT sequence after an
# import. That recycles the IDs of deleted rows, which corrupts cloud sync
# (deletion records and soft-deleted cloud rows are keyed by ID) — so it was
# removed deliberately. Do not reintroduce it while sync exists.
