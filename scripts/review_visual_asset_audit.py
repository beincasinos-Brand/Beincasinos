#!/usr/bin/env python3
"""Read-only QA for review-page brand artwork and repeated images.

This deliberately does not invent logos, scores, ratings, or bonus values.
It reports missing brand-specific image assets and generic assets repeated
across review pages so editors can replace them with verified operator assets.
"""
from __future__ import annotations

import argparse
import collections
import html
import json
import re
from pathlib import Path


IMG_RE = re.compile(r"<img\\b([^>]*?)>", re.IGNORECASE | re.DOTALL)
ATTR_RE = re.compile(r"""([a-zA-Z_:][-a-zA-Z0-9_:.]*)\\s*=\\s*(?:"([^"]*)"|'([^']*)'|([^\\s>]+))""")
BRAND_MARKERS = ("logo", "brand", "operator")
GENERIC_MARKERS = ("review-card-art", "casino-placeholder", "placeholder", "generic-casino")


def attrs_for(tag: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for match in ATTR_RE.finditer(tag):
        key = match.group(1).lower()
        out[key] = html.unescape(next((v for v in match.groups()[1:] if v is not None), ""))
    return out


def inspect_page(path: Path, root: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    images = []
    for match in IMG_RE.finditer(text):
        attrs = attrs_for(match.group(1))
        src = attrs.get("src", "").strip()
        alt = attrs.get("alt", "").strip()
        if not src:
            continue
        lower = src.lower()
        is_site_brand = any(marker in lower for marker in ("beincasinos", "favicon", "site-logo"))
        if is_site_brand:
            continue
        images.append({
            "src": src,
            "alt": alt,
            "brand_specific_name": any(marker in lower for marker in BRAND_MARKERS),
            "generic_name": any(marker in lower for marker in GENERIC_MARKERS),
        })
    has_brand_logo = any(item["brand_specific_name"] and not item["generic_name"] for item in images)
    return {
        "page": path.relative_to(root).as_posix(),
        "images": images,
        "has_brand_specific_logo_asset": has_brand_logo,
        "missing_alt": [item["src"] for item in images if not item["alt"]],
        "generic_images": [item["src"] for item in images if item["generic_name"]],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--json", type=Path, help="Optional JSON report output")
    parser.add_argument("--csv", type=Path, help="Optional CSV report output")
    args = parser.parse_args()
    root = args.root.resolve()
    pages = sorted((root / "reviews").glob("*/index.html"))
    results = [inspect_page(path, root) for path in pages]
    counts = collections.Counter(
        image["src"] for page in results for image in page["images"]
    )
    repeated = {src: count for src, count in counts.items() if count > 1}
    summary = {
        "review_pages_scanned": len(results),
        "pages_with_brand_specific_logo_asset": sum(p["has_brand_specific_logo_asset"] for p in results),
        "pages_missing_brand_specific_logo_asset": [p["page"] for p in results if not p["has_brand_specific_logo_asset"]],
        "repeated_image_sources": dict(sorted(repeated.items(), key=lambda pair: (-pair[1], pair[0]))),
        "pages_with_missing_alt": {p["page"]: p["missing_alt"] for p in results if p["missing_alt"]},
        "pages_using_generic_art": {p["page"]: p["generic_images"] for p in results if p["generic_images"]},
        "warning": "A brand-specific filename is only a QA signal; a human must verify source, brand match, and usage permission.",
    }
    print(json.dumps(summary, indent=2))
    if args.json:
        args.json.write_text(json.dumps({"summary": summary, "pages": results}, indent=2) + "\\n", encoding="utf-8")
    if args.csv:
        import csv
        with args.csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=[
                "page", "has_brand_specific_logo_asset", "image_count",
                "missing_alt_count", "generic_image_count", "image_sources",
            ])
            writer.writeheader()
            for page in results:
                writer.writerow({
                    "page": page["page"],
                    "has_brand_specific_logo_asset": page["has_brand_specific_logo_asset"],
                    "image_count": len(page["images"]),
                    "missing_alt_count": len(page["missing_alt"]),
                    "generic_image_count": len(page["generic_images"]),
                    "image_sources": " | ".join(item["src"] for item in page["images"]),
                })
    return 1 if summary["pages_missing_brand_specific_logo_asset"] or repeated else 0


if __name__ == "__main__":
    raise SystemExit(main())
