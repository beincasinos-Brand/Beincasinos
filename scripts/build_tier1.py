#!/usr/bin/env python3
"""Render the unified Tier 1 review card + evidence table, and apply the Tier 1 SEO focus.

Source: data/tier1-reviews.json (never published) and data/affiliate-links.json (market codes).

  python3 scripts/build_tier1.py apply   # write marked blocks into pages (idempotent)
  python3 scripts/build_tier1.py check   # read-only; exit 1 if pages are out of sync or a rule is broken

Rules enforced here
  * A numeric score appears only when all six criteria are rated, evidence_complete and
    second_review are true. Otherwise the card shows evidence coverage and "score withheld".
  * Reviews outside the Tier 1 markets get noindex, are removed from sitemap.xml and are hidden
    in the /reviews/ directory. Nothing is deleted; set the market back in the data to undo.
"""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
T1 = json.loads((ROOT / "data" / "tier1-reviews.json").read_text(encoding="utf-8"))
AFF = json.loads((ROOT / "data" / "affiliate-links.json").read_text(encoding="utf-8"))
REVIEWS = ROOT / "reviews"
CARD = ("<!-- tier1-card:start -->", "<!-- tier1-card:end -->")
EVID = ("<!-- tier1-evidence:start -->", "<!-- tier1-evidence:end -->")
ROBOTS = ("<!-- tier1-robots:start -->", "<!-- tier1-robots:end -->")
CRITERIA = T1["criteria"]
TIER1_MARKETS = set(T1["tier1_markets"])
LOGO_EXTS = ("svg", "png", "webp")


def e(s: str) -> str:
    return html.escape(s, quote=True)


