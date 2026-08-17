#!/usr/bin/env python3
"""Microsoft Store listing images — `packaging/msix/store-listing/`.

Separate from the landing page on purpose. This script *imports* the device
geometry and materials from build_hero.py and writes nothing into `docs/`;
build_hero.py in turn knows nothing about this file. Run either one in any
order and the other's output does not move.

What it shares, and why: the laptop and phone are drawn from
``build_hero.laptop_body`` / ``phone_body`` against ``build_hero.DEFS``, so a
device in the Store is the same object as the device on the site. Redrawing it
here would be a second laptop that drifts from the first at the next tweak.

What it deliberately does not share: the stage. The site hero is a three-device
lineup at 1041x554; the Store wants 16:9 with the e-reader gone, so the frame,
the backdrop and the split are computed here.

The set
-------
``01-themes.png``  the teaser — one laptop crossed by a diagonal, dark theme on
                   the left, light on the right, plus the phone. The two halves
                   are the *same screenshot* rendered in both themes, so the
                   seam lands on the same row, the same glyph, on both sides.
                   That pixel-for-pixel agreement is the whole trick; it is why
                   this reads as one window shown twice rather than two images
                   badly stitched. Built by rendering the scene twice, wholly
                   dark and wholly light, and cross-fading the two rasters —
                   see seam_alpha(), which also explains why this cannot be an
                   SVG <mask>.
``02..``           one app window per feature, light theme, floating on a shared
                   canvas at the same size and position in every frame.

Microsoft's rules that shaped this (learn.microsoft.com "App screenshots,
images, and trailers"):

* Desktop shots are >=1366x768 PNG, <=50 MB, up to 10. Rendered at 2560x1440.
* "Keep critical visuals and text in the top two-thirds" — text overlays land on
  the bottom third. Every device sits in the upper two-thirds.
* "Don't use highly-contrasting stripes that may interfere with readability of
  text overlays." A hard dark/light diagonal is exactly such a stripe, so
  FLOOR_FADE converges both halves into one tone before the caption band starts.
* "Don't add additional logos, icons, or marketing messages to your
  screenshots." So nothing is captioned *in* the image — the copy goes in the
  Store's own 200-character caption field. CAPTIONS below is that text, written
  to captions.md beside the images.

    python3 tools/site/build_store_shots.py
"""
import base64
import io
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import cairosvg
from PIL import Image

if TYPE_CHECKING:                 # numpy is imported lazily, inside the two
    import numpy as np            # functions that need it — see seam_alpha()

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_hero as H          # geometry + materials, single source of truth

ROOT = H.ROOT
OUT = ROOT / "packaging" / "msix" / "store-listing"

# Every image is rendered to this height and lets its width follow its own
# content, so the set reads as one sequence in a carousel that scales to fit
# height. No image is forced to 16:9: the Store recommends that ratio but
# requires only >=1366x768, and honouring it costs dead canvas in every frame.
ROW_H = 1440

# build_hero draws everything inside translate(0, GROUP_DY); this file works in
# that same group-local space and only converts when computing the viewBox.
DY = H.GROUP_DY

# ── The teaser frame ─────────────────────────────────────────────────────────
# Ink is the laptop plus the phone (the e-reader is dropped for the Store: a
# KOReader plugin is not what a Windows customer is buying). Their union in
# stage units, with room under it for the contact shadows and their blur.
# The teaser is held to 16:9 — the ratio the Store lays out for, and the one a
# composed scene can absorb without waste showing. The plain shots are not; they
# size their canvas to their content (see MARGIN).
#
# Vertical padding is the input and width is derived from it, never the reverse.
# Solving the other way — fixing the width and letting height fall out — is what
# makes 16:9 eat the top and bottom bands, since this ink is wider than 16:9
# wants relative to its height. So the frame grows sideways to reach the ratio
# and these two numbers are whatever looks right above and below the devices.
TEASER_ASPECT = 16 / 9
PAD_TOP, PAD_BOTTOM = 18, 24

# Pushing the phone right widens the ink toward the frame's own aspect, which is
# the only way to buy back side margin without shrinking the devices. It costs
# the small overlap with the laptop deck that build_hero uses as a depth cue —
# affordable at two devices, where a clean gap reads as deliberate spacing
# rather than as a lineup with a hole in it.
PHONE_DX = 58

