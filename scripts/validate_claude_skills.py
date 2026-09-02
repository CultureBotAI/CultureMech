#!/usr/bin/env python3
"""Validate repository Claude skill layout, metadata, and local references."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".claude" / "skills"
REQUIRED_FRONTMATTER = {"name", "description"}
LOCAL_REFERENCE = re.compile(
    r"`((?:scripts|src|docs|conf|\.claude)/[^`\s]+|(?:README|NEXT_TASKS|project\.justfile)[^`\s]*)`"
)


def frontmatter(path: Path) -> dict:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    try:
        _, header, _ = text.split("---", 2)
    except ValueError as error:
        raise ValueError("unterminated YAML frontmatter") from error
    value = yaml.safe_load(header)
    if not isinstance(value, dict):
        raise ValueError("frontmatter must be a mapping")
    return value


def normalize_reference(raw: str) -> str | None:
    value = raw.rstrip(".,:;)")
    value = value.split(":", 1)[0] if re.search(r":(?:\d+|[A-Za-z_]+)$", value) else value
    if any(token in value for token in ("*", "{", "}", "<", ">", "[", "]", "$")):
        return None
    return value


def validate_skills() -> list[str]:
    errors: list[str] = []
    loose_markdown = sorted(SKILLS_DIR.glob("*.md"))
    for path in loose_markdown:
        errors.append(f"{path.relative_to(ROOT)}: use <skill>/SKILL.md layout")

    for directory in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{directory.relative_to(ROOT)}: missing SKILL.md")
            continue
        try:
            metadata = frontmatter(skill_file)
        except ValueError as error:
            errors.append(f"{skill_file.relative_to(ROOT)}: {error}")
            continue
        missing = sorted(REQUIRED_FRONTMATTER - metadata.keys())
        if missing:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing {', '.join(missing)}")
        nested_metadata = metadata.get("metadata")
        nested_version = (
            nested_metadata.get("version") if isinstance(nested_metadata, dict) else None
        )
        if not metadata.get("version") and not nested_version:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing version")
        if metadata.get("name") != directory.name:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: name must match directory {directory.name!r}"
            )

        for document in directory.rglob("*.md"):
            for match in LOCAL_REFERENCE.finditer(document.read_text()):
                reference = normalize_reference(match.group(1))
                if reference and not (ROOT / reference).exists():
                    errors.append(f"{document.relative_to(ROOT)}: missing local path {reference}")
    return errors


def main() -> int:
    errors = validate_skills()
    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1
    count = len(list(SKILLS_DIR.glob("*/SKILL.md")))
    print(f"validated {count} Claude skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
