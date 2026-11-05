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
        known = limits.AccountLimits(**caps) if active else limits.NONE
        p = mock.patch.object(limits, "current", return_value=known)
        p.start()
        self.addCleanup(p.stop)


class WordLimitTests(_AdapterCase):
    def test_insert_stops_at_the_limit(self):
        self._limited(words=2)
        self.a.insert_word(_word(1))
        self.a.insert_word(_word(2))
        with self.assertRaises(LimitError):
            self.a.insert_word(_word(3))
        self.assertEqual(self.a.count_words(), 2)

    def test_no_limit_when_inactive(self):
        self._limited(active=False, words=1)
        self.a.insert_word(_word(1))
        self.a.insert_word(_word(2))
        self.assertEqual(self.a.count_words(), 2)

    def test_bulk_over_the_limit_writes_nothing(self):
        self._limited(words=3)
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
        self._limited(text_length=5)
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
        self._limited(text_length=5)
        self.a.update_text(text_id, {"Title": "renamed", "Text": "123456"})
        with self.assertRaises(LimitError):
            self.a.update_text(text_id, {"Text": "1234567"})

    def test_text_count(self):
        self._limited(texts=1)
        self.a.insert_text(self._text())
        with self.assertRaises(LimitError):
            self.a.insert_text(self._text())

    def test_no_text_limits_when_inactive(self):
        self._limited(active=False, texts=1, text_length=1)
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


class _Rpc:
    def __init__(self, data=None, error=None):
        self.data, self.error = data, error

    def rpc(self, _name):
        return self

    def execute(self):
        if self.error:
            raise self.error
        return self


