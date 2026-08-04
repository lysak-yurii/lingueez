# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Generate the MSIX visual assets from the master app icon.

The manifest references logos by unqualified name; Windows resolves each to a
scale-/targetsize-/altform-qualified file beside it. The taskbar needs the
_altform-unplated variants — without them it draws the logo shrunk inside a
plate filled from BackgroundColor. Resolution goes through resources.pri, so
these files only take effect if the package is built with makepri (see
README.md).

We commit the results so CI needn't depend on Pillow. Rerun whenever
assets/icons/icon.png changes:

    python packaging/msix/generate_assets.py

Squares are a LANCZOS downscale of the master; the wide tile centres it on a
transparent canvas. Variants larger than the master are skipped, not upscaled.
"""
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
MASTER = os.path.join(REPO, "assets", "icons", "icon.png")
OUT = os.path.join(HERE, "Assets")

# Logo base name -> its 100%-scale logical size, as referenced by the manifest.
SQUARE = {
    "Square44x44Logo": 44,
    "Square71x71Logo": 71,
    "Square150x150Logo": 150,
    "Square310x310Logo": 310,
    "StoreLogo": 50,
}
WIDE = ("Wide310x150Logo", (310, 150))

# Display scale factors Windows may ask for.
SCALES = (100, 125, 150, 200, 400)

# Pixel sizes the shell requests for the app icon; it picks the nearest match.
TARGET_SIZES = (16, 24, 32, 40, 48, 64, 96, 256)

# Plated, then the dark- and light-shell unplated forms. The mark reads on
# both, so all three share one rendering.
ALTFORMS = ("", "_altform-unplated", "_altform-lightunplated")


def main():
    os.makedirs(OUT, exist_ok=True)
    master = Image.open(MASTER).convert("RGBA")
    limit = min(master.size)
    written = skipped = 0

    def save(img, name):
        nonlocal written
        img.save(os.path.join(OUT, name))
        written += 1

    def square(size):
        return master.resize((size, size), Image.LANCZOS)

    def wide(w, h):
        canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        logo = master.resize((h, h), Image.LANCZOS)  # fit to height, keep square
        canvas.paste(logo, ((w - h) // 2, 0), logo)
        return canvas

    for name, base in SQUARE.items():
        for scale in SCALES:
            size = round(base * scale / 100)
            if size > limit:
                skipped += 1
                continue
            img = square(size)
            save(img, f"{name}.scale-{scale}.png")
            if scale == 100:
                save(img, f"{name}.png")  # unqualified fallback

    name, (bw, bh) = WIDE
    for scale in SCALES:
        w, h = round(bw * scale / 100), round(bh * scale / 100)
        if h > limit:
            skipped += 1
            continue
        img = wide(w, h)
        save(img, f"{name}.scale-{scale}.png")
        if scale == 100:
            save(img, f"{name}.png")

    for size in TARGET_SIZES:
        if size > limit:
            skipped += 1
            continue
        img = square(size)
        for altform in ALTFORMS:
            save(img, f"Square44x44Logo.targetsize-{size}{altform}.png")

    print(f"{written} files written to {OUT}")
    if skipped:
        print(
            f"{skipped} variants skipped — they exceed the {limit}px master; "
            "supply a larger assets/icons/icon.png to fill them in."
        )


if __name__ == "__main__":
    main()
