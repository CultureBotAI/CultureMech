"""Source scope, annotation retention, audit and guarded-apply regression tests."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_methanogen_stock_boundaries as repair

spec = importlib.util.spec_from_file_location(
    "methanogen_boundaries_audit", repair.HERE / "audit.py"
)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}


@pytest.mark.parametrize("key", ITEMS)
def test_complete_source_backed_projection(key):
    item = ITEMS[key]
    before = repair.runner.load_yaml(item["before_text"])
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original
    assert after == repair.runner.load_yaml(item["after_text"])
    assert (claims, lineage) == (item["claims"], item["lineage"])
    assert audit.check(before, after, item)["new_curation_history"] == 1


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize("change", ["id", "ingredients", "references"])
def test_baseline_drift_refused(key, change):
    before = repair.runner.load_yaml(ITEMS[key]["before_text"])
    before[change] = "changed"
    with pytest.raises(ValueError, match="baseline"):
        repair.build(before, key, PLAN["created_at"])


@pytest.mark.parametrize("key", ["url", "response_url", "http_status", "sha256"])
def test_capture_drift_refused(key):
    context = copy.deepcopy(repair.frozen())
    context["sources"]["J985"]["metadata"][key] = "changed"
    with pytest.raises(ValueError, match="Capture drift"):
        repair.sources(context)


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "dose",
        "batch_rate",
        "grounding",
        "quote",
        "locator",
        "history",
        "year",
        "extra_stock",
        "missing_stock",
        "root",
        "stock_rate",
    ],
)
def test_independent_audit_rejects_wrong_claims(key, mutation):
    item = ITEMS[key]
    before = repair.runner.load_yaml(item["before_text"])
    after = repair.runner.load_yaml(item["after_text"])
    leaf = after["ingredients"][1]
    if mutation == "dose":
        after["solutions"][0]["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "batch_rate":
        leaf["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "grounding":
        leaf["term"]["id"] = "CHEBI:15377"
    elif mutation == "quote":
        leaf["evidence"][0]["snippet"] = "fabricated"
    elif mutation == "locator":
        leaf["evidence"][0]["explanation"] = "No claim linkage"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "changed"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "extra_stock":
        after["solutions"].append(copy.deepcopy(after["solutions"][0]))
    elif mutation == "missing_stock":
        after["solutions"][0]["composition"].pop()
    elif mutation == "root":
        after["ph_value"] = 7.0
    elif mutation == "stock_rate":
        after["solutions"][0]["composition"][0]["concentration"] = {"value": "1", "unit": "G_PER_L"}
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ITEMS)
def test_audit_rejects_missing_old_claim(key):
    item = copy.deepcopy(ITEMS[key])
    item["claims"] = [
        c for c in item["claims"] if c["old_pointer"] != ["ingredients", 1, "concentration"]
    ]
    with pytest.raises(AssertionError):
        audit.check(
            repair.runner.load_yaml(item["before_text"]),
            repair.runner.load_yaml(item["after_text"]),
            item,
        )


def fixture_repo(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    targets = []
    for item in ITEMS.values():
        target = tmp_path / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(item["before_text"])
        targets.append(target)
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    original = subprocess.check_output

    def output(args, **kwargs):
        if args == ["git", "rev-parse", "HEAD"]:
            return PLAN["commit"] + "\n"
        return original(args, **kwargs)

    monkeypatch.setattr(subprocess, "check_output", output)
    return targets


def test_preview_apply_readback_and_noop(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    initial = [p.read_bytes() for p in targets]
    plan_path = tmp_path / "plan.json"
    plan, result = repair.process(tmp_path, plan_path, "preview")
    assert [p.read_bytes() for p in targets] == initial and result["changed"] == 0
    assert repair.process(tmp_path, plan_path, "apply")[1]["changed"] == 3
    applied = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan_path, "verify")[1]["already_applied"] == 3
    assert repair.process(tmp_path, plan_path, "apply")[1]["changed"] == 0
    assert (
        [p.read_bytes() for p in targets]
        == applied
        == [r["after_text"].encode() for r in plan["records"]]
    )
    with pytest.raises(ValueError, match="overwrite"):
        repair.process(tmp_path, plan_path, "preview")


def test_concurrent_edit_refused_before_any_write(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan_path = tmp_path / "plan.json"
    repair.process(tmp_path, plan_path, "preview")
    targets[-1].write_text(targets[-1].read_text() + "\n# concurrent note\n")
    current = [p.read_bytes() for p in targets]
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan_path, "apply")
    assert [p.read_bytes() for p in targets] == current


def test_forged_plan_refused(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan_path = tmp_path / "plan.json"
    plan, _ = repair.process(tmp_path, plan_path, "preview")
    plan["records"][0]["after_text"] += "\n# changed plan\n"
    plan_path.write_text(json.dumps(plan))
    with pytest.raises(ValueError, match="Frozen decision drift"):
        repair.process(tmp_path, plan_path, "apply")
    assert targets[0].read_text() == ITEMS["J985"]["before_text"]


def test_symlink_refused(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    target = targets[-1]
    original = target.with_suffix(".original")
    target.rename(original)
    target.symlink_to(original)
    with pytest.raises(ValueError, match="symlink"):
        repair.process(tmp_path, tmp_path / "plan.json", "preview")
