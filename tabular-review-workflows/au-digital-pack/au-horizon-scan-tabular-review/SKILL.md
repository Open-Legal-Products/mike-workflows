---
name: au-horizon-scan-tabular-review
description: Use this workflow to australian regulatory horizon scanning and obligation mapping for digital, content, data and AI regulation
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: AU Horizon Scan Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Regulatory
  jurisdictions: Australia
---

# Regulatory Horizon Scan & Obligation Map — Australia

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Australian regulatory horizon scanning and obligation mapping for digital, content, data and AI regulation.
- Ingests new or amended Commonwealth and state/territory instruments — Acts and delegated legislation (via the Federal Register of Legislation), eSafety industry codes and standards registered under the Online Safety Act 2021 (Cth), ACMA instruments under the Broadcasting Services Act 1992 (Cth), OAIC guidance and Privacy Act reform items, sector rules (ACCC/ASIC/APRA), and consultation papers — and maps each obligation onto the organisation's products and owners, tracking status from proposed through enacted to in force and compliance due.
- Prompts anchor on official Australian sources and the Commonwealth's commencement conventions (each Act's commencement provisions and the Legislation Act 2003 (Cth) default rules).
