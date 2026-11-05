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


class ChannelTests(unittest.TestCase):
    def setUp(self):
        package_env._msix_cache = None
        self.addCleanup(setattr, package_env, "_msix_cache", None)

    def _channel(self, *, msix=False, win_frozen=False, snap=False, flatpak=False, appimage=False):
        from unittest import mock

        from app.system import hotkey_env

        with (
            mock.patch.object(package_env, "is_msix", return_value=msix),
            mock.patch.object(package_env, "is_snap", return_value=snap),
            mock.patch.object(hotkey_env, "is_flatpak", return_value=flatpak),
            mock.patch.object(package_env, "is_appimage", return_value=appimage),
            mock.patch.object(package_env.sys, "platform", "win32" if win_frozen else "linux"),
            mock.patch.object(package_env.sys, "frozen", win_frozen, create=True),
        ):
            return package_env.channel()

    def test_each_install_type(self):
        self.assertEqual(self._channel(msix=True, win_frozen=True), "msix")
        self.assertEqual(self._channel(win_frozen=True), "windows-installer")
        self.assertEqual(self._channel(snap=True), "snap")
        self.assertEqual(self._channel(flatpak=True), "flatpak")
        self.assertEqual(self._channel(appimage=True), "appimage")
        self.assertEqual(self._channel(), "source")
        self.assertIn(self._channel(), package_env.CHANNELS)

    def test_appimage_needs_this_module_inside_its_mount(self):
        from unittest import mock

        outside = {"APPIMAGE": "/tmp/x.AppImage", "APPDIR": "/tmp/.mount_x"}
        with mock.patch.dict(os.environ, outside):
            self.assertFalse(package_env.is_appimage())
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        inside = {"APPIMAGE": "/tmp/x.AppImage", "APPDIR": here}
        with mock.patch.dict(os.environ, inside):
            self.assertTrue(package_env.is_appimage())


if __name__ == "__main__":
    unittest.main()
