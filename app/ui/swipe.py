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

"""Swipe-to-grade for the flashcard, mirroring the phone's gesture.

Left → Hard, right → Easy, up → Good; down grades nothing. The dragged card
is a snapshot on an overlay over the whole window, so it can leave the card's
own slot without being clipped by it. The slot it leaves shows the next card,
coming into focus as the drag nears the point where it commits.
"""
from PySide6.QtCore import QEasingCurve, QPoint, QPointF, QRectF, Qt, QVariantAnimation
from PySide6.QtGui import QColor, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QWidget

#: A swipe commits after this fraction of the card's shorter side...
COMMIT_FRACTION = 0.14
#: ...but never asks for more than this many pixels.
COMMIT_MAX = 72
MAX_TILT_DEG = 5.0
TINT_ALPHA = 56
SETTLE_MS = 240
FLY_MS = 180
#: How far past the release point a committed card travels, as a multiple
#: of the drag that committed it.
FLY_REACH = 2.4
#: Strength of the next card's face before the drag has gone anywhere.
UNDER_OPACITY = 0.35
GRADE_COLOR_KEYS = {"easy": "success", "good": "warning", "hard": "danger"}


def commit_distance(width, height):
    return min(min(width, height) * COMMIT_FRACTION, COMMIT_MAX)


def leaning(dx, dy):
    """The grade a drag is heading for, or None when it heads nowhere."""
    if abs(dy) > abs(dx):
        return "good" if dy < 0 else None
    if dx == 0:
        return None
    return "hard" if dx < 0 else "easy"


def reach(dx, dy, width, height):
    """How far into the commit a drag is, 0..1."""
    commit = commit_distance(width, height)
    if commit <= 0:
        return 0.0
    travel = -dy if abs(dy) > abs(dx) else abs(dx)
    return max(0.0, min(1.0, travel / commit))


def grade_for_drag(dx, dy, width, height):
    """The grade a drag of (dx, dy) across a width×height card commits."""
    return leaning(dx, dy) if reach(dx, dy, width, height) >= 1.0 else None


def _rounded(pixmap, size, radius):
    out = QPixmap(pixmap.size())
    out.setDevicePixelRatio(pixmap.devicePixelRatio())
    out.fill(Qt.transparent)
    p = QPainter(out)
    p.setRenderHint(QPainter.Antialiasing)
    p.setPen(Qt.NoPen)
    p.setBrush(Qt.black)
    p.drawRoundedRect(QRectF(0, 0, size.width(), size.height()), radius, radius)
    p.setCompositionMode(QPainter.CompositionMode_SourceIn)
    p.drawPixmap(0, 0, pixmap)
    p.end()
    return out


class SwipeOverlay(QWidget):
    """A snapshot of `card` that follows the drag, tilting and tinting toward
    the grade it is heading for. `under` is a snapshot of the next card, shown
    in the slot the dragged one leaves; None leaves the slot empty."""

    def __init__(self, card, colors, under=None, radius=18):
        host = card.window()
        super().__init__(host)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self._colors = colors
        self._radius = radius
        self._under = (_rounded(under, card.size(), radius)
                       if under is not None else None)
        self._opacity = 1.0
        self._flying = False
        self._home = QRectF(card.mapTo(host, QPoint(0, 0)), card.size())
        self._pixmap = _rounded(card.grab(), card.size(), radius)
        self.drag = QPointF(0, 0)
        self.setGeometry(host.rect())
        self.show()
        self.raise_()

    def set_drag(self, drag):
        self.drag = QPointF(drag)
        self.update()

    def settle(self, on_done):
        """Ease an abandoned swipe back home, then call `on_done`."""
        start = QPointF(self.drag)
        anim = QVariantAnimation(self)
        anim.setDuration(SETTLE_MS)
        anim.setStartValue(1.0)
        anim.setEndValue(0.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.valueChanged.connect(lambda t: self.set_drag(start * float(t)))
        anim.finished.connect(on_done)
        anim.start(QVariantAnimation.DeleteWhenStopped)

    def fly_out(self):
        """Carry a committed card on along its drag, fading, then delete.

        The real card already shows what `under` did, so the slot is no longer
        covered."""
        self._flying = True
        start = QPointF(self.drag)

        def step(t):
            t = float(t)
            self._opacity = 1.0 - t
            self.set_drag(start * (1.0 + (FLY_REACH - 1.0) * t))

        anim = QVariantAnimation(self)
        anim.setDuration(FLY_MS)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.valueChanged.connect(step)
        anim.finished.connect(self.deleteLater)
        anim.start(QVariantAnimation.DeleteWhenStopped)

    def paintEvent(self, _event):  # noqa: N802
        c = self._colors
        home = self._home
        w, h = home.width(), home.height()
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setRenderHint(QPainter.SmoothPixmapTransform)
        dx, dy = self.drag.x(), self.drag.y()
        if not self._flying:
            p.fillRect(home, QColor(c["bg"]))  # covers the real card underneath
            if self._under is not None:
                p.setBrush(QColor(c["surface"]))
                p.setPen(QPen(QColor(c["border"]), 1))
                p.drawRoundedRect(home.adjusted(0.5, 0.5, -0.5, -0.5),
                                  self._radius, self._radius)
                p.setOpacity(UNDER_OPACITY
                             + (1.0 - UNDER_OPACITY) * reach(dx, dy, w, h))
                p.drawPixmap(home.topLeft(), self._under)
        p.setOpacity(self._opacity)
        p.translate(home.center() + self.drag)
        p.rotate(max(-1.0, min(1.0, dx / w)) * MAX_TILT_DEG if w > 0 else 0.0)
        p.drawPixmap(QPointF(-w / 2, -h / 2), self._pixmap)
        grade = leaning(dx, dy)
        if grade:
            tint = QColor(c[GRADE_COLOR_KEYS[grade]])
            tint.setAlpha(round(TINT_ALPHA * reach(dx, dy, w, h)))
            p.setPen(Qt.NoPen)
            p.setBrush(tint)
            p.drawRoundedRect(QRectF(-w / 2, -h / 2, w, h),
                              self._radius, self._radius)
        p.end()
