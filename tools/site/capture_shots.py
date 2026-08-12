#!/usr/bin/env python3
"""Capture the product screenshots the website uses — every page, both themes.

The shots used to be taken by hand on a real desktop, which is why the old ones
carry wallpaper around the window and why no light-theme set exists at all.
This drives the real MainWindow offscreen instead, so:

* light and dark are framed identically, pixel for pixel;
* the content is the same seeded vocabulary every time, so a re-run after a UI
  change produces a clean diff rather than a different library;
* there is no desktop chrome to crop off.

Everything happens in a throwaway sandbox directory. See
`.claude/skills/verify/SKILL.md` — in particular the three cloud paths that
must be cut before MainWindow is constructed, or a "local" run quietly writes
words to the real server.

    python3 tools/site/capture_shots.py
    python3 tools/site/capture_shots.py --theme Light --page words
    python3 tools/site/capture_shots.py --keep-sandbox      # to poke at the DB
"""
from __future__ import annotations

import argparse
import contextlib
import os
import shutil
import sqlite3
import sys
import tempfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "docs" / "assets" / "shots"

# The demo library. Real content beats anything generated: 33 words across all
# four statuses, 4 texts, 1278 listens and a full set of tags.
DUMMY_DB = REPO.parent / "data" / "dictionary_dummy_data.db"
# Set from --db in main(); reset_library() reads it between themes.
DB_SOURCE = DUMMY_DB

# Window width in logical pixels, and how large the app draws its own widgets
# inside it. These two together decide how big the UI *reads* in the shot: a
# wide window at 1.0 scaling makes the app look sparse and its text tiny, which
# is what a screenshot on a large monitor gives you. A narrower window with the
# widgets scaled up is what the app looks like to someone actually using it.
WIN_W = 1160
SCALING = 1.5

# Content width per page, in logical units before widget scaling. A page not
# listed here uses the default window. This is an override, not a floor: some
# pages need more room than the default and one needs less.
#
# texts and stats sit next to each other in the site's showcase rows, so they
# share one width and therefore read at exactly the same scale. 950 is the
# tightest value that satisfies both: texts needs ~900 before its filter combos
# and search box elide their own labels, and stats needs a little more — at
# 1.5x the six KPI cards' own size hints add up to 1271px plus margins
# (measured, not guessed — the fixed setMinimumWidth(190) in charts.KpiCard
# stops binding above 1.25x and the caption text takes over), below which the
# sixth card wraps onto a row of its own.
#
# review is the exception that wants *less*: it is one card centred in the
# window, so the default leaves wide empty margins around it.
#
# flashcards used to sit at 700 alongside review, which drew the deck preview
# at three columns and two rows and made the whole page read zoomed-in. Note
# what does *not* scale: _CardGridLayout's min_item_width (250) and
# _PreviewCard.HEIGHT (138) are fixed pixels, while widget_scaling grows the
# type inside them — so a card never gets bigger, its text just crowds it, and
# lowering --scaling would only narrow the window (width is content x scaling)
# and cost a column. Widening the content is the lever that actually works.
#
# 850 is chosen to sit in the middle of the four-column band, not at its edge.
# The grid takes another column every time the preview clears
# n*250 + (n-1)*14 px, which lands the fifth at ~1306 and the fourth at ~1042;
# the showcase width of 950 puts the preview at 1309 and tips into five columns
# by three pixels, which is both too small to read and too fragile to keep — a
# font change would silently drop it back to four. 850 gives 4 x 3.
SHOWCASE_CONTENT = 950
PAGE_CONTENT = {"texts": SHOWCASE_CONTENT, "stats": SHOWCASE_CONTENT,
                "flashcards": 850, "review": 700}
# Height is derived, not chosen: the hero's laptop screen rect is 552x387 SVG
# units (1.4264:1), so a capture at exactly that aspect drops into it with
# nothing cropped and nothing letterboxed.
ASPECT = 552 / 387
SCALE = "2"          # device pixel ratio; 2x keeps the shots crisp when zoomed

