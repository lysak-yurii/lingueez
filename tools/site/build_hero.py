#!/usr/bin/env python3
"""Build the landing-page hero: three devices carrying real product screenshots.

Sources (all already dark — run tools/site/darken_eink.py first if you add new
reader shots):

    docs/assets/dashboard.png          -> laptop
    docs/assets/koreader/save-word.png -> e-reader
    docs/assets/mobile/flashcards.jpg  -> phone

Outputs:

    docs/assets/hero.svg   self-contained (screenshots embedded as data URIs),
                           served to anyone who opens the maximised view
    docs/assets/hero.png   1600x933 raster fallback
    docs/assets/hero.webp  1600x933, what browsers actually fetch

Layout
------
* The laptop stays dead-centre (x=600) — that is what reads as a "standard" hero.
* Both side devices live in the front plane: each overlaps the laptop by a small
  amount (reader -> lid bezel, phone -> deck corner) and their bottom edges share
  one floor line at y=604. That overlap + drop is what sells the depth.
* The e-reader is the heavier side device, so the right margin is ~35px wider
  than the left: optical balance rather than geometric.
* Screen rects match their screenshot's aspect, so nothing is cropped at all:
  laptop 1.4267 = the complete app window (nav rail, all rows, status bar);
  phone and reader letterbox into their own black.

    python3 tools/site/build_hero.py              # transparent, for the site
    python3 tools/site/build_hero.py --backdrop  # painted background, standalone
"""
import base64
import io
import sys
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "docs" / "assets"

# The laptop screen is 552x387 in SVG units and the hero renders at up to ~2x,
# so ~1200px of source is as much detail as the screen can ever show.
DESKTOP_W, READER_W, PHONE_W = 1200, 520, 340
RASTER_W = 1600

# The devices are laid out on a 1200x700 stage but only ink x 73.5..1093.5 /
# y 83.2..616.5 of it. Publishing the whole stage would waste ~25% of the image
# on empty margin and shrink the devices for a given column width, so the view
# is cropped to the ink plus a little breathing room for the shadows.
VIEW_X, VIEW_Y, VIEW_W, VIEW_H = 63, 73, 1041, 554


def _uri(data: bytes, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


def _png(img: Image.Image) -> str:
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    return _uri(buf.getvalue(), "image/png")


def _jpeg(img: Image.Image, quality: int = 88) -> str:
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=quality, subsampling=1, optimize=True)
    return _uri(buf.getvalue(), "image/jpeg")


def _scaled(img: Image.Image, width: int) -> Image.Image:
    return img.resize((width, round(width * img.height / img.width)), Image.LANCZOS)


def desktop_shot() -> str:
    """The complete app window, trimmed off the desktop wallpaper around it.

    Bounds are the window's own edges in dashboard.png; the crop is exactly
    1926x1350 (1.4267), which is the aspect the laptop screen is cut to."""
    img = Image.open(ASSETS / "dashboard.png").convert("RGB").crop((11, 15, 1937, 1365))
    return _png(_scaled(img, DESKTOP_W))


def reader_shot() -> str:
    img = Image.open(ASSETS / "koreader" / "save-word.png").convert("L")
    if _mean(img) > 128:
        raise SystemExit("koreader/save-word.png is still light — run tools/site/darken_eink.py")
    return _png(_scaled(img, READER_W))


def phone_shot() -> str:
    img = Image.open(ASSETS / "mobile" / "flashcards.jpg").convert("RGB")
    return _jpeg(_scaled(img, PHONE_W))


def _mean(img: Image.Image) -> float:
    hist = img.histogram()
    total = sum(hist)
    return sum(i * n for i, n in enumerate(hist)) / total if total else 0.0


