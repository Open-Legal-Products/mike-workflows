---
name: "output-scoring"
description: "Score the quality of an AI-produced legal output before it goes out, in two layers kept deliberately apart: an objective layer of mechanically checkable facts (do the cited authorities exist, are the provisions and docket numbers real, did any red-flagged finding drop out of the summary) and a subjective layer judged against an explicit 1-5 rubric (legal correctness, completeness, clarity, jurisdiction fit, grounding). Returns a scorecard and one of three decisions: send, revise, or route to full verification. A layer above the deliverable - it scores, it does not write or fix. Jurisdiction-neutral. Use before sending an opinion, memo, or brief, or whenever the question is whether an AI-assisted draft is ready to go out."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Wieslaw Mazur / MateMatic Solutions"
  language: "English"
  mike-display-name: "Output Scoring"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Legal Review"
  jurisdictions: "General"
---
# Output Scoring

Before you send it, score it - and keep what is checkable apart from what must be judged. An AI output can read smoothly and still be wrong. This workflow scores it in two layers: objective (facts you can verify mechanically) and subjective (quality you have to judge against an explicit rubric). Mixing the two is where false confidence comes from - "sounds right" is not "the citations check out".

It scores; it does not write or send. The decision is the lawyer's; the scorecard is the basis.

## Layer 1 - objective (mechanically checkable)

Check, do not guess:

- Citations and provisions - does each cited authority exist, and does the quoted or paraphrased content match the source; were all citations caught (a missed citation is an unverified one).
- Dockets and identifiers - real and correctly written.
- Completeness against the underlying analysis - did any red-flagged finding drop out of the final summary.

The objective result is binary per item: matches or does not. Even one mismatched citation means the output is not ready, whatever the subjective score.

## Layer 2 - subjective (1-5 rubric)

Score each dimension 1-5 with a one-sentence reason:

| Dimension | 1 | 5 |
|---|---|---|
| Legal correctness | thesis wrong or unsupported | thesis sound and grounded in the rule |
| Completeness | omits material issues | covers everything material to the question |
| Clarity | muddled, inconsistent | precise, readable for the intended reader |
| Jurisdiction fit | confuses systems or rules | correct for the governing law |
| Grounding (anti-hallucination) | claims with no basis | every claim has a basis |

## Decision

- Send - Layer 1 clean and the subjective average is at least 4, with no dimension below 3.
- Revise - Layer 1 clean but a dimension scores 2-3 (name it and say why).
- Full verification - Layer 1 has a mismatch or any dimension scores 1: route the deliverable to citation verification and the adversarial-legal-review workflow in this pack.

## Output format

A compact scorecard: the Layer 1 line (citations, provisions, dockets, completeness - each OK or X), the five Layer 2 dimensions with scores and reasons, the average, and the decision with its trigger, for example: "Revise (Completeness 3 - limitation period not addressed)".

## Limits

- The subjective score is judgement against a rubric, not an oracle - at high stakes the final call is the lawyer's, and the scorecard is evidence of due diligence.
- Layer 1 does not replace the verification steps it draws on - it aggregates them into one decision.
- It scores the output; it does not create or fix it.

## Attribution

The two-layer method - objective matching plus a subjective judge rubric on a 1-5 scale - is based on DISC-Law-Eval from DISC-LawLLM (Fudan DISC Lab), Apache-2.0. Exam data and the judge model are dropped; the rubric dimensions, thresholds, and framing are the author's own.
