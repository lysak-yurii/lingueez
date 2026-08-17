# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Keeps the MSIX startup task in step with the code that drives it.

The Store build's "start on login" is a manifest declaration plus a WinRT call
that looks the task up *by id*. Nothing links the two at build time: a renamed
TaskId, a renamed executable or a dropped extension all produce a package that
installs and runs fine while autostart silently does nothing — the exact failure
the registry Run key had. These tests are that link.

Also covers the routing in app/system/autostart.py, which must keep sending the
plain .exe and Linux to their own (untouched) backends.

Run with the project venv:  python -m unittest tests.test_msix_startup_task
"""

import os
import re
import sys
import unittest
import xml.etree.ElementTree as ET
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.system import autostart, startup_task  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(REPO, "packaging", "msix", "AppxManifest.xml")

NS = {
    "f": "http://schemas.microsoft.com/appx/manifest/foundation/windows10",
    "desktop": "http://schemas.microsoft.com/appx/manifest/desktop/windows10",
}


def _application():
    root = ET.parse(MANIFEST).getroot()
    return root.find("f:Applications/f:Application", NS)


def _startup_extension():
    for ext in _application().iterfind("f:Extensions/desktop:Extension", NS):
        if ext.get("Category") == "windows.startupTask":
            return ext
    return None


class ManifestTests(unittest.TestCase):
    def test_startup_task_is_declared(self):
        self.assertIsNotNone(
            _startup_extension(),
            "packaging/msix/AppxManifest.xml no longer declares the "
            'windows.startupTask extension — the Store build would lose "start '
            'on login" entirely (its registry Run-key writes are virtualized away).',
        )

    def test_task_id_matches_the_code(self):
        task = _startup_extension().find("desktop:StartupTask", NS)
        self.assertEqual(
            task.get("TaskId"),
            startup_task.TASK_ID,
            "TaskId must equal startup_task.TASK_ID — StartupTask.get_async() "
            "looks the task up by that id and finds nothing otherwise.",
        )

    def test_extension_points_at_the_packaged_executable(self):
        ext = _startup_extension()
        self.assertEqual(ext.get("Executable"), _application().get("Executable"))
        self.assertEqual(ext.get("EntryPoint"), "Windows.FullTrustApplication")

    def test_enabled_by_default(self):
        # Mirrors the .exe build's first-run default (MainWindow's
        # _maybe_enable_autostart_default); the user can still switch it off.
        task = _startup_extension().find("desktop:StartupTask", NS)
        self.assertEqual(task.get("Enabled"), "true")

    def test_desktop_namespace_is_ignorable(self):
        # A namespace missing from IgnorableNamespaces fails package validation.
        with open(MANIFEST, encoding="utf-8") as fh:
            text = fh.read()
        ignorable = re.search(r'IgnorableNamespaces="([^"]+)"', text).group(1)
        self.assertIn("desktop", ignorable.split())


class RoutingTests(unittest.TestCase):
    """Only a packaged process may take the startup-task path."""

    def test_msix_routes_to_the_startup_task(self):
        with (
            mock.patch.object(autostart, "is_msix", return_value=True),
            mock.patch.object(startup_task, "set_enabled") as set_enabled,
        ):
            autostart.set_autostart(True)
        set_enabled.assert_called_once_with(True)

    def test_unpackaged_windows_still_uses_the_registry(self):
        with (
            mock.patch.object(autostart, "is_msix", return_value=False),
            mock.patch.object(autostart.sys, "platform", "win32"),
            mock.patch.object(autostart, "_set_autostart_windows") as reg,
        ):
            autostart.set_autostart(True)
        reg.assert_called_once_with(True)

    def test_linux_still_writes_the_desktop_entry(self):
        with (
            mock.patch.object(autostart, "is_msix", return_value=False),
            mock.patch.object(autostart.sys, "platform", "linux"),
            mock.patch.object(autostart, "is_flatpak", return_value=False),
            mock.patch.object(autostart, "_set_autostart_linux") as desktop,
        ):
            autostart.set_autostart(True)
        desktop.assert_called_once_with(True)

    def test_sync_autostart_path_skips_the_packaged_build(self):
        # There is no recorded executable path to repair inside a package.
        with (
            mock.patch.object(autostart, "is_msix", return_value=True),
            mock.patch.object(autostart, "is_flatpak", return_value=False),
            mock.patch.object(autostart, "get_autostart_enabled") as enabled,
        ):
            autostart.sync_autostart_path()
        enabled.assert_not_called()


class InertOffStoreTests(unittest.TestCase):
    """Every startup_task entry point is a no-op without package identity, so
    callers on Linux and the .exe never need to guard their calls."""

    def setUp(self):
        startup_task._activation_cache = None

    def tearDown(self):
        startup_task._activation_cache = None

    def test_queries_return_safe_defaults(self):
        with mock.patch.object(startup_task, "is_msix", return_value=False):
            self.assertIsNone(startup_task.state_name())
            self.assertFalse(startup_task.is_enabled())
            self.assertFalse(startup_task.is_locked())
            self.assertIsNone(startup_task.set_enabled(True))
            self.assertFalse(startup_task.launched_at_startup())

    def test_a_failing_winrt_call_does_not_propagate(self):
        # WinRT is absent everywhere this suite runs, so an is_msix() that lies
        # exercises the real failure path: import error inside the worker thread.
        with mock.patch.object(startup_task, "is_msix", return_value=True):
            self.assertIsNone(startup_task.state_name())
            self.assertFalse(startup_task.launched_at_startup())

    def test_activation_is_probed_once(self):
        with (
            mock.patch.object(startup_task, "is_msix", return_value=True),
            mock.patch.object(startup_task, "_off_gui_thread", return_value=True) as probe,
        ):
            self.assertTrue(startup_task.launched_at_startup())
            self.assertTrue(startup_task.launched_at_startup())
        probe.assert_called_once()


if __name__ == "__main__":
    unittest.main()
