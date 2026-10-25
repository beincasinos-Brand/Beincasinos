# Market Gate Audit — Batch 08
Date: 2026-10-25
Status: INTERNAL ONLY — NO PUBLIC SCORE OR LEGAL CLEARANCE

## Purpose
This batch hardens the release workflow for BeInCasinos' 12 target markets (AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE). A regulator directory is a starting point, not blanket permission for every gambling product. For each public casino profile, record exact domain, legal entity, regulator record, licence status, permitted product type, jurisdiction, date checked and evidence URL. If any of these do not match, the market gate remains blocked.

## Official starting points and constraints

### Australia (AU)
Official source: https://www.acma.gov.au/check-if-gambling-operator-legal
- ACMA's current register is for licensed interactive gambling providers. The listed services are largely wagering/betting providers; appearance on the register does not imply a general online casino/slots licence.
- Require exact product-category confirmation. Do not infer that a sportsbook brand may lawfully offer online casino games in Australia.
- Current source search result explicitly says users should avoid providers not on the register and notes that licensed providers may still face restrictions (including credit and in-play betting).

### Canada (CA)
- Canada must be treated province-by-province, not as one national online casino market.
- Ontario's iGaming Ontario operator directory is relevant only to Ontario-authorised products/operators; British Columbia has its own regulatory framework. A provincial record does not clear all of Canada.
- No Canada-wide pass should be applied to a profile. Record province and exact domain separately.

### Great Britain (GB)
Official source: https://www.gamblingcommission.gov.uk/licensees-and-businesses/page/public-register
- Search both operator/company and exact website/app/domain in the UKGC register.
- The register also records regulatory actions and settlements. Capture these as separate risk evidence.
- A brand name alone is insufficient; match the legal entity, account/licence scope and domain.

### United States (US)
- No nationwide online casino clearance. Require state-specific regulator and product authorisation, plus exact domain/operator matching.
- A US-state permission must not be extended to other states. If the state/product cannot be substantiated, mark the US market gate blocked.

### Switzerland (CH)
Official source: https://www.esbk.admin.ch/en/online-gambling/
- The ESBK/FGB official online casino list is a useful domain-level starting point.
- The official list states that a casino's general licence extension is not sufficient by itself; individual games also need the relevant permit.
- Capture exact casino domain and concessionaire; do not treat foreign licences as Swiss authorisation.

### Germany (DE)
- Use the official GGL whitelist and match exact domain and authorised product category.
- Authorisation is category-specific; a sports-betting listing is not permission for virtual slots or other online casino products.
- Do not score a casino product based on an operator's generic statement that it is “licensed in Germany”.

### Netherlands (NL)
Official source: https://kansspelautoriteit.nl/register-licensees
- The KSA register lets users search company, website, app or licence number.
- Require exact domain and current status. A licence in another jurisdiction is not Dutch authorisation.
- Record current enforcement or licence changes and do not assume historical listing remains active.

### Sweden (SE)
- Use Spelinspektionen's official licence register for commercial online gaming/betting, then confirm exact domain and product scope.
- Do not infer authorisation from a Swedish-language site, SEK currency, or a generic international licence.
- Capture current licence status and product category before any Sweden-targeted recommendation.

### Spain (ES)
Official operator finder: https://www.ordenacionjuego.es/en/operadores-juego/operadores/licencia/operadores
Recent resolutions: https://www.ordenacionjuego.es/operadores-juego/resoluciones
- Check exact operator/domain and the specific game licences shown by DGOJ.
- Recent resolutions and game-specific authorisations may change scope. Do not treat a domain/operator appearance as proof that every casino game category is authorised.
- Recheck the current operator record before publication.

### Italy (IT)
Official ADM concessionaire source: https://www.adm.gov.it/portale/monopoli/giochi/gioco_distanza/gioco_dist_concessionari?pager=2
- Verify the current remote-gambling concession and the exact domain/operator relationship.
- A lead in a concessionaire list is not a complete review of casino products, bonus terms or current availability.
- Recheck the official source immediately before any Italy market claim.

### France (FR)
- Use the ANJ's official licensed-operator information and authorised-product categories.
- Do not label a general online slots/table casino “legal in France” based on sports betting, horse betting or poker authorisation. Category matters.
- If the exact game category is not authorised, do not publish a French casino offer as available or approved.

### Belgium (BE)
- Use the Belgian Gaming Commission's official register; check the specific online licence class and associated domain.
- A general foreign licence is not Belgian authorisation. The domain and permitted product must match the Belgian record.
- If no exact record can be substantiated, keep the Belgium market gate blocked.

## Release checklist (must be completed per brand x market)
1. Exact canonical gambling domain recorded (not just brand name or affiliate redirect).
2. Legal operator entity recorded from current first-party terms.
3. Exact operator/domain checked in the official regulator register on the review date.
4. Licence status is active and the product category is permitted in that jurisdiction.
5. Brand's terms, bonus offer, cashier and responsible-gambling page belong to that same domain/market.
6. Excluded-country clauses do not exclude the target market.
7. Bonus details have a timestamp and full wagering conditions; headline copy is not used as proof.
8. Payment/withdrawal methods, limits, fees and processing times are attributed to their exact source; actual payout testing is labelled separately.
9. Complaint data is separated into open allegations, resolved complaints, and regulator decisions.
10. Numeric score is published only when every methodology criterion has evidence and the market gate has passed.
11. Affiliate commission, commercial relationships and paid placements do not affect score.
12. Record the evidence freshness date and recheck volatile facts before publication.

## Immediate application to Batch 07
- Kokobet: do not use the headline welcome package until reconciled with detailed terms; verify exact domain/operator/licence and target market.
- Casea: verify licence claim and exact domain/operator; test cashier and offer details.
- Casinia: casiniaz.com is a specific domain variant and cannot be conflated with other Casinia domains; the text's AU wording is not proof of Australian casino authorisation.
- BinoBet: terms snapshot is dated 2024; refresh before using any offer or payment claim.
- MrPunter: terms list the US and Sweden among excluded jurisdictions; do not recommend there unless current terms materially change and official gate is independently passed.
- Bull Casino: general-terms fetch returned HTTP 403; locale-specific bonus terms cannot stand in for every market.
- Legiano: fetched operator definition did not fully specify legal entity/licence details; keep gate blocked until verified.
- SGCasino: verify licence reference and exact domain/operator through the relevant official register; locale-specific bonus must be checked.
- Millioner and Betscore: exact domains unresolved; no legal or product assessment can begin until identity is established.

## Evidence limitations
This file records official-register workflow and high-level market restrictions, not a completed licence audit for every listed brand. It is not legal advice. No real-money testing or account activity was performed. Do not expose this internal document in the public site build.
