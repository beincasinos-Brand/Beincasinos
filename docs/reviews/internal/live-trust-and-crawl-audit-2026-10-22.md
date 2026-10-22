# Live trust, privacy-route and crawl audit — 22 October 2026

**Scope:** Read-only fetches of live policy pages, privacy URLs, robots.txt and sitemap.xml, plus a source-document consistency check. No Actions workflow, deployment, DNS change or Search Console action was triggered.

## Verified live findings

### Crawl directives and sitemap
- `https://beincasinos.online/robots.txt` returns:
  ```text
  User-agent: *
  Allow: /
  Sitemap: https://beincasinos.online/sitemap.xml
  ```
- `https://beincasinos.online/sitemap.xml` is fetchable and lists **45 absolute URLs**, including `/privacy/`, `/markets/`, `/reviews/`, policy pages and educational guides.
- This confirms crawl permission and sitemap availability only. It does not confirm Google has crawled, indexed or ranked those URLs.
- A stale README launch-blocker line still says to keep a temporary robots.txt disallow rule. That conflicts with the current live file and must not be used as an instruction to re-block crawling without a deliberate owner decision. Source docs should distinguish crawlability from permission to launch/index the business.

### Privacy URL
- Canonical privacy notice is live at **https://beincasinos.online/privacy/** and self-canonicalises there.
- **https://beincasinos.online/privacy-policy/** returns 404 in the current fetch. The latter is not in the current sitemap; the valid route is `/privacy/`. Do not call this a broken canonical unless internal links or search listings are found pointing to the old route.
- Privacy notice says the current site has no visitor accounts, contact form, analytics integration, advertising pixel or active affiliate tracking; calculator/checklist values remain in the browser. It notes that hosting/security infrastructure may process request metadata and links Cloudflare's privacy policy.
- This is a repository/site-content statement, not an independent audit of Cloudflare configuration, logs, email provider, legal compliance or CNDP filings.

### Editorial and publisher transparency
- `/about/`, `/contact/`, `/editorial-policy/`, `/affiliate-disclosure/` and `/terms/` are fetchable and disclose the public-facing publisher identity and contact mailbox, correction channel, commercial independence rules, and the current fact that there are no scored casino profiles.
- The affiliate disclosure says paid listings and affiliate links are planned but not currently offered. Keep that statement aligned with actual production links and commercial arrangements.
- A fetched third-party automated trust-score page flags the domain as very new and low-traffic, while also reporting valid SSL and HTTP 200. This is a weak, automated heuristic—not evidence that the site is fraudulent and not an SEO metric. Do not publish or rely on that score as a factual quality verdict. New-domain age and low visibility are normal early-stage constraints; strengthen verifiable publisher, editorial and legal transparency instead.

## Actions / priorities
1. Keep the live `robots.txt` as-is unless a deliberate owner decision is made to pause crawling; do not change DNS, hosting, robots or indexing settings during this audit.
2. Before claiming indexing, inspect the Search Console URL Inspection and Page indexing reports. Google documents that sitemap submission is a hint and URL inspection is the correct way to check the indexed version and live indexability.
3. Keep `/privacy/` as the canonical route; only add a redirect for `/privacy-policy/` if there is evidence of existing backlinks, user-facing references or a deliberate compatibility requirement.
4. Keep public statements about publisher identity, mailbox, hosting, analytics, cookies and affiliate tracking synchronized with the actual production configuration. The internal privacy/data-handling gate remains open for legal/controller, hosting data-flow and applicable Moroccan CNDP review.
5. Keep the brand-name/trademark and launch gates visible. Crawlability is not legal launch approval.
6. Continue to keep internal evidence packs out of the public build and sitemap.

## Status
- Sitemap fetch: 45 URLs.
- Robots: allows crawling; sitemap directive present.
- Privacy canonical route: `/privacy/` works; `/privacy-policy/` returned 404 and is not listed in the sitemap.
- Google indexing: not verified by this audit.
- Actions/deploy: none triggered.
- Approved casino reviews: 0/100.

## Sources
- https://beincasinos.online/robots.txt
- https://beincasinos.online/sitemap.xml
- https://beincasinos.online/privacy/
- https://beincasinos.online/privacy-policy/ (404 observed)
- https://beincasinos.online/about/
- https://beincasinos.online/contact/
- https://beincasinos.online/editorial-policy/
- https://beincasinos.online/affiliate-disclosure/
- https://beincasinos.online/terms/
- https://support.google.com/webmasters/answer/9012289
- https://developers.google.com/search/docs/crawling-indexing/build-sitemap
