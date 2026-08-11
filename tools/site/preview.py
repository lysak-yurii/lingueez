#!/usr/bin/env python3
"""Render and serve docs/ locally, so the site can be looked at without Ruby.

GitHub Pages builds docs/ with real Jekyll; this is a stand-in for the machines
that do not have it. It implements the exact Liquid subset the site uses and
nothing else — if a page starts failing here, check this list before assuming
the page is wrong:

    {% include file.html key=value %}   Jekyll's own include syntax (not
                                        Shopify's), binding `include.key`
    {% if x %} / {% else %} / {% endif %}   truthiness, ==, !=, contains
    {% for x in list %} … {% endfor %}
    {% assign x = expr %}   {% capture x %}…{% endcapture %}
    {% comment %} … {% endcomment %}
    {{ x }} and the `default:` filter
    front matter, `permalink`, `_config.yml` `defaults:`/`exclude:`

Everything else Liquid can do is deliberately absent. Whitespace-control dashes
({%- … -%}) are honoured.

    python3 tools/site/preview.py            # build + serve on :4000
    python3 tools/site/preview.py --build    # build only, into docs/_preview
    python3 tools/site/preview.py --port 8080

Needs PyYAML and Markdown (both in requirements-dev.txt).
"""
from __future__ import annotations

import argparse
import functools
import http.server
import re
import shutil
import socketserver
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - dependency hint
    raise SystemExit("preview.py needs PyYAML — pip install -r requirements-dev.txt")

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
OUT = DOCS / "_preview"

# Directories Jekyll never publishes, plus our own output.
SKIP_DIRS = {"_layouts", "_includes", "_preview", "_site", ".jekyll-cache", "store"}


# ─────────────────────────────────────────────────────────────────────────────
# Liquid subset
# ─────────────────────────────────────────────────────────────────────────────

TAG = re.compile(r"\{%-?\s*(.*?)\s*-?%\}|\{\{-?\s*(.*?)\s*-?\}\}", re.S)
# Whitespace control: a leading `{%-` eats the whitespace before it, `-%}` after.
TRIM_L = re.compile(r"\{\{-|\{%-")
TRIM_R = re.compile(r"-\}\}|-%\}")

_STRING = re.compile(r"^(['\"])(.*)\1$", re.S)


def _lookup(path: str, ctx: dict):
    """Resolve `a.b.c` against the context. Missing links resolve to None."""
    cur = ctx
    for part in path.split("."):
        if isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return None
        if cur is None:
            return None
    return cur


def _value(expr: str, ctx: dict):
    """Evaluate a single term: a literal, or a dotted context path."""
    expr = expr.strip()
    m = _STRING.match(expr)
    if m:
        return m.group(2)
    if expr in ("true", "false"):
        return expr == "true"
    if re.fullmatch(r"-?\d+", expr):
        return int(expr)
    return _lookup(expr, ctx)


def _filters(expr: str, ctx: dict):
    """Evaluate `term | default: fallback`. `default:` is the only filter used."""
    head, *rest = expr.split("|")
    out = _value(head, ctx)
    for f in rest:
        f = f.strip()
        if f.startswith("default:"):
            if out in (None, "", False):
                out = _value(f[len("default:"):], ctx)
        else:
            raise ValueError(f"preview.py does not implement the {f!r} filter")
    return out


def _truthy(expr: str, ctx: dict) -> bool:
    """Evaluate an {% if %} condition."""
    for op, test in (
        ("==", lambda a, b: a == b),
        ("!=", lambda a, b: a != b),
        (" contains ", lambda a, b: (b or "") in (a or "")),
    ):
        if op in expr:
            left, right = expr.split(op, 1)
            return test(_filters(left, ctx), _filters(right, ctx))
    v = _filters(expr, ctx)
    return bool(v) and v != ""


def _split(text: str):
    """Split a template into ('text', str) and ('tag'|'out', body, raw) tokens."""
    out, pos = [], 0
    for m in TAG.finditer(text):
        if m.start() > pos:
            out.append(("text", text[pos:m.start()], m.group(0)))
        kind = "tag" if m.group(1) is not None else "out"
        out.append((kind, (m.group(1) if kind == "tag" else m.group(2)), m.group(0)))
        pos = m.end()
    if pos < len(text):
        out.append(("text", text[pos:], ""))
    return out


def _trim(tokens):
    """Apply whitespace-control dashes to the neighbouring text tokens."""
    for i, (kind, _body, raw) in enumerate(tokens):
        if kind == "text":
            continue
        if TRIM_L.match(raw) and i and tokens[i - 1][0] == "text":
            k, b, r = tokens[i - 1]
            tokens[i - 1] = (k, b.rstrip(), r)
        if TRIM_R.search(raw) and i + 1 < len(tokens) and tokens[i + 1][0] == "text":
            k, b, r = tokens[i + 1]
            tokens[i + 1] = (k, b.lstrip(), r)
    return tokens


