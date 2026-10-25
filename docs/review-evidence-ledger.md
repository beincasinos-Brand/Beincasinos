# BeInCasinos review evidence ledger

**Purpose:** Internal quality-control tracker for market-specific casino reviews. This file is intentionally outside the public build; do not copy it into `dist/`.

**Rule:** No overall numeric score or star rating until eligibility checks pass and all six weighted criteria have dated primary-source evidence. Do not convert missing evidence into a zero or guess. A regulator-register match is not proof of permission for every product, nor proof of payment reliability or a current bonus.

## Editorial scoring model

- Terms clarity and fairness — 25 points
- Payments and withdrawal transparency — 20 points
- Safer-gambling controls — 20 points
- Complaints and customer support — 15 points
- Operator and licence transparency — 10 points
- Usability and accessibility — 10 points

**Eligibility gate (pass/fail before scoring):** exact consumer domain, legal entity, regulator register, product permission, market eligibility, current terms and withdrawal rules. Any unresolved gate means “Not scored — verification incomplete.”

**Required evidence per profile:** source URL and source type; access/check date; exact entity/domain/product/market match; notes or captured facts; criterion-level finding and rationale; unresolved claims; next review date. Bonus data needs official offer terms, eligibility, wagering calculation, expiry, maximum stake/cashout and restrictions. Never imply a deposit, withdrawal, support interaction, or hands-on test that was not performed.

## Official research references

- Google Search Central, helpful people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search Central, reviews system: https://developers.google.com/search/docs/appearance/reviews-system
- Google Search Central, write high-quality reviews: https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews
- Spain, DGOJ operator finder: https://www.ordenacionjuego.es/en/operadores-juego/operadores
- Australia, ACMA licensed interactive gambling providers register: https://www.acma.gov.au/check-if-gambling-operator-legal

Google's review guidance emphasizes original research and useful analysis rather than thin summaries. These sources are quality guidance; they do not prove any individual casino's current status.

## Market gates

| Target market | Minimum primary-source verification | Current disposition |
|---|---|---|
| Australia (AU) | Check the exact service on ACMA's licensed interactive wagering register and assess product-specific legal restrictions before publication. | **Hold** until product/service category and legal eligibility are reviewed; do not imply online casino slots are authorised because a wagering brand is licensed. |
| Canada (CA) | Province-specific regulator, exact operator/domain and permitted product. Ontario and other provincial regimes must not be conflated. | **Unscored** until province and product are matched. |
| Great Britain (GB) | UK Gambling Commission public register, exact legal entity/domain and product permissions. | **Unscored** until current register and terms captured. |
| United States (US) | State regulator and state/product-specific permissions; a state licence cannot be generalized nationally. | **State-specific only**; no US-wide claim. |
| Switzerland (CH) | Federal Gaming Board (ESBK/Comlot as applicable) authorised online casino list and exact domain/operator. | **Unscored** until current list and product scope captured. |
| Germany (DE) | GGL official whitelist, exact domain/legal entity and permitted game category. | **Unscored**; virtual slots permission does not establish other casino products. |
| Netherlands (NL) | Kansspelautoriteit licence register, exact domain/entity and product scope. | **Unscored** until current register and terms captured. |
| Sweden (SE) | Spelinspektionen licence register, exact operator/domain/product. | **Unscored** until current register and terms captured. |
| Spain (ES) | DGOJ operator finder plus current general/singular licences for exact domain and game type. | **Register-level leads only**; product permissions and commercial terms need separate checks. |
| Italy (IT) | ADM official concessionaire/domain/product verification. | **Unscored** until current official evidence captured. |
| France (FR) | ANJ official information and product legality check. Do not assume online casino games are authorised; French online gambling permissions are product-specific. | **Hold** until product category/legal gate is cleared. |
| Belgium (BE) | Belgian Gaming Commission official licence list and permitted website/product category. | **Unscored** until exact current licence and domain match captured. |

## Initial audit findings (25 October 2026)

- The current directory contains 100 research profiles, but the current live page and source HTML show **no numeric scores or star ratings**. Each card displays “NOT RATED”, “Editorial score: Pending verification”, and “Current bonus: Not verified”. This is more honest than invented numbers but does not satisfy the intended final review-card experience.
- The current review directory's market distribution is highly uneven: Spain 67; Switzerland 9; Netherlands 8; Germany 7; Great Britain 4; Belgium 1; Sweden 1; Italy 1; Canada (British Columbia) 1; United States (Michigan) 1. Australia and France have no profiles. This needs to be corrected before claiming balanced coverage across all 12 target markets.
- Profile copy is mostly desk research, not hands-on testing. A regulator record alone cannot justify an overall product rating. Payment performance, support quality, bonuses and safer-gambling tools require their own evidence.
- The live site was checked at https://beincasinos.online/reviews/ and still clearly identifies the scoring method as planned and profiles as unrated. Do not claim recent source changes are deployed unless verified live.
- **Batch 1 spot check — Fuego Casino (Spain), 25 October 2026:** the official consumer homepage returned operator identity and a self-reported DGOJ authorisation statement for 8PE España PLC, including singular licence identifiers MAZ/2020/065, RLT/2020/033 and BLJ/2020/031 dated 19 August 2020. This is operator-published evidence, not an independently captured current DGOJ register result. The requested terms URL returned essentially the same generic footer/responsible-gambling copy rather than accessible full bonus/withdrawal terms; the official site metadata also exposed `noindex,nofollow`. Therefore current bonus, cashier, withdrawal, support quality, accessibility and several safer-gambling criteria remain unassessed. **No overall score or stars justified.** Sources: https://www.fuegocasino.es/ and https://www.fuegocasino.es/terminos-y-condiciones/ . The English DGOJ URL previously referenced returned 404 during this check; use the regulator's current operator-finder route and capture the exact record before marking the gate passed.

## Batch tracker

| Batch | Scope | Status |
|---|---|---|
| 0 | Current live/source audit and scoring guardrails | Complete |
| 1 | Re-check 10 profiles in the priority markets against primary regulator sources and current official terms | In progress — Fuego Casino spot check done; current terms/register capture incomplete, remains unrated |
| 2 | Complete per-criterion evidence capture and score calculations for eligible profiles | Not started |
| 3 | Add researched score breakdowns, ratings, bonus status, sources and check dates to cards and detail pages | Not started |
| 4 | Expand/correct market distribution, legal review and technical QA | Not started |
| 5 | Deploy only after review gates; verify domain and Pages preview, robots, sitemap and representative pages | Blocked on deployment verification and legal/content gates |

## Release gates

- No made-up scores, ratings, bonus amounts, official logos, author credentials or hands-on test claims.
- Every score must be reproducible from criterion-level notes and sources.
- Every bonus must show official source, conditions and check date or remain “Not verified”.
- Affiliate compensation and listing fees must not influence scores or ordering.
- Public indexing must remain blocked until the content/legal release gates are cleared; current `robots.txt` is `Disallow: /` and must not be changed casually.
- Before launch, check mobile UX, accessibility, internal links, canonical URLs, sitemap accuracy, structured data validity, 404/redirects, privacy disclosures, security headers, and live deployment parity.
