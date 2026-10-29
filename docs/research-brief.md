# Research brief: BeInCasinos Tier 1 operator evidence (v2, 2026-10-27)

You are a desk researcher. Use ONLY WebSearch and WebFetch. Primary sources only: the regulator's own register/pages and the operator's OWN help centre / terms / promo / safer-gambling / complaints pages for the named market. Never use affiliate or review sites as evidence. Never register, log in, deposit or test anything. Paraphrase; quote at most 12 words from any page. Do not invent. If a page cannot be opened (the fetch tool often says a host is not on the allowlist) record the URL in "unreachable" and leave that item null / "unverified". Try 2-3 alternative official URLs (help centre, terms, 'responsible gaming', 'complaints', 'payments') and web search with site: filters before giving up. Today is 2026-10-27.

## The single scoring metric (out of 100) - do not change it
Eligibility comes before points. All five checks must be "pass" or the profile is "Not scored - verification incomplete":
 1 domain: the exact domain is identified and appears in the regulator's record where the regulator publishes domains/whitelists.
 2 operator: the legal operating entity is named in the operator's terms and matches the regulator record.
 3 regulator: current official regulator evidence (register entry, licence/concession, whitelist) for that entity/product.
 4 market_permission: the product is permitted for the named market (e.g. GB remote casino licence; NL KSA licence for online casino; DE GGL licence/whitelist for virtual slots/casino; CH ESBK/federal casino concession with online extension; US-MI MGCB internet gaming licence).
 5 terms_and_withdrawal_rules: current official terms and withdrawal rules can be opened and read.
Then six criteria, each rated 0-5 (or null = not assessed) from documented evidence. Weights: terms 25 (bonus conditions, wagering basis, expiry, restrictions, max cashout, accessible full terms) | payments 20 (published limits, processing stages, fees, verification/KYC requirements, complaint steps - not untested speed claims) | safer 20 (visible limits, time-outs, self-exclusion, age info, support resources, product restrictions; include the national scheme: GAMSTOP / CRUKS / OASIS / Swiss Sperrliste) | complaints 15 (support routes, formal complaint process, escalation/ADR route) | licence 10 (named legal entity, exact domain, current product/territory permissions, direct official-register links, relevant published enforcement decisions with follow-up) | usability 10 (important terms/restrictions findable and readable; mobile).
Anchors: 0 documented material failure; 1 very weak; 2 weak, meaningful gaps; 3 adequate but limitations remain; 4 strong, only limited gaps; 5 exemplary, unusually clear and complete. NEVER rate from absence of research or an unreachable page: use null. A 0 is only for a documented failing. Commission, listing fees or sponsorship never affect anything.

## Output
Write ONE JSON file per operator to /tmp/claude-0/-home-claude/36fe192b-c77c-5f27-ac89-51445b9378a0/scratchpad/research/<slug>.json (valid JSON, UTF-8, use the Write tool). Schema:
{
 "slug": "", "checked": "2026-10-27",
 "eligibility": {"domain":{"status":"pass|fail|unverified","note":"","url":""}, "operator":{...}, "regulator":{...}, "market_permission":{...}, "terms_and_withdrawal_rules":{...}},
 "criteria": {"terms":{"rating":0-5 or null,"note":"<=40 words, paraphrased evidence","url":""}, "payments":{...}, "safer":{...}, "complaints":{...}, "licence":{...}, "usability":{...}},
 "facts": {
   "licence": {"value":"regulator + number/entity","url":""},
   "welcome_offer": {"headline":"","min_deposit":"","wagering":"","expiry":"","max_cashout":"","verified":true|false,"seen":"2026-10-27","url":""},
   "withdrawals": {"timing":"as published","limits":"","fees":"","url":""},
   "kyc": {"summary":"when/what documents, as published","url":""},
   "payment_methods": [],
   "support": {"channels":"","hours":"","url":""},
   "complaints_route": {"summary":"","url":""},
   "safer_tools": [],
   "launched": ""},
 "red_flags": [{"date":"YYYY-MM-DD","text":"regulator action or documented issue, paraphrased","url":""}],
 "pros": ["max 3, each backed by a fact above"], "cons": ["max 3, each backed by a fact above"],
 "unreachable": ["urls that failed"], "notes": "anything the editor must know"
}
Use "" or null for unknown. A welcome offer is "verified": true only if you read the operator's own offer page AND its conditions. If the market bans or heavily restricts bonuses (e.g. DE, NL, CH) say what is allowed instead of inventing a bonus.
Your final chat message must be SHORT: one line per operator with slug, eligibility pass count (x/5), criteria rated (x/6), offer verified (y/n), and the main blockers. Do not paste JSON into chat.
