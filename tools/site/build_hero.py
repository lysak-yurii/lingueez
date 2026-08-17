#!/usr/bin/env python3
"""Build the landing-page hero: three devices carrying real product screenshots.

Two different things come out of here, and they are not interchangeable.

**The stage** — ``docs/_includes/hero-stage.html``. Markup only (~12 KB),
inlined into the page. It is the inline SVG plus a focusable ``.dev-hit``
button positioned over each device, because an SVG ``<g tabindex="0">`` is not
actually focusable. Each screen is an external ``<image href>`` so the
screenshots cache separately and swap with the theme. This is what visitors
load; behaviour lives in ``docs/assets/hero.js``.

**The social card** — ``docs/assets/hero.{svg,png,webp}``. One sealed image with
the screenshots embedded as data URIs and a painted backdrop, because Open
Graph cannot reference a page's CSS or its external assets. Dark only; that is
what a link preview should look like.

Sources
-------
``docs/assets/shots/words-{light,dark}.png``       laptop  (tools/site/capture_shots.py)
``docs/assets/koreader/save-word-{light,dark}.png`` e-reader (tools/site/eink_theme.py)
``docs/assets/mobile/flashcards{,-light}.jpg``      phone   (captured by hand)

A missing light variant falls back to the dark one and is reported, so the
build never fails just because one shot has not been taken yet.

Layout
------
* The laptop stays dead-centre (x=600) — that is what reads as a "standard" hero.
* Both side devices live in the front plane: each overlaps the laptop by a small
  amount (reader -> lid bezel, phone -> deck corner) and their bottom edges share
  one floor line at y=604. That overlap + drop is what sells the depth.
* The e-reader is the heavier side device, so the right margin is ~35px wider
  than the left: optical balance rather than geometric.
* Screen rects match their screenshot's aspect, so nothing is cropped at all.
  The laptop's 552x387 (1.4264) is why capture_shots.py derives its window
  height from that ratio rather than picking a round number.

    python3 tools/site/build_hero.py
"""
import base64
import io
import sys
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "docs" / "assets"
HERO = ASSETS / "hero"
INCLUDES = ROOT / "docs" / "_includes"

# The laptop screen is 552x387 in SVG units and the hero renders at up to ~2x,
# so ~1200px of source is as much detail as the screen can ever show.
DESKTOP_W, READER_W, PHONE_W = 1200, 520, 340
RASTER_W = 1600

# The devices are laid out on a 1200x700 stage but only ink x 73.5..1093.5 /
# y 83.2..616.5 of it. Publishing the whole stage would waste ~25% of the image
# on empty margin and shrink the devices for a given column width, so the view
# is cropped to the ink plus a little breathing room for the shadows.
VIEW_X, VIEW_Y, VIEW_W, VIEW_H = 63, 73, 1041, 554

# Everything in the stage is drawn inside a translate(0,-4) wrapper.
GROUP_DY = -4

# The bounding box of each device *body* in stage units: (x0, y0, x1, y1).
# The hotspot buttons are derived from these, so the geometry has one home —
# an SVG <g tabindex="0"> is not focusable (Chromium leaves activeElement on
# <body> and Tab skips it), so the keyboard-reachable control has to be real
# HTML sitting over the artwork.
BODY = {
    "laptop": (269, 88, 931, 529),      # lid plus the deck seen edge-on
    "reader": (74, 264, 330, 604),
    "phone": (918.4, 255, 1093.6, 604),
}

# Accessible names, bilingual — these are real HTML, so they can use the same
# <span lang> pairs as the rest of the site instead of a JS lookup.
NAMES = {
    "laptop": ("Lingueez on the desktop app", "Lingueez на комп’ютері"),
    "reader": ("Lingueez on an e-reader", "Lingueez на е-читачі"),
    "phone": ("Lingueez on a phone", "Lingueez на смартфоні"),
}

# Screen rect aspect per device, from the clipPaths below. A source is padded
# to this — never cropped — so it fills the screen without letterboxing.
RECT = {"desktop": 552 / 387, "reader": 230 / 296, "phone": 158 / 335}

