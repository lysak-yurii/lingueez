# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Swipe-to-grade on the flashcard: the phone's gesture, driven by the mouse."""

import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import QEvent, QPoint, QPointF, Qt  # noqa: E402
from PySide6.QtGui import QMouseEvent, QWheelEvent  # noqa: E402
from PySide6.QtTest import QTest  # noqa: E402
from PySide6.QtWidgets import QApplication  # noqa: E402

from app import config as app_config  # noqa: E402
from app.ui import flashcards_page as fp  # noqa: E402
from app.ui import swipe, theme  # noqa: E402

_app = QApplication.instance() or QApplication([])


class GradeForDragTests(unittest.TestCase):
    SIZE = (400, 320)  # commits at 320 * 0.14 = 44.8 px

    def test_each_direction_has_its_grade(self):
        self.assertEqual(swipe.grade_for_drag(-60, 0, *self.SIZE), "hard")
        self.assertEqual(swipe.grade_for_drag(60, 0, *self.SIZE), "easy")
        self.assertEqual(swipe.grade_for_drag(0, -60, *self.SIZE), "good")

    def test_down_grades_nothing(self):
        self.assertIsNone(swipe.grade_for_drag(0, 300, *self.SIZE))

    def test_a_short_drag_does_not_commit(self):
        self.assertIsNone(swipe.grade_for_drag(44, 0, *self.SIZE))
        self.assertEqual(swipe.grade_for_drag(45, 0, *self.SIZE), "easy")

    def test_the_longer_axis_wins_a_diagonal_and_a_tie_is_horizontal(self):
        self.assertEqual(swipe.grade_for_drag(50, -80, *self.SIZE), "good")
        self.assertEqual(swipe.grade_for_drag(-80, -50, *self.SIZE), "hard")
        self.assertEqual(swipe.grade_for_drag(60, -60, *self.SIZE), "easy")

    def test_a_big_card_never_asks_for_more_than_the_cap(self):
        self.assertEqual(swipe.commit_distance(2000, 1500), swipe.COMMIT_MAX)

    def test_a_zero_sized_card_never_commits(self):
        self.assertIsNone(swipe.grade_for_drag(500, 0, 0, 0))


def _row(i):
    return {
        "ID": str(i),
        "Word1": f"word{i}",
        "Word2": f"Wort{i}",
        "Language1": "English",
        "Language2": "German",
        "Status": "New",
    }


class _FakeAdapter:
    def get_word(self, wid):
        return {}


