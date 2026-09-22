# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for related-word detection (app.core.related).

Run:  python -m unittest tests.test_related
"""

import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication  # noqa: E402

from app.core import related as r  # noqa: E402
from app.ui import theme  # noqa: E402
from app.ui.flashcards_page import FlashcardWidget  # noqa: E402
from app.ui.widgets import RelatedWordsLabel  # noqa: E402

_app = QApplication.instance() or QApplication([])


def word(wid, w1, w2="", l1="English", l2="German"):
    return {"ID": wid, "Word1": w1, "Word2": w2, "Language1": l1, "Language2": l2}


class KeyTests(unittest.TestCase):
    def test_translation_keys_split_and_strip(self):
        self.assertEqual(r.translation_keys("бігом (поспішно), біг"), {"бігом", "біг"})
        self.assertEqual(r.translation_keys("to run; the Run"), {"run"})

    def test_fold_drops_accents(self):
        self.assertEqual(r.fold("Καλός"), r.fold("καλος"))

    def test_is_headword(self):
        self.assertTrue(r.is_headword("τρέχω / έτρεξα"))
        self.assertTrue(r.is_headword("further (furthermore)"))
        self.assertFalse(r.is_headword("What is your name, please?"))
        self.assertFalse(r.is_headword("τρέχω σαν παλαβός"))

    def test_root_key(self):
        self.assertEqual(r.root_key("Information"), "inform")
        self.assertEqual(r.root_key("rag"), "=rag")
        self.assertIsNone(r.root_key("take off"))


class BuildRelatedTests(unittest.TestCase):
    def test_shared_translation_in_the_same_target_language(self):
        rel = r.build_related(
            [
                word("a", "glücklich", "happy", l1="German", l2="English"),
                word("b", "fröhlich", "cheerful, happy", l1="German", l2="English"),
                word("c", "felice", "happy", l1="Italian", l2="Spanish"),
            ]
        )
        self.assertEqual(rel["a"]["translation"], ["b"])
        self.assertEqual(rel["b"]["translation"], ["a"])
        self.assertNotIn("c", rel)

    def test_root_needs_most_of_the_shorter_word(self):
        rel = r.build_related(
            [
                word("a", "Anstand", l1="German"),
                word("b", "Anstandsdame", l1="German"),
                word("c", "verschleiern", l1="German"),
                word("d", "verscherbeln", l1="German"),
            ]
        )
        self.assertEqual(
            rel, {"a": {"translation": [], "root": ["b"]}, "b": {"translation": [], "root": ["a"]}}
        )

    def test_root_ignores_other_languages(self):
        rel = r.build_related(
            [word("a", "gorgeous", l1="English"), word("b", "gorgeous", l1="French")]
        )
        self.assertEqual(rel, {})

    def test_both_relations_list_the_word_once(self):
        rel = r.build_related([word("a", "friend", "Freund"), word("b", "friendly", "Freund")])
        self.assertEqual(rel["a"], {"translation": ["b"], "root": []})

    def test_oversized_group_is_dropped(self):
        rel = r.build_related([word(str(i), f"w{i}", "same") for i in range(r.MAX_GROUP + 1)])
        self.assertEqual(rel, {})

    def test_duplicate_ids_are_not_self_links(self):
        rel = r.build_related([word("a", "friend", "Freund"), word("a", "friend", "Freund")])
        self.assertEqual(rel, {})


@unittest.skipIf(r.snowballstemmer is None, "snowballstemmer not installed")
class StemTests(unittest.TestCase):
    def test_word_links_to_the_phrases_that_use_it(self):
        rel = r.build_related(
            [
                word("a", "χαλαρά", l1="Greek"),
                word("b", "Δείξε χαλαρός", l1="Greek"),
                word("c", "ο χαλαρός τρόπος ζωής", l1="Greek"),
            ]
        )
        self.assertEqual(sorted(rel["a"]["root"]), ["b", "c"])
        self.assertNotIn("c", rel["b"]["root"])  # two phrases sharing a word

    def test_forms_listed_together_count_as_one_word(self):
        rel = r.build_related(
            [
                word("a", "τρέχω / έτρεξα", l1="Greek"),
                word("b", "τρέχω σαν παλαβός", l1="Greek"),
                word("c", "μου τρέχει η μύτη", l1="Greek"),
            ]
        )
        self.assertEqual(sorted(rel["a"]["root"]), ["b", "c"])

    def test_notes_in_parentheses_are_not_stemmed(self):
        rel = r.build_related([word("a", "when (not as a question)"), word("b", "question")])
        self.assertEqual(rel, {})

    def test_different_stems_stay_apart(self):
        rel = r.build_related(
            [word("a", "άριστα", l1="Greek"), word("b", "στρίβει αριστερά", l1="Greek")]
        )
        self.assertEqual(rel, {})

    def test_without_the_stemmer_only_the_prefix_rule_applies(self):
        words = [word("a", "χαλαρά", l1="Greek"), word("b", "Δείξε χαλαρός", l1="Greek")]
        with mock.patch.object(r, "snowballstemmer", None):
            self.assertEqual(r.build_related(words), {})


class RelatedSettingTests(unittest.TestCase):
    def _window(self, enabled):
        from app.ui.main_window import MainWindow

        win = MainWindow.__new__(MainWindow)  # no Qt init: pure logic
        win.settings = {"flashcards_related_words": str(enabled)}
        win._related = {"a": {"translation": ["b"], "root": []}}
        win._related_records = {"b": {"ID": "b", "Word1": "fröhlich"}}
        return win

    def test_on_by_default_lists_the_group(self):
        win = self._window(True)
        self.assertEqual(
            win._related_for("a"), [("translation", [{"ID": "b", "Word1": "fröhlich"}])]
        )

    def test_turned_off_shows_nothing(self):
        self.assertEqual(self._window(False)._related_for("a"), [])


class FlashcardRelatedLineTests(unittest.TestCase):
    def setUp(self):
        self.card = FlashcardWidget(theme.current_colors())
        self.card.set_card(word("a", "glücklich", "happy"))
        self.card.set_related(
            [
                (
                    "translation",
                    [{"ID": "b", "Word1": "fröhlich", "Word2": "happy", "Status": "New"}],
                )
            ]
        )

    def test_shown_on_the_back_only(self):
        self.assertTrue(self.card.related.isHidden())
        self.card.flip(animate=False)
        self.assertFalse(self.card.related.isHidden())
        self.assertIn("fröhlich", self.card.related.text())

    def test_next_card_clears_the_line(self):
        self.card.set_card(word("c", "Anstand"))
        self.card.flip(animate=False)
        self.assertTrue(self.card.related.isHidden())

    def test_word_text_is_escaped(self):
        self.card.set_related([("root", [{"ID": "x", "Word1": "<b>bold</b>"}])])
        self.assertIn("&lt;b&gt;bold", self.card.related.text())


class RelatedWordsLabelTests(unittest.TestCase):
    RECORD = {"ID": "3f2c-secret-id", "Word1": "fröhlich", "Word2": "happy", "Status": "New"}

    def test_links_never_carry_the_word_id(self):
        label = RelatedWordsLabel()
        label.set_groups([("translation", [self.RECORD])])
        self.assertNotIn("3f2c-secret-id", label.text())
        self.assertIn("fröhlich", label.text())

    def test_click_reports_the_record_only_when_clickable(self):
        for clickable, expected in ((True, [self.RECORD]), (False, [])):
            label = RelatedWordsLabel(clickable=clickable)
            label.set_groups([("translation", [self.RECORD])])
            seen = []
            label.word_clicked.connect(seen.append)
            label.linkActivated.emit("w0")
            self.assertEqual(seen, expected)

    def test_menu_offers_jump_only_when_jumpable(self):
        for jumpable, expected in ((True, ["Jump to word", "Copy"]), (False, ["Copy"])):
            label = RelatedWordsLabel(jumpable=jumpable)
            menu = label.menu_for(self.RECORD)
            self.assertEqual([a.text() for a in menu.actions()], expected)

    def test_jump_and_copy_act_on_the_word(self):
        label = RelatedWordsLabel(jumpable=True)
        jumped = []
        label.jump_requested.connect(jumped.append)
        jump, copy = label.menu_for(self.RECORD).actions()
        jump.trigger()
        copy.trigger()
        self.assertEqual(jumped, [self.RECORD])
        self.assertEqual(QApplication.clipboard().text(), "fröhlich")


class FlashcardRelatedClickTests(unittest.TestCase):
    def test_clicking_a_related_word_does_not_flip_the_card(self):
        from PySide6.QtCore import QPoint, Qt
        from PySide6.QtTest import QTest

        card = FlashcardWidget(theme.current_colors())
        card.resize(420, 340)
        flips = []
        card.clicked.connect(lambda: flips.append(1))
        QTest.mouseClick(card, Qt.LeftButton, pos=QPoint(20, 300))
        self.assertEqual(flips, [1])
        card.related._hovered = "w0"  # the mouse is over a related word
        QTest.mouseClick(card, Qt.LeftButton, pos=QPoint(20, 300))
        self.assertEqual(flips, [1])


class DefinitionDialogRelatedTests(unittest.TestCase):
    def _dialog(self, groups):
        from app.ui.dialogs.definition import DefinitionDialog

        adapter = mock.Mock()
        adapter.get_word.return_value = {"ID": "a", "Word1": "glücklich", "Word2": "happy"}
        return DefinitionDialog(
            None, {"ID": "a", "Word1": "glücklich"}, adapter, lambda _id: groups
        )

    def test_shows_the_related_row(self):
        dialog = self._dialog([("translation", [RelatedWordsLabelTests.RECORD])])
        self.assertFalse(dialog.related.parentWidget().isHidden())

    def test_hides_the_row_without_related_words(self):
        dialog = self._dialog([])
        self.assertTrue(dialog.related.parentWidget().isHidden())


if __name__ == "__main__":
    unittest.main()
