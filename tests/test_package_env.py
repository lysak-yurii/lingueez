# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for MSIX package-identity detection.

Run with the project venv:  python -m unittest tests.test_package_env
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.system import package_env  # noqa: E402


class IsMsixTests(unittest.TestCase):
    def setUp(self):
        # is_msix() caches its answer; reset between tests so each starts clean.
        package_env._msix_cache = None

    def tearDown(self):
        package_env._msix_cache = None

    @unittest.skipIf(sys.platform == "win32", "non-Windows behaviour only")
    def test_false_off_windows(self):
        self.assertFalse(package_env.is_msix())

    def test_result_is_cached(self):
        # First call resolves and caches; a poisoned cache is returned verbatim,
        # proving the second call doesn't re-probe.
        package_env.is_msix()
        package_env._msix_cache = "sentinel"
        self.assertEqual(package_env.is_msix(), "sentinel")


if __name__ == "__main__":
    unittest.main()
