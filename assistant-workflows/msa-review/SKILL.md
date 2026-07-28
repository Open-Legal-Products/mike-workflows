---
name: msa-review
description: >
  Reviews supplied Master Services Agreements, customer agreements,
  SaaS-plus-services contracts, and counterparty redlines for commercial,
  intellectual-property, data, security, professional-services, indemnity, and
  liability risk. Use when the user asks to review, check, mark up, compare, or
  negotiate an MSA or customer agreement, including a redline of existing
  paper. Do not use to draft a new MSA from the bundled template; use an
  appropriate MSA-drafting workflow for that task.
license: MIT
metadata:
  version: 1.0.0
  author: Victor Wang
  language: English
  mike-display-name: MSA Review
  mike-type: assistant
  mike-availability: system
  practice: Commercial
  jurisdictions: General
---

# MSA Review

## Objective

Review the supplied agreement and its attachments as the operative contract.
Use `assets/template.docx` only as a house-form comparator for issue spotting,
fallback language, and negotiation posture. Never substitute the bundled
template for the supplied paper and never describe the house form as neutral or
as proof of market practice.

## Document rules

- Read the full supplied agreement before forming conclusions, including
  tables, headers, footers, hyperlinks, incorporated policies, order forms,
  SOWs, DPAs, SLAs, security exhibits, and redline history if available.
- Never edit or overwrite `assets/template.docx` or the user's original file.
  Make a working copy before creating a redline.
- Use the host's deterministic DOCX editor when available. If it is unavailable,
  deliver a review memo and structured edit plan; do not rebuild the agreement
  from Markdown or silently edit OOXML.
- Quote the contract accurately and distinguish contract text, user facts,
  assumptions, and recommendations.
- When tracked changes or comments exist, extract the full revision and comment
  record. Verify each comment author's side from the document or supplied facts
  before attributing a negotiating position; if affiliation is uncertain, name
  the author without assigning a side.
- Use only the user-supplied package as the factual record. A house form or
  public comparator may help build the private issue checklist, but do not cite
  it in the deliverable or introduce its facts unless the user asks for a
  comparison.
- Do not send, sign, publish, or share the output. Deliver it for human review.

## Establish the review posture

Use information already provided. Ask only for missing facts that affect the
analysis:

- Which party do we represent: provider/vendor or customer/buyer?
- Is this our paper, counterparty paper, or a response to prior redlines?
- What is the negotiation stage, deal value, leverage, deadline, and business
  priority, if known?
- Is the deal SaaS-only, professional services only, or both?
- What product, implementation, data, security, AI/ML, SLA, and regulated-data
  facts matter?
- Which order form, SOW, DPA, SLA, security exhibit, support terms, policies,
  and URL terms form part of the package? Identify referenced but missing items.
- Does the user want an issue memo, proposed language, a tracked-change DOCX, or
  all three?

Apply context in this order: current user instructions and deal facts; supplied
client or matter playbook; specifically approved prior positions; the bundled
house template; public comparators. Treat prior deals as evidence, not automatic
authority. When reviewing for a customer, invert the provider-oriented house
comparator rather than treating it as the customer's desired result.

## Review workflow

1. Read the package once for structure and business purpose without drafting
   edits.
2. Create a contract map covering parties, services, documents, economics,
   term, data flows, IP, risk allocation, termination, and dispute terms.
3. Create a private coverage ledger. Disposition every contract section,
   exhibit, incorporated document, and issue-playbook row as **Finding**,
   **Acceptable**, **Not Applicable**, or **Missing Information**. Do not
   finalize until every item has a disposition.
4. Run a structural-integrity sweep for blanks, undefined or unused terms,
   duplicate numbering, broken cross-references, wrong exhibit references,
   mutable URLs, signature defects, supersession, assignment, termination
   reach, and order of precedence.
5. Review each issue in context. A broad warranty may be contained by an
   exclusive remedy and cap; an IP assignment may be narrowed by background-IP
   reservations; a DPA or SOW may alter the MSA's practical effect.
6. For each material issue, identify the exact text, the gap from the desired
   position, the practical risk, proposed language, fallback, and dependencies.
7. Reconcile the package across documents before assigning final severity.
8. Prioritize a small set of must-haves. Use favorable terms as trade value and
   calibrate negotiable issues to leverage without concealing existential risk.

## Issue playbook

