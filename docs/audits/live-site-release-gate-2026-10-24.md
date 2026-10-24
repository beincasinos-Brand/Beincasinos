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
