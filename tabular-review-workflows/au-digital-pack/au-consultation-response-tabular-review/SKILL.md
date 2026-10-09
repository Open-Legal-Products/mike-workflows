---
name: au-consultation-response-tabular-review
description: Draft and review Australian regulator and government consultation responses for human approval.
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: AU Consultation Response Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Regulatory
  jurisdictions: Australia
---

# Consultation Response Drafting — Australia (eSafety/ACMA/OAIC/Commonwealth Departments)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Review the consultation paper and draft responses using the issuer’s exact question numbering. Verify the actual issuing body, deadline, submission channel and publication/confidentiality rules from its official paper and page. Do not presume ACMA and eSafety are interchangeable.
- Use supplied approved positions, prior submissions, complete response drafts, metrics and confidentiality/sign-off records. Label unsupported positions and drafting plans as proposals.
- The Privacy Act does not impose a universal PIA requirement. Agencies covered by the Privacy (Australian Government Agencies — Governance) APP Code 2017 must conduct a PIA for all high privacy risk projects. Assess whether that Code applies; otherwise use OAIC guidance to determine whether a PIA is warranted.
- The six additional age-restricted-material codes were registered on 9 September 2025 and commenced from 9 March 2026, with some measures commencing later. Identify the applicable service’s code or standard and each relevant measure’s commencement date; do not assume every measure applied on 9 March 2026.
- Verify the applicable code/standard, current register entry and clause before stating any legal consequence.
- Separate document facts, supplied organisational materials (identify source/version), cited law with pinpoint references and current official-source version/status, and labelled assessments/proposals. Return Not found for missing facts and Not assessed for unsupported analysis. Never infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence. Proposed actions require human approval; do not submit, publish, deploy or accept residual risk.
