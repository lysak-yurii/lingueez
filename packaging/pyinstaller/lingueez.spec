# -*- mode: python ; coding: utf-8 -*-
# PyInstaller build definition for Lingueez. Runs natively on each CI runner,
# so `sys.platform` here reflects the OS being built for.
#
# Layout: a **onedir** build with `contents_directory='.'`, i.e. the executable
# and its data (assets/, locales/, ffmpeg/) sit side by side — matching
# the app's path logic, which chdir's to `dirname(sys.executable)` and reads
# *and writes* every file relative to it (dictionary.db, settings.cfg, backups/,
# .env, …). Run the extracted folder from a writable location.
#
# Build:  pyinstaller packaging/pyinstaller/lingueez.spec
import os
import sys

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Every source path below is written relative to the repo root, so anchor on the
# spec's own location (PyInstaller injects SPECPATH) instead of the invoking
# directory. dist/ and build/ are unaffected: PyInstaller resolves those before
# running the spec, so they still land beside wherever the build was started.
os.chdir(os.path.abspath(os.path.join(SPECPATH, os.pardir, os.pardir)))  # noqa: F821

block_cipher = None


def collect_dir(folder, includes=None):
    """Return (src, dest_dir) tuples for every file under *folder*, preserving
    the tree. *includes*, if given, keeps only basenames in that set."""
    items = []
    for root, _dirs, files in os.walk(folder):
        for name in files:
            if includes is not None and name not in includes:
                continue
            src = os.path.join(root, name)
            items.append((src, root))  # dest mirrors the relative tree
    return items


datas = []
datas += collect_dir("assets")  # includes assets/fonts/
# Ship the locale modules as real .py files beside the exe (contents_directory
# is '.'), not only inside the PYZ. main.py adds the bundle dir to sys.path, so
# importlib resolves locales.* from disk, and i18n._available_locales()'s
# os.listdir() can actually see them in the frozen build. Picks up every
# locales/*.py automatically, so future languages need no spec change.
datas += [(src, dest) for src, dest in collect_dir("locales")
          if src.endswith(".py")]
locale_codes = [os.path.splitext(os.path.basename(src))[0]
                for src, _dest in collect_dir("locales")
                if src.endswith(".py") and not os.path.basename(src).startswith("__")]
# Qt's own translations for the standard dialog buttons (OK/Cancel/Yes/No),
# file dialogs and text-field context menus, loaded at runtime via
# QLibraryInfo(TranslationsPath) in main.py. Derived from the locales shipped
# above rather than hardcoded, so a new locales/<code>.py brings its Qt strings
# with it. Qt names a few of these differently from our codes, hence
# qt_translation_code(); locales Qt has no translation for simply match nothing
# here and keep English buttons (main.py logs it).
sys.path.insert(0, os.path.abspath("."))
from app.i18n import qt_translation_code  # noqa: E402

datas += collect_data_files("PySide6", includes=[
    f"Qt/translations/qtbase_{qt_translation_code(code)}.qm"
    for code in sorted(locale_codes)
])
# License/attribution must travel with the binary (AGPL §7 + ffmpeg).
datas += [("NOTICE", "."), ("THIRD-PARTY-LICENSES.md", "."), ("LICENSE.txt", ".")]

# ffmpeg: bundle ONLY the current OS's binaries into ffmpeg/bin/, the relative
# path read_ffmpeg_path() (app/core/shell_utils.py) looks for. Drop the other
# platform's binaries, ffplay, and the docs/presets — pydub only runs ffmpeg
# and ffprobe.
if sys.platform == "win32":
    ff = {"ffmpeg.exe", "ffprobe.exe"}
else:
    ff = {"ffmpeg", "ffprobe"}
datas += [(os.path.join("ffmpeg", "bin", n), os.path.join("ffmpeg", "bin"))
          for n in ff if os.path.isfile(os.path.join("ffmpeg", "bin", n))]
if os.path.isfile(os.path.join("ffmpeg", "LICENSE")):
    datas += [(os.path.join("ffmpeg", "LICENSE"), "ffmpeg")]

# Packages PyInstaller's static analysis tends to under-collect.
hiddenimports = [
    "supabase", "gotrue", "postgrest", "realtime", "storage3",
    "google.genai", "openai", "feedparser", "trafilatura",
    "pydub", "gtts", "google.cloud.texttospeech",
    "segno",   # imported lazily inside app/ui/android_promo.qr_pixmap
]
# i18n loads locale modules dynamically (importlib.import_module("locales.uk")),
# which static analysis can't see — collect them explicitly so the Ukrainian
# translation is actually bundled instead of silently falling back to English.
hiddenimports += collect_submodules("locales")
# The X11 global-hotkey agent (app/system/hotkey_agent.py) is never imported —
# it's launched as a subprocess — so analysis misses it and pynput. Frozen builds
# re-invoke themselves with --hotkey-agent, which imports it, so bundle both.
# pynput's X11 backend (pynput.keyboard._xorg) connects to an X server at import
# time, so collect_submodules can only enumerate it when a display exists; on a
# headless builder it silently returns nothing and the hotkey ships dead. Build
# under a virtual display (CI runs PyInstaller via `xvfb-run`) and hard-fail here
# if the backend is missing, rather than shipping a broken AppImage.
# Linux-only: Windows drives the hotkey in-process via the `keyboard` lib.
if sys.platform != "win32":
    _pynput_mods = collect_submodules("pynput")
    hiddenimports += ["app.system.hotkey_agent"]
    hiddenimports += _pynput_mods
    hiddenimports += collect_submodules("Xlib")
    if not any(m.endswith("keyboard._xorg") for m in _pynput_mods):
        raise SystemExit(
            "lingueez.spec: pynput X11 backend (_xorg) was not collected — the "
            "global hotkey would be dead. Run PyInstaller under a display, e.g. "
            "`xvfb-run -a pyinstaller packaging/pyinstaller/lingueez.spec`."
        )

icon = os.path.join("assets", "icons",
                    "icon.ico" if sys.platform == "win32" else "icon.png")

a = Analysis(
    ["main.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["tkinter"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Lingueez",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,           # GUI app: no console window on Windows
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="Lingueez",
    contents_directory=".",   # data beside the exe, matching the app's path logic
)
