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

"""Quiz page: recall practice that grades itself, in one picker → ask → score loop.

Where Flashcards reveals the answer and asks the learner to rate their own
recall, a quiz makes them produce it first — by picking one of several options
or typing it. That removes the self-assessment step, which is why grading here
only knows Good and Hard (see :mod:`app.core.quiz`), and why the answer is
committed the instant it is given: nothing shown afterwards can change it.

Question building and answer matching live entirely in :mod:`app.core.quiz`;
this module is the view. Like the Flashcards page it owns no word data — decks
come from the ``deck_provider(kind, n)`` callable the main window injects, the
distractor library from ``pool_provider()``, and status promotions are emitted
back for the main window to write through the normal synced update path.
"""

from __future__ import annotations

import logging
import random
import threading
from collections import Counter
from datetime import datetime

from PySide6.QtCore import (
    QEasingCurve, QEvent, QRectF, QSize, Qt, QTimer, QVariantAnimation, Signal,
)
from PySide6.QtGui import QColor, QIcon, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import (
    QButtonGroup, QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpinBox, QStackedLayout, QVBoxLayout, QWidget,
)

from app.core import audio
from app.core import db as dbq
from app.core import progression
from app.core import quiz
from app.core import srs
from app.i18n import lang_label, tr
from app.ui import icons, theme
from app.ui.animations import AnimatedStackedWidget, fade_swap
from app.ui.charts import FlowLayout
from app.ui.flashcards_page import (
    HOVER_EDGE_MIX, HOVER_MS, HOVER_WASH_ALPHA, PICKER_LOGO_SCALE, _DeckLogo,
    _Panel, _SlimBar, _mix, _snippet, _soft,
)
from app.ui.toast import show_toast
from app.ui.widgets import ElidedLabel
from app.ui.workers import run_in_thread

DECK_KINDS = ("due", "filtered", "newest", "selected")
OPTION_LETTERS = ("A", "B", "C", "D", "E", "F")

#: Long enough to read the verdict, short enough not to feel like a wait.
AUTO_ADVANCE_MS = 1100
#: The tail after the answer has been pronounced. Shorter than the silent
#: pause because the audio has already given the eye time on the verdict.
AUTO_ADVANCE_AFTER_SPEECH_MS = 450
#: Hard ceiling on waiting for pronunciation. Only a stalled synthesis (a
#: hung network TTS request) should ever reach it; without it a quiz set to
#: auto-advance would sit on one question forever.
AUTO_ADVANCE_STALL_MS = 10000
COUNT_ANIM_MS = 400
RING_ANIM_MS = 700
OPTION_ANIM_MS = 200
#: Breathing room under the question block, inside the scrolled area.
SESSION_PAD = 6


def _verdict_color(verdict, colors):
    """The one colour a verdict is drawn in, everywhere it appears."""
    return colors["success"] if quiz.is_correct(verdict) else colors["danger"]


def _prompt_font_pt(text):
    """Step the prompt down the type scale so long words still fit one line."""
    length = len(str(text or ""))
    if length <= 16:
        return theme.font_pt("display")
    if length <= 32:
        return theme.font_pt("headline")
    return theme.font_pt("title")


class _PromptCard(QWidget):
    """The asked word, on a card tinted with its learning status.

    The tint is the same status ramp the words table and flashcards use, so
    the card says how well this word is known before it is answered — which is
    context, not a hint, since it never indicates the answer itself.
    """

    speak_clicked = Signal()
    ignore_clicked = Signal()

    def __init__(self, colors, parent=None):
        super().__init__(parent)
        self._colors = colors
        self._ink = colors["accent"]
        self._ignorable = False
        self.setMinimumHeight(150)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 20, 20, 18)
        lay.setSpacing(6)
        self.eyebrow = QLabel(alignment=Qt.AlignCenter)
        self.prompt = QLabel(alignment=Qt.AlignCenter)
        self.prompt.setWordWrap(True)
        lay.addStretch(1)
        lay.addWidget(self.eyebrow)
        lay.addWidget(self.prompt)

        speak_row = QHBoxLayout()
        speak_row.addStretch(1)
        self.speak_btn = QPushButton(objectName="iconButton")
        self.speak_btn.setCursor(Qt.PointingHandCursor)
        self.speak_btn.setIconSize(QSize(18, 18))
        self.speak_btn.setToolTip(tr("Pronounce"))
        self.speak_btn.clicked.connect(self.speak_clicked)
        speak_row.addWidget(self.speak_btn)
        speak_row.addStretch(1)

        # Parked in the corner rather than beside Pronounce: two equal buttons
        # under a two-word prompt read as a toolbar and crowd the one thing
        # worth looking at. Unmanaged, so it cannot shift the centred column.
        self.ignore_btn = QPushButton(self, objectName="iconButton")
        self.ignore_btn.setCursor(Qt.PointingHandCursor)
        self.ignore_btn.setIconSize(QSize(16, 16))
        self.ignore_btn.setFixedSize(24, 24)
        self.ignore_btn.setToolTip(tr("Ignore this word"))
        self.ignore_btn.clicked.connect(self.ignore_clicked)
        lay.addSpacing(2)
        lay.addLayout(speak_row)
        self.answer_hint = QLabel(alignment=Qt.AlignCenter)
        lay.addWidget(self.answer_hint)
        lay.addStretch(1)

    def set_question(self, question):
        self._ink = theme.status_style(question.record.get("Status"))["ink"]
        self.eyebrow.setText(lang_label(question.prompt_language).upper())
        self.prompt.setText(question.prompt)
        answer_language = question.answer_language
        self.answer_hint.setText(
            tr("Answer in {language}").format(
                language=lang_label(answer_language)) if answer_language else "")
        self.answer_hint.setVisible(bool(answer_language))
        self.speak_btn.setVisible(audio.is_language_supported(
            question.prompt_language))
        self._ignorable = progression.is_studiable(question.record.get("Status"))
        self.ignore_btn.setVisible(self._ignorable)
        self._apply_styles()
        self.update()

    def set_ignorable(self, ignorable):
        """Hide the ignore button once the question is answered.

        An answer already occupies this question's slot, and pulling the
        question out from under it would misalign ``_answers`` with
        ``_questions`` — which the missed-deck and the progress trail both read
        positionally.
        """
        self.ignore_btn.setVisible(bool(ignorable) and self._ignorable)

    def refresh_theme(self, colors):
        self._colors = colors
        self._apply_styles()
        self.update()

    def _apply_styles(self):
        c = self._colors
        self.eyebrow.setStyleSheet(
            f"color:{c['text_dim']};background:transparent;letter-spacing:1.2px;"
            f"font-size:{theme.font_pt('caption')}pt;font-weight:600;")
        self.prompt.setStyleSheet(
            f"color:{c['text']};background:transparent;font-weight:700;"
            f"font-size:{_prompt_font_pt(self.prompt.text())}pt;")
        self.answer_hint.setStyleSheet(
            f"color:{c['text_dim']};background:transparent;"
            f"font-size:{theme.font_pt('caption')}pt;")
        self.speak_btn.setIcon(icons.icon("volume", c["text_dim"], 18))
        self.ignore_btn.setIcon(icons.icon("slash", c["text_dim"], 16))

    def resizeEvent(self, event):  # noqa: N802
        super().resizeEvent(event)
        self.ignore_btn.move(self.width() - self.ignore_btn.width() - 12, 12)

    def paintEvent(self, _event):  # noqa: N802
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        rect = QRectF(self.rect()).adjusted(0.5, 0.5, -0.5, -0.5)
        fill = QColor(self._ink)
        fill.setAlpha(26)
        p.setBrush(fill)
        edge = QColor(self._ink)
        edge.setAlpha(90)
        p.setPen(QPen(edge, 1))
        p.drawRoundedRect(rect, 18, 18)
        p.end()


