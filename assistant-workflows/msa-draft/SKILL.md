---
name: msa-draft
description: >
  Drafts a provider-side Master Services Agreement or Customer Agreement from
  the bundled DOCX template for SaaS and SaaS-plus-professional-services deals.
  Use when the user asks to draft, prepare, set up, or customize an MSA,
  customer agreement, SaaS-plus-services agreement, or reusable house form,
  including order-form or SOW shells contained in the template.
  Do not use to review counterparty paper or negotiate an existing agreement;
  use an appropriate MSA-review workflow for those tasks.
license: MIT
metadata:
  version: 1.0.0
  author: Victor Wang
  language: English
  mike-display-name: MSA Draft
  mike-type: assistant
  mike-availability: system
  practice: Commercial
  jurisdictions: General
---

# MSA Draft

## Objective

Adapt a working copy of `assets/template.docx` into an attorney-review-ready
MSA. The template is a house starting point, not proof of a required position.

## Document rules

- Require `assets/template.docx`. Never edit, rename, or overwrite the bundled
  asset.
- Copy or replicate the template to a new deal file before making any change.
  Preserve styles, numbering, tables, headers, footers, exhibits, and fields.
- Use the host's deterministic DOCX editor when available. Work from stable
  document anchors or IDs taken from the working copy; do not rely on remembered
  paragraph numbers.
- If no deterministic DOCX editor is available, do not reconstruct the
  agreement from Markdown or silently edit OOXML. Deliver the intake and an
  exact-anchor edit plan, and state that the DOCX was not modified.
- Draft from the bundled template and confirmed facts; do not insert language
  from a public form.
- Record unresolved facts as `[TBD]`; never invent a party name, commercial
  term, security promise, or capability. Use conditional options—not a bare
  `[TBD]`—for unresolved material choices under the confirmation rules below.
- Do not send, sign, publish, or share the output. Deliver it for human review.

## Run the intake

Use facts already supplied and do not re-ask them. Ask the remaining questions
in short, related groups. Explain choices in plain language and confirm the
decision summary before editing the document.

### 1. Choose the drafting mode

- **Deal draft:** Populate the current customer, effective date, pricing, term,
  and other transaction facts.
- **Reusable house form:** Ask how the provider normally does business. Keep
  customer identity, effective date, fees, and other per-deal values as labeled
  `[TBD]` fields.

### 2. Collect the required facts

| Area | Ask for |
|---|---|
| Parties | Provider and customer legal names; entity types and jurisdictions; effective date; notice and signature details. |
| Product | Concise product description; hosted services and documentation; authorized users, usage limits, restrictions, beta features, and third-party components. |
| Deal structure | SaaS only or SaaS plus professional services; order-form mechanics; precedence among the MSA, order form, DPA, SOW, and SLA. |
| Commercial terms | Fees and currency; invoicing; payment period; taxes; disputed invoices; late charges; suspension; price changes; reimbursable expenses. |
| Term | Initial term; auto-renewal and opt-out notice; termination for breach or insolvency; any convenience termination; post-termination access, transition, and data return or deletion. |
| Support and SLA | Support tier, hours, contacts, response targets, uptime commitment, exclusions, service credits, chronic-failure remedy, and whether credits are the sole SLA remedy. Confirm that operations can meet every promise. |
| Professional services | Service model; SOW requirements; scope, milestones, dependencies, change control, personnel, fees, expenses, deliverables, acceptance criteria, cure period, and services warranty. Skip this branch if no services are sold. |
| Data and security | Data types and sensitivity; provider/customer privacy roles; security commitments; subprocessors; breach notice; applicable DPA, BAA, or regulated-data requirements. |
| Data use and AI | Define prompts/Input, Output, Customer Data, feedback, usage telemetry, performance and evaluation metrics, embeddings, retrieval context, caches, and other derived data. Map service delivery, operational monitoring, customer-specific improvement, global product improvement, and model training separately; identify model providers, retention, isolation, opt-outs, and product controls. Match actual behavior. |
| Intellectual property | Ownership of the platform, documentation, Customer Data, feedback, pre-existing materials, generic know-how, and custom deliverables; any licenses or license-backs. |
| Risk allocation | Product and services warranties; disclaimers; provider and customer indemnities; defense and settlement control; direct-damages cap; excluded damages; carve-outs or super caps. |
| Other terms | Confidentiality; insurance actually carried; publicity; assignment/change of control; subcontracting; force majeure; governing law, venue, and dispute process. |

