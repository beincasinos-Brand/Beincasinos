# First-100 queue content-completeness audit — 23 October 2026

## Scope and method

This is a field-completeness check of the market-specific CSV rows attached to the first-100 distinct-ID research work queue on branch `feature/directory-global-brand-count-disclosure-2026-10-23`. It checks whether a field is populated; it does **not** validate the correctness or freshness of the URL, prove a licence is current, or approve a consumer review.

The 100 provisional IDs represent 149 market-specific CSV rows. Keep the market rows separate because local permissions, domains, contracting entities and terms may differ.

## Findings

| Evidence / content field | Blank rows of 149 | Missing |
|---|---:|---:|
| Official regulator register URL | 0 | 0% |
| Legal entity field | 0 | 0% |
| Current terms URL | 132 | 89% |
| Withdrawals / banking URL | 146 | 98% |
| Complaints / ADR URL | 146 | 98% |
| Responsible-gambling URL | 144 | 97% |
| Privacy/tracking review status | 61 | 41% |
| Partnership contact URL | 149 | 100% |

A populated legal-entity or register field may still be a candidate or unresolved match; this is a completeness count only. In particular, the 100% blank partnership-contact URL rate means the data does not support claiming a verified commercial contact for these rows. Do not scrape personal contact details or infer contacts from a brand name.

## Publication gate for every brand-market page

1. Match the current official register to the exact casino vertical, consumer-facing domain and contracting entity.
2. Add a current official terms URL and review bonus terms only if an offer is discussed.
3. Add current banking/withdrawal and complaints/ADR sources; distinguish published estimates from tested outcomes.
4. Add safer-gambling and privacy/cookie sources and record what was actually checked.
5. Check accessibility, customer support and relevant enforcement history; cite dated primary sources.
6. Verify each image's identity, direct rendering, reuse permission and attribution. If rights are unclear, use original CSS/editorial artwork rather than implying permission.
7. Write original market-specific copy with clear source dates and explicit unknowns. No invented ratings, first-hand tests, payout promises, bonuses or operator details.
8. Require an independent second reviewer and recorded editorial approval before publication.

## Immediate priority

The directory can display 100 research cards, but the CSV is not yet rich enough to support 100 publication-quality consumer reviews. Resolve terms, withdrawals, complaints/ADR and safer-gambling source gaps first. Then complete the content and image-rights review for each distinct brand-market page. Current publication-approved review count remains **0/100**.

**Status: OPEN / HOLD.** No entry is certified by this audit, and no Cloudflare deployment is implied.


## Website card-structure check

A structural scan of `brand-directory/index.html` on this branch found **100 cards**. All 100 contain a research summary, official-domain field, legal-operator field, regulator/authority field, evidence-grade field, expandable verification checklist and research-context/evidence-limits section. **50 cards have remote image candidates and 50 use CSS artwork/monogram fallbacks.** The 50 remote images remain **rights pending**; structural presence does not establish reuse permission, current identity, or successful rendering on the production site. This check is markup-level QA only and does not verify factual accuracy of every claim.
