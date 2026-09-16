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

"""Telling an X11 compositor that a window is mid-repaint.

A window that resizes itself flickers on X11: the compositor goes on showing
the window's last frame, stretched to the new size, until the repaint reaches
the screen — everything inside slides and springs back for a few frames. The
cure is the extended half of the _NET_WM_SYNC_REQUEST protocol: a window
publishes a second sync counter, sets it to an odd value while it is drawing a
frame and back to even when that frame is on the way, and the compositor holds
what it has instead of stretching it. GTK does this for every frame, which is
why GTK windows resize cleanly where Qt ones do not — Qt publishes only the
first counter, the one it answers the window manager's own resizes with.

FrameSync adds the second counter. It has to be installed before the window is
mapped, because that is when the compositor reads the property. Everything here
is a no-op off X11, and a held frame is always released by a timer, so a
window can never be left frozen.
"""
import ctypes
import ctypes.util
import sys

from PySide6.QtCore import QEvent, QObject, QTimer, qInstallMessageHandler
from PySide6.QtGui import QGuiApplication

XA_CARDINAL = 6
PROP_MODE_REPLACE = 0
# How long a frame may be held before the compositor is let go regardless. A
# repaint takes a few milliseconds; this is only here so that a missing paint
# event can't leave the window showing a stale frame.
HOLD_TIMEOUT_MS = 500

_libX11 = None
_libXext = None
_display = None
_forward_message = None


def _quiet_frame_messages():
    """Drop the compositor's frame replies from the log.

    Once a window publishes the second counter the compositor answers every
    held frame with _NET_WM_FRAME_DRAWN and _NET_WM_FRAME_TIMINGS, which Qt
    has no use for and warns about once per message.
    """
    global _forward_message
    if _forward_message is not None:
        return

    def handler(mode, context, message):
        if "_NET_WM_FRAME_" in message:
            return
        _forward_message(mode, context, message)

    previous = qInstallMessageHandler(handler)
    _forward_message = previous or (
        lambda mode, context, message: print(message, file=sys.stderr))


class _SyncValue(ctypes.Structure):
    _fields_ = [("hi", ctypes.c_int), ("lo", ctypes.c_uint)]


def _bind():
    """Load Xlib plus the Sync extension, or report that X11 isn't there."""
    global _libX11, _libXext, _display
    if _libX11 is not None:
        return _display is not None
    _libX11, _libXext = False, False
    if QGuiApplication.platformName() != "xcb":
        return False
    try:
        x11 = ctypes.util.find_library("X11")
        xext = ctypes.util.find_library("Xext")
        if not x11 or not xext:
            return False
        _libX11 = ctypes.CDLL(x11)
        _libXext = ctypes.CDLL(xext)
        _libX11.XInternAtom.restype = ctypes.c_ulong
        _libXext.XSyncCreateCounter.restype = ctypes.c_ulong
        _libXext.XSyncCreateCounter.argtypes = [ctypes.c_void_p, _SyncValue]
        _libXext.XSyncSetCounter.argtypes = [ctypes.c_void_p, ctypes.c_ulong,
                                             _SyncValue]
        # Qt's own connection, so our counter updates stay in order with the
        # painting they describe instead of racing it from a second connection.
        _display = ctypes.c_void_p(
            QGuiApplication.instance().nativeInterface().display())
        major, minor = ctypes.c_int(), ctypes.c_int()
        _libXext.XSyncInitialize(_display, ctypes.byref(major), ctypes.byref(minor))
    except Exception:
        _libX11, _libXext, _display = False, False, None
    return _display is not None


def _counters(window_id, atom):
    """The window's published sync counters, as Qt left them."""
    actual_type = ctypes.c_ulong()
    actual_format = ctypes.c_int()
    count = ctypes.c_ulong()
    remaining = ctypes.c_ulong()
    data = ctypes.POINTER(ctypes.c_ulong)()
    status = _libX11.XGetWindowProperty(
        _display, ctypes.c_ulong(window_id), ctypes.c_ulong(atom), 0, 2, False,
        ctypes.c_ulong(XA_CARDINAL), ctypes.byref(actual_type),
        ctypes.byref(actual_format), ctypes.byref(count),
        ctypes.byref(remaining), ctypes.byref(data))
    if status != 0 or not data:
        return []
    values = list(data[:count.value])
    _libX11.XFree(data)
    return values


class FrameSync(QObject):
    """The compositor handshake for one window; install before it is shown.

    hold() freezes what is on screen and the next repaint releases it, so a
    resize and the frame that matches it appear together.
    """

    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._counter = None
        self._value = 0
        self._held = False
        # Bumped by every hold(), so a release armed by an earlier one can't
        # let go of a frame that a later hold is still waiting for.
        self._token = 0
        self._install()
        window.destroyed.connect(self._dispose)

    def _install(self):
        if not _bind():
            return
        try:
            atom = _libX11.XInternAtom(_display, b"_NET_WM_SYNC_REQUEST_COUNTER", False)
            window_id = int(self._window.winId())  # creates the native window
            published = _counters(window_id, atom)
            if len(published) != 1:  # already extended, or not Qt's doing
                return
            self._counter = _libXext.XSyncCreateCounter(_display, _SyncValue(0, 0))
            both = (ctypes.c_long * 2)(published[0], self._counter)
            _libX11.XChangeProperty(
                _display, ctypes.c_ulong(window_id), ctypes.c_ulong(atom),
                ctypes.c_ulong(XA_CARDINAL), 32, PROP_MODE_REPLACE,
                ctypes.cast(both, ctypes.c_void_p), 2)
            _libX11.XFlush(_display)
            _quiet_frame_messages()
        except Exception:
            self._counter = None

    def hold(self):
        """Ask the compositor to keep showing this frame until the next repaint."""
        # a window that isn't on screen yet has no frame to hold and may never
        # paint to release it
        if self._counter is None or not self._window.isVisible():
            return
        self._token += 1
        token = self._token
        if not self._held:
            self._held = True
            self._set(self._value + 1)  # odd: a frame is being drawn
            self._window.installEventFilter(self)
        QTimer.singleShot(HOLD_TIMEOUT_MS, self, lambda: self._release(token))

    def eventFilter(self, watched, event):  # noqa: N802
        if self._held and watched is self._window and event.type() == QEvent.Paint:
            # after this paint pass, when the new frame has been handed over
            token = self._token
            QTimer.singleShot(0, self, lambda: self._release(token))
        return False

    def _release(self, token):
        if not self._held or token != self._token:
            return
        self._held = False
        self._window.removeEventFilter(self)
        self._set(self._value + 1)  # even: the frame is on its way

    def _dispose(self):
        """Hand the counter back; a dialog like Quick Save opens a fresh one
        every time, and counters live as long as the X connection."""
        if self._counter is not None:
            _libXext.XSyncDestroyCounter(_display, ctypes.c_ulong(self._counter))
            _libX11.XFlush(_display)
            self._counter = None

    def _set(self, value):
        self._value = value
        _libXext.XSyncSetCounter(_display, ctypes.c_ulong(self._counter),
                                 _SyncValue(value >> 32, value & 0xFFFFFFFF))
        _libX11.XFlush(_display)
