#!/usr/bin/env python3
"""Save readable text snapshots of the official source pages listed in research/sources.json.

Meant for GitHub Actions (open internet). Output: research/snapshots/<slug>/NN-<host>.txt, each starting with
SOURCE / FETCHED / STATUS lines, so reviewers can quote and cite them. Usage: snapshot_sources.py [slug ...]
"""
from __future__ import annotations
import json, re, sys, time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
MAX_CHARS = 60_000


class Text(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "template"}
    BLOCK = {"p", "div", "li", "br", "h1", "h2", "h3", "h4", "tr", "section", "article", "table", "ul", "ol"}

    def __init__(self) -> None:
        super().__init__(); self.out: list[str] = []; self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP: self.skip += 1
        if tag in self.BLOCK: self.out.append("\n")
        if tag == "a" and not self.skip:
            href = dict(attrs).get("href")
            if href and href.startswith(("http", "/")): self.out.append(f"[{href}] ")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip: self.skip -= 1
        if tag in self.BLOCK: self.out.append("\n")

    def handle_data(self, data):
        if not self.skip: self.out.append(data)


def fetch(url: str) -> tuple[str, str]:
    req = Request(url, headers={"User-Agent": UA, "Accept-Language": "en-GB,en;q=0.8,nl;q=0.6,de;q=0.5", "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.5,*/*;q=0.4"})
    with urlopen(req, timeout=30) as res:
        body = res.read(3_000_000)
        ctype = res.headers.get("content-type", "")
        status = f"{res.status} {ctype.split(';')[0]} final={res.geturl()}"
    if "pdf" in status:
        return status, "[PDF not converted; open the source URL]"
    t = Text(); t.feed(body.decode("utf-8", "replace"))
    text = re.sub(r"[ \t]+", " ", "".join(t.out))
    text = re.sub(r"\n\s*\n+", "\n", text).strip()
    return status, text[:MAX_CHARS]


def main() -> None:
    sources = json.loads((ROOT / "research" / "sources.json").read_text())
    only = set(sys.argv[1:])
    for slug, urls in sources.items():
        if only and slug not in only: continue
        d = ROOT / "research" / "snapshots" / slug; d.mkdir(parents=True, exist_ok=True)
        for i, url in enumerate(urls, 1):
            host = re.sub(r"[^a-z0-9]+", "-", (urlparse(url).netloc + urlparse(url).path).lower()).strip("-")[:60]
            f = d / f"{i:02d}-{host}.txt"
            stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
            try:
                status, text = fetch(url)
            except Exception as exc:  # noqa: BLE001
                status, text = f"ERROR {exc}", ""
            f.write_text(f"SOURCE: {url}\nFETCHED: {stamp}\nSTATUS: {status}\n\n{text}\n", encoding="utf-8")
            print(f"{slug} {i:02d} {status[:60]} {len(text)} chars")
            time.sleep(1)


if __name__ == "__main__":
    main()
