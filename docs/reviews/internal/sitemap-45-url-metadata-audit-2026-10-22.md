# Sitemap 45-URL metadata audit — 22 October 2026

**Method:** Read-only fetch of all 45 URLs exposed by the live XML sitemap using a browser extraction service. Compared requested URL, final URL, page title, meta description and extracted canonical. This is not a raw HTTP status-code crawler, a Googlebot render test, or an indexing report.

## Results
- Sitemap URLs listed: **45**
- Pages successfully fetched and extracted: **45/45**
- Final URL changed from requested URL: **0**
- Extracted canonical missing or different from requested URL: **0**
- Missing page title in extraction: **0**
- Missing meta description in extraction: **0**
- Fetch errors returned by the extraction service: **0**

All 45 sitemap entries returned page content, a title, a description and a self-referencing canonical matching the requested URL in this run. This is a positive metadata consistency check; it does not independently prove HTTP status codes, Googlebot access, structured-data validity, mobile usability, indexation or ranking.

## Out-of-sitemap internal links observed
- Cloudflare email-obfuscation endpoint `/cdn-cgi/l/email-protection` was extracted from the affiliate disclosure and contact pages. This appears to be Cloudflare's email-protection mechanism, not a content URL that should be added to the sitemap. Confirm the email display/contact path in a real browser if it is reported broken.
- Two guide pages link to `/guides` without a trailing slash. The sitemap uses `/guides/`; check whether the host consistently redirects the slashless path to the canonical route. This was not classified as a confirmed broken link because the extraction did not expose the HTTP redirect/status chain.

## Important limitations
1. This extraction service returned page content but did not provide raw HTTP status codes or redirect chains; do not describe this as a verified 200-status crawl.
2. It does not replace Google Search Console's URL Inspection or Page Indexing reports.
3. It does not test JavaScript behavior, form submissions, keyboard navigation, contrast, screen readers, or small-screen layouts.
4. Sitemap presence and canonical consistency are not proof that Google has indexed the pages.
5. The current sitemap has no public casino profiles; the review directory explicitly says that no profiles are scored or ranked.

## Next steps
- Check slashless `/guides` redirect behavior and verify the email link/contact details in an ordinary browser.
- Test the wagering calculator and terms checklist with empty, zero, negative, non-numeric and large inputs, plus keyboard and mobile use.
- Use Search Console URL Inspection for representative URLs and the Page Indexing report for actual Google status.
- Keep the release gate: do not publish brand rankings until market-specific legal entity, domain, product licence, current terms, payments, complaints, safer-gambling and enforcement evidence are complete.

## URLs audited
The complete 45-entry list is the live sitemap at https://beincasinos.online/sitemap.xml (observed 22 October 2026).
