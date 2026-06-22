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

"""Color-coded log viewer (used for imports and general app logging)."""
import logging
import os

from PySide6.QtCore import QObject, Qt, QUrl, Signal
from PySide6.QtGui import (
    QColor, QDesktopServices, QKeySequence, QShortcut, QTextCharFormat, QTextCursor,
)
from PySide6.QtWidgets import (
    QComboBox, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QMessageBox,
    QPushButton, QTextEdit,
)

from app.i18n import tr
from app.ui.dialogs.base import FramelessDialog

LEVEL_COLORS = {
    'info': None,
    'warning': "#d29922",
    'error': "#e5534b",
    'success': "#3fb950",
    'new': "#4f8cff",
    'rejected': "#e5534b",
}

# Severity rank for the level filter — keeps the categorical levels above
# orderable so the filter can show "this level and worse".
LEVEL_RANK = {
    'info': 0, 'success': 0, 'new': 0,
    'warning': 1,
    'error': 2, 'rejected': 2,
}

LOG_FILE = "app.log"
TAIL_BYTES = 256 * 1024  # read only the tail of a (possibly large) log file
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'  # keep in sync with main.py
MAX_RECORDS = 5000  # cap retained records so a long-lived window can't grow forever


def _level_key(levelno):
    if levelno >= logging.ERROR:
        return 'error'
    if levelno >= logging.WARNING:
        return 'warning'
    return 'info'


class _LogBridge(QObject):
    message = Signal(str, str)


class _LiveLogHandler(logging.Handler):
    """Forwards log records to the window across threads via a Qt signal."""

    def __init__(self):
        super().__init__()
        self.bridge = _LogBridge()
        self.setFormatter(logging.Formatter(LOG_FORMAT))
        # Mask secrets in the live stream too (the file handler is redacted
        # separately in main._setup_logging).
        from app.core.log_redaction import RedactionFilter
        self.addFilter(RedactionFilter())

    def emit(self, record):
        try:
            self.bridge.message.emit(self.format(record), _level_key(record.levelno))
        except Exception:
            pass


