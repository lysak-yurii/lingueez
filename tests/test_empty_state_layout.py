# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Tests for the hand-pinned height of the empty-state subtitle.

Centering a word-wrapped QLabel makes the layout skip heightForWidth, so the
empty pages pin the height themselves. Getting that pin wrong only shows up on
some fonts — it clipped on Windows while looking fine on Linux — so it needs a
test rather than a look.

Nothing here may depend on which fonts are installed: the wrap-sensitive cases
build their own text from the running font's metrics.

Run:  python -m unittest tests.test_empty_state_layout
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import Qt  # noqa: E402
from PySide6.QtWidgets import QApplication, QLabel  # noqa: E402

from app.ui.main_window import EMPTY_SUB_WIDTH, pin_wrapped_height  # noqa: E402

_app = QApplication.instance() or QApplication([])

# The real first-run copy — the longest string that goes through the pin.
SUBTITLE = "Add your first word — its translation can be fetched automatically."
NO_MATCH = "Try a different search or filter."


def make_label(text):
    lbl = QLabel(text, alignment=Qt.AlignCenter)
    lbl.setWordWrap(True)
    lbl.setFixedWidth(EMPTY_SUB_WIDTH)
    return lbl


def text_just_too_wide(lbl):
    """Grow a phrase until it no longer fits on one line in the label.

    The result overflows EMPTY_SUB_WIDTH by less than one character, so it
    wraps to two lines at the label's width but still fits on one at any
    meaningfully larger width — which is exactly the case that used to clip.
    """
    fm = lbl.fontMetrics()
    text = "n"
    while fm.horizontalAdvance(text) <= EMPTY_SUB_WIDTH:
        text += " n"
    return text


class SubtitleHeightPinTests(unittest.TestCase):
    def assert_fits(self, lbl):
        self.assertGreaterEqual(
            lbl.height(),
            lbl.heightForWidth(lbl.width()),
            "subtitle is pinned shorter than the text it renders",
        )

    def test_real_copy_fits(self):
        lbl = make_label(SUBTITLE)
        pin_wrapped_height(lbl)
        self.assert_fits(lbl)

    def test_text_that_wraps_only_at_the_label_width_fits(self):
        # The original bug in font-independent form: the old code measured at
        # 380 while the label wraps at 355, so a string that needs two lines at
        # 355 and one at 380 got pinned a line short.
        lbl = make_label("")
        text = text_just_too_wide(lbl)
        lbl.setText(text)
        # Prove the text is wrap-sensitive: somewhere above the label's width
        # it needs fewer lines. Searched rather than hardcoded to 380, so this
        # holds in fonts where one character is wider than the 380 - 355 gap.
        tall = lbl.heightForWidth(EMPTY_SUB_WIDTH)
        wider = next(
            (w for w in range(EMPTY_SUB_WIDTH + 1, 4000) if lbl.heightForWidth(w) < tall),
            None,
        )
        self.assertIsNotNone(wider, "synthesized text never fits on fewer lines")
        pin_wrapped_height(lbl)
        self.assert_fits(lbl)

    def test_pin_shrinks_back_for_shorter_copy(self):
        # One label serves both the first-run and no-match copy. A stale pin
        # can't be spotted on the label itself — heightForWidth is floored by
        # the minimumHeight the pin just set, so it reports the inflated value
        # back. Compare against a fresh label that never held the long text.
        fresh = make_label(NO_MATCH)
        pin_wrapped_height(fresh)

        reused = make_label((text_just_too_wide(make_label("")) + " ") * 3)
        pin_wrapped_height(reused)
        self.assertGreater(reused.height(), fresh.height(), "test text is not taller")

        reused.setText(NO_MATCH)
        pin_wrapped_height(reused)
        self.assertEqual(
            reused.height(), fresh.height(), "height pin ratcheted up and never released"
        )


if __name__ == "__main__":
    unittest.main()
