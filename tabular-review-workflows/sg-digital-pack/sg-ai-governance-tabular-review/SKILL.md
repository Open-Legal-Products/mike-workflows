---
name: sg-ai-governance-tabular-review
description: Review Singapore AI governance, agency calibration, testing evidence and sector overlays against identified current sources.
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: SG AI Governance Tabular Review
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

- Identify the applicable traditional, generative and agentic Model AI Governance Framework versions and cite the relevant passages. Determine agency taxonomy and pathways from the identified text, not display tags.
- Determine AI Verify coverage, limitations, evidence requirements and assurance/certification claims from the identified current scheme source. Determine chatbot disclosures from the identified dated Transparency Guidelines for Generative AI Chatbots and cite each relevant passage.
- Distinguish source-backed framework recommendations, sector requirements and market expectations (for example, MAS, MOH, PDPC or IMDA sources). Compare supplied system and governance evidence; do not presume controls or approvals.
- Use supplied system inventories, architecture, risk assessments, evaluation records, governance policies and approval records; do not treat a single system document as an organisation-wide inventory. Distinguish document facts (cite the reviewed passage), operational facts (cite supplied organisational materials), external law or guidance (identify the current source/version and pinpoint provision), and labelled assessments or proposals. Return Not found for missing facts and Not assessed for unsupported analysis; do not infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence.
- Keep all drafts and proposed actions subject to human review. Do not submit, publish, approve deployment or accept residual risk without human approval.
