---
name: sg-privacy-notice-consent-tabular-review
description: Review Singapore privacy notices and consent flows against the PDPA and identified PDPC guidance; propose evidence-grounded redlines.
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

- Identify the supplied notice, dated user journeys and processing/recipient evidence. Determine the applicable Singapore PDPA consent or exception basis and notification duties from cited current provisions, not a fixed GDPR comparison.
- Determine consent validity, NRIC use and other sensitive-context expectations from identified current statutory or PDPC passages; reconcile dated guidance with current advisory and enforcement developments.
- Compare notice wording with evidenced collection, default choices, withdrawal and request handling; do not infer working channels or actual flows from text alone. Assess marketing and transfer requirements from identified cited sources.
- Use supplied notices and dated flow captures, processing/recipient inventories, request and withdrawal logs and control evidence; a notice alone cannot establish actual practice or a working channel. Distinguish document facts (cite the reviewed passage), operational facts (cite supplied organisational materials), external law or guidance (identify the current source/version and pinpoint provision), and labelled assessments or proposals. Return Not found for missing facts and Not assessed for unsupported analysis; do not infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence.
- Keep all drafts and proposed actions subject to human review. Do not submit, publish, approve deployment or accept residual risk without human approval.
