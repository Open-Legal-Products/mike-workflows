---
name: au-online-safety-tabular-review
description: Use this workflow to australian online-safety obligation mapping for services regulated under the Online Safety Act 2021 (Cth) and eSafety's registered industry codes and standards
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: AU Online Safety Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Online Safety
  jurisdictions: Australia
---

# Online Safety Obligation Map — Australia (eSafety Codes & Standards)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Australian online-safety obligation mapping for services regulated under the Online Safety Act 2021 (Cth) and eSafety's registered industry codes and standards.
- Covers the class 1A/1B (unlawful material) codes and standards and the class 1C/2 (age-restricted material) codes — including the six age-restricted-material codes registered 9 September 2025 and in effect 9 March 2026 (social media core features, messaging, relevant electronic services, designated internet services, app distribution, equipment) and the three registered 27 June 2025 in effect 27 December 2025 (hosting, internet carriage, search) — plus the basic online safety expectations and eSafety's complaints, blocking, and transparency powers.
- The workflow maps each obligation onto the organisation's operational workflows — complaints handling, content moderation, takedown, reporting — with each column requiring the correct code schedule and service class, not generic 'eSafety obligations'.
