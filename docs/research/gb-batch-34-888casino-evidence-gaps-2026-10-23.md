# Batch 34 — 888casino Great Britain evidence check

Research date: 23 October 2026. Status: HOLD; internal evidence only.

## Confirmed
- UKGC account 39028 shows Casino Remote permission as Active: https://www.gamblingcommission.gov.uk/public-register/business/detail/39028
- UKGC domain register lists 888casino.com as Active under account 39028: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/39028
- Operator licensing disclosure identifies 888 UK Limited as the UK operator: https://www.888casino.com/security-and-privacy/licensing/
- The generic agreement at https://www.888casino.com/security-and-privacy/user-agreement-ma/ says it does not apply to UK users and links to the GB-specific route https://www.888casino.com/security-and-privacy/user-agreement-uk/. Use the UK-specific document for any GB review.

## Access gaps
- The generic responsible-gambling and complaints URLs attempted in this pass returned 404. Do not interpret that as proof the policies or services are unavailable.
- Fetches of the UK-specific agreement, withdrawal policy, payment methods, bonus policy, responsible-gambling page, privacy policy and cookie policy timed out in this pass. This is inconclusive access evidence, not proof of absence.

## Decision and next actions
The candidate remains HOLD. Licence/domain/operator identity is better supported, but the exact GB terms and current payment, withdrawal, bonus, complaints/ADR, safer-gambling, privacy/cookie and accessibility evidence remain incomplete. No score, payout-speed claim, support-quality claim or first-hand test should be invented. Re-fetch individual policy pages, capture dates and exact clauses, then request independent second-editor review.

Batch outcome: 0 newly approved brands; 0 newly publication-approved reviews. No production deployment, main-branch change, DNS change, account creation or transaction test.


## Successful follow-up fetch — GB agreement and policy details

The exact UK-specific agreement subsequently loaded successfully: https://www.888casino.com/security-and-privacy/user-agreement-uk/. Its contents include clauses on withdrawals (section 9), complaints/disputes (section 14), safer gambling (section 16) and promotions (section 17).

- **Withdrawals:** the agreement says withdrawals are subject to cleared deposits, verification checks and specified investigations. It says a minimum threshold may vary by payment method, but the full available balance may be processed even below the threshold (the customer may need to contact support). It does not provide a universal processing-time promise in the captured clause. The separate withdrawal policy says ID and other documents may be requested and that the payout method depends on previous deposit methods/amounts. It describes a possibility of casino winnings above £/€/$30,000 being paid in monthly instalments up to £/€/$30,000, and jackpot winnings potentially in up to 24 monthly instalments at the operator's discretion. These clauses require careful plain-English explanation and current UK applicability check.
- **Complaints/ADR:** the GB agreement directs customers to Live Chat first, then the Second Opinion team if unhappy. It names eCOGRA for adjudication if the customer remains unhappy, including where the Second Opinion team has not given a final response within eight weeks. Verify current complaint-policy detail and the applicable eCOGRA scope before publication.
- **Safer gambling:** the agreement says the operator is registered with GAMSTOP and describes exclusion periods of six months, one year or five years. This is the operator's published wording, not an independent functionality test.
- **Bonus policy:** the generic Bonus Policy says, unless promotion-specific terms differ, wagering requirements are generally 30x the initial bonus amount and bonus/associated winnings generally expire after 90 days. It lists different game contributions (slots and many listed game types 100%; some poker/table games 20%; blackjack/roulette/live casino 10%; craps 5%). Do not present these as a current welcome offer: no current offer was established in this pass, and the specific offer terms take precedence.
- **Payments:** the generic deposit landing page lists examples including Visa/Mastercard and other methods and says processing times vary by method. This list is not proven to be the exact set available to a Great Britain account; verify the GB cashier/payment-method page before stating methods or fees.
- The exact agreement fetch was successful after earlier timeouts. Other policy pages were fetched individually; the withdrawal and bonus pages loaded. No account was created and no payment or support test occurred.

**Decision remains HOLD:** important public policy detail is now captured, but current GB-specific payment availability/fees, withdrawal timeframes, current promotion terms, full complaint process, privacy/cookies, accessibility and independent second-editor review remain open.
