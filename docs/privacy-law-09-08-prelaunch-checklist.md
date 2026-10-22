# Privacy and data-protection release checklist — Morocco and international audiences

**Research date:** 21 October 2026  
**Status:** Internal legal-review workpaper only — not a legal opinion and not launch clearance.  
**Scope:** BeInCasinos static informational website, owner-reported Moroccan context, intended international English-language audience.

## Official Moroccan starting points

- CNDP — data processing in Morocco: https://www.cndp.ma/traitement-des-donnees-personnelles-au-maroc/
- CNDP — Law 09-08 and implementing texts: https://www.cndp.ma/textes-et-lois/
- CNDP — processing notification procedures: https://www.cndp.ma/notifier-un-traitement/
- CNDP — notification procedures, including the website-cookie processing category and Decision D-939-2025 dated 28 November 2025: https://www.cndp.ma/procedures-notification-process/
- CNDP — website compliance guidance (Arabic page): https://www.cndp.ma/ar/%D9%85%D9%84%D8%A7%D8%A1%D9%85%D8%A9-%D9%85%D9%88%D8%A7%D9%82%D8%B9-%D8%A7%D9%84%D8%A7%D9%86%D8%AA%D8%B1%D9%86%D8%AA/
- CNDP — FAQ: https://www.cndp.ma/faq/
- Official Law 09-08 PDF: https://www.cndp.ma/images/lois/Loi-09-08-Fr.pdf

The CNDP says that processing by controllers or means of processing located in Morocco is subject to Law 09-08, and its published procedures describe prior notification/authorisation requirements for relevant processing categories. CNDP also lists a dedicated website-cookie processing category and a 2025 decision. The precise obligations for this project depend on the actual processing, technologies, controller, providers, and transfers; do not infer that a static website is automatically exempt.

## Current repository facts to verify against deployment

- Static HTML/CSS/vanilla JS; no visitor accounts or contact form.
- No analytics integration, advertising pixel, or active affiliate-tracking integration in the current source.
- The wagering calculator and terms checklist execute client-side and do not submit entered values to a BeInCasinos application server.
- A mailto contact link is provided; email content and sender details are handled by the user's email system and the publisher mailbox.
- Hosting/security infrastructure may process request metadata. Actual logs, processors, retention, transfers, and cookie/storage behaviour must be verified in the chosen host account and on the deployed site.
- Vercel has been selected but no project is linked and no production deployment exists. Do not describe provider configuration as tested until a controlled preview is authorised and inspected.

## Owner and counsel checklist — do not mark complete by assumption

1. Confirm the controller/publisher's legally required identity, address/contact channel, and whether the processing is personal, sole-trader, or company processing.
2. Inventory every processing activity: host/CDN/security logs, mailbox, monitoring, cookies/local storage, analytics if ever enabled, affiliate tracking, embeds, outbound link tracking, support requests, and any third-party integrations.
3. Determine which processing declarations, authorisations, records, notices, or other CNDP formalities apply under Law 09-08 to each activity; obtain and retain receipts/authorisations where required before processing begins.
4. Assess any transfers outside Morocco, including hosting, email, analytics, affiliate vendors, and support tools; determine whether a separate transfer procedure or authorisation is required.
5. Record the purpose and lawful basis for each activity, minimum necessary data, access controls, retention/deletion schedule, processor contract terms, security measures, and the request-handling process.
6. Confirm the final privacy notice accurately names the controller and contact, purposes, data categories, recipients/processors, transfers, retention, applicable rights, and complaint route.
7. Test the actual preview for Set-Cookie headers, cookies, local/session storage, IndexedDB, third-party requests, external fonts, embedded resources, and form submissions. Document results rather than assuming from source code alone.
8. If cookies or similar technologies are introduced, review the CNDP's current cookie decision/procedure and determine the appropriate declaration, consent, notice, and user-control requirements before enabling them.
9. Review the intended audience markets separately for additional privacy rules; a Moroccan review alone does not settle EU/UK, US state, Australian, Swiss, or Dutch requirements.
10. Obtain qualified legal/privacy review and record the reviewer, date, findings, required changes, and explicit closure decision.

## Hard launch gate

The privacy page and Terms of Use page are drafts. No declaration, authorisation, cookie-consent implementation, vendor configuration, data-transfer assessment, legal review, or production HTTP behaviour is claimed as completed by this workpaper. Keep the site blocked from public launch and indexing until the owner and qualified reviewer close the applicable items with evidence.

## Evidence limitations

This is a practical research checklist built from CNDP-published starting points, not a definitive interpretation of Law 09-08, the 2025 cookie decision, international transfers, or foreign laws. Obtain advice for the exact operating model before launch.
