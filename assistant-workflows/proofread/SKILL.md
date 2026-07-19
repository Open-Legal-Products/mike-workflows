---
name: "proofread"
description: "Review the uploaded document for drafting quality, internal consistency, and mechanical errors."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Open Legal Products"
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

Produce a concise Markdown table with exactly these columns:

- Severity
- Category
- Location
- Issue
- Recommended Fix

Use these severity ratings:

- Critical: an inconsistency or drafting error that may materially change rights, obligations, parties, timing, or enforceability.
- High: an error likely to create ambiguity, negotiation friction, or implementation risk.
- Medium: a proofreading or consistency issue that should be fixed but is unlikely to change the main legal effect.
- Low: a minor typo, grammar, formatting, punctuation, or style issue.

Review the document for these categories:

| Category | What to Check |
| --- | --- |
| Definitions | Check that defined terms are used consistently, all capitalized defined terms are defined, definitions are not duplicated or conflicting, definitions are not circular, unused definitions are identified, and defined terms match the operative provisions. |
| Cross-References | Check that clause, section, schedule, exhibit, annex, and document references exist, point to the correct place, use the correct numbering, and remain accurate after any apparent drafting changes. |
| Internal Consistency | Check for terms, sections, dates, parties, amounts, thresholds, notice periods, conditions, remedies, or obligations that conflict with each other or create inconsistent outcomes. |
| Parties and Entity Names | Check that party names, entity suffixes, registration details, capacities, addresses, signatory names, and role labels are consistent throughout the document. |
| Numbers, Dates, and Calculations | Check monetary amounts, percentages, dates, deadlines, time periods, notice periods, interest rates, formulas, schedules, and words-versus-figures consistency. |
| Grammar and Typos | Check spelling, grammar, punctuation, missing words, duplicate words, repeated phrases, tense, subject-verb agreement, and obvious typographical errors. |
| Numbering | Check clause numbering, section numbering, sub-clause hierarchy, schedule numbering, exhibit numbering, table numbering, skipped numbers, duplicate numbers, and numbering sequences. If the document has a table of contents, check that clause numbers, headings, and hierarchy are consistent with the table of contents. |
| Formatting | Check headings, list formatting, indentation, spacing, fonts, emphasis, table formatting, schedule formatting, and inconsistent styles that may affect readability or references. |

For each issue, include the best available clause, section, page, schedule, or paragraph reference in the **Location** column. If the location is unclear, describe where the issue appears as specifically as possible.

In the **Issue** column, explain the problem and why it matters. In the **Recommended Fix** column, provide a specific correction or drafting action. Where useful, include replacement wording, but keep it concise. Do not rewrite the whole document. If no material issues are found, provide a short table row stating that no material proofreading issues were identified and note any review limitations.

Before finalizing, double-check that definitions, cross-references, numbering, formatting, and internal inconsistencies have each been considered separately. If a table of contents is present, verify that the clause numbers and headings in the document match the table of contents. Keep the response focused on actionable corrections.
