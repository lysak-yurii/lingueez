"""Color-coded log viewer (used for imports and general app logging)."""
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QTextCharFormat, QTextCursor
from PySide6.QtWidgets import (
    QDialog, QFileDialog, QHBoxLayout, QPushButton, QTextEdit, QVBoxLayout,
)

LEVEL_COLORS = {
    'info': None,
    'warning': "#d29922",
    'error': "#e5534b",
    'success': "#3fb950",
    'new': "#4f8cff",
    'rejected': "#e5534b",
}


class LogWindow(QDialog):
    def __init__(self, parent, title="Log"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumSize(700, 460)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(False)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 12)

        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.text.setLineWrapMode(QTextEdit.NoWrap)
        layout.addWidget(self.text, 1)

        buttons = QHBoxLayout()
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.text.clear)
        buttons.addWidget(clear_btn)
        export_btn = QPushButton("Export…")
        export_btn.clicked.connect(self.export_log)
        buttons.addWidget(export_btn)
        buttons.addStretch(1)
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        buttons.addWidget(close_btn)
        layout.addLayout(buttons)

    def log_message(self, message, level='info'):
        cursor = self.text.textCursor()
        cursor.movePosition(QTextCursor.End)
        fmt = QTextCharFormat()
        color = LEVEL_COLORS.get(level)
        if color:
            fmt.setForeground(QColor(color))
        cursor.insertText(message + "\n", fmt)
        self.text.setTextCursor(cursor)
        self.text.ensureCursorVisible()

    def bulk_insert(self, messages):
        for message, level in messages:
            self.log_message(message, level)

    def export_log(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export Log", "log.txt",
                                              "Text files (*.txt)")
        if path:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(self.text.toPlainText())
