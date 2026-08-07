# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Keeps the MSIX package's declared languages in step with locales/.

The <Resources> block in AppxManifest.xml is what the Microsoft Store lists as
the product's supported languages, and CI derives makepri's /dq qualifier list
from it. Neither follows locales/ by itself, so a new locales/<code>.py would
otherwise ship a package that claims one language fewer than the app speaks.

Run with the project venv:  python -m unittest tests.test_msix_languages
"""

import os
import re
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(REPO, "packaging", "msix", "AppxManifest.xml")
WORKFLOWS = [
    os.path.join(REPO, ".github", "workflows", "release.yml"),
    os.path.join(REPO, ".github", "workflows", "test-build.yml"),
]

# Locale code -> BCP-47 tag to declare, where the two differ. Everything else
# is declared under its bare code, which matches every region of that language
# through the normal Windows fallback chain.
#   pt_BR   Python module names can't hold a hyphen.
#   sr      locales/sr.py is Cyrillic ("Српски"), not Latin.
#   zh      locales/zh.py is Simplified ("简体中文"), not Traditional.
#   uk      kept at the region tag the package was first published with.
TAG_OVERRIDES = {"pt_BR": "pt-BR", "sr": "sr-Cyrl", "zh": "zh-Hans", "uk": "uk-UA"}

# English ships no locale module — the source strings are English — but it is
# the package's default language and must be declared first.
DEFAULT_TAG = "en-US"


def _shipped_locales():
    path = os.path.join(REPO, "locales")
    return sorted(f[:-3] for f in os.listdir(path) if f.endswith(".py") and not f.startswith("__"))


def _declared_tags():
    """Language tags from the manifest's <Resources> block, in document order."""
    with open(MANIFEST, encoding="utf-8") as fh:
        text = fh.read()
    section = text.split("<Resources>", 1)[1].split("</Resources>", 1)[0]
    return re.findall(r'<Resource\s+Language="([^"]+)"', section)


class MsixLanguageTests(unittest.TestCase):
    def test_one_declared_language_per_shipped_locale(self):
        expected = {DEFAULT_TAG} | {TAG_OVERRIDES.get(code, code) for code in _shipped_locales()}
        self.assertEqual(
            set(_declared_tags()),
            expected,
            "packaging/msix/AppxManifest.xml <Resources> is out of step with "
            'locales/ — add a <Resource Language="…"/> for the new locale '
            "(and a TAG_OVERRIDES entry if its BCP-47 tag differs from the code).",
        )

    def test_default_language_is_declared_first(self):
        # makepri takes the leading /dq qualifier as the default, and CI builds
        # that list from this block in order.
        self.assertEqual(_declared_tags()[0], DEFAULT_TAG)

    def test_tags_are_unique(self):
        tags = _declared_tags()
        self.assertEqual(sorted(tags), sorted(set(tags)))

    def test_overrides_name_shipped_locales(self):
        # Guards the override table against naming a locale that no longer exists.
        for code in TAG_OVERRIDES:
            self.assertIn(code, _shipped_locales())

    def test_workflows_derive_the_qualifier_list(self):
        # A hardcoded /dq would silently drift from the manifest again.
        for path in WORKFLOWS:
            with self.subTest(workflow=os.path.basename(path)):
                with open(path, encoding="utf-8") as fh:
                    text = fh.read()
                self.assertIn("/dq $env:MSIX_DQ", text)
                self.assertIn("MSIX_DQ=$DQ", text)


if __name__ == "__main__":
    unittest.main()
