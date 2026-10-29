#!/usr/bin/env python3
"""Render every Tier 1 review (summary file, eligibility gate, six scored criteria, key facts,
red flags) and the /reviews/ directory from data/tier1-reviews.json, and apply the Tier 1 SEO focus.

  python3 scripts/build_tier1.py apply   # idempotent
  python3 scripts/build_tier1.py check   # read-only; exit 1 on any broken rule

The single scoring metric (published on /how-we-review/):
  * Eligibility first: domain, operator, regulator, market permission, terms+withdrawal rules.
    If any check is not "pass" the review is "Not scored - verification incomplete".
  * Six criteria rated 0-5 (null = not assessed): terms 25, payments 20, safer 20, complaints 15,
    licence 10, usability 10. Any unassessed criterion means no total.
  * Commission, fees and sponsorship never change a score or an order.
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
CRITERIA = T1["criteria"]
ELIG = [
    ("domain", "Exact domain"),
    ("operator", "Legal operator"),
    ("regulator", "Regulator record"),
    ("market_permission", "Market permission"),
    ("terms_and_withdrawal_rules", "Terms and withdrawal rules"),
]
TIER1 = set(T1["tier1_markets"])
M_NAME = {"GB": "Great Britain", "NL": "Netherlands", "DE": "Germany", "CH": "Switzerland", "US-MI": "United States (Michigan)"}
M_ORDER = ["GB", "NL", "DE", "CH", "US-MI"]
M_REG = {"GB": "UK Gambling Commission", "NL": "Kansspelautoriteit (KSA)", "DE": "GGL", "CH": "ESBK", "US-MI": "Michigan Gaming Control Board"}
LOGO_EXTS = ("svg", "png", "webp")
HERO = ("<!-- bx-hero:start -->", "<!-- bx-hero:end -->")
FILE = ("<!-- bx-file:start -->", "<!-- bx-file:end -->")
BODY = ("<!-- bx-body:start -->", "<!-- bx-body:end -->")
SOCIAL = ("<!-- tier1-social:start -->", "<!-- tier1-social:end -->")
SEO = ("<!-- tier1-seo:start -->", "<!-- tier1-seo:end -->")
ROBOTS = ("<!-- tier1-robots:start -->", "<!-- tier1-robots:end -->")


def e(s) -> str:
    return html.escape(str(s or ""), quote=True)


def fmt_date(iso: str) -> str:
    try:
        d = date.fromisoformat(iso)
    except ValueError:
        return iso or "n/a"
    return f"{d.day} {d.strftime('%B %Y')}"


# ---------------------------------------------------------------- scoring
def elig_pass(r: dict) -> int:
    return sum(1 for k, _ in ELIG if r["eligibility"][k]["status"] == "pass")


def crit_rated(r: dict) -> int:
    return sum(1 for c in CRITERIA if r["criteria"][c["key"]]["rating"] is not None)


def score(r: dict) -> int | None:
    if elig_pass(r) != len(ELIG) or crit_rated(r) != len(CRITERIA):
        return None
    return round(sum(r["criteria"][c["key"]]["rating"] / 5 * c["weight"] for c in CRITERIA))


def band(n: int) -> str:
    return ("Excellent evidence-backed experience" if n >= 90 else "Strong" if n >= 80
            else "Good with limitations" if n >= 70 else "Mixed" if n >= 60 else "Significant shortcomings")


def missing(r: dict) -> str:
    bits = []
    m = [lbl.lower() for k, lbl in ELIG if r["eligibility"][k]["status"] != "pass"]
    if m:
        bits.append("checks: " + ", ".join(m))
    c = [x["label"].lower() for x in CRITERIA if r["criteria"][x["key"]]["rating"] is None]
    if c:
        bits.append("criteria: " + ", ".join(c))
    return "; ".join(bits)


def progress_key(r: dict):
    s = score(r)
    return (-(s if s is not None else -1), -(elig_pass(r) + crit_rated(r)))


# ---------------------------------------------------------------- pieces
def logo_html(slug: str, r: dict, cls: str = "bx-logo") -> str:
    brand = r["brand"]
    initials = "".join(w[0] for w in re.findall(r"[A-Za-z0-9]+", brand)[:2]).upper() or "?"
    mono = f'<span class="bx-mono" aria-hidden="true">{e(initials)}</span>'
    if r.get("logo_dark"):
        cls += " is-dark"
    for ext in LOGO_EXTS:
        if (ROOT / "assets" / "brands" / f"{slug}.{ext}").is_file():
            return f'<span class="{cls}"><img src="/assets/brands/{slug}.{ext}" alt="{e(brand)} logo" width="168" height="64" loading="lazy" decoding="async">{mono}</span>'
    url = r.get("logo_url")
    if url:
        return (f'<span class="{cls}"><img data-logo src="{e(url)}" alt="{e(brand)} logo" width="168" height="64" loading="lazy" decoding="async" referrerpolicy="no-referrer">{mono}</span>')
    return f'<span class="{cls} is-mono">{mono}</span>'


def seal_html(r: dict, size: str = "") -> str:
    s = score(r)
    c = 2 * 3.14159 * 52
    if s is not None:
        return (f'<svg class="bx-ring {size}" viewBox="0 0 120 120" role="img" aria-label="Score {s} out of 100">'
                f'<circle class="trk" cx="60" cy="60" r="52"/><circle class="val" cx="60" cy="60" r="52" stroke-dasharray="{c * s / 100:.1f} {c:.1f}" transform="rotate(-90 60 60)"/>'
                f'<text x="60" y="64" class="num">{s}</text><text x="60" y="84" class="den">/100</text></svg>')
    return (f'<svg class="bx-ring is-empty {size}" viewBox="0 0 120 120" role="img" aria-label="Not scored">'
            f'<circle class="trk" cx="60" cy="60" r="52"/><text x="60" y="68" class="num">n/a</text></svg>')


def meter(done: int, total: int, label: str) -> str:
    segs = "".join(f"<i{' class=on' if i < done else ''}></i>" for i in range(total))
    return f'<div class="bx-meter" role="img" aria-label="{done} of {total} {e(label)}">{segs}</div>'


def fact(label: str, val: str, url: str = "", ok: bool = True) -> str:
    if not val:
        v = '<span class="bx-nv">Not verified yet</span>'
    else:
        v = e(val) + (f' <a href="{e(url)}" rel="nofollow noopener">Source</a>' if url else "")
    return f"<div><dt>{e(label)}</dt><dd>{v}</dd></div>"


def facts_html(r: dict) -> str:
    f = r.get("facts") or {}
    o = r["offer"]
    offer_val = o["headline"] if o["verified"] else ("" if o["headline"].startswith("Not verified") else o["headline"] + " (conditions not fully verified)")
    wd = f.get("withdrawals") or {}
    wd_val = "; ".join(x for x in (wd.get("timing"), wd.get("limits"), (("Fees: " + wd["fees"]) if wd.get("fees") else "")) if x)
    kyc = f.get("kyc") or {}
    pm = f.get("payment_methods") or []
    sup = f.get("support") or {}
    cr = f.get("complaints_route") or {}
    rows = [
        fact("Licence", (f.get("licence") or {}).get("value") or r["licence_line"], (f.get("licence") or {}).get("url", "")),
        fact("Welcome offer", offer_val, o.get("url", "")),
        fact("Offer conditions", o["detail"] if o["verified"] or o["detail"].count(":") else "", o.get("url", "")),
        fact("Withdrawals", wd_val, wd.get("url", "")),
        fact("Verification (KYC)", kyc.get("summary", ""), kyc.get("url", "")),
        fact("Payment methods", ", ".join(pm), ""),
        fact("Support", "; ".join(x for x in (sup.get("channels"), sup.get("hours")) if x), sup.get("url", "")),
        fact("Complaints route", cr.get("summary", ""), cr.get("url", "")),
    ]
    return '<dl class="bx-facts">' + "".join(rows) + "</dl>"


def hero_html(slug: str, r: dict, h1: str, lede: str) -> str:
    return (
        f'<section class="bx-hero"><div class="wrap"><nav class="bx-crumbs" aria-label="Breadcrumb"><a href="/reviews/">Reviews</a><span aria-hidden="true">/</span>'
        f'<a href="/reviews/#{r["market"].lower()}">{e(r["market_label"])}</a></nav><h1>{h1}</h1>'
        f'{"<p class=bx-lede>" + lede + "</p>" if lede else ""}'
        f'<p class="bx-meta">Checked {fmt_date(r["checked"])}<span aria-hidden="true"> · </span>Desk research, no hands-on testing<span aria-hidden="true"> · </span>'
        f'<a href="/how-we-review/">How we score</a><span aria-hidden="true"> · </span><a href="/affiliate-disclosure/">Affiliate disclosure</a></p></div></section>'
    )


def file_html(slug: str, r: dict) -> str:
    s = score(r)
    ep, cr_n = elig_pass(r), crit_rated(r)
    if s is not None:
        status = f'<p class="bx-status is-scored"><strong>{e(band(s))}</strong><span>Score for {e(r["market_label"])}, checked {fmt_date(r["checked"])}</span></p>'
    else:
        status = f'<p class="bx-status"><strong>Not scored: verification incomplete</strong><span>Still open: {e(missing(r))}</span></p>'
    gate = "".join(
        f'<li class="is-{r["eligibility"][k]["status"]}"><span class="bx-tick" aria-hidden="true"></span>{e(lbl)}<span class="sr-only">: {e(r["eligibility"][k]["status"])}</span></li>'
        for k, lbl in ELIG)
    return (
        f'<div class="wrap bx-filewrap"><section class="bx-file" aria-label="{e(r["brand"])} evidence file">'
        f'<header class="bx-file-id">{logo_html(slug, r)}<div><p class="bx-chip">{e(r["market_label"])} · {e(M_REG.get(r["market"], ""))}</p><h2>{e(r["brand"])}</h2>'
        f'<p class="bx-entity">{e(r["entity"])}</p></div></header>'
        f'<div class="bx-seal">{seal_html(r)}{status}</div>'
        f'<div class="bx-gate"><h3>Eligibility checks <span>{ep} of {len(ELIG)}</span></h3><ul>{gate}</ul></div>'
        f'<div class="bx-prog"><h3>Scored criteria <span>{cr_n} of {len(CRITERIA)}</span></h3>{meter(cr_n, len(CRITERIA), "criteria rated")}'
        f'<p>{"Six criteria, 100 points. All six are rated and every check passed." if score(r) is not None else "Six criteria, 100 points. No total until all six are rated and every check passes."}</p></div>'
        f'<div class="bx-keyfacts"><h3>Key facts</h3>{facts_html(r)}</div></section></div>'
    )


def body_html(slug: str, r: dict) -> str:
    out = []
    # eligibility detail
    rows = []
    for k, lbl in ELIG:
        x = r["eligibility"][k]
        src = f' <a href="{e(x["url"])}" rel="nofollow noopener">Source</a>' if x.get("url") else ""
        rows.append(f'<li class="is-{x["status"]}"><span class="bx-tick" aria-hidden="true"></span><div><strong>{e(lbl)}</strong>'
                    f'<span class="bx-st">{ {"pass": "Passed", "fail": "Failed", "unverified": "Not verified"}[x["status"]] }</span><p>{e(x["note"])}{src}</p></div></li>')
    out.append(quick_answers_html(r))
    out.append(f'<h2 id="eligibility">Eligibility checks</h2><p>These come before any points. If one is not passed, the review stays unscored whatever else looks good.</p><ol class="bx-elig">{"".join(rows)}</ol>')
    # criteria
    crow = []
    for c in CRITERIA:
        x = r["criteria"][c["key"]]
        pts = f'{x["rating"] / 5 * c["weight"]:.1f}' if x["rating"] is not None else None
        bar = f'<span class="bx-bar"><i class="w{(x["rating"] or 0) * 20}"></i></span>'
        src = f' <a href="{e(x["url"])}" rel="nofollow noopener">Source</a>' if x.get("url") else ""
        crow.append(
            f'<tr><th scope="row">{e(c["label"])}<small>{c["weight"]} points</small></th>'
            f'<td class="bx-rate">{(str(x["rating"]) + " / 5") if x["rating"] is not None else "Not assessed"}{bar}<small>{(pts + " pts") if pts else "no points"}</small></td>'
            f'<td>{e(x["note"])}{src}</td></tr>')
    s = score(r)
    total = (f'<p class="bx-total"><strong>Total: {s} / 100</strong> {e(band(s))}.</p>' if s is not None
             else f'<p class="bx-total"><strong>No total yet.</strong> {e(missing(r))}.</p>')
    out.append('<h2 id="scoring">How the score is built</h2><div class="bx-tablewrap"><table class="bx-crit"><thead><tr><th>Criterion</th><th>Rating</th><th>Evidence</th></tr></thead><tbody>'
               + "".join(crow) + f'</tbody></table></div>{total}')
    # pros / cons
    if r.get("pros") or r.get("cons"):
        li = lambda xs: "".join(f"<li>{e(x)}</li>" for x in xs)
        out.append(f'<h2>Pros and cons</h2><div class="bx-pc"><div><h3>What the evidence supports</h3><ul class="pro">{li(r.get("pros", []))}</ul></div>'
                   f'<div><h3>Limits and concerns</h3><ul class="con">{li(r.get("cons", []))}</ul></div></div>')
    # red flags
    if r.get("red_flags"):
        fl = "".join(f'<li><time datetime="{e(x["date"])}">{fmt_date(x["date"])}</time><p>{e(x["text"])} <a href="{e(x["url"])}" rel="nofollow noopener">Source</a></p></li>' for x in r["red_flags"])
        out.append(f'<h2>Regulatory history</h2><p>Published enforcement decisions and documented issues. They are context for the licence criterion, not a verdict on today.</p><ul class="bx-flags">{fl}</ul>')
    if r.get("unreachable"):
        out.append('<p class="bx-note">Pages we could not open during this check: ' + ", ".join(e(u) for u in r["unreachable"][:6]) + ". Criteria that depend on them are left unrated rather than guessed.</p>")
    out.append('<h2 id="notes">Detailed research notes</h2>')
    return "\n".join(out)


# ---------------------------------------------------------------- page edit
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
    i = text.find(before)
    if i < 0:
        raise SystemExit(f"anchor not found: {before!r}")
    return text[:i] + wrapped + text[i:]


def strip_text(h: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", h)).strip()


def cover_html(slug: str, r: dict) -> str:
    if not (ROOT / "assets" / "reviews" / f"{slug}.jpg").is_file():
        return ""
    return (f'<div class="wrap"><figure class="bx-cover"><img src="/assets/reviews/{slug}.jpg" width="1200" height="630" loading="lazy" decoding="async" '
            f'alt="Evidence-file summary for {e(r["brand"])} in {e(r["market_label"])}: {elig_pass(r)} of 5 eligibility checks passed, {crit_rated(r)} of 6 criteria rated."></figure></div>\n')


def social_meta(slug: str, r: dict) -> str | None:
    if not (ROOT / "assets" / "reviews" / f"{slug}.jpg").is_file():
        return None
    u = f"https://beincasinos.online/assets/reviews/{slug}.jpg"
    return (f'<meta property="og:image" content="{u}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            f'<meta property="og:image:alt" content="{e(r["brand"])} evidence file, {e(r["market_label"])}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{u}">')


M_SHORT = {"GB": "UK", "NL": "Netherlands", "DE": "Germany", "CH": "Switzerland", "US-MI": "Michigan"}


def review_name(r: dict) -> str:
    b = r["brand"]
    return b + (" Review" if ("casino" in b.lower() or "poker" in b.lower() or b.lower().endswith((".ch", ".com"))) else " Casino Review")


def seo_title(r: dict) -> str:
    s = score(r)
    base = f"{review_name(r)} {M_SHORT[r['market']]}"
    tail = " | BeInCasinos"
    opts = ([f"{base} (2026): {s}/100, Bonus & Withdrawals", f"{base} (2026): {s}/100 Score", f"{base}: {s}/100"] if s is not None
            else [f"{base} (2026): Licence, Bonus & Withdrawals", f"{base} (2026): Licence & Bonus", f"{base} (2026)", base])
    for o in opts:
        if len(o + tail) <= 70:
            return o + tail
    return opts[-1] + tail


def seo_desc(r: dict) -> str:
    s = score(r)
    o = r["offer"]
    offer = (o["headline"] if o["verified"] else "")
    parts = [f"{r['brand']} in {r['market_label']}: " + (f"scored {s}/100 ({band(s)}). " if s is not None else "evidence file with licence checks, not scored yet. ")]
    if offer:
        parts.append(f"Offer: {offer}. ")
    parts.append(f"Withdrawals, safer gambling and complaints, checked {fmt_date(r['checked'])}.")
    d = "".join(parts)
    return d if len(d) <= 168 else d[:165].rsplit(" ", 1)[0] + "..."


def faq_items(r: dict) -> list[tuple[str, str]]:
    f = r.get("facts") or {}
    b, mk, reg = r["brand"], r["market_label"], M_REG.get(r["market"], "the regulator")
    el = r["eligibility"]
    s = score(r)
    items = []
    if el["operator"]["status"] == "pass" and el["regulator"]["status"] == "pass":
        items.append((f"Is {b} legal and licensed in {mk}?", f"{r['licence_line']}. A licence record shows regulatory status for the product and market named; it is not a guarantee of fairness or a safety rating. Checked {fmt_date(r['checked'])}."))
    else:
        items.append((f"Is {b} legal and licensed in {mk}?", f"We have not yet matched {b}'s operator and permit to the {reg} register for this product, so we do not state that it is licensed here. Open items are listed in the eligibility checks above."))
    o = r["offer"]
    if o["headline"] and not o["headline"].startswith("Not verified"):
        tag = "" if o["verified"] else " Conditions are not fully verified, so read the operator's terms before claiming."
        items.append((f"What is the {b} welcome offer?", f"{o['headline']}. {o['detail']}{tag} Seen {fmt_date(o['seen'])}; offers change, so confirm on the operator's page."))
    wd = f.get("withdrawals") or {}
    if wd.get("timing") or wd.get("limits"):
        items.append((f"How long do {b} withdrawals take?", " ".join(x.rstrip(".") + "." for x in (wd.get("timing"), wd.get("limits")) if x) + " These are published estimates, not transaction-tested results; identity checks can add time."))
    st = f.get("safer_tools") or []
    if st:
        items.append((f"What safer-gambling tools does {b} offer?", ", ".join(st) + ". Use them before you deposit, not after."))
    cr = f.get("complaints_route") or {}
    if cr.get("summary"):
        items.append((f"How do I complain about {b}?", cr["summary"]))
    items.append((f"What is the BeInCasinos score for {b}?",
                  (f"{s}/100 ({band(s)}) for {mk}, checked {fmt_date(r['checked'])}. It is built from six weighted criteria after five eligibility checks; commission never changes it." if s is not None
                   else f"{b} has no total yet. {missing(r)}. We show that instead of guessing.")))
    return items


def quick_answers_html(r: dict) -> str:
    qa = "".join(f"<div><dt>{e(q)}</dt><dd>{e(a)}</dd></div>" for q, a in faq_items(r))
    return f'<h2 id="quick-answers">Quick answers</h2><dl class="bx-qa">{qa}</dl>'


def ld_json(slug: str, r: dict) -> str:
    import json as _j
    url = f"https://beincasinos.online/reviews/{slug}/"
    graph = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq_items(r)]}]
    s = score(r)
    if s is not None:
        graph.append({"@context": "https://schema.org", "@type": "Review", "url": url,
                      "itemReviewed": {"@type": "Organization", "name": r["brand"], "url": f"https://{r['site']}/" if r.get("site") else None},
                      "author": {"@type": "Organization", "name": "BeInCasinos"}, "datePublished": r["checked"],
                      "reviewRating": {"@type": "Rating", "ratingValue": s, "bestRating": 100, "worstRating": 0}})
        graph[-1]["itemReviewed"] = {k: v for k, v in graph[-1]["itemReviewed"].items() if v}
    return "".join(f'<script type="application/ld+json">{_j.dumps(g, ensure_ascii=False, separators=(",", ":"))}</script>' for g in graph)


def apply_seo_head(text: str, slug: str, r: dict) -> str:
    title, desc = seo_title(r), seo_desc(r)
    text = re.sub(r"<title>.*?</title>", lambda m: f"<title>{e(title)}</title>", text, count=1, flags=re.S)
    for pat, val in ((r'(<meta name="description" content=")[^"]*(")', desc), (r'(<meta property="og:title" content=")[^"]*(")', title),
                     (r'(<meta property="og:description" content=")[^"]*(")', desc), (r'(<meta name="twitter:title" content=")[^"]*(")', title),
                     (r'(<meta name="twitter:description" content=")[^"]*(")', desc)):
        text = re.sub(pat, lambda m, v=val: m.group(1) + e(v) + m.group(2), text, count=1)
    return put(text, SEO, ld_json(slug, r), before="</head>")


def apply_review_page(slug: str) -> bool:
    p = REVIEWS / slug / "index.html"
    text = before = p.read_text(encoding="utf-8")
    r = T1["reviews"].get(slug)
    if r:
        # 1. read the existing hero (legacy or already generated), then regenerate hero + file blocks
        text = re.sub(re.escape(FILE[0]) + r".*?" + re.escape(FILE[1]) + r"\n?", "", text, flags=re.S)
        m = re.search(re.escape(HERO[0]) + r".*?" + re.escape(HERO[1]) + r"\n?", text, re.S) or re.search(r'<section class="page-hero">.*?</section>', text, re.S)
        if not m:
            raise SystemExit(f"{slug}: no hero found")
        inner = m.group(0)
        h1 = re.search(r"<h1>(.*?)</h1>", inner, re.S)
        lede_m = re.search(r'<p class="?bx-lede"?>(.*?)</p>', inner, re.S)
        if lede_m:
            lede = lede_m.group(1)
        else:
            ps = re.findall(r"<p(?: [^>]*)?>(.*?)</p>", inner, re.S)
            lede = next((x for x in ps if not x.startswith("Last checked") and "Status:" not in x), "")
        lede = re.sub(r"\s+", " ", lede).strip()
        block = f"{HERO[0]}\n{hero_html(slug, r, h1.group(1) if h1 else e(r['brand']), lede)}\n{HERO[1]}\n{FILE[0]}\n{file_html(slug, r)}\n{cover_html(slug, r)}{FILE[1]}\n"
        text = text.replace(inner, block, 1)
        for pat in (r'<div class="rg-callout">.*?</div></div>', r'<section class="evidence-scorecard".*?</section>',
                    r'<figure class="operator-logo-figure[^"]*">.*?</figure>', r'<section id="review-visual-summary".*?</section>',
                    r'<!-- tier1-card:start -->.*?<!-- tier1-card:end -->\n?', r'<!-- tier1-evidence:start -->.*?<!-- tier1-evidence:end -->\n?'):
            text = re.sub(pat, "", text, flags=re.S)
        text = put(text, BODY, body_html(slug, r), after='<article class="prose">')
    if r:
        text = re.sub(r'<meta property="og:image[^>]*>|<meta name="twitter:(?:card|image)"[^>]*>', "", text) if SOCIAL[0] not in text else text
        text = put(text, SOCIAL, social_meta(slug, r), before="</head>")
        text = apply_seo_head(text, slug, r)
    tier1 = AFF["operators"].get(slug, {}).get("market", "") in TIER1
    robots = None if tier1 else '<meta name="robots" content="noindex,follow">'
    if robots and re.search(r'<meta name="robots"', re.sub(re.escape(ROBOTS[0]) + r".*?" + re.escape(ROBOTS[1]), "", text, flags=re.S)):
        robots = None
    text = put(text, ROBOTS, robots, before="</head>")
    if text != before:
        p.write_text(text, encoding="utf-8")
        return True
    return False


# ---------------------------------------------------------------- directory
def directory_card(slug: str, r: dict) -> str:
    s = score(r)
    ep, cn = elig_pass(r), crit_rated(r)
    o = r["offer"]
    offer = e(o["headline"]) + ("" if o["verified"] else (" · unverified" if not o["headline"].startswith("Not verified") else ""))
    state = f"Score {s}" if s is not None else "Not scored"
    return (
        f'<article class="bx-card" data-market="{e(r["market_label"])}" data-code="{e(r["market"])}" data-search="{e((r["brand"] + " " + r["market_label"] + " " + r["entity"]).lower())}">'
        f'<a class="bx-card-link" href="/reviews/{slug}/" aria-label="Read the {e(r["brand"])} review">'
        f'{logo_html(slug, r)}<div class="bx-card-main"><h3>{e(r["brand"])}</h3><p class="bx-entity">{e(r["entity"])}</p></div>'
        f'<div class="bx-card-seal">{seal_html(r, "is-sm")}<span>{e(state)}</span></div>'
        f'<div class="bx-card-prog"><div><span>Checks {ep}/5</span>{meter(ep, 5, "checks passed")}</div><div><span>Criteria {cn}/6</span>{meter(cn, 6, "criteria rated")}</div></div>'
        f'<p class="bx-card-offer"><span>Offer</span>{offer}</p></a></article>'
    )


def apply_directory() -> bool:
    d = ROOT / "reviews" / "index.html"
    text = before = d.read_text(encoding="utf-8")
    by: dict[str, list] = {}
    for slug, r in T1["reviews"].items():
        by.setdefault(r["market"], []).append((slug, r))
    sections = []
    for m in M_ORDER:
        items = sorted(by.get(m, []), key=lambda t: (progress_key(t[1]), t[1]["brand"].lower()))
        if not items:
            continue
        cards = "".join(directory_card(s, r) for s, r in items)
        sections.append(
            f'<section class="bx-market" id="{m.lower()}"><div class="bx-market-head"><h2>{e(M_NAME[m])}</h2><p>{len(items)} review{"s" if len(items) != 1 else ""} · regulator: {e(M_REG[m])}</p></div>'
            f'<div class="bx-grid">{cards}</div></section>')
    total = sum(len(v) for v in by.values())
    scored = sum(1 for r in T1["reviews"].values() if score(r) is not None)
    new_main = (
        '<section class="bx-hero"><div class="wrap"><h1>Casino reviews, ordered by evidence</h1>'
        '<p class="bx-lede">Every review starts with five eligibility checks and then scores six criteria out of 100. If we cannot evidence something, we leave it unrated instead of guessing.</p>'
        f'<p class="bx-meta">{total} reviews · {scored} scored · updated {fmt_date(max(r["checked"] for r in T1["reviews"].values()))} · <a href="/how-we-review/">How we score</a></p></div></section>'
        '<div class="wrap bx-tools"><label for="review-search">Search by brand or operator<input id="review-search" type="search" placeholder="bet365, Casumo, Holland Casino"></label>'
        '<label for="review-market">Market<select id="review-market"><option value="">All markets</option>'
        + "".join(f'<option value="{e(M_NAME[m])}">{e(M_NAME[m])}</option>' for m in M_ORDER if m in by)
        + '</select></label><button type="button" id="review-clear-filters" class="bx-btn bx-btn-quiet">Clear</button>'
        '<p class="bx-count" id="review-results-count" role="status" aria-live="polite">' + f"{total} reviews" + '</p></div>'
        '<div class="wrap" id="review-product-grid">' + "".join(sections)
        + '<p class="bx-empty" id="review-no-results" hidden>No review matches that search. Try a brand name or clear the market filter.</p></div>'
    )
    m = re.search(r'<main id="main">.*?</main>', text, re.S)
    text = text.replace(m.group(0), f'<main id="main">\n{new_main}\n</main>', 1)
    # ItemList structured data limited to Tier 1
    items = [{"@type": "ListItem", "position": i + 1, "url": f"https://beincasinos.online/reviews/{s}/", "name": r["brand"] + " review (" + r["market_label"] + ")"}
             for i, (s, r) in enumerate(sorted(T1["reviews"].items(), key=lambda t: (M_ORDER.index(t[1]["market"]), t[1]["brand"].lower())))]
    ld = json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": "BeInCasinos casino reviews", "itemListElement": items}, ensure_ascii=False)
    text = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda _m: f'<script type="application/ld+json">{ld}</script>', text, count=1, flags=re.S)
    if text != before:
        d.write_text(text, encoding="utf-8")
        return True
    return False


def apply_sitemap() -> bool:
    sm = ROOT / "sitemap.xml"
    text = before = sm.read_text(encoding="utf-8")
    for slug, info in AFF["operators"].items():
        if info["market"] not in TIER1:
            text = re.sub(r"\s*<url>\s*<loc>https://beincasinos\.online/reviews/" + re.escape(slug) + r"/</loc>.*?</url>", "", text, flags=re.S)
    if text != before:
        sm.write_text(text, encoding="utf-8")
        return True
    return False


def cmd_apply() -> int:
    changed = [s for s in sorted(p.parent.name for p in REVIEWS.glob("*/index.html")) if apply_review_page(s)]
    di, sm = apply_directory(), apply_sitemap()
    scored = [s for s, r in T1["reviews"].items() if score(r) is not None]
    print(f"Review pages changed: {len(changed)}. Directory changed: {di}. Sitemap changed: {sm}.")
    print(f"Tier 1 reviews: {len(T1['reviews'])}; scored: {len(scored)}.")
    return 0


def cmd_check() -> int:
    errs = []
    for slug, r in T1["reviews"].items():
        p = REVIEWS / slug / "index.html"
        if not p.is_file():
            errs.append(f"{slug}: no review page")
            continue
        if AFF["operators"].get(slug, {}).get("market", "") not in TIER1:
            errs.append(f"{slug}: not a Tier 1 market")
        for k, _ in ELIG:
            st = r["eligibility"][k]
            if st["status"] not in ("pass", "fail", "unverified"):
                errs.append(f"{slug}/{k}: bad status")
            if st["status"] == "pass" and not st.get("url"):
                errs.append(f"{slug}/{k}: a passed check needs a source URL")
        for c in CRITERIA:
            cr = r["criteria"][c["key"]]
            if cr["rating"] is not None and not (isinstance(cr["rating"], int) and 0 <= cr["rating"] <= 5 and str(cr["url"]).startswith("https://")):
                errs.append(f"{slug}/{c['key']}: a rating needs an int 0-5 and an https source URL")
        if r["offer"]["verified"] and not r["offer"]["url"]:
            errs.append(f"{slug}: verified offer needs a source URL")
        text = p.read_text(encoding="utf-8")
        if FILE[0] not in text or BODY[0] not in text:
            errs.append(f"{slug}: blocks missing; run apply")
        shown = re.search(r'class="bx-ring[^"]*" viewBox="0 0 120 120" role="img" aria-label="Score (\d+) out of 100"', text)
        if shown and score(r) != int(shown.group(1)):
            errs.append(f"{slug}: displayed score {shown.group(1)} does not match the data")
        if shown and score(r) is None:
            errs.append(f"{slug}: score shown without full eligibility and ratings")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for slug, info in AFF["operators"].items():
        page = (REVIEWS / slug / "index.html").read_text(encoding="utf-8")
        if info["market"] not in TIER1:
            if f"/reviews/{slug}/</loc>" in sitemap:
                errs.append(f"{slug}: non-Tier-1 page still in sitemap")
            if 'content="noindex' not in page:
                errs.append(f"{slug}: non-Tier-1 page lacks noindex")
        elif ROBOTS[0] in page:
            errs.append(f"{slug}: Tier 1 page is noindex")
    if errs:
        print("Tier 1 check FAILED:\n  " + "\n  ".join(errs))
        return 1
    print(f"Tier 1 check passed ({len(T1['reviews'])} reviews, {sum(1 for r in T1['reviews'].values() if score(r) is not None)} scored).")
    return 0


if __name__ == "__main__":
    cmds = {"apply": cmd_apply, "check": cmd_check}
    if len(sys.argv) != 2 or sys.argv[1] not in cmds:
        raise SystemExit(__doc__)
    sys.exit(cmds[sys.argv[1]]())
