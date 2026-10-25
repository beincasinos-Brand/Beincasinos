# Batch 98 — Review card image fallback and content integrity
**Purpose:** ensure review cards remain premium and complete when brand image rights or data are missing.

## Card fields
- Brand name from canonical inventory
- Verified product category
- Market eligibility status
- Evidence-backed rating only when rubric is complete
- Current offer only when official terms are checked
- Short factual summary based on evidence
- Image or neutral fallback
- Official terms link and affiliate disclosure where applicable
- Review/update date only if actually checked

## Fallback states
- **Image cleared:** use locally hosted asset with rights record and accurate alt text.
- **Image not cleared:** use a designed initials tile or generic editorial illustration; do not imply it's the brand's logo.
- **Rating pending:** display “Rating pending verification,” not a decorative number.
- **Offer pending:** display “Current offer not verified,” not “No deposit bonus” or a guessed amount.
- **Eligibility pending:** hide promotional CTA and mark the candidate as not yet publish-ready.

## Visual hierarchy
Use consistent spacing, legible contrast, mobile-first layout, clear product category, and a restrained rating treatment. Avoid fake award seals, invented trust badges, and urgency banners.

## QA
Check image loading, alt text, keyboard access, responsive card height, and that missing optional fields don't leave empty boxes or “undefined” text.
