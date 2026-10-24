#!/usr/bin/env python3
"""Validate Cloudflare Pages security headers used by the public-only build."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
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
    lines = headers_path.read_text(encoding="utf-8").splitlines()
except (OSError, UnicodeError) as exc:
    errors.append(f"cloudflare/_headers: cannot read header rules ({exc})")
    lines = []

normalized = [line.strip() for line in lines]
if "/*" not in normalized:
    errors.append("cloudflare/_headers: global /* path rule is required")
for name, expected in required.items():
    if f"{name}: {expected}" not in normalized:
        errors.append(f"cloudflare/_headers: missing or incorrect {name}")
if "Strict-Transport-Security: max-age=31536000" not in normalized:
    errors.append("cloudflare/_headers: HSTS must retain max-age=31536000")

# Confirm the public-only builder will copy the exact file Cloudflare Pages reads.
builder = ROOT / "scripts" / "build_site.py"
try:
    builder_text = builder.read_text(encoding="utf-8")
except (OSError, UnicodeError) as exc:
    errors.append(f"scripts/build_site.py: cannot read builder ({exc})")
    builder_text = ""
if 'CLOUDFLARE_HEADERS = "cloudflare/_headers"' not in builder_text:
    errors.append("scripts/build_site.py: expected Cloudflare header source path is not configured")
if 'shutil.copy2(headers_src, DIST / "_headers")' not in builder_text:
    errors.append("scripts/build_site.py: Cloudflare _headers file is not copied into the build root")

if errors:
    print(f"FAIL: {len(errors)} Cloudflare Pages configuration issue(s)")
    for error in errors:
        print("  ERROR: " + error)
    sys.exit(1)

print("PASS: Cloudflare Pages security-header source and public-build copy rules are valid.")
print("NOTE: this checks repository configuration only; it does not verify deployed response headers, DNS, redirects, or production deployment.")
