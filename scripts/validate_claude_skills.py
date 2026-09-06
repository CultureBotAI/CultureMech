#!/usr/bin/env python3
"""Validate repository Claude skill layout, metadata, and local references.

A local path named in a skill is checked against **git**, not the filesystem
(#419). The filesystem is the wrong oracle in both directions: a generated
artifact such as `app/data.js` exists on a machine that has built the pages
and is absent on a fresh clone, and macOS resolves `TSB.yaml` to the tracked
`tsb.yaml` while Linux CI does not. So a reference passes when it is either

* **tracked** -- a file or directory `git ls-files` knows about, or
* **generated** -- ignored by `.gitignore`, or a directory whose contents an
  ignore pattern declares (`data/raw_yaml/**/*.yaml` declares `data/raw_yaml/`).

Anything else is reported as missing. Paths in a sibling checkout are written
with the repository name first (`MediaIngredientMech/templates/...`) or with a
placeholder root (`<kg-microbe>/data/...`), and are not checked here.
"""

from __future__ import annotations

import re
import subprocess
from functools import cache
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".claude" / "skills"
REQUIRED_FRONTMATTER = {"name", "description"}

# Top-level directories a skill may name as a local path. Anything outside this
# list is treated as prose, so keep it to directories the repository actually
# has; a new top-level directory should be added here when a skill first cites it.
LOCAL_PREFIXES = (
    "scripts",
    "src",
    "docs",
    "conf",
    "data",
    "app",
    "pages",
    "tests",
    "templates",
    "history",
    "output",
    "reports",
    "curation",
    "research",
    ".claude",
    ".github",
)
LOCAL_FILES = ("README", "NEXT_TASKS", "CLAUDE", "project.justfile", "pyproject.toml")
_PREFIX_ALTERNATION = "|".join(re.escape(prefix) for prefix in LOCAL_PREFIXES)
_FILE_ALTERNATION = "|".join(re.escape(name) for name in LOCAL_FILES)
LOCAL_REFERENCE = re.compile(
    rf"`((?:{_PREFIX_ALTERNATION})/[^`\s]+|(?:{_FILE_ALTERNATION})[^`\s]*)`"
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


class NotAGitCheckout(RuntimeError):
    """The validator needs git to answer "is this path tracked or generated"."""


@cache
def _tracked_paths(root: Path) -> frozenset[str]:
    """Every tracked file, plus every directory that contains one."""
    try:
        completed = subprocess.run(
            ["git", "ls-files", "-z"], cwd=root, capture_output=True, text=True, check=True
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise NotAGitCheckout(
            f"{root} is not a git checkout (or git is not installed); local path "
            f"references can only be validated against git"
        ) from error
    listing = completed.stdout
    paths: set[str] = set()
    for entry in listing.split("\0"):
        if not entry:
            continue
        paths.add(entry)
        paths.update(str(parent) for parent in Path(entry).parents if str(parent) != ".")
    return frozenset(paths)


@cache
def _ignore_patterns(root: Path) -> tuple[str, ...]:
    """Positive patterns from the repository `.gitignore`, without a leading slash."""
    ignore_file = root / ".gitignore"
    if not ignore_file.is_file():
        return ()
    patterns = []
    for line in ignore_file.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        patterns.append(line.lstrip("/"))
    return tuple(patterns)


def _is_ignored(root: Path, reference: str) -> bool:
    result = subprocess.run(
        ["git", "check-ignore", "-q", "--no-index", reference], cwd=root, capture_output=True
    )
    return result.returncode == 0


def classify_reference(reference: str, root: Path | None = None) -> str:
    """`tracked`, `generated`, or `missing` -- decided by git, never by the filesystem."""
    root = root or ROOT
    path = reference.rstrip("/")
    if path in _tracked_paths(root):
        return "tracked"
    if _is_ignored(root, reference):
        return "generated"
    # A directory is declared generated when an ignore pattern reaches into it,
    # e.g. `data/raw_yaml/**/*.yaml` for `data/raw_yaml/`.
    if any(pattern.startswith(path + "/") for pattern in _ignore_patterns(root)):
        return "generated"
    return "missing"


def _display(path: Path) -> str:
    """Repository-relative when the file is inside ROOT; a test may point
    SKILLS_DIR elsewhere while still checking references against ROOT's git."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def validate_skills() -> list[str]:
    errors: list[str] = []
    loose_markdown = sorted(SKILLS_DIR.glob("*.md"))
    for path in loose_markdown:
        errors.append(f"{_display(path)}: use <skill>/SKILL.md layout")

    for directory in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{_display(directory)}: missing SKILL.md")
            continue
        try:
            metadata = frontmatter(skill_file)
        except ValueError as error:
            errors.append(f"{_display(skill_file)}: {error}")
            continue
        missing = sorted(REQUIRED_FRONTMATTER - metadata.keys())
        if missing:
            errors.append(f"{_display(skill_file)}: missing {', '.join(missing)}")
        nested_metadata = metadata.get("metadata")
        nested_version = (
            nested_metadata.get("version") if isinstance(nested_metadata, dict) else None
        )
        if not metadata.get("version") and not nested_version:
            errors.append(f"{_display(skill_file)}: missing version")
        if metadata.get("name") != directory.name:
            errors.append(f"{_display(skill_file)}: name must match directory {directory.name!r}")

        for document in sorted(directory.rglob("*.md")):
            seen: set[str] = set()
            for match in LOCAL_REFERENCE.finditer(document.read_text()):
                reference = normalize_reference(match.group(1))
                if not reference or reference in seen:
                    continue
                seen.add(reference)
                if classify_reference(reference, ROOT) == "missing":
                    errors.append(
                        f"{_display(document)}: missing local path {reference} "
                        f"(not tracked by git and not declared generated in .gitignore)"
                    )
    return errors


def main() -> int:
    try:
        errors = validate_skills()
    except NotAGitCheckout as error:
        print(f"error: {error}")
        return 1
    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1
    count = len(list(SKILLS_DIR.glob("*/SKILL.md")))
    print(f"validated {count} Claude skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
