---
name: "ai-rule-catcher"
description: "Build a dated, court-sourced table of the generative-AI rules that bind one court filing — disclosure, certification, verification and use requirements — across all four layers that can carry one: national or statutory, court-wide, the individual judge, and the clerk or bar next door. Catches standing orders that have been superseded or left posted after a judge stopped sitting, proposals mistaken for rules, and the three different things silence can mean. Use before filing anything in a court whose AI obligations have not been checked this month."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Lee Czocher"
  language: "English"
  mike-display-name: "AI Rule Catcher"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Litigation"
  jurisdictions: "United States"
---

# AI Rule Catcher

Produce a dated, court-sourced table of the generative-AI obligations that bind a filing. Not a summary. A table.

No subject lives at one layer, and this one moves faster than any of them. An AI obligation can sit in a national rule, a court-wide local rule, a judge's own standing order, or a clerk's posted procedure, and those layers do not agree with each other. Someone who reads one and stops has read the wrong rule, confidently.

The subject is fixed. Do not widen it into a general rules survey.

## Ask first, research after

Ask these as a numbered list in one message, then stop and wait. Research nothing until they are answered. Do not pad them with explanation.

1. **Scope.** Which courts — one circuit, several, all of them, one district, one judge. Accept a small scope. Do not talk the user out of it and do not widen it quietly.
2. **State courts.** Which states, if any, or federal only.
3. **The judge layer.** Judge-level orders only where the judge's own current page was fetched, or may reported orders appear marked plainly as unconfirmed. Without a judge's name the judge layer is guesswork; say plainly what is lost without one.
4. **Ethics and statutes.** Include the bar-conduct and statutory layers for the states named, or courts only.
5. **Columns.** Every row carries jurisdiction and/or judge and a link to the rule text; those are fixed and are not asked about. Offer the rest as a list to pick from: source of authority, summary, what silence means, operative language quoted verbatim, effective date, verified date, and for any deadline the trigger document, the computation rule applied, and whether it is jurisdictional or procedural. If the user does not answer, use source of authority, summary, what silence means, operative language and effective date, and say so. If they leave out operative language or effective date, note once at delivery that verbatim text is what makes a row defensible and the effective date is what makes supersession visible. Say it once; do not argue.
6. **Where the table should go.** If it can be saved to a location the user names, ask for one and do not pick for them. If it cannot be saved, say so, skip the question, and plan to deliver the table in the conversation with the filename to save it under.

## Divide the scope before researching

Split the scope into slices — roughly one per circuit, one per state system, one for the national layer — and work them separately rather than attempting the whole scope in one pass, which produces summary instead of reading. Match the number of slices to the scope given, not to the maximum available. A single circuit is one or two slices, not eight.

Apply this discipline to every slice:

- Never answer from memory. Every fact comes from a page fetched in this session.
- Sources must be the court's own domain. Third-party trackers, university trackers, firm alerts and news articles may be used to learn where to look, never cited as the source of a rule. AI-rule trackers in particular go stale silently and are widely copied from each other.
- Quote operative language verbatim. A paraphrase cannot be filed.
- Record the negative as a finding. "No provision at this layer, confirmed against the current edition on [date]" is a usable answer. A blank cell is not.
- Anything unfetchable goes in an unverified list below the table, with where it was reported. Never promote it into a row.
- For every rule, state what silence or inaction means.
- Watch for supersession — replaced, withdrawn, or left posted after the judge stopped sitting.

## The four layers, in this order, every time

1. **National or statutory.** The federal rules of appellate, civil, criminal or evidence procedure, or the state equivalents, and any statute. Catch proposals too, and label the posture exactly: published for comment, approved, transmitted, effective. A proposal is not a rule and must never be tabled as one.
2. **Court-wide.** The circuit's or district's own local rules and general orders.
3. **The judge.** Standing order, individual practices, required certificate forms, from the judge's own current page — not a tracker, a memo, or a conference deck.
4. **The room next door.** The clerk's posted procedures, county or district local rules for state filings, and state bar ethics opinions where conduct is in issue.