THEMES = ("Light", "Dark")
# "review" is last on purpose: it grades cards, which writes SRS state, review
# events and status promotions. Any shot taken after it would show a library
# that had been studied. capture() also reinstalls the library per theme, so
# light and dark both start from the same untouched copy.
PAGES = ("words", "flashcards", "texts", "stats", "review")

# A fixed grade sequence, so the trail across the top of the review shot has the
# same colours every run rather than whatever the deck happened to produce.
REVIEW_GRADES = ("good", "easy", "hard", "good", "good",
                 "good", "easy", "good", "good", "good")

def cut_off_the_cloud():
    """Sever every path that reaches the real server. MUST run before the
    MainWindow is built — see SKILL.md; `is_sync_enabled = False` alone does
    NOT stop DatabaseAdapter's per-word write-through."""
    from app.core import auth_manager, sync_manager
    from app.core.database_adapter import DatabaseAdapter
    from app.ui.main_window import MainWindow

    auth_manager.AuthManager.restore_session = lambda self: auth_manager.RESTORE_NONE
    sync_manager.SyncManager.is_sync_enabled = lambda self: False
    DatabaseAdapter._use_cloud = lambda self: False
    # A fourth, for the shots' sake as much as safety: startup sync would post
    # "Not connected. Check internet or credentials" into the status bar (the
    # repo .env names a custom server, so it gets past the signed-out check) and
    # light the error icon in the title bar. Neither belongs in a product shot.
    MainWindow._run_startup_sync = lambda self: None

    # And silence the app. Revealing a flashcard auto-pronounces it, which
    # plays out of the machine's speakers and fetches the audio from a TTS
    # service — neither belongs in a headless screenshot run. The setting below
    # already turns it off; these stubs make it impossible regardless of what
    # any settings file says.
    from app.core import audio

    audio.speak_word = lambda *a, **k: None
    audio.prefetch_word = lambda *a, **k: None
    audio.synthesize_speech = lambda *a, **k: None
    audio.stop_playback = lambda *a, **k: None
    # The words shot starts a read-aloud so the player bar is in frame. The bar
    # is put up by _start_word_playback before WordPlayer.play() is ever
    # called, so stubbing the player leaves the UI exactly as it looks while
    # reading, with no audio and no TTS reachability probe behind it.
    audio.google_cloud_tts_problem = lambda *a, **k: None

    # The reader's word popup translates whatever is clicked, over the network.
    # The texts shot opens that popup, so the lookup is answered locally from
    # WORD_POPUP below instead of reaching a translation service.
    from app.ui import word_popup

    word_popup.translate = lambda word, target, source=None: (
        WORD_POPUP.get(word, word), source)
    from app.ui.player import WordPlayer

    WordPlayer.play = lambda *a, **k: None


def install_library(src: Path) -> tuple:
    """Put the demo library in place, before initialize_database() runs.

    The dummy DB is a copy, never opened in place — it lives outside the repo
    and nothing here should be able to write to it. initialize_database() then
    adds any table or column the app has gained since it was made (srs_progress
    is missing from it, for one), so an older snapshot still works.
    """
    from app.core.db import get_active_db_path

    dst = Path(get_active_db_path())
    if not src.exists():
        raise SystemExit(
            f"demo library not found at {src}\n"
            "Point DUMMY_DB at a copy, or pass --db /path/to/library.db.")
    # Drop the write-ahead sidecars first. This runs again between themes, and
    # a -wal/-shm pair left over from the previous copy describes a database
    # that no longer exists — SQLite then reads the pair as corruption
    # ("database disk image is malformed") on the very next open.
    for suffix in ("-wal", "-shm"):
        dst.with_name(dst.name + suffix).unlink(missing_ok=True)
    shutil.copy2(src, dst)
    with contextlib.closing(sqlite3.connect(dst)) as conn:
        words = conn.execute("SELECT COUNT(*) FROM words").fetchone()[0]
        texts = conn.execute("SELECT COUNT(*) FROM texts").fetchone()[0]
    return words, texts


