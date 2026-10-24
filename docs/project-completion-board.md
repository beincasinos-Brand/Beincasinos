# Latest repository QA checkpoint — 24 October 2026, 19:50 UTC

- Source-level verification on PR #141 branch: the directory has 100 cards and 100 unique displayed titles; its robots meta is `index,follow`; the canonical `https://beincasinos.online/brand-directory/` is present in the 45-URL source sitemap; `robots.txt` allows crawling and advertises that sitemap. This is the source/branch policy, not proof of current production deployment.
- The directory's 100-row image register contains 50 current candidate-image references; HTML has 50 candidate references, and no candidate has a live `src`. All 50 image candidates remain rights-pending; visible monogram fallbacks remain the safe default.
- The latest production observation still recorded `https://beincasinos.online/brand-directory/` as 404. No merge or production deployment has been performed. The prior Cloudflare preview fetch returned index,follow and 45 sitemap URLs but did not expose its exact deployed commit SHA; do not claim the preview matches this head.
- PR #141 remains open, Draft and unmerged; current connector metadata reports 135 changed files. Tier-1 tracker: 114 data rows, 18 columns, zero malformed-width rows, zero duplicate brand/market keys, 84 blank global-brand IDs, 30 populated ID cells / 29 distinct IDs, 58 VERIFY domains, 111 HOLD rows, one generic Exclude and two category exclusions. The Fanatics Casino NJ row maps to existing canonical ID `fanatics-casino`; its exact current approved domain and legal/skin relationship remain unresolved. A conservative ID reconciliation also populated 13 additional Tier-1 rows from existing registry IDs (Admiral, Ember, Horseshoe MI, Betinia NJ, TOTO, Kansino, Bingoal, BetCity, BetMGM, Monopoly NJ, Hard Rock Bet, theScore Bet, FairPlay NL); ambiguous `Starcasino.nl` and generic `Fun Casino` were left blank. Audit: `docs/research/tier1-global-id-reconciliation-2026-10-24.md`. The 100-card directory and 114 prospect rows are not 100 verified eligible operators or 100 finished reviews.
- BetTOM GB was rechecked against current UKGC entity/trading-name/domain/action records and one official casino welcome-offer page; licence/domain/trading name are listed active, no regulatory actions are listed, and the offer states 5× wagering on bonus funds. Full terms and consumer testing remain incomplete; BetTOM remains HOLD. Evidence: `docs/reviews/internal/bettom-gb-evidence-review-2026-10-24.md`.
- Approved consumer reviews remain **0/100**. Betsson Sweden's current official URL lookup lists both Betsson Nordic Ltd and Spin Nordic Ltd; the exact current contract/license-holder mapping remains unresolved. The existing internal dossier and registry audit now record this conflict. The Danske Spil dossier has a fresh official regulator/consumer-page check; its public terms still display 2022/2023 effective-date language.
- Added `scripts/check_tracker_registry_links.py` plus seven unit tests; the gate compares exact case-insensitive brand-name matches to canonical IDs, rejects missing/mismatched IDs when the registry has one unambiguous ID, and leaves ambiguous/alias cases for manual review. The workflow now runs on pushes to all branches and includes the new checker/tests. A JS-side comparison of the current tracker/registry found five exact-name matches; all five now carry the same single canonical ID in both files. Python/CI execution is still unconfirmed.
- A cross-branch comparison confirms the same runner ID 0 / empty runner / no-step symptom on `main`, the PR base branch and this PR branch; GitHub's public status page currently reports all systems operational. No root cause is confirmed. See `docs/quality/github-actions-runner-failure-triage-2026-10-24.md`.
- Latest current-head run [40126884702](https://github.com/beincasinos-Brand/Beincasinos/actions/runs/40126884702) on commit `0645e12451f67ac140619486bd607a8a52c429c4` failed before any steps; no Python/site/artifact/browser test has been executed by that run. The current checker now also rejects tracker IDs absent from the canonical registry and has seven regression tests; the conflict test was corrected to accept both the unknown-ID and exact-name mismatch diagnostics. Their CI execution remains blocked by the runner-start failure.
- Indexability policy is now stated explicitly for this branch: the directory is a transparent, indexable **research queue**, not a recommendation/ranking or a set of completed reviews. Internal evidence drafts remain outside public routes and artifact allowlists. Keep the production release blocked until current-head build/browser checks pass and the owner authorizes deployment.

**Next:** obtain a successful full workflow run on the current PR head; verify Cloudflare preview freshness and the production route only after explicit release authorization; continue market-specific source evidence, rights clearance, independent review and legal/editorial approval.

---

# Historical repository QA checkpoint — 24 October 2026, 19:28 UTC

- The latest live fetch of the Cloudflare branch-preview alias returns `/brand-directory/` with `index,follow` and canonical `https://beincasinos.online/brand-directory/`; `/sitemap.xml` contains 45 URLs including the research directory. The fetched page reports zero loaded brand images, consistent with the image-rights gate. The fetch did not expose the exact deployed commit SHA.
- Production `https://beincasinos.online/brand-directory/` was last observed as 404; no production deployment or merge has been made. Treat production availability as a remaining release blocker until the owner approves deployment and the live route is verified.
- Image-rights gate remains in place: 50 logo candidate URLs are retained in a 50-row internal register and metadata only; all 50 images have no live `src`, and neutral CSS monogram fallbacks are visible. Source checker and browser smoke coverage enforce the policy; CI has not executed these checks.
- Latest observed Static site checks run `40125391224` on earlier head `703df230` failed before any step: runner ID 0, empty runner name and no steps. Job logs remain unavailable. The current PR head `21ff2973` has no associated workflow run visible yet; a previous retry of run `40123489402` (attempt 2) had the same runner-allocation failure. CI is not passing, but these failures do not establish a code/test failure. GitHub Status currently reports services operational; the repository-specific runner-allocation cause remains unknown.
- PR #141 remains open, Draft and unmerged, with 130 changed files. The Tier-1 tracker has 114 market-specific rows, 98 blank global IDs, 58 VERIFY domains, and 111 HOLD plus 3 exclusions (one generic and two market/category-specific). The main registry has 208 market-specific rows across 157 global IDs (206 HOLD, 2 rejected). The 100-name candidate-to-ID map now has 70 provisional mappings (22 exact-name matches and 48 aliases) and 30 unresolved names; these are identity mappings only. The 100-name candidate register is not 100 verified brands. Approved reviews remain **0/100**.

**Next:** investigate the Actions runner allocation failure, obtain authorization before production deployment, verify the production directory route after release, and continue the evidence-led consumer review process with actual usability/accessibility testing and independent sign-off.

---
# Indexability decision correction — 24 October 2026, 19:02 UTC

- Corrected a source-level contradiction found during diff review: `scripts/check_site.py` explicitly requires the 100-card research directory to be `index,follow` and describes it as discoverable for transparency, while the page itself said `noindex,follow` and the sitemap omitted it. The page now declares `index,follow`, its notice no longer claims it is noindex, and the canonical sitemap now contains `https://beincasinos.online/brand-directory/` (45 source sitemap URLs).
- The latest live branch-preview fetch still shows the previous deployed version (`noindex,follow`, 44 sitemap URLs, zero logo image loads) and production `/brand-directory/` still returns 404. Cloudflare's PR bot now reports build in progress for commit `8e7a25b`; recheck after that build completes. Do not claim the corrected indexability metadata is live yet.
- The source now aligns with the existing site-checker's stated policy; deployment-artifact validation should expect the directory URL in the sitemap because its robots meta is index,follow. The route remains a transparent research queue, not a review or recommendation; it explicitly states 0/100 approved reviews.
- Latest Actions run `40123381011` failed before any test step. The job reports runner ID 0, blank runner name, and no steps. GitHub's public status page reports Actions operational, so the cause remains repository-specific/unknown. No test result is available; do not label tests passed or source code failed on the basis of this runner failure.

**Next:** verify Cloudflare's new preview after commit `8e7a25b` finishes, check sitemap count/robots/canonical against the deployed HTML, and investigate runner allocation with repository/Actions settings or GitHub Support. Production deploy/merge remains unauthorized.

---
# Latest verified checkpoint — 24 October 2026, 19:00 UTC

- Brand-directory source and live preview agree: 100 research cards; 50 logo candidates retained in the rights register and HTML metadata; zero candidate image tags have a live `src`; 50 monogram fallbacks are visible. The latest branch preview fetch reports zero loaded images. CSS-only abstract artwork now gives the fallback panels a more polished, original treatment.
- The candidate register has 50 rows / 11 columns, no malformed CSV rows, no duplicate candidate URLs, and exact one-to-one correspondence with the 50 `data-candidate-src` URLs in the HTML. All remain `PENDING — permission not evidenced` and `NOT LOADED — visible monogram fallback`.
- The static checker enforces the image-rights gate. The Chromium smoke suite now includes the brand directory route and tests search for `admiral.ch`, clear/reset behavior, at least 50 cards, zero remote `src` values for pending images and visible fallbacks. These tests have not executed because the runner never starts.
- 888casino GB dossier and master research CSV now use the live UK User Agreement body date of 30 September 2026 (fetched 24 October), and explicitly record the page-metadata mismatch: metadata says Cassava Enterprises (Gibraltar) Limited while substantive UK clause 2 identifies 888 UK Limited / UKGC account 39028.
- Latest current-head Actions run `40123230562` failed in under a few seconds with `runner_id: 0`, no runner name and no steps. A rerun of the prior PR job also failed without starting. Public GitHub Status currently shows systems operational, so the repository-specific cause is **unknown**; do not label the source tests failed or passed. [GitHub Status](https://www.githubstatus.com/).
- Live Cloudflare branch preview still serves `/brand-directory/` as `noindex,follow` with canonical `https://beincasinos.online/brand-directory/`; production `/brand-directory/` remains 404. The branch preview's sitemap lists 44 canonical URLs and excludes the noindex directory. No merge or production deployment was made.
- PR #141 remains open, Draft and unmerged. Latest changed-file count before this checkpoint: 130. Approved consumer reviews remain **0/100**; the 100-name register and 114-row Tier-1 tracker are research queues, not approved reviews.

**Next:** resolve repository-specific Actions runner allocation, decide whether the research directory should be available on production or remain preview-only, run the new browser smoke suite, and continue consumer-terms/cashier evidence plus actual usability/accessibility tests on held profiles.

---
# Latest image-rights and evidence update — 24 October 2026, 18:58 UTC

- Audited the live Cloudflare branch preview and source for the 100-card brand directory. It previously loaded 50 external brand-logo candidates despite labelling them rights pending. Fixed the HTML/JS so all 50 URLs remain only in `data-candidate-src`, all candidate images have `data-image-rights="pending"` and no `src`, and neutral monogram fallbacks are visible. No unapproved logo image requests should occur.
- Created `docs/image-rights-candidate-register-2026-10-24.csv` with 50 candidate rows, official-site URL candidates, market, rights state, display state and required clearance steps. Permission is not assumed from an official-site source.
- Added source-level enforcement to `scripts/check_site.py`: pending logo candidates must not have a live `src`, must retain a candidate URL and must be hidden behind a visible monogram fallback. Added `/brand-directory/` to Chromium smoke routes and smoke checks for directory card count, pending-image blocking, search filtering and clear/reset.
- Static source validation through CSV parsing confirmed 114 Tier-1 market rows, 18 columns, zero malformed rows, zero duplicate brand/market keys, 99 blank global IDs, 58 VERIFY domains, 111 HOLD rows, one generic Exclude and two market/category exclusions. Main research CSV has 207 rows, 33 columns, zero malformed rows; 888casino GB entry now reflects the live UK agreement's body date of **30 September 2026**, fetched 24 October, superseding the old 5 August/version 64.0 note.
- Live preview recheck after the HTML change reports **0 loaded images** on the directory and retains the `noindex,follow` policy. The route works on the branch preview, but production `/brand-directory/` still returns 404. Production deployment/merge remains unauthorized.
- Latest Static site checks run `40123065066` failed before meaningful execution (job had no steps; earlier attempts show runner ID 0 and no logs). Do not interpret this as a code-test failure or a pass. Latest PR #141 remains Draft/open/unmerged; no green CI confirmed.

**Next:** resolve the CI runner/service failure, confirm the directory's intended production visibility, run the new browser smoke checks when a runner is available, and continue first-party terms/cashier capture for the remaining target reviews. Approved reviews remain **0/100**; all profiles remain HOLD until independent review and actual usability/accessibility tests are complete.

---
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

# Latest work checkpoint — 24 October 2026, 18:42 UTC

- Added and linked a dedicated US-state supplemental queue covering Ember Casino (NJ), BetMGM (NJ), BetRivers Casino (PA), Hollywood Casino Online (PA), and Horseshoe Online Casino (MI). It preserves the ten-market international board instead of quietly changing its market scope.
- Rechecked the master prospect tracker with a CSV-aware parser: **114 data rows, 18 columns, zero malformed rows, zero duplicate brand/market keys, all 10 roadmap markets represented, 99 blank global-brand IDs, 58 blank/VERIFY domains, 111 rows marked HOLD**. These are research-lead counts, not 100 completed reviews. BetRivers PA and Hollywood Casino Online PA remain separate HOLD entries; the latter dossier distinguishes the retired legacy pa.hollywoodcasino.com route from the later PGCB-listed hollywoodcasino.com route.
- The latest Static site checks rerun is still failing before a runner starts: run 40120514437, attempt 2, job 120954831508, runner ID 0, zero steps, and unavailable logs. This does not identify a code failure; CI remains unresolved. No successful current-head CI is claimed.
- PR #141 remains open, Draft and unmerged. No production deployment or merge was performed. Approved reviews remain **0/100**; all candidates stay HOLD until consumer evidence, current terms, accessibility/usability testing, image rights and independent review are complete.

**Next:** resolve the CI runner/service issue, run the static checks on an actual runner, continue exact terms/cashier capture for the international priority targets, and complete the independent-review gates.

---

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

- **Main brand registry:** 208 market-specific rows, 157 distinct global-brand IDs, 206 HOLD and 2 rejected. The 100-name candidate register has a candidate-to-ID map with **70 provisional mappings** (22 exact-name matches and 48 explicitly mapped aliases) and **30 unresolved names**. These mappings support deduplication only; they do not prove market eligibility or approve reviews.
- **Tier-1 prospect tracker:** 112 rows, 18 columns, zero malformed-width rows and zero duplicate brand/market keys. Four IDs are filled (Casineo.ch → `casineo`, Jollie.de → `jollie`, BetRivers Casino PA → `betrivers-casino`, Hollywood Casino Online PA → `hollywood-casino`); 108 remain blank. There are 110 rows in the international/supplemental US-state research scope and two category exclusions (FR/AU). Domain values: 58 `VERIFY`, two `NOT APPLICABLE`, zero `UNKNOWN`.
- **International board:** ten roadmap markets — GB, BE, SE, DK, ES, IT, NL, DE-SH, CH and Ontario. US-NJ, US-PA and US-MI are supplemental, not replacements for the ten markets. The board has exactly ten priority brand-market targets, all HOLD.
- **Directory QA:** source contains 100 cards with 100 unique titles, including one BetRivers Casino and one Hollywood Casino Online card; Ivy Casino is absent. The Cloudflare branch preview has canonical `https://beincasinos.online/brand-directory/`, robots `noindex,follow`, and a 44-URL sitemap excluding `/brand-directory/`. Production `https://beincasinos.online/brand-directory/` returns 404. No production deployment or indexing release occurred.
- **Pennsylvania accuracy:** the PGCB's 13 February 2026 certificate-holder list names `http://www.hollywoodcasino.com` for slots/table games from 19 Dec 2024; the old `pa.hollywoodcasino.com` URL ended 14 Dec 2023. Current HTTPS canonical/redirect and customer-contracting entity remain open. BetRivers remains a separate HOLD lead.
- **CI:** recent Static site checks runs fail before any step runs and logs are unavailable. The root cause is unconfirmed; GitHub Status currently reports all systems operational and no incident for 24 October. The repository owner should inspect Actions settings, runner availability and workflow permissions. Do not bypass checks.
- **PR #141:** open, Draft, unmerged, with 126 changed files at this checkpoint. **Approved consumer reviews remain 0/100.** No merge or production deployment was performed.

---



# Tracker reconciliation checkpoint — 24 October 2026, 19:45 UTC

- Added six market-specific target records to `docs/tier-1-master-prospect-tracker.csv` so the tracker represents all ten roadmap markets, not only GB/NL/CH/DE and US-state leads: Betano Casino Belgium (BE), Betsson Casino Sweden (SE), Danske Licens Spil Casino (DK), Luckia Casino Spain (ES), Sisal Casino Italy (IT), and Caesars Casino Ontario (CA-ON). Each row has regulator/source references, explicit HOLD status, market-specific blockers, and no inferred willingness-to-pay claim.
- Re-parsed the full CSV with quote-aware handling: **112 data rows, 18 columns, zero width errors, zero duplicate brand/market keys, 108 blank global brand IDs, 58 VERIFY domains, zero UNKNOWN and two NOT APPLICABLE**. The six new rows are source-backed research leads, not completed reviews.
- Updated the international priority board count to match the tracker. Approved reviews remain **0/100**. The PR is still Draft/unmerged and CI remains blocked by runner allocation; no deployment was made.
---

# Tracker coverage guardrail — 24 October 2026, 19:50 UTC

- `scripts/check_prospect_tracker.py` now requires at least one tracker row in each roadmap market: GB, BE, SE, DK, ES, IT, NL, DE, CH and CA-ON. The goal is to prevent the six-market omission identified during the latest audit.
- The latest quote-aware tracker audit reports 112 data rows, 18 columns, zero malformed-width rows, zero duplicate brand/market keys, 108 blank global IDs, 58 VERIFY domains, zero UNKNOWN and two NOT APPLICABLE.
- Latest observed PR head `dda674d2f744d868a60b27bcfa70a658da152383` still has no successful CI: run `40118399486` failed before runner allocation. Release remains blocked; approved reviews remain 0/100.


## Follow-up verification — 24 October 2026

- Rechecked the 18-column Tier-1 prospect tracker using a CSV-aware parser: 114 data rows, 0 malformed rows, 0 duplicate brand/market keys, 99 blank global brand IDs; Betano Belgium and Hollywood Casino Online Pennsylvania each have explicit market-specific rows and remain HOLD.
- Corrected the Pennsylvania brand interpretation: `pa.hollywoodcasino.com` is the former skin (ended 14 Dec 2023), while the PGCB's 13 Feb 2026 list identifies `http://www.hollywoodcasino.com` for slots/table games from 19 Dec 2024. The newer route is a research lead, not yet a completed review; verify HTTPS redirect and current customer-contracting entity.
- Reconfirmed Betano Belgium's current live regulator table dates in both English/French views as 12 Nov 2024 decision and 31 Dec 2026 expiry. Do not reuse the stale indexed 2019/2034 snippet; recheck before publication.
- Re-ran the failed GitHub Actions job once. Attempt 2 failed at runner allocation with no steps, so no code-level CI result is available.


# Betsuna GB evidence refresh — 24 October 2026 (continued work)

- Re-read the UK-specific Betsuna homepage, FAQ and terms alongside the UKGC account, domain and sanction records. Updated the existing internal dossier and the single Betsuna/GB tracker row.
- New customer-facing facts recorded with source links: current UK welcome offer advertises 100% up to £100 + 50 spins with stated 10x wagering rules; UK terms state a 1% withdrawal processing fee capped at £3, while the FAQ says processing within 3 business days and funds generally arrive within 7 business days; terms describe customer funds as segregated but not protected in insolvency; UKGC domain list labels betsuna.com White Label under ProgressPlay Limited.
- Corrected the tracker’s enforcement date to the official decision date **9 May 2025** (not the 21 August 2025 news-publication date). The £1m sanction, warning, licence condition and required third-party audit are recorded; current audit/remediation outcome remains unverified.
- No account registration, deposit, gameplay, support or withdrawal test was performed. No quality score or recommendation is approved; Betsuna remains HOLD and willingness to pay remains unconfirmed.
- Evidence draft: `docs/reviews/internal/betsuna-gb-evidence-review-2026-10-24.md`. Tracker: `docs/tier-1-master-prospect-tracker.csv`.


# First 100 review-production ledger — 24 October 2026

- Created `docs/targets/100-brand-review-production-ledger-2026-10-24.csv`: 100 unique candidate identities selected from the current scoped registry with a round-robin spread across 15 market codes. This is a controlled worklist, **not** a claim that 100 brands are verified or that 100 reviews are complete.
- The ledger has 30 columns covering official domain, legal entity, regulator/register, terms, withdrawals, complaints, safer-gambling, bonus source/date/status, image source/rights, nine weighted score components, overall score, review/publication state and blockers.
- Re-parsed the written CSV with quote-aware handling: **100 data rows, 30 columns, zero malformed rows**. All 100 bonus entries are explicitly NOT CAPTURED pending current market-specific offer and full terms; all 100 image-rights fields are PENDING; no overall consumer score is assigned; every publication decision remains HOLD.
- Added `docs/targets/100-brand-review-production-protocol-2026-10-24.md` defining the 100-point evidence-first rubric: licence/scope 20, payments 18, safer gambling 15, product 12, bonus 10, complaints/support 10, usability/accessibility 8, privacy/security 4 and evidence/editorial clarity 3. Missing evidence is NOT SCORED; critical licence/domain/legal/safety conflicts block scoring and publication.
- Current approved consumer-review count remains **0/100**. No public directory cards, production pages, logos, bonus claims or scores were promoted by this internal ledger. No merge or Cloudflare production deployment was performed.


## Bonus source research — 24 October 2026

- Captured six first-party Great Britain bonus offer snapshots for bet365 Casino, 888casino, Betfred Casino, Sky Vegas, Coral Casino and Grosvenor Casinos, and entered their official offer URLs, check date and key conditions into the internal 100-brand ledger.
- Created `docs/reviews/internal/gb-bonus-snapshot-batch-2026-10-24.md` with source links and caveats. Sky Vegas is explicitly marked CONFLICT because the homepage advertises 250 spins while the promotions page describes a 50-spin offer/£10 deposit-and-stake path; no definitive bonus headline should be published until reconciled.
- Ledger QA after these edits: 100 rows, 30 columns, zero malformed rows. Six offers have dated source snapshots; 94 rows remain without a captured offer URL. Image-rights fields remain pending across the ledger, all scores remain withheld, and all 100 publication decisions remain HOLD.
- These are operator-published offer snapshots only. No account was opened, offer claimed, deposit made, game played, support contacted or withdrawal tested. Approved consumer reviews remain 0/100.


## Regulator evidence batch — 24 October 2026

- Added [internal regulator evidence batch 01](reviews/internal/regulator-evidence-batch-01-2026-10-24.md), documenting primary-source checks for bet365 Casino (GB), Casino777.be (BE), ComeOn Casino (SE), TOTO Casino (NL), MERKUR Spiel (Schleswig-Holstein only) and Jackpots.ch (CH).
- Updated the matching six ledger blocker/evidence notes. Key diligence: the UKGC register shows an active bet365 Casino Remote licence for Hillside (UK Gaming) ENC, and the UKGC also records a 2024 settlement requiring £343,035 in lieu of penalty/costs for historic AML and customer-harm failings; that history must be reflected fairly. The other records are scoped to the exact market/state described and are not evidence of service quality.
- This is regulator-source verification only. All six remain NOT SCORED / HOLD while consumer terms, payments, current bonus terms, safer gambling, complaints/ADR, privacy/cookies, accessibility, image rights and independent review remain incomplete. No customer accounts, deposits or hands-on tests were performed.


## Regulator evidence batch 02 — 24 October 2026

- Added [internal regulator evidence batch 02](reviews/internal/regulator-evidence-batch-02-2026-10-24.md) for candidates 7–15: Lottomatica (IT), Codere (ES), Caesars Palace Online (Ontario), PlayNow (BC), Loto-Québec, Borgata (NJ), BetMGM (MI), betPARX (PA) and Betano (DE).
- Updated the nine matching ledger blocker/evidence notes. Corrected betPARX's candidate URL to the Pennsylvania-specific `https://pa.betparx.com`. The Betano evidence found permission for virtual slots and sports betting, not a separate table/live-casino permission; the ledger explicitly retains that product-scope limitation.
- The batch-01 and batch-02 notes now cover regulator-source checks for 15 of 100 candidate rows. These remain source checks only, not finished reviews; scores are withheld and publication remains HOLD.


## Regulator evidence batch 03 — 24 October 2026

- Added [internal regulator evidence batch 03](reviews/internal/regulator-evidence-batch-03-2026-10-24.md) for candidates 17–25: Napoleon Casino (BE), Unibet (SE), Winnitt (NL), Tipico (DE-SH), Mycasino.ch (CH), Sisal (IT), Luckia (ES), DraftKings (Ontario) and Espacejeux (Québec).
- Updated nine ledger blocker/evidence notes with market-specific official-source findings. The batch flags unresolved DraftKings Ontario domain mapping and possible Espacejeux/Loto-Québec duplicate identity, and preserves Tipico's Schleswig-Holstein-only online-casino scope.
- Batches 01–03 now document dated regulator evidence for 24 candidate rows (row 16 also has an official offer snapshot but remains incomplete). These are source checks, not approved reviews; all candidates remain HOLD and no score is assigned.


## Regulator evidence batch 04 — 24 October 2026

- Added [internal regulator evidence batch 04](reviews/internal/regulator-evidence-batch-04-2026-10-24.md) for candidates 26–35.
- Updated ten ledger rows with dated regulator-source evidence. Material current findings include Betfred's £900,000-in-lieu settlement announced 30 June 2026 for remote customer-interaction/social-responsibility failings, plus its £240,000 technical-standards penalty in 2025; Betsson's SEK 6.5m AML sanction upheld by the administrative court in July 2026 with further appeal noted; and Betway's GGL entry supporting virtual slots/sports betting, not a separately evidenced full online casino.
- Batches 01–04 now provide dated regulator evidence for 34/100 candidates; 888casino (row 16) also has a regulator record URL and official bonus snapshot. This is not review completion. All 100 remain HOLD and no scores are assigned.


## Regulator evidence batch 05 — 24 October 2026

- Added [internal regulator evidence batch 05](reviews/internal/regulator-evidence-batch-05-2026-10-24.md) for candidates 36–45 and updated ten ledger blockers/evidence notes.
- Findings preserve important limits: LeoVegas Germany's official record covers sports betting/virtual slots, not separately evidenced table/live casino; Paddy Power Games' exact casino licensee is unresolved and the UKGC's 2025 review found social-responsibility remote customer-interaction failings across four Paddy Power/Betfair licensees.
- Batches 01–05 now provide dated regulator-source evidence for 44/100 candidate rows; row 16 / 888casino also has an official UKGC record URL and official bonus snapshot. These are source checks, not finished reviews. All 100 remain HOLD and unscored.


## Regulator evidence batch 06 — 24 October 2026

- Added [internal regulator evidence batch 06](reviews/internal/regulator-evidence-batch-06-2026-10-24.md) for candidates 46–55 and updated ten ledger notes.
- Evidence covers Sportium (IT), Fuegocasino (ES), Hard Rock Bet (Ontario), Monopoly Casino (NJ), Horseshoe (MI), Casumo (DE), Sky Vegas (GB), PokerStars (BE), Pop Casino (SE) and Fair Play Casino (NL). Sky Vegas's 250-vs-50 spin conflict remains unresolved; Casumo's German record supports virtual slots, not a separately evidenced full online casino; Fuegocasino and PlatinCasino share the same DGOJ operator and need distinct-product checks.
- Batches 01–06 now document dated regulator evidence for 54/100 candidates, including row 16's existing UKGC record and offer snapshot. This is not review completion; all 100 remain HOLD and unscored.


## Regulator evidence batch 07 — 24 October 2026

- Added [internal regulator evidence batch 07](reviews/internal/regulator-evidence-batch-07-2026-10-24.md) for candidates 56–65 and updated ten ledger notes.
- Evidence covers 7melons.ch (CH), Admiral Bet (IT), AdmiralBet.es (ES), Golden Nugget (Ontario and Michigan), PartyCasino (NJ), Winfest (DE), William Hill (GB), Ladbrokes (BE) and Svenska Spel (SE). Source freshness and product scope are retained as blockers where needed, including Winfest's virtual-slots-only evidence and Admiral Bet's dated 2024 terms PDF.
- Batches 01–07 now document dated regulator evidence for 64/100 candidates, plus 888casino's existing UKGC record/offer snapshot. All candidates remain HOLD and unscored; this is not review completion.


## Public directory score/bonus completeness pass — 24 October 2026

- Updated all 100 research cards in `brand-directory/index.html` to show an explicit **Editorial rating: Not scored** state and **Bonus offer: Not cleared** state, each with an explanation. This removes empty-looking score/bonus slots without inventing ratings, current offers, wagering terms or eligibility claims.
- Reworked hero metrics to show 0/100 editorial scores cleared and 0/100 bonus offers cleared for publication.
- Added responsive `.card-readiness` styling to `brand-directory/directory.css`.
- Extended `scripts/check_site.py` so every card must contain the readiness panel, both exact status labels and non-empty explanatory notes.
- Source inspection: 100 cards, 100 readiness panels, 100 explicit not-scored states, 100 not-cleared bonus states. This is static source validation only; current-head CI/browser execution remains unresolved due to runner allocation failures.
- This does **not** mean 100 reviews or bonuses are complete. All remain HOLD until market-specific source checks, full terms, review evidence and independent approval pass. No merge, Cloudflare production deployment or DNS change.


# Review-ledger gate update — 24 October 2026

- Added `scripts/check_review_ledger.py` and connected it to `.github/workflows/site-check.yml`. It checks the 100-row ledger schema, unique brand/market identities, HTTPS source URLs, ISO-formatted bonus-check dates, score bounds, all-or-nothing nine-part rubric scoring, and publication-state hard gates.
- Added four regression cases in `scripts/test_review_ledger.py`: a held/unscored candidate set, partial-score rejection, duplicate identity rejection, and rejection of publication without evidence and image rights. The workflow now runs these tests.
- This is a source change only. Python execution, workflow/runner success and browser tests are not confirmed. Existing GitHub Actions runner allocation failures remain a separate blocker.
- No candidate was promoted, no score was fabricated, no logo rights were presumed, and no Cloudflare production deployment or PR merge was performed. Approved reviews remain **0/100** until actual evidence and independent sign-off are complete.


# Full-review evidence schema expansion — 24 October 2026

- Expanded the 100-brand ledger from 30 to 43 columns with explicit evidence slots for deposit methods, fees/limits, privacy/cookies, accessibility, regulatory actions and ADR, plus named primary/secondary reviewers, independent-review date, editorial-approval date, consumer-test status, affiliate-disclosure status and evidence-bundle path.
- All 100 rows explicitly say `NOT PERFORMED` for consumer/usability testing and `NOT REVIEWED` for affiliate disclosure; these are honest blockers, not assumed completion.
- The review-ledger validator now requires those fields in the schema and blocks publication unless the required evidence sources, distinct reviewers, dated approvals, completed consumer/usability testing, reviewed disclosure, consistent nine-part score and cleared image rights are present. Five regression tests cover held/unscored rows, partial scoring, score-total mismatch, duplicate identities, and publication without evidence/rights.
- Source-only update; Python/Actions/browser execution remains unconfirmed due to the existing runner-allocation issue. No merge or Cloudflare production deploy. Approved consumer reviews remain **0/100**.


# Market-specific bonus source pass — 24 October 2026

- Captured dated official promotion-page observations for TOTO Casino (Netherlands) and Lottomatica (Italy) in the 43-column ledger, increasing the number of official bonus-source URLs recorded from six to eight. Internal evidence note: `docs/reviews/internal/bonus-snapshot-toto-nl-lottomatica-it-2026-10-24.md`.
- TOTO's official promotions page showed separate 200-free-spins and €50 live-casino free-chip headlines with qualifying-play conditions; Lottomatica's official page advertised “up to €10,030” for new registrants with an indicated validity window through 1 November 2026. These are volatile headlines, not complete bonus-term verifications.
- Both rows remain `NOT CLEARED FOR PUBLICATION`; wagering, expiry, eligible games, maximum cashout, exclusions and complete offer terms still require reconciliation. No offer was promoted to a public review, and no first-hand gameplay/payment testing is claimed.


# Second market-specific bonus evidence pass — 24 October 2026

- Added official-page snapshots for ComeOn Sweden and PlayNow British Columbia to `docs/reviews/internal/bonus-snapshot-comeon-se-playnow-bc-2026-10-24.md`; the ledger now has ten official bonus-source URLs recorded across the candidate list.
- PlayNow's official 2026/2027 PDF states the BC period 1 April 2026–31 March 2027, $5 minimum initial deposit, up to $1,500 match, 100% spend-through of the initial deposit, 20x token wagering, 14-day token use window and 30-day held-funds expiry; exclusions include Live Casino, Baccarat, Sic Bo and Roulette. Recheck before publication.
- ComeOn Sweden's official page describes a 300% bonus up to SEK 750, 100 spins, SEK 250 minimum deposit and 20x wagering, but its stated start date is anomalous (`04/06/224`) and the page's current validity is not established. It remains explicitly date-conflicted and on HOLD.
- Both records remain not cleared for publication. These observations do not constitute a consumer experience test, and no bonus was claimed.


# Third market-specific bonus evidence pass — 24 October 2026

- Added an official Casino777 Belgium promotion snapshot at `docs/reviews/internal/bonus-snapshot-casino777-be-2026-10-24.md`. The ledger now records eleven official bonus/promotion source URLs.
- The observed 777 Boost is explicitly classified as a game-specific promotion (1000% boost on a qualifying €5+ win up to €50, subject to game, account and age restrictions), not a welcome deposit bonus. Its current availability still requires a fresh check before publication.
- The source and current observation are recorded; the brand remains on HOLD pending all other review gates. No account or gameplay test was performed.


# Final source-integrity sweep — 24 October 2026

- Normalized the Hollywood Casino (PA) candidate URL to its HTTPS official domain after checking the current official homepage; a ledger URL audit found and corrected the only populated URL field using HTTP.
- Current ledger source audit: 100 candidate rows, 43 columns, 100 unique brand/market identities, 11 official bonus/promotion source URLs, zero numeric scores assigned, zero cleared image-rights rows, 100 consumer tests marked `NOT PERFORMED`, and 100 affiliate-disclosure states marked `NOT REVIEWED`.
- The explicit “NOT SCORED” value is allowed as a transparent unscored state; the gate still rejects partial component scores and requires all nine numeric components plus a matching total before any numeric score can be treated as complete.
- Latest workflow attempts continue to fail before any steps start (runner ID 0, no runner name/steps). This is not a test result. No merge, production deployment, public bonus claim or review approval has been made.


# Pre-launch indexing safety correction — 24 October 2026

- Reconciled a launch-safety contradiction: the site had been configured to allow all crawlers despite prior explicit instructions not to enable indexing before launch approval. `robots.txt` now uses `Disallow: /` and retains the sitemap URL for later readiness.
- Updated the deployment-artifact validator to require the pre-launch crawl block and reject a site-wide allow rule. This is a guardrail change only; it does not alter DNS, nameservers, Cloudflare deployment, or PR merge status.
- Public HTML may retain its future launch-ready canonical/index directives, but the published artifact must remain crawl-blocked until legal/privacy/affiliate checks, browser/accessibility verification, domain/DNS/email review and explicit launch approval are complete. A robots block is not a security boundary and does not remove already indexed content by itself.


# Fourth market-specific bonus evidence pass and launch-safety fix — 24 October 2026

- Added official-page research for Jackpots.ch (Switzerland) and Unibet (Sweden), increasing ledger bonus/promotion source URLs to **13**. Internal note: `docs/reviews/internal/bonus-snapshot-jackpots-ch-unibet-se-2026-10-24.md`.
- Jackpots.ch's official welcome page breaks its CHF 2,200 + 200 spins headline into four deposit stages; the bonus-conditions page states a default one-month playthrough deadline, while the payment page describes 3–4 working-day payout release and Swiss-bank-account ownership restrictions. Exact stage-by-stage wagering/cashout/exclusion terms remain outstanding.
- Unibet Sweden's official bonus page describes either SEK 100 for 50 Pirots 4 spins with 1x wagering, or a 100% deposit bonus up to SEK 1,000 with a SEK 200 minimum and 30x wagering. It also states a SEK 25 maximum bonus-play bet, up to 60-day validity, Sweden residence, and one bonus per player/household/payment method. Exact wagering base, exclusions and an account-eligibility contradiction require reconciliation.
- Both rows remain HOLD. No account, deposit, claim, gameplay, support or withdrawal test was performed.
- Corrected the pre-launch crawler policy: `robots.txt` now disallows crawling, and `scripts/check_deploy_artifact.py` requires that block and rejects a site-wide allow rule. This restores the previously authorized no-indexing-before-launch posture. No DNS/nameserver change, merge or production deployment was made.


# Crawl-block regression coverage — 24 October 2026

- Added two regression tests to `scripts/test_deploy_artifact.py`: verify the source `robots.txt` blocks all crawlers pre-launch, and verify the canonical sitemap directive remains prepared for a later approved release.
- The latest Actions job still exits before its first step with `runner_id: 0`, blank runner name and no steps. This is an infrastructure/runner allocation failure, not evidence that source checks passed or failed.


# Fifth market-specific bonus evidence pass — Switzerland — 24 October 2026

- Added official-page bonus sources for Mycasino.ch, 7Melons.ch, Pasino.ch and Casineo.ch. The ledger now has **17** official bonus/promotion source URLs, each tied to its candidate market. Detailed source note: `docs/reviews/internal/bonus-snapshot-mycasino-7melons-pasino-casineo-ch-2026-10-24.md`.
- Mycasino's public hub lists a first-deposit offer and a 99-spin verification bonus but the exact welcome terms were not exposed; the row remains held.
- 7Melons lists two welcome choices (100% up to CHF 100 + 250 spins, or 100% up to CHF 300 + 50 super spins), but the exact wagering bases/expiry/cashout are not captured; held.
- Pasino's detailed offer says 100% up to CHF 500, CHF 10 minimum, 350 spins across six instalments, 35x wagering within 30 days, and six-day spin validity; the detailed page and promotion hub disagree on the eligible spin game, so it remains held.
- Casineo lists CHF 15 credit via TREAT15 until “14 November” without a clearly rendered year; bonus conditions specify a one-month default bonus validity and CHF 10 maximum bonus wager per round. Offer year and current status remain unresolved; held.
- No account, deposit, bonus claim, gameplay, support contact or withdrawal test was performed. No ratings were assigned.


# Sixth market-specific bonus evidence pass — Ontario — 24 October 2026

- Added official Ontario-source checks for OLG.ca, BET99 and Hard Rock Bet; ledger now has **20** official bonus/promotion source URLs. Internal note: `docs/reviews/internal/bonus-snapshot-olg-bet99-hardrock-ontario-2026-10-24.md`.
- OLG's offer detail shows a $25 deposit minimum, $25 qualifying casino-game bet, $250 bonus, 10x wagering and 14-day conversion deadline, while the promotions index summary says $15 minimum deposit; explicitly flagged for reconciliation.
- BET99's official Help Centre states a 100% first-deposit match up to CAD $1,000, code CASINO99, 30x wagering within 30 days and game contribution differences (slots 100%, live/table/crash 10%, progressive/video poker 0%). Its live promotion page was inaccessible to automated retrieval, so current offer/eligibility is not cleared.
- Hard Rock Bet's Ontario-specific offer page describes 200 Sweet Bonanza spins worth CAD $40 after a CAD $10 deposit and up to CAD $1,000 slot lossback with 1x wagering within 14 days; contractual/current terms still need confirmation.
- All three rows remain HOLD; no account, deposit, claim, game, support or withdrawal test was performed.


# CI runner blocker tracked — 24 October 2026

- Opened [Issue #143](https://github.com/beincasinos-Brand/BeIncasinos/issues/143) for the repeated GitHub Actions runner-allocation failure.
- Latest run `40137160128` and prior runs terminate before the first step with `runner_id: 0`, blank runner name and no steps. A retry also failed before steps began.
- The workflow has not validated source, built the Cloudflare artifact or run browser/a11y checks. This issue is an infrastructure blocker; it must not be misreported as a test pass or source-code test failure.


# Seventh market-specific bonus evidence pass — Switzerland — 24 October 2026

- Added official promotion sources for Swiss Casinos Online and StarVegas; ledger now has **22** official bonus/promotion URLs. Internal note: `docs/reviews/internal/bonus-snapshot-swisscasinos-starvegas-ch-2026-10-24.md`.
- Swiss Casinos' official registration page describes up to CHF 1,400 bonus credit + 100 spins, with the components, deposit thresholds, 35x wagering and 30-day expiry recorded. A separate CHF 20 CasinoBoost26 code expired 4 October 2026 and is explicitly excluded from any current-offer claim.
- StarVegas advertises a welcome offer up to 50 Super Spins and has a separate promotional-terms index, but exact live conditions could not be extracted reliably; this remains held pending manual verification.
- Ledger audit after the Hollywood Casino HTTPS correction: 100 rows, 43 columns, 100 unique brand/market identities, all populated bonus sources dated 2026-10-24, no blank bonus-status fields, no non-HTTPS populated URL fields, 0 numeric scores, 100 explicit NOT SCORED states, 100 consumer tests NOT PERFORMED, and 100 affiliate disclosures NOT REVIEWED.


# Ledger validation regression expansion — 24 October 2026

- Expanded the review-ledger regression suite from five to **seven tests** with explicit cases for rejecting non-HTTPS official sources and malformed bonus-check dates.
- Existing coverage also tests held/unscored rows, partial component scoring, score-total mismatches, duplicate brand/market identities, and attempted publication without required evidence or cleared image rights.
- These tests are wired into the existing GitHub Actions workflow, but execution is still blocked by the runner-allocation failure tracked in Issue #143; no test pass is claimed.


# Eighth market-specific bonus evidence pass — Spain — 24 October 2026

- Added official promotion sources for Codere Spain and AdmiralBet Spain; ledger now has **24** official bonus/promotion URLs. Internal note: `docs/reviews/internal/bonus-snapshot-codere-admiralbet-es-2026-10-24.md`.
- Codere's official pages conflict on the minimum qualifying deposit (€10 in the casino journey vs €20 on the welcome-bonus explainer) and mix sports/casino product language; no casino-only offer was cleared.
- AdmiralBet's official casino page describes 50 registration spins, a 100% first-deposit bonus up to €150 and 50 post-deposit spins. Its €10 free bet is a sports benefit and is deliberately excluded from casino bonus value; exact casino wagering/expiry/cashout terms remain outstanding.
- Both rows remain held; no account or offer testing was performed.


# Ninth market-specific bonus evidence pass — Great Britain — 24 October 2026

- Added official offer-source entries for Paddy Power Games, William Hill Casino and Virgin Games. The ledger now contains **30 official bonus/promotion source URLs across 100 candidates**. Internal note: `docs/reviews/internal/bonus-snapshot-paddypower-williamhill-virgingames-gb-2026-10-24.md`.
- Paddy Power's Live Casino welcome offer requires code PASREG and £10 eligible live-casino wagering for 10 Golden Chips worth £5 total; valid UK/IE, debit card/Apple Pay only, three-day expiry and no wagering on chips.
- William Hill's official homepage module advertises up to 200 spins after a £10 qualifying stake, but the exact current GB offer route and deposit-versus-stake sequence still require confirmation.
- Virgin Games' official UK page advertises 100 Game of Thrones spins after opt-in and at least £10 deposit + slot wagering; 10p/spin and 30-day expiry are stated, with full rules still to verify.
- All three remain HOLD. Ledger audit confirms 100 rows, 43 columns, 30 dated bonus sources, zero blank bonus-status fields, zero non-HTTPS populated URLs and zero numerical review scores.


# Tenth bonus source pass and latest ledger reconciliation — 24 October 2026

- Added official-source observations for PlayOJO UK and FanDuel Casino Ontario in `docs/reviews/internal/bonus-snapshot-playojo-fanduel-2026-10-24.md`.
- The latest ledger now has **38** populated official bonus/promotion URLs across the 100 candidates. The additional source URLs now present include market-specific candidates for Caesars Palace Online (Ontario), Borgata (New Jersey), BetMGM (Michigan), betPARX (Pennsylvania), Napoleon (Belgium), Sisal (Italy), LeoVegas (Germany candidate), Ladbrokes (Belgium), and Grosvenor (Great Britain). Each offer still needs full-term reconciliation and the wider review gates; a populated source URL is not publication approval.
- PlayOJO's UK welcome page states 50 Big Bass Bonanza spins at £0.10 per spin with a £10 first-deposit minimum, and says free-spin winnings have no wagering requirement; it excludes Northern Ireland new players. FanDuel Ontario's homepage shows 500 spins + CAD $20 and a separate up-to-CAD $1,000 first-day lossback headline, but the separate offer-specific conditions remain outstanding.
- Current structural audit: 100 rows, 43 columns, 100 unique brand/market identities, 38 dated bonus-source URLs, no blank bonus-status fields, no non-HTTPS populated URL fields, 0 numeric scores and 100 explicit NOT SCORED states. All consumer tests remain NOT PERFORMED and affiliate disclosures NOT REVIEWED.


# Market-specific source correction and Belgian legal hold — 24 October 2026

- Corrected LeoVegas from a UK promotions URL to its German-specific welcome page and bonus conditions. Germany's official page advertises up to €100 real-money bonus plus up to 100 free spins; offer terms describe new-account eligibility from 31 July 2026, activation within seven days and up to 20x deposit wagering to unlock the cash bonus. Exact tier terms remain held.
- Corrected Ladbrokes Belgium from a UK welcome-bonus URL to the Belgium-specific Casinoladbrokes.be domain and promotions page. UK offer terms are explicitly not applicable to Belgium.
- Flagged a Belgian legal/compliance gate for both Ladbrokes Belgium and Casino777.be: Belgium applies strict restrictions to gambling bonuses/promotional inducements. Neither a generic promotions page nor the “777 Boost” game-specific mechanic proves legality. No bonus should be published without confirmation that the exact mechanic is lawful and current.
- Internal source note: `docs/reviews/internal/bonus-snapshot-leovegas-de-ladbrokes-be-2026-10-24.md`; Casino777 note updated with the same legal gate.


# Additional exact-market source correction — Betway Germany — 24 October 2026

- Corrected the Betway (DE) ledger row from a UK-domain URL and UK-only £ offers to the German-specific `betway.de/de-de/` source and Germany terms page.
- The German homepage advertises a 100% first-deposit match up to €100, €10 minimum deposit, 18x wagering and minimum odds 1.75, but the retrieved page is primarily sports-betting marketing and does not establish a casino-specific welcome offer or exact product permission. It remains HOLD pending GGL product-scope and casino terms verification.
- Updated `docs/reviews/internal/bonus-snapshot-leovegas-de-ladbrokes-be-2026-10-24.md` with the correction. UK terms must not be reused for Germany, and Belgian promotional benefits remain subject to local legal review.


# Eleventh bonus source pass and current audit — 24 October 2026

- Added official source notes for Svenska Spel Sport & Casino (SE) and Casino Gran Madrid Online (ES): `docs/reviews/internal/bonus-snapshot-svenskaspel-granmadrid-2026-10-24.md`.
- The ledger now contains **52 official bonus/promotion source URLs** across 100 candidates, all with the 2026-10-24 observation date and non-empty status notes. This includes additional source entries now present for Admiral Bet Italy, Betfair Italy and Betflag Italy; these still require exact offer terms and independent verification.
- Svenska Spel's SEK 100 welcome offer runs 4 September 2026–4 January 2027, with a SEK 25 minimum deposit and SEK 1 first-game bet; it covers multiple product types, so it must not be presented as a casino-only bonus.
- Gran Madrid's current landing page states 200% up to €200, 20x wagering, 14-day validity and a period ending 31 October 2026. Minimum-deposit wording needs reconciliation, and the offer must be rechecked after expiry.
- Structural audit: 100 rows, 43 columns, 100 unique brand/market identities, 52 dated official bonus-source URLs, zero blank bonus-status fields, zero non-HTTPS populated URLs, zero numeric review scores, and 100 NOT SCORED states. Consumer testing and affiliate-disclosure review remain incomplete for all 100 rows.


# Belgian promotional-inducement compliance hold — 24 October 2026

- Corrected Circus Casino Belgium to its current Belgian promotions hub and added `docs/reviews/internal/belgium-promotion-compliance-hold-2026-10-24.md`.
- Casino777.be, Napoleon Casino Belgium, Circus Casino Belgium and Ladbrokes Casino Belgium remain HOLD pending a legal/compliance determination for the exact local promotion mechanic and current terms. Do not describe a generic promo page, game boost, prize drop or tournament as a lawful welcome bonus without that sign-off.
- Latest ledger audit: 100 rows, 43 columns, 100 unique identities, **54** dated official bonus/promotion URLs, zero blank bonus-status notes, zero populated non-HTTPS URLs, zero numerical review scores, and all 100 rows explicitly NOT SCORED. All 100 consumer/usability tests remain NOT PERFORMED and affiliate disclosures NOT REVIEWED.
- Latest Actions runs `40138041825` and `40138026593` still fail before source steps execute; issue #143 tracks runner allocation. No CI pass, merge or production deploy is claimed.


# Twelfth bonus source pass and latest source audit — 24 October 2026

- Added BetRivers Michigan and Fair Play Online Netherlands official-source notes at `docs/reviews/internal/bonus-snapshot-betrivers-mi-fairplay-nl-2026-10-24.md`.
- BetRivers' Michigan landing page describes a 1x bonus playthrough and links a casino-back/spins offer, but the full offer terms were not exposed; the casino offer must not be conflated with sportsbook offers. Fair Play Online's official promotions page is for existing players; no new-customer welcome bonus was verified, so the ledger records that uncertainty rather than inventing one.
- Latest audit: **55/100** candidates have a dated official bonus/promotion source URL; 100 rows, 43 columns, 100 unique brand/market identities, zero blank bonus-status notes, zero populated non-HTTPS URLs, zero numeric review scores and 100 NOT SCORED states. All 100 consumer tests remain NOT PERFORMED and affiliate disclosures NOT REVIEWED.
