# Latest release QA checkpoint — 24 October 2026, 18:54 UTC

- Live read-only browser extraction of the current known Cloudflare branch preview succeeded for `/brand-directory/`, `/reviews/`, `/robots.txt` and `/sitemap.xml`.
- Branch preview `https://ops-2026-10-24-target-reconc.beincasinos.pages.dev/brand-directory/` serves the research directory and declares canonical `https://beincasinos.online/brand-directory/` plus `noindex,follow`. It is intentionally absent from the 44-URL sitemap, consistent with the current noindex policy. The preview robots file allows crawling and points at the production canonical sitemap.
- Production `https://beincasinos.online/brand-directory/` still returns 404 in the live fetch, while the branch preview route returns the directory. Treat this as a deployment/version mismatch or production-route blocker; do not claim the production route is fixed, and do not deploy or merge without authorization.
- Preview `/reviews/` is a methodology/research-queue hub with a partner-portfolio section and explicit statement that no live profiles are scored or ranked. It is not a completed set of 100 consumer reviews. Approved reviews remain **0/100**.
- Latest observed Static site checks run 40122472710 (attempt 2, head SHA `44652598dafddd9ea7840ca05c8cff429b5533b4`) failed before runner allocation: job runner ID 0, zero steps and no retrievable logs. This is not evidence that the tests themselves failed or passed. CI remains unresolved.
- Current PR #141 is open, Draft, unmerged, with 128 changed files at the latest query. No production deployment or merge was performed.
- Tier-1 prospect tracker remains 114 data rows, 18 columns, zero malformed rows and duplicate brand/market keys in the last audit; 99 blank global brand IDs (15 populated rows / 14 distinct IDs), 58 VERIFY domains, 111 HOLD, 1 Exclude and 2 category-specific exclusions. These are market-specific prospect rows, not 114 unique brands or completed reviews.

**Next actions:** resolve why CI is failing before runner allocation; confirm whether production should intentionally expose the research directory or keep it preview-only; validate the built artifact and all route/canonical/noindex behavior after a successful CI run; continue current terms and actual consumer/accessibility tests on the first ten targets. No score or public ranking until evidence and independent review are complete.

---

# Latest work checkpoint — 24 October 2026, 19:00 UTC

- Updated the top-10 board's stale tracker counts to the current audited snapshot: 114 market-specific rows, 99 blank global IDs, 58 VERIFY domains; 0/100 approved reviews.
- Found and documented a material Betway Great Britain route mismatch: opening the cited first-party https://betway.com/gb/en/casino redirected to https://betway.de/de/de/sports (German sportsbook) on 24 Oct 2026. The UKGC licence/domain register remains a regulatory lead, but this URL is not proof of a working GB casino journey. The dossier, top-10 board and brand-research CSV now place the GB product on HOLD until the exact route/contracting entity are re-established. Previously surfaced withdrawal/payment claims are not treated as current GB evidence.
- Re-requested the latest failed Static site checks job (run 40122280507); retry again failed before runner allocation (runner ID 0, zero steps, no logs). This is an infrastructure/runner failure, not a test result. A new commit will trigger another PR check; do not claim green CI until it actually executes.
- PR #141 remains open, Draft and unmerged. No production deployment was performed. The live /brand-directory/ route was still reported as 404 in the latest release-gate audit, even though the current source build includes brand-directory/; that remains a release verification blocker, not a reason to bypass approval.
- Approved reviews remain 0/100. All target dossiers remain HOLD until exact market permissions, current terms, actual consumer/accessibility tests, image rights and independent sign-off are complete.

**Next:** restore/verify the current GB Betway route, continue evidence capture for the remaining first-ten candidates, and get CI to allocate a runner so the public-only Cloudflare artifact can be tested.

---

# Latest work checkpoint — 24 October 2026, 18:45 UTC

