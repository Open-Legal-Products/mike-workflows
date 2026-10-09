---
name: sg-online-safety-tabular-review
description: Use this workflow to singapore online-safety obligation mapping for designated online communication services
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: SG Online Safety Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Online Safety
  jurisdictions: Singapore
---

# Online Safety Obligation Map — Singapore (Broadcasting Act Codes)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Singapore online-safety obligation mapping for designated online communication services.
- Anchors on the Online Safety (Miscellaneous Amendments) Act 2022, which introduced the online-safety part into the Broadcasting Act 1994, the Code of Practice for Online Safety for social media services (in force since 2023 for designated social media services), the Code of Practice for Online Safety for App Distribution Services (effective 31 March 2025 for designated app distribution services such as the major app stores), and IMDA's directions powers (including directions to disable access to egregious content).
- The workflow maps each code obligation onto the organisation's operational workflows — content moderation, user reporting, takedown, transparency reporting — distinguishing obligations binding only designated services (with significant reach or impact) from those that bind on a direction, and separating the code's system-level measures from the underlying statutory powers.
