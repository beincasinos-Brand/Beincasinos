#!/usr/bin/env python3
"""Check that the deployment artifact contains public assets only."""
from pathlib import Path
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET
import sys
import re

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
errors = []

if not DIST.is_dir():
    errors.append("dist/ is missing; run scripts/build_site.py first")
else:
    forbidden = ("docs", "scripts", ".github", "README.md", "vercel.json")
    for rel in forbidden:
        if (DIST / rel).exists():
            errors.append(f"dist/: internal/configuration path must not be published: {rel}")

    required = ("index.html", "404.html", "robots.txt", "sitemap.xml", "_headers", "styles.css", "script.js", "favicon.svg", "site.webmanifest", "tools/wagering-calculator/calculator.js", "tools/wagering-calculator/calculator.css", "tools/terms-checklist/checklist.js", "tools/terms-checklist/checklist.css")
    for rel in required:
        if not (DIST / rel).is_file():
            errors.append(f"dist/: required public asset missing: {rel}")
    if not (DIST / "assets" / "beincasinos-mark.svg").is_file():
        errors.append("dist/: dedicated circular BIC logo asset is missing")
    if not (DIST / "reviews" / "index.html").is_file():
        errors.append("dist/: public Reviews hub is missing")
    if not (DIST / "partners" / "index.html").is_file():
        errors.append("dist/: public operator partnerships page is missing")

    # Verify the Cloudflare Pages header file survives the allowlist build.
    source_headers = ROOT / "cloudflare" / "_headers"
    output_headers = DIST / "_headers"
    if source_headers.is_file() and output_headers.is_file():
        if source_headers.read_text(encoding="utf-8") != output_headers.read_text(encoding="utf-8"):
            errors.append("dist/_headers: Cloudflare security headers differ from source configuration")
    else:
        errors.append("dist/_headers: required Cloudflare Pages security headers missing")

    sitemap = DIST / "sitemap.xml"
    if sitemap.is_file():
        try:
            root = ET.fromstring(sitemap.read_text(encoding="utf-8"))
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            urls = [((item.text or "").strip()) for item in root.findall(".//sm:loc", ns)]
            if len(set(urls)) != len(urls):
                errors.append("dist/sitemap.xml: duplicate canonical URL entries found")

            # Keep the sitemap synchronized with the actual public HTML pages.
            # The 404 page is intentionally excluded from indexable routes.
            expected_urls = set()
            for html_file in DIST.rglob("*.html"):
                rel = html_file.relative_to(DIST).as_posix()
                if re.search(r'<meta name="robots" content="[^"]*\bnoindex\b', html_file.read_text(encoding="utf-8", errors="ignore")[:6000], re.I):
                    continue  # deliberately noindex (Tier 1 focus): must stay out of the sitemap
                if rel in {"404.html", "google05b7a00eb84d7acb.html"}:
                    # Google Search Console verification is a required public asset,
                    # but it is not an indexable content page and must stay out of the sitemap.
                    continue
                if rel == "index.html":
                    route = "/"
                elif rel.endswith("/index.html"):
                    route = "/" + rel[:-len("index.html")]
                else:
                    route = "/" + rel
                expected_urls.add("https://beincasinos.online" + route)
            if len(urls) != len(expected_urls):
                errors.append(f"dist/sitemap.xml: expected one URL per indexable HTML page ({len(expected_urls)}), found {len(urls)}")
            actual_urls = set(urls)
            for missing in sorted(expected_urls - actual_urls):
                errors.append(f"dist/sitemap.xml: public HTML route missing from sitemap: {missing}")
            for unexpected in sorted(actual_urls - expected_urls):
                errors.append(f"dist/sitemap.xml: sitemap URL has no matching indexable HTML route: {unexpected}")
            if "https://beincasinos.online/reviews/" not in urls:
                errors.append("dist/sitemap.xml: Reviews hub is missing from the canonical URL list")
            if "https://beincasinos.online/partners/" not in urls:
                errors.append("dist/sitemap.xml: operator partnerships page is missing from the canonical URL list")
            for url in urls:
                parsed = urlparse(url)
                if parsed.scheme != "https" or parsed.netloc.casefold() != "beincasinos.online":
                    errors.append(f"dist/sitemap.xml: unexpected canonical URL: {url}")
                    continue
                path = unquote(parsed.path or "/").lstrip("/")
                target = DIST / path
                if not path:
                    target = DIST / "index.html"
                elif target.is_dir():
                    target = target / "index.html"
                elif not target.suffix:
                    target = target / "index.html"
                if not target.is_file() or target.suffix.lower() not in (".html", ".htm"):
                    errors.append(f"dist/sitemap.xml: URL does not map to a public HTML file: {url}")
        except (ET.ParseError, OSError, UnicodeError) as exc:
            errors.append(f"dist/sitemap.xml: cannot validate XML ({exc})")

    robots = DIST / "robots.txt"
    if not robots.is_file():
        errors.append("dist/robots.txt: required robots policy is missing")
    else:
        robots_text = robots.read_text(encoding="utf-8")
        # A site-wide crawl block is intentional before explicit public-launch approval.
        # The release evidence register separately tracks when it is safe to remove.
        if not re.search(r"^Sitemap:\s*https://beincasinos[.]online/sitemap[.]xml\s*$", robots_text, re.I | re.M):
            errors.append("dist/robots.txt: canonical sitemap location is missing")

    # Defense in depth: the public artifact must never contain internal source,
    # research trackers, environment files, or provider configuration.
    forbidden_suffixes = {".md", ".csv", ".py", ".toml", ".yml", ".yaml", ".env"}
    for asset in DIST.rglob("*"):
        if asset.is_file() and asset.suffix.lower() in forbidden_suffixes:
            errors.append(f"dist/{asset.relative_to(DIST)}: internal/source file type must not be published")

    # Enforce compatibility with the prepared same-origin-only script/style CSP.
    # JSON-LD is inert structured data, not executable inline JavaScript.
    inline_script = re.compile(r"<script(?![^>]*\bsrc=)(?![^>]*\btype\s*=\s*['\"]application/ld\+json['\"])[^>]*>", re.IGNORECASE)
    inline_style = re.compile(r"<style\b|\sstyle\s*=", re.IGNORECASE)
    for html_file in DIST.rglob("*.html"):
        try:
            markup = html_file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"dist/{html_file.relative_to(DIST)}: cannot inspect HTML ({exc})")
            continue
        if inline_script.search(markup):
            errors.append(f"dist/{html_file.relative_to(DIST)}: inline script violates the same-origin-only CSP")
        if inline_style.search(markup):
            errors.append(f"dist/{html_file.relative_to(DIST)}: inline style violates the same-origin-only CSP")

    # Scan deployable text assets for common accidental secrets and obvious placeholders.
    # This is a lightweight guardrail, not a replacement for a dedicated secret scanner.
    suspicious_patterns = {
        "private-key header": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", re.IGNORECASE),
        "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
        "AWS access key ID": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "Stripe live/test secret": re.compile(r"\b(?:sk|rk)_(?:live|test)_[A-Za-z0-9]{16,}\b"),
        "explicit replacement placeholder": re.compile(r"\b(?:REPLACE_WITH_[A-Z0-9_]+|YOUR_API_KEY|YOUR_SECRET|TODO:|FIXME:|LOREM IPSUM)\b", re.IGNORECASE),
    }
    text_suffixes = {".html", ".css", ".js", ".json", ".txt", ".xml", ".svg", ".webmanifest", ".md"}
    for asset in DIST.rglob("*"):
        if not asset.is_file() or asset.suffix.lower() not in text_suffixes:
            continue
        try:
            source = asset.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"dist/{asset.relative_to(DIST)}: cannot inspect text asset ({exc})")
            continue
        for label, pattern in suspicious_patterns.items():
            if pattern.search(source):
                errors.append(f"dist/{asset.relative_to(DIST)}: suspicious {label} pattern found")

if errors:
    print(f"FAIL: {len(errors)} deployment artifact issue(s)")
    for item in errors:
        print(f"  ERROR: {item}")
    sys.exit(1)

print("PASS: deployment artifact contains public files only; internal docs and trackers are excluded.")
