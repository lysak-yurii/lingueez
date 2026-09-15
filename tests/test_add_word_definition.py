# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Quick Save's folded definition panel and its "Generate on save" switch.

Settings, the database and backups all resolve relative to the cwd, so the
module runs from a temporary directory; cloud write-through is patched off.

Run:  python -m unittest tests.test_add_word_definition
"""

import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtTest import QTest  # noqa: E402
from PySide6.QtWidgets import QApplication  # noqa: E402

from app.config import get_bool, load_settings, save_settings  # noqa: E402
from app.core import ai, auth_manager, db  # noqa: E402
from app.core import definition_autogen as autogen  # noqa: E402
from app.core.database_adapter import DatabaseAdapter  # noqa: E402
from app.ui.dialogs import add_word  # noqa: E402

_app = QApplication.instance() or QApplication([])
_CWD = os.getcwd()
_SANDBOX = None


def setUpModule():
    global _SANDBOX
    _SANDBOX = tempfile.mkdtemp(prefix="lingueez-addword-")
    os.chdir(_SANDBOX)


def tearDownModule():
    os.chdir(_CWD)
    shutil.rmtree(_SANDBOX, ignore_errors=True)


class _DialogCase(unittest.TestCase):
    has_key = False
    switched_on = False

    def setUp(self):
        for path in os.listdir(_SANDBOX):
            full = os.path.join(_SANDBOX, path)
            shutil.rmtree(full) if os.path.isdir(full) else os.remove(full)
        for patcher in (
            mock.patch.object(DatabaseAdapter, "_use_cloud", lambda self: False),
            mock.patch.object(auth_manager, "cloud_backend_active", lambda: False),
            mock.patch.object(ai, "has_api_key", lambda: self.has_key),
        ):
            patcher.start()
            self.addCleanup(patcher.stop)
        db.initialize_database()
        settings = load_settings()
        settings[autogen.ENABLED_KEY] = str(self.switched_on)
        save_settings(settings)
        self.requested = []
        self.dialog = add_word.AddWordDialog(None)
        self.dialog.definition_requested.connect(
            lambda row, word_side, language_side: self.requested.append(
                (row, word_side, language_side)
            )
        )
        self.addCleanup(self.dialog.deleteLater)

    def fill(self, word="haus", translation="house"):
        self.dialog.word1_edit.setText(word)
        self.dialog.word2_edit.setText(translation)

    def open_panel(self):
        self.dialog.toggle_definition_panel()
        QTest.qWait(50)

    def stored(self, word):
        return next(r for r in DatabaseAdapter().get_words() if r["Word1"] == word)


class AtRestTests(_DialogCase):
    def test_folded_and_undotted(self):
        self.assertFalse(self.dialog.definition_panel.isVisible())
        self.assertFalse(self.dialog.definition_btn.has_dot())
        self.assertFalse(self.dialog.is_definition_panel_open())

    def test_opens_and_folds_keeping_the_text(self):
        self.dialog.show()
        folded = self.dialog.height()
        self.open_panel()
        self.assertTrue(self.dialog.definition_panel.isVisible())
        self.assertGreater(self.dialog.height(), folded)
        self.dialog.definition_edit.setPlainText("a building")
        self.dialog.toggle_definition_panel()
        QTest.qWait(50)
        self.assertFalse(self.dialog.definition_panel.isVisible())
        self.assertEqual(self.dialog.height(), folded)
        self.assertEqual(self.dialog.definition_edit.toPlainText(), "a building")


class TypedDefinitionTests(_DialogCase):
    has_key = True
    switched_on = True

    def test_is_saved_with_the_word_and_nothing_is_generated(self):
        self.fill()
        self.open_panel()
        self.dialog.definition_edit.setPlainText("a building people live in")
        self.dialog.save_word()
        row = self.stored("haus")
        self.assertEqual(row["Definition2"], "a building people live in")
        self.assertEqual(self.requested, [])


class NoKeyTests(_DialogCase):
    has_key = False
    switched_on = True

    def test_switch_is_disabled_and_the_setting_turned_off(self):
        self.assertFalse(self.dialog.autogen_switch.isEnabled())
        self.assertFalse(self.dialog.autogen_switch.isChecked())
        self.assertFalse(get_bool(load_settings(), autogen.ENABLED_KEY))
        self.fill()
        self.dialog.save_word()
        self.assertEqual(self.requested, [])


class GenerateOnSaveTests(_DialogCase):
    has_key = True
    switched_on = True

    def test_the_icon_says_it_is_on(self):
        self.assertTrue(self.dialog.autogen_switch.isChecked())
        self.assertTrue(self.dialog.definition_btn.has_dot())

    def test_an_empty_box_asks_for_a_definition_of_the_saved_row(self):
        self.fill()
        self.dialog.save_word()
        self.assertEqual(len(self.requested), 1)
        row, word_side, language_side = self.requested[0]
        self.assertEqual(row["ID"], self.stored("haus")["ID"])
        self.assertEqual((row["Word1"], word_side, language_side), ("haus", "Word1", "Language2"))

    def test_switching_it_off_is_remembered(self):
        self.dialog.autogen_switch.setChecked(False)
        self.assertFalse(self.dialog.definition_btn.has_dot())
        self.assertFalse(get_bool(load_settings(), autogen.ENABLED_KEY))
        self.fill()
        self.dialog.save_word()
        self.assertEqual(self.requested, [])

    def test_a_duplicate_is_not_defined(self):
        self.fill()
        self.dialog.save_word()
        second = add_word.AddWordDialog(None)
        self.addCleanup(second.deleteLater)
        second.definition_requested.connect(lambda *args: self.requested.append(args))
        second.word1_edit.setText("haus")
        second.word2_edit.setText("house")
        with mock.patch.object(add_word.AddWordDialog, "_handle_duplicate") as duplicate:
            second.save_word()
        duplicate.assert_called_once()
        self.assertEqual(len(self.requested), 1)


if __name__ == "__main__":
    unittest.main()