- Added `docs/us-state-supplemental-research-queue-2026-10-24.md`, linked it from README and the international board, and kept NJ/PA/MI supplemental targets separate from the ten-market roadmap.
- Updated BetRivers PA dossier and tracker using a fresh first-party route capture. Footer confirms Rush Street Interactive PA, LLC licence 110298 and names both SugarHouse HSP Gaming, LP / Internet Gaming Certificate 1356 and Holdings Acquisition Co., LP / licence F-1361. The current terms/privacy/protection/RG pages did not yield their substantive contents in text extraction, so these remain open evidence gaps.
- Reparsed the tracker with CSV quote/multiline handling: **114 rows, 18 columns, zero malformed rows, zero duplicate brand/market keys, all ten roadmap markets represented, 99 blank global IDs (15 populated rows / 14 distinct IDs), 58 VERIFY domains, 111 HOLD, 1 Exclude, and 2 category-specific exclusions**. The qualification audit now reflects the current 114-row tracker. This remains a research queue, not 100 approved reviews.
- Current-head workflow run 40122009428 failed before runner allocation (job runner ID 0, zero steps, no logs). A failed-job rerun was requested; the previous run 40120514437 also failed before runner allocation on attempt 2. CI remains an infrastructure/service blocker; no passing check is claimed.
- PR #141 is still open, Draft and unmerged; latest known head at this checkpoint is `6a8cbbdace76cbf3cccd733d8ccb440cb846c1ed`. No production deployment or merge has been performed. Approved reviews remain **0/100**.

**Next:** inspect the latest rerun outcome; once a runner is available, run the full site, tracker, CSP, sitemap/noindex and browser smoke checks. Continue current terms/cashier evidence capture and independent reviews; keep all unqualified targets on HOLD.

---

# Latest checkpoint — 24 October 2026, 18:42 UTC

- Added `docs/us-state-supplemental-research-queue-2026-10-24.md` and linked it from README and the international board. The queue separates state-specific leads from the ten-market roadmap.
- Parsed `docs/tier-1-master-prospect-tracker.csv` with CSV quote/multiline handling: 114 data rows, 18 columns, no malformed rows, no duplicate brand/market keys, all ten roadmap markets represented, 99 blank global-brand IDs, 58 blank/VERIFY domains, and 111 HOLD rows. The two US-PA rows for BetRivers and Hollywood Casino Online remain separate HOLD leads.
- The Hollywood Casino Online PA dossier distinguishes the old retired `pa.hollywoodcasino.com` skin (ended 14 Dec 2023) from the later PGCB-listed `http://www.hollywoodcasino.com` route with a 19 Dec 2024 commencement date. Current HTTPS redirect and customer-contract entity remain unverified.
- Retried the latest observed Static site checks failure: run 40120514437, attempt 2, job 120954831508. It failed in two seconds with runner ID 0 and no steps; logs are unavailable. This is an unresolved runner/workflow service failure, not a diagnosed source-code test failure.
- PR #141 remains open, Draft and unmerged. No production deployment. Approved reviews remain 0/100.

# Latest checkpoint — 24 October 2026, 18:24 UTC

- **100-target slate validation:** parsed the provisional review slate and confirmed exactly 100 numbered rows, 100 distinct global-brand IDs, zero duplicate IDs, and no missing official URL, legal-entity field or regulator/register URL. These are evidence-backed research targets, not approved reviews; every row remains HOLD.
- **Cloudflare preview SEO smoke check:** the existing branch preview responds for the home page, /brand-directory/, /reviews/, robots.txt and sitemap.xml. Home page title/description/canonical metadata are present. The research directory returns robots: noindex,follow and is absent from the sitemap. The sitemap lists 44 canonical https://beincasinos.online/ URLs, and robots.txt exposes the canonical sitemap. This is a read-only check of the existing preview alias; it does not prove that the alias serves the latest commit or replace browser/accessibility tests.
- **CI is not executing:** the latest observed run 40120440984 for head d9ed4a644b0e7caf559d26544d4511b4f11669f failed after about two seconds, with runner ID 0 and zero steps; the rerun of an earlier failure had the same outcome. Logs are unavailable. Public GitHub Community reports describe the same symptom in other repositories, but that does not prove a shared root cause. Do not change the workflow's correct ubuntu-latest label on this evidence alone; preserve run/job IDs and escalate to GitHub Support if the next retry repeats.
- **Holland Casino Online:** first-party eligibility, under-24 restrictions, login-time limits, support channels and optional automatic-withdrawal-limit disclosures are captured in the dossier and trackers. Terms/privacy reads return HTTP 403 to the research fetcher; the current Ksa public profile still displays the prior permit period, so domain notification under the renewed permit remains unresolved.
- **Betano Belgium:** fresh live English and French A+ table views agree on dossier 20000, decision 12 Nov 2024, expiry 31 Dec 2026. The Tier-1 tracker date field is aligned; stale indexed 2019/2034 text is superseded.
- **Data integrity:** Tier-1 prospect tracker has 114 data rows × 18 columns, zero malformed rows or duplicate brand/market keys. Broader research template has 207 data rows × 33 columns, zero malformed rows.
- **Release state:** PR #141 remains open, Draft and unmerged with 126 changed files. No production deployment or merge was made. Approved reviews remain 0/100; all targets remain HOLD.

