# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for DatabaseAdapter's bulk operations.

The single-word paths cost a cloud round trip each (update_word costs two: the
cloud-newer pre-check plus the upsert), so looping them over a selection froze
the GUI for N × RTT — minutes for a select-all. These collapse the cloud half
into one request, so the assertions here are as much about the *number* of cloud
calls as about the resulting rows.

Run:  python -m unittest tests.test_bulk_ops
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


class BulkOpsTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._cwd = os.getcwd()
        os.chdir(self._tmp.name)
        self.path = os.path.join(self._tmp.name, "d.db")
        db.set_active_db_path(self.path)
        db.initialize_database(self.path)

        self.a = DatabaseAdapter(use_cloud=False)
        self.a.set_local_db(self.path)
        # Enable the cloud path with a recorder standing in for Supabase.
        self.sb = MagicMock()
        self.sb.upsert_words_bulk.side_effect = lambda rows: ([str(r["ID"]) for r in rows], [])
        self.sb.delete_words_bulk.side_effect = lambda ids: (list(ids), [])
        self.sb.add_tags_to_words_bulk.return_value = True
        self.sb.remove_tags_from_words_bulk.return_value = True
        self.a.supabase = self.sb
        self.a.use_cloud = True
        self.a.cloud_available = True

        self.ids = [self._insert(f"w{i}", f"W{i}") for i in range(5)]

    def tearDown(self):
        os.chdir(self._cwd)
        db.set_active_db_path(db.DB_PATH)
        self._tmp.cleanup()

    def _insert(self, word1, word2):
        row = self.a._insert_word_sqlite(
            {"Language1": "en", "Word1": word1, "Language2": "de", "Word2": word2, "Status": "New"}
        )
        return row["ID"]

    def _rows(self):
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        rows = [dict(r) for r in conn.execute("SELECT * FROM words")]
        conn.close()
        return rows

    def _pending(self):
        conn = sqlite3.connect(self.path)
        n = conn.execute("SELECT COUNT(*) FROM sync_queue WHERE synced_at IS NULL").fetchone()[0]
        conn.close()
        return n

    # --- updates ---------------------------------------------------------

    def test_bulk_update_writes_every_row_in_one_request(self):
        updated, failed = self.a.update_words_bulk(self.ids, {"favorite": True})

        self.assertEqual((updated, failed), (5, []))
        self.assertTrue(all(r["favorite"] for r in self._rows()))
        # The whole point: one call, not one per word (and no per-word get_word).
        self.assertEqual(self.sb.upsert_words_bulk.call_count, 1)
        self.sb.get_word.assert_not_called()
        self.sb.upsert_word.assert_not_called()
        self.assertEqual(self._pending(), 0)

    def test_bulk_update_queues_rows_the_push_rejected(self):
        rejected = {self.ids[1], self.ids[3]}
        self.sb.upsert_words_bulk.side_effect = lambda rows: (
            [str(r["ID"]) for r in rows if str(r["ID"]) not in rejected],
            [str(r["ID"]) for r in rows if str(r["ID"]) in rejected],
        )

        updated, failed = self.a.update_words_bulk(self.ids, {"Status": "Learning"})

        self.assertEqual((updated, failed), (5, []))  # all landed locally
        self.assertEqual(self._pending(), 2)  # only the rejected two queued
        self.assertTrue(all(r["Status"] == "Learning" for r in self._rows()))

    def test_bulk_update_queues_everything_when_the_push_raises(self):
        self.sb.upsert_words_bulk.side_effect = RuntimeError("offline")

        updated, _failed = self.a.update_words_bulk(self.ids, {"Status": "Learning"})

        self.assertEqual(updated, 5)
        self.assertEqual(self._pending(), 5)

    def test_bulk_update_queues_everything_when_cloud_is_off(self):
        self.a.use_cloud = False

        self.a.update_words_bulk(self.ids, {"favorite": True})

        self.sb.upsert_words_bulk.assert_not_called()
        self.assertEqual(self._pending(), 5)

    def test_bulk_update_reports_unknown_ids_without_aborting(self):
        # One bad id must not strand the rest — the old loop bailed on the first
        # exception and left the remaining words untouched.
        updated, failed = self.a.update_words_bulk(
            [self.ids[0], "no-such-id", self.ids[1]], {"favorite": True}
        )

        self.assertEqual(updated, 2)
        self.assertEqual(failed, ["no-such-id"])

    def test_bulk_update_of_nothing_is_a_no_op(self):
        self.assertEqual(self.a.update_words_bulk([], {"favorite": True}), (0, []))
        self.sb.upsert_words_bulk.assert_not_called()

    # --- deletes ---------------------------------------------------------

    def test_bulk_delete_removes_rows_and_soft_deletes_once(self):
        deleted, failed = self.a.delete_words_bulk(self.ids[:3])

        self.assertEqual((deleted, failed), (3, []))
        self.assertEqual(len(self._rows()), 2)
        self.assertEqual(self.sb.delete_words_bulk.call_count, 1)
        self.sb.delete_word.assert_not_called()

    def test_bulk_delete_captures_the_bin_snapshot(self):
        self.a.delete_words_bulk([self.ids[0]])

        conn = sqlite3.connect(self.path)
        binned = conn.execute(
            "SELECT record_id FROM bin_items WHERE table_name = 'words'"
        ).fetchall()
        conn.close()
        self.assertEqual([r[0] for r in binned], [self.ids[0]])

    def test_bulk_delete_leaves_deletions_pending_when_the_cloud_fails(self):
        self.sb.delete_words_bulk.side_effect = RuntimeError("offline")

        self.a.delete_words_bulk(self.ids[:2])

        conn = sqlite3.connect(self.path)
        n = conn.execute("SELECT COUNT(*) FROM sync_deletions WHERE synced_at IS NULL").fetchone()[
            0
        ]
        conn.close()
        self.assertEqual(n, 2)

    # --- tags ------------------------------------------------------------

    def test_bulk_tag_links_every_word_in_one_request(self):
        tagged, failed = self.a.add_tag_to_words(self.ids, "animals")

        self.assertEqual((tagged, failed), (5, []))
        conn = sqlite3.connect(self.path)
        n = conn.execute("SELECT COUNT(*) FROM word_tags").fetchone()[0]
        conn.close()
        self.assertEqual(n, 5)
        self.assertEqual(self.sb.add_tags_to_words_bulk.call_count, 1)
        self.sb.add_tag_to_word.assert_not_called()
        # Words are pushed first so the link insert cannot trip a foreign key.
        self.sb.upsert_words_bulk.assert_called_once()

    def test_bulk_untag_unlinks_in_one_request(self):
        self.a.add_tag_to_words(self.ids, "animals")
        self.sb.reset_mock()

        untagged, failed = self.a.remove_tag_from_words(self.ids, "animals")

        self.assertEqual((untagged, failed), (5, []))
        conn = sqlite3.connect(self.path)
        n = conn.execute("SELECT COUNT(*) FROM word_tags").fetchone()[0]
        conn.close()
        self.assertEqual(n, 0)
        self.assertEqual(self.sb.remove_tags_from_words_bulk.call_count, 1)

    def test_untagging_an_unknown_tag_is_a_no_op(self):
        untagged, failed = self.a.remove_tag_from_words(self.ids, "nope")

        self.assertEqual(untagged, 0)
        self.assertEqual(failed, self.ids)
        self.sb.remove_tags_from_words_bulk.assert_not_called()


if __name__ == "__main__":
    unittest.main()
