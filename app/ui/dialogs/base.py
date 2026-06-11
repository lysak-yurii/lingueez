"""Frameless dialog base with an integrated title bar matching the app."""
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

from app.ui import icons, theme
from app.ui.titlebar import DragArea


class FramelessDialog(QDialog):
    """QDialog with client-side decorations: draggable header + close button.

    Subclasses build their UI in ``self.content_layout``.
    """

    def __init__(self, parent=None, title=""):
        super().__init__(parent)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.colors = theme.current_colors()

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        bar = DragArea(objectName="DialogTitleBar")
        bl = QHBoxLayout(bar)
        bl.setContentsMargins(18, 8, 8, 8)
        self._title_label = QLabel(title, objectName="DialogTitle")
        bl.addWidget(self._title_label)
        bl.addStretch(1)
        close_btn = QPushButton(objectName="winBtnClose")
        close_btn.setIcon(icons.icon("x", self.colors["text_dim"], 15))
        close_btn.setIconSize(QSize(14, 14))
        close_btn.setFocusPolicy(Qt.NoFocus)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.clicked.connect(self.reject)
        bl.addWidget(close_btn)
        outer.addWidget(bar)

        body = QWidget()
        self.content_layout = QVBoxLayout(body)
        self.content_layout.setContentsMargins(20, 18, 20, 16)
        self.content_layout.setSpacing(12)
        outer.addWidget(body, 1)

        super().setWindowTitle(title)

    def setWindowTitle(self, title):
        super().setWindowTitle(title)
        self._title_label.setText(title)
