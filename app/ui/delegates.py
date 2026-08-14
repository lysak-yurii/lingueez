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

"""Custom item delegates — colored status pills.

paint() runs for every visible status cell on every repaint (scrolling,
resizing, hover), so pills are rendered once per (status, theme, font)
into a pixmap cache and blitted afterwards.
"""
import html

from PySide6.QtCore import QEvent, QPoint, QPointF, QRectF, QSize, Qt
from PySide6.QtGui import QColor, QFont, QFontMetrics, QPainter, QPixmap
from PySide6.QtWidgets import (QStyledItemDelegate, QStyle, QStyleOptionViewItem,
                               QToolTip)

from app.i18n import tr
from app.ui import theme
from app.ui.word_model import ROLE_FAV_STRIPE


# Offset from the point handed to QToolTip.showText() to where the tip's text
# is actually drawn: Qt nudges the tip by (2, 16) to keep it clear of the
# cursor, and the QToolTip style rule adds a 1px border plus 8px/5px padding.
# Subtracting it puts the revealed text exactly where we ask for it.
_TIP_TEXT_OFFSET = QPoint(2 + 9, 16 + 6)

# Gap between the row and the revealed text below it. The tip must not land
# under the pointer: a tooltip window appearing beneath the cursor sends the
# viewport a Leave event, and Qt hides the tip on Leave — which is exactly the
# flicker an overlapping "expand in place" reveal produces.
_TIP_DROP = 10


def _reveal_cell_text(view, cell_rect, text_rect, text, font):
    """Reveal the untruncated ``text`` of a cell too narrow to show it.

    Drops directly below the cell, left-aligned with the cell's own first
    glyph and typeset at its font size, so it reads as that row continuing
    rather than a label chasing the mouse. Stays up while the pointer remains
    inside ``cell_rect`` (viewport coordinates)."""
    point = QPoint(text_rect.left(), cell_rect.bottom() + _TIP_DROP)
    anchor = view.viewport().mapToGlobal(point) - _TIP_TEXT_OFFSET
    size = font.pointSizeF()
    # Table rows are rendered at the current density's font size, which the
    # tooltip does not inherit; restate it so the reveal matches the row.
    tip = (f'<span style="font-size:{size:.1f}pt">{html.escape(text)}</span>'
           if size > 0 else text)
    # The viewport, not the view, is what the mouse events reach — hand
    # QToolTip that widget so it reads cell_rect in the right coordinate
    # system and keeps the tip alive across the whole cell.
    QToolTip.showText(anchor, tip, view.viewport(), cell_rect)


class RowTintDelegate(QStyledItemDelegate):
    """Default table delegate that honors the model's BackgroundRole.

    The app stylesheet defines QTableView::item rules, which makes the
    stylesheet style skip model background brushes entirely — the
    now-playing and queued row tints would never show. Filling the rect
    before the styled paint restores them. Favorite rows are marked
    afterwards with a thin accent bar at their left edge."""

    def paint(self, painter, option, index):
        if not (option.state & QStyle.State_Selected):
            bg = index.data(Qt.BackgroundRole)
            if bg is not None:
                painter.fillRect(option.rect, bg)
        super().paint(painter, option, index)
        # Favorite marker: a thin accent bar at the row's left edge, drawn
        # over selection so the cue survives a selected row.
        stripe = index.data(ROLE_FAV_STRIPE)
        if stripe is not None:
            r = option.rect
            inset = max(3, r.height() // 5)  # keep clear of the row borders
            painter.fillRect(r.left(), r.top() + inset, 3,
                             r.height() - 2 * inset, stripe)

    def helpEvent(self, event, view, option, index):
        """Hovering a cell whose text the column had to elide reveals the whole
        thing; cells that already fit stay silent (a tip on every hover would
        be noise)."""
        if event.type() != QEvent.ToolTip or not index.isValid():
            return super().helpEvent(event, view, option, index)
        text = str(index.data(Qt.DisplayRole) or "")
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)
        text_rect = view.style().subElementRect(QStyle.SE_ItemViewItemText, opt, view)
        if not text or QFontMetrics(opt.font).horizontalAdvance(text) <= text_rect.width():
            QToolTip.hideText()
            return False
        _reveal_cell_text(view, option.rect, text_rect, text, opt.font)
        return True


class StatusPillDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._cache = {}  # (text, dark, font key, dpr) -> QPixmap

    def sizeHint(self, option, index):
        # So resizeColumnToContents() can fit the (localized) pill, not just
        # the raw status text. Mirrors _render_pill's width plus the 6px left
        # paint offset and the 10px clip margin used in paint().
        base = super().sizeHint(option, index)
        text = str(index.data() or "")
        if not text:
            return base
        font = QFont(option.font)
        font.setPointSizeF(max(7.0, option.font.pointSizeF() - 1))
        font.setWeight(QFont.Normal)
        metrics = QFontMetrics(font)
        pill_w = metrics.horizontalAdvance(tr(text)) + 20
        return QSize(pill_w + 16, max(base.height(), metrics.height() + 12))

    def paint(self, painter, option, index):
        text = str(index.data() or "")  # canonical (English) status — drives the color
        if not text:
            return super().paint(painter, option, index)
        label = tr(text)  # localized text actually shown in the pill

        # cell background: selection > favorite tint > alternating row.
        # Painted directly (not via initStyleOption/drawControl) — the
        # style-sheet path is far too slow for a per-cell hot loop.
        rect = option.rect
        if option.state & QStyle.State_Selected:
            painter.fillRect(rect, option.palette.highlight())
        else:
            row_bg = index.data(Qt.BackgroundRole)
            if row_bg is not None:
                painter.fillRect(rect, row_bg)
            elif option.features & QStyleOptionViewItem.Alternate:
                painter.fillRect(rect, option.palette.alternateBase())

        style = theme.status_style(text)
        dpr = painter.device().devicePixelRatioF() if painter.device() else 1.0
        # keyed on the resolved style, so a theme switch invalidates by itself
        key = (label, style["ink"], style["fill"], option.font.key(), dpr)
        pm = self._cache.get(key)
        if pm is None:
            pm = self._render_pill(label, style, option.font, dpr)
            self._cache[key] = pm

        w = pm.width() / dpr
        h = pm.height() / dpr
        pos = QPointF(rect.x() + 6, rect.y() + (rect.height() - h) / 2)
        if w > rect.width() - 10:
            painter.save()
            painter.setClipRect(rect.adjusted(0, 0, -4, 0))
            painter.drawPixmap(pos, pm)
            painter.restore()
        else:
            painter.drawPixmap(pos, pm)

    @staticmethod
    def _render_pill(label, style, base_font, dpr):
        font = QFont(base_font)
        font.setPointSizeF(max(7.0, base_font.pointSizeF() - 1))
        font.setWeight(QFont.Normal)
        metrics = QFontMetrics(font)
        w = metrics.horizontalAdvance(label) + 20
        h = metrics.height() + 6

        # theme.status_style already returns a value tuned for the active mode,
        # so there is nothing to lighten or darken here
        ink = QColor(style["ink"])

        pm = QPixmap(int(w * dpr), int(h * dpr))
        pm.setDevicePixelRatio(dpr)
        pm.fill(Qt.transparent)
        p = QPainter(pm)
        p.setRenderHint(QPainter.Antialiasing)
        fill = QColor(ink)
        fill.setAlpha(style["fill"])
        p.setPen(Qt.NoPen)
        p.setBrush(fill)
        p.drawRoundedRect(QRectF(0, 0, w, h), h / 2, h / 2)
        p.setPen(ink)
        p.setFont(font)
        p.drawText(QRectF(0, 0, w, h), Qt.AlignCenter, label)
        p.end()
        return pm
