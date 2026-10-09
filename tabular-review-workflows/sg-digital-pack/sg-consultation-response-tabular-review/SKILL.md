---
name: sg-consultation-response-tabular-review
description: Use this workflow to singapore regulator consultation-paper response drafting and review
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: SG Consultation Response Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Regulatory
  jurisdictions: Singapore
---

# Consultation Response Drafting — Singapore (IMDA/PDPC/AGC/Ministry)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Singapore regulator consultation-paper response drafting and review.
- Supports responses to consultations issued by Singapore regulators and government bodies — including IMDA (content, media, telecoms, AI frameworks), PDPC (data protection), the Attorney-General's Chambers and ministries on legislative proposals, and sector regulators — where the organisation must extract question references, form a position, and draft a structured public response with cited authority and evidence.
- The workflow keeps regulator identity honest: prompts require naming the actual issuing body and its consultation conventions (e.g.
- IMDA's numbered consultation questions, PDPC's advisory-guideline consultations, public consultation papers published via REACH or the agency site), and flag any mismatch between the regulator named in the task and the regulator that actually issued the paper.
