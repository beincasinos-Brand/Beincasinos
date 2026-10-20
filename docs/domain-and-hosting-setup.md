# Domain and hosting setup runbook

**Status:** domain purchase is owner-reported from the Spaceship purchase confirmation pasted into chat. The registrar account, active registration, DNS, and ownership have not been independently inspected. This runbook does not claim the domain is live.

## 1. Confirm the domain inside Spaceship

- [ ] Sign in to Spaceship directly using a trusted bookmark or manually typed address.
- [ ] Confirm `beincasinos.online` appears in the account's domain list and that registration is active.
- [ ] Record the registration/renewal date, renewal price, auto-renew preference, and any privacy setting in a private record. Do not share account screenshots containing personal/account information publicly.
- [ ] Keep the purchase receipt and renewal reminders.
- [ ] Review any optional Unbox trials and recurring charges. Do not add Spacemail, Alf Website, Web Hosting, or EasyWP merely because they are offered on the confirmation page; only add a service after choosing it deliberately.

## 2. Do not change DNS yet

Before selecting hosting, leave current nameservers and DNS records unchanged unless the owner intentionally approves a documented change. A wrong nameserver change can interrupt the domain or existing email. The owner has explicitly selected `beincasinos@gmail.com` as the temporary public contact email and specified the publisher display identity as Anass Amir. Verify that the Gmail inbox is accessible and monitored; this does not establish that a branded mailbox exists or settle any legal publisher disclosure requirements.

Once hosting is chosen, record the provider's exact DNS instructions and add only the required records. Never guess A, AAAA, CNAME, MX, SPF, DKIM, DMARC, or verification values. Preserve existing email records when changing web hosting. Verify DNS propagation and HTTPS after changes.

## 3. Choose hosting for the intended business model

See [hosting decision note](hosting-decision.md) for the current provider comparison. A read-only check found the connected Vercel team is on Hobby with no linked projects; the proposed commercial site must not be deployed there. Netlify Free is the current low-cost candidate to evaluate, but it has not been connected or approved for publication.

- [ ] Compare static hosting providers whose current terms permit a commercial publisher with paid listings and possible affiliate links.
- [ ] Compare total recurring cost, bandwidth/build limits, custom-domain TLS, redirects, security headers, support, and ease of rollback.
- [ ] Do not use Vercel Hobby for the commercial affiliate/listing business; its Hobby plan is for personal, non-commercial use. If using Vercel, review current Pro pricing/terms before approving spend.
- [ ] Do not start a paid subscription or free trial without the owner's explicit choice and awareness of renewal terms.
- [ ] Keep deployment paused until brand-name risk has been reviewed and the selected plan is approved. The owner has chosen to retain the BeInCasinos name for now; this is not trademark clearance.

## 4. Production domain configuration after approval

- [ ] Add the domain in the chosen host dashboard and follow its exact DNS instructions.
- [ ] Decide the canonical host (`https://beincasinos.online` or `https://www.beincasinos.online`) and configure one permanent redirect to it.
- [ ] Confirm HTTPS certificate issuance and test both apex and www hostnames.
- [ ] Ensure every canonical URL, Open Graph URL, sitemap URL, and internal absolute URL uses the chosen canonical host.
- [ ] Check the 404 page, redirects, mobile navigation, keyboard operation, and all internal links on the real deployed site.
- [ ] Keep `robots.txt` as `Disallow: /` during pre-launch work. Remove that block only after the owner approves launch and the regulatory, editorial, privacy, and technical gates are passed.
- [ ] Submit the sitemap in Google Search Console only after launch approval, the production host works over HTTPS, and robots/indexability settings are intentionally enabled.

## 5. Search Console and measurement

- [ ] Create/choose the Google account that will own Search Console access; use least-privilege access for collaborators.
- [ ] Add a Domain property and follow the exact DNS TXT verification value Google provides. Do not invent or reuse a verification token.
- [ ] Verify ownership and keep the TXT record unless Google says it is no longer needed.
- [ ] Submit `https://<chosen-canonical-host>/sitemap.xml` only after launch approval. Replace the angle-bracket placeholder with the actual chosen hostname; do not publish the placeholder literally.
- [ ] If analytics are later added, choose the tool first, document vendors/data collected, and update the privacy and consent experience before enabling it.
- [ ] Do not promise listing impressions, leads, rankings, or conversions until measured data exists.

## 6. Release gate

No deployment, paid add-on, public indexing, or commercial outreach is authorized by this document. The owner must explicitly approve any paid hosting/email purchase, deployment, DNS change that could affect services, and public launch. Domain ownership does not resolve trademark risk. The brand name, market-specific gambling rules, publisher identity, contact route, privacy notice, commercial disclosures, and browser/mobile/accessibility checks remain launch gates.
