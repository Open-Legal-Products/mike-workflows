---
name: design-partner-draft
description: Draft a provider-side Design Partner Agreement from the bundled DOCX template for an early-access relationship in which a product company and a design partner have ongoing, mutual product-development and feedback obligations. Use when a product company asks to prepare a design partner, early-access co-design, product feedback, launch-partner, or similar agreement. Do not use for design-partner-side drafting or for a pure trial, proof of concept, or pass/fail product evaluation with no meaningful ongoing co-design obligations.
license: MIT
metadata:
  version: 1.0.0
  author: Victor Wang
  language: English
  mike-display-name: Design Partner Draft
  mike-type: assistant
  mike-availability: system
  practice: Commercial
  jurisdictions: General
---

# Design Partner Draft

Draft from `assets/template.docx`. Preserve its structure and baseline positions unless the intake requires a change. Treat it as a starting form, not proof of a universal or market-standard position.

## Scope gate

Classify the relationship before drafting:

- Use this skill when the partner receives early or pre-release access and both sides undertake an ongoing program: the partner tests or uses the product and gives recurring feedback, while the provider develops or improves the product, offers support, or considers agreed feature requests.
- Do not use this skill for a short trial whose primary purpose is a go/no-go evaluation against success criteria. Tell the user that the deal is functionally a pilot or evaluation and use an appropriate pilot workflow.
- If the parties will jointly create technology, share inventorship or ownership, or contribute substantial engineering resources, flag that a joint-development agreement may be more appropriate.
- If the facts are mixed, explain the classification issue and confirm the intended structure before editing the template.

## Intake

Collect answers in one concise round. Accept existing emails, term sheets, product briefs, or prior deal terms instead of repeating answered questions.

| Topic | Required facts |
|---|---|
| Parties and posture | Legal names, entity forms, notice details, represented party, and any affiliate that will use or support the product |
| Product and access | Product description, maturity, intended use, users, environment, access limits, integrations, and prohibited uses |
| Program | Business objective, partner testing/use duties, designated contacts, feedback format and cadence, meetings, and response expectations |
| Provider commitments | Onboarding, support, update cadence, configurations, research or services, and any promised features or delivery dates |
| Fees and costs | Free or paid, amount, invoicing, taxes, expenses, third-party/pass-through costs, and any credit or discount |
| Timing | Effective date, term, extension, termination rights, suspension rights, and wind-down needs |
| Commercial conversion | No commitment, optional negotiation, discount/credit, or agreed conversion mechanics; identify the future commercial agreement |
| Confidentiality | Existing NDA, confidentiality of the relationship, permitted disclosures, and treatment of feedback |
| Data and security | Data categories and flows, personal or regulated data, security commitments, incident notice, retention/deletion, subprocessors, transfers, and whether a DPA is required |
| Intellectual property | Background technology, partner materials, custom work, deliverables, product improvements, feedback rights, third-party materials, and open-source constraints |
| Publicity | Private customer/investor references, name or logo use, public lists, case study, testimonial, reference calls, approval, and revocation |
| Risk allocation | Warranties, disclaimers, liability cap and exclusions, carve-outs, indemnities, insurance, and equitable relief |
| General terms | Governing law/forum, assignment, notices, order of precedence, non-exclusivity, and any related commercial, investment, advisory, or reseller relationship |

Do not invent material facts. Use `[TBD]` for unresolved execution facts. Stop for a decision if the missing answer would change ownership, data rights, feature obligations, conversion, liability, or indemnity.

For an unresolved material choice, do not silently select a term and do not
leave a bare `[TBD]`. Put complete conditional alternatives in the decision
ledger, identify the recommended provider-side opening position and tradeoff,
and mark every alternative non-operative until approved.

## Drafting playbook

Work through every row. Preserve a template position when it fits the facts; otherwise make the narrowest necessary change.

