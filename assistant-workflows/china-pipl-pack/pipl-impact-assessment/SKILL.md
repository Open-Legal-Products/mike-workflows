---
name: "pipl-impact-assessment"
description: "Run the personal-information protection impact assessment required by PIPL Articles 55-56: test the five mandatory triggers, then draft the three-part assessment (lawfulness, necessity and legitimacy of purpose and method; impact and security risk to individual rights; whether protective measures are lawful, effective, and matched to the risk) and the three-year record. Use before processing sensitive personal information, automated decision-making, entrusted processing, provision to another processor, public disclosure, or outbound transfer. The workflow drafts; the processor accepts residual risk and keeps the file."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Xing Peng"
  language: "English"
  mike-display-name: "PIPL Impact Assessment"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Data Protection"
  jurisdictions: "People's Republic of China"
---
# PIPL Impact Assessment

PIPL calls this a personal-information protection impact assessment, not a GDPR DPIA. This workflow tests whether Article 55 requires one and drafts the Article 56 content. Residual-risk acceptance and the decision to proceed stay with the processor. Confirm every cited article in the official Chinese text. Unconfirmed citations stay tagged [TO VERIFY] and cannot support "not required".

## Step 1 - Is an assessment required (Article 55)

A prior assessment and a processing record are mandatory in any of these cases:

1. processing sensitive personal information (Article 28 definition; children's information under fourteen is sensitive);
2. using personal information for automated decision-making;
3. entrusted processing, providing personal information to another personal-information processor, or disclosing personal information;
4. providing personal information abroad;
5. other processing activities that have a major impact on individual rights and interests.

Record required or not required with a per-limb justification. "Other major impact" is not a clearance: if the facts are thin, mark recommended and list the missing facts. Article 54 compliance audits are a separate periodic duty; do not treat this assessment as satisfying Article 54.

## Step 2 - Draft the Article 56 content

Draft all three elements. Missing facts become gaps, not invented findings.

- (1) Whether the purpose and method of processing are lawful, legitimate, and necessary. Tie this to a PIPL Article 13 legal basis and to the principles in Article 5 (lawfulness, legitimacy, necessity, good faith; purpose limitation; minimisation; openness and transparency). For sensitive personal information also walk Article 29 (specific purpose, sufficient necessity, strict measures, separate consent unless a law provides otherwise) and Article 30 (notice of necessity and impact).
- (2) Impact on individual rights and interests, and security risk: confidentiality, integrity, and availability scenarios; likelihood and severity; groups such as children or employees.
- (3) Whether protective measures are lawful, effective, and matched to the risk, against the Article 51 catalogue (internal management rules, classification, encryption or de-identification, access control, training, incident plans) so far as the facts support.

Article 56, second paragraph: keep the assessment report and the processing record for at least three years.

## Step 3 - Entrusted processing and outbound overlays

- Entrusted processing (Article 21): the commission agreement must state purpose, period, method, categories, protection measures, and the rights and duties of both sides. The trustee must process as agreed, return or delete on completion, and not further subcontract without consent. If the user is assessing a vendor deal, list these contract points as open items rather than rewriting the commercial terms.
- Outbound transfer (Article 55(4)): this assessment is required even when the 2024 Cross-border Data Flow Provisions exempt the three filing mechanisms. Do not treat an Article 5 exemption as skipping Article 55.

## Output

A draft assessment: trigger table, Article 56 narrative with gaps marked, three-year retention note, and a residual-risk line for the processor to accept or reject. Do not declare the processing "compliant".

## Governance boundary

The workflow screens the trigger and drafts the file. A human accepts residual risk, signs, and keeps the record. Nothing is filed automatically.
