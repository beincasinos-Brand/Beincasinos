#!/usr/bin/env python3
"""BIC / BeInCasinos brand kit: one vector mark drawn from scratch (no fonts needed), plus PNG exports.
Outputs: assets/beincasinos-mark.svg, favicon.svg, assets/beincasinos-logo.svg (mark + live-text wordmark),
assets/brand/{mark-512.png, mark-1024.png, apple-touch-icon.png, logo-light.png, logo-dark.png, social-1200x630.png}."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INK, BRASS, BRASS_HI, PAPER = "#0e1726", "#b0802a", "#e8c46c", "#f1f3f6"

def mark(size_attr: str = "") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240"{size_attr} role="img" aria-labelledby="t"><title id="t">BIC BeInCasinos</title>
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BRASS_HI}"/><stop offset="1" stop-color="{BRASS}"/></linearGradient></defs>
<rect width="240" height="240" rx="58" fill="{INK}"/>
<rect x="9" y="9" width="222" height="222" rx="50" fill="none" stroke="url(#g)" stroke-opacity=".55" stroke-width="2"/>
<g transform="translate(0 4)"><path d="M72 92 64 56l30 18 26-30 26 30 30-18-8 36z" fill="url(#g)" stroke="url(#g)" stroke-width="5" stroke-linejoin="round"/>
<rect x="72" y="99" width="96" height="6" rx="3" fill="url(#g)"/>
<g fill="none" stroke="#f1f3f6" stroke-width="11" stroke-linecap="round" stroke-linejoin="round" transform="translate(-2 4)">
<path d="M54 124v56M54 124h24a14 14 0 0 1 0 28H54m24 0a14 14 0 0 1 0 28H54"/>
<path d="M108 124v56"/>
<path d="M180 138a28 28 0 1 0 0 28"/></g></g></svg>'''

def main() -> None:
    (ROOT / "assets" / "beincasinos-mark.svg").write_text(mark(), encoding="utf-8")
    (ROOT / "favicon.svg").write_text(mark(), encoding="utf-8")
    logo = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 240" role="img" aria-labelledby="t"><title id="t">BeInCasinos</title>
<g>{mark().split("<title id=\"t\">BIC BeInCasinos</title>")[1].rsplit("</svg>",1)[0]}</g>
<text x="270" y="148" font-family="'Schibsted Grotesk',Arial,Helvetica,sans-serif" font-size="92" font-weight="400" fill="{INK}">BeIn<tspan font-weight="800">Casinos</tspan></text>
<text x="272" y="192" font-family="'Schibsted Grotesk',Arial,Helvetica,sans-serif" font-size="25" letter-spacing="5" fill="{BRASS}">CASINO REVIEWS WITH EVIDENCE</text></svg>'''
    (ROOT / "assets" / "beincasinos-logo.svg").write_text(logo, encoding="utf-8")
    from playwright.sync_api import sync_playwright
    out = ROOT / "assets" / "brand"; out.mkdir(parents=True, exist_ok=True)
    fonts = (ROOT / "assets" / "fonts").as_uri()
    css = f'@font-face{{font-family:G;src:url({fonts}/schibsted-grotesk-latin-wght-normal.woff2);font-weight:400 900}}*{{margin:0;box-sizing:border-box}}'
    def lockup(dark: bool) -> str:
        fg, bg, tag = (PAPER, INK, BRASS_HI) if dark else (INK, "transparent", BRASS)
        return (f'<style>{css}body{{background:{bg};width:1600px;height:480px;display:flex;align-items:center;gap:56px;padding:0 80px;font-family:G}}'
                f'.m{{width:320px;height:320px}}.w{{font-size:190px;line-height:1;color:{fg};font-weight:400;letter-spacing:-.02em}}.w b{{font-weight:800}}'
                f'.s{{font-size:44px;letter-spacing:.2em;color:{tag};margin-top:20px;font-weight:500}}</style>'
                f'<div class="m">{mark(" width=320 height=320")}</div><div><div class="w">BeIn<b>Casinos</b></div><div class="s">CASINO REVIEWS WITH EVIDENCE</div></div>')
    with sync_playwright() as p:
        b = p.chromium.launch()
        def shot(html: str, path: Path, w: int, h: int, transparent=False, scale=1):
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=scale)
            t = ROOT / '.brand-tmp.html'; t.write_text('<!doctype html><meta charset=utf-8>' + html, encoding='utf-8'); pg.goto(t.as_uri()); pg.wait_for_timeout(400)
            pg.screenshot(path=str(path), omit_background=transparent); pg.close()
        sq = lambda n: f'<style>*{{margin:0}}body{{width:{n}px;height:{n}px}}</style>{mark(f" width={n} height={n}")}'
        shot(sq(512), out / "mark-512.png", 512, 512, True)
        shot(sq(1024), out / "mark-1024.png", 1024, 1024, True)
        shot(f'<style>*{{margin:0}}body{{width:180px;height:180px;background:{INK}}}</style>{mark(" width=180 height=180").replace(chr(60)+"rect width=\"240\" height=\"240\" rx=\"58\"", chr(60)+"rect width=\"240\" height=\"240\" rx=\"0\"")}', out / "apple-touch-icon.png", 180, 180)
        shot(lockup(False), out / "logo-light.png", 1600, 480, True)
        shot(lockup(True), out / "logo-dark.png", 1600, 480)
        shot(f'<style>{css}body{{width:1200px;height:630px;background:{INK};display:grid;place-items:center;font-family:G;color:{PAPER}}}.c{{text-align:center}}.w{{font-size:112px;font-weight:400;margin-top:24px;letter-spacing:-.02em}}.w b{{font-weight:800}}.s{{font-size:30px;letter-spacing:.2em;color:{BRASS_HI};margin-top:14px}}</style>'
             f'<div class="c">{mark(" width=240 height=240")}<div class="w">BeIn<b>Casinos</b></div><div class="s">CASINO REVIEWS WITH EVIDENCE</div></div>', out / "social-1200x630.png", 1200, 630)
        b.close()
    (ROOT / ".brand-tmp.html").unlink(missing_ok=True)
    print("brand kit written")

if __name__ == "__main__":
    main()
