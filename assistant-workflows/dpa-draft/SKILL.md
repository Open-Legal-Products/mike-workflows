---
name: dpa-draft
description: Draft a provider-side Data Processing Agreement from the bundled DOCX template after structured intake covering party roles, processing details, security, subprocessors, incidents, audits, deletion, international transfers, US privacy terms, and risk allocation. Use when a service provider or vendor asks to draft, prepare, create, or customize its DPA or privacy addendum. Do not use to draft customer-side paper, review counterparty paper, or negotiate an existing DPA.
license: MIT
metadata:
  version: 1.0.0
  author: Victor Wang
  language: English
  mike-display-name: DPA Draft
  mike-type: assistant
  mike-availability: system
  practice: Commercial
  jurisdictions: General
---

# DPA Draft

Draft from `assets/template.docx`. Preserve its structure and formatting while tailoring it to the actual processing relationship. Do not recreate the agreement from prose or substitute a public form.

## Operating rules

- Treat the bundled template as the sole drafting base. Work on a copy and never overwrite it.
- Determine facts before selecting clauses. Do not assume that every SaaS vendor is a processor or that every international relationship requires SCCs.
- Use plain-language questions in small groups. Reuse facts already supplied; do not ask twice.
- Distinguish facts, recommended positions, and user-approved positions. Mark unresolved deal facts `[TBD]`; never invent them.
- Verify current law and official transfer instruments when the answer turns on a changing legal requirement.
- Treat the current Common Paper DPA only as an issue-spotting comparator. Do not copy its language or replace the bundled template.
- Escalate unusual regulated data, uncertain role allocation, conflicting instructions, or a requested legal position that may not satisfy an applicable legal floor.

## Intake

Collect enough information to complete every applicable body provision and schedule.

### 1. Parties and underlying agreement

Ask for:

- Company and customer legal names, addresses if needed, effective date, and signatories.
- The underlying MSA, SaaS agreement, order form, or other agreement and its defined terms.
- Whether the DPA should be incorporated into, attached to, or stand apart from that agreement.
- The governing law and order-of-precedence structure in the underlying agreement.
- Existing data-use, deidentification, analytics, service-improvement, or AI/ML permissions that the DPA must match.

If the underlying agreement is available, read the relevant privacy, security, confidentiality, data-use, incident, termination, indemnity, liability, and precedence provisions before drafting. If it is unavailable, identify every alignment item that remains conditional.

### 2. Factual roles and instructions

Identify roles from conduct, not labels:

- **Controller to processor:** Customer determines the purposes and essential means; Company processes on documented instructions.
- **Processor to subprocessor:** Customer processes for another controller and appoints Company in the processing chain.
- **Independent or joint controller activity:** Do not force controller activity into processor language. Define or separately document it.

Capture the permitted instructions, service purpose, any legally required processing outside instructions, and the escalation process for an instruction that appears unlawful. Confirm which party receives data-subject requests and regulator inquiries.

### 3. Processing description

Populate the processing schedule with:

- Subject matter, nature, purpose, and duration.
- Categories of data subjects.
- Categories of personal data and any sensitive, special-category, criminal, biometric, financial, health, precise-location, or children's data.
- Processing operations, systems, locations, transfer frequency, and access model.
- Retention period and deletion triggers.
- Controller rights and obligations.

Use a tailored description. “Providing the services” alone is insufficient when the actual processing can be described more precisely.

For AI- or ML-enabled services, also map:

- each product feature and processing channel, including portal, API, messaging,
  integrations, batch processing, and human review;
- whether outputs support or make decisions, who validates them, and who handles
  challenges or legally significant consequences;
- prompts and other Input, Output, source records, feedback, usage telemetry,
  performance and evaluation metrics, embeddings, retrieval context, caches,
  fine-tunes, and other derived data;
- retention and deletion by artifact rather than one undifferentiated period;
- model providers and other subprocessors, their locations, retention, and data-
  use restrictions; and
- customer notices, consents, lawful-basis responsibilities, opt-outs, and other
  instructions relevant to those uses.

Separate permission to provide the service, bounded operational monitoring,
customer-specific improvement, global product improvement, and model training.
Do not infer one permission from another. A no-training position should not
accidentally prohibit necessary inference or approved use of non-content
performance metrics, while “service improvement” or “usage data” language must
not silently authorize training on Input, Output, retrieval context, or personal
data.

### 4. Applicable regimes and transfer corridors

