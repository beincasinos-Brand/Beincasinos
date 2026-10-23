# Official image candidate QA — 23 October 2026

**Branch:** `ops/tier1-10-market-100-brand-roadmap-2026-10-22`  
**Directory:** `brand-directory/index.html`  
**Register:** `docs/targets/brand-image-asset-register-2026-10-23.csv`

## Current inventory

The latest branch-source count is **45 image candidates across 100 cards**. Every candidate is visibly marked **SOURCE FOUND · RIGHTS PENDING** and has alt text, width/height hints, lazy loading and a monogram fallback. The register contains 100 brand rows, 45 with a sourced candidate. The remaining 55 cards use CSS artwork/monograms, not official logos or photographs.

**Important:** a logo or favicon being exposed on a brand's website does not establish permission to republish it. This audit does not certify that every URL still loads, that every asset is visually correct at display size, or that each brand is licensed in the directory's named market.

## Original spot-check retained as historical QA

The initial 20-candidate source spot-check found 18 image candidates exposed on official brand pages; two page fetches timed out (Admiral Switzerland and Betinia NJ). This initial sample is not the current 43-candidate inventory and was not a rights review.

## Notable caveats from later candidate batches

- **ThreeSix Vegas:** the image source is `36vegascasinos.uk`, while the directory entry lists `36vegas.co.uk`. Verify the relationship between domains and operator before treating it as the same brand's logo.
- **Winz.nl, 888.nl, BetTOM, 44Aces, Kansino, FairPlay Casino and Lottoland UK:** several candidates are favicons/small icons, not full-size wordmarks; assess visual quality and suitability before publication.
- **Midnite:** the sourced file is an emblem, not necessarily a full wordmark.
- **Tonybet:** the official page was country-blocked; the asset candidate does not establish Dutch availability or authorisation.
- **Fanatics Casino (US-NJ):** the candidate comes from the official Fanatics Sports & Casino homepage. The exact New Jersey authorised product/domain relationship remains unconfirmed.
- **BestOdds:** this is a betting-information site; its image does not establish that it is itself an online casino operator.
- **Brillbet:** the fetched official URL redirected to a customer-service notice; current consumer-product availability remains unresolved and the card stays on HOLD.
- **Hard Rock Bet:** the logo source does not establish Michigan availability or licensing.
- **BigBangBet:** the official-site fetch returned an invalid URL; no asset path was guessed.
- **Tipico Casino:** official casino page returned HTTP 403. **247Bet:** extraction returned `content_too_large`. **Casino and Friends:** bot-blocked. **Neptune Play:** redirected to a blocked-country page. No asset URLs were guessed for these failed fetches.

## Publication controls

- All 45 candidates remain rights pending.
- The directory remains `noindex,follow` and is excluded from the sitemap until domain/operator, local licence, content and image-rights checks are complete.
- **0/100 reviews are approved.** Image sourcing does not approve a review or change a brand's HOLD status.
- No Cloudflare production deployment is confirmed, and no GitHub Actions run was triggered for this work.
- Before publication, verify the direct asset URL, exact visual identity, current official source, permitted reuse terms, alt text and fallback behaviour. Prefer written permission or appropriately licensed assets where required.


### Additional image candidates — 23 October 2026

- **BetWright:** official homepage header exposed `https://betwright.cdn.prismic.io/betwright/Z-h0LndAxsiBwFaT_logo.svg`. Its card now records the official-site candidate URL, but exact current UKGC domain/trading-name match and casino permission remain pending.
- **Kong Casino:** official homepage exposed `https://www.kongcasino.com/themes/default/logo.png`. The card remains HOLD until the exact domain and current UKGC remote-casino permission are confirmed.

Both assets are visibly marked rights pending; source-page presence is not reuse permission.


## Authoritative current directory state — 23 October 2026

Latest branch-source audit: **100 unique brand cards, 100 visible research snapshots, 45 sourced image candidates, 45 rights-pending labels and 55 CSS artwork/monogram fallbacks**. The image register has 100 rows, 45 with sourced candidates. All image tags have alt text, dimensions, lazy loading and fallback handling. The official-domain field is populated on 48/100 cards; the legal-operator field is populated on 46/100 cards. These are field-coverage counts, not licensing approvals. Evidence grades: A 44, B 7, C 49; statuses: 99 HOLD, 1 EXCLUDE. Review approval remains 0/100. The page is noindex, PR #36 is open/draft/unmerged and not mergeable, and no Cloudflare production deployment is confirmed. Historical counts above describe earlier batch checkpoints only.
