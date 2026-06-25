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

import logging
import sqlite3
import os
from datetime import datetime

from app.core.db import DB_PATH, get_active_db_path

BACKUP_ROOT = 'backups'


def _db_stem(db_path):
    """The bare filename without extension — ``dictionary`` or ``dictionary_<uid>``."""
    return os.path.splitext(os.path.basename(db_path))[0]


def backup_dir_for(db_path=None):
    """Directory that holds restore points for the given (default: active) database.

    The logged-out local store keeps the historical flat ``backups/`` location so
    existing restore points stay visible. Each signed-in account gets its own
    subfolder (``backups/dictionary_<uid>/``) so that, on a device shared by several
    accounts, daily backups (named only by date) never collide or let one account
    restore another's data."""
    db_path = db_path or get_active_db_path()
    if _db_stem(db_path) == _db_stem(DB_PATH):
        return BACKUP_ROOT
    return os.path.join(BACKUP_ROOT, _db_stem(db_path))


def backup_database(db_path=None):
    """Snapshot the active (or given) database into today's restore point."""
    db_path = db_path or get_active_db_path()

    backup_dir = backup_dir_for(db_path)
    os.makedirs(backup_dir, exist_ok=True)  # Create directory if it does not exist

    # Get today's date as a string
    date_str = datetime.now().strftime('%Y-%m-%d')

    # Construct the file path with the date included
    backup_file_path = os.path.join(backup_dir, f'dictionary_backup_{date_str}.db')

    # Connect to the original and backup database files
    conn = sqlite3.connect(db_path)
    backup_conn = sqlite3.connect(backup_file_path)

    # Perform the backup
    with backup_conn:
        conn.backup(backup_conn)

    # Close the connection
    backup_conn.close()
    conn.close()


def manage_backups(backup_root):
    """Prune old restore points down to one-per-month + the last 10 this month.

    Applies to the shared root (the local store's backups) and to every per-account
    subfolder, so account restore points are pruned the same way and don't pile up."""
    _prune_dir(backup_root)
    try:
        for entry in os.listdir(backup_root):
            sub = os.path.join(backup_root, entry)
            if os.path.isdir(sub):
                _prune_dir(sub)
    except OSError as exc:
        logging.error(f"Could not enumerate backup folders in {backup_root}: {exc}")


def _prune_dir(backup_dir):
    current_month = datetime.now().strftime('%Y-%m')
    backups = []

    for filename in os.listdir(backup_dir):
        if filename.startswith('dictionary_backup_') and filename.endswith('.db'):
            date_str = filename[18:-3]  # Extract date from filename
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                backups.append((date, filename))
            except ValueError:
                logging.error(f"Invalid date format in filename: {filename}")

    # Sort backups by date (oldest first)
    backups.sort()

    # Keep track of months for which we've already kept a backup
    months_kept = set()

    # Keep track of backups for the current month
    current_month_backups = []

    for date, filename in backups:
        file_month = date.strftime('%Y-%m')

        if file_month == current_month:
            # Current month: Add to current_month_backups list
            current_month_backups.append((date, filename))
        elif file_month not in months_kept:
            # Other months: Keep one backup per month
            months_kept.add(file_month)
        else:
            # Remove extra backups from other months
            os.remove(os.path.join(backup_dir, filename))

    # Remove older backups from the current month if there are more than 10
    if len(current_month_backups) > 10:
        for _date, filename in current_month_backups[:-10]:  # Keep last 10
            os.remove(os.path.join(backup_dir, filename))
