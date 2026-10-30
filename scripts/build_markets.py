#!/usr/bin/env python3
"""Generate /markets/ as readable cards (desktop and mobile) with live review counts from data/tier1-reviews.json."""
from __future__ import annotations
import re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_tier1 as bt  # noqa: E402
import site_chrome as sc  # noqa: E402

e, ROOT = bt.e, bt.ROOT
M = [  # code, name, regulator label, url, status, summary, checks, guide
 ("GB", "Great Britain", "UK Gambling Commission register", "https://www.gamblingcommission.gov.uk/public-register/businesses", "reviews",
  "Online casinos need a Gambling Commission licence that covers remote casino.",
  ["The legal entity named in the terms matches the register.", "The record includes remote casino, not only betting.", "Your exact domain is listed against the operator."], None),
 ("NL", "Netherlands", "Kansspelautoriteit licence register", "https://kansspelautoriteit.nl/register-licensees", "reviews",
  "Online casino games need a permit from the Kansspelautoriteit (KSA).",
  ["The permit covers remote casino games.", "The operator checks Cruks, the exclusion register.", "Brand and domain match the permit holder."], None),
 ("DE", "Germany", "GGL whitelist of authorised providers", "https://www.gluecksspiel-behoerde.de/de/fuer-spielende/uebersicht-erlaubter-anbieter-whitelist/", "reviews",
  "Online slots and some other casino products are legal only with a GGL licence.",
  ["The provider and domain are on the whitelist.", "The permission covers the product you want (slots, poker and so on).", "Limits and the OASIS exclusion system apply."], None),
 ("CH", "Switzerland", "ESBK / FGB online gambling", "https://www.esbk.admin.ch/en/online-gambling", "reviews",
  "Online casino games may be offered only by casinos with the right Swiss concession.",
  ["The brand is on the ESBK list of authorised online casinos.", "The licensed casino named in the terms matches.", "Foreign sites without Swiss authorisation can be blocked."], None),
 ("US-MI", "United States (Michigan)", "Michigan Gaming Control Board", "https://www.michigan.gov/mgcb", "reviews",
  "Michigan licenses internet casino operators for adults aged 21+ located in the state.",
  ["The operator is on the MGCB's licensed list.", "You must be physically in Michigan.", "A licence in another state does not apply here."], None),
 ("AU", "Australia", "ACMA interactive gambling", "https://www.acma.gov.au/interactivegambling", "guide",
  "Online casino services for people in Australia are generally prohibited under the Interactive Gambling Act, so we do not list casinos for this market.",
  ["ACMA reports gambling-reform amendments passed Parliament on 19 August 2026, with most reforms due to start on 1 January 2027.", "Offshore casino offers are not locally authorised."], "/markets/australia/"),
 ("FR", "France", "ANJ illegal offer information", "https://anj.fr/index.php/joueurs/offre-illegale", "guide",
  "The ANJ treats online casino games as not authorised. Sports betting and poker are separate categories with their own permissions, so we do not list casinos for this market.",
  ["Authorised online categories are not casino games.", "Do not infer permission from a familiar brand name."], "/markets/france/"),
 ("CA", "Canada", "iGaming Ontario regulated market", "https://www.igamingontario.ca/en/player/regulated-igaming-market", "research",
  "Rules are set by province. Ontario has a regulated market, but that does not apply across Canada.",
  ["Identify your province first.", "Verify the exact site, operator and product with the provincial regulator."], None),
 ("IT", "Italy", "ADM licensed distance-gaming operators", "https://www.adm.gov.it/portale/monopoli/giochi/gioco_distanza/gioco_dist_concessionari", "research",
  "Online gaming is run through ADM concessions.",
  ["The domain belongs to a current concessionaire.", "The concession covers casino games."], None),
 ("ES", "Spain", "DGOJ (Ordenación del Juego)", "https://www.ordenacionjuego.es/", "research",
  "Remote casino games need a DGOJ licence for the specific game type.",
  ["The domain and legal entity match DGOJ records.", "A sports-betting licence alone is not proof of casino permission."], None),
 ("BE", "Belgium", "Belgian Gaming Commission", "https://www.gamingcommission.be/", "research",
  "Online casinos need a Gaming Commission licence of the right class.",
  ["Check the licence class and the exact domain.", "A land-based venue licence does not imply online permission."], None),
 ("SE", "Sweden", "Spelinspektionen", "https://www.spelinspektionen.se/", "research",
  "Online casinos need a Swedish Gambling Authority licence.",
  ["Check licence type, validity and the domain.", "Enforcement history is published; read it."], None),
]
STATUS = {"reviews": ("Reviewed here", "is-reviews"), "guide": ("Guide only, no casino list", "is-guide"), "research": ("Research starting point", "is-research")}


