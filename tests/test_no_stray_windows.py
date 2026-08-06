# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Guard against showing a widget before a layout adopts it.

A parentless QWidget *is* a window. Calling show()/setVisible(True) on one
before it is added to a layout makes Qt create and show a real top-level
window, which is then destroyed the moment the layout reparents it. On Linux
the compositor usually never paints that frame, so it is invisible in
development; on Windows it flashes an empty title-bar-only window bearing the
app icon — the deck preview flashed one per tile with a language tag, so the
mixed-language demo deck of the Flashcards tour strobed ~20 of them.

Run:  python -m unittest tests.test_no_stray_windows
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import QEvent, QObject  # noqa: E402
from PySide6.QtWidgets import QApplication, QWidget  # noqa: E402

from app.ui import theme  # noqa: E402
from app.ui.flashcards_page import _PreviewCard  # noqa: E402

_app = QApplication.instance() or QApplication([])

RECORD = {
    "ID": -1,
    "Word1": "house",
    "Word2": "casa",
    "Status": "Mastered",
    "Language1": "English",
    "Language2": "Spanish",
}


class StrayWindowSpy(QObject):
    """Records every widget shown while it still has no parent."""

    def __init__(self):
        super().__init__()
        self.shown = []

    def eventFilter(self, obj, event):  # noqa: N802
        if (
            event.type() == QEvent.Show
            and isinstance(obj, QWidget)
            and obj.parentWidget() is None
            and obj.isWindow()
        ):
            self.shown.append(obj)
        return False


class PreviewCardWindowTests(unittest.TestCase):
    def build(self, lang_tag):
        spy = StrayWindowSpy()
        _app.installEventFilter(spy)
        try:
            card = _PreviewCard(
                RECORD,
                "a dwelling",
                "New",
                "new",
                theme.current_colors(),
                lambda _rec: None,
                lang_tag=lang_tag,
            )
        finally:
            _app.removeEventFilter(spy)
        return card, spy.shown

    def test_language_tag_does_not_flash_a_window(self):
        card, stray = self.build("EN → ES")
        self.assertEqual(
            [w.metaObject().className() for w in stray],
            [],
            "a child widget was shown before its layout adopted it",
        )
        self.assertTrue(card.lang.isVisible() or card.lang.isVisibleTo(card))
        self.assertEqual(card.lang.text(), "EN → ES")

    def test_no_tag_builds_clean_too(self):
        card, stray = self.build("")
        self.assertEqual([w.metaObject().className() for w in stray], [])
        self.assertFalse(card.lang.isVisibleTo(card))


if __name__ == "__main__":
    unittest.main()
