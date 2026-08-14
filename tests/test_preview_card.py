# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Tests for the flashcards deck-preview tile.

Run:  python -m unittest tests.test_preview_card
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtGui import QColor  # noqa: E402
from PySide6.QtWidgets import QApplication  # noqa: E402

from app.ui.flashcards_page import _ClampedLabel  # noqa: E402

_app = QApplication.instance() or QApplication([])

LONG = (
    "Spedition bezeichnet die Organisation und Durchführung von Transporten, "
    "insbesondere im Güterverkehr. Es handelt sich um ein Gewerbe."
)
UNBREAKABLE = (
    "Donaudampfschifffahrtsgesellschaftskapitaenswitwe ist ein unglaublich "
    "langes zusammengesetztes Wort das nicht umbrechen kann."
)


def _rendered_rows_with_ink(label):
    """Row indices that contain any painted text."""
    image = label.grab().toImage()
    background = image.pixelColor(0, 0)
    rows = []
    for y in range(image.height()):
        for x in range(image.width()):
            if image.pixelColor(x, y) != background:
                rows.append(y)
                break
    return rows


def _ink_bands(label, spacing):
    """How many line-height bands contain painted text."""
    return len({y // spacing for y in _rendered_rows_with_ink(label)})


class ClampedLabelTests(unittest.TestCase):
    """The tile's definition must never be sliced through the glyphs.

    A plain QLabel fills its box, so when the height is not a whole multiple
    of the line spacing the final line is drawn cut in half."""

    def _label(self, text, lines_of_room, extra=0):
        label = _ClampedLabel(text)
        label.set_ink(QColor("#ffffff"))
        spacing = label.fontMetrics().lineSpacing()
        label.resize(240, lines_of_room * spacing + extra)
        return label, spacing

    def test_nothing_is_painted_below_the_last_whole_line(self):
        # `extra` leaves room for most of another line — exactly the case that
        # used to be drawn as a half-height row of glyphs.
        for extra_fraction in (0.0, 0.4, 0.6, 0.9):
            with self.subTest(extra=extra_fraction):
                label, spacing = self._label(LONG, 2)
                label.resize(240, int(2 * spacing + spacing * extra_fraction))
                rows = _rendered_rows_with_ink(label)
                self.assertTrue(rows, "nothing was painted at all")
                self.assertLessEqual(
                    max(rows),
                    2 * spacing,
                    "a partial line was painted past the last whole one",
                )

    def test_it_fills_exactly_the_lines_that_fit(self):
        for room in (1, 2, 3):
            with self.subTest(room=room):
                label, spacing = self._label(LONG, room)
                self.assertEqual(_ink_bands(label, spacing), room)

    def test_a_word_too_long_to_break_still_wraps(self):
        label, spacing = self._label(UNBREAKABLE, 2)
        self.assertEqual(_ink_bands(label, spacing), 2)

    def test_short_text_paints_a_single_line(self):
        label, spacing = self._label("Short one.", 2)
        self.assertEqual(_ink_bands(label, spacing), 1)

    def test_empty_text_paints_nothing(self):
        label, _ = self._label("   ", 2)
        self.assertEqual(_rendered_rows_with_ink(label), [])

    def test_a_box_too_short_for_one_line_still_paints_one(self):
        label, spacing = self._label(LONG, 0, extra=6)
        self.assertTrue(
            _rendered_rows_with_ink(label),
            "a squeezed tile went blank instead of eliding to one line",
        )


if __name__ == "__main__":
    unittest.main()