class _OptionRow(QWidget):
    """One answer to choose from: a letter badge, the text, and a verdict.

    Answering locks every row rather than hiding the rejected ones — the point
    of the moment is comparing what was picked against what was right, and a
    row that vanishes cannot be compared.
    """

    clicked = Signal(int)

    def __init__(self, index, colors, parent=None):
        super().__init__(parent)
        self._index = index
        self._colors = colors
        self._state = "idle"  # idle | correct | wrong | dimmed
        self._t = 0.0  # accent fill, animated so the verdict doesn't snap in
        # One animation reused for the widget's life: a throwaway per call
        # would either leak onto the parent or, with DeleteWhenStopped, leave
        # this reference pointing at a destroyed C++ object.
        self._anim = QVariantAnimation(self)
        self._anim.setDuration(OPTION_ANIM_MS)
        self._anim.setEasingCurve(QEasingCurve.OutCubic)
        self._anim.valueChanged.connect(self._set_t)
        self._hover = 0.0
        self._hover_anim = QVariantAnimation(self)
        self._hover_anim.setDuration(HOVER_MS)
        self._hover_anim.setEasingCurve(QEasingCurve.OutCubic)
        self._hover_anim.valueChanged.connect(self._set_hover)
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(48)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        lay = QHBoxLayout(self)
        lay.setContentsMargins(14, 8, 14, 8)
        lay.setSpacing(12)
        self.badge = QLabel(OPTION_LETTERS[index] if index < len(OPTION_LETTERS)
                            else str(index + 1), alignment=Qt.AlignCenter)
        self.badge.setFixedSize(26, 26)
        self.text = QLabel()
        self.text.setWordWrap(True)
        self.mark = QLabel()
        self.mark.setFixedWidth(20)
        lay.addWidget(self.badge)
        lay.addWidget(self.text, 1)
        lay.addWidget(self.mark)
        self._apply_styles()

    def set_text(self, text):
        self.text.setText(str(text or ""))

    def set_state(self, state, animate=True):
        self._state = state
        target = 0.0 if state in ("idle", "dimmed") else 1.0
        self._anim.stop()
        if animate and target != self._t:
            self._anim.setStartValue(float(self._t))
            self._anim.setEndValue(target)
            self._anim.start()
        else:
            self._t = target
        self.setCursor(Qt.ArrowCursor if state != "idle"
                       else Qt.PointingHandCursor)
        if state != "idle":
            self._fade_hover(0.0)
        self._apply_styles()
        self.update()

    def _set_t(self, value):
        self._t = float(value)
        self.update()

    def _set_hover(self, value):
        self._hover = float(value)
        self.update()

    def _fade_hover(self, target):
        self._hover_anim.stop()
        if target == self._hover:
            return
        self._hover_anim.setStartValue(float(self._hover))
        self._hover_anim.setEndValue(float(target))
        self._hover_anim.start()

    def enterEvent(self, event):  # noqa: N802
        if self._state == "idle":
            self._fade_hover(1.0)
        super().enterEvent(event)

    def leaveEvent(self, event):  # noqa: N802
        self._fade_hover(0.0)
        super().leaveEvent(event)

    def _accent(self):
        if self._state == "correct":
            return self._colors["success"]
        if self._state == "wrong":
            return self._colors["danger"]
        return self._colors["border"]

    def refresh_theme(self, colors):
        self._colors = colors
        self._apply_styles()
        self.update()

    def _apply_styles(self):
        c = self._colors
        answered = self._state in ("correct", "wrong")
        accent = self._accent()
        text_color = accent if answered else c["text"]
        body = c["text_dim"] if self._state == "dimmed" else text_color
        self.text.setStyleSheet(
            f"color:{body};background:transparent;"
            f"font-size:{theme.font_pt('body_lg')}pt;"
            f"font-weight:{'600' if answered else '400'};")
        badge_bg = _soft(accent, 46) if answered else _soft(c["text_dim"], 30)
        self.badge.setStyleSheet(
            f"color:{body};background:{badge_bg};border-radius:13px;"
            f"font-size:{theme.font_pt('caption')}pt;font-weight:700;")
        if self._state == "correct":
            self.mark.setPixmap(icons.pixmap("check", c["success"], 18))
        elif self._state == "wrong":
            self.mark.setPixmap(icons.pixmap("x", c["danger"], 18))
        else:
            self.mark.clear()

    def mouseReleaseEvent(self, event):  # noqa: N802
        if event.button() == Qt.LeftButton and self._state == "idle":
            self.clicked.emit(self._index)
        super().mouseReleaseEvent(event)

    def paintEvent(self, _event):  # noqa: N802
        c = self._colors
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        rect = QRectF(self.rect()).adjusted(1.0, 1.0, -1.0, -1.0)
        accent = QColor(self._accent())
        base = QColor(c["surface"])
        if self._state == "dimmed":
            base.setAlpha(120)
        fill = QColor(accent)
        fill.setAlpha(round(34 * self._t))
        p.setBrush(base)
        p.setPen(Qt.NoPen)
        p.drawRoundedRect(rect, 12, 12)
        if self._hover > 0:
            wash = QColor(c["accent"])
            wash.setAlpha(round(HOVER_WASH_ALPHA * self._hover))
            p.setBrush(wash)
            p.drawRoundedRect(rect, 12, 12)
        if self._t > 0:
            p.setBrush(fill)
            p.drawRoundedRect(rect, 12, 12)
        edge = QColor(accent if self._t > 0 else QColor(c["border"]))
        if self._state == "dimmed":
            edge.setAlpha(90)
        elif self._hover > 0:
            edge = _mix(edge, c["accent"], HOVER_EDGE_MIX * self._hover)
        p.setBrush(Qt.NoBrush)
        p.setPen(QPen(edge, 2 if self._t > 0 else 1))
        p.drawRoundedRect(rect, 12, 12)
        p.end()


class _DrainBar(QWidget):
    """The auto-advance countdown — a fill draining toward the next question.

    Clicking it skips the wait. It only ever appears after a correct answer;
    a wrong one holds, because that is the moment worth reading.
    """

    clicked = Signal()

    def __init__(self, colors, parent=None):
        super().__init__(parent)
        self._colors = colors
        self._t = 1.0
        self._anim = QVariantAnimation(self)
        self._anim.setStartValue(1.0)
        self._anim.setEndValue(0.0)
        self._anim.valueChanged.connect(self._set_t)
        self.setFixedHeight(6)
        self.setCursor(Qt.PointingHandCursor)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def start(self, ms=AUTO_ADVANCE_MS):
        self._anim.stop()
        self._anim.setDuration(ms)
        self._anim.start()

    def hold(self):
        """Show a full bar that is not counting down yet."""
        self._anim.stop()
        self._t = 1.0
        self.update()

    def stop(self):
        self._anim.stop()
        self._t = 1.0
        self.update()

    def _set_t(self, value):
        self._t = float(value)
        self.update()

    def refresh_theme(self, colors):
        self._colors = colors
        self.update()

    def mouseReleaseEvent(self, event):  # noqa: N802
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mouseReleaseEvent(event)

    def paintEvent(self, _event):  # noqa: N802
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        r = QRectF(self.rect())
        radius = r.height() / 2
        track = QColor(self._colors["text_dim"])
        track.setAlpha(38)
        p.setPen(Qt.NoPen)
        p.setBrush(track)
        p.drawRoundedRect(r, radius, radius)
        width = r.width() * max(0.0, min(1.0, self._t))
        if width > 0:
            p.setBrush(QColor(self._colors["success"]))
            p.drawRoundedRect(QRectF(r.left(), r.top(), max(r.height(), width),
                                     r.height()), radius, radius)
        p.end()


class _StatusMixBar(QWidget):
    """How the upcoming deck breaks down by learning status.

    One proportional segment per status, in the same ramp the words table and
    the prompt card use. It turns "20 questions" into something you can act on
    — a deck that is all Mastered is a different sitting from one that is all
    New — and it gives the picker's empty middle a reason to exist.
    """

    def __init__(self, colors, parent=None):
        super().__init__(parent)
        self._colors = colors
        self._counts = []  # (status, count), highest rung last
        self.setFixedHeight(10)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def set_counts(self, counts):
        self._counts = list(counts)
        self.update()

    def refresh_theme(self, colors):
        self._colors = colors
        self.update()

    def paintEvent(self, _event):  # noqa: N802
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        r = QRectF(self.rect())
        radius = r.height() / 2
        p.setPen(Qt.NoPen)
        total = sum(n for _, n in self._counts)
        if not total:
            track = QColor(self._colors["text_dim"])
            track.setAlpha(38)
            p.setBrush(track)
            p.drawRoundedRect(r, radius, radius)
            p.end()
            return
        # Rounded ends on the whole bar, square joins between segments: drawn
        # into a clip of the full rounded rect so the seams stay flush.
        path = QPainterPath()
        path.addRoundedRect(r, radius, radius)
        p.setClipPath(path)
        x = r.left()
        for i, (status, count) in enumerate(self._counts):
            width = r.width() * (count / total)
            if i == len(self._counts) - 1:
                width = r.right() - x  # absorb rounding, leave no sliver
            p.setBrush(QColor(theme.status_style(status)["ink"]))
            p.drawRect(QRectF(x, r.top(), width, r.height()))
            x += width
        p.end()