def build(backdrop: bool) -> str:
    """`backdrop=False` drops the painted background, glows and vignette so the
    devices composite straight onto the page — which is what the site wants, since
    it paints its own background and radial glows behind .shot. Pass True for a
    standalone image that has to stand on its own."""
    DESKTOP, READER, PHONE = desktop_shot(), reader_shot(), phone_shot()
    BACKDROP = """
  <rect width="1200" height="700" fill="#0b0f17"/>
  <ellipse cx="600"  cy="255" rx="640" ry="440" fill="url(#bgGlow)"/>
  <ellipse cx="600"  cy="320" rx="440" ry="300" fill="url(#accentBlue)"/>
  <ellipse cx="195"  cy="415" rx="300" ry="245" fill="url(#accentWarm)"/>
  <ellipse cx="1015" cy="405" rx="255" ry="215" fill="url(#accentBlue)"/>""" if backdrop else ""
    VIGNETTE = ('\n  <rect width="1200" height="700" fill="url(#vignette)" pointer-events="none"/>'
                if backdrop else "")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="{VIEW_X} {VIEW_Y} {VIEW_W} {VIEW_H}" width="{VIEW_W * 2}" height="{VIEW_H * 2}" role="img"
     aria-label="Lingueez running on a laptop, an e-reader and a phone">
  <title>Lingueez — one vocabulary, every device</title>

  <defs>
    <!-- ── Backdrop ───────────────────────────────────────────────── -->
    <radialGradient id="bgGlow" cx="50%" cy="38%" r="62%">
      <stop offset="0%"   stop-color="#1b2536" stop-opacity="0.9"/>
      <stop offset="58%"  stop-color="#121a28" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#0b0f17" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="accentBlue" cx="50%" cy="50%" r="50%">
      <stop offset="0%"   stop-color="#3b82f6" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="accentWarm" cx="50%" cy="50%" r="50%">
      <stop offset="0%"   stop-color="#a78bfa" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#a78bfa" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="vignette" cx="50%" cy="45%" r="72%">
      <stop offset="55%"  stop-color="#000000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.55"/>
    </radialGradient>

    <!-- ── Materials ──────────────────────────────────────────────── -->
    <!-- anodised aluminium: the top edge catches the key light -->
    <linearGradient id="metal" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#3c4655"/>
      <stop offset="16%"  stop-color="#262e3a"/>
      <stop offset="82%"  stop-color="#1c222c"/>
      <stop offset="100%" stop-color="#2f3745"/>
    </linearGradient>
    <linearGradient id="metalEdge" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#6b788c" stop-opacity="0.95"/>
      <stop offset="40%"  stop-color="#3c4653" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#181d25" stop-opacity="0.9"/>
    </linearGradient>
    <!-- laptop deck seen edge-on: front lip catches light, body stays readable -->
    <linearGradient id="deck" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#6d7b8f"/>
      <stop offset="22%"  stop-color="#39424f"/>
      <stop offset="70%"  stop-color="#272f3b"/>
      <stop offset="100%" stop-color="#252c38"/>
    </linearGradient>
    <linearGradient id="hinge" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#0b0f16"/>
      <stop offset="100%" stop-color="#414c5c"/>
    </linearGradient>
    <!-- soft diagonal sheen laid over the glass -->
    <linearGradient id="sheen" x1="0" y1="0" x2="0.8" y2="1">
      <stop offset="0%"   stop-color="#ffffff" stop-opacity="0.08"/>
      <stop offset="32%"  stop-color="#ffffff" stop-opacity="0.02"/>
      <stop offset="60%"  stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <!-- ── Shadows ────────────────────────────────────────────────── -->
    <filter id="castLaptop" x="-25%" y="-25%" width="150%" height="165%">
      <feDropShadow dx="0" dy="32" stdDeviation="32" flood-color="#000" flood-opacity="0.55"/>
    </filter>
    <filter id="castSide" x="-45%" y="-25%" width="190%" height="165%">
      <feDropShadow dx="0" dy="24" stdDeviation="24" flood-color="#000" flood-opacity="0.65"/>
    </filter>
    <filter id="blurGround" x="-60%" y="-400%" width="220%" height="900%">
      <feGaussianBlur stdDeviation="13"/>
    </filter>

    <!-- ── Screen clips ───────────────────────────────────────────── -->
    <clipPath id="clipDesktop"><rect x="324" y="99"  width="552" height="387" rx="3"/></clipPath>
    <clipPath id="clipReader"> <rect x="87"  y="277" width="230" height="296" rx="3"/></clipPath>
    <clipPath id="clipPhone">  <rect x="927" y="262" width="158" height="335" rx="24"/></clipPath>
  </defs>

  <!-- ══ Backdrop (omitted when the host page paints its own) ══════ -->{BACKDROP}

  <g transform="translate(0,-4)">
    <!-- contact shadows on the implied floor -->
    <g filter="url(#blurGround)">
      <ellipse cx="600"  cy="531" rx="345" ry="9"  fill="#000" opacity="0.5"/>
      <ellipse cx="202"  cy="611" rx="128" ry="10" fill="#000" opacity="0.55"/>
      <ellipse cx="1006" cy="611" rx="88"  ry="10" fill="#000" opacity="0.55"/>
    </g>

    <!-- ══ 1 · LAPTOP — centre, back plane ══════════════════════════ -->
    <g filter="url(#castLaptop)">
      <!-- lid -->
      <rect x="313" y="88" width="574" height="418" rx="13" fill="url(#metal)"/>
      <rect x="313.8" y="88.8" width="572.4" height="416.4" rx="12.2" fill="none"
            stroke="url(#metalEdge)" stroke-width="1.6"/>
      <!-- glass well -->
      <rect x="321" y="96" width="558" height="393" rx="5" fill="#05070b"/>
      <!-- camera -->
      <circle cx="600" cy="92" r="2.4" fill="#3d4757"/>
      <circle cx="600" cy="92" r="0.9" fill="#66748a"/>

      <!-- screenshot -->
      <image xlink:href="{DESKTOP}" x="324" y="99" width="552" height="387"
             preserveAspectRatio="xMidYMid slice" clip-path="url(#clipDesktop)"/>
      <rect x="324" y="99" width="552" height="387" rx="3" fill="url(#sheen)"/>
      <rect x="324" y="99" width="552" height="387" rx="3" fill="none"
            stroke="#000" stroke-opacity="0.55" stroke-width="1"/>

      <!-- chin + hinge -->
      <rect x="321" y="489" width="558" height="8" fill="#151a23"/>
      <rect x="330" y="502" width="540" height="4" rx="1" fill="url(#hinge)"/>

      <!-- deck seen edge-on -->
      <path d="M 313 506 H 887 L 931 521 Q 939 523.5 931 523.5 H 269 Q 261 523.5 269 521 Z"
            fill="url(#deck)"/>
      <path d="M 314 506.7 H 886" stroke="#9dabc0" stroke-opacity="0.5" stroke-width="1.1"/>
      <path d="M 271 522.8 H 929" stroke="#0a0d12" stroke-opacity="0.7" stroke-width="1"/>
      <!-- front lip notch -->
      <path d="M 570 523.5 H 630 Q 626 529 618 529 H 582 Q 574 529 570 523.5 Z" fill="#0d1118"/>
    </g>

    <!-- ══ 2 · E-READER — left, front plane ═════════════════════════ -->
    <g filter="url(#castSide)">
      <rect x="74" y="264" width="256" height="340" rx="17" fill="url(#metal)"/>
      <rect x="74.8" y="264.8" width="254.4" height="338.4" rx="16.2" fill="none"
            stroke="url(#metalEdge)" stroke-width="1.6"/>
      <!-- e-ink well -->
      <rect x="85" y="275" width="234" height="300" rx="4" fill="#0a0a0a"/>

      <!-- night-mode screenshot; it letterboxes into its own black -->
      <image xlink:href="{READER}" x="87" y="277" width="230" height="296"
             preserveAspectRatio="xMidYMid meet" clip-path="url(#clipReader)"/>
      <rect x="87" y="277" width="230" height="296" rx="3" fill="url(#sheen)" opacity="0.65"/>
      <rect x="85" y="275" width="234" height="300" rx="4" fill="none"
            stroke="#000" stroke-opacity="0.6" stroke-width="1"/>

      <!-- chin detail -->
      <rect x="186" y="587" width="32" height="3" rx="1.5" fill="#414c5c" opacity="0.7"/>
    </g>

    <!-- ══ 3 · PHONE — right, front plane ═══════════════════════════ -->
    <g filter="url(#castSide)">
      <rect x="920" y="255" width="172" height="349" rx="30" fill="url(#metal)"/>
      <rect x="920.8" y="255.8" width="170.4" height="347.4" rx="29.2" fill="none"
            stroke="url(#metalEdge)" stroke-width="1.6"/>
      <!-- side buttons -->
      <rect x="1091"  y="313" width="2.6" height="38" rx="1.3" fill="#3c4655"/>
      <rect x="918.4" y="305" width="2.6" height="20" rx="1.3" fill="#3c4655"/>
      <rect x="918.4" y="333" width="2.6" height="32" rx="1.3" fill="#3c4655"/>

      <!-- display -->
      <rect x="927" y="262" width="158" height="335" rx="24" fill="#0b0b0d"/>
      <image xlink:href="{PHONE}" x="927" y="279" width="158" height="318"
             preserveAspectRatio="xMidYMid meet" clip-path="url(#clipPhone)"/>
      <rect x="927" y="262" width="158" height="335" rx="24" fill="url(#sheen)"/>
      <rect x="927" y="262" width="158" height="335" rx="24" fill="none"
            stroke="#000" stroke-opacity="0.6" stroke-width="1"/>

      <!-- dynamic island -->
      <rect x="977" y="268" width="58" height="14" rx="7" fill="#000"/>
      <circle cx="1027" cy="275" r="2.6" fill="#101822"/>
    </g>
  </g>
{VIGNETTE}
</svg>
"""


def main():
    backdrop = "--backdrop" in sys.argv
    svg = build(backdrop)
    (ASSETS / "hero.svg").write_text(svg)

    # width only: cairosvg derives the height from the viewBox, so no stretching
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=RASTER_W)
    (ASSETS / "hero.png").write_bytes(png)
    # keep RGBA — the transparent build relies on the alpha channel surviving
    Image.open(io.BytesIO(png)).save(
        ASSETS / "hero.webp", "WEBP", quality=86, method=6)

    with Image.open(io.BytesIO(png)) as raster:
        print(f"raster {raster.width}x{raster.height} — "
              f"use these as the <img> width/height in index.html")

    for name in ("hero.svg", "hero.png", "hero.webp"):
        path = ASSETS / name
        print(f"{path.relative_to(ROOT)}  {path.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
