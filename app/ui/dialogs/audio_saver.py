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

"""Save selected words as a single MP3 with progress and cancellation."""
import logging
import threading

from PySide6.QtWidgets import (
    QFileDialog, QHBoxLayout, QLabel, QMessageBox, QProgressBar, QPushButton,
)

from app.config import get_float, get_int, load_settings
from app.core.audio import save_audio_file
from app.i18n import tr
from app.ui.dialogs.base import FramelessDialog
from app.ui.workers import run_in_thread


class AudioSaverDialog(FramelessDialog):
    def __init__(self, parent, words, languages, initial_name):
        super().__init__(parent, title=tr("Save to Audio"))
        self.words = words
        self.languages = languages
        self.initial_name = initial_name
        self.cancel_event = threading.Event()
        self.temp_files = set()
        self._running = False

        self.setMinimumWidth(460)

        layout = self.content_layout
        layout.setContentsMargins(20, 20, 20, 16)
        layout.setSpacing(12)

        self.info_label = QLabel(
            tr("Generate one MP3 file from {count} word/translation pair(s).").format(count=len(words)))
        self.info_label.setWordWrap(True)
        layout.addWidget(self.info_label)

        self.progress = QProgressBar()
        self.progress.setRange(0, len(words) * 1)
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        self.status_label = QLabel("")
        self.status_label.setObjectName("dimLabel")
        layout.addWidget(self.status_label)

        buttons = QHBoxLayout()
        buttons.addStretch(1)
        self.cancel_btn = QPushButton(tr("Cancel"))
        self.cancel_btn.clicked.connect(self.cancel)
        buttons.addWidget(self.cancel_btn)
        self.start_btn = QPushButton(tr("Choose File && Start"), objectName="primaryButton")
        self.start_btn.clicked.connect(self.start)
        buttons.addWidget(self.start_btn)
        layout.addLayout(buttons)

    def start(self):
        path, _ = QFileDialog.getSaveFileName(self, tr("Save Audio As"),
                                              self.initial_name, tr("MP3 files (*.mp3)"))
        if not path:
            return
        settings = load_settings()
        pause_ms = int(get_float(settings, "pause_duration", 0.5) * 1000)
        repeats = get_int(settings, "number_of_repeats", 1)

        self.start_btn.setEnabled(False)
        self._running = True
        self.status_label.setText(tr("Generating audio…"))
        self.progress.setRange(0, len(self.words))

        def progress_callback(current, word):
            if current == 'compiling_audio':
                self.status_label.setText(tr("Compiling final audio file…"))
                self.progress.setRange(0, 0)  # indeterminate
            else:
                self.progress.setValue(int(current))
                self.status_label.setText(tr("Processed: {word}").format(word=word))

        def work(progress_callback=None):
            save_audio_file(
                self.words, path, self.languages,
                progress_callback=progress_callback,
                is_cancelled=self.cancel_event,
                all_temp_files=self.temp_files,
                logger=lambda message, level='info': logging.log(logging.INFO, message),
                pause_duration=pause_ms,
                number_of_repeats=repeats,
            )
            return path

        def done(result):
            self._running = False
            if self.cancel_event.is_set():
                self.status_label.setText(tr("Cancelled."))
                self.reject()
            else:
                self.progress.setRange(0, 1)
                self.progress.setValue(1)
                QMessageBox.information(self, tr("Audio saved"),
                                        tr("Audio file saved to:\n{path}").format(path=result))
                self.accept()

        def fail(message):
            self._running = False
            QMessageBox.critical(self, tr("Audio Error"),
                                 tr("Failed to save audio:\n{error}").format(error=message))
            self.reject()

        run_in_thread(work, wants_progress=True,
                      on_progress=lambda a, b: progress_callback(a, b),
                      on_result=done, on_error=fail)

    def cancel(self):
        if self._running:
            self.cancel_event.set()
            self.status_label.setText(tr("Cancelling…"))
        else:
            self.reject()
