# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for the pure playback-progression ladder.

Run:  python -m unittest tests.test_progression
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import progression as p  # noqa: E402


class NormalizeThresholdsTests(unittest.TestCase):
    def test_defaults_are_strictly_increasing(self):
        th = p.normalize_thresholds()
        self.assertEqual(th, {"Reviewing": 3, "Learning": 15, "Mastered": 100})
        self.assertLess(th["Reviewing"], th["Learning"])
        self.assertLess(th["Learning"], th["Mastered"])

    def test_clamps_non_increasing_values(self):
        # learning <= reviewing and mastered <= learning must be bumped up.
        th = p.normalize_thresholds(reviewing=10, learning=5, mastered=1)
        self.assertEqual(th, {"Reviewing": 10, "Learning": 11, "Mastered": 12})

    def test_floor_of_one_for_reviewing(self):
        th = p.normalize_thresholds(reviewing=0, learning=0, mastered=0)
        self.assertEqual(th, {"Reviewing": 1, "Learning": 2, "Mastered": 3})

    def test_coerces_floats_and_strings(self):
        th = p.normalize_thresholds(reviewing="4", learning=8.9, mastered="50")
        self.assertEqual(th, {"Reviewing": 4, "Learning": 8, "Mastered": 50})


class LevelForCountTests(unittest.TestCase):
    def setUp(self):
        self.th = p.normalize_thresholds(3, 15, 100)

    def test_below_first_threshold_is_new(self):
        self.assertEqual(p.level_for_count(0, self.th), "New")
        self.assertEqual(p.level_for_count(2, self.th), "New")

    def test_boundaries_are_inclusive(self):
        self.assertEqual(p.level_for_count(3, self.th), "Reviewing")
        self.assertEqual(p.level_for_count(14, self.th), "Reviewing")
        self.assertEqual(p.level_for_count(15, self.th), "Learning")
        self.assertEqual(p.level_for_count(99, self.th), "Learning")
        self.assertEqual(p.level_for_count(100, self.th), "Mastered")
        self.assertEqual(p.level_for_count(10_000, self.th), "Mastered")

    def test_accepts_tuple_thresholds(self):
        self.assertEqual(p.level_for_count(15, (3, 15, 100)), "Learning")


class NextStatusTests(unittest.TestCase):
    def setUp(self):
        self.th = p.normalize_thresholds(3, 15, 100)

    def test_promotes_new_to_reviewing(self):
        self.assertEqual(p.next_status("New", 3, self.th), "Reviewing")

    def test_empty_status_treated_as_new(self):
        self.assertEqual(p.next_status("", 3, self.th), "Reviewing")
        self.assertEqual(p.next_status(None, 3, self.th), "Reviewing")

    def test_promotes_across_multiple_rungs_at_once(self):
        # A New word with 100 listens jumps straight to Mastered.
        self.assertEqual(p.next_status("New", 100, self.th), "Mastered")

    def test_no_promotion_when_count_below_next_rung(self):
        self.assertIsNone(p.next_status("New", 2, self.th))
        self.assertIsNone(p.next_status("Reviewing", 14, self.th))

    def test_never_demotes(self):
        # Learning word with only a few listens stays put (no demotion to Reviewing).
        self.assertIsNone(p.next_status("Learning", 3, self.th))

    def test_mastered_is_not_promotable(self):
        self.assertIsNone(p.next_status("Mastered", 10_000, self.th))

    def test_non_ladder_statuses_left_untouched(self):
        for status in ("Ignored", "To Learn", "Custom"):
            self.assertIsNone(p.next_status(status, 10_000, self.th))

    def test_case_and_whitespace_insensitive_for_promotability(self):
        self.assertEqual(p.next_status("  reviewing ", 15, self.th), "Learning")


if __name__ == "__main__":
    unittest.main()