**Next:** resolve the runner-start failure through GitHub Support or an authorized local CI path; confirm the current Ksa domain notification for Holland Casino; continue current terms/cashier capture and independent review.

---

# Latest checkpoint — 24 October 2026, 18:22 UTC

- **Cloudflare preview SEO smoke check:** the existing branch preview responds for the home page, /brand-directory/, /reviews/, robots.txt and sitemap.xml. Home page title/description/canonical metadata are present. The research directory returns robots: noindex,follow and is absent from the sitemap. The sitemap lists 44 canonical https://beincasinos.online/ URLs, and robots.txt exposes the canonical sitemap. This is a read-only content/SEO check of the existing preview alias; it does not prove that the alias serves the latest commit or replace browser/accessibility tests.
- **CI remains blocked before execution:** latest run 40120320531 for head 1323297d2ba5a3ff07ea59035b2972c1e8506739 failed after about two seconds, with runner ID 0 and zero steps. Rerunning the prior failed job produced the same result. No site, artifact or browser checks ran; logs are unavailable. Treat as a GitHub Actions runner/job-start failure, not a passed code test.
- **Holland Casino Online:** first-party eligibility, age-24 restriction, login-time limits, support channels and optional automatic-withdrawal-limit disclosures have been captured in the dossier and trackers. Terms/privacy reads return HTTP 403 to the research fetcher; the current Ksa public profile still displays the prior permit period, so domain notification under the renewed permit remains unresolved.
- **Betano Belgium:** live English and French A+ table views agree on dossier 20000, decision 12 Nov 2024, expiry 31 Dec 2026. The tracker date field is aligned; stale indexed 2019/2034 text is superseded.
- **Data integrity:** Tier-1 prospect tracker has 114 data rows × 18 columns, zero malformed rows or duplicate brand/market keys. Broader research template has 207 data rows × 33 columns, zero malformed rows.
- **Release state:** PR #141 remains open, Draft and unmerged with 126 changed files. No production deployment or merge was made. Approved reviews remain 0/100; all targets remain HOLD.

**Next:** resolve runner allocation or use an authorized local CI path; confirm the current Ksa domain notification for Holland Casino; continue current terms/cashier capture and independent review.

---

# Latest checkpoint — 24 October 2026, 18:20 UTC

- **Holland Casino Online (NL):** expanded the internal dossier and both trackers with first-party Help Center evidence: 18+ and Dutch citizenship/residence-permit requirements; under-24 monthly deposit cap of €149 and no bonuses/offers; login-time limits (max eight hours/day; increases delayed seven days); support phone/email published as 24/7 and live chat 09:00–02:00 for logged-in users; optional automatic-withdrawal-limit tool and its up-to-48-hour processing statement. That 48-hour figure applies only to the optional threshold-triggered automatic withdrawal, not ordinary withdrawals. Terms/privacy fetch returned HTTP 403; no login, payment or support test claimed. The Ksa public Kansspelwijzer profile still shows the previous permit period, so the current domain notification under the renewed permit remains HOLD.
- **Betano Belgium:** fresh live English and French regulator tables agree on A+ dossier 20000 decision 12 Nov 2024 and expiry 31 Dec 2026. The Tier-1 tracker date field now matches the current live table; stale indexed 2019/2034 text is superseded.
- **Data integrity:** Tier-1 prospect tracker is 114 data rows × 18 columns, zero malformed rows, zero duplicate brand/market keys. The broader research template is 207 data rows × 33 columns, zero malformed rows.
- **CI:** reran the failed Actions job once. Attempt 2 also failed before runner allocation: runner ID 0, zero steps, no downloadable logs. This is an environment/job-start failure; the site checks themselves did not execute. PR #141 remains open, Draft and unmerged; no production deployment or merge made. The current PR has 126 changed files.
- **Completion truth:** approved reviews remain **0/100**. The ten international targets and supplemental US-state targets remain HOLD pending exact domain/contract match, full current terms, actual usability/accessibility tests, image rights and independent second review.

