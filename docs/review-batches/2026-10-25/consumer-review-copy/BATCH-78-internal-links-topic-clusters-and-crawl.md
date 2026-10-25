# Batch 78 — Internal linking and crawl design
**Purpose:** support discovery without manufacturing thin pages or misleading geographic coverage.

## Proposed information architecture
- /reviews/ — central index of reviewed products, with filters by verified category and eligible market.
- /reviews/{brand}/ — one canonical brand review where appropriate.
- /markets/{market}/ — only where local rules and eligible products justify a useful market guide.
- /methodology/ — scoring, evidence standards, and editorial independence.
- /responsible-gambling/ — non-promotional support resources.
- /about/ and /affiliate-disclosure/ — ownership, contact, and monetisation disclosure.

## Linking rules
- Link from a market page to brands whose eligibility has been checked for that market.
- Link each review to methodology, official terms, responsible-gambling tools, and relevant market guide.
- Use descriptive anchor text naturally; don't repeat exact-match anchors in every paragraph.
- Breadcrumbs must reflect actual hierarchy.
- Avoid cross-linking unrelated products merely to increase link count.
- No indexable empty category pages, search-filter URLs, or near-duplicate country pages.

## Technical QA
- One canonical URL per content page.
- Unique title and meta description based on actual page.
- HTTP 200 for intended pages; 404/410 for removed pages where appropriate.
- Sitemap contains canonical, indexable URLs only.
- No orphan pages; no accidental noindex on intended content.
- Validate mobile layout and image loading before launch.
- Structured data must match visible content and must not invent aggregate ratings or reviews.

## Measure
Use Search Console query/page data after launch to improve useful pages. Don't promise a fixed number of impressions; indexing and traffic are not guaranteed.
