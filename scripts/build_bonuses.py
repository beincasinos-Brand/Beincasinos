#!/usr/bin/env python3
"""Generate /bonuses/ from the offers recorded in data/tier1-reviews.json. Only offers read on an official page appear;
unverified ones are listed by name without an amount, so the page can never promise something we have not seen."""
from __future__ import annotations
import re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_tier1 as bt  # noqa: E402
import site_chrome as sc  # noqa: E402

e, ROOT, R = bt.e, bt.ROOT, bt.T1["reviews"]


def card(slug: str, r: dict, partial: bool) -> str:
    o = r["offer"]
    tag = "Conditions not fully verified" if partial else "Read on the official page"
    s = bt.score(r)
    return (f'<article class="bx-card bonus-card"><div class="bx-card-link bonus-link">{bt.logo_html(slug, r)}'
            f'<div class="bonus-main"><span class="bx-chip">{e(r["market_label"])}</span><h3>{e(r["brand"])}</h3><p class="bonus-offer">{e(o["headline"])}</p></div>'
            f'<p class="bonus-detail">{e(o["detail"])}</p>'
            f'<p class="bonus-meta"><strong>{e(tag)}</strong> · seen {e(bt.fmt_date(o["seen"]))}'
            + (f' · <a href="{e(o["url"])}" rel="nofollow noopener">Offer page</a>' if o.get("url") else "")
            + f' · <a href="/reviews/{slug}/">Review{" · " + str(s) + "/100" if s is not None else ""}</a></p></div></article>')


def pend_card(slug: str, r: dict) -> str:
    site = r.get("site")
    link = f' · <a href="https://{e(site)}/" rel="nofollow noopener">Operator site</a>' if site else ""
    return (f'<article class="bonus-pend">{bt.logo_html(slug, r)}<div><h3>{e(r["brand"])}</h3><p>{e(r["market_label"])} · offer not verified yet</p>'
            f'<p><a href="/reviews/{slug}/">Open review</a>{link}</p></div></article>')


def main() -> None:
    ok = [(s, r) for s, r in R.items() if r["offer"]["verified"]]
    part = [(s, r) for s, r in R.items() if not r["offer"]["verified"] and r["offer"]["headline"] and not r["offer"]["headline"].startswith(("Not verified", "Current offer not verified"))]
    pending = sorted(r["brand"] + " (" + r["market"] + ")" for s, r in R.items() if (s, r) not in ok and (s, r) not in part)
    old = (ROOT / "index.html").read_text(encoding="utf-8")
    head = old[: old.index("<body>")]
    title = "Casino Bonuses Checked on Official Pages (2026) | BeInCasinos"
    desc = "Welcome offers we have read on the operator's own page, with conditions, the date seen and the market. Unverified offers are not listed."
    url = "https://beincasinos.online/bonuses/"
    for pat, val in ((r"<title>.*?</title>", f"<title>{e(title)}</title>"), (r'(<meta name="description" content=")[^"]*(")', None), (r'(<link rel="canonical" href=")[^"]*(")', None),
                     (r'(<meta property="og:title" content=")[^"]*(")', None), (r'(<meta property="og:description" content=")[^"]*(")', None),
                     (r'(<meta property="og:url" content=")[^"]*(")', None), (r'(<meta name="twitter:title" content=")[^"]*(")', None), (r'(<meta name="twitter:description" content=")[^"]*(")', None)):
        if val:
            head = re.sub(pat, lambda m: val, head, count=1, flags=re.S)
    for key, v in (("name=\"description\"", desc), ("rel=\"canonical\"", url), ("property=\"og:title\"", title), ("property=\"og:description\"", desc),
                   ("property=\"og:url\"", url), ("name=\"twitter:title\"", title), ("name=\"twitter:description\"", desc)):
        attr = "href" if "canonical" in key else "content"
        head = re.sub(r'(<(?:meta|link) ' + re.escape(key) + r' ' + attr + r'=")[^"]*(")', lambda m, v=v: m.group(1) + e(v) + m.group(2), head, count=1)
    head = re.sub(r"<script type=\"application/ld\+json\">.*?</script>", "", head, flags=re.S)
    body = f'''<body>
<a class="skip-link" href="#main">Skip to content</a>
{sc.header("bonuses/")}
<main id="main">
<section class="bx-hero"><div class="wrap"><p class="eyebrow">Offers, with evidence</p><h1>Casino bonuses we have actually read</h1>
<p class="bx-lede">Headlines are marketing. Here you see an offer only after we have opened the operator's own page, with the date we saw it and the market it applies to. Commission never decides what appears or in which order.</p>
<p class="bx-meta">{len(ok)} verified · {len(part)} seen with open conditions · {len(pending)} not yet checked</p></div></section>
<section class="section"><div class="wrap">
<div class="section-heading"><h2>Verified offers</h2></div>
<div class="bx-grid">{"".join(card(s, r, False) for s, r in ok) or "<p>No offer has passed our check yet.</p>"}</div>
<div class="section-heading bonus-gap"><h2>Seen, conditions not fully verified</h2></div>
<p class="muted">The amount below comes from the operator's page, but we could not confirm wagering, expiry or cashout terms. Read the full terms before claiming.</p>
<div class="bx-grid">{"".join(card(s, r, True) for s, r in part)}</div>
<div class="section-heading bonus-gap"><h2>Not yet checked</h2></div>
<p class="muted">We do not print an amount for these because we have not read one on the operator's own page. Each review shows what is still open.</p>
<div class="bonus-pending">{"".join(pend_card(s, r) for s, r in R.items() if (s, r) not in ok and (s, r) not in part)}</div>
</div></section>
<section class="section-compact"><div class="wrap"><h2>Before you claim anything</h2>
<ul class="hm-list"><li><a href="/guides/bonus-terms-explained/"><b>Bonus terms, explained</b><span>The conditions that decide what an offer is worth.</span><em>Read</em></a></li>
<li><a href="/guides/what-wagering-requirements-mean/"><b>What wagering requirements mean</b><span>How the multiple works and why the base matters.</span><em>Read</em></a></li>
<li><a href="/guides/bonus-expiry-terms/"><b>Bonus expiry dates</b><span>Activation windows and what happens at the deadline.</span><em>Read</em></a></li>
<li><a href="/tools/wagering-calculator/"><b>Wagering calculator</b><span>Turn a multiplier into required turnover.</span><em>Open</em></a></li></ul>
<p class="fineprint hm-mt">Offers change often and differ by country, product and account. A bonus is not free money and you can decline it. 18+ (21+ in some US states). Gambling can be addictive.</p></div></section>
</main>
{sc.FOOTER}
<script src="/script.js?v={sc.VERSION}" defer></script>
</body></html>
'''
    out = ROOT / "bonuses"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(head + body, encoding="utf-8")
    sm = ROOT / "sitemap.xml"
    t = sm.read_text(encoding="utf-8")
    if "/bonuses/" not in t:
        t = t.replace("</urlset>", f"  <url>\n    <loc>{url}</loc>\n    <lastmod>2026-10-30</lastmod></url>\n</urlset>")
        sm.write_text(t, encoding="utf-8")
    print(f"bonuses page: {len(ok)} verified, {len(part)} partial, {len(pending)} pending")


if __name__ == "__main__":
    main()