class Renderer:
    def __init__(self, site: dict, includes: Path):
        self.site = site
        self.includes = includes

    def render(self, text: str, ctx: dict) -> str:
        tokens = _trim(_split(text))
        out, _ = self._block(tokens, 0, ctx, stop=())
        return out

    def _block(self, tokens, i, ctx, stop):
        """Render tokens from i until one of `stop` is hit. Returns (html, i)."""
        buf = []
        while i < len(tokens):
            kind, body, _ = tokens[i]
            if kind == "text":
                buf.append(body)
                i += 1
                continue
            if kind == "out":
                v = _filters(body, ctx)
                buf.append("" if v is None else str(v))
                i += 1
                continue

            word = body.split()[0] if body.split() else ""
            if word in stop:
                return "".join(buf), i

            if word == "if":
                buf_i, i = self._if(tokens, i, ctx)
                buf.append(buf_i)
            elif word == "for":
                buf_f, i = self._for(tokens, i, ctx)
                buf.append(buf_f)
            elif word == "comment":
                _, i = self._block(tokens, i + 1, ctx, stop=("endcomment",))
                i += 1
            elif word == "capture":
                name = body.split()[1]
                inner, i = self._block(tokens, i + 1, ctx, stop=("endcapture",))
                ctx[name] = inner
                i += 1
            elif word == "assign":
                name, expr = body[len("assign"):].split("=", 1)
                ctx[name.strip()] = _filters(expr, ctx)
                i += 1
            elif word == "include":
                buf.append(self._include(body, ctx))
                i += 1
            else:
                raise ValueError(f"preview.py does not implement {{% {word} %}}")
        return "".join(buf), i

    def _if(self, tokens, i, ctx):
        """{% if %}…{% else %}…{% endif %}. No elsif — the site does not use it."""
        cond = tokens[i][1][len("if"):].strip()
        taken, i = self._block(tokens, i + 1, ctx, stop=("else", "endif"))
        other = ""
        if tokens[i][1].split()[0] == "else":
            other, i = self._block(tokens, i + 1, ctx, stop=("endif",))
        return (taken if _truthy(cond, ctx) else other), i + 1

    def _for(self, tokens, i, ctx):
        var, _, expr = tokens[i][1][len("for"):].strip().partition(" in ")
        items = _filters(expr, ctx) or []
        body_start = i + 1
        out = []
        for item in items:
            scope = dict(ctx, **{var.strip(): item})
            rendered, end = self._block(tokens, body_start, scope, stop=("endfor",))
            out.append(rendered)
        if not items:  # still have to walk past the body
            _, end = self._block(tokens, body_start, ctx, stop=("endfor",))
        return "".join(out), end + 1

    def _include(self, body: str, ctx: dict) -> str:
        """`include file.html k=v k2="v 2"` — Jekyll's syntax, binding include.k."""
        parts = body[len("include"):].strip()
        name, _, argstr = parts.partition(" ")
        params = {}
        for k, v in re.findall(r'([\w-]+)=("[^"]*"|\'[^\']*\'|\S+)', argstr):
            params[k] = _filters(v, ctx)
        src = (self.includes / name).read_text(encoding="utf-8")
        return self.render(src, dict(ctx, include=params))


# ─────────────────────────────────────────────────────────────────────────────
# Jekyll subset
# ─────────────────────────────────────────────────────────────────────────────

FRONT = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?(.*)\Z", re.S)

# Any local asset reference in the rendered HTML, quoted and without a query.
ASSET_REF = re.compile(r"""(["'])(/assets/[^"'?#]+)\1""")


def version_assets(html: str) -> str:
    """Stamp every /assets/ URL with its file's mtime.

    Preview only — the committed pages keep clean URLs. Without this a browser
    can hold an old stylesheet or script while the page around it is new, and
    the two disagree: a cached site.js with the previous openZoom signature
    turns the new hero.js call into `img.src = "[object Object]"` and the
    lightbox opens blank. A changed file gets a changed URL, so that cannot
    happen no matter what any cache decides to keep.
    """
    def stamp(m):
        quote, url = m.group(1), m.group(2)
        path = DOCS / url.lstrip("/")
        if not path.is_file():
            return m.group(0)
        return f"{quote}{url}?v={int(path.stat().st_mtime)}{quote}"

    return ASSET_REF.sub(stamp, html)


def split_front_matter(text: str):
    m = FRONT.match(text)
    if not m:
        return None, text
    return (yaml.safe_load(m.group(1)) or {}), m.group(2)


def markdown_to_html(md: str) -> str:
    try:
        import markdown
    except ImportError:  # pragma: no cover - dependency hint
        raise SystemExit("preview.py needs Markdown — pip install -r requirements-dev.txt")
    return markdown.markdown(md, extensions=["extra", "sane_lists", "attr_list"])


