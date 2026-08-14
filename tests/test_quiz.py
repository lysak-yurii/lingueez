# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for quiz question building and typed-answer matching.

Run:  python -m unittest tests.test_quiz
"""

import os
import random
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import quiz  # noqa: E402


def _word(wid, w1, w2, l1="English", l2="German"):
    return {"ID": wid, "Word1": w1, "Word2": w2, "Language1": l1, "Language2": l2}


LIBRARY = [
    _word("1", "house", "Haus"),
    _word("2", "tree", "Baum"),
    _word("3", "water", "Wasser"),
    _word("4", "window", "Fenster"),
    _word("5", "bread", "Brot"),
    _word("6", "street", "Straße"),
]


class NormalizeAnswerTests(unittest.TestCase):
    def test_folds_case_and_accents(self):
        self.assertEqual(quiz.normalize_answer("Über"), "uber")
        self.assertEqual(quiz.normalize_answer("CAFÉ"), "cafe")

    def test_expands_letters_nfd_cannot_decompose(self):
        self.assertEqual(quiz.normalize_answer("Straße"), "strasse")
        self.assertEqual(quiz.normalize_answer("Æther"), "aether")
        self.assertEqual(quiz.normalize_answer("Œuvre"), "oeuvre")

    def test_strips_edge_punctuation_but_keeps_internal(self):
        self.assertEqual(quiz.normalize_answer("(the) house."), "the) house")
        self.assertEqual(quiz.normalize_answer("rock-'n'-roll"), "rock-'n'-roll")

    def test_collapses_whitespace(self):
        self.assertEqual(quiz.normalize_answer("  a   b  "), "a b")

    def test_blank_input(self):
        self.assertEqual(quiz.normalize_answer(None), "")
        self.assertEqual(quiz.normalize_answer("   "), "")


class AcceptableAnswersTests(unittest.TestCase):
    def test_comma_alternatives(self):
        # The whole entry stays intact as one candidate — the comma is internal
        # punctuation — and each alternative is accepted on its own as well.
        self.assertEqual(
            quiz.acceptable_answers("window, pane"), ["window, pane", "window", "pane"]
        )

    def test_slash_alternatives(self):
        self.assertIn("die", quiz.acceptable_answers("der/die/das"))

    def test_single_answer_has_no_duplicates(self):
        self.assertEqual(quiz.acceptable_answers("house"), ["house"])


class EditDistanceTests(unittest.TestCase):
    def test_identical(self):
        self.assertEqual(quiz.edit_distance("haus", "haus"), 0)

    def test_substitution_insertion_deletion(self):
        self.assertEqual(quiz.edit_distance("haus", "hauz"), 1)
        self.assertEqual(quiz.edit_distance("haus", "hauss"), 1)
        self.assertEqual(quiz.edit_distance("haus", "hau"), 1)

    def test_transposition_is_one_edit(self):
        self.assertEqual(quiz.edit_distance("haus", "huas"), 1)

    def test_gives_up_past_the_limit(self):
        self.assertEqual(quiz.edit_distance("house", "bread", 1), 2)
        self.assertEqual(quiz.edit_distance("a", "abcdef", 2), 3)


class VerdictTests(unittest.TestCase):
    def test_exact_match_ignoring_case_and_accents(self):
        self.assertEqual(quiz.verdict_for("haus", "Haus"), "correct")
        self.assertEqual(quiz.verdict_for("strasse", "Straße"), "correct")

    def test_one_typo_is_almost(self):
        self.assertEqual(quiz.verdict_for("Fesnter", "Fenster"), "almost")
        self.assertEqual(quiz.verdict_for("hous", "house"), "almost")

    def test_short_words_get_no_typo_forgiveness(self):
        # One edit turns "cat" into "car" — a different word, not a slip.
        self.assertEqual(quiz.verdict_for("car", "cat"), "wrong")

    def test_any_listed_alternative_is_accepted(self):
        self.assertEqual(quiz.verdict_for("pane", "window, pane"), "correct")

    def test_blank_and_unrelated_answers_are_wrong(self):
        self.assertEqual(quiz.verdict_for("", "Haus"), "wrong")
        self.assertEqual(quiz.verdict_for("Baum", "Haus"), "wrong")

    def test_is_correct_treats_almost_as_correct(self):
        self.assertTrue(quiz.is_correct("correct"))
        self.assertTrue(quiz.is_correct("almost"))
        self.assertFalse(quiz.is_correct("wrong"))


class GradeMappingTests(unittest.TestCase):
    def test_every_verdict_maps(self):
        self.assertEqual(set(quiz.GRADE_FOR_VERDICT), set(quiz.VERDICTS))

    def test_a_quiz_never_grades_easy(self):
        # There is no self-assessment step to justify the longer interval, and
        # the mobile app makes the same call against the same shared schedule.
        self.assertNotIn("easy", quiz.GRADE_FOR_VERDICT.values())
        self.assertEqual(quiz.GRADE_FOR_VERDICT["almost"], "good")
        self.assertEqual(quiz.GRADE_FOR_VERDICT["wrong"], "hard")


class BuildQuizTests(unittest.TestCase):
    def setUp(self):
        self.rng = random.Random(0)

    def test_asks_every_deck_word_with_four_options(self):
        questions = quiz.build_quiz(LIBRARY, LIBRARY, "choices", rng=self.rng)
        self.assertEqual(len(questions), len(LIBRARY))
        for q in questions:
            self.assertEqual(len(q.options), 4)
            self.assertEqual(q.options[q.correct_index], q.answer)

    def test_options_are_distinct_after_normalization(self):
        questions = quiz.build_quiz(LIBRARY, LIBRARY, "choices", rng=self.rng)
        for q in questions:
            keys = [quiz.normalize_answer(o) for o in q.options]
            self.assertEqual(len(set(keys)), len(keys))

    def test_distractors_never_come_from_the_asked_word(self):
        questions = quiz.build_quiz(LIBRARY, LIBRARY, "choices", rng=self.rng)
        for q in questions:
            wrong = [o for i, o in enumerate(q.options) if i != q.correct_index]
            self.assertNotIn(q.prompt, wrong)
            self.assertNotIn(q.answer, wrong)

    def test_distractors_match_the_answer_language(self):
        deck = [_word("7", "salt", "Salz")]
        pool = deck + LIBRARY + [_word("8", "sel", "sale", "French", "Italian")]
        questions = quiz.build_quiz(deck, pool, "choices", rng=self.rng)
        german = {w["Word2"] for w in LIBRARY} | {"Salz"}
        self.assertTrue(set(questions[0].options) <= german)

    def test_a_single_word_library_yields_no_choices_questions(self):
        one = [_word("1", "house", "Haus")]
        self.assertEqual(quiz.build_quiz(one, one, "choices", rng=self.rng), [])

    def test_option_count_degrades_instead_of_failing(self):
        two = LIBRARY[:2]
        questions = quiz.build_quiz(two, two, "choices", option_count=4, rng=self.rng)
        self.assertEqual(len(questions), 2)
        for q in questions:
            self.assertEqual(len(q.options), 2)

    def test_words_missing_a_side_are_skipped(self):
        deck = LIBRARY + [_word("9", "orphan", "  ")]
        questions = quiz.build_quiz(deck, LIBRARY, "choices", rng=self.rng)
        self.assertNotIn("orphan", [q.prompt for q in questions])

    def test_typing_questions_carry_no_options(self):
        questions = quiz.build_quiz(LIBRARY, LIBRARY, "typing", rng=self.rng)
        self.assertEqual(len(questions), len(LIBRARY))
        for q in questions:
            self.assertEqual(q.options, [])
            self.assertEqual(q.correct_index, -1)

    def test_typing_works_with_a_one_word_library(self):
        # Nothing to draw distractors from, but the word can still be asked.
        one = [_word("1", "house", "Haus")]
        self.assertEqual(len(quiz.build_quiz(one, one, "typing", rng=self.rng)), 1)

    def test_direction_term_asks_word1(self):
        q = quiz.build_quiz(LIBRARY[:1], LIBRARY, "typing", direction="term", rng=self.rng)[0]
        self.assertEqual((q.prompt, q.answer), ("house", "Haus"))
        self.assertEqual((q.prompt_language, q.answer_language), ("English", "German"))

    def test_direction_translation_asks_word2(self):
        q = quiz.build_quiz(LIBRARY[:1], LIBRARY, "typing", direction="translation", rng=self.rng)[
            0
        ]
        self.assertEqual((q.prompt, q.answer), ("Haus", "house"))
        self.assertEqual((q.prompt_language, q.answer_language), ("German", "English"))

    def test_direction_mixed_uses_both(self):
        deck = LIBRARY * 8
        questions = quiz.build_quiz(deck, LIBRARY, "typing", direction="mixed", rng=self.rng)
        self.assertEqual({q.reversed for q in questions}, {False, True})

    def test_the_same_seed_builds_the_same_quiz(self):
        a = quiz.build_quiz(LIBRARY, LIBRARY, "choices", rng=random.Random(7))
        b = quiz.build_quiz(LIBRARY, LIBRARY, "choices", rng=random.Random(7))
        self.assertEqual(
            [(q.options, q.correct_index) for q in a], [(q.options, q.correct_index) for q in b]
        )


if __name__ == "__main__":
    unittest.main()
