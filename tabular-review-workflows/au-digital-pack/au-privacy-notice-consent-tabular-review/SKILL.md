---
name: au-privacy-notice-consent-tabular-review
description: Use this workflow to clause-by-clause review of privacy policies, collection notices and consent flows under the Australian Privacy Act 1988 (Cth) and Australian Privacy Principles (APPs), applying OAIC guidance
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: AU Privacy Notice Consent Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Data Protection
  jurisdictions: Australia
---

# Privacy Notice & Consent Flow Review — Australia (Privacy Act / APPs)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Clause-by-clause review of privacy policies, collection notices and consent flows under the Australian Privacy Act 1988 (Cth) and Australian Privacy Principles (APPs), applying OAIC guidance.
- Covers: APP 1's open-and-transparent management duty (a clearly expressed, current APP Privacy Policy); APP 5's notification of collection content and timing; APP 3's collection rules and the 'consent' requirements for sensitive information; and APP 6's use and disclosure limits including the secondary-purpose analysis — Australia does not run a GDPR-style opt-in consent regime, so the review treats consent as one basis among several and never assumes it is required for ordinary collection.
- Prompts check notice mechanics against OAIC expectations, flag GDPR-isms, and watch the Privacy Act reform pipeline (automated-decision transparency, direct liability for overseas recipients) where it would change current practice.
