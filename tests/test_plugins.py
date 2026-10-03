# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Local plugin loading: discovery, skipping, failure isolation, the two stages.

Run:  python -m unittest tests.test_plugins
"""

import os
import shutil
import sys
import tempfile
import textwrap
import unittest
from unittest import mock

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from app.system import plugins  # noqa: E402
from app.system.plugins import PluginManager  # noqa: E402


class PluginManagerTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp(prefix="lingueez-plugins-")
        self.addCleanup(shutil.rmtree, self.dir, ignore_errors=True)
        self.window = mock.Mock()
        self.addCleanup(self._forget_modules)

    @staticmethod
    def _forget_modules():
        for name in [n for n in sys.modules if n.startswith("lingueez_plugins.")]:
            del sys.modules[name]

    def _plugin(self, name, body, **extra_files):
        path = os.path.join(self.dir, name)
        os.makedirs(path)
        files = {"__init__.py": body, **extra_files}
        for filename, text in files.items():
            with open(os.path.join(path, filename), "w", encoding="utf-8") as fh:
                fh.write(textwrap.dedent(text))

    def _load(self):
        manager = PluginManager(self.dir)
        manager.load_all()
        return manager

    def test_missing_directory_loads_nothing(self):
        manager = PluginManager(os.path.join(self.dir, "absent"))
        manager.load_all()
        self.assertEqual(manager.loaded, {})

    def test_register_receives_api_and_relative_imports_work(self):
        self._plugin(
            "hello",
            """
            from .helper import VALUE

            SEEN = []

            def register(api):
                SEEN.append((api.id, VALUE, api.window))
        """,
            **{"helper.py": "VALUE = 42\n"},
        )
        manager = self._load()
        self.assertEqual(list(manager.loaded), ["hello"])
        self.assertEqual(sys.modules["lingueez_plugins.hello"].SEEN, [("hello", 42, None)])

    def test_disabled_and_non_package_folders_are_skipped(self):
        for name in ("_off", ".hidden"):
            self._plugin(name, "def register(api):\n    raise AssertionError\n")
        os.makedirs(os.path.join(self.dir, "not_a_plugin"))
        self.assertEqual(self._load().loaded, {})

    def test_broken_plugin_does_not_stop_the_others(self):
        self._plugin("a_broken", "def register(api):\n    raise RuntimeError('boom')\n")
        self._plugin("b_syntax", "def register(api)\n")
        self._plugin("c_good", "def register(api):\n    pass\n")
        with self.assertLogs(level="ERROR"):
            manager = self._load()
        self.assertEqual(list(manager.loaded), ["c_good"])
        self.assertNotIn("lingueez_plugins.a_broken", sys.modules)

    def test_quit_callbacks_run_even_if_one_fails(self):
        self._plugin(
            "quitter",
            """
            CALLS = []

            def register(api):
                api.on_quit(lambda: 1 / 0)
                api.on_quit(lambda: CALLS.append("closed"))
        """,
        )
        manager = self._load()
        with self.assertLogs(level="ERROR"):
            manager.shutdown()
        self.assertEqual(sys.modules["lingueez_plugins.quitter"].CALLS, ["closed"])

    def test_window_arrives_after_register_and_failures_are_isolated(self):
        self._plugin(
            "a_bad_window",
            """
            def register(api):
                api.on_window_ready(lambda window: 1 / 0)
        """,
        )
        self._plugin(
            "b_windowed",
            """
            def register(api):
                api.on_window_ready(lambda window: window.touched.append(api.window))
        """,
        )
        manager = self._load()
        self.window.touched = []
        with self.assertLogs(level="ERROR"):
            manager.window_ready(self.window)
        self.assertEqual(self.window.touched, [self.window])
        self.assertIs(manager.loaded["a_bad_window"].window, self.window)

    def test_register_can_patch_app_classes_before_they_are_used(self):
        self._plugin(
            "patcher",
            """
            from app.core import languages

            def register(api):
                api.previous = languages.canonical
                languages.canonical = lambda name: "patched"
        """,
        )
        from app.core import languages

        manager = self._load()
        self.addCleanup(setattr, languages, "canonical", manager.loaded["patcher"].previous)
        self.assertEqual(languages.canonical("Greek"), "patched")

    def test_manifest_describes_the_plugin(self):
        self._plugin(
            "described",
            "def register(api):\n    pass\n",
            **{
                "plugin.toml": """
                    name = "Described"
                    version = "1.2"
                    description = "Does a thing."
                    author = "Someone"
                    homepage = "https://example.org"
                """
            },
        )
        info = self._load().plugins["described"]
        self.assertEqual(
            (info.name, info.version, info.description, info.author, info.homepage),
            ("Described", "1.2", "Does a thing.", "Someone", "https://example.org"),
        )
        self.assertEqual(info.status, plugins.ACTIVE)

    def test_without_a_manifest_the_folder_and_docstring_stand_in(self):
        self._plugin(
            "bare",
            '"""First paragraph,\nwrapped.\n\nSecond."""\n\ndef register(api):\n    pass\n',
        )
        self._plugin("broken_toml", "def register(api):\n    pass\n", **{"plugin.toml": "name = "})
        with self.assertLogs(level="WARNING"):
            manager = self._load()
        info = manager.plugins["bare"]
        self.assertEqual((info.name, info.description), ("bare", "First paragraph, wrapped."))
        self.assertEqual(manager.plugins["broken_toml"].status, plugins.ACTIVE)

    def test_disabled_plugin_is_listed_but_not_loaded(self):
        self._plugin("off", "def register(api):\n    raise AssertionError\n")
        manager = PluginManager(self.dir, disabled={"off"})
        manager.load_all()
        self.assertEqual(manager.loaded, {})
        self.assertEqual(manager.plugins["off"].status, plugins.DISABLED)

    def test_plugin_for_a_newer_app_is_not_loaded(self):
        self._plugin(
            "future",
            "def register(api):\n    raise AssertionError\n",
            **{"plugin.toml": 'min_app_version = "2.10"\n'},
        )
        self._plugin(
            "old",
            "def register(api):\n    pass\n",
            **{"plugin.toml": 'min_app_version = "2.1"\ntested_app_version = "2.8"\n'},
        )
        manager = PluginManager(self.dir, app_version="2.9.0")
        with self.assertLogs(level="WARNING"):
            manager.load_all()
        self.assertEqual(manager.plugins["future"].status, plugins.INCOMPATIBLE)
        self.assertEqual(manager.plugins["old"].status, plugins.ACTIVE)
        self.assertTrue(manager.plugins["old"].untested)
        self.assertFalse(manager.plugins["future"].untested)

    def test_tested_version_covers_its_patch_releases(self):
        self._plugin(
            "current",
            "def register(api):\n    pass\n",
            **{"plugin.toml": 'tested_app_version = "2.9"\n'},
        )
        manager = PluginManager(self.dir, app_version="2.9.3")
        manager.load_all()
        self.assertFalse(manager.plugins["current"].untested)

    def test_failed_load_keeps_its_traceback(self):
        self._plugin("boom", "def register(api):\n    raise RuntimeError('kaput')\n")
        with self.assertLogs(level="ERROR"):
            info = self._load().plugins["boom"]
        self.assertEqual(info.status, plugins.FAILED)
        self.assertIn("RuntimeError: kaput", info.error)

    def test_plugins_running_when_the_app_died_are_switched_off_next_start(self):
        self._plugin("a_fine", "def register(api):\n    pass\n")
        self._plugin("b_fatal", "def register(api):\n    pass\n")
        self._plugin("c_off", "def register(api):\n    pass\n")
        first = PluginManager(self.dir, disabled={"c_off"})
        first.load_all()  # ...and the app dies before window_ready

        with self.assertLogs(level="WARNING"):
            second = PluginManager(self.dir, disabled={"c_off"})
            second.load_all()
        self.assertEqual(second.crashed, ["a_fine", "b_fatal"])
        self.assertEqual(second.loaded, {})
        self.assertEqual(second.disabled, {"a_fine", "b_fatal", "c_off"})
        self.assertEqual(second.plugins["b_fatal"].status, plugins.CRASHED)
        self.assertEqual(second.plugins["c_off"].status, plugins.DISABLED)

        third = PluginManager(self.dir, disabled=second.disabled, crashed=second.crashed)
        third.load_all()
        self.assertEqual(third.crashed, [])
        self.assertEqual(third.plugins["a_fine"].status, plugins.CRASHED)

    def test_a_start_that_reaches_the_window_blames_nobody(self):
        self._plugin("fine", "def register(api):\n    pass\n")
        first = self._load()
        self.assertTrue(os.path.exists(os.path.join(self.dir, ".starting")))
        first.window_ready(self.window)
        self.assertFalse(os.path.exists(os.path.join(self.dir, ".starting")))
        second = self._load()
        self.assertEqual((second.crashed, list(second.loaded)), ([], ["fine"]))

    def test_a_plugin_that_kills_the_app_while_loading_is_the_only_suspect(self):
        self._plugin("a_fine", "def register(api):\n    pass\n")
        self._plugin("b_fatal", "def register(api):\n    raise SystemExit\n")
        with self.assertRaises(SystemExit):
            self._load()
        with self.assertLogs(level="WARNING"):
            manager = self._load()
        self.assertEqual(manager.crashed, ["b_fatal"])
        self.assertEqual(list(manager.loaded), ["a_fine"])

    def test_safe_mode_lists_plugins_without_loading_them(self):
        self._plugin("idle", "def register(api):\n    raise AssertionError\n")
        manager = PluginManager(self.dir, safe_mode=True)
        manager.load_all()
        self.assertEqual(manager.loaded, {})
        self.assertEqual(manager.plugins["idle"].status, plugins.DISABLED)
        self.assertFalse(os.path.exists(os.path.join(self.dir, ".starting")))


if __name__ == "__main__":
    unittest.main()