**Next:** investigate GitHub Actions runner allocation; get the Ksa current domain notification confirmed for Holland Casino; continue current terms/cashier capture on the priority reviews.

---

# Correction checkpoint — 24 October 2026, live source recheck

- **Betano Belgium A+ register:** fresh live fetches of both the Belgian Gaming Commission's English and French A+ table pages returned the same dossier 20000 row: `www.betanocasino.be`, VIAGE, SA/NV CASINOS AUSTRIA INTERNATIONAL BELGIUM, decision date **12 November 2024**, expiry **31 December 2026**. A search-indexed French snippet that showed 2019/2034 was stale relative to the current page. Updated the Betano dossier, Tier-1 tracker, brand research template and international board to remove the false cross-language-conflict claim. This is a source reconciliation, not review approval; Betano remains HOLD.
- **Hollywood Casino Online (Pennsylvania):** the current dossier remains correct: legacy `pa.hollywoodcasino.com` ended 14 December 2023, but PGCB's newer listing shows `http://www.hollywoodcasino.com` commencing 19 December 2024. Do not incorrectly exclude the whole brand based only on the retired legacy URL. The current HTTPS route, contract entity and consumer terms remain to be verified.
- **BetRivers Pennsylvania:** retained as a separate supplemental US-state lead with PGCB certificate-holder/operator roles separated. It does not replace any of the ten international priority rows.
- **CI:** current head run `40119689309` on `d990e57f979395f196c6c624ddf754501912b5df` failed in about two seconds; job runner ID 0, zero steps, no readable logs. Application checks did not execute. PR #141 remains open, Draft and unmerged; 126 changed files. No production deployment or merge was made.
- **Completion truth:** approved reviews remain **0/100**; all targets stay HOLD until full current terms, exact customer entity, real usability/accessibility testing, image rights and independent review are complete.

**Next:** diagnose the GitHub Actions runner-start failure; recheck Betano's live register before publication; continue evidence capture for the ten market-specific priority targets.

---

# Latest verified continuation — 24 October 2026

- **Superseded Betano note:** earlier in this audit, a search-indexed French snippet appeared to conflict with the English A+ table. Fresh live fetches of the English and French tables on 24 October 2026 both returned decision 12 November 2024 and expiry 31 December 2026 for dossier 20000. The tracker and dossier now match the live data; recheck before publication.
- **Betano Belgium — responsible-gambling sources added:** first-party pages describe daily/weekly/monthly deposit and loss limits, a 1–8 hour session timer, 24-hour to 6-month time-outs, withdrawal-cancellation blocking and EPIS self-exclusion, with SOS Gambling 0800 35 777. These are operator statements, not independently tested controls.
- **International target/identity coverage:** all ten Tier-1 market/brand pairs have matching market-specific tracker rows and expected global IDs. The tracker has 114 data rows / 18 columns, 15 populated global-brand-ID cells, 99 blank IDs, 14 unique IDs among populated cells, 58 `VERIFY` domains, zero `UNKNOWN` domains, two `NOT APPLICABLE` entries and zero duplicate brand/market keys.
- **bet365 GB:** internal evidence dossier now records that the current GB General Terms state an effective date of 1 October 2026. The separate casino rules and linked documents still need archiving; no account, payment, gameplay, support-contact or accessibility test is claimed.
- **StarVegas CH:** the dossier and tracker now cite the FGB's current platform list and 2024 activity report. StarVegas.ch is associated with Casino Interlaken; Casino Interlaken AG is named as concessionaire. Live customer-contracting party and current game-specific permissions remain to be verified.
- **CI/release gate:** latest observed Actions run for the current audit commit failed in about two seconds with runner ID 0, no steps and no downloadable logs. Repeated recent runs show the same pre-runner failure, so application tests have not run in CI. PR #141 remains open, Draft and unmerged; 126 changed files. No production deployment or merge was made.
- **Completion truth:** approved reviews remain **0/100**. All ten priority targets and supplemental US-state leads remain HOLD pending exact current terms, contract/entity match, real usability/accessibility tests, image rights and independent review.

