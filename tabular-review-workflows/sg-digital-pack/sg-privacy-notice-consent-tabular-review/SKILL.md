---
name: sg-privacy-notice-consent-tabular-review
description: Use this workflow to clause-by-clause review of privacy notices and consent flows under the Singapore Personal Data Protection Act 2012 (PDPA) and PDPC guidance
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: SG Privacy Notice Consent Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Data Protection
  jurisdictions: Singapore
---

# Privacy Notice & Consent Flow Review — Singapore (PDPA)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Clause-by-clause review of privacy notices and consent flows under the Singapore Personal Data Protection Act 2012 (PDPA) and PDPC guidance.
- Covers: whether the PDPA's consent model (or an exception) applies to each collection, use and disclosure; whether the notification obligations in s 20 (inform of purposes on or before collection) are met in content, timing and accessibility; whether consent is valid (s 14 — freely given, informed, specific, and capable of withdrawal) under PDPC's interpretation; and whether the notice architecture withstands a PDPC investigation.
- Prompts distinguish the PDPA's opt-in consent baseline from its exceptions (including the deemed-consent limbs and the business-improvement legitimate-interests exception), and check marketing-consent mechanics against the PDPC's Spam Control Act-adjacent expectations only where relevant.
- Every review is jurisdiction-locked to Singapore and must not import GDPR-isms as if they were PDPA requirements.
