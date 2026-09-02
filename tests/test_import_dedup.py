# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for Excel-import dedup logic (normalization + duplicate matching).

Run:  python -m unittest tests.test_import_dedup
"""

import os
import sqlite3
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd  # noqa: E402

from app.core.data_management import (  # noqa: E402
    build_word_index,
    check_duplicate_entry,
    normalize_language_pairs,
)


class NormalizeLanguagePairsTests(unittest.TestCase):
    def _df(self, rows):
        cols = ["Language1", "Language2", "Word1", "Word2", "Status", "ID"]
        return pd.DataFrame(rows, columns=cols)

    def test_swaps_so_language1_is_not_greater_than_language2(self):
        df = self._df([["German", "English", "Hund", "dog", "New", 1]])
        out = normalize_language_pairs(df)
        row = out.iloc[0]
        self.assertEqual(row["Language1"], "English")
        self.assertEqual(row["Language2"], "German")
        # words travel with their language.
        self.assertEqual(row["Word1"], "dog")
        self.assertEqual(row["Word2"], "Hund")

    def test_already_ordered_pair_is_untouched(self):
        df = self._df([["English", "German", "dog", "Hund", "New", 1]])
        out = normalize_language_pairs(df)
        row = out.iloc[0]
        self.assertEqual(row["Word1"], "dog")
        self.assertEqual(row["Word2"], "Hund")

    def test_missing_columns_raise_value_error(self):
        df = pd.DataFrame([["English", "dog"]], columns=["Language1", "Word1"])
        with self.assertRaises(ValueError):
            normalize_language_pairs(df)


class CheckDuplicateEntryTests(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute(
            "CREATE TABLE words (ID INTEGER PRIMARY KEY, Word1 TEXT, Word2 TEXT, "
            "Language1 TEXT, Language2 TEXT)"
        )
        self.conn.executemany(
            "INSERT INTO words (ID, Word1, Word2, Language1, Language2) VALUES (?,?,?,?,?)",
            [
                (1, "cat", "Katze", "English", "German"),
                (2, "Hund", "dog", "German", "English"),
                (3, "слово", "word", "Ukrainian", "English"),
            ],
        )
        self.cur = self.conn.cursor()
        self.addCleanup(self.conn.close)

    def test_exact_duplicate(self):
        kind, rid = check_duplicate_entry(self.cur, "cat", "Katze", "English", "German")
        self.assertEqual(kind, "exact_duplicate")
        self.assertEqual(rid, 1)

    def test_same_words_different_language_needs_update(self):
        kind, rid = check_duplicate_entry(self.cur, "cat", "Katze", "English", "French")
        self.assertEqual(kind, "needs_update")
        self.assertEqual(rid, 1)

    def test_reversed_duplicate(self):
        kind, rid = check_duplicate_entry(self.cur, "dog", "Hund", "English", "German")
        self.assertEqual(kind, "reversed_duplicate")
        self.assertEqual(rid, 2)

    def test_reversed_needs_update(self):
        kind, rid = check_duplicate_entry(self.cur, "dog", "Hund", "English", "French")
        self.assertEqual(kind, "reversed_needs_update")
        self.assertEqual(rid, 2)

    def test_no_match_returns_none(self):
        kind, rid = check_duplicate_entry(self.cur, "xyz", "abc", "English", "German")
        self.assertIsNone(kind)
        self.assertIsNone(rid)

    def test_capitalized_words_find_the_stored_lowercase_entry(self):
        kind, rid = check_duplicate_entry(self.cur, "Cat", "KATZE", "English", "German")
        self.assertEqual(kind, "exact_duplicate")
        self.assertEqual(rid, 1)

    def test_case_folding_covers_non_ascii_alphabets(self):
        # SQLite's own NOCASE collation folds ASCII only, so this is the case
        # that a COLLATE NOCASE fix would silently miss.
        kind, rid = check_duplicate_entry(self.cur, "Слово", "Word", "Ukrainian", "English")
        self.assertEqual(kind, "exact_duplicate")
        self.assertEqual(rid, 3)

    def test_surrounding_whitespace_is_ignored(self):
        kind, rid = check_duplicate_entry(self.cur, " cat ", "Katze", "English", "German")
        self.assertEqual(kind, "exact_duplicate")
        self.assertEqual(rid, 1)

    def test_language_case_does_not_split_an_entry(self):
        kind, rid = check_duplicate_entry(self.cur, "cat", "Katze", "english", "GERMAN")
        self.assertEqual(kind, "exact_duplicate")
        self.assertEqual(rid, 1)

    def test_capitalized_words_still_report_a_language_conflict(self):
        kind, rid = check_duplicate_entry(self.cur, "Cat", "Katze", "English", "French")
        self.assertEqual(kind, "needs_update")
        self.assertEqual(rid, 1)

    def test_capitalized_reversed_pair_matches(self):
        kind, rid = check_duplicate_entry(self.cur, "Dog", "HUND", "English", "German")
        self.assertEqual(kind, "reversed_duplicate")
        self.assertEqual(rid, 2)

    def test_a_prebuilt_index_gives_the_same_answers(self):
        index = build_word_index(self.cur)
        self.assertEqual(
            check_duplicate_entry(self.cur, "Cat", "Katze", "English", "German", index=index),
            ("exact_duplicate", 1))
        self.assertEqual(
            check_duplicate_entry(self.cur, "xyz", "abc", "English", "German", index=index),
            (None, None))


if __name__ == "__main__":
    unittest.main()
