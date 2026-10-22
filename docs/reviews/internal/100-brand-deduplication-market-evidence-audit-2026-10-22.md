# 100-brand programme — deduplication and market-evidence audit

**Prepared:** 22 October 2026  
**Status:** INTERNAL / RESEARCH CONTROL — NOT FOR PUBLICATION  
**Branch:** ops/tier1-10-market-100-brand-roadmap-2026-10-22

## Executive finding

The legacy candidate register has 100 numbered rows, but row count is not the same as 100 distinct global brands, 100 verified market entries, or 100 completed reviews. It repeats global brands under market suffixes (for example, Bet365, 888, Unibet, LeoVegas, Betsson, Mr Green, Betfair and PokerStars) and includes Romania although the current 10-market roadmap calls for Switzerland and Belgium. The register must not be presented as “100 verified brands.”

## Required counting model

Track these three counts independently:

1. **Unique global brand** — deduplicate spelling variants, localisations and market suffixes. A brand counts once globally.
2. **Market-brand eligibility record** — one row per proposed brand + target market, supported by the relevant official regulator and an exact active consumer domain. One brand can have multiple market records, but this does not increase the unique-brand count.
3. **Approved original review** — a market-specific article with archived first-party terms, licence/operator/domain proof, payments and withdrawal policy, bonus rules where relevant, complaint/ADR, privacy, safer-gambling controls, dated enforcement review, citations, and independent editorial sign-off. Desk research alone does not establish live product performance.

## Target markets and allocation

Use the roadmap markets only: Great Britain, Italy, Spain, Netherlands, Germany, Switzerland, Sweden, Denmark, Belgium, and Ontario (Canada). Initial planning allocation: 10 review slots per market, 100 market-specific review slots total. The 100 slots are **not** a promise of 100 unique global brands; deduplicate the global brand count separately and report both figures. If a jurisdiction cannot support 10 eligible brands under its applicable product-specific rules, do not pad the list with unlicensed, inactive, duplicate or non-casino products—document the shortfall and propose a compliant replacement market for approval.

## Market-specific official evidence starting points

- **Great Britain:** UK Gambling Commission business register: https://www.gamblingcommission.gov.uk/public-register/businesses  
  The register can be searched by business, trading name, domain or account number. Confirm the exact consumer-facing domain, active licence status, and the specific remote casino activity; a generic betting or software permission is not enough.
- **Spain:** Dirección General de Ordenación del Juego operator finder: https://www.ordenacionjuego.es/en/operadores-juego/operadores-licencia/operadores  
  Match the exact casino domain and operator. A sports-betting domain or operator presence alone does not prove casino authorisation.
- **Netherlands:** Kansspelautoriteit register of licensees: https://kansspelautoriteit.nl/register-licensees  
  Verify the legal entity and exact site/app, current licence, and the specific permitted product.
- **Other markets:** Use the regulator named in the roadmap (ADM Italy; GGL Germany; ESBK Switzerland; Spelinspektionen Sweden; Spillemyndigheden Denmark; Belgian Gaming Commission; AGCO/iGaming Ontario). Capture a dated regulator result for each record. Do not substitute a general licence logo, affiliate directory, search snippet, or an international licence for local market authorisation.

## Record schema required before approval

Each row must include:
- canonical global brand name and any known aliases (for deduplication);
- target market and market-specific consumer domain;
- legal contracting operator and regulator account/licence identifier;
- current licence status, product permission and verification date;
- official terms URL and captured/version date;
- bonus terms URL or explicit “no offer reviewed”;
- deposit/withdrawal methods, fees, limits, processing language and KYC conditions (source-backed; never claim a withdrawal was tested unless it was);
- complaints and ADR route;
- safer-gambling limits, time-outs, self-exclusion and reality-check tools;
- privacy/data policy and relevant third-party disclosures;
- regulatory actions, dates, exact findings and remediation context;
- research limitations, missing evidence and status (QUEUE / HOLD / APPROVED REVIEW);
- reviewer and independent second-review sign-off.

## Current work inventory (22 October 2026)

- Legacy candidate register: 100 numbered rows; global deduplication and target-market reconciliation still required.
- Great Britain batch 01: 15 evidence-led narrative drafts in gb-batch-01-15-evidence-led-review-drafts-2026-10-22.md; all are HOLD.
- Approved public reviews: 0.
- Confirmed market-specific review approvals: 0 in this programme audit.
- Live public route recheck: recorded in live-public-route-recheck-2026-10-22.md.
- Deployment: intentionally not performed during this research pass. No GitHub Actions run was triggered by this audit.

## Release gates

Do not promote an entry to APPROVED REVIEW until:
1. exact brand + domain + contracting operator + market-specific casino permission are aligned;
2. current terms and material policy pages are captured and cited;
3. key consumer claims are directly supported, with no invented bonus, test result, payout time or score;
4. enforcement history is checked and fairly contextualised;
5. the review includes clear limitations and a dated “last checked” note;
6. independent second review is recorded;
7. legal/editorial and responsible-gambling review gates pass.

Do not publish the internal candidate register or drafts. Do not label a site “safe”, “trusted”, “best”, or “recommended” merely because a regulator lists it. Do not infer Google indexing from robots.txt or sitemap availability.
