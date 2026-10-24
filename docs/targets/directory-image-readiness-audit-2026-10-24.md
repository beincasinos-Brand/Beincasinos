# Directory image and asset readiness audit — 24 October 2026

**Branch:** `feature/directory-global-brand-count-disclosure-2026-10-23`  
**Scope:** Static audit of `docs/targets/brand-image-asset-register-2026-10-23.csv` and targeted official-page image discovery. This checks source metadata and register consistency only; it does not fetch every image file, validate pixel rendering, establish trademark rights, or approve public reuse.

## Current register results

- Asset register: **100 brand-market rows**.
- Remote image candidates: **63** (63%).
- No remote image URL / intended CSS artwork or monogram fallback: **37** (37%).
- Rows with explicit alt text: **100/100**.
- Sourced rows missing a source-page URL: **0**.
- Sourced rows without a rights/permission note: **0**.
- Asset status: **63 SOURCE FOUND — RIGHTS PENDING**; **37 NOT SOURCED**.

## Targeted official-page discovery — 24 October 2026

Fetched ten candidate official-site pages for brands that previously had no image URL in the register. Four candidates were initially assessed; after direct-asset checks, three remain recorded:

- **Los Vegas:** the official page metadata exposed a 128px favicon, but the direct asset check returned **404**. The stale URL was removed from the directory and register; the card now uses its CSS-art fallback.
- **LottoGo Casino:** the official page exposed a default logo SVG, but redirected to a location-unavailable page from the check environment.
- **Alfobet:** the official homepage exposed its logo image. This is image-source evidence only; the existing UKGC record describes `lobby.alfobet.com` as a white-label domain, so the exact consumer-facing domain/operator match remains open.
- **Rollerbet:** the UK sports page exposed a favicon. This is a small-icon candidate; the fetched page does not prove the casino product/domain relationship.

The other checks returned a country-block page for Neptune Play or errors/blocking for Casino and Friends, BigBangBet, Betta Bet and PricedUp. A later 247Bet table-page fetch exposed favicon metadata, but no 247Bet asset was added to the register in this pass. Direct checks of the three remaining newly recorded assets returned empty content for the LottoGo and Alfobet binary files and 403 for the Rollerbet favicon; those results do not establish successful browser rendering. The register and directory now contain 63 candidate assets and 37 CSS fallbacks; all 63 remain rights-pending.

## Interpretation

Finding a logo or favicon on an official site establishes a discovery lead, not permission to republish it. A public page being reachable does not prove that the casino product is authorised in the listed market. Small favicons are not automatically suitable for full-size presentation. Keep each brand on HOLD until its exact domain, operator and local casino-product permission are independently confirmed.

The 37 NOT SOURCED rows should retain original CSS artwork or monogram fallbacks. Do not guess asset URLs or substitute unrelated images. Remote candidates should only be activated in a public release after identity, direct rendering, responsive crop, accessible alternative text and a defensible reuse basis have been reviewed.

## Required next pass

1. Test all 63 candidate assets for response, content type, dimensions, redirects and hotlink behaviour.
2. Review the source page and asset identity together; flag stale, ambiguous, distorted or market-mismatched images.
3. Record a defensible rights basis per asset (explicit permission/licence, documented public-domain basis with trademark caveat, or replacement with original artwork).
4. Keep the no-image fallback for unresolved cases and verify alt text against the actual asset.
5. Run responsive visual review and accessibility checks before any indexing or production release.

**Status: OPEN / HOLD.** The directory has 100 cards, but image-source presence is not image-rights clearance or evidence of 100 eligible distinct global brands.
