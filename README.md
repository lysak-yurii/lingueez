# Dictionary Desktop App — Upgraded (PySide6)

A complete rewrite of the original CustomTkinter dictionary app with a modern
Qt (PySide6) interface. **Full feature parity** with the original, using the
**exact same database schema** (SQLite + Supabase), so your existing data and
cloud sync keep working unchanged.

## What's new vs. the original

- Modern Qt UI with dark/light themes, rounded surfaces, toast notifications
- Native menu bar, proper table view, live search with filter highlighting
- All long-running work (sync, TTS, ChatGPT, DeepL, audio export) runs on
  background threads — the UI never freezes
- Native system tray (QSystemTrayIcon) instead of pystray/GTK workarounds
- Single-instance lock with automatic stale-lock recovery (QLockFile)

## Features (parity with original)

- **Word management** — add/edit/delete, statuses, favorites, tags
- **Live search** — across words, translations and tags with scope settings
- **Filters** — language, translation language, status, tag, favorites, row limit
- **DeepL translation** — with language auto-detect and same-language guard
- **ChatGPT** — definitions (per word/translation) and generated study texts
- **Text-to-speech** — gTTS (free) or Google Cloud TTS (premium); read words
  aloud or export an MP3 with configurable pauses/repeats
- **Texts browser** — read, edit, listen to generated texts
- **Export** — PDF (fully styleable), Excel, CSV, TXT (Anki-friendly headers)
- **Import** — Excel with duplicate/reversed-pair detection and confirm dialogs
- **Cloud sync** — same Supabase tables, sync queue, deletions, conflict logic
- **Bin** — restore or permanently delete soft-deleted words/texts (cloud)
- **Backups** — automatic daily backups with retention, preview and restore
- **System** — tray icon, global hotkey **Ctrl+Shift+V** (add word from
  clipboard + auto-translate), autostart on login, `--minimized` flag

## Running

```bash
./run.sh
```

The first run creates a virtual environment at `~/.venvs/dictionary-upgraded`
and installs dependencies. (The venv cannot live in this folder because exFAT
drives don't support symlinks.)

Manual setup, if you prefer:

```bash
python3 -m venv ~/.venvs/dictionary-upgraded
~/.venvs/dictionary-upgraded/bin/pip install -r requirements.txt
~/.venvs/dictionary-upgraded/bin/python main.py
```

## Configuration

- `settings.cfg` — same flat key=value format as the original app
  (a copy of your original settings was brought over). Editable in-app via
  **Settings → Preferences**.
- `.env` — API keys: `OPENAI_API_KEY`, `SUPABASE_URL`, `SUPABASE_KEY`
  (copied from the original app; also editable in Settings → APIs).
- DeepL key lives in `settings.cfg` (`api_key`), same as before.

## Troubleshooting

**“python3.12 has stopped unexpectedly” on launch** — Qt 6.5+ needs the
system library `libxcb-cursor0`, which Ubuntu doesn't preinstall:
`sudo apt install libxcb-cursor0`.

## Audio export and ffmpeg

MP3 export concatenation uses `pydub`, which needs **ffmpeg**. Either:

- install it system-wide: `sudo apt install ffmpeg`, or
- copy the `ffmpeg/` folder from the original app directory here
  (the app checks `./ffmpeg/bin/` first, same as the original).

## Data

- `dictionary.db` — **a copy** of your original database (the original app's
  file is untouched). Both apps sync against the same Supabase project, so
  changes made in either app converge through cloud sync.
- `backups/` — automatic daily backups, pruned to 10/month for the current
  month and 1/month for older months.

## Project layout

```
main.py                  entry point (single instance, theming, logging)
app/
  config.py              settings.cfg load/save
  version.py
  core/                  GUI-free backend (ported from the original)
    database_adapter.py  local/cloud CRUD + sync queue   (unchanged logic)
    supabase_client.py   Supabase REST wrapper           (unchanged logic)
    sync_manager.py      two-way sync engine             (unchanged logic)
    db.py                schema init (identical SQL) + tag queries
    audio.py             TTS playback/export (tk-free port)
    gpt.py               ChatGPT definitions/texts (tk-free port)
    translator.py        DeepL client
    exporters.py         PDF/Excel/CSV/TXT writers
    importer.py          Excel import analyze/apply pipeline
    backup_management.py daily backup + retention        (unchanged logic)
    data_management.py   normalization + duplicate checks (unchanged logic)
  system/autostart.py    login autostart (Linux .desktop / Windows registry)
  ui/
    theme.py             dark/light palettes + QSS
    main_window.py       main window
    word_model.py        table model + filter pipeline
    workers.py           thread-pool helpers
    toast.py             toast notifications
    dialogs/             add/edit word, definition, tags, texts, bin,
                         backups, audio export, Excel import, settings, log
```

## Keyboard shortcuts

| Shortcut | Action |
| --- | --- |
| Ctrl+Shift+V (global) | Add word from clipboard + translate |
| Ctrl+A | Select all rows |
| Ctrl+C | Copy selected rows |
| Delete | Delete selected rows |
| Double-click row | View definition |
