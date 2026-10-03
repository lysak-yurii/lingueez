# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Additional terms under AGPL-3.0 section 7 apply to this program; see the
# NOTICE file distributed with this source for details.
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Local plugins: Python packages dropped into ``plugins/`` in the data dir.

Each ``plugins/<id>/__init__.py`` defines ``register(api)`` and receives a
:class:`PluginAPI`. ``register`` runs during startup, after the UI language is
set but before the main window module is imported, so a plugin may patch app
classes; the window itself arrives later through ``api.on_window_ready``.
Plugins run in-process with the app's full rights.

An optional ``plugin.toml`` next to ``__init__.py`` describes the plugin::

    name = "Grammar"
    version = "1.0"
    description = "Every form of a word."
    author = "Someone"
    homepage = "https://example.org"
    min_app_version = "2.1"      # not loaded on an older app
    tested_app_version = "2.1"   # warns on a newer app

Without it the folder name and the module docstring are shown instead. Plugins
are switched on and off in Settings (the ``plugins_disabled`` setting); folders
starting with ``.`` or ``_`` are not plugins at all.
"""

import ast
import importlib.util
import logging
import os
import sys
import tomllib
import traceback
import types
from dataclasses import dataclass

from app.version import APP_VERSION

PLUGINS_DIR = "plugins"
MANIFEST = "plugin.toml"
_PACKAGE = "lingueez_plugins"
# Names the plugins being started; still there on the next start if the app died.
_MARKER = ".starting"

ACTIVE, DISABLED, INCOMPATIBLE, FAILED, CRASHED = (
    "active", "disabled", "incompatible", "failed", "crashed")

_current = None


def current():
    """The manager created at startup, or None (tests, the hotkey agent)."""
    return _current


def split_ids(value):
    return {part.strip() for part in str(value or "").split(",") if part.strip()}


def join_ids(ids):
    return ",".join(sorted(ids))


def _version(text):
    parts = []
    for part in str(text).strip().split("."):
        if not part.isdigit():
            break
        parts.append(int(part))
    return tuple(parts)


@dataclass
class PluginInfo:
    id: str
    path: str
    name: str
    version: str = ""
    description: str = ""
    author: str = ""
    homepage: str = ""
    min_app_version: str = ""
    tested_app_version: str = ""
    status: str = DISABLED
    error: str = ""   # traceback of a failed load
    untested: bool = False


def _read_info(plugin_id, path):
    info = PluginInfo(plugin_id, path, plugin_id)
    try:
        with open(os.path.join(path, MANIFEST), "rb") as fh:
            manifest = tomllib.load(fh)
    except FileNotFoundError:
        manifest = {}
    except (OSError, tomllib.TOMLDecodeError) as exc:
        logging.warning(f"Plugin '{plugin_id}': unreadable {MANIFEST}: {exc}")
        manifest = {}
    for key in ("name", "version", "description", "author", "homepage",
                "min_app_version", "tested_app_version"):
        value = manifest.get(key)
        if isinstance(value, (str, int, float)) and str(value).strip():
            setattr(info, key, str(value).strip())
    if not info.description:
        try:
            with open(os.path.join(path, "__init__.py"), encoding="utf-8") as fh:
                doc = ast.get_docstring(ast.parse(fh.read())) or ""
            info.description = " ".join(doc.split("\n\n")[0].split())
        except (OSError, SyntaxError, ValueError):
            pass
    return info


class PluginAPI:
    """What a plugin may call. ``window`` (None until the main window is built)
    is the escape hatch to everything else."""

    def __init__(self, plugin_id, path):
        self.window = None
        self.id = plugin_id
        self.path = path
        self.log = logging.getLogger(f"{_PACKAGE}.{plugin_id}")
        self._window_callbacks = []
        self._quit_callbacks = []

    def on_window_ready(self, callback):
        """Call ``callback(window)`` once the main window is built."""
        self._window_callbacks.append(callback)

    def on_quit(self, callback):
        self._quit_callbacks.append(callback)


class PluginManager:
    def __init__(self, directory=PLUGINS_DIR, disabled=(), crashed=(),
                 app_version=APP_VERSION, safe_mode=False):
        """``disabled`` are the ids switched off in Settings; ``crashed`` those
        among them that an earlier :meth:`load_all` switched off itself.
        ``safe_mode`` (``--no-plugins``) lists the plugins without loading any."""
        global _current
        _current = self
        self.directory = directory
        self.disabled = set(disabled)
        self.app_version = app_version
        self.safe_mode = safe_mode
        self.plugins = {}   # id -> PluginInfo, everything found on disk
        self.loaded = {}    # id -> PluginAPI, what is running
        self.crashed = []   # ids switched off by this start
        self._crashed_before = set(crashed)

    def discover(self):
        self.plugins = {}
        if not os.path.isdir(self.directory):
            return
        for name in sorted(os.listdir(self.directory)):
            path = os.path.join(self.directory, name)
            if name.startswith((".", "_")) or not os.path.isfile(
                    os.path.join(path, "__init__.py")):
                continue
            info = _read_info(name, os.path.abspath(path))
            # "2.1" covers every 2.1.x.
            newest = _version(info.tested_app_version)
            info.untested = newest < _version(self.app_version)[:len(newest)]
            self.plugins[name] = info

    def load_all(self):
        self.discover()
        if self.safe_mode or not self.plugins:
            return
        suspects = self._read_marker()
        for plugin_id, info in self.plugins.items():
            if plugin_id in suspects:
                logging.warning(f"Plugin '{plugin_id}' switched off: the app "
                                f"did not finish starting with it last time")
                self.crashed.append(plugin_id)
                self.disabled.add(plugin_id)
                info.status = CRASHED
            elif plugin_id in self.disabled:
                info.status = (CRASHED if plugin_id in self._crashed_before
                               else DISABLED)
            elif _version(info.min_app_version) > _version(self.app_version):
                logging.warning(f"Plugin '{plugin_id}' needs app version "
                                f"{info.min_app_version}; skipped")
                info.status = INCOMPATIBLE
            else:
                self._write_marker([plugin_id])
                self._load(info)
        # Class patches bite while the window is built, so every running plugin
        # stays under suspicion until window_ready is through.
        self._write_marker(self.loaded)

    def _load(self, info):
        plugin_id, path = info.id, info.path
        module_name = f"{_PACKAGE}.{plugin_id}"
        # Relative imports inside a plugin resolve through this parent package.
        sys.modules.setdefault(_PACKAGE, types.ModuleType(_PACKAGE)).__path__ = []
        api = PluginAPI(plugin_id, path)
        try:
            spec = importlib.util.spec_from_file_location(
                module_name, os.path.join(path, "__init__.py"),
                submodule_search_locations=[path])
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            module.register(api)
        except Exception:
            sys.modules.pop(module_name, None)
            logging.exception(f"Plugin '{plugin_id}' failed to load; skipped")
            info.status, info.error = FAILED, traceback.format_exc()
            return
        self.loaded[plugin_id] = api
        info.status = ACTIVE
        logging.info(f"Plugin '{plugin_id}' loaded")

    def window_ready(self, window):
        for plugin_id, api in self.loaded.items():
            api.window = window
            self._run(plugin_id, api._window_callbacks, "window setup", window)
        self._write_marker([])

    def shutdown(self):
        for plugin_id, api in self.loaded.items():
            self._run(plugin_id, api._quit_callbacks, "quit")

    def _read_marker(self):
        try:
            with open(os.path.join(self.directory, _MARKER), encoding="utf-8") as fh:
                return set(fh.read().split())
        except OSError:
            return set()

    def _write_marker(self, plugin_ids):
        path = os.path.join(self.directory, _MARKER)
        try:
            if plugin_ids:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write("\n".join(plugin_ids))
            elif os.path.exists(path):
                os.remove(path)
        except OSError:
            logging.warning("Could not update the plugin start marker", exc_info=True)

    @staticmethod
    def _run(plugin_id, callbacks, stage, *args):
        for callback in callbacks:
            try:
                callback(*args)
            except Exception:
                logging.exception(f"Plugin '{plugin_id}' failed on {stage}")
