---
name: "any-rule-catcher"
description: "Build a dated, court-sourced table of every rule that actually binds one filing on one subject, across all four layers that can carry one — national or statutory, court-wide, the individual judge, and the room next door. Use for filing deadlines and computation of time, word and page limits, appendices and record excerpts, courtesy copies, sealing and redaction, oral argument, electronic filing, AI disclosure, or any other subject where the governing rule is scattered. Catches superseded standing orders, defaults that bind by silence, and rules a local order cannot lawfully change."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Lee Czocher"
  language: "English"
  mike-display-name: "Any Rule Catcher"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Litigation"
  jurisdictions: "United States"
---

# Any Rule Catcher

Produce a dated, court-sourced table of the rules that bind one filing on one subject. Not a summary. A table.

No subject lives at one layer. A word limit is a national rule modified by a circuit rule modified by a judge's practices. A deadline is a triggering rule plus a computation rule plus a service rule plus a local variation. Someone who reads one of those and stops has read the wrong rule, confidently.

## Ask first, research after

Ask these as a numbered list in one message, then stop and wait. Research nothing until they are answered.

1. **Subject.** One per run. If the user names three, ask which one first.
2. **Scope.** Which courts — one circuit, several, all of them, one district, one judge. Accept a small scope. Do not widen it quietly.
3. **State courts.** Which states, if any, or federal only.
4. **The case.** Court, division, judge, case type. Without the judge, the judge layer is guesswork; say plainly what is lost without a name.
5. **Ethics and statutes.** Include the bar-conduct and statutory layers, or courts only.
6. **Columns.** Every row carries jurisdiction and/or judge and a link to the rule text; those are fixed and are not asked about. Offer the rest as a list to pick from: source of authority, summary, what silence means, operative language quoted verbatim, effective date, verified date, and for deadlines the trigger document, the computation rule applied, and whether the deadline is jurisdictional or procedural. If the user does not answer, use source of authority, summary, what silence means, operative language and effective date, and say so. If they leave out operative language or effective date, note once at delivery that verbatim text is what makes a row defensible and the effective date is what makes supersession visible. Say it once; do not argue.
7. **Where the table should go.** If it can be saved to a location the user names, ask for one. If not, say so, skip the question, and plan to deliver the table in the conversation with the filename to save it under.

## Divide the scope before researching

Split the scope into slices — roughly one per circuit, one per state system, one for the national layer — and work them separately rather than attempting the whole scope in a single pass, which produces summary instead of reading. Match the number of slices to the scope given, not to the maximum available.

Apply this discipline to every slice:

- Never answer from memory. Every fact comes from a page fetched in this session.
- Sources must be the court's own domain. Third-party trackers, treatises, firm alerts and news articles may be used to learn where to look, never cited as the source of a rule. They go stale silently.
- Quote operative language verbatim. The practitioner has to reproduce it or rely on it.
- Record the negative as a finding. "No provision at this layer, confirmed against the current edition on [date]" is a usable answer. A blank cell is not.
- Anything unfetchable goes in an unverified list below the table, with where it was reported. Never promote it into a row.
- For every rule, state what silence or inaction means. A rule that only says what to do when you act is not the whole rule.
- Watch for supersession — replaced, withdrawn, or left posted after the judge stopped sitting.

## The four layers, in this order, every time

1. **National or statutory.** The federal rules, or the state equivalents, and any statute. This is the floor and sometimes the ceiling. Catch proposals too and label the posture exactly: published for comment, approved, transmitted, effective.
2. **Court-wide.** The circuit's or district's own local rules and general orders.
3. **The judge.** Standing order, individual practices, required forms, from the judge's own current page — not a tracker, a memo, or a conference deck.
4. **The room next door.** County or district local rules for state filings, the clerk's own posted procedures, and state bar ethics opinions where conduct is in issue.

Search each layer's rule text for the subject's terms and read around every hit. A count is not a finding. The two subjects that most often bind at the judge layer and nowhere else are courtesy copies and judge-specific certificates; a rules-only search misses them entirely.

## Four traps, checked out loud

**The rule everyone knows has been superseded.** Ask whether a court-wide rule has swallowed a judge's order, whether an order was withdrawn, and whether one is still posted after the judge stopped sitting. The most-cited order in a field is the likeliest to be out of date, because everyone learned it at the same time.

**The default binds by silence.** Some rules make filing nothing an affirmative representation. For every rule caught, ask what it makes silence mean and put the answer in the table.

**The computation stack.** A deadline is never one rule. It is the trigger, the period, the computation rule, the service rule, and any local or standing-order variation. Catch all five or the deadline has not been caught. Name the trigger document, not just the number of days.

**Some rules cannot be changed by the ones below them.** A local rule or standing order cannot alter a jurisdictional deadline, and parties cannot waive or extend one by agreement. Mark every deadline row jurisdictional or procedural. If the text does not settle it, say so in the row rather than guessing — the consequence of being wrong differs completely between the two.

## Output: two tables, withdrawn first

**Withdrawn and modified rules come before the live ones.** The most common way to be wrong is not missing a new rule; it is filing under an old one. Include withdrawn, superseded, declined, lapsed with the judge, still posted but the judge no longer sits, and pending but not yet in force — and say which each one is.

**Then the live rules**, in the columns the user chose: jurisdiction and/or judge first, the chosen fields next, link to the rule text last.

- Source of authority is never just "rule." Say which: statute, national rule, adopted local rule, general order, judge standing order, individual practices, clerk's procedure, ethics opinion, proposal declined, proposal pending. They carry different force and different amendment paths, and flattening them is worse than no table.
- The summary must say what silence means.
- Every row gets a working link. A row without one is not a row.
- Unfetched material goes below the tables, marked reported but unverified, with where it was reported.

**Put the run date on the face of the table.** "Run [date]. Every row fetched that day from the issuing court's own domain." Every such table is a snapshot and must say so.

## Versioning and re-runs

Never overwrite a prior run — each is a new dated file, and superseded versions are archived rather than deleted. One file is the file of record and its name says so.

On a re-run, diff it. Compare row by row against the prior run and report what moved: rules added, rules withdrawn, effective dates changed, judges reassigned. The diff is the product. Anyone can produce a list; the value is knowing what stopped being true.

## Verify at the destination

If the table was saved somewhere, confirm it arrived: the rows are present, the links resolve, and the run date is on it. A tool reporting success only means its command ran. If it could not be saved, deliver the table in full, give the filename to save it under, and hand over the versioning rules rather than skipping them.

## Out of scope

This does not give advice; it reports what a court has published. It cannot see chambers preferences, which are unpublished and bind anyway — call the clerk on the assigned judge the week of filing. Absence is never proven, only confirmed against the current published edition on a date, and the table must say it in those words. This is not a subscription and not a list. It is run by the person filing, on their matter, the week they file, which is the only thing that makes it current.
