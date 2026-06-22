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

"""Bin: deleted words/texts kept in the local trash and (when sync is on) the
Supabase cloud, so they can be restored within the grace period."""
import logging
from datetime import datetime

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QAbstractItemView, QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMessageBox, QPushButton, QTabWidget, QVBoxLayout, QWidget,
)

from app.config import get_int, load_settings
from app.i18n import full_date, lang_label, ntr, tr, weekday_name
from app.ui import icons
from app.ui.dialogs.base import FramelessDialog, confirm


def _parse_dt(value):
    """Parse a stored ISO ``deleted_at`` into a naive local ``datetime``, or None."""
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
        # Compare against local wall-clock dates; drop tzinfo after converting.
        if dt.tzinfo is not None:
            dt = dt.astimezone().replace(tzinfo=None)
        return dt
    except Exception:
        return None


def _deleted_phrase(dt):
    """A deletion time -> 'deleted Today' / 'deleted Yesterday' /
    'deleted Mon · June 9, 2026'. Mirrors backups._friendly_date."""
    if dt is None:
        return ""
    days = (datetime.now().date() - dt.date()).days
    if days <= 0:
        when = tr("Today")
    elif days == 1:
        when = tr("Yesterday")
    elif days < 7:
        when = f"{weekday_name(dt)} · {full_date(dt)}"
    else:
        when = full_date(dt)
    return tr("deleted {when}").format(when=when)


def _countdown(dt, grace_days):
    """(label, urgent) for how long until auto-deletion, or ('', False) if unknown.

    Urgent (warning-colored) when 3 days or fewer remain."""
    if dt is None:
        return "", False
    days = (datetime.now().date() - dt.date()).days
    remaining = max(0, grace_days - days)
    if remaining <= 0:
        return tr("Auto-deletes soon"), True
    label = ntr(remaining,
                tr("Auto-deletes in {n} day").format(n=remaining),
                tr("Auto-deletes in {n} days").format(n=remaining),
                tr("Auto-deletes in {n} days (genitive)").format(n=remaining))
    return label, remaining <= 3