| Area | Review questions and house comparator | Common fallback |
|---|---|---|
| Parties and scope | Check parties, affiliates, users, services, incorporated versions, and whether an order form, URL, or policy can override negotiated terms. | Limit incorporated terms to identified versions and give negotiated documents precedence. |
| Access and restrictions | Check permitted users and purposes, usage limits, suspension, benchmarking, resale, and third-party access. | Tailor users and purposes; require notice and cure for non-emergency suspension. |
| Professional services | Confirm each services obligation runs through a SOW with scope, dependencies, change control, fees, and exit consequences. | Put project detail in the SOW and preserve MSA-level process and risk allocation. |
| Deliverables and acceptance | Separate bespoke work from background IP and open source; test whether acceptance is objective, time-limited, and curable. | Assign only identified bespoke work, reserve background IP, and use deemed acceptance plus cure. |
| Data and AI/ML | Are Customer Data, Input, Output, usage data, telemetry, performance metrics, evaluation results, feedback, embeddings, retrieval context, caches, and other derived data defined distinctly? Do rights for service delivery, operational monitoring, customer-specific improvement, global product improvement, and model training match product reality and the DPA? | Preserve necessary inference and bounded monitoring; separate customer-specific optimization from cross-customer improvement and training; permit only approved, defined uses with appropriate safeguards. |
| Privacy and security | Align roles, instructions, security, subprocessors, incidents, audits, transfers, and deletion with the DPA. | Move processing detail to a DPA and avoid unsupported promises. |
| Confidentiality | Check scope, exclusions, permitted recipients, care, compelled disclosure, remedies, return/destruction, and survival. | Use mutual, need-to-know obligations and longer trade-secret protection. |
| Fees and suspension | Check fees, disputes, expenses, overages, price changes, setoff, and suspension. | Limit suspension to undisputed overdue amounts after notice and cure. |
| Warranties and SLA | Align measurable warranties, disclaimers, credits, chronic failure, beta exclusions, and remedies. | Use repair, re-performance, credit, or termination/refund as stated remedies. |
| Indemnity | Check triggers, exclusions, defense, settlement, cure options, and customer-caused claims. | Narrow triggers, add reciprocal procedure and an IP cure cascade, and cap specified exposure. |
| Liability | What is the cap base, period, amount, and scope? Are paid versus payable fees clear? Which claims sit outside the cap and the indirect-damages waiver? Do the MSA, DPA, SLA, and SOW use the same allocation? | Mutual fee-based cap, indirect-damages exclusion, and bounded super caps for selected risks instead of uncapped exposure. |
| Term and exit | Align term, renewal, termination, refunds, transition, export/deletion, and survival. | Require breach cure, a practical export window, and agreed convenience-termination economics. |
| Insurance and publicity | Match insurance to actual coverage; make reference rights intentional. | Commit only to carried coverage; require consent or revocable reference rights. |
| Assignment and delivery model | Test change-of-control, subcontracting, personnel, and affiliate-use constraints. | Permit ordinary subcontracting and assignment with a business or change of control. |
| Boilerplate and disputes | Check notices, amendments, force majeure, export, forum, remedies, and entire agreement. | Choose a workable forum and coherent notice and electronic-contracting mechanics. |

## AI and ML review lens

When AI or ML features are present, do not treat “training,” “improvement,” and
“analytics” as interchangeable. Build a data-use matrix that separately maps:

- **Artifacts:** prompts and other Input; Output; Customer Data; user feedback;
  usage telemetry; latency, success, quality, safety, and other performance
  metrics; human or automated evaluation results; embeddings; vector-store or
  retrieval context; caches; fine-tunes, adapters, and model weights; and other
  derived, aggregated, or deidentified data.
- **Uses:** providing the feature; inference-time processing; security, abuse,
  malfunction, and abnormal-performance monitoring; improving results solely
  for that customer; improving the product across customers; and training,
  retraining, or fine-tuning any provider or third-party model.
- **Actors and controls:** provider personnel, model providers and other
  subprocessors; tenant isolation; retention; access; deletion; opt-out or
  administrative controls; notice of new AI features or model-provider changes;
  and responsibility for third-party compliance.

For each artifact/use pair, identify the contract's permission, prohibition,
retention period, safeguards, recipient, customer control, and DPA/privacy
dependency. Treat silence as unresolved, not permission.

When the package includes an AI addendum, disposition every clause and redline
in it, not only the general training restriction. Check specifically for:

- unilateral permission-revocation or suspension rights and their operational
  and fee consequences;
- retention, deletion, and return duties that reach Input, Output, fine-tunes,
  adapters, embeddings, evaluation data, or Trained Models;
- production-only or environment restrictions that could block testing,
  debugging, security review, or quality assurance;
- third-party and open-source model restrictions, including flow-down duties the
  model provider may not accept;
- accuracy, bias, hallucination, human-review, safety, high-impact-use, audit,
  governance, model-change, and monitoring duties;
- ownership of Input, Output, models, improvements, and derived data, plus
  output-similarity and infringement allocation; and
- how revocation, deletion, indemnity, confidentiality, and liability caps
  interact across the MSA, DPA, and AI addendum.

