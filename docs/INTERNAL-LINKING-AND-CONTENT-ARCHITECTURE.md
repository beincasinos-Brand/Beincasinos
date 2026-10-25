# BeInCasinos — internal linking and content architecture

## Site structure
Use a shallow, user-first hierarchy:
- Home: editorial promise, market selector and clear methodology.
- Market hubs: /au/, /ca/, /gb/, /us/, /ch/, /de/, /nl/, /se/, /es/, /it/, /fr/, /be/ — only where the market content is lawful and genuinely useful.
- Review pages: /{market}/reviews/{brand}/, with a distinct local scope.
- Evergreen help guides: bonus terms, withdrawal processing vs bank time, identity verification, payment fees, game RTP, complaints, account limits, self-exclusion and privacy.
- Methodology and trust pages: scoring model, editorial independence, affiliate disclosure, corrections, author/reviewer profiles and contact.

Do not publish empty market hubs or generic location pages. If there is not enough verified material, keep the hub noindex until it has useful market-specific content.

## Link rules
1. Every indexable review links to its market hub, scoring methodology, safer-gambling guide, bonus-terms guide and payments guide where relevant.
2. Market hubs link to every approved review in that market with a concise, unique summary and last-checked date.
3. Guides link to reviews only when the example is genuinely relevant; do not force exact-match anchors.
4. Add contextual “compare these features” links only where compared fields are verified and comparable.
5. Breadcrumbs reflect the real hierarchy and match visible navigation.
6. No orphan pages: each indexable URL has at least one meaningful internal link from an approved hub or guide.
7. Avoid footer link dumps, sitewide keyword-rich anchors and generated pages for every filter combination.
8. When two pages answer the same query, consolidate them and redirect only if the destination is equivalent.

## Hub page content requirements
A market hub should include:
- A concise explanation of the legal scope and jurisdiction boundaries.
- A note that availability and licensing are product- and domain-specific.
- Comparison fields only when sourced: exact operator, authorized domain, verified casino category, last checked, evidence status and review score (only if scored).
- Clear distinctions among casino, poker, sports betting and lottery.
- A responsible-gambling section and link to regulator resources.
- A list of independently reviewed, approved pages; do not include HOLD/NOINDEX drafts as recommendations.
- A methodology link and affiliate disclosure.

## Comparison-table integrity
Rows should be comparable and dated. Use “not verified” rather than blank cells or inferred facts. Do not compare payout speeds if one value is operator-stated and another is a hands-on test. Show the source or method in the table or linked notes. Do not assign stars to brands with no completed review.

## Market cautions
- AU: do not promote offshore online casino products as lawful.
- CA: identify province; Ontario eligibility is not nationwide authorization.
- US: identify state; do not imply nationwide online casino availability.
- FR: distinguish regulated poker/sports betting from online casino games.
- CH/DE/NL/SE/ES/IT/BE/GB: check current official regulator and exact domain/product before listing.
- Every local page must be based on current local facts; do not rely on a parent group’s licence or foreign bonus.

## Maintenance
On a material regulatory or terms change, update affected review and hub pages, update the evidence date, recalculate scores only when rubric evidence changes, and remove stale structured data. Maintain a redirect map for renamed pages and keep sitemap output aligned with indexability status.
