---
name: "compare-documents"
description: "Compare the uploaded documents in a structured table, highlighting key similarities, differences, risks, and follow-up points."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "Compare Documents"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "General Transactions"
  jurisdictions: "General"
---
# Compare Documents

## Instructions

Compare the uploaded documents for a legal or business reviewer. Focus on the provisions, terms, risks, and commercial points that differ across the documents. The comparison must work for any number of uploaded documents.

Produce the comparison as a Markdown table. The table must have exactly these columns:

- Topic
- One column for each uploaded document, using the document name or a short readable document label as the column heading
- Difference

For example, if three documents are uploaded, the table should use this shape:

| Topic | Document A | Document B | Document C | Difference |
| --- | --- | --- | --- | --- |

Compare the documents across the most relevant topics, including where available:

- Parties and roles
- Document date and effective date
- Term, expiry, renewal, and extension rights
- Scope of work, services, deliverables, or subject matter
- Fees, pricing, payment terms, penalties, and currency
- Conditions precedent, approvals, consents, and notices
- Representations, warranties, covenants, and restrictions
- Confidentiality, IP ownership, data protection, and use rights
- Assignment, transfer, change of control, and subcontracting
- Termination rights, suspension rights, cure periods, and consequences
- Liability caps, indemnities, exclusions, insurance, and remedies
- Governing law, jurisdiction, dispute resolution, and service of process

Use concise entries in the document columns. Under each document column, state the relevant term and include the best available location with citations, such as clause, section, schedule, page, paragraph, or heading. If citations are available, include them inline with the location. If a location is unclear, describe it as specifically as possible.

In the **Difference** column, explain what changed or diverges, including any negotiation, legal, operational, or commercial significance where useful.

After the table, include a short **Key Takeaways** section with no more than five bullets summarising the most important differences and follow-up actions.

Do not invent facts, clauses, parties, dates, amounts, or obligations. If a topic is not addressed in a document, write "Not stated" for that document. If the uploaded documents are not comparable, explain why and provide the closest useful comparison.
