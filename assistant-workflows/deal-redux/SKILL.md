---
name: "deal-redux"
description: "Turn a counterparty's tracked-changes redline into the small number of negotiating positions it actually contains, and return that instead of a counter-redline. Use whenever a marked-up agreement arrives — an NDA, an MSA, a purchase agreement, any negotiated document — and especially when the markup is voluminous, heavily commented, or looks machine-generated. Produces a one-page position table with a conservation check proving no edit was dropped."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Lee Czocher"
  language: "English"
  mike-display-name: "Deal Redux"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "General Transactions"
  jurisdictions: "General"
---

# Deal Redux

A counterparty sends eighty-four edits. They contain six positions. Send back the six.

Generation is cheap and review is not, and that asymmetry is not fixed by reviewing faster. It is fixed by changing what goes back. Answering a generated redline with another redline doubles the volume that made the document expensive. A position list costs one pass to produce and costs the other side a decision on every line.

This workflow does not detect AI authorship and does not argue that AI was used. A redline that collapses from eighty-four edits to six positions was overproduced whoever made it.

## Input and output

In: a marked-up agreement with tracked changes, and any comments that came with it.

Out: one page. A table of positions ranked by consequence, each with its clause citations, its edit count, and an empty response column.

The response column stays empty. Report what the redline does; the lawyer decides what to do about it. Never fill that column, never suggest a fill, and never characterise a position as reasonable, aggressive, or market.

## Extract from the markup, not the rendered document

Reading the document in reading order is what makes volume feel like substance. Work from the underlying markup instead and pull every insertion, deletion, move, and formatting-only change, each with its author, its timestamp, and the nearest numbered clause. Pull comments separately and anchor each to the text it marks.

Formatting-only and paragraph-property-only changes inflate every raw count and belong in the cosmetic bucket without exception.

Do not use a comment to classify the change it sits on. The comment is the counterparty's characterisation of its own edit. Classify by what the edit does to the operative text.

## Classify by effect

Give every change exactly one category:

1. **Allocates risk** — indemnity, limitation of liability, warranty, IP ownership, insurance, termination rights, exclusivity.
2. **Moves a number or a period** — caps, baskets, thresholds, term, notice, cure, survival.
3. **Changes a definition's scope** — the highest-leverage and most-missed category, because one definitional edit reaches every clause using the term.
4. **Flips directionality** — one-way made mutual, or the reverse.
5. **Procedural** — notices, governing law, venue, assignment, counterparts, order of precedence.
6. **Cosmetic** — capitalisation, cross-references, renumbering, formatting.

Itemise the first four. Count the last two and say so in one line.

## Cluster into positions

A position is the smallest set of changes that must be accepted or rejected together. Test: if accepting one and rejecting another would leave the document incoherent, they are one position.

Converting a one-way agreement to mutual is one position however many clauses it touches. Narrowing a definition and its conforming changes is one position. Two unrelated cap reductions are two positions.

Rank by consequence, not by document order and not by edit count. A one-edit position can outrank a forty-edit one: the forty-edit mutual conversion may be boilerplate, and the single word inserted into the indemnity may be the deal.

## Return one table

Columns: position, what it changes in the operative text, clause references, edit count, effect if accepted, response.

- **Position** — a neutral noun phrase, not a characterisation.
- **Clause references** — on every row. A position without them is not checkable, and an uncheckable summary is the thing this replaces.
- **If accepted** — the effect on the operative text in one sentence. Effect, not risk, and not advice.
- **Response** — left blank.

Then three lines and no more: the cosmetic and mechanical count, the number of comments not reproduced, and the authors and date range of the changes as recorded in the file.

Quote a comment only where its words are themselves a position — a concession, an instruction, a commitment. Never paraphrase one into an argument.

## The conservation check

Every tracked change must land in exactly one position or exactly one of the two counted buckets. Print the arithmetic on the face of the output:

> 84 changes · 6 positions consuming 53 · 31 cosmetic · 0 unaccounted

If the unaccounted number is not zero, the reduction is not finished and does not go out.

This is the integrity of the whole thing. A compression whose value is that the reader can stop reading the document fails the first time something material was left out of it. Speed is not the product; completeness at a smaller size is the product.

## Report the ratio, do not argue it

Record edits per position at the top: 84 → 6. Do not editorialise. The number carries it, and a measurement can be sent to a counterparty where an accusation cannot.

## Second round

When the next markup arrives, run it again and report what moved: positions conceded, positions repeated, positions newly raised. A position repeated unchanged after it was answered is the most useful line in the second reduction.

## Out of scope

Do not advise. Do not fill the response column or propose fallback language. Do not accuse anyone of using AI. Do not open the document and read it in order — that is the failure this replaces. This workflow cannot see side letters, prior drafts, or what was agreed on a call, and those change which position matters most.