A no-training clause should preserve necessary inference and approved non-content
performance metrics. Conversely, “service improvement,” “usage data,” or
“deidentified data” must not silently authorize content or personal-data
training. Reconcile the matrix across the MSA, DPA, privacy disclosures, product
controls, and AI addendum, and specify which document controls.
Whether or not an AI addendum exists, verify Input and Output ownership or
licenses, output similarity and permitted use, human-review and accuracy duties,
high-impact-use limits, output-infringement allocation, and the applicable cap.

## Cross-document reconciliation

Check at minimum:

- **MSA / DPA:** data definitions and use, AI/ML rights, security, subprocessors,
  incident notice, audits, deletion, indemnity, liability, precedence, and term;
- **MSA / SOW:** scope, milestones, dependencies, acceptance, deliverables IP,
  change orders, fees, expenses, warranty, termination, and precedence;
- **MSA / order form:** product, users, usage limits, fees, payment, subscription
  term, renewal, support tier, and deviations; and
- **MSA / SLA or security exhibit:** uptime, exclusions, measurement, credits,
  chronic failure, sole remedy, security standards, and operational capability.

Flag a missing DPA, SOW, SLA, order form, security exhibit, BAA, support policy,
subprocessor list, or incorporated URL when the contract or actual deal requires
it. Do not imply that an unreviewed or inaccessible document is acceptable.

## Severity

| Level | Use when | Examples |
|---|---|---|
| **RED — must fix or approve** | Exposure may be existential, conflicts with product or privacy facts, or leaves a required deal document absent. | Uncapped material exposure; platform or background-IP transfer; data rights inconsistent with the DPA; broad indemnity without defense control; missing DPA for personal-data processing; material services without a SOW. |
| **YELLOW — negotiate with fallback** | The term creates meaningful commercial or operational risk but has a workable compromise. | Ambiguous cap base; broad compliance warranty; aggressive renewal or price increase; vague acceptance; impractical audit, notice, suspension, subcontractor, or personnel requirements. |
| **GREEN — acceptable or favorable** | The term matches the user's posture or is low-risk drafting cleanup. | Appropriate IP cure cascade; workable mutual confidentiality; approved publicity rights; non-substantive cleanup. |

Leverage changes how hard to push a YELLOW issue, not whether to disclose a RED
issue. Never recommend accepting company-threatening exposure without explicit
legal and business approval.

## Prepare the output

### Review memo

Cover:

1. **Bottom line:** whether the agreement is signable, what must change, and
   what may be conceded.
2. **Context:** represented side, paper, stage, deal type, documents reviewed,
   missing documents, and material assumptions.
3. **Key commercial terms:** term/renewal, fees/payment, scope/SOW, data and AI,
   deliverables IP, warranties/SLA, indemnity, and liability.
4. **Issues by severity:** for each issue include section, exact quote, gap,
   practical risk, proposed language, fallback, and approval path.
5. **Cross-document alignment and missing provisions.**
6. **Negotiation priorities:** must-have, should-have, and available trade.

Keep the bottom line selective. Report every material RED or YELLOW finding
supported by the coverage ledger; do not merge distinct findings merely to look
concise.

### Redline or edit plan

If the user requests a redline:

1. Make a working copy of the supplied paper, not the bundled comparator.
2. Use the host's deterministic DOCX editor to apply tracked changes and
   counterparty-facing comments when available.
3. For each change, record the document and section, exact quoted text, stable
   anchor, operation, complete proposed text, rationale, severity, fallback,
   and cross-document dependencies.
4. Validate anchors, avoid conflicting edits, and re-read the result. When the
   host can render DOCX, inspect each page; otherwise use text readback and
   disclose the unavailable visual check.

If no deterministic editor is available, provide that same information as a
structured edit plan and state clearly that the DOCX was not modified.

Do not over-redline acceptable language merely because the bundled house form
phrases it differently.

## Final checks

Before delivery:

- verify every quoted clause and section reference against the current supplied
  version, especially after applying edits; before asserting that a section,
  heading, or cross-reference does not exist, reconstruct the rendered numbering
  because Word auto-numbering may not appear in extracted text;
- verify party names, dates, fees, notice periods, renewal windows, service
  levels, caps, carve-outs, and insurance limits across all documents;
- check defined terms, numbering, cross-references, exhibit references, URL
  versions, order of precedence, survival, and signature blocks;
- confirm each RED and YELLOW issue has a concrete proposal and fallback, or a
  clearly identified business/legal approval path;
- confirm data, AI/ML, privacy, security, indemnity, liability, and the coverage
  ledger remain coherent and complete;
- distinguish missing information from adverse language and list all assumptions;
- remove internal drafting artifacts and ensure redline comments reveal no
  privileged negotiation strategy; and
- obtain human approval before any document is signed or sent.

## Public comparators

The current Common Paper Cloud Service Agreement and Bonterms Standard AI
Addendum may be used for issue spotting only. They are not proof of market
practice and do not replace the supplied agreement or bundled house form; verify
current versions and do not copy their language into the review or redline.