class _CodedError(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


class ServerLimitsTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._cwd = os.getcwd()
        os.chdir(self._tmp.name)
        self.owner = "user-a"
        for name, value in (("active", True),):
            p = mock.patch.object(limits, name, return_value=value)
            p.start()
            self.addCleanup(p.stop)
        p = mock.patch.object(limits, "_current_owner", side_effect=lambda: self.owner)
        p.start()
        self.addCleanup(p.stop)
        limits._owner, limits._limits = None, limits.NONE

    def tearDown(self):
        os.chdir(self._cwd)
        self._tmp.cleanup()

    def test_nothing_is_checked_before_the_server_answers(self):
        self.assertEqual(limits.current(), limits.NONE)

    def test_takes_the_server_answer_and_keeps_it_offline(self):
        limits.refresh(_Rpc(data=[{"words_max": 25000, "texts_max": None}]))
        self.assertEqual(limits.current().words, 25000)
        self.assertIsNone(limits.current().texts)
        limits._owner, limits._limits = None, limits.NONE  # a fresh launch
        limits.refresh(_Rpc(error=OSError("Connection refused")))
        self.assertEqual(limits.current().words, 25000)

    def test_another_account_never_inherits_them(self):
        limits.refresh(_Rpc(data=[{"words_max": 5}]))
        self.owner = "user-b"
        self.assertEqual(limits.current(), limits.NONE)

    def test_a_server_without_the_schema_has_no_limits(self):
        limits.refresh(_Rpc(data=[{"words_max": 5}]))
        limits.refresh(_Rpc(error=_CodedError("PGRST202")))
        self.assertEqual(limits.current(), limits.NONE)

    def test_messages_name_the_number_in_the_ui_language(self):
        from app import i18n

        self.addCleanup(i18n.set_language, i18n._lang)
        self.assertIn("25,000", str(limits.word_limit_error(25000)))
        i18n.set_language("de")
        self.assertIn("25.000", str(limits.word_limit_error(25000)))


class WordLengthTests(_AdapterCase):
    def test_insert_refuses_a_long_word_or_definition(self):
        self._limited(word_length=5, definition_length=10)
        with self.assertRaises(LimitError):
            self.a.insert_word({**_word(1), "Word1": "x" * 6})
        with self.assertRaises(LimitError):
            self.a.insert_word({**_word(2), "Definition2": "d" * 11})
        self.assertEqual(self.a.count_words(), 0)

    def test_update_checks_only_changed_values(self):
        row = self.a.insert_word({**_word(1), "Definition": "d" * 20})
        self._limited(definition_length=10)
        self.a.update_word(row["ID"], {"Definition": "d" * 20, "Status": "Learning"})
        with self.assertRaises(LimitError):
            self.a.update_word(row["ID"], {"Definition": "e" * 20})
        self.assertEqual(self.a._get_word_sqlite(row["ID"])["Definition"], "d" * 20)

    def test_bulk_reports_a_long_word_in_its_slot(self):
        self._limited(word_length=5)
        results = self.a.insert_words_bulk([_word(1), {**_word(2), "Word2": "y" * 6}])
        self.assertEqual(results[0]["Word1"], "w1")
        self.assertIsInstance(results[1], LimitError)


class ShortenTests(unittest.TestCase):
    def test_cuts_at_a_paragraph_or_sentence_end(self):
        self.assertEqual(limits.shorten("One two three.\nFour five six", 20), "One two three.")
        self.assertEqual(limits.shorten("One two three. Four five six", 20), "One two three.")

    def test_falls_back_to_a_word_break_then_a_hard_cut(self):
        self.assertEqual(limits.shorten("alpha beta gamma delta", 18), "alpha beta gamma")
        self.assertEqual(limits.shorten("x" * 30, 10), "x" * 10)

    def test_leaves_text_within_the_limit(self):
        self.assertEqual(limits.shorten("short", 10), "short")
        self.assertEqual(limits.shorten("x" * 30, None), "x" * 30)


def _rejection(hint, details=None, message="rejected"):
    from postgrest.exceptions import APIError

    return APIError({"message": message, "code": "P0001", "hint": hint, "details": details})


class CapRejectedTests(unittest.TestCase):
    def test_cuts_the_rejected_fields_to_the_servers_limit(self):
        payload = {"word1": "w", "definition": "d" * 12, "definition2": "ok"}
        capped = limits.cap_rejected(payload, _rejection("definition_too_long", "10"))
        self.assertEqual(capped, {"word1": "w", "definition": "d" * 10, "definition2": "ok"})
        self.assertEqual(payload["definition"], "d" * 12)

    def test_uses_the_known_limit_without_a_detail(self):
        with mock.patch.object(limits, "current", return_value=limits.AccountLimits(text_length=4)):
            capped = limits.cap_rejected({"text": "abcdef"}, _rejection("text_too_long"))
        self.assertEqual(capped["text"], "abcd")

    def test_fixed_caps(self):
        capped = limits.cap_rejected(
            {"title": "t" * 250, "words": "a, b"}, _rejection("text_field_too_long")
        )
        self.assertEqual(len(capped["title"]), limits.TITLE_MAX)
        tag = _rejection(None, message='violates check constraint "tags_length_check"')
        self.assertEqual(
            len(limits.cap_rejected({"tag_name": "n" * 60}, tag)["tag_name"]), limits.TAG_NAME_MAX
        )

    def test_other_errors_and_nothing_to_cut(self):
        self.assertIsNone(limits.cap_rejected({"word1": "w"}, Exception("timeout")))
        self.assertIsNone(limits.cap_rejected({"word1": "w"}, _rejection("word_too_long", "5")))


class _Table:
    """Stands in for ``client.table(...)``: refuses over-long definitions once."""

    def __init__(self, sent):
        self.sent = sent

    def upsert(self, payload, **_kw):
        self.payload = payload
        return self

    def execute(self):
        self.sent.append(dict(self.payload))
        if len(self.payload.get("definition") or "") > 10:
            raise _rejection("definition_too_long", "10")
        return mock.Mock(data=[self.payload])


class PushFallbackTests(unittest.TestCase):
    def _client(self):
        from app.core.supabase_client import SupabaseClient

        client = SupabaseClient.__new__(SupabaseClient)
        client.sent = []
        client.client = mock.Mock(table=lambda _name: _Table(client.sent))
        return client

    def test_a_refused_definition_is_sent_again_cut_to_the_limit(self):
        client = self._client()
        row = client.upsert_word({"ID": "w1", "Word1": "a", "Word2": "b", "Definition": "d" * 15})
        self.assertEqual([len(p["definition"]) for p in client.sent], [15, 10])
        self.assertEqual(row["Definition"], "d" * 10)

    def test_other_errors_are_not_retried(self):
        from app.core.supabase_client import SupabaseClient

        sent = []

        def fail(_payload):
            sent.append(1)
            raise ConnectionError("connection reset")

        with self.assertRaises(ConnectionError):
            SupabaseClient._within_limits({"definition": "d" * 15}, fail)
        self.assertEqual(sent, [1])


class AiFitsLimitsTests(unittest.TestCase):
    def setUp(self):
        p = mock.patch.object(
            limits,
            "current",
            return_value=limits.AccountLimits(definition_length=20, text_length=30),
        )
        p.start()
        self.addCleanup(p.stop)

    def test_generated_definition_is_shortened(self):
        from app.core import ai

        provider = mock.Mock(
            complete=mock.Mock(return_value="A small house. Usually built of wood.")
        )
        with (
            mock.patch.object(ai, "get_provider", return_value=provider),
            mock.patch.object(
                ai,
                "_task_params",
                return_value={
                    "template": "{word}",
                    "max_tokens": 10,
                    "model": "m",
                    "temperature": 0,
                },
            ),
        ):
            self.assertEqual(ai.get_definition("Hütte", "de", "en"), "A small house.")

    def test_generated_text_and_title_are_shortened(self):
        from app.core import ai

        title, text = ai._split_title_text(
            "T" * 300 + "\n\nIch gehe nach Hause. Dann esse ich Brot."
        )
        self.assertEqual(len(title), limits.TITLE_MAX)
        self.assertEqual(text, "Ich gehe nach Hause.")

    def test_saving_a_generated_text_reports_the_limit(self):
        from app.core import ai

        adapter = mock.Mock(insert_text=mock.Mock(side_effect=limits.text_count_error(3)))
        with mock.patch.object(ai, "_make_db_adapter", return_value=adapter):
            ok, message = ai.save_generated_text_to_db(None, "t", "x", "", "de")
        self.assertFalse(ok)
        self.assertEqual(message, str(limits.text_count_error(3)))


class MinVersionTests(unittest.TestCase):
    def test_compares_padded_versions(self):
        from app.core import updater

        self.assertTrue(updater.is_below_minimum("2.2.0", current="2.1.1"))
        self.assertFalse(updater.is_below_minimum("2.2", current="2.2.0"))
        self.assertFalse(updater.is_below_minimum("2.2.0", current="2.2"))
        self.assertTrue(updater.is_below_minimum("2.2.1", current="2.2"))
        self.assertFalse(updater.is_below_minimum("soon", current="2.1.1"))


if __name__ == "__main__":
    unittest.main()
