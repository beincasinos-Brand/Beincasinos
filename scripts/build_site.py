#!/usr/bin/env python3
"""Build a public-only static artifact; never copy internal research files."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PUBLIC_FILES = (
    "index.html",
    "404.html",
    "favicon.svg",
    "robots.txt",
    "script.js",
    "site.webmanifest",
    "sitemap.xml",
    "styles.css",
)
PUBLIC_DIRS = (
    "about",
    "affiliate-disclosure",
    "contact",
    "editorial-policy",
    "guides",
    "how-we-review",
    "market-research",
    "partners",
    "privacy",
    "responsible-gambling",
    "reviews",
    "tools",
)
FORBIDDEN_PUBLIC_PATHS = (
    "README.md",
    "docs",
    "scripts",
    "vercel.json",
    ".github",
)

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir(parents=True)

for rel in PUBLIC_FILES:
    src = ROOT / rel
    if not src.is_file():
        raise SystemExit(f"Required public file is missing: {rel}")
    shutil.copy2(src, DIST / rel)

for rel in PUBLIC_DIRS:
    src = ROOT / rel
    if not src.is_dir() or not any(src.rglob("*.html")):
        raise SystemExit(f"Required public page directory is missing HTML pages: {rel}")
    shutil.copytree(src, DIST / rel)

for rel in FORBIDDEN_PUBLIC_PATHS:
    if (DIST / rel).exists():
        raise SystemExit(f"Internal or host configuration path leaked into dist/: {rel}")

html_count = len(list(DIST.rglob("*.html")))
print(f"Built public-only static artifact at dist/ ({html_count} HTML files).")
