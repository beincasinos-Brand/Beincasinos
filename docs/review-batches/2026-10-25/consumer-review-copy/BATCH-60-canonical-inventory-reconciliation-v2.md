# Batch 60 — Canonical inventory reconciliation v2
**This is a QA batch, not three additional brands.** It prevents inflating the 100-brand target by counting repeated names, country variants, venues and product categories as unique casinos.

## Canonical identity rules
1. One canonical ID per genuinely distinct brand, with market variants as child records.
2. Keep aliases, former names, domains, corporate parents and local licensees in separate fields.
3. A different country domain does not automatically equal a new brand; a distinct local operator/product may need a market record but not a new global brand count.
4. Casino, sportsbook, poker, bingo, lottery and land-based venue pages must be classified separately.
5. Game suppliers and slot titles are not casino operators.
6. Unverified candidates must not be labelled “verified” or receive a numeric score.

## Minimum inventory fields
- Brand ID and canonical name
- Aliases and official domain by market
- Legal operator and parent company if verified
- Product categories and market scope
- Regulator, official register URL and UTC check date
- Terms URL, offer URL, cashier/help URL and safeguards URL
- Image asset URL and rights status
- Evidence status, rating status and canonical review path
- Duplicate-of field and release blockers

## Status definitions
- Candidate: plausible name, not yet proven as a current distinct casino brand.
- Identity unresolved: exact domain or legal entity ambiguous.
- Market blocked: product or eligibility not established or not permitted.
- Evidence pending: identity plausible, required primary-source checks incomplete.
- Evidence checked: claims have dated primary evidence, but QA may remain.
- Publish ready: legal, content, image, score and SEO checks pass.

## Batch-level findings
- Swiss candidates use the regulator list as a starting point; operator, domain, terms and assets still require current rechecks.
- Michigan and New Jersey candidates are state-specific, not nationwide recommendations.
- Germany, Netherlands, Sweden and France require product-category gates; brand familiarity alone is not permission for an online casino product.
- Country/province/state variants in earlier batches must be merged into canonical records where appropriate.
- User-supplied partnership history is a lead, not independent proof of current licensing, offer terms or permission in all 12 target markets.

## Release decision
Do not claim the 100-brand milestone until the inventory contains 100 distinct canonical casino brands with resolved identity and documented status. Do not publish invented bonuses, scores, licences or generic stock images presented as brand logos. Keep PR draft and production untouched until reconciliation is complete.
