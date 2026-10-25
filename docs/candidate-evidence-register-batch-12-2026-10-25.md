# Batch 12 — Candidate evidence register and market allocation controls
Date: 2026-10-25
Purpose: give the 100-profile programme a consistent evidence ledger. Candidate names below are not approved listings; a candidate is not a verified casino or market-authorised operator merely because its name is known.

## Required fields for every candidate
| Field | Required value |
|---|---|
| Candidate ID | Stable internal ID; never reuse |
| Brand | Exact brand spelling |
| Canonical operating domain | Exact current domain; redirects recorded |
| Legal operator | Legal name + source URL, or “unverified” |
| Market | One of AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE |
| Product category | Casino / sportsbook / poker / bingo / other |
| Regulator and register entry | Exact entry URL or “not found”; date checked |
| Domain and product match | Pass / fail / unclear |
| Terms evidence | Exact terms URL, date fetched, relevant clauses |
| Bonus evidence | Offer URL, eligibility, currency, wagering, expiry, cap, or “not verified” |
| Payments evidence | Official methods/limits URL; do not call estimates tested |
| Safer-gambling evidence | Exact page and controls observed |
| Complaints evidence | Official route and any independently sourced route |
| Review evidence | Source notes for each score dimension |
| Image provenance | Owned/licensed/official press asset/placeholder |
| Editorial decision | READY / PUBLISH UNRATED / HOLD / REMOVE-REDIRECT |
| Reviewer and checked date | Human review record |
| Recheck trigger | Bonus expiry, terms change, domain change, regulator update, complaint escalation |

## Status definitions
- **READY:** exact domain/operator/product passes the target-market gate; all required review evidence is current and score is reproducible.
- **PUBLISH UNRATED:** useful original review can be published, but one or more score dimensions are unassessed. Show no numeric overall score; only publish market claims supported by evidence.
- **HOLD:** identity, domain, terms, legal status, or product-market fit is unclear; do not market as verified or authorised.
- **REMOVE-REDIRECT:** obsolete, duplicate, misleading, unsupported, or irrelevant page. Redirect only to a genuinely equivalent page; otherwise return an appropriate unavailable status.

## Initial research queue (not a verified list)
The following names are seeds for exact-domain resolution, not endorsements or claims of current legal availability:
- Previously mentioned in project notes: Kokobet, Binobet, MrPunter, Casinia, Casea, Legiano, SGCasino, Bull Casino, Millioner, Betscore.
- Every one of the above remains subject to exact-domain, operator, market, category, terms, and regulator checks. Prior familiarity or affiliate acceptance is not regulator evidence.
- Additional candidates must be sourced from official regulator registers first for the intended market, then matched to the operator's official site and product. Do not add a name just to fill a market quota.

## Market allocation is a planning target only
The current 100-slot planning split is: AU 8, CA 8, GB 10, US 8, CH 8, DE 8, NL 8, SE 8, ES 10, IT 8, FR 6, BE 10. These numbers are workload allocation only, not a claim that this many eligible brands exist or have been verified in each market. Some jurisdictions restrict or prohibit specific online casino products; do not force casino reviews into markets where the product is not lawfully authorised.

## Brand-level evidence rules
1. Record the source URL and date for every factual claim that could change.
2. Prefer regulator register for authorisation; operator site for its own current terms; independent source for complaints/context.
3. Separate operator claims from regulator-confirmed facts.
4. Record country/domain variations independently. Do not infer that a licence for one domain or company covers a sister brand.
5. Capture bonus terms in a structured record and reconcile promotional banners against the detailed terms before showing a number.
6. If a source is blocked or unavailable, record the failure and do not substitute a different locale/domain silently.
7. Never claim hands-on payout, customer support, or mobile-app testing unless it was actually performed and dated.
8. Never imply a brand is available to all users in a country when availability differs by state/province or product type.

## Operational next actions
1. Fix and deploy the robots.txt crawl block through a reviewed change.
2. Parse all sitemap URLs and classify them by HTTP status, canonical, robots/noindex, market, product, title/H1 uniqueness, and content completeness.
3. Create one ledger row per existing profile before adding more candidates.
4. Prioritise evidence completion for profiles with reliable official-register matches; keep others on hold or unrated.
5. Add the next candidate batch only when exact official domains and regulator sources are captured.
6. After deployment, confirm live responses and use Search Console to monitor discovery, crawl, indexing, and impressions separately.

## Non-claims
This document does not certify any named brand, confirm 100 eligible brands, assert that all 100 reviews are finished, or indicate a merge/deployment/indexing event.
