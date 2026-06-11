"""Custom item delegates — colored status pills."""
from PySide6.QtCore import QRectF, Qt
from PySide6.QtGui import QColor, QFont, QPainter
from PySide6.QtWidgets import QStyledItemDelegate, QStyle

# status -> (background rgba, text color)
PILL_COLORS = {
    "new":       ("#2f6fed", 38),
    "to learn":  ("#9a6ff0", 38),
    "learning":  ("#d29922", 38),
    "reviewing": ("#d29922", 38),
    "mastered":  ("#2da44e", 38),
    "ignored":   ("#8b98a5", 30),
}
DEFAULT_PILL = ("#8b98a5", 30)


class StatusPillDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        text = str(index.data() or "")
        if not text:
            return super().paint(painter, option, index)

        # background (selection / favorite tint / alternating) first
        opt_text = text
        self.initStyleOption(option, index)
        option.text = ""
        style = option.widget.style() if option.widget else None
        if style:
            style.drawControl(QStyle.CE_ItemViewItem, option, painter, option.widget)

        base_hex, alpha = PILL_COLORS.get(opt_text.strip().lower(), DEFAULT_PILL)
        bg = QColor(base_hex)
        bg.setAlpha(alpha + 25)
        # readable pill text on both themes
        dark_theme = option.palette.window().color().lightness() < 128
        fg = QColor(base_hex).lighter(135) if dark_theme else QColor(base_hex).darker(130)

        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)

        font = QFont(option.font)
        font.setPointSizeF(max(7.0, option.font.pointSizeF() - 1))
        font.setWeight(QFont.DemiBold)
        painter.setFont(font)

        metrics = painter.fontMetrics()
        text_width = metrics.horizontalAdvance(opt_text)
        pill_height = metrics.height() + 6
        pill_width = text_width + 20
        rect = option.rect
        pill = QRectF(rect.x() + 6,
                      rect.y() + (rect.height() - pill_height) / 2,
                      min(pill_width, rect.width() - 10), pill_height)

        painter.setPen(Qt.NoPen)
        painter.setBrush(bg)
        painter.drawRoundedRect(pill, pill_height / 2, pill_height / 2)

        painter.setPen(fg)
        painter.drawText(pill, Qt.AlignCenter, opt_text)
        painter.restore()