# What each device can show, in the order the switcher steps through them.
# (key, English label, Ukrainian label, path stem under docs/assets).
#
# Only sources whose own aspect is close to the screen's are listed: padding a
# 1.65 shot into a 1.43 screen would band it top and bottom and read as the app
# failing to fill the window. That is why the e-reader menu is left out — "Save
# a word" covers the same ground at the right shape. The desktop deck preview
# used to be excluded for the same reason; capture_shots.fit_whole_rows() now
# holds it to the site's aspect, so it belongs here.
SCREENS = {
    "desktop": [
        ("words",      "Your vocabulary",   "Ваш словник",             "shots/words"),
        ("flashcards", "Build a deck",      "Створіть колоду",         "shots/flashcards"),
        ("review",     "Practise a deck",   "Практика колоди",          "shots/review"),
        # Same label as the phone's quiz screen, which is the point: keys collapse
        # on their English text, so this costs no new translation.
        ("quiz",       "Test yourself",     "Перевірте себе",           "shots/quiz-choices"),
        ("texts",      "Read real texts",   "Читайте справжні тексти",  "shots/texts"),
        ("stats",      "See your progress", "Дивіться свій прогрес",    "shots/stats"),
    ],
    "reader": [
        ("save",  "Save a word from a book",  "Збережіть слово з книжки", "koreader/save-word"),
        ("words", "Browse your saved words",  "Перегляд збережених слів", "koreader/view-words"),
        ("cards", "Flashcards on the device", "Флешкартки на пристрої",   "koreader/flashcards"),
    ],
    "phone": [
        ("today",    "Today at a glance",     "Огляд дня",              "mobile/today"),
        ("words",    "Your vocabulary",       "Ваш словник",            "mobile/words"),
        ("cards",    "Review in your pocket", "Повторення в кишені",    "mobile/flashcards"),
        ("quiz",     "Test yourself",         "Перевірте себе",         "mobile/quiz"),
        ("listen",   "Listen hands-free",     "Слухайте на ходу",       "mobile/listen"),
        ("progress", "See your progress",     "Дивіться свій прогрес",  "mobile/progress"),
    ],
}

# Which screen a device shows before anyone touches it, when that should not be
# the first of the walk. The phone's list runs in the app's own bottom-nav order
# — Today, Words, Practice… — but on the shared hero the flashcard is what it
# should open on: among three devices it has one frame to say what the app is
# for, and Today is a dashboard of numbers that means little on sight.
#
# Not on the device's own page, though: there the heading has already said this
# is the Android app, so the walk can start where the app itself does.
START = {"phone": "cards"}


def start_index(device: str, solo: bool = False) -> int:
    want = None if solo else START.get(device)
    keys = [s[0] for s in SCREENS[device]]
    return keys.index(want) if want in keys else 0


# Where "read more" goes for each device, and what the link says. The desktop
# app has no page of its own — this whole site is its page — so it points at
# the feature list rather than inventing a destination.
# The link sits on the same line as the device name, in bold, a few words to
# its left — so naming the device again ("Explore the e-reader plugin") only
# spends width. Ukrainian runs ~40% longer than English and that line also
# carries the screen label and the dots; at the full name it needed ~700px in a
# column that is 534-717px wide, and wrapped.
MORE = {
    "desktop": ("/#features", "See all features", "Усі можливості"),
    "reader":  ("/koreader/", "More about the e-reader", "Детальніше про плагін"),
    "phone":   ("/mobile/",   "More about Android", "Детальніше про застосунок"),
}

# How wide each device's screen images are written.
SCREEN_W = {"desktop": DESKTOP_W, "reader": READER_W, "phone": PHONE_W}

# The "this is your device" glow. It is derived from the device box rather
# than hand-placed, and clamped inside the viewBox: the stage is overflow
# visible (so the hover lift and the maximised device are never cut off), which
# means anything spilling sideways would widen the page itself.
HALO_SPREAD = 1.3        # how far past the device the glow reaches
HALO_MARGIN = 6          # and how far inside the viewBox it must stay


