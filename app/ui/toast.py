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

"""Sliding toast notifications shown in the corner of the main window."""
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QTimer, Qt
from PySide6.QtWidgets import QFrame, QGraphicsOpacityEffect, QHBoxLayout, QLabel

_ICONS = {"info": "ℹ", "success": "✔", "error": "✖", "warning": "⚠"}
_COLORS = {"info": "#4f8cff", "success": "#3fb950", "error": "#e5534b", "warning": "#d29922"}


class Toast(QFrame):
    MARGIN = 16
    SPACING = 8
    _active = []

    def __init__(self, parent, title, message, toast_type="info", duration=4000):
        super().__init__(parent)
        self.setObjectName("ToastFrame")
        self.setAttribute(Qt.WA_DeleteOnClose)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(14, 10, 14, 10)
        icon = QLabel(_ICONS.get(toast_type, "ℹ"))
        icon.setStyleSheet(f"color: {_COLORS.get(toast_type, '#4f8cff')};"
                           f"font-size: 14pt; background: transparent;")
        layout.addWidget(icon)

        text = QLabel(f"<b>{title}</b><br>{message}" if title else message)
        text.setWordWrap(True)
        text.setStyleSheet("background: transparent;")
        layout.addWidget(text, 1)

        self.setMaximumWidth(380)
        self.adjustSize()

        self._effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self._effect)
        self._anim = QPropertyAnimation(self._effect, b"opacity", self)
        self._anim.setDuration(250)
        self._anim.setEasingCurve(QEasingCurve.OutCubic)
        self._anim.setStartValue(0.0)
        self._anim.setEndValue(1.0)

        Toast._active.append(self)
        self._reposition_all()
        self.show()
        self.raise_()
        self._anim.start()

        QTimer.singleShot(duration, self._fade_out)

    def _fade_out(self):
        anim = QPropertyAnimation(self._effect, b"opacity", self)
        anim.setDuration(300)
        anim.setStartValue(1.0)
        anim.setEndValue(0.0)
        anim.finished.connect(self._close)
        anim.start()
        self._fade_anim = anim

    def _close(self):
        if self in Toast._active:
            Toast._active.remove(self)
        self.close()
        Toast._reposition_static(self.parentWidget())

    def _reposition_all(self):
        Toast._reposition_static(self.parentWidget())

    @staticmethod
    def _reposition_static(parent):
        if parent is None:
            return
        y = parent.height() - Toast.MARGIN
        for toast in reversed(Toast._active):
            if toast.parentWidget() is not parent:
                continue
            y -= toast.height()
            toast.move(parent.width() - toast.width() - Toast.MARGIN, y)
            y -= Toast.SPACING


def show_toast(parent, title, message, toast_type="info", duration=4000):
    return Toast(parent, title, message, toast_type, duration)
