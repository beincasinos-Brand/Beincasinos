# 100-brand directory source QA — 23 October 2026

**Branch:** `ops/tier1-10-market-100-brand-roadmap-2026-10-22`  
**File checked:** `brand-directory/index.html`  
**Purpose:** Static source audit only. This is not a live-browser test, regulator re-verification, legal sign-off, or proof of Cloudflare deployment.

## Current checks

| Check | Result |
|---|---:|
| Brand cards | 100 |
| Unique brand labels | 100 |
| Cards with legal-operator field | 100/100 |
| Cards with regulator/authority field | 100/100 |
| Cards with evidence-grade field | 100/100 |
| Cards with verification checklist | 100/100 |
| Cards with research-context panel | 100/100 |
| Visible source-backed research snapshots | 100/100 |
| Logo/image candidates | 34 |
| Candidate images with alt text | 34/34 |
| Candidate images with explicit width/height | 34/34 |
| Candidate images with lazy loading | 34/34 |
| Duplicate HTML IDs | 0 |
| New-tab links missing `noopener noreferrer` | 0 |

## Visual asset status

- 34/100 cards have a sourced image candidate; all remain **rights pending**.
- 66/100 cards use CSS-generated editorial artwork and monograms, not official logos or photographs.
- BigBangBet has no image URL because its official-site fetch failed; no URL was guessed.
- The directory hero now accurately states 100 research entries, 34 sourced image candidates with rights pending, and 66 CSS artwork/monogram fallbacks.

## Publication and deployment gates

- The directory remains `noindex,follow` and excluded from the sitemap while brand-level checks remain incomplete.
- The 100 cards are research queue entries, not 100 approved consumer reviews. Publication approval remains 0/100.
- No GitHub Actions run was triggered. No Cloudflare production deployment is confirmed.
- Before publication, verify exact local domain/operator/casino authorisation, current terms and safer-gambling information, complaints/enforcement scope, image reuse rights, and independent editorial sign-off.


## Brand-list scope correction — 23 October 2026

The 100-card list no longer includes the excluded planned Maine placeholder `Caesars online casino brands`. It now includes `Horseshoe Online Casino (Michigan)`, sourced to the Michigan Gaming Control Board's authorized-platform list and exact Michigan casino URL. It remains HOLD, with exact contracting entity, current terms, payment/withdrawal, complaints, safer-gambling and enforcement checks outstanding. This change does not alter the 25-image-candidate count.


## Official-site image follow-up — 23 October 2026

Three candidates were added after official-site extraction: ThreeSix Vegas (source site `36vegascasinos.uk`; confirm its relationship to the listed `36vegas.co.uk` domain), Midnite (`logo-emblem-2025.svg`), and Winz.nl (favicon candidate only, not a full-size logo). The current total is 33 sourced image candidates, all rights pending; 75 cards retain CSS-generated editorial artwork. This source-level count does not establish permission to reuse the assets.


## Visible content enhancement — 23 October 2026

Added a visible **Research snapshot** to each of the 100 cards, drawn from that card's existing research-context paragraph, so key evidence/limitations are not hidden entirely inside the expandable panel. This is an editorial presentation enhancement, not new verification. Ten snapshots remain intentionally short because the underlying evidence is only a preliminary lead; they should stay marked as research leads rather than be padded with unsupported claims.

Post-change source audit: 100 cards, 100 unique names, 100 visible snapshots, 100 context panels, 25 image candidates with alt text/dimensions/lazy loading, 25 rights-pending labels, no duplicate IDs, no unsafe new-tab links. Page remains `noindex,follow`.


## Additional favicon candidates — 23 October 2026

Three official-page metadata favicon URLs were added for 888.nl, BetTOM and 44Aces. These are **small-icon candidates**, not full-size logos, and all remain rights pending. BetTOM's fetched page was the sportsbook route, so its casino-product/market association still needs confirmation. Current total: 28 sourced image candidates; 72 cards retain editorial CSS artwork. The 100 visible research snapshots remain based on existing research-context text, not a claim of new verification.


## Latest image inventory reconciliation — 23 October 2026

After adding Brillbet's official-site `media/logo.png` candidate, the current branch contains **100 unique brand cards, 29 image candidates, and 100 visible research snapshots**. All 29 candidate images have alt text, explicit width/height and lazy loading, and each candidate is marked rights pending. Brillbet's official page redirected to a customer-service notice during inspection, so current product status must be checked before any recommendation. The directory remains `noindex,follow`; no Cloudflare production deployment is confirmed.


## Latest content-quality pass — 23 October 2026

A static audit after enriching ten previously thin snapshots found:

- **100/100** cards have visible research snapshots and 100/100 have expandable evidence-context panels.
- **0** visible snapshots are blank or shorter than 90 characters. The ten formerly terse leads now explain what is and is not verified and give a primary-source verification direction; no licence, live product, consumer test or positive recommendation was invented.
- **29/29** image candidates have alt text, width/height hints and lazy loading; all remain rights pending.
- **100** unique brand labels; no duplicate HTML IDs; no new-tab links missing `noopener noreferrer`.

This is source-level QA only. It does not confirm that every remote image loads in a real browser, that image reuse rights exist, that each licence is current, or that Cloudflare has deployed the branch.


## Starcasino image addition — 23 October 2026

Added a logo candidate exposed by Starcasino's official casino page: `https://images.ctfassets.net/yru0bhhzza0c/01H8BF5CMT8EY0RDSR845X5YEA/c4fff10c35356e63159f77c3d08e3833/Starcasino-Logo-2025-Vertical-White.png?fm=webp&w=256&q=75`. It is labelled rights pending. Current inventory: 30 image candidates and 70 cards using editorial CSS artwork. No reuse permission is inferred.


## Additional official image candidates — 23 October 2026

Added three further source-exposed assets: TOTO's logo SVG from `toto.nl`, Kansino's homepage favicon, and Stakewise's UK homepage favicon image. All three are registered with explicit alt text and remain **rights pending**; the latter two are small-icon candidates, not full-size logos. Current total: 34/100 sourced image candidates and 67 cards with CSS editorial artwork. Source-level HTML QA is not a live browser test, direct-asset uptime check, reuse licence, legal review, or deployment confirmation.


### Betty Casino image candidate — 23 October 2026

Added the official Betty Casino homepage favicon `https://playbetty.co.uk/favicon/android-icon-192x192.png`. This is a square icon candidate rather than a full-size wordmark and remains rights pending. The current inventory is 34/100 sourced candidates, with 66 cards retaining CSS-generated editorial artwork. Source presence is not permission to reuse.


### Final image inventory reconciliation — 23 October 2026

Current checked source state: 100 unique brand cards, 100 visible research snapshots, 100 verification checklists, 34 sourced image candidates and 34 matching rights-pending labels. The remaining 66 cards use CSS-generated editorial artwork/monograms. The asset register retains 100 brand rows. This is static source QA only; image candidates are not reuse-cleared, the page remains `noindex,follow`, and no production deployment is confirmed.


The directory's methodology section now explicitly separates image discovery from reuse rights: official-site presence does not grant permission, and each image candidate remains rights pending until identity, direct rendering and reuse permission are checked. The hero label now accurately describes the 66 remaining cards as CSS artwork/monogram fallbacks.
