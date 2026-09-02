# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for tag cleanup when the words carrying a tag are deleted.

Run:  python -m unittest tests.test_orphan_tags
"""

import os
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import db  # noqa: E402
from app.core.db import (  # noqa: E402
    get_all_tags,
    get_tag_usage_counts,
    initialize_database,
    purge_orphan_tags,
)
from app.core.database_adapter import DatabaseAdapter  # noqa: E402


class OrphanTagTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        # The suite runs from the repo root and settings resolve against the
        # cwd, so stay inside the sandbox for the duration of the test.
        cwd = os.getcwd()
        os.chdir(self.tmp.name)
        self.addCleanup(os.chdir, cwd)

        self.db_path = os.path.join(self.tmp.name, "test.db")
        db.set_active_db_path(self.db_path)
        initialize_database(self.db_path)

        self.adapter = DatabaseAdapter(use_cloud=False)
        self.adapter.set_local_db(self.db_path)

    def _word(self, word1, word2, tags=()):
        row = self.adapter._insert_word_sqlite(
            {
                "Language1": "English",
                "Word1": word1,
                "Language2": "German",
                "Word2": word2,
                "Status": "New",
                "Source": "test",
            }
        )
        for name in tags:
            self.adapter._add_tag_to_word_sqlite(
                row["ID"], self.adapter._get_or_create_tag_sqlite(name)
            )
        return row["ID"]

    def _rows(self, query):
        conn = sqlite3.connect(self.db_path)
        try:
            return conn.execute(query).fetchall()
        finally:
            conn.close()


class DeleteWordTests(OrphanTagTestCase):
    def test_deleting_the_last_word_of_a_tag_removes_the_tag(self):
        word_id = self._word("house", "Haus", tags=["home"])
        self.adapter.delete_word(word_id)
        self.assertEqual(get_all_tags(self.db_path), [])
        self.assertEqual(self._rows("SELECT * FROM word_tags"), [])

    def test_a_tag_still_used_by_another_word_survives(self):
        first = self._word("house", "Haus", tags=["noun"])
        self._word("dog", "Hund", tags=["noun"])
        self.adapter.delete_word(first)
        self.assertEqual(get_all_tags(self.db_path), ["noun"])
        self.assertEqual(get_tag_usage_counts(self.db_path), {"noun": 1})

    def test_bulk_delete_cleans_up_too(self):
        ids = [
            self._word("house", "Haus", tags=["home", "noun"]),
            self._word("dog", "Hund", tags=["noun"]),
        ]
        self.adapter.delete_words_bulk(ids)
        self.assertEqual(get_all_tags(self.db_path), [])

    def test_restoring_a_word_brings_its_tags_back(self):
        word_id = self._word("house", "Haus", tags=["home"])
        self.adapter.delete_word(word_id)
        self.assertTrue(self.adapter.restore_word(word_id))
        self.assertEqual(get_all_tags(self.db_path), ["home"])
        self.assertEqual(get_tag_usage_counts(self.db_path), {"home": 1})


class PurgeOrphanTagsTests(OrphanTagTestCase):
    def _orphan(self):
        """A tag and a link left behind the way older versions left them."""
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO tags (tag_id, tag_name) VALUES ('t-old', 'leftover')")
        conn.execute(
            "INSERT INTO word_tags (word_id, tag_id, synced) " "VALUES ('gone', 't-old', 1)"
        )
        conn.commit()
        conn.close()

    def test_dangling_links_and_unused_tags_are_removed(self):
        self._orphan()
        conn = sqlite3.connect(self.db_path)
        links, tag_ids = purge_orphan_tags(conn.cursor())
        conn.commit()
        conn.close()
        self.assertEqual((links, tag_ids), (1, ["t-old"]))
        self.assertEqual(get_all_tags(self.db_path), [])

    def test_opening_an_old_database_sweeps_it(self):
        self._orphan()
        initialize_database(self.db_path)
        self.assertEqual(get_all_tags(self.db_path), [])

    def test_a_link_to_a_deleted_word_is_not_counted_as_a_use(self):
        # The count has to stay honest even before the sweep runs.
        self._word("house", "Haus", tags=["home"])
        conn = sqlite3.connect(self.db_path)
        tag_id = conn.execute("SELECT tag_id FROM tags").fetchone()[0]
        conn.execute(
            "INSERT INTO word_tags (word_id, tag_id, synced) VALUES (?, ?, 1)", ("gone", tag_id)
        )
        conn.commit()
        conn.close()
        self.assertEqual(get_tag_usage_counts(self.db_path), {"home": 1})


class CloudCleanupTests(OrphanTagTestCase):
    """A cloud word is only soft-deleted, so its links must be cleared by hand."""

    def setUp(self):
        super().setUp()
        self.cloud = MagicMock()
        self.cloud.delete_word.return_value = True
        self.cloud.delete_words_bulk.side_effect = lambda ids: (list(ids), [])
        self.adapter.supabase = self.cloud
        self.adapter.use_cloud = True
        self.adapter.cloud_available = True

    def test_deleting_a_word_clears_its_cloud_links_and_the_dead_tag(self):
        word_id = self._word("house", "Haus", tags=["home"])
        tag_id = self._rows("SELECT tag_id FROM tags")[0][0]

        self.adapter.delete_word(word_id)

        self.cloud.remove_word_tags_for_words.assert_called_once_with([word_id])
        self.cloud.delete_tag.assert_called_once_with(tag_id)

    def test_a_tag_other_words_still_use_is_kept_in_the_cloud(self):
        first = self._word("house", "Haus", tags=["noun"])
        self._word("dog", "Hund", tags=["noun"])

        self.adapter.delete_word(first)

        self.cloud.remove_word_tags_for_words.assert_called_once_with([first])
        self.cloud.delete_tag.assert_not_called()

    def test_bulk_delete_clears_the_cloud_links_in_one_call(self):
        ids = [self._word("house", "Haus", tags=["home"]), self._word("dog", "Hund", tags=["home"])]

        self.adapter.delete_words_bulk(ids)

        self.cloud.remove_word_tags_for_words.assert_called_once_with(ids)


class SyncDoesNotResurrectTests(OrphanTagTestCase):
    """The bug the user hit: a sync brought deleted words' links back as uses."""

    def _sync(self, cloud_tags, cloud_links):
        from app.core.sync_manager import SyncManager

        manager = SyncManager.__new__(SyncManager)
        manager.local_db = self.db_path
        manager.db_adapter = self.adapter
        manager.supabase = MagicMock()
        manager.supabase.get_tags.return_value = cloud_tags
        manager.supabase.get_all_word_tags.return_value = cloud_links
        manager.supabase.add_tags_to_words_bulk.return_value = True
        manager._sync_tags_incremental(None)
        return manager.supabase

    def test_a_link_for_a_word_this_device_does_not_have_is_not_pulled_in(self):
        cloud = self._sync(
            [{"tag_id": "t-old", "tag_name": "leftover"}],
            [{"word_id": "deleted-word", "tag_id": "t-old"}],
        )
        self.assertEqual(self._rows("SELECT * FROM word_tags"), [])
        self.assertEqual(
            get_all_tags(self.db_path), [], "a tag with no local word must not linger in the picker"
        )
        cloud.add_tags_to_words_bulk.assert_not_called()

    def test_links_for_words_this_device_has_are_still_pulled_in(self):
        word_id = self._word("house", "Haus")
        self._sync([{"tag_id": "t-1", "tag_name": "home"}], [{"word_id": word_id, "tag_id": "t-1"}])
        self.assertEqual(get_tag_usage_counts(self.db_path), {"home": 1})


if __name__ == "__main__":
    unittest.main()
