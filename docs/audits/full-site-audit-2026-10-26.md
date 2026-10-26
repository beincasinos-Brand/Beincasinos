# BeInCasinos full-site audit — 26 October 2026

## Scope and evidence
- Live homepage: https://beincasinos.online/
- Live review directory: https://beincasinos.online/reviews/
- Competitor methodology reviewed: Casino.org /reviews and /how-we-rate, plus TheCasinoReviews editorial policy and Gambling.com review methodology.
- Repository reviewed: beincasinos-Brand/Beincasinos, current `main` sources for `index.html`, `reviews/index.html`, `styles.css`, `script.js`, and `assets/reviews-directory.css`.

## Confirmed observations
1. Homepage currently positions itself as evidence-led casino research and displays five featured desk-research profiles. It correctly says they are not product-tested and does not publish invented numeric scores.
2. Reviews directory advertises 100 market research profiles, but cards are marked NOT RATED and often show pending evidence / bonus not verified. Candidate count must not be described as 100 finished, scored, or independently tested reviews.
3. Directory cards share a generic art asset with brand-colored CSS/monogram treatment. That is a fallback, not a distinct official brand image. Use official logo assets only when their source and use are appropriate; otherwise keep a branded monogram/wordmark fallback.
4. Editorial methodology is already a useful foundation: weighted criteria, eligibility gate, market scope, source checks, limitations and commercial independence.
5. Live HTML confirms the main navigation and footer links exist. Automated source inspection cannot prove every tap target, theme contrast, or viewport behavior works in a real browser; those still need preview/device QA.
6. Prior PR metadata reports the site-wide dark-mode/responsive batch (#263) and custom-page theme follow-up (#264). Confirm their merge/deploy state and verify the actual production behavior before treating all fixes as complete.

## Competitor practices worth adopting (without copying)
- Show concise comparison cards with clear identity, market scope, evidence status, important terms and a direct full-review link.
- Publish a transparent methodology and visible affiliate/commercial disclosure.
- Separate regulatory eligibility from a score; never let a high score override failed legal/market checks.
- Distinguish published terms from hands-on testing; do not claim deposit, support or withdrawal tests that were not performed.
- Date material claims and corrections, and prioritize primary regulator/operator sources over competitor summaries.
- Use unique, rights-cleared brand images where possible; never rely on repeated stock artwork as a substitute for brand identity.

## Changes in this branch
- Strengthened responsive navigation/control layout and mobile tap target sizing.
- Added visible keyboard focus states for navigation, controls, cards/links and footer links.
- Improved long-word wrapping and overflow behavior for review-card content, tables and code.
- Added narrow-screen layout refinements for review metrics, footer columns and page gutters.
- Added reduced-motion handling and bounded language-menu dimensions.

## Remaining release blockers
- Verify current state of PRs #263 and #264; avoid duplicate changes if already merged.
- Run repository checks and a real Cloudflare Pages preview/browser pass at 320px, 375px, 768px, 1024px and desktop widths; test keyboard, menu open/close, theme persistence, contrast and broken image fallbacks.
- Test each sitemap URL for status, redirect chain, canonical consistency, unique title/H1 and meaningful content; compare live Search Console redirect-error examples against actual redirect rules.
- Fix page-specific copy/graphics overflow found in the user's latest screenshots, especially Guides and Partners.
- Review language selector wording: only English is live; other languages must remain visibly unavailable until translated pages exist.
- Check contact page and Zoho-backed `contact@beincasinos.online` flow end-to-end without exposing private credentials.
- For the 100-brand milestone, candidate records and research dossiers are not completed reviews. Keep each candidate on HOLD until exact domain/operator, jurisdiction/product eligibility, current terms, payment/withdrawal rules, safer-gambling information, complaints, image rights and independent review are complete.
- Do not fabricate ratings, bonuses, logo rights, player testing, withdrawal speeds or indexing outcomes.

## Release note
This branch is a proposed code change, not proof of a successful production deployment. Do not trigger extra GitHub Actions runs solely for appearance; use existing CI status and a single preview/release verification pass.
