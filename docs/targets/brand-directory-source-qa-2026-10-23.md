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
| Logo/image candidates | 28 |
| Candidate images with alt text | 28/28 |
| Candidate images with explicit width/height | 28/28 |
| Candidate images with lazy loading | 28/28 |
| Duplicate HTML IDs | 0 |
| New-tab links missing `noopener noreferrer` | 0 |

## Visual asset status

- 28/100 cards have a sourced image candidate; all remain **rights pending**.
- 72/100 cards use CSS-generated editorial artwork and monograms, not official logos or photographs.
- BigBangBet has no image URL because its official-site fetch failed; no URL was guessed.
- The directory hero now accurately states 100 research entries, 28 sourced image candidates with rights pending, and 72 editorial card artworks.

## Publication and deployment gates

- The directory remains `noindex,follow` and excluded from the sitemap while brand-level checks remain incomplete.
- The 100 cards are research queue entries, not 100 approved consumer reviews. Publication approval remains 0/100.
- No GitHub Actions run was triggered. No Cloudflare production deployment is confirmed.
- Before publication, verify exact local domain/operator/casino authorisation, current terms and safer-gambling information, complaints/enforcement scope, image reuse rights, and independent editorial sign-off.


## Brand-list scope correction — 23 October 2026

The 100-card list no longer includes the excluded planned Maine placeholder `Caesars online casino brands`. It now includes `Horseshoe Online Casino (Michigan)`, sourced to the Michigan Gaming Control Board's authorized-platform list and exact Michigan casino URL. It remains HOLD, with exact contracting entity, current terms, payment/withdrawal, complaints, safer-gambling and enforcement checks outstanding. This change does not alter the 25-image-candidate count.


## Official-site image follow-up — 23 October 2026

Three candidates were added after official-site extraction: ThreeSix Vegas (source site `36vegascasinos.uk`; confirm its relationship to the listed `36vegas.co.uk` domain), Midnite (`logo-emblem-2025.svg`), and Winz.nl (favicon candidate only, not a full-size logo). The current total is 28 sourced image candidates, all rights pending; 75 cards retain CSS-generated editorial artwork. This source-level count does not establish permission to reuse the assets.


## Visible content enhancement — 23 October 2026

Added a visible **Research snapshot** to each of the 100 cards, drawn from that card's existing research-context paragraph, so key evidence/limitations are not hidden entirely inside the expandable panel. This is an editorial presentation enhancement, not new verification. Ten snapshots remain intentionally short because the underlying evidence is only a preliminary lead; they should stay marked as research leads rather than be padded with unsupported claims.

Post-change source audit: 100 cards, 100 unique names, 100 visible snapshots, 100 context panels, 25 image candidates with alt text/dimensions/lazy loading, 25 rights-pending labels, no duplicate IDs, no unsafe new-tab links. Page remains `noindex,follow`.


## Additional favicon candidates — 23 October 2026

Three official-page metadata favicon URLs were added for 888.nl, BetTOM and 44Aces. These are **small-icon candidates**, not full-size logos, and all remain rights pending. BetTOM's fetched page was the sportsbook route, so its casino-product/market association still needs confirmation. Current total: 28 sourced image candidates; 72 cards retain editorial CSS artwork. The 100 visible research snapshots remain based on existing research-context text, not a claim of new verification.
