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

"""The Android companion app's presence inside the desktop app.

Two surfaces, deliberately unequal:

  • ``AndroidDialog`` — the permanent home, reachable from the app menu, About and
    Settings → Sync. It never appears on its own; the user always asks for it.
  • ``AndroidPromoBanner`` — a dismissible strip shown on sign-in or launch with a
    cloud account, because that is when "your words are already on your phone" is
    literally true. It returns each launch until the user answers it, and answering
    it — opening the dialog or closing the strip — retires it permanently.

Both centre on a QR code rather than a link: a Play Store URL on a desktop screen
is a dead end, since the phone that would install the app cannot click it.

The QR is always dark-on-white regardless of the app theme — inverted codes scan
unreliably on older cameras — so it sits on its own light card that reads as a
deliberate object rather than a theming mistake.
"""
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QDesktopServices, QImage, QPainter, QPixmap
from PySide6.QtWidgets import (
    QApplication, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout,
)

from app.config import get_bool, save_settings
from app.i18n import tr
from app.ui import icons
from app.ui.dialogs.base import FramelessDialog
from app.ui.widgets import style_as_link
from app.version import android_url

# Written to settings.cfg once the user answers the banner — by opening the dialog
# or closing the strip. Being shown is not an answer: someone who never looked at it
# has not declined anything, so display alone must not retire it.
DISMISSED_KEY = "android_promo_dismissed"

_QR_DARK = "#0e1116"
_QR_LIGHT = "#ffffff"
_QR_BORDER = 2   # quiet zone, in modules — below 2 the code stops scanning reliably


