# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for when Quick Save generates a definition on its own.

Run:  python -m unittest tests.test_definition_autogen
"""

import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core import ai  # noqa: E402
from app.core import definition_autogen as autogen  # noqa: E402


def _settings(on=True, failures=0):
    return {autogen.ENABLED_KEY: str(on), autogen.FAILURES_KEY: str(failures)}


class EnabledTests(unittest.TestCase):
    def test_needs_both_the_switch_and_a_key(self):
        with mock.patch.object(ai, "has_api_key", return_value=True):
            self.assertTrue(autogen.enabled(_settings(on=True)))
            self.assertFalse(autogen.enabled(_settings(on=False)))
        with mock.patch.object(ai, "has_api_key", return_value=False):
            self.assertFalse(autogen.enabled(_settings(on=True)))

    def test_no_key_switches_it_off(self):
        settings = _settings(on=True, failures=2)
        with mock.patch.object(ai, "has_api_key", return_value=False):
            self.assertTrue(autogen.disable_if_unavailable(settings))
        self.assertEqual(settings, _settings(on=False))

    def test_a_key_or_an_off_switch_leaves_it_alone(self):
        on = _settings(on=True, failures=1)
        with mock.patch.object(ai, "has_api_key", return_value=True):
            self.assertFalse(autogen.disable_if_unavailable(on))
        self.assertEqual(on, _settings(on=True, failures=1))
        off = _settings(on=False)
        with mock.patch.object(ai, "has_api_key", return_value=False):
            self.assertFalse(autogen.disable_if_unavailable(off))


class OutcomeTests(unittest.TestCase):
    def test_a_success_forgives_earlier_failures(self):
        settings = _settings()
        self.assertEqual(autogen.record_outcome(settings, False), "failed")
        self.assertEqual(autogen.record_outcome(settings, False), "failed")
        self.assertEqual(autogen.record_outcome(settings, True), "ok")
        self.assertEqual(settings, _settings(on=True, failures=0))

    def test_three_failures_in_a_row_turn_it_off(self):
        settings = _settings()
        outcomes = [autogen.record_outcome(settings, False) for _ in range(3)]
        self.assertEqual(outcomes, ["failed", "failed", "turned_off"])
        self.assertEqual(settings, _settings(on=False, failures=0))

    def test_switching_it_on_by_hand_resets_the_count(self):
        settings = _settings(on=False, failures=2)
        autogen.set_enabled(settings, True)
        self.assertEqual(settings, _settings(on=True, failures=0))
        self.assertEqual(autogen.record_outcome(settings, False), "failed")


if __name__ == "__main__":
    unittest.main()
