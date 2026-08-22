---
name: "pipl-incident-notification"
description: "Run the PIPL Article 57 incident tree for leakage, tampering, or loss of personal information, including the 'may occur' limb: take immediate remedial measures, decide whether notice to the personal-information protection department and to individuals is required, apply the Article 57 exception where measures can effectively avoid harm, and draft the department notice, the individual notice, and the internal record. Use for a leak, ransomware event, misdirected message, or lost device. The workflow drafts; a human decides and sends."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Xing Peng"
  language: "English"
  mike-display-name: "PIPL Incident Notification"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Data Protection"
  jurisdictions: "People's Republic of China"
---
# PIPL Incident Notification

PIPL Article 57 is an immediate-remediation and notice duty, not a GDPR 72-hour transplant. This workflow classifies the event, lists the statutory notice content, and produces drafts. The decision to notify and the act of sending stay with the processor. Confirm the official Chinese text in session. Do not import the GDPR 72-hour clock unless a separate PRC rule in the file actually supplies a clock, and then cite that rule or mark [TO VERIFY].

## Step 1 - Is it an Article 57 event

Article 57 applies when personal information has been, or may be, leaked, tampered with, or lost. Record the type (confidentiality, integrity, availability), the categories and approximate volume of personal information, whether any are sensitive, how individuals could be identified, and the remedial measures already taken. If the facts do not support leakage, tampering, or loss, stop rather than stretching the article.

## Step 2 - Immediate measures and who must be notified

The processor must immediately take remedial measures and notify the department performing personal-information protection duties and the individuals. Identify the competent department from the facts (sector regulator and/or local cyberspace administration). If the department cannot be named from the file, list it as a gap.

Article 57, second paragraph: if the measures taken can effectively avoid harm to information security, notice to individuals may not be required; if the department believes harm can still occur, it may require the processor to notify individuals. Record the harm-avoidance analysis explicitly. "We would rather not notify" is not an analysis.

## Step 3 - Content of the notice (Article 57, third paragraph)

Draft notices covering:

- the categories of personal information that were or may be leaked, tampered with, or lost;
- the causes and the possible harm;
- the remedial measures taken;
- measures individuals can take to mitigate harm;
- contact information of the personal-information processor.

Write the individual notice in clear language. Keep a parallel internal record of facts, effects, and measures even when individual notice is withheld under the second paragraph.

## Step 4 - Overlays to check, not to invent

Ask whether any of these also apply, and mark each [TO VERIFY] against the current official text rather than merging them into Article 57:

- the Network Data Security Management Regulation, if the incident is a network-data security incident with its own reporting channel and time limit;
- sector rules (finance, telecoms, healthcare) that impose shorter clocks or extra recipients;
- PIPL Article 51(6) contingency plans, which should already exist; note their absence as a gap.

Do not silently replace Article 57 with a GDPR Articles 33-34 template.

## Output

An incident card: classification, remedial steps taken, department identified, individual-notice on or off with the Article 57 second-paragraph reasoning, drafts of both notices, and the internal record. Missing facts stay as gaps.

## Governance boundary

The workflow runs the tree and drafts. A human approves the harm analysis, picks the department, and sends. Sending is never automatic.