class _ScoreRing(QWidget):
    """The final score as a ring that fills to the share answered correctly."""

    def __init__(self, colors, parent=None):
        super().__init__(parent)
        self._colors = colors
        self._t = 0.0
        self._anim = QVariantAnimation(self)
        self._anim.setDuration(RING_ANIM_MS)
        self._anim.setEasingCurve(QEasingCurve.OutCubic)
        self._anim.valueChanged.connect(self._set_t)
        self.setFixedSize(168, 168)

    def set_score(self, fraction, animate=True):
        target = max(0.0, min(1.0, float(fraction)))
        self._anim.stop()
        if not animate:
            self._t = target
            self.update()
            return
        self._anim.setStartValue(0.0)
        self._anim.setEndValue(target)
        self._anim.start()

    def _set_t(self, value):
        self._t = float(value)
        self.update()

    def refresh_theme(self, colors):
        self._colors = colors
        self.update()

    def paintEvent(self, _event):  # noqa: N802
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        stroke = 11
        r = QRectF(self.rect()).adjusted(stroke / 2 + 1, stroke / 2 + 1,
                                         -stroke / 2 - 1, -stroke / 2 - 1)
        track = QColor(self._colors["text_dim"])
        track.setAlpha(45)
        p.setPen(QPen(track, stroke, Qt.SolidLine, Qt.FlatCap))
        p.drawArc(r, 0, 360 * 16)
        if self._t > 0:
            p.setPen(QPen(QColor(self._colors["success"]), stroke,
                          Qt.SolidLine, Qt.RoundCap))
            p.drawArc(r, 90 * 16, -round(360 * 16 * self._t))
        p.end()


