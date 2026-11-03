# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Account limits on writes, and the daily cap on new words in the due deck.

Run:  python -m unittest tests.test_limits
"""

import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import db, limits, srs  # noqa: E402
from app.core.database_adapter import DatabaseAdapter  # noqa: E402
from app.core.errors import DuplicateWordError, LimitError  # noqa: E402


def _word(i):
    return {"Language1": "en", "Word1": f"w{i}", "Language2": "de", "Word2": f"t{i}"}


class _AdapterCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._cwd = os.getcwd()
        os.chdir(self._tmp.name)
        self.path = os.path.join(self._tmp.name, "d.db")
        db.set_active_db_path(self.path)
        db.initialize_database(self.path)
        self.a = DatabaseAdapter(use_cloud=False)
        self.a.set_local_db(self.path)

    def tearDown(self):
        os.chdir(self._cwd)
        db.set_active_db_path(db.DB_PATH)
        self._tmp.cleanup()

    def _limited(self, active=True, **caps):
        patches = [mock.patch.object(limits, "active", return_value=active)]
        patches += [mock.patch.object(limits, name, value) for name, value in caps.items()]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)


class WordLimitTests(_AdapterCase):
    def test_insert_stops_at_the_limit(self):
        self._limited(WORD_LIMIT=2)
        self.a.insert_word(_word(1))
        self.a.insert_word(_word(2))
        with self.assertRaises(LimitError):
            self.a.insert_word(_word(3))
        self.assertEqual(self.a.count_words(), 2)

    def test_no_limit_when_inactive(self):
        self._limited(active=False, WORD_LIMIT=1)
        self.a.insert_word(_word(1))
        self.a.insert_word(_word(2))
        self.assertEqual(self.a.count_words(), 2)

    def test_bulk_over_the_limit_writes_nothing(self):
        self._limited(WORD_LIMIT=3)
        self.a.insert_word(_word(0))
        with self.assertRaises(LimitError):
            self.a.insert_words_bulk([_word(i) for i in range(1, 4)])
        self.assertEqual(self.a.count_words(), 1)

    def test_bulk_results_line_up_with_the_input(self):
        self.a.insert_word(_word(1))
        results = self.a.insert_words_bulk([_word(2), _word(1), _word(3)])
        self.assertEqual(results[0]["Word1"], "w2")
        self.assertIsInstance(results[1], DuplicateWordError)
        self.assertEqual(results[2]["Word1"], "w3")
        self.assertEqual(self.a.count_words(), 3)


class TextLimitTests(_AdapterCase):
    def _text(self, body="x"):
        return {"Title": "t", "Text": body, "Language": "English"}

    def test_text_length(self):
        self._limited(TEXT_LENGTH_LIMIT=5)
        self.a.insert_text(self._text("12345"))
        with self.assertRaises(LimitError):
            self.a.insert_text(self._text("123456"))
        text_id = self.a.get_texts()[0]["ID"]
        with self.assertRaises(LimitError):
            self.a.update_text(text_id, {"Text": "123456"})

    def test_existing_oversized_text_stays_editable(self):
        self._limited(active=False)
        self.a.insert_text(self._text("123456"))
        text_id = self.a.get_texts()[0]["ID"]
        self._limited(TEXT_LENGTH_LIMIT=5)
        self.a.update_text(text_id, {"Title": "renamed", "Text": "123456"})
        with self.assertRaises(LimitError):
            self.a.update_text(text_id, {"Text": "1234567"})

    def test_text_count(self):
        self._limited(TEXT_LIMIT=1)
        self.a.insert_text(self._text())
        with self.assertRaises(LimitError):
            self.a.insert_text(self._text())

    def test_no_text_limits_when_inactive(self):
        self._limited(active=False, TEXT_LIMIT=1, TEXT_LENGTH_LIMIT=1)
        self.a.insert_text(self._text("long"))
        self.a.insert_text(self._text("long"))
        self.assertEqual(self.a.count_texts(), 2)


class DailyNewWordTests(_AdapterCase):
    def _add(self, i, days_ago=0):
        created = (datetime.now(timezone.utc) - timedelta(days=days_ago)).isoformat()
        return self.a._insert_word_sqlite(dict(_word(i), created_at=created))["ID"]

    def _grade(self, wid, due_in_days=1):
        card = srs.apply_grade(None, "good", datetime.now())
        card["next_review"] = (datetime.now() + timedelta(days=due_in_days)).isoformat(
            timespec="seconds"
        )
        db.srs_upsert(wid, card, db_path=self.path)

    def test_reviews_come_first_then_new_words_oldest_first(self):
        newer = self._add(1, days_ago=1)
        older = self._add(2, days_ago=5)
        review = self._add(3, days_ago=9)
        self._grade(review, due_in_days=-1)
        self.assertEqual(db.srs_due_word_ids(10, db_path=self.path), [review, older, newer])

    def test_new_limit_caps_only_new_words(self):
        reviews = [self._add(i, days_ago=10) for i in range(3)]
        for wid in reviews:
            self._grade(wid, due_in_days=-1)
        for i in range(3, 8):
            self._add(i)
        ids = db.srs_due_word_ids(10, db_path=self.path, new_limit=2)
        self.assertEqual(len(ids), 5)
        self.assertEqual(set(ids[:3]), set(reviews))
        self.assertEqual(db.srs_due_word_ids(10, db_path=self.path, new_limit=0), ids[:3])

    def test_counts(self):
        review = self._add(1)
        self._grade(review, due_in_days=-1)
        later = self._add(2)
        self._grade(later, due_in_days=3)
        self._add(3)
        self._add(4)
        self.assertEqual(db.srs_due_counts(db_path=self.path), (1, 2))

    def test_allowance_counts_words_first_graded_today(self):
        first = self._add(1)
        self._grade(first)
        self.assertEqual(db.srs_new_allowance(20, db_path=self.path), 19)

        again = self._add(2)
        self._grade(again)
        row = db.srs_get(again, db_path=self.path)
        db.srs_upsert(again, srs.apply_grade(row, "good", datetime.now()), db_path=self.path)
        self.assertEqual(db.srs_new_allowance(20, db_path=self.path), 19)

        pulled = self._add(3)
        yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
        db.srs_write_row(
            {"word_id": pulled, "review_count": 1, "last_reviewed": yesterday},
            synced=True,
            db_path=self.path,
        )
        self.assertEqual(db.srs_new_allowance(20, db_path=self.path), 19)
        self.assertEqual(db.srs_new_allowance(1, db_path=self.path), 0)


if __name__ == "__main__":
    unittest.main()
