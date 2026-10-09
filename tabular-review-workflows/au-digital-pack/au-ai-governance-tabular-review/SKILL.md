---
name: au-ai-governance-tabular-review
description: Use this workflow to australia-specific AI governance assessment and readiness review
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: AU Ai Governance Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: AI Governance
  jurisdictions: Australia
---

# AI Governance Assessment — Australia (Guidance for AI Adoption & AI Safety Standard)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Australia-specific AI governance assessment and readiness review.
- Anchors on the Australian Government's voluntary Guidance for AI Adoption (21 October 2025) with its 6 essential practices (which superseded and simplified the Voluntary AI Safety Standard's 10 guardrails), Australia's AI Ethics Principles, and the Australian Signals Directorate / industry technical guidance where security applies.
- Explicitly separates voluntary guidance from binding Australian law that governs the same AI use: the Privacy Act 1988 (Cth) and APPs (incl. automated-decision transparency expectations), the Competition and Consumer Act 2010 (Cth) and the ACL's misleading-conduct provisions for AI outputs, anti-discrimination law, and eSafety obligations for AI-generated content.
- Workflow maps each practice to evidence and flags the 'soft law hardening' trajectory of Australian AI regulation.
