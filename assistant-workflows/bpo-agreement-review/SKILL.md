---
name: "bpo-agreement-review"
description: "Review an uploaded Business Process Outsourcing (BPO), IS outsourcing, or IT outsourcing agreement and produce a comprehensive table-based legal review from the perspective of the Customer or Supplier represented by the user."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Polina Chtchelok"
  language: "English"
  mike-display-name: "BPO Agreement Review"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "Commercial"
  jurisdictions: "General"
---
# BPO Agreement Review

## Instructions

Review the uploaded Business Process Outsourcing (BPO), IS outsourcing, or IT outsourcing agreement from the perspective of the party represented by the user. If the user has not already identified the represented party, ask them to clarify whether they represent:

- the **Customer**, meaning the entity receiving the outsourced services, sometimes together with local Service Recipients or Affiliates; or
- the **Supplier**, meaning the entity providing the outsourced services, potentially through Affiliates and Subcontractors.

Do not produce the review until the represented party is clear.

Once the represented party is clear, provide exactly one Markdown result table. Use one row for each material issue found in the agreement, guided by the review checklist below, and add a final row called **Overall Risk Rating**. The result table must have exactly these columns:

- Issue
- Summary
- Recommended Change

Use these risk ratings inside the **Summary** column:

- **Low** — standard or minimal concern.
- **Medium** — a manageable negotiation concern.
- **High** — a material legal, commercial, operational, or enforceability concern requiring negotiation.
- **Critical** — a severe issue that may block signing unless resolved.

Start each summary with the risk rating, for example: "High — Service Credit cap is too low to create a meaningful remediation incentive."

Include only points relevant to the represented party, drawing from the **General** checklist column and that party's checklist column. Do not include issues adverse only to the other party unless they also create risk for the represented party. Cite the relevant clause, schedule, or page where available. Draft every recommendation from the represented party's perspective.

Also flag drafting errors that may affect the represented party, including inconsistent defined terms or entity names, unresolved placeholders, cross-reference errors, numbering issues, duplicated provisions, missing or unattached Schedules, inconsistent timelines or thresholds, and internal inconsistencies. Keep the response concise and avoid prose outside the table.

## Result Table Format

Use this structure. The example rows are illustrative only; tailor the actual rows to the uploaded agreement and represented party.

| Issue | Summary | Recommended Change |
| --- | --- | --- |
| Service Credits | High — Clause [x] caps Service Credits at [x]% of monthly Charges and states that Service Credits are the sole price adjustment rather than liquidated damages. The cap may be too low to incentivize remediation. | For the Customer, raise the aggregate cap, add escalating credits for repeat breaches, and confirm that Service Credits do not limit termination or damages rights. |
| Drafting Consistency | Medium — Clauses [x] and [y] leave the governance committee name as an unresolved placeholder ("[Name of the relevant committee]"), creating ambiguity over which body approves escalations and Correction Plans. | For the represented party, name the governance body and confirm its composition, escalation authority, and meeting cadence before signing. |

## Review Checklist

Use this checklist as guidance. Do not reproduce it verbatim in the result. For each issue, consider the **General** column together with the column for the represented party.

