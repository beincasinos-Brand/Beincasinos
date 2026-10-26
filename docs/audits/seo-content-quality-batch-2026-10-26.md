# BeInCasinos SEO + content quality batch — 26 October 2026

## Findings from source inspection
- `sitemap.xml` contains 148 unique absolute HTTPS URLs on the preferred `https://beincasinos.online` host. The source file is parseable by a simple URL-entry scan and contains no duplicate `loc` values.
- Several sitemap entries have no `lastmod`; this is not inherently an error. Do not fill dates unless the corresponding page had a significant, verifiable update.
- The reviews directory's SEO title, Open Graph title, Twitter title, and JSON-LD page name previously used “Casino Reviews Directory”, while the visible page calls the entries “market research profiles.” The title has now been aligned around “Casino Reviews & Market Research”.
- The directory's old meta description explicitly said “Browse 100 market research profiles”; the updated description now avoids making the count the main promise and explains that scores are published only when evidence supports them.
- The visible directory filter includes Belgium, British Columbia, Germany, Great Britain, Italy, Netherlands, Spain, Sweden, Switzerland, and Michigan. Australia and France are not represented in the current filter; do not imply all target markets are already covered.
- The visible page itself correctly distinguishes research profiles from scored reviews, and says numeric scores are withheld until current evidence and market eligibility checks are complete.

## Changes in this batch
1. Refined the review-directory description to be evidence-led rather than count-led.
2. Aligned HTML title, Open Graph title, Twitter title, and JSON-LD name.
3. Added a visible note that explains the research status, avoids implying every profile has been hands-on tested, and flags incomplete market-filter coverage.
4. Added light/dark styles for the evidence note and a small-screen layout rule.

## SEO guardrails
- Sitemap inclusion is a discovery hint, not proof of indexation or ranking.
- Keep sitemap URLs aligned with self-canonical URLs and actual preferred destinations. Google treats redirects and rel=canonical as stronger signals than sitemap inclusion; keep those signals consistent.
- Set `lastmod` only for significant changes that actually occurred; never update every URL's date just to look fresh.
- Use Search Console URL Inspection / live test on the actual examples listed as “Redirect error”, then fix the real redirect chain or destination. Do not guess a global redirect rule from the category name alone.
- Verify the response code, canonical target, indexability, title, H1, and useful unique content of each review URL before asking Google to recrawl it.
- Market eligibility is jurisdiction-specific; a listing's presence in a directory is not a claim that the operator is legal or available everywhere.

## Still requires production QA
- Test the actual preview build on 320px, 375px, 768px, 1024px and desktop widths.
- Verify review-search and market filters work with keyboard and screen readers.
- Run a real XML parser and HTTP status/redirect/canonical audit against every sitemap URL.
- Compare the sitemap list to the Search Console examples of redirect errors, soft 404s, duplicate canonical pages and discovered-not-indexed URLs.
- Confirm Australia and France coverage before claiming all target markets are live.
- Confirm deployed production output after PR merge; these source changes do not themselves deploy the site.
