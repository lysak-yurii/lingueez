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

"""Login autostart for the Microsoft Store (MSIX) build.

The packaged build cannot use the ``HKCU\\...\\Run`` key the plain `.exe` writes:
MSIX copies every ``HKCU`` write into the package's own private hive, so the
value reads back intact while Windows never sees it at logon. The supported
mechanism is the ``windows.startupTask`` extension declared in
``packaging/msix/AppxManifest.xml`` plus the ``Windows.ApplicationModel``
`StartupTask` WinRT API, which is what this module wraps.

Two things follow from that API and shape everything below:

* The user owns the final say. Switching the entry off in Settings -> Apps ->
  Startup puts it in ``DISABLED_BY_USER``, and ``RequestEnableAsync`` then does
  nothing — so the UI has to *show* that rather than offer a dead toggle.
* A startup task takes no arguments, so ``--minimized`` cannot be passed. The
  app asks Windows how it was activated instead (:func:`launched_at_startup`).

Every entry point is inert (``False``/``None``) off the Store build, so callers
can use it unconditionally; :func:`app.system.package_env.is_msix` is the gate.
"""
import logging
import threading

from app.system.package_env import is_msix

# Must match <desktop:StartupTask TaskId="..."> in packaging/msix/AppxManifest.xml —
# an id Windows does not know returns no task at all. tests/test_msix_startup_task.py
# guards the pairing.
TASK_ID = "LingueezAutostart"

# StartupTaskState member names. Compared by name rather than value so the
# numbering of the WinRT enum is never baked into this file.
_ENABLED_STATES = frozenset({"ENABLED", "ENABLED_BY_POLICY"})
_LOCKED_STATES = frozenset({"DISABLED_BY_USER", "DISABLED_BY_POLICY"})

# Generous ceiling for a process-local call that normally returns in milliseconds;
# it exists so a wedged WinRT call can never hang the GUI thread.
_CALL_TIMEOUT = 5.0

_activation_cache = None


def _off_gui_thread(fn, default):
    """Run *fn* on a fresh thread and return its result, or *default* on failure.

    Qt OleInitialize()s the GUI thread as an STA, and pywinrt's blocking
    ``IAsyncOperation.get()`` raises RuntimeError when called from one. A plain
    worker thread joins the MTA on first WinRT use, which makes ``get()`` legal
    and leaves Qt's apartment alone.
    """
    box = [default]

    def run():
        try:
            box[0] = fn()
        except Exception as exc:
            logging.warning(f"Startup task query failed: {exc}")

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    thread.join(_CALL_TIMEOUT)
    return box[0]


def _fetch_task():
    from winrt.windows.applicationmodel import StartupTask
    return StartupTask.get_async(TASK_ID).get()


def state_name():
    """Current ``StartupTaskState`` as its member name, or None when unavailable."""
    if not is_msix():
        return None
    return _off_gui_thread(lambda: _fetch_task().state.name, None)


def is_enabled() -> bool:
    return state_name() in _ENABLED_STATES


def is_locked() -> bool:
    """True when the state is the user's or an admin policy's to change, not ours."""
    return state_name() in _LOCKED_STATES


def set_enabled(enabled: bool):
    """Ask Windows to enable/disable the startup entry; returns the resulting
    state name (None when unavailable).

    Enabling is a *request*: Windows may prompt, and it is silently refused once
    the entry sits in one of the :data:`_LOCKED_STATES`. Callers should compare
    the returned state against what they asked for.
    """
    if not is_msix():
        return None

    def apply():
        task = _fetch_task()
        if enabled:
            return task.request_enable_async().get().name
        task.disable()
        return task.state.name

    return _off_gui_thread(apply, None)


def launched_at_startup() -> bool:
    """Whether this process was started by the login startup task.

    Cached: ``GetActivatedEventArgs`` yields the activation arguments only on its
    first call in a process, so the answer has to be taken once and kept.
    """
    global _activation_cache
    if _activation_cache is not None:
        return _activation_cache

    def query():
        from winrt.windows.applicationmodel import AppInstance
        from winrt.windows.applicationmodel.activation import ActivationKind
        args = AppInstance.get_activated_event_args()
        return args is not None and args.kind == ActivationKind.STARTUP_TASK

    _activation_cache = _off_gui_thread(query, False) if is_msix() else False
    return _activation_cache
