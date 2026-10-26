# Brand artwork, score and bonus release gate — 26 October 2026

This checklist applies to every casino review route and every homepage/ directory card.

## Official brand artwork
- Use a logo or wordmark taken from the operator's own site, verified media kit, or a source that explicitly grants reuse.
- Record the source page, direct asset URL or repository asset path, retrieval date, market/domain checked, and any permission/terms note.
- Do not create a fake official logo from initials, recolour a logo to imply endorsement, or reuse a generic casino illustration as the brand image.
- Store a local copy when permitted; give the file a brand-specific path such as `assets/brands/<brand-slug>-logo.svg` or `.webp`.
- Use descriptive alt text (for example, `bet365 logo`) only when the image is genuinely that brand's logo. If an asset cannot be verified, show the brand name as text and keep the logo marked pending.
- Never hotlink a guessed asset URL. Test the image response, file type, dimensions, and mobile crop before release.
- A brand logo is a trademark; editorial identification is not a claim of partnership or operator approval. Do not state that every operator has explicitly approved our use unless written permission exists.

## Images and duplicate prevention
- Each brand page must have a brand-matched logo/wordmark asset and a distinct relevant hero/illustration, or a deliberate text-only layout while assets are pending.
- A generic stock image may not be presented as an operator logo.
- Run `python scripts/review_visual_asset_audit.py --root . --json /tmp/review-visual-audit.json --csv /tmp/review-visual-audit.csv` before release.
- Resolve repeated generic artwork and missing image alt text. Human-review every flagged image: filename heuristics cannot prove authenticity or rights.
- Check cards at 360px, 390px, 768px, and desktop widths. No cropped logo, overlapping brand name, broken image, or misdirected review link may remain.

## Ratings and scores
The site's existing six-factor method weights terms clarity 25%, withdrawals/payment transparency 20%, safer-gambling controls 20%, complaints/support 15%, operator/licence transparency 10%, and usability/accessibility 10%. Each criterion is scored 0–5 from recorded evidence; weighted points are (criterion rating / 5) × weight.

Do not publish a numeric total unless all market/operator/domain/product eligibility gates pass and all six criteria have evidence-backed ratings. A missing criterion is **not assessed**, not zero. Do not claim hands-on testing unless the test was actually performed and documented. Keep the public status as **Not rated — evidence incomplete** until the gate passes.

## Current bonus and review copy
- Capture the exact operator offer URL, offer headline, currency, minimum deposit, wagering requirements, eligible games, expiry, maximum cashout, and eligibility exclusions where stated.
- Record the check date and quote or link the operator's own terms. Re-check time-limited promotions before release.
- If no current offer can be verified, write **No current offer verified** rather than inventing an amount.
- Each description must match the named operator and exact market. Avoid copy/paste boilerplate that implies features or licence coverage not established by evidence.
- Include a source list, editorial disclosure, safer-gambling information, update date, and clear limitations on each page.

## Release checklist
- [ ] Official logo asset and source/rights record confirmed for each brand.
- [ ] No repeated generic artwork masquerading as a brand image.
- [ ] All image alt text checked and mobile crop inspected.
- [ ] Six score criteria supported by dated evidence, or score withheld.
- [ ] Current bonus terms confirmed, or explicitly marked unverified.
- [ ] Description and market/legal claims checked against primary sources.
- [ ] Human review approval recorded; only then consider merge/deploy/indexing.