# --------------------------------------------------------------------------- #
# QR rendering
# --------------------------------------------------------------------------- #
def qr_pixmap(url, size=160, dpr=2.0):
    """A crisp QR for ``url``, ``size`` logical pixels square.

    Drawn as filled rectangles rather than rasterised from SVG: QR modules are
    axis-aligned squares, so painting them directly avoids the antialiased edges
    that make a scaled-down code harder for a camera to lock onto. The module size
    is snapped to whole device pixels and the device pixel ratio is derived from
    the result, which keeps every module identical in width — the property phone
    scanners actually depend on.
    """
    import segno

    matrix = list(segno.make(url, error="m").matrix_iter(border=_QR_BORDER))
    modules = len(matrix)
    module_px = max(1, int(size * dpr) // modules)
    side = module_px * modules

    image = QImage(side, side, QImage.Format_ARGB32_Premultiplied)
    image.fill(QColor(_QR_LIGHT))
    painter = QPainter(image)
    painter.setPen(Qt.NoPen)
    painter.setBrush(QColor(_QR_DARK))
    for row, cells in enumerate(matrix):
        # Coalesce each horizontal run of dark modules into one rect: far fewer
        # draw calls, and no hairline seams between adjacent modules.
        start = None
        for col, cell in enumerate(cells):
            if cell and start is None:
                start = col
            elif not cell and start is not None:
                painter.drawRect(start * module_px, row * module_px,
                                 (col - start) * module_px, module_px)
                start = None
        if start is not None:
            painter.drawRect(start * module_px, row * module_px,
                             (modules - start) * module_px, module_px)
    painter.end()

    pixmap = QPixmap.fromImage(image)
    pixmap.setDevicePixelRatio(side / size)
    return pixmap


def _qr_card(url, size, colors):
    """The QR on its white card — the light background is part of the code."""
    card = QLabel()
    card.setPixmap(qr_pixmap(url, size))
    card.setFixedSize(size + 20, size + 20)
    card.setAlignment(Qt.AlignCenter)
    card.setStyleSheet(
        f"background:{_QR_LIGHT}; border:1px solid {colors['border']}; border-radius:10px;")
    return card


# --------------------------------------------------------------------------- #
# gating
# --------------------------------------------------------------------------- #
def should_show_promo(settings, auth):
    """Whether the banner may still be shown.

    True only for someone the mobile app can actually serve: signed into a cloud
    account on the built-in server. Offline profiles and own-server users get
    nothing from an app that syncs through our backend, so they are never asked.

    It keeps returning until the user answers it, so a strip that arrived mid-task
    is not silently spent. One click on the ✕ ends that for good.
    """
    from app.core.supabase_client import is_custom_server

    if get_bool(settings, DISMISSED_KEY, False):
        return False
    if is_custom_server():
        return False
    return bool(auth and auth.is_logged_in() and not auth.is_local_active())


def _record_dismissed(settings):
    settings[DISMISSED_KEY] = "True"
    save_settings(settings)


# --------------------------------------------------------------------------- #
# the permanent home
# --------------------------------------------------------------------------- #
class AndroidDialog(FramelessDialog):
    """Scan-to-install, with the pitch that only applies to an existing user."""

    def __init__(self, parent=None, surface="menu"):
        super().__init__(parent, title=tr("Lingueez on Android"))
        self.setMinimumWidth(420)
        c = self.colors
        self._url = android_url(surface)

        head = QHBoxLayout()
        head.setSpacing(10)
        glyph = QLabel()
        glyph.setPixmap(icons.icon("smartphone", c["accent"], 22).pixmap(QSize(22, 22)))
        head.addWidget(glyph, 0, Qt.AlignVCenter)
        title = QLabel(tr("Take your vocabulary with you"))
        title.setWordWrap(True)
        title.setStyleSheet(f"font-size:15px; font-weight:600; color:{c['text']};")
        head.addWidget(title, 1)
        self.content_layout.addLayout(head)

        # The pitch is continuity, not novelty: nothing to set up, nothing to move.
        body = QLabel(tr(
            "Browse and add words, review with flashcards, and listen hands-free "
            "with lock-screen playback controls. Sign in with your Lingueez "
            "account and everything stays in sync."))
        body.setWordWrap(True)
        body.setStyleSheet(f"color:{c['text_dim']}; font-size:12.5px;")
        self.content_layout.addWidget(body)

        qr_row = QHBoxLayout()
        qr_row.addStretch(1)
        qr_row.addWidget(_qr_card(self._url, 160, c))
        qr_row.addStretch(1)
        self.content_layout.addLayout(qr_row)

        hint = QLabel(tr("Point your phone's camera at the code"))
        hint.setAlignment(Qt.AlignCenter)
        hint.setStyleSheet(f"color:{c['text_dim']}; font-size:12px;")
        self.content_layout.addWidget(hint)

        open_btn = QPushButton(tr("Get it on Google Play"), objectName="primaryButton")
        open_btn.setCursor(Qt.PointingHandCursor)
        open_btn.setDefault(True)
        open_btn.clicked.connect(self._open)
        self.content_layout.addWidget(open_btn)

        # For anyone who wants the link on another machine, or has no camera to hand.
        self._copy_btn = QPushButton(tr("Copy link"))
        self._copy_btn.setFlat(True)
        style_as_link(self._copy_btn)
        self._copy_btn.setStyleSheet(
            f"color:{c['accent']}; border:none; background:transparent;")
        self._copy_btn.clicked.connect(self._copy)
        self.content_layout.addWidget(self._copy_btn, 0, Qt.AlignCenter)

    def _open(self):
        from PySide6.QtCore import QUrl
        QDesktopServices.openUrl(QUrl(self._url))

    def _copy(self):
        QApplication.clipboard().setText(self._url)
        self._copy_btn.setText(tr("Link copied"))


def open_android_dialog(parent, surface="menu"):
    """Open the Android dialog, tagging which surface the user arrived from."""
    AndroidDialog(parent, surface=surface).exec()


# --------------------------------------------------------------------------- #
# the one-time nudge
# --------------------------------------------------------------------------- #
class AndroidPromoBanner(QFrame):
    """A slim strip below the top bar, shown at most once per session.

    It deliberately carries no QR: at the height a banner may occupy, the code's
    modules land at barely one screen pixel each and no camera would read it. The
    strip is the invitation; the dialog behind it does the actual handoff.

    Both acting on it and closing it retire the banner for good.
    """

    def __init__(self, parent, settings, colors, on_closed=None):
        super().__init__(parent)
        self._settings = settings
        self._on_closed = on_closed
        self.setObjectName("AndroidPromoBanner")

        row = QHBoxLayout(self)
        row.setContentsMargins(16, 10, 10, 10)
        row.setSpacing(12)

        self._glyph = QLabel()
        row.addWidget(self._glyph, 0, Qt.AlignVCenter)

        text_box = QVBoxLayout()
        text_box.setSpacing(1)
        self._head = QLabel(tr("Lingueez is now on Android"))
        text_box.addWidget(self._head)
        self._sub = QLabel(tr("Sign in with your Lingueez account — "
                              "your vocabulary is already there."))
        self._sub.setWordWrap(True)
        text_box.addWidget(self._sub)
        row.addLayout(text_box, 1)

        self._get_btn = QPushButton(tr("Get the app…"))
        self._get_btn.setFlat(True)
        style_as_link(self._get_btn)
        self._get_btn.clicked.connect(self._details)
        row.addWidget(self._get_btn, 0, Qt.AlignVCenter)

        self._close = QPushButton()
        self._close.setFlat(True)
        self._close.setIconSize(QSize(14, 14))
        self._close.setFixedSize(24, 24)
        self._close.setCursor(Qt.PointingHandCursor)
        self._close.setToolTip(tr("Dismiss"))
        self._close.clicked.connect(self.dismiss)
        row.addWidget(self._close, 0, Qt.AlignVCenter)

        self.refresh_theme(colors)

    def refresh_theme(self, colors):
        """Re-tint everything this widget colours itself.

        The banner paints from inline stylesheets rather than the app-wide QSS, so
        a live theme switch has to reach it explicitly — MainWindow._refresh_icons
        calls this the same way it does the player and the pages.
        """
        self.setStyleSheet(
            f"#AndroidPromoBanner {{ background:{colors['accent_soft']}; "
            f"border-bottom:1px solid {colors['border']}; }}")
        self._glyph.setPixmap(
            icons.icon("smartphone", colors["accent"], 22).pixmap(QSize(22, 22)))
        self._head.setStyleSheet(f"font-weight:600; color:{colors['text']};")
        self._sub.setStyleSheet(f"color:{colors['text_dim']}; font-size:12px;")
        self._get_btn.setStyleSheet(
            f"color:{colors['accent']}; border:none; background:transparent;")
        self._close.setIcon(icons.icon("x", colors["text_dim"], 14))

    def _details(self):
        open_android_dialog(self.window(), surface="nudge")
        self.dismiss()

    def dismiss(self):
        """Retire the banner for good — the ✕ and following the link both count as
        an answer, so neither deserves to be asked again."""
        _record_dismissed(self._settings)
        if self._on_closed:
            self._on_closed()
        self.setParent(None)
        self.deleteLater()


def show_promo_banner(window, root_layout, index, settings, colors, on_closed=None):
    """Insert the banner at ``index`` of the content column.

    Writes nothing: showing is not an answer, so the state only changes once the
    user acts (see ``AndroidPromoBanner.dismiss``).
    """
    banner = AndroidPromoBanner(window, settings, colors, on_closed=on_closed)
    root_layout.insertWidget(index, banner)
    return banner
