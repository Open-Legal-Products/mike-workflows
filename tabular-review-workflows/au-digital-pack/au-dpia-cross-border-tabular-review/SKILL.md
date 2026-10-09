---
name: au-dpia-cross-border-tabular-review
description: Use this workflow to australia-specific privacy impact assessment and cross-border disclosure review under the Privacy Act 1988 (Cth) and Australian Privacy Principles (APPs), as administered by the Office of the Australian Information Commissioner (OAIC)
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: AU DPIA Cross Border Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Data Protection
  jurisdictions: Australia
---

# DPIA & Transfer Assessment — Australia (Privacy Act / APPs)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Australia-specific privacy impact assessment and cross-border disclosure review under the Privacy Act 1988 (Cth) and Australian Privacy Principles (APPs), as administered by the Office of the Australian Information Commissioner (OAIC).
- Covers: whether a PIA is warranted under OAIC guidance (a PIA is not mandatory under the Act but the OAIC recommends and expects one for high-risk projects and for APP 8 assessments); the APP 8 cross-border disclosure framework — the 'reasonable steps' obligation, the exception where the recipient is bound by the APPs or a prescribed scheme, the reduced protections where an exception applies, and accountability for onward disclosure; and the interaction with the Notifiable Data Breaches (NDB) scheme under Part IIIC.
- Prompts flag the Privacy Act reform pipeline (including proposed automated-decision transparency obligations) where it affects current assessment practice.
