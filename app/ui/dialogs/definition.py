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

"""Definition viewer/editor with AI generation.

Renders the stored '***' / '**' / '*' markup as rich text, supports
editing the raw definition, switching between Definition (Word1) and
Definition2 (Word2), and generating missing definitions via the
configured AI provider (ChatGPT or Gemini).
"""
import html
import logging
import re

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel, QMessageBox, QPushButton, QTextEdit,
    QVBoxLayout, QWidget,
)

from app.core import ai
from app.i18n import lang_label, tr
from app.ui import icons
from app.ui.dialogs.base import FramelessDialog
from app.ui.workers import run_in_thread


def _inline_markup(text):
    """Apply the inline ***bold*** / **bold** / *italic* markup to escaped text."""
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b>\1</b>', text, flags=re.S)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text, flags=re.S)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text, flags=re.S)
    return text


def markup_to_html(text):
    """Convert the stored ***heading*** / **bold** / *italic* markup into clean
    block HTML — one ``<h3>`` per heading line and one ``<p>`` per paragraph, so
    vertical spacing stays even instead of piling up stray ``<br>`` between
    blank lines."""
    if not text:
        return ""
    text = re.sub(r'\n{3,}', '\n\n', text.replace('\r\n', '\n').strip())
    out = []
    for block in re.split(r'\n{2,}', text):
        block = block.strip()
        if not block:
            continue
        heading = re.fullmatch(r'\*\*\*(.+?)\*\*\*', block, flags=re.S)
        if heading:
            out.append(f"<h3>{_inline_markup(html.escape(heading.group(1).strip()))}</h3>")
        else:
            body = _inline_markup(html.escape(block)).replace("\n", "<br>")
            out.append(f"<p>{body}</p>")
    return "".join(out)


