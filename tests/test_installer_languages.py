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
ISS = os.path.join(REPO, "packaging", "inno", "lingueez.iss")
RELEASE_WORKFLOW = os.path.join(REPO, ".github", "workflows", "release.yml")

# Locales deliberately left without a wizard language, with the reason. Inno
# Setup has no Hindi translation, official or unofficial (checked against
# jrsoftware/issrc Files/Languages and .../Unofficial).
NO_WIZARD_TRANSLATION = {"hi": "Inno Setup ships no Hindi .isl"}

# The .isl files this Inno version ships in its own Languages\ folder, i.e. every
# name a `compiler:Languages\<Name>.isl` reference may use. Referencing anything
# else aborts ISCC ("Couldn't open include file"), which only surfaces on a
# Windows runner — so it is pinned here instead of discovered during a release.
#
# Taken from https://github.com/jrsoftware/issrc/tree/is-6_7_1/Files/Languages.
# Note it is *narrower* than the same folder on `main`: ChineseSimplified and
# ChineseTraditional were promoted out of Unofficial/ after 6.7.1, so they are
# vendored under languages/ instead. When INNO_VERSION is bumped, re-read that
# folder at the matching tag and update this set.
INNO_VERSION = "6.7.1"
OFFICIAL_LANGUAGES = {
    "Arabic",
    "Armenian",
    "BrazilianPortuguese",
    "Bulgarian",
    "Catalan",
    "Corsican",
    "Czech",
    "Danish",
    "Dutch",
    "Finnish",
    "French",
    "German",
    "Hebrew",
    "Hungarian",
    "Italian",
    "Japanese",
    "Korean",
    "Norwegian",
    "Polish",
    "Portuguese",
    "Russian",
    "Slovak",
    "Slovenian",
    "Spanish",
    "Swedish",
    "Tamil",
    "Thai",
    "Turkish",
    "Ukrainian",
}


def _shipped_locales():
    path = os.path.join(REPO, "locales")
    return sorted(f[:-3] for f in os.listdir(path) if f.endswith(".py") and not f.startswith("__"))


def _wizard_languages():
    """(name, MessagesFile) for every [Languages] entry in lingueez.iss."""
    text = open(ISS, encoding="utf-8").read()
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
        # checked at compile time; the vendored ones must be in the repo.
        # {#SourcePath} is Inno's preprocessor variable for the script's own
        # directory — MessagesFile ignores SourceDir, so the .iss anchors on it.
        for name, path in _wizard_languages():
            if path.startswith("compiler:"):
                continue
            with self.subTest(language=name):
                self.assertTrue(
                    path.startswith("{#SourcePath}"),
                    f"{name}: vendored message file must be {{#SourcePath}}-relative: {path}",
                )
                rel = path[len("{#SourcePath}") :].replace("\\", os.sep)
                self.assertTrue(
                    os.path.isfile(os.path.join(os.path.dirname(ISS), rel)),
                    f"{name}: vendored message file missing: {path}",
                )

    def test_compiler_languages_exist_in_the_pinned_inno(self):
        # The failure this guards produced a green local repo and a dead release
        # build: ISCC aborts on the first compiler:Languages\ file its own
        # installation does not have.
        for name, path in _wizard_languages():
            if not path.startswith("compiler:Languages"):
                continue
            with self.subTest(language=name):
                lang = os.path.splitext(path.split("\\")[-1])[0]
                self.assertIn(
                    lang,
                    OFFICIAL_LANGUAGES,
                    f"{lang}.isl does not ship with Inno Setup {INNO_VERSION} — "
                    "vendor it under packaging/inno/languages/ (from the "
                    f"is-{INNO_VERSION.replace('.', '_')} tag) and reference it "
                    "as {#SourcePath}languages\\<Name>.isl instead.",
                )

    def test_pinned_inno_version_matches_the_language_set(self):
        # OFFICIAL_LANGUAGES is only valid for one Inno release; if CI installs a
        # different one, the set above has to be re-read at the matching tag.
        with open(RELEASE_WORKFLOW, encoding="utf-8") as fh:
            text = fh.read()
        self.assertIn(
            f"innosetup --version={INNO_VERSION}",
            text,
            "release.yml pins a different Inno Setup version than the one "
            "OFFICIAL_LANGUAGES was read from — update INNO_VERSION and re-read "
            "Files/Languages at the matching is-<version> tag.",
        )

    def test_untranslatable_locales_are_still_shipped(self):
        # Guards the exception list against naming a locale that no longer exists.
        for code in NO_WIZARD_TRANSLATION:
            self.assertIn(code, _shipped_locales())


if __name__ == "__main__":
    unittest.main()
