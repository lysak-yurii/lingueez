"""Texts page: master-detail browser/reader embedded in the main window.

Left: filterable, sortable list of saved texts rendered as cards.
Right: reader card with inline title editing, TTS, save and delete.
"""
import logging

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QColor, QFont, QFontMetrics, QPainter
from PySide6.QtWidgets import (
    QAbstractItemView, QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMessageBox, QPushButton, QSplitter,
    QStackedLayout, QStyle, QStyledItemDelegate, QTextEdit, QVBoxLayout,
    QWidget,
)

from app.core.audio import lang_codes, read_words_list, stop_playback
from app.core.backup_management import backup_database
from app.ui import icons
from app.ui.animations import fade_swap
from app.ui.dialogs.definition import markup_to_html
from app.ui.toast import show_toast
from app.ui.widgets import ElidedLabel
from app.ui.workers import run_in_thread

META_ROLE = Qt.UserRole + 1
SNIPPET_ROLE = Qt.UserRole + 2

SORT_NEWEST = "Newest first"
SORT_OLDEST = "Oldest first"
SORT_TITLE = "Title A–Z"
ALL_LANGUAGES = "All languages"


class TextCardDelegate(QStyledItemDelegate):
    """Paints each text as a card: title, meta line and a one-line snippet."""

    def __init__(self, colors, parent=None):
        super().__init__(parent)
        self._c = colors

    def set_colors(self, colors):
        self._c = colors

    def _fonts(self, base):
        title = QFont(base)
        title.setWeight(QFont.DemiBold)
        small = QFont(base)
        small.setPointSizeF(max(7.0, base.pointSizeF() - 1))
        return title, small

    def sizeHint(self, option, index):
        title_font, small_font = self._fonts(option.font)
        height = (10 + QFontMetrics(title_font).height() + 3
                  + 2 * QFontMetrics(small_font).height() + 2 + 10 + 4)
        return QSize(option.rect.width(), height)

    def paint(self, painter, option, index):
        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)
        rect = option.rect.adjusted(4, 2, -4, -2)
        if option.state & QStyle.State_Selected:
            painter.setBrush(QColor(self._c["selection"]))
        elif option.state & QStyle.State_MouseOver:
            painter.setBrush(QColor(self._c["surface_alt"]))
        else:
            painter.setBrush(Qt.NoBrush)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, 8, 8)

        title_font, small_font = self._fonts(option.font)
        x = rect.x() + 12
        width = rect.width() - 24
        y = rect.y() + 10

        painter.setFont(title_font)
        fm = painter.fontMetrics()
        painter.setPen(QColor(self._c["text"]))
        painter.drawText(x, y + fm.ascent(),
                         fm.elidedText(index.data(Qt.DisplayRole) or "", Qt.ElideRight, width))
        y += fm.height() + 3

        painter.setFont(small_font)
        fm = painter.fontMetrics()
        painter.setPen(QColor(self._c["text_dim"]))
        painter.drawText(x, y + fm.ascent(),
                         fm.elidedText(index.data(META_ROLE) or "", Qt.ElideRight, width))
        y += fm.height() + 2
        painter.drawText(x, y + fm.ascent(),
                         fm.elidedText(index.data(SNIPPET_ROLE) or "", Qt.ElideRight, width))
        painter.restore()