# The word the texts shot has open in the reader's popup, and the answer the
# stubbed translator gives for it. "Wiederholung" is the demo article's own
# subject, so the panel says something that belongs to the page it sits on.
POPUP_WORD = "Wiederholung"
WORD_POPUP = {"Wiederholung": "repetition"}

# The dummy library's texts are one or two sentences each — fine as library
# rows, but the reader pane is what the site's "learn from real content"
# section shows, and a single sentence in a full-width pane undersells it.
# So one proper article is added to the sandbox copy (never to the source).
# German, B2, a few paragraphs: long enough to fill the pane and to make the
# point that this is real reading, not a flashcard.
DEMO_TEXT = {
    "title": "Wörter, die bleiben",
    "language": "German",
    "level": "B2",
    "category": "Artikel",
    "body": """Jeder, der eine Sprache lernt, kennt das Gefühl: Ein Wort, das \
gestern noch selbstverständlich war, ist heute verschwunden. Man erinnert sich \
an den Klang, vielleicht an den ersten Buchstaben — aber das Wort selbst bleibt \
außer Reichweite.

Das ist kein Zeichen von Vergesslichkeit, sondern ganz normal. Unser Gedächtnis \
behält nicht alles, sondern das, was es für wichtig hält. Und wichtig ist für \
das Gehirn vor allem das, was regelmäßig wiederkehrt. Ein Wort, das man einmal \
gesehen hat, wirkt wie ein Weg durch hohes Gras: Er ist da, aber nach wenigen \
Tagen wieder zugewachsen.

Der Trick besteht also nicht darin, öfter zu lernen, sondern zum richtigen \
Zeitpunkt zu wiederholen — kurz bevor man ein Wort vergessen würde. Genau dann \
ist die Wiederholung am wertvollsten, und genau dann wird aus dem Trampelpfad \
langsam ein fester Weg.

Deshalb lohnt es sich, Wörter dort zu sammeln, wo man ihnen zum ersten Mal \
begegnet: in einem Artikel, in einem Buch, in einem Gespräch. Ein Wort mit \
Kontext bleibt fast immer länger als eine Vokabel aus einer Liste.""",
}


def add_demo_text(src_had: int) -> None:
    """Insert the reading article into the sandbox library."""
    from app.core.db import get_active_db_path, new_id

    with contextlib.closing(sqlite3.connect(get_active_db_path())) as conn:
        conn.execute(
            "INSERT INTO texts (ID, RowNumber, Title, Text, Language, Category,"
            " Level, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))",
            (new_id(), src_had + 1, DEMO_TEXT["title"], DEMO_TEXT["body"],
             DEMO_TEXT["language"], DEMO_TEXT["category"], DEMO_TEXT["level"]))
        # closing() closes but does not commit — `with connect(...)` used to do
        # that implicitly, so this has to be explicit now.
        conn.commit()


# What the site displays a screenshot at, times two for high-density screens.
# Anything above this is detail no visitor can see, paid for on every load.
WEB_W = 1600


def _downscale(png: Path) -> Path:
    from PIL import Image

    webp = png.with_suffix(".webp")
    with Image.open(png) as img:
        if img.width > WEB_W:
            img = img.resize((WEB_W, round(img.height * WEB_W / img.width)),
                             Image.LANCZOS)
        img.convert("RGB").save(webp, "WEBP", quality=86, method=6)
    return webp


def widen_virtual_screen():
    """Report a screen at least as large as anything we capture.

    The offscreen platform always claims 800x800, whatever the window size, and
    it ignores a size argument. Anything that positions itself against the
    screen then gets clamped into a corner — the reader's word popup lands over
    the text list instead of above the word it belongs to. Reporting a
    realistic screen lets the app's own placement code run exactly as it does
    on a desktop, rather than the harness second-guessing where it should go.
    """
    from PySide6.QtCore import QRect
    from PySide6.QtGui import QScreen

    big = QRect(0, 0, 4096, 4096)
    QScreen.availableGeometry = lambda self: big
    QScreen.geometry = lambda self: big


