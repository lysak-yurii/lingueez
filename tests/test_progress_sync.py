# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Cross-device learning-progress sync (word_progress).

Covers the PROGRESS-MERGE rule (counters by max, scheduling as a group from
the newer updated_at), the local dirty tracking that feeds the push, the
listen-count backfill migration, srs rows following a word re-key, and
SyncManager._sync_word_progress's pull-merge-push against a mocked cloud.

Run:  python -m unittest tests.test_progress_sync
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


def _row(word_id="w1", **overrides):
    base = {
        "word_id": word_id,
        "ease_factor": 2.5,
        "interval_days": 1,
        "next_review": None,
        "last_reviewed": None,
        "review_count": 0,
        "correct_count": 0,
        "listen_count": 0,
        "updated_at": "2026-07-01 10:00:00",
    }
    base.update(overrides)
    return base


class MergeRuleTests(unittest.TestCase):
    def test_one_side_missing_takes_other(self):
        cloud = _row(listen_count=7)
        self.assertEqual(db.merge_progress_rows(None, cloud)["listen_count"], 7)
        self.assertEqual(db.merge_progress_rows(cloud, None)["listen_count"], 7)
        self.assertIsNone(db.merge_progress_rows(None, None))

    def test_counters_take_max_of_both_sides(self):
        # Two devices listened offline: neither side's count may regress.
        local = _row(
            listen_count=12, review_count=3, correct_count=2, updated_at="2026-07-02 09:00:00"
        )
        cloud = _row(
            listen_count=9, review_count=5, correct_count=1, updated_at="2026-07-02 08:00:00"
        )
        merged = db.merge_progress_rows(local, cloud)
        self.assertEqual(merged["listen_count"], 12)
        self.assertEqual(merged["review_count"], 5)
        self.assertEqual(merged["correct_count"], 2)

    def test_scheduling_travels_as_group_from_newer_side(self):
        local = _row(
            ease_factor=1.8,
            interval_days=4,
            next_review="2026-07-10T00:00:00",
            updated_at="2026-07-03 12:00:00",
        )
        cloud = _row(
            ease_factor=2.3,
            interval_days=9,
            next_review="2026-07-20T00:00:00",
            updated_at="2026-07-01 12:00:00",
        )
        merged = db.merge_progress_rows(local, cloud)
        # Local is newer: its whole scheduling group wins (no field mixing).
        self.assertEqual(merged["ease_factor"], 1.8)
        self.assertEqual(merged["interval_days"], 4)
        self.assertEqual(merged["next_review"], "2026-07-10T00:00:00")

    def test_tie_prefers_second_argument(self):
        # Deterministic tie-break: callers pass the preferred (cloud) side as b.
        stamp = "2026-07-03 12:00:00"
        local = _row(ease_factor=1.5, updated_at=stamp)
        cloud = _row(ease_factor=2.2, updated_at=stamp)
        self.assertEqual(db.merge_progress_rows(local, cloud)["ease_factor"], 2.2)

    def test_reinstall_cannot_erase_cloud_progress(self):
        # A wiped device has a fresh row with zeros but a newer stamp: counters
        # must survive from the cloud even though scheduling follows the newer row.
        fresh = _row(listen_count=0, review_count=0, updated_at="2026-07-05 10:00:00")
        cloud = _row(listen_count=40, review_count=6, updated_at="2026-07-01 10:00:00")
        merged = db.merge_progress_rows(fresh, cloud)
        self.assertEqual(merged["listen_count"], 40)
        self.assertEqual(merged["review_count"], 6)

    def test_mixed_timestamp_formats_compare(self):
        # SQLite CURRENT_TIMESTAMP (naive UTC) vs Postgres ISO with offset.
        local = _row(ease_factor=1.5, updated_at="2026-07-02 10:00:00")
        cloud = _row(ease_factor=2.2, updated_at="2026-07-02T11:30:00+00:00")
        self.assertEqual(db.merge_progress_rows(local, cloud)["ease_factor"], 2.2)


class LocalStoreTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._cwd = os.getcwd()
        os.chdir(self._tmp.name)
        self.path = os.path.join(self._tmp.name, "d.db")
        db.set_active_db_path(self.path)
        db.initialize_database(self.path)

    def tearDown(self):
        os.chdir(self._cwd)
        db.set_active_db_path(db.DB_PATH)
        self._tmp.cleanup()

    def test_log_review_increments_listen_count_and_marks_dirty(self):
        db.log_review("w1", db_path=self.path)
        db.log_review("w1", db_path=self.path)
        self.assertEqual(db.get_listen_count("w1", db_path=self.path), 2)
        dirty = db.srs_get_dirty(self.path)
        self.assertEqual([r["word_id"] for r in dirty], ["w1"])

    def test_log_review_preserves_srs_fields(self):
        db.srs_upsert(
            "w1",
            {
                "ease_factor": 1.9,
                "interval_days": 6,
                "next_review": "2026-07-20T00:00:00",
                "review_count": 4,
                "correct_count": 3,
            },
            db_path=self.path,
        )
        db.log_review("w1", db_path=self.path)
        row = db.srs_get("w1", db_path=self.path)
        self.assertEqual(row["ease_factor"], 1.9)
        self.assertEqual(row["review_count"], 4)
        self.assertEqual(row["listen_count"], 1)

    def test_mark_synced_clears_dirty_until_next_change(self):
        db.log_review("w1", db_path=self.path)
        db.srs_mark_synced(["w1"], db_path=self.path)
        self.assertEqual(db.srs_get_dirty(self.path), [])
        db.log_review("w1", db_path=self.path)
        self.assertEqual(len(db.srs_get_dirty(self.path)), 1)

    def test_backfill_seeds_listen_count_from_review_events(self):
        # Simulate a pre-listen_count database: drop the new columns, log
        # history, then re-run initialize_database (the app upgrade path).
        conn = sqlite3.connect(self.path)
        conn.execute("DROP TABLE srs_progress")
        conn.execute("""
            CREATE TABLE srs_progress (
                word_id       TEXT PRIMARY KEY,
                ease_factor   REAL NOT NULL DEFAULT 2.5,
                interval_days INTEGER NOT NULL DEFAULT 0,
                next_review   DATETIME,
                review_count  INTEGER NOT NULL DEFAULT 0,
                correct_count INTEGER NOT NULL DEFAULT 0,
                updated_at    DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")
        for _ in range(3):
            conn.execute("INSERT INTO review_events (word_id) VALUES ('w1')")
        conn.execute("INSERT INTO review_events (word_id) VALUES ('w2')")
        conn.commit()
        conn.close()

        db.initialize_database(self.path)

        self.assertEqual(db.get_listen_count("w1", db_path=self.path), 3)
        self.assertEqual(db.get_listen_count("w2", db_path=self.path), 1)
        # Backfilled rows are dirty so the first sync seeds the cloud.
        dirty_ids = {r["word_id"] for r in db.srs_get_dirty(self.path)}
        self.assertEqual(dirty_ids, {"w1", "w2"})

    def test_rekey_moves_progress_row(self):
        db.log_review("old", db_path=self.path)
        conn = sqlite3.connect(self.path)
        db.rekey_progress(conn.cursor(), "old", "new")
        conn.commit()
        conn.close()
        self.assertEqual(db.get_listen_count("new", db_path=self.path), 1)
        self.assertEqual(db.get_listen_count("old", db_path=self.path), 0)

    def test_rekey_merges_when_both_rows_exist(self):
        # Old id: listens only. New id: SRS grades only. The merged row must
        # keep both, dirty, and drop the old row.
        db.log_review("old", db_path=self.path)
        db.log_review("old", db_path=self.path)
        db.srs_upsert(
            "new",
            {
                "ease_factor": 2.1,
                "interval_days": 3,
                "next_review": "2026-07-15T00:00:00",
                "review_count": 2,
                "correct_count": 2,
            },
            db_path=self.path,
        )
        conn = sqlite3.connect(self.path)
        db.rekey_progress(conn.cursor(), "old", "new")
        conn.commit()
        conn.close()
        row = db.srs_get("new", db_path=self.path)
        self.assertEqual(row["listen_count"], 2)
        self.assertEqual(row["review_count"], 2)
        self.assertEqual(row["ease_factor"], 2.1)
        self.assertIsNone(db.srs_get("old", db_path=self.path))
        self.assertIsNone(row["synced_at"])


class SyncWordProgressTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._cwd = os.getcwd()
        os.chdir(self._tmp.name)
        self.path = os.path.join(self._tmp.name, "d.db")
        db.set_active_db_path(self.path)
        db.initialize_database(self.path)
        conn = sqlite3.connect(self.path)
        conn.execute("INSERT INTO words (ID, Word1, Word2) VALUES ('w1', 'cat', 'Katze')")
        conn.commit()
        conn.close()

        self.sm = SyncManager.__new__(SyncManager)
        self.sm.local_db = self.path
        self.sm.supabase = MagicMock()
        self.sm.db_adapter = MagicMock()
        self.metadata = {}
        self.sm.db_adapter.get_sync_metadata.side_effect = self.metadata.get
        self.sm.db_adapter.set_sync_metadata.side_effect = self.metadata.__setitem__
        # Default: pushes succeed.
        self.sm.supabase.upsert_word_progress_bulk.side_effect = lambda rows: (
            [str(r["word_id"]) for r in rows],
            [],
        )

    def tearDown(self):
        os.chdir(self._cwd)
        db.set_active_db_path(db.DB_PATH)
        self._tmp.cleanup()

    def test_pull_merges_cloud_counts_into_local(self):
        db.log_review("w1", db_path=self.path)  # local: 1 listen
        self.sm.supabase.get_word_progress_changes.return_value = [
            _row("w1", listen_count=5, updated_at="2026-07-01T10:00:00+00:00")
        ]

        self.sm._sync_word_progress()

        self.assertEqual(db.get_listen_count("w1", db_path=self.path), 5)
        # Merge beat the cloud row (local counter folded in via max on a later
        # local stamp) or matched it; either way nothing is lost. The merged
        # row was pushed and marked clean.
        self.assertEqual(db.srs_get_dirty(self.path), [])

    def test_cloud_row_for_unknown_word_is_deferred(self):
        self.sm.supabase.get_word_progress_changes.return_value = [
            _row("missing-word", listen_count=5)
        ]
        self.sm._sync_word_progress()
        self.assertIsNone(db.srs_get("missing-word", db_path=self.path))

    def test_failed_push_rows_stay_dirty(self):
        db.log_review("w1", db_path=self.path)
        self.sm.supabase.get_word_progress_changes.return_value = []
        self.sm.supabase.upsert_word_progress_bulk.side_effect = lambda rows: (
            [],
            [str(r["word_id"]) for r in rows],
        )

        self.sm._sync_word_progress()

        self.assertEqual([r["word_id"] for r in db.srs_get_dirty(self.path)], ["w1"])

    def test_watermark_advances_to_max_cloud_updated_at(self):
        self.sm.supabase.get_word_progress_changes.return_value = [
            _row("w1", updated_at="2026-07-01T10:00:00+00:00"),
            _row("missing", updated_at="2026-07-04T08:30:00+00:00"),
        ]
        self.sm._sync_word_progress()
        self.assertEqual(self.metadata["word_progress_last_sync"], "2026-07-04T08:30:00+00:00")

    def test_full_ignores_watermark(self):
        self.metadata["word_progress_last_sync"] = "2026-07-05T00:00:00+00:00"
        self.sm.supabase.get_word_progress_changes.return_value = []
        self.sm._sync_word_progress(full=True)
        self.sm.supabase.get_word_progress_changes.assert_called_once_with(None)

    def test_cloud_error_does_not_raise(self):
        self.sm.supabase.get_word_progress_changes.side_effect = Exception("network down")
        self.sm._sync_word_progress()  # must not propagate


if __name__ == "__main__":
    unittest.main()