def fmt_date(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def assessed(r: dict) -> int:
    return sum(1 for c in CRITERIA if r["criteria"][c["key"]]["rating"] is not None)


def score(r: dict) -> int | None:
    if assessed(r) != len(CRITERIA) or not r.get("evidence_complete") or not r.get("second_review"):
        return None
    total = sum(r["criteria"][c["key"]]["rating"] / 5 * c["weight"] for c in CRITERIA)
    return round(total)


def band(n: int) -> str:
    return ("Strong documented transparency" if n >= 90 else "Good documented transparency" if n >= 80
            else "Mixed evidence or meaningful gaps" if n >= 70 else "Significant weaknesses" if n >= 60
            else "Material weaknesses in assessed criteria")


def logo_html(slug: str, brand: str) -> str:
    for ext in LOGO_EXTS:
        if (ROOT / "assets" / "brands" / f"{slug}.{ext}").is_file():
            return f'<img class="t1-logo-img" src="/assets/brands/{slug}.{ext}" alt="{e(brand)} logo" width="160" height="64" loading="lazy" decoding="async">'
    initials = "".join(w[0] for w in re.findall(r"[A-Za-z0-9]+", brand)[:2]).upper() or "?"
    return f'<span class="t1-monogram" aria-hidden="true">{e(initials)}</span>'


def card_html(slug: str, r: dict) -> str:
    n, s = assessed(r), score(r)
    total = len(CRITERIA)
    segs = "".join(f'<i class="{"on" if r["criteria"][c["key"]]["rating"] is not None else ""}"></i>' for c in CRITERIA)
    if s is not None:
        score_block = f'<div class="t1-score"><strong>{s}</strong><span>/100</span><small>{e(band(s))}</small></div>'
    else:
        why = "complete the remaining criteria" if n < total else "pending editor sign-off"
        score_block = f'<div class="t1-score t1-score--withheld"><strong>&ndash;</strong><small>Score withheld: {why}</small></div>'
    offer = r["offer"]
    flag = "Verified" if offer["verified"] else "Not fully verified"
    status = "No hands-on testing" if not r.get("hands_on") else "Hands-on tested"
    return (
        f'<div class="wrap t1-wrap"><section class="t1-card" aria-label="{e(r["brand"])} research snapshot"><div class="t1-card-logo">{logo_html(slug, r["brand"])}</div>'
        f'<div class="t1-card-main"><p class="t1-kicker">{e(r["market_label"])} &middot; Desk research &middot; {status}</p>'
        f'<h2 class="t1-title">{e(r["brand"])}</h2><p class="t1-licence">{e(r["entity"])} &middot; {e(r["licence_line"])}</p>'
        f'<div class="t1-grid"><div class="t1-cell"><small>Evidence coverage</small><div class="t1-meter" role="img" aria-label="{n} of {total} criteria assessed">{segs}</div><strong>{n} of {total} criteria assessed</strong></div>'
        f'<div class="t1-cell"><small>Current offer ({flag})</small><strong>{e(offer["headline"])}</strong></div>'
        f'<div class="t1-cell"><small>Last checked</small><strong>{fmt_date(r["checked"])}</strong></div></div>'
        f'<p class="t1-note">Offer details change often; check the operator&rsquo;s current terms. Not a recommendation.</p></div>{score_block}</section></div>'
    )


def evidence_html(r: dict) -> str:
    rows = []
    for c in CRITERIA:
        cr = r["criteria"][c["key"]]
        rating = f'{cr["rating"]}/5' if cr["rating"] is not None else "Not assessed"
        src = f'<a href="{e(cr["url"])}" rel="nofollow noopener">Source</a>' if cr["url"] else "&ndash;"
        rows.append(f'<tr><td>{e(c["label"])}<br><small>Weight {c["weight"]}</small></td><td>{rating}</td><td>{e(cr["note"])}</td><td>{src}</td></tr>')
    flags = "".join(
        f'<li><strong>{fmt_date(f["date"])}:</strong> {e(f["text"])} <a href="{e(f["url"])}" rel="nofollow noopener">Source</a></li>' for f in r.get("red_flags", [])
    )
    flags_block = f'<h3>Regulatory history</h3><ul>{flags}</ul>' if flags else ""
    notes = "".join(f"<li>{e(x)}</li>" for x in r.get("notes", []))
    notes_block = f'<h3>Verify before relying on this page</h3><ul>{notes}</ul>' if notes else ""
    offer = r["offer"]
    offer_src = f' <a href="{e(offer["url"])}" rel="nofollow noopener">Offer page</a>' if offer["url"] else ""
    return (
        '<h2>Research evidence and scoring</h2>'
        '<p>Ratings follow our <a href="/how-we-review/">published rubric</a>: six criteria rated 0&ndash;5 from primary sources. '
        'A criterion we could not evidence is shown as &ldquo;Not assessed&rdquo;, never as a low score, and a total is shown only when all six are rated and an editor has signed off. '
        'Ratings here describe published information on the date checked; they are not product tests.</p>'
        f'<table class="t1-evidence"><thead><tr><th>Criterion</th><th>Rating</th><th>Evidence (paraphrased)</th><th>Link</th></tr></thead><tbody>{"".join(rows)}</tbody></table>'
        f'<h3>Current offer</h3><p><strong>{e(offer["headline"])}</strong> &mdash; {e(offer["detail"])} Seen {fmt_date(offer["seen"])}.{offer_src}</p>'
        f'{flags_block}{notes_block}'
    )


def put(text: str, markers: tuple[str, str], block: str | None, after: str | None = None, before: str | None = None) -> str:
    s, en = markers
    text = re.sub(re.escape(s) + r".*?" + re.escape(en) + r"\n?", "", text, flags=re.S)
    if block is None:
        return text
    wrapped = f"{s}\n{block}\n{en}\n"
    if after is not None:
        i = text.find(after)
        if i < 0:
            raise SystemExit(f"anchor not found: {after!r}")
        i += len(after)
        return text[:i] + wrapped + text[i:]
    i = text.rfind(before)
    if i < 0:
        raise SystemExit(f"anchor not found: {before!r}")
    return text[:i] + wrapped + text[i:]


def page_for(slug: str) -> Path:
    return REVIEWS / slug / "index.html"


def market_of(slug: str) -> str:
    return AFF["operators"].get(slug, {}).get("market", "")


def is_tier1(slug: str) -> bool:
    return market_of(slug) in TIER1_MARKETS


def apply_review_page(slug: str) -> bool:
    p = page_for(slug)
    text = before = p.read_text(encoding="utf-8")
    r = T1["reviews"].get(slug)
    if r:
        hero = text.index('<section class="page-hero">')
        end = text.index("</section>", hero) + len("</section>")
        text = put(text, CARD, None)
        text = re.sub(r'<figure class="operator-logo-figure">.*?</figure>', "", text, count=1, flags=re.S)  # legacy hotlinked logo; the unified card owns the logo
        hero = text.index('<section class="page-hero">')
        end = text.index("</section>", hero) + len("</section>")
        text = text[:end] + f"\n{CARD[0]}\n{card_html(slug, r)}\n{CARD[1]}" + text[end:]
        text = put(text, EVID, evidence_html(r), before="</article>")
    # SEO focus: noindex outside Tier 1
    robots = None if is_tier1(slug) else '<meta name="robots" content="noindex,follow">'
    if robots and re.search(r'<meta name="robots"', re.sub(re.escape(ROBOTS[0]) + r".*?" + re.escape(ROBOTS[1]), "", text, flags=re.S)):
        robots = None  # page already declares its own robots meta
    text = put(text, ROBOTS, robots, before="</head>")
    if text != before:
        p.write_text(text, encoding="utf-8")
        return True
    return False


def apply_sitemap() -> bool:
    sm = ROOT / "sitemap.xml"
    text = before = sm.read_text(encoding="utf-8")
    for slug in AFF["operators"]:
        if not is_tier1(slug):
            text = re.sub(r"\s*<url>\s*<loc>https://beincasinos\.online/reviews/" + re.escape(slug) + r"/</loc>.*?</url>", "", text, flags=re.S)
    if text != before:
        sm.write_text(text, encoding="utf-8")
        return True
    return False


def apply_directory() -> bool:
    d = ROOT / "reviews" / "index.html"
    text = before = d.read_text(encoding="utf-8")

    def fix(m: re.Match) -> str:
        card = m.group(0)
        sm = re.search(r'href="/reviews/([^/"]+)/"', card)
        if not sm:
            return card
        slug = sm.group(1)
        head = re.match(r"<article\b[^>]*>", card).group(0)
        head_clean = re.sub(r"\s+(?:hidden|data-tier=\"[^\"]*\")(?:=\"[^\"]*\")?", "", head)
        new_head = head_clean[:-1] + (' data-tier="tier1">' if is_tier1(slug) else ' data-tier="other">')
        card = new_head + card[len(head):]
        r = T1["reviews"].get(slug)
        if r:
            n = assessed(r)
            s = score(r)
            pill = f"SCORE {s}/100" if s is not None else f"EVIDENCE {n}/{len(CRITERIA)}"
            card = re.sub(r'<span class="review-status-pill">[^<]*</span>', f'<span class="review-status-pill">{pill}</span>', card)
            metrics = (
                '<div class="review-card-metrics">'
                f'<div><span>Evidence coverage</span><strong>{n} of {len(CRITERIA)} criteria</strong></div>'
                f'<div><span>Current offer</span><strong>{e(r["offer"]["headline"] if r["offer"]["verified"] else "Not fully verified")}</strong></div></div>'
            )
            card = re.sub(r'<div class="review-card-metrics">.*?</div>\s*</div>', lambda _m: metrics, card, count=1, flags=re.S)
        return card

    text = re.sub(r"<article class=\"review-product-card\".*?</article>", fix, text, flags=re.S)
    n1 = sum(1 for sl in AFF["operators"] if is_tier1(sl))
    text = re.sub(r'(<div class="review-count-panel"><strong>)\d+(</strong><span>)[^<]*(</span>)', lambda m: f"{m.group(1)}{n1}{m.group(2)}Tier 1 research profiles{m.group(3)}", text)
    text = re.sub(r'(id="review-results-count"[^>]*>)\d+ profiles?', lambda m: f"{m.group(1)}{n1} profiles", text)
    tier1_labels = {AFF["operators"][sl]["market"] for sl in AFF["operators"] if is_tier1(sl)}
    keep = {"GB": "Great Britain only", "NL": "Netherlands only", "DE": "Germany only", "CH": "Switzerland only", "US-MI": "United States \u2014 Michigan"}
    allowed = {keep[m] for m in tier1_labels if m in keep}
    text = re.sub(r'<option value="([^"]+)">[^<]*</option>', lambda m: m.group(0) if m.group(1) in allowed else "", text)
    if text != before:
        d.write_text(text, encoding="utf-8")
        return True
    return False


def cmd_apply() -> int:
    changed = [s for s in sorted(p.parent.name for p in REVIEWS.glob("*/index.html")) if apply_review_page(s)]
    sm, di = apply_sitemap(), apply_directory()
    t1 = [s for s in AFF["operators"] if is_tier1(s)]
    print(f"Review pages changed: {len(changed)}. Sitemap changed: {sm}. Directory changed: {di}.")
    print(f"Tier 1 reviews: {len(t1)} indexable; non-Tier-1: {len(AFF['operators']) - len(t1)} noindex.")
    return 0


def cmd_check() -> int:
    errs = []
    for slug, r in T1["reviews"].items():
        if not page_for(slug).is_file():
            errs.append(f"{slug}: no review page")
        if not is_tier1(slug):
            errs.append(f"{slug}: in tier1-reviews.json but market {market_of(slug)!r} is not Tier 1")
        for c in CRITERIA:
            cr = r["criteria"][c["key"]]
            if cr["rating"] is not None and not (isinstance(cr["rating"], int) and 0 <= cr["rating"] <= 5 and cr["url"].startswith("https://")):
                errs.append(f"{slug}/{c['key']}: a rating needs an int 0-5 and an https source URL")
        if r["offer"]["verified"] and not r["offer"]["url"]:
            errs.append(f"{slug}: verified offer needs a source URL")
        text = page_for(slug).read_text(encoding="utf-8")
        if CARD[0] not in text or EVID[0] not in text:
            errs.append(f"{slug}: card/evidence blocks missing; run apply")
        elif re.search(r'class="t1-score"><strong>\d+', text) and score(r) is None:
            errs.append(f"{slug}: numeric score shown without full evidence and sign-off")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for slug in AFF["operators"]:
        if not is_tier1(slug):
            if f"/reviews/{slug}/</loc>" in sitemap:
                errs.append(f"{slug}: non-Tier-1 page still in sitemap")
            if ROBOTS[0] not in page_for(slug).read_text(encoding="utf-8") and 'content="noindex' not in page_for(slug).read_text(encoding="utf-8"):
                errs.append(f"{slug}: non-Tier-1 page lacks noindex")
        elif ROBOTS[0] in page_for(slug).read_text(encoding="utf-8"):
            errs.append(f"{slug}: Tier 1 page is marked noindex")
    if errs:
        print("Tier 1 check FAILED:\n  " + "\n  ".join(errs))
        return 1
    print(f"Tier 1 check passed ({len(T1['reviews'])} evidence-backed reviews).")
    return 0


if __name__ == "__main__":
    cmds = {"apply": cmd_apply, "check": cmd_check}
    if len(sys.argv) != 2 or sys.argv[1] not in cmds:
        raise SystemExit(__doc__)
    sys.exit(cmds[sys.argv[1]]())
