"""Excel-import flow: analyze in background, confirm, apply, report."""
import logging
import os

from PySide6.QtWidgets import QDialog, QDialogButtonBox, QFileDialog, QLabel, QListWidget, QVBoxLayout

from app.config import load_settings
from app.core.backup_management import backup_database
from app.core.importer import analyze_excel_import, apply_additions, apply_updates, reset_sqlite_sequence
from app.ui.dialogs.log_window import LogWindow
from app.ui.workers import run_in_thread


class ItemsConfirmDialog(QDialog):
    def __init__(self, parent, title, message, items):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumSize(520, 420)
        layout = QVBoxLayout(self)
        label = QLabel(message)
        label.setWordWrap(True)
        layout.addWidget(label)
        listing = QListWidget()
        listing.addItems(items)
        layout.addWidget(listing, 1)
        buttons = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        buttons.button(QDialogButtonBox.Yes).clicked.connect(self.accept)
        buttons.button(QDialogButtonBox.No).clicked.connect(self.reject)
        layout.addWidget(buttons)


class ImportExcelFlow:
    def __init__(self, main_window, db_adapter):
        self.main = main_window
        self.db_adapter = db_adapter
        self.log_window = None

    def _log(self, message, level='info'):
        if self.log_window is not None:
            self.log_window.log_message(message, level)
        logging.info(message)

    def run(self):
        path, _ = QFileDialog.getOpenFileName(self.main, "Import Excel", "",
                                              "Excel files (*.xlsx)")
        if not path:
            return

        self.log_window = LogWindow(self.main, title="Import Log")
        self.log_window.show()
        self._log(f"Selected file: {os.path.basename(path)}")

        settings = load_settings()

        def work():
            return analyze_excel_import(path, settings, log=self._log)

        run_in_thread(work, on_result=self._on_analyzed,
                      on_error=lambda e: self._log(f"Import failed: {e}", 'error'))

    def _on_analyzed(self, result):
        if result is None:
            self._log("Could not read the Excel file.", 'error')
            return

        added = updated = 0

        items_to_add = result['items_to_add']
        if items_to_add:
            labels = [f"{i['Language1']}:  {i['Word1']}   --   {i['Language2']}:  {i['Word2']}"
                      for i in items_to_add]
            dialog = ItemsConfirmDialog(
                self.main, "Add New Items",
                f"The following {len(items_to_add)} items are new and will be added:", labels)
            if dialog.exec():
                try:
                    self.main._sync_before_db_operation()
                    added = apply_additions(self.db_adapter, items_to_add, log=self._log)
                except Exception as exc:
                    self._log(f"Error adding new items: {exc}", 'error')
            else:
                self._log("No new items were added.", 'warning')
        else:
            self._log("No new items found.")

        items_to_update = result['items_to_update']
        if items_to_update:
            labels = [f"{i['Language1']}:  {i['Word1']}   --   {i['Language2']}:  {i['Word2']}"
                      for i in items_to_update]
            dialog = ItemsConfirmDialog(
                self.main, "Update Existing Items",
                f"The following {len(items_to_update)} items exist with different languages "
                "and will be updated:", labels)
            if dialog.exec():
                try:
                    updated = apply_updates(self.db_adapter, items_to_update, log=self._log)
                except Exception as exc:
                    self._log(f"Error updating items: {exc}", 'error')
            else:
                self._log("No existing items were updated.", 'warning')
        else:
            self._log("No items found to update.")

        self._log("\nImport Summary:", 'success')
        self._log(f"New items found: {len(items_to_add)}, added: {added}", 'new')
        self._log(f"Items to update: {len(items_to_update)}, updated: {updated}", 'new')
        self._log(f"Skipped (placeholders): {len(result['skipped_placeholders'])}", 'warning')
        self._log(f"Skipped (empty): {len(result['skipped_empty'])}", 'warning')
        self._log(f"Skipped (invalid): {len(result['skipped_invalid'])}", 'warning')
        self._log(f"Skipped (duplicates): {len(result['skipped_duplicates'])}", 'warning')

        try:
            reset_sqlite_sequence()
            backup_database()
            self._log("Database backed up.", 'info')
        except Exception as exc:
            self._log(f"Error during backup: {exc}", 'error')

        self.main.load_data()
        self._log("Import finished.", 'success')
