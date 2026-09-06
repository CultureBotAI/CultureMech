import importlib.util
from pathlib import Path

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts" / "validate_claude_skills.py"
SPEC = importlib.util.spec_from_file_location("validate_claude_skills", SCRIPT)
assert SPEC and SPEC.loader
validate_claude_skills = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_claude_skills)


def test_repository_skills_have_valid_layout_metadata_and_references() -> None:
    assert validate_claude_skills.validate_skills() == []


def test_stats_report_uses_discoverable_skill_layout() -> None:
    path = ROOT / ".claude" / "skills" / "stats-report" / "SKILL.md"

    assert path.is_file()
    assert validate_claude_skills.frontmatter(path)["name"] == "stats-report"
    assert not (ROOT / ".claude" / "skills" / "stats-report.md").exists()


def test_validator_accepts_standard_nested_skill_metadata(tmp_path, monkeypatch) -> None:
    skill_dir = tmp_path / ".claude" / "skills" / "curate-yaml-record"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        "---\n"
        "name: curate-yaml-record\n"
        "description: Curate one record.\n"
        "metadata:\n"
        "  version: 1.0.0\n"
        "---\n\n"
        "# Curate one record\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(validate_claude_skills, "ROOT", tmp_path)
    monkeypatch.setattr(validate_claude_skills, "SKILLS_DIR", tmp_path / ".claude" / "skills")

    assert validate_claude_skills.validate_skills() == []


# --- existence is decided by git, not the filesystem (#419) -------------------


def _skill_referencing(tmp_path: Path, monkeypatch, body: str) -> list[str]:
    """Validate one throwaway skill against the REAL repository's git state."""
    skill_dir = tmp_path / ".claude" / "skills" / "throwaway"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        "---\nname: throwaway\ndescription: x\nversion: 1.0.0\n---\n\n" + body,
        encoding="utf-8",
    )
    monkeypatch.setattr(validate_claude_skills, "SKILLS_DIR", tmp_path / ".claude" / "skills")
    return validate_claude_skills.validate_skills()


def test_a_tracked_path_is_present() -> None:
    assert validate_claude_skills.classify_reference("scripts/validate_claude_skills.py") == (
        "tracked"
    )
    assert validate_claude_skills.classify_reference("src/culturemech/schema/") == "tracked"


def test_a_generated_artifact_counts_as_present_whether_or_not_it_is_on_disk() -> None:
    """`app/data.js` exists only on a machine that has built the pages, and
    `data/raw_yaml/` only where a conversion has run. Both are declared
    generated in `.gitignore`, which is the fact the skill boundary rests on."""
    assert validate_claude_skills.classify_reference("app/data.js") == "generated"
    assert validate_claude_skills.classify_reference("data/raw_yaml/") == "generated"


def test_a_directory_is_generated_when_an_ignore_pattern_reaches_into_it() -> None:
    """`.gitignore` says `data/raw_yaml/**/*.yaml`, not `data/raw_yaml/`, so
    `git check-ignore` on the bare directory says no. The layer is still
    declared, and the validator has to read the declaration, not the answer."""
    assert validate_claude_skills._is_ignored(validate_claude_skills.ROOT, "data/raw_yaml/") is (
        False
    )
    assert validate_claude_skills.classify_reference("data/raw_yaml/") == "generated"


def test_case_is_decided_by_git_not_by_the_filesystem() -> None:
    """On macOS `Path('docs/data_layers.md').exists()` is True because the
    tracked file is `DATA_LAYERS.md`; on Linux CI it is False. Git gives one
    answer on both, which is how `TSB.yaml` was caught standing in for the
    tracked `tsb.yaml` in the create-recipe skill (#419)."""
    assert validate_claude_skills.classify_reference("docs/DATA_LAYERS.md") == "tracked"
    assert validate_claude_skills.classify_reference("docs/data_layers.md") == "missing"


def test_an_unknown_path_under_a_data_prefix_is_reported(tmp_path, monkeypatch) -> None:
    """The regression guard for #419: `data/` was outside the old prefix list,
    so a wrong data-layer path in prose was never looked at."""
    errors = _skill_referencing(tmp_path, monkeypatch, "Never edit `data/raw_yamlx/`.\n")
    assert len(errors) == 1
    assert "data/raw_yamlx/" in errors[0]


def test_a_declared_generated_path_is_accepted(tmp_path, monkeypatch) -> None:
    errors = _skill_referencing(
        tmp_path, monkeypatch, "Never edit `data/raw_yaml/` or `app/data.js`.\n"
    )
    assert errors == []


def test_sibling_repository_paths_are_not_checked_here(tmp_path, monkeypatch) -> None:
    """A path in another checkout is written with the repository name first or
    a placeholder root; neither matches a local prefix, so neither is checked."""
    errors = _skill_referencing(
        tmp_path,
        monkeypatch,
        "See `MediaIngredientMech/templates/ingredient_role_research.md` and "
        "`<kg-microbe>/data/transformed_last9/mediadive/edges.tsv`.\n",
    )
    assert errors == []
