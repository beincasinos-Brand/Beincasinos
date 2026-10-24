#!/usr/bin/env python3
"""Validate Cloudflare Pages security headers and the public build assumptions.

The production host is Cloudflare Pages. This check intentionally does not
validate Vercel deployment settings or claim to inspect live production headers.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
required = {
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "X-Frame-Options": "DENY",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
    "X-Permitted-Cross-Domain-Policies": "none",
    "Content-Security-Policy": "default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; form-action 'self'; script-src 'self'; style-src 'self'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self'; frame-src 'none'; upgrade-insecure-requests",
}

headers_path = ROOT / "cloudflare" / "_headers"
try:
    content = headers_path.read_text(encoding="utf-8")
except (OSError, UnicodeError) as exc:
    errors.append(f"cloudflare/_headers: cannot read Cloudflare Pages header rules ({exc})")
    content = ""

lines = [line.strip() for line in content.splitlines()]
if "/*" not in lines:
    errors.append("cloudflare/_headers: global /* rule is required")
for name, expected in required.items():
    if f"{name}: {expected}" not in lines:
        errors.append(f"cloudflare/_headers: missing or incorrect {name}")
if "Strict-Transport-Security: max-age=31536000" not in lines:
    errors.append("cloudflare/_headers: HSTS must retain max-age=31536000")
csp = next((line for line in lines if line.startswith("Content-Security-Policy:")), "")
if "object-src 'none'" not in csp or "frame-ancestors 'none'" not in csp:
    errors.append("cloudflare/_headers: CSP must block plugins and framing")

builder = ROOT / "scripts" / "build_site.py"
try:
    builder_source = builder.read_text(encoding="utf-8")
except (OSError, UnicodeError) as exc:
    errors.append(f"scripts/build_site.py: cannot read Cloudflare Pages builder ({exc})")
    builder_source = ""
if 'CLOUDFLARE_HEADERS = "cloudflare/_headers"' not in builder_source:
    errors.append("scripts/build_site.py: must copy the Cloudflare Pages _headers file")
if '"brand-directory"' not in builder_source:
    errors.append("scripts/build_site.py: brand-directory must be included in the public artifact allowlist")
if "vercel.json" not in builder_source:
    errors.append("scripts/build_site.py: Vercel config must remain excluded from the public artifact")

if errors:
    print(f"FAIL: {len(errors)} Cloudflare Pages configuration issue(s)")
    for error in errors:
        print("  ERROR: " + error)
    sys.exit(1)

print("PASS: Cloudflare Pages security-header configuration and build allowlist are valid.")
print("Note: this source-level check does not verify live deployment headers, DNS, redirects, or production behavior.")
