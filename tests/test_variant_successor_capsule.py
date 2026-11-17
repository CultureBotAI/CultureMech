"""Squash portability and immutable retained evidence boundaries (#775, 2026-11-16)."""

from __future__ import annotations

import copy
import json
import shutil
import subprocess
import sys
from pathlib import Path

import audit_variant_ingredient_successor as audit
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
HISTORICAL = (
    "reports/ingredient_concentration_curation/20261007-dsmz1399-stock-boundary/audit_diff.py"
)
PROBE = ROOT / "scripts/adhoc/verify_variant_successor_capsule_775.py"


@pytest.fixture
def retained_checkout(tmp_path):
    """Copy the bounded tracked proof closure, never any original .git objects."""
    root = tmp_path / "checkout"
    paths = [
        "scripts/audit_variant_ingredient_successor.py",
        "scripts/adhoc/audit_variant_coverage_683.py",
        HISTORICAL,
        audit.PLAN.relative_to(ROOT).as_posix(),
        *audit.PROPOSALS,
    ]
    paths += [
        path.relative_to(ROOT).as_posix() for path in audit.CAPSULE.rglob("*") if path.is_file()
    ]
    for relative in paths:
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, target)
    return root


def probe(root, *options):
    return subprocess.run(
        [sys.executable, "-B", str(PROBE), "--checkout", str(root), *options],
        capture_output=True,
        text=True,
        check=False,
    )


def test_all_edges_and_historical_consumer_work_without_original_commits(retained_checkout):
    root = retained_checkout
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
            "Synthetic squash-equivalent proof checkout",
        ],
        cwd=root,
        check=True,
        capture_output=True,
    )
    result = probe(root, "--require-single-commit")
    assert result.returncode == 0, result.stderr
    receipt = json.loads(result.stdout)
    assert receipt["records"] == 87 and receipt["events"] == 377
    assert receipt["original_commits_unavailable"] == [audit.BASE, audit.RESULT]
    assert receipt["historical_consumer"] == "invert_chain"


@pytest.mark.parametrize(
    "mutation", ["manifest", "plan", "proposal", "extra_file", "missing_proposal"]
)
def test_retained_evidence_tampering_is_refused(retained_checkout, mutation):
    root = retained_checkout
    capsule = root / audit.CAPSULE.relative_to(ROOT)
    manifest = json.loads((capsule / "manifest.json").read_bytes())
    proposal = capsule / next(iter(manifest["proposals"].values()))["path"]
    if mutation == "manifest":
        manifest["events"] = 378
        (capsule / "manifest.json").write_text(json.dumps(manifest))
    elif mutation == "plan":
        path = root / audit.PLAN.relative_to(ROOT)
        plan = json.loads(path.read_bytes())
        item = plan["records"][0]
        item["before_text"] += "\n"
        item["before_sha256"] = audit.sha(item["before_text"].encode())
        path.write_text(json.dumps(plan))
    elif mutation == "proposal":
        data = json.loads(proposal.read_bytes())
        data["records"][0]["recipe_id"] = "CultureMech:999999"
        proposal.write_text(json.dumps(data))
    elif mutation == "extra_file":
        (capsule / "unreviewed.json").write_text("{}")
    else:
        proposal.unlink()
    result = probe(root)
    assert result.returncode != 0
    assert "AssertionError" in result.stderr or "FileNotFoundError" in result.stderr


def test_current_proposal_changes_cannot_rewrite_retained_historical_evidence(retained_checkout):
    """Current drafts are not the immutable claims; a new draft grants no old-edge approval."""
    path = retained_checkout / audit.PROPOSALS[0]
    changed = json.loads(path.read_bytes())
    changed["records"][0]["recipe_id"] = "CultureMech:999999"
    path.write_text(json.dumps(changed))
    result = probe(retained_checkout)
    assert result.returncode == 0, result.stderr
    item = copy.deepcopy(next(iter(audit.retained_evidence()[0].values())))
    item["proposal_sha256"] = audit.sha(path.read_bytes())
    with pytest.raises(AssertionError, match="reviewed retained snapshots"):
        audit.check(
            yaml.load(item["before_text"], Loader=yaml.CSafeLoader),
            yaml.load(item["after_text"], Loader=yaml.CSafeLoader),
            item,
        )