def grab(window, app):
    """The window, with any open popup drawn onto it.

    WordPopup is Qt.Popup | Qt.FramelessWindowHint, so it is a top-level window
    of its own and window.grab() does not contain it. Grabbing it separately
    and compositing at its offset reproduces exactly what is on screen.
    """
    from PySide6.QtCore import QPoint
    from PySide6.QtGui import QPainter

    shot = window.grab()
    origin = window.mapToGlobal(QPoint(0, 0))
    extras = [w for w in app.topLevelWidgets()
              if w is not window and w.isVisible() and w.width() > 1]
    if not extras:
        return shot
    painter = QPainter(shot)
    for w in extras:
        offset = w.mapToGlobal(QPoint(0, 0)) - origin
        painter.drawPixmap(offset, w.grab())
    painter.end()
    return shot


def open_word_popup(window, app) -> None:
    """Click a word in the reader, so the shot shows the add-to-vocabulary
    panel rather than a page nobody is interacting with."""
    page = window.texts_page
    body = getattr(page, "body", None)
    if body is None:
        return
    text = body.toPlainText()
    start = text.find(POPUP_WORD)
    if start < 0:
        print(f"    [texts] {POPUP_WORD!r} is not in the demo text; no popup",
              flush=True)
        return
    page._show_word_popup(POPUP_WORD, start, start + len(POPUP_WORD))
    pump(app, 1.6)          # the translation arrives on a worker thread


def close_popups(window, app) -> None:
    """Dismiss every top-level popup before moving on.

    grab() deliberately composites any open popup onto the shot, and the texts
    page leaves the word popup up. Nothing closed it, so it was still on screen
    for the next page and the statistics shot came out with the reader's
    "Wiederholung" panel floating over it. Popups are not owned by the page
    that opened them, so the page switch alone will not take them down.
    """
    for w in app.topLevelWidgets():
        if w is not window and w.isVisible():
            w.close()
    pump(app, 0.4)


def pump(app, seconds):
    """Drive the event loop without app.exec()."""
    deadline = time.time() + seconds
    while time.time() < deadline:
        app.processEvents()
        time.sleep(0.01)


def fit_whole_rows(window, app, rounds: int = 4) -> None:
    """Size the window so the deck preview ends exactly on a row boundary.

    The preview is a scroll area of equal-height card rows, so at an arbitrary
    height the last visible row is sliced through the middle — which reads as a
    rendering fault in a screenshot rather than as "there is more below".

    The earlier version simply pulled the window bottom up to the last whole
    row. That worked, but it cost up to a full row of height and left this the
    only shot not at the site's aspect: 1.65 against everyone else's 1.43, which
    showed as a visible jump when the showcase cross-faded between this and the
    review session.

    So instead of only shrinking, this moves to the *nearest* row boundary in
    either direction and then restores the width from the new height, keeping
    the canonical aspect. Changing the width can re-flow the grid and move the
    boundary again, so it iterates to a fixed point — in practice one or two
    rounds.
    """
    page = window.flashcards_page
    for _ in range(rounds):
        cards = [c for c in page._preview_cards if c.isVisible()]
        if not cards:
            return
        viewport = page.preview_scroll.viewport().height()
        bottoms = sorted({c.geometry().bottom() for c in cards})
        target = min(bottoms, key=lambda b: abs(b - viewport))
        delta = target - viewport
        if delta == 0:
            return
        height = max(400, window.height() + delta)
        width = round(height * ASPECT)
        if (width, height) == (window.width(), window.height()):
            return
        window.resize(width, height)
        pump(app, 0.6)
    print(f"    [flashcards] rows did not settle in {rounds} rounds", flush=True)


