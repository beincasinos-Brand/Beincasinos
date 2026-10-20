#!/usr/bin/env python3
"""Dependency-free quality checks for the BeInCasinos static site.

Run from the repository root: python3 scripts/check_site.py
This is a source-level check, not a substitute for browser, accessibility,
legal, privacy, or production-host testing.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
IGNORE_DIRS = {".git", ".vercel", "node_modules"}
errors = []
warnings = []
pages = sorted(p for p in ROOT.rglob("*.html") if not any(part in IGNORE_DIRS for part in p.parts))
titles = {}

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_depth = 0
        self.title = ""
        self.description = ""
        self.h1_depth = 0
        self.h1_text = []
        self.h1_count = 0
        self.links = []
        self.ids = set()
        self.id_counts = {}
        self.images_missing_alt = 0
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
            self.id_counts[a["id"]] = self.id_counts.get(a["id"], 0) + 1
        if tag == "img" and "alt" not in a:
            self.images_missing_alt += 1
        if tag == "title":
            self.title_depth += 1
        if tag == "meta" and a.get("name", "").lower() == "description":
            self.description = a.get("content", "").strip()
        if tag == "h1":
            self.h1_count += 1
            self.h1_depth += 1
        if tag in ("a", "area") and a.get("href"):
            self.links.append(a["href"].strip())
    def handle_endtag(self, tag):
        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        if tag == "h1" and self.h1_depth:
            self.h1_depth -= 1
    def handle_data(self, data):
        if self.title_depth:
            self.title += data

def resolve_local_url(page, raw):
    parsed = urlparse(raw)
    if parsed.scheme or parsed.netloc or raw.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None, parsed.fragment
    path = unquote(parsed.path)
    if not path:
        target = page
    elif path.startswith("/"):
        target = ROOT / path.lstrip("/")
    else:
        target = page.parent / path
    if target.is_dir():
        target = target / "index.html"
    elif not target.suffix:
        target = target / "index.html"
    return target.resolve(), parsed.fragment

for page in pages:
    rel = page.relative_to(ROOT).as_posix()
    parser = PageParser()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        errors.append(f"{rel}: cannot read HTML ({exc})")
        continue
    title = " ".join(parser.title.split())
    if not title:
        errors.append(f"{rel}: missing <title>")
    else:
        titles.setdefault(title.casefold(), []).append(rel)
    if not parser.description:
        errors.append(f"{rel}: missing meta description")
    if parser.h1_count != 1:
        errors.append(f"{rel}: expected exactly one h1, found {parser.h1_count}")
    duplicate_ids = sorted(identifier for identifier, count in parser.id_counts.items() if count > 1)
    if duplicate_ids:
        errors.append(f"{rel}: duplicate id attribute(s): " + ", ".join(duplicate_ids))
    if parser.images_missing_alt:
        errors.append(f"{rel}: {parser.images_missing_alt} image(s) missing alt attribute")
    for raw in parser.links:
        target, fragment = resolve_local_url(page, raw)
        if target is None:
            continue
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{rel}: local link escapes site root: {raw}")
            continue
        if not target.exists():
            errors.append(f"{rel}: broken local link: {raw}")
        elif fragment and target.suffix.lower() in (".html", ".htm"):
            try:
                target_parser = PageParser()
                target_parser.feed(target.read_text(encoding="utf-8"))
                if fragment not in target_parser.ids:
                    warnings.append(f"{rel}: fragment target not statically verified: {raw}")
            except (OSError, UnicodeError):
                pass

for title, paths in titles.items():
    if len(paths) > 1:
        errors.append(f"duplicate title {title!r}: " + ", ".join(paths))

robots = ROOT / "robots.txt"
if robots.exists() and "Disallow: /" not in robots.read_text(encoding="utf-8"):
    warnings.append("robots.txt no longer blocks crawling; confirm launch approval before removing the pre-launch block")
sitemap = ROOT / "sitemap.xml"
if sitemap.exists() and re.search(r"YOUR-DOMAIN|example\.com|\.example", sitemap.read_text(encoding="utf-8"), re.I):
    warnings.append("sitemap.xml contains a domain placeholder; replace after the production domain is chosen")
for rel in ("privacy/index.html", "contact/index.html"):
    page = ROOT / rel
    if page.exists() and re.search(r"pre-launch|not yet been finalised|not yet been finalized|draft", page.read_text(encoding="utf-8"), re.I):
        warnings.append(f"{rel}: contains an explicit pre-launch notice and must be finalised before public launch")

print(f"Checked {len(pages)} HTML pages.")
if errors:
    print(f"\nFAIL: {len(errors)} error(s)")
    for item in errors:
        print(f"  ERROR: {item}")
if warnings:
    print(f"\nWARN: {len(warnings)} launch/verification warning(s)")
    for item in warnings:
        print(f"  WARN: {item}")
if not errors:
    print("\nPASS: no structural errors detected by this source-level checker.")
    print("Reminder: this does not test rendering, accessibility, external links, legal compliance, or production behaviour.")
sys.exit(1 if errors else 0)
