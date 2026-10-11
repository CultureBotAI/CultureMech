"""Guarded application and adversarial scientific-scope regression checks."""

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_komodo650_752_762_preparations as repair  # noqa: E402


def frozen():
    return json.loads((repair.HERE / "plan.json").read_text())


def audit():
    spec = importlib.util.spec_from_file_location("preparation_audit", repair.HERE / "audit.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL)


@pytest.fixture
def fixture(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    for item in frozen()["records"]:
        path = root / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    git(root, "init", "-q")
    git(root, "add", "data")
    git(
        root,
        "-c",
        "user.name=Test",
        "-c",
        "user.email=test@example.org",
        "commit",
        "-qm",
        "baseline",
    )
    return root, repair.COHORT, tmp_path / "plan.json"


def test_preview_apply_verify_noop(fixture, tmp_path):
    plan, result = repair.process(*fixture, "preview")
    assert result["records"] == 3 and result["changed"] == 0
    for item in plan["records"]:
        before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
        audit().check(before, after, item)
        assert not repair.runner.errors(before, "MediaRecipe")
        assert not repair.runner.errors(after, "MediaRecipe")
    assert repair.process(*fixture, "apply")[1]["changed"] == 3
    assert repair.process(*fixture, "verify")[1]["already_applied"] == 3
    assert repair.process(*fixture, "apply")[1]["changed"] == 0
    repair.report(tmp_path / "reports", plan, True)
    for item in plan["records"]:
        text = (tmp_path / "reports" / (item["medium_id"] + "-followup.md")).read_text()
        assert text.count("- Follow-up target:") == 1 and "- Record:" not in text
        assert item["path"] in text and item["after_sha256"] in text


@pytest.mark.parametrize("mid", list(repair.TARGETS))
def test_concurrent_edit_aborts_before_writing(fixture, mid):
    repair.process(*fixture, "preview")
    path = fixture[0] / repair.TARGETS[mid]["path"]
    path.write_bytes(path.read_bytes() + b"\n# concurrent edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(*fixture, "apply")
    for other, spec in repair.TARGETS.items():
        if other != mid:
            assert (
                repair.runner.sha((fixture[0] / spec["path"]).read_bytes()) == spec["before_sha256"]
            )


@pytest.mark.parametrize("kind", ["symlink", "untracked", "case"])
def test_exact_tracked_paths_required(fixture, monkeypatch, kind):
    specs = copy.deepcopy(repair.TARGETS)
    monkeypatch.setattr(repair, "TARGETS", specs)
    path = fixture[0] / specs["752"]["path"]
    if kind == "symlink":
        path.rename(path.with_suffix(".backup"))
        path.symlink_to(path.with_suffix(".backup").name)
    elif kind == "untracked":
        git(fixture[0], "rm", "--cached", specs["752"]["path"])
    else:
        specs["752"]["path"] = specs["752"]["path"].replace("KOMODO_", "komodo_")
    with pytest.raises((ValueError, FileNotFoundError, StopIteration)):
        repair.process(*fixture, "preview")


def test_frozen_plan_cannot_be_rewritten(fixture):
    plan, _ = repair.process(*fixture, "preview")
    with pytest.raises(ValueError, match="overwrite"):
        repair.process(*fixture, "preview")
    plan["records"][0]["claims"][0]["snippet"] = "Invented evidence"
    fixture[2].write_text(json.dumps(plan))
    with pytest.raises(ValueError, match="Frozen plan"):
        repair.process(*fixture, "apply")
    assert git(fixture[0], "diff", "--name-only") == b""


@pytest.mark.parametrize("mid", list(repair.TARGETS))
def test_source_hash_drift(mid):
    item = next(i for i in frozen()["records"] if i["medium_id"] == mid)
    source = repair.sources(repair.COHORT, mid)
    source["raw"] += " "
    with pytest.raises(ValueError, match="Source hash"):
        repair.build(
            repair.runner.load_yaml(item["before_text"]), source, mid, frozen()["created_at"]
        )


@pytest.mark.parametrize(
    "change",
    [
        "stock_strength",
        "stock_dose",
        "water_basis",
        "agar_branch",
        "snippet",
        "mapping",
        "history",
        "identity",
        "carbonate_strength",
        "carbonate_dose",
        "pyruvate",
    ],
)
def test_independent_audit_rejects_regressions(change):
    mid = "762" if change.startswith("carbonate") else "650" if change == "pyruvate" else "752"
    item = next(i for i in frozen()["records"] if i["medium_id"] == mid)
    before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
    if change == "stock_strength":
        after["solutions"][0]["composition"][0]["concentration"]["value"] = "1"
    elif change in {"stock_dose", "carbonate_dose"}:
        after["solutions"][0]["concentration"] = {"value": "0.1", "unit": "L"}
    elif change == "carbonate_strength":
        after["solutions"][0]["composition"][0]["concentration"] = {
            "value": "54",
            "unit": "G_PER_L",
        }
    elif change == "water_basis":
        after["ingredients"][-1]["concentration"]["unit"] = "ML_PER_L"
    elif change == "agar_branch":
        after["preparation_steps"][0]["description"] += " Add 20-30 ml carbonate stock."
    elif change == "snippet":
        after["ingredients"][0]["evidence"][0]["snippet"] = "Invented evidence"
    elif change == "mapping":
        after["evidence"][-1]["snippet"] = "Wrong source mapping"
    elif change == "history":
        after["curation_history"][0]["curator"] = "Wrong curator"
    elif change == "identity":
        after["solutions"][0]["composition"][0]["term"]["id"] = "CHEBI:15377"
    else:
        after["ingredients"][5]["concentration"]["unit"] = "G_PER_L"
    with pytest.raises(AssertionError):
        audit().check(before, after, item)
