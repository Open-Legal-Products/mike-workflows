#!/usr/bin/env python3

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
FORMATS = {"text", "date", "monetary_amount", "percentage", "bulleted_list", "yes_no", "tag"}
SKILL_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
METADATA_KEYS = {
    "version", "author", "language", "mike-display-name", "mike-type",
    "mike-availability", "practice", "jurisdictions",
}
PACK_KEYS = {
    "$schema", "id", "title", "description", "publisher", "license", "version",
    "practice", "jurisdiction", "source", "workflows", "required_connectors",
}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?$")
PROHIBITED_SKILL_PATTERNS = {
    re.compile(r"\bgenerate_docx\b", re.I): "named generate_docx tool",
    re.compile(r"\bsection object\b", re.I): "section-object implementation detail",
    re.compile(r"\btable field\b", re.I): "table-field implementation detail",
    re.compile(r"according to the host system", re.I): "host-system-specific output instruction",
    re.compile(r"```(?:bash|sh|shell|zsh|powershell)", re.I): "CLI command block",
    re.compile(r"\b(?:codex|claude|chatgpt)\s+[a-z-]+", re.I): "harness-specific command",
}

errors = []


def load_yaml(file):
    try:
        return yaml.safe_load(file.read_text())
    except yaml.YAMLError as error:
        errors.append(f"{file}: invalid YAML: {str(error).splitlines()[0]}")
        return None


def display_slug(value):
    return re.sub(r"(^-|-$)", "", re.sub(r"[^a-z0-9]+", "-", str(value).lower()))


def unique_sorted(paths):
    return sorted(set(paths))


schema_dir = Path(__file__).resolve().parent
canonical_source = (schema_dir / "tabular-review-instructions.md").read_text()
canonical_match = re.search(r"```markdown\n(.*?)\n```", canonical_source, re.DOTALL)
if not canonical_match:
    raise SystemExit("Canonical tabular instruction block not found")
canonical_instructions = canonical_match.group(1)

for file in schema_dir.glob("*.schema.yaml"):
    load_yaml(file)

skill_files = unique_sorted(
    list((ROOT / "assistant-workflows").glob("*/SKILL.md"))
    + list((ROOT / "assistant-workflows").glob("*-pack/*/SKILL.md"))
    + list((ROOT / "tabular-review-workflows").glob("*/SKILL.md"))
    + list((ROOT / "tabular-review-workflows").glob("*-pack/*/SKILL.md"))
)

frontmatter_pattern = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)

for file in skill_files:
    text = file.read_text()
    frontmatter = frontmatter_pattern.match(text)
    if not frontmatter:
        errors.append(f"{file}: missing YAML frontmatter")
        continue

    try:
        data = yaml.safe_load(frontmatter.group(1))
    except yaml.YAMLError as error:
        errors.append(f"{file}: invalid frontmatter: {str(error).splitlines()[0]}")
        continue

    if not isinstance(data, dict):
        errors.append(f"{file}: frontmatter must be a map")
        continue

    unknown_keys = set(data) - SKILL_KEYS
    if unknown_keys:
        errors.append(f"{file}: unsupported top-level fields: {', '.join(sorted(unknown_keys))}")

    name = str(data.get("name", ""))
    folder = file.parent.name
    if name != folder:
        errors.append(f"{file}: name must match its folder")
    if not 1 <= len(name) <= 64 or not NAME_PATTERN.fullmatch(name):
        errors.append(f"{file}: invalid name")

    description = str(data.get("description", ""))
    if not 1 <= len(description) <= 1024:
        errors.append(f"{file}: description must be 1-1024 characters")
    if description.endswith("..."):
        errors.append(f"{file}: description appears truncated")
    if not isinstance(data.get("license"), str) or not data["license"]:
        errors.append(f"{file}: license must be a non-empty string")

    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        errors.append(f"{file}: metadata must be a map")
        continue

    missing_metadata = METADATA_KEYS - set(metadata)
    if missing_metadata:
        errors.append(f"{file}: missing metadata: {', '.join(sorted(missing_metadata))}")
    if not all(isinstance(value, str) for value in metadata.values()):
        errors.append(f"{file}: metadata values must be strings")

    if folder != display_slug(metadata.get("mike-display-name", "")):
        errors.append(f"{file}: folder must match mike-display-name")
    if not SEMVER_PATTERN.fullmatch(str(metadata.get("version", ""))):
        errors.append(f"{file}: version must use semantic versioning")
    if metadata.get("mike-availability") not in {"system", "add-on"}:
        errors.append(f"{file}: mike-availability must be system or add-on")

    expected_type = "assistant" if "assistant-workflows" in file.parts else "tabular"
    if metadata.get("mike-type") != expected_type:
        errors.append(f"{file}: mike-type must be {expected_type}")

    if file.parent.parent.name.endswith("-pack") and metadata.get("mike-availability") != "add-on":
        errors.append(f"{file}: workflows inside packs must use mike-availability add-on")

    if expected_type == "tabular":
        if canonical_instructions not in text:
            errors.append(f"{file}: instructions are not synchronized with the canonical block")
        if not (file.parent / "table-columns.yaml").is_file():
            errors.append(f"{file}: missing table-columns.yaml")

    body = frontmatter_pattern.sub("", text, count=1)
    for pattern, label in PROHIBITED_SKILL_PATTERNS.items():
        if pattern.search(body):
            errors.append(f"{file}: contains {label}")

