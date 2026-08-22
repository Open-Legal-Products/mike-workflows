---
name: "pipl-cross-border-triage"
description: "Select the lawful outbound path for personal information leaving the PRC under PIPL Articles 38-40 and the Provisions on Promoting and Regulating Cross-border Data Flows (CAC Order No. 16, 2024): classify the processor and the data, apply the Article 5 exemptions and FTZ negative-list route, then route to security assessment, standard contract or certification, or no three-mechanism filing. Use when a vendor, HQ, cloud region, or HR system will receive PRC personal information abroad. The workflow drafts; a human files and signs."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Xing Peng"
  language: "English"
  mike-display-name: "PIPL Cross Border Triage"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Data Protection"
  jurisdictions: "People's Republic of China"
---
# PIPL Cross Border Triage

PIPL does not treat every outbound transfer the same way. This workflow classifies the transfer against the statute and the 2024 Provisions, then produces a path card. Filing, signing the standard contract, and submitting an assessment stay with the lawyer. Do not guess counts, CIIO status, or important-data designations; mark missing inputs as gaps.

Confirm every cited article in the official Chinese text in session. If a number cannot be confirmed, keep a [TO VERIFY] tag and do not treat the path as closed.

## Step 1 - Is this an outbound provision of personal information

Record: who is the personal-information processor; whether it is a critical information infrastructure operator (CIIO); categories of personal information and whether any are sensitive (PIPL Article 28); whether any data have been identified as important data; destination, recipient, purpose, and necessity. PIPL Article 4 is the personal-information definition. Important data that has not been identified or notified is not presumed important solely because it is outbound (Provisions Article 3). If the facts do not show an outbound provision, stop.

## Step 2 - Separate consent and PIPL Chapter III duties

PIPL Article 39 requires informing the individual of the recipient's name, contact method, purpose, method, and categories, and obtaining separate consent, unless another law or administrative regulation provides otherwise. PIPL Article 38, second paragraph, requires necessary measures so the overseas recipient meets PIPL protection standards. These duties sit alongside, not instead of, the path in Step 4. Flag them as open items on every path.

## Step 3 - Exemptions and FTZ overlay (Provisions Articles 5-6)

Test Provisions Article 5 before any filing path. Any one qualifying limb can exempt the three mechanisms (security assessment, standard contract, certification), provided the data are not important data:

1. necessary to conclude or perform a contract to which the individual is a party (the article lists examples such as cross-border shopping, delivery, remittance, payment, account opening, tickets and hotels, visas, examination services);
2. necessary for cross-border human-resources management under lawfully adopted work rules and a lawfully concluded collective contract;
3. necessary in an emergency to protect life, health, or property;
4. a non-CIIO whose cumulative outbound non-sensitive personal information from 1 January of the current year is below 100,000 individuals.

Then test Provisions Article 6: if the processor is in a free-trade zone and the data are outside that zone's published negative list, the three mechanisms may also not apply. Quote the list in force for that zone or mark [TO VERIFY]. Article 5 and Article 6 do not waive PIPL Articles 39 and 55(4).

## Step 4 - Choose the remaining mechanism

If no exemption applies, route in this order. Counts run from 1 January of the current year, unique natural persons, as explained in the CAC Q&A on the Provisions. Recheck the official text before using a number.

- Security assessment (PIPL Articles 38(1) and 40; Provisions Article 7): CIIO providing personal information or important data abroad; or a non-CIIO providing important data, or cumulative outbound non-sensitive personal information of 1,000,000 or more individuals, or sensitive personal information of 10,000 or more individuals. File through the provincial cyberspace administration to the national CAC. Provisions Article 9: an assessment result is valid for 3 years from issuance; extension is an application, not automatic.
- Standard contract or certification (PIPL Article 38(2)-(3); Provisions Article 8): a non-CIIO with cumulative outbound non-sensitive personal information of 100,000 or more and fewer than 1,000,000 individuals, or sensitive personal information of fewer than 10,000 individuals. The Standard Contract Measures require a PIPIA before using the CAC template and a filing with the provincial CAC within 10 working days after the contract takes effect. Confirm those filing details in the Measures text in session.
- Do not invent a fourth "other conditions" path under PIPL Article 38(4) unless the user supplies a specific law, administrative regulation, or CAC rule.

If Article 5 or 6 applies, the card is "no three-mechanism filing on these facts", with the limb cited, not "unrestricted export".

## Output

A path card: facts used, exemption limbs tested, selected mechanism or exemption, PIPL Article 39 and Article 55(4) open items, documents to draft next, and every [TO VERIFY] item. If counts or CIIO status are unknown, stop at a gap list rather than picking a path.

## Governance boundary

The workflow classifies and drafts. A human confirms the official text, signs the standard contract, files the assessment or filing, and sends anything outward. No filing is automatic.
