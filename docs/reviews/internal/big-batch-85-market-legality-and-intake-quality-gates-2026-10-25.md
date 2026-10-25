# Big Batch 85 — Market legality and candidate-intake quality gates

Date: 2026-10-25  
Branch: `ops/2026-10-24-target-reconciliation-and-release-gates`

## Outcome

This batch adds an editorial/SEO intake gate for the 12 declared target markets. It does not add casino candidates where the market's legal framework does not permit the relevant product, and it does not promote queue candidates to verified or publishable status.

## Market-specific gates

| Target market | Required gate before adding a casino review |
|---|---|
| Australia (AU) | Do not publish or promote offshore interactive online casino offers as lawful. ACMA explains that online casino-style gambling services are prohibited under the Interactive Gambling Act, and advertising prohibited services is also restricted. Only consider genuinely lawful, non-casino products after specific legal review. |
| Canada (CA) | Evidence must be province-specific. The current queue's Ontario entries are Ontario-only; they do not establish nationwide Canadian eligibility. Verify current iGaming Ontario operator/site listing and Ontario presence rules before any Ontario-facing review. |
| Great Britain (GB) | Match the exact domain to the UK Gambling Commission public register, identify the licensed entity and relevant remote casino permission, then check current terms and product availability. A brand name alone is insufficient. |
| United States (US) | Treat each state as a separate market. Require an exact domain and operator match in the relevant state regulator's current list and a casino-specific authorization. Do not extrapolate one state's approval nationwide. |
| Switzerland (CH) | Confirm exact online domain and operator against the ESBK/authorized Swiss online casino register; keep any unmatched domain on hold. |
| Germany (DE) | Confirm the exact domain, operator and permitted product against the current GGL whitelist. A generic company or brand entry is not enough. |
| Netherlands (NL) | Confirm exact domain and licence in the current Kansspelautoriteit register; check the licensed offering and current restrictions before describing it as authorized. |
| Sweden (SE) | Exact-domain Spelinspektionen evidence is recorded for ten queue candidates, but each still requires live-site/operator, terms and consumer-review checks. |
| Spain (ES) | DGOJ operator pages can show general and singular licences, but casino-specific scope must be confirmed. In this batch, AdmiralBet and Betway have captured domain/product evidence; Betfred's captured page lists general licences and records prior singular licence extinctions, so do not assume current casino permission. 888's captured page supports a candidate lead only; reconcile the exact live domain before scoring. |
| Italy (IT) | The three current entries are ADM search-result leads only. Open and capture the current official concession/domain record and confirm casino-specific scope before using a stronger verification label. |
| France (FR) | Do not build an online-casino review/listing target. The ANJ says online casinos are not authorized in France; the authorized online categories are limited to specified lotteries, sports betting, horse-race betting and poker. Any future FR work must be limited to a separately verified lawful category, not casino gambling. |
| Belgium (BE) | The ten queue entries are leads captured from the A+ register. Re-open the live register, match the exact domain and contracting entity, and confirm current validity before review or publication. |

## Queue state at this batch

The intake CSV has 47 candidate rows: CA-ON 20, SE 10, BE 10, ES 4 and IT 3. All 47 remain `HOLD`; all 47 remain `NOT SCORED`. This is an intake queue, not the production ledger and not 47 completed reviews.

Queue file: `docs/targets/ca-on-se-candidate-intake-queue-2026-10-25.csv`.

## Critical SEO/editorial rules

1. Never call a brand “verified” based solely on an affiliate application, affiliate network, brand marketing page, or search-result snippet.
2. Preserve evidence date, exact URL, operator/legal entity, product scope, and any limitations.
3. Do not fabricate bonus values, wagering requirements, withdrawal speeds, payout rates, ratings, review scores, player tests, complaints history, or image permissions.
4. Use licensed/official brand assets only when rights and usage terms are established; otherwise create original neutral artwork.
5. Keep France casino and Australia prohibited interactive-casino offers out of the eligible casino-review inventory unless qualified legal review documents a lawful basis.
6. Do not publish geo pages for unsupported target markets merely to fill a quota. Market fit and legality outrank reaching 100 rows quickly.
7. A register match is one evidence checkpoint; publication additionally requires a current live-site review, terms capture, consumer-protection checks, score methodology, editorial QA and legal review where needed.

## Official references

- Australia ACMA, interactive gambling: https://www.acma.gov.au/interactivegambling
- Ontario iGaming Ontario operator directory: https://igamingontario.ca/en/operator/operators
- UK Gambling Commission public register: https://www.gamblingcommission.gov.uk/public-register/businesses
- Switzerland ESBK online gambling: https://www.esbk.admin.ch/en/online-gambling/
- Germany GGL whitelist: https://www.gluecksspiel-behoerde.de/de/fuer-spielende/uebersicht-erlaubter-anbieter-whitelist
- Netherlands Ksa licence register: https://kansspelautoriteit.nl/register-licensees
- Sweden Spelinspektionen licence register: https://www.spelinspektionen.se/licens-o-tillstand/licensregister/
- Spain DGOJ operators: https://www.ordenacionjuego.es/en/operadores-juego/operadores
- Italy ADM remote gaming concessionaires: https://www.adm.gov.it/portale/monopoli/giochi/gioco_distanza/gioco_dist_concessionari
- France ANJ permitted online games FAQ: https://www.anj.fr/foire-aux-questions/offre-de-jeu-legale-et-illegale/quels-sont-les-jeux-dargent-et-paris-sportifs
- Belgium Belgian Gaming Commission A+ register: https://data.gamingcommission.be/licenses/APLUS/latest/table.html?lang=en

## Not done in this batch

No production-ledger status or score changed. No bonus was asserted as current. No live cashier/payment test was claimed. No tests, Actions workflows, merge or deployment were run.
