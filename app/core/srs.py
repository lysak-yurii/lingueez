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

"""SM-2 spaced repetition for flashcard grading (pure, Qt-free, testable).

The algorithm intentionally matches the companion web app's server-side
implementation, so a word graded on either client schedules the same way:

    Easy (difficulty 1, correct)  → interval × ease × 1.5, ease +0.15
    Good (difficulty 3, correct)  → interval × ease,       ease +0.10
    Hard (difficulty 5, incorrect)→ interval = 1,          ease −0.20

Ease is clamped to [1.3, 2.5] (it never grows past its starting value —
a web-app quirk kept for parity) and intervals cap at ten years. Scheduling
state lives only in the local ``srs_progress`` table; the resulting Status
promotion goes through the normal synced update path, reusing the same
never-demote semantics as the listening ladder in :mod:`progression`.
"""
from __future__ import annotations

from datetime import datetime, timedelta

from app.core import progression

GRADES = ("easy", "good", "hard")
_GRADE_DIFFICULTY = {"easy": 1, "good": 3, "hard": 5}
_GRADE_CORRECT = {"easy": True, "good": True, "hard": False}

INITIAL_EASE = 2.5
MAX_EASE = 2.5
MIN_EASE = 1.3
MAX_INTERVAL_DAYS = 3650

# The ease a lapse pulls a word down *to* — just under the 2.0 gate in
# ``status_from_progress``, so it maps to Reviewing whatever its counters say.
# A ceiling rather than a fixed drop, because a lapse can follow a Hard grade
# that has already taken 0.2 off: subtracting again would punish one click
# twice. A word already below it is only rescheduled, not pushed lower.
LAPSE_EASE = 1.9


def apply_grade(card, grade: str, now: datetime | None = None) -> dict:
    """Return the next scheduling state after grading a card.

    ``card`` is the current ``srs_progress`` row as a dict (or ``None`` /
    ``review_count == 0`` for a word never graded before). Returns the full
    replacement row: ``{ease_factor, interval_days, next_review (ISO string),
    review_count, correct_count}``.
    """
    if grade not in _GRADE_DIFFICULTY:
        raise ValueError(f"unknown grade: {grade!r}")
    now = now or datetime.now()
    difficulty = _GRADE_DIFFICULTY[grade]
    correct = _GRADE_CORRECT[grade]

    if not card or int(card.get("review_count") or 0) == 0:
        interval = 1
        ease = INITIAL_EASE
        review_count = 1
        correct_count = 1 if correct else 0
    else:
        ease = float(card.get("ease_factor") or INITIAL_EASE)
        interval = int(card.get("interval_days") or 1)
        review_count = int(card["review_count"]) + 1
        correct_count = int(card.get("correct_count") or 0)
        if correct:
            correct_count += 1
            if difficulty <= 2:
                interval = int(interval * ease * 1.5)
                ease = min(ease + 0.15, MAX_EASE)
            else:
                interval = int(interval * ease)
                ease = min(ease + 0.1, MAX_EASE)
        else:
            interval = 1
            ease = max(ease - 0.2, MIN_EASE)

    interval = max(1, min(interval, MAX_INTERVAL_DAYS))
    return {
        "ease_factor": round(ease, 4),
        "interval_days": interval,
        "next_review": (now + timedelta(days=interval)).isoformat(timespec="seconds"),
        "review_count": review_count,
        "correct_count": correct_count,
    }


def lapse(card, now: datetime | None = None) -> dict:
    """Return the scheduling state for a word the user says they have forgotten.

    Due immediately, interval back to one day, and ease dropped below the
    Learning gate so the word has to climb ``status_from_progress`` again
    instead of snapping back to Mastered on its next correct grade.

    The counters are deliberately left untouched. ``review_count`` and
    ``correct_count`` are monotonic across devices — :func:`db.merge_progress_rows`
    merges them by ``max`` — so zeroing them here would be undone by the next
    sync pull. The scheduling fields travel as one group from the side with the
    newer ``updated_at``, which is why the lapse has to work through ease.
    """
    now = now or datetime.now()
    ease = float((card or {}).get("ease_factor") or INITIAL_EASE)
    return {
        "ease_factor": round(max(min(ease, LAPSE_EASE), MIN_EASE), 4),
        "interval_days": 1,
        "next_review": now.isoformat(timespec="seconds"),
        "review_count": int((card or {}).get("review_count") or 0),
        "correct_count": int((card or {}).get("correct_count") or 0),
    }


def lapses_on_grade(status, grade: str) -> bool:
    """Whether ``grade`` on a word at ``status`` means "I have forgotten this".

    Only a Hard grade on the top rung. That is the one case where the SM-2
    mapping and the label disagree in a way worth acting on — the mapping keeps
    saying Mastered because ``correct_count`` never falls, while the user has
    just said the opposite. Lower rungs are left alone: the interval reset the
    grade itself applied is already the right answer there.
    """
    return (grade == "hard"
            and progression.rank(status) == len(progression.LADDER) - 1)


def seconds_until_due(next_review, now: datetime | None = None) -> float | None:
    """Seconds from ``now`` until a ``next_review`` stamp, or None if unusable.

    The stamp comes in two shapes: naive local time, written by
    :func:`apply_grade` here, and UTC with an offset, written by the web and
    mobile apps and pulled in by sync. Callers must not subtract one from the
    other blindly — mixing the two raises TypeError, which is how a single
    cloud-graded word could blank a whole screen.
    """
    try:
        due = datetime.fromisoformat(
            str(next_review or "").replace(" ", "T").replace("Z", "+00:00"))
    except ValueError:
        return None
    now = now or datetime.now()
    if due.tzinfo is None and now.tzinfo is not None:
        now = now.astimezone().replace(tzinfo=None)
    elif due.tzinfo is not None and now.tzinfo is None:
        now = now.astimezone()  # a naive `now` is local time
    return (due - now).total_seconds()


def status_from_progress(review_count: int, ease: float, correct_count: int) -> str:
    """The familiarity status a card's scheduling state maps to (web-app rules)."""
    if int(review_count or 0) == 0:
        return "New"
    if float(ease) >= 2.3 and int(correct_count) >= 5:
        return "Mastered"
    if float(ease) >= 2.0 and int(correct_count) >= 3:
        return "Learning"
    return "Reviewing"


def promotion_target(current, mapped: str):
    """Return the status ``current`` should be promoted to given the SM-2
    mapping ``mapped``, or ``None`` to leave it unchanged.

    Same never-demote contract as :func:`progression.next_status`, with one
    difference: ``"To Learn"`` counts as promotable at New rank — the user is
    actively studying it, unlike passive listening. ``Ignored``/custom
    statuses stay untouched.
    """
    key = (current or "").strip()
    if key.lower() in ("", "new", "to learn"):
        current_rank = 0
    elif key in progression.LADDER:
        current_rank = progression.LADDER.index(key)
    else:
        return None
    mapped_rank = progression.LADDER.index(mapped) if mapped in progression.LADDER else 0
    if mapped_rank > current_rank:
        return mapped
    return None
