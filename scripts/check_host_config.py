#!/usr/bin/env python3
"""Validate Vercel's static build/output settings and production security headers."""
import json
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

try:
    config = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
except (OSError, UnicodeError, json.JSONDecodeError) as exc:
    errors.append(f"vercel.json: cannot parse config ({exc})")
    config = {}

if config.get("buildCommand") != "python3 scripts/build_site.py":
    errors.append("vercel.json: buildCommand must run the allowlist site builder")
if config.get("outputDirectory") != "dist":
    errors.append("vercel.json: outputDirectory must be dist")
if config.get("cleanUrls") is not True:
    errors.append("vercel.json: cleanUrls must remain enabled")
if config.get("trailingSlash") is not True:
    errors.append("vercel.json: trailingSlash must remain enabled")

headers = {}
for rule in config.get("headers", []):
    for item in rule.get("headers", []):
        headers[item.get("key", "")] = item.get("value", "")

for name, expected in required.items():
    if headers.get(name) != expected:
        errors.append(f"vercel.json: missing or incorrect {name}")

hsts = headers.get("Strict-Transport-Security", "")
if "max-age=31536000" not in hsts:
    errors.append("vercel.json: HSTS must retain max-age=31536000")
csp = headers.get("Content-Security-Policy", "")
if "object-src 'none'" not in csp or "frame-ancestors 'none'" not in csp:
    errors.append("vercel.json: CSP must block plugins and framing")

redirects = config.get("redirects", [])
www_redirect = any(
    item.get("source") == "/:path*"
    and item.get("destination") == "https://beincasinos.online/:path*"
    and item.get("permanent") is True
    and any(
        condition.get("type") == "host"
        and condition.get("value") == "www.beincasinos.online"
        for condition in item.get("has", [])
    )
    for item in redirects
)
if not www_redirect:
    errors.append("vercel.json: add a permanent www.beincasinos.online to apex redirect")

# Cloudflare Pages uses a plain-text _headers file copied into dist/.
cf_path = ROOT / "cloudflare" / "_headers"
try:
    cf_headers = cf_path.read_text(encoding="utf-8")
except (OSError, UnicodeError) as exc:
    errors.append(f"cloudflare/_headers: cannot read header rules ({exc})")
    cf_headers = ""

for name, expected in required.items():
    if not any(line.strip() == f"{name}: {expected}" for line in cf_headers.splitlines()):
        errors.append(f"cloudflare/_headers: missing or incorrect {name}")
if not any(line.strip() == "Strict-Transport-Security: max-age=31536000" for line in cf_headers.splitlines()):
    errors.append("cloudflare/_headers: HSTS must retain max-age=31536000")
if not any(line.strip() == "/*" for line in cf_headers.splitlines()):
    errors.append("cloudflare/_headers: global path rule is required")

if errors:
    print(f"FAIL: {len(errors)} Vercel configuration issue(s)")
    for error in errors:
        print("  ERROR: " + error)
    sys.exit(1)

print("PASS: Vercel fallback config and Cloudflare Pages security-header configuration are valid.")
print("Note: configuration checks do not verify deployed HTTP responses or domain routing.")
