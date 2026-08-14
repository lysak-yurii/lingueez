# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Parking a word on Ignored so practice stops offering it.

Three layers get covered here: the predicate every caller shares, the deck
provider that keeps ignored words out of flashcards / quiz / read-aloud, and
the session pages that drop the card once the word has been parked.

A page test builds a real picker, whose settings write resolves relative to
the cwd — see ``tests.test_quiz_page`` for why that has to be neutralised.

Run:  python -m unittest tests.test_ignore_word
"""

import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pandas as pd  # noqa: E402
from PySide6.QtWidgets import QApplication  # noqa: E402

from app import config as app_config  # noqa: E402
from app.core import progression  # noqa: E402
from app.ui import theme  # noqa: E402
from app.ui import flashcards_page as fp  # noqa: E402
from app.ui import quiz_page as qp  # noqa: E402

_app = QApplication.instance() or QApplication([])


class IgnoredStatusTests(unittest.TestCase):
    """The predicate is the contract with the phone, which writes the value."""

    def test_matches_however_another_client_cased_it(self):
        for value in ("Ignored", "ignored", "IGNORED", "  Ignored  "):
            with self.subTest(value=value):
                self.assertTrue(progression.is_ignored(value))
                self.assertFalse(progression.is_studiable(value))

    def test_everything_else_is_studiable(self):
        for value in ("New", "Mastered", "To Learn", "", "  ", "Ignore"):
            with self.subTest(value=value):
                self.assertFalse(progression.is_ignored(value))
                self.assertTrue(progression.is_studiable(value))

    def test_non_strings_are_studiable(self):
        # A blank status becomes NaN once it has been through a DataFrame, and
        # NaN is truthy — an `or ""` guard would hand .strip() a float.
        for value in (None, float("nan"), 0):
            with self.subTest(value=value):
                self.assertFalse(progression.is_ignored(value))
                self.assertTrue(progression.is_studiable(value))

    def test_ignored_is_offered_by_the_status_picker(self):
        self.assertIn(progression.IGNORED_STATUS, progression.ALL_STATUSES)

    def test_listening_never_promotes_off_the_ignored_rung(self):
        thresholds = progression.normalize_thresholds()
        self.assertIsNone(progression.next_status(progression.IGNORED_STATUS, 10_000, thresholds))


def _row(i, status="New"):
    return {
        "ID": str(i),
        "Word1": f"word{i}",
        "Word2": f"Wort{i}",
        "Language1": "English",
        "Language2": "German",
        "Status": status,
    }


class DeckProviderFilterTests(unittest.TestCase):
    """``MainWindow._flashcards_deck`` feeds flashcards, the quiz *and* the
    read-aloud playlist, so it is the one place the opt-out has to hold."""

    def setUp(self):
        from app.ui.main_window import MainWindow

        self.win = MainWindow.__new__(MainWindow)  # no Qt init: pure logic
        self.win.df = pd.DataFrame(
            [
                _row(0),
                _row(1, "Ignored"),
                _row(2),
                _row(3, "ignored"),
                _row(4),
                _row(5, "Mastered"),
            ]
        )

    def _ids(self, kind, n=10):
        return [r["ID"] for r in self.win._flashcards_deck(kind, n)]

    def test_newest_skips_ignored_however_cased(self):
        self.assertEqual(self._ids("newest"), ["0", "2", "4", "5"])

    def test_filtered_skips_ignored(self):
        from app.ui.word_model import WordFilter

        self.win.word_filter = WordFilter()
        self.assertEqual(self._ids("filtered"), ["0", "2", "4", "5"])

    def test_filtering_shortens_the_pool_not_the_deck(self):
        # Trimming to length before dropping ignored rows would return 1 card
        # for a deck of 2, which reads as a bug rather than as the opt-out.
        self.assertEqual(self._ids("newest", n=2), ["0", "2"])

    def test_an_explicit_table_selection_is_honoured(self):
        # Silently shrinking rows the user hand-picked would look broken.
        self.win.selected_records = lambda: [_row(1, "Ignored")]
        self.assertEqual(self._ids("selected"), ["1"])

    def test_quiz_distractor_pool_skips_ignored(self):
        self.assertEqual([r["ID"] for r in self.win._quiz_pool()], ["0", "2", "4", "5"])
        self.assertEqual(self.win._quiz_pool(count_only=True), 4)

    def test_a_blank_status_still_studies(self):
        self.win.df = pd.DataFrame([_row(0, None), _row(1, "Ignored")])
        self.assertEqual(self._ids("newest"), ["0"])


class _SettingsIsolation:
    """Keeps the pages' settings writes off the developer's real settings.cfg."""

    def setUp(self):
        super().setUp()
        patcher = mock.patch.object(
            app_config, "save_settings", side_effect=lambda values, *a, **k: None
        )
        patcher.start()
        self.addCleanup(patcher.stop)
        sandbox = tempfile.mkdtemp(prefix="ignoreword-")
        origin = os.getcwd()
        os.chdir(sandbox)
        self.addCleanup(os.chdir, origin)


class _FakeAdapter:
    def get_word(self, wid):
        return {}


class FlashcardsIgnoreTests(_SettingsIsolation, unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.records = [_row(i) for i in range(4)]
        self.settings = {
            "flashcards_deck_size": "4",
            "flashcards_shuffle": "False",
            "flashcards_pronounce": "False",
        }
        self.page = fp.FlashcardsPage(
            _FakeAdapter(),
            theme.current_colors(),
            lambda kind, n: [dict(r) for r in self.records[:n]],
            lambda: self.settings,
        )
        self.addCleanup(self.page.deleteLater)
        self.ignored = []
        self.page.ignore_requested.connect(
            lambda wid, prev, label: self.ignored.append((wid, prev, label))
        )
        self.page.start_session([dict(r) for r in self.records], autoplay=False)

    def test_ignoring_reports_the_previous_rung_and_drops_the_card(self):
        self.page._ignore_current()
        self.assertEqual(self.ignored, [("0", "New", "word0")])
        self.assertEqual([r["ID"] for r in self.page._deck], ["1", "2", "3"])
        # dropped, not graded: nothing was answered about this word
        self.assertEqual(self.page._grade_history, {})
        self.assertEqual(self.page._graded, set())

    def test_the_next_card_slides_into_the_same_slot(self):
        self.page._ignore_current()
        self.assertEqual(self.page._index, 0)
        self.assertEqual(self.page._deck[self.page._index]["ID"], "1")

    def test_ignoring_the_last_card_ends_the_session(self):
        self.page._show_card(3)
        self.page._ignore_current()
        self.assertEqual(self.page._stack.currentIndex(), self.page.STATE_COMPLETE)

    def test_ignoring_the_only_card_returns_to_the_picker(self):
        # An empty summary would read as a bug, not as an emptied deck.
        self.page.start_session([dict(self.records[0])], autoplay=False)
        self.page._ignore_current()
        self.assertEqual(self.page._stack.currentIndex(), self.page.STATE_PICKER)

    def test_an_already_ignored_word_is_a_no_op(self):
        self.page._deck[0]["Status"] = "Ignored"
        self.page._ignore_current()
        self.assertEqual(self.ignored, [])
        self.assertEqual(len(self.page._deck), 4)

    def test_a_graded_card_is_refused(self):
        # _grade_history is keyed by deck index; pulling a card out from under
        # an answer that already occupies that slot would misalign the trail.
        self.page._graded.add("0")
        self.page._ignore_current()
        self.assertEqual(self.ignored, [])
        self.assertEqual(len(self.page._deck), 4)

    def test_the_grade_trail_stays_aligned_with_the_deck(self):
        self.page._grade_history = {0: "hard", 1: "good"}
        self.page._graded = {"0", "1"}
        self.page._show_card(2)
        self.page._ignore_current()
        # keys past the removed index shift down with the cards they describe
        self.assertEqual(self.page._grade_history, {0: "hard", 1: "good"})
        self.assertEqual([r["ID"] for r in self.page._deck], ["0", "1", "3"])

    def test_autoplay_skips_instead_of_rebuilding_the_queue(self):
        # The deck mirrors a frozen player queue; dropping a card would desync
        # the audio, so the word only leaves on the next deck build.
        skips = []
        self.page.player_next_requested.connect(lambda: skips.append(True))
        self.page.start_session([dict(r) for r in self.records], autoplay=True)
        self.page._ignore_current()
        self.assertEqual(len(self.ignored), 1)
        self.assertEqual(skips, [True])
        self.assertEqual(len(self.page._deck), 4)

    def test_the_button_hides_once_the_word_is_parked(self):
        self.page.card.set_card(_row(9, "Ignored"))
        self.assertFalse(self.page.card.ignore_btn.isVisible())
        self.page.card.set_card(_row(9, "New"))
        self.assertTrue(self.page.card.ignore_btn.isVisibleTo(self.page.card))


class QuizIgnoreTests(_SettingsIsolation, unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.records = [_row(i) for i in range(6)]
        self.settings = {
            "quiz_deck_size": "6",
            "quiz_format": "choices",
            "quiz_direction": "term",
            "quiz_auto_advance": "False",
            "quiz_shuffle": "False",
            "quiz_pronounce": "False",
        }
        self.page = qp.QuizPage(
            _FakeAdapter(),
            theme.current_colors(),
            lambda kind, n: [dict(r) for r in self.records[:n]],
            lambda: [dict(r) for r in self.records],
            lambda: self.settings,
        )
        self.addCleanup(self.page.deleteLater)
        self.ignored = []
        self.page.ignore_requested.connect(
            lambda wid, prev, label: self.ignored.append((wid, prev, label))
        )
        self.page._speak_prompt = lambda auto=False: None
        self.page._speak_answer = lambda on_done=None: False
        self.page._start_clicked()
        self.assertTrue(self.page._questions, "no questions were built")

    def test_ignoring_drops_the_question(self):
        before = len(self.page._questions)
        self.page._ignore_current()
        self.assertEqual(len(self.ignored), 1)
        self.assertEqual(len(self.page._questions), before - 1)
        self.assertEqual(self.page._answers, [])

    def test_an_answered_question_is_refused(self):
        # An answer already occupies this slot, and _answers is read
        # positionally by the missed deck and the progress trail.
        question = self.page._current()
        self.page._answer_choice(question.correct_index)
        self.assertTrue(self.page._revealed)
        before = len(self.page._questions)
        self.page._ignore_current()
        self.assertEqual(self.ignored, [])
        self.assertEqual(len(self.page._questions), before)

    def test_the_button_hides_once_the_question_is_answered(self):
        self.assertTrue(self.page.prompt_card.ignore_btn.isVisibleTo(self.page.prompt_card))
        question = self.page._current()
        self.page._answer_choice(question.correct_index)
        self.assertFalse(self.page.prompt_card.ignore_btn.isVisibleTo(self.page.prompt_card))


if __name__ == "__main__":
    unittest.main()
