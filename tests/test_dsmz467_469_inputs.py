"""Offline source, preparation-boundary and guarded-write regression tests."""

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_dsmz467_469_inputs as repair  # noqa: E402
import review_komodo_concentration_evidence as komodo  # noqa: E402

HERE = repair.HERE


def frozen():
    return json.loads((HERE / "plan.json").read_text())


def auditor():
    spec = importlib.util.spec_from_file_location("inputs_audit", HERE / "audit.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL)


@pytest.fixture
def fixture(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    plan = frozen()
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
    return repo, plan["sources"], tmp_path / "plan.json"


def test_preview_apply_verify_noop(fixture, tmp_path):
    plan, result = repair.process(*fixture, "preview")
    assert result["changed"] == 0 and result["scoped_claims"] == 59
    counts = []
    for item in plan["records"]:
        before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
        counts.append(auditor().check(before, after, item, plan["sources"]))
        assert not repair.runner.errors(before, item["target_class"])
        assert not repair.runner.errors(after, item["target_class"])
    assert sum(c["new_evidence"] for c in counts) == 30
    assert sum(c["quantity_corrections"] for c in counts) == 4
    assert sum(c["unsupported_quantity_slots_removed"] for c in counts) == 6
    assert repair.process(*fixture, "apply")[1]["changed"] == 6
    assert repair.process(*fixture, "verify")[1]["already_applied"] == 6
    assert repair.process(*fixture, "apply")[1]["changed"] == 0
    repair.report(tmp_path / "reports", plan, True)
    for item in plan["records"]:
        text = (tmp_path / "reports" / (item["key"] + "-followup.md")).read_text()
        assert text.count("- Follow-up target:") == 1 and "- Record:" not in text
        assert item["path"] in text and item["after_sha256"] in text
        assert "unsupported" in text or "verified" in text


@pytest.mark.parametrize("key", list(repair.TARGETS))
def test_concurrent_edit_aborts_before_any_write(fixture, key):
    repair.process(*fixture, "preview")
    target = fixture[0] / repair.TARGETS[key]["path"]
    target.write_bytes(target.read_bytes() + b"\n# concurrent edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(*fixture, "apply")
    for other, spec in repair.TARGETS.items():
        if other != key:
            assert (
                repair.runner.sha((fixture[0] / spec["path"]).read_bytes()) == spec["before_sha256"]
            )


@pytest.mark.parametrize("kind", ["symlink", "untracked", "case"])
def test_exact_tracked_paths_required(fixture, monkeypatch, kind):
    specs = copy.deepcopy(repair.TARGETS)
    monkeypatch.setattr(repair, "TARGETS", specs)
    target = fixture[0] / specs["469-komodo"]["path"]
    if kind == "symlink":
        target.rename(target.with_suffix(".backup"))
        target.symlink_to(target.with_suffix(".backup").name)
    elif kind == "untracked":
        git(fixture[0], "rm", "--cached", specs["469-komodo"]["path"])
    else:
        specs["469-komodo"]["path"] = specs["469-komodo"]["path"].replace(
            "KOMODO_469", "komodo_469"
        )
    with pytest.raises((ValueError, FileNotFoundError)):
        repair.process(*fixture, "preview")


@pytest.mark.parametrize("ref", list(repair.HASHES))
def test_source_byte_drift(fixture, ref):
    fixture[1][ref]["raw"] += " "
    with pytest.raises(ValueError, match="Source hash"):
        repair.process(*fixture, "preview")
    assert git(fixture[0], "diff", "--name-only") == b""


@pytest.mark.parametrize(
    "change", ["water", "step", "hydrate", "attribute", "volume", "id", "unit", "optional"]
)
def test_rehashed_semantic_source_drift(change, monkeypatch):
    sources = frozen()["sources"]
    ref = repair.API + "medium/469"
    doc = json.loads(sources[ref]["raw"])
    data = doc["data"]["solutions"][0]
    if change == "water":
        data["recipe"][-1]["amount"] = 1000
    elif change == "step":
        data["steps"][0]["step"] = repair.STEP.replace("each", "combined")
    elif change == "hydrate":
        data["recipe"][3]["compound"] = "MgSO4"
    elif change == "attribute":
        data["recipe"][5]["attribute"] = "Other product"
    elif change in {"volume", "id"}:
        data[change] += 1
    else:
        data["recipe"][3][change] = "mg" if change == "unit" else 1
    raw = json.dumps(doc)
    sources[ref]["raw"] = raw
    digest = repair.runner.sha(raw.encode())
    sources[ref]["metadata"]["sha256"] = digest
    monkeypatch.setitem(repair.HASHES, ref, digest)
    with pytest.raises(ValueError, match="drift"):
        repair.check_sources(sources)


def test_plan_edit_and_preview_overwrite_refused(fixture):
    plan, _ = repair.process(*fixture, "preview")
    with pytest.raises(ValueError, match="overwrite"):
        repair.process(*fixture, "preview")
    plan["records"][0]["claims"][0]["snippet"] = "Invented evidence"
    fixture[2].write_text(json.dumps(plan))
    with pytest.raises(ValueError, match="Frozen plan"):
        repair.process(*fixture, "apply")
    assert git(fixture[0], "diff", "--name-only") == b""


@pytest.mark.parametrize(
    "change",
    [
        "strength",
        "dose",
        "water",
        "snippet",
        "mapping",
        "history",
        "ph",
        "preparation",
        "pdf",
        "source_difference",
    ],
)
def test_independent_audit_rejects_regressions(change):
    plan = frozen()
    item = next(i for i in plan["records"] if i["key"] == "469-dsmz")
    before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
    solute = after["solutions"][0]["composition"][0]
    if change == "strength":
        solute["concentration"] = {"value": "20", "unit": "G_PER_L"}
    elif change == "dose":
        after["solutions"][0]["concentration"] = {"value": "10", "unit": "ML_PER_L"}
    elif change == "water":
        after["solutions"][1]["composition"][1]["concentration"]["unit"] = "ML_PER_L"
    elif change == "snippet":
        solute["evidence"][0]["snippet"] = "Wrong quote"
    elif change == "mapping":
        solute["term"]["id"] = "CHEBI:15377"
    elif change == "history":
        after["curation_history"][0]["curator"] = "Wrong curator"
    elif change == "ph":
        after["ph_value"] = 8.5
    elif change == "preparation":
        after["solutions"][0]["preparation_notes"] = repair.STEP
    elif change == "pdf":
        after["evidence"][1]["snippet"] = "980 ml"
    else:
        after["notes"] = "Both sources specify 980/10/10."
    with pytest.raises(AssertionError):
        auditor().check(before, after, item, plan["sources"])


def historical_komodo():
    plan = json.loads((HERE.parent / "20261007-komodo-media-1500-2000/plan.json").read_text())
    plan["records"] = [r for r in plan["records"] if r["medium_id"] == "467"]
    assert len(plan["records"]) == 1
    return plan


def test_mapping_verification_requires_explicit_followup_and_preserves_history(fixture):
    new, _ = repair.process(*fixture, "preview")
    repair.process(*fixture, "apply")
    old = historical_komodo()
    with pytest.raises(ValueError, match="hash"):
        komodo.verify_mapping(fixture[0], old)
    assert komodo.verify_mapping(fixture[0], old, new["records"])["verified_mapping_snippets"] == 1
    successors = copy.deepcopy(new["records"])
    target = next(r for r in successors if r["key"] == "467-komodo")
    doc = repair.runner.load_yaml(target["after_text"])
    doc["curation_history"].pop(-2)
    raw = repair.runner.render(target["after_text"], doc)
    target["after_text"] = raw.decode()
    target["after_sha256"] = repair.runner.sha(raw)
    (fixture[0] / target["path"]).write_bytes(raw)
    with pytest.raises(ValueError, match="Historical curation"):
        komodo.verify_mapping(fixture[0], old, successors)


def test_applied_records_and_historical_claim_resolutions():
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
        if item["key"].startswith("467") or item["key"].endswith("komodo"):
            assert item["claim_resolutions"] == []
            continue
        folder = (
            "20261007-mediadive-solutions-0500-1000"
            if item["key"].endswith("solution")
            else "20261007-mediadive-media-0500-1000"
        )
        old = next(
            r
            for r in json.loads((HERE.parent / folder / "plan.json").read_text())["records"]
            if r["path"] == item["path"]
        )
        assert repair.runner.followup_result_hash(old, [item]) == (item["after_sha256"], 1)
        resolved = [
            repair.runner.resolved_claim(
                old, c, [item], plan["sources"][repair.reference_for(item["key"])]["raw"]
            )
            for c in old["claims"]
            if c["status"] in repair.runner.SUPPORTED
        ]
        assert len(resolved) == 5 and sum(r[2] for r in resolved) == 1
