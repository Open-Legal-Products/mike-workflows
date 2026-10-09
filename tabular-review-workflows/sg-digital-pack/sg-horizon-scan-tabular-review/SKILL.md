---
name: sg-horizon-scan-tabular-review
description: Use this workflow to singapore regulatory horizon scanning and obligation mapping for digital, content, data and AI regulation
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: SG Horizon Scan Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Regulatory
  jurisdictions: Singapore
---

# Regulatory Horizon Scan & Obligation Map — Singapore

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Singapore regulatory horizon scanning and obligation mapping for digital, content, data and AI regulation.
- Ingests new or amended Singapore instruments — Acts (via Singapore Statutes Online / SSO and the Government Gazette), subsidiary legislation, IMDA codes of practice and directions, PDPC advisories and guidelines, MAS or other sector rules, and public consultation papers — and maps each obligation onto the organisation's products, features and owners, tracking status from proposed through assented and in force to compliance due.
- Prompts anchor on Singapore's official sources (SSO/AGC for statutes, IMDA and PDPC websites for codes and guidance, REACH/AGC for consultations) and Singapore's commencement conventions (e.g. section 1 of each Act specifying commencement).
