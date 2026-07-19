# Versioning

Workflows and packs use semantic versioning: `MAJOR.MINOR.PATCH`.

## Workflow Versions

- **MAJOR**: incompatible output changes, renamed or removed fields, changed
  workflow identity, or materially different user-facing behavior.
- **MINOR**: backward-compatible capabilities, review topics, columns, or
  substantive instruction improvements.
- **PATCH**: corrections and clarifications that do not materially change the
  expected output or workflow behavior.

Increment the `metadata.version` value of every changed workflow. Do not change
the folder, `name`, or `mike-display-name` of a published workflow without an
explicit migration or alias in the consuming application.

## Pack Versions

Increment a pack version when its metadata or membership changes. Removing or
renaming a member is a major change; adding a member is a minor change; metadata
corrections are patch changes.

Schema versions are managed independently. A breaking schema change requires a
migration plan for all affected workflows and packs.