### 3. Require express confirmation for material choices

Do not silently default any of the following:

- ownership of custom deliverables and treatment of pre-existing materials;
- permission to train on or otherwise reuse Customer Data content;
- whether performance metrics, agent-output evaluations, prompts, configurations,
  or other derived data may improve results solely for the customer or the
  product globally;
- regulated or sensitive data commitments and the need for a DPA or BAA;
- indemnity scope, liability carve-outs, and any enhanced or uncapped exposure;
- uptime, security, insurance, support, or implementation promises that depend
  on actual operational capability; and
- termination for convenience or other unusual commercial concessions.

If free-text notes conflict with a structured answer, follow the structured
answer and flag the conflict. Identify every inference in the decision summary
for confirmation.

Do not resolve an unapproved material choice with invented language or a bare
`[TBD]`. In the decision ledger—a change list keyed to exact anchors—provide
complete conditional options, the recommended provider-side opening position
and tradeoff, and mark every option non-operative until approved.

If the facts support more than one material transaction structure, draft each
viable branch completely enough for counsel to select it. A blocking question
alone is not an adequate deliverable for the deal's central ownership, license,
exclusivity, revenue-share, or order-form architecture.

## Complete-coverage gate

Before editing or delivering an edit plan, make a private coverage ledger for
every instrument contained in the supplied DOCX: cover page, MSA body, each
order-form or SOW shell, SLA, schedule, exhibit, option, and drafting note. Mark
each item `edit`, `retain`, `delete`, `not applicable`, or `open`, with the
reason and dependencies. Do not narrow the assignment to the MSA body when the
template itself contains transaction documents needed to implement the facts.

Test the document architecture against the actual transaction. In particular:

- determine whether multiple order forms or SOWs operate concurrently and fix
  any supersession language that would cancel a sibling instrument;
- keep the hosted Product and professional-services or custom-deliverable scope
  distinct where access rights, warranties, acceptance, and the SLA depend on
  that distinction;
- scope each SLA, support tier, fee table, and term to the correct product or
  order form; and
- conform every precedence, cross-reference, survival, termination, and exhibit
  reference affected by a selected structure.

## Apply the house starting positions

Use these only as provider-side opening positions when the user has not supplied
a different approved playbook. Confirm any position that materially affects
risk or product behavior.

