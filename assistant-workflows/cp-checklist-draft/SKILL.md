---
name: "cp-checklist-draft"
description: "Review the uploaded credit agreement or financing document and generate a comprehensive Conditions Precedent (CP) checklist."
license: "MIT"
metadata:
  version: "2.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "CP Checklist Draft"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "General Transactions"
  jurisdictions: "General"
---
# CP Checklist Draft

Review the uploaded credit agreement or financing document and generate a comprehensive Conditions Precedent (CP) checklist.

Produce the checklist as an exportable Word (`.docx`) document in landscape
orientation. Return the completed document as a file rather than displaying the
checklist inline.

Structure the document as follows:
- For each category of conditions (e.g. Corporate, Financial, Legal, Security), add a section with a heading
- Under each category heading, include a table with exactly these four columns in this order:
  1. Index — sequential number within the category (1, 2, 3…)
  2. Clause Number — the clause or schedule reference from the agreement
  3. Clause — a concise description of the condition precedent
  4. Status — leave blank (empty string) for the user to fill in

Place each category's rows in a table under the relevant category heading.

## Result Table Format

The document contains one section per category, each with a table in this format:

### Corporate

| Index | Clause Number | Clause | Status |
| --- | --- | --- | --- |
| 1 | Cl. 4.1(a)(i) | Certificate of incorporation and constitutional documents of the borrower | |
| 2 | Cl. 4.1(a)(ii) | Board resolution authorising execution of the finance documents and approving the terms of the transaction | |
| 3 | Cl. 4.1(a)(iii) | Specimen signatures of all authorised signatories | |

### Legal

| Index | Clause Number | Clause | Status |
| --- | --- | --- | --- |
| 1 | Cl. 4.1(c)(i) | Legal opinion from counsel to the borrower in form and substance satisfactory to the agent | |
| 2 | Cl. 4.1(c)(ii) | Legal opinion from counsel to the arrangers as to the laws of the relevant jurisdiction | |

Before finalizing, double-check that every table is formatted correctly: each table must have exactly the four columns above in the same order, headers must match exactly (Index, Clause Number, Clause, Status), every row must have the same number of cells as the headers, the Index column must be sequential starting from 1 within each category, and no cells should contain stray markdown, newlines, or placeholder text (use an empty string for Status).
