"""Small reusable widgets."""
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QLabel


class ElidedLabel(QLabel):
    """Single-line label that elides its text and exposes it as a tooltip.

    Unlike a plain QLabel it never enforces the full text width as a
    layout minimum, so it can be squeezed without growing the window.
    """

    def __init__(self, parent=None, min_width=24):
        super().__init__(parent)
        self._full = ""
        self._min_width = min_width

    def minimumSizeHint(self):
        return QSize(self._min_width, super().minimumSizeHint().height())

    def set_full_text(self, text):
        self._full = text or ""
        self.setToolTip(self._full)
        self._refit()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._refit()

    def _refit(self):
        fm = self.fontMetrics()
        self.setText(fm.elidedText(self._full, Qt.ElideRight, max(0, self.width() - 2)))