column_files = unique_sorted(
    list((ROOT / "tabular-review-workflows").glob("*/table-columns.yaml"))
    + list((ROOT / "tabular-review-workflows").glob("*-pack/*/table-columns.yaml"))
)

for file in column_files:
    data = load_yaml(file)
    if not isinstance(data, dict):
        continue

    unknown_keys = set(data) - {"$schema", "columns"}
    if unknown_keys:
        errors.append(f"{file}: unsupported root fields: {', '.join(sorted(unknown_keys))}")

    schema_ref = data.get("$schema")
    schema_file = (file.parent / schema_ref).resolve() if isinstance(schema_ref, str) else None
    if not schema_file or not schema_file.is_file() or schema_file.name != "table-columns.schema.yaml":
        errors.append(f"{file}: $schema must resolve to table-columns.schema.yaml")

    columns = data.get("columns")
    if not isinstance(columns, list) or not columns:
        errors.append(f"{file}: columns must be a non-empty array")
        continue

    indexes = [column.get("index") if isinstance(column, dict) else None for column in columns]
    if indexes != list(range(len(columns))):
        errors.append(f"{file}: indexes must be contiguous from 0")

    names = [column.get("name") if isinstance(column, dict) else None for column in columns]
    if len(set(names)) != len(names):
        errors.append(f"{file}: column names must be unique")

    for column in columns:
        if not isinstance(column, dict):
            errors.append(f"{file}: every column must be a map")
            continue

        unknown_column_keys = set(column) - {"index", "name", "format", "tags", "prompt"}
        if unknown_column_keys:
            errors.append(f"{file}: unsupported column fields: {', '.join(sorted(unknown_column_keys))}")

        label = column.get("name") or f"index {column.get('index')}"
        if not isinstance(column.get("name"), str) or not column["name"]:
            errors.append(f"{file}: {label} must have a non-empty name")
        if not isinstance(column.get("prompt"), str) or not column["prompt"]:
            errors.append(f"{file}: {label} must have a non-empty prompt")

        column_format = column.get("format")
        if column_format not in FORMATS:
            errors.append(f"{file}: {label} has an unsupported format")

        tags = column.get("tags")
        if column_format == "tag":
            valid_tags = (
                isinstance(tags, list) and bool(tags)
                and all(isinstance(tag, str) and tag for tag in tags)
                and len(set(tags)) == len(tags)
            )
            if not valid_tags:
                errors.append(f"{file}: {label} must have unique, non-empty tags")
        elif tags is not None:
            errors.append(f"{file}: {label} may only define tags when format is tag")

pack_files = unique_sorted(
    list((ROOT / "assistant-workflows").glob("*-pack/pack.yaml"))
    + list((ROOT / "tabular-review-workflows").glob("*-pack/pack.yaml"))
)
pack_folders = unique_sorted(
    list((ROOT / "assistant-workflows").glob("*-pack"))
    + list((ROOT / "tabular-review-workflows").glob("*-pack"))
)

for folder in pack_folders:
    if folder.is_dir() and not (folder / "pack.yaml").is_file():
        errors.append(f"{folder}: missing pack.yaml")

for file in pack_files:
    data = load_yaml(file)
    if not isinstance(data, dict):
        continue

    required = {"id", "title", "description", "publisher", "license", "version", "workflows"}
    missing = required - set(data)
    if missing:
        errors.append(f"{file}: missing fields: {', '.join(sorted(missing))}")

    unknown_keys = set(data) - PACK_KEYS
    if unknown_keys:
        errors.append(f"{file}: unsupported fields: {', '.join(sorted(unknown_keys))}")

    folder = file.parent
    expected_id = folder.name.removesuffix("-pack")
    pack_id = str(data.get("id", ""))
    if data.get("id") != expected_id:
        errors.append(f"{file}: id must match the pack folder")
    if not 1 <= len(pack_id) <= 64 or not NAME_PATTERN.fullmatch(pack_id):
        errors.append(f"{file}: invalid id")
    if not SEMVER_PATTERN.fullmatch(str(data.get("version", ""))):
        errors.append(f"{file}: version must use semantic versioning")

    for field in ("practice", "jurisdiction"):
        if field in data and (not isinstance(data[field], str) or not data[field]):
            errors.append(f"{file}: {field} must be a non-empty string")

    schema_ref = data.get("$schema")
    schema_file = (folder / schema_ref).resolve() if isinstance(schema_ref, str) else None
    if not schema_file or not schema_file.is_file() or schema_file.name != "pack.schema.yaml":
        errors.append(f"{file}: $schema must resolve to pack.schema.yaml")

    workflows = data.get("workflows")
    if not isinstance(workflows, list) or not workflows or len(set(workflows)) != len(workflows):
        errors.append(f"{file}: workflows must be a unique, non-empty array")
        continue

    actual = sorted(path.parent.name for path in folder.glob("*/SKILL.md"))
    if sorted(workflows) != actual:
        errors.append(f"{file}: manifest workflows must match its child workflow folders")

if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)

print(f"Validated {len(skill_files)} workflows, {len(column_files)} column files, and {len(pack_files)} packs.")
