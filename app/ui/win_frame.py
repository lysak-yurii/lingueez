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

"""Native Windows frame for the frameless main window.

The main window is frameless so its controls can live in the app's own top bar,
but on Windows that strips WS_CAPTION/WS_THICKFRAME from the HWND — and the
shell keys drag-to-snap, Snap Assist and the Windows 11 Snap Layouts flyout to
those styles and to the non-client hit test. This module puts the styles back,
removes the frame again with WM_NCCALCSIZE so nothing is drawn on top of the
app, and answers WM_NCHITTEST so the shell knows where the caption, the resize
borders and the maximize button are. Import is safe anywhere;
install_native_frame() is what touches Win32.
"""
import ctypes
from ctypes import wintypes

from PySide6.QtCore import QAbstractNativeEventFilter, QEvent, QObject, QPoint, Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from app.ui.titlebar import RESIZE_MARGIN

GWL_STYLE = -16
WS_POPUP = 0x80000000
WS_CAPTION = 0x00C00000
WS_THICKFRAME = 0x00040000
WS_SYSMENU = 0x00080000
WS_MINIMIZEBOX = 0x00020000
WS_MAXIMIZEBOX = 0x00010000
# WS_MINIMIZEBOX/WS_MAXIMIZEBOX are inert without WS_SYSMENU, and the Snap
# Layouts flyout is the maximize button's own shell UI: no effective maximize
# box, no flyout. WS_THICKFRAME is what DefWindowProc requires before it will
# start a sizing loop, so the window silently stops resizing without it.
FRAME_STYLES = (WS_CAPTION | WS_THICKFRAME | WS_SYSMENU
                | WS_MINIMIZEBOX | WS_MAXIMIZEBOX)

WM_NCCALCSIZE = 0x0083
WM_NCHITTEST = 0x0084
WM_NCMOUSELEAVE = 0x02A2
WM_NCLBUTTONDOWN = 0x00A1
WM_NCLBUTTONUP = 0x00A2
WM_NCLBUTTONDBLCLK = 0x00A3
WM_WINDOWPOSCHANGED = 0x0047

HTCLIENT = 1
HTCAPTION = 2
HTMAXBUTTON = 9
HTLEFT = 10
HTRIGHT = 11
HTTOP = 12
HTTOPLEFT = 13
HTTOPRIGHT = 14
HTBOTTOM = 15
HTBOTTOMLEFT = 16
HTBOTTOMRIGHT = 17

DWMWA_WINDOW_CORNER_PREFERENCE = 33
DWMWCP_DONOTROUND = 1

SM_CXSIZEFRAME = 32
SM_CXPADDEDBORDER = 92
SW_SHOWMAXIMIZED = 3

SWP_NOSIZE = 0x0001
SWP_NOMOVE = 0x0002
SWP_NOZORDER = 0x0004
SWP_NOACTIVATE = 0x0010
SWP_FRAMECHANGED = 0x0020

ABM_GETSTATE = 0x00000004
ABM_GETTASKBARPOS = 0x00000005
ABS_AUTOHIDE = 0x00000001
ABE_LEFT = 0
ABE_TOP = 1
ABE_RIGHT = 2
ABE_BOTTOM = 3

# Bound by _bind() on first use: ctypes.windll does not exist off Windows, and
# the release smoke test imports every module under app/ on Linux too.
_user32 = None
_shell32 = None
_dwmapi = None
_get_window_long = None
_set_window_long = None
_get_dpi_for_window = None
_get_metrics_for_dpi = None


class _WindowPlacement(ctypes.Structure):
    _fields_ = [("length", wintypes.UINT),
                ("flags", wintypes.UINT),
                ("showCmd", wintypes.UINT),
                ("ptMinPosition", wintypes.POINT),
                ("ptMaxPosition", wintypes.POINT),
                ("rcNormalPosition", wintypes.RECT)]


class _NcCalcSizeParams(ctypes.Structure):
    _fields_ = [("rgrc", wintypes.RECT * 3), ("lppos", ctypes.c_void_p)]


