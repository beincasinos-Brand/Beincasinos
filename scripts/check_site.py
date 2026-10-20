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
        self.h1_count = 0
        self.links = []
        self.resources = []
        self.ids = set()
        self.id_counts = {}
        self.images_missing_alt = 0
        self.html_lang = None
        self.has_viewport = False
        self.unsafe_new_tab_links = []
        self.empty_links = []
        self._link_depth = 0
        self._link_text = []
        self._current_link = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.html_lang = a.get("lang", "").strip()
        if "id" in a:
            self.ids.add(a["id"])
            self.id_counts[a["id"]] = self.id_counts.get(a["id"], 0) + 1
        if tag == "img" and "alt" not in a:
            self.images_missing_alt += 1
        if tag == "title":
            self.title_depth += 1
        if tag == "meta":
            if a.get("name", "").lower() == "description":
                self.description = a.get("content", "").strip()
            if a.get("name", "").lower() == "viewport":
                self.has_viewport = bool(a.get("content", "").strip())
        if tag == "h1":
            self.h1_count += 1
            self.h1_depth += 1
        if tag in ("a", "area") and a.get("href"):
            self.links.append(a["href"].strip())
            if tag == "a":
                if a.get("target", "").lower() == "_blank":
                    rel = {part.lower() for part in a.get("rel", "").split()}
                    if "noopener" not in rel:
                        self.unsafe_new_tab_links.append(a.get("href", ""))
                self._current_link = {"href": a["href"], "has_label": bool(a.get("aria-label", "").strip() or a.get("aria-labelledby", "").strip())}
                self._link_text = []
                self._link_depth = 1
        elif self._link_depth and tag in ("img", "svg", "input"):
            if tag == "img" and a.get("alt", "").strip():
                self._link_text.append("image alt")
            elif a.get("aria-label", "").strip() or a.get("title", "").strip():
                self._link_text.append("accessible label")
        if tag in ("script", "img", "source", "iframe", "audio", "video") and a.get("src"):
            self.resources.append(a["src"].strip())
        if tag == "link" and a.get("href"):
            self.resources.append(a["href"].strip())

    def handle_endtag(self, tag):
        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        if tag == "h1" and self.h1_depth:
            self.h1_depth -= 1
        if tag == "a" and self._link_depth:
            text_content = " ".join(" ".join(self._link_text).split())
            if not text_content and not self._current_link.get("has_label"):
                self.empty_links.append(self._current_link.get("href", ""))
            self._link_depth = 0
            self._current_link = None
            self._link_text = []

    def handle_data(self, data):
        if self.title_depth:
            self.title += data
        if self._link_depth:
            self._link_text.append(data)


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
    if not parser.html_lang:
        errors.append(f"{rel}: missing html lang attribute")
    if not parser.has_viewport:
        errors.append(f"{rel}: missing responsive viewport meta tag")
    duplicate_ids = sorted(identifier for identifier, count in parser.id_counts.items() if count > 1)
    if duplicate_ids:
        errors.append(f"{rel}: duplicate id attribute(s): " + ", ".join(duplicate_ids))
    if parser.images_missing_alt:
        errors.append(f"{rel}: {parser.images_missing_alt} image(s) missing alt attribute")
    for href in parser.unsafe_new_tab_links:
        errors.append(f"{rel}: target=_blank link missing rel=noopener: {href}")
    for href in parser.empty_links:
        errors.append(f"{rel}: link has no text or accessible label: {href}")
    for raw in parser.links + parser.resources:
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
# Surface content whose market-specific primary-source review is still pending.
for page in pages:
    rel = page.relative_to(ROOT).as_posix()
    try:
        source = page.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        continue
    if re.search(r"Reviewed for launch: pending|review status: pending", source, re.I):
        warnings.append(f"{rel}: content review is explicitly pending; verify claims against current primary sources before launch")

for rel in ("privacy/index.html", "contact/index.html"):
    page = ROOT / rel
    if page.exists() and re.search(r"pre-launch|not yet been finalised|not yet been finalized|draft", page.read_text(encoding="utf-8"), re.I):
        warnings.append(f"{rel}: contains an explicit pre-launch notice and must be finalised before public launch")

# Validate that every sitemap URL points to an existing local HTML page.
if sitemap.exists():
    try:
        import xml.etree.ElementTree as ET
        sitemap_root = ET.fromstring(sitemap.read_text(encoding="utf-8"))
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        for loc in sitemap_root.findall(".//sm:loc", ns):
            url = (loc.text or "").strip()
            parsed = urlparse(url)
            if parsed.scheme not in ("http", "https") or not parsed.netloc:
                errors.append(f"sitemap.xml: invalid absolute URL: {url}")
                continue
            sitemap_path = unquote(parsed.path or "/")
            target = ROOT / sitemap_path.lstrip("/")
            if target.is_dir():
                target = target / "index.html"
            elif not target.suffix:
                target = target / "index.html"
            try:
                target.resolve().relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"sitemap.xml: URL path escapes site root: {url}")
                continue
            if not target.is_file() or target.suffix.lower() not in (".html", ".htm"):
                errors.append(f"sitemap.xml: URL does not map to an HTML page: {url}")
    except (ET.ParseError, OSError, UnicodeError) as exc:
        errors.append(f"sitemap.xml: cannot parse sitemap XML ({exc})")

# Guard the two interactive learning tools against accidental markup regressions.
calculator_path = ROOT / "tools/wagering-calculator/index.html"
if calculator_path.exists():
    calculator_source = calculator_path.read_text(encoding="utf-8")
    for required_id in ("wager-form", "eligible", "currency", "multiplier", "turnover", "result-summary", "calc-error"):
        if not re.search(r'\\bid=["\\']' + re.escape(required_id) + r'["\\']', calculator_source):
            errors.append(f"tools/wagering-calculator/index.html: required calculator control missing: {required_id}")
    if "Number.isFinite(result)" not in calculator_source or "event.preventDefault()" not in calculator_source:
        errors.append("tools/wagering-calculator/index.html: calculation validation or form-submit handling is missing")

checklist_path = ROOT / "tools/terms-checklist/index.html"
if checklist_path.exists():
    checklist_source = checklist_path.read_text(encoding="utf-8")
    checkbox_count = len(re.findall(r'<input\\b[^>]*type=["\\']checkbox["\\']', checklist_source, re.I))
    if checkbox_count != 13:
        errors.append(f"tools/terms-checklist/index.html: expected 13 checklist items, found {checkbox_count}")
    for required_id in ("checked-count", "total-count", "progress-fill", "progress-track", "progress-message", "print-checklist", "reset-checklist"):
        if not re.search(r'\\bid=["\\']' + re.escape(required_id) + r'["\\']', checklist_source):
            errors.append(f"tools/terms-checklist/index.html: required checklist control missing: {required_id}")
    for required_behavior in ("aria-valuenow", "aria-valuemax", "window.print()", "box.checked = false"):
        if required_behavior not in checklist_source:
            errors.append(f"tools/terms-checklist/index.html: expected interaction/accessibility behavior missing: {required_behavior}")

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
