---
name: au-consultation-response-tabular-review
description: Use this workflow to australian regulator and government consultation-paper response drafting and review
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

# Consultation Response Drafting — Australia (eSafety/ACMA/AGD/industry.gov.au)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Australian regulator and government consultation-paper response drafting and review.
- Supports responses to consultations issued by Australian regulators and agencies — eSafety Commissioner (online safety codes and standards, complaints and transparency frameworks), ACMA (communications and media regulation), the Attorney-General's Department and other Commonwealth departments on legislative and policy proposals, OAIC on privacy matters, and the Department of Industry/industry.gov.au on AI and technology policy.
- The workflow extracts question references, forms positions, and scaffolds a structured response with cited Australian authority (Federal Register of Legislation, regulator guidance, explanatory material).
- Prompts keep regulator identity honest — naming the actual issuing body and flagging any mismatch with the regulator assumed in the task (e.g.
- ACMA is Australian; eSafety is a separate statutory office for online-safety matters).
