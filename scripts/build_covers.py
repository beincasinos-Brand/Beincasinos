#!/usr/bin/env python3
"""Render a 1200x630 evidence-file cover image for every Tier 1 review (og:image + on-page figure).
Requires Playwright + Chromium. Output: assets/reviews/<slug>.jpg. Derived only from data/tier1-reviews.json."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_tier1 as bt  # noqa: E402

ROOT = bt.ROOT
OUT = ROOT / "assets" / "reviews"
e = bt.e


def cover_html(slug: str, r: dict) -> str:
    s = bt.score(r)
    ep, cn = bt.elig_pass(r), bt.crit_rated(r)
    initials = "".join(w[0] for w in __import__("re").findall(r"[A-Za-z0-9]+", r["brand"])[:2]).upper()
    ticks = "".join(
        f'<li class="{"ok" if r["eligibility"][k]["status"] == "pass" else ""}"><i></i>{e(lbl)}</li>' for k, lbl in bt.ELIG)
    segs = "".join(f'<b class="{"on" if i < cn else ""}"></b>' for i in range(6))
    seal = (f'<div class="seal"><span>{s}</span><small>/100</small></div>' if s is not None
            else '<div class="seal off"><span>n/a</span><small>not scored</small></div>')
    fonts = (ROOT / "assets" / "fonts").as_uri()
    return f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:G;src:url({fonts}/schibsted-grotesk-latin-wght-normal.woff2);font-weight:400 900}}
*{{box-sizing:border-box;margin:0}}
body{{width:1200px;height:630px;background:#0e1726;color:#f1f3f6;font-family:G,sans-serif;position:relative;overflow:hidden}}
.bg{{position:absolute;inset:0;background:radial-gradient(900px 500px at 100% 0,#1c2b44,transparent 70%),repeating-linear-gradient(90deg,transparent 0 79px,#ffffff08 79px 80px)}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:14px;background:#b0802a}}
.wrap{{position:absolute;inset:56px 64px 52px 78px;display:flex;flex-direction:column;justify-content:space-between}}
.top{{display:flex;justify-content:space-between;align-items:center;font-size:24px;letter-spacing:.04em;color:#c9d2e0}}
.top b{{color:#e0b657;font-weight:700}}
.mid{{display:flex;justify-content:space-between;align-items:center;gap:40px}}
.mono{{width:96px;height:96px;border-radius:50%;background:#f1f3f6;color:#0e1726;font-weight:800;font-size:40px;display:grid;place-items:center;margin-bottom:26px}}
h1{{font-size:{84 if len(r["brand"]) < 14 else 64}px;line-height:1.02;font-weight:800;letter-spacing:-.02em}}
.sub{{font-size:28px;color:#c9d2e0;margin-top:14px}}
.seal{{width:232px;height:232px;border-radius:50%;border:12px solid #e0b657;display:grid;place-content:center;text-align:center;flex:none}}
.seal span{{font-size:78px;font-weight:800;line-height:1}}.seal small{{font-size:22px;color:#c9d2e0}}
.seal.off{{border-color:#4a5a75;border-style:dashed}}.seal.off span{{color:#9fb0c9;font-size:60px}}
.bot{{display:flex;justify-content:space-between;align-items:flex-end;gap:30px}}
ul{{list-style:none;padding:0;display:flex;gap:20px;font-size:19px;white-space:nowrap;color:#9fb0c9}}
li{{display:flex;align-items:center;gap:9px}}li i{{flex:none;width:18px;height:18px;border-radius:50%;border:2px solid #4a5a75}}
li.ok{{color:#f1f3f6}}li.ok i{{background:#1fa38a;border-color:#1fa38a}}
.crit{{text-align:right;font-size:20px;color:#9fb0c9}}.crit div{{display:flex;gap:6px;margin-top:8px;justify-content:flex-end}}
.crit b{{width:40px;height:10px;border-radius:5px;background:#2a3850}}.crit b.on{{background:#1fa38a}}
</style><div class="bg"></div><div class="bar"></div><div class="wrap">
<div class="top"><span><b>BeInCasinos</b> · Evidence file</span><span>Checked {e(bt.fmt_date(r["checked"]))}</span></div>
<div class="mid"><div><div class="mono">{e(initials)}</div><h1>{e(r["brand"])}</h1>
<p class="sub">{e(r["market_label"])} · {e(bt.M_REG.get(r["market"], ""))}</p></div>{seal}</div>
<div class="bot"><ul>{ticks}</ul><div class="crit">Criteria rated {cn} of 6<div>{segs}</div></div></div></div>'''


def main() -> None:
    from playwright.sync_api import sync_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = ROOT / ".cover-tmp.html"
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        for slug, r in bt.T1["reviews"].items():
            tmp.write_text(cover_html(slug, r), encoding="utf-8")
            pg.goto(tmp.as_uri())
            pg.wait_for_timeout(150)
            pg.screenshot(path=str(OUT / f"{slug}.jpg"), type="jpeg", quality=84)
        b.close()
    tmp.unlink(missing_ok=True)
    print(f"{len(bt.T1['reviews'])} covers written to assets/reviews/")


if __name__ == "__main__":
    main()