Determine the actual people, establishments, data locations, access locations, and transfer routes. Consider:

- EU GDPR and EEA transfers.
- UK GDPR and UK transfers.
- Swiss FADP and Swiss transfers.
- CCPA/CPRA and other applicable US state processor-contract requirements.
- Sectoral requirements such as HIPAA, GLBA, FERPA, COPPA, or another specialized regime.

Do not add jurisdictions merely because the template offers them. Do not treat a generic DPA as a substitute for a required BAA or other sector-specific addendum.

For a restricted transfer, identify the available lawful mechanism before selecting contract language. If SCCs are used, select the module that matches the factual chain—commonly Module 2 for controller-to-processor or Module 3 for processor-to-processor—and complete all selections and annexes. Address the UK Addendum or other current UK mechanism and Swiss adaptations where applicable. Record whether adequacy or a verified Data Privacy Framework certification applies, and whether a transfer assessment or supplementary measures are required. Never claim or rely on a certification without verification.

### 5. Subprocessors

Ask for the current list or URL, processing locations, change-notice period, and operational approval model.

Provider-side baseline:

- General written authorization.
- Current list plus advance notice of intended additions or replacements.
- Objection limited to reasonable data-protection grounds.
- Good-faith resolution, with a practical termination or service-change path if unresolved.
- Written flow-down of materially equivalent data-protection duties.
- Company remains responsible for its subprocessors to the extent required by law and the negotiated agreement.

Use specific prior written approval only when required by the facts, regulation, or approved deal posture; confirm the business can operate it.

### 6. Security and incidents

Describe only controls the Company actually maintains. Use a complete security
schedule, incorporated exhibit, or stable security-document URL, addressing as
applicable access, encryption, monitoring, vulnerability and incident response,
physical/network security, resilience, data lifecycle, training, and vendor
oversight.

For SCC annexes, provide sufficiently specific technical and organizational measures; do not rely only on “appropriate security.” Reconcile every statement with actual practices, certifications, and the underlying agreement.

Set the incident clause by operational capability:

- Define the trigger precisely, distinguishing an attempted event from a confirmed personal-data breach where appropriate.
- Use “without undue delay” and any agreed outside period only if operations can meet it.
- Require known details, affected data and people, likely consequences, mitigation, contact information, rolling updates, evidence preservation, and reasonable cooperation.
- Allocate regulatory and data-subject notifications consistently with the parties' roles; do not let the processor notify externally without controller direction unless law requires it.

### 7. Assistance, audits, and cooperation

Cover reasonable assistance with data-subject requests, security inquiries, regulator consultations, DPIAs, transfer assessments, and breach response, taking account of the nature of processing and information available to the processor.

Provider-side audit baseline:

- Supply current independent reports or certifications first.
- Permit targeted written follow-up where those materials are insufficient.
- Limit routine audits by frequency, scope, notice, confidentiality, non-interference, and cost allocation.
- Preserve broader access when an authority requires it or a material incident or substantiated compliance concern warrants it.
- Do not promise customer-directed penetration testing against production systems.

State any fees for extraordinary assistance without charging for work the processor must perform to cure its own breach or noncompliance.

### 8. Return, deletion, and survival

Specify whether data is returned, deleted, or both at termination or instruction; the completion period; certification on request; and transition mechanics. Include narrow backups, logs, legal-hold, and mandatory-retention exceptions, with continued protection and no further use. Align the clause with actual retention architecture and the underlying agreement. Continue the DPA while Company processes covered personal data.

### 9. US state privacy terms

Where Company acts as a CCPA service provider or contractor, include the required business-purpose scope and restrictions applicable to the relationship, including restrictions on selling or sharing, use outside the specified purposes or direct business relationship, and combining data except as permitted. Include appropriate confidentiality, equivalent-level protection, audit or monitoring rights, remediation, and notice if Company can no longer comply. Address any applicable US state processor-contract requirements without assuming one California clause satisfies every state.

### 10. Liability, indemnity, and precedence

Choose intentionally among:

- DPA claims inside the underlying agreement's general cap.
- A defined, higher privacy or security super-cap.
- A separately negotiated fixed cap.
- An express carveout approved by the user.

State the relationship between caps and claim categories clearly; avoid double counting and accidental uncapped exposure. Align any DPA indemnity with the underlying agreement, or use a standalone indemnity only when necessary and approved. Confirm defense control, covered third-party claims, exclusions, notice, cooperation, and whether the indemnity is subject to the selected cap.

