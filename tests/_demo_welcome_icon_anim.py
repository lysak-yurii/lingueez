# Lingueez — standalone preview harness (NOT a unit test).
#
# Plays three "two halves unite" animations of the app icon side by side so the
# logo's blue top block and yellow bottom block can be compared and one picked.
# The winning variant is then folded into AnimatedAppIcon in
# app/ui/dialogs/welcome_dialog.py. Safe to delete after a choice is made.
#
# Run:  ~/.venvs/dictionary-upgraded/bin/python tests/welcome_icon_anim_demo.py
#
# SPDX-License-Identifier: AGPL-3.0-or-later
import os
import sys

from PySide6.QtCore import (
    Property,
    QEasingCurve,
    QParallelAnimationGroup,
    QPropertyAnimation,
    QRectF,
    Qt,
    QTimer,
)
from PySide6.QtGui import QFont, QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

# Resolve the icon relative to the repo root, regardless of where we're launched.
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICON_PATH = os.path.join(_ROOT, "assets", "icons", "icon.png")

ICON_BASE = 96  # resting display width of the full logo (px)
ICON_BOX_W = 150  # generous box so separation + float never clip
ICON_BOX_H = 190
SPLIT_RATIO = 0.71  # transparent gap between blue (≤69%) and yellow (≥74%)


class UnitingIcon(QWidget):
    """The app icon split into a blue top layer and a yellow bottom layer, each
    independently positioned so they can start apart and animate together.

    `variant` selects the choreography: 'magnetic', 'snap' or 'book'.
    Pre-scales each layer ONCE; per frame it only blits the two pixmaps, so the
    motion stays smooth (no per-frame resampling of the 549px source)."""

    def __init__(self, variant, parent=None):
        super().__init__(parent)
        self.variant = variant
        screen = QApplication.primaryScreen()
        dpr = screen.devicePixelRatio() if screen else 1.0

        src = QPixmap(ICON_PATH)
        self._ok = not src.isNull()
        if self._ok:
            w, h = src.width(), src.height()
            split = round(h * SPLIT_RATIO)
            self._split_ratio = split / h
            top_src = src.copy(0, 0, w, split)
            bot_src = src.copy(0, split, w, h - split)
            maxpx = max(1, int(ICON_BASE * 1.25 * dpr))
            self._top = top_src.scaledToWidth(maxpx, Qt.SmoothTransformation)
            self._bottom = bot_src.scaledToWidth(maxpx, Qt.SmoothTransformation)

        # animatable state
        self._gap = 0.0  # vertical separation between the two halves (px)
        self._gap_top = 0.0  # book-close: only the top block carries a gap
        self._scale = 1.0  # snap: brief scale pulse on meeting
        self._opacity = 0.0  # fade in
        self._offset = 0.0  # idle float (whole unit)

        self.setFixedSize(ICON_BOX_W, ICON_BOX_H)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

    # --- animatable Qt properties ---------------------------------------
    def _g(self):
        return self._gap

    def _sg(self, v):
        self._gap = v
        self.update()

    def _gt(self):
        return self._gap_top

    def _sgt(self, v):
        self._gap_top = v
        self.update()

    def _sc(self):
        return self._scale

    def _ssc(self, v):
        self._scale = v
        self.update()

    def _op(self):
        return self._opacity

    def _sop(self, v):
        self._opacity = v
        self.update()

    def _of(self):
        return self._offset

    def _sof(self, v):
        self._offset = v
        self.update()

    gap = Property(float, _g, _sg)
    gapTop = Property(float, _gt, _sgt)
    scaleF = Property(float, _sc, _ssc)
    opacityF = Property(float, _op, _sop)
    offsetY = Property(float, _of, _sof)

    # --- paint -----------------------------------------------------------
    def paintEvent(self, event):
        if not self._ok:
            return
        p = QPainter(self)
        p.setRenderHint(QPainter.SmoothPixmapTransform)
        p.setOpacity(max(0.0, min(1.0, self._opacity)))

        size = ICON_BASE * self._scale
        top_h = size * self._split_ratio
        bot_h = size * (1.0 - self._split_ratio)
        x = (self.width() - size) / 2.0
        # vertical center of the assembled logo, plus idle float
        base_y = (self.height() - size) / 2.0 + self._offset

        # 'book' splits only the top; the others split symmetrically.
        top_off = self._gap_top if self.variant == "book" else self._gap
        bot_off = 0.0 if self.variant == "book" else self._gap

        p.drawPixmap(QRectF(x, base_y - top_off, size, top_h), self._top, QRectF(self._top.rect()))
        p.drawPixmap(
            QRectF(x, base_y + top_h + bot_off, size, bot_h),
            self._bottom,
            QRectF(self._bottom.rect()),
        )

    # --- choreography ----------------------------------------------------
    def play(self):
        """Run the entrance for this variant, then start the idle float."""
        if not self._ok:
            return
        # reset
        self._scale = 1.0
        self._offset = 0.0
        self._opacity = 0.0
        self._gap = 0.0
        self._gap_top = 0.0

        grp = QParallelAnimationGroup(self)

        def anim(prop, start, end, dur, curve, delay=0):
            a = QPropertyAnimation(self, prop, self)
            a.setStartValue(start)
            a.setEndValue(end)
            a.setDuration(dur)
            a.setEasingCurve(curve)
            if delay:
                # express a delay as an extra leading keyframe holding `start`
                a.setStartValue(start)
            grp.addAnimation(a)
            return a

        if self.variant == "magnetic":
            self._gap = 22.0
            anim(b"opacityF", 0.0, 1.0, 420, QEasingCurve.OutCubic)
            # glide together, then a tiny settle handled in finished()
            anim(b"gap", 22.0, 0.0, 720, QEasingCurve.OutCubic)
            grp.finished.connect(self._magnetic_settle)

        elif self.variant == "snap":
            self._gap = 20.0
            anim(b"opacityF", 0.0, 1.0, 320, QEasingCurve.OutCubic)
            back = QEasingCurve(QEasingCurve.OutBack)
            back.setOvershoot(1.7)
            anim(b"gap", 20.0, 0.0, 560, back)
            grp.finished.connect(self._snap_pop)

        else:  # book close
            self._gap_top = 30.0
            self._opacity = 1.0  # base is visible; cover drops in
            anim(b"opacityF", 0.4, 1.0, 300, QEasingCurve.OutCubic)
            anim(b"gapTop", 30.0, 0.0, 700, QEasingCurve.OutCubic)
            grp.finished.connect(self._book_land)

        grp.start()
        self._entrance = grp  # keep ref

    def _magnetic_settle(self):
        a = QPropertyAnimation(self, b"gap", self)
        a.setDuration(360)
        a.setKeyValueAt(0.0, 0.0)
        a.setKeyValueAt(0.5, -3.0)  # gentle press past the seam
        a.setKeyValueAt(1.0, 0.0)
        a.setEasingCurve(QEasingCurve.InOutSine)
        a.finished.connect(self._start_float)
        a.start()
        self._settle = a

    def _snap_pop(self):
        a = QPropertyAnimation(self, b"scaleF", self)
        a.setDuration(300)
        a.setKeyValueAt(0.0, 1.0)
        a.setKeyValueAt(0.45, 1.04)  # satisfying click
        a.setKeyValueAt(1.0, 1.0)
        a.setEasingCurve(QEasingCurve.OutCubic)
        a.finished.connect(self._start_float)
        a.start()
        self._pop = a

    def _book_land(self):
        # soft landing damp: a 2px micro-bounce of the whole unit
        a = QPropertyAnimation(self, b"offsetY", self)
        a.setDuration(320)
        a.setKeyValueAt(0.0, 0.0)
        a.setKeyValueAt(0.5, 2.5)
        a.setKeyValueAt(1.0, 0.0)
        a.setEasingCurve(QEasingCurve.OutCubic)
        a.finished.connect(self._start_float)
        a.start()
        self._land = a

    def _start_float(self):
        a = QPropertyAnimation(self, b"offsetY", self)
        a.setDuration(3800)
        a.setKeyValueAt(0.0, 0.0)
        a.setKeyValueAt(0.5, -5.0)
        a.setKeyValueAt(1.0, 0.0)
        a.setEasingCurve(QEasingCurve.InOutSine)
        a.setLoopCount(-1)
        a.start()
        self._float = a