class _AppBarData(ctypes.Structure):
    _fields_ = [("cbSize", wintypes.DWORD),
                ("hWnd", wintypes.HWND),
                ("uCallbackMessage", wintypes.UINT),
                ("uEdge", wintypes.UINT),
                ("rc", wintypes.RECT),
                ("lParam", ctypes.c_ssize_t)]


class _Msg(ctypes.Structure):
    _fields_ = [("hWnd", wintypes.HWND),
                ("message", wintypes.UINT),
                ("wParam", ctypes.c_size_t),
                ("lParam", ctypes.c_ssize_t),
                ("time", wintypes.DWORD),
                ("pt", wintypes.POINT)]


def _bind():
    """Resolve the Win32 entry points this module needs."""
    global _user32, _shell32, _dwmapi, _get_window_long, _set_window_long
    global _get_dpi_for_window, _get_metrics_for_dpi
    if _user32 is not None:
        return
    user32 = ctypes.windll.user32
    shell32 = ctypes.windll.shell32
    # The Ptr variants only exist on 64-bit; the plain ones are the same call.
    get_long = getattr(user32, "GetWindowLongPtrW", None) or user32.GetWindowLongW
    get_long.argtypes = [wintypes.HWND, ctypes.c_int]
    get_long.restype = ctypes.c_ssize_t
    set_long = getattr(user32, "SetWindowLongPtrW", None) or user32.SetWindowLongW
    set_long.argtypes = [wintypes.HWND, ctypes.c_int, ctypes.c_ssize_t]
    set_long.restype = ctypes.c_ssize_t
    user32.GetWindowRect.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.RECT)]
    user32.GetWindowPlacement.argtypes = [wintypes.HWND,
                                          ctypes.POINTER(_WindowPlacement)]
    user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, ctypes.c_int,
                                    ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                    wintypes.UINT]
    shell32.SHAppBarMessage.argtypes = [wintypes.DWORD, ctypes.POINTER(_AppBarData)]
    shell32.SHAppBarMessage.restype = ctypes.c_size_t
    _get_dpi_for_window = getattr(user32, "GetDpiForWindow", None)
    _get_metrics_for_dpi = getattr(user32, "GetSystemMetricsForDpi", None)
    _get_window_long, _set_window_long = get_long, set_long
    _user32, _shell32 = user32, shell32
    try:
        _dwmapi = ctypes.windll.dwmapi
    except OSError:
        _dwmapi = None


def _frame_thickness(hwnd):
    """Width of the sizing frame, which a maximized window is inflated by."""
    if _get_dpi_for_window is not None and _get_metrics_for_dpi is not None:
        dpi = _get_dpi_for_window(hwnd)
        if dpi:
            return (_get_metrics_for_dpi(SM_CXSIZEFRAME, dpi)
                    + _get_metrics_for_dpi(SM_CXPADDEDBORDER, dpi))
    return (_user32.GetSystemMetrics(SM_CXSIZEFRAME)
            + _user32.GetSystemMetrics(SM_CXPADDEDBORDER))


def _is_maximized(hwnd):
    # Read the native placement rather than Qt's window state: WM_NCCALCSIZE
    # arrives while the state change is still in flight, so Qt's is stale.
    placement = _WindowPlacement()
    placement.length = ctypes.sizeof(placement)
    if not _user32.GetWindowPlacement(hwnd, ctypes.byref(placement)):
        return False
    return placement.showCmd == SW_SHOWMAXIMIZED


def _autohide_taskbar_edge():
    """The screen edge an auto-hiding taskbar sits on, or None."""
    data = _AppBarData()
    data.cbSize = ctypes.sizeof(data)
    if not _shell32.SHAppBarMessage(ABM_GETSTATE, ctypes.byref(data)) & ABS_AUTOHIDE:
        return None
    position = _AppBarData()
    position.cbSize = ctypes.sizeof(position)
    if _shell32.SHAppBarMessage(ABM_GETTASKBARPOS, ctypes.byref(position)):
        return position.uEdge
    return None


