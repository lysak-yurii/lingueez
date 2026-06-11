"""Add Word dialog — compact two-row capture with DeepL translation,
language detect and inline TTS preview. New words are saved as 'New'."""
import logging

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtWidgets import (
    QComboBox, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox,
    QPushButton,
)

from app.config import get_bool, load_settings
from app.core.audio import speak_word
from app.core.backup_management import backup_database
from app.core.database_adapter import DatabaseAdapter
from app.core.translator import DEEPL_LANGUAGE_CODES, translate
from app.ui import icons
from app.ui.dialogs.base import FramelessDialog
from app.ui.workers import run_in_thread


class AddWordDialog(FramelessDialog):
    word_saved = Signal()

    def __init__(self, parent, prefill=None, auto_translate=False):
        super().__init__(parent, title="Add Word")
        self.setMinimumWidth(540)
        self.setAttribute(Qt.WA_DeleteOnClose)

        settings = load_settings()
        enable_sync = get_bool(settings, "enable_sync", False)
        self.db_adapter = DatabaseAdapter(use_cloud=enable_sync)
        colors = self.colors

        languages = sorted(DEEPL_LANGUAGE_CODES.keys())
        layout = self.content_layout
        layout.setContentsMargins(16, 14, 16, 12)
        layout.setSpacing(10)

        grid = QGridLayout()
        grid.setHorizontalSpacing(8)
        grid.setVerticalSpacing(8)

        self.lang1_combo = QComboBox()
        self.lang1_combo.addItems(["Detect language"] + languages)
        self.lang1_combo.setCurrentText("English")
        self.lang1_combo.setFixedWidth(150)
        self.lang1_combo.setCursor(Qt.PointingHandCursor)
        grid.addWidget(self.lang1_combo, 0, 0)

        self.word1_edit = QLineEdit()
        self.word1_edit.setPlaceholderText("Type a word or phrase…")
        self.word1_edit.setClearButtonEnabled(True)
        speak1 = self.word1_edit.addAction(
            icons.icon("volume", colors["text_dim"], 16), QLineEdit.TrailingPosition)
        speak1.setToolTip("Pronounce")
        speak1.triggered.connect(lambda: self._speak(self.word1_edit.text(),
                                                     self.lang1_combo.currentText()))
        grid.addWidget(self.word1_edit, 0, 1)

        self.swap_btn = QPushButton(objectName="iconButton")
        self.swap_btn.setIcon(icons.icon("swap", colors["text_dim"], 17))
        self.swap_btn.setIconSize(QSize(17, 17))
        self.swap_btn.setToolTip("Swap word and translation")
        self.swap_btn.setCursor(Qt.PointingHandCursor)
        self.swap_btn.clicked.connect(self.swap_entries)
        grid.addWidget(self.swap_btn, 0, 2, 2, 1, Qt.AlignVCenter)

        self.lang2_combo = QComboBox()
        self.lang2_combo.addItems(languages)
        self.lang2_combo.setCurrentText("German")
        self.lang2_combo.setFixedWidth(150)
        self.lang2_combo.setCursor(Qt.PointingHandCursor)
        grid.addWidget(self.lang2_combo, 1, 0)

        self.word2_edit = QLineEdit()
        self.word2_edit.setPlaceholderText("Translation…")
        self.word2_edit.setClearButtonEnabled(True)
        speak2 = self.word2_edit.addAction(
            icons.icon("volume", colors["text_dim"], 16), QLineEdit.TrailingPosition)
        speak2.setToolTip("Pronounce")
        speak2.triggered.connect(lambda: self._speak(self.word2_edit.text(),
                                                     self.lang2_combo.currentText()))
        grid.addWidget(self.word2_edit, 1, 1)

        grid.setColumnStretch(1, 1)
        layout.addLayout(grid)

        self.info_label = QLabel("")
        self.info_label.setObjectName("dimLabel")
        self.info_label.setWordWrap(True)
        self.info_label.hide()
        layout.addWidget(self.info_label)

        buttons = QHBoxLayout()
        self.translate_btn = QPushButton("  Translate")
        self.translate_btn.setIcon(icons.icon("globe", colors["text"], 15))
        self.translate_btn.setToolTip("Translate with DeepL (Enter)")
        self.translate_btn.setCursor(Qt.PointingHandCursor)
        self.translate_btn.clicked.connect(self.do_translate)
        buttons.addWidget(self.translate_btn)
        buttons.addStretch(1)
        cancel = QPushButton("Cancel")
        cancel.setCursor(Qt.PointingHandCursor)
        cancel.clicked.connect(self.reject)
        buttons.addWidget(cancel)
        save = QPushButton("Save Word", objectName="primaryButton")
        save.setCursor(Qt.PointingHandCursor)
        save.clicked.connect(self.save_word)
        save.setDefault(True)
        buttons.addWidget(save)
        layout.addLayout(buttons)

        self.word1_edit.returnPressed.connect(self.do_translate)
        self.word2_edit.returnPressed.connect(self.save_word)
        self.word1_edit.setFocus()

        if prefill:
            self.word1_edit.setText(prefill)
            self.lang1_combo.setCurrentText("Detect language")
            if len(prefill.split()) >= 100:
                self._info("The text was truncated to the first 100 words.")
        if auto_translate and prefill:
            self.do_translate()

    # ------------------------------------------------------------------

    def _info(self, message):
        self.info_label.setText(message)
        self.info_label.setVisible(bool(message))

    def _speak(self, word, language):
        if not word.strip():
            return
        if language == "Detect language":
            language = "English"
        run_in_thread(speak_word, word, language, on_error=self._info)

    def swap_entries(self):
        w1, w2 = self.word1_edit.text(), self.word2_edit.text()
        l1 = self.lang1_combo.currentText()
        l2 = self.lang2_combo.currentText()
        self.word1_edit.setText(w2)
        self.word2_edit.setText(w1)
        if l1 != "Detect language":
            self.lang1_combo.setCurrentText(l2)
            self.lang2_combo.setCurrentText(l1)

    def do_translate(self):
        word = self.word1_edit.text().strip()
        if not word:
            self._info("Enter a word to translate.")
            return
        source = self.lang1_combo.currentText()
        target = self.lang2_combo.currentText()
        self.translate_btn.setEnabled(False)
        self._info("Translating…")

        def work():
            translation, detected = translate(word, target, source)
            # Same-language guard: switch target like the original app
            effective_source = detected or (None if source == "Detect language" else source)
            if effective_source == target:
                new_target = 'German' if effective_source == 'English' else 'English'
                translation, _ = translate(word, new_target, effective_source)
                return translation, effective_source, new_target
            return translation, effective_source, target

        def done(result):
            translation, detected_source, target_used = result
            self.word2_edit.setText(translation)
            if detected_source and self.lang1_combo.currentText() == "Detect language":
                self.lang1_combo.setCurrentText(detected_source)
            if target_used != self.lang2_combo.currentText():
                self.lang2_combo.setCurrentText(target_used)
                self._info(f"Source equals target — translated to {target_used} instead.")
            else:
                self._info("")

        run_in_thread(work, on_result=done, on_error=self._info,
                      on_finished=lambda: self.translate_btn.setEnabled(True))

    def save_word(self):
        word1 = self.word1_edit.text().strip()
        word2 = self.word2_edit.text().strip()
        lang1 = self.lang1_combo.currentText()
        lang2 = self.lang2_combo.currentText()

        if not word1 or not word2:
            self._info("Both word and translation are required.")
            return
        if lang1 == "Detect language":
            self._info("Please select the source language before saving.")
            return

        try:
            result = self.db_adapter.insert_word({
                'Language1': lang1, 'Word1': word1,
                'Language2': lang2, 'Word2': word2,
                'Status': 'New', 'Source': 'manual',
            })
            if not result:
                self._info(f"'{word1} – {word2}' already exists in your dictionary.")
                return
            backup_database()
            self.word_saved.emit()
            self.accept()
        except Exception as exc:
            logging.error(f"Error saving new word: {exc}")
            QMessageBox.critical(self, "Error", f"Failed to save word:\n{exc}")
