# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Flagging a word for relearning: the "To Learn" rung and its schedule reset.

The flag is two writes on two sync channels — the label on ``words.Status`` and
a lapse on the ``srs_progress`` row — so the cases that matter are the ones
where doing only half the job would look like it worked: a label with no reset
leaves the word scheduled months out, and a reset that zeroes the counters is
silently undone by the next sync pull.

Run:  python -m unittest tests.test_relearn
"""

import os
import sys
import tempfile
import unittest
import uuid
from unittest import mock
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from app.core import db  # noqa: E402
from app.core import progression  # noqa: E402
from app.core import srs  # noqa: E402

NOW = datetime(2026, 8, 28, 12, 0, 0)


def _mastered_card():
    """The row a thoroughly mastered word carries: ease pinned at the ceiling
    and a correct count far above the Mastered gate."""
    return {
        "ease_factor": 2.5,
        "interval_days": 180,
        "next_review": "2027-02-24T12:00:00",
        "review_count": 25,
        "correct_count": 20,
    }


class CanLapseTests(unittest.TestCase):
    def test_only_words_with_an_interval_worth_pulling_back(self):
        for status in ("Learning", "Mastered", "  mastered  "):
            with self.subTest(status=status):
                self.assertTrue(progression.can_lapse(status))

    def test_reviewing_is_below_the_bar(self):
        # Its ease is already under the ceiling srs.lapse pulls down to, so for
        # a word due today the flag would only relabel — see LAPSABLE_FROM.
        card = {"ease_factor": 1.5, "interval_days": 1, "review_count": 9, "correct_count": 1}
        lapsed = srs.lapse(card, NOW)
        self.assertEqual(lapsed["ease_factor"], card["ease_factor"])
        self.assertEqual(lapsed["interval_days"], card["interval_days"])
        self.assertFalse(progression.can_lapse("Reviewing"))

    def test_nothing_to_forget_off_the_ladder_or_at_the_bottom(self):
        for status in ("New", "", "  ", "To Learn", "Ignored", "Custom", None):
            with self.subTest(status=status):
                self.assertFalse(progression.can_lapse(status))

    def test_non_strings(self):
        # A blank status is NaN once it has been through a DataFrame.
        self.assertFalse(progression.can_lapse(float("nan")))

    def test_to_learn_is_offered_by_the_status_picker(self):
        self.assertIn(progression.TO_LEARN_STATUS, progression.ALL_STATUSES)

    def test_is_to_learn_matches_however_another_client_cased_it(self):
        for value in ("To Learn", "to learn", "TO LEARN", "  To Learn  "):
            with self.subTest(value=value):
                self.assertTrue(progression.is_to_learn(value))
        for value in ("Mastered", "", None, float("nan"), "ToLearn"):
            with self.subTest(value=value):
                self.assertFalse(progression.is_to_learn(value))


class LapseTests(unittest.TestCase):
    def test_due_now_and_interval_reset(self):
        state = srs.lapse(_mastered_card(), NOW)
        self.assertEqual(state["interval_days"], 1)
        self.assertEqual(state["next_review"], NOW.isoformat(timespec="seconds"))

    def test_ease_drops_below_the_learning_gate(self):
        state = srs.lapse(_mastered_card(), NOW)
        self.assertEqual(state["ease_factor"], 1.9)
        # The whole point: the mapping must not still say Mastered, even though
        # correct_count is untouched and far past the gate.
        self.assertEqual(
            srs.status_from_progress(
                state["review_count"], state["ease_factor"], state["correct_count"]
            ),
            "Reviewing",
        )

    def test_counters_are_left_alone(self):
        # merge_progress_rows takes the max of both sides for these, so a reset
        # here would be undone by the next cloud pull.
        card = _mastered_card()
        state = srs.lapse(card, NOW)
        self.assertEqual(state["review_count"], card["review_count"])
        self.assertEqual(state["correct_count"], card["correct_count"])

    def test_a_lapse_survives_the_sync_merge(self):
        card = dict(_mastered_card(), updated_at="2026-08-01T00:00:00+00:00", word_id="w1")
        lapsed = dict(card, **srs.lapse(card, NOW), updated_at="2026-08-28T12:00:00+00:00")
        # Cloud still holds the pre-lapse row; the local write is newer.
        merged = db.merge_progress_rows(card, lapsed)
        self.assertEqual(merged["ease_factor"], 1.9)
        self.assertEqual(merged["interval_days"], 1)

    def test_a_word_already_below_the_gate_is_only_rescheduled(self):
        # The lapse ease is a ceiling, not a fixed drop: nothing to punish here,
        # the word just needs to come back around.
        state = srs.lapse({"ease_factor": 1.4, "review_count": 3}, NOW)
        self.assertEqual(state["ease_factor"], 1.4)
        self.assertEqual(state["interval_days"], 1)

    def test_ease_never_falls_below_the_floor(self):
        state = srs.lapse({"ease_factor": 0.5, "review_count": 3}, NOW)
        self.assertEqual(state["ease_factor"], srs.MIN_EASE)

    def test_a_lapse_after_a_hard_grade_does_not_punish_twice(self):
        # The Hard grade has already taken 0.2 off; subtracting a fixed drop on
        # top would land at 1.7 for one click.
        graded = srs.apply_grade(_mastered_card(), "hard", NOW)
        self.assertEqual(graded["ease_factor"], 2.3)
        self.assertEqual(srs.lapse(graded, NOW)["ease_factor"], srs.LAPSE_EASE)

    def test_an_ungraded_card_is_harmless(self):
        state = srs.lapse(None, NOW)
        self.assertEqual(state["review_count"], 0)
        self.assertEqual(state["interval_days"], 1)


class LapsesOnGradeTests(unittest.TestCase):
    """Which grades mean "I have forgotten this" rather than "schedule me sooner"."""

    def test_hard_on_mastered(self):
        for status in ("Mastered", "mastered", "  Mastered  "):
            with self.subTest(status=status):
                self.assertTrue(srs.lapses_on_grade(status, "hard"))

    def test_correct_grades_never_lapse(self):
        for grade in ("good", "easy"):
            with self.subTest(grade=grade):
                self.assertFalse(srs.lapses_on_grade("Mastered", grade))

    def test_lower_rungs_keep_the_plain_interval_reset(self):
        for status in ("New", "Reviewing", "Learning", ""):
            with self.subTest(status=status):
                self.assertFalse(srs.lapses_on_grade(status, "hard"))

    def test_off_ladder_statuses_are_untouched(self):
        for status in ("To Learn", "Ignored", "Custom", None, float("nan")):
            with self.subTest(status=status):
                self.assertFalse(srs.lapses_on_grade(status, "hard"))


class ReclimbTests(unittest.TestCase):
    """What the user actually sees after flagging: four correct grades back to
    Mastered, on any client — the phone runs this same arithmetic."""

    def _grades(self, n):
        card = dict(_mastered_card(), **srs.lapse(_mastered_card(), NOW))
        status = progression.TO_LEARN_STATUS
        seen = []
        for _ in range(n):
            card = srs.apply_grade(card, "good", NOW)
            mapped = srs.status_from_progress(
                card["review_count"], card["ease_factor"], card["correct_count"]
            )
            status = srs.promotion_target(status, mapped) or status
            seen.append((card["interval_days"], status))
        return seen

    def test_the_climb_back(self):
        self.assertEqual(
            self._grades(4),
            [(1, "Learning"), (2, "Learning"), (4, "Learning"), (8, "Mastered")],
        )

    def test_a_hard_grade_knocks_it_back_down(self):
        card = dict(_mastered_card(), **srs.lapse(_mastered_card(), NOW))
        card = srs.apply_grade(card, "hard", NOW)
        self.assertEqual(
            srs.status_from_progress(
                card["review_count"], card["ease_factor"], card["correct_count"]
            ),
            "Reviewing",
        )

    def test_listening_never_promotes_off_the_to_learn_rung(self):
        # Passive audio must not clear a relearn flag — only studying may.
        thresholds = progression.normalize_thresholds()
        self.assertIsNone(progression.next_status(progression.TO_LEARN_STATUS, 10_000, thresholds))


class ImmediateProgressPushTests(unittest.TestCase):
    """The label reaches the cloud synchronously; the ease drop must chase it.

    Left to the normal sync cycle the schedule waits for app close or next
    startup, and in that window a second device sees "To Learn" against the
    pre-lapse ease — one correct grade there maps to Mastered and erases the
    flag. These pin the push, not the network.
    """

    def setUp(self):
        from app.ui.main_window import MainWindow

        self.win = MainWindow.__new__(MainWindow)  # no Qt init: pure logic
        self.pushes = 0

        class _Sync:
            def is_sync_enabled(_self):
                return True

            def push_progress_now(_self):
                self.pushes += 1
                return 1

        self.win.sync_manager = _Sync()

    def test_the_bulk_path_pushes_after_writing(self):
        with (
            mock.patch.object(db, "srs_get_many", return_value={"w1": _mastered_card()}),
            mock.patch.object(db, "srs_upsert_many") as write,
        ):
            self.win._lapse_schedules(["w1"])
        self.assertEqual(write.call_count, 1)
        self.assertEqual(self.pushes, 1)

    def test_a_failed_write_does_not_push_a_half_state(self):
        with (
            mock.patch.object(db, "srs_get_many", return_value={"w1": _mastered_card()}),
            mock.patch.object(db, "srs_upsert_many", side_effect=RuntimeError("disk")),
        ):
            self.win._lapse_schedules(["w1"])  # swallowed and logged
        self.assertEqual(self.pushes, 0)

    def test_push_is_skipped_when_sync_is_off(self):
        from app.core.sync_manager import SyncManager

        mgr = SyncManager.__new__(SyncManager)
        with (
            mock.patch.object(SyncManager, "is_sync_enabled", return_value=False),
            mock.patch.object(SyncManager, "_push_dirty_word_progress") as push,
        ):
            self.assertEqual(mgr.push_progress_now(), 0)
        push.assert_not_called()

    def test_a_push_failure_is_swallowed_for_the_next_sync(self):
        from app.core.sync_manager import SyncManager

        mgr = SyncManager.__new__(SyncManager)
        with (
            mock.patch.object(SyncManager, "is_sync_enabled", return_value=True),
            mock.patch.object(
                SyncManager, "_push_dirty_word_progress", side_effect=OSError("offline")
            ),
        ):
            self.assertEqual(mgr.push_progress_now(), 0)


class WrongAnswerNeverPromotesTests(unittest.TestCase):
    """A word whose SM-2 state has run ahead of its label used to be promoted
    by getting it *wrong*: one Hard barely moves cumulative counters, so the
    mapping still read higher than the rung and promotion_target applied it."""

    def test_the_mapping_can_outrun_the_label(self):
        # The setup that made this reachable: ease still high, plenty correct,
        # but the word is only labelled Learning.
        graded = srs.apply_grade(
            {"ease_factor": 2.5, "interval_days": 30,
             "review_count": 25, "correct_count": 20}, "hard", NOW)
        mapped = srs.status_from_progress(
            graded["review_count"], graded["ease_factor"], graded["correct_count"])
        self.assertEqual(mapped, "Mastered")
        # promotion_target is pure and still says "yes" — the grade is what the
        # pages now refuse to promote on, so the rule lives at the call site.
        self.assertEqual(srs.promotion_target("Learning", mapped), "Mastered")

    def test_pages_do_not_promote_on_hard(self):
        import inspect
        from app.ui import flashcards_page, quiz_page
        self.assertIn('elif grade != "hard":',
                      inspect.getsource(flashcards_page.FlashcardsPage._grade))
        self.assertIn('if grade == "hard":',
                      inspect.getsource(quiz_page.QuizPage._grade))


class LapseStorageTests(unittest.TestCase):
    def setUp(self):
        fd, self.db_path = tempfile.mkstemp(suffix=".db")
        os.close(fd)
        os.unlink(self.db_path)
        db.initialize_database(self.db_path)

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.unlink(self.db_path)

    def _graded_word(self):
        import sqlite3

        wid = str(uuid.uuid4())
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO words (ID, Word1, Word2, Status) VALUES (?, ?, ?, ?)",
            (wid, f"w-{wid[:8]}", f"t-{wid[:8]}", "Mastered"),
        )
        conn.commit()
        conn.close()
        db.srs_upsert(wid, _mastered_card(), db_path=self.db_path)
        return wid

    def test_lapsing_makes_the_word_due(self):
        wid = self._graded_word()
        later = datetime(2026, 8, 28, 13, 0, 0).isoformat(timespec="seconds")
        self.assertEqual(db.srs_due_word_ids(10, now_iso=later, db_path=self.db_path), [])
        db.srs_upsert(
            wid,
            srs.lapse(db.srs_get(wid, db_path=self.db_path), NOW),
            db_path=self.db_path,
            touch_reviewed=False,
        )
        self.assertEqual(db.srs_due_word_ids(10, now_iso=later, db_path=self.db_path), [wid])

    def test_a_lapse_does_not_count_as_a_review(self):
        wid = self._graded_word()
        before = db.srs_get(wid, db_path=self.db_path)["last_reviewed"]
        db.srs_upsert(
            wid,
            srs.lapse(before and _mastered_card(), NOW),
            db_path=self.db_path,
            touch_reviewed=False,
        )
        self.assertEqual(db.srs_get(wid, db_path=self.db_path)["last_reviewed"], before)

    def test_a_grade_still_stamps_last_reviewed(self):
        wid = self._graded_word()
        row = db.srs_get(wid, db_path=self.db_path)
        self.assertIsNotNone(row["last_reviewed"])

    def test_the_lapse_is_queued_for_push(self):
        wid = self._graded_word()
        db.srs_mark_synced([wid], db_path=self.db_path)
        self.assertEqual(db.srs_get_dirty(db_path=self.db_path), [])
        db.srs_upsert(
            wid,
            srs.lapse(db.srs_get(wid, db_path=self.db_path), NOW),
            db_path=self.db_path,
            touch_reviewed=False,
        )
        dirty = db.srs_get_dirty(db_path=self.db_path)
        self.assertEqual([r["word_id"] for r in dirty], [wid])

    def test_upsert_many_writes_a_whole_selection(self):
        ids = [self._graded_word() for _ in range(3)]
        rows = db.srs_get_many(ids, db_path=self.db_path)
        db.srs_upsert_many(
            {w: srs.lapse(r, NOW) for w, r in rows.items()},
            db_path=self.db_path,
            touch_reviewed=False,
        )
        for wid in ids:
            with self.subTest(wid=wid):
                row = db.srs_get(wid, db_path=self.db_path)
                self.assertEqual(row["interval_days"], 1)
                self.assertEqual(row["ease_factor"], 1.9)

    def test_upsert_many_on_nothing(self):
        db.srs_upsert_many({}, db_path=self.db_path)


if __name__ == "__main__":
    unittest.main()
