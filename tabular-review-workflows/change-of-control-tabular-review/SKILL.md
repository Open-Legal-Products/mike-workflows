---
name: "change-of-control-tabular-review"
description: "This workflow performs a change of control due diligence review across the selected documents."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "Change of Control Tabular Review"
  mike-type: "tabular"
  mike-availability: "system"
  practice: "Corporate"
  jurisdictions: "General"
---
# Change of Control Tabular Review

## Purpose

Use this workflow to review uploaded documents for change of control provisions and extract structured diligence findings into the columns defined in `table-columns.yaml`.

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Change of Control Guidance

- Capture the exact triggering language and summarize its practical effect in plain English.
- For consent, termination, option, and financial-consequence provisions, identify who holds the right or obligation, when it is triggered, and any timing or procedural requirements.
- Do not infer a change-of-control restriction from general assignment, transfer, merger, or affiliate provisions unless the document text supports that connection.

