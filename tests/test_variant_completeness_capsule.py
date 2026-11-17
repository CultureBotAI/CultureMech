"""Retained completeness proof survives squash and rejects drift (#683, 2026-11-16)."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import audit_variant_completeness_successor as audit
import audit_variant_ingredient_successor as earlier
import pytest

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "scripts/adhoc/verify_variant_completeness_capsule_683.py"
HISTORICAL = (
    "reports/ingredient_concentration_curation/20261007-dsmz1399-stock-boundary/audit_diff.py"
)


def test_current_recipes_and_both_registered_layers_survive_single_commit_checkout(tmp_path):
    """Copy source/proof closure and current recipes, never original Git objects."""
    root = tmp_path / "checkout"
    paths = {
        "scripts/audit_variant_completeness_successor.py",
        "scripts/audit_variant_ingredient_successor.py",
        "scripts/curate_variant_completeness.py",
        "scripts/curate_variant_ingredients.py",
        "scripts/adhoc/audit_variant_coverage_683.py",
        HISTORICAL,
        audit.PLAN.relative_to(ROOT).as_posix(),
        earlier.PLAN.relative_to(ROOT).as_posix(),
    }
    for directory in (audit.CAPSULE, earlier.CAPSULE):
        paths.update(
            path.relative_to(ROOT).as_posix() for path in directory.rglob("*") if path.is_file()
        )
    paths.update(item["path"] for item in json.loads(audit.PLAN.read_bytes())["records"])
    paths.update(
        subprocess.check_output(
            ["git", "ls-files", "--", "src/culturemech"], cwd=ROOT, text=True
        ).splitlines()
    )
    for relative in sorted(paths):
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, target)
    subprocess.run(
        ["git", "init", "--initial-branch=main", str(root)], check=True, capture_output=True
    )
    subprocess.run(["git", "add", "."], cwd=root, check=True, capture_output=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Capsule fixture",
            "-c",
            "user.email=capsule@example.invalid",
            "-c",
            "commit.gpgsign=false",
            "-c",
            "core.hooksPath=/dev/null",
            "commit",
            "-m",
            "Synthetic squash-equivalent completeness proof",
        ],
        cwd=root,
        check=True,
        capture_output=True,
    )
    result = subprocess.run(
        [sys.executable, "-B", str(PROBE), "--checkout", str(root), "--require-single-commit"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    receipt = json.loads(result.stdout)
    assert receipt["status"] == "PASS"
    assert receipt["records"] == 58 and receipt["two_layer_records"] == 47
    assert receipt["original_commits_unavailable"] == [earlier.BASE, earlier.RESULT, audit.BASE]


@pytest.fixture
def isolated_evidence(tmp_path, monkeypatch):
    root = tmp_path / "evidence"
    plan = root / audit.PLAN.relative_to(ROOT)
    capsule = root / audit.CAPSULE.relative_to(ROOT)
    plan.parent.mkdir(parents=True)
    shutil.copyfile(audit.PLAN, plan)
    shutil.copytree(audit.CAPSULE, capsule)
    monkeypatch.setattr(audit, "ROOT", root)
    monkeypatch.setattr(audit, "PLAN", plan)
    monkeypatch.setattr(audit, "CAPSULE", capsule)
    audit.retained_evidence.cache_clear()
    yield plan, capsule
    audit.retained_evidence.cache_clear()


@pytest.mark.parametrize(
    "mutation", ["manifest", "plan_rehash", "decisions", "extra_file", "missing_decisions"]
)
def test_capsule_drift_cannot_reauthorize_historical_edges(isolated_evidence, mutation):
    plan, capsule = isolated_evidence
    if mutation == "manifest":
        path = capsule / "manifest.json"
        path.write_bytes(path.read_bytes() + b"\n")
    elif mutation == "plan_rehash":
        document = json.loads(plan.read_bytes())
        item = document["records"][0]
        item["before_text"] += "\n"
        item["before_sha256"] = audit.sha(item["before_text"].encode())
        plan.write_text(json.dumps(document))
    elif mutation == "decisions":
        path = capsule / "decisions.json"
        document = json.loads(path.read_bytes())
        document["records"][0]["recipe_id"] = "CultureMech:999999"
        path.write_text(json.dumps(document))
    elif mutation == "extra_file":
        (capsule / "unreviewed.json").write_text("{}")
    else:
        (capsule / "decisions.json").unlink()
    with pytest.raises((AssertionError, FileNotFoundError)):
        audit.retained_evidence()


def test_unapplied_or_changed_current_recipe_is_not_accepted_as_new_successor(isolated_evidence):
    plan, _ = isolated_evidence
    item = json.loads(plan.read_bytes())["records"][0]
    for raw in (item["before_text"].encode(), (item["after_text"] + "\n").encode()):
        with pytest.raises(AssertionError, match="Current completeness successor hash mismatch"):
            audit.restore_before(raw, item["path"])
    assert (
        audit.restore_before(item["after_text"].encode(), item["path"])
        == item["before_text"].encode()
    )
