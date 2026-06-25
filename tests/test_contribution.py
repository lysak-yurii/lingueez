# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Tests for the non-destructive 'add local words to account' contribution flow.

Covers SyncManager.local_only_delta (content diff of the logged-out dictionary.db
vs the active account DB) and contribute_local_items (additive copy-up that leaves
the local store untouched and is idempotent).

Run:  python -m unittest tests.test_contribution
"""

import hashlib
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import db  # noqa: E402
from app.core.database_adapter import DatabaseAdapter  # noqa: E402
from app.core.sync_manager import SyncManager  # noqa: E402


def _adapter(path):
    a = DatabaseAdapter(use_cloud=False)
    a.set_local_db(path)
    return a


def _md5(path):
    with open(path, "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()


class ContributionTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._cwd = os.getcwd()
        os.chdir(self._tmp.name)
        # Local-only store == db.DB_PATH ('dictionary.db'), as the real app uses.
        db.initialize_database(db.DB_PATH)
        self.acct = "dictionary_acc.db"
        db.initialize_database(self.acct)

        # Local store: cat (tagged + definition + favorite), dog (shared), one text.
        self.local = _adapter(db.DB_PATH)
        cat = self.local.insert_word(
            {
                "Language1": "en",
                "Word1": "cat",
                "Language2": "de",
                "Word2": "Katze",
                "Status": "New",
            }
        )
        self.local.update_word(cat["ID"], {"Definition": "a feline", "favorite": 1})
        self.local.add_tag_to_word(cat["ID"], "animals")
        self.local.insert_word(
            {"Language1": "en", "Word1": "dog", "Language2": "de", "Word2": "Hund", "Status": "New"}
        )
        self.local.insert_text({"Title": "Local text", "Text": "hello", "Language": "en"})

        # Account already has 'dog' and a different text.
        self.account = _adapter(self.acct)
        self.account.insert_word(
            {"Language1": "en", "Word1": "dog", "Language2": "de", "Word2": "Hund", "Status": "New"}
        )
        self.account.insert_text({"Title": "Account text", "Text": "other", "Language": "en"})

        # SyncManager pointed at the account DB (cloud-off queue adapter).
        self.sm = SyncManager.__new__(SyncManager)
        self.sm.local_db = self.acct
        self.sm.db_adapter = _adapter(self.acct)

    def tearDown(self):
        os.chdir(self._cwd)
        db.set_active_db_path(db.DB_PATH)
        self._tmp.cleanup()

    def test_delta_finds_only_non_shared_items_with_tags(self):
        delta = self.sm.local_only_delta()
        words = delta["words"]
        self.assertEqual([w["Word1"] for w in words], ["cat"])  # 'dog' excluded (shared)
        self.assertEqual(words[0]["_tags"], ["animals"])
        self.assertEqual(words[0]["Definition"], "a feline")
        self.assertEqual(
            [t["Title"] for t in delta["texts"]], ["Local text"]
        )  # by (Title,Text,Language)

    def test_delta_empty_when_logged_out(self):
        # Active DB IS the local-only store → nothing to contribute.
        self.sm.local_db = db.DB_PATH
        self.sm.db_adapter = _adapter(db.DB_PATH)
        self.assertEqual(self.sm.local_only_delta(), {"words": [], "texts": []})

    def test_contribute_is_additive_and_preserves_fidelity(self):
        delta = self.sm.local_only_delta()
        added, failed = self.sm.contribute_local_items(delta["words"], delta["texts"], self.account)
        self.assertEqual((added, failed), (2, 0))

        words = {w["Word1"]: w for w in self.account.get_words()}
        self.assertIn("cat", words)
        self.assertEqual(words["cat"]["Definition"], "a feline")
        self.assertTrue(words["cat"]["favorite"])
        self.assertEqual(
            [t["tag_name"] for t in self.account.get_word_tags(words["cat"]["ID"])], ["animals"]
        )
        self.assertTrue(any(t["Title"] == "Local text" for t in self.account.get_texts()))
        # 'dog' not duplicated.
        self.assertEqual(sum(1 for w in self.account.get_words() if w["Word1"] == "dog"), 1)

    def test_source_store_untouched(self):
        before = _md5(db.DB_PATH)
        delta = self.sm.local_only_delta()
        self.sm.contribute_local_items(delta["words"], delta["texts"], self.account)
        self.assertEqual(_md5(db.DB_PATH), before, "local dictionary.db must not change")

    def test_idempotent(self):
        delta = self.sm.local_only_delta()
        self.sm.contribute_local_items(delta["words"], delta["texts"], self.account)
        # Second pass: nothing left to add.
        self.assertEqual(self.sm.local_only_delta(), {"words": [], "texts": []})
        added, failed = self.sm.contribute_local_items([], [], self.account)
        self.assertEqual((added, failed), (0, 0))

    def test_partial_selection(self):
        delta = self.sm.local_only_delta()
        # Contribute only the texts, not the words.
        added, _ = self.sm.contribute_local_items([], delta["texts"], self.account)
        self.assertEqual(added, 1)
        self.assertNotIn("cat", {w["Word1"] for w in self.account.get_words()})
        # cat is still offered next time.
        self.assertEqual([w["Word1"] for w in self.sm.local_only_delta()["words"]], ["cat"])


class SuppressFlagTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        from app.core.accounts import AccountRegistry

        self.reg = AccountRegistry(data_dir=self._tmp.name)
        self.reg.upsert("uid-1", "a@example.com")

    def tearDown(self):
        self._tmp.cleanup()

    def test_suppress_round_trip(self):
        self.assertFalse(self.reg.contribution_suppressed("uid-1"))
        self.reg.set_contribution_suppressed("uid-1", True)
        self.assertTrue(self.reg.contribution_suppressed("uid-1"))
        self.reg.set_contribution_suppressed("uid-1", False)
        self.assertFalse(self.reg.contribution_suppressed("uid-1"))

    def test_unknown_uid_is_false(self):
        self.assertFalse(self.reg.contribution_suppressed("nope"))


if __name__ == "__main__":
    unittest.main()