def config_defaults(config: dict, relpath: str) -> dict:
    """Apply _config.yml `defaults:` whose scope path prefixes this page."""
    values = {}
    for entry in config.get("defaults", []) or []:
        scope = (entry.get("scope") or {}).get("path", "")
        if not scope or relpath.startswith(scope):
            values.update(entry.get("values") or {})
    return values


def url_for(page: dict, relpath: str) -> str:
    """Where the rendered page lands, as a site-absolute URL."""
    if page.get("permalink"):
        return page["permalink"]
    stem = relpath.rsplit(".", 1)[0]
    if stem == "index":
        return "/"
    if relpath.endswith(".md"):
        return f"/{stem}/"
    return f"/{relpath}"


def out_path(url: str) -> Path:
    if url.endswith("/"):
        return OUT / url.lstrip("/") / "index.html"
    return OUT / url.lstrip("/")


def build(quiet: bool = False) -> int:
    config = yaml.safe_load((DOCS / "_config.yml").read_text(encoding="utf-8")) or {}
    excluded = tuple(config.get("exclude", []) or [])
    site = {k: v for k, v in config.items() if k not in ("defaults", "exclude", "include")}
    renderer = Renderer(site, DOCS / "_includes")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # Two passes: collect every page's front matter first, so `site.pages` is
    # populated before anything renders (sitemap.xml iterates it).
    todo = []
    for src in sorted(DOCS.rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(DOCS)
        if set(rel.parts) & SKIP_DIRS or rel.parts[0].startswith("_"):
            continue
        relstr = rel.as_posix()
        if excluded and relstr.startswith(excluded):
            continue

        front, body = (None, None)
        if src.suffix in (".html", ".md", ".xml"):
            front, body = split_front_matter(src.read_text(encoding="utf-8"))
        if front is None:  # a static file, or one that merely ends in .html
            dst = OUT / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            continue

        page = dict(config_defaults(config, relstr), **front)
        page["url"] = url_for(page, relstr)
        page["path"] = relstr
        todo.append((src, relstr, page, body))

    site["pages"] = [p for _, _, p, _ in todo]

    pages = 0
    for src, relstr, page, body in todo:
        url = page["url"]
        ctx = {"site": site, "page": page}

        content = renderer.render(body, dict(ctx))
        if src.suffix == ".md":
            content = markdown_to_html(content)

        layout = page.get("layout")
        while layout:
            tmpl_src = (DOCS / "_layouts" / f"{layout}.html").read_text(encoding="utf-8")
            tmpl_front, tmpl_body = split_front_matter(tmpl_src)
            content = renderer.render(tmpl_body, dict(ctx, content=content))
            layout = (tmpl_front or {}).get("layout")

        dst = out_path(url)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(version_assets(content) if dst.suffix == ".html" else content,
                       encoding="utf-8")
        pages += 1
        if not quiet:
            print(f"  {relstr:38} → {url}")

    if not quiet:
        print(f"built {pages} pages into {OUT.relative_to(ROOT)}")
    return pages


def _source_stamp() -> tuple:
    """Newest mtime across everything the build reads. Cheap enough to call per
    request, and it means an unchanged tree is never rebuilt."""
    newest = 0.0
    count = 0
    for f in DOCS.rglob("*"):
        if f.is_file() and not (set(f.relative_to(DOCS).parts) & SKIP_DIRS):
            newest = max(newest, f.stat().st_mtime)
            count += 1
    return (newest, count)


class Handler(http.server.SimpleHTTPRequestHandler):
    """Rebuilds when a source file has changed, so an edit only needs a refresh
    — but an unchanged tree serves straight from disk."""

    stamp = None

    def do_GET(self):  # noqa: N802 - stdlib naming
        if not Path(self.path).suffix or self.path.endswith((".html", ".xml")):
            now = _source_stamp()
            if now != Handler.stamp:
                try:
                    build(quiet=True)
                except Exception as exc:  # a broken template must not kill the server
                    self.send_error(500, "template error", str(exc))
                    print(f"!! {exc}", file=sys.stderr)
                    return
                Handler.stamp = now
        super().do_GET()

    def end_headers(self):
        # Never cache. Without this the stdlib handler sends only Last-Modified,
        # browsers fall back to heuristic caching, and an edited stylesheet can
        # keep serving from cache without revalidating — which looks exactly
        # like the change not working.
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def log_message(self, fmt, *args):
        if "404" in (fmt % args):
            super().log_message(fmt, *args)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--build", action="store_true", help="build only, do not serve")
    ap.add_argument("--port", type=int, default=4000)
    args = ap.parse_args()

    build()
    if args.build:
        return

    handler = functools.partial(Handler, directory=str(OUT))
    # Threading matters: a page pulls its CSS, JS and images while the first
    # response is still open, and a single-threaded server serialises them into
    # a timeout.
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("127.0.0.1", args.port), handler) as httpd:
        print(f"\nhttp://127.0.0.1:{args.port}/   (Ctrl-C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print()


if __name__ == "__main__":
    main()
