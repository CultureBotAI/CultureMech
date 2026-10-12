"""Canonical concentration coverage must not count archived preview ledgers."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "followup_report_coverage",
    ROOT / "reports/ingredient_concentration_curation/summarize_followup_coverage.py",
)
coverage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(coverage)
TARGET = "data/normalized_yaml/bacterial/exact.yaml"


def report(path, state, target=TARGET):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# Review\n\n- Record: {target}\n- State: {state}\n")


@pytest.mark.parametrize("state", ["preview", "Preview only; authoritative YAML unchanged."])
def test_preview_does_not_add_coverage_or_conflict_with_canonical(tmp_path, state):
    report(tmp_path / "preview.md", state)
    reviewed, previews = coverage.report_inventory({TARGET}, tmp_path)
    assert reviewed == set() and len(previews) == 1
    report(tmp_path / "canonical.md", "applied locally")
    reviewed, previews = coverage.report_inventory({TARGET}, tmp_path)
    assert reviewed == {TARGET} and len(previews) == 1
    assert previews[0]["target"] == TARGET and len(previews[0]["sha256"]) == 64


def test_duplicate_canonical_reports_are_still_rejected(tmp_path):
    report(tmp_path / "a.md", "applied locally")
    report(tmp_path / "b.md", "applied locally")
    report(tmp_path / "preview.md", "preview")
    with pytest.raises(AssertionError):
        coverage.report_inventory({TARGET}, tmp_path)


@pytest.mark.parametrize("state", ["preview", "applied locally"])
@pytest.mark.parametrize("damage", ["wrong_case", "two_targets"])
def test_exact_target_and_one_marker_are_required_even_for_previews(tmp_path, state, damage):
    path = tmp_path / "report.md"
    report(path, state, TARGET.upper() if damage == "wrong_case" else TARGET)
    if damage == "two_targets":
        path.write_text(path.read_text() + f"- Record: {TARGET}\n")
    with pytest.raises(AssertionError):
        coverage.report_inventory({TARGET}, tmp_path)


def test_inventory_includes_hidden_and_ignored_files(tmp_path):
    (tmp_path / ".gitignore").write_text(".ignored/\n")
    report(tmp_path / ".ignored" / "canonical.md", "applied locally")
    report(tmp_path / ".ignored" / "preview.md", "preview")
    reviewed, previews = coverage.report_inventory({TARGET}, tmp_path)
    assert reviewed == {TARGET} and len(previews) == 1
