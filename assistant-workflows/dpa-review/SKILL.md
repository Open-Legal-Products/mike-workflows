---
name: dpa-review
description: Review a supplied Data Processing Agreement, Data Processing Addendum, privacy addendum, or DPA redline for legal-floor and commercial issues, then provide prioritized findings and optional deterministic DOCX edits. Use when a customer or vendor sends DPA paper, a user asks to check or negotiate privacy terms, or an existing DPA must be compared with the bundled house template. Do not use to draft a new DPA from scratch.
license: MIT
metadata:
  version: 1.0.0
  author: Victor Wang
  language: English
  mike-display-name: DPA Review
  mike-type: assistant
  mike-availability: system
  practice: Commercial
  jurisdictions: General
---

# DPA Review

Review the supplied agreement as the operative paper. Use `assets/template.docx` only as a house-form comparator for issue coverage and fallback positions. Never replace supplied paper with the bundled template.

## Operating rules

- Establish the represented party, factual processing roles, and applicable legal floor before judging language. A processor-side and controller-side review often invert the preferred result.
- Read the full supplied DPA, cover page, schedules, security materials, incorporated links, transfer instruments, and underlying agreement before concluding the review.
- Separate legal or compliance defects from negotiable commercial preferences.
- Quote and anchor findings to the supplied paper. Do not report that the house template “requires” a position; explain the actual risk.
- Treat missing incorporated material as missing, not acceptable by assumption. Qualify the review when the underlying agreement or annexes are unavailable.
- Verify current law, official transfer forms, adequacy status, and certifications when material.
- Create a private coverage ledger before writing. Disposition every section,
  schedule, incorporated document, and review topic as **Finding**,
  **Acceptable**, **Not Applicable**, or **Missing Information**. The bottom-line
  summary may be short; the material findings table must be complete.

## Establish context

Determine or state a clearly labeled assumption for:

- Who is represented and whether the review posture is provider-side or customer-side.
- Whether each party is a controller, processor, subprocessor, independent controller, or joint controller for each processing activity.
- Whether the DPA is original paper, a counterparty redline, or an amendment to existing terms.
- The underlying MSA, SaaS agreement, order form, or services agreement and its defined terms.
- Applicable laws, regulated-data overlays, data locations, access locations, transfer corridors, and mechanisms.
- Data categories, data subjects, sensitive data, processing purpose, retention, and operational security posture.
- Deal leverage, must-have positions, approved fallbacks, and requested output: memo, comments, redline, or all three.

If role or direction remains uncertain, explain how that uncertainty changes the analysis rather than silently choosing a side.

## Review sequence

### 1. Processing roles, scope, and instructions

Check whether labels match reality and whether the DPA distinguishes controller-to-processor, processor-to-subprocessor, and any independent-controller processing. Verify:

- Processing occurs only for documented, lawful instructions and specified purposes.
- The processor must notify the controller if an instruction appears unlawful, subject to legal limits.
- Subject matter, nature, purpose, duration, operations, data subjects, data types, sensitive data, frequency, and retention are complete.
- Confidentiality duties bind authorized personnel.
- Controller obligations do not improperly shift the processor's mandatory duties.
- Product-improvement, analytics, deidentification, and AI/ML rights align with the underlying agreement and role allocation.

Wrong or ambiguous roles are a legal-floor issue because they can invalidate downstream duties and transfer-module choices.

Run a separate structural and deployment-fit sweep. Check party and product
identity, blank Main Agreement fields, definitions, duplicate or missing
numbering, every annex and schedule reference, incorporated URLs, assignment,
supersession, amendment scope, termination reach and cure, order of precedence,
and whether the DPA matches the actual deployment, geography, customer, and data
flow. Record broken references and mismatched paper as findings rather than
burying them inside another issue.

### 2. Applicable law and regulated-data gate

