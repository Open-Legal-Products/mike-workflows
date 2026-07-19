---
name: "shareholder-agreement-review"
description: "Review the uploaded shareholder agreement and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "Shareholder Agreement Review"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "Corporate"
  jurisdictions: "General"
---
# Shareholder Agreement Review

## Instructions

Review the uploaded shareholder agreement and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client. If the user has not already identified which party they represent, ask them to clarify that party before producing the review.

Once the represented party is clear, provide exactly one Markdown result table. Use one row for each material issue found in the agreement, guided by the review checklist below, and add a final row called **Overall Risk Rating**. The result table must have exactly these columns:

- Issue
- Summary
- Recommended Change

Use these risk ratings inside the **Summary** column: Low means standard or minimal concern; Medium means a manageable negotiation concern; High means a material legal, commercial, operational, or enforceability concern requiring negotiation; Critical means a severe issue that may block signing unless resolved. Start each summary with the risk rating, e.g. "High — drag threshold is too low".

The **Summary** column should include only the relevant points from the **General** checklist column and the party-specific checklist column for the represented party, together with clause references where available. Do not include issues that are adverse only to the other party unless they also create risk for the represented party. The **Recommended Change** column must be drafted from the represented party's perspective. Also flag general drafting errors that may affect the represented party, including inconsistent defined terms, inconsistent entity names, cross-reference errors, numbering issues, duplicated provisions, missing schedules, and internal inconsistencies. Keep the response concise and avoid long prose outside the table.

## Result Table Format

Use this result table structure. Cite the relevant clause, section, schedule, or page directly in the **Summary** and **Recommended Change** columns. The example rows are illustrative only; tailor the actual rows to the uploaded agreement and represented party.

| Issue | Summary | Recommended Change |
| --- | --- | --- |
| Drag-Along Rights | High — Clause [x] sets the drag threshold at [x]% and does not include a minimum price protection. The minority-specific checklist point indicates the minority can be forced to sell at an unfavorable price. | For the minority, raise the drag threshold, add a minimum price equal to fair market value, and limit warranties to proceeds received. |
| Drafting Consistency | Medium — Clauses [x] and [y] use inconsistent defined terms for the share classes. The general drafting point indicates ambiguity that may affect the represented party's rights. | For the represented party, align defined terms, share class definitions, and cross-references before signing. |

## Review Checklist

Use this checklist as guidance for what to review and flag. It is not the result-table template and should not be reproduced verbatim. For each checklist issue, consider both the **General** column and the party-specific column for the represented party (Majority or Minority).

| Issue | General | Majority | Minority |
| --- | --- | --- | --- |
| Parties and Shareholdings | Identify each shareholder, role, share class, percentage holding, and fully diluted position. Flag inconsistent cap table information, missing parties, or unclear beneficial ownership. | | |
| Share Classes and Rights | Summarize voting rights, dividend rights, liquidation preferences, conversion rights, redemption rights, and class consents. | Flag class consents or voting requirements that effectively give minority approval rights over ordinary decisions. | Flag hidden preference rights, disproportionate majority voting rights, or unfavorable class economics. |
| Board Composition and Governance | Identify board size, appointment rights, observer rights, quorum, chair, and casting vote. | Flag quorum or deadlock provisions giving minority an effective veto over governance. | Flag entrenched majority appointment rights, casting vote held by a majority nominee, or no observer rights for minority. |
| Reserved Matters | List matters requiring special majority, unanimity, investor consent, or board consent. | Flag reserved matters requiring minority consent that constrain ordinary business decisions. | Flag absence of meaningful minority veto rights or low-dollar thresholds allowing majority to structure around them. |
| Pre-emption on New Shares | Summarize pre-emption rights, offer process, timing, exclusions, and carve-outs. | Flag mechanics slowing fundraising or requiring minority consent to issue new shares. | Flag broad carve-outs, short exercise periods, or mechanics permitting dilution without proper notice. |
| Transfer Restrictions | Summarize lock-ups, prohibited transfers, permitted transfers, and consent requirements. | Flag restrictions preventing majority exit or group reorganisation without minority consent. | Flag absence of lock-up on majority transfers or mechanics allowing majority to exit leaving minority trapped. |
| Right of First Refusal / Pre-emption on Transfer | Identify trigger, process, pricing, matching rights, and exceptions. | Flag long ROFR processes or pricing mechanics delaying majority exit. | Flag unclear matching rights, long processes excluding minority participation, or exceptions removing minority protections. |
| Drag-Along Rights | Identify drag threshold, sale conditions, minority protections, and power of attorney. | Flag high drag threshold or conditions preventing majority from executing a sale. | Flag low drag threshold, no minimum price protection, forced warranties beyond proceeds received, or broad power of attorney. |
| Tag-Along Rights | Identify triggering transfers, eligible holders, and sale terms. | Flag broad tag triggers complicating majority exit. | Flag missing or narrow tag rights, or mechanics allowing majority to exclude minority from exit proceeds. |
| Anti-Dilution Protections | Identify anti-dilution mechanics, carve-outs, and adjustment triggers. | Flag mechanics punishing founders or majority holders on down-rounds. | Flag absence of anti-dilution protection, full ratchet terms, or unclear carve-outs from adjustment. |
| Dividend Policy | Summarize dividend rights, preferential dividends, restrictions, and discretion. | Flag mandatory dividend obligations impairing business cash flow or restricting majority discretion. | Flag unclear preferential dividend rights or majority discretion over dividends without minority consent. |
| Exit and Liquidity | Identify IPO, trade sale, redemption, put/call rights, timelines, and liquidation preferences. | Flag forced exit timelines or investor put rights constraining majority exit strategy. | Flag unclear waterfall on exit, exit rights not applying equally, or no minority participation in liquidity events. |
| Deadlock | Summarize deadlock definition, escalation, expert determination, shoot-out, and liquidation mechanics. | Flag deadlock provisions giving minority disproportionate leverage or effective veto. | Flag shoot-out rights triggered at low thresholds or mechanics structurally favoring majority. |
| Non-Compete and Non-Solicitation | Identify who is bound, restricted activities, geography, duration, and carve-outs. | Flag restraints binding the majority entity or overly broad scope applied to the majority group. | Flag broad non-competes restricting the minority's ability to operate independently after exit. |
| Information Rights | Identify reporting, inspection, management accounts, and confidentiality obligations. | Flag extensive information rights giving minority commercially sensitive operational visibility. | Flag absence of reporting or inspection rights, or inadequate confidentiality obligations on recipients. |
| Related Party Transactions | Identify approval requirements, disclosure duties, and arm's-length standards. | Flag overly strict conflict controls restricting legitimate majority-group transactions. | Flag weak conflict controls, broad permitted related-party dealings, or no arm's-length enforcement. |
| Governing Law and Dispute Resolution | State governing law, forum, arbitration, escalation, and interim relief rights. Flag unclear or ambiguous forum or dispute mechanics. | | |

Deliver the review inline in your chat response. Do not generate a downloadable Word document unless the user explicitly asks for one.
