# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for the snap-confined code paths.

The snap only differs from a native install through environment variables snapd
sets, so every branch here is exercised by faking them — no snapd required.

Run with the project venv:  python -m unittest tests.test_snap_env
"""

import contextlib
import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main  # noqa: E402
from app.system import autostart, hotkey_env, package_env  # noqa: E402

# What snapd exports for a confined app; SNAP carries the revision, the two
# *_USER_* dirs are the writable ones (COMMON survives refresh, DATA is copied).
SNAP_ENV = {
    "SNAP": "/snap/lingueez/42",
    "SNAP_INSTANCE_NAME": "lingueez",
    "SNAP_USER_COMMON": "/home/u/snap/lingueez/common",
    "SNAP_USER_DATA": "/home/u/snap/lingueez/42",
}

# Child processes inherit SNAP_*, so a program started from a snapped terminal
# (VS Code ships as a classic snap) sees another snap's values.
LEAKED_ENV = {
    "SNAP": "/snap/code/258",
    "SNAP_INSTANCE_NAME": "code",
    "SNAP_USER_COMMON": "/home/u/snap/code/common",
    "SNAP_USER_DATA": "/home/u/snap/code/258",
}


@contextlib.contextmanager
def running_as_snap(**extra):
    """Fake being installed as the snap: snapd's environment *and* an app tree
    inside $SNAP, which is what tells our own snap apart from a leaked one."""
    env = dict(SNAP_ENV, **extra)
    inside = os.path.join(env["SNAP"], "usr", "lingueez", "app", "system", "package_env.py")
    with (
        mock.patch.dict(os.environ, env, clear=False),
        mock.patch.object(package_env, "__file__", inside),
    ):
        yield


@contextlib.contextmanager
def snap_env_leaked_from_parent():
    """Snapd's variables present, but the app tree is *not* inside that snap."""
    with mock.patch.dict(os.environ, LEAKED_ENV, clear=False):
        yield


class IsSnapTests(unittest.TestCase):
    def test_true_when_snapd_exports_snap(self):
        with running_as_snap():
            self.assertTrue(package_env.is_snap())

    def test_false_otherwise(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertFalse(package_env.is_snap())

    def test_true_when_reached_through_the_current_symlink(self):
        # /snap/<name>/current symlinks to the revision dir; $SNAP names the
        # revision. Comparing the two unresolved reports False from inside the snap.
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            rev = os.path.join(tmp, "x2")
            os.makedirs(os.path.join(rev, "usr", "lingueez", "app", "system"))
            os.symlink(rev, os.path.join(tmp, "current"))
            through_symlink = os.path.join(
                tmp, "current", "usr", "lingueez", "app", "system", "package_env.py"
            )
            with (
                mock.patch.dict(os.environ, {"SNAP": rev}, clear=False),
                mock.patch.object(package_env, "__file__", through_symlink),
            ):
                self.assertTrue(package_env.is_snap())

    def test_false_when_a_snapped_parent_leaked_its_env(self):
        # Launching the AppImage or the source tree from a snapped terminal must
        # not put the app into snap mode.
        with snap_env_leaked_from_parent():
            self.assertFalse(package_env.is_snap())


class UserDataDirTests(unittest.TestCase):
    @unittest.skipIf(sys.platform in ("win32", "darwin"), "Linux packaging only")
    def test_snap_uses_common_not_the_revisioned_dir(self):
        # XDG_DATA_HOME points into $SNAP_USER_DATA, which snapd copies on every
        # refresh — the database must not live there.
        with running_as_snap(XDG_DATA_HOME="/home/u/snap/lingueez/42/.local/share"):
            self.assertEqual(
                main._user_data_dir("Lingueez"), "/home/u/snap/lingueez/common/Lingueez"
            )

    @unittest.skipIf(sys.platform in ("win32", "darwin"), "Linux packaging only")
    def test_leaked_snap_env_does_not_move_the_database(self):
        # The frozen AppImage resolves its data dir here; a snapped parent's
        # variables must not send the library into that snap's directory.
        with snap_env_leaked_from_parent():
            with mock.patch.dict(os.environ, {"XDG_DATA_HOME": "/home/u/.local/share"}):
                self.assertEqual(main._user_data_dir("Lingueez"), "/home/u/.local/share/Lingueez")

    @unittest.skipIf(sys.platform in ("win32", "darwin"), "Linux packaging only")
    def test_native_still_follows_xdg(self):
        with mock.patch.dict(os.environ, {"XDG_DATA_HOME": "/home/u/.local/share"}, clear=True):
            self.assertEqual(main._user_data_dir("Lingueez"), "/home/u/.local/share/Lingueez")


class AutostartTests(unittest.TestCase):
    def test_entry_goes_to_the_dir_snapd_reads(self):
        # ~/.config is denied by the home interface; snapd reads its own copy.
        with running_as_snap():
            self.assertEqual(
                autostart._autostart_dir(), "/home/u/snap/lingueez/42/.config/autostart"
            )

    def test_leaked_snap_env_keeps_the_entry_in_home(self):
        with snap_env_leaked_from_parent():
            self.assertTrue(autostart._autostart_dir().endswith("/.config/autostart"))
            self.assertNotIn("/snap/code/", autostart._autostart_dir())

    def test_native_entry_stays_in_home(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertTrue(autostart._autostart_dir().endswith("/.config/autostart"))

    def test_command_is_the_revision_independent_wrapper(self):
        # $SNAP contains the revision, so recording it would strand the entry on
        # the next refresh.
        with running_as_snap():
            cmd, workdir = autostart._get_app_command_and_workdir()
        self.assertEqual(cmd, "/snap/bin/lingueez")
        self.assertNotIn("/42", cmd)
        self.assertEqual(workdir, "/home/u/snap/lingueez/common")


class HotkeyCapabilityTests(unittest.TestCase):
    def setUp(self):
        hotkey_env._portal_cache = None

    def tearDown(self):
        hotkey_env._portal_cache = None

    def test_snap_on_wayland_reports_sandboxed(self):
        # The gsettings keybinding fallback can't reach the host from confinement,
        # so the UI must degrade instead of claiming a working hotkey.
        with running_as_snap(XDG_SESSION_TYPE="wayland", XDG_CURRENT_DESKTOP="GNOME"):
            available, reason = hotkey_env.hotkey_capability()
        self.assertFalse(available)
        self.assertEqual(reason, hotkey_env.CAP_WAYLAND_SANDBOXED)

    def test_snap_on_x11_still_works(self):
        # X11 has no isolation, so the pynput agent registers the hotkey normally.
        with (
            mock.patch.dict(os.environ, {"WAYLAND_DISPLAY": ""}, clear=True),
            running_as_snap(XDG_SESSION_TYPE="x11", XDG_CURRENT_DESKTOP="GNOME"),
        ):
            os.environ.pop("WAYLAND_DISPLAY", None)
            available, reason = hotkey_env.hotkey_capability()
        self.assertTrue(available)
        self.assertEqual(reason, hotkey_env.CAP_OK)


if __name__ == "__main__":
    unittest.main()
