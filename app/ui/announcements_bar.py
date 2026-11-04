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
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Banners for messages from the Lingueez team, above the pages."""

from PySide6.QtCore import QSize, Qt, QUrl, Signal
from PySide6.QtGui import QColor, QDesktopServices
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget)

from app.core.announcements import Announcement, localized
from app.i18n import current_language, tr
from app.ui import icons

# At most this many at once; closing one lets the next move up.
MAX_BANNERS = 2

_ICON = {"info": "sparkles", "success": "check", "warning": "alert", "critical": "alert"}


def severity_color(colors, severity: str) -> str:
    return {"info": colors["accent"], "success": colors["success"],
            "warning": colors["warning"], "critical": colors["danger"]}[severity]


def _tint(color: str, base: str, amount: float) -> str:
    """*color* laid over *base* at *amount* opacity, as a hex colour."""
    c, b = QColor(color), QColor(base)
    mix = [round(cc * amount + bb * (1 - amount))
           for cc, bb in ((c.red(), b.red()), (c.green(), b.green()), (c.blue(), b.blue()))]
    return QColor(*mix).name()


class AnnouncementBanner(QFrame):
    closed = Signal(object)  # the Announcement

    def __init__(self, message: Announcement, colors, parent=None):
        super().__init__(parent)
        self.message = message
        lang = current_language()
        accent = severity_color(colors, message.severity)
        self.setObjectName("AnnouncementBanner")
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.setStyleSheet(
            f"#AnnouncementBanner {{ background: {_tint(accent, colors['surface'], 0.14)};"
            f" border: none; border-left: 3px solid {accent}; }}"
            f"#AnnouncementBanner QLabel {{ color: {colors['text']}; background: transparent; }}")

        row = QHBoxLayout(self)
        row.setContentsMargins(14, 8, 8, 8)
        row.setSpacing(10)
        glyph = QLabel()
        glyph.setPixmap(icons.pixmap(_ICON[message.severity], accent, size=18))
        glyph.setAlignment(Qt.AlignTop)
        row.addWidget(glyph)

        texts = QVBoxLayout()
        texts.setSpacing(2)
        title = localized(message.title, lang)
        if title:
            heading = QLabel(title)
            heading.setStyleSheet("font-weight: 600;")
            heading.setWordWrap(True)
            texts.addWidget(heading)
        body = QLabel(localized(message.body, lang) or "")
        body.setWordWrap(True)
        body.setTextFormat(Qt.PlainText)
        texts.addWidget(body)
        action = localized(message.action_label, lang)
        if action and message.link:
            link = QPushButton(action)
            link.setFlat(True)
            link.setCursor(Qt.PointingHandCursor)
            link.setStyleSheet(f"QPushButton {{ color: {accent}; text-decoration: underline;"
                               " border: none; padding: 0; text-align: left; }")
            link.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(message.link)))
            texts.addWidget(link, 0, Qt.AlignLeft)
        row.addLayout(texts, 1)

        if message.dismissible:
            close = QPushButton()
            close.setIcon(icons.icon("x", colors["text_dim"], size=16))
            close.setIconSize(QSize(16, 16))
            close.setFlat(True)
            close.setCursor(Qt.PointingHandCursor)
            close.setToolTip(tr("Close"))
            close.setStyleSheet("QPushButton { border: none; padding: 4px; }")
            close.clicked.connect(lambda: self.closed.emit(self.message))
            row.addWidget(close, 0, Qt.AlignTop)


class AnnouncementsBar(QWidget):
    """Shows the first :data:`MAX_BANNERS` messages it is given."""
    closed = Signal(object)  # the Announcement

    def __init__(self, colors, parent=None):
        super().__init__(parent)
        self._colors = colors
        self._messages = []
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(1)
        self.setVisible(False)

    def set_colors(self, colors) -> None:
        self._colors = colors
        self._rebuild()

    def set_messages(self, messages) -> None:
        self._messages = list(messages)
        self._rebuild()

    def _rebuild(self) -> None:
        while self._layout.count():
            item = self._layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        shown = self._messages[:MAX_BANNERS]
        for message in shown:
            banner = AnnouncementBanner(message, self._colors, self)
            banner.closed.connect(self.closed.emit)
            self._layout.addWidget(banner)
        self.setVisible(bool(shown))
