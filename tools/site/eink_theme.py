#!/usr/bin/env python3
"""Produce light and dark variants of the e-ink (KOReader) screenshots.

The site used to be dark-only, so its predecessor (darken_eink.py) inverted
these shots in place and the black-on-white originals were lost. Now that the
site has a light theme they are needed again: an inverted e-ink screen on a
white page reads as broken, because a real e-reader *is* black on white.

So this writes a pair beside each source and never overwrites it:

    save-word.png  ->  save-word-light.png   black on white (the true look)
                       save-word-dark.png    compressed band, for a dark page

Either direction works — hand a light shot or a dark one, the missing twin is
derived. Deriving light from dark is an approximate inverse of the band
compression, not a re-shoot; at the ~340 px these are displayed it is
indistinguishable, but a fresh capture from the device is always better.

    python3 tools/site/eink_theme.py                   # docs/assets/koreader
    python3 tools/site/eink_theme.py path/to/shot.png  # or specific files
"""
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
KOREADER = ROOT / "docs" / "assets" / "koreader"

# Screenshots of the reader UI, by base name. lingueez_hero.jpg is an
# illustration, not a screenshot — inverting it would wreck it, so it is
# deliberately not listed.
DEFAULTS = ["save-word", "flashcards", "menu", "view-words"]

# Where inverted black / inverted white land. A straight invert would blow the
# page to pure white on pure black; this softer band sits on a dark page.
#
# The dark page colour is an RGB triple, not a grey: the site's dark surfaces
# are faintly blue, and a neutral-grey screen reads as a foreign object dropped
# into them. It must also stay clearly darker than the device bezel it sits in
# (build_hero.py's `metal` gradient bottoms out at #1c222c) or the screen stops
# reading as recessed — a lighter page was tried and merged into the frame.
DARK_BG = (16, 20, 24)      # the app's own --bg, #101418
DARK_FG = (232, 232, 232)
BG, FG = 10, 232


def to_dark(a: np.ndarray) -> np.ndarray:
    """Light (black on white) -> the site's dark band, as RGB.

    Returns H x W x 3 so the page colour can carry the site's faint blue.
    """
    t = (255.0 - a) / 255.0                       # 0 at page, 1 at ink
    bg = np.array(DARK_BG, dtype=np.float32)
    fg = np.array(DARK_FG, dtype=np.float32)
    return bg + t[..., None] * (fg - bg)


def to_light(a: np.ndarray) -> np.ndarray:
    """The dark band -> light. The inverse of to_dark, clamped."""
    return np.clip(255.0 - (a - BG) * 255.0 / (FG - BG), 0.0, 255.0)


def _hex(rgb) -> str:
    return "#%02x%02x%02x" % tuple(int(v) for v in rgb)


def resolve(base: Path) -> Path | None:
    """The source for a base name, whichever variant survives.

    Once a pair has been generated the un-suffixed original is usually gone, so
    a re-run has to be able to start from `-light` (or `-dark`) instead. Without
    this the script finds nothing and quietly does no work at all.
    """
    for candidate in (base, base.with_name(base.stem + "-light" + base.suffix),
                      base.with_name(base.stem + "-dark" + base.suffix)):
        if candidate.exists():
            return candidate
    return None


# The device screenshots carry KOReader's own hairline border. The site frames
# them again with a rounded 1px border of its own, so the two nest — a sharp
# black rectangle a couple of pixels inside a soft grey one. Trimming the
# device's own edge leaves the page's frame as the only one.
#
# Bounded, and re-running is a no-op: once the edge is gone the detector finds
# nothing to trim, so the shot cannot creep inwards over repeated builds.
MAX_TRIM = 8
EDGE_INK = 160
# How far in from each corner the frame's radius can reach.
CORNER = 12


def trim_frame(light: np.ndarray) -> np.ndarray:
    """Drop the screenshot's own border, measured on the light representation."""
    def run(lines) -> int:
        """How many lines in from this edge the frame reaches.

        Whole lines, not one sampled pixel: a border can sit a pixel inside the
        edge (save-word has a blank column before its rule), and stopping at the
        first light pixel then found nothing to trim. Scans to the deepest
        mostly-dark line within the budget rather than the first.
        """
        deepest = -1
        for i in range(min(MAX_TRIM, len(lines))):
            if (lines[i] < EDGE_INK).mean() > 0.5:
                deepest = i
        return deepest + 1

    h, w = light.shape
    top = run(light)
    bottom = run(light[::-1])
    left = run(light.T)
    right = run(light.T[::-1])
    if top or bottom or left or right:
        light = light[top:h - bottom or None, left:w - right or None]
    return clear_corners(light)


def clear_corners(light: np.ndarray) -> np.ndarray:
    """Erase the frame's rounded corners, left behind by the straight trim.

    The device frame is a rounded rectangle. Trimming its straight rules leaves
    four little quarter-circle arcs, and those are invisible on the page — the
    site rounds these shots anyway — but the lightbox shows the picture flat,
    where they read as black nicks in the corners.

    Painted out rather than cropped away: cropping a fixed extra margin would
    eat a few pixels on every rebuild, while once an arc is white there is
    nothing left for the next run to find.
    """
    page = float(np.median(light))
    if page < EDGE_INK:                       # not a light-on-white shot
        return light
    out = light.copy()
    # The whole corner square, not a walk inward from the corner pixel: an arc
    # does not necessarily touch the very corner (save-word's stops a pixel
    # short), and a walk that starts on a light pixel gives up immediately.
    # After the straight rules are trimmed these squares hold nothing but frame
    # remnants — the UI itself keeps well clear of the corners.
    for rows in (slice(None, CORNER), slice(-CORNER, None)):
        for cols in (slice(None, CORNER), slice(-CORNER, None)):
            block = out[rows, cols]
            block[block < EDGE_INK] = page
    return out


def variants(path: Path) -> tuple[Path, Path]:
    """Write <stem>-light and <stem>-dark next to `path`. Returns both."""
    a = np.asarray(Image.open(path).convert("L"), dtype=np.float32)
    source_is_dark = a.mean() < 128
    light = trim_frame(a if not source_is_dark else to_light(a))
    dark = to_dark(light)

    # Strip any variant suffix so re-running never yields "save-word-light-dark".
    stem = re.sub(r"-(light|dark)$", "", path.stem)
    out = []
    for name, data in (("light", light), ("dark", dark)):
        dst = path.with_name(f"{stem}-{name}{path.suffix}")
        mode = "RGB" if data.ndim == 3 else "L"
        Image.fromarray(data.astype(np.uint8), mode).save(dst, optimize=True)
        out.append(dst)
    return tuple(out)


def main(argv):
    targets = [Path(p) for p in argv] or [KOREADER / f"{n}.png" for n in DEFAULTS]
    for base in targets:
        path = resolve(base)
        if path is None:
            print(f"missing: no source for {base}")
            continue
        for dst in variants(path):
            rel = dst.relative_to(ROOT) if ROOT in dst.parents else dst
            print(f"  {rel}  {dst.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main(sys.argv[1:])
