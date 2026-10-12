"""Guarded writes, historical claims and adversarial preparation-scope tests."""

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_dsmz650_752_762_preparations as repair  # noqa: E402
import review_medium_concentration_evidence as medium  # noqa: E402


def frozen():
    return json.loads((repair.HERE / "plan.json").read_text())


def audit():
    spec = importlib.util.spec_from_file_location(
        "dsmz_preparation_audit", repair.HERE / "audit.py"
    )
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
    return root, repair.sources(), tmp_path / "plan.json"


def test_preview_apply_verify_noop(fixture, tmp_path):
    plan, result = repair.process(*fixture, "preview")
    assert result["records"] == 6 and result["changed"] == 0
    for item in plan["records"]:
        before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
        audit().check(before, after, item, plan["sources"])
        assert not repair.runner.errors(before, item["target_class"])
        assert not repair.runner.errors(after, item["target_class"])
    assert repair.process(*fixture, "apply")[1]["changed"] == 6
    assert repair.process(*fixture, "verify")[1]["already_applied"] == 6
    assert repair.process(*fixture, "apply")[1]["changed"] == 0
    repair.report(plan, True, tmp_path / "reports")
    for item in plan["records"]:
        text = (tmp_path / "reports" / (item["key"] + "-followup.md")).read_text()
        assert text.count("- Follow-up target:") == 1 and "- Record:" not in text
        assert item["path"] in text and item["after_sha256"] in text
        field = "composition" if item["key"].endswith("solution") else "ingredients"
        assert f"| {field}[0].concentration |" in text


@pytest.mark.parametrize("key", list(repair.TARGETS))
def test_concurrent_edit_aborts_all_writes(fixture, key):
    repair.process(*fixture, "preview")
    path = fixture[0] / repair.TARGETS[key]["path"]
    path.write_bytes(path.read_bytes() + b"\n# concurrent edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(*fixture, "apply")
    for other, spec in repair.TARGETS.items():
        if other != key:
            assert (
                repair.runner.sha((fixture[0] / spec["path"]).read_bytes()) == spec["before_sha256"]
            )


@pytest.mark.parametrize("kind", ["symlink", "untracked", "case"])
def test_exact_tracked_path(fixture, monkeypatch, kind):
    specs = copy.deepcopy(repair.TARGETS)
    monkeypatch.setattr(repair, "TARGETS", specs)
    path = fixture[0] / specs["752-solution"]["path"]
    if kind == "symlink":
        path.rename(path.with_suffix(".backup"))
        path.symlink_to(path.with_suffix(".backup").name)
    elif kind == "untracked":
        git(fixture[0], "rm", "--cached", specs["752-solution"]["path"])
    else:
        specs["752-solution"]["path"] = specs["752-solution"]["path"].replace(
            "Main_sol", "main_sol"
        )
    with pytest.raises((ValueError, FileNotFoundError)):
        repair.process(*fixture, "preview")


def test_frozen_plan_guard(fixture):
    plan, _ = repair.process(*fixture, "preview")
    with pytest.raises(ValueError, match="overwrite"):
        repair.process(*fixture, "preview")
    plan["records"][0]["claims"][0]["snippet"] = "Invented evidence"
    fixture[2].write_text(json.dumps(plan))
    with pytest.raises(ValueError, match="Frozen plan"):
        repair.process(*fixture, "apply")
    assert git(fixture[0], "diff", "--name-only") == b""


@pytest.mark.parametrize("key", list(repair.TARGETS))
def test_source_drift_rejected(key):
    bundle = repair.sources()
    bundle[key]["raw"] += " "
    with pytest.raises(ValueError, match="Source hash"):
        repair.check_sources(bundle)


def test_prior_reports_verify_with_explicit_withdrawals(fixture, tmp_path):
    plan, _ = repair.process(*fixture, "preview")
    repair.process(*fixture, "apply")
    for key, capture in plan["sources"].items():
        mid, kind = key.split("-")
        cache = tmp_path / kind
        cache.mkdir(exist_ok=True)
        accession = mid if kind == "medium" else str(repair.SIDS[mid])
        (cache / (accession + ".json")).write_text(capture["raw"])
        (cache / (accession + ".metadata.json")).write_text(json.dumps(capture["metadata"]))
    paths = {r["path"] for r in plan["records"]}
    withdrawn = superseded = 0
    for name in ("media-0500-1000", "solutions-0500-1000", "solutions-1000-1500"):
        prior = json.loads(
            (repair.HERE.parent / ("20261007-mediadive-" + name) / "plan.json").read_text()
        )
        prior["records"] = [r for r in prior["records"] if r["path"] in paths]
        is_medium = name.startswith("media-")
        cache = tmp_path / ("medium" if is_medium else "solution")
        result = repair.runner.verify(
            fixture[0],
            prior,
            cache,
            plan["records"],
            adapter=medium.adapter() if is_medium else None,
        )
        withdrawn += result.get("withdrawn_concentration_claims", 0)
        superseded += result["superseded_record_hashes"]
    assert withdrawn == 4 and superseded == 6


@pytest.mark.parametrize("kind", ["medium", "solution"])
@pytest.mark.parametrize(
    "change",
    [
        "stock_strength",
        "stock_dose",
        "water_basis",
        "agar_branch",
        "snippet",
        "prior_explanation",
        "history",
        "identity",
        "carbonate_strength",
        "carbonate_dose",
        "resolution",
        "pyruvate",
    ],
)
def test_independent_audit_rejects_regressions(kind, change):
    mid = (
        "762"
        if change.startswith("carbonate") or change == "resolution"
        else "650" if change == "pyruvate" else "752"
    )
    item = next(r for r in frozen()["records"] if r["key"] == mid + "-" + kind)
    before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
    field = "composition" if kind == "solution" else "ingredients"
    if change == "stock_strength":
        after["solutions"][0]["composition"][0]["concentration"]["value"] = "1"
    elif change in {"stock_dose", "carbonate_dose"}:
        after["solutions"][0]["concentration"] = {"value": "0.1", "unit": "L"}
    elif change == "water_basis":
        after[field][-1]["concentration"]["unit"] = "ML_PER_L"
    elif change == "agar_branch":
        if kind == "solution":
            after["preparation_notes"] = (
                "Liquid medium may be prepared by adding all components together."
            )
        else:
            after["preparation_steps"][0]["description"] += " Add carbonate stock."
    elif change == "snippet":
        after[field][0]["evidence"][0]["snippet"] = "Invented evidence"
    elif change == "prior_explanation":
        after[field][0]["evidence"][0]["explanation"] = after[field][0]["evidence"][0][
            "explanation"
        ].split(" Historical explanation")[0]
    elif change == "history":
        after["curation_history"][0]["curator"] = "Wrong curator"
    elif change == "identity":
        after["solutions"][0]["composition"][0]["term"]["id"] = "CHEBI:15377"
    elif change == "carbonate_strength":
        after["solutions"][0]["composition"][0]["concentration"] = {
            "value": "54",
            "unit": "G_PER_L",
        }
    elif change == "resolution":
        item["claim_resolutions"][0]["disposition"] = "relocated"
    else:
        after[field][5]["concentration"]["unit"] = "G_PER_L"
    with pytest.raises(AssertionError):
        audit().check(before, after, item)