class DefinitionDialog(FramelessDialog):
    definition_changed = Signal()

    def __init__(self, parent, record, db_adapter):
        super().__init__(parent, title=tr("Definition — {word}").format(word=record.get('Word1', '')))
        self.record = record
        self.db_adapter = db_adapter
        self.word_id = record["ID"]
        self.current_field = 'Word1'   # which word's definition is shown
        self._pick_initial_field = True  # on first load, open the side that has a definition
        self.editing = False
        self.ai_label = ai.provider_label()

        self.setMinimumSize(620, 480)
        self.setAttribute(Qt.WA_DeleteOnClose)

        layout = self.content_layout
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)

        # Header: the word being defined, led by a small book glyph.
        head = QHBoxLayout()
        head.setSpacing(10)
        glyph = QLabel()
        glyph.setPixmap(icons.icon("book-open", self.colors["text_dim"], 20).pixmap(QSize(20, 20)))
        head.addWidget(glyph, 0, Qt.AlignVCenter)
        self.header_label = QLabel(objectName="AppTitle")
        head.addWidget(self.header_label, 0, Qt.AlignVCenter)
        head.addStretch(1)
        layout.addLayout(head)

        # Segmented toggle: pick which side's definition to show — the word's or
        # its translation's. Replaces the old "Show … definition" text button.
        toggle = QHBoxLayout()
        toggle.setSpacing(6)
        self.lang_chips = []
        for field, lang_key in (('Word1', 'Language1'), ('Word2', 'Language2')):
            chip = QPushButton(lang_label(self.record.get(lang_key, '')), objectName="chipButton")
            chip.setCheckable(True)
            chip.setAutoExclusive(True)
            chip.setCursor(Qt.PointingHandCursor)
            chip.clicked.connect(lambda _checked, f=field: self._select_field(f))
            toggle.addWidget(chip)
            self.lang_chips.append((chip, field))
        toggle.addStretch(1)
        layout.addLayout(toggle)

        # Definition body inside a soft card: a rich-text view that doubles as the
        # raw-markup editor, with a centered empty state when nothing is stored.
        card = QFrame(objectName="DefinitionCard")
        card.setStyleSheet(
            f"#DefinitionCard{{background:{self.colors['surface']};"
            f" border:1px solid {self.colors['border']}; border-radius:10px;}}")
        card_lay = QVBoxLayout(card)
        card_lay.setContentsMargins(4, 4, 4, 4)
        card_lay.setSpacing(0)
        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.text.setStyleSheet("QTextEdit{background:transparent; border:none; padding:8px 10px;}")
        # Themed, tight block spacing for the rendered definition (accent
        # headings; modest paragraph gaps instead of blank-line pile-up).
        self.text.document().setDefaultStyleSheet(
            f"h3 {{ color:{self.colors['accent_text']}; margin-top:14px; margin-bottom:2px; }}"
            "p { margin-top:0px; margin-bottom:8px; }")
        card_lay.addWidget(self.text, 1)
        self.empty_widget = self._build_empty_state()
        card_lay.addWidget(self.empty_widget, 1)
        layout.addWidget(card, 1)

        # Footer: the AI action on the left; edit/save/cancel + close on the right.
        buttons = QHBoxLayout()
        buttons.setSpacing(8)
        self.generate_btn = QPushButton(tr("Generate with AI"), objectName="tonalButton")
        self.generate_btn.setIcon(icons.icon("sparkles", self.colors["accent_text"], 15))
        self.generate_btn.setIconSize(QSize(15, 15))
        self.generate_btn.setCursor(Qt.PointingHandCursor)
        self.generate_btn.clicked.connect(self.generate_definition)
        buttons.addWidget(self.generate_btn)
        buttons.addStretch(1)

        self.edit_btn = QPushButton(tr("Edit"))
        self.edit_btn.setIcon(icons.icon("edit", self.colors["text_dim"], 15))
        self.edit_btn.setIconSize(QSize(15, 15))
        self.edit_btn.setCursor(Qt.PointingHandCursor)
        self.edit_btn.clicked.connect(self.toggle_edit)
        buttons.addWidget(self.edit_btn)

        self.cancel_btn = QPushButton(tr("Cancel"))
        self.cancel_btn.setCursor(Qt.PointingHandCursor)
        self.cancel_btn.clicked.connect(self.cancel_edit)
        self.cancel_btn.hide()
        buttons.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(tr("Save"), objectName="primaryButton")
        self.save_btn.setIcon(icons.icon("check", "#ffffff", 15))
        self.save_btn.setIconSize(QSize(15, 15))
        self.save_btn.setCursor(Qt.PointingHandCursor)
        self.save_btn.clicked.connect(self.save_definition)
        self.save_btn.hide()
        buttons.addWidget(self.save_btn)

        self.close_btn = QPushButton(tr("Close"))
        self.close_btn.setCursor(Qt.PointingHandCursor)
        self.close_btn.clicked.connect(self.close)
        buttons.addWidget(self.close_btn)
        layout.addLayout(buttons)

        self.reload_word()

    def _build_empty_state(self):
        """Centered placeholder shown in the card when no definition is stored."""
        wrap = QWidget()
        col = QVBoxLayout(wrap)
        col.setContentsMargins(20, 20, 20, 20)
        col.setSpacing(8)
        col.addStretch(1)
        glyph = QLabel()
        glyph.setPixmap(icons.icon("file-text", self.colors["text_dim"], 34).pixmap(QSize(34, 34)))
        glyph.setAlignment(Qt.AlignCenter)
        col.addWidget(glyph)
        title = QLabel(tr("No definition yet"), objectName="EmptyTitle")
        title.setAlignment(Qt.AlignCenter)
        col.addWidget(title)
        self.empty_hint = QLabel(objectName="dimLabel")
        self.empty_hint.setAlignment(Qt.AlignCenter)
        self.empty_hint.setWordWrap(True)
        col.addWidget(self.empty_hint)
        col.addStretch(1)
        return wrap

    def _show_body(self, empty):
        """Swap between the editor/viewer and the empty placeholder. The editor
        always wins while editing, regardless of content."""
        show_empty = empty and not self.editing
        self.text.setVisible(not show_empty)
        self.empty_widget.setVisible(show_empty)

    # ------------------------------------------------------------------

    def reload_word(self):
        word = self.db_adapter.get_word(self.word_id) or self.record
        self.word = word
        if self._pick_initial_field:
            self._pick_initial_field = False
            has_def1 = bool(str(word.get('Definition') or "").strip())
            has_def2 = bool(str(word.get('Definition2') or "").strip())
            if not has_def1 and has_def2:
                self.current_field = 'Word2'
        self.refresh_view()

    def _definition_column(self):
        return 'Definition' if self.current_field == 'Word1' else 'Definition2'

    def _displayed_word(self):
        return self.word.get(self.current_field) or ""

    def refresh_view(self):
        definition = str(self.word.get(self._definition_column()) or "").strip()
        self.header_label.setText(str(self._displayed_word()))
        for chip, field in self.lang_chips:
            chip.setChecked(field == self.current_field)
        if definition:
            self.text.setHtml(markup_to_html(definition))
            self.generate_btn.setText(tr("Regenerate with AI"))
            self._show_body(empty=False)
        else:
            self.generate_btn.setText(tr("Generate with AI"))
            self.empty_hint.setText(tr("Generate one with AI, or write your own with Edit."))
            self._show_body(empty=True)

    def _select_field(self, field):
        if self.editing or field == self.current_field:
            return
        self.current_field = field
        self.refresh_view()

    # ------------------------------------------------------------ editing

    def toggle_edit(self):
        self.editing = True
        raw = self.word.get(self._definition_column()) or ""
        self.text.setReadOnly(False)
        self.text.setPlainText(str(raw))
        self._show_body(empty=False)
        self.edit_btn.hide()
        self.close_btn.hide()
        self.save_btn.show()
        self.cancel_btn.show()
        self.generate_btn.setEnabled(False)
        for chip, _field in self.lang_chips:
            chip.setEnabled(False)
        self.text.setFocus()

    def cancel_edit(self):
        self.editing = False
        self.text.setReadOnly(True)
        self.edit_btn.show()
        self.close_btn.show()
        self.save_btn.hide()
        self.cancel_btn.hide()
        self.generate_btn.setEnabled(True)
        for chip, _field in self.lang_chips:
            chip.setEnabled(True)
        self.refresh_view()

    def save_definition(self):
        new_text = self.text.toPlainText().strip()
        try:
            self.db_adapter.update_word(self.word_id, {self._definition_column(): new_text})
            self.definition_changed.emit()
        except Exception as exc:
            logging.error(f"Error saving definition: {exc}")
            QMessageBox.critical(self, tr("Error"), tr("Failed to save definition:\n{error}").format(error=exc))
            return
        self.cancel_edit()
        self.reload_word()

    # --------------------------------------------------------------- gpt

    def generate_definition(self):
        word = self._displayed_word()
        if not str(word).strip():
            QMessageBox.warning(self, tr("No word"), tr("There is no word to define."))
            return
        if not ai.has_api_key():
            QMessageBox.warning(self, tr("API key missing"),
                                tr("Set your {ai} API key in Settings → Translation & AI → AI first.").format(ai=self.ai_label))
            return
        lang1 = self.word.get('Language1') or "English"
        lang2 = self.word.get('Language2') or "English"
        if self.current_field == 'Word2':
            lang1, lang2 = lang2, lang1

        self.generate_btn.setEnabled(False)
        self._show_body(empty=False)
        self.text.setHtml(f"<p><i>{tr('Generating definition…')}</i></p>")

        field = self.current_field

        def work():
            return ai.update_definition_in_db(str(word), lang1, lang2, field, self.word_id)

        def done(result):
            ok, message = result
            if ok:
                self.definition_changed.emit()
                self.reload_word()
            else:
                self.refresh_view()
                QMessageBox.warning(self, self.ai_label, message)

        run_in_thread(work, on_result=done,
                      on_error=lambda e: (self.refresh_view(),
                                          QMessageBox.critical(self, self.ai_label, e)),
                      on_finished=lambda: self.generate_btn.setEnabled(True))