class TextsPage(QWidget):
    """Embedded replacement for the old Texts popup dialog."""

    counts_changed = Signal(int, int)  # (shown, total)
    reading_done = Signal()
    tts_started = Signal()  # lets the main window stop its word player

    def __init__(self, db_adapter, colors, parent=None):
        super().__init__(parent)
        self.db_adapter = db_adapter
        self._colors = colors
        self.texts = []        # everything fetched from the database
        self.filtered = []     # what the list currently shows
        self.current = None    # text dict loaded in the reader
        self.search_query = ""
        self.is_reading = False
        self._loading = False  # populating editors programmatically
        self._dirty = False
        self._loaded_once = False
        self._themed = []      # (button, icon name, color key, size)

        self.reading_done.connect(self._tts_finished)
        self._build_ui()

    # ------------------------------------------------------------------ UI

    def _icon_button(self, name, color_key, tooltip, slot, size=18):
        btn = QPushButton(objectName="iconButton")
        btn.setIcon(icons.icon(name, self._colors[color_key], size))
        btn.setIconSize(QSize(size, size))
        btn.setToolTip(tooltip)
        btn.setCursor(Qt.PointingHandCursor)
        btn.clicked.connect(slot)
        self._themed.append((btn, name, color_key, size))
        return btn

    def _build_ui(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(16, 12, 16, 8)

        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(8)
        splitter.setChildrenCollapsible(False)

        # ---------- left: filters + list ----------
        left = QWidget()
        ll = QVBoxLayout(left)
        ll.setContentsMargins(0, 0, 0, 0)
        ll.setSpacing(8)

        filter_row = QHBoxLayout()
        filter_row.setSpacing(8)
        self.lang_filter = QComboBox()
        self.lang_filter.setMinimumWidth(120)
        self.lang_filter.addItem(ALL_LANGUAGES)
        self.lang_filter.currentTextChanged.connect(self._refresh_list)
        filter_row.addWidget(self.lang_filter, 1)
        self.sort_combo = QComboBox()
        self.sort_combo.addItems([SORT_NEWEST, SORT_OLDEST, SORT_TITLE])
        self.sort_combo.currentTextChanged.connect(self._refresh_list)
        filter_row.addWidget(self.sort_combo)
        ll.addLayout(filter_row)

        self.listing = QListWidget(objectName="TextsList")
        self.listing.setMouseTracking(True)
        self.listing.viewport().setAttribute(Qt.WA_Hover, True)
        self.listing.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listing.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._delegate = TextCardDelegate(self._colors, self.listing)
        self.listing.setItemDelegate(self._delegate)
        self.listing.currentRowChanged.connect(self._on_row_changed)
        ll.addWidget(self.listing, 1)
        splitter.addWidget(left)

        # ---------- right: empty state / reader card ----------
        right = QWidget()
        self.reader_stack = QStackedLayout(right)

        empty = QWidget()
        ev = QVBoxLayout(empty)
        ev.addStretch(1)
        self.empty_icon = QLabel(alignment=Qt.AlignCenter)
        self.empty_icon.setPixmap(icons.pixmap("file-text", self._colors["text_dim"], 44))
        ev.addWidget(self.empty_icon)
        self.empty_title = QLabel("No texts yet", objectName="EmptyTitle",
                                  alignment=Qt.AlignCenter)
        ev.addWidget(self.empty_title)
        self.empty_sub = QLabel("", objectName="dimLabel", alignment=Qt.AlignCenter)
        self.empty_sub.setWordWrap(True)
        ev.addWidget(self.empty_sub)
        ev.addStretch(2)
        self.reader_stack.addWidget(empty)

        card = QFrame(objectName="ReaderCard")
        cv = QVBoxLayout(card)
        cv.setContentsMargins(18, 12, 18, 12)
        cv.setSpacing(6)

        top = QHBoxLayout()
        top.setSpacing(4)
        self.title_edit = QLineEdit(objectName="ReaderTitle")
        self.title_edit.setPlaceholderText("Title")
        self.title_edit.textEdited.connect(self._mark_dirty)
        top.addWidget(self.title_edit, 1)
        self.tts_btn = self._icon_button("volume", "text", "Read aloud", self.toggle_tts)
        top.addWidget(self.tts_btn)
        delete_btn = self._icon_button("trash", "danger", "Delete text", self.delete_current)
        top.addWidget(delete_btn)
        cv.addLayout(top)

        meta = QHBoxLayout()
        meta.setSpacing(10)
        self.language_combo = QComboBox()
        self.language_combo.setEditable(True)
        self.language_combo.addItems(sorted(lang_codes.keys()))
        self.language_combo.editTextChanged.connect(self._mark_dirty)
        meta.addWidget(self.language_combo)
        self.created_label = QLabel("", objectName="dimLabel")
        meta.addWidget(self.created_label)
        meta.addStretch(1)
        cv.addLayout(meta)

        self.words_line = ElidedLabel()
        self.words_line.setObjectName("dimLabel")
        cv.addWidget(self.words_line)

        self.body = QTextEdit(objectName="ReaderBody")
        self.body.textChanged.connect(self._mark_dirty)
        cv.addWidget(self.body, 1)

        bottom = QHBoxLayout()
        bottom.setSpacing(4)
        self.prev_btn = self._icon_button("chevron-left", "text", "Previous text",
                                          lambda: self._select_relative(-1))
        bottom.addWidget(self.prev_btn)
        self.page_label = QLabel("", objectName="dimLabel")
        bottom.addWidget(self.page_label)
        self.next_btn = self._icon_button("chevron-right", "text", "Next text",
                                          lambda: self._select_relative(1))
        bottom.addWidget(self.next_btn)
        bottom.addStretch(1)
        self.save_btn = QPushButton("Save Changes", objectName="primaryButton")
        self.save_btn.setEnabled(False)
        self.save_btn.clicked.connect(self.save_current)
        bottom.addWidget(self.save_btn)
        cv.addLayout(bottom)

        self.reader_card = card
        self.reader_stack.addWidget(card)

        splitter.addWidget(right)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)
        splitter.setSizes([300, 620])
        root.addWidget(splitter)

    def refresh_theme(self, colors):
        """Re-tint icons and delegate colors after a theme change."""
        self._colors = colors
        self._delegate.set_colors(colors)
        self.listing.viewport().update()
        for btn, name, color_key, size in self._themed:
            btn.setIcon(icons.icon(name, colors[color_key], size))
        if self.is_reading:
            self.tts_btn.setIcon(icons.icon("stop", colors["danger"], 18))
        self.empty_icon.setPixmap(icons.pixmap("file-text", colors["text_dim"], 44))

    # ---------------------------------------------------------------- data

    def set_search(self, query):
        self.search_query = query or ""
        if self._loaded_once:
            self._refresh_list()

    def load_texts(self, preserve_id=None):
        """(Re)fetch texts from the database and rebuild the list."""
        if preserve_id is None and self.current is not None:
            preserve_id = self.current.get("ID")
        try:
            self.texts = self.db_adapter.get_texts() or []
        except Exception as exc:
            logging.error(f"Failed to load texts: {exc}")
            self.texts = []
        self._loaded_once = True

        languages = sorted({str(t.get('Language') or '').strip()
                            for t in self.texts if str(t.get('Language') or '').strip()})
        selected = self.lang_filter.currentText()
        self.lang_filter.blockSignals(True)
        self.lang_filter.clear()
        self.lang_filter.addItem(ALL_LANGUAGES)
        self.lang_filter.addItems(languages)
        if selected and self.lang_filter.findText(selected) >= 0:
            self.lang_filter.setCurrentText(selected)
        self.lang_filter.blockSignals(False)

        self._refresh_list(preserve_id=preserve_id)

    def _refresh_list(self, *_, preserve_id=None):
        if preserve_id is None and self.current is not None:
            preserve_id = self.current.get("ID")

        query = self.search_query.strip().lower()
        language = self.lang_filter.currentText()
        items = list(self.texts)
        if language and language != ALL_LANGUAGES:
            items = [t for t in items if str(t.get('Language') or '').strip() == language]
        if query:
            items = [t for t in items if query in str(t.get('Title') or '').lower()
                     or query in str(t.get('Text') or '').lower()
                     or query in str(t.get('Words') or '').lower()]

        sort = self.sort_combo.currentText()
        if sort == SORT_TITLE:
            items.sort(key=lambda t: str(t.get('Title') or '').lower())
        else:
            items.sort(key=lambda t: str(t.get('created_at') or ''),
                       reverse=(sort != SORT_OLDEST))
        self.filtered = items

        self.lang_filter.setProperty("filterActive", language not in (ALL_LANGUAGES, ""))
        self.lang_filter.style().unpolish(self.lang_filter)
        self.lang_filter.style().polish(self.lang_filter)

        self.listing.blockSignals(True)
        self.listing.clear()
        target_row = 0
        for row, text in enumerate(self.filtered):
            title = str(text.get('Title') or '').strip() or "(untitled)"
            lang = str(text.get('Language') or '').strip()
            date = str(text.get('created_at') or '')[:10]
            item = QListWidgetItem(title)
            item.setData(META_ROLE, " · ".join(p for p in (lang, date) if p))
            item.setData(SNIPPET_ROLE, " ".join(str(text.get('Text') or '').split())[:200])
            self.listing.addItem(item)
            if preserve_id is not None and text.get('ID') == preserve_id:
                target_row = row
        self.listing.blockSignals(False)

        self.counts_changed.emit(len(self.filtered), len(self.texts))

        if not self.filtered:
            self.current = None
            self._set_dirty(False)
            if self.texts:
                self.empty_title.setText("No matching texts")
                self.empty_sub.setText("Try a different search or language filter.")
            else:
                self.empty_title.setText("No texts yet")
                self.empty_sub.setText(
                    'Select words in the Words view and use the "Text" action\n'
                    "to generate a study text from them.")
            self.reader_stack.setCurrentIndex(0)
            return

        # setCurrentRow with the same row index would not re-emit, so force
        # a refresh of the reader for the (possibly different) record
        self.listing.setCurrentRow(target_row)
        if self.listing.currentRow() == target_row:
            self._on_row_changed(target_row)

    # -------------------------------------------------------------- reader

    def _on_row_changed(self, row):
        if row < 0 or row >= len(self.filtered):
            return
        text = self.filtered[row]
        if self._dirty and self.current is not None and text is not self.current:
            self._maybe_save_pending()
        self._show_text(text, row)

    def _show_text(self, text, row):
        if self.reader_stack.currentIndex() == 1 and self.current is not None \
                and text is not self.current:
            fade_swap(self.reader_card)
        self.current = text

        self._loading = True
        self.title_edit.setText(str(text.get('Title') or ""))
        self.language_combo.setCurrentText(str(text.get('Language') or "English"))
        created = str(text.get('created_at') or "")[:16].replace("T", " ")
        self.created_label.setText(f"Created {created}" if created else "")
        words = str(text.get('Words') or "").strip()
        self.words_line.set_full_text(f"From words: {words}" if words else "")
        self.words_line.setVisible(bool(words))
        self.body.setHtml(markup_to_html(str(text.get('Text') or "")))
        self._loading = False
        self._set_dirty(False)

        self.page_label.setText(f"{row + 1} / {len(self.filtered)}")
        self.prev_btn.setEnabled(row > 0)
        self.next_btn.setEnabled(row < len(self.filtered) - 1)
        self.reader_stack.setCurrentIndex(1)

    def _select_relative(self, delta):
        row = self.listing.currentRow() + delta
        if 0 <= row < self.listing.count():
            self.listing.setCurrentRow(row)

    # --------------------------------------------------------------- edits

    def _mark_dirty(self, *_):
        if not self._loading and self.current is not None:
            self._set_dirty(True)

    def _set_dirty(self, dirty):
        self._dirty = dirty
        self.save_btn.setEnabled(dirty and self.current is not None)

    def _editor_data(self):
        return {
            'Title': self.title_edit.text().strip(),
            'Language': self.language_combo.currentText().strip(),
            'Text': self.body.toPlainText().strip(),
        }

    def _write_text(self, text, data):
        try:
            self.db_adapter.update_text(int(text['ID']), data)
            backup_database()
            text.update(data)
            return True
        except Exception as exc:
            logging.error(f"Failed to save text: {exc}")
            QMessageBox.critical(self, "Error", f"Failed to save text:\n{exc}")
            return False

    def _maybe_save_pending(self):
        """Offer to keep edits when navigating away from a modified text."""
        data = self._editor_data()
        previous = self.current
        self._set_dirty(False)
        title = str(previous.get('Title') or '(untitled)')
        if QMessageBox.question(
                self, "Unsaved changes", f"Save changes to '{title}'?",
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        self._write_text(previous, data)

    def save_current(self):
        if self.current is None:
            return
        if self._write_text(self.current, self._editor_data()):
            self._set_dirty(False)
            show_toast(self.window(), "Texts", "Changes saved.", "success")
            self.load_texts(preserve_id=self.current.get('ID'))

    def delete_current(self):
        if self.current is None:
            return
        title = str(self.current.get('Title') or "(untitled)")
        if QMessageBox.question(self, "Delete Text", f"Delete '{title}'?",
                                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        row = self.listing.currentRow()
        neighbor = None
        if 0 <= row < len(self.filtered) - 1:
            neighbor = self.filtered[row + 1].get('ID')
        elif row > 0:
            neighbor = self.filtered[row - 1].get('ID')
        try:
            self.db_adapter.delete_text(int(self.current['ID']))
            backup_database()
        except Exception as exc:
            logging.error(f"Failed to delete text: {exc}")
            QMessageBox.critical(self, "Error", f"Failed to delete text:\n{exc}")
            return
        self.current = None
        self._set_dirty(False)
        show_toast(self.window(), "Texts", f"'{title}' moved to bin.", "success")
        self.load_texts(preserve_id=neighbor)

    # ----------------------------------------------------------------- tts

    def toggle_tts(self):
        if self.is_reading:
            stop_playback()
            self._tts_finished()
            return
        if self.current is None:
            return
        content = self.body.toPlainText().strip()
        language = self.language_combo.currentText()
        if not content or language not in lang_codes:
            return

        self.tts_started.emit()
        self.is_reading = True
        self.tts_btn.setIcon(icons.icon("stop", self._colors["danger"], 18))
        self.tts_btn.setToolTip("Stop reading")

        # Read the text in chunks (sentences grouped to ~400 chars)
        chunks, buf = [], ""
        for sentence in content.replace("\n", " ").split(". "):
            buf += sentence + ". "
            if len(buf) > 400:
                chunks.append(buf)
                buf = ""
        if buf.strip():
            chunks.append(buf)
        pairs = [(chunk, "") for chunk in chunks]
        langs = [(language, language)] * len(pairs)

        run_in_thread(read_words_list, pairs, langs, self.reading_done.emit)

    def _tts_finished(self):
        self.is_reading = False
        self.tts_btn.setIcon(icons.icon("volume", self._colors["text"], 18))
        self.tts_btn.setToolTip("Read aloud")
