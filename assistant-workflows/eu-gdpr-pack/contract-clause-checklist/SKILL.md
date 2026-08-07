---
name: "contract-clause-checklist"
description: "Walk a single contract against 41 clause categories from the CUAD taxonomy: first assess which categories this deal needs, then mark each applicable one present, absent, or risky, quoting the clause when present, so that a safeguard the deal needs does not slip through by omission. Extractive: findings come from the contract text, not paraphrase. Use before signing, in negotiation, or in due diligence of one agreement, when the question is what is missing from this contract and which clauses bite. Jurisdiction-neutral framing with common-law roots; the assessment and the recommendation stay with the lawyer."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Wieslaw Mazur / MateMatic Solutions"
  language: "English"
  mike-display-name: "Contract Clause Checklist"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "General Transactions"
  jurisdictions: "General"
---
# Contract Clause Checklist

The most expensive clauses are the ones that are not in the contract. Reviewing a contract is not only reading what is written - it is checking that no safeguard the deal needs is absent. This workflow walks the contract against a fixed list of 41 clause categories and, for each, says: present, absent, or present-but-risky, quoting the clause when present.

It is extractive - what it shows comes from the contract, not from paraphrase. It flags presence and risk; the assessment and the call stay with the lawyer.

One caution built into the method: CUAD is an extraction taxonomy, not a list of safeguards every agreement must contain. Several categories are deal-specific, and some are mutually exclusive pairs - uncapped liability versus a cap on liability, unlimited versus limited licence grants. Treating every absence as a red flag would bury the real gaps in false positives.

## The 41 categories (CUAD taxonomy)

Each category is assessed in two steps. First, applicability: does this deal need the clause at all, given the contract type, the parties, and the subject matter? Then, for applicable categories only: present / absent / risky, plus a quote when present. Mutually exclusive pairs count as one decision - record which side the contract takes, not the "absence" of the other side.

### Contract metadata
- Document name, Parties (verify authority to sign), Governing law.

### Group 1 - term and dates
- Agreement date, Effective date, Expiration date, Renewal term (auto-renew?), Notice period to terminate renewal.

### Group 2 - competition restrictions
- Non-compete, Exclusivity, No-solicit of customers, Competitive restriction exception (carve-outs).

### Group 3 - control and assignment
- Change of control (consent or termination on M&A?), Anti-assignment.

### Group 4 - licences
- License grant, Non-transferable license, Affiliate license (licensor), Affiliate license (licensee), Unlimited license, Irrevocable or perpetual license.

### Group 5 - post-term and audit
- Post-termination services, Audit rights.

### Group 6 - liability
- Uncapped liability, Cap on liability.

### Ungrouped
- Most favored nation, No-solicit of employees, Non-disparagement, Termination for convenience, ROFR/ROFO/ROFN, Revenue/profit sharing, Price restrictions, Minimum commitment, Volume restriction, IP ownership assignment, Joint IP ownership, Source code escrow, Covenant not to sue, Liquidated damages, Warranty duration, Insurance, Third-party beneficiary.

## Output format

Start with the red flags, then the full table:

- RED FLAGS: each category that is applicable and absent, with why this deal needs it, and each risky category with how it is one-sided. A category marked not applicable never becomes a red flag.
- 41-CATEGORY TABLE with columns: Category, Applicable (yes/no + why), Status, Note, Quote (if present).

## Limits

- This is a presence-and-risk checklist, not an interpretation of clause wording. Whether a clause is effective, and the recommendation, are the lawyer's.
- The taxonomy is common-law-oriented at source; for a specific jurisdiction, add local-law anchors.
- Descriptive references without a clause ("the parties intend to cooperate") have nothing to match - mark them as "no clause, manual check".

## Attribution

The 41-category clause taxonomy is based on CUAD (Contract Understanding Atticus Dataset), The Atticus Project, licensed CC BY 4.0 (https://www.atticusprojectai.org/cuad). Category descriptions and the risk framing are the author's own.
