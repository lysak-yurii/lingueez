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
  • ``AndroidPromoBanner`` — a dismissible strip shown once the user has a library
    worth carrying (more than ``MIN_WORDS`` words), whatever kind of account they
    are on. It returns each launch until the user answers it, and answering it —
    opening the dialog or closing the strip — retires it permanently.

What differs between those users is the wording, not the invitation: only someone
signed into a cloud account can be told their words are *already* on the phone, so
``_continuity_line`` picks the claim that is actually true for them. The phone app
has no offline mode (``auth_gate.dart`` routes to the login screen), so everyone
else is told plainly that it takes an account.

Both centre on a QR code rather than a link: a Play Store URL on a desktop screen
is a dead end, since the phone that would install the app cannot click it.

The QR is always dark-on-white regardless of the app theme — inverted codes scan
unreliably on older cameras — so it sits on its own light card that reads as a
deliberate object rather than a theming mistake.

The dialog also carries a drawn preview of the phone app (``PhoneMock``), mirroring
what the Android client does for the desktop in ``desktop_app_screen.dart``. Each
client shows the other rather than describing it, and the two mocks list the same
words, so the pair reads as one product.
"""
from PySide6.QtCore import QRectF, QSize, Qt
from PySide6.QtGui import (
    QColor, QDesktopServices, QFont, QImage, QPainter, QPainterPath, QPen, QPixmap,
)
from PySide6.QtWidgets import (
    QApplication, QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget,
)

from app.config import get_bool, save_settings
from app.i18n import tr
from app.ui import icons, theme
from app.ui.dialogs.base import FramelessDialog
from app.ui.widgets import style_as_link
from app.version import android_url

# Written to settings.cfg once the user answers the banner — by opening the dialog
# or closing the strip. Being shown is not an answer: someone who never looked at it
# has not declined anything, so display alone must not retire it.
DISMISSED_KEY = "android_promo_dismissed"

# How big a library has to be before the strip is worth showing. A handful of
# words is someone still trying the app out; interrupting them to pitch a second
# client is noise. Above it, there is something on the phone worth opening.
MIN_WORDS = 3

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
# the drawn phone
# --------------------------------------------------------------------------- #
# The design canvas the phone is drawn on, then scaled to fit the widget. Fixed
# sizes inside a contain-fit keep every proportion — and the small type — exact at
# any dialog size, with no overflow to guard against and nothing for the
# widget_scaling setting to reflow.
_MOCK_W, _MOCK_H = 200, 420

# The five pairs the Android app's own mock of the desktop shows, in the same
# order (lingueez-mobile/lib/screens/desktop_app_screen.dart), plus two more to
# fill a phone's taller list. Whoever sees both previews sees one library, and the
# mixed scripts say what the program is for without a word of copy.
#
# The trailing float is the width of the definition-preview bar, as a fraction:
# the real row shows one dim line of the definition, and a bar says "there is more
# here" without this drawing having to invent dictionary entries.
_MOCK_ROWS = [
    ("Learning",  "neighborhood",   "el barrio",         0.72),
    ("Reviewing", "le dépaysement", "change of scenery", 0.55),
    ("Mastered",  "наполегливість", "perseverance",      0.80),
    ("Learning",  "die Umwelt",     "довкілля",          0.48),
    ("New",       "breakfast",      "le petit-déjeuner", 0.66),
    ("Reviewing", "el consejo",     "порада",            0.58),
    ("Mastered",  "der Vorschlag",  "the suggestion",    0.74),
]

_ROW_H = 44
_LIST_TOP, _LIST_BOTTOM = 81, 374
_NAV_H = 34
_NAV_SLOTS = 5
_NAV_CURRENT = 1  # "Words" — the screen being previewed


class PhoneMock(QWidget):
    """The Android app's word list, drawn at a fifth of the size.

    Drawn rather than screenshotted, for the same reasons the phone app draws the
    desktop instead of capturing it: a real capture would be a wall of illegible
    type, would need a light and a dark version, and would go stale the first time
    that UI moved. This is recognisably the same program and it can never be wrong.

    It is painted from the *desktop's* palette, so it is lit by whatever theme the
    dialog is in. What makes it read as Android is the shapes — the status strip,
    the full-height status spine on each row, the floating add button, the stadium
    pill under the current tab — not borrowed colour.
    """

    def __init__(self, colors, parent=None):
        super().__init__(parent)
        self._colors = colors
        self.setFixedWidth(_MOCK_W)
        self.setMinimumHeight(340)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        # A diagram, not a control: give assistive tech something to announce
        # instead of an unlabelled blank.
        self.setAccessibleName(tr("Preview of Lingueez on a phone"))

    def sizeHint(self):
        return QSize(_MOCK_W, _MOCK_H)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        # Contain-fit: the drawing never distorts, and a column taller than the
        # phone leaves it centred rather than stretched.
        scale = min(self.width() / _MOCK_W, self.height() / _MOCK_H)
        painter.translate((self.width() - _MOCK_W * scale) / 2,
                          (self.height() - _MOCK_H * scale) / 2)
        painter.scale(scale, scale)
        self._paint_phone(painter)
        painter.end()

    # -- pieces, all in design units ---------------------------------------- #
    def _font(self, px, weight=QFont.Normal):
        font = QFont(QApplication.font())
        font.setPixelSize(px)
        font.setWeight(weight)
        return font

    def _text(self, painter, rect, text, px, color, weight=QFont.Normal,
              align=Qt.AlignLeft | Qt.AlignVCenter):
        painter.setFont(self._font(px, weight))
        painter.setPen(QColor(color))
        # Elide by clipping rather than wrapping: a wrapped word would break the
        # row rhythm the whole drawing depends on.
        painter.drawText(QRectF(*rect), align | Qt.TextSingleLine, text)

    def _fill(self, painter, rect, color, radius=0):
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(color))
        if radius:
            painter.drawRoundedRect(QRectF(*rect), radius, radius)
        else:
            painter.drawRect(QRectF(*rect))

    def _paint_phone(self, painter):
        c = self._colors

        shell = QPainterPath()
        shell.addRoundedRect(QRectF(0.5, 0.5, _MOCK_W - 1, _MOCK_H - 1), 20, 20)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(c["surface"]))
        painter.drawPath(shell)
        # Everything inside is clipped to the shell, so the bands can run edge to
        # edge without spilling past the rounded corners.
        painter.save()
        painter.setClipPath(shell)

        self._paint_status_strip(painter)
        self._paint_app_bar(painter)
        self._paint_search(painter)
        self._paint_list(painter)
        self._paint_fab(painter)
        self._paint_nav(painter)

        painter.restore()
        painter.setPen(QPen(QColor(c["border"]), 1))
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(shell)

    def _paint_status_strip(self, painter):
        """Clock and indicators — the whole vocabulary of "this is a phone"."""
        c = self._colors
        self._text(painter, (12, 0, 60, 13), "09:34", 7, c["text_dim"])
        for i, w in enumerate((5, 6, 8)):
            self._fill(painter, (163 + i * 10, 5.5 - w * 0.2, w * 0.8, w * 0.45),
                       c["text_dim"], 1)

    def _paint_app_bar(self, painter):
        c = self._colors
        self._text(painter, (12, 13, 120, 34), "Lingueez", 13, c["accent"],
                   QFont.Bold)
        # The import and filter actions the real app bar carries, as glyph blocks:
        # naming them would put untranslated English inside a picture. Held at half
        # strength — at this size a solid block outweighs the words it sits above,
        # and the eye should land on the list.
        muted = QColor(c["text_dim"])
        muted.setAlpha(120)
        for i in range(2):
            self._fill(painter, (158 + i * 19, 26, 10, 9), muted, 2)

    def _paint_search(self, painter):
        c = self._colors
        self._fill(painter, (10, 51, 180, 26), c["surface_alt"], 13)
        painter.setPen(QPen(QColor(c["text_dim"]), 1.2))
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QRectF(22, 60, 8, 8))
        painter.drawLine(29, 67, 32, 70)
        self._fill(painter, (40, 62, 66, 4), c["border"], 2)

    def _paint_list(self, painter):
        """The word rows, clipped at the bottom so the list reads as scrollable."""
        c = self._colors
        painter.save()
        painter.setClipRect(QRectF(1, _LIST_TOP, _MOCK_W - 2,
                                   _LIST_BOTTOM - _LIST_TOP), Qt.IntersectClip)
        y = _LIST_TOP
        for status, term, translation, bar in _MOCK_ROWS:
            if y >= _LIST_BOTTOM:
                break
            # The status spine: a thin full-height bar rather than a chip, which is
            # how the phone app marks status and how it differs from the desktop's
            # pill. The ramp is the desktop's own, and the two already agree.
            self._fill(painter, (0, y, 3, _ROW_H), theme.status_style(status)["ink"])
            self._text(painter, (14, y + 4, 176, 13), term, 9, c["text"])
            self._text(painter, (14, y + 17, 176, 12), translation, 8, c["text_dim"])
            self._fill(painter, (14, y + 33, 120 * bar, 3.5), c["border"], 1.75)
            painter.setPen(QPen(QColor(c["border"]), 1))
            painter.drawLine(3, y + _ROW_H, _MOCK_W, y + _ROW_H)
            y += _ROW_H
        painter.restore()

    def _paint_fab(self, painter):
        """The extended add button, floating over the list as it does on Home."""
        c = self._colors
        self._fill(painter, (116, 330, 72, 26), c["accent"], 13)
        painter.setPen(QPen(QColor("#ffffff"), 1.6))
        painter.drawLine(129, 343, 137, 343)
        painter.drawLine(133, 339, 133, 347)
        self._fill(painter, (145, 341, 32, 4), "#ffffff", 2)

    def _paint_nav(self, painter):
        c = self._colors
        top = _MOCK_H - 12 - _NAV_H
        self._fill(painter, (0, top, _MOCK_W, _NAV_H), c["surface_alt"])
        painter.setPen(QPen(QColor(c["border"]), 1))
        painter.drawLine(0, top, _MOCK_W, top)

        slot = _MOCK_W / _NAV_SLOTS
        for i in range(_NAV_SLOTS):
            cx = slot * (i + 0.5)
            current = i == _NAV_CURRENT
            if current:
                # The stadium behind the current destination — the phone app's
                # most distinctive piece of chrome.
                self._fill(painter, (cx - 13, top + 4, 26, 15), c["accent_soft"], 7.5)
            tint = c["accent"] if current else c["text_dim"]
            self._fill(painter, (cx - 4.5, top + 7.5, 9, 8), tint, 2)
            self._fill(painter, (cx - 6, top + 23, 12, 2.5),
                       c["accent"] if current else c["border"], 1.25)

        # Gesture bar: the last thing that says phone rather than tablet-shaped box.
        self._fill(painter, (72, _MOCK_H - 9, 56, 3), c["border"], 1.5)


# --------------------------------------------------------------------------- #
# gating
# --------------------------------------------------------------------------- #
def has_cloud_library(auth=None):
    """Whether this user's words are already on the server the phone reads.

    The one fact the copy turns on. False for offline profiles and for anyone not
    signed in — their library lives on this machine only, so nothing is waiting
    for them on a phone yet.
    """
    if auth is None:
        from app.core.auth_manager import get_auth_manager
        auth = get_auth_manager()
    try:
        return bool(auth.is_logged_in() and not auth.is_local_active())
    except Exception:
        return False


def _continuity_line(long_form=False):
    """The pitch, matched to what is true for this user rather than to the best case."""
    if has_cloud_library():
        if long_form:
            return tr("Sign in with your Lingueez account and your vocabulary is "
                      "already there — nothing to set up, nothing to move across.")
        return tr("Sign in with your Lingueez account — "
                  "your vocabulary is already there.")
    # No cloud library yet, so promising one would be a lie. Name the step instead.
    if long_form:
        return tr("Sign in with a free Lingueez account on both and your vocabulary "
                  "syncs to the phone — no files to copy across.")
    return tr("Sign in with a free Lingueez account and your words sync to your phone.")


def should_show_promo(settings, word_count):
    """Whether the banner may still be shown.

    True for anyone with a library worth carrying who has not yet answered the
    strip. It was once limited to cloud accounts, on the grounds that only they
    could be told their words were already on the phone — but that was a fact
    about the *wording*, not about who the app is for. Offline and own-server
    users study the same vocabulary and the phone app serves them too, so they
    get the invitation and an honest version of the claim.

    It keeps returning until the user answers it, so a strip that arrived mid-task
    is not silently spent. One click on the ✕ ends that for good.
    """
    if get_bool(settings, DISMISSED_KEY, False):
        return False
    return (word_count or 0) > MIN_WORDS


def _record_dismissed(settings):
    settings[DISMISSED_KEY] = "True"
    save_settings(settings)


# --------------------------------------------------------------------------- #
# the permanent home
# --------------------------------------------------------------------------- #
def _feature(colors, icon_name, title, body):
    """One reason to install it: an accent glyph beside a claim and its detail."""
    row = QHBoxLayout()
    row.setSpacing(11)
    glyph = QLabel()
    glyph.setPixmap(icons.icon(icon_name, colors["accent"], 16).pixmap(QSize(16, 16)))
    glyph.setFixedWidth(16)
    row.addWidget(glyph, 0, Qt.AlignTop)

    text = QVBoxLayout()
    text.setSpacing(1)
    head = QLabel(title)
    head.setWordWrap(True)
    head.setStyleSheet(f"font-weight:600; color:{colors['text']}; font-size:12.5px;")
    text.addWidget(head)
    detail = QLabel(body)
    detail.setWordWrap(True)
    detail.setStyleSheet(f"color:{colors['text_dim']}; font-size:11.5px;")
    text.addWidget(detail)
    row.addLayout(text, 1)
    return row


class AndroidDialog(FramelessDialog):
    """Scan-to-install, with the pitch that only applies to an existing user.

    Two columns rather than the phone app's single scroll: the drawn phone is
    portrait and a dialog is landscape, so the picture sits beside the words
    instead of above them and the whole thing fits without scrolling.
    """

    def __init__(self, parent=None, surface="menu"):
        super().__init__(parent, title=tr("Lingueez on Android"))
        self.setMinimumWidth(660)
        c = self.colors
        self._url = android_url(surface)

        columns = QHBoxLayout()
        columns.setSpacing(24)
        self._mock = PhoneMock(c)
        columns.addWidget(self._mock)

        right = QVBoxLayout()
        right.setSpacing(9)

        title = QLabel(tr("Take your vocabulary with you"))
        title.setWordWrap(True)
        title.setStyleSheet(f"font-size:15px; font-weight:600; color:{c['text']};")
        right.addWidget(title)

        # The pitch is continuity, not novelty: nothing to set up, nothing to move.
        body = QLabel(_continuity_line(long_form=True))
        body.setWordWrap(True)
        body.setStyleSheet(f"color:{c['text_dim']}; font-size:12.5px;")
        right.addWidget(body)
        right.addSpacing(4)

        # Three things the phone does that the desk cannot.
        for icon_name, head, detail in (
            ("sync", tr("Synced both ways"),
             tr("Words you add on the phone are waiting on the computer, and the "
                "other way round.")),
            ("volume", tr("Listen with the screen off"),
             tr("Lock-screen controls, so a review keeps running with the phone "
                "in your pocket.")),
            ("plus", tr("Save a word from any app"),
             tr("Share text to Lingueez and it lands in your vocabulary, ready to "
                "fill in later.")),
        ):
            right.addLayout(_feature(c, icon_name, head, detail))
        right.addStretch(1)

        # The code and the two ways past it, on one row: the QR is the handoff, the
        # button is for the person reading this on the machine they will install
        # from, and the link is for everyone whose camera is elsewhere.
        handoff = QHBoxLayout()
        handoff.setSpacing(14)
        handoff.addWidget(_qr_card(self._url, 136, c), 0, Qt.AlignTop)

        actions = QVBoxLayout()
        actions.setSpacing(8)
        # Centred against the code rather than pinned to its top edge: the caption
        # and the two buttons are one cluster, and a stretch above and below keeps
        # them reading that way at any dialog height.
        actions.addStretch(1)
        hint = QLabel(tr("Point your phone's camera at the code"))
        hint.setWordWrap(True)
        hint.setStyleSheet(f"color:{c['text_dim']}; font-size:12px;")
        actions.addWidget(hint)
        actions.addSpacing(2)

        open_btn = QPushButton(tr("Get it on Google Play"), objectName="primaryButton")
        open_btn.setCursor(Qt.PointingHandCursor)
        open_btn.setDefault(True)
        open_btn.clicked.connect(self._open)
        actions.addWidget(open_btn)

        # For anyone who wants the link on another machine, or has no camera to hand.
        self._copy_btn = QPushButton(tr("Copy link"))
        self._copy_btn.setFlat(True)
        style_as_link(self._copy_btn)
        self._copy_btn.setStyleSheet(
            f"color:{c['accent']}; border:none; background:transparent;")
        self._copy_btn.clicked.connect(self._copy)
        actions.addWidget(self._copy_btn, 0, Qt.AlignCenter)
        actions.addStretch(1)

        handoff.addLayout(actions, 1)
        right.addLayout(handoff)

        columns.addLayout(right, 1)
        self.content_layout.addLayout(columns)

        # Nail the floor to the assembled content. Word-wrapped labels give
        # QVBoxLayout a minimumSizeHint that assumes they can always run wider, so
        # without this the resize grip happily drags the QR off the bottom edge.
        self.setMinimumHeight(self.sizeHint().height())

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
        self._sub = QLabel(_continuity_line())
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