| Issue | Starting position | Negotiation alternative |
|---|---|---|
| Structure | Put deal economics in an order form; use a SOW for professional services. | Add deal-specific detail without duplicating the MSA. |
| Access rights | Grant a limited right to use the service during the term; prohibit resale, interference, circumvention, and unauthorized access. | Tailor affiliates, contractors, user counts, and permitted-purpose language. |
| Professional services | Define scope, milestones, dependencies, change control, acceptance, and fees in a SOW. | Use deemed acceptance and a cure/re-performance process if objective testing is unavailable. |
| Deliverables | Preserve platform, background IP, tools, and generic know-how; state who owns bespoke deliverables. | Assign identified bespoke work while reserving background IP and a license-back. |
| Customer Data | Customer retains ownership; provider may use it to provide, secure, support, and comply with law. | Permit narrowly defined deidentified/aggregated analytics that cannot identify the customer or individuals. |
| AI/ML | Do not authorize training on Input, Output, retrieval context, or customer content without express support. Preserve inference and bounded monitoring. | Permit defined customer-specific optimization or non-content metrics; allow global training only if approved, supportable, and aligned with the DPA and disclosures. |
| Payment | Use clear invoice and dispute periods, taxes, late-payment consequences, and a notice/cure path before suspension. | Extend the cure period or limit suspension to undisputed overdue amounts. |
| Warranty and SLA | Limit warranties to substantial conformity and professional/workmanlike services; use repair, re-performance, credit, or termination/refund as the stated remedy. | Add a defined cure period or chronic-failure termination right. |
| Indemnity | Provider IP infringement indemnity with defense control and a cure cascade; customer protection for customer content and unlawful or unauthorized use. | Narrow claim triggers, add reciprocal procedure, or place specified claims under a higher but bounded cap. |
| Liability | Exclude indirect and consequential damages and use a mutual direct-damages cap tied to a defined fee period. | Use a separate negotiated super cap for selected data, confidentiality, or indemnity risks rather than uncapped exposure. |
| Term | Use a defined initial term and clear renewal notice; permit termination for uncured material breach and insolvency. | Add limited convenience termination only with an agreed economic consequence. |
| Publicity | Require written consent before public use of names or logos unless the user approves reference rights. | Permit customer-list name or logo use subject to brand guidelines and revocation. |

## Edit the working copy

1. Read the entire working copy, including tables, headers, footers, exhibits,
   signature blocks, drafting notes, option blocks, and defined terms.
2. Complete the coverage ledger and architecture tests above for every
   instrument in the supplied file.
3. Build a decision ledger before editing. For each change, record the issue,
   confirmed fact, section or anchor, operation, complete proposed text,
   rationale, dependencies, and any remaining `[TBD]`.
4. Apply only confirmed decisions. Select one option where the template offers
   alternatives; remove the unselected option, its label, and its drafting note.
5. Delete professional-services provisions and related definitions only when
   the deal is SaaS-only and no services obligation remains elsewhere.
6. Keep Customer Data, AI/ML, DPA, security, breach, indemnity, and liability
   provisions aligned. Keep SOW, deliverables, acceptance, warranty, expenses,
   and termination provisions aligned.
7. For deterministic edits, use complete replacement text, anchor insertions to
   current text, avoid conflicting operations on the same block, validate before
   applying, and re-read the resulting document after each batch.
8. Remove all drafting instructions, option headings, selection prompts,
   internal comments, and rejected alternatives from the clean draft.

If no deterministic editor is available, deliver an edit plan using the same
fields as the decision ledger, with exact anchor text. Do not claim the DOCX was
modified.

## Deliverables

Provide:

1. the completed clean DOCX, when document editing is available;
2. a short drafting memo listing selected positions, deviations from the
   template, assumptions, inferences, `[TBD]` items, and attorney decisions; and
3. companion-document flags for any required DPA, SOW, SLA, BAA, security
   exhibit, or order form.

## Final checks

Before delivery:

- confirm party names, entity details, dates, fees, renewal periods, notice
  periods, percentages, caps, and insurance limits everywhere they appear;
- confirm every defined term is used consistently and every cross-reference,
  exhibit reference, and order-of-precedence rule resolves;
- confirm deal structure, data/AI rights, risk allocation, remedies, survival,
  and companion documents are coherent with actual product behavior;
- search for drafting notes, option labels, internal instructions, comments,
  hidden revisions, stray client names, and unexplained placeholders;
- verify the output opens with intact numbering, tables, headers, footers, and
  signatures; render and inspect each page when the host supports it, otherwise
  use text readback and disclose the unavailable visual check; and
- obtain human approval for deliverables IP, AI/ML rights, regulated data,
  indemnity, liability, and any nonstandard operational commitment.

## Public comparator

The current Common Paper Cloud Service Agreement may be used for issue spotting
only. It is not proof of market practice and does not replace the bundled MSA;
do not copy its language into the draft.
