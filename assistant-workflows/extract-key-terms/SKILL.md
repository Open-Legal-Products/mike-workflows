---
name: "extract-key-terms"
description: "Extract the key legal, commercial, and operational terms from the uploaded documents."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "Extract Key Terms"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "General Transactions"
  jurisdictions: "General"
---
# Extract Key Terms

## Instructions

Extract the key legal, commercial, and operational terms from the uploaded documents. Present the result as a concise Markdown table.

The table must have exactly these columns:

- Term
- Value
- Location
- Notes

Extract the terms that are most useful for legal review, including where available:

- Parties and roles
- Document date and effective date
- Term, expiry, renewal, and extension rights
- Scope of work, services, deliverables, or subject matter
- Fees, pricing, payment terms, interest, penalties, and currency
- Conditions precedent, approvals, consents, and notices
- Representations, warranties, covenants, and restrictions
- Confidentiality, IP ownership, data protection, and use rights
- Assignment, transfer, change of control, and subcontracting
- Termination rights, suspension rights, cure periods, and consequences
- Liability caps, indemnities, exclusions, insurance, and remedies
- Governing law, jurisdiction, dispute resolution, and service of process

Use the **Location** column for the best available clause, section, schedule, page, or paragraph reference. If a location is unclear, describe it as specifically as possible. Use the **Notes** column to explain ambiguity, missing information, conflicts between documents, or why a term may matter.

If a key term is not found, do not include a speculative value. Instead, include a row only where the absence itself is material, with "Not stated" in the **Value** column. Do not invent facts, citations, clauses, parties, dates, amounts, or obligations.
