---
name: sg-ai-governance-tabular-review
description: Use this workflow to singapore-specific AI governance assessment and readiness review of an AI system or feature
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: SG Ai Governance Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: AI Governance
  jurisdictions: Singapore
---

# AI Governance Assessment — Singapore (IMDA Model Frameworks + AI Verify)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Singapore-specific AI governance assessment and readiness review of an AI system or feature.
- Anchors on IMDA's Model AI Governance Framework (2nd Ed), the Model AI Governance Framework for Generative AI (May 2024, IMDA/AI Verify Foundation), the Model AI Governance Framework for Agentic AI (v1.5, 2026) and the AI Verify testing/assurance toolkit.
- Singapore's frameworks are voluntary — this workflow separates 'what the framework recommends', 'what sector regulators separately require' (e.g.
- MAS, MOH, PDPC where AI touches their remits), and 'what is market expectation'.
- Uses AI Verify as the assurance/testing vehicle and identifies the accountability and evidence posture expected of a provider or deployer operating in or serving users from Singapore.