| Issue | General | Customer | Supplier |
| --- | --- | --- | --- |
| Definitions and Interpretation | Review defined terms such as Affiliate, Control, Applicable Laws, Change, Charges, Service Levels, and Service Recipients for consistency, circularity, unresolved brackets, and conflicts between body definitions and a glossary Schedule. | Flag definitions that narrow Supplier responsibility, such as narrow definitions of Services or Best Industry Practice, or create ambiguity over qualifying Service Recipients and Affiliates. | Flag broad or open-ended definitions, such as Services including anything reasonably necessary or incidental, that expand scope without a corresponding Charge adjustment. |
| Purpose and Scope of Services | Identify how Services are structured into Service Towers or Schedules, whether the arrangement is exclusive, and how new services or towers may be added. | Flag non-exclusivity language allowing Supplier to serve competitors or weak obligations to tender for new services in good faith. | Flag open-ended obligations to tender for undefined future services without a right to decline or reprice. |
| Outsourcing Objectives | Summarize objectives such as flexibility, scalability, continuous improvement, end-to-end responsibility, and governance. Flag objectives expressed as binding obligations rather than aspirations. | Flag vague objectives without measurable KPIs that weaken enforcement of continuous-improvement commitments. | Flag broad end-to-end responsibility language that could expand liability beyond the agreed Service Towers. |
| Due Diligence | Identify "as is" disclaimers for Customer-provided systems or data and any deadline for Supplier to raise discrepancies. | Flag due-diligence disclaimers that shift all risk of inaccurate Customer information to Supplier without a fair notice period. | Flag short, ambiguous, or internally inconsistent notice deadlines and deemed acceptance if concerns are not raised in time. |
| Term and Extension | Identify the Initial Term, extension periods, applicable notice periods, and any automatic renewal. | Flag a long Initial Term without adequate termination-for-convenience rights or a short extension-notice window. | Flag short extension notice creating planning or staffing risk and any missing rate-adjustment mechanism for extensions. |
| Transition Services | Summarize transition scope, acceptance, exit criteria, and Service Levels during transition. | Flag vague acceptance criteria or lack of Customer sign-off before go-live. | Flag Service Levels or penalties applying before operations have stabilized. |
| Transformation Services | Summarize modernization or optimization scope and any duty to propose improvement initiatives. | Flag obligations without concrete deliverables, milestones, or committed savings. | Flag open-ended duties to recommend initiatives without cost or resource caps. |
| Service Recipients and Local Agreements | Identify how Affiliates become Service Recipients, including Local Services Agreements, and how Charges and liability flow to each Recipient. | Flag cumbersome Local Services Agreement execution delaying Affiliate onboarding or gaps in liability among Recipients. | Flag obligations to sign Local Services Agreements with any Affiliate without assessing creditworthiness or added risk. |
| Assets Used in Service Provision | Identify ownership and licensing of Assets and Key Equipment, plus Asset Register maintenance and update frequency. | Flag unclear ownership of jointly funded or Commissioned Assets or infrequent Asset Register updates. | Flag definitions of Assets that could capture Supplier Background IP without a carve-out. |
| Service Delivery Location | Identify permitted locations, relocation rights, and restrictions relating to data residency or security. | Flag broad Supplier discretion to relocate without Customer consent or security review. | Flag rigid restrictions preventing use of global delivery centers. |
| Supplier Solution | Identify how Supplier's delivery methodology is documented and whether Customer approval is required for changes. | Flag a vague Supplier Solution that makes the agreed delivery model difficult to enforce. | Flag approval rights that unduly constrain operational flexibility. |
| Cooperation with Other Suppliers | Identify duties to cooperate with Customer Affiliates and third-party suppliers, including interface responsibilities. | Flag weak cooperation duties that allow Supplier to attribute failures to third parties. | Flag open-ended cooperation with unnamed third parties without liability protection or cost recovery. |
| Change in Applicable Law | Identify who bears the cost and risk of new laws and the process for compliance changes. | Flag mechanisms allowing unjustified pass-through of law-change costs without benchmarking or transparency. | Flag absence of cost recovery for changes outside Supplier's control. |
| Service Levels and Service Credits | Identify Service Level categories, measurement, stabilization periods, Service Credit caps, and whether credits are a sole remedy. | Flag low caps, long stabilization periods, or sole-remedy language limiting damages or termination rights. | Flag undefined Service Levels at signing or uncapped Service Credits exposing Supplier to open-ended deductions. |
| Business Continuity | Identify Disaster Recovery Plan obligations, testing frequency, and invocation triggers. | Flag plans left to be agreed after signing or tested too infrequently. | Flag testing or reporting obligations without cost allocation for exercises requested by Customer. |
| Correction Plan for Supplier Failure | Identify Supplier Failure triggers, notice periods, approval mechanics, and implementation duties. | Flag long submission or resubmission timelines and standards allowing Supplier to self-certify remediation. | Flag unilateral Customer rejection rights without an objective reasonableness standard. |
| Step-in Rights | Identify step-in triggers, notice, scope, duration, governance, and cost allocation. | Flag triggers set so high that Customer cannot protect operations promptly. | Flag step-in without adequate notice or clear limits on Supplier liability during Customer control. |
| Governance and Reporting | Identify governance bodies, membership, meeting cadence, escalation authority, and reporting obligations. Flag unresolved committee names. | Flag missing or vague governance reducing visibility and escalation effectiveness. | Flag reporting frequency or granularity disproportionate to Charges. |
| Change Control Procedure | Identify how Change Requests and Change Orders are raised, evaluated, priced, approved, and implemented. | Flag unilateral Supplier pricing without benchmarking or cost transparency. | Flag unilateral Customer rejection without commercial discussion or compensation for preparatory work. |
| Charges | Identify fixed, unit-based, or mixed Charges; rate-card mechanics; volume assumptions; and adjustment triggers. | Flag weak cost transparency, unclear volume bands, or adjustments not tied to objective measures. | Flag Charges fixed for long periods without inflation, volume, scope, or cost adjustment. |
| Taxes | Identify VAT and tax allocation, withholding mechanics, and gross-up provisions. | Flag broad gross-up obligations shifting unexpected tax liability to Customer. | Flag unclear withholding treatment across multi-jurisdictional Service Recipients. |
| Payment | Identify invoicing, payment terms, invoice disputes, late interest, withholding, and set-off rights. | Flag absent or one-sided set-off rights and weak rights to withhold genuinely disputed amounts. | Flag short payment periods combined with broad withholding rights or no time limit for dispute resolution. |
| Benchmarking | Identify frequency, comparator methodology, scope, independent benchmarker arrangements, and consequences of unfavorable results. | Flag benchmarking limited to Charges without comparing scope or quality. | Flag mandatory price reductions without a floor protecting reasonable margin or reflecting service differences. |
| Staff Transfer | Identify applicable employment-transfer laws and allocation of pre-transfer, transfer, and post-transfer liabilities. | Flag unclear allocation of pre-transfer liabilities to Customer or weak indemnity protection. | Flag assumption of undisclosed employment liabilities or employee terms without due diligence. |
| Customer Assets | Identify ownership, licensing, permitted use, maintenance, liens, and return obligations for Customer Assets. | Flag weak protection against liens, third-party claims, misuse, or failure to return assets. | Flag "as is" provision without warranty, support, or relief for integration risk. |
| Data Security and System Access | Identify access controls, security standards and certifications, incident notice, remediation, and audit rights. | Flag vague or lengthy incident-notification timelines, weak security standards, or insufficient remediation duties. | Flag disproportionate certifications, audit duties, or security changes without cost recovery. |
| Customer Obligations | Identify Customer dependencies such as information, access, decisions, approvals, and consequences of delay. | Flag relief from liability triggered by minor or unproven Customer delay. | Flag lack of a documented process for schedule relief and cost recovery caused by Customer dependency failures. |
| Supplier Personnel | Identify Key Personnel, retention and replacement commitments, background checks, location, and skills requirements. | Flag easy substitution rights that undermine continuity or insufficient control over critical personnel. | Flag unilateral replacement demands without cause, replacement time, or cost reimbursement. |
| Supplier Subcontractors | Identify consent rights, approved Subcontractors, flow-down obligations, and Supplier liability for their acts. | Flag broad subcontracting without consent or flow-down of confidentiality, security, data protection, IP, continuity, and audit duties. | Flag approval over every Subcontractor or restrictions that create operational bottlenecks. |
| Customer Policies | Identify applicable Customer policies and the process for communicating and updating them. | Flag informal policy communication or weak enforcement against Supplier Personnel and Subcontractors. | Flag unilateral updates with immediate effect or material cost and scope consequences. |
| Warranties | Identify service quality, conformity, non-infringement, authority, and legal-compliance warranties. | Flag warranties limited to reasonable skill and care where stronger objective or industry standards are appropriate. | Flag warranties extending to third-party systems, outcomes outside Supplier control, or absolute compliance standards. |
| Intellectual Property Rights | Identify ownership of Background IP, Commissioned Materials and Software, developments, licenses, and IP indemnities. | Flag Supplier ownership of Customer-funded bespoke deliverables or insufficient perpetual use and transition rights. | Flag assignment of reusable tools, methods, or accelerators without carve-outs or license-back rights. |
| Data Protection | Identify controller and processor roles, data-processing terms, sub-processor controls, audit rights, incident handling, and transfer mechanisms. | Flag incomplete processing terms, weak sub-processor controls, or inadequate cross-border transfer safeguards. | Flag broad audits, instructions, or liabilities without notice, frequency, scope, and cost limits. |
| Limitation of Liability | Identify caps, baskets, exclusions, carve-outs, super-caps, and the cap calculation basis. | Flag caps too low for operational dependency or carve-outs improperly subject to the general cap. | Flag broad or unlimited carve-outs disproportionate to Charges and risks within Supplier control. |
| Conduct of Claims | Identify indemnification procedure, defense control, settlement consent, notice, and cooperation obligations. | Flag indemnitor control without consent over settlements affecting Customer operations, reputation, or admissions. | Flag broad Customer step-in rights over defense without objective triggers or cost sharing. |
| Insurance | Identify required policies, limits, duration, insurer requirements, and evidence obligations. | Flag limits too low relative to contract value, liability exposure, or regulated risks. | Flag insurance requirements exceeding available or market-standard coverage for the Services. |
| Payment and Performance Guarantees | Identify parent guarantees, letters of credit, performance bonds, security amounts, and release conditions. | Flag absence of credit support where the contracting Supplier has limited assets. | Flag guarantee obligations without reduction or a sunset after satisfactory performance. |
| Audit and Record Keeping | Identify audit scope, frequency, notice, retention, regulator access, confidentiality, and costs. | Flag scope or frequency limits that prevent meaningful oversight, especially in regulated services. | Flag unlimited or disruptive audits without reasonable notice, confidentiality, frequency, or cost controls. |
| Confidentiality | Identify protected information, exclusions, permitted disclosures, security standard, duration, and survival. | Flag obligations that expire too soon or omit sensitive operational, customer, or security information. | Flag perpetual obligations for all information without standard exclusions or practical retention rights. |
| Announcements and Publicity | Identify approval for public statements, customer references, trademarks, and case studies. | Flag use of Customer's name or logo without prior consent. | Flag blanket restrictions preventing generic capability statements or legally required disclosures. |
| Suspension | Identify grounds, notice, cure periods, scope, service restoration, and treatment of Charges. | Flag broad Supplier suspension for disputed payments or minor breaches without continuity safeguards. | Flag Customer suspension without standby compensation or protection against prolonged underutilization. |
| Termination | Identify cause events, insolvency, persistent Service Level breach, change of control, cure periods, convenience rights, and fees. | Flag high thresholds for cause termination or absent, costly, or impractical convenience termination. | Flag low or subjective termination thresholds, immediate termination without cure, or inadequate stranded-cost recovery. |
| Partial Termination | Identify termination of Service Towers or Local Services Agreements and the resulting Charge and resource adjustment. | Flag unclear or Supplier-controlled Charge reductions following partial termination. | Flag rights that undermine economies of scale without repricing, minimum commitments, or stranded-cost recovery. |
| Consequences of Termination | Identify wind-down, asset and data return, knowledge transfer, cooperation, and Termination Assistance scope and Charges. | Flag an assistance period or transition obligations insufficient to move to Customer or a Successor Supplier safely. | Flag extended assistance at no additional charge, below-market rates, or without capacity and dependency assumptions. |
| Anti-Corruption | Identify compliance representations, controls, Subcontractor obligations, audits, investigations, and termination rights. | Flag inadequate rights to verify compliance throughout the delivery chain. | Flag termination or suspension based on unsubstantiated allegations without materiality or due process. |
| Health and Safety | Identify responsibility at each party's premises, site rules, training, reporting, and indemnities. | Flag gaps in responsibility for Supplier Personnel at Customer premises. | Flag liability or indemnity for incidents caused by Customer premises or matters outside Supplier control. |
| Force Majeure | Identify qualifying events, exclusions, notice, mitigation, continuity obligations, relief, and termination thresholds. | Flag definitions broad enough to excuse routine failures, labor shortages, or preventable supplier problems. | Flag narrow definitions or short termination thresholds that do not reflect recovery realities. |
| Assignment | Identify consent, Affiliate transfers, financing assignments, change-of-control effects, and M&A transfers. | Flag Supplier transfers without consent, creditworthiness review, or continued parent support. | Flag Customer transfers to Affiliates or Successor Suppliers without credit protection or transition-cost recovery. |
| Governing Law and Escalation | Identify governing law, jurisdiction or arbitration, escalation stages, service of process, and urgent-relief carve-outs. | Flag an inconvenient forum or escalation that delays urgent operational or injunctive relief. | Flag asymmetric rights allowing Customer to bypass escalation or pursue broad interim relief. |

## Additional Checks

Always flag:

- unresolved bracketed or placeholder text, such as `[date]`, `[Name of Party's entity]`, `[Name of the relevant committee]`, `[TBC]`, or `[●]`;
- any referenced Schedule that is missing, unattached, incomplete, or left to be agreed, including Service Towers, Service Levels, Charges, Change Control, Security, Business Continuity, Data Processing, and Termination Assistance; and
- numeric inconsistencies in timelines, thresholds, caps, rates, or notice periods that appear to be drafting errors rather than negotiated terms.

Deliver the review inline in the chat response. Do not generate a downloadable Word document unless the user explicitly asks for one.
