# AdSense readiness audit — 2026-10-31

## Policy reality (Google AdSense)
- Online casinos, bookmakers and "aggregator or affiliate sites that promote online gambling pages" are **restricted content**: limited ad demand, Google Ads will not serve on it. The restriction is lifted for users in listed countries (incl. US, UK, Germany, Canada, Australia).
- Educational gambling content (guides) can carry unrestricted ads. Approval is not guaranteed; expect low RPM on review pages.
- EEA/UK (since 16 Jan 2024) and Switzerland (since 31 Jul 2024) need a Google-certified TCF CMP for personalised ads.

## Passed
- Trust pages exist: about, contact, privacy, terms, editorial policy, affiliate disclosure, responsible gambling, how we review.
- Sitemap: 98 URLs, none noindex, none missing. No broken internal links. No duplicate titles. Thin-content placeholders (71 draft reviews) are noindex and out of the sitemap.
- No trackers/ad scripts today; privacy notice says so and promises an update before any are added.
- CSP is strict (`script-src 'self'`, `frame-src 'none'`) — must be relaxed only when ads go live.

## Fixed now
- About and Editorial policy no longer claim "no casino profiles are scored".

## Open before applying
1. Add a Google-certified CMP (TCF) + update privacy notice (ads, cookies, Google as vendor) and CSP.
2. Create `ads.txt` with the publisher ID Google gives at signup (not created now — no fake ID).
3. Grow thin pages: contact (~170 words), 14 guides under 300 words of main text.
4. Fill remaining reviews (2/29 scored, bonuses 1 verified) — needs UK/NL/DE/CH/US-IP evidence runs.
5. Domain age/traffic: AdSense reviewers prefer a site with real original content and some visitors; reapplying after rejection is allowed.

## Recommendation
Apply after items 1–3 and once guides are the visible bulk of indexable content; do not rely on ad revenue from review pages. Keep `data/affiliate-links.json` all `active=false` until traffic exists (see `docs/affiliate-go-live-runbook.md`).

## Phone-friendly go-live steps
1. On adsense.google.com sign in, choose "Add site" -> beincasinos.online.
2. Copy the publisher ID (looks like `ca-pub-1234567890123456`) and send it to Claude.
3. Claude runs `python3 scripts/enable_adsense.py <ID>` (meta tag + ads.txt), pushes, you press "Verify" in AdSense.
4. After approval: AdSense -> Privacy & messaging -> create the free EU/UK/CH consent message (Google-certified CMP), then Claude adds the ad script, CSP change and privacy update.
