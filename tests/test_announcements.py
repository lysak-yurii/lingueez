# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Messages from the Lingueez team.

Run:  python -m unittest tests.test_announcements
"""

import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import announcements  # noqa: E402
from app.core.announcements import Announcement, Store, localized  # noqa: E402


def _row(id_, **extra):
    row = {
        "id": id_,
        "severity": "info",
        "placement": "banner",
        "body": {"en": f"body {id_}", "de": f"Text {id_}"},
    }
    row.update(extra)
    return row


class _Rpc:
    def __init__(self, data):
        self.data, self.calls = data, []

    def rpc(self, name, params):
        self.calls.append((name, params))
        return self

    def execute(self):
        return self


class ModelTests(unittest.TestCase):
    def test_reads_a_row(self):
        m = Announcement.from_row(
            _row(
                "a",
                severity="nonsense",
                placement="dialog",
                dismissible=False,
                body={"en": " hi ", "de": ""},
            )
        )
        self.assertEqual(m.severity, "info")
        self.assertTrue(m.dialog)
        self.assertFalse(m.dismissible)
        self.assertEqual(m.body, {"en": "hi"})

    def test_only_https_links_open(self):
        self.assertIsNotNone(
            Announcement.from_row(_row("a", action_url="https://lingueez.app")).link
        )
        self.assertIsNone(Announcement.from_row(_row("a", action_url="http://lingueez.app")).link)
        self.assertIsNone(Announcement.from_row(_row("a", action_url="javascript:x")).link)

    def test_localized_falls_back_to_the_language_then_english(self):
        texts = {"en": "Hello", "pt": "Olá", "pt-BR": "Oi"}
        self.assertEqual(localized(texts, "pt_BR"), "Oi")
        self.assertEqual(localized(texts, "pt"), "Olá")
        self.assertEqual(localized(texts, "de"), "Hello")
        self.assertEqual(localized({"fr": "Salut"}, "de"), "Salut")
        self.assertIsNone(localized({}, "de"))

    def test_fetch_asks_as_this_app(self):
        client = _Rpc([_row("a"), _row("empty", body={})])
        with mock.patch.object(announcements, "audience", return_value="signed_in"):
            got = announcements.fetch("2.2.0", client=client)
        self.assertEqual([m.id for m in got], ["a"])
        self.assertEqual(
            client.calls,
            [
                (
                    "active_messages",
                    {"p_platform": "desktop", "p_version": "2.2.0", "p_audience": "signed_in"},
                )
            ],
        )


class StoreTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self._tmp.name, "a.json")

    def tearDown(self):
        self._tmp.cleanup()

    def _messages(self):
        return [
            Announcement.from_row(r)
            for r in (
                _row("a"),
                _row("b", placement="dialog"),
                _row("c", placement="dialog", dismissible=False),
            )
        ]

    def test_a_closed_message_stays_closed_after_a_relaunch(self):
        store = Store(self.path)
        store.update(self._messages())
        store.dismiss(store.banners()[0])
        store.dismiss(store.dialogs()[0])
        again = Store(self.path)
        self.assertEqual(again.banners(), [])
        self.assertEqual([m.id for m in again.dialogs()], ["c"])

    def test_one_that_is_not_dismissible_cant_be_closed_for_good(self):
        store = Store(self.path)
        store.update(self._messages())
        store.dismiss(store.dialogs()[1])
        self.assertIn("c", [m.id for m in Store(self.path).dialogs()])

    def test_offline_the_last_messages_stay(self):
        Store(self.path).update(self._messages())
        self.assertEqual([m.id for m in Store(self.path).banners()], ["a"])

    def test_closings_of_messages_that_are_gone_are_forgotten(self):
        store = Store(self.path)
        store.update(self._messages())
        store.dismiss(store.banners()[0])
        store.update(self._messages()[1:])
        self.assertEqual(store.dismissed, set())


class BarTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from PySide6.QtWidgets import QApplication

        cls.app = QApplication.instance() or QApplication([])

    def test_shows_two_at_a_time_and_hides_when_empty(self):
        from app.ui import theme
        from app.ui.announcements_bar import AnnouncementBanner, AnnouncementsBar

        bar = AnnouncementsBar(theme.LIGHT)
        bar.set_messages([Announcement.from_row(_row(i)) for i in "abc"])
        self.app.processEvents()
        self.assertEqual(len(bar.findChildren(AnnouncementBanner)), 2)
        self.assertFalse(bar.isHidden())
        bar.set_messages([])
        self.app.processEvents()
        self.assertTrue(bar.isHidden())

    def test_a_banner_that_is_not_dismissible_has_no_close_button(self):
        from PySide6.QtWidgets import QPushButton
        from app.ui import theme
        from app.ui.announcements_bar import AnnouncementBanner

        closable = AnnouncementBanner(Announcement.from_row(_row("a")), theme.DARK)
        fixed = AnnouncementBanner(Announcement.from_row(_row("b", dismissible=False)), theme.DARK)
        self.assertEqual(len(closable.findChildren(QPushButton)), 1)
        self.assertEqual(len(fixed.findChildren(QPushButton)), 0)


if __name__ == "__main__":
    unittest.main()