**Next:** get the Actions runner/job-start failure resolved; recheck Betano's live A+ record before publication; run full site/artifact/browser tests once a runner is available; continue terms/cashier capture and independent review. Do not count candidate rows or regulator listings as completed reviews.

---

# Latest verified continuation — 24 October 2026

- **International target coverage:** the ten Tier-1 market/brand pairs on the international board now each have a matching market-specific row and expected global brand ID in the Tier-1 prospect tracker. This closes an identity/coverage gap, not the consumer-review gates.
- **Tracker snapshot:** 114 data rows, 18 columns, 15 populated global-brand-ID cells, 99 blank IDs, 14 unique IDs among populated cells, 58 `VERIFY` domain placeholders, zero `UNKNOWN` domains, two `NOT APPLICABLE` entries and zero duplicate brand/market keys. bet365 intentionally shares `bet365-casino` across GB and NL, preserving separate market rows.
- **bet365 GB evidence:** updated the internal dossier with the current first-party GB General Terms effective date of 1 October 2026. The current terms still cross-reference casino-specific rules and other linked documents; payment/withdrawal processing statements need careful contextualisation. No account, deposit, withdrawal, gameplay, support-contact or accessibility test is claimed.
- **StarVegas CH evidence:** strengthened the dossier and tracker with the FGB's current platform list and 2024 activity report. StarVegas.ch is associated with Casino Interlaken; Casino Interlaken AG is named as concessionaire. Current customer-contracting party and game-specific permissions remain to be verified.
- **CI state:** latest-head Static site checks run `40119516612` was observed queued immediately after commit `e4521526bfe333f79bbed2e5aafd6d2cff3cd5b0`; final outcome not yet verified at this checkpoint. Recent earlier runs failed in under three seconds with runner ID 0 and no steps. PR #141 remains open, Draft and unmerged; 126 changed files. No production deployment or merge was made.
- **Completion truth:** approved reviews remain **0/100**. All ten priority targets and supplemental US-state leads remain HOLD pending exact current terms, customer-contract match, real usability/accessibility testing, image rights and independent review.

**Next:** verify latest CI result, run full site and artifact tests if a runner is allocated, and continue source/terms capture. Keep all publication and production gates intact.

---

# Latest verified continuation — 24 October 2026

- **Market-pair coverage:** added the missing Great Britain bet365 row as a distinct market-specific record (UKGC account 55149, active Casino Remote permission and bet365.com domain), while retaining the Netherlands row separately under the same global brand ID. Both remain HOLD; the UKGC's 4 April 2024 settlement is captured with context and must not be hidden from a future review.
- **Swiss target coverage:** added StarVegas — Switzerland to the Tier-1 prospect tracker using the FGB's current online-platform list: starvegas.ch is listed for Casino Interlaken, with online business starting 24 February 2020. Game-specific authorisations and current customer-contracting entity still need checking.
- **Identity reconciliation:** normalized BetRivers Pennsylvania to global ID `betrivers-casino` and Caesars Casino Ontario to `caesars-palace-online-casino`, matching the existing global identity ledger. This does not collapse their separate jurisdiction-specific evidence or grant cross-market permissions.
- **Tier-1 prospect tracker:** now **114 data rows / 18 columns**, 15 populated global-brand-ID cells, 99 blank IDs, 14 unique IDs among populated cells, 58 `VERIFY` domain placeholders, zero `UNKNOWN` domains, two `NOT APPLICABLE` entries and zero duplicate brand/market keys. The same ID appearing for bet365 in GB and NL is intentional market-level deduplication, not a duplicate pair.
- **International 10-market board:** all ten targets now have a matching market-specific tracker row and expected global ID. This is identity/coverage QA only; all ten remain HOLD, current terms and consumer testing remain incomplete, and approved reviews remain **0/100**.
- **CI/release gate:** recent Static site checks still fail immediately with runner ID 0 and no workflow steps; no successful current-head CI is confirmed. Parser regression suite has 17 test methods, but no full site build/browser run is verified in this session. PR #141 remains open, Draft and unmerged; no production deployment or merge was made.

**Next:** unblock GitHub Actions job startup, run the full static build and artifact checks, then continue current terms/cashier capture and independent second-review gates. Do not count candidate rows or regulator listings as completed reviews.

