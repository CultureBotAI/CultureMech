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
