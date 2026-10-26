# BeInCasinos image production batch — review cards

**State:** production specification; no third-party image rights claimed.

## Visual direction
Premium editorial casino-review identity, not a generic blog: charcoal/ink base, restrained champagne-gold accent, high-contrast white type, clean card grid, generous whitespace, compact factual metadata and visible “last checked” labels. Use a consistent 3:2 hero crop and square logo slot; never alter official logos or imply endorsement.

## Asset policy
1. Brand logos: use only official press assets with explicit terms or written editorial-use permission. Keep source URL, permission basis, date, allowed placements and expiration in the asset register.
2. Casino imagery: prefer original commissioned, brand-neutral editorial artwork. Do not scrape competitor images, copy another site's layout pixel-for-pixel, or use casino/provider images without permission.
3. Game thumbnails: show only games confirmed in the reviewed market and current catalogue; otherwise omit.
4. Offer artwork: do not bake bonus amounts, wagering terms, ratings or “verified” claims into images. Those facts must remain accessible as text and updateable.
5. Avoid decorative slot-machine imagery on pages where the product's legal status is on HOLD; use a neutral research/status visual instead.

## Image QA
- Use WebP/AVIF derivatives and responsive image sources.
- Set width/height or aspect ratio to reduce layout shift.
- Compress assets; lazy-load below the fold; load the lead image eagerly only when justified.
- Use meaningful alt text, no keyword stuffing, and empty alt for purely decorative artwork.
- Check mobile crop at narrow Android widths, contrast, keyboard focus and readable text outside images.
- No image goes live until rights are cleared and the asset register is updated.

## Suggested alt-text patterns
- Authorized brand mark: “Brand logo” only if it is truly the approved logo asset.
- Original editorial art: “Illustration for the brand casino review” if it accurately describes the image.
- UI screenshot: describe the exact screen and date only if captured lawfully by the reviewer.
- Decorative texture: empty alt attribute.

## Reusable review-card fields
Brand; market eligibility; legal status; score or NOT RATED; offer or “not verified”; last checked; image; primary CTA to full review; affiliate disclosure adjacent to commercial links. Never use green trust badges before legal and evidence checks pass.