---

# Latest verified continuation — 24 October 2026, 20:30 UTC

- **Tracker reconciliation:** matched eight more market-specific records to the main registry's existing global brand IDs: bet365 (NL) → `bet365-casino`, Betano (BE) → `betano`, Betsson (SE) → `betsson`, Danske Licens Spil (DK) → `danske-spil-casino`, Luckia (ES) → `luckia`, Sisal (IT) → `sisal`, Holland Casino Online (NL) → `holland-casino-online`, and Tipico → `tipico-casino`. The Tipico tracker market was corrected from generic `DE` to `DE-SH` to match the actual Schleswig-Holstein-only scope. Notes were added to each affected row; no review was approved by assigning an ID.
- **Current tracker count:** 112 data rows, 18 columns, 12 filled global-brand IDs and 100 blank IDs. These are prospect identity mappings, not review approvals. The ten-market international board still has ten targets, all HOLD.
- **Review accuracy:** corrected 888casino's Great Britain evidence dossier so the GB operator/terms citation points to the UK-specific User Agreement, not the separate `user-agreement-ma/` regional page. Current UKGC evidence continues to show active Casino Remote permission for account 39028 and the 2024–2025 enforcement context; no account or payment testing is claimed.
- **Noindex QA:** added five robots-meta parser regression cases in `scripts/test_deploy_artifact.py`. An isolated local reproduction of the repository parser and all 17 unit cases passed; this is **not** a full repository CI/build test. GitHub Actions still fails before runner allocation (runner ID 0, no steps and no logs); a retry did not resolve it.
- **PR #141:** open, Draft, unmerged; 126 changed files at the last confirmed PR file-list check. Latest commits have new workflow runs, but no successful current-head CI is confirmed. No current preview refresh, production deployment, or merge is confirmed. Approved reviews remain **0/100**.

**Next:** resolve Actions runner/job-start failure through repository settings or GitHub support; then run the complete static site, tracker, deployment artifact, parser-unit and browser-smoke tests. Keep all consumer-review publication gates in place.

---

# Current continuation checkpoint — 24 October 2026, 20:15 UTC

- Added five regression cases to `scripts/test_deploy_artifact.py` for crawler-specific noindex directives among unrelated meta tags, exact directive-token matching, HTML-comment handling, mixed case/whitespace, and attribute order. Commit: `b256768a6264f231eafbf1e77d3bc5f8af6ba1ba`. The workflow contains a dedicated `python3 -m unittest scripts.test_deploy_artifact -v` step, but it cannot run until the GitHub runner is allocated.
- Re-ran the failed workflow job once. The retry also failed before any step began: runner ID remains `0`, runner name is blank, the step list is empty, and no diagnostic log is available. The corresponding PR run failed in the same way. This points to an Actions job-start/runner problem rather than a test assertion, but the root cause is **not confirmed**. GitHub Status currently reports all systems operational; do not claim the incident is solved or bypass the gate.
- Current tracker recheck: **112 data rows**, 18 columns; BetRivers Casino PA and Hollywood Casino Online PA are both present as distinct research leads, and the ten-market board retains its original GB/BE/SE/DK/ES/IT/NL/DE-SH/CH/Ontario scope. All targets remain HOLD.
- PR #141 remains open, Draft and unmerged with **126 changed files**. No successful current-head CI, fresh preview verification, production deployment or merge is confirmed. Approved consumer reviews remain **0/100**.

**Next:** repository owner needs to inspect Actions settings/runner availability and job-start logs; after a runner is available, execute the complete static-site, tracker, artifact, parser-unit and browser-smoke suite. Then verify a new Cloudflare Pages preview before any release decision.

---

# Latest verified work checkpoint — 24 October 2026, 17:58 UTC

