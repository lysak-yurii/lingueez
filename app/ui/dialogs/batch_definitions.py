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

"""Generate AI definitions for many selected words in one run."""
import shiboken6
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QHBoxLayout, QLabel, QMessageBox, QProgressBar,
    QPushButton,
)

from app.core import ai
from app.i18n import lang_label, tr
from app.ui.dialogs.base import FramelessDialog
from app.ui.dialogs.definition import build_for_in_row, remember_side, remembered_sides
from app.ui.workers import run_in_thread


class BatchDefinitionsDialog(FramelessDialog):
    def __init__(self, parent, records, on_done):
        super().__init__(parent, title=tr("Generate Definitions"))
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setMinimumWidth(460)
        self.records = records
        self._on_done = on_done
        self._running = False
        self._cancelled = False

        layout = self.content_layout
        count = len(records)
        intro = QLabel(tr("Words selected: {n}").format(n=count))
        intro.setWordWrap(True)
        layout.addWidget(intro)

        word_side, language_side = remembered_sides()
        self.word_combo = QComboBox()
        self.word_combo.addItem(tr("Word"), "Word1")
        self.word_combo.addItem(tr("Translation"), "Word2")
        self.word_combo.setCurrentIndex(max(self.word_combo.findData(word_side), 0))
        self.language_combo = QComboBox()
        pairs = {(r.get("Language1"), r.get("Language2")) for r in records}
        if len(pairs) == 1:
            lang1, lang2 = next(iter(pairs))
            labels = (lang_label(lang1 or ""), lang_label(lang2 or ""))
        else:
            labels = (tr("the word's language"), tr("the translation's language"))
        for label, side in zip(labels, ai.LANGUAGE_SIDES, strict=True):
            self.language_combo.addItem(label, side)
        self.language_combo.setCurrentIndex(max(self.language_combo.findData(language_side), 0))
        self.word_combo.currentIndexChanged.connect(
            lambda _i: remember_side("definition_ai_word", self.word_combo.currentData()))
        self.language_combo.currentIndexChanged.connect(
            lambda _i: remember_side("definition_ai_language", self.language_combo.currentData()))
        row = QHBoxLayout()
        row.addWidget(build_for_in_row(self.word_combo, self.language_combo))
        row.addStretch(1)
        layout.addLayout(row)

        self.skip_check = QCheckBox(tr("Skip words that already have one"))
        self.skip_check.setChecked(True)
        layout.addWidget(self.skip_check)

        self.progress = QProgressBar()
        self.progress.setRange(0, max(count, 1))
        self.progress.setValue(0)
        self.progress.hide()
        layout.addWidget(self.progress)

        buttons = QHBoxLayout()
        buttons.addStretch(1)
        self.cancel_btn = QPushButton(tr("Cancel"))
        self.cancel_btn.setCursor(Qt.PointingHandCursor)
        self.cancel_btn.clicked.connect(self.reject)
        buttons.addWidget(self.cancel_btn)
        self.start_btn = QPushButton(tr("Generate"), objectName="primaryButton")
        self.start_btn.setCursor(Qt.PointingHandCursor)
        self.start_btn.setDefault(True)
        self.start_btn.clicked.connect(self.start)
        buttons.addWidget(self.start_btn)
        layout.addLayout(buttons)

    def start(self):
        if not ai.has_api_key():
            QMessageBox.warning(
                self, tr("API key missing"),
                tr("Set your {ai} API key in Settings → Translation & AI → AI first.")
                .format(ai=ai.provider_label()))
            return
        self._running = True
        for widget in (self.word_combo, self.language_combo, self.skip_check, self.start_btn):
            widget.setEnabled(False)
        self.progress.show()
        on_done = self._on_done

        def progress(done, total):
            if shiboken6.isValid(self):
                self.progress.setValue(done)

        def finished(stats):
            on_done(stats)
            if shiboken6.isValid(self):
                self._running = False
                self.accept()

        def failed(error):
            on_done(None)
            if shiboken6.isValid(self):
                self._running = False
                QMessageBox.critical(self, ai.provider_label(), error)
                self.reject()

        run_in_thread(ai.generate_definitions, self.records,
                      self.word_combo.currentData(), self.language_combo.currentData(),
                      skip_existing=self.skip_check.isChecked(),
                      is_cancelled=lambda: self._cancelled,
                      wants_progress=True, on_progress=progress,
                      on_result=finished, on_error=failed)

    def reject(self):
        # Stopping between words keeps what already landed; the dialog closes
        # once the worker reports back.
        if self._running:
            self._cancelled = True
            self.cancel_btn.setEnabled(False)
            self.cancel_btn.setText(tr("Stopping…"))
            return
        super().reject()
