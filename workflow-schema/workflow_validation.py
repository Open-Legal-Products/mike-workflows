import re
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import unquote


INLINE_CODE_PATTERN = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
FENCED_CODE_BLOCK_PATTERN = re.compile(
    r"(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*(?:\n|\Z)"
)
HTML_COMMENT_PATTERN = re.compile(r"<!--.*?-->", re.DOTALL)
REQUIRED_DOCX_MEMBERS = {"[Content_Types].xml", "word/document.xml"}


def _markdown_link_destinations(text):
    """Yield destinations from inline Markdown links and images."""
    position = 0
    while True:
        opening = text.find("](", position)
        if opening == -1:
            return

        cursor = opening + 2
        while cursor < len(text) and text[cursor] in " \t":
            cursor += 1

        if cursor < len(text) and text[cursor] == "<":
            cursor += 1
            destination_start = cursor
            while cursor < len(text):
                if text[cursor] == ">" and text[cursor - 1] != "\\":
                    yield text[destination_start:cursor]
                    position = cursor + 1
                    break
                cursor += 1
            else:
                position = opening + 2
            continue

        destination_start = cursor
        nesting = 0
        escaped = False
        while cursor < len(text):
            character = text[cursor]
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == "(":
                nesting += 1
            elif character == ")":
                if nesting == 0:
                    yield text[destination_start:cursor]
                    position = cursor + 1
                    break
                nesting -= 1
            elif character in " \t\n" and nesting == 0:
                # A bare link destination ends before an optional title.
                yield text[destination_start:cursor]
                position = cursor + 1
                break
            cursor += 1
        else:
            position = opening + 2


def _normalize_docx_reference(value, *, decode_url=False):
    reference = unquote(value) if decode_url else value
    reference = re.sub(r"\\([\\()`])", r"\1", reference.strip())
    path = PurePosixPath(reference)
    if (
        len(path.parts) >= 2
        and path.parts[0] == "assets"
        and path.suffix.lower() == ".docx"
    ):
        return reference
    return None


def docx_references(markdown):
    """Return DOCX asset paths referenced by Markdown links or inline code."""
    searchable = HTML_COMMENT_PATTERN.sub("", markdown)
    searchable = FENCED_CODE_BLOCK_PATTERN.sub("", searchable)

    references = set()
    for match in INLINE_CODE_PATTERN.finditer(searchable):
        reference = _normalize_docx_reference(match.group(1))
        if reference:
            references.add(reference)

    for destination in _markdown_link_destinations(searchable):
        reference = _normalize_docx_reference(destination, decode_url=True)
        if reference:
            references.add(reference)

    return references


def docx_assets(workflow_directory):
    """Return DOCX files under assets/, matching the extension case-insensitively."""
    assets_directory = Path(workflow_directory) / "assets"
    if not assets_directory.is_dir():
        return []
    return sorted(
        path for path in assets_directory.rglob("*")
        if path.is_file() and path.suffix.lower() == ".docx"
    )


def validate_docx(path):
    """Return an error message when path is not a minimally valid DOCX package."""
    try:
        with zipfile.ZipFile(path) as archive:
            members = set(archive.namelist())
            missing = sorted(REQUIRED_DOCX_MEMBERS - members)
            if missing:
                return f"missing required package member(s): {', '.join(missing)}"
            corrupt_member = archive.testzip()
            if corrupt_member:
                return f"corrupt package member: {corrupt_member}"
    except (OSError, RuntimeError, zipfile.BadZipFile) as error:
        return f"invalid OOXML ZIP package: {error}"
    return None