def _accepts_mouse(widget):
    """Whether a press on `widget` is consumed instead of reaching the drag area.

    Native hit testing decides the caption region before Qt sees the click, so
    Qt's propagation has to be predicted here. QLabel overrides mousePressEvent
    but ignores the event unless its text is interactive.
    """
    if isinstance(widget, QLabel):
        return widget.textInteractionFlags() != Qt.NoTextInteraction
    return type(widget).mousePressEvent is not QWidget.mousePressEvent


class NativeFrame(QObject, QAbstractNativeEventFilter):
    """Restores the native frame behaviours on a frameless main window."""

    def __init__(self, window, drag_area, controls):
        super().__init__(window)
        self._window = window
        self._drag_area = drag_area
        self._controls = controls
        self._hwnd = int(window.winId())
        self._restyling = False
        window.installEventFilter(self)

    # ---------- native window setup ----------

    def apply_styles(self):
        """Put the native frame styles back on the current HWND."""
        hwnd = self._hwnd
        style = _get_window_long(hwnd, GWL_STYLE)
        # WS_POPUP is what Qt gives a frameless window, and the shell leaves
        # popups out of the snap features whatever else they carry.
        _set_window_long(hwnd, GWL_STYLE, (style & ~WS_POPUP) | FRAME_STYLES)
        _user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE
                             | SWP_NOZORDER | SWP_NOACTIVATE | SWP_FRAMECHANGED)
        # WS_THICKFRAME makes Windows 11 round the corners, which would clip the
        # square 1px border the app paints itself; unsupported before Win11.
        if _dwmapi is not None:
            preference = ctypes.c_int(DWMWCP_DONOTROUND)
            _dwmapi.DwmSetWindowAttribute(
                wintypes.HWND(hwnd), DWMWA_WINDOW_CORNER_PREFERENCE,
                ctypes.byref(preference), ctypes.sizeof(preference))

    def ensure_styles(self):
        """Re-apply the frame styles whenever something has dropped them.

        Qt writes GWL_STYLE from its own cached flags (which still say
        frameless) on show and on window-state changes, so the styles can't be
        set once and trusted: they go missing without a single Qt-level event
        to hang the re-apply on, and a window that merely lacks WS_THICKFRAME
        still moves and paints normally — it just never resizes again.
        """
        if self._restyling:
            return
        style = _get_window_long(self._hwnd, GWL_STYLE)
        if style & FRAME_STYLES == FRAME_STYLES and not style & WS_POPUP:
            return
        self._restyling = True   # apply_styles re-enters through SetWindowPos
        try:
            self.apply_styles()
        finally:
            self._restyling = False

    def eventFilter(self, obj, event):
        if obj is not self._window:
            return False
        # Qt destroys and recreates the HWND on some state changes; the styles
        # go with it, so re-apply them against the new handle.
        if event.type() == QEvent.WinIdChange:
            self._hwnd = int(self._window.winId())
            self.apply_styles()
        elif event.type() in (QEvent.Show, QEvent.WindowStateChange):
            self.ensure_styles()
        return False

    # ---------- message handling ----------

    def nativeEventFilter(self, event_type, message):
        if event_type != b"windows_generic_MSG":
            return False, 0
        try:
            msg = _Msg.from_address(int(message))
        except (TypeError, ValueError):
            return False, 0
        if msg.hWnd != self._hwnd:
            return False, 0

        if msg.message == WM_NCCALCSIZE:
            self._trim_client_area(msg)
            return True, 0

        if msg.message == WM_NCHITTEST:
            hit = self._hit_test(msg.lParam)
            if hit is None:
                return False, 0
            self._controls.set_max_hover(hit == HTMAXBUTTON)
            return True, hit

        if msg.message == WM_WINDOWPOSCHANGED:
            # Fires after every show, move, resize and z-order change — the
            # cheapest hook that covers whatever Qt restyles behind our back.
            self.ensure_styles()
            return False, 0

        if msg.message == WM_NCMOUSELEAVE:
            self._controls.set_max_hover(False)
            return False, 0

        # Claiming HTMAXBUTTON routes the button's own clicks through the
        # non-client messages, so the maximize has to be driven from here.
        if msg.message in (WM_NCLBUTTONDOWN, WM_NCLBUTTONDBLCLK):
            if msg.wParam == HTMAXBUTTON:
                return True, 0
        elif msg.message == WM_NCLBUTTONUP and msg.wParam == HTMAXBUTTON:
            self._controls.toggle_maximize()
            return True, 0
        return False, 0

    def _trim_client_area(self, msg):
        """Drop the non-client frame so the app paints over the whole window."""
        if not msg.wParam:
            return
        rect = _NcCalcSizeParams.from_address(msg.lParam).rgrc[0]
        if not _is_maximized(self._hwnd) or self._window.isFullScreen():
            return
        # A maximized WS_THICKFRAME window is inflated past the work area by the
        # frame width; without this inset the content bleeds off-screen.
        thickness = _frame_thickness(self._hwnd)
        rect.left += thickness
        rect.top += thickness
        rect.right -= thickness
        rect.bottom -= thickness
        # An auto-hidden taskbar stops un-hiding once its edge is fully covered.
        edge = _autohide_taskbar_edge()
        if edge == ABE_TOP:
            rect.top += 1
        elif edge == ABE_BOTTOM:
            rect.bottom -= 1
        elif edge == ABE_LEFT:
            rect.left += 1
        elif edge == ABE_RIGHT:
            rect.right -= 1

    def _hit_test(self, lparam):
        """Map a screen position to a hit-test code, or None to fall through."""
        x = ctypes.c_short(lparam & 0xFFFF).value
        y = ctypes.c_short((lparam >> 16) & 0xFFFF).value
        rect = wintypes.RECT()
        if not _user32.GetWindowRect(self._hwnd, ctypes.byref(rect)):
            return None
        # lParam is in physical pixels; widget geometry is in logical ones.
        ratio = self._window.devicePixelRatioF() or 1.0
        local = QPoint(int((x - rect.left) / ratio), int((y - rect.top) / ratio))
        width, height = self._window.width(), self._window.height()
        if not (0 <= local.x() <= width and 0 <= local.y() <= height):
            return None

        if not (_is_maximized(self._hwnd) or self._window.isFullScreen()):
            left = local.x() <= RESIZE_MARGIN
            right = local.x() >= width - RESIZE_MARGIN
            top = local.y() <= RESIZE_MARGIN
            bottom = local.y() >= height - RESIZE_MARGIN
            if top:
                return HTTOPLEFT if left else HTTOPRIGHT if right else HTTOP
            if bottom:
                return HTBOTTOMLEFT if left else HTBOTTOMRIGHT if right else HTBOTTOM
            if left:
                return HTLEFT
            if right:
                return HTRIGHT

        if self._controls.max_button_rect().contains(local):
            return HTMAXBUTTON
        if self._is_caption(local):
            return HTCAPTION
        # Never fall through inside the window: WS_CAPTION is back on the HWND,
        # so DefWindowProc would call the whole top strip a caption.
        return HTCLIENT

    def _is_caption(self, pos):
        bar = self._drag_area
        if not bar.rect().contains(bar.mapFrom(self._window, pos)):
            return False
        child = self._window.childAt(pos)
        while child is not None and child is not bar:
            if _accepts_mouse(child):
                return False
            child = child.parentWidget()
        return True


def install_native_frame(window, drag_area, controls):
    """Hand the frameless window's frame behaviours back to Windows.

    Returns the installed filter, or None if the native setup failed — the
    caller then falls back to the Qt-side frameless handling.
    """
    app = QApplication.instance()
    frame = None
    try:
        _bind()
        frame = NativeFrame(window, drag_area, controls)
        app.installNativeEventFilter(frame)
        # Restoring the styles fires WM_NCCALCSIZE at once, so the filter has to
        # be in place first or the frame is drawn before anything trims it.
        frame.apply_styles()
    except Exception:
        if frame is not None:
            app.removeNativeEventFilter(frame)
        return None
    return frame