INK_X0, INK_X1 = H.BODY["laptop"][0], H.BODY["phone"][2] + PHONE_DX
INK_Y0, INK_Y1 = H.BODY["laptop"][1], 616                    # 88 .. floor + blur

# ── The seam ─────────────────────────────────────────────────────────────────
# Two anchors on the laptop screen, as a fraction of its 552x387 rect. The line
# through them is extended across the whole canvas.
#
# The angle is the design decision here. Near-vertical would run alongside the
# app's left nav rail and read as "this app has a dark sidebar" rather than as
# two themes. 45 degrees is the before/after-slider cliche and slices diagonally
# through every line of text. These anchors give ~22 degrees off vertical, which
# sweeps the seam across the Word and Translation columns — so the same word
# appears half dark, half light, which is the proof that it is one layout.
SEAM_TOP_F, SEAM_BOTTOM_F = 0.68, 0.40
SCREEN = (324, 99, 552, 387)                # x, y, w, h — matches clipDesktop

# How wide the two themes cross-fade, measured perpendicular to the seam.
#
# The backdrop can take a wide, soft blend: there is nothing there but colour,
# and softness is what stops the seam reading as a cut.
#
# The screen cannot take one at any width, and this is not a tuning problem. The
# halves are the same layout, so a cross-fade lays a light-on-dark glyph over a
# dark-on-light one at the identical position — the two converge on the same
# mid-grey as the paper behind them and the letter is *erased*. At 22 units
# "experience" rendered as "expe ience". So the screen gets 1.2 units, which is
# ~3px at output: an antialiased edge rather than a blend, crisp with no
# stair-stepping.
#
# What makes that hard edge read as deliberate instead of accidental is the
# accent hairline drawn along it — see seam_line(). Crisp where the content is,
# atmospheric where it is not; the bezel separates the two so they never meet.
BLEND_SCREEN, BLEND_BG = 1.2, 90

# The hairline along the screen's seam. Accent rather than white: white would be
# invisible against the light half, so the line would appear to emerge from the
# dark side and die halfway, which looks like a defect. A mid-blue holds against
# both. Drawn identically into both renders, so the composite leaves it exact.
SEAM_ACCENT = "#3b82f6"

# Where the two halves stop disagreeing. Below the laptop the backdrop converges
# to one tone, so the Store's caption band sits on flat colour instead of on a
# hard black/white edge.
#
# It has to *start* above the floor line, not at it: the contact shadows sit at
# y~531, and a black blurred ellipse dropped on a still-light backdrop reads as
# a grey shelf under the laptop rather than as a shadow. Beginning the fade at
# 460 means the floor is already half dark by the time the shadows land on it.
FADE_Y0, FADE_Y1 = 460, 585
FLOOR = "#0b0f17"

# ...and once the floor is dark, the site's contact shadows are far too heavy —
# those values are tuned to sit under a device on a near-black page.
GROUND_OPACITY = "0.34"

# The phone is wholly on the light side, so it carries the light theme. It shows
# practice rather than the word list: the laptop is already showing a table, and
# a second table beside it says nothing new — a flashcard mid-review says what
# the app is actually for.
PHONE_SCREEN = "mobile/flashcards"

DARK_BG = "#0b0f17"
LIGHT_BG = "#e9eef6"

# The device drop shadows in build_hero.DEFS carry dark-page values as their
# CSS-variable fallback (0.55 / 0.65), which is what cairosvg actually renders.
# Because the teaser is composited from a whole dark render and a whole light
# one, each can carry the shadow its own backdrop wants and the two blend along
# with everything else — no single compromise value that is too heavy on the
# light side and too weak on the dark.
SHADOW = {
    "dark":  {"var(--dev-shadow, 0.55)": "0.55", "var(--dev-shadow-side, 0.65)": "0.62"},
    "light": {"var(--dev-shadow, 0.55)": "0.26", "var(--dev-shadow-side, 0.65)": "0.20"},
}


