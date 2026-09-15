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

"""Add Word dialog — compact two-row capture with DeepL translation,
language detect and inline TTS preview. New words are saved as 'New'.

A definition can ride along: a folded panel to type one, or to have the AI
write it after the save (see :mod:`app.core.definition_autogen`)."""
import logging

from PySide6.QtCore import QPointF, QRectF, QSize, Qt, QTimer, Signal
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget,
)

from app.config import load_settings, save_settings
from app.core import ai, definition_autogen
from app.core.audio import is_language_supported, speak_word
from app.core.backup_management import backup_database
from app.core.database_adapter import DatabaseAdapter
from app.core.errors import DuplicateWordError
from app.core.languages import TRANSLATION_CODES
from app.core.translator import translate
from app.i18n import fill_lang_combo, get_lang, lang_label, set_lang, tr
from app.ui import icons
from app.ui.dialogs.base import FramelessDialog
from app.ui.dialogs.definition import build_for_in_row, remember_side, remembered_sides
from app.ui.widgets import ContentComboBox, ElidedLabel
from app.ui.workers import run_in_thread


class _DotButton(QPushButton):
    """An icon button that can wear a small accent dot on its glyph's corner."""

    def __init__(self, dot_color):
        super().__init__(objectName="iconButton")
        self._dot = False
        self._dot_color = QColor(dot_color)

    def set_dot(self, on):
        if on != self._dot:
            self._dot = on
            self.update()

    def has_dot(self):
        return self._dot

    def paintEvent(self, event):  # noqa: N802
        super().paintEvent(event)
        if not self._dot:
            return
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        p.setBrush(self._dot_color)
        p.drawEllipse(QPointF(self.width() / 2 + 7, self.height() / 2 - 7), 3.5, 3.5)
        p.end()


class _Switch(QCheckBox):
    """A compact pill switch, painted instead of the square checkbox indicator."""

    def __init__(self, colors):
        super().__init__()
        self._colors = colors
        self.setFixedSize(30, 18)
        self.setCursor(Qt.PointingHandCursor)

    def hitButton(self, pos):  # noqa: N802
        return self.rect().contains(pos)

    def paintEvent(self, event):  # noqa: N802
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        on, enabled = self.isChecked(), self.isEnabled()
        track = QColor(self._colors["accent"] if on else self._colors["border"])
        knob = QColor("#ffffff")
        if not enabled:
            track.setAlphaF(0.45)
            knob.setAlphaF(0.7)
        rect = QRectF(0.5, 1.5, 29, 15)
        p.setBrush(track)
        p.drawRoundedRect(rect, 7.5, 7.5)
        p.setBrush(knob)
        x = rect.right() - 13.5 if on else rect.left() + 1.5
        p.drawEllipse(QRectF(x, rect.top() + 1.5, 12, 12))
        p.end()


class _DefinitionEdit(QPlainTextEdit):
    """Plain-text definition box where Ctrl+Enter saves and Enter is a new line."""
    submit = Signal()

    def keyPressEvent(self, event):  # noqa: N802
        if event.key() in (Qt.Key_Return, Qt.Key_Enter) and event.modifiers() & Qt.ControlModifier:
            self.submit.emit()
            return
        super().keyPressEvent(event)


