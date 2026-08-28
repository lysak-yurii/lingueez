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

"""Playback-driven learning progression (pure, Qt-free, testable).

Passive listening promotes a word along a familiarity ladder, but only after
*many* completed listens — audio-only exposure is weak, so the thresholds are
deliberately high. Each rung's listen-count is configured independently:

    New ──(reviewing_at)──▶ Reviewing ──(learning_at)──▶ Learning ──(mastered_at)──▶ Mastered

Defaults are 3 / 15 / 100. Promotion never demotes, and never touches words
the user owns the meaning of (``Mastered``, ``Ignored``, or any status outside
the ladder).
"""
from __future__ import annotations

# Increasing familiarity. Matches the app's canonical status order.
LADDER = ["New", "Reviewing", "Learning", "Mastered"]
_RANK = {name: i for i, name in enumerate(LADDER)}

# Every status the app offers, in canonical order. This is the single source of
# truth: the status picker, the stats donut ordering and the color ramp all read
# it, so a word can never be promoted into a state the UI refuses to offer back.
ALL_STATUSES = ["New", "To Learn", "Reviewing", "Learning", "Mastered", "Ignored"]

# The rung a word is parked on to stop being asked about it. Off the ladder on
# purpose: nothing promotes onto it and nothing promotes off it. Writes use this
# exact string; reads go through ``is_ignored``, because the phone and the web
# app do not agree with us on casing.
IGNORED_STATUS = "Ignored"

# The rung a word is parked on when the user says they have forgotten it. Off
# the ladder like ``IGNORED_STATUS`` but with the opposite intent: it pulls a
# word back into study rather than out of it. Writes use this exact string;
# reads go through ``is_to_learn``, for the same reason ``is_ignored`` exists.
TO_LEARN_STATUS = "To Learn"


def rank(status):
    """Zero-based position on the ladder, or ``None`` for anything off it.

    Non-strings are off the ladder: a blank status arrives as NaN once it has
    been through a DataFrame, and NaN is truthy, so an ``or ""`` guard alone
    would hand ``.strip()`` a float — see ``is_ignored``.
    """
    if not isinstance(status, str):
        return None
    return _RANK.get(status.strip().title())


def is_ignored(status) -> bool:
    """Whether ``status`` is the ignored rung, however another client cased it.

    Anything that is not a string — ``None``, or the NaN a blank status becomes
    once it has been through a DataFrame — is not ignored.
    """
    if not isinstance(status, str):
        return False
    return status.strip().lower() == "ignored"


def is_to_learn(status) -> bool:
    """Whether ``status`` is the relearn rung, however another client cased it."""
    if not isinstance(status, str):
        return False
    return status.strip().lower() == "to learn"


# The lowest rung the relearn flag is offered on. Below it the flag has nothing
# to do: a Reviewing word is already in short-interval rotation, its ease is
# already under the gate ``srs.lapse`` pulls down to, and for one that is
# due today the reset is a no-op — leaving a button that only relabels.
LAPSABLE_FROM = "Learning"


def can_lapse(status) -> bool:
    """Whether "I have forgotten this" is a meaningful thing to say about a word.

    Only from ``LAPSABLE_FROM`` up: those words have an interval worth pulling
    back and a rung worth re-earning. New and Reviewing have neither, and
    anything off the ladder (To Learn, Ignored, custom) is not a candidate.
    Setting the status by hand stays available for the rest.
    """
    r = rank(status)
    return r is not None and r >= _RANK[LAPSABLE_FROM]


def is_studiable(status) -> bool:
    """Whether a word with ``status`` may appear in a practice session.

    Shared by the deck builder, the quiz's distractor pool and the read-aloud
    playlist, so all three agree on what "your words" means.
    """
    return not is_ignored(status)


DEFAULT_REVIEWING_LISTENS = 3
DEFAULT_LEARNING_LISTENS = 15
DEFAULT_MASTERED_LISTENS = 100

# Statuses that listening may promote *from*. Anything else (Mastered,
# Ignored, "To Learn", custom values) is left untouched.
_PROMOTABLE = {"", "new", "reviewing", "learning"}


def normalize_thresholds(reviewing=DEFAULT_REVIEWING_LISTENS,
                         learning=DEFAULT_LEARNING_LISTENS,
                         mastered=DEFAULT_MASTERED_LISTENS) -> dict:
    """Per-rung cumulative listen counts, clamped strictly increasing so the
    ladder is always well-formed regardless of the saved values."""
    r = max(1, int(reviewing))
    l = max(r + 1, int(learning))
    m = max(l + 1, int(mastered))
    return {"Reviewing": r, "Learning": l, "Mastered": m}


def level_for_count(n: int, thresholds) -> str:
    """The highest ladder status whose threshold is met by ``n`` listens."""
    th = thresholds if isinstance(thresholds, dict) else normalize_thresholds(*thresholds)
    if n >= th["Mastered"]:
        return "Mastered"
    if n >= th["Learning"]:
        return "Learning"
    if n >= th["Reviewing"]:
        return "Reviewing"
    return "New"


def next_status(current, n: int, thresholds):
    """Return the status ``current`` should be promoted to after ``n`` total
    completed listens, or ``None`` if it should stay unchanged.

    Never demotes; only acts on promotable statuses (empty / New / Reviewing /
    Learning). ``thresholds`` is a dict from :func:`normalize_thresholds` (or a
    ``(reviewing, learning, mastered)`` tuple).
    """
    key = (current or "").strip().lower()
    if key not in _PROMOTABLE:
        return None
    current_rank = 0 if key == "" else _RANK.get((current or "New").strip(), 0)
    target = level_for_count(n, thresholds)
    if _RANK[target] > current_rank:
        return target
    return None
