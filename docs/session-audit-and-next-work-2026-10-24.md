# Latest live-preview QA — 24 October 2026, 17:52 UTC

- Read-only Cloudflare Pages preview fetch now confirms the branch directory reflects the latest Pennsylvania evidence text: it includes one BetRivers card and one Hollywood Casino Online card, while Ivy Casino is absent. Source-level check: 100 `article.brand-card` entries and 100 unique card titles, no duplicate titles.
- Preview page metadata: canonical `https://beincasinos.online/brand-directory/`, robots `noindex,follow`. The preview sitemap has 44 URLs and does **not** include `/brand-directory/`. This is the intended draft gate; it is not a production indexing release.
- Production `https://beincasinos.online/brand-directory/` still returns **404**. No production deployment, merge or indexing release has occurred.
- The Hollywood card now says the PGCB lists `http://www.hollywoodcasino.com` for slots/table games with 19 December 2024 commencement; the HTTP URL is plain text, not a direct clickable link. The current HTTPS canonical/redirect and customer-contracting entity remain open.
- CI has not passed. The latest observed Static site checks attempts fail before any step runs (runner ID 0/no step records/no readable logs); this remains an Actions runner-allocation issue, not a diagnosed source-test failure. Do not bypass checks.
- PR #141 remains open, Draft and unmerged. Approved consumer reviews remain **0/100**.

---

# Latest exact-ID mapping — 24 October 2026

- Tier-1 tracker remains 106 data rows, 18 columns, zero malformed rows and zero duplicate brand/market keys. Source-matched global IDs are now filled for Hollywood Casino Online (PA) → `hollywood-casino`, BetRivers Casino (PA) → `betrivers-casino`, Casineo.ch (CH) → `casineo`, and Jollie.de (DE) → `jollie`. These assignments use an existing exact brand ID or an exact normalized brand/market match; no broader aliases were inferred. **102 IDs remain blank**, so deduplication is still incomplete.
- The source directory contains exactly 100 cards, including one BetRivers and one Hollywood Casino Online; the latter cites the PGCB-listed `http://www.hollywoodcasino.com` URL and keeps HTTPS/customer-contract matching as an open gate. Directory remains `noindex,follow` and absent from the sitemap.
- PR #141 remains Draft/open/unmerged. CI runner-allocation failure continues; latest preview is stale relative to source changes. Approved reviews remain 0/100 and production release remains blocked.

---

# Latest correction — Pennsylvania brand/domain distinction — 24 October 2026

- The PGCB's 2024–2025 Annual Report reports a new Hollywood Casino iGaming-site launch in December 2024 under the Hollywood Casino at Penn National Race Course certificate, and the current PGCB operator directory displays Hollywood Casino Online. The separate legacy URL `pa.hollywoodcasino.com` is listed as a former site ending 14 December 2023 in the 13 February 2026 certificate-holder PDF.
- Correct disposition: **do not reuse the retired legacy URL; retain Hollywood Casino Online as a HOLD research lead** until its current customer route, contracting entity and terms are verified. The prior claim that the brand itself should be excluded is withdrawn.
- Added a Pennsylvania-specific row to `docs/brand-research-template.csv` under existing global brand ID `hollywood-casino`, market `US-PA`, with official URL `VERIFY` and no public score.
- Updated the global-ID reconciliation CSV after the added market row. Registry count is now 205 market-specific rows across 154 global IDs; the 100-name candidate register remains a separate selection queue. Exact normalized slug matches remain only a diagnostic; aliases need manual reconciliation.
- Sources: https://gamingcontrolboard.pa.gov/sites/default/files/2025-09/PGCB%20Annual%20Report%202024-2025%20FINAL.pdf ; https://gamingcontrolboard.pa.gov/interactive-gaming-operators ; https://gamingcontrolboard.pa.gov/sites/default/files/2026-02/2.13.26%20Licensed%20Interactive%20Gaming%20Certificateholders%20and%20Authorized%20Interactive%20Gaming%20websites.pdf

---

# Latest verified continuation — 24 October 2026

