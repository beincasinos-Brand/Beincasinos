#!/usr/bin/env python3
"""Generate the commercial-intent guides from scripts/seo_guides_data.py, then covers via build_guide_art.py."""
from __future__ import annotations
import html, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import seo_guides_data as D  # noqa: E402
import site_chrome as sc  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
e = html.escape
DATE = "2026-10-30"
CARDS = ("<!-- seo-guides:start -->", "<!-- seo-guides:end -->")


def body_html(g: dict) -> str:
    out = []
    for h, parts in g["sections"]:
        out.append(f"<h2>{e(h)}</h2>")
        for p in parts:
            if isinstance(p, tuple):
                out.append("<ul>" + "".join(f"<li>{e(x)}</li>" for x in p[1]) + "</ul>")
            else:
                out.append(f"<p>{e(p)}</p>")
    out.append("<h2>Frequently asked questions</h2>")
    out += [f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in g["faq"]]
    out.append("<h2>Official sources</h2><ul>" + "".join(f'<li><a href="{e(u)}" rel="noopener noreferrer">{e(l)}</a></li>' for l, u in g["sources"]) + "</ul>")
    out.append('<p class="site-note">Editorial check: 30 October 2026. General information, not legal or financial advice. Rules change and differ by country, product and account; confirm on the regulator\'s own site. '
               'Gambling is for adults (18+, 21+ in some US states) and can be addictive. <a href="/responsible-gambling/">Find support</a>. See our <a href="/affiliate-disclosure/">affiliate disclosure</a>.</p>')
    out.append('<p><a href="/guides/">← Back to all guides</a></p>')
    return "".join(out)


def page(g: dict) -> str:
    slug, url = g["slug"], f"https://beincasinos.online/guides/{g['slug']}/"
    title = f"{g['title']} | BeInCasinos"
    if len(title) > 70:
        title = g["title"][: 70 - len(" | BeInCasinos")].rsplit(" ", 1)[0] + " | BeInCasinos"
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}
    art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "datePublished": DATE, "dateModified": DATE,
           "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "author": {"@type": "Organization", "name": "BeInCasinos", "url": "https://beincasinos.online/about/"},
           "publisher": {"@type": "Organization", "name": "BeInCasinos", "url": "https://beincasinos.online/"}, "inLanguage": "en"}
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False, separators=(",", ":"))}</script>' for x in (art, faq))
    head = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="description" content="{e(g["desc"])}"><title>{e(title)}</title><link rel="icon" href="/favicon.svg" type="image/svg+xml">'
            f'<link rel="canonical" href="{url}"><meta property="og:type" content="article"><meta property="og:title" content="{e(title)}">'
            f'<meta property="og:description" content="{e(g["desc"])}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary_large_image">'
            f'{ld}<meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(g["desc"])}"><meta name="color-scheme" content="light dark">'
            f'{sc.HEAD_LINKS}</head>')
    side = "".join(f'<a href="{u}">{e(l)}</a>' for u, l in g["related"])
    return (head + f'<body><a class="skip-link" href="#main">Skip to content</a>{sc.header("guides/" + slug + "/")}<main id="main">'
            f'<section class="page-hero"><div class="wrap"><p class="eyebrow">{e(g["eyebrow"])} · 5 minute read</p><h1>{e(g["title"])}</h1><p>{e(g["lede"])}</p></div></section>'
            f'<div class="wrap content-layout"><article class="prose">{body_html(g)}</article><aside class="sidebar"><b>Related</b>{side}<a href="/reviews/">All reviews</a><a href="/responsible-gambling/">Safer gambling</a></aside></div></main>'
            f'{sc.FOOTER}<script src="/script.js?v={sc.VERSION}" defer></script></body></html>')


def main() -> None:
    import build_guide_art as art
    art.motif_for = lambda s, m={g["slug"]: g["motif"] for g in D.GUIDES}: m.get(s, "lens")
    for g in D.GUIDES:
        d = ROOT / "guides" / g["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(g), encoding="utf-8")
    # directory cards
    idx = ROOT / "guides" / "index.html"
    t = idx.read_text(encoding="utf-8")
    cards = "".join(
        f'<a class="guide-card" href="/guides/{g["slug"]}/"><img class="guide-thumb" src="/assets/guides/{g["slug"]}.jpg" alt="" width="600" height="315" loading="lazy" decoding="async">'
        f'<span class="card-meta">{e(g["eyebrow"].upper())} · 5 MIN</span><h3>{e(g["title"])}</h3><p>{e(g["desc"])}</p><span class="card-arrow">Read the guide ↗</span></a>' for g in D.GUIDES)
    t = re.sub(re.escape(CARDS[0]) + r".*?" + re.escape(CARDS[1]), "", t, flags=re.S)
    t = t.replace('<div class="list-grid">', f'<div class="list-grid">{CARDS[0]}{cards}{CARDS[1]}', 1)
    idx.write_text(t, encoding="utf-8")
    sm = ROOT / "sitemap.xml"
    s = sm.read_text(encoding="utf-8")
    for g in D.GUIDES:
        u = f"https://beincasinos.online/guides/{g['slug']}/"
        if u not in s:
            s = s.replace("</urlset>", f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{DATE}</lastmod></url>\n</urlset>")
    sm.write_text(s, encoding="utf-8")
    print(f"{len(D.GUIDES)} guides written")


if __name__ == "__main__":
    main()