Search each layer's rule text for: artificial intelligence, generative, large language model, ChatGPT, machine-generated, certification, disclosure, verification. Then read around every hit rather than trusting the count. Also check whether a bankruptcy court within the same district has its own order — it frequently does, and it is missed because it is not where anyone looks.

## Four traps, checked out loud

**The order everyone knows has been superseded.** The most-cited AI standing orders are the likeliest to be out of date, because everyone learned them at the same moment and few went back. Ask whether a court-wide rule has swallowed a judge's order, whether the order was withdrawn, and whether it is still posted after the judge stopped sitting.

**Silence means three different things and the table must say which.** Under some orders a filing that says nothing about AI is facially non-compliant. Under others, saying nothing is itself a representation that no AI was used. Where there is no provision at all, silence makes no representation. These are not variations on one rule; they are three different exposures.

**Disclosure is not certification is not prohibition.** Some rules require a statement that AI was used, some require certification that every citation was verified by a human, some restrict use outright, and some do two of the three. Table what the rule actually requires, in its own words, rather than the category it gets filed under.

**A proposal is not a rule, and a tracker is not a court.** Both errors produce a confident row that cannot be filed under. Label posture, and cite the issuing court's own page.

## Output: two tables, withdrawn first

**Withdrawn and modified rules come before the live ones.** The most common way to be wrong about AI rules is not missing a new one; it is filing under an old one. Include withdrawn, superseded, declined, lapsed with the judge, still posted but the judge no longer sits, and pending but not yet in force — and say which each one is.

**Then the live rules**, in the columns the user chose: jurisdiction and/or judge first, the chosen fields next, link to the rule text last.

- Source of authority is never just "rule." Say which: statute, national rule, adopted local rule, general order, judge standing order, individual practices, clerk's procedure, ethics opinion, proposal declined, proposal pending. They carry different force and different amendment paths, and flattening them is worse than no table.
- The summary must say what silence means.
- Every row gets a working link. A row without one is not a row.
- Unfetched material goes below the tables, marked reported but unverified, with where it was reported.

**Put the run date on the face of the table.** "Run [date]. Every row fetched that day from the issuing court's own domain." A compilation of AI rules with no run date tells the reader it is current when nobody knows whether it is.

## Versioning and re-runs

This field moves faster than the file does, and the second run is only useful if it shows what changed.

- Never overwrite — not the file, not a row, not a date. Every material change is a new dated file.
- One file is the file of record and its name says so. If someone opening the folder cannot tell which is current, the naming has already failed.
- Nothing is deleted. Superseded versions are archived, not removed.
- Once a folder holds three or more versions of the same document, move every version but the current one into an archive subfolder, keeping their full original names — the names carry the change history. If it is unclear which is current, move nothing and ask.
- A rename does not start a new family, and different formats are siblings rather than versions.
- A live value gets updated; a recorded event does not. A row stating what the rule is today will change. A note stating what the rule was on a given date never changes, because it describes something that happened rather than asserting something that is true now.
- On a re-run, diff it. Compare row by row against the prior run and report what moved: rules added, rules withdrawn, effective dates changed, judges reassigned. The diff is the product. Anyone can produce a list; the value is knowing what stopped being true.

## Verify at the destination

If the table was saved somewhere, confirm it arrived: the rows are present, the links resolve, and the run date is on it. A tool reporting success only means its command ran. If it could not be saved, deliver the table in full, give the filename to save it under, and hand over the versioning rules rather than skipping them.

## Out of scope

This does not give advice; it reports what a court has published. It cannot see chambers preferences, which are unpublished and bind anyway — call the clerk on the assigned judge the week of filing. Absence is never proven, only confirmed against the current published edition on a date, and the table must say it in those words. It is run by the person filing, on their matter, the week they file, which is the only thing that makes it current.
