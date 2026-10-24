# BeInCasinos — target reconciliation and release gates
**Reconciled:** 24 October 2026  
**Repository:** `beincasinos-Brand/Beincasinos`  
**Production platform:** Cloudflare Pages (no deployment performed by this change)

## Executive state — do not inflate the numbers

| Metric | Verified state | Interpretation |
|---|---:|---|
| Target directory entries | 100 | A research queue, not 100 eligible/licensed brands |
| Unique labels in directory | 100 (latest prior source-level audit) | Label uniqueness alone does not prove unique operator, product or jurisdiction |
| Current official-site image candidates | 50 (latest tracker snapshot) | Source discovery only; every candidate remains rights-pending |
| Cards with a populated official-domain field | 53/100 (latest tracker snapshot) | Field coverage, not validation of every domain |
| Cards with a populated legal-operator field | 50/100 (latest tracker snapshot) | Field coverage, not regulator-confirmed identity for all rows |
| Evidence grades | A: 44; B: 7; C: 49 | Grade is a source-quality indicator, not publication approval |
| Directory statuses | HOLD: 99; EXCLUDE: 1 | Re-check current branch before using as a live count |
| Publication-approved reviews | **0/100** | No candidate or internal draft is counted as a finished review |
| Cloudflare production deployment in this work | **None** | This report does not claim that any draft is live |

The 100-card directory and its visual work are substantial queue-building progress, but the actual goal is **100 distinct, jurisdiction-appropriate brands plus 100 independently reviewed and publication-approved review pages**. Those are different measures. Never describe the goal as complete until the approval ledger contains 100 approved reviews.

## New draft batches reported on 24 October

These open draft PRs are separate from this reconciliation document and must be reviewed/merged deliberately; they are not production releases.

- [PR #138 — Sky Vegas, Virgin Games, Ladbrokes Casino, Unibet Casino](https://github.com/beincasinos-Brand/Beincasinos/pull/138)
- [PR #139 — Gala Casino, BetMGM Casino, Foxy Games, Slingo](https://github.com/beincasinos-Brand/Beincasinos/pull/139)
- [PR #140 — Bet365 Casino, Casumo, PlayOJO, kwiff Casino](https://github.com/beincasinos-Brand/Beincasinos/pull/140)

Each batch adds four internal noindex drafts. The pages must not be added to the approved count. Their exact contracting entity, domain-to-licence mapping and product-specific permissions remain gates where the draft says so. A brand name or a broad operator licence is not sufficient proof.

## Required 100-brand identity ledger

Before finalising the 100-brand set, each row must have the following normalized key and evidence. Keep one row per materially distinct local product only when it is genuinely distinct; do not count the same operator/brand multiple times simply because it appears in different lead lists.

- `brand_display_name`
- `market_code` and specific state/province/canton where applicable
- `official_live_domain` and the date it was checked
- `contracting_legal_entity`
- `regulator`, official register URL, permission type/status and check date
- `casino_product_scope` (online casino games specifically, not merely sports betting, poker, bingo or a supplier partnership)
- `identity_match_status`: verified / pending / conflict / excluded
- `duplicate_group_key` to catch shared brands, entities, white labels and aliases
- `publication_status`: candidate / hold / exclude / approved
- `next_action` with a primary-source URL

Do not infer that two brands are distinct operators because they have separate homepages. Do not infer that a company permitted for sports betting or poker may offer online casino games. Local permission must match the precise product and territory.

## Mandatory review evidence package

A review is not complete until the record includes dated primary-source evidence for:

1. **Regulatory permission:** current official register entry and the exact casino permission.
2. **Domain and contracting party:** domain, legal operator and customer contract align.
3. **Terms and promotions:** complete terms, wagering rules, exclusions, expiry, maximum bet and cashout restrictions where applicable.
4. **Payments and withdrawals:** published methods, fees, limits, verification, processing statements and the source date. Do not present operator estimates as independently measured results.
5. **Complaints and dispute resolution:** complaint route, ADR/ombudsman where applicable, and escalation details.
6. **Safer gambling:** deposit/time limits, self-exclusion, reality checks and locally relevant support.
7. **Privacy, cookies and accessibility:** privacy notice, cookie controls and documented accessibility checks.
8. **Enforcement and risk:** relevant current and historical regulatory actions, with dates, context and status/appeal where available.
9. **Original editorial work:** useful market-specific prose, clear limitations, methodology, affiliate disclosure and no unsupported superlatives.
10. **Second review and release approval:** another reviewer checks sources, claims, calculations, legal framing, images and links; record the approval date and reviewer.

Where lawful and feasible, distinguish published claims from reproducible consumer checks. Never claim to have deposited, played, contacted support, or withdrawn money unless that exact test was actually performed and recorded. If evidence is unavailable, say so and withhold the score.

## Image and visual quality gates

The 50 image candidates in the prior directory audit are **not rights-cleared assets**. Before production use, record for every image:

- source page and exact asset URL;
- whether the asset is a logo, wordmark, favicon or editorial illustration;
- owner/rights basis and permission or licence terms;
- download/check date and a stable local asset path if permitted;
- dimensions, format, file size, alt text and fallback;
- confirmation that the asset represents the exact brand and local product.

A logo appearing on an official site does not itself grant republication rights. Keep rights-pending assets labelled as such and use original CSS artwork or properly licensed assets until clearance is documented. Verify contrast, keyboard focus, reduced motion, responsive layout, image loading and real-device rendering before release.

## Market-scope safeguards

- **Australia:** do not use offshore casino brands to fill the target; online casino services are generally prohibited.
- **France:** do not treat a sports/poker licence as an online-casino authorisation; online casino is not generally authorised.
- **US and Canada:** permission is state/province/tribal-specific. Never generalise one jurisdiction's authorisation to the whole country.
- **Germany:** verify the exact permitted product and territory; a state-specific slot authorisation is not blanket nationwide online-casino permission.
- **All other markets:** confirm current local regulator, exact domain, legal entity and casino-game scope at the time of review.

## Release sequence

1. Reconcile all candidate rows against the 100-card directory and the latest open PRs; deduplicate brand + market + product + legal entity.
2. Resolve every candidate's domain/entity/product permission. Exclude legal-scope mismatches and inactive/surrendered permissions.
3. Complete evidence packages and original reviews for the qualified set; leave unresolved entries on HOLD.
4. Clear image rights or retain the designed fallback; never invent image URLs or rights.
5. Run source and link checks, accessibility checks, mobile/desktop visual QA, sitemap/robots/canonical/noindex review and duplicate-content checks.
6. Obtain independent editorial/legal approval and update the approval ledger.
7. Only after the approved target and site QA are genuinely complete, prepare a separate Cloudflare release plan and confirm the intended production action before deploying.

## Non-negotiable counting rule

**Research lead ≠ verified eligible brand ≠ draft review ≠ approved review.** The 100-card directory is a useful interface and queue; it is not evidence that 100 brands are cleared. The current approval count remains **0/100** until documented sign-offs say otherwise. This document changes tracking and release controls only; it does not publish candidate reviews, run GitHub Actions, or deploy to Cloudflare.
