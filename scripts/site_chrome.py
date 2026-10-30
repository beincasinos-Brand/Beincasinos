#!/usr/bin/env python3
"""Give every page the same <head> assets, header and footer. Idempotent.

  python3 scripts/site_chrome.py

Edit HEADER / FOOTER here, run the script, commit. Nothing else carries navigation markup.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "20261029-bx1"
NAV = [("/reviews/", "Reviews"), ("/bonuses/", "Bonuses"), ("/markets/", "Markets"), ("/guides/", "Guides"), ("/how-we-review/", "How we score"), ("/responsible-gambling/", "Safer gambling")]
SKIP = {"google05b7a00eb84d7acb.html"}
OLD_CSS = re.compile(r'<link rel="stylesheet" href="/(?:styles\.css|homepage-luxury\.css|assets/(?:reviews-directory|how-we-review|review-brand-logos)\.css)[^"]*">\s*')
OLD_JS = re.compile(r'<script[^>]*src="/assets/review-brand-logos\.js[^"]*"[^>]*></script>\s*')
PRELOAD = ('<link rel="preload" href="/assets/fonts/schibsted-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>'
           '<link rel="preload" href="/assets/fonts/source-serif-4-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>')
HEAD_LINKS = PRELOAD + f'<link rel="stylesheet" href="/styles.css?v={VERSION}">'


def header(path: str) -> str:
    cur = "/" + path.strip("/") + "/" if path.strip("/") else "/"
    links = []
    for href, label in NAV:
        here = cur.startswith(href) or (href == "/markets/" and cur.startswith("/market-research/"))
        links.append(f'<a href="{href}"{" aria-current=\"page\"" if here else ""}>{label}</a>')
    return (
        '<header class="site-header"><div class="wrap bar"><a class="brand" href="/" aria-label="BeInCasinos home">'
        '<img src="/assets/beincasinos-mark.svg" alt="" width="40" height="40"><span>BeIn<b>Casinos</b></span></a>'
        '<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-nav">Menu</button>'
        f'<nav id="primary-nav" class="nav-links" aria-label="Primary">{"".join(links)}'
        '<button class="theme-toggle" type="button" data-theme-toggle aria-pressed="false">Dark mode</button></nav></div></header>'
    )


FOOTER = (
    '<footer class="site-footer"><div class="wrap foot-grid"><div><a class="brand" href="/"><img src="/assets/beincasinos-mark.svg" alt="" width="40" height="40"><span>BeIn<b>Casinos</b></span></a>'
    '<p>Casino reviews that show their evidence. Educational information, not financial or legal advice.</p></div>'
    '<div><h2>Reviews</h2><ul><li><a href="/reviews/">All reviews</a></li><li><a href="/bonuses/">Bonuses</a></li><li><a href="/reviews/#gb">Great Britain</a></li><li><a href="/reviews/#nl">Netherlands</a></li><li><a href="/reviews/#de">Germany</a></li><li><a href="/reviews/#ch">Switzerland</a></li></ul></div>'
    '<div><h2>Standards</h2><ul><li><a href="/how-we-review/">How we score</a></li><li><a href="/editorial-policy/">Editorial policy</a></li><li><a href="/affiliate-disclosure/">Affiliate disclosure</a></li><li><a href="/responsible-gambling/">Safer gambling</a></li><li><a href="/guides/">Guides</a></li></ul></div>'
    '<div><h2>Company</h2><ul><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li><li><a href="/partners/">For operators</a></li><li><a href="/privacy/">Privacy</a></li><li><a href="/terms/">Terms of use</a></li></ul></div></div>'
    '<div class="wrap foot-base"><span>© BeInCasinos. 18+ (21+ in some US states). Gambling laws vary by location.</span><span>Gambling can be addictive. Play within your limits.</span></div></footer>'
)


def process(page: Path) -> bool:
    rel = page.relative_to(ROOT).as_posix()
    text = before = page.read_text(encoding="utf-8")
    if "</head>" not in text:
        return False
    path = rel[: -len("index.html")] if rel.endswith("index.html") else rel
    # head: drop legacy stylesheets, add the one system + font preloads once
    text = re.sub(r"<link rel=\"preload\" href=\"/assets/fonts/[^>]*>", "", text)
    first = OLD_CSS.search(text)
    text = OLD_CSS.sub("", text)
    text = re.sub(r'<link rel="stylesheet" href="/styles\.css[^"]*">', "", text)
    text = text.replace("</head>", HEAD_LINKS + "</head>", 1)
    text = OLD_JS.sub("", text)
    text = re.sub(r'<meta name="theme-color" content="[^"]*">', '<meta name="theme-color" content="#f1f3f6">', text)
    text = re.sub(r'<script[^>]*data-review-brand-map[^>]*></script>', "", text)
    if "color-scheme" not in text:
        text = text.replace("</head>", '<meta name="color-scheme" content="light dark"></head>', 1)
    if '<header class="site-header">' in text:
        text = re.sub(r'<header class="site-header">.*?</header>', lambda _m: header(path), text, count=1, flags=re.S)
    if '<footer class="site-footer">' in text:
        text = re.sub(r'<footer class="site-footer">.*?</footer>', lambda _m: FOOTER, text, count=1, flags=re.S)
    if text != before:
        page.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    n = 0
    for page in sorted(ROOT.rglob("*.html")):
        if any(p in {".git", "dist", "node_modules"} for p in page.parts) or page.name in SKIP:
            continue
        n += process(page)
    print(f"Chrome applied to {n} page(s).")


if __name__ == "__main__":
    main()
