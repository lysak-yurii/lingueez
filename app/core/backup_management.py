import logging
import sqlite3
import os
from datetime import datetime


def backup_database():
    # Ensure the "database" folder exists
    backup_dir = 'backups'
    os.makedirs(backup_dir, exist_ok=True)  # Create directory if it does not exist

    # Get today's date as a string
    date_str = datetime.now().strftime('%Y-%m-%d')

    # Construct the file path with the date included
    backup_file_path = os.path.join(backup_dir, f'dictionary_backup_{date_str}.db')

    # Connect to the original and backup database files
    conn = sqlite3.connect('dictionary.db')
    backup_conn = sqlite3.connect(backup_file_path)

    # Perform the backup
    with backup_conn:
        conn.backup(backup_conn)

    # Close the connection
    backup_conn.close()
    conn.close()


def manage_backups(backup_dir):
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
        for date, filename in current_month_backups[:-10]:  # Keep last 10
            os.remove(os.path.join(backup_dir, filename))
