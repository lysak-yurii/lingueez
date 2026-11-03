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
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Display-name rules shared by sign-up and renaming."""

import unicodedata
from typing import Optional

NAME_MIN = 2
NAME_MAX = 50
_SEPARATORS = " -'’."


def normalize_name(raw: Optional[str]) -> Optional[str]:
    """The cleaned-up display name, or None when it breaks the name rules.

    Letters of any script plus spaces, hyphens, apostrophes and periods; 2 to 50
    characters, starting with a letter and holding at least two. A name typed
    all in one case is capitalized word by word; any other casing is kept.
    """
    name = " ".join((raw or "").split())
    if not NAME_MIN <= len(name) <= NAME_MAX:
        return None
    letters = 0
    for ch in name:
        category = unicodedata.category(ch)
        if category.startswith("L"):
            letters += 1
        elif not (category.startswith("M") or ch in _SEPARATORS):
            return None
    if letters < 2 or not unicodedata.category(name[0]).startswith("L"):
        return None
    if name in (name.lower(), name.upper()):
        name = name.title()
    return name
