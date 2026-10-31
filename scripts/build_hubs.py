#!/usr/bin/env python3
"""Market hub pages: /online-casinos-<market>/ . Reads data/tier1-reviews.json. Idempotent.

  python3 scripts/build_hubs.py && python3 scripts/site_chrome.py
"""
from __future__ import annotations
import html, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_tier1 as T  # noqa: E402
import site_chrome as sc  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
e = html.escape
BASE = "https://beincasinos.online"
DATE = "2026-10-31"
DATA = json.loads((ROOT / "data/tier1-reviews.json").read_text(encoding="utf-8"))["reviews"]

HUBS = [
dict(code="GB", slug="online-casinos-uk", name="Great Britain", short="UK", reg="UK Gambling Commission (UKGC)", reg_url="https://www.gamblingcommission.gov.uk/public-register/business/index",
 title="Online Casinos in the UK: Licence Checks and Reviews", h1="Online casinos in the UK: check the licence, then read the evidence",
 desc="How to check a UK online casino: UKGC licence, exact domain, GAMSTOP, bonus terms and withdrawals. Reviews show their evidence and dates.",
 lede="Any casino serving Great Britain needs a UK Gambling Commission licence. Start with the register, then compare what each operator actually publishes.",
 steps=["Find the legal entity named in the casino's terms and conditions.", "Search that company on the UKGC public register and match the licence number shown in the site footer.", "Check that the exact domain you are on is listed against the operator.", "Confirm GAMSTOP is offered and that deposit limits and reality checks are available.", "Read the bonus terms: wagering base, maximum bet, expiry and cashout cap."],
 protect="Licensed operators must offer GAMSTOP, deposit limits, time-outs and reality checks, verify your age and identity, and handle complaints through an approved dispute service such as IBAS.",
 guides=[("/guides/how-to-find-a-legit-online-casino-uk/", "How to find a legit online casino in the UK"), ("/guides/gamstop-self-exclusion-explained/", "GAMSTOP explained"), ("/guides/fastest-withdrawal-casinos-how-to-check/", "Fastest withdrawal casinos: how to check"), ("/guides/paypal-casinos-withdrawals-what-to-check/", "PayPal casinos: what to check"), ("/guides/ibas-casino-complaints-uk/", "IBAS complaints")],
 faq=[("Are online casinos legal in the UK?", "Yes, when the operator holds a UK Gambling Commission licence for remote casino and the exact domain is listed on its record."), ("How do I know a UK casino is safe?", "Match the company, licence number and domain to the UKGC register, and check that GAMSTOP and deposit limits are available."), ("Can I withdraw quickly?", "Speed depends on the operator's pending period, verification and payment method. Read the withdrawal terms.")]),
dict(code="NL", slug="online-casinos-netherlands", name="the Netherlands", short="Netherlands", reg="Kansspelautoriteit (KSA)", reg_url="https://kansspelautoriteit.nl/",
 title="Online Casinos in the Netherlands: KSA Licence Guide", h1="Online casinos in the Netherlands: only with a KSA licence",
 desc="Dutch online casinos need a Kansspelautoriteit licence. Check the register, Cruks exclusion and bonus terms before you play. Reviews show their evidence.",
 lede="Since 1 October 2021 online casino games are legal in the Netherlands only for operators licensed by the Kansspelautoriteit.",
 steps=["Find the company in the casino's terms and conditions.", "Search for it on the KSA register of licence holders.", "Check that the exact domain is listed.", "Confirm the operator connects to Cruks, the exclusion register.", "Read bonus, withdrawal and complaint terms."],
 protect="Licensed operators must offer limits, connect to Cruks, verify age and identity and follow Dutch rules on advertising and bonuses.",
 guides=[("/guides/online-casinos-netherlands-legal-ksa/", "Dutch online casinos: legal and KSA"), ("/guides/cruks-self-exclusion-netherlands-explained/", "Cruks explained"), ("/nl/legale-online-casinos-nederland/", "Legale online casino's (Nederlands)"), ("/nl/", "Alle Nederlandse gidsen")],
 faq=[("Are online casinos legal in the Netherlands?", "Yes, but only with a Dutch licence from the Kansspelautoriteit."), ("What is Cruks?", "The central register for self-exclusion. Licensed operators must check it."), ("Is a Malta or Curaçao licence enough?", "No. An operator targeting the Dutch market needs a Dutch licence.")]),
dict(code="DE", slug="online-casinos-germany", name="Germany", short="Germany", reg="Gemeinsame Glücksspielbehörde der Länder (GGL)", reg_url="https://www.gluecksspiel-behoerde.de/",
 title="Online Casinos in Germany: GGL Licence and Whitelist", h1="Online casinos in Germany: GGL licence, whitelist and OASIS",
 desc="Online slots in Germany need a GGL licence. Check the whitelist, the monthly deposit limit and OASIS exclusion. Reviews show their evidence.",
 lede="Since the 2021 Interstate Treaty on Gambling, virtual slots and online poker in Germany may be offered only with a German licence.",
 steps=["Find the company in the casino's terms.", "Search for it in the GGL whitelist of authorised providers.", "Check the domain and that the product (for example virtual slots) is covered.", "Confirm connection to OASIS and the LUGAS deposit-limit system.", "Read bonus and withdrawal terms."],
 protect="Licensed providers apply a cross-provider monthly deposit limit, a per-spin stake limit and a minimum spin duration on virtual slots, and query the OASIS exclusion system.",
 guides=[("/guides/legal-online-casinos-germany-ggl/", "Legal online casinos in Germany"), ("/de/legale-online-casinos-deutschland/", "Legale Online-Casinos (Deutsch)"), ("/de/oasis-sperrsystem-erklaert/", "OASIS erklärt"), ("/de/", "Alle deutschen Ratgeber")],
 faq=[("Are online casinos legal in Germany?", "Online slots and certain products are legal only with a German licence. Check the GGL whitelist."), ("What is OASIS?", "The central self-exclusion system licensed providers must query."), ("Does a Malta licence work in Germany?", "Not for the products that require a German licence.")]),
dict(code="CH", slug="online-casinos-switzerland", name="Switzerland", short="Switzerland", reg="ESBK / Federal Gaming Board", reg_url="https://www.esbk.admin.ch/",
 title="Online Casinos in Switzerland: ESBK Licence Guide", h1="Online casinos in Switzerland: only licensed Swiss casinos",
 desc="Swiss online casinos need a concession and ESBK supervision. Check the official list and bonus terms before you play. Reviews show their evidence.",
 lede="Only casinos with a Swiss concession may offer online games to players in Switzerland. The ESBK blocks access to unlicensed foreign sites.",
 steps=["Check the casino on the ESBK's list of authorised providers.", "Confirm you are on the licensed operator's own domain.", "Check the player protection tools: limits and self-exclusion.", "Read bonus and withdrawal terms.", "Avoid sites that are blocked or not listed."],
 protect="Licensed Swiss casinos must provide social-protection measures, including limits and exclusion, and are supervised by the ESBK.",
 guides=[("/guides/swiss-online-casinos-legal-esbk/", "Swiss online casinos: legal and ESBK"), ("/guides/how-to-check-a-casino-licence/", "How to check a casino licence")],
 faq=[("Are online casinos legal in Switzerland?", "Yes, when run by a licensed Swiss land-based casino with an online concession. Check the ESBK list."), ("Are foreign casinos blocked?", "Access to unlicensed foreign offers is blocked by Swiss authorities."), ("How do I check a Swiss casino?", "Use the official ESBK list and the operator's own domain.")]),
dict(code="US-MI", slug="online-casinos-michigan", name="Michigan", short="Michigan", reg="Michigan Gaming Control Board (MGCB)", reg_url="https://www.michigan.gov/mgcb",
 title="Online Casinos in Michigan: MGCB Licence Guide", h1="Online casinos in Michigan: licensed by the MGCB",
 desc="Michigan online casinos are licensed by the Michigan Gaming Control Board. Check the list, age 21+ and geolocation rules before you play.",
 lede="In Michigan online casino gaming is regulated by the Michigan Gaming Control Board. Players must be 21 or older and physically in the state.",
 steps=["Check the operator on the MGCB's official list.", "Confirm you are on the operator's own site or app.", "Expect age and location verification.", "Read bonus and withdrawal terms for Michigan.", "Use the responsible gaming tools."],
 protect="Licensed operators must verify age and location and provide responsible gaming tools, including self-exclusion and limits.",
 guides=[("/guides/michigan-online-casinos-legal-mgcb/", "Michigan online casinos: legal and MGCB"), ("/guides/how-to-check-a-casino-licence/", "How to check a casino licence")],
 faq=[("Are online casinos legal in Michigan?", "Yes, with an MGCB licence. Players must be 21 or older and in Michigan."), ("How do I check the operator?", "Match it to the MGCB's official list."), ("Do offers differ by state?", "Yes. Read the terms for Michigan on the operator's own page.")]),
]


