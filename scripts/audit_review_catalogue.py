#!/usr/bin/env python3
"""Audit BeInCasinos' public brand-review catalogue without running CI/deploy.

Run from the repository root: python3 scripts/audit_review_catalogue.py
This checks source files only; it cannot confirm live HTTP status or indexing.
"""
from pathlib import Path
from urllib.parse import urlparse
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://beincasinos.online"
REVIEWS = ROOT / "reviews"
SITEMAP = ROOT / "sitemap.xml"

def canonical_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        suffix = "/"
    elif rel.endswith("/index.html"):
        suffix = "/" + rel[:-len("index.html")]
    else:
        suffix = "/" + rel
    return ORIGIN + suffix

if not SITEMAP.exists():
    raise SystemExit("ERROR: sitemap.xml is missing")
try:
    root = ET.parse(SITEMAP).getroot()
except (ET.ParseError, OSError) as exc:
    raise SystemExit(f"ERROR: cannot parse sitemap.xml: {exc}")
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap_urls = {
    (node.text or "").strip()
    for node in root.findall(".//sm:loc", ns)
    if (node.text or "").strip()
}

html_pages = sorted(
    p for p in REVIEWS.rglob("*.html")
    if p.is_file() and p.name.lower() != "index.html"
) if REVIEWS.exists() else []
# An index.html at a brand-specific nested path is a page, not the reviews hub.
nested_index_pages = sorted(
    p for p in REVIEWS.rglob("index.html")
    if p.is_file() and p.parent != REVIEWS
) if REVIEWS.exists() else []
review_pages = sorted(set(html_pages + nested_index_pages))

print("BeInCasinos public brand-review source audit")
print(f"Dedicated review HTML pages: {len(review_pages)}")
print(f"Sitemap URLs: {len(sitemap_urls)}")
missing = []
for page in review_pages:
    source = page.read_text(encoding="utf-8", errors="replace")
    url = canonical_url(page)
    if url not in sitemap_urls:
        missing.append((page.relative_to(ROOT).as_posix(), url, "missing from sitemap"))
    match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)', source, re.I)
    if not match:
        missing.append((page.relative_to(ROOT).as_posix(), url, "canonical missing"))
    elif match.group(1) != url:
        missing.append((page.relative_to(ROOT).as_posix(), url, f"canonical mismatch: {match.group(1)}"))

if not review_pages:
    print("STATUS: NO DEDICATED BRAND REVIEW PAGES FOUND")
else:
    for page in review_pages:
        print(f"- {page.relative_to(ROOT).as_posix()} -> {canonical_url(page)}")

if missing:
    print("BLOCKERS:")
    for path, url, issue in missing:
        print(f"- {path}: {issue} ({url})")
else:
    print("Review-page canonical/sitemap source checks: PASS")

print("LIMITATION: source audit only; does not verify deployment, HTTP status, robots, "
      "Search Console discovery/indexing, editorial evidence, or second-editor approval.")
