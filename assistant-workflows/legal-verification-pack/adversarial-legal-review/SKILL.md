---
name: "adversarial-legal-review"
description: "A red team for a high-stakes deliverable - takes a finished document (a legal opinion, a DD or M&A memo, a court or board submission, a recommendation) and runs an adversarial debate: a builder constructs the strongest version of the thesis, an attacker tears it apart with counter-arguments and contrary authority, a synthesizer reconciles pillar by pillar, and a verifier runs a ten-point final check. A bounded revision loop with regression-revert guarantees the delivered version is never worse than the best one seen. Cost-gated: for high-stakes work only, not every query. Use when the question is what the other side will say, where the weaknesses are, or whether a thesis survives attack - before an opinion, memo, or submission goes out."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Wieslaw Mazur / MateMatic Solutions"
  language: "English"
  mike-display-name: "Adversarial Legal Review"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Legal Review"
  jurisdictions: "General"
---
# Adversarial Legal Review

Better your own assistant finds the weakness in your thesis than your opponent finds it in the hearing. A single pass produces an argument that sounds confident - because the model is trained to sound confident. That is an illusion of competence. The real value of an expert is to foresee the counter-argument, the contrary authority, and the gap in reasoning before the other side does. This workflow builds that move into the method: one role defends, one attacks, one reconciles, one verifies.

This is NOT writing a deliverable from scratch. It is a stress-test of a finished deliverable.

## Cost gate (read BEFORE running)

The full cycle is expensive. Run it only for high-stakes work:

| Run (high-stakes) | Do NOT run (routine) |
|---|---|
| A legal opinion going to a client | An internal note |
| Due diligence / an M&A memo | A summary of a judgment |
| A court submission before a deadline | A working draft |
| A recommendation to a board | FAQ, marketing content |
| A position carrying material financial or reputational risk | A routine query |

If the matter is not high-stakes, say so plainly and offer an ordinary single-pass review (or the opposing-counsel-attack workflow in this pack) instead of the full debate.

## Workflow (4 roles + verification)

Each role is a separate pass with a clean mandate. Pseudonymise the input if the document contains privileged or personal data.

### Reviewer access tiers (anti-bias)

Reviewers split into two tiers with DIFFERENT access - deliberately:

- ISOLATED (internal consistency): the logic-and-structure reviewer sees only the current draft - no sources, no authority. Mandate: does the thesis contradict the reasoning, do the conclusions follow from the premises, are there logical gaps. It does NOT judge whether a citation is real. If this reviewer saw the sources, it would confuse "sounds-like-the-source" with "is-internally-consistent".
- AUGMENTED (grounding): the attacker and the citation check see the sources and the intake, and pull contrary authority.

When one model simulates all the roles, isolation is prompt discipline, not a hard sandbox - explicitly instruct the ISOLATED role not to reach for sources.

### 0. High-stakes gate
Assess whether the matter qualifies (table above). If not, stop and offer an ordinary review.

### 1. Builder - the strongest version of the thesis
Build the strongest possible argument for the deliverable's thesis. Gather the best rules, authority, and doctrine. Goal: give the attacker a hard target, not a straw man. Output: thesis + 3-7 pillars, each with its legal or evidentiary basis.

### 2. Attacker - devil's advocate
Attack each pillar like opposing counsel or a sceptical court: contrary authority (real sources for the relevant jurisdiction), a doctrinal counter-argument, a factual or evidentiary gap, over-reading of a rule, an omitted exception, an out-of-date line of authority, procedural risk (deadlines, standing, jurisdiction). Output per pillar: the charge, its strength (high/medium/low), and the source of the charge.

### 3. Synthesizer - the balance
For each pillar decide: survived / weakened / defeated. State what is left of the thesis after the attack, where the deliverable needs reframing, where a caveat is required ("contested risk, authority is split"). Output: a table of pillar, verdict, recommended change.

