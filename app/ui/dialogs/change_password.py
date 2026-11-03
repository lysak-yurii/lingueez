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
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Change the signed-in account's password."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton

from app.core.auth_manager import get_auth_manager
from app.i18n import tr
from app.ui.dialogs.base import FramelessDialog
from app.ui.workers import run_in_thread

MIN_PASSWORD = 6


class ChangePasswordDialog(FramelessDialog):
    """Current, new and confirmed password; accepts once the server took it."""

    def __init__(self, parent=None):
        super().__init__(parent, title=tr("Change password"))
        self.setMinimumWidth(380)
        self.current = self._field(tr("Current password"))
        self.new = self._field(tr("New password"))
        self.confirm = self._field(tr("Confirm new password"))
        self.status = QLabel("")
        self.status.setWordWrap(True)
        self.status.setStyleSheet(f"color: {self.colors['danger']}; background: transparent;")
        self.status.hide()
        self.content_layout.addWidget(self.status)

        row = QHBoxLayout()
        row.addStretch(1)
        cancel = QPushButton(tr("Cancel"))
        cancel.setCursor(Qt.PointingHandCursor)
        cancel.clicked.connect(self.reject)
        row.addWidget(cancel)
        self.save = QPushButton(tr("Change password"), objectName="primaryButton")
        self.save.setCursor(Qt.PointingHandCursor)
        self.save.setDefault(True)
        self.save.clicked.connect(self._submit)
        row.addWidget(self.save)
        self.content_layout.addLayout(row)
        self.current.setFocus()

    def _field(self, placeholder):
        edit = QLineEdit()
        edit.setEchoMode(QLineEdit.Password)
        edit.setPlaceholderText(placeholder)
        edit.returnPressed.connect(self._submit)
        self.content_layout.addWidget(edit)
        return edit

    def _show(self, text):
        self.status.setText(text)
        self.status.setVisible(bool(text))

    def _submit(self):
        current, new = self.current.text(), self.new.text()
        if not current or not new:
            return self._show(tr("Enter your current password and a new password."))
        if new != self.confirm.text():
            return self._show(tr("Passwords don't match."))
        if len(new) < MIN_PASSWORD:
            return self._show(tr("Your password is too short — use at least 6 characters."))
        if new == current:
            return self._show(tr("New password must be different from the current one."))
        self._show("")
        self.save.setEnabled(False)
        run_in_thread(get_auth_manager().change_password, current, new,
                      on_result=self._done, on_error=self._failed)

    def _done(self, result):
        ok, err = result
        if ok:
            self.accept()
        else:
            self._failed(err)

    def _failed(self, message):
        self.save.setEnabled(True)
        self._show(message or tr("Something went wrong."))