Map the actual relationship to EU GDPR, UK GDPR, Swiss FADP, CCPA/CPRA, other applicable US state laws, and any sectoral regime. Check whether the contract includes all mandatory processor terms for the regimes in scope without importing irrelevant regimes.

Escalate when PHI, financial information, education records, children's data, biometrics, precise location, communications content, or another specially regulated category may require a BAA or specialized terms beyond a generic DPA.

### 3. Subprocessors

Review:

- General or specific authorization and whether it is operationally workable.
- A current list or accessible URL and accurate processing locations.
- Advance notice of intended changes.
- A meaningful objection process and practical remedy if unresolved.
- Written flow-down of materially equivalent obligations.
- Responsibility for subprocessor performance.

Provider-side concerns include specific approval that can block infrastructure changes, unrestricted objections, and impractical termination. Controller-side concerns include no list, no notice, no objection right, weak flow-down, and no remedy.

### 4. Security and technical measures

Check whether the security commitment points to a complete exhibit, stable
document, current certification, or specific controls covering access,
encryption, monitoring, incident response, physical/network security,
resilience, data lifecycle, training, and vendor oversight.

For SCC annexes, reject empty, generic, or contradictory TOM descriptions. Compare promises with known operational practices and the underlying agreement. Flag absolute security warranties, prescriptive controls the represented party cannot meet, unilateral security changes, and obligations that depend on unavailable third-party systems.

### 5. Personal-data incidents

Check:

- Trigger: awareness, discovery, reasonable confirmation, actual breach, or any security event.
- Timing: “without undue delay,” a fixed outside period, or both.
- Required content, rolling updates, preservation, mitigation, and cooperation.
- Allocation of regulator, consumer, and public notices.
- Whether cost allocation or admissions language is overbroad.

Provider-side review should test whether the notice clock and information demands are operationally possible. Controller-side review should preserve enough time and information for its own statutory notices.

### 6. Assistance, audits, and regulator cooperation

Check assistance for data-subject requests, DPIAs, prior consultations, regulator inquiries, transfer assessments, compliance evidence, and incident response. Calibrate timing, scope, fees, and information-control procedures.

For audits, evaluate independent reports and certifications, written follow-up, on-site rights, frequency, notice, confidentiality, non-interference, auditor conflicts, production-system testing, regulator access, incident exceptions, and cost allocation. Provider-side review should resist unlimited customer-by-customer audits and penetration testing; controller-side review needs a meaningful verification path when reports are insufficient.

### 7. Return, deletion, and retention

Check the trigger, choice of return or deletion, completion period, certification, transition, and treatment of backups, logs, legal holds, and mandatory retention. Retained copies should remain protected, isolated from ordinary use, and deleted under the ordinary cycle when the exception ends. Compare the promise with product architecture and the underlying agreement.

### 8. International transfers

Identify each exporter, importer, role, origin, destination, remote-access route, onward transfer, and lawful mechanism. Then verify:

- Correct current SCC module—commonly Module 2 for controller-to-processor or Module 3 for processor-to-processor—without assuming either.
- Completed docking, optional clauses, supervisory authority, governing law, forum, annexes, parties, subprocessors, and TOMs.
- Correct UK Addendum or other current UK mechanism and required tables.
- Appropriate Swiss adaptations.
- Any adequacy or Data Privacy Framework reliance is current and verified.
- Transfer assessments and supplementary measures are addressed where required.
- Mandatory SCC or transfer-instrument precedence is preserved.

If an incorporated transfer document, URL, annex, or subprocessor list is missing, label the review partial and request it.

### 9. US state privacy terms

Where CCPA/CPRA applies, check the factual service-provider or contractor designation, specified business purposes, and applicable restrictions on selling, sharing, use outside those purposes or the direct relationship, and combining data. Check confidentiality, equivalent-level protection, monitoring or audit rights, remediation, and notice of inability to comply. Consider other applicable US state processor-contract requirements separately; do not assume California language satisfies all states.

