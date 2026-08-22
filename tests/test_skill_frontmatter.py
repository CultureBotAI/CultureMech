"""Every project skill and command must carry loadable frontmatter.

Written after two real breakages found the same day:

  - `boss/SKILL.md` had `argument-hint: [ "curate" | "enrich" | ... ]`, an
    unquoted YAML flow sequence containing `|`. Invalid since it was added.
  - A new skill's `description` contained "Read-only: never merges", and the
    `: ` turned the rest of the line into a nested mapping.

Both are silent: the file looks fine, renders fine on GitHub, and fails only
in whatever loads it. This test is vendored byte-identically across the Mech
fleet so each repository blocks the defect at the pull request that adds it.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

SKILLS_DIR = Path(__file__).resolve().parents[1] / ".claude" / "skills"
COMMANDS_DIR = Path(__file__).resolve().parents[1] / ".claude" / "commands"
BACKLOG_PROMPT = Path(__file__).resolve().parents[1] / "prompts" / "backlog-loop-goal.md"


def _discover_skill_files() -> list[Path]:
    """Every skill file, whatever its casing, listed exactly once.

    Globbing `*/SKILL.md` under-reports on Linux CI when a skill is named
    `skill.md`; ProteinTraitsMech carried such a split until it normalised to
    all-uppercase, and nothing enforces the convention across the fleet.
    Globbing both patterns instead over-reports on macOS, where a
    case-insensitive filesystem matches each file twice and `resolve()` does not
    canonicalise the spelling, so the pair does not dedupe.

    Reading real directory entries sidesteps both: each file appears once,
    under its true on-disk name, on either filesystem.
    """
    if not SKILLS_DIR.is_dir():
        return []
    found = []
    for directory in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        found.extend(
            sorted(
                entry
                for entry in directory.iterdir()
                if entry.is_file() and entry.name.lower() == "skill.md"
            )
        )
    return found


SKILL_FILES = _discover_skill_files()
COMMAND_FILES = sorted(COMMANDS_DIR.glob("*.md")) if COMMANDS_DIR.is_dir() else []


def _frontmatter_text(text: str, label: str = "<text>") -> str:
    """Return the frontmatter block, rejecting shapes YAML would accept anyway.

    Splitting on the fence is not enough. `---\\nname: x\\n\\n# Title\\n` with no
    closing fence still yields a parseable block, because a markdown `#` heading
    is a YAML comment -- so an unterminated file passes every downstream
    assertion. That is the same silent-breakage class this module exists to
    catch, so the fence is located structurally instead.

    Searching for "\\n---" (unindented) also means a `---` inside an indented
    block scalar does not end the block early.
    """
    assert text.startswith("---\n"), f"{label} does not open with a --- fence"
    body = text[4:]
    end = body.find("\n---")
    assert end != -1, f"{label} has no closing --- fence"
    # The closing fence must be alone on its line: `---`, not `--- foo`.
    rest = body[end + 4 :]
    assert rest[:1] in ("", "\n", "\r"), f"{label} closing --- fence is not alone on its line"
    return body[: end + 1]


def _frontmatter(path: Path) -> str:
    return _frontmatter_text(path.read_text(), str(path))


class _StrictLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate keys instead of taking the last one."""


def _no_duplicate_keys(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicate_keys)


def test_there_are_skills_to_check():
    """Guard the guard: a glob that matches nothing passes every test below."""
    assert SKILL_FILES, "found no skill files under .claude/skills"


def test_project_does_not_shadow_the_builtin_goal_command():
    """The native /goal owns this name; backlog prompts live under prompts/.

    Claude Code documents precedence between custom commands and skills, and
    between custom and bundled skills, but not between a custom item and the
    fixed built-in /goal command. Rejecting both custom shapes makes that
    unspecified precedence irrelevant.
    """
    collisions = [path for path in COMMAND_FILES if path.stem.casefold() == "goal"]
    collisions.extend(path for path in SKILL_FILES if path.parent.name.casefold() == "goal")
    assert (
        not collisions
    ), "project-local goal command/skill collides with Claude Code's built-in: " + ", ".join(
        str(path) for path in collisions
    )


