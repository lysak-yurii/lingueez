# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for importing definitions and tags from a spreadsheet.

Run:  python -m unittest tests.test_import_extras
"""

import os
import sqlite3
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd  # noqa: E402

from app.core.data_management import normalize_language_pairs  # noqa: E402
from app.core.importer import (  # noqa: E402
    ACTION_ADD, ACTION_SKIP, ACTION_UPDATE, analyze_excel_import,
    apply_additions, apply_updates, brings_extras, parse_tags,
)

SETTINGS = {}


class FakeAdapter:
    """Records what the apply phase would write."""

    def __init__(self, insert_ids=None):
        self.inserted = []
        self.updated = []
        self.tag_calls = []
        self._insert_ids = list(insert_ids or [])

    def insert_word(self, word_data):
        self.inserted.append(word_data)
        word_id = self._insert_ids.pop(0) if self._insert_ids else f"id-{len(self.inserted)}"
        return dict(word_data, ID=word_id)

    def update_word(self, word_id, patch):
        self.updated.append((word_id, patch))
        return {"ID": word_id}

    def add_tag_to_words(self, word_ids, tag_name):
        self.tag_calls.append((tag_name, list(word_ids)))
        return len(word_ids), []


class ParseTagsTests(unittest.TestCase):
    def test_splits_trims_and_drops_blanks(self):
        self.assertEqual(parse_tags(" noun , food ,, "), ["noun", "food"])

    def test_deduplicates_case_insensitively_keeping_first_spelling(self):
        self.assertEqual(parse_tags("Noun, noun, NOUN"), ["Noun"])

    def test_blank_cells_give_no_tags(self):
        self.assertEqual(parse_tags(None), [])
        self.assertEqual(parse_tags(float("nan")), [])
        self.assertEqual(parse_tags(""), [])


class NormalizeKeepsDefinitionsWithWordsTests(unittest.TestCase):
    def test_definitions_travel_with_their_word(self):
        df = pd.DataFrame(
            [["German", "English", "Hund", "dog", "New", 1, "Haustier", "an animal"]],
            columns=["Language1", "Language2", "Word1", "Word2", "Status", "ID",
                     "Definition", "Definition2"])
        row = normalize_language_pairs(df).iloc[0]
        self.assertEqual(row["Word1"], "dog")
        self.assertEqual(row["Definition"], "an animal")
        self.assertEqual(row["Definition2"], "Haustier")


class AnalyzeExtrasTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db_path = os.path.join(self.tmp.name, "test.db")
        conn = sqlite3.connect(self.db_path)
        conn.executescript("""
            CREATE TABLE words (ID TEXT PRIMARY KEY, Word1 TEXT, Word2 TEXT,
                                Language1 TEXT, Language2 TEXT,
                                Definition TEXT, Definition2 TEXT);
            CREATE TABLE tags (tag_id TEXT PRIMARY KEY, tag_name TEXT UNIQUE NOT NULL);
            CREATE TABLE word_tags (word_id TEXT, tag_id TEXT,
                                    PRIMARY KEY (word_id, tag_id));
        """)
        conn.commit()
        conn.close()

    def _store(self, word_id, word1, word2, lang1="English", lang2="German",
               definition=None, definition2=None, tags=()):
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO words VALUES (?,?,?,?,?,?,?)",
                     (word_id, word1, word2, lang1, lang2, definition, definition2))
        for name in tags:
            conn.execute("INSERT OR IGNORE INTO tags VALUES (?,?)", (f"tag-{name}", name))
            conn.execute("INSERT INTO word_tags VALUES (?,?)", (word_id, f"tag-{name}"))
        conn.commit()
        conn.close()

    def _analyze(self, records, settings=None):
        path = os.path.join(self.tmp.name, "words.xlsx")
        pd.DataFrame(records, columns=["Language1", "Language2", "Word1", "Word2",
                                       "Definition", "Definition2", "Tags"]).to_excel(
            path, index=False)
        return analyze_excel_import(path, settings or SETTINGS,
                                    db_path=self.db_path)['rows']

    def _row(self, **overrides):
        record = {"Language1": "English", "Language2": "German", "Word1": "house",
                  "Word2": "Haus", "Definition": "", "Definition2": "", "Tags": ""}
        record.update(overrides)
        return record

    def test_new_entry_carries_definitions_and_tags(self):
        row = self._analyze([self._row(Definition="a building", Definition2="ein Gebäude",
                                       Tags="noun, home")])[0]
        self.assertEqual(row['action'], ACTION_ADD)
        self.assertEqual(row['Definition'], "a building")
        self.assertEqual(row['Definition2'], "ein Gebäude")
        self.assertEqual(row['Tags'], ["noun", "home"])
        self.assertTrue(brings_extras(row))

    def test_existing_word_gains_missing_definition_and_new_tags(self):
        self._store("w1", "house", "Haus", tags=["noun"])
        row = self._analyze([self._row(Definition="a building", Tags="noun, home")])[0]
        self.assertEqual(row['action'], ACTION_UPDATE)
        self.assertEqual(row['reason'], 'merge')
        self.assertEqual(row['ID'], "w1")
        self.assertEqual(row['patch'], {"Definition": "a building"})
        self.assertEqual(row['new_tags'], ["home"])

    def test_stored_definition_is_never_overwritten(self):
        self._store("w1", "house", "Haus", definition="already here")
        row = self._analyze([self._row(Definition="a building")])[0]
        self.assertEqual(row['action'], ACTION_SKIP)
        self.assertEqual(row['reason'], 'db_duplicate')

    def test_duplicate_with_nothing_new_is_still_skipped(self):
        self._store("w1", "house", "Haus", tags=["noun"])
        row = self._analyze([self._row(Tags="Noun")])[0]
        self.assertEqual(row['action'], ACTION_SKIP)
        self.assertFalse(brings_extras(row))

    def test_capitalized_file_row_updates_the_stored_word(self):
        self._store("w1", "house", "Haus")
        row = self._analyze([self._row(Word1="House", Word2="HAUS",
                                       Definition="a building", Tags="home")])[0]
        self.assertEqual(row['action'], ACTION_UPDATE)
        self.assertEqual(row['ID'], "w1")
        # The stored spelling wins and the review says so.
        self.assertNotIn('Word1', row['patch'])
        self.assertIn('as "house – Haus"', row['detail'])

    def test_capitalized_duplicate_with_nothing_new_is_skipped_not_added(self):
        self._store("w1", "house", "Haus", definition="a building")
        row = self._analyze([self._row(Word1="House", Definition="a building")])[0]
        self.assertEqual(row['action'], ACTION_SKIP)
        self.assertEqual(row['reason'], 'db_duplicate')
        self.assertIn('as "house – Haus"', row['detail'])

    def test_language_conflict_also_merges_extras(self):
        self._store("w1", "house", "Haus", lang2="French")
        row = self._analyze([self._row(Definition="a building", Tags="noun")])[0]
        self.assertEqual(row['action'], ACTION_UPDATE)
        self.assertEqual(row['reason'], 'language_conflict')
        self.assertEqual(row['patch'], {"Definition": "a building",
                                        "Language1": "English", "Language2": "German"})
        self.assertEqual(row['new_tags'], ["noun"])

    def test_reversed_match_lines_definitions_up_with_the_stored_row(self):
        # Stored as German→English; the file writes the pair the other way round.
        # Normalization is off so the row reaches the duplicate check reversed.
        self._store("w1", "Haus", "house", lang1="German", lang2="English")
        row = self._analyze(
            [self._row(Definition="a building", Definition2="ein Gebäude", Tags="home")],
            settings={"excel_import_normalize": "False"})[0]
        self.assertEqual(row['action'], ACTION_UPDATE)
        self.assertEqual(row['Word1'], "Haus")
        self.assertEqual(row['Language1'], "German")
        # Word1 is now the German word, so it takes the German definition.
        self.assertEqual(row['patch']['Definition'], "ein Gebäude")
        self.assertEqual(row['patch']['Definition2'], "a building")
        self.assertEqual(row['new_tags'], ["home"])


class ApplyExtrasTests(unittest.TestCase):
    def test_additions_write_definitions_and_group_tag_calls(self):
        adapter = FakeAdapter(insert_ids=["w1", "w2"])
        items = [
            {'row': 1, 'Language1': 'English', 'Language2': 'German', 'Word1': 'house',
             'Word2': 'Haus', 'Definition': 'a building', 'Definition2': '',
             'Tags': ['noun', 'home']},
            {'row': 2, 'Language1': 'English', 'Language2': 'German', 'Word1': 'dog',
             'Word2': 'Hund', 'Definition': '', 'Definition2': '', 'Tags': ['noun']},
        ]
        added, failed = apply_additions(adapter, items)
        self.assertEqual((added, failed), (2, []))
        self.assertEqual(adapter.inserted[0]['Definition'], 'a building')
        self.assertIsNone(adapter.inserted[1]['Definition'])
        self.assertEqual(dict(adapter.tag_calls), {'noun': ['w1', 'w2'], 'home': ['w1']})

    def test_tag_only_update_touches_no_word_columns(self):
        adapter = FakeAdapter()
        updated, failed = apply_updates(adapter, [
            {'row': 1, 'ID': 'w1', 'Language1': 'English', 'Language2': 'German',
             'patch': {}, 'new_tags': ['home']}])
        self.assertEqual((updated, failed), (1, []))
        self.assertEqual(adapter.updated, [])
        self.assertEqual(adapter.tag_calls, [('home', ['w1'])])

    def test_update_without_a_patch_still_writes_languages(self):
        adapter = FakeAdapter()
        apply_updates(adapter, [{'row': 1, 'ID': 'w1', 'Language1': 'English',
                                 'Language2': 'German'}])
        self.assertEqual(adapter.updated,
                         [('w1', {'Language1': 'English', 'Language2': 'German'})])


if __name__ == "__main__":
    unittest.main()
