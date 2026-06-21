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

"""Stale-reconnect deletion review.

When a device reconnects after being offline longer than the cloud's tombstone
retention, rows that were deleted on other devices in the meantime have lost their
tombstone, so the sync engine can't tell "deleted while away" from "new local data".
Rather than guess (and risk resurrecting deletions or losing local work), we ask the
user. See ``SyncManager.detect_stale_orphans``.
"""
from typing import List, Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView, QDialog, QHBoxLayout, QLabel, QListWidget, QPushButton,
)

from app.i18n import lang_label, tr
from app.ui.dialogs.base import FramelessDialog


class SyncReviewDialog(FramelessDialog):
    """Lets the user Keep (re-upload) or Remove rows that were deleted elsewhere
    while this device was offline past the retention window."""

    def __init__(self, parent, words: List[dict], texts: List[dict]):
        super().__init__(parent, title=tr("Items deleted on another device"))
        self.setMinimumSize(560, 420)
        self._choice: Optional[bool] = None  # True=keep, False=remove, None=cancel

        total = len(words) + len(texts)
        msg = QLabel(tr(
            "This device was offline long enough that {n} item(s) below were deleted "
            "on your other devices in the meantime, yet still exist here.\n\n"
            "Keep them (re-upload to the cloud for all your devices), or remove them "
            "from this device?").format(n=total))
        msg.setWordWrap(True)
        self.content_layout.addWidget(msg)

        listing = QListWidget()
        listing.setSelectionMode(QAbstractItemView.NoSelection)
        listing.setFocusPolicy(Qt.NoFocus)
        for w in words:
            w1, w2 = w.get('Word1', '') or '', w.get('Word2', '') or ''
            lang = lang_label(w.get('Language1', '') or '')
            suffix = f"  ({lang})" if lang else ""
            listing.addItem(f"{w1}  →  {w2}{suffix}")
        for t in texts:
            title = t.get('Title', '') or tr("(untitled)")
            listing.addItem(tr("[Text] {title}").format(title=title))
        self.content_layout.addWidget(listing, 1)

        row = QHBoxLayout()
        remove = QPushButton(tr("Remove from this device"), objectName="dangerButton")
        remove.setCursor(Qt.PointingHandCursor)
        remove.clicked.connect(self._remove)
        row.addWidget(remove)
        row.addStretch(1)
        cancel = QPushButton(tr("Decide later"))
        cancel.setCursor(Qt.PointingHandCursor)
        cancel.clicked.connect(self.reject)
        row.addWidget(cancel)
        keep = QPushButton(tr("Keep & upload"), objectName="primaryButton")
        keep.setCursor(Qt.PointingHandCursor)
        keep.setDefault(True)
        keep.clicked.connect(self._keep)
        row.addWidget(keep)
        self.content_layout.addLayout(row)

    def _keep(self):
        self._choice = True
        self.accept()

    def _remove(self):
        self._choice = False
        self.accept()

    @classmethod
    def ask(cls, parent, words: List[dict], texts: List[dict]) -> Optional[bool]:
        """Show the review. Returns True (keep & upload), False (remove), or None
        (the user deferred — leave everything untouched for now)."""
        dlg = cls(parent, words, texts)
        if dlg.exec() != QDialog.Accepted:
            return None
        return dlg._choice
