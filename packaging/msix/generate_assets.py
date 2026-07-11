# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Generate the MSIX visual assets from the master app icon.

The Microsoft Store package (AppxManifest.xml) references a set of sized PNG
tiles/logos. Rather than depend on Pillow in CI, we regenerate them here and
*commit* the results under packaging/msix/Assets/ — CI just consumes them. Rerun
this whenever assets/icons/icon.png changes:

    python packaging/msix/generate_assets.py

Square logos are a straight LANCZOS downscale of the (square) master. The wide
tile centres the square logo on a transparent canvas so nothing is cropped.
"""
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
MASTER = os.path.join(REPO, "assets", "icons", "icon.png")
OUT = os.path.join(HERE, "Assets")

# name -> (width, height). Square tiles + the Store logo, plus the wide tile.
SQUARE = {
    "Square44x44Logo.png": 44,
    "Square71x71Logo.png": 71,
    "Square150x150Logo.png": 150,
    "Square310x310Logo.png": 310,
    "StoreLogo.png": 50,
}
WIDE = ("Wide310x150Logo.png", (310, 150))


def main():
    os.makedirs(OUT, exist_ok=True)
    master = Image.open(MASTER).convert("RGBA")

    for name, size in SQUARE.items():
        master.resize((size, size), Image.LANCZOS).save(os.path.join(OUT, name))
        print(f"  {name}  {size}x{size}")

    name, (w, h) = WIDE
    canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    logo = master.resize((h, h), Image.LANCZOS)  # fit to height, keep square
    canvas.paste(logo, ((w - h) // 2, 0), logo)
    canvas.save(os.path.join(OUT, name))
    print(f"  {name}  {w}x{h}")


if __name__ == "__main__":
    main()
