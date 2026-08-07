# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Keeps the Windows installer's wizard languages in step with locales/.

The PyInstaller spec derives what it ships from locales/*.py, so app languages
and their Qt translations follow along by themselves. lingueez.iss cannot —
its [Languages] block is a hand-written list, so adding locales/<code>.py
without touching it silently leaves that language an English setup wizard.

Run with the project venv:  python -m unittest tests.test_installer_languages
"""

import os
import re
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Locales deliberately left without a wizard language, with the reason. Inno
# Setup has no Hindi translation, official or unofficial (checked against
# jrsoftware/issrc Files/Languages and .../Unofficial).
NO_WIZARD_TRANSLATION = {"hi": "Inno Setup ships no Hindi .isl"}


def _shipped_locales():
    path = os.path.join(REPO, "locales")
    return sorted(f[:-3] for f in os.listdir(path) if f.endswith(".py") and not f.startswith("__"))


def _wizard_languages():
    """(name, MessagesFile) for every [Languages] entry in lingueez.iss."""
    text = open(os.path.join(REPO, "lingueez.iss"), encoding="utf-8").read()
    section = text.split("[Languages]", 1)[1].split("\n[", 1)[0]
    return re.findall(r'Name:\s*"([^"]+)";\s*MessagesFile:\s*"([^"]+)"', section)


class InstallerLanguageTests(unittest.TestCase):
    def test_one_wizard_language_per_shipped_locale(self):
        # English has no locale module but is always the fallback wizard entry.
        expected = len(_shipped_locales()) - len(NO_WIZARD_TRANSLATION) + 1
        self.assertEqual(
            len(_wizard_languages()),
            expected,
            "lingueez.iss [Languages] is out of step with locales/ — add a "
            "wizard language for the new locale, or list it in "
            "NO_WIZARD_TRANSLATION with the reason.",
        )

    def test_english_fallback_is_declared(self):
        self.assertIn("compiler:Default.isl", [path for _name, path in _wizard_languages()])

    def test_names_are_unique(self):
        names = [name for name, _path in _wizard_languages()]
        self.assertEqual(sorted(names), sorted(set(names)))

    def test_vendored_message_files_exist(self):
        # compiler:* paths resolve inside the Inno install and can only be
        # checked at compile time; relative ones must be in the repo.
        for name, path in _wizard_languages():
            if path.startswith("compiler:"):
                continue
            with self.subTest(language=name):
                self.assertTrue(
                    os.path.isfile(os.path.join(REPO, path.replace("\\", os.sep))),
                    f"{name}: vendored message file missing: {path}",
                )

    def test_untranslatable_locales_are_still_shipped(self):
        # Guards the exception list against naming a locale that no longer exists.
        for code in NO_WIZARD_TRANSLATION:
            self.assertIn(code, _shipped_locales())


if __name__ == "__main__":
    unittest.main()
