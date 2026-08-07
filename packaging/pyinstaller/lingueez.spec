# -*- mode: python ; coding: utf-8 -*-
# PyInstaller build definition for Lingueez. Runs natively on each CI runner,
# so `sys.platform` here reflects the OS being built for.
#
# Layout: a **onedir** build with PyInstaller's default contents directory, so
# the data (assets/, locales/, ffmpeg/) lands in `_internal/` beside the
# executable. That is what the app expects: main.py resolves the bundle through
# `sys._MEIPASS`, which points at the contents directory, and seeds those
# read-only resources into a writable per-user data dir it then chdir's to — so
# user files (dictionary.db, settings.cfg, backups/, .env, …) never depend on
# where the folder was extracted.
#
# Build:  pyinstaller packaging/pyinstaller/lingueez.spec
import os
import sys

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Every source path below is written relative to the repo root, so anchor on the
# spec's own location (PyInstaller injects SPECPATH) instead of the invoking
# directory. dist/ and build/ are unaffected: PyInstaller resolves those before
# running the spec, so they still land beside wherever the build was started.
REPO = os.path.abspath(os.path.join(SPECPATH, os.pardir, os.pardir))  # noqa: F821
os.chdir(REPO)


def repo_path(*parts):
    """Absolute path to a repo file, for anything handed to PyInstaller.

    chdir() above is not enough: PyInstaller resolves the relative paths in
    `datas` and in Analysis(scripts) against the *spec file's* directory
    (`format_binaries_and_datas(..., workingdir=spec_dir)`), not the working
    directory — so a bare "main.py" is looked for next to this spec. Every such
    path is made absolute here; target directories stay relative, since those
    are positions inside the bundle.
    """
    return os.path.join(REPO, *parts)

block_cipher = None


def collect_dir(folder, includes=None):
    """Return (abs_src, dest_dir) tuples for every file under *folder*, preserving
    the tree. *includes*, if given, keeps only basenames in that set."""
    items = []
    for root, _dirs, files in os.walk(repo_path(folder)):
        dest = os.path.relpath(root, REPO)  # dest mirrors the relative tree
        for name in files:
            if includes is not None and name not in includes:
                continue
            items.append((os.path.join(root, name), dest))
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
sys.path.insert(0, REPO)
from app.i18n import qt_translation_code  # noqa: E402

datas += collect_data_files("PySide6", includes=[
    f"Qt/translations/qtbase_{qt_translation_code(code)}.qm"
    for code in sorted(locale_codes)
])
# License/attribution must travel with the binary (AGPL §7 + ffmpeg).
datas += [(repo_path(n), ".")
          for n in ("NOTICE", "THIRD-PARTY-LICENSES.md", "LICENSE.txt")]

# ffmpeg: bundle ONLY the current OS's binaries into ffmpeg/bin/, the relative
# path read_ffmpeg_path() (app/core/shell_utils.py) looks for. Drop the other
# platform's binaries, ffplay, and the docs/presets — pydub only runs ffmpeg
# and ffprobe.
if sys.platform == "win32":
    ff = {"ffmpeg.exe", "ffprobe.exe"}
else:
    ff = {"ffmpeg", "ffprobe"}
datas += [(repo_path("ffmpeg", "bin", n), os.path.join("ffmpeg", "bin"))
          for n in ff if os.path.isfile(repo_path("ffmpeg", "bin", n))]
if os.path.isfile(repo_path("ffmpeg", "LICENSE")):
    datas += [(repo_path("ffmpeg", "LICENSE"), "ffmpeg")]

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

icon = repo_path("assets", "icons",
                 "icon.ico" if sys.platform == "win32" else "icon.png")

a = Analysis(
    [repo_path("main.py")],
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
    # NB: `contents_directory` is an EXE() argument — COLLECT only inherits it
    # from the EXE it is passed (PyInstaller/building/api.py). Setting it here
    # did nothing; every release so far shipped the default `_internal/` layout,
    # which is what main.py's sys._MEIPASS lookup expects. Left as the default
    # rather than "fixed" onto EXE, which would move every bundled file.
)