def halo(name: str) -> str:
    x0, y0, x1, y1 = BODY[name]
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    seen_y = cy + GROUP_DY          # where it actually lands once translated
    rx = min((x1 - x0) / 2 * HALO_SPREAD,
             cx - (VIEW_X + HALO_MARGIN), (VIEW_X + VIEW_W - HALO_MARGIN) - cx)
    ry = min((y1 - y0) / 2 * HALO_SPREAD,
             seen_y - (VIEW_Y + HALO_MARGIN), (VIEW_Y + VIEW_H - HALO_MARGIN) - seen_y)
    return (f'cx="{cx:.0f}" cy="{cy:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" '
            f'fill="url(#haloPaint)"')


def _t(s):
    """A translated string in the stage markup. The Ukrainian in the tables
    above is the seed for tools/site/i18n.py; the pages look it up by English."""
    return "{%% include t.html s='%s' %%}" % s


_missing = []


def _scaled(img: Image.Image, width: int) -> Image.Image:
    height = round(img.height * width / img.width)
    return img.resize((width, height), Image.LANCZOS)


def _resolve(stem: str, theme: str) -> Path:
    """The file for one screen+theme.

    Tries `<stem>-<theme>.(png|jpg)`, then the other theme, then the bare stem —
    so a source that has never been themed (the phone shot) still works and is
    reported rather than failing the build.
    """
    other = "dark" if theme == "light" else "light"
    for suffix in (f"-{theme}", f"-{other}", ""):
        for ext in (".png", ".jpg", ".webp"):
            path = ASSETS / f"{stem}{suffix}{ext}"
            if path.exists():
                if suffix != f"-{theme}":
                    _missing.append(f"{stem} {theme}: using {path.relative_to(ROOT)}")
                return path
    raise SystemExit(f"no source for {stem} ({theme})")


