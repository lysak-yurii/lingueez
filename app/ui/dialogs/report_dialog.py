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

"""'Report an issue' chooser — lets the user pick what kind of issue to report.

A thin selector with no MainWindow dependencies: it records the picked category
in ``self.choice`` and closes. The caller (MainWindow._report_an_issue) dispatches
to the matching flow. The "Inappropriate AI-generated content" option is the
user-facing "means to report" required by Microsoft Store policy 11.16.
"""
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout,
)

from app.i18n import tr
from app.ui import icons
from app.ui.dialogs.base import FramelessDialog


def _tint(hex_color, alpha):
    """A translucent rgba() of an accent hex — used for the icon chip fill so it
    reads as a soft accent wash rather than a hard block."""
    try:
        h = hex_color.lstrip("#")
        r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        return f"rgba({r}, {g}, {b}, {alpha})"
    except (ValueError, IndexError):
        return hex_color


class _OptionCard(QFrame):
    """A whole-row clickable option: accent icon chip + title + description.

    Behaves like a big flat button — pointing-hand cursor, a hover outline, and a
    single click anywhere on the row selects it. Children are transparent to mouse
    events so the click always lands on the card."""

    def __init__(self, colors, icon_name, title, caption, on_click, parent=None):
        super().__init__(parent, objectName="OptionCard")
        self._on_click = on_click
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(
            f"#OptionCard{{background:{colors['surface_alt']};"
            f" border:1px solid {colors['border']}; border-radius:12px;}}"
            f"#OptionCard:hover{{border-color:{colors['accent']};"
            f" background:{_tint(colors['accent'], 0.06)};}}")

        row = QHBoxLayout(self)
        row.setContentsMargins(14, 12, 16, 12)
        row.setSpacing(13)

        chip = QLabel()
        chip.setFixedSize(38, 38)
        chip.setAlignment(Qt.AlignCenter)
        chip.setPixmap(icons.icon(icon_name, colors["accent"], 19).pixmap(QSize(19, 19)))
        chip.setStyleSheet(
            f"background:{_tint(colors['accent'], 0.14)}; border-radius:10px;")
        row.addWidget(chip, 0, Qt.AlignVCenter)

        text = QVBoxLayout()
        text.setSpacing(2)
        head = QLabel(title)
        head.setStyleSheet(
            f"color:{colors['text']}; font-size:13.5px; font-weight:600;")
        text.addWidget(head)
        sub = QLabel(caption)
        sub.setWordWrap(True)
        sub.setStyleSheet(f"color:{colors['text_dim']}; font-size:11.5px;")
        text.addWidget(sub)
        row.addLayout(text, 1)

        for child in (chip, head, sub):
            child.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._on_click()
        else:
            super().mousePressEvent(event)


class ReportIssueDialog(FramelessDialog):
    """Two-way chooser: a technical bug vs. inappropriate AI-generated content."""

    def __init__(self, parent=None):
        super().__init__(parent, title=tr("Report an issue"))
        self.setMinimumWidth(460)
        self.choice = None
        # Centre over whatever dialog launched us (usually About), not the corner.
        self._center_ref = QApplication.activeWindow()
        c = self.colors

        intro = QLabel(tr("What would you like to report?"))
        intro.setWordWrap(True)
        intro.setStyleSheet(f"font-size:14px; font-weight:600; color:{c['text']};")
        self.content_layout.addWidget(intro)

        self.content_layout.addWidget(_OptionCard(
            c, "alert",
            tr("A bug or technical problem"),
            tr("Creates a report with app diagnostics to send to the developers."),
            lambda: self._pick("bug")))
        self.content_layout.addWidget(_OptionCard(
            c, "sparkles",
            tr("Inappropriate AI-generated content"),
            tr("Report a definition, text, or translation the AI produced."),
            lambda: self._pick("ai")))

        self.content_layout.addStretch(1)

        row = QHBoxLayout()
        row.addStretch(1)
        cancel = QPushButton(tr("Cancel"))
        cancel.setCursor(Qt.PointingHandCursor)
        cancel.clicked.connect(self.reject)
        row.addWidget(cancel)
        self.content_layout.addLayout(row)

    def showEvent(self, event):
        super().showEvent(event)
        ref = self._center_ref or self.parentWidget()
        if ref is not None:
            geo = self.frameGeometry()
            geo.moveCenter(ref.frameGeometry().center())
            self.move(geo.topLeft())

    def _pick(self, choice):
        self.choice = choice
        self.accept()
