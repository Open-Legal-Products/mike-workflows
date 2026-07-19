---
name: "credit-agreement-review"
description: "Review the uploaded credit agreement and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "Credit Agreement Review"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "Finance"
  jurisdictions: "General"
---
# Credit Agreement Review

## Instructions

Review the uploaded credit agreement and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client. If the user has not already identified which party they represent, ask them to clarify that party before producing the review.

Once the represented party is clear, provide exactly one Markdown result table. Use one row for each material issue found in the agreement, guided by the review checklist below, and add a final row called **Overall Risk Rating**. The result table must have exactly these columns:

- Issue
- Summary
- Recommended Change

Use these risk ratings inside the **Summary** column: Low means standard or minimal concern; Medium means a manageable negotiation concern; High means a material legal, commercial, operational, or enforceability concern requiring negotiation; Critical means a severe issue that may block signing unless resolved. Start each summary with the risk rating, e.g. "High — covenant headroom is tight".

The **Summary** column should include only the relevant points from the **General** checklist column and the party-specific checklist column for the represented party, together with clause or schedule references where available. Do not include issues that are adverse only to the other party unless they also create risk for the represented party. The **Recommended Change** column must be drafted from the represented party's perspective. Also flag general drafting errors that may affect the represented party, including inconsistent defined terms, inconsistent entity names, cross-reference errors, numbering issues, duplicated provisions, missing schedules, and internal inconsistencies. Keep the response concise and avoid long prose outside the table.

## Result Table Format

Use this result table structure. Cite the relevant clause, section, schedule, or page directly in the **Summary** and **Recommended Change** columns. The example rows are illustrative only; tailor the actual rows to the uploaded agreement and represented party.

| Issue | Summary | Recommended Change |
| --- | --- | --- |
| Financial Covenants | High — Clause [x] sets the leverage covenant at [x]x with quarterly testing and no equity cure right. The borrower-specific checklist point indicates limited headroom and no remedy for a technical breach. | For the borrower, widen the covenant threshold, add an equity cure right, and reduce testing frequency to semi-annual. |
| Drafting Consistency | Medium — Clauses [x] and [y] use inconsistent defined terms for the facility amount. The general drafting point indicates ambiguity that may affect the represented party's rights. | For the represented party, align defined terms, amounts, and cross-references before signing. |

## Review Checklist

Use this checklist as guidance for what to review and flag. It is not the result-table template and should not be reproduced verbatim. For each checklist issue, consider both the **General** column and the party-specific column for the represented party (Borrower or Lender).

| Issue | General | Borrower | Lender |
| --- | --- | --- | --- |
| Parties | Identify all lenders, borrowers, guarantors, agents, and other finance parties with full legal names, roles, and jurisdictions. Flag missing or incorrect entities, unclear agent roles, missing authority confirmations, or transfer mechanics that could result in unknown lenders. | | |
| Guarantors | Identify guarantors, guarantee scope, limits, and coverage requirements. | Flag uncapped guarantees, missing limits, or upstream guarantee concerns exposing the borrower group. | Flag weak guarantor coverage, missing entities, or guarantees not covering the full facility. |
| Other Parties | Identify facility agent, security agent, arrangers, issuing banks, and other material parties. | Flag unclear agent roles or mechanics creating additional obligations on the borrower. | Flag inconsistent secured party mechanics or missing parties affecting security validity. |
| Date of Agreement | State signing date, effective date, and conditions to effectiveness. Flag inconsistent or unclear dates or effectiveness conditions. | | |
| Facilities | List each facility, type, tranche, availability, and key structural features. | Flag excessive lender discretion, unclear facility purpose, or mismatched terms restricting drawdown. | Flag unclear facility structure or purpose creating enforcement ambiguity. |
| Amount | State total commitments, currencies, tranche amounts, and accordion or incremental facilities. | Flag unclear currency exposure, uncapped accordion provisions without borrower consent, or inconsistent commitment figures. | Flag uncapped increase mechanics or dilutive accordion provisions not agreed at signing. |
| Purpose | Summarize permitted use of proceeds and restrictions. | Flag vague purpose wording restricting flexibility or creating sanctions risk. | Flag broad purpose language permitting restricted payment leakage or unapproved use of proceeds. |
| Interest | Identify reference rate, margin, floors, fallback rates, interest periods, and default interest. | Flag high margins, aggressive floors, benchmark fallback gaps, or high default interest. | Flag unclear fallback rate mechanics or interest calculation ambiguities. |
| Commitment Fee | State commitment, utilisation, ticking, arrangement, agency, and other fees. | Flag hidden fees, fees payable after cancellation, or unclear calculation basis. | Flag missing fee provisions or fee timing delaying recovery. |
| Repayment Schedule | Summarize amortisation, scheduled repayments, bullet payments, and cash sweep. | Flag aggressive amortisation, unclear prepayment application, or cash sweep uncertainty. | Flag bullet repayments without adequate covenant or security protection. |
| Maturity | State final maturity date and any extension options. | Flag short maturity, lender-only extension discretion, or mismatch with the business plan. | Flag unclear extension conditions or borrower-controlled extension mechanics. |
| Security | Identify security package, assets, entities, perfection steps, and post-closing obligations. | Flag all-asset security beyond deal scope, onerous post-closing steps, or missing release mechanics on disposal. | Flag gaps in the security package, missing perfection steps, or inadequate post-closing obligations. |
| Guarantees | Summarize guarantee obligations, guarantors, limitations, and release triggers. | Flag broad all-monies language, unlimited guarantees, or no release mechanics after repayment or disposal. | Flag guarantee gaps, weak limitations, or no coverage test requirements. |
| Financial Covenants | Identify covenant metrics, thresholds, testing frequency, cure rights, and reporting. | Flag tight headroom, frequent testing, no equity cure, or ambiguous EBITDA adjustments. | Flag loose covenant thresholds or wide EBITDA adjustments obscuring true financial performance. |
| Events of Default | Summarize default triggers, grace periods, materiality thresholds, cross-default, and MAE. | Flag low materiality thresholds, no cure periods, broad cross-default, or subjective MAE defaults. | Flag weak default triggers, long cure periods, or materiality thresholds delaying enforcement. |
| Assignment | Summarize lender transfer rights, borrower consent mechanics, and disqualified institutions. | Flag free transfers to competitors, distressed investors, or lenders on a borrower blacklist. | Flag consent mechanics giving the borrower excessive veto over lender transfers. |
| Change of Control | Identify triggers and resulting prepayment, cancellation, or default consequences. | Flag broad triggers, no cure period, or definitions catching ordinary-course ownership changes. | Flag narrow change of control definitions missing material ownership shifts. |
| Prepayment Fee | Identify make-whole, soft-call, premium periods, and exceptions. | Flag excessive fees, long premium periods, or unclear exceptions for mandatory prepayments. | Flag exceptions allowing free prepayment during premium periods. |
| Governing Law and Dispute Resolution | State governing law, jurisdiction, forum, and service of process. Flag unclear or ambiguous governing law, jurisdiction, or service mechanics. | | |

Deliver the review inline in your chat response. Do not generate a downloadable Word document unless the user explicitly asks for one.
