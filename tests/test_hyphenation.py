# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Soft hyphens for the justified reader.

The reader indexes its document by character offset — for read-aloud, word
highlighting and click-to-translate — so the break points must be exact offsets,
never land inside the protected edges of a word, and vanish without a trace
when stripped.

Run with the project venv:  python -m unittest tests.test_hyphenation
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import hyphenation  # noqa: E402
from app.core.hyphenation import MIN_SIDE, MIN_WORD, SOFT_HYPHEN  # noqa: E402
from app.ui.reader import tokenize  # noqa: E402

GREEK = "Έτσι αισθάνθηκαν οι Έλληνες την διοργάνωση των Ολυμπιακών αγώνων το 1896."


class HyphenationTests(unittest.TestCase):
    def test_breaks_long_words(self):
        hyphenated = hyphenation.hyphenate(GREEK, "el")
        self.assertIn(f"διορ{SOFT_HYPHEN}γάνωση", hyphenated)

    def test_strip_restores_the_text(self):
        self.assertEqual(hyphenation.strip(hyphenation.hyphenate(GREEK, "el")), GREEK)

    def test_short_words_and_word_edges_stay_whole(self):
        for word in hyphenation.hyphenate(GREEK, "el").split():
            letters = hyphenation.strip(word.strip(".,"))
            parts = word.strip(".,").split(SOFT_HYPHEN)
            with self.subTest(word=letters):
                if len(letters) < MIN_WORD:
                    self.assertEqual(len(parts), 1)
                elif len(parts) > 1:
                    self.assertGreaterEqual(len(parts[0]), MIN_SIDE)
                    self.assertGreaterEqual(len(parts[-1]), MIN_SIDE)

    def test_language_without_a_dictionary_is_left_alone(self):
        self.assertEqual(
            hyphenation.hyphenate("日本語のテキストです", "ja"), "日本語のテキストです"
        )
        self.assertEqual(hyphenation.break_points(GREEK, None), [])

    def test_reader_keeps_a_hyphenated_word_whole(self):
        # Word timing and highlighting would split at the soft hyphen otherwise.
        text = hyphenation.hyphenate(GREEK, "el")
        words = [hyphenation.strip(text[a:b]) for chunk in tokenize(text) for a, b in chunk.words]
        self.assertIn("διοργάνωση", words)
        self.assertIn("Ολυμπιακών", words)


if __name__ == "__main__":
    unittest.main()
