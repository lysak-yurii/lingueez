#!/usr/bin/env python3
"""Prepare the Android screenshots the site shows, from the store captures.

The store screenshots are real device captures, so they carry the Android status
bar — clock, signal, battery. On a phone that reads as the system chrome it is;
dropped into the site's drawn phone frame it reads as clutter that belongs to
somebody else's device, and the 79% battery dates the shot.

So the bar is painted over in the app's own background colour rather than cropped
away. Cropping shortened the image, which changed its aspect and left the drawn
phone's black display well showing through above it — the frame insets the screen
to leave room for the dynamic island, and that gap is only invisible while the
picture reaches the top. Filling keeps the original height and hands the frame an
image that covers the whole display.

Where the bar ends is measured, not guessed: it is the first band of ink at the
top of the image, and the fill stops at the first clear row beneath it. That
survives a different device, a different Android version or a longer clock.

    python3 tools/site/mobile_shots.py                 # the default source
    python3 tools/site/mobile_shots.py path/to/shots   # or somewhere else
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "assets" / "mobile"
SOURCE = Path.home() / "dev" / "lingueez-mobile" / "assets" / "store" / "screenshots"

# Which captures the site uses, and what it calls them. The names line up with
# build_hero.py's SCREENS["phone"]; the rest of the store set is left alone.
WANTED = {
    "01_today": "today",
    "02_my_words": "words",
    "03_flashcards": "flashcards",
    "04_quiz": "quiz",
    "05_listen_review": "listen",
    "06_progress": "progress",
}

# The phone screen is ~158 SVG units wide and renders at up to ~2x, so a little
# over 340px of source is all it can show. Kept generous for the lightbox.
WIDTH = 520

# How far from the page colour a pixel has to be to count as ink, and how many
# clear rows in a row mean the status bar is behind us rather than a gap between
# glyphs.
INK = 28
CLEAR_RUN = 12

# The Android app's own surfaces are warm (#faf7f0 light, #16130e dark) while the
# desktop app's are neutral (#ffffff, #161b22). Side by side in the hero the phone
# read as yellowed, so the shots are colour-matched to the desktop.
#
# The whole image is corrected, not just the page: the cards, chips and grading
# buttons are all tinted to sit on that warm ground, and swapping only the
# background would leave them floating on a colour they were never designed for.
#
# Anchor per theme: light fixes black and scales up, dark fixes white and scales
# what is left. Scaling a near-black page toward a cool one multiplicatively
# would need a 2.4x blue gain and would wreck the picture.
DESKTOP = {"light": (255, 255, 255), "dark": (22, 27, 34)}


def match_desktop(img: Image.Image, theme: str) -> Image.Image:
    """Neutralise the app's warm cast toward the desktop app's surfaces."""
    target = DESKTOP.get(theme)
    if target is None:
        return img
    a = np.asarray(img, dtype=np.float32)
    page = np.median(a[: int(a.shape[0] * 0.06)].reshape(-1, 3), axis=0)
    t = np.array(target, dtype=np.float32)
    if theme == "light":
        out = a * (t / np.maximum(page, 1))
    else:
        out = 255.0 - (255.0 - a) * ((255.0 - t) / np.maximum(255.0 - page, 1))
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGB")


def status_bar_height(img: Image.Image) -> int:
    """Rows the status bar occupies, or 0 if none is found."""
    a = np.asarray(img.convert("RGB"), dtype=np.int16)
    top = a[: int(a.shape[0] * 0.12)]
    page = np.median(top.reshape(-1, 3), axis=0)
    ink = np.abs(top - page).max(axis=2).max(axis=1) > INK

    seen_ink, clear = False, 0
    for y, has in enumerate(ink):
        if has:
            seen_ink, clear = True, 0
        elif seen_ink:
            clear += 1
            if clear >= CLEAR_RUN:
                return y - clear + 1
    return 0


def main(argv):
    src = Path(argv[0]) if argv else SOURCE
    if not src.is_dir():
        raise SystemExit(f"no screenshots at {src}")
    OUT.mkdir(parents=True, exist_ok=True)

    for stem, name in sorted(WANTED.items(), key=lambda kv: kv[1]):
        for theme in ("light", "dark"):
            path = src / f"{stem}_{theme}.jpg"
            if not path.exists():
                print(f"missing: {path}")
                continue
            img = Image.open(path).convert("RGB")
            cut = status_bar_height(img)
            if cut:
                # The app's own page colour, read from the clear row the bar
                # ends at — so light and dark each get their own, and a future
                # theme needs no table here.
                a = np.asarray(img, dtype=np.int16)
                page = np.median(a[cut:cut + 8].reshape(-1, 3), axis=0)
                a[:cut] = page
                img = Image.fromarray(a.astype(np.uint8), "RGB")
            img = match_desktop(img, theme)
            img = img.resize((WIDTH, round(img.height * WIDTH / img.width)),
                             Image.LANCZOS)
            dst = OUT / f"{name}-{theme}.jpg"
            img.save(dst, quality=88, optimize=True, progressive=True)
            print(f"  {dst.relative_to(ROOT)}  {img.width}x{img.height}  "
                  f"bar {cut}px filled  {dst.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main(sys.argv[1:])
