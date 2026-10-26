# Search-growth quality batch — 26 October 2026

## Scope

This batch fixes a live-source inconsistency on the review directory: its HTML meta description described evidence-led market research, while Open Graph and Twitter previews still claimed “100 market research profiles” with older wording. The social descriptions now match the current meta description exactly. This prevents stale snippets when the URL is shared and keeps metadata consistent with the page's stated limitations.

## SEO north star and constraints

The long-term aspiration of 100 million Google Search impressions per day is not a forecast or a controllable delivery promise. It would require extraordinary scale, broad demand, strong rankings and sustained quality. Track progress using Search Console impressions, clicks, CTR, average position, indexed canonical URLs, and qualified page-level engagement. Do not interpret sitemap submission or URL discovery as guaranteed indexing.

## Target-market architecture

The current approved target-market list is: Australia (AU), Canada (CA), Great Britain (GB), United States (US), Switzerland (CH), Germany (DE), Netherlands (NL), Sweden (SE), Spain (ES), Italy (IT), France (FR), and Belgium (BE).

Important product/legal distinctions:
- Australia and France must not be marketed as markets for locally legal real-money online casino recommendations where the applicable framework prohibits that product category. Build lawful, primary-source education pages instead.
- Canada and the United States require province/state-level scope. A page must not imply nationwide authorisation from a provincial or state permission.
- For all other markets, verify the exact operator, legal entity, domain, licence class, product scope, and current register entry before describing a casino as authorised.
- Do not publish all 12 markets merely to fill a country grid. Each market page must have original, useful local information and official primary sources.

## Recommended page clusters

1. **Regulatory hubs:** one source-led page per target market; identify regulator, exact register, product-specific limits, consumer-protection routes, last-check date, and links to primary sources.
2. **Review profiles:** one canonical profile per operator-market pair only where the operator/domain and market eligibility are evidenced. Clearly separate research profile, hands-on test, and scored review.
3. **Consumer guides:** licence and legal-entity checks; bonus and withdrawal terms; complaint evidence; RTP/volatility/house edge; safer-gambling tools. Each guide should answer a distinct question and link to the relevant regulator and methodology.
4. **Tools:** wagering-turnover calculator and terms checklist, with plain-language limitations and accessible mobile controls.
5. **Trust pages:** methodology, editorial policy, affiliate disclosure, correction/contact route, privacy, terms and responsible-gambling resources.

## Publication gate for every review

Do not publish or imply a numeric score, bonus amount, hands-on test, licence approval, or recommendation without dated evidence. The evidence record should contain the official URL, legal entity, exact domain, regulator register URL, licence/product scope, market allowed/excluded, date checked, reviewer, source for any bonus claim, and unresolved issues. If material evidence is missing, use HOLD and keep scores withheld.

## Technical QA before a release

- Review `/reviews` and `/reviews/` redirects on the production hostname; confirm a single permanent redirect to the canonical trailing-slash URL and no chains.
- Investigate the Search Console `/cdn-cgi/l/email-protection` 404 as a Cloudflare-generated path. Do not add a fake page or include it in the sitemap; confirm whether the live page still emits email-obfuscation markup and whether the reported URL is historical.
- Check canonical URL, `robots` directives, sitemap membership and live HTTP status for each reported affected URL.
- Keep sitemap URLs absolute, canonical, indexable and mapped to real public HTML pages. Set `lastmod` only when the page was materially updated and the date is accurate.
- Run the repository's source-level checker and browser/mobile smoke tests; then test the actual Cloudflare Pages deployment. Source checks alone do not confirm production behavior.
- Avoid repeated deployments while the PR chain is incomplete; merge and release in dependency order after reviewing CI and diffs.

## Measurement cadence

Record a baseline in Search Console before each release. After deployment, inspect representative URLs and the sitemap, then compare 7-day and 28-day windows for impressions, clicks, CTR, average position, and indexed pages. Separate branded and non-branded queries, and compare markets and page clusters. Prioritise pages with meaningful impressions but low CTR, pages ranking near the first page, and URLs with indexing/canonical problems. Do not chase impressions by creating near-duplicate pages or publishing unsupported operator claims.

## Current status

- The metadata-parity correction is committed on branch `search-growth-quality-batch-20261026`.
- This branch is based on `seo-content-quality-batch-20261026`, which itself depends on `audit-big-batch-20261026`; review/merge the chain in order.
- No merge, deployment, live redirect validation, or Search Console outcome is claimed by this document.