| Issue | Drafting direction |
|---|---|
| Program and product scope | Define the product, permitted internal use, authorized users, access conditions, and program objective. Avoid implying production readiness, unlimited use, or a service level that was not approved. |
| Mutual obligations | State what each side must do, who owns coordination, the feedback cadence, and any reasonable dependencies. Separate binding duties from goals or anticipated collaboration. |
| Feature commitments | Identify each promised feature, configuration, or deliverable; its target timing; dependencies; acceptance, if any; and change process. Preserve provider roadmap discretion for anything not expressly committed. Do not turn general feedback into unlimited bespoke development. |
| Fees and costs | State whether access is free or paid and allocate approved expenses and third-party costs. Specify payment timing and taxes if fees apply. Do not call a deal free while leaving uncapped pass-through costs. |
| Term and termination | Align the effective date, term, extensions, termination for convenience or cause, suspension, and effects of termination. Address access cutoff, accrued fees, return/deletion, transition, and survival. |
| Conversion | Prefer an optional later commercial agreement unless the parties intentionally choose another model. If a discount or credit applies, define eligible fees, duration, conditions, expiration, and exclusions. Never imply that a production subscription begins without its governing terms. |
| Confidentiality | Reconcile any prior NDA. Protect non-public product and partner information, state whether the agreement's existence is confidential, and distinguish usable feedback from the partner's confidential materials. |
| Data, security, and DPA | Separate identifiable Partner Data used to provide and support the program; bounded security, abuse, malfunction, and performance monitoring; customer-specific improvement; deidentified/aggregated global analytics; and model training. Define retention, isolation, deletion, reidentification limits, model providers, and DPA dependencies. Do not infer training rights from “improvement,” “analytics,” or “usage data.” |
| IP and feedback | Preserve each party's background technology and the partner's materials/data. Allocate custom features, deliverables, improvements, and derivative work expressly. Use either an assignment or a sufficiently broad license for feedback as selected; do not create joint ownership accidentally. |
| Publicity and references | Separate private identification from public name/logo use, case studies, testimonials, and reference calls. Define approval, permitted wording, revocation, and post-termination treatment. Silence is not consent. |
| Warranties and disclaimers | Calibrate early-stage and availability disclaimers to the product and law. Address authority and rights in contributed materials. Add regulated-industry or output-reliance disclaimers only when the use case supports them. |
| Liability and indemnity | Make an affirmative decision; do not silently inherit an omission. Select any consequential-damages exclusion, cap base and amount, carve-outs, and claim procedures. Decide whether there is no indemnity, a limited IP indemnity, or another negotiated allocation. Flag an uncapped or indemnity-free form rather than describing it as standard. |
| General terms | Check restrictions, non-exclusivity, assignment, notices, governing law/forum, modifications, entire agreement, order of precedence, independent-contractor status, third-party rights, equitable relief, counterparts, and survival. Separate this agreement from any other relationship unless incorporation is intentional. |

## Deterministic DOCX workflow

1. Verify that `assets/template.docx` exists and make a working copy. Never overwrite the asset.
2. Read the entire working copy, including tables, headers, footers, signature blocks, comments, and tracked changes. Record a source hash if the environment supports hashing.
3. Build an edit plan against the current copy using exact text and structural anchors. When the selected editor uses stable paragraph or table-cell identifiers, record those identifiers too. For every edit, record the issue, operation, exact anchor, complete replacement or insertion text, and rationale.
4. Apply each approved change with the available deterministic DOCX editor. If the editor uses blocks, use one operation per block and current identifiers. Use full replacement text; never reconstruct the agreement from extracted text or Markdown.
5. Validate the edit plan against the unchanged working baseline before application. If an anchor is missing or ambiguous, stop and re-extract rather than guessing.
6. If no deterministic DOCX editor is available, or the editor cannot safely
   reach required content, stop and provide the completed intake and
   clause-by-clause plan keyed to exact template anchors.
   State that no DOCX was modified. Never substitute a reconstructed Markdown or
   prose agreement for the template.
7. If editing succeeds, produce a clean DOCX by default and a tracked comparison only when requested. Re-read the resulting DOCX and verify that every approved edit appears exactly once and no content was truncated.
8. When the host can render DOCX, inspect every page and repair layout defects
   through the same edit path. Otherwise use text readback and disclose the
   unavailable visual check.

## Deliverable

If editing succeeds, deliver the drafted DOCX and a short decision summary covering:

- program and feature commitments;
- fees, term, termination, and conversion;
- data/DPA and IP/feedback choices;
- publicity, warranty, liability, and indemnity positions; and
- every remaining `[TBD]` or approval item.

For any unresolved liability, damages exclusion, carve-out, indemnity, data-use,
or ownership choice, include complete conditional clause options in the edit
plan. Do not leave the agreement with a non-operative drafting note as its only
risk allocation.

If step 6 triggered, deliver the intake, decision summary, and edit plan; do not
claim that a drafted DOCX was produced.

## Final checks

Before delivery, confirm:

- the agreement is truly a design-partner arrangement, not a mislabeled pilot or joint-development deal;
- party names, dates, product description, defined terms, section references, order of precedence, and signature blocks are consistent;
- every program and feature commitment has a clear scope and no drafting note, unused option, or client-specific example remains;
- data rights align with the actual data flow and a required DPA is attached or clearly gated;
- IP, feedback, publicity, conversion, liability, and indemnity decisions are explicit;
- the Data/AI distinctions in the drafting playbook were applied and identifiable
  Partner Data was not treated as deidentified merely because it supports
  product improvement;
- tracked-change status matches the request, and no unintended comments, metadata, or revisions remain in a clean deliverable; and
- the final file opens intact, matches the text readback, and renders correctly
  when the host supports rendering.

## Public comparator

The current Common Paper Design Partner Agreement may be used for issue spotting.
It is intentionally lean: omitted privacy/security terms, liability limits,
indemnities, or service commitments are not automatic drafting choices. Do not
replace `assets/template.docx`, copy its language, or call it market proof.
