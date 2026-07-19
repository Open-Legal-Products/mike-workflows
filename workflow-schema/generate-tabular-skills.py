#!/usr/bin/env python3

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path(__file__).with_name("tabular-review-instructions.md")

match = re.search(r"```markdown\n(.*?)\n```", SOURCE.read_text(), re.DOTALL)
if not match:
    raise SystemExit("Canonical tabular instruction block not found")

canonical = match.group(1)
files = sorted(
    set((ROOT / "tabular-review-workflows").glob("*/SKILL.md"))
    | set((ROOT / "tabular-review-workflows").glob("*-pack/*/SKILL.md"))
)
pattern = re.compile(r"## Instructions\n.*?(?=\n## [^\n]+\n|\Z)", re.DOTALL)

for file in files:
    text = file.read_text()
    if not pattern.search(text):
        raise SystemExit(f"Instructions section not found: {file}")
    file.write_text(pattern.sub(canonical, text, count=1))

print(f"Generated canonical instructions for {len(files)} tabular skills.")
