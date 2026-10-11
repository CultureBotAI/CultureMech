"""Offline preparation semantics and guarded-write tests for medium 489."""

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_dsmz489_stocks as repair  # noqa: E402


def frozen():
    return json.loads((repair.HERE / "plan.json").read_text())


def auditor():
    spec = importlib.util.spec_from_file_location("dsmz489_audit", repair.HERE / "audit.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def fixture(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    plan = frozen()
    for item in plan["records"]:
        path = root / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    for args in (
        ("init", "-q"),
        ("add", "data"),
        ("-c", "user.name=Test", "-c", "user.email=test@example.org", "commit", "-qm", "baseline"),
    ):
        subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
    return root, plan["sources"], tmp_path / "plan.json"


def test_preview_apply_verify_noop(fixture):
    plan, result = repair.process(*fixture, "preview")
    assert result["changed"] == 0 and result["records"] == 3 and result["scoped_claims"] == 76
    counts = []
    for item in plan["records"]:
        before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
        counts.append(auditor().check(before, after, item, plan["sources"]))
    assert sum(c["new_evidence"] for c in counts) == 23
    assert sum(c["unsupported_quantity_slots_removed"] for c in counts) == 6
    assert repair.process(*fixture, "apply")[1]["changed"] == 3
    assert repair.process(*fixture, "verify")[1]["already_applied"] == 3
    assert repair.process(*fixture, "apply")[1]["changed"] == 0
    folder = fixture[2].parent / "reports"
    repair.report(folder, plan, True)
    for item in plan["records"]:
        report = (folder / (item["key"] + "-followup.md")).read_text()
        assert report.count("- Follow-up target:") == 1 and "- Record:" not in report
        assert item["path"] in report and item["after_sha256"] in report
        assert "unsupported" in report
        if item["key"] == "solution":
            assert "not verified composition" in report


@pytest.mark.parametrize("key", list(repair.TARGETS))
def test_concurrent_edit_prevents_all_writes(fixture, key):
    repair.process(*fixture, "preview")
    path = fixture[0] / repair.TARGETS[key]["path"]
    path.write_bytes(path.read_bytes() + b"\n# concurrent\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(*fixture, "apply")
    for other, spec in repair.TARGETS.items():
        if key != other:
            assert (
                repair.runner.sha((fixture[0] / spec["path"]).read_bytes()) == spec["before_sha256"]
            )


@pytest.mark.parametrize("kind", ["symlink", "untracked", "case"])
def test_exact_tracked_target_guard(fixture, monkeypatch, kind):
    targets = copy.deepcopy(repair.TARGETS)
    monkeypatch.setattr(repair, "TARGETS", targets)
    path = fixture[0] / targets["komodo"]["path"]
    if kind == "symlink":
        path.rename(path.with_suffix(".backup"))
        path.symlink_to(path.with_suffix(".backup").name)
    elif kind == "untracked":
        subprocess.run(
            ["git", "rm", "--cached", targets["komodo"]["path"]],
            cwd=fixture[0],
            check=True,
            capture_output=True,
        )
    else:
        targets["komodo"]["path"] = targets["komodo"]["path"].replace("KOMODO", "komodo")
    with pytest.raises((ValueError, FileNotFoundError)):
        repair.process(*fixture, "preview")


@pytest.mark.parametrize("ref", list(repair.HASHES))
def test_source_byte_drift(fixture, ref):
    fixture[1][ref]["raw"] += " "
    with pytest.raises(ValueError, match="source drift"):
        repair.process(*fixture, "preview")


@pytest.mark.parametrize(
    "change", ["strength", "dose", "hydrate", "step", "volume", "optional", "unit"]
)
def test_rehashed_semantic_drift(change, monkeypatch):
    sources = frozen()["sources"]
    ref = repair.reference_for("dsmz")
    payload = json.loads(sources[ref]["raw"])
    data = payload["data"]["solutions"][0]
    if change == "strength":
        data["recipe"][8]["attribute"] = "1% w/v"
    elif change == "dose":
        data["recipe"][8]["amount"] = 5
    elif change == "hydrate":
        data["recipe"][10]["compound"] = "Na2S"
    elif change == "step":
        data["steps"][0]["step"] = data["steps"][0]["step"].replace("After", "Before")
    elif change == "volume":
        data["volume"] = 500
    else:
        data["recipe"][9][change] = 1 if change == "optional" else "mg"
    raw = json.dumps(payload)
    digest = repair.runner.sha(raw.encode())
    sources[ref]["raw"] = raw
    sources[ref]["metadata"]["sha256"] = digest
    monkeypatch.setitem(repair.HASHES, ref, digest)
    with pytest.raises(ValueError, match="drift"):
        repair.check_sources(sources)


@pytest.mark.parametrize(
    "change", ["stock_strength", "stock_dose", "water", "ontology", "history", "snippet", "growth"]
)
def test_independent_audit_rejects_tampering(change):
    plan = frozen()
    item = plan["records"][0]
    before, after = [repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")]
    if change == "stock_strength":
        after["solutions"][1]["composition"][0]["concentration"] = {
            "value": "0.15",
            "unit": "G_PER_L",
        }
    elif change == "stock_dose":
        after["solutions"][0]["concentration"]["unit"] = "ML_PER_L"
    elif change == "water":
        after["ingredients"][8]["concentration"]["value"] = "1000"
    elif change == "ontology":
        after["solutions"][0]["composition"][0]["term"]["id"] = "CHEBI:15377"
    elif change == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif change == "snippet":
        after["solutions"][2]["composition"][0]["evidence"][0]["snippet"] = "invented"
    else:
        after["applications"].append("Unsupported growth claim")
    with pytest.raises(AssertionError):
        auditor().check(before, after, item, plan["sources"])


def test_frozen_plan_tamper_rejected(fixture):
    plan, _ = repair.process(*fixture, "preview")
    plan["records"][0]["claims"][0]["explanation"] = "unreviewed"
    fixture[2].write_text(json.dumps(plan))
    with pytest.raises(ValueError, match="Frozen plan/decision drift"):
        repair.process(*fixture, "apply")
