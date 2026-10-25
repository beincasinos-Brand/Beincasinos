# BeInCasinos visual asset and review-card system

Goal: a polished comparison experience, not a generic blog. This file is an implementation/editorial specification; it does not itself change the live site.

## Design principles

- Strong BeInCasinos/BIC identity; restrained dark ink, warm metallic accent and accessible neutral surfaces.
- Cards align on a consistent grid: brand/title, market badge, verified operator, score breakdown link, offer status, concise pros/cons and transparent CTA.
- Make the score and its rationale more prominent than promotional copy. Never let a bonus overwhelm eligibility or risk information.
- Use consistent spacing, readable type, clear focus states and mobile-first stacking. No tiny legal text, deceptive urgency or misleading button hierarchy.
- Separate organic editorial ranking from paid placement. Paid cards require a visible “Sponsored” or “Paid placement” label and cannot masquerade as independently ranked reviews.

## Image rights and asset status

Each image must have an asset record containing:
- asset filename/URL and brand it depicts;
- source URL and date retrieved;
- creator/rightsholder where known;
- licence or written permission and allowed commercial uses;
- required attribution, if any;
- market/brand match check;
- alt text and compression/format status.

Do not copy casino.org or other competitors' screenshots, layouts as image files, logos, promotional banners or review-card artwork. Brand logos and screenshots are not automatically free to reuse. If permission/licence is unclear, leave the image out and use a text-led card with a designed neutral placeholder.

## Alt-text rules

- Describe the image's meaningful content, e.g. “BeInCasinos comparison card for [brand], [market]” only if the image actually shows that card.
- Do not stuff bonus keywords, repeat the same alt text for decorative elements or imply endorsement.
- Decorative images should have empty alt text in the HTML implementation.

## Required card data contract

- canonical brand ID and canonical review URL;
- market code and eligibility status;
- operator and regulator source;
- review status (candidate, researching, hold, review-ready, approved, published);
- score plus dated category breakdown, or “Not yet rated”;
- current bonus evidence/status or “No current offer verified”;
- payment source/status;
- responsible-gambling/complaint source;
- image rights status;
- affiliate disclosure and commercial status;
- last evidence check and independent editor approval.

## Quality gates before card is public

1. No placeholder scores, guessed bonus amounts or fake star ratings.
2. No broken links, distorted logos, unlicensed artwork or low-resolution stretched images.
3. Card text remains understandable at phone width and at 200% zoom.
4. Market, licence and offer status are not communicated by colour alone.
5. Screen-reader label and keyboard focus are present on interactive controls.
6. Affiliate disclosure is visible before or alongside the relevant click.
7. A card is excluded from public recommendation lists until its market evidence and editorial approval are complete.