# Words added per week, oldest week last in the chart's terms — this list runs
# oldest -> current, and the final entry is the current, partial week.
#
# The source library's own dates stop dead two months before today, which left
# the statistics shot with a spike, a flat line, a 0-day streak and 0 added this
# week: all true of that snapshot, and a poor advertisement for a tool whose
# point is steady progress. These counts never decrease, so the series only ever
# climbs, and the last week is level with the one before it rather than dipping
# — the current week is only a day or two old whenever the shot is taken.
WEEK_COUNTS = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# The most recent two weeks are packed onto consecutive days, which is what the
# streak counter reads; older weeks are spread out, which is what a real history
# looks like.
PACKED_WEEKS = 2

# Spread through the waking day so the list does not read as a bulk import.
HOURS = [8, 12, 17, 21, 10, 19, 14]


def _day_offsets(total: int, weekday: int) -> list:
    """Days-ago for each word, newest first, honouring WEEK_COUNTS.

    `weekday` is date.today().weekday(), so the current week is however many
    days old it actually is — the schedule is built from week boundaries rather
    than hardcoded offsets, and re-running on a Friday gives the same shape as
    on a Tuesday.
    """
    counts = list(WEEK_COUNTS)
    while sum(counts) < total:          # a bigger library grows the tail
        counts.insert(0, 1)
    while sum(counts) > total and counts:
        drop = min(counts[0], sum(counts) - total)
        counts[0] -= drop
        if counts[0] == 0:
            counts.pop(0)

    offsets = []
    for back, n in enumerate(reversed(counts)):     # back=0 is the current week
        if back == 0:
            days = list(range(weekday + 1))          # Monday .. today
        else:
            first = weekday + 1 + (back - 1) * 7
            days = list(range(first, first + 7))
        if not days or n == 0:
            continue
        if back < PACKED_WEEKS:
            picked = [days[i % len(days)] for i in range(n)]
        else:
            step = len(days) / n
            picked = [days[min(len(days) - 1, int(i * step))] for i in range(n)]
        offsets.extend(sorted(picked))
    return sorted(offsets)[:total]


def redate_words() -> None:
    """Re-date the sandbox library so its history ends today.

    Only the copy is touched — install_library() has already run, so this can
    never reach the source. Relative order is preserved: the newest word stays
    the newest, so every list that sorts by date looks the same as before.
    """
    from datetime import date, datetime, timedelta

    from app.core.db import get_active_db_path

    now = datetime.now()
    with contextlib.closing(sqlite3.connect(get_active_db_path())) as conn:
        ids = [r[0] for r in conn.execute(
            "SELECT ID FROM words ORDER BY created_at DESC, ID DESC")]
        offsets = _day_offsets(len(ids), date.today().weekday())
        for i, word_id in enumerate(ids):
            stamp = (now - timedelta(days=offsets[i])).replace(
                hour=HOURS[i % len(HOURS)], minute=(i * 7) % 60, second=0,
                microsecond=0)
            conn.execute("UPDATE words SET created_at = ? WHERE ID = ?",
                         (stamp.strftime("%Y-%m-%d %H:%M:%S"), word_id))
        conn.commit()


def reset_library() -> tuple:
    """Put the library back to its pristine state: a fresh copy of the source,
    migrated, plus the demo article."""
    from app.core.db import initialize_database

    words, texts = install_library(DB_SOURCE)
    initialize_database()
    redate_words()
    add_demo_text(texts)
    return words, texts + 1


def start_reading(window, app, rows=(1, 2, 3)) -> None:
    """Select a few words and start reading them aloud.

    This is what the hand-made original showed, and it is the vocabulary page
    at its most characteristic: the selection's action bar on one side, the
    player on the other, and the queue highlighted in the table. Rows are
    0-indexed, so (1, 2, 3) is the 2nd to 4th word.
    """
    from PySide6.QtCore import QItemSelection, QItemSelectionModel

    table = window.table
    model = table.model()
    if model is None or model.rowCount() <= max(rows):
        return
    span = QItemSelection(model.index(min(rows), 0),
                          model.index(max(rows), model.columnCount() - 1))
    table.selectionModel().select(
        span, QItemSelectionModel.ClearAndSelect | QItemSelectionModel.Rows)
    pump(app, 0.6)
    window.read_words_action()
    pump(app, 1.0)
    # With WordPlayer stubbed there is no audio thread to emit the first index,
    # so nudge it: this is the same call the running player makes, and it is
    # what paints the played row and the queued band behind it.
    window._on_player_index(0)
    pump(app, 0.8)


