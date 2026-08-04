---
name: "legal-syllogism"
description: "Build the explicit legal syllogism for an issue: state the major premise (the rule and its interpretation), the minor premise (the material facts), the application subsuming each fact under each element of the rule, and the conclusion, then flag the weak links - unstated assumptions, contested facts, debatable interpretation. Forces every step of the reasoning to be said out loud and checkable instead of jumping from facts to a holding. Maps to civil-law subsumption and common-law IRAC/CREAC. Use when drafting an opinion, brief, or memo and the reasoning needs to be laid out element by element."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Wieslaw Mazur / MateMatic Solutions"
  language: "English"
  mike-display-name: "Legal Syllogism"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Legal Analysis"
  jurisdictions: "General"
---
# Legal Syllogism

A flawed opinion rarely fails at the conclusion - it fails at the premise nobody stated. Legal reasoning is a syllogism: the rule (major premise), the facts (minor premise), the application, and the conclusion. When a step is left unsaid because it seems obvious, that is where the gap hides, and that is where the other side, or the court, will strike. This workflow forces each step to be stated and marks what is settled and what is contested.

It structures the reasoning; it does not decide the case. Judgement and the decision stay with the lawyer.

## Method (subsumption / IRAC)

1. Major premise (rule and interpretation) - identify the governing rule, then its reading: how each element of the rule is construed (text, structure, purpose). Note where authority or commentary splits.
2. Minor premise (material facts) - list the facts that matter to the rule's elements. Separate undisputed facts from contested ones, and facts from characterisations.
3. Application (subsumption) - for each element of the rule, show which fact satisfies it or does not. This is the real work: matching fact to element.
4. Conclusion - the legal consequence that follows from the application.
5. Weak-link test - mark which elements are contested in interpretation, which facts are contested on the evidence, and which assumptions were made silently. This is the map for any adversarial review that follows.

## Output format

```
ISSUE: <the legal question>

MAJOR PREMISE (rule): <provision/authority> - "<elements>"
  Interpretation: <how the elements are read; any split in authority>

MINOR PREMISE (material facts):
  - undisputed: <...>
  - contested (evidence): <...>

APPLICATION (element -> fact):
  - <element 1> : satisfied by <fact> | NOT satisfied | contested
  - <element 2> : ...

CONCLUSION: <legal consequence>

WEAK LINKS:
  - interpretation: <which element is contested and why>
  - facts: <what needs proof>
  - silent assumptions: <...>
```

## Limits

- The syllogism orders reasoning - it does not perform interpretation or fact-finding. Whether the rule, its reading, and the facts are right is for the lawyer.
- It does not weigh competing arguments - it arranges them so attack and verification have something to work on.
- Subsumption assumes a rule with elements. For open-textured standards and the balancing of principles, a pure syllogism is not enough - mark it as balancing, not subsumption.
