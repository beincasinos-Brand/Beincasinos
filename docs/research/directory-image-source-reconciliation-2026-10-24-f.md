# Directory image-source reconciliation — batch F

**Checked:** 24 October 2026  
**Scope:** Three additional logo candidates for existing Great Britain directory cards.  
**Publication status:** SOURCE FOUND — RIGHTS PENDING. These URLs are candidates discovered on the relevant official website or its page metadata; this does not grant permission to republish a trademark or image.

## Betmaster UK

- **Card:** Betmaster; UK-only domain and operator scope retained.
- **Official source page:** https://betmaster.co.uk/en
- **Image candidate:** https://src.bmstatic.cloud/betmaster_uk/assets/images/logo-large.brand-B785eDud-609.svg
- **Discovery:** Extracted from image URLs served by the official UK website.
- **Editorial limit:** Do not conflate the UK entity/domain with international Betmaster. Official-site statements about fast payments, safety or user experience are marketing claims, not independent test results.
- **Rights / QA:** Reuse permission unconfirmed; direct image rendering and visual crop should be checked before production.

## DynoBet

- **Card:** DynoBet; existing UKGC white-label caveat retained.
- **Official source page:** https://www.dynobet.com/
- **Image candidate:** https://data.progressplay.net/content/general/labels/dynobet/dynobet.webp
- **Discovery:** The official site page returned this brand image. Existing research associates dynobet.com with a UKGC white-label record under ProgressPlay Limited; this image does not independently prove the customer-contracting entity or a standalone operator.
- **Rights / QA:** Reuse permission unconfirmed; test image load and exact brand matching before production.

## BetGoodwin Casino

- **Card:** BetGoodwin Casino; UKGC operator/domain/trading-name evidence is already recorded, while the casino journey and launch timing still need direct checks.
- **Official source page:** https://www.betgoodwin.co.uk/en/sport/
- **Image candidate:** https://storage.googleapis.com/stateless-em-ndw/2024/09/89b62c98-betgoodwinlogonew.svg
- **Discovery:** Returned in the official page's Open Graph metadata. The fetched landing page is a sports page; the image source alone is not proof of casino-specific scope or review completion.
- **Rights / QA:** Reuse permission unconfirmed; direct render and image rights must be checked.

## Directory implementation and QA

- Added all three candidates to `brand-directory/index.html` using the existing image-card component.
- Each card has an explicit alt text, lazy loading, asynchronous decoding, a fallback monogram and a visible “OFFICIAL ASSET · RIGHTS PENDING” label.
- Added three corresponding rows to `docs/targets/brand-image-asset-register-2026-10-23.csv`.
- Post-edit static check: 100 brand cards; 59 image elements; all 59 have `loading="lazy"`, all 59 have `onerror` fallback handling, and no image is missing alt text.
- The directory still contains 100 research entries, not 100 independently verified global brands. The image candidates are not rights-cleared, and the publication-approved consumer review count remains 0/100.

## Sources

- Betmaster UK official site: https://betmaster.co.uk/en
- DynoBet official site: https://www.dynobet.com/
- BetGoodwin official site: https://www.betgoodwin.co.uk/en/sport/
