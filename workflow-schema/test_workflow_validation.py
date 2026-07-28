import tempfile
import unittest
import zipfile
from pathlib import Path

from workflow_validation import docx_assets, docx_references, validate_docx


def write_docx(path, members=None):
    members = members or {
        "[Content_Types].xml": b"<Types/>",
        "word/document.xml": b"<document/>",
    }
    with zipfile.ZipFile(path, "w") as archive:
        for name, contents in members.items():
            archive.writestr(name, contents)


class DocxReferenceTests(unittest.TestCase):
    def test_finds_flexible_inline_code_and_link_paths(self):
        markdown = """
Use `assets/Client template (中文).DOCX`.
Or use [the alternate](<assets/Another template.docx>).
Or use [the encoded alternate](assets/Encoded%20template.docx).
"""
        self.assertEqual(
            docx_references(markdown),
            {
                "assets/Client template (中文).DOCX",
                "assets/Another template.docx",
                "assets/Encoded template.docx",
            },
        )

    def test_ignores_plain_text_fenced_code_and_comments(self):
        markdown = """
The path assets/plain-text.docx is only an example.
```markdown
`assets/fenced.docx`
```
<!-- `assets/commented.docx` -->
"""
        self.assertEqual(docx_references(markdown), set())

    def test_preserves_invalid_traversal_for_caller_validation(self):
        self.assertEqual(
            docx_references("Use `assets/../outside.docx`."),
            {"assets/../outside.docx"},
        )


class DocxAssetTests(unittest.TestCase):
    def test_discovers_extensions_case_insensitively(self):
        with tempfile.TemporaryDirectory() as directory:
            assets = Path(directory) / "assets"
            assets.mkdir()
            write_docx(assets / "template.DOCX")
            self.assertEqual(docx_assets(directory), [assets / "template.DOCX"])

    def test_accepts_valid_docx_package(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.docx"
            write_docx(path)
            self.assertIsNone(validate_docx(path))

    def test_rejects_non_zip_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fake.docx"
            path.write_text("not a DOCX")
            self.assertIn("invalid OOXML ZIP package", validate_docx(path))

    def test_rejects_missing_required_member(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "incomplete.docx"
            write_docx(path, {"[Content_Types].xml": b"<Types/>"})
            self.assertIn("word/document.xml", validate_docx(path))


if __name__ == "__main__":
    unittest.main()