def logo(slug: str, dark: bool = False) -> str:
    for ext in ("svg", "png", "webp"):
        if (ROOT / f"assets/brands/{slug}.{ext}").exists():
            return f'<img class="hub-logo{" hub-dark" if dark else ""}" src="/assets/brands/{slug}.{ext}" alt="" width="64" height="40" loading="lazy">'
    return ""


def rows(code: str) -> str:
    items = [(slug, r) for slug, r in DATA.items() if r["market"] == code]
    items.sort(key=lambda x: T.progress_key(x[1]))
    out = []
    for slug, r in items:
        s = T.score(r)
        status = (f'<b class="hub-score">{s}/100</b> {e(T.band(s))}' if s is not None
                  else f'Evidence in progress: {T.elig_pass(r)}/5 checks passed, {T.crit_rated(r)}/6 criteria rated')
        out.append(f'<a class="hub-row" href="/reviews/{slug}/">{logo(slug, bool(r.get("logo_dark")))}<span class="hub-name"><b>{e(r["brand"])}</b><small>{e(status)}</small></span><span aria-hidden="true">→</span></a>'
                   .replace(f"<small>{e(status)}</small>", f"<small>{status if s is not None else e(status)}</small>"))
    return "".join(out) or "<p>Reviews for this market are being prepared.</p>"


