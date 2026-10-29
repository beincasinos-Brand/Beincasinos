#!/usr/bin/env python3
"""Download each Tier 1 operator's own logo into assets/brands/<slug>.<ext>.

Run from an environment with open internet (GitHub Actions: .github/workflows/fetch-logos.yml).
Order per review: 1) logo_url from the data file, 2) the operator homepage: JSON-LD logo, <img> whose
src/alt/class mentions "logo", og:image, apple-touch-icon, icon. Logos are the operators' trademarks,
used only to identify the brand being reviewed. Failed brands keep the monogram; see the printed report.
"""
from __future__ import annotations
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "tier1-reviews.json"
OUT = ROOT / "assets" / "brands"
UA = "Mozilla/5.0 (compatible; BeInCasinosLogoFetch/1.0; +https://beincasinos.online/about/)"
TYPES = {"image/svg+xml": "svg", "image/png": "png", "image/webp": "webp", "image/x-icon": None, "image/vnd.microsoft.icon": None}
MAX = 400_000


def get(url: str, binary: bool = False, timeout: int = 20):
    req = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urlopen(req, timeout=timeout) as res:
        ctype = (res.headers.get("content-type") or "").split(";")[0].strip().lower()
        body = res.read(MAX + 1)
        return ctype, body if binary else body.decode("utf-8", "replace")


class Scan(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.found: list[tuple[int, str]] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img":
            src = a.get("src") or a.get("data-src") or ""
            hay = " ".join([src, a.get("alt", ""), a.get("class", ""), a.get("id", "")]).lower()
            if src and "logo" in hay and not src.startswith("data:"):
                self.found.append((0 if src.lower().split("?")[0].endswith(".svg") else 1, src))
        elif tag == "meta" and a.get("property") in ("og:image", "og:image:url") and a.get("content"):
            self.found.append((3, a["content"]))
        elif tag == "link" and a.get("href"):
            rel = (a.get("rel") or "").lower()
            if "apple-touch-icon" in rel:
                self.found.append((4, a["href"]))
            elif "icon" in rel and a["href"].lower().split("?")[0].endswith(".svg"):
                self.found.append((2, a["href"]))


def candidates(r: dict) -> list[str]:
    urls = [r["logo_url"]] if r.get("logo_url") else []
    sites = [x for x in [r.get("site")] + list(r.get("site_alt", [])) if x]
    for site in sites:
        home = f"https://{site}/"
        try:
            _, html = get(home)
            scan = Scan(); scan.feed(html)
            for m in re.findall(r'"logo"\s*:\s*"([^"]+)"', html):
                scan.found.append((0, m))
            urls += [urljoin(home, u) for _, u in sorted(scan.found, key=lambda t: t[0])]
        except Exception as exc:  # noqa: BLE001
            print(f"   homepage failed ({site}): {exc}")
        for path in ("logo.svg", "images/logo.svg", "assets/logo.svg", "favicon.svg", "apple-touch-icon.png", "apple-touch-icon-180x180.png"):
            urls.append(f"https://{site}/{path}")
    for site in sites:
        host = site.removeprefix("www.")
        # Last resorts: icon services return the operator's own site icon as PNG.
        urls += [f"https://www.google.com/s2/favicons?domain={host}&sz=256"]
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u); out.append(u)
    return out[:30]


def too_small(body: bytes, ext: str) -> bool:
    if ext == "svg":
        return False
    try:
        import io
        from PIL import Image
        w, h = Image.open(io.BytesIO(body)).size
        return max(w, h) < 64
    except Exception:  # noqa: BLE001
        return False


def clean_svg(body: bytes) -> bytes | None:
    t = body.decode("utf-8", "replace")
    if "<svg" not in t or re.search(r"<script|onload=|onerror=|<foreignObject|javascript:", t, re.I):
        return None
    return t.encode()


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    data = json.loads(DATA.read_text(encoding="utf-8"))
    ok = fail = 0
    for slug, r in data["reviews"].items():
        if any((OUT / f"{slug}.{x}").is_file() for x in TYPES.values()):
            print(f"= {slug}: already present"); ok += 1; continue
        done = False
        for url in candidates(r):
            try:
                ctype, body = get(url, binary=True)
                ext = TYPES.get(ctype) or ("svg" if url.lower().split("?")[0].endswith(".svg") else None)
                if ext is None or len(body) > MAX or len(body) < 200:
                    continue
                if too_small(body, ext):
                    continue
                if ext == "svg":
                    body = clean_svg(body)
                    if body is None:
                        continue
                (OUT / f"{slug}.{ext}").write_bytes(body)
                print(f"+ {slug}: {url} -> {slug}.{ext}"); done = True; break
            except Exception:  # noqa: BLE001
                continue
        if done: ok += 1
        else: fail += 1; print(f"! {slug}: no logo found (monogram stays)")
    print(f"logos: {ok} ok, {fail} missing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
