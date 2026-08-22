---
name: "pipl-individual-rights-requests"
description: "Handle an individual's request under PIPL Chapter IV (Articles 44-50): identify the right invoked (know and decide, access and copy, correction, deletion, explanation of processing rules, rights of close relatives of a deceased person), verify identity, apply the Article 47 deletion grounds and the Article 50 refusal-and-explanation duty, and draft the response plus a request register entry. Use when an access, deletion, or correction request arrives. The workflow drafts; a human decides, performs deletion or export, and sends the response."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Xing Peng"
  language: "English"
  mike-display-name: "PIPL Individual Rights Requests"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Data Protection"
  jurisdictions: "People's Republic of China"
---
# PIPL Individual Rights Requests

A rights request is a classification plus a reasoned response, not an automation. The workflow names the right, drafts, and keeps a register. Fulfil-or-refuse, deletion, and sending stay with the processor. Confirm articles in the official Chinese text; unconfirmed citations stay [TO VERIFY].

## Step 0 - Identity, channel, and clock

PIPL Article 50 requires convenient mechanisms for individuals to exercise their rights. Record receipt date, channel, and the identity evidence offered. Where identity is reasonably in doubt, ask for what is needed to confirm it; do not use verification to obstruct the request. PIPL does not copy the GDPR one-month clock. Do not import a 30-day deadline from GDPR. Use any deadline the processor has published in its privacy notice or that a specific law or regulation supplies, and mark [TO VERIFY] if none is in the file. Preserve the original receipt date in the register.

## Step 1 - Classify the right

Interpret substance, not the heading.

| Article | Right | What to extract from the facts |
|---|---|---|
| 44 | Know and decide; restrict or refuse handling of their personal information | scope of processing challenged |
| 45 | Access and copy | systems that actually hold the person's data, not only a processing inventory |
| 46 | Correction or supplementation | the inaccurate or incomplete fields |
| 47 | Deletion | match a ground in Article 47, then check whether deletion is technically infeasible (in which case stop processing except for storage and necessary security measures) |
| 48 | Explanation of processing rules | the rules actually applied, not a generic policy paraphrase |
| 49 | Close relatives of a deceased person, for their own lawful and legitimate interests | relationship and the interest claimed |

Article 24 (automated decision-making) is a related objection and explanation right; if the request is about a solely automated decision, route it here as well and do not treat it as a free-standing GDPR Article 22 analogue.

## Step 2 - Deletion grounds (Article 47)

Deletion is required if any of these apply: the handling purpose has been achieved, cannot be achieved, or is no longer necessary; the processor stops providing products or services, or the retention period has expired; the individual withdraws consent; the processor handled personal information in violation of law, administrative regulation, or the agreement; other circumstances provided by law or administrative regulation. If the retention period has not expired or deletion is technically hard, record the statutory fallback (stop processing other than storage and security) rather than inventing a "keep" justification.

## Step 3 - Refusal, explanation, and next forum (Article 50)

If the processor rejects the request, it must explain the reason. Draft that explanation from a cited provision, not from convenience. Tell the individual of the right to complain to a department performing personal-information protection duties and to bring a lawsuit. A refusal without a statutory anchor is a gap, not a draft to send.

## Step 4 - Draft the response and the register

Draft in clear language. For access, retrieve from operational systems; a response written only from a processing inventory is incomplete. Close with a register line: receipt date, right invoked, identity steps, outcome, and any deletion or export still waiting on a human.

## Governance boundary

The workflow classifies and drafts. A human verifies identity, decides fulfil or refuse, performs deletion or export, and sends. Irreversible and outward acts are never automatic.
