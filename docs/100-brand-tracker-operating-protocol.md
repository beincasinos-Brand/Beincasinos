# 100-brand tracker operating protocol

## One row means one distinct brand-market pair
A single company may operate multiple brands; one brand may have different operators or terms by market. Keep separate rows when legal entity, domain, permission, bonus or consumer terms differ. Do not count a supplier, operator group, sports betting product or bingo-only entity as a casino consumer brand unless a distinct casino consumer offer is evidenced.

## Deduplication keys
Compare canonical consumer brand; official domain and redirect chain; contracting legal entity; regulator account/licence identifier; market and permitted casino product; white-label relationship and brand aliases. Do not merge brands solely because they share a parent company. Do not count market variants as separate unique global brands when the target metric is 100 unique brands; report unique brands and brand-market review pages separately.

## Required statuses
| Status | Meaning | Counts toward 100 approved reviews? |
|---|---|---:|
| Candidate | Lead only | No |
| Researching | Evidence collection started | No |
| Hold | Material evidence gap/conflict | No |
| Identity matched | Domain/operator/register aligned | No |
| Review ready | Required factual evidence collected | No |
| Editorial review | Independent review pending | No |
| Approved | Evidence gate and second editor passed | Yes |
| Published | Approved page verified in deployed site | Published count only |
| Index observed | First-party search reporting confirms observation | Index-observed count only |
| Excluded | Not eligible or unresolved identity | No |

## Evidence quality
Prioritise primary sources: official regulator registers, operator terms, bonus terms, payment pages, complaint/ADR pages, safer-gambling pages and official domains. Affiliate networks and third-party reviews can provide leads but cannot replace licensing and terms evidence. For every claim store source URL, checked date, market, exact claim supported and reviewer note. An inaccessible or unexpected redirect is not adequate evidence by itself.

## Report counts separately
Candidate names; distinct consumer brands after deduplication; brand-market pairs; identity-matched pairs; holds and blockers; review-ready drafts; editorial reviews awaiting sign-off; approved reviews; published pages verified live; sitemap URLs; index-observed URLs. Never collapse these into one progress percentage.

## Safe execution
Keep research changes separate from public content. Avoid deployments and CI runs until the owner requests a release batch. Check for existing equivalents before adding documents. Do not add unsupported ratings, bonus claims, testimonials, logos or payout promises to make a page appear complete.