- **Main brand registry:** 207 market-specific rows, 156 distinct global-brand IDs, 205 HOLD and 2 rejected. The 100-name candidate register has a candidate-to-ID map with **39 provisional mappings** (22 exact normalized slugs and 17 explicitly listed aliases) and **61 unresolved names**. These mappings support deduplication only; they do not prove market eligibility or approve reviews.
- **Tier-1 prospect tracker:** 112 rows, 18 columns, zero malformed-width rows and zero duplicate brand/market keys. Four IDs are filled (Casineo.ch → `casineo`, Jollie.de → `jollie`, BetRivers Casino PA → `betrivers-casino`, Hollywood Casino Online PA → `hollywood-casino`); 108 remain blank. There are 110 rows in the international/supplemental US-state research scope and two category exclusions (FR/AU). Domain values: 58 `VERIFY`, two `NOT APPLICABLE`, zero `UNKNOWN`.
- **International board:** ten roadmap markets — GB, BE, SE, DK, ES, IT, NL, DE-SH, CH and Ontario. US-NJ, US-PA and US-MI are supplemental, not replacements for the ten markets. The board has exactly ten priority brand-market targets, all HOLD.
- **Directory QA:** source contains 100 cards with 100 unique titles, including one BetRivers Casino and one Hollywood Casino Online card; Ivy Casino is absent. The Cloudflare branch preview has canonical `https://beincasinos.online/brand-directory/`, robots `noindex,follow`, and a 44-URL sitemap excluding `/brand-directory/`. Production `https://beincasinos.online/brand-directory/` returns 404. No production deployment or indexing release occurred.
- **Pennsylvania accuracy:** the PGCB's 13 February 2026 certificate-holder list names `http://www.hollywoodcasino.com` for slots/table games from 19 Dec 2024; the old `pa.hollywoodcasino.com` URL ended 14 Dec 2023. Current HTTPS canonical/redirect and customer-contracting entity remain open. BetRivers remains a separate HOLD lead.
- **CI:** recent Static site checks runs fail before any step runs and logs are unavailable. The root cause is unconfirmed; GitHub Status currently reports all systems operational and no incident for 24 October. The repository owner should inspect Actions settings, runner availability and workflow permissions. Do not bypass checks.
- **PR #141:** open, Draft, unmerged, with 126 changed files at this checkpoint. **Approved consumer reviews remain 0/100.** No merge or production deployment was performed.

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

5. Restored the international priority board to the original ten-market roadmap: Great Britain, Belgium, Sweden, Denmark, Spain, Italy, the Netherlands, Germany (Schleswig-Holstein only for Tipico), Switzerland and Ontario, Canada. Supplemental US-state research (NJ, PA and MI) is tracked separately and does not replace these ten targets.
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

The master tracker `docs/tier-1-master-prospect-tracker.csv` contains 106 data rows (107 lines including its header). Source-matched IDs are filled for Hollywood Casino Online (PA), BetRivers Casino (PA), Casineo.ch (CH) and Jollie.de (DE); 102 `global_brand_id` fields remain blank. 104 rows are in the current GB/NL/CH/DE/US-state research scope; two rows are explicit FR/AU category exclusions., preventing reliable cross-market deduplication. Its entries are mixed research leads across markets and evidence grades; each still needs the specific follow-up described in its row. Do not represent this as 100 completed reviews.

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
- The master tracker now has 106 rows. Hollywood Casino Online remains HOLD using the newer PGCB-listed `hollywoodcasino.com` route (launch 19 December 2024); only the older `pa.hollywoodcasino.com` route is retired. BetRivers is a separate Pennsylvania HOLD lead. The qualification audit records 58 VERIFY domains, one UNKNOWN and 106 blank global brand IDs.
- Nine noindex parser regression tests passed in an isolated local harness. Current GitHub Actions runs still fail before runner allocation (runner ID 0, no steps/logs); a rerun was requested. The full site build, browser smoke tests and artifact check remain unverified.

## Latest continuation checkpoint — 24 October 2026, 19:35 UTC

