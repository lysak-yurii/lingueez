"""Edit Word dialog."""
from PySide6.QtWidgets import (
    QComboBox, QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
)

from app.ui.dialogs.base import FramelessDialog


class EditWordDialog(FramelessDialog):
    def __init__(self, parent, record, languages, statuses):
        super().__init__(parent, title=f"Edit — {record.get('Word1', '')}")
        self.setMinimumWidth(520)

        layout = self.content_layout
        grid = QGridLayout()
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(8)

        grid.addWidget(QLabel("Language"), 0, 0)
        self.lang1_combo = QComboBox()
        self.lang1_combo.setEditable(True)
        self.lang1_combo.addItems(languages)
        self.lang1_combo.setCurrentText(str(record.get('Language1') or ""))
        grid.addWidget(self.lang1_combo, 1, 0)

        grid.addWidget(QLabel("Word"), 0, 1)
        self.word1_edit = QLineEdit(str(record.get('Word1') or ""))
        grid.addWidget(self.word1_edit, 1, 1)

        grid.addWidget(QLabel("Translation language"), 2, 0)
        self.lang2_combo = QComboBox()
        self.lang2_combo.setEditable(True)
        self.lang2_combo.addItems(languages)
        self.lang2_combo.setCurrentText(str(record.get('Language2') or ""))
        grid.addWidget(self.lang2_combo, 3, 0)

        grid.addWidget(QLabel("Translation"), 2, 1)
        self.word2_edit = QLineEdit(str(record.get('Word2') or ""))
        grid.addWidget(self.word2_edit, 3, 1)

        grid.addWidget(QLabel("Status"), 4, 0)
        self.status_combo = QComboBox()
        self.status_combo.addItems(statuses)
        self.status_combo.setCurrentText(str(record.get('Status') or "New"))
        grid.addWidget(self.status_combo, 5, 0)

        grid.setColumnStretch(1, 1)
        layout.addLayout(grid)

        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def result_data(self):
        return {
            'Language1': self.lang1_combo.currentText().strip(),
            'Word1': self.word1_edit.text().strip(),
            'Language2': self.lang2_combo.currentText().strip(),
            'Word2': self.word2_edit.text().strip(),
            'Status': self.status_combo.currentText().strip(),
        }