def test_backlog_prompt_is_plain_and_fits_native_goal():
    """The shared prompt is input to /goal, not a competing slash command."""
    text = BACKLOG_PROMPT.read_text(encoding="utf-8")
    assert text.strip(), f"{BACKLOG_PROMPT} is empty"
    assert not text.startswith(
        "---\n"
    ), f"{BACKLOG_PROMPT} has frontmatter and could be registered as a command"
    assert text.isascii(), "/goal length is measured in UTF-16 units; keep the proxy exact"
    assert (
        len(text.strip()) <= 4000
    ), f"{BACKLOG_PROMPT} is {len(text.strip())} characters; /goal rejects over 4000"


# --------------------------------------------------------------------------
# _frontmatter itself — the helper is the part that can pass on broken input
# --------------------------------------------------------------------------


def test_frontmatter_rejects_a_missing_closing_fence():
    """A markdown heading is a YAML comment, so an unterminated block parses
    clean and would satisfy every other assertion in this file."""
    with pytest.raises(AssertionError, match="closing"):
        _frontmatter_text("---\nname: x\ndescription: d\n\n# Title\n\nbody\n")


def test_frontmatter_ignores_a_horizontal_rule_in_the_body():
    text = "---\nname: x\ndescription: d\n---\n\n# Title\n\n---\n\nmore\n"
    assert yaml.safe_load(_frontmatter_text(text)) == {"name": "x", "description": "d"}


def test_frontmatter_does_not_truncate_on_an_indented_dashes_line():
    """A `---` inside a block scalar is indented, so it must not end the block."""
    text = "---\nname: x\ndescription: |\n  line one\n  ---\n  line two\n---\n\nbody\n"
    meta = yaml.safe_load(_frontmatter_text(text))
    assert meta["description"] == "line one\n---\nline two\n"


@pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
def test_skill_frontmatter_has_no_duplicate_keys(path: Path):
    """PyYAML takes the last of a duplicated key silently, so `name:` twice
    would let the directory check pass against the wrong value."""
    yaml.load(_frontmatter(path), Loader=_StrictLoader)  # noqa: S506


@pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
def test_skill_frontmatter_is_valid_yaml(path: Path):
    meta = yaml.safe_load(_frontmatter(path))
    assert isinstance(meta, dict), f"{path} frontmatter is not a mapping"


@pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
def test_skill_name_matches_its_directory(path: Path):
    """The loader keys on the directory; a mismatched name: is a silent alias."""
    meta = yaml.safe_load(_frontmatter(path))
    assert meta.get("name") == path.parent.name


@pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
def test_skill_declares_a_usable_description(path: Path):
    """The description is what a model matches a request against."""
    meta = yaml.safe_load(_frontmatter(path))
    description = meta.get("description")
    assert isinstance(description, str) and description.strip(), f"{path} has no usable description"


@pytest.mark.parametrize("path", COMMAND_FILES, ids=lambda p: p.name)
def test_command_frontmatter_has_no_duplicate_keys(path: Path):
    yaml.load(_frontmatter(path), Loader=_StrictLoader)  # noqa: S506


@pytest.mark.parametrize("path", COMMAND_FILES, ids=lambda p: p.name)
def test_command_frontmatter_is_valid_yaml(path: Path):
    meta = yaml.safe_load(_frontmatter(path))
    assert isinstance(meta, dict), f"{path} frontmatter is not a mapping"


@pytest.mark.parametrize("path", COMMAND_FILES, ids=lambda p: p.name)
def test_command_declares_a_usable_description(path: Path):
    meta = yaml.safe_load(_frontmatter(path))
    description = meta.get("description")
    assert isinstance(description, str) and description.strip(), f"{path} has no usable description"