Priority hierarchy when charges collide: logic (consistency) ~ citations (grounding) ~ counter-arguments, all above style, above clarity. The substantive layer never trades against itself - on conflict, accumulate BOTH views and add a caveat; do not pick arbitrarily. Style and clarity never override substance.

### 4. Verifier - final check (10 points)
1. Every citation grounded - the quote exists in the source word for word (BLOCK on a failure)
2. Every pillar has a basis
3. No defeated pillar left in the final thesis without a caveat
4. The attacker's contrary authority addressed, not swept under the rug
5. No categorical claims where the line is contested
6. Currency of the rules (not repealed or amended)
7. Internal consistency (thesis does not contradict the reasoning)
8. Scope matches the client's question - no more, no less
9. Procedural risks listed
10. Confidence level stated explicitly (no false certainty)

## Revision loop (bounded)

The debate is not single-pass, but it runs within hard limits, with a guarantee that the shipped version is never worse than the best one seen.

- Versioning: draft_v1 (after the first synthesis), draft_v2... Each iteration = targeted edits from the synthesizer's recommendation, then a re-attack and verification.
- aggregate_score (0-100) = the mean of: verifier (X/10, scaled) + consistency (ISOLATED, 0-100) + grounding (AUGMENTED, 0-100). Hard component: the citation grounding check - any failure blocks regardless of score.
- v_best: after each iteration, remember the draft with the highest aggregate_score.
- Iteration cap: high-stakes = max 3 rounds; quick mode = max 1.

The synthesizer owns the exit decision, evaluated in order:

1. Clean approval - all reviewers accepted, no blockers: exit approved_on_vN.
2. Regression-revert (from round 2) - the new score is lower than v_best: reject the round, restore v_best, exit with a banner "round N made the deliverable worse - reverted to the best version".
3. Plateau early-exit (from round 2) - score at or above threshold (default 85) but improvement under 1 point: exit early rather than burn effort on marginal gains.
4. Continue - blockers remain, cap not reached, no regression or plateau: another round of targeted edits.
5. Forced exit at max - cap reached with blockers: deliver the best version with a banner listing the unresolved blockers.

## Terminal states and always-deliver

Every ending MUST produce an artefact for the human - never a silent or empty exit. Terminal states: approved_on_vN, accepted_early_on_vN, forced_exit_on_v_best (regression), forced_exit_at_max, failed_with_fallback (e.g. no source material - deliver what exists plus the reason). The closing banner always shows the terminal state, which draft version was delivered, and what blockers remain.

## Output

A review block containing: the stakes assessment, iteration history with scores, a pillar table (pillar, attack and strength, verdict, action), the ten-point verifier result, the confidence level after the debate, and a plain recommendation ("do NOT send before fixing the failed citation and adding a caveat to the defeated pillar"). Keep the full debate transcript (builder, attacker, synthesizer) as an attachment - it is the evidence of adversarial verification. Where AI-governance rules apply to the firm's tooling (e.g. EU AI Act Articles 12 and 14), the transcript doubles as the record of human oversight.

## Governance boundary

The workflow produces a recommendation and draft versions; it does NOT send the document. The decision to send despite remaining blockers stays with the human. For privileged material, pseudonymise the input before running; pulling contrary authority uses public sources.

## Position in this pack

The judicial-first-impression workflow reports neutrally how a text lands; the opposing-counsel-attack workflow is the cheap single-pass attack; this workflow is the top rung - the full debate for high-stakes deliverables. After revision, the output-scoring workflow turns the result into a send / revise / verify decision.

## Attribution

The debate-plus-verification pattern is inspired by AnttiHero/lavern (Apache-2.0); roles, prompts, and the ten-point check are written from scratch. Bounded self-revision (the exit tree with regression-revert), reviewer access tiers (isolated/augmented), the synthesizer's conflict-priority rule, and the always-deliver invariant are adapted clean-room from gregmos/memoforge (MIT) - concepts of loop control and roles, not prompts or code.
