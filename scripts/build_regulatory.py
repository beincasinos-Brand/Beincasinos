#!/usr/bin/env python3
"""Regulator actions tracker built only from red_flags in data/tier1-reviews.json (each has a dated official source). Idempotent."""
from __future__ import annotations
import html, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome as sc  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
e = html.escape
BASE = "https://beincasinos.online"
DATE = "2026-10-31"
D = json.loads((ROOT / "data/tier1-reviews.json").read_text(encoding="utf-8"))["reviews"]


def main() -> None:
    rows = []
    for slug, r in D.items():
        for f in r.get("red_flags", []):
            rows.append((f["date"], r["brand"], r["market_label"], f["text"], f["url"], slug))
    rows.sort(reverse=True)
    items = "".join(
        f'<article class="reg-item"><p class="reg-meta"><time datetime="{d}">{d}</time> · {e(m)}</p><h3><a href="/reviews/{s}/">{e(b)}</a></h3><p>{e(t)}</p>'
        f'<p><a href="{e(u)}" rel="noopener noreferrer">Official regulator source ↗</a></p></article>' for d, b, m, t, u, s in rows)
    title = "Regulator Actions Against Online Casinos: Tracker"
    desc = f"{len(rows)} dated regulator actions (settlements, penalties) affecting operators we review, each linked to the official source. Updated {DATE}."
    url = f"{BASE}/regulatory-actions/"
    head = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="description" content="{e(desc)}"><title>{e(title)} | BeInCasinos</title><link rel="icon" href="/favicon.svg" type="image/svg+xml">'
            f'<link rel="canonical" href="{url}"><meta property="og:type" content="website"><meta property="og:title" content="{e(title)} | BeInCasinos">'
            f'<meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary">'
            f'<meta name="twitter:title" content="{e(title)} | BeInCasinos"><meta name="twitter:description" content="{e(desc)}"><meta name="color-scheme" content="light dark">{sc.HEAD_LINKS}</head>')
    page = (head + f'<body><a class="skip-link" href="#main">Skip to content</a>{sc.header("regulatory-actions/")}<main id="main">'
            f'<section class="page-hero"><div class="wrap"><p class="eyebrow">Evidence tracker</p><h1>Regulator actions affecting operators we review</h1>'
            f'<p>Settlements and penalties published by regulators, newest first. A regulatory action is a fact about past conduct, not a verdict on today\'s product. Each entry links to the official source.</p></div></section>'
            f'<div class="wrap content-layout"><article class="prose"><p>{len(rows)} actions across {len({r[1] for r in rows})} operators · reviewed {DATE}.</p>{items}'
            f'<h2>How to read this page</h2><p>Regulators publish actions when an operator breached its licence conditions. A payment in lieu of a penalty usually means the operator accepted failings and agreed remedies. We show these facts in each review under red flags and they do not by themselves change a score, which follows the published method on <a href="/how-we-review/">how we score</a>.</p>'
            f'<p>This tracker only lists actions we have verified against an official source. It is not complete, and absence of an entry is not a clean record. Check the regulator\'s own register before you play. See <a href="/guides/how-to-read-casino-regulatory-actions/">how to read casino regulatory actions</a>.</p>'
            f'<p class="site-note">Educational information, not advice. Gambling is for adults (18+, 21+ in some US states) and can be addictive. <a href="/responsible-gambling/">Find support</a>.</p></article>'
            f'<aside class="sidebar"><b>Related</b><a href="/reviews/">All reviews</a><a href="/how-we-review/">How we score</a><a href="/online-casinos-uk/">UK hub</a><a href="/markets/">Regulators by market</a></aside></div></main>'
            f'{sc.FOOTER}<script src="/script.js?v={sc.VERSION}" defer></script></body></html>')
    d = ROOT / "regulatory-actions"; d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page, encoding="utf-8")
    sm = ROOT / "sitemap.xml"; s = sm.read_text(encoding="utf-8")
    if f"<loc>{url}</loc>" not in s:
        s = s.replace("</urlset>", f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{DATE}</lastmod></url>\n</urlset>"); sm.write_text(s, encoding="utf-8")
    print(len(rows), "actions")


if __name__ == "__main__":
    main()
