# Privacy and data-handling review — BeInCasinos

**Status: OPEN — internal release gate, not legal advice.** Prepared 20 October 2026. The owner has specified the publisher display identity as Anass Amir and the temporary contact email as beincasinos@gmail.com. The legal publisher/controller details, host, data flows, and actual processing configuration remain unverified.

## Primary Moroccan source

The Moroccan CNDP's official website guidance for websites using personal data explains requirements under Law 09-08, including identifying the controller, stating processing purposes and recipients, explaining rights and contact routes, limiting collection and retention, securing information, and completing applicable CNDP formalities before processing. It also explains that hosting/storing personal data on servers abroad may require a separate transfer request after the underlying processing has been declared or authorised.

- CNDP — website compliance guidance: https://www.cndp.ma/ar/%D9%85%D9%84%D8%A7%D8%A1%D9%85%D8%A9-%D9%85%D9%88%D8%A7%D9%82%D8%B9-%D8%A7%D9%84%D8%A7%D9%86%D8%AA%D8%B1%D9%86%D8%AA/
- CNDP — Law 09-08 and related texts: https://www.cndp.ma/textes-et-lois/
- CNDP — data-protection duties: https://www.cndp.ma/conditions/

These sources are a compliance starting point, not a conclusion that a particular filing or consent basis definitely applies. Obtain qualified advice or confirmation from CNDP where needed, especially before collecting contact form submissions, analytics identifiers, or affiliate click data.

## Before any public launch

- [ ] Confirm who legally operates/publishes the website and whether “Anass Amir” is the full legal identity required for notices, or only the public-facing publisher name.
- [ ] Verify that beincasinos@gmail.com is accessible, secured with strong account protection, and checked regularly. Do not invite sensitive personal data by email.
- [ ] Select the host and record its legal entity, server/processing locations, logs, subprocessors, retention periods, and data-processing terms.
- [ ] Map each data flow: ordinary server logs, contact email, analytics, cookies/local storage, outbound affiliate clicks, advertising pixels, embeds, and any future forms. Do not claim a service is not used until the production configuration confirms it.
- [ ] Determine applicable CNDP notification/authorisation and international-transfer formalities before personal-data processing starts; do not assume that using a free static host removes these questions.
- [ ] Check obligations for readers in each intended audience market, including any applicable EU/UK privacy rules. Obtain qualified review rather than relying on this checklist alone.
- [ ] Keep analytics, advertising pixels, third-party forms, non-essential cookies, and affiliate tracking disabled until the applicable notice/consent and regulatory review is complete.
- [ ] Write a final notice that accurately names the controller, purposes, lawful bases where applicable, recipients/processors, retention, transfers, user rights, and contact route.
- [ ] Establish a process for access/correction/objection or other applicable rights requests, correction requests, complaints, and incident response.
- [ ] Minimise data collection. Do not collect gambling account credentials, financial details, identity documents, or health/addiction information.
- [ ] Record the reviewer, decision, evidence, and review date. Reassess when hosting, analytics, affiliate networks, or forms change.

## Current implementation notes

- The site is a static HTML/CSS/JavaScript project; its wagering calculator and terms checklist run in the browser and do not need user entries sent to a server.
- No analytics or advertising tool should be added without updating this review and the public notice.
- The current public privacy page remains a pre-launch draft and must not be represented as final legal advice or proof of compliance.
- The temporary contact email is owner-selected but has not been independently tested for accessibility or monitoring.
