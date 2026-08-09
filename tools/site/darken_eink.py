#!/usr/bin/env python3
"""Repaint e-ink (KOReader) screenshots as dark, to match the rest of the site.

The reader shoots white-on-black by default, which is the one bright rectangle on
an otherwise dark page. A straight invert blows the page to pure white text on
pure black, so the inverted values are compressed into a softer band instead:
background lands on #0a0a0a and text on #e8e8e8.

Already-dark files are left alone, so re-running this is safe.

    python3 tools/site/darken_eink.py                  # every shot in docs/assets/koreader
    python3 tools/site/darken_eink.py path/to/shot.png # or specific files
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
KOREADER = ROOT / "docs" / "assets" / "koreader"

# Screenshots of the reader UI. lingueez_hero.jpg is an illustration, not a
# screenshot — inverting it would wreck it, so it is deliberately not listed.
DEFAULTS = ["save-word.png", "flashcards.png", "menu.png"]

BG, FG = 10, 232  # where inverted black / inverted white end up


def darken(path: Path) -> bool:
    """Invert one screenshot in place. Returns False if it was already dark."""
    img = Image.open(path).convert("L")
    a = np.asarray(img, dtype=np.float32)
    if a.mean() < 128:
        return False
    a = 255.0 - a
    a = BG + a * (FG - BG) / 255.0
    Image.fromarray(a.astype(np.uint8), "L").save(path, optimize=True)
    return True


def main(argv):
    targets = [Path(p) for p in argv] or [KOREADER / n for n in DEFAULTS]
    for path in targets:
        if not path.exists():
            print(f"missing: {path}")
            continue
        print(f"{'darkened' if darken(path) else 'already dark'}: "
              f"{path.relative_to(ROOT) if ROOT in path.parents else path}")


if __name__ == "__main__":
    main(sys.argv[1:])