def page(h: dict) -> str:
    url = f"{BASE}/{h['slug']}/"
    t = f"{h['title']} | BeInCasinos"
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in h["faq"]]}
    ld = f'<script type="application/ld+json">{json.dumps(faq, ensure_ascii=False, separators=(",", ":"))}</script>'
    n = sum(1 for r in DATA.values() if r["market"] == h["code"])
    steps = "".join(f"<li>{e(s)}</li>" for s in h["steps"])
    guides = "".join(f'<li><a href="{u}">{e(l)}</a></li>' for u, l in h["guides"])
    faqh = "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in h["faq"])
    head = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="description" content="{e(h["desc"])}"><title>{e(t)}</title><link rel="icon" href="/favicon.svg" type="image/svg+xml">'
            f'<link rel="canonical" href="{url}"><meta property="og:type" content="website"><meta property="og:title" content="{e(t)}">'
            f'<meta property="og:description" content="{e(h["desc"])}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary">'
            f'<meta name="twitter:title" content="{e(t)}"><meta name="twitter:description" content="{e(h["desc"])}"><meta name="color-scheme" content="light dark">{ld}{sc.HEAD_LINKS}</head>')
    return (head + f'<body><a class="skip-link" href="#main">Skip to content</a>{sc.header(h["slug"] + "/")}<main id="main">'
            f'<section class="page-hero"><div class="wrap"><p class="eyebrow">Market guide · {e(h["short"])}</p><h1>{e(h["h1"])}</h1><p>{e(h["lede"])}</p></div></section>'
            f'<div class="wrap content-layout"><article class="prose"><h2>How to check an operator in {e(h["name"])}</h2><p>The regulator is the {e(h["reg"])}. Always use its own register, not a badge on a website.</p><ol>{steps}</ol>'
            f'<p><a href="{e(h["reg_url"])}" rel="noopener noreferrer">Open the {e(h["short"])} regulator site ↗</a></p>'
            f'<h2>Reviews for {e(h["name"])} ({n})</h2><p>Each review lists five eligibility checks and six rated criteria. A total score appears only when every check passes and every criterion has dated evidence. Others show exactly what is still open.</p><div class="hub-list">{rows(h["code"])}</div>'
            f'<h2>What licensed operators must provide</h2><p>{e(h["protect"])}</p>'
            f'<h2>Guides for this market</h2><ul>{guides}</ul><h2>Frequently asked questions</h2>{faqh}'
            f'<p class="site-note">Educational information, not advice. Gambling is for adults (18+, 21+ in some US states) and can be addictive. <a href="/responsible-gambling/">Find support</a>. See our <a href="/affiliate-disclosure/">affiliate disclosure</a> and <a href="/how-we-review/">how we score</a>. Last reviewed {DATE}.</p></article>'
            f'<aside class="sidebar"><b>Other markets</b>' + "".join(f'<a href="/{x["slug"]}/">{e(x["name"])}</a>' for x in HUBS if x is not h) + '<a href="/markets/">All regulators</a><a href="/reviews/">All reviews</a><a href="/tools/">Free tools</a></aside></div></main>'
            f'{sc.FOOTER}<script src="/script.js?v={sc.VERSION}" defer></script></body></html>')


