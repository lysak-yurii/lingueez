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

"""Quiz question building and answer matching (pure, Qt-free, testable).

A quiz asks a word and takes an answer back, either as one of several choices
or as typed text. That is the whole difference from a flashcard, where the
learner reveals the answer and rates their own recall — here the answer has to
be produced before anything is shown.

Both halves of that live here and nowhere else, so the page above stays a view.
Everything takes an injectable :class:`random.Random`, which is what makes a
generated quiz reproducible in tests.

Grading is deliberately coarse. A quiz has no self-assessment step, so it can
only say *right* or *wrong* — :data:`GRADE_FOR_VERDICT` therefore never yields
``"easy"``, and a correct answer claims the ordinary Good interval rather than
the long one. The companion mobile app makes the same choice, and both write
the same shared ``srs_progress``/``word_progress`` schedule, so the two must
not drift.

Records are the plain dicts the rest of the UI passes around, with the keys
``ID``, ``Word1``, ``Word2``, ``Language1``, ``Language2``.
"""

from __future__ import annotations

import random
import re
import unicodedata
from dataclasses import dataclass, field

FORMATS = ("choices", "typing")
DIRECTIONS = ("term", "translation", "mixed")
VERDICTS = ("correct", "almost", "wrong")

DEFAULT_OPTION_COUNT = 4
MIN_OPTION_COUNT = 2

#: A quiz cannot tell "easy" from "good" — see the module docstring.
GRADE_FOR_VERDICT = {"correct": "good", "almost": "good", "wrong": "hard"}

#: Below this length a one-character edit is a different word, not a typo.
NEAR_MISS_MIN_LENGTH = 4

# Expansions NFD decomposition does *not* perform: these letters have no
# combining-mark form to strip, so folding them needs an explicit table.
_EXPANSIONS = {
    "ß": "ss", "æ": "ae", "œ": "oe", "ø": "o", "đ": "d", "ð": "d",
    "ł": "l", "þ": "th", "ħ": "h", "ı": "i", "ŋ": "n", "ẞ": "ss",
}

# Stripped from either end of an answer, but never from inside it: "rock-'n'-roll"
# keeps its punctuation, while "(the) house." matches "the house".
_EDGE_PUNCTUATION = ".,;:!?\"'“”‘’„«»()[]{}<>…-–—"

# An entry may list several accepted answers: "window, pane", "der/die/das".
_ALTERNATIVE_SPLIT = re.compile(r"[,;/|]")

_WHITESPACE = re.compile(r"\s+")


@dataclass
class QuizQuestion:
    """One asked word, with the options it is answered from.

    ``reversed`` flips which stored column is shown: normally the prompt is
    ``Word1`` and the answer ``Word2``, and reversed swaps them. ``options``
    is empty and ``correct_index`` is -1 in the typing format.
    """

    record: dict
    reversed: bool = False
    options: list[str] = field(default_factory=list)
    correct_index: int = -1

    @property
    def word_id(self):
        return self.record.get("ID")

    @property
    def prompt(self) -> str:
        return str(self.record.get("Word2" if self.reversed else "Word1") or "")

    @property
    def prompt_language(self) -> str:
        key = "Language2" if self.reversed else "Language1"
        return str(self.record.get(key) or "")

    @property
    def answer(self) -> str:
        return str(self.record.get("Word1" if self.reversed else "Word2") or "")

    @property
    def answer_language(self) -> str:
        key = "Language1" if self.reversed else "Language2"
        return str(self.record.get(key) or "")


# ---------------------------------------------------------------- answers ---

def normalize_answer(text) -> str:
    """Fold *text* to the form two answers are compared in.

    Case, accents and edge punctuation are all noise for recall: someone who
    types "uber" for "über" knew the word. Internal hyphens and apostrophes
    survive, because they do distinguish words.
    """
    value = str(text or "").strip().lower()
    if not value:
        return ""
    value = "".join(_EXPANSIONS.get(ch, ch) for ch in value)
    decomposed = unicodedata.normalize("NFD", value)
    value = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    value = _WHITESPACE.sub(" ", value)
    return value.strip(_EDGE_PUNCTUATION).strip()


def acceptable_answers(expected) -> list[str]:
    """Every normalized form that counts as answering *expected*.

    The whole entry, plus each of its comma/slash-separated alternatives, so
    "window, pane" is answered by either word and "der/die/das" by any article.
    Order is preserved and duplicates dropped.
    """
    whole = normalize_answer(expected)
    out = [whole] if whole else []
    for part in _ALTERNATIVE_SPLIT.split(str(expected or "")):
        candidate = normalize_answer(part)
        if candidate and candidate not in out:
            out.append(candidate)
    return out


