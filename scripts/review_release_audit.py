#!/usr/bin/env python3
"""Read-only QA report for BeInCasinos review HTML files.

Uses Python's standard library only. It does not edit files, publish pages, or
submit URLs to search engines. Run from repository root:
  python3 scripts/review_release_audit.py
  python3 scripts/review_release_audit.py --root reviews --json /tmp/review-audit.json
Exit status: 0 when no high-severity technical flags are found, 1 otherwise.
Human editorial/legal review is still required; this tool cannot verify claims.
"""
from __future__ import annotations
import argparse
import csv
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_parts = []
        self.h1_parts = []
        self.description = ""
        self.canonical = ""
        self.images = []
        self.links = []
        self.text_parts = []
        self._title = self._h1 = False
        self._meta = {}
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title": self._title = True
        if tag == "h1": self._h1 = True
        if tag == "meta":
            name = (a.get("name") or "").lower()
            if name == "description": self.description = a.get("content", "")
        if tag == "link" and "canonical" in (a.get("rel") or "").lower().split():
            self.canonical = a.get("href", "")
        if tag == "img": self.images.append({"src": a.get("src", ""), "alt": a.get("alt")})
        if tag == "a": self.links.append(a.get("href", ""))
    def handle_endtag(self, tag):
        if tag == "title": self._title = False
        if tag == "h1": self._h1 = False
    def handle_data(self, data):
        value = data.strip()
        if value:
            self.text_parts.append(value)
            if self._title: self.title_parts.append(value)
            if self._h1: self.h1_parts.append(value)

def audit(path: Path, root: Path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    parser = PageParser()
    try: parser.feed(raw)
    except Exception: pass
    text = re.sub(r"\s+", " ", " ".join(parser.text_parts)).strip()
    rel = path.relative_to(root).as_posix()
    flags = []
    def flag(code, severity, detail): flags.append({"code": code, "severity": severity, "detail": detail})
    title = " ".join(parser.title_parts).strip()
    h1 = " ".join(parser.h1_parts).strip()
    if not title: flag("missing_title", "high", "No parsed <title>.")
    if not h1: flag("missing_h1", "high", "No parsed <h1>.")
    if len(parser.description.strip()) < 70: flag("short_description", "medium", "Meta description absent or under 70 characters.")
    if parser.canonical and "index.html" in urlparse(parser.canonical).path:
        flag("canonical_index_html", "high", "Canonical URL points to index.html.")
    if not parser.canonical: flag("missing_canonical", "high", "No canonical link found.")
    if not parser.images:
        flag("no_images", "medium", "No <img> element; confirm a deliberate, polished visual fallback.")
    for n, img in enumerate(parser.images, 1):
        if not img["src"]: flag("image_missing_src", "high", f"Image {n} has no src.")
        if img["alt"] is None or not img["alt"].strip():
            flag("image_missing_alt", "medium", f"Image {n} has no useful alt text.")
    if len(text) < 700:
        flag("thin_text", "high", f"Only about {len(text)} characters of parsed visible text.")
    if not re.search(r"affiliate|commission|commercial relationship", text, re.I):
        flag("affiliate_disclosure_not_detected", "high", "Disclosure wording not detected; manual check required.")
    if not re.search(r"responsible gambling|safer gambling|gambling support|gamble responsibly", text, re.I):
        flag("safer_gambling_not_detected", "high", "Safer-gambling wording not detected; manual check required.")
    if re.search(r"\b(we tested|our hands-on test|we deposited|we withdrew)\b", text, re.I):
        flag("first_hand_testing_claim", "critical", "First-hand testing language found; verify a documented test actually occurred.")
    if re.search(r"\b(100% safe|guaranteed win|risk[- ]free)\b", text, re.I):
        flag("absolute_gambling_claim", "critical", "Potentially misleading absolute claim found.")
    if re.search(r"\bscore\s*:?\s*\d+(?:\.\d+)?\s*/\s*10\b", text, re.I):
        flag("numeric_score_present", "info", "Numeric score detected; verify completed evidence rubric and approval.")
    return {
        "file": rel, "title": title, "h1": h1, "canonical": parser.canonical,
        "visible_text_chars": len(text), "image_count": len(parser.images),
        "internal_link_count": sum(1 for u in parser.links if u.startswith("/") and not u.startswith("//")),
        "flag_count": len(flags), "flags": flags,
    }

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default="reviews", help="Directory containing review HTML files (default: reviews)")
    ap.add_argument("--json", dest="json_path", help="Optional path for a JSON report")
    ap.add_argument("--csv", dest="csv_path", help="Optional path for a flat CSV report")
    args = ap.parse_args()
    root = Path(args.root)
    if not root.exists():
        print(f"ERROR: review root does not exist: {root}", file=sys.stderr); return 2
    pages = sorted(root.rglob("*.html"))
    if not pages:
        print(f"ERROR: no HTML files found under {root}", file=sys.stderr); return 2
    results = [audit(p, root) for p in pages]
    counts = Counter(f["code"] for page in results for f in page["flags"])
    summary = {
        "scope": str(root), "page_count": len(results),
        "pages_with_flags": sum(bool(p["flags"]) for p in results),
        "flag_counts_by_code": dict(sorted(counts.items())),
        "pages": results,
        "limitations": [
            "Static heuristics only; they do not verify current licensing, terms, bonus eligibility, facts, image rights, or market legality.",
            "A detected disclosure phrase is not proof of adequate disclosure; a missing phrase may be expressed differently.",
            "No files are changed and no deployment, sitemap submission, or indexing request is performed."
        ]
    }
    print(f"Review HTML files: {len(results)}")
    print(f"Pages with at least one flag: {summary['pages_with_flags']}")
    for code, count in sorted(counts.items()): print(f"  {code}: {count}")
    if args.json_path: Path(args.json_path).write_text(json.dumps(summary, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    if args.csv_path:
        with Path(args.csv_path).open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["file","title","h1","canonical","visible_text_chars","image_count","internal_link_count","flag_count","flags"])
            w.writeheader()
            for p in results:
                row = dict(p); row["flags"] = "; ".join(f'{x["severity"]}:{x["code"]}' for x in p["flags"])
                w.writerow(row)
    return 1 if any(f["severity"] in ("high", "critical") for p in results for f in p["flags"]) else 0

if __name__ == "__main__":
    raise SystemExit(main())
