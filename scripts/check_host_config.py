#!/usr/bin/env python3
"""Validate that both prepared static-host configs retain aligned security headers."""
import json
import re
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
    "Content-Security-Policy": "default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; form-action 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self'; frame-src 'none'; upgrade-insecure-requests",
}

try:
    vercel = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
    vercel_headers = {}
    for rule in vercel.get("headers", []):
        for item in rule.get("headers", []):
            vercel_headers[item.get("key", "")] = item.get("value", "")
except (OSError, UnicodeError, json.JSONDecodeError) as exc:
    errors.append(f"vercel.json: cannot parse host config ({exc})")
    vercel_headers = {}

try:
    netlify_text = (ROOT / "netlify.toml").read_text(encoding="utf-8")
    netlify_headers = {
        key: value for key, value in re.findall(r'^\s*([A-Za-z0-9-]+)\s*=\s*"([^"]*)"\s*, netlify_text, re.MULTILINE)
    }
except (OSError, UnicodeError) as exc:
    errors.append(f"netlify.toml: cannot read host config ({exc})")
    netlify_headers = {}

for name, expected in required.items():
    if vercel_headers.get(name) != expected:
        errors.append(f"vercel.json: missing or incorrect {name}")
    if netlify_headers.get(name) != expected:
        errors.append(f"netlify.toml: missing or incorrect {name}")

for name, headers in (("vercel.json", vercel_headers), ("netlify.toml", netlify_headers)):
    hsts = headers.get("Strict-Transport-Security", "")
    if "max-age=31536000" not in hsts:
        errors.append(f"{name}: HSTS must retain max-age=31536000")
    csp = headers.get("Content-Security-Policy", "")
    if "object-src 'none'" not in csp or "frame-ancestors 'none'" not in csp:
        errors.append(f"{name}: CSP must block plugins and framing")

if errors:
    print(f"FAIL: {len(errors)} host security configuration issue(s)")
    for error in errors:
        print("  ERROR: " + error)
    sys.exit(1)

print("PASS: Netlify and Vercel security headers are present and aligned.")
print("Note: configuration checks do not verify headers on a deployed host.")
, netlify_text, re.MULTILINE)
    }
except (OSError, UnicodeError) as exc:
    errors.append(f"netlify.toml: cannot read host config ({exc})")
    netlify_headers = {}

for name, expected in required.items():
    if vercel_headers.get(name) != expected:
        errors.append(f"vercel.json: missing or incorrect {name}")
    if netlify_headers.get(name) != expected:
        errors.append(f"netlify.toml: missing or incorrect {name}")

for name, headers in (("vercel.json", vercel_headers), ("netlify.toml", netlify_headers)):
    hsts = headers.get("Strict-Transport-Security", "")
    if "max-age=31536000" not in hsts:
        errors.append(f"{name}: HSTS must retain max-age=31536000")
    csp = headers.get("Content-Security-Policy", "")
    if "object-src 'none'" not in csp or "frame-ancestors 'none'" not in csp:
        errors.append(f"{name}: CSP must block plugins and framing")

if errors:
    print(f"FAIL: {len(errors)} host security configuration issue(s)")
    for error in errors:
        print("  ERROR: " + error)
    sys.exit(1)

print("PASS: Netlify and Vercel security headers are present and aligned.")
print("Note: configuration checks do not verify headers on a deployed host.")
