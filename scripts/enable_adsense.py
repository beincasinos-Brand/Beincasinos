#!/usr/bin/env python3
"""Step 1 of AdSense: add the verification meta tag to every page and create ads.txt.

  python3 scripts/enable_adsense.py ca-pub-1234567890123456

Needs only the publisher ID from the AdSense dashboard. No ad script is loaded (no CSP change needed).
"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if len(sys.argv) != 2 or not re.fullmatch(r"ca-pub-\d{10,20}", sys.argv[1]):
    sys.exit("usage: enable_adsense.py ca-pub-<digits>")
pub = sys.argv[1]
tag = f'<meta name="google-adsense-account" content="{pub}">'
n = 0
for p in ROOT.rglob("*.html"):
    if any(x in {"dist", ".git", "node_modules", "research"} for x in p.parts) or p.name.startswith("google"):
        continue
    t = p.read_text(encoding="utf-8")
    if "</head>" not in t:
        continue
    new = re.sub(r'<meta name="google-adsense-account"[^>]*>', "", t).replace("</head>", tag + "</head>", 1)
    if new != t:
        p.write_text(new, encoding="utf-8"); n += 1
(ROOT / "ads.txt").write_text(f"google.com, pub-{pub.split('pub-')[1]}, DIRECT, f08c47fec0942fa0\n", encoding="utf-8")
print(f"tag on {n} pages; ads.txt written")
