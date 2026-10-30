#!/usr/bin/env python3
"""Original cover images (assets/guides/<slug>.jpg) and inline diagrams for the guide pages.
Everything is drawn from scratch; nothing is taken from operators or third parties.
Requires Playwright + Chromium for the covers. Idempotent via marker comments."""
from __future__ import annotations
import html, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "guides"
OUT = ROOT / "assets" / "guides"
e = html.escape
COVER = ("<!-- guide-cover:start -->", "<!-- guide-cover:end -->")
DIAG = ("<!-- guide-diagram:start -->", "<!-- guide-diagram:end -->")
SOCIAL = ("<!-- guide-social:start -->", "<!-- guide-social:end -->")

MOTIFS = {
    "doc": '<rect x="62" y="30" width="116" height="156" rx="10"/><path d="M84 70h72M84 98h72M84 126h44"/><circle cx="160" cy="170" r="30" fill="#0e1726"/><path d="M146 170l10 10 18-22"/>',
    "calc": '<rect x="54" y="26" width="132" height="176" rx="14"/><rect x="76" y="48" width="88" height="34" rx="5"/><path d="M82 112h14M114 112h14M146 112h14M82 142h14M114 142h14M146 142h14M82 172h14M114 172h14M146 172h14"/>',
    "clock": '<circle cx="120" cy="116" r="84"/><path d="M120 62v54l36 22"/><path d="M120 20v14M120 198v14M24 116h14M202 116h14"/>',
    "scales": '<path d="M120 36v156M80 192h80M44 76h152"/><path d="M44 76l-26 62h52zM196 76l-26 62h52z"/><path d="M18 138a26 18 0 0 0 52 0M170 138a26 18 0 0 0 52 0"/>',
    "dice": '<rect x="46" y="46" width="148" height="148" rx="22"/><circle cx="86" cy="86" r="9"/><circle cx="154" cy="86" r="9"/><circle cx="120" cy="120" r="9"/><circle cx="86" cy="154" r="9"/><circle cx="154" cy="154" r="9"/>',
    "shield": '<path d="M120 24l84 30v58c0 52-36 84-84 104-48-20-84-52-84-104V54z"/><path d="M84 116l26 26 48-54"/>',
    "lens": '<circle cx="106" cy="106" r="66"/><path d="M154 154l52 52"/><path d="M78 108h56M78 128h36"/>',
}
RULES = [
    (("licence", "operator", "regulatory", "regulator"), "doc"), (("wager", "bonus", "cashout", "maximum-bet", "expiry", "terms"), "calc"),
    (("withdraw", "payment", "processing", "delayed"), "clock"), (("complain", "dispute", "complaint"), "scales"),
    (("rtp", "house", "probab", "random", "volatility", "return"), "dice"), (("self-exclusion", "safer"), "shield"),
]


def motif_for(slug: str) -> str:
    for keys, m in RULES:
        if any(k in slug for k in keys):
            return m
    return "lens"


def cover_page(slug: str, eyebrow: str, title: str) -> str:
    fonts = (ROOT / "assets" / "fonts").as_uri()
    return f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:G;src:url({fonts}/schibsted-grotesk-latin-wght-normal.woff2);font-weight:400 900}}
