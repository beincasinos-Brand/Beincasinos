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

## Content policy
No invented ratings, bonus offers, licensing claims, or claims of independent testing. Any future commercial recommendation must be verified, dated, market-specific, and clearly disclosed.
