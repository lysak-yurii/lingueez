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

"""Compact floating player shown while words/texts play and the app is hidden.

A thin, frameless, always-on-top bar with two modes:
- words: the current word + translation, with a highlight that slides left→right
  as each side is spoken (driven by the words-table player);
- text: the current sentence as a single scrolling "running line", with the
  spoken word highlighted and auto-centered (driven by the texts reader).
The transport controls (prev / pause / next) stay collapsed behind a chevron so
the content gets the full width, and slide out when the pointer is over the right
side. The bar can be dragged (body), resized horizontally (left/right edges), and
a plain click restores the main window.
"""
from PySide6.QtCore import (
    QEasingCurve, QPoint, QPropertyAnimation, QRect, QRectF, QSize, Qt, Signal,
)
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QPushButton, QStackedLayout, QWidget,
)

from app.ui import icons
from app.ui.animations import fade_swap
from app.ui.widgets import ElidedLabel


class MiniPlayer(QWidget):
    """Floating mini playback bar with a sliding word/translation highlight."""

    prev_clicked = Signal()
    toggle_clicked = Signal()
    next_clicked = Signal()
    restore_requested = Signal()  # plain click on the bar body
    moved = Signal()              # drag/resize finished — host persists geometry

    WIDTH = 360       # initial width (resizable)
    HEIGHT = 34
    MIN_WIDTH = 240
    STUB = 46         # min px kept for the inactive phrase so it never vanishes
    RESIZE_MARGIN = 6
    HOT_ZONE = 130    # right-side reveal zone
    HILITE_ANIM_MS = 220
    DOCK_ANIM_MS = 160

    def __init__(self, colors, parent=None):
        super().__init__(parent, objectName="MiniPlayer")
        self.setWindowFlags(
            Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # hand-painted rounded bg
        self.setMouseTracking(True)
        self.setFixedHeight(self.HEIGHT)
        self.setMinimumWidth(self.MIN_WIDTH)
        screen = QApplication.primaryScreen()
        self.setMaximumWidth(screen.availableGeometry().width() if screen else 4000)
        self.resize(self.WIDTH, self.HEIGHT)

        self._colors = colors
        self._paused = False
        self._part = 0            # 0 = word, 1 = translation
        self._w1 = ""             # current word / translation text
        self._w2 = ""
        self._press_pos = None    # global press point, for drag/click telling
        self._dragging = False
        self._expanded = False
        self._cursor_horiz = False

        lay = QHBoxLayout(self)
        lay.setContentsMargins(12, 0, self.RESIZE_MARGIN, 0)
        lay.setSpacing(4)

        # ---- left: a stack of the word-pair view and the running-line view ----
        self._left = QWidget()
        self._left_stack = QStackedLayout(self._left)
        self._left_stack.setContentsMargins(0, 0, 0, 0)

        # word-pair view: two labels with a highlight pill behind them
        self._words = QWidget(objectName="MiniWords")
        wl = QHBoxLayout(self._words)
        wl.setContentsMargins(8, 0, 0, 0)  # room for the pill's left inset
        wl.setSpacing(8)
        self._pill = QWidget(self._words)  # behind the labels, animated
        self._pill.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.word_label = ElidedLabel(min_width=0)
        self.word_label.setObjectName("MiniWord")
        self.sep_label = QLabel("›", objectName="MiniSep")
        self.trans_label = ElidedLabel(min_width=0)
        self.trans_label.setObjectName("MiniWord")
        wl.addWidget(self.word_label)
        wl.addWidget(self.sep_label)
        wl.addWidget(self.trans_label)
        wl.addStretch(1)
        self._left_stack.addWidget(self._words)

        # running-line view: a clipped viewport with a horizontally-scrolled label
        self._line = QWidget(objectName="MiniLine")
        self._line.setAttribute(Qt.WA_TransparentForMouseEvents)
        self._line_pill = QWidget(self._line)
        self._line_pill.setAttribute(Qt.WA_TransparentForMouseEvents)
        self._line_label = QLabel(self._line, objectName="MiniWord")
        self._line_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self._line_text = ""
        self._line_word = None  # (local_start, local_end) of the current word
        self._line_offset = 0   # logical horizontal scroll of the line (<= 0)
        self._left_stack.addWidget(self._line)

        lay.addWidget(self._left, 1)

        # ---- right: transport controls, collapsed behind a chevron handle ----
        self._controls = QWidget(objectName="MiniControls")
        cl = QHBoxLayout(self._controls)
        cl.setContentsMargins(0, 0, 0, 0)
        cl.setSpacing(0)
        self.prev_btn = self._button("skip-back", "Previous word", self.prev_clicked)
        self.play_btn = self._button("pause", "Pause", self.toggle_clicked)
        self.next_btn = self._button("skip-forward", "Next word", self.next_clicked)
        for b in (self.prev_btn, self.play_btn, self.next_btn):
            cl.addWidget(b)
        self._controls_w = self._controls.sizeHint().width()
        self._controls.setMaximumWidth(0)  # start collapsed
        lay.addWidget(self._controls, 0)

        self._handle = self._button("chevron-left", "Show controls", None)
        lay.addWidget(self._handle, 0)

        self._dock_anim = QPropertyAnimation(self._controls, b"maximumWidth", self)
        self._dock_anim.setEasingCurve(QEasingCurve.OutCubic)
        self._dock_anim.setDuration(self.DOCK_ANIM_MS)
        self._hilite_anim = QPropertyAnimation(self._pill, b"geometry", self)
        self._hilite_anim.setEasingCurve(QEasingCurve.OutCubic)
        self._hilite_anim.setDuration(self.HILITE_ANIM_MS)
        self._line_pill_anim = QPropertyAnimation(self._line_pill, b"geometry", self)
        self._line_pill_anim.setEasingCurve(QEasingCurve.OutCubic)
        self._line_pill_anim.setDuration(self.HILITE_ANIM_MS)
        self._line_scroll_anim = QPropertyAnimation(self._line_label, b"pos", self)
        self._line_scroll_anim.setEasingCurve(QEasingCurve.OutCubic)
        self._line_scroll_anim.setDuration(self.HILITE_ANIM_MS)
        self._apply_pill_style()
        self._apply_label_styles()
        self._apply_line_style()

    # ------------------------------------------------------------- controls

    def _button(self, name, tooltip, signal, size=14):
        btn = QPushButton()
        btn.setIcon(icons.icon(name, self._colors["text"], size))
        btn.setIconSize(QSize(size, size))
        if tooltip:
            btn.setToolTip(tooltip)
        btn.setCursor(Qt.PointingHandCursor)
        if signal is not None:
            btn.clicked.connect(signal.emit)
        return btn

    # -------------------------------------------------------------- public

    def set_mode(self, mode):
        """Switch the left area between 'words' and 'text' (running line)."""
        view = self._line if mode == "text" else self._words
        if self._left_stack.currentWidget() is not view:
            self._left_stack.setCurrentWidget(view)

    def set_pair(self, word, translation):
        """Show a new word/translation pair, dissolving the previous one."""
        self.set_mode("words")
        fade_swap(self._words, 180)  # snapshot old pair, fade out over the new
        self._w1 = str(word or "")
        self._w2 = str(translation or "")
        self.word_label.set_full_text(self._w1)
        self.trans_label.set_full_text(self._w2)
        self.sep_label.setVisible(bool(self._w2.strip()))
        self._part = 0
        self._relayout_words()
        self._move_pill(animate=False)

    def set_line(self, text):
        """Show a new sentence as the running line, dissolving the previous one."""
        self.set_mode("text")
        fade_swap(self._line, 180)
        self._line_text = str(text or "").replace("\n", " ").strip()
        self._line_word = None
        self._line_offset = 0
        self._line_label.setText(self._line_text)
        self._line_label.adjustSize()
        self._line_label.move(0, self._line_label_y())
        self._line_pill.hide()

    def set_text_word(self, local_start, local_end):
        """Highlight the spoken word at the given offsets in the current line and
        scroll so it stays centered."""
        text = self._line_text
        n = len(text)
        local_start = max(0, min(local_start, n))
        local_end = max(local_start, min(local_end, n))
        self._line_word = (local_start, local_end)
        self._apply_line_word(animate=True)

    def set_active_part(self, slot):
        """Highlight the word (0) or translation (1). The active phrase gets
        layout priority, so as the highlight crosses the two phrases swap which
        is shown in full — slide when nothing reflows, crossfade when it does."""
        self._part = 1 if slot else 0
        reflowed = self._relayout_words()
        if reflowed:
            fade_swap(self._words, 170)  # mask the width reflow of long phrases
            self._move_pill(animate=False)
        else:
            self._move_pill(animate=True)

    def set_paused(self, paused):
        self._paused = paused
        self.play_btn.setIcon(icons.icon(
            "play" if paused else "pause", self._colors["text"], 14))
        self.play_btn.setToolTip("Resume" if paused else "Pause")

    def refresh_theme(self, colors):
        self._colors = colors
        self.prev_btn.setIcon(icons.icon("skip-back", colors["text"], 14))
        self.next_btn.setIcon(icons.icon("skip-forward", colors["text"], 14))
        self._handle.setIcon(icons.icon(
            "chevron-right" if self._expanded else "chevron-left", colors["text"], 14))
        self.set_paused(self._paused)
        self._apply_pill_style()
        self._apply_label_styles()
        self._apply_line_style()
        self.update()

    # ---------------------------------------------------------- word layout

    def _relayout_words(self):
        """Fit both labels inside the available width, giving the active phrase
        priority. Returns True if either label's width changed."""
        fm = self.word_label.fontMetrics()
        pad = 6
        w1 = fm.horizontalAdvance(self._w1) + pad if self._w1 else 0
        w2 = fm.horizontalAdvance(self._w2) + pad if self._w2 else 0

        inner = self._words.contentsRect().width()
        spacing = self._words.layout().spacing()
        sep_w = (self.sep_label.sizeHint().width() + 2 * spacing) if self._w2 else 0
        avail = inner - sep_w - spacing  # spacing before the trailing stretch
        if avail <= 0:  # not laid out yet — showEvent/resizeEvent will retry
            return False

        if w1 + w2 <= avail:
            a1, a2 = w1, w2
        else:
            active, _other = (w1, w2) if self._part == 0 else (w2, w1)
            active_w = min(active, max(self.STUB, avail - self.STUB))
            other_w = max(0, avail - active_w)
            a1, a2 = (active_w, other_w) if self._part == 0 else (other_w, active_w)

        changed = (self.word_label.width() != a1) or (self.trans_label.width() != a2)
        self.word_label.setFixedWidth(a1)
        self.trans_label.setFixedWidth(a2)
        self._words.layout().activate()
        return changed

    # -------------------------------------------------------------- internals

    def _apply_pill_style(self):
        self._pill.setStyleSheet(
            f"background:{self._colors['accent_soft']};"
            f"border-radius:8px;")

    def _apply_label_styles(self):
        active = self._colors["text"]
        dim = self._colors["text_dim"]
        self.word_label.setStyleSheet(
            f"color:{active if self._part == 0 else dim};"
            f"background:transparent;font-weight:600;")
        self.trans_label.setStyleSheet(
            f"color:{active if self._part == 1 else dim};"
            f"background:transparent;font-weight:600;")
        self.sep_label.setStyleSheet(
            f"color:{dim};background:transparent;")

    def _active_label(self):
        return self.trans_label if self._part == 1 else self.word_label

    # ----------------------------------------------------------- running line

    def _apply_line_style(self):
        self._line_label.setStyleSheet(
            f"color:{self._colors['text']};background:transparent;font-weight:600;")
        self._line_pill.setStyleSheet(
            f"background:{self._colors['accent_soft']};border-radius:8px;")

    def _line_label_y(self):
        return (self._line.height() - self._line_label.height()) // 2

    def _apply_line_word(self, animate):
        if self._line_word is None or not self._line_text:
            return
        local_start, local_end = self._line_word
        fm = self._line_label.fontMetrics()
        x0 = fm.horizontalAdvance(self._line_text[:local_start])
        x1 = fm.horizontalAdvance(self._line_text[:local_end])
        y = self._line_label_y()
        strip_w = self._line_label.width()
        view_w = self._line.width()
        min_off = min(0, view_w - strip_w)

        # Calm scroll: hold the line still and let the highlight travel across
        # it; only advance the view when the word reaches the right margin (or
        # falls left of the view after a backward jump). Then bring it to the
        # left margin so a fresh viewport of text reads statically.
        left_margin = 28
        right_edge = max(left_margin + 1, view_w - 40)
        offset = self._line_offset
        word_left = offset + x0
        word_right = offset + x1
        if word_right > right_edge or word_left < left_margin:
            offset = left_margin - x0
        offset = int(round(max(min_off, min(0, offset))))
        self._line_offset = offset

        # pill lives in the viewport; its x already includes the scroll offset
        target_pos = QPoint(offset, y)
        target_pill = QRect(offset + x0 - 4, (self.HEIGHT - 22) // 2,
                            (x1 - x0) + 8, 22)
        self._line_pill.lower()
        self._line_pill.show()
        self._line_scroll_anim.stop()
        self._line_pill_anim.stop()
        if animate and self.isVisible():
            self._line_scroll_anim.setStartValue(self._line_label.pos())
            self._line_scroll_anim.setEndValue(target_pos)
            self._line_scroll_anim.start()
            self._line_pill_anim.setStartValue(self._line_pill.geometry())
            self._line_pill_anim.setEndValue(target_pill)
            self._line_pill_anim.start()
        else:
            self._line_label.move(target_pos)
            self._line_pill.setGeometry(target_pill)

    def _move_pill(self, animate):
        self._apply_label_styles()
        self._words.layout().activate()
        label = self._active_label()
        if label.width() <= 0:  # not laid out yet — defer to first real paint
            return
        target = label.geometry().adjusted(-6, -3, 6, 3)
        self._pill.lower()
        self._hilite_anim.stop()
        if animate and self.isVisible() and self._pill.width() > 0:
            self._hilite_anim.setStartValue(self._pill.geometry())
            self._hilite_anim.setEndValue(target)
            self._hilite_anim.start()
        else:
            self._pill.setGeometry(target)

    # ------------------------------------------------------- reveal controls

    def _reveal_zone(self):
        return max(self.HOT_ZONE, self._controls_w + self._handle.width() + 24)

    def _set_expanded(self, expanded):
        if expanded == self._expanded:
            return
        self._expanded = expanded
        self._dock_anim.stop()
        self._dock_anim.setStartValue(self._controls.maximumWidth())
        self._dock_anim.setEndValue(self._controls_w if expanded else 0)
        self._dock_anim.start()
        self._handle.setIcon(icons.icon(
            "chevron-right" if expanded else "chevron-left", self._colors["text"], 14))

    def place_default(self):
        """Bottom-right of the primary screen, with a margin."""
        screen = self.screen() or QApplication.primaryScreen()
        if screen is None:
            return
        geo = screen.availableGeometry()
        self.move(geo.right() - self.width() - 24, geo.bottom() - self.HEIGHT - 24)

    # ----------------------------------------------------------- paint / drag

    def paintEvent(self, event):
        # A translucent top-level window does not reliably honour its QSS
        # background, so paint the rounded pill by hand (as WordPopup does).
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = QRectF(self.rect()).adjusted(0.5, 0.5, -0.5, -0.5)
        painter.setBrush(QColor(self._colors["surface_alt"]))
        painter.setPen(QPen(QColor(self._colors["border"]), 1))
        painter.drawRoundedRect(rect, 9, 9)

    def showEvent(self, event):
        super().showEvent(event)
        self._controls.ensurePolished()  # natural width now reflects the QSS
        self._controls_w = self._controls.sizeHint().width()
        if not self._expanded:
            self._controls.setMaximumWidth(0)
        self._relayout_words()  # geometry is valid now
        self._move_pill(animate=False)
        self._apply_line_word(animate=False)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._relayout_words()
        self._move_pill(animate=False)
        self._apply_line_word(animate=False)  # re-center the running line

    def hideEvent(self, event):
        super().hideEvent(event)
        self._set_expanded(False)
        self.moved.emit()  # persist geometry whenever the bar goes away

    def leaveEvent(self, event):
        self._set_expanded(False)
        if self._cursor_horiz:
            self.unsetCursor()
            self._cursor_horiz = False
        super().leaveEvent(event)

    def _edge_at(self, x):
        if x <= self.RESIZE_MARGIN:
            return Qt.LeftEdge
        if x >= self.width() - self.RESIZE_MARGIN:
            return Qt.RightEdge
        return None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            edge = self._edge_at(event.position().toPoint().x())
            if edge is not None:
                handle = self.windowHandle()
                if handle is not None:
                    self._press_pos = None
                    handle.startSystemResize(edge)
                    return
            self._press_pos = event.globalPosition().toPoint()
            self._drag_offset = self._press_pos - self.frameGeometry().topLeft()
            self._dragging = False
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        pos = event.globalPosition().toPoint()
        if self._press_pos is not None:  # dragging the bar
            if not self._dragging:
                if (pos - self._press_pos).manhattanLength() < QApplication.startDragDistance():
                    return
                self._dragging = True
            self.move(pos - self._drag_offset)
            return
        # hover (no button): edge-resize cursor + reveal controls on the right
        x = event.position().toPoint().x()
        horiz = self._edge_at(x) is not None
        if horiz != self._cursor_horiz:
            self.setCursor(Qt.SizeHorCursor) if horiz else self.unsetCursor()
            self._cursor_horiz = horiz
        self._set_expanded(x >= self.width() - self._reveal_zone())
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._press_pos is not None:
            was_drag = self._dragging
            self._press_pos = None
            self._dragging = False
            if was_drag:
                self.moved.emit()
            else:
                self.restore_requested.emit()
        super().mouseReleaseEvent(event)
