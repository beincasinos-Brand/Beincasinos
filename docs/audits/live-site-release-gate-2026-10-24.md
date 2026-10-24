# Live-site release gate audit — 24 October 2026

**Site checked:** https://beincasinos.online/  
**Method:** public live-page fetch of the homepage, review directory, methodology, robots.txt and sitemap.xml.  
**Scope:** publication readiness and crawl configuration only. This is not a full browser, accessibility, performance, legal or security audit.

## Findings confirmed on the live site

### Crawlability
- `robots.txt` currently returns `User-agent: * Allow: /` and declares `https://beincasinos.online/sitemap.xml`.
- The sitemap is reachable and currently advertises **46 URLs**.
- The sitemap includes the homepage, review directory, guides, tools, market/research pages, editorial/legal pages and contact page.
- This fetch confirms the published crawl directives and URL list only. It does **not** confirm that Google has indexed the URLs or that Search Console ownership/coverage is healthy.

### Review publication state
- `/reviews/` explicitly says the review directory is still in development and that no casino profiles are currently scored or ranked.
- The methodology describes eligibility gates before scoring and six weighted criteria: terms clarity/fairness (25), payments/withdrawals (20), safer-gambling controls (20), complaints/support (15), operator/licence transparency (10), usability/accessibility (10).
- The methodology says no deposit, withdrawal, customer-service or gameplay tests will be claimed unless documented.
- This wording is aligned with the current evidence posture: internal candidate records and evidence drafts must not be presented as approved consumer reviews.

### Presentation metadata
- The homepage and review directory expose canonical URLs, viewport metadata, Open Graph title/description/URL and a Twitter summary-card declaration in the fetched page metadata.
- This spot-check did not verify all pages' metadata, image previews, structured data, actual image rights, responsive rendering, keyboard operation or Core Web Vitals.

## Additional read-only production smoke check — 24 October 2026, 18:46 UTC

A fresh fetch of the live homepage, `/reviews/`, `/robots.txt`, and `/sitemap.xml` confirmed the current public copy and crawl directives remain consistent with the no-unapproved-reviews posture. The live sitemap advertises **46 URLs** and the homepage exposes canonical/Open Graph metadata. The current public `/brand-directory/` route returns **404**. The current working branch contains a separate `brand-directory/index.html` research queue whose page-level robots directive is `index,follow`, but the branch's source `robots.txt` currently says `Disallow: /` as an explicit pre-launch crawl block. Neither source change is live: the production route is still absent, and the live site's `robots.txt` was observed allowing crawl. Treat these as a source/production mismatch, not a live-site feature. Before any launch, the owner must explicitly choose the intended crawl policy, ensure the production `robots.txt` matches it, verify the route and sitemap after deployment, and confirm the queue's research-only status is clear to users.

The live fetch did not verify mobile/keyboard accessibility, image loading, Core Web Vitals, licence claims or browser workflows. No production deployment was made.

## Release gates still open

1. **100 approved reviews:** current reconciled status is 0/100 publication-approved. Do not count leads, internal drafts, duplicate brands, inactive licences, non-casino products or territory-limited permissions outside their territory.
2. **Evidence completeness:** every candidate needs exact live domain, contracting legal entity, current primary-regulator permission for the exact online-casino product and market, dated current terms, bonus restrictions, payment/withdrawal limits and fees, verification requirements, complaint/ADR route, safer-gambling tools, privacy/cookies, accessibility notes, enforcement review, image-rights provenance, independent second review and editorial/legal sign-off.
3. **Jurisdiction controls:** retain market-specific restrictions. A local or state/province permission must not be described as nationwide or international. Exclude markets where online casino is not generally authorised; do not fill the target with offshore recommendations.
4. **Public-page content:** the current public review directory should remain transparent that no profiles are scored/ranked until evidence and sign-offs exist. Internal review drafts must remain unpublished and noindex.
5. **Publisher and compliance:** verify the real publisher identity and monitored contact route; review privacy/cookie implementation, affiliate disclosures and commercial relationships, target-market requirements, and brand/trademark clearance before a commercial launch.
6. **Technical QA:** test key pages and tools in desktop/mobile browsers, keyboard and screen-reader paths, broken/internal/external links, image alt text and rights, structured data, metadata uniqueness, HTTP status/redirects, sitemap consistency, security headers and performance.
7. **Search monitoring:** validate ownership and sitemap processing in Search Console. A reachable sitemap and permissive robots.txt are not proof of indexing.
8. **Release control:** no merge-to-production or Cloudflare deployment is authorized by this audit. Respect the project constraint to wait until the 100-review target and required checks are complete, then perform the planned single deployment only with the required approval.

## Next execution order

1. Reconcile all existing candidate files into one deduplicated master table keyed by market + product + domain + contracting entity.
2. Re-check primary regulator records and exact domain/entity matches, rejecting or holding ambiguous candidates.
3. Complete each review's consumer-evidence checklist and second-review/sign-off record.
4. Run automated and manual site QA; fix issues on the working branch.
5. Re-run the release gate, confirm all 100 distinct reviews are approved, and request explicit approval before any production deployment.

## Evidence limitations

This audit is a dated snapshot of publicly fetched pages. It does not establish live user experience across devices, accessibility conformance, site analytics, Search Console status, full legal compliance, or the correctness of third-party operator claims. Re-run checks immediately before release.


## Source/production crawl-policy reconciliation — branch review, 24 October 2026

- Source `brand-directory/index.html` currently declares `index,follow`, canonical and Open Graph metadata, and describes the 100 entries as research leads, not recommendations.
- Source `robots.txt` currently contains `Disallow: /` with a pre-launch comment. Therefore the working branch as a whole is not configured for crawlable launch, despite the directory page's indexable meta directive.
- Production's most recent public observation is different: live `robots.txt` allowed crawling and the sitemap exposed 46 URLs, while `/brand-directory/` returned 404.
- **Action before launch:** reconcile the source robots policy with the intended approved release policy; do not simply remove the block by default. Deploy only after owner authorization, then verify production `/robots.txt`, `/sitemap.xml`, `/brand-directory/`, canonical URL and page robots directive from the live host.
