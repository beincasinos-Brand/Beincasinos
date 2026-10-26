#!/usr/bin/env python3
"""Manage affiliate links for BeInCasinos in one place.

Source of truth: data/affiliate-links.json (never published; the build allowlist
does not include data/).

Commands
  init   Add a skeleton entry for every review page missing from the data file.
  apply  Validate active entries, then (re)write the managed blocks:
           - /go/<slug> redirects in _redirects
           - sponsored CTA + disclosure inside each active review page
           - live wording on /affiliate-disclosure/ and /privacy/
         Entries with "active": false get their blocks removed.
  check  Read-only consistency check used by CI (exit 1 on any problem).

Nothing is ever activated by this script itself: an entry goes live only when
the owner sets "active": true AND every gate below passes.
"""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "affiliate-links.json"
REVIEWS = ROOT / "reviews"
REDIRECTS = ROOT / "_redirects"
DISCLOSURE = ROOT / "affiliate-disclosure" / "index.html"
PRIVACY = ROOT / "privacy" / "index.html"

REL = "sponsored nofollow noopener"
CTA_START, CTA_END = "<!-- affiliate-cta:start -->", "<!-- affiliate-cta:end -->"
DISC_START, DISC_END = "<!-- affiliate-disclosure:start -->", "<!-- affiliate-disclosure:end -->"
LIVE_START, LIVE_END = "<!-- affiliate-live:start -->", "<!-- affiliate-live:end -->"
RED_START, RED_END = "# affiliate-links:start", "# affiliate-links:end"

SLUG_MARKETS = [  # (slug fragment, market code) — a starting guess only; owner confirms
    ("great-britain", "GB"), ("-gb", "GB"), ("spain", "ES"), ("germany", "DE"),
    ("switzerland", "CH"), ("netherlands", "NL"), ("belgium", "BE"), ("sweden", "SE"),
    ("italy", "IT"), ("michigan", "US-MI"), ("british-columbia", "CA-BC"),
]

DEFAULT_BLOCKED = {
    "IT": "Italian gambling advertising rules (Decreto Dignita) are very restrictive; get legal advice before any affiliate promotion.",
    "BE": "Belgian online-casino advertising is tightly restricted; get legal advice before any affiliate promotion.",
    "FR": "France does not license online casino games; promotion needs specialist legal review.",
    "AU": "Australia restricts online-casino services and promotion; needs specialist legal review.",
    "ES": "Spain regulates gambling commercial communications and bonus promotion; confirm affiliate rules with DGOJ guidance and the programme.",
    "SE": "Sweden requires moderate marketing and restricts bonus promotion; confirm against Spelinspektionen guidance.",
}
SAFER_NOTES = {
    "GB": "18+ only. T&amp;Cs apply. Gambling can be addictive: <a href=\"https://www.begambleaware.org/\" rel=\"nofollow noopener\">BeGambleAware</a> · <a href=\"https://www.gamstop.co.uk/\" rel=\"nofollow noopener\">GAMSTOP</a>.",
}
GENERIC_NOTE = "18+ only where legal. T&amp;Cs apply. Gambling involves risk of loss; see our <a href=\"/responsible-gambling/\">safer gambling</a> page."


def load() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def save(data: dict) -> None:
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def guess_market(slug: str) -> str:
    for frag, code in SLUG_MARKETS:
        if frag in slug:
            return code
    return ""


def brand_from_page(slug: str) -> str:
    text = (REVIEWS / slug / "index.html").read_text(encoding="utf-8")
    m = re.search(r"<h1>(.*?)</h1>", text, re.S)
    name = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else slug
    name = re.split(r"\s+(?:review|casino review)\b", name, flags=re.I)[0].strip(": -")
    return html.unescape(name) or slug


def review_slugs() -> list[str]:
    return sorted(p.parent.name for p in REVIEWS.glob("*/index.html"))


def new_entry(slug: str) -> dict:
    return {
        "brand": brand_from_page(slug),
        "market": guess_market(slug),
        "active": False,
        "affiliate_url": "",
        "programme": "",
        "programme_terms_checked": "",
        "geo_confirmed": False,
        "licence_verified": False,
        "legal_review_ref": "",
        "licence_line": "",
    }


def cmd_init() -> int:
    data = load() if DATA.exists() else {
        "schema_version": 1,
        "_readme": "Set active=true only after every gate in scripts/affiliate_links.py passes. Never store passwords or API keys here; affiliate URLs are public once live.",
        "privacy_updated": False,
        "blocked_markets": DEFAULT_BLOCKED,
        "operators": {},
    }
    added = 0
    for slug in review_slugs():
        if slug not in data["operators"]:
            data["operators"][slug] = new_entry(slug)
            added += 1
    save(data)
    print(f"Skeleton written: {added} new operator entries, {len(data['operators'])} total. Nothing is active.")
    return 0


