# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""LANGUAGES.md and the README summaries must match the code.

Documented language support is the kind of thing that silently rots: a locale
gets added, a service drops a voice, and the published list keeps promising the
old set. Everything here is derived from app.core.languages and locales/, so
these checks fail the moment the docs stop telling the truth.

Regenerate with:  python tools/gen_languages_md.py

Run with the project venv:  python -m unittest tests.test_languages_doc
"""

import os
import re
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

# Translated READMEs live here, one README.<code>.md per language; the English
# original stays at the repo root where GitHub renders it by default.
TRANSLATIONS = os.path.join("docs", "i18n")

from app.core.languages import SPEECH_CODES, TRANSLATION_CODES  # noqa: E402
from tools.gen_languages_md import interface_languages, render  # noqa: E402


class GeneratedDocTests(unittest.TestCase):
    def test_languages_md_is_up_to_date(self):
        with open(os.path.join(REPO, "LANGUAGES.md"), encoding="utf-8") as fh:
            on_disk = fh.read()
        self.assertEqual(
            on_disk, render(), "LANGUAGES.md is stale — run: python tools/gen_languages_md.py"
        )

    def test_every_translatable_language_has_a_row(self):
        with open(os.path.join(REPO, "LANGUAGES.md"), encoding="utf-8") as fh:
            text = fh.read()
        for name in TRANSLATION_CODES:
            with self.subTest(language=name):
                self.assertRegex(text, re.compile(rf"^\| {re.escape(name)} +\|", re.M))

    def test_speech_column_matches_the_speech_map(self):
        rows = {}
        with open(os.path.join(REPO, "LANGUAGES.md"), encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r"^\| (.+?) +\| +(.) +\| +(.) +\| +(.) +\|$", line)
                if m and m.group(1) != "Language":
                    rows[m.group(1)] = m.group(4)
        self.assertTrue(rows, "no table rows parsed out of LANGUAGES.md")
        for name, mark in rows.items():
            with self.subTest(language=name):
                self.assertEqual(mark == "✓", name in SPEECH_CODES)


class ReadmeSummaryTests(unittest.TestCase):
    """The counts quoted in both READMEs, which are written by hand."""

    @classmethod
    def setUpClass(cls):
        cls.expected = (
            sum(len(v) for v in interface_languages().values()) + 1,
            len(TRANSLATION_CODES),
            len(SPEECH_CODES),
        )

    def _numbers_in(self, filename):
        with open(os.path.join(REPO, filename), encoding="utf-8") as fh:
            text = fh.read()
        line = next((block for block in text.split("\n- ") if "LANGUAGES.md" in block), None)
        self.assertIsNotNone(line, f"{filename} does not link to LANGUAGES.md")
        return tuple(int(n) for n in re.findall(r"\b(\d+)\b", line))

    def test_english_readme_counts_match(self):
        self.assertEqual(self._numbers_in("README.md"), self.expected)

    def test_translated_readme_counts_match(self):
        # Discovered rather than listed, so a new docs/i18n/README.<code>.md is
        # guarded the moment it lands — no edit here required.
        names = sorted(
            f
            for f in os.listdir(os.path.join(REPO, TRANSLATIONS))
            if f.startswith("README.") and f.endswith(".md")
        )
        self.assertTrue(names, f"no translated READMEs found in {TRANSLATIONS}")
        for name in names:
            with self.subTest(readme=name):
                self.assertEqual(self._numbers_in(os.path.join(TRANSLATIONS, name)), self.expected)


if __name__ == "__main__":
    unittest.main()