def seam_line() -> str:
    """The hairline along the seam, clipped to the screen.

    A soft wide stroke under a crisp thin one: the glow gives the edge some
    depth on the dark side, the core keeps it legible on the light side. Both
    ends are extended past the screen rect so the line reaches into the corners
    rather than stopping a few pixels short of them.
    """
    sx, sy, sw, sh = SCREEN
    ex, ey = (SEAM_BOTTOM_F - SEAM_TOP_F) * sw, float(sh)
    n = (ex * ex + ey * ey) ** 0.5
    ox, oy = ex / n * 12, ey / n * 12
    x1, y1 = sx + SEAM_TOP_F * sw - ox, sy - oy
    x2, y2 = sx + SEAM_BOTTOM_F * sw + ox, sy + sh + oy
    coords = f'x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"'
    return (f'        <g clip-path="url(#clipDesktop)">\n'
            f'          <line {coords} stroke="{SEAM_ACCENT}" stroke-width="6" '
            f'stroke-opacity="0.13"/>\n'
            f'          <line {coords} stroke="{SEAM_ACCENT}" stroke-width="2.4" '
            f'stroke-opacity="0.22"/>\n'
            f'          <line {coords} stroke="{SEAM_ACCENT}" stroke-width="0.9" '
            f'stroke-opacity="0.75"/>\n'
            f'        </g>')


def view_box() -> tuple:
    """The 16:9 viewBox framing the laptop+phone ink, in *seen* coords.

    Height comes from the ink and its two vertical pads; width is then whatever
    16:9 asks of that height, centred on the ink. Side margin is therefore an
    output, not a setting — PHONE_DX is the lever that changes it, by widening
    the ink itself.
    """
    top, bottom = INK_Y0 + DY - PAD_TOP, INK_Y1 + DY + PAD_BOTTOM
    vh = bottom - top
    vw = vh * TEASER_ASPECT
    return (INK_X0 + INK_X1) / 2 - vw / 2, top, vw, vh


def seam_alpha(w: int, h: int) -> "np.ndarray":
    """Per-pixel weight of the light render, 0 (all dark) to 1 (all light).

    The blend is done here, on the rasters, rather than with an SVG <mask>:
    cairosvg parses masks and then ignores them — a masked white rect paints
    solid white — so a mask would have silently produced a fully light image.

    Distance is measured perpendicular to the seam, so the band keeps one width
    all the way down instead of widening as the line leans. Inside the laptop's
    screen rect the band narrows to BLEND_SCREEN; everywhere else it opens up to
    BLEND_BG. The step between the two falls exactly on the screen's edge, which
    is the bezel — and the bezel is identical in both renders, so the
    discontinuity has nothing to show itself on.
    """
    import numpy as np

    vx, vy, vw, vh = view_box()
    sx, sy, sw, sh = SCREEN

    # Pixel centres -> stage units. x needs no correction; y is drawn inside
    # translate(0, DY), so seen y is local y + DY.
    x = (vx + (np.arange(w) + 0.5) / w * vw)[None, :]
    y = (vy + (np.arange(h) + 0.5) / h * vh - DY)[:, None]

    dx = (SEAM_BOTTOM_F - SEAM_TOP_F) * sw          # seam direction, top to bottom
    dy = float(sh)
    length = (dx * dx + dy * dy) ** 0.5
    ux, uy = dy / length, -dx / length              # unit normal, pointing light-ward

    dist = (x - (sx + SEAM_TOP_F * sw)) * ux + (y - sy) * uy
    on_screen = (x >= sx) & (x <= sx + sw) & (y >= sy) & (y <= sy + sh)
    band = np.where(on_screen, BLEND_SCREEN, BLEND_BG)
    return np.clip(0.5 + dist / band, 0.0, 1.0)