class QuizPage(QWidget):
    """Deck picker → question loop → score summary."""

    status_change_requested = Signal(str, str, str)  # word_id, status, label
    ignore_requested = Signal(str, str, str)         # word_id, previous, label

    STATE_PICKER, STATE_SESSION, STATE_COMPLETE = 0, 1, 2

    def __init__(self, db_adapter, colors, deck_provider, pool_provider,
                 settings_provider, parent=None):
        super().__init__(parent)
        self.db_adapter = db_adapter
        self._colors = colors
        self._deck_provider = deck_provider
        self._pool_provider = pool_provider
        self._settings_provider = settings_provider

        self._questions = []
        self._answers = []          # index-aligned with _questions
        self._index = 0
        self._graded = set()
        self._drill = False
        self._definitions = {}
        self._option_rows = []
        self._speak_cancel = None
        self._advance_timer = QTimer(self)
        self._advance_timer.setSingleShot(True)
        self._advance_timer.timeout.connect(self._next_question)
        # Fires only if pronunciation never reports back — see the constant.
        self._stall_timer = QTimer(self)
        self._stall_timer.setSingleShot(True)
        self._stall_timer.timeout.connect(
            lambda: self._begin_countdown(spoken=True))
        self._preview_timer = QTimer(self)
        self._preview_timer.setSingleShot(True)
        self._preview_timer.setInterval(160)
        self._preview_timer.timeout.connect(self._refresh_picker_info)
        self._preview_total = 0
        self._missed_deck = []
        self._count_anim = QVariantAnimation(self)
        self._count_anim.setDuration(COUNT_ANIM_MS)
        self._count_anim.setEasingCurve(QEasingCurve.OutCubic)
        self._count_anim.valueChanged.connect(
            lambda v: self.count_value.setText(str(int(v))))
        # An animation that never runs (the page is hidden) or is cut short
        # must still leave the real number on screen, not a frame of the ramp.
        self._count_anim.finished.connect(
            lambda: self.count_value.setText(str(self._preview_total)))

        self._recentring = False
        self.setFocusPolicy(Qt.StrongFocus)
        self._build_ui()
        self._apply_styles()

    # ------------------------------------------------------------------ ui

    def _build_ui(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(28, 24, 28, 30)
        self._stack = QStackedLayout()
        self._stack.setStackingMode(QStackedLayout.StackOne)
        outer.addLayout(self._stack)

        from app.config import get_bool, get_int
        settings = self._settings_provider()
        size = max(1, min(200, get_int(settings, "quiz_deck_size", 20)))
        fmt = str(settings.get("quiz_format") or "choices")
        direction = str(settings.get("quiz_direction") or "term")

        self._stack.addWidget(self._build_picker(
            size, fmt if fmt in quiz.FORMATS else "choices",
            direction if direction in quiz.DIRECTIONS else "term",
            get_bool(settings, "quiz_shuffle", False),
            get_bool(settings, "quiz_pronounce", True),
            get_bool(settings, "quiz_auto_advance", True)))
        self._stack.addWidget(self._build_session())
        self._stack.addWidget(self._build_complete())

    def _chip_group(self, flow, options, checked):
        """A row of exclusive #chipButton choices, returned keyed by value."""
        group = QButtonGroup(self)
        group.setExclusive(True)
        chips = {}
        for value, label in options:
            chip = QPushButton(label, objectName="chipButton")
            chip.setCheckable(True)
            chip.setCursor(Qt.PointingHandCursor)
            chip.setChecked(value == checked)
            group.addButton(chip)
            chips[value] = chip
            flow.addWidget(chip)
        return group, chips

    def _build_picker(self, size, fmt, direction, shuffle_on, pronounce_on,
                      auto_advance_on):
        picker = QWidget()
        pk = QVBoxLayout(picker)
        pk.setContentsMargins(0, 0, 0, 0)
        pk.setSpacing(12)

        self.picker_panel = _Panel(self._colors, max_width=None)
        # The controls flow wraps to more rows as the window narrows, so the
        # bar's height depends on its width. `_Panel` is Fixed vertically,
        # which caps its maximum at sizeHint and stops heightForWidth from
        # growing it — the bar clipped its last chip. Minimum lifts that cap,
        # so the layout gets the right height in the pass that resizes it,
        # rather than needing a correction one frame later (which is what made
        # the title visibly hop while the window was being dragged).
        sp = self.picker_panel.sizePolicy()
        sp.setVerticalPolicy(QSizePolicy.Minimum)
        sp.setHeightForWidth(True)
        self.picker_panel.setSizePolicy(sp)
        bar = QVBoxLayout(self.picker_panel)
        bar.setContentsMargins(24, 14, 24, 16)
        bar.setSpacing(10)

        head = QHBoxLayout()
        head.setSpacing(14)
        # Claims the same box as the Flashcards deck emblem, so the two study
        # pages open with a mark of one size and their titles sit on one line.
        self.picker_icon = QLabel(alignment=Qt.AlignCenter)
        self.picker_icon.setFixedSize(_DeckLogo.size_for(PICKER_LOGO_SCALE))
        head.addWidget(self.picker_icon, 0, Qt.AlignVCenter)
        id_col = QVBoxLayout()
        id_col.setSpacing(2)
        id_col.addStretch(1)
        self.picker_title = QLabel(tr("Quiz"))
        # Elided, not plain: a full-width subtitle would pin the whole page's
        # minimum width to its own text and clip the control flow below it.
        self.picker_sub = ElidedLabel(min_width=40)
        self.picker_sub.set_full_text(
            tr("Recall your words, one question at a time"))
        id_col.addWidget(self.picker_title)
        id_col.addWidget(self.picker_sub)
        id_col.addStretch(1)
        head.addLayout(id_col)
        head.addStretch(1)
        bar.addLayout(head)

        flow_host = QWidget()
        fsp = flow_host.sizePolicy()
        fsp.setHeightForWidth(True)
        flow_host.setSizePolicy(fsp)
        flow = FlowLayout(flow_host, margin=0, h_spacing=8, v_spacing=8)

        self._deck_group, self._deck_chips = self._chip_group(
            flow, (("due", tr("Due cards")), ("filtered", tr("Current filter")),
                   ("newest", tr("Newest")), ("selected", tr("Selected words"))),
            "due")
        self._deck_group.buttonToggled.connect(self._on_chip_toggled)

        size_widget = QWidget()
        size_lay = QHBoxLayout(size_widget)
        size_lay.setContentsMargins(12, 0, 0, 0)
        size_lay.setSpacing(6)
        self.size_label = QLabel(tr("Questions"))
        self.size_spin = QSpinBox()
        self.size_spin.setRange(1, 200)
        self.size_spin.setValue(size)
        self.size_spin.setMinimumWidth(72)
        self.size_spin.valueChanged.connect(self._persist_quiz_prefs)
        self.size_spin.valueChanged.connect(self._schedule_picker_refresh)
        size_lay.addWidget(self.size_label)
        size_lay.addWidget(self.size_spin)
        flow.addWidget(size_widget)
        bar.addWidget(flow_host)

        modes_host = QWidget()
        msp = modes_host.sizePolicy()
        msp.setHeightForWidth(True)
        modes_host.setSizePolicy(msp)
        modes = FlowLayout(modes_host, margin=0, h_spacing=8, v_spacing=8)

        self.format_label = QLabel(tr("Answer with"))
        modes.addWidget(self.format_label)
        self._format_group, self._format_chips = self._chip_group(
            modes, (("choices", tr("Choices")), ("typing", tr("Typing"))), fmt)
        self._format_group.buttonToggled.connect(self._on_chip_toggled)

        self.ask_label = QLabel(tr("Ask"))
        self.ask_label.setContentsMargins(12, 0, 0, 0)
        modes.addWidget(self.ask_label)
        self._direction_group, self._direction_chips = self._chip_group(
            modes, (("term", tr("Term")), ("translation", tr("Translation")),
                    ("mixed", tr("Mixed"))), direction)
        self._direction_group.buttonToggled.connect(self._on_chip_toggled)

        self.shuffle_btn = self._toggle_chip(tr("Shuffle"), shuffle_on)
        self.pronounce_btn = self._toggle_chip(
            tr("Auto-pronounce"), pronounce_on,
            tr("Speak the question, then the answer once it is revealed"))
        self.advance_btn = self._toggle_chip(
            tr("Auto-advance"), auto_advance_on,
            tr("Move on by itself after a correct answer"))
        # Added to the flow one by one, never boxed together: a group of three
        # in an HBox cannot wrap apart, so its combined width would become the
        # page's minimum and clip the whole bar on a narrow window.
        for btn in (self.shuffle_btn, self.pronounce_btn, self.advance_btn):
            modes.addWidget(btn)
        bar.addWidget(modes_host)
        pk.addWidget(self.picker_panel)

        pk.addStretch(3)
        self.session_panel = _Panel(self._colors, max_width=460)
        # Between two stretches the panel would collapse to its content width.
        # The floor stays under the page minimum so a narrow window still fits.
        self.session_panel.setMinimumWidth(300)
        card = QVBoxLayout(self.session_panel)
        card.setContentsMargins(28, 24, 28, 24)
        card.setSpacing(0)

        self.count_value = QLabel("0", alignment=Qt.AlignCenter)
        self.count_caption = QLabel(alignment=Qt.AlignCenter)
        card.addWidget(self.count_value)
        card.addWidget(self.count_caption)

        self.mix_bar = _StatusMixBar(self._colors)
        card.addSpacing(20)
        card.addWidget(self.mix_bar)
        self.mix_legend = QLabel(alignment=Qt.AlignCenter)
        self.mix_legend.setWordWrap(True)
        self.mix_legend.setTextFormat(Qt.RichText)
        card.addSpacing(10)
        card.addWidget(self.mix_legend)

        self.picker_hint = QLabel(alignment=Qt.AlignCenter)
        self.picker_hint.setWordWrap(True)
        self.picker_hint.setVisible(False)
        card.addSpacing(10)
        card.addWidget(self.picker_hint)

        self.start_btn = QPushButton(tr("Start quiz"), objectName="primaryButton")
        self.start_btn.setCursor(Qt.PointingHandCursor)
        self.start_btn.setMinimumHeight(46)
        self.start_btn.clicked.connect(self._start_clicked)
        card.addSpacing(22)
        card.addWidget(self.start_btn)

        card_row = QHBoxLayout()
        card_row.addStretch(1)
        card_row.addWidget(self.session_panel, 2)
        card_row.addStretch(1)
        pk.addLayout(card_row)
        pk.addStretch(4)
        return picker

    def _toggle_chip(self, label, checked, tooltip=None):
        btn = QPushButton(label, objectName="toggleChip")
        btn.setCheckable(True)
        btn.setChecked(checked)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setIconSize(QSize(14, 14))
        if tooltip:
            btn.setToolTip(tooltip)
        btn.toggled.connect(self._persist_quiz_prefs)
        return btn

    def _build_session(self):
        session = QWidget()
        sv = QVBoxLayout(session)
        sv.setContentsMargins(0, 0, 0, 0)
        sv.setSpacing(10)

        top = QHBoxLayout()
        self.progress_label = QLabel("")
        self.session_tag = QLabel(tr("Missed words"))
        self.session_tag.setVisible(False)
        self.correct_label = QLabel("")
        self.end_btn = QPushButton(objectName="iconButton")
        self.end_btn.setToolTip(tr("End quiz"))
        self.end_btn.setCursor(Qt.PointingHandCursor)
        self.end_btn.setIconSize(QSize(16, 16))
        self.end_btn.clicked.connect(self._show_picker)
        top.addWidget(self.progress_label)
        top.addSpacing(8)
        top.addWidget(self.session_tag)
        top.addStretch(1)
        top.addWidget(self.correct_label)
        top.addSpacing(8)
        top.addWidget(self.end_btn)
        sv.addLayout(top)
        self.slim_bar = _SlimBar(
            self._colors, color_keys={"correct": "success", "wrong": "danger"})
        sv.addWidget(self.slim_bar)

        # The question column is scrollable: a long definition in the feedback
        # block must not push the Next button off the bottom of the page.
        self.session_scroll = QScrollArea()
        self.session_scroll.setWidgetResizable(True)
        self.session_scroll.setFrameShape(QFrame.NoFrame)
        self.session_scroll.viewport().setAutoFillBackground(False)
        body = QWidget()
        body.setAutoFillBackground(False)
        col_row = QHBoxLayout(body)
        col_row.setContentsMargins(0, 18, 0, SESSION_PAD)
        col_row.addStretch(1)
        column = QVBoxLayout()
        column.setSpacing(10)
        col_row.addLayout(column, 6)
        col_row.addStretch(1)
        self._session_body = body
        # A measured spacer, not a stretch: a stretch would recentre the whole
        # column the moment the feedback block appears and yank the card upward
        # mid-answer. _recentre_question sizes this one instead.
        self._question_spacer = QWidget()
        self._question_spacer.setFixedHeight(0)
        column.addWidget(self._question_spacer)

        self.prompt_card = _PromptCard(self._colors)
        self.prompt_card.speak_clicked.connect(self._speak_prompt)
        self.prompt_card.ignore_clicked.connect(self._ignore_current)
        column.addWidget(self.prompt_card)

        self.options_host = QWidget()
        self.options_lay = QVBoxLayout(self.options_host)
        self.options_lay.setContentsMargins(0, 0, 0, 0)
        self.options_lay.setSpacing(8)
        column.addWidget(self.options_host)

        self.typing_host = QWidget()
        typing = QVBoxLayout(self.typing_host)
        typing.setContentsMargins(0, 0, 0, 0)
        typing.setSpacing(8)
        self.answer_edit = QLineEdit()
        self.answer_edit.setPlaceholderText(tr("Type the answer"))
        self.answer_edit.setMinimumHeight(46)
        self.answer_edit.returnPressed.connect(self._submit_typed)
        typing.addWidget(self.answer_edit)
        typing_actions = QHBoxLayout()
        typing_actions.setSpacing(10)
        self.reveal_btn = QPushButton(tr("Show answer"), objectName="chipButton")
        self.reveal_btn.setCursor(Qt.PointingHandCursor)
        self.reveal_btn.setMinimumHeight(42)
        self.reveal_btn.clicked.connect(self._reveal_answer)
        self.check_btn = QPushButton(tr("Check"), objectName="primaryButton")
        self.check_btn.setCursor(Qt.PointingHandCursor)
        self.check_btn.setMinimumHeight(42)
        self.check_btn.clicked.connect(self._submit_typed)
        typing_actions.addWidget(self.reveal_btn, 1)
        typing_actions.addWidget(self.check_btn, 2)
        typing.addLayout(typing_actions)
        column.addWidget(self.typing_host)

        # Named so its stylesheet can be scoped: an unscoped rule on a parent
        # widget also matches every child, which drew the block's border around
        # each label inside it.
        self.feedback = QWidget(objectName="QuizFeedback")
        fb = QVBoxLayout(self.feedback)
        fb.setContentsMargins(14, 12, 14, 12)
        fb.setSpacing(6)
        verdict_row = QHBoxLayout()
        verdict_row.setSpacing(8)
        self.verdict_icon = QLabel()
        self.verdict_icon.setFixedWidth(20)
        self.verdict_label = QLabel()
        self.verdict_label.setWordWrap(True)
        verdict_row.addWidget(self.verdict_icon, 0, Qt.AlignTop)
        verdict_row.addWidget(self.verdict_label, 1)
        fb.addLayout(verdict_row)
        # The promotion belongs here and not in a toast: show_toast floats over
        # the bottom-right of the page, exactly where the Next button sits.
        self.promotion_label = QLabel()
        self.promotion_label.setVisible(False)
        fb.addWidget(self.promotion_label)
        self.definition_label = QLabel()
        self.definition_label.setWordWrap(True)
        self.definition_label.setVisible(False)
        fb.addWidget(self.definition_label)
        self.feedback.setVisible(False)
        column.addWidget(self.feedback)
        column.addStretch(1)

        self.session_scroll.setWidget(body)
        self.session_scroll.viewport().installEventFilter(self)
        body.installEventFilter(self)
        sv.addWidget(self.session_scroll, 1)

        # Stacked, not shown and hidden: a stacked layout is always as tall as
        # its tallest page, so the question area above keeps one height whether
        # the footer is empty, counting down, or offering Next.
        self.footer = QWidget()
        self.footer_stack = QStackedLayout(self.footer)
        self.footer_stack.setContentsMargins(0, 0, 0, 0)
        self.footer_blank = QWidget()
        self.footer_stack.addWidget(self.footer_blank)
        self.drain_host = QWidget()
        drain = QVBoxLayout(self.drain_host)
        drain.setContentsMargins(0, 6, 0, 0)
        drain.setSpacing(4)
        self.drain_bar = _DrainBar(self._colors)
        self.drain_bar.clicked.connect(self._next_question)
        self.drain_caption = QLabel(tr("Click to continue"),
                                    alignment=Qt.AlignCenter)
        drain.addWidget(self.drain_bar)
        drain.addWidget(self.drain_caption)
        self.footer_stack.addWidget(self.drain_host)
        self.next_btn = QPushButton(tr("Next"), objectName="primaryButton")
        self.next_btn.setCursor(Qt.PointingHandCursor)
        self.next_btn.setMinimumHeight(48)
        self.next_btn.clicked.connect(self._next_question)
        self.footer_stack.addWidget(self.next_btn)
        self.footer_stack.setCurrentWidget(self.footer_blank)
        sv.addWidget(self.footer)
        return session

    def _recentre_question(self):
        """Sit the prompt and answers in the middle of the question area.

        Measured from the laid-out geometry instead of being centred by
        stretches, so the block keeps its place when the feedback grows below
        it. Only feedback too tall to fit moves it, and only as far as it must.
        """
        body = getattr(self, "_session_body", None)
        if body is None or not body.isVisible() or self._recentring:
            return
        # Resizing the spacer can bring a scroll bar in or out, which resizes
        # the viewport, which lands back here.
        self._recentring = True
        try:
            self._measure_question(body)
        finally:
            self._recentring = False

    def _measure_question(self, body):
        body.layout().activate()
        viewport = self.session_scroll.viewport().height()
        host = (self.options_host if self.options_host.isVisibleTo(body)
                else self.typing_host)
        top = self.prompt_card.y()
        lead = top - self._question_spacer.height()  # margin above the spacer
        group = host.y() + host.height() - top
        want = (viewport - group) // 2 - lead
        if self.feedback.isVisibleTo(body):
            tail = self.feedback.y() + self.feedback.height() - top - group
            want = min(want, viewport - lead - group - tail - SESSION_PAD)
        self._question_spacer.setFixedHeight(max(0, want))

    def eventFilter(self, obj, event):  # noqa: N802
        # Recentre when the question area settles, not when the page resizes:
        # the block's own height is only final a layout pass after its options
        # are swapped in, and the viewport's only after the animated page swap.
        if obj is self.session_scroll.viewport():
            if event.type() == QEvent.Resize:
                self._recentre_question()
        elif obj is self._session_body:
            if event.type() == QEvent.LayoutRequest:
                self._recentre_question()
        return super().eventFilter(obj, event)

    def _build_complete(self):
        complete = QWidget()
        cv = QVBoxLayout(complete)
        cv.setContentsMargins(0, 0, 0, 0)
        cv.setSpacing(10)
        cv.addStretch(1)

        self.complete_title = QLabel(alignment=Qt.AlignCenter)
        cv.addWidget(self.complete_title)

        ring_row = QHBoxLayout()
        ring_row.addStretch(1)
        ring_host = QWidget()
        ring_host.setFixedSize(168, 168)
        self.ring = _ScoreRing(self._colors, ring_host)
        self.ring.move(0, 0)
        ring_inner = QVBoxLayout(ring_host)
        ring_inner.setContentsMargins(0, 0, 0, 0)
        ring_inner.setSpacing(0)
        self.ring_score = QLabel(alignment=Qt.AlignCenter)
        self.ring_caption = QLabel(tr("Correct"), alignment=Qt.AlignCenter)
        ring_inner.addStretch(1)
        ring_inner.addWidget(self.ring_score)
        ring_inner.addWidget(self.ring_caption)
        ring_inner.addStretch(1)
        ring_row.addWidget(ring_host)
        ring_row.addStretch(1)
        cv.addSpacing(6)
        cv.addLayout(ring_row)

        tally_row = QHBoxLayout()
        tally_row.addStretch(1)
        self.tally_correct = self._tally(tally_row, tr("Correct"))
        tally_row.addSpacing(48)
        self.tally_missed = self._tally(tally_row, tr("Missed"))
        tally_row.addStretch(1)
        cv.addSpacing(10)
        cv.addLayout(tally_row)

        self.missed_panel = _Panel(self._colors, max_width=520)
        missed = QVBoxLayout(self.missed_panel)
        missed.setContentsMargins(18, 14, 18, 14)
        missed.setSpacing(4)
        self.missed_title = QLabel(tr("Worth another look"))
        missed.addWidget(self.missed_title)
        self.missed_list = QLabel()
        self.missed_list.setWordWrap(True)
        missed.addWidget(self.missed_list)
        missed_row = QHBoxLayout()
        missed_row.addStretch(1)
        missed_row.addWidget(self.missed_panel)
        missed_row.addStretch(1)
        self.missed_panel.setVisible(False)
        cv.addSpacing(14)
        cv.addLayout(missed_row)

        actions = QHBoxLayout()
        actions.addStretch(1)
        self.practice_btn = QPushButton(objectName="primaryButton")
        self.practice_btn.setCursor(Qt.PointingHandCursor)
        self.practice_btn.setMinimumHeight(44)
        self.practice_btn.clicked.connect(self._practice_missed_clicked)
        self.again_btn = QPushButton(tr("Again"), objectName="chipButton")
        self.again_btn.setCursor(Qt.PointingHandCursor)
        self.again_btn.setMinimumHeight(44)
        self.again_btn.clicked.connect(self._again_clicked)
        self.done_btn = QPushButton(tr("Done"), objectName="chipButton")
        self.done_btn.setCursor(Qt.PointingHandCursor)
        self.done_btn.setMinimumHeight(44)
        self.done_btn.clicked.connect(self._show_picker)
        for btn in (self.practice_btn, self.again_btn, self.done_btn):
            actions.addWidget(btn)
        actions.addStretch(1)
        cv.addSpacing(16)
        cv.addLayout(actions)
        cv.addStretch(2)
        return complete

    def _tally(self, row, label_text):
        host = QWidget()
        lay = QVBoxLayout(host)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        value = QLabel(alignment=Qt.AlignCenter)
        caption = QLabel(label_text, alignment=Qt.AlignCenter)
        lay.addWidget(value)
        lay.addWidget(caption)
        row.addWidget(host)
        return value, caption

    # -------------------------------------------------------------- styling

    def refresh_theme(self, colors):
        self._colors = colors
        self.picker_panel.refresh_theme(colors)
        self.session_panel.refresh_theme(colors)
        self.missed_panel.refresh_theme(colors)
        self.mix_bar.refresh_theme(colors)
        self.slim_bar.refresh_theme(colors)
        self.prompt_card.refresh_theme(colors)
        self.drain_bar.refresh_theme(colors)
        self.ring.refresh_theme(colors)
        for row in self._option_rows:
            row.refresh_theme(colors)
        self._apply_styles()
        self._recentre_question()

    def _apply_styles(self):
        c = self._colors
        dim = f"color:{c['text_dim']};background:transparent;"
        body = f"font-size:{theme.font_pt('body')}pt;"
        # Derived from the box so it tracks the shared emblem scale.
        glyph = max(24, int(self.picker_icon.height() * 0.88))
        self.picker_icon.setPixmap(icons.pixmap("quiz", c["accent"], glyph))
        self.picker_title.setStyleSheet(
            f"color:{c['text']};background:transparent;"
            f"font-size:{theme.font_pt('title')}pt;font-weight:700;")
        for label in (self.picker_sub, self.size_label, self.format_label,
                      self.ask_label, self.count_caption, self.picker_hint,
                      self.drain_caption, self.ring_caption, self.mix_legend):
            label.setStyleSheet(dim + body)
        self.picker_hint.setStyleSheet(
            dim + f"font-size:{theme.font_pt('caption')}pt;")
        self.mix_legend.setStyleSheet(
            f"background:transparent;font-size:{theme.font_pt('caption')}pt;")
        self.count_value.setStyleSheet(
            f"color:{c['accent']};background:transparent;font-weight:700;"
            f"font-size:{theme.font_pt('hero')}pt;")
        self.progress_label.setStyleSheet(dim + "font-weight:600;")
        self.session_tag.setStyleSheet(
            f"color:{c['danger']};background:{_soft(c['danger'], 34)};"
            "padding:2px 10px;border-radius:9px;"
            f"font-size:{theme.font_pt('caption')}pt;font-weight:600;")
        self.correct_label.setStyleSheet(
            f"color:{c['success']};background:transparent;font-weight:600;")
        self.definition_label.setStyleSheet(dim + body)
        self.promotion_label.setStyleSheet(dim + body)
        self.session_scroll.setStyleSheet(
            "QScrollArea{background:transparent;}"
            "QScrollArea > QWidget > QWidget{background:transparent;}")
        self.complete_title.setStyleSheet(
            f"color:{c['text']};background:transparent;"
            f"font-size:{theme.font_pt('headline')}pt;font-weight:700;")
        self.ring_score.setStyleSheet(
            f"color:{c['text']};background:transparent;font-weight:700;"
            f"font-size:{theme.font_pt('title')}pt;")
        self.missed_title.setStyleSheet(
            f"color:{c['text']};background:transparent;font-weight:700;"
            f"font-size:{theme.font_pt('body')}pt;")
        self.missed_list.setStyleSheet(dim + body)
        for (value, caption), key in ((self.tally_correct, "success"),
                                      (self.tally_missed, "danger")):
            value.setStyleSheet(
                f"color:{c[key]};background:transparent;font-weight:700;"
                f"font-size:{theme.font_pt('headline')}pt;")
            caption.setStyleSheet(dim + body)
        self.end_btn.setIcon(icons.icon("x", c["text_dim"], 16))

        def toggle_icon(name):
            ic = QIcon()
            ic.addPixmap(icons.pixmap(name, c["text_dim"], 14),
                         QIcon.Normal, QIcon.Off)
            ic.addPixmap(icons.pixmap(name, c["accent_text"], 14),
                         QIcon.Normal, QIcon.On)
            return ic

        self.shuffle_btn.setIcon(toggle_icon("shuffle"))
        self.pronounce_btn.setIcon(toggle_icon("volume"))
        self.advance_btn.setIcon(toggle_icon("play"))
        self._style_answer_edit()
        self._style_feedback()

    def _style_answer_edit(self, verdict=None):
        c = self._colors
        tint = _verdict_color(verdict, c) if verdict else c["border"]
        width = 2 if verdict else 1
        self.answer_edit.setStyleSheet(
            f"QLineEdit{{background:{c['surface']};color:{c['text']};"
            f"border:{width}px solid {tint};border-radius:12px;padding:6px 12px;"
            f"font-size:{theme.font_pt('body_lg')}pt;}}"
            f"QLineEdit:focus{{border-color:{c['accent']};}}"
            f"QLineEdit:disabled{{color:{c['text']};background:{c['surface']};}}")

    def _style_feedback(self, verdict=None):
        c = self._colors
        tint = _verdict_color(verdict, c) if verdict else c["border"]
        self.feedback.setStyleSheet(
            f"QWidget#QuizFeedback{{background:{_soft(tint, 26)};"
            f"border:1px solid {_soft(tint, 90)};border-radius:12px;}}")
        self.verdict_label.setStyleSheet(
            f"color:{tint};background:transparent;font-weight:600;"
            f"font-size:{theme.font_pt('body_lg')}pt;")

    # -------------------------------------------------------------- picker

    def on_shown(self):
        """Called by the main window whenever the page becomes current.

        The page slides in behind a snapshot overlay, so anything that queries
        or relayouts here fights that animation for frames — which is what made
        the picker visibly jump and resize on the first open. Only the cheap
        chip state runs synchronously, so the grabbed frame looks right; the
        deck query and the count roll-up wait until the slide has landed.
        """
        self._settle_geometry()
        if self._stack.currentIndex() == self.STATE_PICKER:
            self._refresh_picker_chips()
            QTimer.singleShot(AnimatedStackedWidget.DURATION + 40,
                              self._on_shown_settled)
        self.setFocus(Qt.OtherFocusReason)

    def _settle_geometry(self):
        """Lay the page out at its real size before the stack snapshots it.

        A hidden page keeps whatever geometry it was last laid out at, which
        is narrower than the stack — so the control flow wraps to extra rows
        and the bar is taller. The page transition grabs the incoming page the
        instant it becomes current, so without this the crossfade blends that
        stale tall frame into the settled short one and the bar visibly jumps
        from bigger to smaller.
        """
        parent = self.parentWidget()
        if parent is not None and self.size() != parent.size():
            self.resize(parent.size())
        layout = self.layout()
        if layout is not None:
            layout.activate()

    def _on_shown_settled(self):
        if not self.isVisible() or self._stack.currentIndex() != self.STATE_PICKER:
            return  # already navigated away, or a session has started
        self._refresh_picker_info()

    def _on_chip_toggled(self, _btn, on):
        if on:
            self._persist_quiz_prefs()
            self._schedule_picker_refresh()

    def _schedule_picker_refresh(self, *_args):
        self._preview_timer.start()

    def _checked(self, chips, fallback):
        for value, chip in chips.items():
            if chip.isChecked():
                return value
        return fallback

    def _deck_kind(self):
        return self._checked(self._deck_chips, "due")

    def _format(self):
        return self._checked(self._format_chips, "choices")

    def _direction(self):
        return self._checked(self._direction_chips, "term")

    def _refresh_picker_chips(self):
        has_selection = bool(self._fetch_deck("selected", 1))
        chip = self._deck_chips["selected"]
        # Re-checking a chip fires buttonToggled → a provider query; callers
        # decide when to refresh the count, so keep this a pure state update.
        self._deck_group.blockSignals(True)
        chip.setEnabled(has_selection)
        if has_selection:
            chip.setChecked(True)
        elif chip.isChecked():
            self._deck_chips["due"].setChecked(True)
        self._deck_group.blockSignals(False)

    def _refresh_picker_info(self):
        deck = self._fetch_deck(self._deck_kind(), self.size_spin.value())
        total = len(deck)
        library = self._pool_count()
        choices = self._format() == "choices"
        # A choices question needs somewhere to draw wrong answers from, so a
        # one-word library can be quizzed by typing but not by picking.
        blocked = not total or (choices and library < 2)
        self._animate_count(total)
        self.count_caption.setText(
            tr("questions ready") if total else tr("Nothing to quiz"))
        self._refresh_mix(deck)
        if not total:
            hint = (tr("No cards due — great job!")
                    if self._deck_kind() == "due"
                    else tr("No words match this deck."))
        elif choices and library < 2:
            hint = tr("A quiz needs at least two words — the ones you are not "
                      "being asked about are where the wrong answers come from.")
        else:
            hint = ""
        self.picker_hint.setText(hint)
        self.picker_hint.setVisible(bool(hint))
        self.start_btn.setEnabled(not blocked)

    def _refresh_mix(self, deck):
        """Break the upcoming deck down by status, in ladder order."""
        counts = Counter(str(rec.get("Status") or "New").strip() or "New"
                         for rec in deck)
        # Ladder order, so the bar always reads New → Mastered left to right and
        # doesn't reshuffle its colours when one status happens to grow.
        ordered = [(s, counts.pop(s)) for s in progression.LADDER if s in counts]
        ordered += sorted(counts.items())  # "To Learn", Ignored, custom statuses
        self.mix_bar.set_counts(ordered)
        c = self._colors
        parts = []
        for status, n in ordered:
            # Every space *inside* an entry is non-breaking, so a wrapping
            # legend breaks between entries and never mid-status-name.
            label = f"{tr(status)} {n}".replace(" ", "&nbsp;")
            parts.append(
                f'<span style="color:{theme.status_style(status)["ink"]};">'
                f'●&nbsp;</span>'
                f'<span style="color:{c["text_dim"]};">{label}</span>')
        self.mix_legend.setText("&nbsp; ".join(parts))
        self.mix_bar.setVisible(bool(ordered))
        self.mix_legend.setVisible(bool(ordered))

    def _animate_count(self, total):
        self._count_anim.stop()
        start = self._preview_total
        self._preview_total = total
        if start == total:
            self.count_value.setText(str(total))
            return
        self._count_anim.setStartValue(int(start))
        self._count_anim.setEndValue(int(total))
        self._count_anim.start()

    def _fetch_deck(self, kind, n):
        try:
            return list(self._deck_provider(kind, n) or [])
        except Exception as exc:
            logging.error(f"Quiz deck fetch failed: {exc}")
            return []

    def _pool(self):
        try:
            return list(self._pool_provider() or [])
        except Exception as exc:
            logging.error(f"Quiz word pool fetch failed: {exc}")
            return []

    def _pool_count(self):
        """How many words the distractor pool holds, without building it."""
        try:
            return int(self._pool_provider(count_only=True) or 0)
        except TypeError:
            return len(self._pool())  # provider predates the count fast path
        except Exception as exc:
            logging.error(f"Quiz word pool count failed: {exc}")
            return 0

    def _persist_quiz_prefs(self, *_args):
        try:
            from app.config import save_settings
            settings = self._settings_provider()
            settings["quiz_deck_size"] = str(self.size_spin.value())
            settings["quiz_format"] = self._format()
            settings["quiz_direction"] = self._direction()
            settings["quiz_shuffle"] = str(self.shuffle_btn.isChecked())
            settings["quiz_pronounce"] = str(self.pronounce_btn.isChecked())
            settings["quiz_auto_advance"] = str(self.advance_btn.isChecked())
            save_settings(settings)
        except Exception as exc:
            logging.error(f"Saving quiz prefs failed: {exc}")

    # ------------------------------------------------------------- session

    def _start_clicked(self):
        records = self._fetch_deck(self._deck_kind(), self.size_spin.value())
        if self.shuffle_btn.isChecked():
            random.shuffle(records)
        self._build_and_start(records)

    def _build_and_start(self, records, drill=False):
        questions = quiz.build_quiz(
            records, self._pool(), self._format(),
            direction=self._direction())
        if not questions:
            show_toast(self, tr("Not enough words"),
                       tr("Add a few more words, or widen the deck."),
                       "warning", 3000)
            self._show_picker()
            return
        self._questions = questions
        self._answers = []
        self._index = 0
        self._graded = set()
        self._drill = drill
        self.session_tag.setVisible(drill)
        self._stack.setCurrentIndex(self.STATE_SESSION)
        self._show_question(animate=False)

    @property
    def _revealed(self):
        """Whether the current question has been answered.

        Answers are appended the moment they are given and stay aligned with
        the question list, so their count is the state — no separate flag can
        fall out of step with it.
        """
        return len(self._answers) > self._index

    def _current(self):
        if 0 <= self._index < len(self._questions):
            return self._questions[self._index]
        return None

    def _clear_options(self):
        for row in self._option_rows:
            self.options_lay.removeWidget(row)
            row.setParent(None)
            row.deleteLater()
        self._option_rows = []

    def _show_question(self, animate=True):
        question = self._current()
        if question is None:
            self._complete()
            return
        self._advance_timer.stop()
        self._stall_timer.stop()
        self.drain_bar.stop()
        self.footer_stack.setCurrentWidget(self.footer_blank)
        self.feedback.setVisible(False)
        self.promotion_label.setVisible(False)
        self.definition_label.setVisible(False)
        self._style_feedback()
        self._style_answer_edit()

        choices = bool(question.options)
        self._clear_options()
        self.options_host.setVisible(choices)
        self.typing_host.setVisible(not choices)
        if choices:
            for i, text in enumerate(question.options):
                row = _OptionRow(i, self._colors)
                row.set_text(text)
                row.clicked.connect(self._answer_choice)
                self.options_lay.addWidget(row)
                self._option_rows.append(row)
        else:
            self.answer_edit.setEnabled(True)
            self.answer_edit.clear()
            self.reveal_btn.setEnabled(True)
            self.check_btn.setEnabled(True)

        # fade_swap snapshots what is on screen now and fades it out over
        # whatever is painted next, so the new question goes in after the call.
        if animate:
            fade_swap(self.prompt_card)
        self.prompt_card.set_question(question)
        self._refresh_session_header()
        self._recentre_question()
        self.session_scroll.verticalScrollBar().setValue(0)
        # Choices are answered with the number keys, which the page handles
        # itself; typing needs the field to have focus for the very first key.
        if choices:
            self.setFocus(Qt.OtherFocusReason)
        else:
            QTimer.singleShot(0, self.answer_edit.setFocus)
        self._speak_prompt(auto=True)

    def _refresh_session_header(self):
        total = len(self._questions)
        self.progress_label.setText(
            tr("Question {n} of {total}").format(n=min(self._index + 1, total),
                                                 total=total))
        correct = sum(1 for a in self._answers if quiz.is_correct(a["verdict"]))
        self.correct_label.setText(
            tr("{n} correct").format(n=correct) if correct else "")
        outcomes = {i: ("correct" if quiz.is_correct(a["verdict"]) else "wrong")
                    for i, a in enumerate(self._answers)}
        self.slim_bar.set_progress(len(self._answers), total, outcomes)

    # -------------------------------------------------------------- answers

    def _answer_choice(self, index):
        question = self._current()
        if question is None or self._revealed:
            return
        self._record("correct" if index == question.correct_index else "wrong",
                     picked=index)

    def _submit_typed(self):
        question = self._current()
        if question is None or self._revealed:
            return
        typed = self.answer_edit.text().strip()
        if not typed:
            return  # an empty box is an unfinished answer, not a wrong one
        self._record(quiz.verdict_for(typed, question.answer))

    def _reveal_answer(self):
        """Give up on a typed question — graded Hard, like any wrong answer."""
        if self._current() is None or self._revealed:
            return
        self._record("wrong")

    def _record(self, verdict, picked=None):
        question = self._current()
        answer = {"verdict": verdict, "picked": picked, "promoted": None}
        self._answers.append(answer)
        self.prompt_card.set_ignorable(False)
        answer["promoted"] = self._grade(question, verdict)
        self._show_verdict(question, verdict, picked)
        self._refresh_session_header()
        advancing = quiz.is_correct(verdict) and self.advance_btn.isChecked()
        if advancing:
            self.footer_stack.setCurrentWidget(self.drain_host)
            # Held full, not draining: the countdown to the next question only
            # starts once the answer has actually been heard.
            self.drain_bar.hold()
            self._stall_timer.start(AUTO_ADVANCE_STALL_MS)
        else:
            # A wrong answer never auto-advances.
            self.next_btn.setText(tr("See results")
                                  if self._index >= len(self._questions) - 1
                                  else tr("Next"))
            self.footer_stack.setCurrentWidget(self.next_btn)
        # Kicked off last, and given the countdown as its completion callback:
        # a fixed timer running alongside the audio cut long answers off
        # mid-word, because how long a word takes to say is not a constant.
        spoke = self._speak_answer(
            on_done=(lambda: self._begin_countdown(spoken=True))
            if advancing else None)
        if advancing and not spoke:
            self._begin_countdown(spoken=False)

    def _begin_countdown(self, spoken):
        """Start the run-up to the next question.

        After audio it is only a short tail — the answer has been both shown
        and heard by then — where a silent answer gets the full pause.
        """
        self._stall_timer.stop()
        if not self._revealed or self._stack.currentIndex() != self.STATE_SESSION:
            return  # already moved on, or left the session entirely
        if self._advance_timer.isActive():
            return
        delay = AUTO_ADVANCE_AFTER_SPEECH_MS if spoken else AUTO_ADVANCE_MS
        self.drain_bar.start(delay)
        self._advance_timer.start(delay)

    def _grade(self, question, verdict):
        """Write the answer into the shared SM-2 schedule and promote Status.

        Identical in shape to ``FlashcardsPage._grade`` on purpose — this is
        the same ``srs_progress`` row the flashcards, the web app and the
        mobile app all schedule from, so the two paths must not drift.
        """
        wid = question.record.get("ID")
        if wid is None or wid in self._graded:
            return None
        grade = quiz.GRADE_FOR_VERDICT[verdict]
        try:
            state = srs.apply_grade(dbq.srs_get(wid), grade, datetime.now())
            dbq.srs_upsert(wid, state)
            dbq.log_review(wid, datetime.now().isoformat(timespec="seconds"))
        except Exception as exc:
            logging.error(f"Recording quiz answer failed: {exc}")
            return None
        self._graded.add(wid)
        mapped = srs.status_from_progress(
            state["review_count"], state["ease_factor"], state["correct_count"])
        target = srs.promotion_target(question.record.get("Status"), mapped)
        if target:
            question.record["Status"] = target
            # No word label: the feedback block below the question already says
            # what the word was promoted to, so the main window's toast would
            # repeat it — and land on top of the Next button while doing so.
            self.status_change_requested.emit(str(wid), target, "")
        return target

    def _show_verdict(self, question, verdict, picked):
        c = self._colors
        for i, row in enumerate(self._option_rows):
            if i == question.correct_index:
                row.set_state("correct")
            elif i == picked:
                row.set_state("wrong")
            else:
                row.set_state("dimmed")
        if not question.options:
            self.answer_edit.setEnabled(False)
            if verdict == "wrong" and not self.answer_edit.text().strip():
                self.answer_edit.setText(question.answer)
            self.reveal_btn.setEnabled(False)
            self.check_btn.setEnabled(False)
            self._style_answer_edit(verdict)

        tint = _verdict_color(verdict, c)
        self._style_feedback(verdict)
        self.verdict_icon.setPixmap(icons.pixmap(
            "check" if quiz.is_correct(verdict) else "x", tint, 18))
        if verdict == "correct":
            text = tr("Correct")
        elif verdict == "almost":
            text = tr('Almost — it is "{answer}"').format(answer=question.answer)
        else:
            text = tr('It is "{answer}"').format(answer=question.answer)
        self.verdict_label.setText(text)

        promoted = self._answers[self._index]["promoted"]
        if promoted:
            self.promotion_label.setText(
                tr("Now {status}").format(status=tr(promoted)))
            self.promotion_label.setStyleSheet(
                f"color:{theme.status_style(promoted)['ink']};"
                f"background:transparent;font-weight:600;"
                f"font-size:{theme.font_pt('body')}pt;")
        self.promotion_label.setVisible(bool(promoted))

        definition = _snippet(self._definition_for(question.record),
                              question.prompt, limit=220)
        self.definition_label.setText(definition)
        self.definition_label.setVisible(bool(definition))
        self.feedback.setVisible(True)
        self._recentre_question()

    def _definition_for(self, record):
        wid = record.get("ID")
        if wid is None:
            return ""
        if wid not in self._definitions:
            text = ""
            try:
                row = self.db_adapter.get_word(wid) or {}
                parts = [str(row.get("Definition") or "").strip(),
                         str(row.get("Definition2") or "").strip()]
                text = "\n\n".join(p for p in parts if p)
            except Exception as exc:
                logging.error(f"Definition lookup failed: {exc}")
            self._definitions[wid] = text
        return self._definitions[wid]

    def _ignore_current(self):
        """Park the current question's word on Ignored and drop the question.

        Refused once answered — see ``_PromptCard.set_ignorable``.
        """
        if self._stack.currentIndex() != self.STATE_SESSION or self._revealed:
            return
        question = self._current()
        if question is None:
            return
        rec = question.record
        wid = rec.get("ID")
        if wid is None or not progression.is_studiable(rec.get("Status")):
            return
        previous = rec.get("Status")
        rec["Status"] = progression.IGNORED_STATUS
        self._advance_timer.stop()
        self._stall_timer.stop()
        self.drain_bar.stop()
        self.ignore_requested.emit(
            str(wid), previous if isinstance(previous, str) else "",
            str(rec.get("Word1") or ""))
        self._questions.pop(self._index)
        if not self._questions:
            self._show_picker()
        elif self._index >= len(self._questions):
            self._complete()
        else:
            self._show_question()

    def _next_question(self):
        self._advance_timer.stop()
        self._stall_timer.stop()
        self.drain_bar.stop()
        if not self._revealed:
            return
        if self._index >= len(self._questions) - 1:
            self._complete()
            return
        self._index += 1
        self._show_question()

    # ------------------------------------------------------------ pronounce

    def _pronounce_enabled(self):
        return self.pronounce_btn.isChecked()

    def _cancel_speech(self):
        if self._speak_cancel is not None:
            self._speak_cancel.set()
            self._speak_cancel = None

    def _speak(self, text, language, on_done=None):
        """Say *text*, superseding anything still in flight.

        Returns whether audio will actually play. ``on_done`` runs on the GUI
        thread once this pronunciation has finished playing, and *only* then —
        never when there was nothing to say, so the caller can tell "heard it"
        from "no audio" by the return value alone. It also never fires for a
        superseded call: that one finished because it was cancelled rather than
        heard, and letting it call back would advance off the wrong question.
        """
        text = str(text or "").strip()
        if not text or not audio.is_language_supported(language):
            return False
        self._cancel_speech()
        cancel = threading.Event()
        self._speak_cancel = cancel

        def finished():
            if cancel.is_set() or self._speak_cancel is not cancel:
                return
            self._speak_cancel = None
            if on_done is not None:
                on_done()

        run_in_thread(audio.speak_word, text, language, cancel_event=cancel,
                      on_error=lambda msg: logging.warning(
                          f"Quiz pronunciation failed: {msg}"),
                      on_finished=finished)
        return True

    def _speak_prompt(self, auto=False):
        question = self._current()
        if question is None:
            return
        if auto and not self._pronounce_enabled():
            return
        self._speak(question.prompt, question.prompt_language)

    def _speak_answer(self, on_done=None):
        """Pronounce the revealed answer. Returns whether audio will play."""
        question = self._current()
        if question is None or not self._pronounce_enabled():
            return False
        return self._speak(question.answer, question.answer_language,
                           on_done=on_done)

    # -------------------------------------------------------------- summary

    def _complete(self):
        self._advance_timer.stop()
        self._stall_timer.stop()
        self.drain_bar.stop()
        self._cancel_speech()
        total = len(self._answers)
        correct = sum(1 for a in self._answers if quiz.is_correct(a["verdict"]))
        missed = total - correct
        self._missed_deck = [self._questions[i].record
                             for i, a in enumerate(self._answers)
                             if not quiz.is_correct(a["verdict"])]

        if self._drill and not missed:
            title = tr("Missed words cleared!")
        elif total and not missed:
            title = tr("Perfect run")
        else:
            title = tr("Quiz complete")
        self.complete_title.setText(title)
        self.ring_score.setText(f"{correct}/{total}")
        self.ring.set_score(correct / total if total else 0.0)
        self.tally_correct[0].setText(str(correct))
        self.tally_missed[0].setText(str(missed))

        rows = [f"{q.record.get('Word1') or ''} → {q.record.get('Word2') or ''}"
                for i, q in enumerate(self._questions)
                if i < len(self._answers)
                and not quiz.is_correct(self._answers[i]["verdict"])]
        self.missed_list.setText("\n".join(rows))
        self.missed_panel.setVisible(bool(rows))
        self.practice_btn.setText(
            tr("Practice missed") + f"  ·  {len(self._missed_deck)}")
        self.practice_btn.setVisible(bool(self._missed_deck))
        self._stack.setCurrentIndex(self.STATE_COMPLETE)

    def _practice_missed_clicked(self):
        """Re-ask just the words missed, as a fresh quiz over the same options.

        Grading still goes through SM-2, so a word recalled on the second pass
        earns its longer interval instead of staying stuck at one day.
        """
        records = list(self._missed_deck)
        if not records:
            self._show_picker()
            return
        self._build_and_start(records, drill=True)

    def _again_clicked(self):
        records = self._fetch_deck(self._deck_kind(), self.size_spin.value())
        if self.shuffle_btn.isChecked():
            random.shuffle(records)
        self._build_and_start(records)

    def _show_picker(self):
        self._advance_timer.stop()
        self._stall_timer.stop()
        self.drain_bar.stop()
        self._cancel_speech()
        self._clear_options()
        self._questions = []
        self._answers = []
        self._index = 0
        self._drill = False
        self._stack.setCurrentIndex(self.STATE_PICKER)
        self._refresh_picker_chips()
        self._refresh_picker_info()

    # ---------------------------------------------------------------- input

    def keyPressEvent(self, event):  # noqa: N802
        """Answer and advance from the keyboard.

        Handled here rather than through QShortcut on purpose: a shortcut fires
        for the whole widget subtree regardless of focus, so it would swallow
        the spaces and digits of a typed answer. Key events reach the page only
        once the focused widget has declined them, which is exactly the rule.
        """
        if self._stack.currentIndex() != self.STATE_SESSION:
            super().keyPressEvent(event)
            return
        key = event.key()
        if key == Qt.Key_Escape:
            self._show_picker()
            return
        if not self._revealed and self._option_rows:
            if Qt.Key_1 <= key <= Qt.Key_9:
                index = key - Qt.Key_1
                if index < len(self._option_rows):
                    self._answer_choice(index)
                    return
        if key in (Qt.Key_Space, Qt.Key_Return, Qt.Key_Enter) and self._revealed:
            self._next_question()
            return
        super().keyPressEvent(event)

    def hideEvent(self, event):  # noqa: N802 — leaving the page silences it
        self._advance_timer.stop()
        self._stall_timer.stop()
        self.drain_bar.stop()
        self._cancel_speech()
        super().hideEvent(event)
