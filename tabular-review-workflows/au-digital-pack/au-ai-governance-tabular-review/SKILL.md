---
name: au-ai-governance-tabular-review
description: Assess Australian AI governance and readiness against current official guidance and applicable law.
license: MIT
metadata:
  version: 1.0.0
  author: Si Han Xu
  language: English
  mike-display-name: AU AI Governance Tabular Review
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

- Assess Australian AI governance and readiness by identifying the system, legal nexus and supplied governance evidence.
- Identify and cite the current official Guidance for AI Adoption, Voluntary AI Safety Standard and Australia’s AI Ethics Principles from ai.gov.au or industry.gov.au, including title, dated version, relevant passage and current relationship/supersession status. Do not assume a fixed supersession date or an exhaustive six-practice list.
- Distinguish voluntary practice guidance from applicable Privacy Act 1988 (Cth), Australian Consumer Law, anti-discrimination, sector and online-safety duties. Establish each legal test from current official authority with a pinpoint. Treat accountability, risk/benefit, human oversight, data governance, transparency and testing/monitoring as provisional review topics to map against current guidance, not an asserted official exhaustive list.
- For security guidance, identify a named, dated original official publication and cite the relevant passage before applying it; do not assert requirements from unnamed ASD guidance.
- Determine current enactment and commencement status of each relevant reform from the Federal Register of Legislation and AGD/OAIC official sources, citing the instrument, provision, version, commencement table and assessment date. Separate proposals, enacted future duties and commenced duties; do not describe an enacted reform as merely proposed or assume a proposal is law.
- Separate document facts, supplied organisational materials (identify source/version), cited law with pinpoint references and current official-source version/status, and labelled assessments/proposals. Return Not found for missing facts and Not assessed for unsupported analysis. Never infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence. Proposed actions require human approval; do not submit, publish, deploy or accept residual risk.
