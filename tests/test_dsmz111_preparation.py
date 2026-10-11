"""Offline preparation, provenance and guarded-transaction tests for medium 111."""

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz111-preparation"
sys.path.insert(0, str(ROOT / "scripts"))
import repair_dsmz111_preparation as repair  # noqa: E402


def frozen():
    return json.loads((HERE / "plan.json").read_text())


def auditor():
    spec = importlib.util.spec_from_file_location("dsmz111_audit", HERE / "audit.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL)


@pytest.fixture
def fixture(tmp_path, monkeypatch):
    plan = frozen()
    repo, medium, solution = (tmp_path / s for s in ("repo", "medium", "solution"))
    for folder in (repo, medium, solution):
        folder.mkdir()
    for ref, cache, sid in ((repair.MEDIUM, medium, "111"), (repair.SOLUTION, solution, "190")):
        (cache / (sid + ".json")).write_text(plan["sources"][ref]["raw"])
        (cache / (sid + ".metadata.json")).write_text(json.dumps(plan["sources"][ref]["metadata"]))
    # Synthetic one-row HTML tests the parser without depending on a local cache.
    header = ["ID", "Name", "PH Info", "Is Complex", "Is Aerobic", "Is SubMedium", "Instructions"]
    html = (
        "<table><tr>"
        + "".join("<td>" + c + "</td>" for c in header)
        + "</tr>"
        + plan["sources"]["mapping"]["snippet"]
        + "</table>"
    )
    mapping = tmp_path / "mapping.html"
    mapping.write_text(html)
    meta = copy.deepcopy(repair.MAPPING_META)
    meta["sha256"] = repair.runner.sha(html.encode())
    monkeypatch.setattr(repair, "MAPPING_META", meta)
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
    return repo, medium, solution, mapping


def preview(fixture, tmp_path):
    path = tmp_path / "plan.json"
    plan, result = repair.process(*fixture, path, "preview")
    assert result["changed"] == 0 and result["scoped_claims"] == 52
    return path, plan


def test_preview_apply_verify_noop_and_independent_inversion(fixture, tmp_path):
    path, plan = preview(fixture, tmp_path)
    counts = []
    for item in plan["records"]:
        before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
        counts.append(auditor().check(before, after, item, plan["sources"]))
        assert not repair.runner.errors(after, item["target_class"])
    assert sum(c["new_evidence"] for c in counts) == 20
    assert repair.process(*fixture, path, "apply")[1]["changed"] == 3
    assert repair.process(*fixture, path, "verify")[1]["already_applied"] == 3
    assert repair.process(*fixture, path, "apply")[1]["changed"] == 0
    repair.report(tmp_path / "reports", plan, True)
    for item in plan["records"]:
        text = (tmp_path / "reports" / (item["key"] + "-followup.md")).read_text()
        assert text.count("- Follow-up target:") == 1 and "- Record:" not in text
        assert item["path"] in text and item["after_sha256"] in text
        assert text.count("| ") >= len(item["claims"])


@pytest.mark.parametrize("target", ["medium", "solution", "mapping"])
def test_source_byte_drift_refuses_batch(fixture, tmp_path, target):
    path, _ = preview(fixture, tmp_path)
    file = {
        "medium": fixture[1] / "111.json",
        "solution": fixture[2] / "190.json",
        "mapping": fixture[3],
    }[target]
    file.write_bytes(file.read_bytes() + b" ")
    with pytest.raises(ValueError, match="hash"):
        repair.process(*fixture, path, "apply")
    assert git(fixture[0], "diff", "--name-only") == b""


@pytest.mark.parametrize("target", list(repair.TARGETS))
def test_concurrent_edit_and_partial_apply_refused(fixture, tmp_path, target):
    path, _ = preview(fixture, tmp_path)
    file = fixture[0] / repair.TARGETS[target]["path"]
    file.write_bytes(file.read_bytes() + b"\n# concurrent edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(*fixture, path, "apply")
    for key, spec in repair.TARGETS.items():
        if key != target:
            assert (
                repair.runner.sha((fixture[0] / spec["path"]).read_bytes()) == spec["before_sha256"]
            )


@pytest.mark.parametrize("change", ["step", "unit", "hydrate", "volume", "id", "optional"])
def test_rehashed_source_semantic_drift_refused(change, monkeypatch):
    sources = frozen()["sources"]
    doc = json.loads(sources[repair.MEDIUM]["raw"])
    data = doc["data"]["solutions"][0]
    if change == "step":
        data["steps"][0]["step"] = repair.STEP.replace("50 ml", "500 ml")
    elif change == "volume":
        data["volume"] = 1000
    elif change == "id":
        data["id"] = 191
    elif change == "hydrate":
        data["recipe"][3]["compound"] = "MgSO4"
    else:
        data["recipe"][0][change] = "mg" if change == "unit" else 1
    raw = json.dumps(doc)
    sources[repair.MEDIUM]["raw"] = raw
    digest = repair.runner.sha(raw.encode())
    sources[repair.MEDIUM]["metadata"]["sha256"] = digest
    monkeypatch.setitem(repair.HASHES, repair.MEDIUM, digest)
    with pytest.raises(ValueError, match="drift"):
        repair.check_sources(sources)


def test_plan_tampering_and_preview_overwrite_refused(fixture, tmp_path):
    path, plan = preview(fixture, tmp_path)
    with pytest.raises(ValueError, match="overwrite"):
        repair.process(*fixture, path, "preview")
    plan["records"][0]["claims"][0]["snippet"] = "Invented evidence"
    path.write_text(json.dumps(plan))
    with pytest.raises(ValueError, match="Frozen plan"):
        repair.process(*fixture, path, "apply")
    assert git(fixture[0], "diff", "--name-only") == b""


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
        specs["komodo"]["path"] = specs["komodo"]["path"].replace("KOMODO_111", "komodo_111")
    with pytest.raises((ValueError, FileNotFoundError)):
        repair.process(*fixture, tmp_path / "plan.json", "preview")


@pytest.mark.parametrize(
    "change",
    ["stock_rate", "water_rate", "dose", "snippet", "mapping", "history", "ph", "stock_ph"],
)
def test_independent_audit_rejects_scientific_or_provenance_regressions(change):
    plan = frozen()
    item = plan["records"][0]
    before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
    glucose = after["solutions"][0]["composition"][0]
    if change == "stock_rate":
        glucose["concentration"] = {"value": "200", "unit": "G_PER_L"}
    elif change == "water_rate":
        after["ingredients"][-1]["concentration"]["unit"] = "ML_PER_L"
    elif change == "dose":
        after["solutions"][0]["concentration"] = {"value": "50", "unit": "ML_PER_L"}
    elif change == "snippet":
        glucose["evidence"][0]["snippet"] = "Invented evidence"
    elif change == "mapping":
        glucose["term"]["id"] = "CHEBI:15377"
    elif change == "history":
        after["curation_history"][0]["curator"] = "wrong"
    elif change == "stock_ph":
        after["solutions"][0]["preparation_notes"] = repair.STEP
    else:
        after["ph_value"] = 7
    with pytest.raises(AssertionError):
        auditor().check(before, after, item, plan["sources"])


def test_applied_records_and_explicit_prior_claim_resolutions():
    plan = frozen()
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert repair.runner.sha(raw) == item["after_sha256"]
        before, after = repair.runner.load_yaml(item["before_text"]), repair.runner.load_yaml(raw)
        auditor().check(before, after, item, plan["sources"])
        if item["key"] == "komodo":
            assert item["claim_resolutions"] == []
            continue
        folder = (
            "20261007-mediadive-solutions-0000-0500"
            if item["key"] == "solution"
            else "20261007-mediadive-media-0000-0500"
        )
        historical = json.loads((HERE.parent / folder / "plan.json").read_text())
        old = next(r for r in historical["records"] if r["path"] == item["path"])
        assert repair.runner.followup_result_hash(old, [item]) == (item["after_sha256"], 1)
        ref = repair.SOLUTION if item["key"] == "solution" else repair.MEDIUM
        resolved = [
            repair.runner.resolved_claim(old, c, [item], plan["sources"][ref]["raw"])
            for c in old["claims"]
            if c["status"] in repair.runner.SUPPORTED
        ]
        assert len(resolved) == 10 and sum(r[2] for r in resolved) == 1
