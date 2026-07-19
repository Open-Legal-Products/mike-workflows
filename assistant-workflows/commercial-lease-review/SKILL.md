---
name: "commercial-lease-review"
description: "Review the uploaded commercial lease and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "Commercial Lease Review"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "Real Estate"
  jurisdictions: "General"
---
# Commercial Lease Review

## Instructions

Review the uploaded commercial lease and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client. If the user has not already identified which party they represent, ask them to clarify that party before producing the review.

Once the represented party is clear, provide exactly one Markdown result table. Use one row for each material issue found in the agreement, guided by the review checklist below, and add a final row called **Overall Risk Rating**. The result table must have exactly these columns:

- Issue
- Summary
- Recommended Change

Use these risk ratings inside the **Summary** column: Low means standard or minimal concern; Medium means a manageable negotiation concern; High means a material legal, commercial, operational, or enforceability concern requiring negotiation; Critical means a severe issue that may block signing unless resolved. Start each summary with the risk rating, e.g. "High — reinstatement obligation is uncapped".

The **Summary** column should include only the relevant points from the **General** checklist column and the party-specific checklist column for the represented party, together with clause references where available. Do not include issues that are adverse only to the other party unless they also create risk for the represented party. The **Recommended Change** column must be drafted from the represented party's perspective. Also flag general drafting errors that may affect the represented party, including inconsistent defined terms, inconsistent entity names, cross-reference errors, numbering issues, duplicated provisions, missing schedules, and internal inconsistencies. Keep the response concise and avoid long prose outside the table.

## Result Table Format

Use this result table structure. Cite the relevant clause, section, schedule, or page directly in the **Summary** and **Recommended Change** columns. The example rows are illustrative only; tailor the actual rows to the uploaded agreement and represented party.

| Issue | Summary | Recommended Change |
| --- | --- | --- |
| Break Rights | High — Clause [x] imposes vacant possession as a break condition with no cure period. The lessee-specific checklist point indicates the break is fragile and may be lost on a technicality. | For the lessee, remove vacant possession as a break condition or add a cure period and express the condition narrowly. |
| Drafting Consistency | Medium — Clauses [x] and [y] use inconsistent defined terms for the premises. The general drafting point indicates ambiguity that may affect the represented party's rights. | For the represented party, align defined terms, premises description, and cross-references before signing. |

## Review Checklist

Use this checklist as guidance for what to review and flag. It is not the result-table template and should not be reproduced verbatim. For each checklist issue, consider both the **General** column and the party-specific column for the represented party (Lessor or Lessee).

| Issue | General | Lessor | Lessee |
| --- | --- | --- | --- |
| Parties and Premises | Identify landlord, tenant, guarantor, property, premises, title references, and included or excluded areas. Flag incorrect entities, missing plans, or premises description inconsistent with title. | | |
| Term | State commencement, expiry, rent commencement, and any conditions precedent. | Flag renewal rights or holding-over provisions that limit the landlord's ability to recover the premises. | Flag uncertain commencement mechanics, no renewal clarity, or landlord-only discretion over start conditions. |
| Rent and Payments | Confirm rent quantum, payment dates, and deposit mechanics. | Flag unclear payment mechanics, weak late-payment provisions, or rent-free periods exceeding what was agreed. | Flag unclear payment obligations, high default interest, or missing rent-free mechanics. |
| Rent Review | Identify review dates, mechanism, assumptions, disregards, and dispute process. | Flag review mechanics too favorable to the tenant, downward review provisions, or no upward adjustment. | Flag upward-only review, no cap, aggressive assumptions, or tenant-unfriendly dispute process. |
| Service Charge and Operating Costs | Identify tenant contribution scope, cap mechanics, audit rights, and reconciliation process. | Flag cost exclusions too broad, caps too low, or audit rights creating undue operational burden. | Flag broad pass-throughs, no cap, capital expenditure exposure, or weak audit rights. |
| Use | State permitted use, prohibited uses, trading obligations, and change-of-use restrictions. | Flag permitted use too broad or absence of continuous trading obligation. | Flag narrow use restriction, continuous trading obligations, or restrictions inconsistent with operations. |
| Repairs and Maintenance | Identify landlord and tenant repair obligations, condition standard, and schedule of condition. | Flag limited tenant repairing obligations, repair gaps, or yielding-up conditions below acceptable standard. | Flag full repairing obligation extending to pre-existing defects or structural issues outside tenant control. |
| Alterations and Fit-Out | Identify consent requirements and reinstatement obligations. | Flag broad alteration rights without landlord consent or no reinstatement obligation. | Flag absolute consent rights, broad reinstatement obligations, or unclear fit-out approval timing. |
| Assignment, Underletting, and Sharing Occupation | Identify transfer restrictions, consent tests, and group sharing rights. | Flag broad permitted transfer rights allowing assignment to unsuitable tenants without approval. | Flag absolute assignment bans, excessive consent conditions, or no group sharing rights. |
| Insurance and Damage | Identify who insures, insured risks, rent suspension, and termination rights on damage. | Flag tenant insurance obligations too narrow or absence of rent suspension protection. | Flag no rent suspension on damage, uninsured risk exposure, or no termination right after prolonged damage. |
| Break Rights | Identify break dates, notice periods, and conditions. | Flag broadly exercisable break conditions allowing tenant exit without adequate penalty. | Flag fragile break conditions, strict vacant possession tests, or excessive preconditions. |
| Default and Remedies | Identify default events, cure periods, and enforcement rights. | Flag long cure periods, high default thresholds, or limited remedies that delay enforcement. | Flag short cure periods, broad default triggers, or landlord self-help without adequate notice. |
| Compliance Obligations | Identify which party bears responsibility for regulatory compliance. | Flag compliance gaps exposing the landlord to regulatory liability. | Flag tenant responsibility for landlord works, historic contamination, or compliance beyond the demised premises. |
| Security Package | Identify security type, quantum, and release conditions. | Flag security inadequate for the tenant's covenant strength or release mechanics too easy to trigger. | Flag excessive security requirements, no step-down on release, or unclear deposit return mechanics. |
| Rights Reserved and Easements | Identify reserved landlord rights, access arrangements, and tenant rights over common parts. | Flag insufficient reserved rights limiting the landlord's ability to manage the building. | Flag broad landlord entry or disruption rights, or missing rights needed for the tenant's permitted use. |
| End of Term | Identify yielding-up condition, reinstatement obligations, and dilapidations process. | Flag inadequate reinstatement obligations, unclear yielding-up conditions, or weak dilapidations recovery. | Flag overly broad reinstatement obligations or handback conditions requiring a better standard than at commencement. |
| Governing Law and Dispute Resolution | State governing law, court forum, expert determination process, and mandatory dispute procedures. Flag ambiguous forum, missing expert determination terms, or inadequate dispute mechanics. | | |

Deliver the review inline in your chat response. Do not generate a downloadable Word document unless the user explicitly asks for one.
