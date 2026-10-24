# Brand directory release QA snapshot — 24 October 2026

## Scope

Static source inspection of `brand-directory/index.html` on branch `feature/directory-global-brand-count-disclosure-2026-10-23`. This is a source-level check only; it does not fetch the live Cloudflare site, verify that images load, test links, or establish search indexing.

## Measured source counts

- Brand cards found: **100**
- Cards with `data-status="HOLD"`: **98**
- Cards with `data-status="EXCLUDE"`: **2**
- Cards with expandable details/checklist: **100**
- Image elements found inside cards: **60**
- Images with explicit `alt` attribute: **60/60**
- Images with remote HTTP(S) source: **60/60**
- Images whose alt text or nearby markup explicitly says reuse permission is not confirmed / rights pending: **59/60**
- External-link anchors in cards: **323** (anchors counted from source; destinations not fetched or tested)
- Robots meta in source: `index,follow`
- Sitemap entry in this branch: `https://beincasinos.online/brand-directory/`

## Release interpretation

The page states that these are 100 market-scoped research leads, not 100 verified distinct global brands or consumer recommendations. The 98 HOLD and 2 EXCLUDE statuses must not be converted into implied approval in structured data, titles, affiliate calls to action or social copy.

All 60 images are remote sources, which means the source check cannot establish that they will load reliably. Remote images are not proof of reuse rights. The markup explicitly labels 59 as pending/not confirmed; the remaining image also needs a documented rights record before reuse. Replace unlicensed images with neutral local CSS/typographic fallback art or record a valid permission/licence.

## Pre-release checks still required

1. Run an actual mobile/desktop browser check and keyboard-only filter test.
2. Test all official-domain links and verify each still matches the listed market and operator.
3. Check image HTTP status, layout shift, fallback behaviour and external hotlink restrictions.
4. Review canonical URL, robots policy, sitemap and Cloudflare production response after an approved release.
5. Decide whether the directory is useful enough to index; `index,follow` is a directive, not a guarantee of indexing.
6. Keep candidate identity, market eligibility, current terms, image rights and editorial approval separate in the tracker.

## Limitations

This snapshot describes only the HTML source in the named feature branch. It is not a live deployment report, automated Lighthouse result, image-rights audit, or Search Console/indexing report.