def _uri(data: bytes, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


def shot(stem: str, theme: str, width: int, aspect: float = None) -> str:
    """One screenshot as an embedded data URI. Store images are single sealed
    PNGs — nothing can be an external href the way the site's hero screens are."""
    img = Image.open(H._resolve(stem, theme)).convert("RGB")
    if aspect:
        img = H._pad_to_aspect(img, aspect)
    buf = io.BytesIO()
    H._scaled(img, width).save(buf, "PNG", optimize=True)
    return _uri(buf.getvalue(), "image/png")


def swap_screen(body: str, marker: str, replacement: str) -> str:
    """Replace the screen build_hero drew into a device body with our own.

    build_hero's sealed-image path (``embed=True``) always embeds the *dark*
    variant — correct for a social card, wrong here, where one device is split
    across both themes and the other is light. Everything else about the body —
    bezel, buttons, sheen, camera — is kept exactly as the site draws it, so the
    swap is surgical: cut from the first <image> up to the sheen overlay, which
    is the first element painted on top of the screen.
    """
    head, tail = body.split(marker)
    return f"{head[:head.index('        <image')]}{replacement}\n        {marker}{tail}"


def ground() -> str:
    """The contact shadows, retuned and with the phone's moved to stay under the
    phone — it is drawn at PHONE_DX, and a shadow left behind would read as a
    smudge on the floor beside it."""
    out = []
    for k in ("laptop", "phone"):
        ellipse = (H.GROUND[k].replace('opacity="0.5"', f'opacity="{GROUND_OPACITY}"')
                              .replace('opacity="0.55"', f'opacity="{GROUND_OPACITY}"'))
        if k == "phone":
            ellipse = f'      <g transform="translate({PHONE_DX},0)">\n  {ellipse}\n      </g>'
        out.append(ellipse)
    return "\n".join(out)


def defs(theme: str) -> str:
    """build_hero's materials, with the drop shadows retuned for this theme's
    backdrop. Textual substitution rather than an override block: SVG has no
    cascade for duplicate ids, so a second <filter id="castLaptop"> would be
    ignored by some renderers and honoured by others."""
    out = H.DEFS
    for var, value in SHADOW[theme].items():
        out = out.replace(var, value)
    return out


# ═════════════════════════════════════════════════════════════════════════════
# 01 — the teaser
# ═════════════════════════════════════════════════════════════════════════════
# The two backdrops the composite fades between. The light one's glows are
# pushed right of centre and the dark one's left, so each is brightest on the
# side of the frame it actually survives into — a glow centred on the laptop
# would spend most of its strength under whichever half gets faded away.
BACKDROP = {
    "dark": f"""    <rect x="-2000" y="-2000" width="6000" height="6000" fill="{DARK_BG}"/>
    <ellipse cx="600" cy="255" rx="640" ry="440" fill="url(#bgGlow)"/>
    <ellipse cx="600" cy="320" rx="440" ry="300" fill="url(#accentBlue)"/>""",
    "light": f"""    <rect x="-2000" y="-2000" width="6000" height="6000" fill="{LIGHT_BG}"/>
    <ellipse cx="820" cy="300" rx="620" ry="430" fill="url(#lightGlow)"/>
    <ellipse cx="1000" cy="360" rx="380" ry="300" fill="url(#accentBlue)"/>""",
}
def teaser(theme: str) -> str:
    """One whole-theme render of the teaser. Two of these — "dark" and "light" —
    are composited by seam_alpha() into the finished image. Everything except
    the backdrop, the laptop's screen and the shadow weights is identical
    between them, so the cross-fade moves the theme without moving a glyph."""
    vx, vy, vw, vh = view_box()
    sx, sy, sw, sh = SCREEN

    laptop = swap_screen(
        H.laptop_body(embed=True),
        f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="3" fill="url(#sheen)"/>',
        f'        <image xlink:href="{shot("shots/words", theme, 1400, sw / sh)}"\n'
        f'               x="{sx}" y="{sy}" width="{sw}" height="{sh}"\n'
        f'               preserveAspectRatio="xMidYMid slice" clip-path="url(#clipDesktop)"/>\n'
        + seam_line())

    # The phone sits wholly to the right of the seam at every y it occupies, so
    # it is light-theme throughout — no split, nothing to align.
    phone = swap_screen(
        H.phone_body(embed=True, solo=True),
        '<rect x="927" y="262" width="158" height="335" rx="24" fill="url(#sheen)"/>',
        f'        <image xlink:href="{shot(PHONE_SCREEN, "light", 420, 158 / 335)}"\n'
        f'               x="927" y="262" width="158" height="335"\n'
        f'               preserveAspectRatio="xMidYMid slice" clip-path="url(#clipPhone)"/>')

    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="{vx:.1f} {vy:.1f} {vw:.1f} {vh:.1f}"
     width="{round(ROW_H * vw / vh)}" height="{ROW_H}"
     role="img" aria-label="Lingueez in dark and light themes, with the Android app">
{defs(theme)}
  <defs>
    <radialGradient id="lightGlow" cx="50%" cy="42%" r="60%">
      <stop offset="0%"   stop-color="#ffffff" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="floorFade" x1="0" y1="{FADE_Y0}" x2="0" y2="{FADE_Y1}"
                    gradientUnits="userSpaceOnUse">
      <stop offset="0%"   stop-color="{FLOOR}" stop-opacity="0"/>
      <stop offset="100%" stop-color="{FLOOR}" stop-opacity="1"/>
    </linearGradient>
  </defs>

  <g transform="translate(0,{DY})">
    <!-- ══ Backdrop, this render's theme throughout ════════════════ -->
{BACKDROP[theme]}
    <!-- Both halves converge before the caption band. See FADE_Y0. -->
    <rect x="-2000" y="{FADE_Y0}" width="6000" height="{FADE_Y1 - FADE_Y0 + 2000}"
          fill="url(#floorFade)"/>

    <!-- ══ Contact shadows ══════════════════════════════════════════ -->
    <g filter="url(#blurGround)">
{ground()}
    </g>

    <!-- ══ Devices ══════════════════════════════════════════════════ -->
    <g filter="url(#castLaptop)">
{laptop}
    </g>
    <g filter="url(#castSide)" transform="translate({PHONE_DX},0)">
{phone}
    </g>
  </g>
</svg>
"""


# ═════════════════════════════════════════════════════════════════════════════
# 02.. — one app window per feature
# ═════════════════════════════════════════════════════════════════════════════
# The app window is 1.427:1 and the Store frame is 16:9, so something has to
# give. Letterboxing with black bars looks like a mistake; cropping loses the
# chrome that says "this is a real Windows app". Instead the window floats,
# shadowed, on the teaser's own light backdrop — the aspect mismatch becomes
# margin, and the frames read as one set because the canvas never moves.
# These do not use 16:9, and that is the point. 16:9 is what the Store
# *recommends*; what it requires is >=1366x768 PNG. Forcing a 1.4264 window into
# a 1.7778 frame costs ~13% dead canvas down each side that no amount of
# nudging removes — it is the aspect gap, not slack. So the canvas is derived
# from the window instead of the other way round: one uniform MARGIN on all four
# sides, and whatever aspect that lands on.
#
# Uniform means uniform in stage units, so the band looks the same width at the
# top, the bottom and both sides. Matching it proportionally instead would make
# the side bands visibly wider than the top one.
WIN_H = 624
WIN_W = WIN_H * (552 / 387)               # the site's window aspect, shared
MARGIN = 40
PLAIN = (WIN_W + 2 * MARGIN, WIN_H + 2 * MARGIN)
WIN_X = WIN_Y = MARGIN

# With a margin this tight the drop shadow has to live inside it, or it is
# sliced off square at the canvas edge and reads as a printing error. Its reach
# (dy + ~3 sigma) is held just under MARGIN.
SHADOW_DY, SHADOW_BLUR = 8, 9

# The plain shots need a deeper ground than the teaser's light half: the app in
# light theme is nearly white, and on the teaser's #e9eef6 the window edge
# dissolved into the backdrop. This is far enough down to hold an edge without
# competing with the screenshot.
PLAIN_BG = "#d7e1f0"

SHOTS = [
    ("02-words",      "shots/words",        "Your whole vocabulary in one searchable table."),
    ("03-review",     "shots/review",       "Spaced-repetition review that schedules itself."),
    ("04-flashcards", "shots/flashcards",   "Build decks from the words you actually saved."),
    ("05-quiz",       "shots/quiz-choices", "Quiz yourself on your own words — multiple choice, "
                                            "in either direction."),
    ("06-quiz-typed", "shots/quiz-typing",  "Or type the answer and have it checked, with the "
                                            "definition and an example when you are right."),
    ("07-stats",      "shots/stats",        "See what is sticking and what needs work."),
    ("08-texts",      "shots/texts",        "Read real texts and save words as you go."),
]

CAPTIONS = {
    # Deliberately not "the same words on both screens": the phone shot is a
    # real capture with its own list, and a caption that invites the comparison
    # loses it. The claim made here is sync, which is true.
    "01-themes": "Light and dark themes, and your vocabulary on your phone too "
                 "— it syncs with the free Lingueez app for Android.",
}


def plain(stem: str) -> str:
    w, h = PLAIN
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {w:.1f} {h:.1f}" width="{round(ROW_H * w / h)}" height="{ROW_H}" role="img">
  <defs>
    <radialGradient id="lightGlow" cx="50%" cy="36%" r="58%">
      <stop offset="0%"   stop-color="#ffffff" stop-opacity="0.72"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="tint" cx="50%" cy="50%" r="50%">
      <stop offset="0%"   stop-color="#3b82f6" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/>
    </radialGradient>
    <filter id="winShadow" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="{SHADOW_DY}" stdDeviation="{SHADOW_BLUR}"
                    flood-color="#16233b" flood-opacity="0.30"/>
    </filter>
    <clipPath id="clipWin">
      <rect x="{WIN_X:.1f}" y="{WIN_Y}" width="{WIN_W:.1f}" height="{WIN_H}" rx="10"/>
    </clipPath>
  </defs>

  <rect width="{w:.1f}" height="{h:.1f}" fill="{PLAIN_BG}"/>
  <ellipse cx="{w / 2:.0f}" cy="{h * 0.42:.0f}" rx="{w * 0.55:.0f}" ry="{h * 0.62:.0f}"
           fill="url(#lightGlow)"/>
  <ellipse cx="{w * 0.5:.0f}" cy="{h * 0.52:.0f}" rx="{w * 0.42:.0f}" ry="{h * 0.45:.0f}"
           fill="url(#tint)"/>

  <g filter="url(#winShadow)">
    <rect x="{WIN_X:.1f}" y="{WIN_Y}" width="{WIN_W:.1f}" height="{WIN_H}" rx="10"
          fill="#ffffff"/>
    <image xlink:href="{shot(stem, 'light', 1850, WIN_W / WIN_H)}"
           x="{WIN_X:.1f}" y="{WIN_Y}" width="{WIN_W:.1f}" height="{WIN_H}"
           preserveAspectRatio="xMidYMid slice" clip-path="url(#clipWin)"/>
    <rect x="{WIN_X:.1f}" y="{WIN_Y}" width="{WIN_W:.1f}" height="{WIN_H}" rx="10"
          fill="none" stroke="#0b1220" stroke-opacity="0.14" stroke-width="1"/>
  </g>
</svg>
"""


def rasterise(svg: str) -> Image.Image:
    # No output_width/height override: each SVG declares its own, because the
    # teaser and the plain shots deliberately do not share an aspect.
    png = cairosvg.svg2png(bytestring=svg.encode())
    # cairosvg writes RGBA; the Store wants an opaque frame, and a stray alpha
    # channel would let its page background show through the corners.
    return Image.open(io.BytesIO(png)).convert("RGB")


def save(name: str, img: Image.Image) -> None:
    dst = OUT / f"{name}.png"
    img.save(dst, "PNG", optimize=True)
    print(f"  {dst.relative_to(ROOT)}  {img.width}x{img.height}  "
          f"{dst.stat().st_size / 1024:.0f} KB")


def render(name: str, svg: str) -> None:
    save(name, rasterise(svg))


def render_teaser(name: str) -> None:
    """Rasterise both themes at full size and cross-fade them along the seam."""
    import numpy as np

    dark = np.asarray(rasterise(teaser("dark")), dtype=np.float32)
    light = np.asarray(rasterise(teaser("light")), dtype=np.float32)
    if dark.shape != light.shape:                    # cannot happen; cheap to prove
        raise SystemExit(f"teaser renders disagree: {dark.shape} vs {light.shape}")
    a = seam_alpha(dark.shape[1], dark.shape[0])[..., None]
    blended = np.clip(dark * (1.0 - a) + light * a + 0.5, 0, 255).astype(np.uint8)
    save(name, Image.fromarray(blended, "RGB"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"store listing images (PNG, {ROW_H}px tall, >= 1366x768):")
    render_teaser("01-themes")
    for name, stem, _caption in SHOTS:
        render(name, plain(stem))

    captions = dict(CAPTIONS, **{n: c for n, _s, c in SHOTS})
    lines = ["# Store listing captions", "",
             "Paste into Partner Center -> Store listings -> Screenshots. The Store",
             "renders these as an overlay on the bottom third of each image, which is",
             "why no copy is baked into the artwork. 200 characters max.", ""]
    for name in ["01-themes"] + [n for n, _s, _c in SHOTS]:
        lines.append(f"- **{name}.png** — {captions[name]}")
    (OUT / "captions.md").write_text("\n".join(lines) + "\n")
    print(f"  {(OUT / 'captions.md').relative_to(ROOT)}")

    if H._missing:
        print("\nfell back to the other theme:", file=sys.stderr)
        for m in dict.fromkeys(H._missing):
            print(f"  {m}", file=sys.stderr)


if __name__ == "__main__":
    main()
