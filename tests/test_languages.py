# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Integrity of the per-service language code maps.

These maps used to be derived from one another, which capped Google Translate
at DeepL's language list and left 44 of the 106 offered languages with a gTTS
code that cannot actually be synthesized. The checks here keep the three maps
independent but consistent, and catch drift in the one authority that ships
locally — gTTS's own supported-language list.

Run with the project venv:  python -m unittest tests.test_languages
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import languages  # noqa: E402


class VocabularyTests(unittest.TestCase):
    def test_translation_is_the_widest_map(self):
        # Everything speakable or DeepL-routable must be a language the app
        # knows how to translate, or it could never be reached from the UI.
        for name in languages.SPEECH_CODES:
            with self.subTest(language=name):
                self.assertIn(name, languages.TRANSLATION_CODES)
        for name in languages.DEEPL_CODES:
            with self.subTest(language=name):
                self.assertIn(name, languages.TRANSLATION_CODES)

    def test_no_empty_names_or_codes(self):
        for label, table in (
            ("translation", languages.TRANSLATION_CODES),
            ("speech", languages.SPEECH_CODES),
            ("deepl", languages.DEEPL_CODES),
        ):
            for name, code in table.items():
                with self.subTest(map=label, language=name):
                    self.assertTrue(name.strip())
                    self.assertTrue(str(code).strip())

    def test_maps_are_not_derived_from_each_other(self):
        # The regression that started this: GOOGLE == {k: v.lower() for DeepL}.
        derived = {n: c.lower() for n, c in languages.DEEPL_CODES.items()}
        self.assertNotEqual(languages.TRANSLATION_CODES, derived)
        self.assertNotEqual(languages.SPEECH_CODES, languages.TRANSLATION_CODES)


class SpeechCodeTests(unittest.TestCase):
    """gTTS ships its supported-language list locally, so this needs no network."""

    @classmethod
    def setUpClass(cls):
        from gtts.lang import tts_langs

        cls.supported = tts_langs()

    def test_every_speech_code_is_one_gtts_supports(self):
        for name, code in languages.SPEECH_CODES.items():
            with self.subTest(language=name, code=code):
                self.assertIn(code, self.supported)

    def test_known_divergences_use_the_gtts_spelling(self):
        # Same vendor, different code — the bugs this split exists to prevent.
        for name, speech_code, translation_code in (
            ("Hebrew", "iw", "he"),
            ("Filipino", "tl", "fil"),
            ("Javanese", "jw", "jv"),
            ("Cantonese", "yue", "zh-HK"),
        ):
            with self.subTest(language=name):
                self.assertEqual(languages.SPEECH_CODES[name], speech_code)
                self.assertEqual(languages.TRANSLATION_CODES[name], translation_code)

    def test_translatable_but_silent_languages_are_absent_not_broken(self):
        # Better to have no entry than an entry gTTS will reject at play time.
        for name in ("Slovenian", "Persian", "Georgian", "Macedonian"):
            with self.subTest(language=name):
                self.assertIn(name, languages.TRANSLATION_CODES)
                self.assertNotIn(name, languages.SPEECH_CODES)
                self.assertFalse(languages.can_speak(name))


class AliasTests(unittest.TestCase):
    def test_legacy_chinese_resolves_to_mandarin(self):
        self.assertEqual(languages.canonical("Chinese"), "Mandarin")
        self.assertTrue(languages.is_known("Chinese"))
        # It had no TTS entry at all before, so those words never spoke.
        self.assertTrue(languages.can_speak("Chinese"))

    def test_aliases_point_at_real_languages(self):
        for old, new in languages.ALIASES.items():
            with self.subTest(alias=old):
                self.assertIn(new, languages.TRANSLATION_CODES)
                self.assertNotIn(old, languages.TRANSLATION_CODES)

    def test_canonical_leaves_ordinary_names_alone(self):
        for name in ("German", "Ukrainian", "Detect language", "", "Nonsense"):
            self.assertEqual(languages.canonical(name), name)


class RoutingTests(unittest.TestCase):
    """translate() picks a provider without a network call being needed."""

    def test_deepl_covers_the_languages_users_actually_asked_for(self):
        for name in ("Turkish", "Korean", "Arabic", "Hebrew", "Indonesian", "Vietnamese", "Thai"):
            with self.subTest(language=name):
                self.assertIn(name, languages.DEEPL_CODES)

    def test_deepl_is_a_strict_subset(self):
        self.assertLess(len(languages.DEEPL_CODES), len(languages.TRANSLATION_CODES))

    def test_unknown_target_is_rejected(self):
        from app.core.translator import TranslationError, translate

        with self.assertRaises(TranslationError):
            translate("book", "Klingon")


if __name__ == "__main__":
    unittest.main()
