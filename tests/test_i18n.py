# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for i18n language resolution, pluralization, and locale integrity.

Run:  python -m unittest tests.test_i18n
"""

import importlib
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import i18n  # noqa: E402


class CanonicalLanguageTests(unittest.TestCase):
    def test_english_name_maps_to_itself(self):
        self.assertEqual(i18n.canonical_language("German"), "German")

    def test_case_and_whitespace_insensitive(self):
        self.assertEqual(i18n.canonical_language("  german "), "German")
        self.assertEqual(i18n.canonical_language("GERMAN"), "German")

    def test_localized_native_name_resolves_to_canonical(self):
        # The Ukrainian word for German must resolve back to the English key
        # the DB stores, even when the UI is in English.
        self.assertEqual(i18n.canonical_language("Німецька"), "German")
        self.assertEqual(i18n.canonical_language("Українська"), "Ukrainian")

    def test_unknown_returns_none(self):
        self.assertIsNone(i18n.canonical_language("Klingon"))
        self.assertIsNone(i18n.canonical_language(""))
        self.assertIsNone(i18n.canonical_language(None))


class NtrPluralTests(unittest.TestCase):
    def setUp(self):
        self._orig = i18n._lang
        self.addCleanup(lambda: i18n.set_language(self._orig))

    def test_english_uses_one_and_few(self):
        i18n.set_language("en")
        self.assertEqual(i18n.ntr(1, "word", "words"), "word")
        self.assertEqual(i18n.ntr(0, "word", "words"), "words")
        self.assertEqual(i18n.ntr(5, "word", "words"), "words")

    def test_ukrainian_three_forms(self):
        i18n.set_language("uk")
        one, few, many = "слово", "слова", "слів"
        # one: 1, 21, 31 …
        self.assertEqual(i18n.ntr(1, one, few, many), one)
        self.assertEqual(i18n.ntr(21, one, few, many), one)
        # few: 2-4, 22-24 …
        self.assertEqual(i18n.ntr(2, one, few, many), few)
        self.assertEqual(i18n.ntr(23, one, few, many), few)
        # many: 0, 5-20, 11-14 …
        self.assertEqual(i18n.ntr(0, one, few, many), many)
        self.assertEqual(i18n.ntr(5, one, few, many), many)
        self.assertEqual(i18n.ntr(11, one, few, many), many)
        self.assertEqual(i18n.ntr(13, one, few, many), many)


class UkLocaleIntegrityTests(unittest.TestCase):
    """Guards against an inconsistent shipped Ukrainian locale."""

    @classmethod
    def setUpClass(cls):
        cls.uk = importlib.import_module("locales.uk")

    def test_declares_native_name(self):
        self.assertTrue(getattr(self.uk, "LANGUAGE_NAME", "").strip())

    def test_translations_is_a_str_str_mapping(self):
        self.assertIsInstance(self.uk.TRANSLATIONS, dict)
        self.assertGreater(len(self.uk.TRANSLATIONS), 0)
        for k, v in self.uk.TRANSLATIONS.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, str)

    def test_no_empty_values(self):
        empties = [k for k, v in self.uk.TRANSLATIONS.items() if not v.strip()]
        self.assertEqual(empties, [], f"empty translations for keys: {empties}")

    def test_listed_as_a_selectable_language(self):
        codes = [code for code, _ in i18n.available_languages()]
        self.assertIn("en", codes)
        self.assertIn("uk", codes)


# Placeholders the UI feeds through str.format() / %-formatting, and inline
# markup Qt renders as rich text. Both must survive translation intact: a
# dropped "{n}" silently prints the wrong message, a dropped "</a>" breaks the
# link. uk.py is the reference — it covers every key the UI looks up.
_PLACEHOLDER = re.compile(r"\{[a-zA-Z_][a-zA-Z_0-9]*\}|\{\}|%[sdif]")
_MARKUP = re.compile(r"</?[a-zA-Z][^>]*>")

_DATE_TABLES = {"MONTHS": 12, "MONTHS_ABBR": 12, "WEEKDAYS": 7, "WEEKDAYS_ABBR": 7}


class ShippedLocaleIntegrityTests(unittest.TestCase):
    """Every shipped locale must match the reference locale's contract.

    Machine-translated locale files fail in ways that stay invisible until the
    relevant screen opens: a key drifts and the string falls back to English, a
    "{count}" is absorbed into the translated text, the date tables are cut
    short and weekday names come out English. This checks all of it at once.
    """

    @classmethod
    def setUpClass(cls):
        cls.reference = importlib.import_module("locales.uk").TRANSLATIONS
        cls.codes = [code for code, _ in i18n.available_languages() if code != "en"]

    def test_at_least_the_reference_locale_ships(self):
        self.assertIn("uk", self.codes)

    def test_declares_a_native_language_name(self):
        for code in self.codes:
            with self.subTest(locale=code):
                mod = importlib.import_module(f"locales.{code}")
                self.assertTrue(getattr(mod, "LANGUAGE_NAME", "").strip())

    def test_translations_is_a_non_empty_str_str_mapping(self):
        for code in self.codes:
            with self.subTest(locale=code):
                table = importlib.import_module(f"locales.{code}").TRANSLATIONS
                self.assertIsInstance(table, dict)
                self.assertGreater(len(table), 0)
                for key, value in table.items():
                    self.assertIsInstance(key, str)
                    self.assertIsInstance(value, str)
                    self.assertTrue(value.strip(), f"empty translation for {key!r}")

    def test_key_set_matches_the_reference_locale(self):
        for code in self.codes:
            with self.subTest(locale=code):
                keys = set(importlib.import_module(f"locales.{code}").TRANSLATIONS)
                missing = sorted(set(self.reference) - keys)
                unknown = sorted(keys - set(self.reference))
                self.assertEqual(missing, [], f"{code}: untranslated source strings")
                self.assertEqual(unknown, [], f"{code}: keys no source string matches")

    def test_placeholders_and_markup_survive_translation(self):
        for code in self.codes:
            table = importlib.import_module(f"locales.{code}").TRANSLATIONS
            for source, translated in table.items():
                for label, pattern in (("placeholder", _PLACEHOLDER), ("markup", _MARKUP)):
                    expected, actual = sorted(pattern.findall(source)), sorted(
                        pattern.findall(translated))
                    if expected != actual:
                        with self.subTest(locale=code, kind=label, source=source[:60]):
                            self.fail(f"{code}: {label} {expected} became {actual} "
                                      f"in {translated[:80]!r}")

    def test_date_tables_are_complete(self):
        for code in self.codes:
            mod = importlib.import_module(f"locales.{code}")
            for name, length in _DATE_TABLES.items():
                with self.subTest(locale=code, table=name):
                    # A missing table silently falls back to English names.
                    table = getattr(mod, name, None)
                    self.assertIsNotNone(table, f"{code} does not define {name}")
                    self.assertEqual(len(table), length)
                    self.assertTrue(all(str(x).strip() for x in table))


if __name__ == "__main__":
    unittest.main()
