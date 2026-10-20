# BeInCasinos

An English-language educational resource for understanding online casino terms, licensing, withdrawals, bonuses, and safer gambling.

## Stack
- Static HTML, CSS, and vanilla JavaScript
- No build step or runtime dependencies
- Prepared for static hosting once launch blockers and commercial-use terms are cleared
- Includes a client-side wagering calculator and a terms-review checklist; no user entries are sent to a server

## Local preview
Open `index.html` directly, or run `python -m http.server 8080` from the project root.

## Source-level quality check
Run `python3 scripts/check_site.py` from the repository root. The dependency-free checker scans HTML pages for missing titles/descriptions, unexpected H1 counts, duplicate page titles or IDs, missing image alt attributes, broken local navigation/resource references, and known launch placeholders. GitHub Actions runs this check on pushes and pull requests to `main`. It is a guardrail—not a replacement for browser testing, accessibility review, checking external links, or legal/privacy review.

## Launch blockers — do not deploy yet
1. **Resolve brand risk before buying a domain or launching.** The name contains “BEIN”, which is an established mark associated with beIN Media Group. A WIPO domain-name decision describes beIN marks registered in Morocco and records a dispute over a domain incorporating BEIN. This does not by itself decide whether “BeInCasinos” infringes, but it makes a proper clearance review particularly important. Search WIPO and OMPIC records for the exact and similar marks in relevant classes and markets, and get qualified trademark advice if uncertain. References: https://www.wipo.int/amc/en/domains/decisions/text/2018/dma2018-0003.html and https://www.wipo.int/en/web/global-brand-database/index.
2. Buy and select the production domain only after the name review, then replace the domain placeholder in `sitemap.xml` and add canonical/OG URLs.
3. Verify every legal/regulatory statement against current primary sources for each target market.
4. Add the real publisher identity and a monitored contact address.
5. Update privacy/cookie wording to match the actual analytics, tracking, affiliate links, and vendors in use.
6. Review affiliate program rules, allowed geographies, marketing restrictions, and required disclosures.
7. Keep the temporary `robots.txt` disallow rule until the launch review is complete.
8. Confirm the chosen hosting plan permits commercial affiliate use. Vercel Hobby is restricted to personal/non-commercial use, and Vercel explicitly includes affiliate-link sites whose primary purpose is affiliate linking in its commercial-use examples. If Vercel remains the host, plan for Pro before commercial deployment; alternatively, choose a host whose current terms allow the intended business model.

## Hosting decision
- Do not deploy the monetized affiliate publication to Vercel Hobby. The official policy says Hobby is personal/non-commercial; see https://vercel.com/docs/limits/fair-use-guidelines#commercial-usage.
- No host has been selected or connected yet. Keep deployment paused until the commercial-use plan and recurring cost are approved.

## Quality checks
- Check every new page for a unique title/description, one clear H1, mobile layout, keyboard operation, and working internal links.
- Tools run in the browser only. The shared stylesheet uses system fonts and makes no third-party font request. Do not add analytics, cookies, affiliate tracking, remote fonts, or third-party scripts without updating the privacy notice and checking applicable consent requirements.
- The terms checklist is a personal review aid, not legal advice or a substitute for regulator records or the operator’s full terms.

## Business model and directory strategy

The intended commercial sequence is **audience first, paid listings second, affiliate revenue later**. Do not present listing fees as available or charge brands until the site has measurable traffic and a documented media kit. The initial research target is 100 casino brands, but a brand is not publishable merely because its name is on a prospect list.

### Staged plan
1. **Before domain purchase:** resolve the BEIN trademark/name risk and choose the initial target market(s). Do not buy a domain until the name is cleared.
2. **Build the 100-brand prospect list:** record the brand, exact operating/legal entity, official website, regulator/register evidence, permitted territories, source URLs, date checked, contact route, and research status. Unknown fields stay marked unknown; never infer licence status.
3. **Publish verified profiles only:** each profile needs unique useful content, market-specific caveats, clear update dates, official source links, and an editorial review. Avoid 100 thin or near-duplicate pages. Keep unverified prospects out of the public sitemap.
4. **First six months:** focus on genuinely useful guides, tools, technical SEO, indexation, and audience measurement. No promise of traffic or revenue; use the first six months as a review period, not a guarantee.
5. **Paid listings after evidence of audience:** prepare a transparent media kit from real Search Console/analytics data. Clearly label paid placements as sponsored/paid listings; payment must not buy a licence claim, safety verdict, editorial rating, or undisclosed ranking advantage.
6. **Affiliate links later and secondary:** only add after the listing model and disclosure workflow are ready. Verify each affiliate program's rules, allowed markets, tracking, and legal requirements. Clearly disclose affiliate links near them and update the privacy notice for any tracking.

### Minimum profile review fields
- Brand name and official domain checked against the brand's own site.
- Legal operating entity and regulator record independently checked where applicable.
- Exact jurisdiction/product scope and whether the audience market is permitted.
- Terms/withdrawal/complaints information and official source links.
- Last checked date, reviewer, evidence notes, unresolved questions.
- Commercial relationship: none / paid listing / affiliate / both, disclosed on the profile.

See docs/listing-fee-business-model.md for the commercial plan, docs/brand-prospect-list.md for the initial 100-name research queue, and docs/brand-research-template.csv for the row-by-row tracker. The prospect list is not a recommendation or licensing verification. Use docs/brand-profile-template.md before publishing any profile and docs/paid-listing-media-kit-template.md only after real audience data exists.

## Content policy
No invented ratings, bonus offers, licensing claims, or claims of independent testing. Any future commercial recommendation must be verified, dated, market-specific, and clearly disclosed.
