# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Behaviour tests for the Quiz page that need real widgets.

A picker persists its choices through ``app.config.save_settings``, which
resolves ``settings.cfg`` relative to the cwd — and the suite runs from the
repo root. Any test that builds a real picker therefore has to neutralise
that write, or running the tests silently overwrites the developer's own
settings with defaults: tours reappear, dismissed banners come back, table
density resets. ``_SettingsIsolation`` below is not optional politeness.

Run:  python -m unittest tests.test_quiz_page
"""

import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication, QWidget  # noqa: E402

from app import config as app_config  # noqa: E402
from app.ui import theme  # noqa: E402
from app.ui import quiz_page as qp  # noqa: E402

_app = QApplication.instance() or QApplication([])


def _record(i):
    return {
        "ID": str(i),
        "Word1": f"word{i}",
        "Word2": f"Wort{i}",
        "Language1": "English",
        "Language2": "German",
        "Status": "New",
    }


RECORDS = [_record(i) for i in range(6)]

SETTINGS = {
    "quiz_deck_size": "6",
    "quiz_format": "choices",
    "quiz_direction": "term",
    "quiz_auto_advance": "True",
    "quiz_shuffle": "False",
    "quiz_pronounce": "True",
}


class _FakeAdapter:
    def get_word(self, wid):
        return {}


class _SettingsIsolation:
    """Keeps a test's settings writes off the developer's real settings.cfg.

    Two layers on purpose. Stubbing save_settings captures what the page
    *meant* to persist, so the tests can assert on it; the temporary cwd is
    the backstop, so anything else that resolves a path relative to the
    working directory lands in a sandbox rather than the repo.
    """

    def setUp(self):
        super().setUp()
        self.saved = []
        patcher = mock.patch.object(
            app_config,
            "save_settings",
            side_effect=lambda values, *a, **k: self.saved.append(dict(values)),
        )
        patcher.start()
        self.addCleanup(patcher.stop)

        sandbox = tempfile.mkdtemp(prefix="quizpage-")
        origin = os.getcwd()
        os.chdir(sandbox)
        self.addCleanup(os.chdir, origin)


class AutoAdvanceTimingTests(_SettingsIsolation, unittest.TestCase):
    """Auto-advance must wait for the answer's audio instead of racing it.

    A fixed delay cut long answers off mid-word, because how long a word takes
    to pronounce is not a constant. These tests drive the seam directly rather
    than real playback, so they stay deterministic."""

    def setUp(self):
        super().setUp()
        self.settings = {
            "quiz_deck_size": "6",
            "quiz_format": "choices",
            "quiz_direction": "term",
            "quiz_auto_advance": "True",
            "quiz_shuffle": "False",
            "quiz_pronounce": "True",
        }
        self.page = qp.QuizPage(
            _FakeAdapter(),
            theme.current_colors(),
            lambda kind, n: RECORDS[:n],
            lambda: RECORDS,
            lambda: self.settings,
        )
        self.addCleanup(self.page.deleteLater)
        self.spoken = []

    def _start(self, speaks):
        """Begin a session whose answer pronunciation is stubbed out.

        ``speaks`` is what the stub reports back: True stands for audio that
        is now playing and will call back when it ends."""

        def fake_speak_answer(on_done=None):
            self.spoken.append(on_done)
            return speaks

        self.page._speak_answer = fake_speak_answer
        self.page._speak_prompt = lambda auto=False: None
        self.page._start_clicked()
        self.assertTrue(self.page._questions, "no questions were built")

    def _answer_correctly(self):
        question = self.page._current()
        self.page._answer_choice(question.correct_index)

    def test_countdown_waits_while_the_answer_is_being_spoken(self):
        self._start(speaks=True)
        self._answer_correctly()
        self.assertTrue(self.page._revealed)
        self.assertFalse(
            self.page._advance_timer.isActive(),
            "advanced on a fixed timer while the answer was still playing",
        )
        self.assertTrue(self.page.drain_host.isVisibleTo(self.page))

    def test_countdown_starts_when_the_speech_reports_back(self):
        self._start(speaks=True)
        self._answer_correctly()
        self.assertEqual(len(self.spoken), 1)
        self.spoken[0]()  # the pronunciation finished playing
        self.assertTrue(self.page._advance_timer.isActive())
        self.assertEqual(self.page._advance_timer.interval(), qp.AUTO_ADVANCE_AFTER_SPEECH_MS)

    def test_a_silent_answer_keeps_the_full_pause(self):
        self._start(speaks=False)
        self._answer_correctly()
        self.assertTrue(self.page._advance_timer.isActive())
        self.assertEqual(self.page._advance_timer.interval(), qp.AUTO_ADVANCE_MS)

    def test_a_stall_guard_is_armed_while_waiting_on_audio(self):
        # Without it, a hung TTS request would park the quiz on one question.
        self._start(speaks=True)
        self._answer_correctly()
        self.assertTrue(self.page._stall_timer.isActive())
        self.spoken[0]()
        self.assertFalse(self.page._stall_timer.isActive())

    def test_a_wrong_answer_never_auto_advances(self):
        self._start(speaks=True)
        question = self.page._current()
        self.page._answer_choice((question.correct_index + 1) % len(question.options))
        # The answer is still pronounced, but with no completion callback:
        # there is no countdown for it to start.
        self.assertEqual(self.spoken, [None])
        self.assertFalse(self.page._advance_timer.isActive())
        self.assertFalse(self.page._stall_timer.isActive())
        self.assertTrue(self.page.next_btn.isVisibleTo(self.page))

    def test_a_late_callback_cannot_advance_a_question_already_left(self):
        self._start(speaks=True)
        self._answer_correctly()
        index = self.page._index
        self.page._next_question()  # the user clicked through first
        self.assertEqual(self.page._index, index + 1)
        self.spoken[0]()  # the superseded pronunciation reports back
        self.assertFalse(
            self.page._advance_timer.isActive(),
            "a stale speech callback started a countdown on the next question",
        )

    def test_auto_advance_off_shows_the_next_button_instead(self):
        self.page.advance_btn.setChecked(False)
        self._start(speaks=True)
        self._answer_correctly()
        self.assertFalse(self.page._advance_timer.isActive())
        self.assertTrue(self.page.next_btn.isVisibleTo(self.page))


class PickerGeometryTests(_SettingsIsolation, unittest.TestCase):
    """The picker bar must be settled before the page transition grabs it.

    A hidden page keeps the geometry it was last laid out at — narrower than
    the stack, so the control flow wraps to extra rows and the bar is taller.
    The transition snapshots the incoming page the instant it becomes current,
    so a stale frame there shows up as the bar visibly shrinking on open."""

    def _page_in_parent(self, width):
        parent = QWidget()
        parent.resize(width, 800)
        page = qp.QuizPage(
            _FakeAdapter(),
            theme.current_colors(),
            lambda kind, n: RECORDS[:n],
            lambda: RECORDS,
            lambda: dict(SETTINGS),
            parent,
        )
        self.addCleanup(parent.deleteLater)
        return page

    def test_on_shown_leaves_the_bar_at_its_final_height(self):
        for width in (1400, 1000, 700, 520):
            with self.subTest(width=width):
                page = self._page_in_parent(width)
                page.on_shown()
                panel = page.picker_panel
                self.assertEqual(
                    panel.height(),
                    panel.heightForWidth(panel.width()),
                    "the bar would still resize after the transition snapshot",
                )

    def test_settling_adopts_the_parent_width(self):
        page = self._page_in_parent(1400)
        self.assertNotEqual(page.width(), 1400)  # not laid out yet
        page.on_shown()
        self.assertEqual(page.width(), 1400)

    def test_resizing_never_leaves_the_bar_a_frame_behind(self):
        """The title must not hop while the window is being dragged.

        The bar's height depends on its width, so if the layout needs a second
        pass to get it right, the first frame is drawn at the wrong height and
        everything below the title shifts and shifts back."""
        parent = QWidget()
        parent.resize(1200, 800)
        page = self._page_in_parent(1200)
        parent = page.parentWidget()
        page.on_shown()
        panel = page.picker_panel
        title = page.picker_title

        def title_y():
            return title.mapTo(page, title.rect().topLeft()).y()

        for width in (1000, 820, 640, 520, 430, 380, 520, 820, 1200):
            with self.subTest(width=width):
                parent.resize(width, 800)
                page.resize(parent.size())
                during = title_y()
                _app.processEvents()
                _app.processEvents()
                self.assertEqual(
                    during,
                    title_y(),
                    "the title moved and moved back — the bar resized a frame late",
                )
                self.assertEqual(panel.height(), panel.heightForWidth(panel.width()))

    def test_the_last_control_is_never_clipped(self):
        """The bar must grow to fit its wrapped rows, not cut the last one."""
        page = self._page_in_parent(1200)
        page.on_shown()
        parent = page.parentWidget()
        for width in (900, 700, 560, 460, 380):
            with self.subTest(width=width):
                parent.resize(width, 800)
                page.resize(parent.size())
                _app.processEvents()
                _app.processEvents()
                chip = page.advance_btn
                self.assertLessEqual(
                    chip.geometry().bottom(),
                    chip.parentWidget().height(),
                    "the last chip fell outside the bar",
                )


class PickerPreferenceTests(_SettingsIsolation, unittest.TestCase):
    """Picker choices are written back the moment they are made."""

    def setUp(self):
        super().setUp()
        self.settings = {
            "quiz_deck_size": "20",
            "quiz_format": "choices",
            "quiz_direction": "term",
            "quiz_auto_advance": "True",
            "quiz_shuffle": "False",
            "quiz_pronounce": "True",
        }
        self.page = qp.QuizPage(
            _FakeAdapter(),
            theme.current_colors(),
            lambda kind, n: RECORDS[:n],
            lambda: RECORDS,
            lambda: self.settings,
        )
        self.addCleanup(self.page.deleteLater)

    def test_building_the_page_persists_nothing(self):
        # Restoring saved choices must not look like the user making them.
        self.assertEqual(self.saved, [])

    def test_changing_the_format_is_persisted(self):
        self.page._format_chips["typing"].setChecked(True)
        self.assertTrue(self.saved, "the format change was never written")
        self.assertEqual(self.saved[-1]["quiz_format"], "typing")

    def test_changing_the_direction_is_persisted(self):
        self.page._direction_chips["mixed"].setChecked(True)
        self.assertEqual(self.saved[-1]["quiz_direction"], "mixed")

    def test_toggles_and_size_are_persisted(self):
        self.page.advance_btn.setChecked(False)
        self.assertEqual(self.saved[-1]["quiz_auto_advance"], "False")
        self.page.size_spin.setValue(35)
        self.assertEqual(self.saved[-1]["quiz_deck_size"], "35")

    def test_restored_choices_come_back_checked(self):
        self.settings.update({"quiz_format": "typing", "quiz_direction": "mixed"})
        page = qp.QuizPage(
            _FakeAdapter(),
            theme.current_colors(),
            lambda kind, n: RECORDS[:n],
            lambda: RECORDS,
            lambda: self.settings,
        )
        self.addCleanup(page.deleteLater)
        self.assertEqual(page._format(), "typing")
        self.assertEqual(page._direction(), "mixed")


if __name__ == "__main__":
    unittest.main()