def problems_for(slug: str, e: dict, data: dict) -> list[str]:
    errs: list[str] = []
    if not e.get("active"):
        return errs
    url = e.get("affiliate_url", "")
    p = urlparse(url)
    if p.scheme != "https" or not p.netloc:
        errs.append("affiliate_url must be an https URL")
    if re.search(r"[\s\"'<>]", url):
        errs.append("affiliate_url contains unsafe characters")
    if not (REVIEWS / slug / "index.html").is_file():
        errs.append("no review page for this slug")
    if not e.get("programme"):
        errs.append("programme (name of the official affiliate programme) is required")
    try:
        date.fromisoformat(e.get("programme_terms_checked", ""))
    except ValueError:
        errs.append("programme_terms_checked must be an ISO date (YYYY-MM-DD)")
    if not e.get("geo_confirmed"):
        errs.append("geo_confirmed must be true (programme allows this market and your traffic)")
    if not e.get("licence_verified"):
        errs.append("licence_verified must be true (checked against the regulator register)")
    market = e.get("market", "")
    if not market:
        errs.append("market is required")
    if market in data.get("blocked_markets", {}) and not e.get("legal_review_ref"):
        errs.append(f"market {market} is flagged: {data['blocked_markets'][market]} Add legal_review_ref once cleared.")
    if not data.get("privacy_updated"):
        errs.append("privacy_updated is false at top level; confirm the privacy notice matches your tracking first")
    return errs


def active_entries(data: dict) -> dict:
    return {s: e for s, e in data["operators"].items() if e.get("active")}


def replace_block(text: str, start: str, end: str, block: str | None, anchor_before: str | None = None, anchor_after: str | None = None) -> str:
    """Remove any existing marked block, then insert `block` once (if given)."""
    text = re.sub(re.escape(start) + r".*?" + re.escape(end) + r"\n?", "", text, flags=re.S)
    if block is None:
        return text
    wrapped = f"{start}\n{block}\n{end}\n"
    if anchor_after and anchor_after in text:
        return text.replace(anchor_after, anchor_after + wrapped, 1)
    if anchor_before and anchor_before in text:
        return text.replace(anchor_before, wrapped + anchor_before, 1)
    raise SystemExit(f"Anchor not found for block {start}")


def cta_html(slug: str, e: dict) -> str:
    brand = html.escape(e["brand"])
    note = SAFER_NOTES.get(e["market"], GENERIC_NOTE)
    licence = f'<p class="small muted">{html.escape(e["licence_line"])}</p>' if e.get("licence_line") else ""
    return (
        '<div class="aff-box"><p class="aff-label">Sponsored link</p>'
        f'<a class="aff-btn" href="/go/{slug}" rel="{REL}" target="_blank">Visit {brand} &#8599;</a>'
        f"{licence}"
        '<p class="small muted">We may earn a commission if you register through this link. '
        'It does not change our evidence checks or the facts on this page. '
        '<a href="/affiliate-disclosure/">Affiliate disclosure</a></p>'
        f'<p class="small muted">{note}</p></div>'
    )


def disclosure_html(e: dict) -> str:
    brand = html.escape(e["brand"])
    return (
        f'<p><strong>Commercial disclosure:</strong> BeInCasinos has an affiliate relationship with {brand}'
        f' ({html.escape(e["programme"])}) and may earn a commission if you register or deposit through the sponsored link on this page. '
        'The relationship does not determine our research findings, and a commission is not evidence that an operator is safe, '
        'licensed for your location or suitable for you. See our <a href="/affiliate-disclosure/">affiliate disclosure</a>.</p>'
    )


OLD_DISCLOSURE = re.compile(r"<p><strong>Commercial disclosure:</strong> No brand-specific paid placement or affiliate relationship is asserted by this review\.[^<]*</p>")


def apply_page(slug: str, e: dict | None) -> bool:
    page = REVIEWS / slug / "index.html"
    text = page.read_text(encoding="utf-8")
    before = text
    live = bool(e and e.get("active"))
    text = replace_block(text, CTA_START, CTA_END, cta_html(slug, e) if live else None, anchor_after='<aside class="sidebar">')
    text = replace_block(text, DISC_START, DISC_END, disclosure_html(e) if live else None, anchor_before="</article>")
    if live:
        text = OLD_DISCLOSURE.sub("", text)  # would contradict the live disclosure
    if text != before:
        page.write_text(text, encoding="utf-8")
        return True
    return False


def redirects_block(actives: dict) -> str | None:
    if not actives:
        return None
    lines = [f"/go/{slug} {e['affiliate_url']} 302" for slug, e in sorted(actives.items())]
    return "\n".join(lines)


def write_redirects(actives: dict) -> None:
    text = REDIRECTS.read_text(encoding="utf-8")
    text = re.sub(r"\n?" + re.escape(RED_START) + r".*?" + re.escape(RED_END) + r"\n?", "\n", text, flags=re.S).rstrip("\n") + "\n"
    block = redirects_block(actives)
    if block:
        text += f"\n{RED_START}\n{block}\n{RED_END}\n"
    REDIRECTS.write_text(text, encoding="utf-8")


