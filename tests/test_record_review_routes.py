"""Native audit routes must not bypass the shared persistence contract."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_curate_audit_saves_review_without_changing_scientific_inputs():
    text = (ROOT / ".claude/skills/curate-yaml-record/SKILL.md").read_text()
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["metadata"]["version"] == "2.0.0"
    assert "preserves scientific inputs and saves a new structured review" in text


@pytest.mark.parametrize("name", ["audit-schema-gaps", "schema-gap-analysis"])
def test_audit_routes_are_registered_with_native_axes_and_output(name):
    profile = yaml.safe_load((ROOT / "conf/record_review.yaml").read_text())
    path = f".claude/skills/{name}/SKILL.md"
    assert path in profile["skills"]
    assert path in profile["rubrics"]
    text = (ROOT / path).read_text()
    for required in (
        "docs/record-reviews.md",
        "reviews/structured/<timestamp>-<slug>/",
        "audit_axis",
        "scientific_review: false",
        "diagnostic",
        "schema / instances / process",
    ):
        assert required in text


def test_deep_audit_saves_assessed_findings_not_legacy_prose():
    text = (ROOT / ".claude/skills/audit-schema-gaps/SKILL.md").read_text()
    for command in ("inspect --targets", "validate /tmp/", "save --content"):
        assert f"scripts/record_review.py {command}" in text
    assert "Hand-compose `reports/" not in text
    assert "Compose `reports/gap_fix_backlog" not in text
    assert "schema, writers, status gates or history" in text
