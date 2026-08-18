---
name: "verity-the-hallucination-audit"
description: "Detect fabricated cases, fabricated or altered quotations, and inaccurate parentheticals in a filing, using Westlaw-delivered opinions as ground truth rather than model recall. Runs in sequential rounds with an attorney approval gate after each, matches quotations by script rather than by reading, and produces one growing colour-coded deliverable sorted by severity. Use before signing or filing any brief or motion whose citations have not been mechanically verified."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Lee Czocher"
  language: "English"
  mike-display-name: "Verity: the Hallucination Audit"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Litigation"
  jurisdictions: "United States"
---

# Verity: the Hallucination Audit

Check a filing's citations against the opinions themselves — existence, quotation, characterization. Not style. The fingerprint a drafting tool leaves is not how a brief sounds; it is whether the authorities hold when you pull on them.

⛔ **Ground truth is delivered, not remembered.** Never verify a citation or a quotation from model knowledge — that is the exact failure this audit exists to catch. Extract, then compare against the full text of the delivered opinions by script: exact match first, then normalized fuzzy match. Judgment is spent on the exception queue only, never on reading whole opinions per quote.

**Requires a Westlaw subscription.** The attorney's only manual step is a five-minute bulk download.

## Setup

Create a matter folder named for the filing. Inside it: an `opinions` folder, a working folder for JSON state and converted text that the attorney never needs to open, and the deliverable at the top level — the only file they should ever have to open.

## Round 0 — Intake

Extract every citation by pattern-matching the filing's full text, **body and footnotes, not just the table of authorities** — body-only cites are the classic gap. Dedupe.

Hand back a pull list for Westlaw: **bare reporter cites only, one per line** (`411 U.S. 138`), never full Bluebook form — case names break the bulk-retrieval parser. Ship it as one-click copy-paste, with the retrieval page linked beside it.

When the download is saved, unpack it into `opinions` and **count-check delivered files against the request list.** A silent retrieval miss has to surface here, not in Round 2.

## Round 1 — Existence

Compare each delivered file's name to the cited case name. No content parsing: Westlaw returns whatever opinion actually occupies that volume and page, so a mismatched filename is itself the finding.

Table it: the cited case with no corresponding opinion, the surrounding text in the filing, and the legal principle now needing replacement support. Also flag table-of-authorities-versus-body discrepancies — years, first pages, party names — and harvest negative-treatment flags from the delivered files' headers. Both are free signal at this stage.

## Round 2 — Quote accuracy

Convert the delivered opinions to text and match every quotation by script.

Normalize what causes false alarms: smart versus straight quotes, hyphenation and dashes, star-pagination markers. Segment quotes on ellipses and bracketed alterations and match segments independently. Track `Id.` chains and cite-then-quote attribution order. Quotations of record documents, statutes and regulations are out of scope — filter them by context.

⚠ **On a low match score, search the whole corpus before flagging.** A real quote attributed to the wrong case is a proofing note, not a fabrication, and keeping those categories apart is what keeps the red rows credible.

Severity tiers:

1. **Tier 1** — the quote appears nowhere in the cited opinion or the corpus, or the opinion is missing. Fabricated or unverifiable.
2. **Tier 2** — unmarked or misleading alteration: deleted hedge words, unbracketed insertions, uncredited cleanup.
3. **Tier 3** — verbatim-level proofing noise.

Bring only the script's exceptions to the attorney, in batches of about five, and record each ruling in the working files.

## Round 3 — Parentheticals and characterizations

Extract every explanatory parenthetical and cite-adjacent characterization with its signal — held that, see, see e.g., cf. — skipping court-year parentheticals. Screen in this order:

1. **Headnote screen.** No match against the delivered opinion's headnotes earns the terminal label *no obvious match in headnotes*, and no further investigation. Diagnosis is a different job.
2. **Binary-facts screen.** Only objectively verifiable items: claimed disposition versus actual, pincite within the opinion's page range, party posture.
3. **Judgment queue.** Everything surviving, where accuracy is a lawyer's call.

⛔ **No recommendations in the judgment queue.** Present items one at a time: the opinion's actual language, the parenthetical as filed, and a terse statement of the gap. Nothing else unless expressly asked. The ruling options are Flag, Mark for further research, or Pass — there is no gray option, because the queue *is* the gray zone.

Log every ruling and the principle the attorney states with it to a running precedents file, and consult it before escalating later items. A pattern already ruled on should not be asked again. Severity presumption scales with the signal: *held that* claims more than *cf.*

## Gates

The rounds are strictly sequential. A round closes only when the deliverable has been regenerated with that round's section and presented, **and** the attorney has explicitly approved proceeding.

⛔ Do not begin any next-round work, even cheap extraction, before the gate clears — even if the round found nothing. Each round's output is the next round's input, so an error that slips a gate contaminates everything downstream.

If told to run straight through, confirm once and skip the approval stops. **The per-round deliverable versions are not waivable.**

## Deliverable

One landscape document that grows a section per round. Rows sorted by severity and colour-coded: red for fabricated or flagged, amber for an alteration or a terminal label, white for a pass.

Regenerate it each round from the structured working files on disk, **never from chat recall**. Save every material update as a new versioned file — never overwrite — with the round and the scope of the update in the filename. The in-chat record and the on-disk record are parallel checkpoint trails; either should survive the loss of the other.

## Handoff

After Round 3, validate the final deliverable — every table row traces to a working-file entry, section counts match the tables — then present it with a compact findings summary.

## Order matters, and it is the cost design

Filename existence checks cost almost nothing and catch the worst errors before a single quote match is spent on a case that does not exist. Scripted matching disposes of the volume. Only the residue reaches the judgment rounds. Running these out of order works and wastes most of the budget.

## Out of scope

Style, voice and argument. This checks facts — existence, quotation, characterization — and touches nothing else. Replacement-authority research and argument-level review are separate engagements.

It is a discipline, not a delegation: the pipeline narrows and organizes, and a licensed attorney resolves. It does not replace the duty of candor, the signature, or reading the cases relied on.
