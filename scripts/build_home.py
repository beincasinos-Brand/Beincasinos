#!/usr/bin/env python3
"""Generate index.html from live review data so the homepage never contradicts the reviews."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_tier1 as bt  # noqa: E402
import site_chrome as sc  # noqa: E402

ROOT = bt.ROOT
R = bt.T1["reviews"]
e = bt.e

DEMO = "bet365-casino-gb"
GUIDES = [
    ("/guides/how-to-check-a-casino-licence/", "How to check a casino licence", "Find the legal operator, name the regulator, and match claims to the official register."),
    ("/guides/bonus-terms-explained/", "Bonus terms, explained", "Wagering, eligible games, expiry dates and maximum cashout, in plain words."),
    ("/guides/withdrawal-terms/", "Understand withdrawal rules", "Limits, verification steps, fees and processing times to check before you deposit."),
    ("/guides/how-casino-review-sites-make-money/", "How casino review sites make money", "What affiliate commissions do to incentives, and what honest disclosure looks like."),
    ("/guides/online-gambling-self-exclusion/", "Self-exclusion and support", "Blocking tools and where to find help in your country."),
    ("/guides/how-to-complain-about-a-casino/", "How to complain about a casino", "Document the issue, use the formal route, and avoid recovery scams."),
]


def market_tile(code: str) -> str:
    items = [r for r in R.values() if r["market"] == code]
    checks = sum(bt.elig_pass(r) for r in items)
    return (f'<a class="hm-market" href="/reviews/#{code.lower()}"><h3>{e(bt.M_NAME[code])}</h3><strong>{len(items)}</strong>'
            f'<p>reviews · regulator: {e(bt.M_REG[code])}<br>{checks} of {len(items) * 5} eligibility checks passed so far</p></a>')


def row(slug: str, r: dict) -> str:
    ep, cn = bt.elig_pass(r), bt.crit_rated(r)
    s = bt.score(r)
    return (f'<a class="hm-row" href="/reviews/{slug}/">{bt.logo_html(slug, r)}<div><b>{e(r["brand"])}</b><small>{e(r["market_label"])}</small></div>'
            f'<div><span class="lbl">Eligibility {ep} of 5</span>{bt.meter(ep, 5, "checks passed")}</div>'
            f'<div><span class="lbl">Criteria {cn} of 6</span>{bt.meter(cn, 6, "criteria rated")}</div>'
            f'<span class="go">{"Score " + str(s) if s is not None else "Open file"} →</span></a>')


def main() -> None:
    page = ROOT / "index.html"
    old = page.read_text(encoding="utf-8")
    head = old[: old.index("<body>")]
    scored = sum(1 for r in R.values() if bt.score(r) is not None)
    furthest = sorted(R.items(), key=lambda t: (bt.progress_key(t[1]), t[1]["brand"].lower()))[:6]
    demo = R[DEMO]
    weights = "".join(
        f'<li><span>{e(c["label"])}</span><span class="bar"><i class="w{c["weight"] * 4}"></i></span><b>{c["weight"]}</b></li>' for c in bt.CRITERIA)
    gate = "".join(f'<li><span class="bx-tick" aria-hidden="true"></span>{e(lbl)}</li>' for _, lbl in bt.ELIG)
    guides = "".join(f'<li><a href="{h}"><b>{e(t)}</b><span>{e(d)}</span><em>Read</em></a></li>' for h, t, d in GUIDES)
    body = f'''<body>
<a class="skip-link" href="#main">Skip to content</a>
{sc.header("")}
<main id="main">
<section class="hm-hero"><div class="wrap hm-hero-grid">
<div><h1>Casino reviews that show their evidence.</h1>
<p class="hm-lede">Each review starts with five eligibility checks, then scores six criteria out of 100. Anything we cannot verify from an official source stays unrated instead of guessed.</p>
<div class="hero-actions"><a class="button button-primary" href="/reviews/">Browse the reviews</a><a class="button button-outline" href="/how-we-review/">See how we score</a></div>
<p class="hm-proof">{len(R)} reviews across Great Britain, the Netherlands, Germany and Switzerland. {scored} fully scored so far; the rest show exactly what is still open.</p></div>
<div class="hm-demo"><div class="hm-demo-in">{bt.file_html(DEMO, demo).replace('<div class="wrap bx-filewrap">', '<div class="bx-filewrap">', 1)}</div>
<p class="hm-demo-note">A live example: {e(demo["brand"])} in {e(demo["market_label"])} passes every eligibility check, but one criterion is not yet rated, so it has no total. We would rather show that than a number we cannot support.</p></div>
</div></section>

<section class="section"><div class="wrap"><div class="section-heading"><h2>Reviews by market</h2><a class="text-link" href="/reviews/">All reviews</a></div>
<div class="hm-markets">{"".join(market_tile(m) for m in ("GB", "NL", "DE", "CH"))}</div>
<p class="fineprint hm-mt">Also covered: Michigan, United States. Each review is written for one market and one product; we do not mix them.</p></div></section>

<section class="section"><div class="wrap"><div class="section-heading"><div><h2>Evidence files furthest along</h2><p class="muted hm-sub">Ordered by how much we have verified. Commission, fees and sponsorship never change an order.</p></div></div>
<div class="hm-rows">{"".join(row(s, r) for s, r in furthest)}</div></div></section>

<section class="section"><div class="wrap hm-split">
<div><h2>One score, built from six criteria.</h2><p class="muted">Points come only after the gate. Every rating links to the source it rests on, and any unrated criterion means no total.</p>
<ul class="hm-weights">{weights}</ul><p class="hm-mt"><a class="text-link" href="/how-we-review/">Read the full method</a></p></div>
<div><h2>The gate comes first.</h2><p class="muted">If one of these cannot be evidenced, the review stays “Not scored: verification incomplete”, whatever else looks good.</p>
<ul class="hm-gate">{gate}</ul></div></div></section>

<section class="section"><div class="wrap"><div class="section-heading"><h2>Learn the terms before you play</h2><a class="text-link" href="/guides/">All guides</a></div><ul class="hm-list">{guides}</ul></div></section>

<section class="section-compact"><div class="wrap rg-callout"><div class="rg-symbol" aria-hidden="true">+</div><div><h2>It is fine not to gamble.</h2><p>Gambling carries financial risk and is for adults only. If it stops feeling like a choice, pause and speak to a support service in your country.</p></div><a class="text-link" href="/responsible-gambling/">Find support</a></div></section>
</main>
{sc.FOOTER}
<script src="/script.js?v={sc.VERSION}" defer></script>
</body></html>
'''
    page.write_text(head + body, encoding="utf-8")
    print("index.html generated")


if __name__ == "__main__":
    main()
