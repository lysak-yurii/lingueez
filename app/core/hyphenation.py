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

"""Where long words may break with a hyphen, for the justified reading pane.

Qt has no automatic hyphenation, but its text layout honours U+00AD soft
hyphens: a line may break there, and the hyphen is only drawn when it does. The
reader inserts them at the break points found here (pyphen, which carries the
LibreOffice hyphenation dictionaries). Same limits as the web reader: only words
of MIN_WORD+ letters, at least MIN_SIDE letters on either side of a break, so
the short words a learner scans stay whole.

Soft hyphens are layout only. Anything that leaves the pane — a clicked word,
text sent to translation or speech, a save — goes through strip() first.
"""

import logging
import re
from functools import lru_cache

SOFT_HYPHEN = "­"

MIN_WORD = 8
MIN_SIDE = 3

_WORD = re.compile(r"[^\W\d_]{%d,}" % MIN_WORD)


@lru_cache(maxsize=None)
def _dictionary(code):
    try:
        import pyphen
    except ImportError:  # a build without it simply doesn't hyphenate
        logging.warning("pyphen is not installed; reader hyphenation is off")
        return None
    lang = pyphen.language_fallback(code.replace("-", "_"))
    return pyphen.Pyphen(lang=lang, left=MIN_SIDE, right=MIN_SIDE) if lang else None


def break_points(text, code):
    """Ascending offsets in *text* where a soft hyphen may go.

    *code* is a Google Translate language code (languages.TRANSLATION_CODES);
    a language without a dictionary gets no break points.
    """
    dictionary = _dictionary(code) if code else None
    if dictionary is None:
        return []
    return [match.start() + pos
            for match in _WORD.finditer(text)
            for pos in dictionary.positions(match.group())]


def hyphenate(text, code):
    """*text* with soft hyphens inserted at its break points."""
    parts, last = [], 0
    for pos in break_points(text, code):
        parts.append(text[last:pos])
        last = pos
    parts.append(text[last:])
    return SOFT_HYPHEN.join(parts)


def strip(text):
    return text.replace(SOFT_HYPHEN, "")
