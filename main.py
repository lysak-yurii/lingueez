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

"""Lingueez — modern edition. Entry point."""
import logging
import os
import sys


def _setup_paths():
    """Run from the project directory so relative data files resolve."""
    if getattr(sys, 'frozen', False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base)
    if base not in sys.path:
        sys.path.insert(0, base)


def _setup_logging():
    logging.basicConfig(
        filename='app.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
    )
    # Native-crash stack traces land in crash.log (segfaults bypass app.log)
    import faulthandler
    global _crash_log
    _crash_log = open('crash.log', 'a')
    faulthandler.enable(file=_crash_log)


def main():
    _setup_paths()
    _setup_logging()

    from app.version import APP_ID, APP_NAME, APP_VERSION
    logging.info("The application is launched.")
    logging.info(f"Application version: {APP_VERSION}")

    from PySide6.QtCore import QLockFile, Qt
    from PySide6.QtGui import QIcon
    from PySide6.QtWidgets import QApplication, QMessageBox

    start_hidden = "--minimized" in sys.argv

    app = QApplication(sys.argv)
    # applicationName becomes the X11 WM_CLASS — must match StartupWMClass
    # in the installed .desktop file for proper dock/taskbar association
    app.setApplicationName(APP_ID)
    app.setApplicationDisplayName(APP_NAME)
    app.setDesktopFileName(APP_ID)
    app.setWindowIcon(QIcon("icon.png"))
    app.setQuitOnLastWindowClosed(False)  # we live in the tray

    # Single instance guard (stale locks are released automatically)
    lock = QLockFile(os.path.join(os.getcwd(), "app.lock"))
    lock.setStaleLockTime(0)
    if not lock.tryLock(100):
        QMessageBox.warning(None, APP_NAME, f"{APP_NAME} is already running.")
        return 0

    from app.config import get_float, load_settings
    from app.core.backup_management import manage_backups
    from app.core.db import initialize_database
    from app.ui import theme
    from app.ui.main_window import MainWindow

    settings = load_settings()

    os.makedirs('backups', exist_ok=True)
    try:
        manage_backups('backups')
    except Exception as exc:
        logging.error(f"Backup management failed: {exc}")

    initialize_database()

    theme.apply_theme(app,
                      settings.get("appearance_mode", "System"),
                      get_float(settings, "widget_scaling", 1.0))

    window = MainWindow(settings, start_hidden=start_hidden)
    if not start_hidden:
        window.show()

    rc = app.exec()

    # Give background workers (sync, TTS) a moment to wind down cleanly
    from PySide6.QtCore import QThreadPool
    QThreadPool.globalInstance().waitForDone(3000)

    lock.unlock()
    return rc


if __name__ == "__main__":
    sys.exit(main())