def edit_distance(a: str, b: str, limit: int = 2) -> int:
    """Damerau-OSA distance between *a* and *b*, giving up past *limit*.

    Returns ``limit + 1`` as soon as no cell in a row can still come in under
    the limit — the caller only ever asks "is this within one edit?", so the
    full matrix is wasted work.
    """
    if a == b:
        return 0
    if abs(len(a) - len(b)) > limit:
        return limit + 1
    if not a:
        return len(b)
    if not b:
        return len(a)

    prev2 = None
    prev = list(range(len(b) + 1))
    for i, ch_a in enumerate(a, start=1):
        cur = [i] + [0] * len(b)
        for j, ch_b in enumerate(b, start=1):
            cost = 0 if ch_a == ch_b else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
            if (prev2 is not None and i > 1 and j > 1
                    and ch_a == b[j - 2] and a[i - 2] == ch_b):
                cur[j] = min(cur[j], prev2[j - 2] + 1)
        if min(cur) > limit:
            return limit + 1
        prev2, prev = prev, cur
    return prev[len(b)]


def verdict_for(typed, expected) -> str:
    """Judge a typed answer as ``"correct"``, ``"almost"`` or ``"wrong"``.

    ``"almost"`` is a single edit away from an accepted answer and counts as
    correct for grading — it marks a typo, not a gap in recall. Short answers
    are exempt: one edit turns "cat" into "car", which is a different word.
    """
    given = normalize_answer(typed)
    if not given:
        return "wrong"
    candidates = acceptable_answers(expected)
    if given in candidates:
        return "correct"
    for candidate in candidates:
        if len(candidate) < NEAR_MISS_MIN_LENGTH:
            continue
        if edit_distance(given, candidate, 1) <= 1:
            return "almost"
    return "wrong"


def is_correct(verdict: str) -> bool:
    """Whether *verdict* counts as a correct answer (``almost`` does)."""
    return verdict in ("correct", "almost")


# -------------------------------------------------------------- questions ---

def _plausible_first(candidates: list[str], answer: str,
                     rng: random.Random) -> list[str]:
    """Shuffle *candidates*, floating the ones close in length to *answer*.

    A quiz where the right answer is the only long word is answered without
    reading it. Sorting by nothing but length would be just as obvious in the
    other direction, so this shuffles first and only then partitions.
    """
    shuffled = list(candidates)
    rng.shuffle(shuffled)
    tolerance = max(2, len(answer) // 2)
    close, far = [], []
    for candidate in shuffled:
        target = close if abs(len(candidate) - len(answer)) <= tolerance else far
        target.append(candidate)
    return close + far


def _distractor_pool(record: dict, pool, correct: str, language: str,
                     rng: random.Random) -> list[str]:
    """Wrong answers for *record*, drawn from the rest of the library.

    Both sides of every other word are fair game, filtered to the language the
    answer is in — a German prompt answered by a mix of German and English
    options gives the answer away. A word with no language recorded filters
    nothing, which is the only sensible reading of "unknown".
    """
    wanted = str(language or "").strip().lower()
    taken = {normalize_answer(correct)}
    candidates = []
    word_id = record.get("ID")
    for other in pool:
        if word_id is not None and other.get("ID") == word_id:
            continue
        for text_key, lang_key in (("Word1", "Language1"), ("Word2", "Language2")):
            text = str(other.get(text_key) or "").strip()
            if not text:
                continue
            if wanted and str(other.get(lang_key) or "").strip().lower() != wanted:
                continue
            key = normalize_answer(text)
            if not key or key in taken:
                continue
            taken.add(key)
            candidates.append(text)
    return _plausible_first(candidates, correct, rng)


def build_quiz(deck, pool, fmt: str = "choices", *,
               option_count: int = DEFAULT_OPTION_COUNT,
               direction: str = "term",
               rng: random.Random | None = None) -> list[QuizQuestion]:
    """Turn *deck* into askable questions, drawing distractors from *pool*.

    *pool* is the whole studiable library rather than the deck, so a five-word
    session still gets plausible wrong answers.

    A question is dropped rather than asked badly: a word missing either side
    cannot be asked at all, and a choices question that cannot reach two
    distinct options is not a question. So the returned list may be shorter
    than *deck*, and ``option_count`` is an upper bound that degrades toward
    :data:`MIN_OPTION_COUNT` rather than a promise.
    """
    rng = rng or random.Random()
    typing = fmt == "typing"
    pool = list(pool)
    questions = []
    for record in deck:
        if not str(record.get("Word1") or "").strip():
            continue
        if not str(record.get("Word2") or "").strip():
            continue

        if direction == "mixed":
            reversed_ = rng.choice((False, True))
        else:
            reversed_ = direction == "translation"

        if typing:
            questions.append(QuizQuestion(record=record, reversed=reversed_))
            continue

        question = QuizQuestion(record=record, reversed=reversed_)
        correct = question.answer.strip()
        candidates = _distractor_pool(record, pool, correct,
                                      question.answer_language, rng)
        count = min(option_count, len(candidates) + 1)
        if count < MIN_OPTION_COUNT:
            continue
        # Shuffle the pairs and read the index back off the shuffle: recovering
        # it by searching for the answer text would pick the wrong row whenever
        # an option repeats it.
        entries = [(correct, True)] + [(d, False) for d in candidates[:count - 1]]
        rng.shuffle(entries)
        question.options = [text for text, _ in entries]
        question.correct_index = next(i for i, (_, ok) in enumerate(entries) if ok)
        questions.append(question)
    return questions
