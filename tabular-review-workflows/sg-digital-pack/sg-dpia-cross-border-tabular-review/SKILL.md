---
name: sg-dpia-cross-border-tabular-review
description: Use this workflow to singapore-specific data-protection impact assessment and cross-border transfer review under the Personal Data Protection Act 2012 (PDPA) as administered by the Personal Data Protection Commission (PDPC)
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: SG DPIA Cross Border Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Data Protection
  jurisdictions: Singapore
---

# DPIA & Transfer Assessment — Singapore (PDPA)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Singapore-specific data-protection impact assessment and cross-border transfer review under the Personal Data Protection Act 2012 (PDPA) as administered by the Personal Data Protection Commission (PDPC).
- Covers: whether a DPIA is warranted under PDPC guidance (the PDPA does not mandate a DPIA for all processing; PDPC recommends DPIAs for high-risk processing and provides a DPIA framework), the PDPA's consent, notification and purpose-limitation obligations, and the transfer-limitation obligation (s 26) — noting Singapore moved away from the prescribed-whitelist approach and instead requires the transferring organisation to ensure the recipient is bound by comparable protection, with PDPC-recognised mechanisms including contractual terms and binding corporate rules.
- Prompts distinguish PDPA obligations from PDPC advisory guidance and from GDPR-derived expectations where a multinational adopts EU-style practice in Singapore.
