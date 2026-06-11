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

    # Swap columns where Language1 > Language2
    for index, row in df.iterrows():
        if row['Language1'] > row['Language2']:
            df.at[index, 'Language1'], df.at[index, 'Language2'] = row['Language2'], row['Language1']
            df.at[index, 'Word1'], df.at[index, 'Word2'] = row['Word2'], row['Word1']

    return df


def check_duplicate_entry(cursor, word1, word2, lang1, lang2):
    """
    Check if an entry exists in the database in various forms.
    Returns:
        - 'exact_duplicate' if an exact match is found.
        - 'needs_update' if an entry with the same Word1 and Word2 but different languages exists.
        - 'reversed_duplicate' if a reversed match with matching languages is found.
        - 'reversed_needs_update' if a reversed match with different languages is found.
        - None if no duplicate is found.
    """
    # Check for exact duplicate
    cursor.execute("""
        SELECT ID FROM words 
        WHERE 
            (Word1 = ? OR (Word1 IS NULL AND ? IS NULL)) 
            AND 
            (Word2 = ? OR (Word2 IS NULL AND ? IS NULL)) 
            AND 
            (Language1 = ? OR (Language1 IS NULL AND ? IS NULL)) 
            AND 
            (Language2 = ? OR (Language2 IS NULL AND ? IS NULL))
    """, (word1, word1, word2, word2, lang1, lang1, lang2, lang2))
    exact_match = cursor.fetchone()
    if exact_match:
        return 'exact_duplicate', exact_match[0]

    # Check for same Word1 and Word2 but different languages
    cursor.execute("""
        SELECT ID FROM words 
        WHERE 
            (Word1 = ? OR (Word1 IS NULL AND ? IS NULL)) 
            AND 
            (Word2 = ? OR (Word2 IS NULL AND ? IS NULL))
            AND 
            (
                (Language1 != ? OR Language1 IS NULL OR ? IS NULL) 
                OR 
                (Language2 != ? OR Language2 IS NULL OR ? IS NULL)
            )
    """, (word1, word1, word2, word2, lang1, lang1, lang2, lang2))
    same_word_diff_lang = cursor.fetchone()
    if same_word_diff_lang:
        return 'needs_update', same_word_diff_lang[0]

    # Check for reversed duplicate
    cursor.execute("""
        SELECT ID FROM words 
        WHERE 
            (Word1 = ? OR (Word1 IS NULL AND ? IS NULL)) 
            AND 
            (Word2 = ? OR (Word2 IS NULL AND ? IS NULL)) 
            AND 
            (Language1 = ? OR (Language1 IS NULL AND ? IS NULL)) 
            AND 
            (Language2 = ? OR (Language2 IS NULL AND ? IS NULL))
    """, (word2, word2, word1, word1, lang2, lang2, lang1, lang1))
    reversed_exact_match = cursor.fetchone()
    if reversed_exact_match:
        return 'reversed_duplicate', reversed_exact_match[0]

    # Check for reversed pair with different languages
    cursor.execute("""
        SELECT ID FROM words 
        WHERE 
            (Word1 = ? OR (Word1 IS NULL AND ? IS NULL)) 
            AND 
            (Word2 = ? OR (Word2 IS NULL AND ? IS NULL))
            AND 
            (
                (Language1 != ? OR Language1 IS NULL OR ? IS NULL) 
                OR 
                (Language2 != ? OR Language2 IS NULL OR ? IS NULL)
            )
    """, (word2, word2, word1, word1, lang2, lang2, lang1, lang1))
    reversed_diff_lang = cursor.fetchone()
    if reversed_diff_lang:
        return 'reversed_needs_update', reversed_diff_lang[0]

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