### 10. Liability, indemnity, term, and precedence

Trace DPA claims through every definition, carveout, indemnity, damages exclusion, cap, super-cap, and order-of-precedence clause in both documents. Determine whether exposure is:

- Within the underlying agreement's general cap.
- Subject to a defined privacy or security super-cap.
- Subject to a separate fixed cap.
- Uncapped or functionally uncapped.

Flag duplicate recoveries, an indemnity that bypasses the negotiated cap, asymmetric regulatory-risk allocation, and conflicts between the DPA and underlying agreement. Confirm defense control, covered claims, exclusions, notice, and cooperation.

The DPA should generally control conflicts only for covered personal-data processing, while mandatory transfer instruments retain their required precedence. Confirm the DPA lasts as long as covered processing continues and does not accidentally amend unrelated commercial terms.

### 11. AI, ML, performance data, and derived data

When the service uses AI or ML, distinguish privacy-role compliance from the
separate commercial permission to use data. Build a data-use matrix covering:

- **Artifacts:** prompts and other Input; Output; Customer Personal Data; user
  feedback; usage telemetry; latency, success, quality, safety, and other
  performance metrics; human or automated evaluation results; embeddings;
  retrieval context and vector stores; caches; fine-tunes, adapters, model
  weights; and other derived, aggregated, or deidentified data.
- **Uses:** providing the service; inference-time processing; security, abuse,
  malfunction, and abnormal-performance monitoring; improving agent outputs or
  configurations solely for that customer; improving the product globally; and
  training, retraining, or fine-tuning any provider or model-provider model.
- **Actors and controls:** provider personnel, model providers and other
  subprocessors; access, isolation, retention, deletion, and reidentification;
  customer opt-out or administrative controls; new-feature and provider-change
  notice; and responsibility for downstream compliance.

For each artifact/use pair, identify the instruction or other legal basis,
contractual permission, purpose limitation, retention, safeguards, recipient,
customer control, and treatment at termination. Treat silence as unresolved.

Preserve necessary inference and approved non-content monitoring in any
no-training clause. Conversely, “service improvement,” “usage data,” or
“deidentified data” must not silently authorize content or personal-data
training. Determine whether improvements and artifacts are customer-isolated or
may benefit the product globally.

Reconcile these rights with controller instructions, purpose limitation,
subprocessor terms, deletion, transfers, security, the MSA, privacy disclosures,
product controls, and any AI addendum. Also flag Input/Output IP, output
similarity, accuracy and human-review duties, high-impact decisions, output
infringement, model-provider responsibility, and liability allocation when those
issues belong in the MSA or AI addendum rather than the DPA.


## Directional house positions

Use these as starting points, not automatic outcomes:

| Topic | Provider-side starting point | Customer-side starting point |
|---|---|---|
| Instructions | Defined service purposes and lawful documented instructions | Processing only for complete documented instructions |
| Subprocessors | General authorization, notice, reasonable objection | List, advance notice, flow-down, objection and remedy |
| Security proof | Independent reports/certifications first | Specific TOMs plus meaningful verification |
| Incident notice | Operationally achievable trigger and timing; rolling updates | Prompt notice with enough facts for statutory duties |
| Audit | Reports first; limited targeted audit | Reports plus targeted audit when evidence is insufficient |
| Deletion | Defined period with narrow backup/legal-retention exceptions | Prompt return/deletion, certification, protected exceptions |
| Liability | Agreement cap or approved super-cap | Cap proportionate to data sensitivity and exposure |
| Indemnity | No backdoor around the cap | Effective remedy for allocated third-party risk |

## Severity and recommendations

Classify each finding:

