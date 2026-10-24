#!/usr/bin/env python3
"""Static release gate for the internal 100-card brand research directory.

This check validates source consistency only. It does not certify legal eligibility,
image reuse rights, live image rendering, or publication approval.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "brand-directory" / "index.html"
REGISTER_PATH = ROOT / "docs" / "targets" / "brand-image-asset-register-2026-10-23.csv"
SITEMAP_PATH = ROOT / "sitemap.xml"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    for path in (HTML_PATH, REGISTER_PATH, SITEMAP_PATH):
        if not path.is_file():
            fail(f"required file missing: {path.relative_to(ROOT)}")

    html = HTML_PATH.read_text(encoding="utf-8")
    sitemap = SITEMAP_PATH.read_text(encoding="utf-8")
    with REGISTER_PATH.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    cards = re.findall(r'<article class="brand-card"[^>]*>[\s\S]*?</article>', html)
    if len(cards) != 100:
        fail(f"expected 100 directory cards, found {len(cards)}")

    def card_title(card: str) -> str:
        match = re.search(r"<h2[^>]*>([\s\S]*?)</h2>", card)
        return re.sub(r"<[^>]+>", "", match.group(1)).strip() if match else ""

    titles = [card_title(card) for card in cards]
    if any(not title for title in titles):
        fail("one or more cards has no readable h2 title")
    duplicates = sorted({title.casefold() for title in titles if titles.count(title) > 1})
    if duplicates:
        fail("duplicate displayed titles: " + ", ".join(duplicates))

    robots = re.search(r'<meta\s+name="robots"\s+content="([^"]+)"', html, re.I)
    if not robots or robots.group(1).strip().lower() != "noindex,follow":
        fail("directory must remain noindex,follow until release gates pass")
    if "brand-directory" in sitemap:
        fail("directory URL must remain excluded from sitemap while on HOLD")

    if len(rows) != 100:
        fail(f"expected 100 image-register rows, found {len(rows)}")
    by_name = {row.get("brand_name", "").strip().casefold(): row for row in rows}
    if len(by_name) != len(rows):
        fail("duplicate brand_name keys in image register")
    missing_register_names = sorted(set(title.casefold() for title in titles) - set(by_name))
    if missing_register_names:
        fail("card titles missing from image register: " + ", ".join(missing_register_names))

    images = 0
    mismatches: list[str] = []
    for card, title in zip(cards, titles):
        match = re.search(r"<img\b[^>]*>", card, re.I)
        if not match:
            continue
        images += 1
        tag = match.group(0)
        src = re.search(r'\bsrc="([^"]+)"', tag, re.I)
        alt = re.search(r'\balt="([^"]*)"', tag, re.I)
        if not src or not src.group(1).strip():
            fail(f"{title}: image has no src")
        if not alt or not alt.group(1).strip():
            fail(f"{title}: image has no useful alt text")
        if 'loading="lazy"' not in tag:
            fail(f"{title}: image is missing lazy loading")
        if "onerror=" not in tag:
            fail(f"{title}: image is missing its fallback handler")
        row = by_name.get(title.casefold())
        if row is None or row.get("image_asset_url", "").strip() != src.group(1).strip():
            mismatches.append(title)

    if mismatches:
        fail("HTML/register image URL mismatch: " + ", ".join(mismatches))

    hold = sum('data-status="HOLD"' in card for card in cards)
    exclude = sum('data-status="EXCLUDE"' in card for card in cards)
    candidates = sum(bool(row.get("image_asset_url", "").strip()) for row in rows)
    fallbacks = len(rows) - candidates
    print("PASS: static brand-directory source checks")
    print(f"Cards: {len(cards)}; unique titles: {len(set(t.casefold() for t in titles))}")
    print(f"Status: {hold} HOLD / {exclude} EXCLUDE")
    print(f"Images: {images}; register candidates: {candidates}; fallback rows: {fallbacks}")
    print("All HTML image URLs match the register; alt text, lazy loading and fallback hooks are present.")
    print("SEO guardrail: noindex,follow; directory excluded from sitemap.")
    print("NOTE: source QA only; no legal, rights, live-browser, or publication approval is implied.")


if __name__ == "__main__":
    main()