- **Pennsylvania correction:** the legacy `pa.hollywoodcasino.com` URL ended on 14 December 2023, but the PGCB's 2024–2025 Annual Report records a later Hollywood Casino online-brand launch in December 2024. The prior blanket exclusion was too broad. Current Hollywood Casino is HOLD/UNKNOWN until the exact live domain and customer-contracting entity are matched; BetRivers remains a separate Pennsylvania HOLD lead.
- **Directory QA:** source has exactly 100 brand cards, one BetRivers card and one Hollywood Casino Online card; Ivy Casino (inactive in the cited UKGC record) was replaced. The directory has `noindex,follow` and is excluded from the sitemap. Current preview fetched before the latest card commit confirmed BetRivers and noindex; verify freshness again for the new Hollywood card.
- **Production vs preview:** production `https://beincasinos.online/brand-directory/` returns 404 and production sitemap has 46 URLs; the branch preview sitemap has 44 URLs. No production release was made.
- **Tracker:** 106 data rows, 18 columns, zero malformed rows and zero duplicate brand/market keys; 58 VERIFY domains, one UNKNOWN, two NOT APPLICABLE, and 106 blank global brand IDs. Global deduplication remains incomplete.
- **PR/CI:** PR #141 is open, Draft, and unmerged; changed-file count 123 at last check. Static site checks continue to fail before runner allocation (runner ID 0, no steps/logs); no successful current-head CI is confirmed.
- **Completion truth:** 100 research cards do not equal 100 approved reviews. Approved reviews remain **0/100**. No merge, production deploy, indexing release or paid outreach performed.

**Next:** fetch the preview after the latest card commit; obtain a functioning runner and run the full build/site/artifact checks; continue dated terms, cashier, complaints, responsible-gambling, accessibility, rights and independent-review gates.

---

# Latest QA checkpoint — 24 October 2026, 18:00 UTC

- Audited the two different registries rather than treating them as one count. `docs/brand-research-template.csv` contains **204 market-specific rows, 154 distinct global_brand_id values, 202 HOLD and 2 rejected**. The separate Tier-1 prospect tracker contains **106 rows and 106 blank global_brand_id values**.
- The 100-name candidate register contains 100 candidates. Exact normalized slug matching finds only 20 direct matches against the 154-ID registry; this is a reconciliation diagnostic, not proof that the other 80 candidate names are absent. Aliases, market variants, and entity/product differences need manual mapping before claiming the selected 100 are globally deduplicated.
- Added `docs/reviews/internal/global-brand-id-reconciliation-2026-10-24.csv`: one row per distinct registry ID, market-row counts, name variants, market codes, decisions, exact candidate matches and a manual-reconciliation status. No aliases were guessed.
- Confirmed the PGCB's 13 February 2026 certificate-holder list names BetRivers under SugarHouse HSP Gaming, LP d/b/a Rivers Casino Philadelphia (certificate holder) and Rush Street Interactive PA, LLC (interactive-gaming operator), with slots/table games/poker and a BetRivers launch date of 30 January 2020. The legacy `pa.hollywoodcasino.com` URL is in the former-site section, but the PGCB 2024–2025 Annual Report records a later Hollywood Casino online-brand launch in December 2024. Keep the current brand as HOLD until the exact new domain and customer contract are matched. <https://gamingcontrolboard.pa.gov/sites/default/files/2026-02/2.13.26%20Licensed%20Interactive%20Gaming%20Certificateholders%20and%20Authorized%20Interactive%20Gaming%20websites.pdf>
- Latest observed Static site checks runs #1493–#1495 failed in roughly 1–3 seconds, with no recorded steps and no readable logs; job metadata is consistent with runner allocation failing before any source test. A retry was requested for the latest failed run. No successful current-head CI is confirmed.
- PR #141 remains open, Draft and unmerged, with 122 changed files at the latest count before this reconciliation file; verify the changed-file count again after the latest commit. No production deployment or merge was performed. Approved reviews remain **0/100**.

**Next:** manually resolve the candidate-to-global-ID alias map, inspect current GitHub Actions run status, and only then decide which 100 unique brands are the approved programme cohort. Keep all profiles HOLD until consumer testing and independent review are complete.