- **Red — must fix or obtain explicit legal approval:** wrong or unclear roles; missing mandatory processor terms; missing required transfer mechanism; incomplete SCC annexes or TOMs; missing sectoral addendum; uncapped or functionally uncapped exposure; material conflict with the underlying agreement; or an obligation the represented party cannot lawfully or operationally perform.
- **Yellow — negotiate or verify:** restrictive subprocessor approval, impractical incident timing, broad audit rights, generic security language curable by evidence, deletion inconsistent with backups, or a broad but capped indemnity.
- **Green — acceptable or note:** aligned roles and processing details, reasonable authorization and notice, usable audit evidence, workable deletion exceptions, and intentional cap alignment.

For every Red or Yellow issue provide:

1. Section or schedule and exact quote.
2. The gap and whether it is a legal-floor, operational, commercial, or alignment issue.
3. Practical consequence for the represented party.
4. Specific proposed edit or comment.
5. Negotiation fallback or factual verification needed.

Do not over-redline acceptable language merely because the bundled template phrases it differently.

## Output

Provide a review memo with:

1. **Bottom line:** signability, must-fix issues, and the next action.
2. **Context and assumptions:** roles, paper direction, laws, transfers, data, documents reviewed, and missing materials.
3. **Legal-floor table:** roles/instructions, processor duties, US state terms, transfers, TOMs, and any sectoral overlay.
4. **Findings by severity:** the five-part analysis above.
5. **Underlying-agreement alignment:** data/AI use, security, incidents, liability/indemnity, deletion, term, and precedence.
6. **Negotiation priorities:** a short ranked list with fallbacks.

The ranked list may be short, but do not cap or combine materially distinct
findings merely to keep the memo concise.

If the user requests only a high-level review, keep the memo concise but do not omit legal-floor defects. If the user asks for a redline, also prepare deterministic edits to a copy of the supplied DOCX.

## Build a redline deterministically

1. Preserve the supplied file and create a byte-for-byte working copy.
2. Read the complete document, including tables, schedules, headers, footers, comments, and existing revisions.
3. Build an edit-intent list containing section, exact quote, surrounding anchor, operation, complete proposed text, rationale, severity, dependencies, and fallback.
4. Apply only approved edits. If the editor uses block IDs, use current IDs, one
   operation per block, complete replacement text, and strict validation.
   Re-extract after any intervening change; never reuse stale IDs.
5. If two edits affect the same block, reconcile them into one complete operation before application. Fail on unresolved conflicts.
6. If the editor cannot safely reach a table, schedule, header, or footer, return the edit-intent list and identify the limitation rather than silently omitting the edit.
7. Keep tracked changes visible in the redline and attach concise counterparty-facing comments only where they help negotiation. Do not include internal strategy in margin comments.

Do not rebuild supplied paper from Markdown or substitute `assets/template.docx` as the redline base.

## Final checks

Before delivery:

- Re-read the supplied paper, review memo, and any redline.
- Confirm every material section, schedule, and available incorporated document
  was reviewed and dispositioned in the coverage ledger.
- Confirm roles, processing, security, incidents, assistance, audits, deletion,
  transfers, US terms, risk allocation, term, and precedence are addressed.
- Verify every quote, section number, recommendation, cross-reference, SCC
  selection, annex reference, and underlying-agreement citation. Before asserting
  that a section, heading, or cross-reference does not exist, reconstruct the
  rendered numbering because Word auto-numbering may not appear in extracted
  text.
- Confirm the AI/ML data-use matrix was applied.
- Confirm proposed language does not contradict another provision or promise controls the represented party cannot meet.
- Validate and reopen the DOCX. When the host can render, inspect every page;
  otherwise use text readback and disclose the unavailable visual check.
- Compare the applied edits with the edit-intent list; require all expected edits and no unexplained edits, skipped operations, truncation, or corruption warnings.
- Clearly state any missing document, unresolved fact, legal research dependency, or tool limitation. Do not call a qualified review complete without the qualification.

## Public comparators

The current Common Paper DPA and Bonterms Standard AI Addendum may be used for
issue spotting only. They are not proof of market practice; verify current
versions and do not copy their language or replace the supplied agreement.