- Read-only Cloudflare preview verification was repeated for `/brand-directory/` and `/sitemap.xml`. Preview page returned 200 with canonical `https://beincasinos.online/brand-directory/` and `robots=noindex,follow`; the preview sitemap contains 44 URLs and excludes the directory. Production `https://beincasinos.online/brand-directory/` still returns 404. This is not a production release and does not prove the preview is built from the very latest branch head.
- Current PR #141 head observed through the GitHub API: `b6254cb541276795743a7def195554c971e8db3e`; 124 changed files. PR remains open, Draft and unmerged.
- Latest workflow attempt #1573 (run ID `40118090721`) was retried; attempt 2 still failed in roughly one second with runner ID 0 and no steps. This does not identify a source-code failure; source tests and artifact checks remain unverified on GitHub Actions.
- Reconciled the Pennsylvania status distinction: `hollywoodcasino.com` is listed in the current PGCB certificate-holder PDF for slots/table games with commencement 19 December 2024; only `pa.hollywoodcasino.com` is recorded as a former site ending 14 December 2023. Hollywood remains HOLD. BetRivers is a separate Pennsylvania research lead and does not replace one of the ten roadmap-market priorities.
- The shared robots parser and regression tests are present in source; `scripts/check_deploy_artifact.py` imports `RobotsMetaParser` from `scripts/robots_meta.py`, and the workflow includes `python3 -m unittest scripts.test_deploy_artifact -v`. Successful execution is still pending an allocated runner.
- Tracker remains 106 data rows, 18 columns, no malformed rows/duplicate brand-market keys; 102 global IDs remain blank. Approved consumer reviews remain **0/100**. No merge, production deploy, indexing release, or paid placement was made.

**Next actions:** resolve Actions runner availability with the repository owner; get a current-head preview or deployment identifier before asserting freshness; complete exact customer-contract/current terms and actual usability/accessibility evidence for the ten roadmap targets; reconcile the remaining 102 global brand IDs; obtain independent second reviews.
## Regulatory-source continuation — 24 October 2026, 19:40 UTC

- Re-opened the Swedish regulator's live Betsson Nordic Ltd enforcement page. It still records the 28 May 2025 warning and SEK 6.5 million sanction, the 2 July 2026 administrative-court rejection, and a subsequent appeal to the Administrative Court of Appeal; no later outcome was displayed on the official page checked today. Updated the Sweden dossier and the Betsson (SE) row in docs/brand-research-template.csv to distinguish the first appeal from the pending further appeal and record the check date.
- Official source: https://www.spelinspektionen.se/vara-beslut/beslutslista/betsson-nordic-ltd---varning-penningtvatt/ ; enforcement summary: https://www.spelinspektionen.se/nyhetsarkiv/betsson-nordic-ltd-far-varning-och-sanktionsavgift-for-brister-i-arbetet-mot-penningtvatt/
- Current source changes are documentation-only. They do not change Betsson's HOLD status, do not settle the appeal, and do not count as a completed consumer review.
## Ten-market tracker reconciliation — 24 October 2026, 19:45 UTC

- Identified a material coverage gap: before this pass, the Tier-1 tracker had no market rows for Belgium, Sweden, Denmark, Spain, Italy or Ontario despite the international priority board naming these markets. Added six market-specific records with regulator/source URLs and explicit HOLD blockers: Betano (BE), Betsson (SE), Danske Licens Spil (DK), Luckia (ES), Sisal (IT), and Caesars Casino Ontario (CA-ON).
- Validated the full CSV using a quote-aware parser: 112 data rows; 18 columns; zero malformed-width rows; zero duplicate brand/market keys; 108 blank global IDs; 58 VERIFY domains; zero UNKNOWN domains; two NOT APPLICABLE rows. All six additions remain HOLD; no willingness-to-pay inference or consumer testing is claimed.
- The international board now reflects the reconciled row counts. Approved reviews remain 0/100; no merge, production deployment or indexing release occurred.
## Tracker guardrail and latest CI check — 24 October 2026, 19:50 UTC

- Hardened `scripts/check_prospect_tracker.py` to fail when any of the ten roadmap markets (GB, BE, SE, DK, ES, IT, NL, DE, CH, CA-ON) has no row in the Tier-1 tracker. This prevents the earlier market-coverage gap from silently recurring; it supplements the existing schema and duplicate brand/market checks.
- Current tracker remains 112 rows, 18 columns, zero width errors, zero duplicate brand/market keys, 108 blank global IDs, 58 VERIFY domains, zero UNKNOWN and two NOT APPLICABLE. All six newly added market targets remain HOLD.
- Latest observed PR head is `dda674d2f744d868a60b27bcfa70a658da152383`; PR #141 remains open, Draft and unmerged, with 126 changed files. Workflow run `40118399486` for that exact commit failed before any step ran (runner ID 0; no steps). The code changes have not been validated by a successful CI run.
- Preview QA remains: preview directory 200 with `noindex,follow`, 44-URL sitemap excludes the directory; production directory remains 404. No production deploy or indexing release was made.