class BinWindow(FramelessDialog):
    def __init__(self, parent, db_adapter, on_restored=None):
        super().__init__(parent, title=tr("Bin — Deleted Items"))
        self.db_adapter = db_adapter
        self.on_restored = on_restored

        self.setMinimumSize(680, 480)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.grace_days = get_int(load_settings(), 'cleanup_grace_period_days', 30)

        layout = self.content_layout

        self.tabs = QTabWidget()
        self.words_list, words_tab = self._make_tab(
            tr("The bin is empty. Deleted words will appear here."))
        self.texts_list, texts_tab = self._make_tab(
            tr("The bin is empty. Deleted texts will appear here."))
        self.tabs.addTab(words_tab, tr("Words"))
        self.tabs.addTab(texts_tab, tr("Texts"))
        self.tabs.currentChanged.connect(self._update_actions)
        for listing in (self.words_list, self.texts_list):
            listing.itemSelectionChanged.connect(self._update_actions)
        layout.addWidget(self.tabs, 1)

        buttons = QHBoxLayout()
        buttons.setSpacing(8)

        # Bulk maintenance is a rare, different kind of action from the per-item
        # restore/delete, so it sits apart on the left as a quiet icon button
        # (its label lives in the tooltip) and never crowds the primary actions.
        cleanup_btn = QPushButton(objectName="iconButton")
        cleanup_btn.setIcon(icons.icon("clock", self.colors["text_dim"], 17))
        cleanup_btn.setIconSize(QSize(17, 17))
        cleanup_btn.setToolTip(tr("Cleanup Old Items…"))
        cleanup_btn.setCursor(Qt.PointingHandCursor)
        cleanup_btn.clicked.connect(self.manual_cleanup)
        buttons.addWidget(cleanup_btn)
        buttons.addStretch(1)

        # A compact, dim selection count keeps the action labels short and stable
        # (so they never clip in longer languages) while still showing intent.
        self.sel_label = QLabel(objectName="dimLabel")
        buttons.addWidget(self.sel_label)
        buttons.addSpacing(2)

        # Destructive action: red icon normally, white on hover (when the button
        # fills red) via QIcon's Active mode.
        self.delete_btn = QPushButton(tr("Delete Permanently"), objectName="dangerButton")
        trash = QIcon()
        trash.addPixmap(icons.pixmap("trash", self.colors["danger"], 16), QIcon.Normal)
        trash.addPixmap(icons.pixmap("trash", "#ffffff", 16), QIcon.Active)
        self.delete_btn.setIcon(trash)
        self.delete_btn.setIconSize(QSize(16, 16))
        self.delete_btn.setCursor(Qt.PointingHandCursor)
        self.delete_btn.clicked.connect(self.delete_selected)
        buttons.addWidget(self.delete_btn)

        self.restore_btn = QPushButton(tr("Restore"), objectName="primaryButton")
        self.restore_btn.setIcon(icons.icon("rotate-ccw", "#ffffff", 16))
        self.restore_btn.setIconSize(QSize(16, 16))
        self.restore_btn.setCursor(Qt.PointingHandCursor)
        self.restore_btn.clicked.connect(self.restore_selected)
        buttons.addWidget(self.restore_btn)

        close_btn = QPushButton(tr("Close"))
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.clicked.connect(self.accept)
        buttons.addWidget(close_btn)
        layout.addLayout(buttons)

        self.load_data()
        self._update_actions()

    def _update_actions(self):
        """Keep the restore/delete buttons in step with the selection: enabled
        only when something is picked, with a compact '{n} selected' hint."""
        listing = self.words_list if self.tabs.currentIndex() == 0 else self.texts_list
        n = len(listing.selectedItems())
        self.restore_btn.setEnabled(n > 0)
        self.delete_btn.setEnabled(n > 0)
        self.sel_label.setText(tr("{n} selected").format(n=n) if n else "")

    def _make_tab(self, empty_text):
        """A tab page holding a styled list and a centered empty-state label that
        swap depending on whether the list has items. Returns ``(list, page)``."""
        page = QWidget()
        box = QVBoxLayout(page)
        box.setContentsMargins(0, 12, 0, 0)
        box.setSpacing(0)

        listing = QListWidget(objectName="BinList")
        listing.setSelectionMode(QAbstractItemView.ExtendedSelection)
        listing.setUniformItemSizes(False)
        listing.itemDoubleClicked.connect(lambda _i: self.restore_selected())
        box.addWidget(listing, 1)

        empty = self._empty_state(empty_text)
        empty.hide()
        box.addWidget(empty, 1)

        listing._empty_label = empty  # toggled together in _fill_list
        return listing, page

    def _empty_state(self, text):
        """A friendly placeholder for an empty tab: a soft circular badge with a
        large trash glyph above a dim, centered caption — the look professional
        apps use so an empty list never reads as broken or blank."""
        wrap = QWidget()
        col = QVBoxLayout(wrap)
        col.setContentsMargins(24, 24, 24, 24)
        col.setSpacing(16)
        col.addStretch(1)

        badge = QLabel()
        badge.setFixedSize(QSize(84, 84))
        badge.setAlignment(Qt.AlignCenter)
        badge.setPixmap(icons.icon("trash", self.colors["text_dim"], 38).pixmap(QSize(38, 38)))
        badge.setStyleSheet(
            f"background:{self.colors['surface_alt']};"
            f" border:1px solid {self.colors['border']}; border-radius:42px;")
        badge_row = QHBoxLayout()
        badge_row.addStretch(1)
        badge_row.addWidget(badge)
        badge_row.addStretch(1)
        col.addLayout(badge_row)

        caption = QLabel(text, objectName="dimLabel")
        caption.setAlignment(Qt.AlignCenter)
        caption.setWordWrap(True)
        col.addWidget(caption)

        col.addStretch(1)
        return wrap

    def _row_widget(self, icon_name, primary, secondary, dt):
        """An elegant list row: leading icon, bold primary line over a dim
        secondary line, and a right-aligned auto-delete countdown."""
        row = QWidget()
        h = QHBoxLayout(row)
        h.setContentsMargins(12, 9, 12, 9)
        h.setSpacing(11)

        glyph = QLabel()
        glyph.setPixmap(icons.icon(icon_name, self.colors["text_dim"], 17).pixmap(QSize(17, 17)))
        h.addWidget(glyph, 0, Qt.AlignTop)

        text = QVBoxLayout()
        text.setContentsMargins(0, 0, 0, 0)
        text.setSpacing(2)
        title = QLabel(primary, objectName="backupTitle")
        text.addWidget(title)
        sub = QLabel(secondary, objectName="dimLabel")
        text.addWidget(sub)
        h.addLayout(text, 1)

        label, urgent = _countdown(dt, self.grace_days)
        if label:
            badge = QLabel(label)
            color = self.colors["warning"] if urgent else self.colors["text_dim"]
            badge.setStyleSheet(f"color:{color}; font-size:11.5px;")
            h.addWidget(badge, 0, Qt.AlignVCenter)
        return row

    def _cloud(self):
        """The cloud client when sync is active for this session, else None.

        Honors the user's sync setting (via the adapter), so a disabled-sync
        session never lists/acts on cloud items it cannot manage."""
        if self.db_adapter._use_cloud():
            return self.db_adapter.supabase
        return None

    def _binned(self, table_name):
        """Union of locally-binned items and (when sync is active) cloud
        soft-deletes, de-duplicated by ID with the local copy preferred."""
        items = {}
        for it in self.db_adapter.get_binned_items(table_name):
            key = it.get('ID') or it.get('id')
            if key is not None:
                items[key] = it
        cloud = self._cloud()
        if cloud:
            # Items permanently deleted on this device keep a (propagating) cloud
            # soft-delete until the grace-period purge; hide those from this Bin.
            purged = self.db_adapter.get_purged_ids(table_name)
            for it in cloud.get_all_soft_deleted_items(table_name):
                key = it.get('ID') or it.get('id')
                if key is not None and key not in items and key not in purged:
                    items[key] = it
        return list(items.values())

    def load_data(self):
        try:
            self._fill_list(self.words_list, self._binned('words'), self._word_row)
            self._fill_list(self.texts_list, self._binned('texts'), self._text_row)
        except Exception as exc:
            logging.error(f"Error loading deleted items: {exc}")
            QMessageBox.critical(self, tr("Error"), tr("Failed to load deleted items:\n{error}").format(error=exc))

    def _fill_list(self, listing, records, build):
        """Populate ``listing`` with one item per record, newest-deleted first.
        Each item carries its record id in ``Qt.UserRole`` and an icon+label for
        confirmation summaries in (UserRole+1, UserRole+2)."""
        listing.clear()
        records.sort(key=lambda r: str(r.get('deleted_at') or ''), reverse=True)
        for record in records:
            record_id = record.get('ID') or record.get('id')
            icon_name, primary, secondary, dt = build(record)
            item = QListWidgetItem(listing)
            item.setData(Qt.UserRole, str(record_id))
            item.setData(Qt.UserRole + 1, icon_name)
            item.setData(Qt.UserRole + 2, primary)
            widget = self._row_widget(icon_name, primary, secondary, dt)
            item.setSizeHint(widget.sizeHint())
            listing.setItemWidget(item, widget)

        has_items = listing.count() > 0
        listing.setVisible(has_items)
        listing._empty_label.setVisible(not has_items)

    def _word_row(self, word):
        pair = " → ".join(p for p in (word.get('Word1', ''), word.get('Word2', '')) if p)
        langs = " → ".join(lang_label(word.get(k, '')) for k in ('Language1', 'Language2')
                           if word.get(k))
        dt = _parse_dt(word.get('deleted_at'))
        secondary = " · ".join(p for p in (langs, _deleted_phrase(dt)) if p)
        return "book", pair or tr("(empty)"), secondary, dt

    def _text_row(self, text):
        dt = _parse_dt(text.get('deleted_at'))
        meta = " · ".join(p for p in (
            lang_label(text.get('Language', '')), text.get('Category', ''),
            _deleted_phrase(dt)) if p)
        return "file-text", text.get('Title', '') or tr("Untitled"), meta, dt

    def _selected(self):
        """The active tab's selection as ``(item_type, record_id, item, list,
        icon, label)`` tuples — enough to act on, remove, and summarize each."""
        if self.tabs.currentIndex() == 0:
            listing, item_type = self.words_list, "words"
        else:
            listing, item_type = self.texts_list, "texts"
        return [(item_type, it.data(Qt.UserRole), it, listing,
                 it.data(Qt.UserRole + 1), it.data(Qt.UserRole + 2))
                for it in listing.selectedItems()]

    def restore_selected(self):
        items = self._selected()
        if not items:
            QMessageBox.information(self, tr("Bin"), tr("Select item(s) to restore."))
            return
        if not confirm(
                self, tr("Restore"),
                tr("Restore {count} item(s)?").format(count=len(items)),
                ok_text=tr("Restore"),
                rows=[(icon, label, "") for _t, _id, _it, _l, icon, label in items]):
            return
        restored = failed = 0
        for item_type, record_id, item, listing, _icon, _label in items:
            try:
                ok = (self.db_adapter.restore_word(record_id) if item_type == "words"
                      else self.db_adapter.restore_text(record_id))
                if ok:
                    listing.takeItem(listing.row(item))
                    restored += 1
                else:
                    failed += 1
            except Exception as exc:
                logging.error(f"Error restoring {item_type} {record_id}: {exc}")
                failed += 1
        self._refresh_empty_state()
        if restored and self.on_restored:
            self.on_restored()
        msg = tr("Restored {count} item(s).").format(count=restored)
        if failed:
            msg += " " + tr("{n} failed.").format(n=failed)
        QMessageBox.information(self, tr("Restore"), msg)

    def delete_selected(self):
        items = self._selected()
        if not items:
            QMessageBox.information(self, tr("Bin"), tr("Select item(s) to delete permanently."))
            return
        if not confirm(
                self, tr("Permanent Delete"),
                tr("Permanently delete {count} item(s)? This cannot be undone.").format(count=len(items)),
                ok_text=tr("Delete Permanently"), danger=True,
                rows=[(icon, label, "") for _t, _id, _it, _l, icon, label in items]):
            return
        deleted = failed = 0
        for item_type, record_id, item, listing, _icon, _label in items:
            try:
                ok = self.db_adapter.delete_binned_item(item_type, record_id)
                if ok:
                    listing.takeItem(listing.row(item))
                    deleted += 1
                else:
                    failed += 1
            except Exception as exc:
                logging.error(f"Error permanently deleting {item_type} {record_id}: {exc}")
                failed += 1
        self._refresh_empty_state()
        msg = tr("Permanently deleted {count} item(s).").format(count=deleted)
        if failed:
            msg += " " + tr("{n} failed.").format(n=failed)
        QMessageBox.information(self, tr("Delete"), msg)

    def _refresh_empty_state(self):
        """Re-toggle list/empty-label visibility after rows are removed in place."""
        for listing in (self.words_list, self.texts_list):
            has_items = listing.count() > 0
            listing.setVisible(has_items)
            listing._empty_label.setVisible(not has_items)

    def manual_cleanup(self):
        settings = load_settings()
        grace_days = get_int(settings, 'cleanup_grace_period_days', 30)
        cloud = self._cloud()
        try:
            local_count = self.db_adapter.count_old_binned_items(grace_days)
            cloud_count = 0
            if cloud:
                cloud_count = (cloud.get_old_soft_deletes_count('words', grace_days)
                               + cloud.get_old_soft_deletes_count('texts', grace_days))
        except Exception as exc:
            QMessageBox.critical(self, tr("Cleanup"), tr("Failed to count old items:\n{error}").format(error=exc))
            return
        total = max(local_count, cloud_count)
        if total == 0:
            QMessageBox.information(self, tr("Cleanup"),
                                    tr("No items older than {n} days found.").format(n=grace_days))
            return
        if QMessageBox.question(
                self, tr("Cleanup"),
                tr("Permanently delete items deleted more than {days} days ago?\n\n"
                   "This cannot be undone!").format(days=grace_days),
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        try:
            removed = self.db_adapter.purge_old_binned_items(grace_days)
            if cloud:
                cloud.cleanup_old_soft_deletes('words', grace_days)
                cloud.cleanup_old_soft_deletes('texts', grace_days)
            QMessageBox.information(
                self, tr("Cleanup"),
                tr("Permanently deleted {count} old item(s).").format(count=removed))
            self.load_data()
        except Exception as exc:
            logging.error(f"Cleanup failed: {exc}")
            QMessageBox.critical(self, tr("Cleanup"), tr("Failed to cleanup:\n{error}").format(error=exc))
