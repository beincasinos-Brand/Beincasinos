#!/usr/bin/env python3
"""Version local static CSS/JS references so CDN/browser caches refresh site-wide."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"google05b7a00eb84d7acb.html"}
VERSION = "20261031-nav1"
ASSETS = [
    ("href", "/styles.css"),
    ("src", "/script.js"),
]

def version_reference(source: str, attr: str, path: str) -> str:
    pattern = re.compile(
        r"(\b" + attr + r"\s*=\s*['\"])" + re.escape(path) + r"(?:\?[^'\"]*)?(['\"])",
        re.I,
    )
    return pattern.sub(lambda m: m.group(1) + path + "?v=" + VERSION + m.group(2), source)

changed = []
for page in sorted(ROOT.rglob("*.html")):
    if page.name in SKIP or any(part in {".git", "dist", "node_modules"} for part in page.parts):
        continue
    source = page.read_text(encoding="utf-8")
    updated = source
    for attr, path in ASSETS:
        updated = version_reference(updated, attr, path)
    if updated != source:
        page.write_text(updated, encoding="utf-8")
        changed.append(str(page.relative_to(ROOT)))

print(f"Versioned static CSS/JS references on {len(changed)} HTML page(s).")
if changed:
    print("\n".join(changed))
