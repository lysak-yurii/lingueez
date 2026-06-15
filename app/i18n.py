# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Additional terms under AGPL-3.0 section 7 apply to this program; see the
# NOTICE file distributed with this source for details.
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Lightweight i18n: tr() lookup + ntr() plural selector.

set_language() is called once at startup (before any UI import) from main.py.
All UI files import tr() and wrap string literals with it.
"""

_lang = "en"
_translations: dict = {}


def set_language(lang: str) -> None:
    global _lang, _translations
    _lang = lang
    if lang == "en":
        _translations = {}
        return
    try:
        import importlib
        mod = importlib.import_module(f"locales.{lang}")
        _translations = mod.TRANSLATIONS
    except Exception:
        _translations = {}


def tr(text: str) -> str:
    """Return the translation of *text* for the current language, or *text* itself."""
    return _translations.get(text, text)


def ntr(count: int, one: str, few: str, many: str = None) -> str:
    """Return the right plural form for *count*.

    For English: one (count==1) or few/many otherwise.
    For Ukrainian: uses modular arithmetic — Ukrainian has three plural forms:
      - one  → 1, 21, 31, 41, …  (mod10==1 and mod100 not in 11-14)
      - few  → 2-4, 22-24, …     (mod10 in 2-4 and mod100 not in 11-14)
      - many → everything else (0, 5-20, 11-14, 25-30, …)
    """
    if _lang != "uk":
        return one if count == 1 else (many or few)
    mod100 = count % 100
    if 11 <= mod100 <= 14:
        return many or few
    mod10 = count % 10
    if mod10 == 1:
        return one
    if 2 <= mod10 <= 4:
        return few
    return many or few
