"""Offline source, preparation, provenance and transaction tests for medium 265."""

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz265-preparations"
sys.path.insert(0, str(ROOT / "scripts"))
import repair_dsmz265_preparations as repair  # noqa: E402


def frozen():
    return json.loads((HERE / "plan.json").read_text())


def auditor():
    spec = importlib.util.spec_from_file_location("dsmz265_audit", HERE / "audit.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL)


@pytest.fixture
def fixture(tmp_path):
    plan = frozen()
    repo = tmp_path / "repo"
    repo.mkdir()
    for item in plan["records"]:
        path = repo / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    git(repo, "init", "-q")
    git(repo, "add", "data")
    git(
        repo,
        "-c",
        "user.name=Test",
        "-c",
        "user.email=test@example.org",
        "commit",
        "-qm",
        "baseline",
    )
    return repo, plan["sources"]


def preview(fixture, tmp_path):
    path = tmp_path / "plan.json"
    plan, result = repair.process(*fixture, path, "preview")
    assert result["changed"] == 0 and result["scoped_claims"] == 102
    return path, plan


def test_preview_apply_verify_noop_and_full_inversion(fixture, tmp_path):
    path, plan = preview(fixture, tmp_path)
    counts = []
    for item in plan["records"]:
        before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
        counts.append(auditor().check(before, after, item, plan["sources"]))
        assert not repair.runner.errors(after, item["target_class"])
    assert sum(c["new_evidence"] for c in counts) == 50
    assert sum(c["stock_nodes_relocated"] for c in counts) == 49
    assert repair.process(*fixture, path, "apply")[1]["changed"] == 3
    assert repair.process(*fixture, path, "verify")[1]["already_applied"] == 3
    assert repair.process(*fixture, path, "apply")[1]["changed"] == 0
    repair.report(plan, tmp_path / "reports", True)
    for item in plan["records"]:
        text = (tmp_path / "reports" / (item["key"] + "-followup.md")).read_text()
        assert text.count("- Follow-up target:") == 1 and "- Record:" not in text
        assert item["path"] in text and item["after_sha256"] in text


@pytest.mark.parametrize("reference", [repair.MEDIUM, repair.SOLUTION, repair.PDF])
def test_source_byte_drift_refuses_without_partial_writes(fixture, tmp_path, reference):
    path, _ = preview(fixture, tmp_path)
    fixture[1][reference]["raw"] += " "
    with pytest.raises(ValueError, match="drift"):
        repair.process(*fixture, path, "apply")
    assert git(fixture[0], "diff", "--name-only") == b""


@pytest.mark.parametrize("key", list(repair.TARGETS))
def test_concurrent_edit_refuses_whole_batch(fixture, tmp_path, key):
    path, _ = preview(fixture, tmp_path)
    target = fixture[0] / repair.TARGETS[key]["path"]
    target.write_bytes(target.read_bytes() + b"\n# concurrent edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(*fixture, path, "apply")
    for other, spec in repair.TARGETS.items():
        if other != key:
            assert (
                repair.runner.sha((fixture[0] / spec["path"]).read_bytes()) == spec["before_sha256"]
            )


@pytest.mark.parametrize("kind", ["symlink", "untracked", "case"])
def test_exact_tracked_targets_required(fixture, tmp_path, monkeypatch, kind):
    specs = copy.deepcopy(repair.TARGETS)
    monkeypatch.setattr(repair, "TARGETS", specs)
    target = fixture[0] / specs["komodo"]["path"]
    if kind == "symlink":
        target.rename(target.with_suffix(".backup"))
        target.symlink_to(target.with_suffix(".backup").name)
    elif kind == "untracked":
        git(fixture[0], "rm", "--cached", specs["komodo"]["path"])
    else:
        specs["komodo"]["path"] = specs["komodo"]["path"].replace("KOMODO_265", "komodo_265")
    with pytest.raises((ValueError, FileNotFoundError)):
        repair.process(*fixture, tmp_path / "plan.json", "preview")


def test_frozen_plan_and_overwrite_guards(fixture, tmp_path):
    path, plan = preview(fixture, tmp_path)
    with pytest.raises(ValueError, match="overwrite"):
        repair.process(*fixture, path, "preview")
    plan["records"][0]["claims"][0]["snippet"] = "Fabricated amount"
    path.write_text(json.dumps(plan))
    with pytest.raises(ValueError, match="Frozen decision"):
        repair.process(*fixture, path, "apply")
    assert git(fixture[0], "diff", "--name-only") == b""


@pytest.mark.parametrize(
    "kind",
    [
        "yeast_final",
        "dose_per_litre",
        "lipid_midpoint",
        "lipid_mass",
        "sulfur_rate",
        "water_percent",
        "fixed_carrier",
        "snippet",
        "identity",
        "history",
        "ph",
        "base_dose",
    ],
)
def test_independent_audit_rejects_scientific_or_provenance_regressions(kind):
    plan = frozen()
    item = plan["records"][0]
    before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
    stocks = after["solutions"]
    if kind == "yeast_final":
        stocks[1]["composition"][0]["concentration"] = {"value": "2", "unit": "G_PER_L"}
    elif kind == "dose_per_litre":
        stocks[1]["concentration"] = {"value": "20", "unit": "ML_PER_L"}
    elif kind == "lipid_midpoint":
        stocks[4]["concentration"]["value"] = "0.009"
    elif kind == "lipid_mass":
        stocks[4]["composition"][0]["concentration"] = {"value": "10", "unit": "G_PER_L"}
    elif kind == "sulfur_rate":
        after["ingredients"][0]["concentration"] = {"value": "10", "unit": "G_PER_L"}
    elif kind == "water_percent":
        stocks[0]["composition"][-1]["concentration"]["unit"] = "PERCENT_V_V"
    elif kind == "fixed_carrier":
        stocks[1]["composition"][1]["concentration"] = {"value": "0.02", "unit": "L"}
    elif kind == "snippet":
        stocks[0]["composition"][0]["evidence"][0]["snippet"] = "Fabricated evidence"
    elif kind == "identity":
        stocks[0]["composition"][0]["term"]["id"] = "CHEBI:15377"
    elif kind == "history":
        after["curation_history"][0]["curator"] = "wrong"
    elif kind == "base_dose":
        stocks[0]["concentration"] = {"value": "1", "unit": "L"}
    else:
        after["ph_value"] = 7
    with pytest.raises(AssertionError):
        auditor().check(before, after, item, plan["sources"])


def test_historical_claims_follow_explicit_resolutions():
    plan = frozen()
    for item in plan["records"]:
        if item["key"] == "komodo":
            assert item["claim_resolutions"] == []
            continue
        folder = (
            "20261007-mediadive-solutions-0000-0500"
            if item["key"] == "solution"
            else "20261007-mediadive-media-0000-0500"
        )
        prior_plan = json.loads((HERE.parent / folder / "plan.json").read_text())
        old = next(r for r in prior_plan["records"] if r["path"] == item["path"])
        assert repair.runner.followup_result_hash(old, plan["records"])[0] == item["after_sha256"]
        accepted = [c for c in old["claims"] if c["status"] in repair.runner.SUPPORTED]
        assert len(accepted) == len(item["claim_resolutions"]) == 12
        raw = plan["sources"][repair.SOLUTION if item["key"] == "solution" else repair.MEDIUM][
            "raw"
        ]
        for c in accepted:
            pointer, field, withdrawn = repair.runner.resolved_claim(old, c, plan["records"], raw)
            assert pointer[:3] == ["solutions", 0, "composition"] and not withdrawn
            assert field.endswith(".concentration")


def test_applied_records_and_saved_claim_reports():
    plan = frozen()
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert repair.runner.sha(raw) == item["after_sha256"]
        auditor().check(
            repair.runner.load_yaml(item["before_text"]),
            repair.runner.load_yaml(raw),
            item,
            plan["sources"],
        )
        text = (HERE / (item["key"] + "-followup.md")).read_text()
        assert "- State: applied locally" in text and item["path"] in text