*{{box-sizing:border-box;margin:0}}body{{width:1200px;height:630px;background:#0e1726;color:#f1f3f6;font-family:G,sans-serif;position:relative;overflow:hidden}}
.bg{{position:absolute;inset:0;background:radial-gradient(800px 480px at 90% 10%,#203353,transparent 70%),repeating-linear-gradient(0deg,transparent 0 79px,#ffffff08 79px 80px)}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:14px;background:#b0802a}}
.wrap{{position:absolute;inset:60px 70px 56px 84px;display:flex;justify-content:space-between;align-items:center;gap:30px}}
.t{{flex:1}}.k{{font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:#e0b657;font-weight:700;margin-bottom:22px}}
h1{{font-size:{76 if len(title) < 34 else 62}px;line-height:1.05;font-weight:800;letter-spacing:-.02em}}
.b{{position:absolute;left:84px;bottom:52px;font-size:24px;color:#9fb0c9}}.b b{{color:#e0b657}}
svg{{width:340px;height:340px;flex:none}}svg *{{stroke:#e0b657;stroke-width:6;fill:none;stroke-linecap:round;stroke-linejoin:round}}svg [fill="#0e1726"]{{fill:#0e1726}}
</style><div class="bg"></div><div class="bar"></div><div class="wrap"><div class="t"><p class="k">{e(eyebrow)}</p><h1>{e(title)}</h1></div>
<svg viewBox="0 0 240 240">{MOTIFS[motif_for(slug)]}</svg></div><p class="b"><b>BeInCasinos</b> · Learning library · Educational, not advice</p>'''


# ---------------------------------------------------------------- diagrams
def flow_svg(label: str, steps: list[tuple[str, str]], caption: str) -> str:
    n = len(steps)
    w = 720
    bw = (w - 24 * (n - 1) - 24) // n
    parts = []
    for i, (big, small) in enumerate(steps):
        x = 12 + i * (bw + 24)
        parts.append(f'<rect class="dg-box" x="{x}" y="14" width="{bw}" height="104" rx="12"/><text class="dg-big" x="{x + bw / 2:.0f}" y="62" text-anchor="middle">{e(big)}</text>'
                     f'<text class="dg-small" x="{x + bw / 2:.0f}" y="92" text-anchor="middle">{e(small)}</text>')
        if i < n - 1:
            ax = x + bw + 4
            parts.append(f'<path class="dg-arrow" d="M{ax} 66h16m-6-6l6 6-6 6"/>')
    svg = f'<svg class="dg" viewBox="0 0 {w} 132" role="img" aria-labelledby="dgt"><title id="dgt">{e(label)}</title>{"".join(parts)}</svg>'
    return f'<figure class="dg-fig">{svg}<figcaption>{e(caption)}</figcaption></figure>'


def bars_svg(label: str, rows: list[tuple[str, float, str]], caption: str) -> str:
    out = []
    for i, (name, pct, note) in enumerate(rows):
        y = 16 + i * 52
        out.append(f'<text class="dg-small" x="12" y="{y + 14}">{e(name)}</text><rect class="dg-track" x="190" y="{y}" width="440" height="24" rx="6"/>'
                   f'<rect class="dg-fill" x="190" y="{y}" width="{440 * pct / 100:.0f}" height="24" rx="6"/><text class="dg-note" x="{190 + 440 * pct / 100 + 10:.0f}" y="{y + 17}">{e(note)}</text>')
    h = 16 + len(rows) * 52
    return (f'<figure class="dg-fig"><svg class="dg" viewBox="0 0 720 {h}" role="img" aria-labelledby="dgt"><title id="dgt">{e(label)}</title>{"".join(out)}</svg>'
            f'<figcaption>{e(caption)}</figcaption></figure>')


def lines_svg(label: str, caption: str) -> str:
    calm = "M12 70 L80 64 L150 74 L220 60 L290 72 L360 58 L430 66 L500 52 L570 60 L640 46 L708 54"
    wild = "M12 70 L80 20 L150 112 L220 34 L290 118 L360 26 L430 102 L500 14 L570 96 L640 30 L708 60"
    svg = (f'<svg class="dg" viewBox="0 0 720 132" role="img" aria-labelledby="dgt"><title id="dgt">{e(label)}</title>'
           f'<path class="dg-line wild" d="{wild}"/><path class="dg-line calm" d="{calm}"/>'
           '<text class="dg-small" x="14" y="128">Low volatility: small, frequent swings</text><text class="dg-small" x="420" y="128">High volatility: large, uneven swings</text></svg>')
    return f'<figure class="dg-fig">{svg}<figcaption>{e(caption)}</figcaption></figure>'


DIAGRAMS = {
    "what-wagering-requirements-mean": flow_svg("Wagering example", [("20", "bonus (example)"), ("× 30", "wagering multiple"), ("= 600", "eligible wagering")], "Hypothetical example only. Always use the base your actual terms name: bonus only, or deposit plus bonus."),
    "bonus-terms-explained": flow_svg("Wagering example", [("20", "bonus (example)"), ("× 30", "wagering multiple"), ("= 600", "eligible wagering")], "Hypothetical example only. Check whether the multiple applies to the bonus, the deposit or both."),
    "how-to-check-a-casino-licence": flow_svg("Five-step licence check", [("1", "Exact domain"), ("2", "Legal entity"), ("3", "Regulator register"), ("4", "Product and market"), ("5", "Terms and payouts")], "The order used in every BeInCasinos eligibility check. A failed step stops the review from being scored."),
    "what-a-gambling-licence-means": flow_svg("Five-step licence check", [("1", "Exact domain"), ("2", "Legal entity"), ("3", "Regulator register"), ("4", "Product and market"), ("5", "Terms and payouts")], "A licence covers a named entity, product and territory. Check each step before trusting a claim."),
    "brand-name-vs-legal-operator": flow_svg("Brand to operator", [("Brand", "what you see"), ("Domain", "where you play"), ("Entity", "who contracts"), ("Register", "who is licensed")], "Match the brand to the legal entity named in the terms, then to the regulator's record."),
    "withdrawal-processing-times": flow_svg("Withdrawal timeline", [("Request", "you submit"), ("Checks", "operator review"), ("Dispatch", "payment sent"), ("Settlement", "bank or wallet")], "Each stage has its own clock. Published times usually cover only some of them."),
    "casino-withdrawal-verification-explained": flow_svg("Withdrawal timeline", [("Request", "you submit"), ("Verification", "ID and source"), ("Dispatch", "payment sent"), ("Settlement", "bank or wallet")], "Verification can sit before dispatch. Providing documents early removes avoidable delay."),
    "how-to-complain-about-a-casino": flow_svg("Complaint ladder", [("1", "Operator"), ("2", "Escalation"), ("3", "ADR body"), ("4", "Regulator")], "Use the operator's formal route first, keep dated evidence, then the independent body your market names."),
    "alternative-dispute-resolution-gambling": flow_svg("Complaint ladder", [("1", "Operator"), ("2", "Escalation"), ("3", "ADR body"), ("4", "Regulator")], "ADR bodies differ by market. Check which one your operator's licence requires it to offer."),
    "house-edge-explained": bars_svg("House edge example", [("Staked", 100, "100"), ("Expected return", 97, "97"), ("House edge", 3, "3")], "Illustration of a game with a 3% house edge: over a very long run about 3 of every 100 staked is kept. It predicts nothing about one session."),
    "return-to-player-rtp-explained": bars_svg("RTP example", [("Staked", 100, "100"), ("RTP 96%", 96, "96")], "A 96% RTP is a long-run theoretical average across huge numbers of plays, not what you should expect today."),
    "rtp-vs-volatility": lines_svg("Volatility illustration", "Schematic, not data: two games can share the same RTP and still feel very different."),
}


def put(text: str, markers: tuple[str, str], block: str | None, anchor: str, after: bool) -> str:
    s, en = markers
    text = re.sub(re.escape(s) + r".*?" + re.escape(en) + r"\n?", "", text, flags=re.S)
    if block is None:
        return text
    i = text.find(anchor)
    if i < 0:
        return text
    i += len(anchor) if after else 0
    return text[:i] + f"{s}\n{block}\n{en}\n" + text[i:]


def main() -> None:
    from playwright.sync_api import sync_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = ROOT / ".guide-tmp.html"
    pages = sorted(p for p in GUIDES.glob("*/index.html"))
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 1200, "height": 630})
        for f in pages:
            slug = f.parent.name
            t = f.read_text(encoding="utf-8")
            h1 = re.search(r"<h1>(.*?)</h1>", t, re.S)
            eyebrow = re.search(r'<p class="eyebrow">(.*?)</p>', t, re.S)
            if not h1:
                continue
            title = html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip()
            eb = html.unescape(re.sub(r"<[^>]+>", "", eyebrow.group(1))).split("·")[0].strip() if eyebrow else "Guide"
            tmp.write_text(cover_page(slug, eb, title), encoding="utf-8")
            pg.goto(tmp.as_uri()); pg.wait_for_timeout(120)
            pg.screenshot(path=str(OUT / f"{slug}.jpg"), type="jpeg", quality=84)
            fig = (f'<div class="wrap"><figure class="bx-cover is-guide"><img src="/assets/guides/{slug}.jpg" width="1200" height="630" loading="lazy" decoding="async" '
                   f'alt="Illustration for the guide: {e(title)}"></figure></div>')
            t = put(t, COVER, fig, "</section>", True) if False else t
            # cover goes right after the hero section, i.e. before the content layout
            t = put(t, COVER, fig, '<div class="wrap content-layout">', False)
            diag = DIAGRAMS.get(slug)
            t = re.sub(re.escape(DIAG[0]) + r".*?" + re.escape(DIAG[1]) + r"\n?", "", t, flags=re.S)
            if diag:
                m = re.search(r'<article class="prose">.*?(<h2)', t, re.S)
                if m:
                    j = m.start(1)
                    t = t[:j] + f"{DIAG[0]}\n{diag}\n{DIAG[1]}\n" + t[j:]
            u = f"https://beincasinos.online/assets/guides/{slug}.jpg"
            meta = (f'<meta property="og:image" content="{u}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
                    f'<meta name="twitter:image" content="{u}">')
            t = re.sub(r'<meta name="twitter:card" content="summary(?:_large_image)?">', '<meta name="twitter:card" content="summary_large_image">', t)
            t = put(t, SOCIAL, meta, "</head>", False)
            f.write_text(t, encoding="utf-8")
        br.close()
    tmp.unlink(missing_ok=True)
    print(f"{len(pages)} guide pages updated")


if __name__ == "__main__":
    main()
