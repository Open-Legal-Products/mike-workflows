# Mike Legal Workflows

Public workflow definitions for Mike. We are open sourcing the workflows
available in Mike so that people can contribute improvements and use them with
the agent harness of their choice. The workflows follow the
[`SKILL.md` Agent Skills specification](https://agentskills.io/specification)
used by popular agent harnesses, making them straightforward to adapt and reuse.

The repository has two top-level workflow collections:

- `assistant-workflows/` contains assistant workflows.
- `tabular-review-workflows/` contains tabular review workflows.

System and add-on workflows use the same simple folder structure. Their
availability is declared in `SKILL.md` rather than encoded through
additional directory nesting.

## Structure

```text
mike-legal-workflows/
  assistant-workflows/
    <workflow-id>/
      SKILL.md
    <pack-id>-pack/
      pack.yaml
      <workflow-id>/
        SKILL.md

  tabular-review-workflows/
    <workflow-id>/
      SKILL.md
      table-columns.yaml
    <pack-id>-pack/
      pack.yaml
      <workflow-id>/
        SKILL.md
        table-columns.yaml

  workflow-schema/
    workflow-metadata.schema.yaml
    table-columns.schema.yaml
    pack.schema.yaml
    tabular-review-instructions.md
    generate-tabular-skills.py
    validate-workflows.py
```

Ordinary workflow folders are kept flat directly under the appropriate
top-level collection. Only workflows that belong to a pack are nested inside
their pack folder.

## Authoring Principles

Keep skills lightweight and focused instead of making them overly complicated.
Models are increasingly capable of handling general reasoning on their own, so
skill instructions should provide only the workflow-specific context,
constraints, and steps needed to produce a reliable result. Avoid unnecessary
explanation, repetition, and prescriptive detail to keep workflows
token-efficient.

Skills should not include CLI commands or commands specific to any particular
agent harness. Describe the intended action in harness-neutral language so the
workflow remains portable across compatible environments.

## System and Add-on Workflows

Every `SKILL.md` declares a `mike-availability` value inside its YAML
frontmatter metadata:

```yaml
metadata:
  mike-availability: "system"
```

Use `system` for trusted workflows that ship with Mike and appear as
non-editable system workflows. Use `add-on` for workflows that users can
optionally install or copy into their own workspace:

```yaml
metadata:
  mike-availability: "add-on"
```

This explicit metadata is the source of truth. Folder names should describe
what a workflow does, not how it is distributed.

## Workflow Types

### Assistant Workflows

Assistant workflows contain metadata in `SKILL.md` YAML frontmatter and
instructions in the Markdown body.

Assistant workflows can prompt users for additional information or document
uploads when needed. For example, a drafting workflow can ask the user to
provide a template or precedent before continuing. Mike supports these
interactive requests as part of the workflow.

### Tabular Review Workflows

Tabular review workflows contain metadata in `SKILL.md` YAML frontmatter,
workflow-level instructions in the Markdown body, and column definitions in
`table-columns.yaml`.

Mike does not currently use the instructions in a tabular review workflow's
`SKILL.md` when running the workflow. Users trigger tabular review runs directly,
and Mike applies fixed system prompts together with the workflow's
`table-columns.yaml`. The results are rendered as an interactive table in the
Mike application UI rather than having an agent generate the presentation on
the fly.

The `SKILL.md` is included to describe the workflow and ensure that it remains
portable to other agent harnesses that use skill-based instructions. Outside
Mike, the skill instructs the agent to produce an exportable Excel file and to
fall back to a Markdown table when Excel output is unavailable.

The canonical baseline is maintained in
[`workflow-schema/tabular-review-instructions.md`](workflow-schema/tabular-review-instructions.md).
Every tabular review `SKILL.md` should include these instructions and may add
subject-specific guidance in a separate section where needed. After changing
the canonical baseline, regenerate the tabular skill instructions with:

```bash
python3 workflow-schema/generate-tabular-skills.py
```

The `mike-type` metadata field must agree with the top-level collection:

```yaml
metadata:
  mike-type: "assistant"
```

or:

```yaml
metadata:
  mike-type: "tabular"
```

## Packs

A pack is a named bundle of add-on workflows of the same type. Pack folders
live in the relevant workflow collection and must end in `-pack` so they are
easy for both people and Mike to identify.

```text
assistant-workflows/
  commercial-drafting-pack/
    pack.yaml
    draft-service-agreement/
      SKILL.md
    draft-nda/
      SKILL.md
```

The pack's `pack.yaml` lists its direct child workflow folders:

```yaml
$schema: "../../workflow-schema/pack.schema.yaml"
id: "commercial-drafting"
title: "Commercial Drafting"
description: "Add-on workflows for drafting commercial agreements."
publisher:
  name: "Mike"
license: "MIT"
version: "1.0.0"
practice: "General Transactions"
workflows:
  - "draft-service-agreement"
  - "draft-nda"
required_connectors: []
```

Packs may optionally declare a `practice`, a `jurisdiction`, or both to
describe the bundle. These values are non-empty strings when present.

Each listed directory must exist directly inside the pack folder, and each
workflow in a pack must declare `mike-availability: "add-on"` inside its
`metadata`. Packs should not contain system workflows. Installing a pack
installs all workflows listed in its manifest.

The pack `id` is immutable after publication and must match the pack folder name
without its `-pack` suffix. For example, `commercial-drafting-pack/` uses
`"id": "commercial-drafting"`.

Packs are type-specific: an assistant pack belongs in `assistant-workflows/`,
while a tabular review pack belongs in `tabular-review-workflows/`. This keeps
the repository flat and avoids another cross-cutting directory hierarchy.

## Skill Frontmatter

Each workflow has a `SKILL.md` file with YAML frontmatter followed by Markdown
instructions. To remain portable across compatible agent harnesses, the
frontmatter uses the standard Agent Skills fields. `name` and `description` are
required by the open specification; `license` and `metadata` are also required
for workflows in this repository.

Only fields whose meaning is specific to Mike use the `mike-` prefix. General
fields such as `version`, `author`, `language`, `practice`, and `jurisdictions`
remain unprefixed. Metadata values are strings for compatibility with the Agent
Skills specification. Use the author or publishing organisation's name for
`author`.

```yaml
---
name: "nda-review"
description: "Review an NDA and identify material legal and commercial issues."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Open Legal Products"
  language: "English"
  mike-display-name: "NDA Review"
  mike-type: "assistant"
  mike-availability: "system"
  practice: "General Transactions"
  jurisdictions: "General"
---
```

The workflow folder and the `name` field must both match the lowercase,
hyphenated form of `metadata.mike-display-name`. For example, a Mike display
name of `Credit Agreement Review` uses the folder
`credit-agreement-review/` and `name: "credit-agreement-review"`. Keep these
identifiers stable once published. Because the identifier is derived from the
display name, treat `mike-display-name` as immutable after publication. A
breaking rename requires an explicit migration or alias in the consuming
application.

## Reference Documents

Assistant workflows may bundle document templates and other reference
documents in the standard Agent Skills `assets/` directory:

```text
assistant-workflows/
  draft-service-agreement/
    SKILL.md
    assets/
      service-agreement-template.docx
```

Reference each document directly from the `SKILL.md` body using its relative
path:

```markdown
Use the bundled template at `assets/service-agreement-template.docx` as the
starting document.
```

Reference documents are currently supported only for assistant workflows.
Every bundled `.docx` file must be located under `assets/` and referenced by
`SKILL.md`; no additional metadata declaration is required.

Tabular review `table-columns.yaml` files use:

```yaml
$schema: "../../workflow-schema/table-columns.schema.yaml"
```

For a tabular workflow inside a pack, use:

```yaml
$schema: "../../../workflow-schema/table-columns.schema.yaml"
```

## Validation

Validate workflow metadata, canonical tabular instructions, column formats,
indexes, names, and tags with:

```bash
python3 workflow-schema/validate-workflows.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for authoring and validation rules,
[PROVENANCE.md](PROVENANCE.md) for third-party licensing requirements, and
[VERSIONING.md](VERSIONING.md) for workflow and pack versioning.

## License

MIT License. See [LICENSE](LICENSE).