def run_review_session(window, app) -> None:
    """Drive a flashcard session far enough to photograph it mid-review.

    The reference shot shows a session in progress: a part-filled grade trail, a
    "N correct" counter, and a revealed card with the three grade buttons and
    their SM-2 interval previews. So: start the deck, answer a fixed run of
    cards, then reveal one more and stop there.
    """
    page = window.flashcards_page
    page._start_clicked()
    pump(app, 1.2)
    for grade in REVIEW_GRADES:
        if not page._deck:
            return
        page.flip()             # the grade buttons only accept a revealed card
        pump(app, 0.7)
        page._grade(grade)
        pump(app, 0.7)
    page.flip()                 # leave the card face-up, buttons armed
    pump(app, 1.0)


def capture(theme: str, pages, app, settings, width, scaling):
    """Build a window under `theme` and shoot each page.

    A fresh MainWindow per theme, deliberately. Calling theme.apply_theme() on
    a live window only swaps the app stylesheet — the model's colours, the
    icons, the table density and every page that caches a colour dict in its
    own refresh_theme() are left on the old palette, which is why a switched
    window photographs half-dark. MainWindow._apply_appearance() does handle
    all that, but constructing the window under the theme cannot leave a stale
    colour anywhere, and a few seconds per theme is nothing here.
    """
    from app.config import save_settings
    from app.ui import main_window as mw
    from app.ui import theme as theme_mod

    settings["appearance_mode"] = theme
    settings["widget_scaling"] = str(scaling)
    save_settings(settings)

    # Fresh library for every theme: the review shot studies cards, and without
    # this the second theme would photograph a library the first had graded.
    reset_library()

    theme_mod.apply_theme(app, theme, scaling)
    window = mw.MainWindow(settings)
    window.resize(width, round(width / ASPECT))
    window.show()
    pump(app, 2.0)

    index = {
        "words": mw.PAGE_WORDS,
        "flashcards": mw.PAGE_FLASHCARDS,
        "texts": mw.PAGE_TEXTS,
        "stats": mw.PAGE_STATS,
        "review": mw.PAGE_FLASHCARDS,
    }
    for name in pages:
        # A page that needs more room gets it, at the same widget scaling.
        # Both dimensions are compared: fit_whole_rows() resizes the window
        # for the flashcards shot, and a width-only check would let that carry
        # over into whatever page is captured next.
        want = round(PAGE_CONTENT.get(name, width / scaling) * scaling)
        want_h = round(want / ASPECT)
        if (window.width(), window.height()) != (want, want_h):
            window.resize(want, want_h)
            pump(app, 0.5)
        window.switch_page(index[name])
        # Page switches animate (~220 ms) and first-visit tours fire ~450 ms in.
        pump(app, 1.6)
        if name == "flashcards":
            fit_whole_rows(window, app)
        if name == "review":
            run_review_session(window, app)
        if name == "words":
            start_reading(window, app)
        if name == "texts":
            # Land in the reader, not the library list — the site uses this shot
            # for "learn from real content". Pick the longest text that is not
            # in the UI language: an English page in an English UI does not read
            # as language learning, and the shortest ones leave the pane empty.
            page = window.texts_page
            rows = list(enumerate(page.filtered))
            foreign = [r for r in rows if str(r[1].get("Language") or "") != "English"]
            row = max(foreign or rows,
                      key=lambda r: len(str(r[1].get("Text") or "")))[0]
            page.listing.setCurrentRow(row)
            pump(app, 1.2)
            open_word_popup(window, app)
        path = OUT / f"{name}-{theme.lower()}.png"
        grab(window, app).save(str(path))
        close_popups(window, app)      # nothing leaks into the next page
        # The PNG is the full-resolution original, kept for the lightbox and as
        # the source build_hero.py reads. The page itself loads the WebP, which
        # is what actually fits a showcase row.
        webp = _downscale(path)
        for p in (path, webp):
            print(f"  {p.relative_to(REPO)}  {p.stat().st_size / 1024:.0f} KB", flush=True)

    window.close()
    pump(app, 0.3)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--theme", choices=THEMES, action="append",
                    help="capture only this theme (repeatable)")
    ap.add_argument("--page", choices=PAGES, action="append",
                    help="capture only this page (repeatable)")
    ap.add_argument("--width", type=int, default=WIN_W,
                    help=f"window width in logical px (default {WIN_W})")
    ap.add_argument("--scaling", type=float, default=SCALING,
                    help=f"the app's widget_scaling (default {SCALING})")
    ap.add_argument("--db", type=Path, default=DUMMY_DB,
                    help="library to shoot; copied, never opened in place")
    ap.add_argument("--keep-sandbox", action="store_true",
                    help="leave the sandbox directory in place for inspection")
    args = ap.parse_args()
    themes = [t for t in THEMES if t in set(args.theme or THEMES)]
    # Always capture in PAGES order, whatever order the flags arrived in:
    # "review" starts a session and leaves the page in it, so a run that took
    # it before "flashcards" would photograph the session twice and never the
    # deck picker.
    pages = [p for p in PAGES if p in set(args.page or PAGES)]

    sandbox = Path(tempfile.mkdtemp(prefix="lingueez-shots-"))
    # cwd first: every path in the app (settings.cfg, dictionary.db, backups/)
    # resolves relative to it, and that must be true before the first import.
    os.chdir(sandbox)
    sys.path.insert(0, str(REPO))
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
    os.environ["QT_SCALE_FACTOR"] = SCALE

    try:
        from PySide6.QtWidgets import QApplication

        from app.config import load_settings, save_settings
        from app.i18n import set_language

        cut_off_the_cloud()

        app = QApplication([])
        widen_virtual_screen()
        settings = load_settings()
        settings.update({
            "language": "en", "language_configured": "True",
            "welcome_seen": "True",           # else the welcome modal blocks the UI
            # Every page has its own first-visit tour, and its overlay outlives
            # the page switch — one missing flag greys out an unrelated shot.
            "tour_words_seen": "True", "tour_flashcards_seen": "True",
            "tour_texts_seen": "True", "tour_stats_seen": "True",
            "tour_completed": "True",
            "auto_check_updates": "False",
            "autostart_configured": "True",   # never touch the real autostart entry
            "hotkey": "",                     # never grab a global hotkey
            "android_promo_dismissed": "True",  # the banner is promo, not product
            # A deck as long as the library, so the review shot reads "Card 11
            # of 33" rather than stopping at the default 20.
            "flashcards_deck_size": "33",
            # read_words_action() would otherwise jump to the Flashcards page
            # to follow the audio, and the words shot wants to stay put.
            "flashcards_autoswitch": "False",
        })
        save_settings(settings)
        set_language("en")

        # Library first, then initialize_database() — it migrates whatever it
        # finds, adding tables and columns the snapshot predates.
        global DB_SOURCE
        DB_SOURCE = args.db
        words, texts = reset_library()
        print(f"{words} words, {texts} texts "
              f"({args.db.name} + the demo article)\n"
              f"{args.width}x{round(args.width / ASPECT)} logical "
              f"@ {args.scaling}x widgets, {SCALE}x pixels\n", flush=True)

        OUT.mkdir(parents=True, exist_ok=True)
        for t in themes:
            print(f"{t}:", flush=True)
            capture(t, pages, app, settings, args.width, args.scaling)
    finally:
        os.chdir(REPO)
        if args.keep_sandbox:
            print(f"sandbox kept at {sandbox}", flush=True)
        else:
            shutil.rmtree(sandbox, ignore_errors=True)


if __name__ == "__main__":
    main()
