---
name: "proofread"
description: "Review the uploaded document for drafting quality, internal consistency, and mechanical errors."
license: "MIT"
metadata:
  version: "1.1.0"
  author: "Anna Guo"
  language: "English"
  mike-display-name: "Proofread"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "General Transactions"
  jurisdictions: "General"
---
# Proofread

## Instructions

Review the uploaded document for drafting quality, internal consistency, and mechanical errors. Focus on issues that a lawyer or reviewer should correct before the document is circulated, signed, or filed.

Treat this as a forensic audit, not a quick read-through. Inconsistent numbering, stale cross-references, dead definitions, future-dated metadata, and hidden hyperlinks do not jump out on a single read. They require deliberate, structured passes with different lenses. **The standard:** when you finish, a second reviewer should find nothing material that you missed.

## Working Principles

- **Inspect the artefact, not just the text.** For document files, inspect the underlying structure—such as hyperlinks and their targets, fonts, styles, comments, and tracked changes—in addition to the rendered text when the available tools support it. Rendered text can hide defects such as an embedded `mailto:` target pointing to the wrong domain, an inconsistent font run, or an unaccepted revision. If only plain text or pasted content is available, say so explicitly and note that hyperlink, font, revision, comment, and metadata checks could not be performed.
- **Build reference maps first, then audit.** You cannot spot a stale cross-reference without a section map or a dead definition without a defined-terms map. Build these before reviewing individual defects.
- **Use separate passes, each with one lens.** Trying to catch everything in one read misses issues. Treat each review category below as its own pass.
- **Flag, do not silently fix.** Surface defects so the reviewer can decide. Do not rewrite the document.
- **Separate errors from style preferences.** A genuine error is unambiguously wrong, such as a misspelling, a reference to a clause that does not exist, or an incorrect date. A style choice, such as use of the Oxford comma or UK rather than US spelling, is only an issue when it is internally inconsistent. Overflagging undermines the credibility of the review.

## Step 1: Extract and Inspect

For document files, inspect both the rendered content and the underlying structure when supported, including paragraph text, hyperlink targets, font runs, paragraph styles, comments, and tracked changes. For PDFs, inspect the extracted text together with the rendered pages and document structure. For cloud-hosted documents, inspect the rendered document and its layout. If the file itself is unavailable and only text is in context, proceed but state that the metadata and visual-layout passes could not be completed.

## Step 2: Build Reference Maps

Before reviewing individual defects, build three maps:

- **Entity map** — every name used for each party, including exact capitalization, punctuation, and spelling, together with where each form appears. Multiple variants of one company name may indicate an error.
- **Section and numbering map** — every heading and its number in order. Use it to identify missing numbers, jumps, duplicates, and mixed hierarchy levels. If a table of contents is present, map it separately for comparison.
- **Defined-terms map** — every term introduced as a definition, where it is defined, and each later use. Use it to identify inconsistent casing, capitalized but undefined terms, and dead definitions that are defined but never used.

## Step 3: Review Categories

Run each category as a separate pass. Apply the **paste-fingerprint heuristic** when multiple anomalies cluster in the same paragraph or block. For example, a font variance and a defective hyperlink together may indicate that text was pasted from an external source. Widen the review across that block for related defects such as wrong names, an incorrect jurisdiction, inconsistent quotation marks, or stray spaces. Treat the cluster as a reason for closer inspection, not conclusive proof of its origin, and report related defects together where that is clearer.