def card(m) -> str:
    code, name, reg, url, st, summ, checks, guide = m
    n = sum(1 for r in bt.T1["reviews"].values() if r["market"] == code)
    label, cls = STATUS[st]
    lis = "".join(f"<li>{e(c)}</li>" for c in checks)
    links = [f'<a class="text-link" href="{e(url)}" rel="noopener noreferrer">{e(reg)} ↗</a>']
    if st == "reviews":
        anchor = {"US-MI": "us-mi"}.get(code, code.lower())
        links.insert(0, f'<a class="button button-primary" href="/reviews/#{anchor}">See the {n} review{"s" if n != 1 else ""}</a>')
    if guide:
        links.insert(0, f'<a class="button button-outline" href="{guide}">Read the market guide</a>')
    return (f'<article class="mk-card {cls}" id="{code.lower()}"><div class="mk-head"><h3>{e(name)}</h3><span class="mk-chip">{e(label)}</span></div>'
            f'<p class="mk-sum">{e(summ)}</p><p class="mk-lbl">What to check</p><ul>{lis}</ul><div class="mk-links">{"".join(links)}</div></article>')


def main() -> None:
    page = ROOT / "markets" / "index.html"
    old = page.read_text(encoding="utf-8")
    head = old[: old.index("<body>")]
    desc = ("Which regulator covers online casinos in each country, what to check before trusting a licence claim, "
            "and where we publish reviews. Great Britain, Netherlands, Germany, Switzerland and Michigan.")
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + e(desc) + m.group(2), head, count=1)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + e(desc) + m.group(2), head, count=1)
    head = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', lambda m: m.group(1) + e(desc) + m.group(2), head, count=1)
    reviewed = "".join(card(m) for m in M if m[4] == "reviews")
    others = "".join(card(m) for m in M if m[4] != "reviews")
    body = f'''<body>
<a class="skip-link" href="#main">Skip to content</a>
{sc.header("markets/")}
<main id="main">
<section class="bx-hero"><div class="wrap"><p class="eyebrow">Markets</p><h1>Online gambling rules, country by country</h1>
<p class="bx-lede">A licence is not a passport. The same brand can be legal in one country and not in another, so every review here is written for one market and one product.</p></div></section>
<section class="section"><div class="wrap"><div class="section-heading"><h2>Markets we review</h2></div><div class="mk-grid">{reviewed}</div>
<div class="section-heading mk-gap"><h2>Other markets</h2></div><p class="muted">We do not publish casino lists for these yet. The guides explain the rules and where to check.</p><div class="mk-grid">{others}</div></div></section>
<section class="section-compact"><div class="wrap"><h2>What counts as evidence</h2><ul class="mk-evidence">
<li><b>Regulator record.</b> The official register entry: legal entity, licence number, product scope and the date we checked.</li>
<li><b>Domain.</b> The address you use must match the regulator record and the operator's legal notice. Similar names are not enough.</li>
<li><b>Product.</b> Casino games, sports betting, poker and bingo are different permissions. One does not prove another.</li>
<li><b>Consumer terms.</b> Bonus rules, deposits and withdrawals, privacy, safer-gambling tools and complaints.</li>
<li><b>Independent testing.</b> We record what was actually tested and what was not. Operator marketing is never presented as a test.</li></ul>
<p class="fineprint hm-mt">Educational information, not legal advice. Laws, licences and domains change: check the regulator's own page before you rely on a claim. See <a href="/how-we-review/">how we score</a>, our <a href="/editorial-policy/">editorial policy</a> and <a href="/affiliate-disclosure/">affiliate disclosure</a>.
Related guides: <a href="/guides/how-to-check-a-casino-licence/">how to check a casino licence</a> · <a href="/guides/brand-name-vs-legal-operator/">brand name vs legal operator</a> · <a href="/guides/how-to-read-casino-regulatory-actions/">how to read regulatory actions</a>.</p></div></section>
</main>
{sc.FOOTER}
<script src="/script.js?v={sc.VERSION}" defer></script>
</body></html>
'''
    page.write_text(head + body, encoding="utf-8")
    print("markets page generated")


if __name__ == "__main__":
    main()
