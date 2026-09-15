# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Definition generation: prompt rendering, legacy-prompt migration, column
mapping and the batch loop.

Run with the project venv:  python -m unittest tests.test_definition_prompt
"""

import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import config  # noqa: E402
from app.core import ai  # noqa: E402

RECORD = {"ID": "w1", "Word1": "Bank", "Word2": "bench",
          "Language1": "German", "Language2": "English"}


class PromptTests(unittest.TestCase):
    def render(self, **overrides):
        kwargs = dict(word="Bank", word_language="German", language="German",
                      translation="bench", translation_language="English")
        kwargs.update(overrides)
        return ai.build_definition_prompt(config.DEFINITION_PROMPT, **kwargs)

    def test_same_language_stays_monolingual(self):
        prompt = self.render()
        self.assertIn("solely in German", prompt)
        self.assertNotIn("in parentheses", prompt)
        self.assertNotIn("'Translations'", prompt)

    def test_cross_language_lists_translations_per_sense(self):
        prompt = self.render(language="English")
        self.assertIn("'Definition', 'Translations', 'Example Sentences' and 'Synonyms'", prompt)
        self.assertIn("possible English translations as one list item per sense", prompt)
        self.assertIn("synonyms in German", prompt)

    def test_saved_translation_leads_without_narrowing(self):
        prompt = self.render()
        self.assertIn('translation "bench": start with that sense', prompt)
        self.assertIn("other common senses", prompt)

    def test_no_sense_hint_without_translation(self):
        self.assertNotIn("saved it with", self.render(translation=""))

    def test_legacy_template_still_renders(self):
        prompt = ai.build_definition_prompt(
            config._LEGACY_DEFINITION_PROMPTS[0], "Haus", "German", "English", "house", "English")
        self.assertIn("Define the word: Haus in English", prompt)

    def test_broken_template_raises_ai_error(self):
        with self.assertRaises(ai.AIError):
            ai.build_definition_prompt("{nope}", "Haus", "German", "German")


class RequestTests(unittest.TestCase):
    def test_column_follows_the_written_language(self):
        self.assertEqual(ai.definition_column("Language1"), "Definition")
        self.assertEqual(ai.definition_column("Language2"), "Definition2")

    def test_word1_explained_in_language2(self):
        request = ai.definition_request(RECORD, "Word1", "Language2")
        self.assertEqual(request, {"word": "Bank", "word_language": "German",
                                   "language": "English", "translation": "bench",
                                   "translation_language": "English"})

    def test_word2_uses_word1_as_its_translation(self):
        request = ai.definition_request(RECORD, "Word2", "Language2")
        self.assertEqual((request["word"], request["word_language"], request["translation"]),
                         ("bench", "English", "Bank"))


class OrientationTests(unittest.TestCase):
    STORED = {"Word1": "ξετυλίγω", "Word2": "розгортати", "Language1": "Greek",
              "Language2": "Ukrainian", "Definition": "el", "Definition2": "uk"}

    def test_detects_a_flipped_record(self):
        shown = ai.oriented(self.STORED, True)
        self.assertEqual((shown["Word1"], shown["Language1"], shown["Definition"]),
                         ("розгортати", "Ukrainian", "uk"))
        self.assertTrue(ai.is_mirrored(self.STORED, shown))
        self.assertFalse(ai.is_mirrored(self.STORED, dict(self.STORED)))

    def test_same_language_pair_is_never_mirrored(self):
        row = dict(self.STORED, Language2="Greek")
        self.assertFalse(ai.is_mirrored(row, ai.oriented(row, True)))

    def test_stored_column_flips_back(self):
        self.assertEqual(ai.stored_column("Definition", True), "Definition2")
        self.assertEqual(ai.stored_column("Definition2", True), "Definition")
        self.assertEqual(ai.stored_column("Definition", False), "Definition")


class MigrationTests(unittest.TestCase):
    def load(self, content):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "settings.cfg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(f"chatgpt_content={content}\n")
            return config.load_settings(path)

    def test_old_defaults_are_upgraded(self):
        for legacy in config._LEGACY_DEFINITION_PROMPTS:
            settings = self.load(legacy)
            self.assertEqual(settings["chatgpt_content"], config.DEFINITION_PROMPT)

    def test_custom_prompt_is_kept(self):
        settings = self.load("Define {word} briefly in {language1}.")
        self.assertEqual(settings["chatgpt_content"], "Define {word} briefly in {language1}.")


class _FakeAdapter:
    def __init__(self, rows):
        self.rows = rows
        self.updates = []

    def get_word(self, word_id):
        return self.rows.get(word_id)

    def update_word(self, word_id, patch):
        self.updates.append((word_id, patch))


class BatchTests(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.object(ai, "backup_database")
        patcher.start()
        self.addCleanup(patcher.stop)

    def rows(self):
        return {
            "a": dict(RECORD, ID="a", Definition2=""),
            "b": dict(RECORD, ID="b", Definition2="already there"),
            "c": dict(RECORD, ID="c", Definition2=None),
        }

    def records(self, *ids):
        rows = self.rows()
        return [rows[i] for i in ids]

    def test_filtered_table_rows_are_read_as_shown(self):
        # The language filter shows the stored row with its sides flipped.
        stored = {"ID": "g", "Word1": "ξετυλίγω", "Word2": "розгортати", "Language1": "Greek",
                  "Language2": "Ukrainian", "Definition": "", "Definition2": ""}
        shown = ai.oriented(stored, True)
        adapter = _FakeAdapter({"g": stored})
        with mock.patch.object(ai, "get_definition", return_value="new") as get:
            ai.generate_definitions([shown], "Word2", "Language1", db_adapter=adapter)
        self.assertEqual(get.call_args.kwargs["word"], "ξετυλίγω")
        self.assertEqual(get.call_args.kwargs["language"], "Ukrainian")
        # written in Ukrainian → stored Language2 side
        self.assertEqual(adapter.updates, [("g", {"Definition2": "new"})])

    def test_skips_existing_and_writes_the_rest(self):
        adapter = _FakeAdapter(self.rows())
        with mock.patch.object(ai, "get_definition", return_value="new") as get:
            stats = ai.generate_definitions(self.records("a", "b", "c"), "Word1", "Language2",
                                            db_adapter=adapter)
        self.assertEqual((stats["generated"], stats["skipped"], stats["failed"]), (2, 1, 0))
        self.assertEqual(adapter.updates, [("a", {"Definition2": "new"}),
                                           ("c", {"Definition2": "new"})])
        self.assertEqual(get.call_count, 2)

    def test_overwrites_when_not_skipping(self):
        adapter = _FakeAdapter(self.rows())
        with mock.patch.object(ai, "get_definition", return_value="new"):
            stats = ai.generate_definitions(self.records("b"), "Word1", "Language2",
                                            skip_existing=False, db_adapter=adapter)
        self.assertEqual(stats["generated"], 1)

    def test_stops_when_the_same_error_repeats(self):
        adapter = _FakeAdapter(self.rows())
        error = ai.AIError("quota exhausted")
        with mock.patch.object(ai, "get_definition", side_effect=error) as get:
            stats = ai.generate_definitions(self.records("a", "c", "a"), "Word1", "Language2",
                                            skip_existing=False, db_adapter=adapter)
        self.assertEqual(get.call_count, 2)
        self.assertEqual(stats["error"], "quota exhausted")
        self.assertEqual(adapter.updates, [])

    def test_cancel_stops_before_the_next_word(self):
        adapter = _FakeAdapter(self.rows())
        with mock.patch.object(ai, "get_definition", return_value="new"):
            stats = ai.generate_definitions(
                self.records("a", "c"), "Word1", "Language2", db_adapter=adapter,
                is_cancelled=lambda: bool(adapter.updates))
        self.assertTrue(stats["cancelled"])
        self.assertEqual(stats["generated"], 1)


if __name__ == "__main__":
    unittest.main()
