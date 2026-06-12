"""Settings dialog. Persists to settings.cfg (and API keys to .env)."""
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QDialog, QDialogButtonBox, QDoubleSpinBox,
    QFileDialog, QFormLayout, QGroupBox, QHBoxLayout, QKeySequenceEdit,
    QLabel, QLineEdit, QMessageBox, QPushButton, QScrollArea, QSpinBox,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget,
)

from app.config import get_bool, get_float, get_int, load_settings, save_settings
from app.system.autostart import get_autostart_enabled, set_autostart


def _read_env():
    env = {}
    if os.path.exists('.env'):
        with open('.env', encoding='utf-8') as fh:
            for line in fh:
                line = line.strip()
                if line and '=' in line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    env[key.strip()] = value.strip()
    return env


def _write_env(updates):
    env = _read_env()
    env.update(updates)
    with open('.env', 'w', encoding='utf-8') as fh:
        for key, value in env.items():
            fh.write(f"{key}={value}\n")
    for key, value in updates.items():
        os.environ[key] = value


def _scrollable(widget):
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setFrameShape(QScrollArea.NoFrame)
    scroll.setWidget(widget)
    return scroll


class SettingsDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setMinimumSize(720, 560)
        self.settings = load_settings()
        self.env = _read_env()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 12)

        self.tabs = QTabWidget()
        self.tabs.addTab(self._appearance_tab(), "Appearance")
        self.tabs.addTab(self._audio_tab(), "Audio")
        self.tabs.addTab(self._export_tab(), "Export")
        self.tabs.addTab(self._import_tab(), "Import")
        self.tabs.addTab(self._apis_tab(), "APIs")
        self.tabs.addTab(self._system_tab(), "System")
        layout.addWidget(self.tabs, 1)

        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.save)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # ----------------------------------------------------------- helpers

    def _line(self, key, width=None):
        edit = QLineEdit(str(self.settings.get(key, "")))
        if width:
            edit.setMaximumWidth(width)
        setattr(self, f"w_{key}", edit)
        return edit

    @staticmethod
    def _secret(edit):
        """Mask a line edit (API keys) and add an eye toggle to reveal it."""
        from app.ui import icons, theme
        dim = theme.current_colors()["text_dim"]
        edit.setEchoMode(QLineEdit.Password)
        action = edit.addAction(icons.icon("eye", dim, 16),
                                QLineEdit.TrailingPosition)
        action.setToolTip("Show / hide")

        def toggle():
            hidden = edit.echoMode() == QLineEdit.Password
            edit.setEchoMode(QLineEdit.Normal if hidden else QLineEdit.Password)
            action.setIcon(icons.icon("eye-off" if hidden else "eye", dim, 16))

        action.triggered.connect(toggle)
        return edit

    def _spin(self, key, lo, hi, default=0):
        spin = QSpinBox()
        spin.setRange(lo, hi)
        spin.setValue(get_int(self.settings, key, default))
        setattr(self, f"w_{key}", spin)
        return spin

    def _dspin(self, key, lo, hi, default=0.0, step=0.1):
        spin = QDoubleSpinBox()
        spin.setRange(lo, hi)
        spin.setSingleStep(step)
        spin.setValue(get_float(self.settings, key, default))
        setattr(self, f"w_{key}", spin)
        return spin

    def _check(self, key, default=False):
        box = QCheckBox()
        box.setChecked(get_bool(self.settings, key, default))
        setattr(self, f"w_{key}", box)
        return box

    def _combo(self, key, values, default=None):
        combo = QComboBox()
        combo.addItems(values)
        current = str(self.settings.get(key, default or values[0]))
        if combo.findText(current) >= 0:
            combo.setCurrentText(current)
        setattr(self, f"w_{key}", combo)
        return combo

    def _ai_provider_page(self, prefix, key_label, key_edit, note_html, extra_rows=()):
        """One provider's settings page: API key + Definitions/Texts groups."""
        page = QWidget()
        form = QFormLayout(page)
        form.setContentsMargins(18, 18, 18, 18)
        form.addRow(key_label, key_edit)
        note = QLabel(note_html)
        note.setOpenExternalLinks(True)
        note.setObjectName("dimLabel")
        note.setWordWrap(True)
        form.addRow(note)
        for label, widget in extra_rows:
            form.addRow(label, widget)
        for title, task in (("Definitions", prefix), ("Generated Texts", f"{prefix}_texts")):
            group = QGroupBox(title)
            g_form = QFormLayout(group)
            g_form.addRow("Model", self._line(f"{task}_model", 220))
            g_form.addRow("Max tokens", self._spin(f"{task}_max_tokens", 16, 8000, 400))
            g_form.addRow("Temperature", self._dspin(f"{task}_temperature", 0, 2, 0.5))
            content = QTextEdit(str(self.settings.get(f"{task}_content", "")))
            content.setMaximumHeight(90)
            setattr(self, f"w_{task}_content", content)
            g_form.addRow("Prompt template", content)
            form.addRow(group)
        return _scrollable(page)

    # -------------------------------------------------------------- tabs

    def _appearance_tab(self):
        from app.ui.theme import TABLE_DENSITY, TABLE_DENSITY_DEFAULT
        widget = QWidget()
        form = QFormLayout(widget)
        form.setContentsMargins(18, 18, 18, 18)
        form.addRow("Appearance mode", self._combo("appearance_mode", ["System", "Light", "Dark"]))
        form.addRow("Widget scaling", self._dspin("widget_scaling", 0.5, 3.0, 1.0))
        self.settings.setdefault("table_density", TABLE_DENSITY_DEFAULT)
        form.addRow("Table size", self._combo("table_density", list(TABLE_DENSITY.keys()), TABLE_DENSITY_DEFAULT))
        return _scrollable(widget)

    def _export_tab(self):
        tabs = QTabWidget()
        tabs.setDocumentMode(True)

        # Excel / CSV
        excel = QWidget()
        form = QFormLayout(excel)
        form.setContentsMargins(18, 18, 18, 18)
        form.addRow("Data format", self._combo("excel_format", ["Excel", "CSV"]))
        form.addRow("CSV delimiter", self._line("csv_delimiter", 80))
        form.addRow("Sheet name", self._line("sheet_name", 160))
        form.addRow("Start row", self._spin("start_row", 0, 100))
        form.addRow("Start column", self._spin("start_column", 0, 100))
        form.addRow("Excluded columns", self._line("exclude_columns_excel"))
        form.addRow("Alternate row color", self._line("alternate_row_color", 120))
        form.addRow("Auto column width", self._check("auto_column_width", True))
        form.addRow("Freeze header row", self._check("freeze_panes", False))
        tabs.addTab(_scrollable(excel), "Excel / CSV")

        # TXT
        txt = QWidget()
        form = QFormLayout(txt)
        form.setContentsMargins(18, 18, 18, 18)
        form.addRow("Delimiter (\\t = tab)", self._line("txt_delimiter", 80))
        form.addRow("Include header lines", self._check("txt_include_headers", True))
        form.addRow("Header lines", self._line("txt_header_lines"))
        form.addRow("Excluded columns", self._line("exclude_columns_txt"))
        tabs.addTab(_scrollable(txt), "TXT")

        # PDF
        pdf = QWidget()
        form = QFormLayout(pdf)
        form.setContentsMargins(18, 18, 18, 18)
        form.addRow("Page size", self._combo("page_size", ["Letter", "A4"]))
        form.addRow("Font name", self._line("font_name", 200))
        form.addRow("Font size", self._dspin("font_size", 4, 40, 10))
        form.addRow("Leading", self._dspin("leading", 4, 60, 12))
        form.addRow("Alignment", self._combo("alignment", ["LEFT", "CENTER", "RIGHT"]))
        margins = QHBoxLayout()
        for key in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
            margins.addWidget(self._dspin(key, 0, 100, 10))
        margins_w = QWidget()
        margins_w.setLayout(margins)
        form.addRow("Margins (L/R/T/B)", margins_w)
        widths = QHBoxLayout()
        for i in range(1, 7):
            widths.addWidget(self._dspin(f"col_width_{i}", 0.1, 10, 1.0))
        widths_w = QWidget()
        widths_w.setLayout(widths)
        form.addRow("Column widths (in)", widths_w)
        form.addRow("Header background", self._line("header_bg_color", 120))
        form.addRow("Row background", self._line("bg_color", 120))
        form.addRow("Header text color", self._line("text_color", 120))
        form.addRow("Grid color", self._line("grid_color", 120))
        bg_row = QHBoxLayout()
        bg_row.addWidget(self._line("bg_image"))
        browse = QPushButton("Browse…")
        browse.clicked.connect(self._pick_bg_image)
        bg_row.addWidget(browse)
        bg_w = QWidget()
        bg_w.setLayout(bg_row)
        form.addRow("Background image", bg_w)
        form.addRow("Excluded columns", self._line("exclude_columns"))
        tabs.addTab(_scrollable(pdf), "PDF")

        # Audio export (MP3)
        audio_export = QWidget()
        form = QFormLayout(audio_export)
        form.setContentsMargins(18, 18, 18, 18)
        form.addRow("Pause between words (s)", self._dspin("pause_duration", 0, 10, 0.5))
        form.addRow("Repeats per pair", self._spin("number_of_repeats", 1, 10, 1))
        form.addRow("Concurrent workers", self._spin("max_concurrent_workers", 1, 16, 2))
        form.addRow("Requests per second", self._spin("requests_per_sec", 1, 50, 5))
        note = QLabel("Used only when exporting words to an MP3 file. "
                      "The voice itself is configured in the Audio tab.")
        note.setObjectName("dimLabel")
        note.setWordWrap(True)
        form.addRow(note)
        tabs.addTab(_scrollable(audio_export), "Audio (MP3)")

        return tabs

    def _audio_tab(self):
        """Text-to-speech settings (used by Read Aloud and MP3 export alike)."""
        audio = QWidget()
        form = QFormLayout(audio)
        form.setContentsMargins(18, 18, 18, 18)
        form.addRow("TTS provider", self._combo("tts_provider", ["gTTS", "google_cloud_tts"]))
        cred_row = QHBoxLayout()
        cred_row.addWidget(self._line("google_cloud_tts_credentials_path"))
        cred_browse = QPushButton("Browse…")
        cred_browse.clicked.connect(self._pick_credentials)
        cred_row.addWidget(cred_browse)
        cred_w = QWidget()
        cred_w.setLayout(cred_row)
        form.addRow("Google Cloud credentials", cred_w)
        form.addRow("Voice type", self._combo("google_cloud_tts_voice_type", ["standard", "wavenet"]))
        form.addRow("Voice name (optional)", self._line("google_cloud_tts_voice_name"))
        note = QLabel("The voice used everywhere words are spoken: in-app Read Aloud "
                      "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
                      "needs a service-account JSON key (Cloud Console → IAM & Admin → "
                      "Service Accounts → Keys) and billing enabled on the project — "
                      "usage within the free monthly quota is not charged.")
        note.setObjectName("dimLabel")
        note.setWordWrap(True)
        form.addRow(note)
        return _scrollable(audio)

    def _import_tab(self):
        widget = QWidget()
        form = QFormLayout(widget)
        form.setContentsMargins(18, 18, 18, 18)
        form.addRow("Placeholder values", self._line("excel_import_placeholders"))
        form.addRow("Skip placeholder rows", self._check("excel_import_skip_placeholders", True))
        form.addRow("Skip empty rows", self._check("excel_import_skip_empty", True))
        form.addRow("Normalize language pairs", self._check("excel_import_normalize", True))
        return _scrollable(widget)

    def _apis_tab(self):
        tabs = QTabWidget()
        tabs.setDocumentMode(True)

        # DeepL
        deepl = QWidget()
        form = QFormLayout(deepl)
        form.setContentsMargins(18, 18, 18, 18)
        form.addRow("API key", self._secret(self._line("api_key")))
        form.addRow("API URL", self._line("api_url"))
        note = QLabel('Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. '
                      'Use https://api-free.deepl.com/v2/translate for free-tier keys.')
        note.setOpenExternalLinks(True)
        note.setObjectName("dimLabel")
        note.setWordWrap(True)
        form.addRow(note)
        tabs.addTab(_scrollable(deepl), "DeepL")

        # AI (OpenAI / Gemini)
        ai_w = QWidget()
        ai_layout = QVBoxLayout(ai_w)
        ai_layout.setContentsMargins(18, 18, 18, 0)
        selector = QFormLayout()
        self.ai_provider_combo = QComboBox()
        self.ai_provider_combo.addItem("OpenAI (ChatGPT)", "openai")
        self.ai_provider_combo.addItem("Google Gemini", "gemini")
        current = str(self.settings.get("ai_provider", "openai")).strip().lower()
        self.ai_provider_combo.setCurrentIndex(max(self.ai_provider_combo.findData(current), 0))
        selector.addRow("Active provider", self.ai_provider_combo)
        ai_layout.addLayout(selector)

        self.openai_key_edit = self._secret(QLineEdit(self.env.get("OPENAI_API_KEY", "")))
        self.gemini_key_edit = self._secret(QLineEdit(self.env.get("GOOGLE_API_KEY", "")))

        ai_tabs = QTabWidget()
        ai_tabs.setDocumentMode(True)
        ai_tabs.addTab(
            self._ai_provider_page(
                "chatgpt", "OpenAI API key (.env)", self.openai_key_edit,
                'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">'
                'platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini…'),
            "OpenAI")
        ai_tabs.addTab(
            self._ai_provider_page(
                "gemini", "Google API key (.env)", self.gemini_key_edit,
                'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">'
                'aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite…',
                extra_rows=[("Thinking budget (0 = off, -1 = auto)",
                             self._spin("gemini_thinking_budget", -1, 24576, 0))]),
            "Gemini")
        ai_tabs.setCurrentIndex(self.ai_provider_combo.currentIndex())
        self.ai_provider_combo.currentIndexChanged.connect(ai_tabs.setCurrentIndex)
        ai_layout.addWidget(ai_tabs, 1)
        tabs.addTab(ai_w, "AI")

        # Sync
        sync = QWidget()
        form = QFormLayout(sync)
        form.setContentsMargins(18, 18, 18, 18)
        form.addRow("Enable cloud sync", self._check("enable_sync", False))
        self.supabase_url_edit = QLineEdit(self.env.get("SUPABASE_URL", ""))
        form.addRow("Supabase URL (.env)", self.supabase_url_edit)
        self.supabase_key_edit = self._secret(QLineEdit(self.env.get("SUPABASE_KEY", "")))
        form.addRow("Supabase key (.env)", self.supabase_key_edit)
        form.addRow("Bin cleanup grace (days)", self._spin("cleanup_grace_period_days", 1, 365, 30))
        test_btn = QPushButton("Test Connection")
        test_btn.clicked.connect(self._test_supabase)
        form.addRow(test_btn)
        note = QLabel("Restart the app after enabling sync for the first time.")
        note.setObjectName("dimLabel")
        form.addRow(note)
        tabs.addTab(_scrollable(sync), "Sync")

        return tabs

    def _system_tab(self):
        widget = QWidget()
        form = QFormLayout(widget)
        form.setContentsMargins(18, 18, 18, 18)
        self.autostart_check = QCheckBox("Start automatically on login (minimized to tray)")
        self.autostart_check.setChecked(get_autostart_enabled())
        form.addRow(self.autostart_check)
        autostart_note = QLabel("Autostart launches the app with the --minimized flag, so it "
                                "begins hidden in the tray.")
        autostart_note.setObjectName("dimLabel")
        autostart_note.setWordWrap(True)
        form.addRow(autostart_note)

        self.hotkey_edit = QKeySequenceEdit(
            QKeySequence(self.settings.get("hotkey", "Ctrl+Shift+V")))
        try:
            self.hotkey_edit.setMaximumSequenceLength(1)
            self.hotkey_edit.setClearButtonEnabled(True)
        except AttributeError:  # Qt < 6.4/6.5
            pass
        form.addRow("Add Word hotkey (global)", self.hotkey_edit)
        hotkey_note = QLabel("Click the field and press the desired key combination — it opens "
                             "'Add Word' with the clipboard content from anywhere. "
                             "Leave empty to disable.")
        hotkey_note.setObjectName("dimLabel")
        hotkey_note.setWordWrap(True)
        form.addRow(hotkey_note)
        return _scrollable(widget)

    # ----------------------------------------------------------- actions

    def _pick_bg_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Background Image", "",
                                              "Images (*.png *.jpg *.jpeg)")
        if path:
            self.w_bg_image.setText(path)

    def _pick_credentials(self):
        path, _ = QFileDialog.getOpenFileName(self, "Google Cloud Credentials", "",
                                              "JSON files (*.json)")
        if path:
            self.w_google_cloud_tts_credentials_path.setText(path)

    def _test_supabase(self):
        _write_env({
            "SUPABASE_URL": self.supabase_url_edit.text().strip(),
            "SUPABASE_KEY": self.supabase_key_edit.text().strip(),
        })
        try:
            from app.core.supabase_client import SupabaseClient
            client = SupabaseClient()
            if client.is_connected():
                QMessageBox.information(self, "Supabase", "Connection successful! ✅")
            else:
                QMessageBox.warning(self, "Supabase",
                                    "Could not connect. Check the URL/key and your internet connection.")
        except Exception as exc:
            QMessageBox.critical(self, "Supabase", f"Connection test failed:\n{exc}")

    def save(self):
        updated = dict(self.settings)
        for key in list(updated.keys()):
            widget = getattr(self, f"w_{key}", None)
            if widget is None:
                continue
            if isinstance(widget, QLineEdit):
                updated[key] = widget.text()
            elif isinstance(widget, QTextEdit):
                updated[key] = widget.toPlainText().replace("\n", "\\n")
            elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                updated[key] = str(widget.value())
            elif isinstance(widget, QCheckBox):
                updated[key] = "True" if widget.isChecked() else "False"
            elif isinstance(widget, QComboBox):
                updated[key] = widget.currentText()

        seq = self.hotkey_edit.keySequence().toString(QKeySequence.PortableText)
        updated["hotkey"] = seq.split(", ")[0]  # first chord only

        updated["ai_provider"] = self.ai_provider_combo.currentData()

        save_settings(updated)

        env_updates = {}
        if self.openai_key_edit.text().strip() != self.env.get("OPENAI_API_KEY", ""):
            env_updates["OPENAI_API_KEY"] = self.openai_key_edit.text().strip()
        if self.gemini_key_edit.text().strip() != self.env.get("GOOGLE_API_KEY", ""):
            env_updates["GOOGLE_API_KEY"] = self.gemini_key_edit.text().strip()
        if self.supabase_url_edit.text().strip() != self.env.get("SUPABASE_URL", ""):
            env_updates["SUPABASE_URL"] = self.supabase_url_edit.text().strip()
        if self.supabase_key_edit.text().strip() != self.env.get("SUPABASE_KEY", ""):
            env_updates["SUPABASE_KEY"] = self.supabase_key_edit.text().strip()
        if env_updates:
            _write_env(env_updates)
            if "OPENAI_API_KEY" in env_updates or "GOOGLE_API_KEY" in env_updates:
                from app.core import ai
                ai.reset_clients()

        try:
            set_autostart(self.autostart_check.isChecked())
        except Exception as exc:
            QMessageBox.warning(self, "Autostart", f"Could not update autostart entry:\n{exc}")

        from app.core.audio import google_cloud_tts_problem
        problem = google_cloud_tts_problem()
        if problem:
            QMessageBox.warning(self, "Google Cloud TTS",
                                f"Google Cloud TTS is selected but {problem}\n\n"
                                f"Audio will fall back to gTTS until this is fixed.")

        self.accept()
