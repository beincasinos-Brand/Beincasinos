#!/usr/bin/env python3
"""Build a public-only static artifact; never copy internal research files."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
CLOUDFLARE_HEADERS = "cloudflare/_headers"

PUBLIC_FILES = (
    "index.html",
    "google05b7a00eb84d7acb.html",
    "404.html",
    "favicon.svg",
    "robots.txt",
    "ads.txt",
    "_redirects",
    "script.js",
    "site.webmanifest",
    "sitemap.xml",
    "styles.css",
)
PUBLIC_DIRS = (
    "assets",
    "about",
    "affiliate-disclosure",
    "contact",
    "editorial-policy",
    "guides",
    "bonuses",
    "nl",
    "online-casinos-uk",
    "online-casinos-netherlands",
    "online-casinos-germany",
    "online-casinos-switzerland",
    "online-casinos-michigan",
    "de",
    "how-we-review",
    "market-research",
    "markets",
    "partners",
    "privacy",
    "responsible-gambling",
    "reviews",
    "tools",
    "terms",
)
FORBIDDEN_PUBLIC_PATHS = (
    "README.md",
    "docs",
    "scripts",
    "vercel.json",
    ".github",
)
PUBLIC_SUFFIXES = {
    ".html", ".css", ".js", ".svg", ".png", ".jpg", ".jpeg", ".webp",
    ".avif", ".gif", ".ico", ".woff", ".woff2", ".ttf", ".otf", ".txt",
}

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir(parents=True)

for rel in PUBLIC_FILES:
    src = ROOT / rel
    if not src.is_file() or src.is_symlink():
        raise SystemExit(f"Required public file is missing or unsafe: {rel}")
    shutil.copy2(src, DIST / rel)

headers_src = ROOT / CLOUDFLARE_HEADERS
if not headers_src.is_file() or headers_src.is_symlink():
    raise SystemExit(f"Required Cloudflare security header file is missing or unsafe: {CLOUDFLARE_HEADERS}")
shutil.copy2(headers_src, DIST / "_headers")

for rel in PUBLIC_DIRS:
    src = ROOT / rel
    missing_pages = rel != "assets" and not any(src.rglob("*.html")) if src.is_dir() else True
    if not src.is_dir() or src.is_symlink() or missing_pages:
        raise SystemExit(f"Required public page directory is missing HTML pages or is unsafe: {rel}")
    for item in sorted(src.rglob("*")):
        relative = item.relative_to(ROOT)
        if item.is_symlink():
            raise SystemExit(f"Refusing to publish symlink from public directory: {relative}")
        if item.is_dir():
            continue
        if item.suffix.lower() not in PUBLIC_SUFFIXES:
            raise SystemExit(f"Unexpected file type in public directory; add it deliberately to PUBLIC_SUFFIXES if it is a public asset: {relative}")
        destination = DIST / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, destination)

for rel in FORBIDDEN_PUBLIC_PATHS:
    if (DIST / rel).exists():
        raise SystemExit(f"Internal or host configuration path leaked into dist/: {rel}")

html_count = len(list(DIST.rglob("*.html")))
print(f"Built public-only static artifact at dist/ ({html_count} HTML files).")