def _pad_to_aspect(img: Image.Image, aspect: float) -> Image.Image:
    """Grow the canvas to `aspect` without cropping, filling with the image's
    own border colour so the pad is invisible against the screenshot's edge."""
    want_w, want_h = img.width, img.height
    if img.width / img.height > aspect:
        want_h = round(img.width / aspect)
    else:
        want_w = round(img.height * aspect)
    if (want_w, want_h) == (img.width, img.height):
        return img
    # The image's most common colour, which for every source here is the page
    # behind the content. Sampling the outermost row instead would pick up the
    # e-ink screenshots' black frame border and pad the page with black.
    small = img.resize((64, 64), Image.NEAREST)
    fill = max(small.getcolors(64 * 64), key=lambda c: c[0])[1]
    out = Image.new("RGB", (want_w, want_h), fill)
    out.paste(img, ((want_w - img.width) // 2, (want_h - img.height) // 2))
    return out


def write_screens() -> None:
    """Pad and scale every screen into the exact rect it occupies, as WebP the
    page fetches directly."""
    HERO.mkdir(parents=True, exist_ok=True)
    # Clear first: the filenames encode the screen set, so renaming or dropping
    # a screen would otherwise leave an orphan behind for good.
    for stale in HERO.glob("*.webp"):
        stale.unlink()
    total = 0
    for device, screens in SCREENS.items():
        for key, _en, _uk, stem in screens:
            for theme in ("light", "dark"):
                img = Image.open(_resolve(stem, theme)).convert("RGB")
                img = _pad_to_aspect(img, RECT[device])
                dst = HERO / f"{device}-{key}-{theme}.webp"
                _scaled(img, SCREEN_W[device]).save(dst, "WEBP", quality=88, method=6)
                total += dst.stat().st_size
    n = sum(len(s) for s in SCREENS.values()) * 2
    print(f"  {n} screen images in docs/assets/hero/  {total / 1024:.0f} KB total")


# --------------------------------------------------------------------------- #
# data URIs — social card only
# --------------------------------------------------------------------------- #
def _uri(data: bytes, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


def _embedded(device: str) -> str:
    """The device's first screen as a data URI, for the self-contained social
    card. The card is a single fixed image, so it only ever shows screen one."""
    stem = SCREENS[device][0][3]
    img = Image.open(_resolve(stem, "dark")).convert("RGB")
    img = _scaled(_pad_to_aspect(img, RECT[device]), SCREEN_W[device])
    buf = io.BytesIO()
    if device == "phone":
        img.save(buf, "JPEG", quality=88, subsampling=1, optimize=True)
        return _uri(buf.getvalue(), "image/jpeg")
    img.save(buf, "PNG", optimize=True)
    return _uri(buf.getvalue(), "image/png")


# --------------------------------------------------------------------------- #
# markup
# --------------------------------------------------------------------------- #
def _screen(device: str, x, y, w, h, clip, embed: bool, fit="slice", start=0) -> str:
    """The screen image(s) for one device.

    Inline: four <image> elements. One pair per theme, toggled by the
    .only-light / .only-dark utilities in site.css — light-dark() handles every
    colour on the site but it cannot swap a raster, so this is the one thing it
    cannot cover.

    Within a theme the pair is a double buffer. Changing an <image>'s href makes
    the element reload that resource even when it is already in the HTTP cache,
    and it paints nothing until that finishes — a visible blank flash on the
    first pass through the screens, which is why the flicker stops once every
    screen has been shown once and is in the memory cache. So hero.js never
    touches the href of a visible element: it loads into the buffer behind and
    cross-fades once that has fired `load`.

    Social card: a single embedded dark image.
    """
    common = (f'x="{x}" y="{y}" width="{w}" height="{h}" '
              f'preserveAspectRatio="xMidYMid {fit}" clip-path="url(#{clip})"')
    if embed:
        return f'<image xlink:href="{_embedded(device)}" {common}/>'
    # The resting screen — usually the first of the walk, see START. The back
    # buffers start empty; hero.js fills whichever is behind when the switcher
    # moves.
    first = SCREENS[device][start][0]
    out = []
    for theme in ("light", "dark"):
        out.append(f'<image class="screen only-{theme}" '
                   f'href="/assets/hero/{device}-{first}-{theme}.webp" {common}/>')
        out.append(f'<image class="screen only-{theme} is-back" {common}/>')
    return "\n      ".join(out)


# The contact shadow each device casts on the implied floor.
GROUND = {
    "laptop": '      <ellipse cx="600"  cy="531" rx="345" ry="9"  fill="#000" opacity="0.5"/>',
    "reader": '      <ellipse cx="202"  cy="611" rx="128" ry="10" fill="#000" opacity="0.55"/>',
    "phone":  '      <ellipse cx="1006" cy="611" rx="88"  ry="10" fill="#000" opacity="0.55"/>',
}

# How much room a solo stage leaves around its one device, as a fraction of the
# device box. Generous below, where the contact shadow and its blur land.
SOLO_PAD = (0.12, 0.10, 0.17)      # sides, top, bottom


def solo_view(device: str) -> tuple:
    """viewBox for a stage holding only `device`, framed on that device."""
    x0, y0, x1, y1 = BODY[device]
    w, h = x1 - x0, y1 - y0
    sx, st, sb = SOLO_PAD
    return (x0 - w * sx, y0 + GROUP_DY - h * st,
            w * (1 + 2 * sx), h * (1 + st + sb))


def solo_width(device: str) -> float:
    """How wide a solo stage must be, as a fraction of its column.

    A solo device has to come out the same size as that device maximised on the
    home page, or the two heroes disagree about how big a phone is. Maximising
    fits the device body to the stage: both side devices are taller than they
    are wide, so height is the limit and the body ends up exactly VIEW_H tall,
    which renders at VIEW_H / VIEW_W of the column width.

    The solo stage frames the same body inside its own padded viewBox, so ask
    for the width that lands the body at that same height. Derived rather than
    tuned by eye, and it tracks the column at every viewport the way the home
    stage does — a viewport-height cap would not.
    """
    _, _, vw, _ = solo_view(device)
    _, y0, _, y1 = BODY[device]
    # The SVG scales uniformly by width/vw, so a body of `y1-y0` user units
    # draws at (y1-y0) * width/vw px. Solve that for the width.
    return VIEW_H / VIEW_W * vw / (y1 - y0)


def laptop_body(embed: bool) -> str:
    return f"""        <!-- lid -->
        <rect x="313" y="88" width="574" height="418" rx="13" fill="url(#metal)"/>
        <rect x="313.8" y="88.8" width="572.4" height="416.4" rx="12.2" fill="none"
              stroke="url(#metalEdge)" stroke-width="1.6"/>
        <!-- glass well -->
        <rect x="321" y="96" width="558" height="393" rx="5" fill="#05070b"/>
        <!-- camera -->
        <circle cx="600" cy="92" r="2.4" fill="#3d4757"/>
        <circle cx="600" cy="92" r="0.9" fill="#66748a"/>

        {_screen("desktop", 324, 99, 552, 387, "clipDesktop", embed)}
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
        <path d="M 570 523.5 H 630 Q 626 529 618 529 H 582 Q 574 529 570 523.5 Z" fill="#0d1118"/>"""


def reader_body(embed: bool) -> str:
    return f"""        <rect x="74" y="264" width="256" height="340" rx="17" fill="url(#metal)"/>
        <rect x="74.8" y="264.8" width="254.4" height="338.4" rx="16.2" fill="none"
              stroke="url(#metalEdge)" stroke-width="1.6"/>
        <!-- e-ink well. Matches eink_theme.DARK_BG so the screen and the page
             printed on it are one colour rather than two that nearly agree,
             and matches the app's own background token. Not lifted further:
             the metal gradient bottoms out at #1c222c, and a screen at that
             value stops reading as recessed. -->
        <rect x="85" y="275" width="234" height="300" rx="4" fill="#101418"/>

        {_screen("reader", 87, 277, 230, 296, "clipReader", embed, fit="meet")}
        <rect x="87" y="277" width="230" height="296" rx="3" fill="url(#sheen)" opacity="0.65"/>
        <rect x="85" y="275" width="234" height="300" rx="4" fill="none"
              stroke="#000" stroke-opacity="0.6" stroke-width="1"/>

        <!-- chin detail -->
        <rect x="186" y="587" width="32" height="3" rx="1.5" fill="#414c5c" opacity="0.7"/>"""


def phone_body(embed: bool, solo: bool = False) -> str:
    return f"""        <rect x="920" y="255" width="172" height="349" rx="30" fill="url(#metal)"/>
        <rect x="920.8" y="255.8" width="170.4" height="347.4" rx="29.2" fill="none"
              stroke="url(#metalEdge)" stroke-width="1.6"/>
        <!-- side buttons -->
        <rect x="1091"  y="313" width="2.6" height="38" rx="1.3" fill="#3c4655"/>
        <rect x="918.4" y="305" width="2.6" height="20" rx="1.3" fill="#3c4655"/>
        <rect x="918.4" y="333" width="2.6" height="32" rx="1.3" fill="#3c4655"/>

        <!-- display -->
        <rect x="927" y="262" width="158" height="335" rx="24" fill="#0b0b0d"/>
        {_screen("phone", 927, 262, 158, 335, "clipPhone", embed, fit="slice",
                 start=start_index("phone", solo))}
        <rect x="927" y="262" width="158" height="335" rx="24" fill="url(#sheen)"/>
        <rect x="927" y="262" width="158" height="335" rx="24" fill="none"
              stroke="#000" stroke-opacity="0.6" stroke-width="1"/>

        <!-- punch-hole camera, centred: the pill-shaped island reads as one
             specific phone and takes a bite out of the screenshot behind it.
             A single hole is what most phones have and barely covers anything. -->
        <circle cx="1006" cy="272" r="3.1" fill="#05070a"/>
        <circle cx="1006" cy="272" r="1.7" fill="#18222f"/>
        <circle cx="1005.2" cy="271.2" r="0.6" fill="#4a5a70" opacity="0.7"/>"""


# The gradients, filters and screen clips every stage draws with. Module level so
# other generators (tools/site/build_store_shots.py) paint devices out of the same
# materials as the site — a device that looks different in the Store than on the
# landing page is a device drawn twice.
DEFS = """  <defs>
    <!-- ── Backdrop (social card only) ────────────────────────────── -->
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
    <!-- the "this is your device" bloom; tinted from the page's accent -->
    <radialGradient id="haloPaint" cx="50%" cy="50%" r="50%">
      <stop offset="0%"   stop-color="currentColor" stop-opacity="0.42"/>
      <stop offset="65%"  stop-color="currentColor" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="currentColor" stop-opacity="0"/>
    </radialGradient>

    <!-- ── Materials ──────────────────────────────────────────────── -->
    <!-- anodised aluminium: the top edge catches the key light. Kept dark in
         both themes — a real laptop does not turn white because a website did,
         and Apple ships the same silver-on-white shot either way. -->
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

    <!-- ── Shadows ────────────────────────────────────────────────────
         flood-opacity is a real CSS property, so the page drives these from
         its own tokens: a shadow tuned for a near-black page is far too heavy
         on a white one. The custom properties below carry the dark values as
         their fallback, so the social card renders unchanged without any CSS.
         (No double hyphen in this comment: XML forbids it, and the same string
         is parsed as XML when the social card is rastered.) -->
    <filter id="castLaptop" x="-25%" y="-25%" width="150%" height="165%">
      <feDropShadow dx="0" dy="32" stdDeviation="32" flood-color="#000"
                    flood-opacity="var(--dev-shadow, 0.55)"/>
    </filter>
    <filter id="castSide" x="-45%" y="-25%" width="190%" height="165%">
      <feDropShadow dx="0" dy="24" stdDeviation="24" flood-color="#000"
                    flood-opacity="var(--dev-shadow-side, 0.65)"/>
    </filter>
    <filter id="blurGround" x="-60%" y="-400%" width="220%" height="900%">
      <feGaussianBlur stdDeviation="13"/>
    </filter>

    <!-- ── Screen clips ───────────────────────────────────────────── -->
    <clipPath id="clipDesktop"><rect x="324" y="99"  width="552" height="387" rx="3"/></clipPath>
    <clipPath id="clipReader"> <rect x="87"  y="277" width="230" height="296" rx="3"/></clipPath>
    <clipPath id="clipPhone">  <rect x="927" y="262" width="158" height="335" rx="24"/></clipPath>
  </defs>"""


def build(embed: bool, backdrop: bool, only: str = None) -> str:
    """`embed=False` writes the interactive stage: external screenshot hrefs,
    per-device groups, no painted background (the page paints its own).
    `embed=True, backdrop=True` writes the standalone social card.
    `only` narrows the stage to a single device, framed on it — what the
    e-reader and Android pages use for their own heroes."""
    BACKDROP = """
  <rect width="1200" height="700" fill="#0b0f17"/>
  <ellipse cx="600"  cy="255" rx="640" ry="440" fill="url(#bgGlow)"/>
  <ellipse cx="600"  cy="320" rx="440" ry="300" fill="url(#accentBlue)"/>
  <ellipse cx="195"  cy="415" rx="300" ry="245" fill="url(#accentWarm)"/>
  <ellipse cx="1015" cy="405" rx="255" ry="215" fill="url(#accentBlue)"/>""" if backdrop else ""
    VIGNETTE = ('\n  <rect width="1200" height="700" fill="url(#vignette)" pointer-events="none"/>'
                if backdrop else "")

    keys = [only] if only else ["laptop", "reader", "phone"]
    ground = "\n".join(GROUND[k] for k in keys)
    vx, vy, vw, vh = solo_view(only) if only else (VIEW_X, VIEW_Y, VIEW_W, VIEW_H)

    # Only the interactive stage carries the hooks: an id to address a device
    # by, and a halo the page can bloom. Focus and clicks belong to the hotspot
    # buttons (see hotspots()), not to the SVG.
    def dev(idname, label, filt, body, halo):
        if idname not in keys:
            return ""            # a solo stage holds one device
        if embed:
            return f'    <g filter="url(#{filt})">\n{body}\n    </g>'
        return (f'    <g id="dev-{idname}" class="dev" data-dev="{idname}">\n'
                f'      <ellipse class="halo" {halo}/>\n'
                f'      <g class="dev-body" filter="url(#{filt})">\n{body}\n      </g>\n'
                f'    </g>')

    # The interactive stage is decoration over real buttons, so it is hidden
    # from assistive tech entirely rather than described twice.
    root_attrs = ('role="img" aria-label="Lingueez running on a laptop, an e-reader and a phone"'
                  if embed else
                  'class="hero-stage" data-hero-stage="" aria-hidden="true"')

    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="{vx:.0f} {vy:.0f} {vw:.0f} {vh:.0f}" width="{vw * 2:.0f}" height="{vh * 2:.0f}"
     {root_attrs}>
  <title>Lingueez — one vocabulary, every device</title>

{DEFS}
{BACKDROP}
  <g transform="translate(0,-4)">
    <!-- contact shadows on the implied floor -->
    <g class="ground" filter="url(#blurGround)">
{ground}
    </g>

    <!-- The three devices share one group so the page can fade them as a
         unit. Fading them individually lets the e-reader go translucent over
         the laptop and the keyboard shows through it. -->
    <g class="devices">
    <!-- ══ 1 · LAPTOP — centre, back plane ══════════════════════════ -->
{dev("laptop", "Lingueez on the desktop app", "castLaptop", laptop_body(embed),
     halo("laptop"))}

    <!-- ══ 2 · E-READER — left, front plane ═════════════════════════ -->
{dev("reader", "Lingueez on an e-reader", "castSide", reader_body(embed),
     halo("reader"))}

    <!-- ══ 3 · PHONE — right, front plane ═══════════════════════════ -->
{dev("phone", "Lingueez on a phone", "castSide", phone_body(embed, bool(only)),
     halo("phone"))}
    </g>
  </g>
{VIGNETTE}
</svg>
"""


def screen_lists(only: str = None) -> str:
    """The screens each device can show, as markup rather than a JS table.

    hero.js builds the switcher from this, and the labels stay bilingual the
    same way every other string on the site is — no second translation path.
    Devices with a single screen still emit their list; the switcher simply
    does not appear for them.

    The final <li class="more"> is not a screen: it is the label for the link
    out to that device's own page, kept here so it is translated alongside.
    """
    out = []
    for device, screens in SCREENS.items():
        key = {"desktop": "laptop"}.get(device, device)   # the <g> ids use "laptop"
        if only and key != only:
            continue
        items = []
        for skey, en, _uk, stem in screens:
            # data-full-* is the untouched source, for the lightbox; the hero
            # image is only as wide as the device screen can ever show.
            full = {th: "/" + _resolve(stem, th).relative_to(ROOT / "docs").as_posix()
                    for th in ("light", "dark")}
            items.append(
                f'      <li data-screen="{skey}"\n'
                f'          data-light="/assets/hero/{device}-{skey}-light.webp"\n'
                f'          data-dark="/assets/hero/{device}-{skey}-dark.webp"\n'
                f'          data-full-light="{full["light"]}"\n'
                f'          data-full-dark="{full["dark"]}"'
                f'>{_t(en)}</li>')
        href, more_en, more_uk = MORE[device]
        out.append(f'  <ul class="dev-screens" data-screens="{key}"\n'
                   f'      data-start="{start_index(device, bool(only))}"\n'
                   f'      data-more-href="{href}" hidden>\n'
                   + "\n".join(items) + "\n"
                   f'      <li class="more">{_t(more_en)}</li>\n  </ul>')
    return "\n".join(out)


def hotspots(only: str = None) -> str:
    """A focusable button over each device, positioned from BODY.

    Tab order runs left to right as the devices are seen, not as they are
    painted, so the reader comes first and the phone last.
    """
    out = []
    names = [only] if only else ["reader", "laptop", "phone"]
    vx, vy, vw, vh = solo_view(only) if only else (VIEW_X, VIEW_Y, VIEW_W, VIEW_H)
    for name in names:
        x0, y0, x1, y1 = BODY[name]
        left = (x0 - vx) / vw * 100
        top = (y0 + GROUP_DY - vy) / vh * 100
        width = (x1 - x0) / vw * 100
        height = (y1 - y0) / vh * 100
        en, uk = NAMES[name]
        out.append(
            f'  <button type="button" class="dev-hit" data-hit="{name}"\n'
            f'          style="--l:{left:.2f}%; --t:{top:.2f}%; '
            f'--w:{width:.2f}%; --h:{height:.2f}%">\n'
            f'    <span class="sr-only">{_t(en)}</span>\n'
            f'  </button>')
    return "\n".join(out)


def main():
    print("screens:")
    write_screens()

    stage = ('<!-- Generated by tools/site/build_hero.py — do not edit by hand. -->\n'
             '<div class="stage-wrap" data-hero>\n'
             + build(embed=False, backdrop=False)
             + hotspots() + "\n"
             + screen_lists() + "\n"
             '</div>\n')
    (INCLUDES / "hero-stage.html").write_text(stage)
    (INCLUDES / "hero-stage.svg").unlink(missing_ok=True)
    print(f"\nstages:\n  docs/_includes/hero-stage.html  "
          f"{len(stage.encode()) / 1024:.1f} KB")

    # One-device stages for the pages that are about one device. Same markup and
    # the same hero.js — data-solo is what tells it there is nothing to choose
    # between, so the device arrives already open with its switcher live.
    for key in ("reader", "phone"):
        one = ('<!-- Generated by tools/site/build_hero.py — do not edit by hand. -->\n'
               f'<div class="stage-wrap is-solo" data-hero data-solo="{key}"\n'
               f'     style="--solo-w:{solo_width(key) * 100:.2f}%">\n'
               + build(embed=False, backdrop=False, only=key)
               + hotspots(only=key) + "\n"
               + screen_lists(only=key) + "\n"
               # The home page keeps its caption in index.html, sharing a slot
               # with the rotating ribbon. A solo page has no ribbon, so the
               # caption belongs here, in normal flow under the device.
               '  <div class="stage-note is-solo">\n'
               '    <p class="dev-caption" data-dev-caption></p>\n'
               '  </div>\n'
               '</div>\n')
        (INCLUDES / f"hero-stage-{key}.html").write_text(one)
        print(f"  docs/_includes/hero-stage-{key}.html  "
              f"{len(one.encode()) / 1024:.1f} KB")

    print("\nsocial card:")
    card = build(embed=True, backdrop=True)
    (ASSETS / "hero.svg").write_text(card)
    # width only: cairosvg derives the height from the viewBox, so no stretching
    png = cairosvg.svg2png(bytestring=card.encode(), output_width=RASTER_W)
    (ASSETS / "hero.png").write_bytes(png)
    Image.open(io.BytesIO(png)).convert("RGB").save(
        ASSETS / "hero.webp", "WEBP", quality=86, method=6)
    for name in ("hero.svg", "hero.png", "hero.webp"):
        path = ASSETS / name
        print(f"  {path.relative_to(ROOT)}  {path.stat().st_size / 1024:.0f} KB")

    if _missing:
        print("\nfell back (a light shot has not been taken yet):", file=sys.stderr)
        for m in dict.fromkeys(_missing):
            print(f"  {m}", file=sys.stderr)


if __name__ == "__main__":
    main()
