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

import logging
import pandas as pd
import numpy as np


def normalize_language_pairs(df):
    """
    Normalize language pairs in the dataframe to ensure consistency.
    Swaps Language1 and Language2 if Language1 > Language2 to maintain a consistent ordering.
    """
    expected_columns = {'Language1', 'Language2', 'Word1', 'Word2', 'Status', 'ID'}
    if not expected_columns.issubset(df.columns):
        raise ValueError(f"Excel file must contain columns: {', '.join(expected_columns)}")

    # Convert columns to string
    df['Language1'] = df['Language1'].astype(str)
    df['Language2'] = df['Language2'].astype(str)
    df['Status'] = df['Status'].astype(str)

    # Definitions belong to their word, so they travel with the swap.
    paired = [('Word1', 'Word2')]
    if {'Definition', 'Definition2'}.issubset(df.columns):
        paired.append(('Definition', 'Definition2'))

    # Swap columns where Language1 > Language2
    for index, row in df.iterrows():
        if row['Language1'] > row['Language2']:
            df.at[index, 'Language1'], df.at[index, 'Language2'] = row['Language2'], row['Language1']
            for first, second in paired:
                df.at[index, first], df.at[index, second] = row[second], row[first]

    return df


def fold(value):
    """Comparison form of a word or language: trimmed and lowercased.

    Python's ``str.lower`` folds every alphabet the app supports; SQLite's own
    NOCASE collation and LOWER() only fold ASCII, which would leave Cyrillic,
    Greek and accented Latin words matching case-sensitively.
    """
    return None if value is None else str(value).strip().lower()


def build_word_index(cursor):
    """Every stored word keyed by its folded pair, for duplicate matching.

    ``{(folded Word1, folded Word2): [(ID, Language1, Language2), …]}``. Built
    once per import; matching each row with four SQL queries instead costs a
    full table scan per spreadsheet row.
    """
    index = {}
    cursor.execute("SELECT ID, Word1, Word2, Language1, Language2 FROM words")
    for row_id, word1, word2, language1, language2 in cursor.fetchall():
        index.setdefault((fold(word1), fold(word2)), []).append(
            (row_id, language1, language2))
    return index


def _languages_match(stored, incoming):
    """True when both language slots agree; a missing language matches only NULL."""
    return all(
        (left is None and right is None) or
        (left is not None and right is not None and fold(left) == fold(right))
        for left, right in zip(stored, incoming, strict=True))


def _match_id(rows, languages, same_languages):
    """First row id whose languages match (or differ from) *languages*."""
    for row_id, stored1, stored2 in rows:
        if _languages_match((stored1, stored2), languages) == same_languages:
            return row_id
    return None


def check_duplicate_entry(cursor, word1, word2, lang1, lang2, index=None):
    """
    Check if an entry exists in the database in various forms.

    Words and languages are compared folded (trimmed, lowercased), so a
    spreadsheet's "House" finds a stored "house" instead of adding a second
    entry for it.

    Pass *index* from :func:`build_word_index` to reuse one scan across a whole
    import; without it the index is rebuilt on every call.

    Returns:
        - 'exact_duplicate' if an exact match is found.
        - 'needs_update' if an entry with the same Word1 and Word2 but different languages exists.
        - 'reversed_duplicate' if a reversed match with matching languages is found.
        - 'reversed_needs_update' if a reversed match with different languages is found.
        - None if no duplicate is found.
    """
    if index is None:
        index = build_word_index(cursor)

    forward = index.get((fold(word1), fold(word2)), ())
    backward = index.get((fold(word2), fold(word1)), ())

    for rows, languages, matched, differing in (
            (forward, (lang1, lang2), 'exact_duplicate', 'needs_update'),
            (backward, (lang2, lang1), 'reversed_duplicate', 'reversed_needs_update')):
        for kind, same in ((matched, True), (differing, False)):
            row_id = _match_id(rows, languages, same)
            if row_id is not None:
                return kind, row_id

    return None, None


def open_words_from_excel(file_path):
    """
    Import words from an Excel file, ensuring all expected columns are present even if some are entirely empty,
    and add headers above the existing data if they are missing.
    """
    # Read the Excel file without headers to inspect the first row
    if file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path, header=None, engine='openpyxl')
    elif file_path.endswith('.xls'):
        df = pd.read_excel(file_path, header=None, engine='xlrd')
    else:
        logging.error("Unsupported file format. Please provide an .xls or .xlsx file.")
        raise ValueError("Unsupported file format. Please provide an .xls or .xlsx file.")

    # Define the expected header
    expected_header = ["Language1", "Language2", "Word1", "Word2", "Status", "ID", "Source", "created_at",
                       "edited_at", "favorite"]

    # Check if the first row matches the expected headers
    if not set(df.iloc[0]).issuperset(set(expected_header)):
        # Headers are missing, prepend the expected headers
        df.columns = expected_header[:df.shape[1]]  # Set headers for the columns present
        additional_cols = len(expected_header) - df.shape[1]
        if additional_cols > 0:
            # Add missing columns if any
            for col in expected_header[-additional_cols:]:
                df[col] = np.nan
    else:
        # Set the first row as the header if it matches expected headers
        df.columns = expected_header
        df = df[1:]  # Drop the header row

    # Ensure all expected columns are present
    df = df.reindex(columns=expected_header, fill_value=np.nan)  # Reorder and fill missing columns

    df = normalize_language_pairs(df)
    return df