class LogWindow(FramelessDialog):
    def __init__(self, parent, title=None, follow_app_log=False):
        super().__init__(parent, title=title or tr("Activity Log"))
        self.setMinimumSize(700, 460)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(False)
        self._live_handler = None
        self._follow_app_log = follow_app_log
        self._records = []  # (message, level) — source of truth for re-filtering
        self._min_rank = 0  # current level-filter threshold

        layout = self.content_layout
        layout.setContentsMargins(14, 14, 14, 12)

        # --- Filter + find row ---
        tools = QHBoxLayout()
        tools.addWidget(QLabel(tr("Level:")))
        self.level_combo = QComboBox()
        for label, rank in ((tr("All"), 0), (tr("Warnings & errors"), 1),
                            (tr("Errors only"), 2)):
            self.level_combo.addItem(label, rank)
        self.level_combo.currentIndexChanged.connect(self._on_filter_changed)
        tools.addWidget(self.level_combo)
        tools.addStretch(1)
        self.find_edit = QLineEdit()
        self.find_edit.setPlaceholderText(tr("Find…"))
        self.find_edit.setClearButtonEnabled(True)
        self.find_edit.setMaximumWidth(220)
        # Live search as the user types; Enter jumps to the next match.
        self.find_edit.textChanged.connect(self._find_incremental)
        self.find_edit.returnPressed.connect(self._find_next)
        tools.addWidget(self.find_edit)
        layout.addLayout(tools)

        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.text.setLineWrapMode(QTextEdit.NoWrap)
        layout.addWidget(self.text, 1)

        buttons = QHBoxLayout()
        clear_btn = QPushButton(tr("Clear"))
        clear_btn.clicked.connect(self.clear_log)
        buttons.addWidget(clear_btn)
        export_btn = QPushButton(tr("Export…"))
        export_btn.clicked.connect(self.export_log)
        buttons.addWidget(export_btn)
        if follow_app_log:
            folder_btn = QPushButton(tr("Open log folder"))
            folder_btn.clicked.connect(self.open_log_folder)
            buttons.addWidget(folder_btn)
            diag_btn = QPushButton(tr("Export diagnostics"))
            diag_btn.clicked.connect(self.export_diagnostics)
            buttons.addWidget(diag_btn)
        buttons.addStretch(1)
        close_btn = QPushButton(tr("Close"))
        close_btn.clicked.connect(self.close)
        buttons.addWidget(close_btn)
        layout.addLayout(buttons)

        # Keep Enter in the find field bound to "find next" — without this the
        # dialog routes Enter to the first autoDefault button (Clear, or the
        # titlebar close button), so disable that on every button here.
        for btn in self.findChildren(QPushButton):
            btn.setAutoDefault(False)
            btn.setDefault(False)

        QShortcut(QKeySequence.Find, self, activated=self.find_edit.setFocus)

        if follow_app_log:
            self._load_app_log_tail()
            self._live_handler = _LiveLogHandler()
            self._live_handler.bridge.message.connect(self.log_message)
            logging.getLogger().addHandler(self._live_handler)

    # ---------------------------------------------------------------- loading

    def _load_app_log_tail(self):
        """Load only the tail of the log file (bounded memory, fast on big files)."""
        try:
            size = os.path.getsize(LOG_FILE)
            with open(LOG_FILE, "rb") as fh:
                if size > TAIL_BYTES:
                    fh.seek(size - TAIL_BYTES)
                    fh.readline()  # drop the partial first line after the seek
                raw = fh.read()
            lines = raw.decode("utf-8", errors="replace").splitlines()
        except OSError as exc:
            self.log_message(f"Could not read {LOG_FILE}: {exc}", 'warning')
            return
        self.text.setUpdatesEnabled(False)
        level = 'info'
        for line in lines:
            # continuation lines (tracebacks) keep the previous level
            if " - ERROR - " in line or " - CRITICAL - " in line:
                level = 'error'
            elif " - WARNING - " in line:
                level = 'warning'
            elif " - INFO - " in line or " - DEBUG - " in line:
                level = 'info'
            self.log_message(line, level)
        self.text.setUpdatesEnabled(True)

    def closeEvent(self, event):
        if self._live_handler is not None:
            logging.getLogger().removeHandler(self._live_handler)
            self._live_handler = None
        super().closeEvent(event)

    # ------------------------------------------------------------- rendering

    def _append_line(self, message, level):
        cursor = self.text.textCursor()
        cursor.movePosition(QTextCursor.End)
        fmt = QTextCharFormat()
        color = LEVEL_COLORS.get(level)
        if color:
            fmt.setForeground(QColor(color))
        cursor.insertText(message + "\n", fmt)
        self.text.setTextCursor(cursor)
        self.text.ensureCursorVisible()

    def log_message(self, message, level='info'):
        self._records.append((message, level))
        if len(self._records) > MAX_RECORDS:
            del self._records[:len(self._records) - MAX_RECORDS]
        if LEVEL_RANK.get(level, 0) >= self._min_rank:
            self._append_line(message, level)

    def bulk_insert(self, messages):
        for message, level in messages:
            self.log_message(message, level)

    def _on_filter_changed(self):
        self._min_rank = self.level_combo.currentData() or 0
        self.text.clear()
        self.text.setUpdatesEnabled(False)
        for message, level in self._records:
            if LEVEL_RANK.get(level, 0) >= self._min_rank:
                self._append_line(message, level)
        self.text.setUpdatesEnabled(True)

    def _find_incremental(self):
        """Search live as the user types — match from the current selection start
        so the highlight grows with the query instead of skipping ahead."""
        query = self.find_edit.text()
        if not query:
            return
        cursor = self.text.textCursor()
        cursor.setPosition(cursor.selectionStart())
        self.text.setTextCursor(cursor)
        self._find_from_cursor(query)

    def _find_next(self):
        query = self.find_edit.text()
        if query:
            self._find_from_cursor(query)

    def _find_from_cursor(self, query):
        if not self.text.find(query):
            # wrap around to the top and try once more
            cursor = self.text.textCursor()
            cursor.movePosition(QTextCursor.Start)
            self.text.setTextCursor(cursor)
            self.text.find(query)

    # --------------------------------------------------------------- actions

    def clear_log(self):
        """Clear the view, and (when following app.log) truncate the file too —
        users expect "Clear" to actually discard, not just hide."""
        if self._follow_app_log:
            if QMessageBox.question(
                    self, tr("Clear"),
                    tr("Clear the log file? This cannot be undone."),
            ) != QMessageBox.Yes:
                return
            try:
                open(LOG_FILE, "w", encoding="utf-8").close()
            except OSError as exc:
                logging.warning(f"Could not clear {LOG_FILE}: {exc}")
        self._records.clear()
        self.text.clear()

    def export_log(self):
        path, _ = QFileDialog.getSaveFileName(self, tr("Export Log"), "log.txt",
                                              tr("Text files (*.txt)"))
        if path:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(self.text.toPlainText())

    def open_log_folder(self):
        folder = os.path.dirname(os.path.abspath(LOG_FILE))
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder))

    def export_diagnostics(self):
        from app.core.diagnostics import build_diagnostics_zip
        try:
            zip_path = build_diagnostics_zip()
        except Exception as exc:
            logging.warning(f"Could not build diagnostics bundle: {exc}")
            QMessageBox.warning(self, tr("Export diagnostics"),
                                tr("Could not create the diagnostics file."))
            return
        QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.dirname(zip_path)))
        QMessageBox.information(
            self, tr("Export diagnostics"),
            tr("Diagnostics saved to:\n{path}").format(path=zip_path))