def write_policy_pages(actives: dict) -> None:
    live_disc = (
        "<h2>Affiliate links are live</h2><p>Some review pages now contain links to operators with which BeInCasinos has an affiliate relationship. "
        "Each such link is labelled &ldquo;Sponsored link&rdquo; next to the button, carries <code>rel=\"sponsored nofollow\"</code>, "
        "and the page states the relationship. Links route through a <code>/go/</code> address on this site so the destination can be corrected in one place. "
        "A commission is not proof that an operator is safe, licensed for your location or suitable for you. "
        "Rankings and conclusions are not sold, and unverified operators are not recommended.</p>"
    )
    live_priv = (
        "<h2>Affiliate links and outbound clicks</h2><p>When you click a sponsored link, your request passes through a redirect on this site "
        "to the operator's official affiliate address. The operator or its affiliate network may set cookies or log your visit to credit BeInCasinos with a referral; "
        "that processing is under their own privacy policy. BeInCasinos does not add analytics or advertising cookies of its own for this purpose. "
        "Cloudflare processes technical request data as described above.</p>"
    )
    for path, s, e, body, before in (
        (DISCLOSURE, LIVE_START, LIVE_END, live_disc, "<h2>Questions</h2>"),
        (PRIVACY, LIVE_START, LIVE_END, live_priv, "<h2>Technical data and hosting</h2>"),
    ):
        text = path.read_text(encoding="utf-8")
        new = replace_block(text, s, e, body if actives else None, anchor_before=before)
        # The static "currently none" wording is only true while nothing is active.
        if path == DISCLOSURE:
            new = new.replace("No paid listings, operator rankings, bonus offers, or affiliate links are currently being offered or endorsed on this page.",
                              "No paid listings, operator rankings or bonus offers are being sold on this page; affiliate links are listed in the section above where they apply." if actives else
                              "No paid listings, operator rankings, bonus offers, or affiliate links are currently being offered or endorsed on this page.")
        if new != text:
            path.write_text(new, encoding="utf-8")


def cmd_apply() -> int:
    data = load()
    errors = []
    for slug, e in data["operators"].items():
        for msg in problems_for(slug, e, data):
            errors.append(f"{slug}: {msg}")
    if errors:
        print("Refusing to apply — fix these first:\n  " + "\n  ".join(errors))
        return 1
    actives = active_entries(data)
    changed = [s for s in review_slugs() if apply_page(s, data["operators"].get(s))]
    write_redirects(actives)
    write_policy_pages(actives)
    print(f"Applied. Active affiliate links: {len(actives)}. Review pages changed: {len(changed)}.")
    return 0


def cmd_check() -> int:
    data = load()
    errs: list[str] = []
    actives = active_entries(data)
    for slug, e in data["operators"].items():
        errs += [f"{slug}: {m}" for m in problems_for(slug, e, data)]
        if not (REVIEWS / slug / "index.html").is_file():
            errs.append(f"{slug}: listed in data but no review page")
    red = REDIRECTS.read_text(encoding="utf-8")
    m = re.search(re.escape(RED_START) + r"\n(.*?)\n" + re.escape(RED_END), red, re.S)
    if (m.group(1) if m else None) != redirects_block(actives):
        errs.append("_redirects affiliate block is out of sync; run `python3 scripts/affiliate_links.py apply`")
    hosts = {urlparse(e["affiliate_url"]).netloc.lower() for e in actives.values() if e.get("affiliate_url")}
    for page in ROOT.rglob("*.html"):
        if any(part in {".git", "dist", "node_modules"} for part in page.parts):
            continue
        text = page.read_text(encoding="utf-8")
        rel_path = page.relative_to(ROOT)
        has_block = CTA_START in text
        slug = page.parent.name if page.parent.parent == REVIEWS else None
        should = bool(slug and slug in actives)
        if has_block != should:
            errs.append(f"{rel_path}: affiliate block {'present' if has_block else 'missing'} but entry is {'active' if should else 'inactive'}")
        if has_block and (DISC_START not in text or "18+" not in text):
            errs.append(f"{rel_path}: affiliate page lacks disclosure paragraph or 18+ notice")
        for tag in re.findall(r"<a\b[^>]*>", text):
            href = re.search(r'href="([^"]*)"', tag)
            if not href:
                continue
            h = href.group(1)
            if h.startswith("/go/"):
                if not all(w in tag for w in ("sponsored", "nofollow", "noopener")):
                    errs.append(f"{rel_path}: /go/ link missing rel=sponsored nofollow noopener")
                if h[4:] not in actives:
                    errs.append(f"{rel_path}: /go/ link to inactive slug {h}")
            elif hosts and urlparse(h).netloc.lower() in hosts:
                errs.append(f"{rel_path}: raw affiliate URL used directly; use the /go/ path")
    if errs:
        print("Affiliate check FAILED:\n  " + "\n  ".join(errs))
        return 1
    print(f"Affiliate check passed. Active links: {len(actives)} of {len(data['operators'])} operators.")
    return 0


if __name__ == "__main__":
    cmds = {"init": cmd_init, "apply": cmd_apply, "check": cmd_check}
    if len(sys.argv) != 2 or sys.argv[1] not in cmds:
        raise SystemExit(__doc__)
    sys.exit(cmds[sys.argv[1]]())