| Category | What to Check | Example |
| --- | --- | --- |
| Definitions | Defined terms used consistently, including case; all capitalized defined terms actually defined; no duplicate, conflicting, or circular definitions; dead definitions identified; and defined terms matching the operative provisions. | "Financial Information" is defined once but never used again → delete it or use it where intended. |
| Cross-References | Every clause, section, schedule, exhibit, annex, and document reference exists, points to the correct place, uses correct numbering, and remains accurate after apparent drafting changes. | The preamble says "Terms of Use" while clause 4 says "Terms of Service" for the same document → confirm and use one title consistently. |
| Internal Consistency | Terms, sections, dates, parties, amounts, thresholds, notice periods, conditions, remedies, or obligations that conflict or create inconsistent outcomes, including scope conflicts where a term includes Affiliates in one place but excludes them elsewhere. | "Confidential Information" includes Affiliates in clause 1 but excludes them in clause 9 → reconcile the scope. |
| Parties and Entity Names | Party names, entity suffixes, registration details, capacities, addresses, signatory names, and role labels used consistently; name variants differing by a letter, space, or capitalization; and legal-entity conflicts between the preamble and definitions. | "Acme Holdings, Inc." in the preamble but "Acme Holdings LLC" in the definitions → confirm the correct legal entity. |
| Numbers, Dates, and Calculations | Monetary amounts, percentages, dates, deadlines, time periods, notice periods, interest rates, formulas, schedules, and words-versus-figures consistency; future-dated metadata that may be incorrect. | "Under the age of 16 (seventeen)" → the digit and word disagree; confirm the intended threshold. |
| Grammar and Typos | Spelling, grammar, punctuation, missing words, articles or prepositions, duplicate words, repeated phrases, tense, subject-verb agreement, dangling modifiers, truncated or unfinished sentences, sentence fragments, missing possessives, and missing terminal punctuation. | "...such as a phone number or an)" → the sentence is truncated and the provision may be incomplete. |
| Numbering | Clause, section, sub-clause, schedule, exhibit, and table numbering; skipped, duplicate, or out-of-sequence numbers; unnumbered headings that should be numbered; and mixed hierarchy markers within one list. If a table of contents is present, verify that numbers, headings, and hierarchy match it exactly. | Sections run from 5 to 7 with no section 6, or two clauses are both labelled (vii) → identify the missing or duplicate number. |
| Formatting | Headings, list formatting, indentation, spacing, fonts, emphasis, table and schedule formatting, heading-case consistency, compound-word and hyphenation consistency; hyperlink targets that mismatch visible text; font variance from the body default; leftover comments or tracked changes; and whitespace anomalies. | Visible text says `privacy@acme.com` but the embedded `mailto:` target is `privacy@acme.com.ph` → correct the hidden target. |

## Severity Ratings

- **Critical** — an inconsistency or drafting error that may materially change rights, obligations, parties, timing, or enforceability, such as the wrong legal entity, a hyperlink directing a legal notice to the wrong recipient, incorrect operative metadata, or numbering defects that break the cross-reference scheme. Do not downgrade an issue merely because the visible difference is small.
- **High** — an error likely to create ambiguity, negotiation friction, or implementation risk, such as a truncated sentence, numerical conflict, material dead definition, or grammatical defect that changes meaning.
- **Medium** — a proofreading or consistency issue that should be fixed but is unlikely to change the main legal effect.
- **Low** — a minor typo, grammar, formatting, punctuation, or style issue.

Assign severity according to the likely consequence in the document under review, not merely the category of defect.

## Deliverable

Produce a concise Markdown table with exactly these columns:

- Severity
- Category
- Location
- Issue
- Recommended Fix

For each issue, give the best available clause, section, page, schedule, or paragraph reference in **Location**. If the location is unclear, describe where it appears as specifically as possible. In **Issue**, explain the defect and why it matters. In **Recommended Fix**, give a specific correction and include concise replacement wording where useful, but do not rewrite the whole document. Sort the table by severity, with Critical issues first.

After the table, add a short **Summary of most critical issues** listing the two to five items to fix first.

## Things That Are Not Errors

To keep findings credible, do not flag:

- consistent style choices you disagree with, such as the Oxford comma, US rather than UK spelling, or bullet rather than numbered lists, unless the usage is internally inconsistent;
- sentence length or readability unless the text is actually unclear or ungrammatical;
- valid word choices that are merely not your preference; or
- a reference to a clause by its top-level number where that clause exists and is sufficiently specific in context.

When uncertain whether something is an error or a style preference, identify that uncertainty rather than presenting the issue as definitively wrong.

## Before Finalizing

Confirm that you separately considered definitions, cross-references, numbering, formatting, parties and entities, numbers and dates, grammar, and internal consistency. If a table of contents is present, verify that its clause numbers and headings match the document. If you inspected the artifact, confirm that you completed the available metadata pass, including hyperlinks, fonts, comments, and tracked changes. If no material issues are found, provide a single table row stating so and note any review limitations, such as metadata not being inspected because only text was provided. Keep the response focused on actionable corrections.