class AddWordDialog(FramelessDialog):
    word_saved = Signal()
    # Emitted (with the existing word's ID) when the user chooses to open an
    # already-existing entry instead of adding a duplicate.
    open_existing = Signal(str)
    # The saved row, when the AI should define it once the dialog has closed;
    # the dialog is deleted on close, so its owner runs the request.
    definition_requested = Signal(dict, str, str)
    # A setting was written; the main window writes its whole settings dict
    # back elsewhere, so it has to re-read these keys or undo the change.
    settings_saved = Signal()

    def __init__(self, parent, prefill=None, auto_translate=False, language1=None,
                 language2=None):
        super().__init__(parent, title=tr("Add Word"))
        self.setMinimumWidth(540)
        self.setAttribute(Qt.WA_DeleteOnClose)
        # Set while the dialog writes a combo itself, so those writes don't
        # come back through the auto-translate handler (see _set_lang).
        self._suppress_lang_signal = False

        settings = load_settings()
        # Cloud writes follow the backend identity (account *or* personal server),
        # so a new word is pushed as it's saved instead of queued for later.
        from app.core.auth_manager import cloud_backend_active
        self.db_adapter = DatabaseAdapter(use_cloud=cloud_backend_active())
        colors = self.colors

        languages = sorted(TRANSLATION_CODES)
        layout = self.content_layout
        layout.setContentsMargins(16, 14, 16, 12)
        layout.setSpacing(10)

        grid = QGridLayout()
        grid.setHorizontalSpacing(8)
        grid.setVerticalSpacing(8)

        self.lang1_combo = QComboBox()
        fill_lang_combo(self.lang1_combo, languages, head=["Detect language"])
        set_lang(self.lang1_combo, language1 if language1 in languages else "English")
        self.lang1_combo.setFixedWidth(150)
        self.lang1_combo.setCursor(Qt.PointingHandCursor)
        grid.addWidget(self.lang1_combo, 0, 0)

        self.word1_edit = QLineEdit()
        self.word1_edit.setPlaceholderText(tr("Type a word or phrase…"))
        self.word1_edit.setClearButtonEnabled(True)
        speak1 = self.word1_edit.addAction(
            icons.icon("volume", colors["text_dim"], 16), QLineEdit.TrailingPosition)
        self.speak1_action = speak1
        speak1.triggered.connect(lambda: self._speak(self.word1_edit.text(),
                                                     get_lang(self.lang1_combo)))
        grid.addWidget(self.word1_edit, 0, 1)

        self.swap_btn = QPushButton(objectName="iconButton")
        self.swap_btn.setIcon(icons.icon("swap", colors["text_dim"], 17))
        self.swap_btn.setIconSize(QSize(17, 17))
        self.swap_btn.setToolTip(tr("Swap word and translation"))
        self.swap_btn.setCursor(Qt.PointingHandCursor)
        self.swap_btn.clicked.connect(self.swap_entries)
        grid.addWidget(self.swap_btn, 0, 2, 2, 1, Qt.AlignVCenter)

        self.lang2_combo = QComboBox()
        fill_lang_combo(self.lang2_combo, languages)
        last_target = language2 or settings.get("addword_target_language") or "German"
        set_lang(self.lang2_combo, last_target if last_target in languages else "German")
        self.lang2_combo.setFixedWidth(150)
        self.lang2_combo.setCursor(Qt.PointingHandCursor)
        grid.addWidget(self.lang2_combo, 1, 0)

        self.word2_edit = QLineEdit()
        self.word2_edit.setPlaceholderText(tr("Translation…"))
        self.word2_edit.setClearButtonEnabled(True)
        speak2 = self.word2_edit.addAction(
            icons.icon("volume", colors["text_dim"], 16), QLineEdit.TrailingPosition)
        self.speak2_action = speak2
        speak2.triggered.connect(lambda: self._speak(self.word2_edit.text(),
                                                     get_lang(self.lang2_combo)))
        grid.addWidget(self.word2_edit, 1, 1)

        grid.setColumnStretch(1, 1)
        layout.addLayout(grid)

        self.info_label = QLabel("")
        self.info_label.setObjectName("dimLabel")
        self.info_label.setWordWrap(True)
        self.info_label.hide()
        layout.addWidget(self.info_label)

        layout.addWidget(self._build_definition_panel(settings))

        buttons = QHBoxLayout()
        self.translate_btn = QPushButton(f"  {tr('Translate')}")
        self.translate_btn.setIcon(icons.icon("globe", colors["text"], 15))
        self.translate_btn.setToolTip(tr("Translate with DeepL (Enter)"))
        self.translate_btn.setCursor(Qt.PointingHandCursor)
        self.translate_btn.clicked.connect(self.do_translate)
        buttons.addWidget(self.translate_btn)
        self.ai_btn = QPushButton(objectName="iconButton")
        self.ai_btn.setIcon(icons.icon("sparkles", colors["text_dim"], 16))
        self.ai_btn.setIconSize(QSize(16, 16))
        self.ai_btn.setToolTip(tr("Fill with AI (lemma + best translation)"))
        self.ai_btn.setCursor(Qt.PointingHandCursor)
        self.ai_btn.clicked.connect(self.do_ai_fill)
        buttons.addWidget(self.ai_btn)
        self.definition_btn = _DotButton(colors["accent"])
        self.definition_btn.setIconSize(QSize(16, 16))
        self.definition_btn.setToolTip(tr("Add definition"))
        self.definition_btn.setCursor(Qt.PointingHandCursor)
        self.definition_btn.clicked.connect(self.toggle_definition_panel)
        buttons.addWidget(self.definition_btn)
        buttons.addStretch(1)
        cancel = QPushButton(tr("Cancel"))
        cancel.setCursor(Qt.PointingHandCursor)
        cancel.clicked.connect(self.reject)
        buttons.addWidget(cancel)
        save = QPushButton(tr("Save Word"), objectName="primaryButton")
        save.setCursor(Qt.PointingHandCursor)
        save.clicked.connect(self.save_word)
        save.setDefault(True)
        buttons.addWidget(save)
        layout.addLayout(buttons)

        self.word1_edit.returnPressed.connect(self.do_translate)
        self.word2_edit.returnPressed.connect(self.save_word)
        self.word1_edit.setFocus()

        # Picking a language re-translates on the spot — connected last so the
        # combo defaults set up above don't fire it.
        self.lang1_combo.currentIndexChanged.connect(self._on_language_changed)
        self.lang2_combo.currentIndexChanged.connect(self._on_language_changed)
        # Separate from _on_language_changed, which bails out when there's
        # nothing to re-translate — the button state has to follow regardless.
        self.lang1_combo.currentIndexChanged.connect(self._sync_speak_actions)
        self.lang2_combo.currentIndexChanged.connect(self._sync_speak_actions)
        self._sync_speak_actions()
        self.lang1_combo.currentIndexChanged.connect(self._fill_definition_languages)
        self.lang2_combo.currentIndexChanged.connect(self._fill_definition_languages)
        self._sync_definition_button()

        if prefill:
            self.apply_prefill(prefill, language1=language1, auto_translate=auto_translate)

    def apply_prefill(self, text, language1=None, auto_translate=False):
        """Fill the word field from text (e.g. the clipboard) and optionally
        translate. Exposed so callers can populate the dialog AFTER it is shown —
        needed on Wayland, where the clipboard is only readable once the dialog has
        focus, so the hotkey flow fills it in post-show rather than at launch."""
        if not text:
            return
        self.word1_edit.setText(text)
        if language1 and self.lang1_combo.findData(language1) >= 0:
            self._set_lang(self.lang1_combo, language1)
        else:
            self._set_lang(self.lang1_combo, "Detect language")
        if len(text.split()) >= 100:
            self._info(tr("The text was truncated to the first 100 words."))
        if auto_translate:
            self.do_translate()

    # ------------------------------------------------------------ definition

    def _build_definition_panel(self, settings):
        """The folded definition box, its "Generate on save" switch and the
        "for <word> in <language>" choice both of them use."""
        self.definition_panel = QWidget()
        column = QVBoxLayout(self.definition_panel)
        column.setContentsMargins(0, 0, 0, 0)
        column.setSpacing(8)

        self.definition_edit = _DefinitionEdit()
        self.definition_edit.setPlaceholderText(tr("Add a definition…"))
        self.definition_edit.setTabChangesFocus(True)
        self.definition_edit.setFixedHeight(self.definition_edit.fontMetrics().lineSpacing() * 4 + 16)
        self.definition_edit.submit.connect(self.save_word)
        self.definition_edit.textChanged.connect(self._sync_definition_button)
        column.addWidget(self.definition_edit)

        row = QHBoxLayout()
        row.setSpacing(8)
        self.autogen_switch = _Switch(self.colors)
        # the one part of the row that may give way when a translation runs long
        self.autogen_label = ElidedLabel(min_width=60)
        self.autogen_label.set_full_text(tr("Generate on save"))
        self.autogen_label.setCursor(Qt.PointingHandCursor)
        self.autogen_label.mousePressEvent = lambda _e: (
            self.autogen_switch.isEnabled() and self.autogen_switch.toggle())
        if definition_autogen.disable_if_unavailable(settings):
            save_settings(settings)
        has_key = ai.has_api_key()
        self.autogen_switch.setChecked(definition_autogen.enabled(settings))
        for widget in (self.autogen_switch, self.autogen_label):
            widget.setEnabled(has_key)
            if not has_key:
                widget.setToolTip(tr("Set up an AI key in Settings → Translation & AI to use this"))
        self.autogen_switch.toggled.connect(self._on_autogen_toggled)
        row.addWidget(self.autogen_switch)
        row.addWidget(self.autogen_label, 1)
        row.addSpacing(10)

        word_side, language_side = remembered_sides()
        self._definition_language_side = language_side
        self.def_word_combo = ContentComboBox()
        self.def_word_combo.addItem(tr("Word"), "Word1")
        self.def_word_combo.addItem(tr("Translation"), "Word2")
        self.def_word_combo.setCurrentIndex(max(self.def_word_combo.findData(word_side), 0))
        self.def_language_combo = ContentComboBox()
        for combo in (self.def_word_combo, self.def_language_combo):
            combo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            combo.setCursor(Qt.PointingHandCursor)
        self.def_word_combo.currentIndexChanged.connect(self._on_definition_word_changed)
        self.def_language_combo.currentIndexChanged.connect(self._on_definition_language_changed)
        row.addWidget(build_for_in_row(self.def_word_combo, self.def_language_combo))
        column.addLayout(row)

        self._definition_open = False
        self.definition_panel.hide()
        return self.definition_panel

    def _fill_definition_languages(self, *_args):
        """Both languages of the entry, or just one when the pair shares it."""
        lang1, lang2 = get_lang(self.lang1_combo), get_lang(self.lang2_combo)
        combo = self.def_language_combo
        combo.blockSignals(True)
        combo.clear()
        if lang1 == lang2:
            own = "Language2" if self.def_word_combo.currentData() == "Word2" else "Language1"
            combo.addItem(lang_label(lang1), own)
        else:
            combo.addItem(lang_label(lang1), "Language1")
            combo.addItem(lang_label(lang2), "Language2")
        combo.setCurrentIndex(max(combo.findData(self._definition_language_side), 0))
        combo.blockSignals(False)

    def _on_definition_word_changed(self, _index):
        self._remember("definition_ai_word", self.def_word_combo.currentData())
        self._fill_definition_languages()

    def _on_definition_language_changed(self, _index):
        self._definition_language_side = self.def_language_combo.currentData()
        self._remember("definition_ai_language", self._definition_language_side)

    def _remember(self, key, value):
        remember_side(key, value)
        self.settings_saved.emit()

    def _on_autogen_toggled(self, on):
        settings = load_settings()
        definition_autogen.set_enabled(settings, on)
        save_settings(settings)
        self.settings_saved.emit()
        self._sync_definition_button()

    def _sync_definition_button(self):
        typed = bool(self.definition_edit.toPlainText().strip())
        color = self.colors["accent"] if typed else self.colors["text_dim"]
        self.definition_btn.setIcon(icons.icon("file-text", color, 16))
        self.definition_btn.set_dot(self.autogen_switch.isChecked())

    def is_definition_panel_open(self):
        return self._definition_open

    def toggle_definition_panel(self):
        self._definition_open = not self._definition_open
        if not self.def_language_combo.count():
            self._fill_definition_languages()
        self.definition_panel.setVisible(self._definition_open)
        if self._definition_open:
            self.definition_edit.setFocus()
        else:
            self.word1_edit.setFocus()
        self._fit_height()
        # a layout keeps a just-hidden child's size until the hide event is
        # processed, so refit once more on the next event-loop turn
        QTimer.singleShot(0, self._fit_height)

    def _fit_height(self):
        self.layout().activate()
        self.resize(self.width(), self.sizeHint().height())

    # ------------------------------------------------------------------

    def _info(self, message):
        self.info_label.setText(message)
        self.info_label.setVisible(bool(message))

    def _set_lang(self, combo, language):
        """set_lang() that doesn't wake the auto-translate handler — the dialog
        adjusts the combos itself (detected source, target fallback, swap) and
        those writes must not translate on top of what it just produced."""
        previous = self._suppress_lang_signal
        self._suppress_lang_signal = True
        try:
            set_lang(combo, language)
        finally:
            self._suppress_lang_signal = previous

    def _on_language_changed(self):
        if self._suppress_lang_signal or not self.word1_edit.text().strip():
            return
        self.do_translate()

    @staticmethod
    def _fallback_target(source):
        """Target to use when the source language is also the chosen target."""
        return 'German' if source == 'English' else 'English'

    def _sync_speak_actions(self):
        """Grey out a pronounce button when its language has no voice.

        Plenty of languages the app can translate have no text-to-speech voice
        (Slovenian, Persian, Georgian, …), so the button would only ever raise.
        Showing it disabled says why, rather than failing after the click.
        """
        for action, combo in ((self.speak1_action, self.lang1_combo),
                              (self.speak2_action, self.lang2_combo)):
            language = get_lang(combo)
            if language == "Detect language":
                language = "English"
            speakable = is_language_supported(language)
            action.setEnabled(speakable)
            action.setToolTip(
                tr("Pronounce") if speakable
                else tr("Unsupported language: {language}").format(
                    language=lang_label(language)))

    def _speak(self, word, language):
        if not word.strip():
            return
        if language == "Detect language":
            language = "English"
        run_in_thread(speak_word, word, language, on_error=self._info)

    def swap_entries(self):
        w1, w2 = self.word1_edit.text(), self.word2_edit.text()
        l1 = get_lang(self.lang1_combo)
        l2 = get_lang(self.lang2_combo)
        self.word1_edit.setText(w2)
        self.word2_edit.setText(w1)
        if l1 != "Detect language":
            self._set_lang(self.lang1_combo, l2)
            self._set_lang(self.lang2_combo, l1)

    def do_translate(self):
        word = self.word1_edit.text().strip()
        if not word:
            self._info(tr("Enter a word to translate."))
            return
        source = get_lang(self.lang1_combo)
        target = get_lang(self.lang2_combo)
        self.translate_btn.setEnabled(False)
        self._info(tr("Translating…"))

        def work():
            translation, detected = translate(word, target, source)
            # Same-language guard: switch target like the original app
            effective_source = detected or (None if source == "Detect language" else source)
            if effective_source == target:
                new_target = self._fallback_target(effective_source)
                translation, _ = translate(word, new_target, effective_source)
                return translation, effective_source, new_target
            return translation, effective_source, target

        def done(result):
            translation, detected_source, target_used = result
            self.word2_edit.setText(translation)
            if detected_source and get_lang(self.lang1_combo) == "Detect language":
                self._set_lang(self.lang1_combo, detected_source)
            if target_used != get_lang(self.lang2_combo):
                self._set_lang(self.lang2_combo, target_used)
                self._info(tr("Source equals target — translated to {lang} instead.").format(lang=lang_label(target_used)))
            else:
                self._info("")

        run_in_thread(work, on_result=done, on_error=self._info,
                      on_finished=lambda: self.translate_btn.setEnabled(True))

    def do_ai_fill(self):
        """Rewrite the entry in its dictionary (lemma) form with a translation
        picked for that form — the same capture the reader's word popup makes,
        except here the fields are filled and the user still presses Save."""
        word = self.word1_edit.text().strip()
        if not word:
            self._info(tr("Enter a word to fill with AI."))
            return
        source = get_lang(self.lang1_combo)
        target = get_lang(self.lang2_combo)
        self.ai_btn.setEnabled(False)
        self.translate_btn.setEnabled(False)
        self._info(tr("Thinking…"))

        def work():
            effective_source = source
            if effective_source == "Detect language":
                # lemma_translate needs a named source language, so borrow the
                # translator's detector rather than making the model guess.
                _, detected = translate(word, target, None)
                effective_source = detected or "English"
            target_used = target
            if effective_source == target_used:
                target_used = self._fallback_target(effective_source)
            lemma, translation = ai.lemma_translate(word, "", effective_source, target_used)
            return lemma, translation, effective_source, target_used

        def done(result):
            lemma, translation, detected_source, target_used = result
            self.word1_edit.setText(lemma)
            self.word2_edit.setText(translation)
            if get_lang(self.lang1_combo) == "Detect language":
                self._set_lang(self.lang1_combo, detected_source)
            if target_used != get_lang(self.lang2_combo):
                self._set_lang(self.lang2_combo, target_used)
                self._info(tr("Source equals target — translated to {lang} instead.").format(lang=lang_label(target_used)))
            else:
                self._info("")

        def finished():
            self.ai_btn.setEnabled(True)
            self.translate_btn.setEnabled(True)

        run_in_thread(work, on_result=done, on_error=self._info, on_finished=finished)

    def save_word(self):
        word1 = self.word1_edit.text().strip()
        word2 = self.word2_edit.text().strip()
        lang1 = get_lang(self.lang1_combo)
        lang2 = get_lang(self.lang2_combo)

        if not word1 or not word2:
            self._info(tr("Both word and translation are required."))
            return
        if lang1 == "Detect language":
            self._info(tr("Please select the source language before saving."))
            return

        if not self.def_language_combo.count():
            self._fill_definition_languages()
        definition = self.definition_edit.toPlainText().strip()
        word_side = self.def_word_combo.currentData()
        language_side = self.def_language_combo.currentData()
        payload = {
            'Language1': lang1, 'Word1': word1,
            'Language2': lang2, 'Word2': word2,
            'Status': 'New', 'Source': 'manual',
        }
        if definition:
            payload[ai.definition_column(language_side)] = definition

        try:
            row = self.db_adapter.insert_word(payload)
            backup_database()
            # Remember the translation language for the next time the dialog opens.
            settings = load_settings()
            settings["addword_target_language"] = lang2
            generate = (not definition and row and self.autogen_switch.isChecked()
                        and not definition_autogen.disable_if_unavailable(settings))
            save_settings(settings)
            self.settings_saved.emit()
            self.word_saved.emit()
            if generate:
                self.definition_requested.emit(dict(row), word_side, language_side)
            self.accept()
        except DuplicateWordError as exc:
            self._handle_duplicate(exc)
        except Exception as exc:
            logging.error(f"Error saving new word: {exc}")
            QMessageBox.critical(self, tr("Error"), tr("Failed to save word:\n{error}").format(error=exc))

    def _handle_duplicate(self, exc: DuplicateWordError):
        """A word with this spelling already exists — offer to open it."""
        pair = f"{exc.word1} – {exc.word2}"
        box = QMessageBox(self)
        box.setIcon(QMessageBox.Information)
        box.setWindowTitle(tr("Already in your dictionary"))
        box.setText(tr("'{word}' is already in your dictionary.").format(word=pair))
        if exc.existing_id:
            open_btn = box.addButton(tr("Show existing"), QMessageBox.AcceptRole)
            box.addButton(tr("Cancel"), QMessageBox.RejectRole)
            box.exec()
            if box.clickedButton() is open_btn:
                self.open_existing.emit(exc.existing_id)
                self.accept()
        else:
            box.addButton(tr("OK"), QMessageBox.AcceptRole)
            box.exec()