---

# Latest QA checkpoint — 24 October 2026, 17:41 UTC

- Read-only browser fetch of the existing branch preview `https://ops-2026-10-24-target-reconc.beincasinos.pages.dev/brand-directory/` returned the older directory content: it still showed the pre-replacement research cards, so the current BetRivers source change is not confirmed live in the preview. The preview sitemap exposed 44 URLs. A read-only check of production found `/brand-directory/` returning 404 and a 46-URL production sitemap; this confirms production is not updated with the branch-only directory.
- Commit-prefix preview URLs tested for the recent commit SHAs returned 404, so they are not valid per-commit preview addresses in this project. No alternate current-preview URL was established.
- GitHub Actions Static site checks continues to fail before a runner is assigned. Run #1473 (ID 40117091388) for commit `b6a85cb97b632e0d8ce563bec939446f3f32888e` had `runner_id: 0`, no steps, and no logs. Rerunning its failed job created run #1474, which failed the same way. A newer run for the current directory head was queued at last observation; no successful current-head build is confirmed.
- This is not a source-test failure diagnosis. Do not bypass CI, merge PR #141, or publish the directory. PR remains Draft/open/unmerged; production release remains blocked.

---

# BeInCasinos session audit and next-work queue — 24 October 2026

**Scope:** Repository branch and PR #141 review. This is an internal engineering/research checkpoint, not a release approval.

## Repository state at this checkpoint

- Repository: `beincasinos-Brand/Beincasinos`
- Working branch: `ops/2026-10-24-target-reconciliation-and-release-gates`
- Base: `ops/tier1-10-market-100-brand-roadmap-2026-10-22`
- PR: https://github.com/beincasinos-Brand/Beincasinos/pull/141
- PR state: open, Draft, not merged.
- Latest observed changed-file count at the prior checkpoint was 117; after adding tested robots-meta parsing, regression tests, and the Pennsylvania target correction, PR #141 has 122 changed files at the latest observed count.
- Public-release decision remains BLOCKED. No production deployment, merge, DNS change, crawl-unblock, or brand outreach was authorized by this work.

## Work completed in this session

5. Re-aligned the ten-target priority board to the approved Tier-1 market scope: GB, NL, CH, DE (Schleswig-Holstein only), US-NJ, US-PA and US-MI. The programme now uses ten brand-market targets across seven market codes, not a claim of ten countries.
6. Added internal primary-source dossiers for admiral.ch (FGB), Ember (NJ DGE), BetRivers (PA PGCB) and Horseshoe Online Casino (MI MGCB). The prior Hollywood Casino Online draft is now a historical-status correction: the PGCB records the legacy skin ending in December 2023. BetRivers remains HOLD; no firsthand real-money testing is claimed.
7. Fixed a sitemap checker inconsistency: it now uses the shared robots-meta parser, omits noindex pages from expected sitemap URLs, and rejects any noindex page found in the sitemap. The parser has regression tests. Updated the public directory copy to state that it remains noindex pending approval.
8. Added a `global_brand_id` column to the 106-row master prospect tracker and a CI validator for required columns, row widths and duplicate brand/market keys. All 106 IDs are explicitly blank; the validator warns rather than disguising the outstanding deduplication work.

1. Added internal brand evidence/reconciliation worksheets for Betfair Casino, Coral Casino, Gala Casino and Virgin Games in Great Britain, plus prior worksheets for the other brands listed in PR history. These are HOLD worksheets, not approved consumer reviews.
2. Corrected stale README hosting statements that incorrectly said Cloudflare was not connected and Vercel was selected. The final deployment runbook records Cloudflare Pages `beincasinos` connected to GitHub and a preview URL; freshness of the current branch deployment is still unverified.
3. Corrected stale project-completion-board statements that contradicted later Cloudflare setup notes.
4. Investigated latest Static site checks workflow run #1312, run ID `40114310640`, for commit `59b74bf192f3a2784f9fdbf171803589714205da`. It failed within approximately one second with runner ID 0 and no recorded steps. The log download returned BlobNotFound. This is **not enough evidence to diagnose a source-code failure**. A rerun of the failed job was requested and also failed before runner allocation. Later commit checks show the same immediate failure pattern; no source-level failure has been isolated.

