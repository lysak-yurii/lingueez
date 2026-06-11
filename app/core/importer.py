"""Excel import pipeline, GUI-free.

The analysis phase classifies every spreadsheet row; the apply phase
inserts/updates through the DatabaseAdapter so sync keeps working. The
caller (UI) shows confirmation dialogs between the two phases.
"""
import logging
import os
import sqlite3

import numpy as np
import pandas as pd

from app.core.data_management import check_duplicate_entry, normalize_language_pairs

REQUIRED_HEADERS = ["Language1", "Language2", "Word1", "Word2"]
OPTIONAL_HEADERS = ["Status", "ID"]


def _noop_log(message, level='info'):
    logging.log(logging.INFO, message)


def read_excel_with_headers(file_path, log=_noop_log):
    """Read an Excel file, with or without a header row. Returns df or None."""
    all_headers = REQUIRED_HEADERS + OPTIONAL_HEADERS
    log(f"Attempting to read Excel file: {file_path}", level='info')

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


def analyze_excel_import(file_path, settings, log=_noop_log, db_path='dictionary.db'):
    """Classify rows into additions/updates/skips.

    Returns dict with keys: items_to_add, items_to_update,
    skipped_placeholders, skipped_empty, skipped_invalid, skipped_duplicates.
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
    log("Excel file read successfully.", level='success')

    if normalize_df:
        df = normalize_language_pairs(df)
        log("Data normalized.")
    else:
        log("Data normalization skipped as per settings.")

    result = {
        'items_to_add': [], 'items_to_update': [],
        'skipped_placeholders': [], 'skipped_empty': [],
        'skipped_invalid': [], 'skipped_duplicates': [],
    }

    with sqlite3.connect(os.path.abspath(db_path)) as conn:
        cursor = conn.cursor()

        for index, row in df.iterrows():
            word1, word2 = row.get('Word1'), row.get('Word2')
            lang1, lang2 = row.get('Language1'), row.get('Language2')
            entry = {'Row': index + 1, 'Language1': lang1, 'Word1': word1,
                     'Language2': lang2, 'Word2': word2}

            if skip_placeholders and any(
                    str(w).strip().lower() in placeholders for w in [word1, word2, lang1, lang2]):
                log(f"Skipping row {index + 1}: contains placeholder values.", level='warning')
                result['skipped_placeholders'].append(entry)
                continue

            if skip_empty and (pd.isna(word1) or pd.isna(word2)
                               or not str(word1).strip() or not str(word2).strip()):
                log(f"Skipping row {index + 1}: empty Word1 or Word2.", level='warning')
                result['skipped_empty'].append(entry)
                continue

            word1 = str(word1).strip() if not pd.isna(word1) else None
            word2 = str(word2).strip() if not pd.isna(word2) else None
            lang1 = str(lang1).strip() if isinstance(lang1, str) else lang1
            lang2 = str(lang2).strip() if isinstance(lang2, str) else lang2

            log(f'Processing row {index + 1}: {lang1}: "{word1}"  -  {lang2}: "{word2}"', level='info')

            if word1 is None and word2 is None:
                result['skipped_invalid'].append(entry)
                continue

            duplicate_status, db_id = check_duplicate_entry(cursor, word1, word2, lang1, lang2)
            if duplicate_status in ('exact_duplicate', 'reversed_duplicate'):
                log(f"Row {index + 1}: duplicate '{word1} - {word2}' exists. Skipping.", level='warning')
                result['skipped_duplicates'].append(entry)
            elif duplicate_status == 'needs_update':
                log(f"Row {index + 1}: languages differ — marked for update.", level='new')
                result['items_to_update'].append({
                    'Row': index + 1, 'ID': db_id, 'Word1': word1, 'Word2': word2,
                    'Language1': lang1, 'Language2': lang2,
                })
            elif duplicate_status == 'reversed_needs_update':
                log(f"Row {index + 1}: reversed entry, languages differ — marked for update.", level='new')
                result['items_to_update'].append({
                    'Row': index + 1, 'ID': db_id, 'Word1': word2, 'Word2': word1,
                    'Language1': lang2, 'Language2': lang1,
                })
            else:
                log("Item not found. Marking for addition.", level='new')
                result['items_to_add'].append({
                    'Word1': word1, 'Word2': word2, 'Language1': lang1, 'Language2': lang2,
                })

    return result


def apply_additions(db_adapter, items_to_add, log=_noop_log):
    added = 0
    for item in items_to_add:
        word_data = {
            'Language1': item['Language1'], 'Language2': item['Language2'],
            'Word1': item['Word1'], 'Word2': item['Word2'],
            'Status': 'New', 'Source': 'excel_import',
        }
        if db_adapter.insert_word(word_data):
            added += 1
    log(f"Added {added} new items.", level='success')
    return added


def apply_updates(db_adapter, items_to_update, log=_noop_log):
    updated = 0
    for item in items_to_update:
        if db_adapter.update_word(item['ID'], {
                'Language1': item['Language1'], 'Language2': item['Language2']}):
            updated += 1
    log(f"Updated {updated} items.", level='success')
    return updated


def reset_sqlite_sequence(db_path='dictionary.db'):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(ID) FROM words")
        max_id = cursor.fetchone()[0] or 0
        cursor.execute("UPDATE SQLITE_SEQUENCE SET seq = ? WHERE name = 'words'", (max_id,))
        conn.commit()
