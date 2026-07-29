---
name: "issues-list-draft"
description: "Review the uploaded agreement and draft a comprehensive issues list from the perspective of the party represented by the user/client."
license: "MIT"
metadata:
  version: "2.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "Issues List Draft"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "General Transactions"
  jurisdictions: "General"
---
# Issues List Draft

## Instructions

Review the uploaded agreement and draft a comprehensive issues list from the perspective of the party represented by the user/client. If the user has not already identified which party they represent, ask them to clarify that party before drafting the issues list.

An issues list identifies open, unresolved, or contentious points in the current draft that require negotiation or resolution before signing. Focus on points that are material to the represented party's commercial and legal position.

Once the represented party is clear, produce the issues list as an exportable
Word (`.docx`) document in landscape orientation. Return the completed document
as a file rather than displaying the issues list inline.

The Word document must contain exactly one result table. List each open issue in order from highest to lowest priority and add a final row called **Overall Negotiation Position**. The result table must have exactly these columns:

- Issue
- Current Position
- Proposed Change

Use these priority ratings at the start of the **Current Position** column: Critical means a blocking issue that must be resolved before signing; High means a material point requiring negotiation; Medium means a negotiation concern but manageable; Low means a minor point for consideration only. Include relevant clause references in the **Current Position** column. The **Proposed Change** column must state the specific amendment or position the represented party should seek, drafted from that party's perspective. Keep the response concise and focused on actionable negotiation points.

## Result Table Format

The Word document must use this result table structure. The example rows are illustrative only; tailor the actual rows to the uploaded agreement and represented party.

| Issue | Current Position | Proposed Change |
| --- | --- | --- |
| Liability Cap | High — Clause [x] contains no monetary cap on the represented party's total liability under the agreement. | Add a liability cap equal to [amount] or a multiple of fees paid, with carve-outs limited to fraud and wilful misconduct. |
| Governing Law | Medium — Clause [x] specifies [jurisdiction] law, which is inconvenient for the represented party's operations and legal advisers. | Change governing law to [preferred jurisdiction] and amend the dispute resolution clause accordingly. |

Place the issues list rows in the result table rather than presenting them as
prose.

Before finalizing, double-check that the table is formatted correctly: it must have exactly the three columns above in the same order, headers must match exactly (Issue, Current Position, Proposed Change), every row must have the same number of cells as the headers, issues must be ordered from highest to lowest priority, and no cells should contain stray markdown, newlines, or placeholder text unless the source document requires a placeholder.