MARK = ("<!-- hubs:start -->", "<!-- hubs:end -->")
TOP_GUIDES = [("/guides/how-to-find-a-legit-online-casino-uk/", "Find a legit UK casino"), ("/guides/what-wagering-requirements-mean/", "What wagering means"), ("/guides/fastest-withdrawal-casinos-how-to-check/", "Fastest withdrawals"),
              ("/guides/how-to-check-slot-rtp/", "Check slot RTP"), ("/guides/can-a-casino-confiscate-winnings/", "Can a casino keep winnings?"), ("/guides/how-to-write-a-casino-complaint/", "Write a complaint")]


def home_links() -> None:
    import re
    f = ROOT / "index.html"; t = f.read_text(encoding="utf-8")
    t = re.sub(re.escape(MARK[0]) + r".*?" + re.escape(MARK[1]), "", t, flags=re.S)
    mk = "".join(f'<a class="tool-card" href="/{h["slug"]}/"><h3>{e(h["name"])}</h3><p>{e(h["reg"])}</p></a>' for h in HUBS)
    gd = "".join(f'<a class="tool-card" href="{u}"><h3>{e(l)}</h3></a>' for u, l in TOP_GUIDES)
    tl = "".join(f'<a class="tool-card" href="{u}"><h3>{e(l)}</h3></a>' for u, l in [("/tools/wagering-calculator/", "Wagering calculator"), ("/tools/bonus-value-calculator/", "Bonus value calculator"), ("/tools/house-edge-calculator/", "Expected loss calculator"), ("/tools/roulette-odds-calculator/", "Roulette odds calculator")])
    block = (MARK[0] + f'<section class="section"><div class="wrap"><h2>Online casinos by market</h2><div class="tool-grid">{mk}</div></div></section>'
             f'<section class="section"><div class="wrap"><h2>Popular guides</h2><div class="tool-grid">{gd}</div><p><a href="/guides/">All 60 guides →</a></p></div></section>'
             f'<section class="section"><div class="wrap"><h2>Free tools</h2><div class="tool-grid">{tl}</div></div></section>' + MARK[1])
    t = t.replace("</main>", block + "</main>", 1)
    f.write_text(t, encoding="utf-8")


def main() -> None:
    sm = ROOT / "sitemap.xml"; s = sm.read_text(encoding="utf-8")
    for h in HUBS:
        d = ROOT / h["slug"]; d.mkdir(exist_ok=True)
        (d / "index.html").write_text(page(h), encoding="utf-8")
        u = f"{BASE}/{h['slug']}/"
        if f"<loc>{u}</loc>" not in s:
            s = s.replace("</urlset>", f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{DATE}</lastmod></url>\n</urlset>")
    sm.write_text(s, encoding="utf-8")
    home_links()
    print(len(HUBS), "market hubs")


if __name__ == "__main__":
    main()
