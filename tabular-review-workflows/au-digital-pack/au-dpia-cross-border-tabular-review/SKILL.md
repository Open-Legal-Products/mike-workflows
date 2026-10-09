---
name: au-dpia-cross-border-tabular-review
description: Assess Australian privacy impacts and cross-border disclosures under the Privacy Act 1988 (Cth), APPs and OAIC guidance.
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

# PIA & Cross-Border Disclosure Assessment — Australia (Privacy Act / APPs)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Assess Australian privacy impact and cross-border disclosure risks under the Privacy Act 1988 (Cth), APPs and identified OAIC guidance.
- Identifiers retain 'DPIA' for cross-jurisdiction familiarity while the Australian task is a PIA / cross-border disclosure review under the Privacy Act.
- The Privacy Act does not impose a universal PIA requirement. Agencies covered by the Privacy (Australian Government Agencies — Governance) APP Code 2017 must conduct a PIA for all high privacy risk projects. Assess whether that Code applies; otherwise use OAIC guidance to determine whether a PIA is warranted.
- For APP 8.2(a), assess the reasonable belief that the recipient is subject to a substantially similar protective law or binding scheme and that the individual can access mechanisms to enforce that protection. For APP 8.2(b), assess express informed consent after telling the individual that APP 8.1 will not apply to the disclosure.
- Determine APP 8.1 reasonable steps and any other exception from its full statutory conditions. Review onward disclosures and NDB Part IIIC separately using current authority and supplied flow, contract, testing and response-plan evidence.
- Determine current enactment and commencement status of each relevant reform from the Federal Register of Legislation and AGD/OAIC official sources, citing the instrument, provision, version, commencement table and assessment date. Separate proposals, enacted future duties and commenced duties; do not describe an enacted reform as merely proposed or assume a proposal is law.
- Separate document facts, supplied organisational materials (identify source/version), cited law with pinpoint references and current official-source version/status, and labelled assessments/proposals. Return Not found for missing facts and Not assessed for unsupported analysis. Never infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence. Proposed actions require human approval; do not submit, publish, deploy or accept residual risk.