## Key quality findings

### The 100-brand goal must not be confused with file count

The legacy `docs/brand-prospect-list.md` contains 100 names but explicitly spans markets outside the current Tier-1 focus and marks all prospects as unverified. The new international priority board now tracks one market-specific candidate in each of ten roadmap markets, but all ten remain HOLD. The master tracker is a separate 105-row research dataset. The project strategy focuses on GB, DE, NL, CH and specifically authorized US state/product markets; AU and FR are research-only for online-casino promotions pending category-specific legal review. A list entry is not a verified operator, permitted market, consumer-tested product, approved review or willing buyer.

The master tracker `docs/tier-1-master-prospect-tracker.csv` contains 106 data rows (107 lines including its header). 104 rows are in the current GB/NL/CH/DE/US-state research scope; two rows are explicit FR/AU category exclusions. All 106 `global_brand_id` fields are blank, preventing reliable cross-market deduplication. Its entries are mixed research leads across markets and evidence grades; each still needs the specific follow-up described in its row. Do not represent this as 100 completed reviews.

### Review approval criteria

A review counts as approved only after all applicable items are evidenced:
- Exact official domain, legal operator, product scope, jurisdiction and current primary regulator evidence.
- Current terms and promotion conditions, cashier/payment disclosures, complaints/ADR, safer-gambling tools and privacy disclosures.
- Regulatory history attributed to the exact licensee with dates, outcomes and context.
- Dated consumer testing with reproducible steps; no fabricated first-hand experience.
- Image/logo rights and any affiliate/sponsored disclosure requirements.
- Independent editorial/factual sign-off.
- Public page has useful unique content, correct metadata, working links, and passes the repository checks.
- Explicit publication gate is cleared; HOLD drafts stay internal and excluded from the public build/sitemap.

The project board's most recent baseline and current checkpoint both say **0/100 fully publication-approved brand reviews**. Do not change that number until each profile passes the approval gate.

## Open blockers

1. Diagnose GitHub Actions runs that fail before runner allocation. If this persists, inspect repository Actions settings/availability with the owner; do not guess that a source check failed.
2. Reconcile any remaining hosting-status contradictions. Cloudflare Pages is the preferred host; a prior preview deployment succeeded for commit `ee28cc0`, but freshness of the current branch preview remains unverified. Production currently returns 404 for `/brand-directory/`, and the public sitemap lists 46 URLs without that route. No production release is authorized; verify preview freshness and real production behavior separately.
3. Keep `robots.txt` and the public-release gate unchanged until explicit approval and the legal/editorial/manual-host acceptance gates are cleared.
4. Requalify the 100-name legacy prospect queue against the actual market strategy, deduplicate brands/legal entities, exclude inactive or out-of-scope products, and maintain separate counts for prospects, evidence-complete drafts, and approved reviews.
5. Prefer finishing and independently reviewing a smaller number of evidence-complete profiles over producing additional generic HOLD templates.

## Current decision

**BLOCKED — continue internal research and source/CI fixes only.** This checkpoint does not approve publication, deployment, indexing, paid placement or outreach.


## Additional 24 October work checkpoint

- Expanded current first-party GB evidence dossiers and the research template rows for bet365, 888casino and William Hill. Captured payment/withdrawal wording, complaints/ADR routes where found, safer-gambling disclosures and dated regulatory action context. No account or transaction tests are claimed.
- The master tracker now has 106 rows. The legacy Hollywood Casino Online target is marked Exclude/UNKNOWN pending resolution of conflicting PGCB signals; BetRivers is the replacement PA target. The qualification audit records 58 VERIFY domains, one UNKNOWN and 106 blank global brand IDs.
- Nine noindex parser regression tests passed in an isolated local harness. Current GitHub Actions runs still fail before runner allocation (runner ID 0, no steps/logs); a rerun was requested. The full site build, browser smoke tests and artifact check remain unverified.
