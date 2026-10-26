# Affiliate go-live runbook

Everything is built but **nothing is active**. A link goes live only when you set it to active in
`data/affiliate-links.json` and every gate passes. This is internal; `docs/` is not published.

## One-time steps (before the first link)
1. Update `privacy/index.html` only if you add analytics, pixels or cookies of your own. The `/go/` redirect itself adds none.
2. In `data/affiliate-links.json` set `"privacy_updated": true` once the privacy notice matches what you actually run.
3. Resolve the brand/trademark point in README "Launch blockers" (BEIN). Affiliate networks may ask for it.
4. Cloudflare Pages: confirm `_redirects` is deployed (a `302` to an external URL is supported) and test one `/go/` link end to end.

## Per operator (repeat for each programme)
1. Join the operator's **official** affiliate programme (or its network) and read the terms: allowed countries, bonus/wording rules, whether review sites are accepted.
2. Copy your tracking URL from the programme dashboard. Use the official `https://` URL only.
3. Edit that operator's entry:
   - `affiliate_url`: your tracking URL
   - `programme`: programme or network name
   - `programme_terms_checked`: today's date (`YYYY-MM-DD`)
   - `geo_confirmed`: `true` only if the programme accepts traffic for the review's market
   - `licence_verified`: `true` only after checking the regulator register
   - `licence_line` (optional): one factual line, e.g. `UKGC account 55149`
   - `active`: `true`
4. Flagged markets (`blocked_markets`: IT, BE, FR, AU, ES, SE) refuse to activate until you add `legal_review_ref` (who advised, when). These are cautions, not legal conclusions: check them.
5. Run:
   ```
   python3 scripts/affiliate_links.py apply
   python3 scripts/affiliate_links.py check
   python3 scripts/check_site.py
   ```
   `apply` adds a labelled "Sponsored link" button and disclosure to that review, writes `/go/<slug>` into `_redirects`, and switches the wording on `/affiliate-disclosure/` and `/privacy/`.
6. Commit and push; CI runs the same `check`.

## To switch a link off
Set `"active": false`, run `apply`. The button, disclosure and redirect are removed.
Note: on first activation the script deletes the old sentence "No brand-specific paid placement or affiliate relationship is asserted" from that page (it would contradict the disclosure). Use git history if you need it back.

## What the gates enforce
- `rel="sponsored nofollow noopener"` on every `/go/` link; raw tracking URLs never appear in page HTML.
- Disclosure paragraph and an 18+ / safer-gambling line on every page with a link.
- `/go/` is disallowed in `robots.txt`.

## Content gaps worth fixing before traffic (separate from the plumbing)
- 67 of 100 reviews cover Spain, which is outside the README's Tier 1 list (AU, US, FR, DE, CH, GB, NL).
- No "best casinos in <market>" comparison page yet, and no review is hands-on tested or rated.
- Operator logos are hotlinked from Wikimedia and operator domains; host them locally (programme media kits).
- Affiliate-programme approval often needs the brand/trademark point settled and a mailbox on the domain.