Provide that the DPA controls conflicts only to the extent concerning covered personal-data processing. Preserve any mandatory precedence of SCCs or other transfer instruments. Avoid broadly displacing unrelated commercial terms in the underlying agreement.

## Complete-coverage gate

Before editing or delivering an edit plan, make a private coverage ledger for
every cover-page field, body section, subsection, schedule, annex, and option in
the template. Mark each item `edit`, `retain`, `delete`, `not applicable`, or
`open`, with its dependency and reason. Do not silently omit assistance, audit,
deletion, liability, precedence, or conflict provisions merely because the main
commercial changes sit elsewhere.

When an edit makes another provision inaccurate or inert, include every
conforming edit in the plan. In particular, deleting or disabling a transfer
schedule requires checking all definitions, precedence clauses, liability
carveouts, annex references, and survival provisions that point to it. Run the
same dependency check for changes to incident timing, subprocessors, deletion,
AI/ML permissions, and the underlying-agreement cross-references.

An unknown fact or required local-law approval does not justify an unusable
placeholder where the drafting choice is otherwise known. Provide complete
conditional language for each viable option, label the assumption and approval
gate, and recommend which option should become operative after confirmation.
Use a bare `[TBD]` only for a value that cannot responsibly be bounded or for
language that genuinely requires jurisdiction-specific advice. Never present
conditional local-law language as verified law without checking an official
source or obtaining the required local-law review.

## Confirm the drafting plan

Before editing, summarize and obtain confirmation of roles; processing and
sensitive-data scope; applicable laws, transfers, and SCC module; subprocessors;
security and incident timing; audits and assistance; return/deletion; the AI/ML
data-use map above; US or sectoral terms; liability, indemnity, term, precedence;
and every unresolved fact or underlying-agreement assumption.

## Build the DOCX deterministically

1. Copy `assets/template.docx` to a new working file.
2. Read the entire copy, including cover-page tables, body text, schedules, headers, footers, comments, and existing revisions.
3. Create an edit plan keyed to exact text and structural anchors. Include the complete replacement text, rationale, dependencies, and any required table-cell edit.
4. Reconcile the edit plan against the complete-coverage ledger. Every template item must have a disposition, and every removed or changed mechanism must have all dependent references conformed.
5. Resolve every mutually exclusive option. Remove unused options and all drafting instructions without deleting adjacent substantive text.
6. Apply edits to the working copy only. If the editor uses block IDs, use current
   IDs, one operation per block, complete replacement text, and strict
   validation. Re-extract after any intervening change; never reuse stale IDs.
7. If no deterministic DOCX editor is available, or the available editor cannot
   safely modify required content, stop and provide the completed intake and edit
   plan rather than flattening or omitting content. State that no DOCX was
   modified and identify the unavailable capability.
8. Produce a clean DOCX by default. Produce a tracked comparison only if requested.

Do not regenerate the document from Markdown, paste it into a new blank DOCX, or normalize styles globally.

## Deliverables

Provide the clean DPA, a concise memo covering selected positions, assumptions,
unresolved facts, and approvals, plus a verification summary. If step 7
triggered, provide instead the completed intake, exact-anchor edit plan, and a
limitation note stating that the bundled template remains unmodified.

## Final checks

Before delivery:

- Re-read the output and compare it with the source copy and confirmed drafting plan.
- Confirm correct party names, roles, effective date, defined terms, and underlying-agreement references.
- Confirm the processing schedule is complete and consistent with the operative clauses.
- Confirm every retained jurisdictional part applies and every required transfer annex is present and completed.
- Confirm the SCC module, parties, governing-law selections, annexes, UK/Swiss modifications, and TOMs align.
- Confirm subprocessor, security, incident, audit, assistance, deletion, risk
  allocation, precedence, and the AI/ML data-use map are coherent with the
  underlying agreement and operationally supportable.
- Search for drafting notes, option labels, bracketed guidance, duplicate alternatives, unresolved placeholders, client-specific residue, comments, and unintended tracked changes. Disclose any approved `[TBD]`; otherwise remove all such artifacts.
- Validate and reopen the DOCX. When the host can render, inspect every page;
  otherwise use text readback and disclose the unavailable visual check.
- Never describe the draft as final or execution-ready while material facts, transfer details, schedules, or required approvals remain unresolved.
