"""Guard that relative Markdown links resolve CASE-SENSITIVELY (#161).

macOS sets `core.ignorecase=true` and its filesystem is case-insensitive, so a
link to `../create-recipe/skill.md` opens fine locally even after the file has
been renamed to `SKILL.md`. Linux CI is case-sensitive and it does not.

That asymmetry is why this needs a deliberate test. It has already bitten twice:
once as the `skill.md` / `SKILL.md` split itself, and again when the commit
fixing that split repaired the links in `review-recipes/reference/` but missed
three in the parent `SKILL.md` — because both spellings opened on the machine
doing the work.

Implementation note: `Path.exists()` is useless here. On macOS it returns True
for a wrong-case path, so the check compares the filename against an actual
directory listing instead.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

# Directories whose links are enforced. `docs/archive/` is deliberately excluded:
# it is a historical record, and its links pointing at since-renamed files is
# accurate rather than broken — the same call the SKILL.md rename made.
ROOTS = (".claude/skills", "docs")
EXCLUDED = ("docs/archive",)

LINK_RE = re.compile(r"\]\(([^)]+)\)")


def _markdown_files() -> list[Path]:
    out: list[Path] = []
    for root in ROOTS:
        base = REPO_ROOT / root
        if not base.is_dir():
            continue
        for md in base.rglob("*.md"):
            rel = md.relative_to(REPO_ROOT).as_posix()
            if any(rel.startswith(x) for x in EXCLUDED):
                continue
            out.append(md)
    return sorted(out)


MARKDOWN_FILES = _markdown_files()


def _resolves_case_sensitively(path: Path) -> bool:
    """True iff every component of `path` exists with exactly this spelling."""
    if not path.parent.is_dir():
        return False
    return path.name in {p.name for p in path.parent.iterdir()}


def _relative_link_targets(md: Path) -> list[str]:
    targets = []
    for match in LINK_RE.finditer(md.read_text(errors="replace")):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#", "<")):
            continue
        target = target.split("#", 1)[0].split(" ", 1)[0]
        if not target or not target.endswith(".md"):
            continue
        targets.append(target)
    return targets


def test_markdown_files_were_discovered():
    """Guards the parametrization — an empty glob would pass vacuously."""
    assert len(MARKDOWN_FILES) >= 10, f"only found {len(MARKDOWN_FILES)} markdown files"


@pytest.mark.parametrize("md", MARKDOWN_FILES, ids=lambda p: p.relative_to(REPO_ROOT).as_posix())
def test_relative_markdown_links_resolve_case_sensitively(md: Path):
    """Two distinct failures, reported separately because their causes differ.

    A wrong-CASE link works locally and only breaks on Linux — insidious, and the
    reason this test exists. A MISSING target is broken everywhere and usually
    means the file moved. Collapsing them into one message would have mislabelled
    the moved-file case as a case-sensitivity problem.
    """
    wrong_case, missing = [], []
    for target in _relative_link_targets(md):
        resolved = (md.parent / target).resolve()
        if _resolves_case_sensitively(resolved):
            continue
        (wrong_case if resolved.exists() else missing).append(target)

    problems = []
    if wrong_case:
        problems.append(
            f"wrong case (opens on macOS, 404s on Linux CI): {wrong_case}")
    if missing:
        problems.append(f"target does not exist at all: {missing}")
    assert not problems, f"{md.relative_to(REPO_ROOT)} — " + "; ".join(problems)


def test_every_skill_dir_has_an_uppercase_skill_md():
    """The convention the rename established; a lowercase one is invisible on macOS."""
    skills = REPO_ROOT / ".claude" / "skills"
    if not skills.is_dir():
        pytest.skip("no .claude/skills directory")
    offenders = []
    for d in sorted(p for p in skills.iterdir() if p.is_dir()):
        names = {p.name for p in d.iterdir()}
        if "SKILL.md" not in names and "skill.md" in names:
            offenders.append(d.name)
    assert not offenders, f"skill dir(s) still using lowercase skill.md: {offenders}"