class SwipeGradesTests(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.object(
            app_config, "save_settings", side_effect=lambda values, *a, **k: None
        )
        patcher.start()
        self.addCleanup(patcher.stop)
        origin = os.getcwd()
        os.chdir(tempfile.mkdtemp(prefix="swipe-"))
        self.addCleanup(os.chdir, origin)
        for name in ("srs_get", "srs_upsert", "log_review"):
            p = mock.patch.object(fp.dbq, name, return_value=None)
            p.start()
            self.addCleanup(p.stop)
        p = mock.patch.object(fp.srs.CREDITS, "record")
        p.start()
        self.addCleanup(p.stop)

        self.settings = {"flashcards_pronounce": "False"}
        self.page = fp.FlashcardsPage(
            _FakeAdapter(),
            theme.current_colors(),
            lambda kind, n: [],
            lambda: self.settings,
        )
        self.addCleanup(self.page.deleteLater)
        self.page.resize(900, 700)
        self.page.show()
        self.page.start_session([_row(i) for i in range(3)], autoplay=False)
        _app.processEvents()
        self.card = self.page.card

    def _mouse(self, kind, offset, held=Qt.LeftButton):
        local = QPointF(self.card.rect().center()) + QPointF(*offset)
        button = Qt.NoButton if kind == QEvent.MouseMove else Qt.LeftButton
        QApplication.sendEvent(
            self.card,
            QMouseEvent(
                kind,
                local,
                QPointF(self.card.mapToGlobal(local.toPoint())),
                button,
                held,
                Qt.NoModifier,
            ),
        )

    def _drag(self, dx, dy):
        self._mouse(QEvent.MouseButtonPress, (0, 0))
        for step in (0.5, 1.0):
            self._mouse(QEvent.MouseMove, (dx * step, dy * step))
        self._mouse(QEvent.MouseButtonRelease, (dx, dy), held=Qt.NoButton)

    def test_a_swipe_grades_from_the_front_and_advances(self):
        self._drag(-120, 0)
        self.assertEqual(self.page._grade_history, {0: "hard"})
        self.assertEqual(self.page._index, 1)
        self.assertIsNone(self.card._swipe)

    def test_right_is_easy_and_up_is_good(self):
        self._drag(120, 0)
        self._drag(0, -120)
        self.assertEqual(self.page._grade_history, {0: "easy", 1: "good"})

    def test_a_short_drag_neither_grades_nor_flips(self):
        self._drag(20, 0)
        self.assertEqual(self.page._grade_history, {})
        self.assertEqual(self.card.side, 0)

    def test_a_plain_click_still_flips(self):
        self._drag(0, 0)
        _app.processEvents()
        self.assertEqual(self.page._grade_history, {})
        self.assertIsNone(self.card._swipe)
        self.assertTrue(self.card._flipping or self.card.side == 1)

    def test_no_swipe_while_autoplay_is_listening(self):
        self.page.start_session([_row(i) for i in range(3)], autoplay=True)
        self._drag(-120, 0)
        self.assertEqual(self.page._grade_history, {})

    def test_a_graded_card_cannot_be_swiped_again(self):
        self._drag(-120, 0)
        self.page._show_card(0)
        self._drag(120, 0)
        self.assertEqual(self.page._grade_history, {0: "hard"})


class CardZoomTests(SwipeGradesTests):
    def _wheel(self, target, dy, modifiers=Qt.ControlModifier):
        # Qt only walks an ignored wheel event up the parents when it came from
        # the window system, so a synthetic one has to be walked by hand.
        while target is not None:
            pos = QPointF(target.rect().center())
            event = QWheelEvent(
                pos,
                QPointF(target.mapToGlobal(pos.toPoint())),
                QPoint(0, 0),
                QPoint(0, dy),
                Qt.NoButton,
                modifiers,
                Qt.NoScrollPhase,
                False,
            )
            if QApplication.sendEvent(target, event) and event.isAccepted():
                return
            target = target.parentWidget()

    def test_ctrl_scroll_grows_the_card_and_its_buttons(self):
        font_before = self.card.word.font().pointSize()
        width_before = self.page.hard_btn.minimumWidth()
        self._wheel(self.card, 120)
        self._wheel(self.card, 120)
        self.assertEqual(self.page._zoom_step, 2)
        self.assertGreater(self.card.maximumWidth(), 640)
        self.assertGreater(self.page.hard_btn.minimumWidth(), width_before)
        _app.processEvents()
        self.assertGreater(self.card.word.font().pointSize(), font_before)

    def test_it_reaches_the_page_from_over_the_definition(self):
        self._wheel(self.card.body_scroll.viewport(), -120)
        self.assertEqual(self.page._zoom_step, -1)

    def test_a_plain_scroll_does_not_zoom(self):
        self._wheel(self.card, 120, Qt.NoModifier)
        self.assertEqual(self.page._zoom_step, 0)

    def test_the_zoom_is_clamped_and_ctrl_0_resets_it(self):
        for _ in range(40):
            self._wheel(self.card, 120)
        self.assertEqual(self.page._zoom_step, fp.ZOOM_MAX)
        QTest.keyClick(self.page, Qt.Key_0, Qt.ControlModifier)
        self.assertEqual(self.page._zoom_step, 0)
        self.assertEqual(self.card.maximumWidth(), 640)

    def test_the_corner_buttons_step_reset_and_show_the_zoom(self):
        self.page.zoom_in_btn.click()
        self.page.zoom_in_btn.click()
        self.assertEqual(self.page.zoom_reset_btn.text(), "120%")
        self.page.zoom_out_btn.click()
        self.assertEqual(self.page._zoom_step, 1)
        self.page.zoom_reset_btn.click()
        self.assertEqual(self.page._zoom_step, 0)
        self.assertEqual(self.page.zoom_reset_btn.text(), "100%")

    def test_the_buttons_stop_at_the_limits(self):
        for _ in range(40):
            self.page.zoom_out_btn.click()
        self.assertEqual(self.page._zoom_step, fp.ZOOM_MIN)
        self.assertFalse(self.page.zoom_out_btn.isEnabled())
        self.assertTrue(self.page.zoom_in_btn.isEnabled())

    def test_the_step_is_remembered(self):
        self._wheel(self.card, 120)
        self.assertEqual(self.settings["flashcards_zoom"], "1")


if __name__ == "__main__":
    unittest.main()
