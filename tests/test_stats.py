# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for the pure dashboard-stats layer.

Dates are expressed relative to ``date.today()`` so the streak/heatmap helpers
stay deterministic without freezing the clock.

Run:  python -m unittest tests.test_stats
"""

import os
import sys
import unittest
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd  # noqa: E402

from app.core import stats as s  # noqa: E402

TODAY = date.today()


def _ago(n):
    return TODAY - timedelta(days=n)


class StreakTests(unittest.TestCase):
    def test_empty_is_zero(self):
        self.assertEqual(s._streaks(set()), (0, 0))

    def test_consecutive_days_ending_today(self):
        active = {_ago(0), _ago(1), _ago(2)}
        cur, longest = s._streaks(active)
        self.assertEqual(cur, 3)
        self.assertEqual(longest, 3)

    def test_empty_today_does_not_break_current_streak(self):
        # No activity today, but yesterday + the day before -> current streak 2.
        active = {_ago(1), _ago(2)}
        cur, _ = s._streaks(active)
        self.assertEqual(cur, 2)

    def test_gap_resets_current_but_longest_remembers(self):
        active = {_ago(0), _ago(5), _ago(6), _ago(7)}
        cur, longest = s._streaks(active)
        self.assertEqual(cur, 1)
        self.assertEqual(longest, 3)


class FillDailyTests(unittest.TestCase):
    def test_empty_returns_empty(self):
        self.assertEqual(s._fill_daily([]), [])

    def test_zero_fills_gaps_and_sorts_ascending(self):
        out = s._fill_daily([(_ago(3), 2), (_ago(1), 5)])
        days = [d for d, _ in out]
        self.assertEqual(days, sorted(days))
        # contiguous: no missing calendar days between first and last
        for earlier, later in zip(days, days[1:], strict=False):
            self.assertEqual((later - earlier).days, 1)
        counts = dict(out)
        self.assertEqual(counts[_ago(3)], 2)
        self.assertEqual(counts[_ago(2)], 0)  # filled gap
        self.assertEqual(counts[_ago(1)], 5)

    def test_accepts_iso_string_keys(self):
        out = s._fill_daily([(_ago(1).isoformat(), 4)])
        self.assertTrue(out)
        self.assertEqual(dict(out)[_ago(1)], 4)


class TopTests(unittest.TestCase):
    def test_sorts_by_count_then_name_and_truncates(self):
        counts = {"b": 5, "a": 5, "c": 1, "z": 0}
        out = s._top(counts, 2)
        # ties broken alphabetically; zero-count dropped.
        self.assertEqual(out, [("a", 5), ("b", 5)])


class ComputeStatsTests(unittest.TestCase):
    def test_empty_dataframe_returns_zeroed_stats(self):
        st = s.compute_stats(pd.DataFrame())
        self.assertIsInstance(st, s.DashboardStats)
        self.assertEqual(st.total_words, 0)
        self.assertEqual(st.mastered, 0)
        self.assertEqual(st.definitions_pct, 0.0)

    def test_counts_totals_favorites_languages_and_status(self):
        df = pd.DataFrame(
            [
                {
                    "Language1": "English",
                    "Language2": "German",
                    "Word1": "a",
                    "Status": "Mastered",
                    "favorite": 1,
                    "created_at": _ago(0).isoformat(),
                },
                {
                    "Language1": "English",
                    "Language2": "German",
                    "Word1": "b",
                    "Status": "New",
                    "favorite": 0,
                    "created_at": _ago(1).isoformat(),
                },
                {
                    "Language1": "English",
                    "Language2": "French",
                    "Word1": "c",
                    "Status": "Reviewing",
                    "favorite": 0,
                    "created_at": _ago(1).isoformat(),
                },
            ]
        )
        st = s.compute_stats(df, tag_counts={"verb": 3, "noun": 1}, definition_counts=(2, 3))
        self.assertEqual(st.total_words, 3)
        self.assertEqual(st.favorites, 1)
        self.assertEqual(st.language_count, 3)  # English, German, French
        self.assertEqual(st.mastered, 1)
        self.assertEqual(st.status_counts["Mastered"], 1)
        self.assertEqual(st.in_progress, 1)  # only "Reviewing"
        self.assertAlmostEqual(st.definitions_pct, 100.0 * 2 / 3)
        self.assertEqual(st.top_tags[0], ("verb", 3))
        self.assertTrue(st.has_dates)
        self.assertEqual(st.added_today, 1)

    def test_unparseable_dates_are_dropped_from_series_but_counted(self):
        df = pd.DataFrame(
            [
                {"Word1": "a", "Status": "New", "created_at": "not-a-date"},
                {"Word1": "b", "Status": "New", "created_at": _ago(0).isoformat()},
            ]
        )
        st = s.compute_stats(df)
        self.assertEqual(st.total_words, 2)  # both counted
        self.assertTrue(st.has_dates)
        self.assertEqual(st.added_today, 1)  # only the parseable one


class ResampleAndHeatmapTests(unittest.TestCase):
    def _daily(self, span_days=30):
        return [(_ago(span_days - 1 - i), i % 3) for i in range(span_days)]

    def test_resample_day_is_identity(self):
        daily = self._daily()
        self.assertEqual(s.resample(daily, "day"), daily)

    def test_resample_max_points_keeps_most_recent(self):
        daily = self._daily()
        out = s.resample(daily, "day", max_points=5)
        self.assertEqual(out, daily[-5:])

    def test_resample_week_aggregates(self):
        daily = self._daily(14)
        out = s.resample(daily, "week")
        self.assertTrue(out)
        self.assertEqual(sum(c for _, c in out), sum(c for _, c in daily))

    def test_heatmap_grid_shape(self):
        grid = s.heatmap_weeks(self._daily(30), weeks=10)
        self.assertEqual(len(grid["columns"]), 10)
        for col in grid["columns"]:
            self.assertEqual(len(col), 7)  # Mon..Sun
        self.assertIn("max", grid)
        self.assertGreaterEqual(grid["max"], 0)


if __name__ == "__main__":
    unittest.main()
