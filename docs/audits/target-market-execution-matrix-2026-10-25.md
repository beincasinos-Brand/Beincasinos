# Target-market execution matrix — 25 October 2026

Branch: `ops/2026-10-24-target-reconciliation-and-release-gates`
Status: internal research plan; not legal advice and not publication approval.

## Non-negotiable rules

- A brand is eligible for a market only when the relevant regulator's current primary register, domain/trading-name record, contracting entity, and consumer terms agree for that exact market.
- Do not infer nationwide US access from a state licence; do not infer Canada-wide access from a provincial authorisation.
- Record the source URL, checked-at UTC timestamp, reviewer, terms version/effective date, product scope, age rule, excluded locations, bonus terms, withdrawal/complaint routes, safer-gambling resources, and image-use permission.
- Keep all 100 records HOLD / NOT SCORED until source checks and independent editorial review are complete. No fabricated scores, bonus amounts, ratings, testing claims, or implied endorsement.
- A regulator register can establish licence/domain facts; it does not automatically prove a current offer, product quality, fair withdrawals, or consumer experience.

## Twelve-market execution matrix

| Target | Required primary-source checks before any brand is assigned | Important scope guardrail | Queue |
|---|---|---|---|
| AU | [ACMA online gambling rules](https://www.acma.gov.au/interactivegambling), [licensed-provider register](https://www.acma.gov.au/check-if-gambling-operator-legal), state/territory regulator where relevant; operator terms and exact domain | Do not describe an offshore interactive casino as locally licensed merely because it accepts Australian visitors. Separate legal context from brand eligibility. | Research legality and exclusions first; no consumer-facing casino recommendation without a documented legal basis. |
| CA | Provincial regulator and official registry, including [iGaming Ontario's regulated-site directory](https://igamingontario.ca/en/operator/operators) where applicable; provincial terms/domain | Province-specific only. Do not convert CA-ON/CA-BC/CA-QC leads into blanket Canadian eligibility. | Reconcile each province-coded lead; no national Canada label without province-by-province evidence. |
| GB | [UK Gambling Commission business register](https://www.gamblingcommission.gov.uk/public-register/businesses), active remote casino permissions, domain and trading names; current UK-facing terms | A licence number alone is insufficient; match the live domain and contracting entity. | Highest-volume research queue; re-check register and current terms before drafting. |
| US | State regulator's official casino/iGaming licence and authorised-domain list for each state; examples: [New Jersey regulator](https://www.nj.gov/casinos/) and [Pennsylvania Gaming Control Board](https://gamingcontrolboard.pa.gov/licensing/licensing_applications_and_other_forms/slot-machine) | State-specific only. NJ/PA/MI are not equivalent to US-wide access; exclude unlicensed states from any claim. | Keep separate state-market records; prohibit generic “licensed in the US” copy. |
| CH | [Swiss Federal Gaming Board's online-gambling guidance and lists](https://www.esbk.admin.ch/en/unauthorised-online-games) and intercantonal Gespa lists; exact domain | Swiss online casino access is restricted to authorised operators; foreign licence evidence is not a substitute. | Verify each exact .ch-authorised operator/domain and current list status. |
| DE | [GGL official whitelist](https://www.gluecksspiel-behoerde.de/de/fuer-spielende/uebersicht-erlaubter-anbieter-whitelist) and operator/domain entry; current German terms | Whitelist and permitted product type must match; do not treat a general foreign licence as German authorisation. | Reconcile each brand against the current whitelist and product scope. |
| NL | [Ksa register of licensees](https://kansspelautoriteit.nl/register-licensees) and enforcement notices; exact Dutch domain, terms and local offer | Market access, minimum age, offer rules and enforcement history must be checked against current Dutch primary sources. | Recheck current register and offer terms; record adverse notices neutrally and with dates. |
| SE | [Spelinspektionen licence register](https://www2.spelinspektionen.se/licens-o-tillstand/licensregister/) and licence scope; Swedish terms and responsible-gambling information | Exact Swedish licence/domain and product permissions required; foreign licence does not prove Swedish eligibility. | Confirm licence type, domain, bonus restrictions and local consumer-support routes. |
| ES | [DGOJ licensed-operator and domain search](https://www.ordenacionjuego.es/en/operadores-juego/operadores-licencia/operadores) and current resolutions; Spanish terms | Verify operator and product-specific permissions, not just brand recognition. | Confirm exact legal entity, domain and product scope before market assignment. |
| IT | [ADM authorised remote-gaming concessionaires](https://www.adm.gov.it/portale/en/monopoli/giochi/gioco_distanza/gioco_dist_concessionari?codconc=desc) and notices; Italian terms | Verify active concession and the precise domain; do not rely on brand-name similarity or affiliate pages. | Reconcile high-volume Italy leads in batches; validate concession and domain independently. |
| FR | [ANJ approved operators](https://www.anj.fr/offre-de-jeu-et-marche/operateurs-agrees) and public guidance on authorised online gambling categories | Online casino games such as slots are not generally authorised in France; do not label offshore casino brands as France-licensed. | Treat France as a legal-context/exclusion review first; only list products legally authorised for the market. |
| BE | Belgian Gaming Commission (Kansspelcommissie) official [online licence data](https://data.gamingcommission.be/licenses/A/latest/table.html?lang=en) and linked-domain records, plus current local terms | Verify the appropriate licence class and exact approved domain; a foreign licence is insufficient. | Check current licence and domain association before assigning a brand to BE. |

## Source-level coverage snapshot

Existing research trackers are uneven and use mixed granularity:
- `docs/brand-research-template.csv`: 208 non-empty rows; market-coded leads include GB 24, US-NJ 30, US-MI 14, DE 13, CA-ON 13, CH 10, BE 10, NL 8, SE 7, ES 19, IT 46, US-PA 2, FR 2, CA-BC 1, CA-QC 2, DE-SH 2, DK 1; plus excluded/unconfirmed rows.
- `docs/tier-1-master-prospect-tracker.csv`: 114 non-empty rows; GB 70, NL 18, US-NJ 7, US-PA 4, CH 3, US-MI 2, and single/low-count leads for several others.
- The current directory's market labels remain concentrated in GB and NL. The presence of a lead in a tracker is not proof of eligibility or verification.

## Publication gate for every brand × market pair

1. Official regulator record captured and dated.
2. Exact domain/trading name matched to the active licence and legal entity.
3. Current local terms, product permissions, age rule, deposit/withdrawal and complaints routes captured.
4. Bonus terms independently checked; if unclear or inconsistent, publish “not cleared” rather than an amount.
5. Safer-gambling tools and local help route checked.
6. Image source and reuse rights cleared, or use a non-infringing text/monogram treatment.
7. Editorial evidence reviewed by a second reviewer; affiliate/commercial disclosure checked.
8. Market-specific claims and internal links checked; no unsupported nationwide or cross-border implication.
9. Record status stays HOLD until all applicable gates are satisfied; then a separate editorial approval is required.

## Immediate order of work

1. Fix the source-level geo labels and the production-vs-branch robots/sitemap/directory mismatch before requesting launch approval.
2. Work one regulator-first batch per market, prioritising GB/NL/CH/DE/SE/ES/IT/BE; treat AU/CA/US/FR as jurisdiction-sensitive queues requiring especially explicit scope notes.
3. Do not fill gaps by inventing bonuses, images, ratings, testing, or eligibility.
4. Re-run automated checks and live production smoke tests after an approved deployment only. This document does not authorise merge, indexing, or deployment.
