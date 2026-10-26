#!/usr/bin/env python3
"""Normalize public HTML social metadata before site QA."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"404.html", "google05b7a00eb84d7acb.html"}

def get_meta(source, key, value):
    attr = "name" if key == "name" else "property"
    for match in re.finditer(r"<meta\b[^>]*>", source, re.I):
        tag = match.group(0)
        found = re.search(r"\b" + attr + r""" \s*=\s*(['"])(.*?)\1""".replace(" ", ""), tag, re.I)
        if found and found.group(2).lower() == value.lower():
            content = re.search(r"""\bcontent\s*=\s*(['"])(.*?)\1""", tag, re.I)
            return content.group(2) if content else ""
    return None

def update_meta(source, key, value, content):
    attr = "name" if key == "name" else "property"
    pattern = re.compile(r"<meta\b(?=[^>]*\b" + attr + r"""\s*=\s*(['"])""" + re.escape(value) + r"""\1)[^>]*>""", re.I)
    match = pattern.search(source)
    safe = content.replace('"', "&quot;")
    replacement = f'<meta {attr}="{value}" content="{safe}">'
    if match:
        old = match.group(0)
        if re.search(r"""\bcontent\s*=\s*(['"]).*?\1""", old, re.I):
            updated = re.sub(r"""\bcontent\s*=\s*(['"]).*?\1""", f'content="{safe}"', old, count=1, flags=re.I)
            return source[:match.start()] + updated + source[match.end():]
        return source[:match.start()] + replacement + source[match.end():]
    head_end = re.search(r"</head\s*>", source, re.I)
    if not head_end:
        return source
    return source[:head_end.start()] + replacement + source[head_end.start():]

changed = 0
problems = []
for page in sorted(ROOT.rglob("*.html")):
    if page.name in SKIP or any(part in {".git", "dist", "node_modules"} for part in page.parts):
        continue
    source = page.read_text(encoding="utf-8")
    title_match = re.search(r"<title\b[^>]*>(.*?)</title\s*>", source, re.I | re.S)
    description = get_meta(source, "name", "description")
    if not title_match or description is None:
        problems.append(f"{page.relative_to(ROOT)}: missing title/description")
        continue
    title = " ".join(title_match.group(1).split())
    description = " ".join(description.split())
    updated = source
    updated = update_meta(updated, "property", "og:title", title)
    updated = update_meta(updated, "property", "og:description", description)
    updated = update_meta(updated, "name", "twitter:card", "summary")
    updated = update_meta(updated, "name", "twitter:title", title)
    updated = update_meta(updated, "name", "twitter:description", description)
    if updated != source:
        page.write_text(updated, encoding="utf-8")
        changed += 1
print(f"Normalized social metadata on {changed} HTML page(s).")
if problems:
    print("\n".join(problems))
    raise SystemExit(1)
