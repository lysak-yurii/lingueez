# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for SyncManager._sync_operation_queue (the local -> cloud channel).

On the incremental sync path the queue is the *only* way a local word or text
edit reaches the cloud (the full content union runs on first sync and on a manual
reconcile). So the drain must push what the row says now, not the snapshot taken
when the operation was queued — replaying a stale snapshot silently reverts any
edit made after queueing, and the count-only _validate_sync never notices.

Run:  python -m unittest tests.test_sync_queue_drain
"""

import os
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import db  # noqa: E402
from app.core.sync_manager import SyncManager  # noqa: E402


def _op(queue_id, op_type, table, record_id, data=None):
    return {
        "id": queue_id,
        "operation_type": op_type,
        "table_name": table,
        "record_id": record_id,
        "operation_data": data,
        "created_at": "2026-01-01T00:00:00",
    }


class SyncOperationQueueTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self._tmp.name, "d.db")
        db.initialize_database(self.path)

        self.sm = SyncManager.__new__(SyncManager)
        self.sm.local_db = self.path
        self.sm.supabase = MagicMock()
        self.sm.db_adapter = MagicMock()
        self.sm.supabase.upsert_word.side_effect = lambda w: {"ID": w["ID"]}
        self.sm.supabase.upsert_text.side_effect = lambda t: {"ID": t["ID"]}

    def tearDown(self):
        self._tmp.cleanup()

    def _insert_word(self, wid="w1", word1="cat", word2="Katze", status="New"):
        conn = sqlite3.connect(self.path)
        conn.execute(
            "INSERT INTO words (ID, Language1, Word1, Language2, Word2, Status) "
            "VALUES (?, 'en', ?, 'de', ?, ?)", (wid, word1, word2, status))
        conn.commit()
        conn.close()

    def _pushed_word(self):
        self.assertEqual(self.sm.supabase.upsert_word.call_count, 1)
        return self.sm.supabase.upsert_word.call_args[0][0]

    def test_pushes_the_current_row_not_the_queued_snapshot(self):
        # The regression: a word queued while offline, then edited once the write
        # -through worked again. Replaying the snapshot would push "Katze"/New
        # over the newer cloud row.
        self._insert_word(word2="Katze (edited)", status="Learning")
        stale = {"ID": "w1", "Language1": "en", "Word1": "cat",
                 "Language2": "de", "Word2": "Katze", "Status": "New"}

        self.sm._sync_operation_queue([_op(1, "INSERT", "words", "w1", stale)])

        payload = self._pushed_word()
        self.assertEqual(payload["Word2"], "Katze (edited)")
        self.assertEqual(payload["Status"], "Learning")
        self.sm.db_adapter._mark_operation_synced.assert_called_once_with(1)

    def test_falls_back_to_the_snapshot_when_the_row_is_gone(self):
        stale = {"ID": "gone", "Language1": "en", "Word1": "cat",
                 "Language2": "de", "Word2": "Katze"}

        self.sm._sync_operation_queue([_op(1, "INSERT", "words", "gone", stale)])

        self.assertEqual(self._pushed_word()["Word1"], "cat")
        self.sm.db_adapter._mark_operation_synced.assert_called_once_with(1)

    def test_operation_with_neither_row_nor_snapshot_is_dropped(self):
        # Nothing left to push: the operation must not be retried on every sync
        # forever (it would sit in the queue and in the 'Pending' badge).
        self.sm._sync_operation_queue([_op(1, "UPDATE", "words", "gone", None)])

        self.sm.supabase.upsert_word.assert_not_called()
        self.sm.db_adapter._mark_operation_synced.assert_called_once_with(1)

    def test_content_collision_rekeys_the_local_row(self):
        self._insert_word(wid="local-id")
        self.sm.supabase.upsert_word.side_effect = lambda w: {"ID": "cloud-id"}

        self.sm._sync_operation_queue([_op(1, "INSERT", "words", "local-id", None)])

        self.sm.db_adapter._rekey_word_sqlite.assert_called_once_with(
            "local-id", "cloud-id")
        self.sm.db_adapter._mark_operation_synced.assert_called_once_with(1)

    def test_texts_are_pushed_from_the_current_row(self):
        conn = sqlite3.connect(self.path)
        conn.execute("INSERT INTO texts (ID, Title, Text, Language) "
                     "VALUES ('t1', 'New title', 'body', 'en')")
        conn.commit()
        conn.close()

        self.sm._sync_operation_queue(
            [_op(1, "INSERT", "texts", "t1", {"ID": "t1", "Title": "Old title"})])

        self.assertEqual(
            self.sm.supabase.upsert_text.call_args[0][0]["Title"], "New title")

    def test_word_tags_operation_is_cleared_not_stranded(self):
        # _sync_tags_incremental reconciles link rows wholesale; this drain has no
        # way to push one, so leaving it unsynced would strand it permanently.
        self.sm._sync_operation_queue(
            [_op(1, "INSERT", "word_tags", "w1", {"tag_id": "t-1"})])

        self.sm.db_adapter._mark_operation_synced.assert_called_once_with(1)

    def test_failed_push_stays_queued(self):
        self._insert_word()
        self.sm.supabase.upsert_word.side_effect = lambda w: None

        self.sm._sync_operation_queue([_op(1, "INSERT", "words", "w1", None)])

        self.sm.db_adapter._mark_operation_synced.assert_not_called()

    def test_restore_and_hard_delete_still_dispatch(self):
        self.sm.supabase.restore_word.return_value = True
        self.sm.supabase.hard_delete_text.return_value = True

        self.sm._sync_operation_queue([
            _op(1, "RESTORE", "words", "w1", None),
            _op(2, "HARD_DELETE", "texts", "t1", None),
        ])

        self.sm.supabase.restore_word.assert_called_once_with("w1")
        self.sm.supabase.hard_delete_text.assert_called_once_with("t1")
        self.assertEqual(self.sm.db_adapter._mark_operation_synced.call_count, 2)


if __name__ == "__main__":
    unittest.main()
