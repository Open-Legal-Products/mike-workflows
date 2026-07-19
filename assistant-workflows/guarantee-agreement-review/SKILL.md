---
name: "guarantee-agreement-review"
description: "Review an uploaded guarantee, guaranty, or guarantee-and-indemnity agreement from the perspective of the party represented by the user."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "Guarantee Agreement Review"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "Finance"
  jurisdictions: "General"
---
# Guarantee Agreement Review

## Instructions

Review the uploaded guarantee, guaranty, or guarantee-and-indemnity agreement and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client. If the user has not already identified which party they represent, ask them to clarify that party before producing the review.

Once the represented party is clear, provide exactly one Markdown result table. Use one row for each material issue found in the agreement, guided by the review checklist below, and add a final row called **Overall Risk Rating**. The result table must have exactly these columns:

- Issue
- Summary
- Recommended Change

Use these risk ratings inside the **Summary** column: Low means standard or minimal concern; Medium means a manageable negotiation concern; High means a material legal, commercial, operational, or enforceability concern requiring negotiation; Critical means a severe issue that may block signing unless resolved. Start each summary with the risk rating, e.g. "High - guarantee is uncapped".

The **Summary** column should include only the relevant points from the **General** checklist column and the party-specific checklist column for the represented party, together with clause references where available. Do not include issues that are adverse only to another party unless they also create risk for the represented party. The **Recommended Change** column must be drafted from the represented party's perspective. Also flag general drafting errors that may affect the represented party, including inconsistent defined terms, inconsistent entity names, cross-reference errors, numbering issues, duplicated provisions, missing schedules, and internal inconsistencies. Keep the response concise and avoid long prose outside the table.

## Result Table Format

Use this result table structure. Cite the relevant clause, section, schedule, or page directly in the **Summary** and **Recommended Change** columns. The example rows are illustrative only; tailor the actual rows to the uploaded agreement and represented party.

| Issue | Summary | Recommended Change |
| --- | --- | --- |
| Cap and Limits | High - Clause [x] does not include a monetary cap or time limit. The general exposure point and the guarantor-specific checklist point indicate uncapped liability risk for the guarantor. | For the guarantor, add a monetary cap, currency limit, time limit, and exclusions for obligations outside the agreed transaction. |
| Drafting Consistency | Medium - Clauses [x] and [y] use inconsistent defined terms or party names. The general drafting point indicates ambiguity that may affect the represented party's rights or obligations. | For the represented party, align the defined terms, party names, numbering, and cross-references before signing. |

## Review Checklist

Use this checklist as guidance for what to review and flag. It is not the result-table template and should not be reproduced verbatim. For each checklist issue, consider both the **General** column and the party-specific column for the represented party (Guarantor or Guarantee Holder).

| Issue | General | Guarantor | Guarantee Holder |
| --- | --- | --- | --- |
| Parties | Identify all parties with full legal names and roles, including guarantor, principal obligor, agent, and security trustee. Flag incorrect entities, missing capacity details, or unclear party or agent structure. | | |
| Guaranteed Obligations | Summarize payment, performance, indemnity, costs, interest, fees, future advances, and all-monies coverage. | Flag broad all-monies coverage, obligations beyond the intended transaction, or future advances not agreed at outset. | Flag gaps in guaranteed obligations or exclusions of fees, interest, or enforcement costs. |
| Nature of Liability | State whether liability is primary, secondary, joint and several, continuing, independent, on-demand, or principal debtor liability. | Flag primary, on-demand, or principal debtor liability where only secondary guarantee risk was intended. | Flag secondary-only liability or absence of principal debtor language that weakens enforcement. |
| Guarantee vs Indemnity | Identify any separate indemnity or principal debtor language and explain practical effect. | Flag separate indemnity language that expands exposure beyond the underlying obligation or bypasses guarantor defences. | Flag absence of indemnity or principal debtor language that could allow defences to defeat enforcement. |
| Cap and Limits | State monetary cap, currency, interest cap, time limit, excluded obligations, and other limits. | Flag uncapped exposure, unclear currency, or no temporal limit on guaranteed obligations. | Flag caps too low to cover the full facility, or caps that exclude interest, fees, and enforcement costs. |
| Continuing Security | Summarize future, contingent, amended, refinanced, reinstated, or continuing obligations. | Flag coverage of unknown future obligations or amendments to the underlying facility without guarantor consent. | Flag gaps in continuing security coverage or restrictions on amendments that limit lender flexibility. |
| Demand Mechanics | Explain demand triggers, notice, payment timing, evidence, and conclusiveness. | Flag immediate payment without adequate evidence, conclusive certificates, or no notice period before demand. | Flag demand mechanics too cumbersome or conditions that allow the guarantor to delay payment. |
| Defences and Waivers | Identify waivers of suretyship defences, diligence, presentment, set-off, marshalling, subrogation, contribution, and notice. | Flag broad waivers of fundamental defences, excessive restriction of set-off, or waiver of subrogation rights. | Flag incomplete waiver of suretyship defences that could allow the guarantor to avoid payment. |
| Variations and Releases | Summarize effect of amendments, waivers, releases, insolvency events, or underlying document changes. | Flag guarantee surviving material changes to the underlying facility without guarantor consent. | Flag restrictions on amendments or waivers requiring guarantor consent that limit lender flexibility. |
| Reinstatement | Identify clawback, preference, invalid payment, or reinstatement provisions. | Flag indefinite reinstatement obligations or reinstatement beyond reasonable insolvency clawback risk. | Flag absence of reinstatement provisions that could leave the guarantee holder exposed after a clawback. |
| Subordination | Summarize restrictions on guarantor claims, subrogation, contribution, or proof in insolvency. | Flag indefinite blockage of guarantor recovery or subrogation rights after the guarantee holder is paid in full. | Flag absence of subordination provisions that could allow the guarantor to compete with the guarantee holder in insolvency. |
| Representations and Covenants | Identify capacity, authority, solvency, consents, sanctions, and compliance covenants. | Flag repeating representations, broad compliance obligations, or solvency statements that may be difficult to give. | Flag weak representations or covenants that do not adequately confirm guarantor capacity and authority. |
| Termination and Release | State how the guarantee may be terminated, released, discharged, or reduced. | Flag no release mechanism after repayment or facility termination, or unclear discharge conditions. | Flag release mechanics too easy to trigger or that do not require full repayment and discharge. |
| Costs, Expenses, and Taxes | Summarize reimbursement, gross-up, tax indemnities, and enforcement costs. | Flag unlimited costs, gross-up for avoidable taxes, or broad indemnities beyond reasonable enforcement costs. | Flag cost recovery gaps that leave enforcement costs unrecoverable from the guarantor. |
| Assignment and Transfer | Identify whether the guarantee holder may assign or transfer benefit and whether guarantor consent is required. | Flag free transfer of benefit to unknown creditors, distressed debt purchasers, or competitors without consent. | Flag consent mechanics that give the guarantor excessive control over assignment of the guarantee benefit. |
| Governing Law and Dispute Resolution | State governing law, jurisdiction, arbitration, service of process, and immunity waiver provisions. Flag unfamiliar law, inconvenient forum, broad immunity waiver, unclear service mechanics, or inadequate interim relief provisions. | | |

Deliver the review inline in your chat response. Do not generate a downloadable Word document unless the user explicitly asks for one.
