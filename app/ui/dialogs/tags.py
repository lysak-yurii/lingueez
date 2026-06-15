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

"""Tag management dialog (add/remove tags for one or many words)."""
import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMessageBox, QPushButton,
)

from app.core import db as dbq
from app.i18n import tr
from app.ui.dialogs.base import FramelessDialog


class TagDialog(FramelessDialog):
    def __init__(self, parent, word_ids, db_adapter):
        super().__init__(parent, title=tr("Tags — {count} word(s)").format(count=len(word_ids)))
        self.word_ids = word_ids
        self.db_adapter = db_adapter
        self.setMinimumSize(420, 460)

        layout = self.content_layout
        layout.setContentsMargins(18, 18, 18, 14)
        layout.setSpacing(10)

        hint_text = tr("Tags marked ✓ apply to all selected words.")
        if len(word_ids) > 1:
            hint_text += "  " + tr("◐ (partial) means only some of them have the tag.")
        hint = QLabel(hint_text)
        hint.setObjectName("dimLabel")
        hint.setWordWrap(True)
        layout.addWidget(hint)

        row = QHBoxLayout()
        self.tag_input = QLineEdit()
        self.tag_input.setPlaceholderText(tr("New tag name…"))
        self.tag_input.returnPressed.connect(self.add_tag)
        row.addWidget(self.tag_input, 1)
        add_btn = QPushButton(tr("Add Tag"), objectName="primaryButton")
        add_btn.clicked.connect(self.add_tag)
        row.addWidget(add_btn)
        layout.addLayout(row)

        self.listing = QListWidget()
        self.listing.setSelectionMode(QListWidget.ExtendedSelection)
        layout.addWidget(self.listing, 1)

        buttons = QHBoxLayout()
        apply_btn = QPushButton(tr("Apply Selected to All"))
        apply_btn.setToolTip(tr("Attach the selected tag(s) to every selected word"))
        apply_btn.clicked.connect(self.apply_selected)
        buttons.addWidget(apply_btn)
        remove_btn = QPushButton(tr("Remove Selected"), objectName="dangerButton")
        remove_btn.clicked.connect(self.remove_selected)
        buttons.addWidget(remove_btn)
        buttons.addStretch(1)
        close_btn = QPushButton(tr("Close"))
        close_btn.clicked.connect(self.accept)
        buttons.addWidget(close_btn)
        layout.addLayout(buttons)

        self.populate()

    # ------------------------------------------------------------------

    def populate(self):
        self.listing.clear()
        all_tags = dbq.get_all_tags()
        counts = dbq.get_tag_usage_counts()

        per_word = {wid: set(dbq.get_tags_for_word(wid)) for wid in self.word_ids}
        common = set.intersection(*per_word.values()) if per_word else set()
        union = set.union(*per_word.values()) if per_word else set()

        for tag in all_tags:
            if tag in common:
                marker = "✓ "
            elif tag in union:
                marker = "◐ "
            else:
                marker = "   "
            partial = f"  {tr('(partial)')}" if tag in union and tag not in common else ""
            item = QListWidgetItem(f"{marker}{tag}{partial}   ·  {counts.get(tag, 0)} {tr('use(s)')}")
            item.setData(Qt.UserRole, tag)
            self.listing.addItem(item)

    def _selected_tags(self):
        return [item.data(Qt.UserRole) for item in self.listing.selectedItems()]

    def add_tag(self):
        tag_name = self.tag_input.text().strip()
        if not tag_name:
            return
        try:
            for word_id in self.word_ids:
                self.db_adapter.add_tag_to_word(word_id, tag_name)
            self.tag_input.clear()
            self.populate()
        except Exception as exc:
            logging.error(f"Error adding tag: {exc}")
            QMessageBox.critical(self, tr("Error"), tr("Failed to add tag:\n{error}").format(error=exc))

    def apply_selected(self):
        tags = self._selected_tags()
        if not tags:
            QMessageBox.information(self, tr("Tags"), tr("Select tag(s) in the list first."))
            return
        try:
            for tag in tags:
                for word_id in self.word_ids:
                    self.db_adapter.add_tag_to_word(word_id, tag)
            self.populate()
        except Exception as exc:
            logging.error(f"Error applying tags: {exc}")
            QMessageBox.critical(self, tr("Error"), tr("Failed to apply tags:\n{error}").format(error=exc))

    def remove_selected(self):
        tags = self._selected_tags()
        if not tags:
            QMessageBox.information(self, tr("Tags"), tr("Select tag(s) in the list first."))
            return
        try:
            for tag in tags:
                for word_id in self.word_ids:
                    self.db_adapter.remove_tag_from_word(word_id, tag)
            self.populate()
        except Exception as exc:
            logging.error(f"Error removing tags: {exc}")
            QMessageBox.critical(self, tr("Error"), tr("Failed to remove tags:\n{error}").format(error=exc))
