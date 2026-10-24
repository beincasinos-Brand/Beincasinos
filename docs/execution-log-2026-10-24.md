# BeInCasinos execution log — 2026-10-24

This log records repository changes and evidence verified during this work session. It does not claim the public website has deployed or that Google Search Console has registered impressions.

## Repository changes made

1. Added `docs/switzerland-esbk-official-online-casino-shortlist-2026-10-24.md` (commit `c336e726e0b45b4dd66820ea7160c7ec83b3d33a`). It records the ten platforms on the Swiss Federal Gaming Board's official online-casino list, their listed URLs and online start dates. All ten remain **HOLD** for public reviews until company, terms, payments, complaints, safer-gambling and editorial checks are complete.
2. Added `docs/brand-profile-bet365-casino-gb.md` (commit `b37699f2fa52b247074a757bf319890895ff3cbe`). It records the Great Britain regulator's current bet365 gaming entity, active domain and Casino Remote permission, plus the dated 2024 regulatory settlement. It is an evidence dossier, not an approved public review.

## Verified primary-source findings

- ESBK's official list names ten Swiss online platforms: Jackpots.ch, mycasino, Swiss Casinos, Casino777, StarVegas, 7melons, PASINO.ch, Swiss4Win, Admiral and Casineo. The ESBK page says operators need a concession extension and approvals for individual games before online operation. Source: https://www.esbk.admin.ch/de/online-spielbanken
- The Great Britain Gambling Commission register identifies Hillside (UK Gaming) ENC, account 55149, lists bet365.com as active, and shows Casino Remote permission 055149-R-331499-004 as Active. Source: https://www.gamblingcommission.gov.uk/public-register/business/detail/55149
- The regulator's 4 April 2024 announcement says Hillside (UK Gaming) ENC agreed to pay £343,035 in lieu of a financial penalty following findings relating to anti-money-laundering and social-responsibility failures. Source: https://www.gamblingcommission.gov.uk/news/article/bet365-to-pay-gbp582-120-for-regulatory-failures

## Release blockers still open

- Existing research inventory has 100 candidate rows, but candidates are not the same as verified brands.
- The verification sprint document previously reported 0/100 candidates approved for publication. This session has added primary-source evidence, but has not completed the remaining reviews or second-editor checks for 100 brands.
- The latest known static-site check run `39953731470` failed. Fetching the job logs returned a not-found response, and the attempt to rerun the job was blocked; no successful rerun is claimed.
- Cloudflare is the hosting target. No deployment, DNS change, cache purge, or secret change was performed in this session.
- No live Google Search Console data was accessed. Daily impressions and the 10-million/day ambition are not guaranteed and must be measured against actual Search Console data.

## Next work queue

1. Resolve the static-site check failure using the current Actions run and repository workflow configuration.
2. Continue Swiss official-regulator list checks and complete operator-level evidence for each of the ten rows.
3. Verify additional market-specific batches (Great Britain, Netherlands, Germany) against official registers, deduplicate brands/entities, and record primary URLs and UTC timestamps.
4. Produce individual reviews only after evidence and market eligibility gates; include disclosures and no invented hands-on testing.
5. Run build and browser checks, verify Cloudflare deployment and canonical URLs, then inspect sitemap and Search Console coverage.
