# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for word_tags reconciliation in SyncManager._sync_tags_incremental.

word_tags has no cloud-side timestamp, so "absent from the cloud" is ambiguous:
the link was either created locally and not yet pushed, or deleted on another
device. The engine used to act on both readings at once — deleting a local link
and pushing that same link in the same run — which made offline tagging lose the
tag until a later sync, and turned a failed get_all_word_tags() (it returns []
on any error) into a wipe of every local link.

The local-only ``synced`` flag disambiguates: 0 = local addition, push it;
1 = previously seen in the cloud, so its absence is a genuine remote removal.

Run:  python -m unittest tests.test_tag_link_sync
"""

import os
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import db  # noqa: E402
from app.core.database_adapter import DatabaseAdapter  # noqa: E402
from app.core.sync_manager import SyncManager  # noqa: E402

TAG = "t1"


class TagLinkSyncTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._cwd = os.getcwd()
        os.chdir(self._tmp.name)
        self.path = os.path.join(self._tmp.name, "d.db")
        db.set_active_db_path(self.path)
        db.initialize_database(self.path)

        conn = sqlite3.connect(self.path)
        for i in range(3):
            conn.execute(
                "INSERT INTO words (ID, Word1, Word2) VALUES (?, ?, ?)",
                (f"w{i}", f"cat{i}", f"Katze{i}"),
            )
        conn.execute("INSERT INTO tags (tag_id, tag_name) VALUES (?, 'animals')", (TAG,))
        conn.commit()
        conn.close()

        self.sm = SyncManager.__new__(SyncManager)
        self.sm.local_db = self.path
        self.sm.supabase = MagicMock()
        self.sm.db_adapter = DatabaseAdapter(use_cloud=False)
        self.sm.db_adapter.set_local_db(self.path)
        self.sm.supabase.get_tags.return_value = [{"tag_id": TAG, "tag_name": "animals"}]
        self.sm.supabase.add_tags_to_words_bulk.return_value = True

    def tearDown(self):
        os.chdir(self._cwd)
        db.set_active_db_path(db.DB_PATH)
        self._tmp.cleanup()

    def _link(self, word_id, synced):
        conn = sqlite3.connect(self.path)
        conn.execute(
            "INSERT OR REPLACE INTO word_tags (word_id, tag_id, synced) VALUES (?, ?, ?)",
            (word_id, TAG, 1 if synced else 0),
        )
        conn.commit()
        conn.close()

    def _links(self):
        conn = sqlite3.connect(self.path)
        rows = {r[0]: r[1] for r in conn.execute("SELECT word_id, synced FROM word_tags")}
        conn.close()
        return rows

    def _cloud(self, *word_ids):
        self.sm.supabase.get_all_word_tags.return_value = [
            {"word_id": w, "tag_id": TAG} for w in word_ids
        ]

    # --- the regression --------------------------------------------------

    def test_unsynced_link_is_pushed_not_deleted(self):
        # Tagged locally (offline); the cloud legitimately reports other links.
        self._link("w0", synced=False)
        self._cloud("w1")

        self.sm._sync_tags_incremental(None)

        links = self._links()
        self.assertIn("w0", links, "a local-only link must survive the sync")
        self.assertEqual(links["w0"], 1, "and be marked synced once pushed")
        self.sm.supabase.add_tags_to_words_bulk.assert_called_once_with([("w0", TAG)])

    def test_unsynced_link_survives_a_failed_push(self):
        self._link("w0", synced=False)
        self._cloud("w1")
        self.sm.supabase.add_tags_to_words_bulk.return_value = False

        self.sm._sync_tags_incremental(None)

        links = self._links()
        self.assertIn("w0", links, "a link must never be dropped before it reaches the cloud")
        self.assertEqual(links["w0"], 0, "still unsynced, so the next sync retries it")

    def test_empty_cloud_response_does_not_wipe_local_links(self):
        # get_all_word_tags() returns [] on any error; that must not read as
        # "the cloud has no links, delete them all".
        for i in range(3):
            self._link(f"w{i}", synced=True)
        self._cloud()  # empty

        self.sm._sync_tags_incremental(None)

        self.assertEqual(len(self._links()), 3)

    # --- removals still propagate ----------------------------------------

    def test_synced_link_missing_from_cloud_is_removed(self):
        self._link("w0", synced=True)  # previously in the cloud
        self._link("w1", synced=True)
        self._cloud("w1")  # w0 was untagged on another device

        self.sm._sync_tags_incremental(None)

        self.assertEqual(set(self._links()), {"w1"})

    def test_cloud_links_are_pulled_in_as_synced(self):
        self._cloud("w2")

        self.sm._sync_tags_incremental(None)

        self.assertEqual(self._links(), {"w2": 1})

    def test_link_present_on_both_sides_is_marked_synced(self):
        self._link("w0", synced=False)  # e.g. pushed but never flagged
        self._cloud("w0")

        self.sm._sync_tags_incremental(None)

        self.assertEqual(self._links(), {"w0": 1})
        self.sm.supabase.add_tags_to_words_bulk.assert_not_called()

    def test_migrated_links_are_pushed_rather_than_dropped(self):
        # Rows that predate the synced column default to 0, so the first sync
        # after the migration pushes them instead of deleting them.
        conn = sqlite3.connect(self.path)
        for i in range(3):
            conn.execute("INSERT INTO word_tags (word_id, tag_id) VALUES (?, ?)", (f"w{i}", TAG))
        conn.commit()
        conn.close()
        self._cloud("w0")  # cloud only knows one of them

        self.sm._sync_tags_incremental(None)

        self.assertEqual(len(self._links()), 3)
        self.assertTrue(all(v == 1 for v in self._links().values()))


class TagLinkSchemaTests(unittest.TestCase):
    def test_synced_column_is_added_to_pre_existing_databases(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "old.db")
            conn = sqlite3.connect(path)
            conn.execute(
                "CREATE TABLE word_tags (word_id TEXT NOT NULL, "
                "tag_id TEXT NOT NULL, PRIMARY KEY (word_id, tag_id))"
            )
            conn.execute("INSERT INTO word_tags VALUES ('w0', 't1')")
            conn.commit()
            conn.close()

            db.initialize_database(path)

            conn = sqlite3.connect(path)
            cols = {r[1] for r in conn.execute("PRAGMA table_info(word_tags)")}
            synced = conn.execute("SELECT synced FROM word_tags WHERE word_id = 'w0'").fetchone()[0]
            conn.close()
            self.assertIn("synced", cols)
            self.assertEqual(synced, 0, "existing links migrate in as unsynced")


if __name__ == "__main__":
    unittest.main()
