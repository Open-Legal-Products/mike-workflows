---
name: "draft-from-template"
description: "Edit a copy of an uploaded template using the user's instructions and source materials while preserving the original file."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "Draft from Template"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "General Transactions"
  jurisdictions: "General"
---
# Draft from Template

## Instructions

If the user has not provided a template file, ask them to upload one.

Use an available file-copy tool call to create a copy of the uploaded template,
then edit that copy directly. Do not recreate the file from its extracted text,
and never modify the original template. Preserve the copied file's format,
layout, styles, numbering, section order, clause structure, and other content
unless the user asks for a change.

Replace placeholders and template text using the user's instructions and any
supporting materials. Keep definitions, cross-references, names, dates,
schedules, and exhibits internally consistent. Do not invent missing facts; ask
for essential information or leave a clear placeholder where appropriate.

Return the completed copy in the same file format as the uploaded template.
