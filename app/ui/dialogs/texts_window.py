"""Texts browser: list + reader view with paging, TTS, edit and delete."""
import logging

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QComboBox, QDialog, QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMessageBox, QPushButton, QSplitter, QTextEdit,
    QVBoxLayout, QWidget,
)

from app.core.audio import lang_codes, read_words_list, stop_playback
from app.core.backup_management import backup_database
from app.ui.workers import run_in_thread
from app.ui.dialogs.definition import markup_to_html


class TextsWindow(QDialog):
    reading_done = Signal()

    def __init__(self, parent, db_adapter):
        super().__init__(parent)
        self.reading_done.connect(self._tts_finished)
        self.db_adapter = db_adapter
        self.texts = []
        self.current_index = -1
        self.is_reading = False

        self.setWindowTitle("Texts")
        self.setMinimumSize(900, 560)
        self.setAttribute(Qt.WA_DeleteOnClose)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 12)

        splitter = QSplitter(Qt.Horizontal)

        # left: list of texts
        left = QWidget()
        left_lay = QVBoxLayout(left)
        left_lay.setContentsMargins(0, 0, 8, 0)
        self.listing = QListWidget()
        self.listing.currentRowChanged.connect(self.show_text)
        left_lay.addWidget(self.listing, 1)

        left_buttons = QHBoxLayout()
        delete_btn = QPushButton("Delete", objectName="dangerButton")
        delete_btn.clicked.connect(self.delete_current)
        left_buttons.addWidget(delete_btn)
        left_buttons.addStretch(1)
        left_lay.addLayout(left_buttons)
        splitter.addWidget(left)

        # right: reader
        right = QWidget()
        right_lay = QVBoxLayout(right)
        right_lay.setContentsMargins(8, 0, 0, 0)

        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Title")
        right_lay.addWidget(self.title_edit)

        meta_row = QHBoxLayout()
        self.language_combo = QComboBox()
        self.language_combo.setEditable(True)
        self.language_combo.addItems(sorted(lang_codes.keys()))
        meta_row.addWidget(QLabel("Language:"))
        meta_row.addWidget(self.language_combo)
        meta_row.addStretch(1)
        self.words_label = QLabel("")
        self.words_label.setObjectName("dimLabel")
        self.words_label.setWordWrap(True)
        meta_row.addWidget(self.words_label, 2)
        right_lay.addLayout(meta_row)

        self.body = QTextEdit()
        right_lay.addWidget(self.body, 1)

        controls = QHBoxLayout()
        self.prev_btn = QPushButton("← Previous")
        self.prev_btn.clicked.connect(lambda: self.select_relative(-1))
        controls.addWidget(self.prev_btn)
        self.page_label = QLabel("")
        controls.addWidget(self.page_label)
        self.next_btn = QPushButton("Next →")
        self.next_btn.clicked.connect(lambda: self.select_relative(1))
        controls.addWidget(self.next_btn)
        controls.addStretch(1)
        self.tts_btn = QPushButton(" Read Aloud")
        from app.ui import icons, theme
        self._colors = theme.current_colors()
        self.tts_btn.setIcon(icons.icon("volume", self._colors["text"]))
        self.tts_btn.clicked.connect(self.toggle_tts)
        controls.addWidget(self.tts_btn)
        save_btn = QPushButton("Save Changes", objectName="primaryButton")
        save_btn.clicked.connect(self.save_current)
        controls.addWidget(save_btn)
        right_lay.addLayout(controls)

        splitter.addWidget(right)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)
        layout.addWidget(splitter)

        self.load_texts()

    # ------------------------------------------------------------------

    def load_texts(self):
        try:
            self.texts = self.db_adapter.get_texts() or []
        except Exception as exc:
            logging.error(f"Failed to load texts: {exc}")
            self.texts = []
        self.texts.sort(key=lambda t: str(t.get('created_at') or ''), reverse=True)
        self.listing.clear()
        for text in self.texts:
            title = str(text.get('Title') or "(untitled)").strip()
            lang = str(text.get('Language') or "")
            item = QListWidgetItem(f"{title}\n{lang} · {str(text.get('created_at') or '')[:10]}")
            self.listing.addItem(item)
        if self.texts:
            self.listing.setCurrentRow(0)
        else:
            self.page_label.setText("No texts yet")

    def show_text(self, row):
        if row < 0 or row >= len(self.texts):
            self.current_index = -1
            return
        self.current_index = row
        text = self.texts[row]
        self.title_edit.setText(str(text.get('Title') or ""))
        self.language_combo.setCurrentText(str(text.get('Language') or "English"))
        self.words_label.setText(str(text.get('Words') or ""))
        self.body.setHtml(markup_to_html(str(text.get('Text') or "")))
        self.page_label.setText(f"{row + 1} / {len(self.texts)}")
        self.prev_btn.setEnabled(row > 0)
        self.next_btn.setEnabled(row < len(self.texts) - 1)

    def select_relative(self, delta):
        new_row = self.current_index + delta
        if 0 <= new_row < len(self.texts):
            self.listing.setCurrentRow(new_row)

    def save_current(self):
        if self.current_index < 0:
            return
        text = self.texts[self.current_index]
        data = {
            'Title': self.title_edit.text().strip(),
            'Language': self.language_combo.currentText().strip(),
            'Text': self.body.toPlainText().strip(),
        }
        try:
            self.db_adapter.update_text(int(text['ID']), data)
            backup_database()
            self.load_texts()
        except Exception as exc:
            logging.error(f"Failed to save text: {exc}")
            QMessageBox.critical(self, "Error", f"Failed to save text:\n{exc}")

    def delete_current(self):
        if self.current_index < 0:
            return
        text = self.texts[self.current_index]
        title = str(text.get('Title') or "(untitled)")
        if QMessageBox.question(self, "Delete Text", f"Delete '{title}'?",
                                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        try:
            self.db_adapter.delete_text(int(text['ID']))
            backup_database()
            self.load_texts()
        except Exception as exc:
            logging.error(f"Failed to delete text: {exc}")
            QMessageBox.critical(self, "Error", f"Failed to delete text:\n{exc}")

    # --------------------------------------------------------------- tts

    def toggle_tts(self):
        if self.is_reading:
            stop_playback()
            self._tts_finished()
            return
        if self.current_index < 0:
            return
        content = self.body.toPlainText().strip()
        language = self.language_combo.currentText()
        if not content or language not in lang_codes:
            return

        self.is_reading = True
        self.tts_btn.setText(" Stop")
        from app.ui import icons
        self.tts_btn.setIcon(icons.icon("stop", self._colors["danger"]))

        # Read the text in chunks (sentences grouped to ~400 chars)
        chunks, buf = [], ""
        for sentence in content.replace("\n", " ").split(". "):
            buf += sentence + ". "
            if len(buf) > 400:
                chunks.append(buf)
                buf = ""
        if buf.strip():
            chunks.append(buf)
        pairs = [(chunk, "") for chunk in chunks]
        langs = [(language, language)] * len(pairs)

        run_in_thread(read_words_list, pairs, langs, self.reading_done.emit)

    def _tts_finished(self):
        self.is_reading = False
        self.tts_btn.setText(" Read Aloud")
        from app.ui import icons
        self.tts_btn.setIcon(icons.icon("volume", self._colors["text"]))

    def closeEvent(self, event):
        if self.is_reading:
            stop_playback()
        super().closeEvent(event)