class DemoWindow(QWidget):
    VARIANTS = (
        ("magnetic", "1 · Magnetic settle", "soft pull + 3px settle"),
        ("snap", "2 · Snap pop", "overshoot + scale click"),
        ("book", "3 · Book close", "cover drops onto base"),
    )

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome icon — unite animation preview")
        self.setStyleSheet("background:#f8f4dc;")
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 22, 28, 22)
        root.setSpacing(18)

        heading = QLabel("Which way should the two halves unite?")
        heading.setAlignment(Qt.AlignCenter)
        heading.setFont(QFont("Sans", 15, QFont.Bold))
        heading.setStyleSheet("color:#1c1c1c;")
        root.addWidget(heading)

        row = QHBoxLayout()
        row.setSpacing(24)
        self.icons = []
        for variant, title, sub in self.VARIANTS:
            col = QVBoxLayout()
            col.setSpacing(4)
            icon = UnitingIcon(variant)
            self.icons.append(icon)
            col.addWidget(icon, 0, Qt.AlignHCenter)
            t = QLabel(title)
            t.setAlignment(Qt.AlignCenter)
            t.setFont(QFont("Sans", 11, QFont.Bold))
            t.setStyleSheet("color:#1c1c1c;")
            s = QLabel(sub)
            s.setAlignment(Qt.AlignCenter)
            s.setStyleSheet("color:#6b6b6b; font-size:11px;")
            col.addWidget(t)
            col.addWidget(s)
            row.addLayout(col)
        root.addLayout(row)

        replay = QPushButton("↻  Replay all")
        replay.setCursor(Qt.PointingHandCursor)
        replay.setStyleSheet(
            "QPushButton{background:#39a0e3;color:white;border:none;"
            "padding:9px 22px;border-radius:8px;font-size:13px;font-weight:600;}"
            "QPushButton:hover{background:#2e8fcf;}"
        )
        replay.clicked.connect(self.replay)
        root.addWidget(replay, 0, Qt.AlignCenter)

        hint = QLabel("Tell me the number you like (1, 2 or 3).")
        hint.setAlignment(Qt.AlignCenter)
        hint.setStyleSheet("color:#6b6b6b; font-size:11px;")
        root.addWidget(hint)

        QTimer.singleShot(350, self.replay)

    def replay(self):
        for icon in self.icons:
            icon.play()


def main():
    app = QApplication(sys.argv)
    if QPixmap(ICON_PATH).isNull():
        print("ERROR: could not load", ICON_PATH)
        return 1
    w = DemoWindow()
    w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
