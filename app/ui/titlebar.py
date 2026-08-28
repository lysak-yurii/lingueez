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

"""Client-side window decorations: integrated min/max/close controls,
drag-to-move header and frameless edge resizing."""
from PySide6.QtCore import QEvent, QObject, QPoint, QRect, QSize, Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

from app.i18n import tr
from app.ui import icons

RESIZE_MARGIN = 7


class WindowControls(QWidget):
    """Minimize / maximize-restore / close buttons for a frameless window."""

    def __init__(self, window, colors):
        super().__init__(window)
        self._window = window
        self._colors = colors

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.min_btn = self._button("win-min", tr("Minimize"), window.showMinimized)
        self.max_btn = self._button("win-max", tr("Maximize"), self.toggle_maximize)
        self.close_btn = self._button("x", tr("Close"), window.close, close=True)

        window.windowHandle() and None  # noqa: B018 - handle created lazily
        window.installEventFilter(self)

    def _button(self, icon_name, tip, slot, close=False):
        btn = QPushButton(self)
        btn.setObjectName("winBtnClose" if close else "winBtn")
        btn.setIcon(icons.icon(icon_name, self._colors["text_dim"], 16))
        btn.setIconSize(QSize(15, 15))
        btn.setToolTip(tip)
        btn.setFocusPolicy(Qt.NoFocus)
        btn.setCursor(Qt.PointingHandCursor)
        btn.clicked.connect(slot)
        self.layout().addWidget(btn)
        return btn

    def set_colors(self, colors):
        """Re-tint the control icons after a theme change."""
        self._colors = colors
        self.min_btn.setIcon(icons.icon("win-min", colors["text_dim"], 16))
        maximized = self._window.isMaximized()
        self.max_btn.setIcon(icons.icon(
            "win-restore" if maximized else "win-max", colors["text_dim"], 16))
        self.close_btn.setIcon(icons.icon("x", colors["text_dim"], 16))

    def toggle_maximize(self):
        if self._window.isMaximized():
            self._window.showNormal()
        else:
            self._window.showMaximized()

    def max_button_rect(self):
        """The maximize button in top-level window coordinates."""
        return QRect(self.max_btn.mapTo(self._window, QPoint(0, 0)),
                     self.max_btn.size())

    def set_max_hover(self, hovered):
        """Drive the maximize button's hover look from outside Qt.

        On Windows the shell owns that button's rectangle (so it can offer Snap
        Layouts), which means Qt never sees enter/leave for it and the QSS
        :hover state never fires; #winBtn[ncHover] mirrors it.
        """
        if bool(self.max_btn.property("ncHover")) == bool(hovered):
            return
        self.max_btn.setProperty("ncHover", bool(hovered))
        self.max_btn.style().unpolish(self.max_btn)
        self.max_btn.style().polish(self.max_btn)

    def eventFilter(self, obj, event):
        if obj is self._window and event.type() == QEvent.WindowStateChange:
            maximized = self._window.isMaximized()
            self.max_btn.setIcon(icons.icon(
                "win-restore" if maximized else "win-max",
                self._colors["text_dim"], 16))
            self.max_btn.setToolTip(tr("Restore") if maximized else tr("Maximize"))
        return False


class DragArea(QWidget):
    """A widget that moves its frameless top-level window when dragged."""

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            win = self.window().windowHandle()
            if win is not None:
                win.startSystemMove()
                event.accept()
                return
        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            top = self.window()
            if top.isMaximized():
                top.showNormal()
            else:
                top.showMaximized()
            event.accept()
            return
        super().mouseDoubleClickEvent(event)


class FramelessResizer(QObject):
    """Application-level event filter providing 8-direction edge resizing
    for a frameless window (with cursor feedback)."""

    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._cursor_overridden = False
        self._cursor_shape = None

    def _apply_cursor(self, cursor):
        """Push, reshape or pop the application-wide override cursor.

        Qt keeps override cursors on a stack, so every set needs exactly one
        restore; track the active shape rather than a bare flag, or moving from a
        left edge to a top edge keeps showing the horizontal arrow."""
        if cursor is None:
            if self._cursor_overridden:
                QApplication.restoreOverrideCursor()
                self._cursor_overridden = False
                self._cursor_shape = None
            return
        if not self._cursor_overridden:
            QApplication.setOverrideCursor(cursor)
            self._cursor_overridden = True
        elif self._cursor_shape != cursor:
            QApplication.changeOverrideCursor(cursor)
        self._cursor_shape = cursor

    def _edges_at(self, global_pos):
        if self._window.isMaximized() or self._window.isFullScreen():
            return Qt.Edges()
        # Work in the window's own coordinates. A frameless window's
        # frameGeometry() is unreliable on some platforms (fractional scaling,
        # Wayland CSD shadow margins): it reports a position/size that doesn't
        # match the rendered surface, which pushed the resize bands inside the
        # window. mapFromGlobal() + the live width()/height() always describe
        # what's actually drawn, so the edges line up with the visible border.
        local = self._window.mapFromGlobal(global_pos)
        x, y = local.x(), local.y()
        w, h = self._window.width(), self._window.height()
        if not (0 <= x <= w and 0 <= y <= h):
            return Qt.Edges()
        edges = Qt.Edges()
        if x <= RESIZE_MARGIN:
            edges |= Qt.LeftEdge
        if x >= w - RESIZE_MARGIN:
            edges |= Qt.RightEdge
        if y <= RESIZE_MARGIN:
            edges |= Qt.TopEdge
        if y >= h - RESIZE_MARGIN:
            edges |= Qt.BottomEdge
        return edges

    @staticmethod
    def _cursor_for(edges):
        if edges in (Qt.LeftEdge | Qt.TopEdge, Qt.RightEdge | Qt.BottomEdge):
            return Qt.SizeFDiagCursor
        if edges in (Qt.RightEdge | Qt.TopEdge, Qt.LeftEdge | Qt.BottomEdge):
            return Qt.SizeBDiagCursor
        if edges & (Qt.LeftEdge | Qt.RightEdge):
            return Qt.SizeHorCursor
        if edges & (Qt.TopEdge | Qt.BottomEdge):
            return Qt.SizeVerCursor
        return None

    def eventFilter(self, obj, event):
        # Defensive: this filter sees every event in the app; never let an
        # unexpected event type take the process down.
        try:
            etype = event.type()
            if etype == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                # Only react to presses on the main window itself
                widget = obj if hasattr(obj, 'window') and callable(obj.window) else None
                if widget is None or widget.window() is not self._window:
                    return False
                edges = self._edges_at(event.globalPosition().toPoint())
                if edges:
                    handle = self._window.windowHandle()
                    if handle is not None:
                        handle.startSystemResize(edges)
                        return True
            elif etype == QEvent.MouseMove and not event.buttons():
                widget = obj if hasattr(obj, 'window') and callable(obj.window) else None
                if widget is not None and widget.window() is self._window:
                    self._apply_cursor(
                        self._cursor_for(self._edges_at(event.globalPosition().toPoint())))
                else:
                    # Pointer moved onto another window; ours no longer owns the shape.
                    self._apply_cursor(None)
            elif etype in (QEvent.WindowDeactivate, QEvent.Hide, QEvent.Close):
                # A modal dialog opening over an edge (sign-in is the usual one), the
                # window losing focus, or it being hidden all steal the pointer without
                # ever delivering the MouseMove that would pop the override — leaving
                # the resize arrow stuck across the whole app until restart.
                if obj is self._window:
                    self._apply_cursor(None)
            elif etype == QEvent.Leave and obj is self._window:
                self._apply_cursor(None)
        except Exception:
            return False
        return False
