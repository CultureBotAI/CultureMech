"""Evidence integrity, source scope and guarded publication regressions."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_jcm_stock_preparations as repair

spec = importlib.util.spec_from_file_location("jcm_preparations_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}


@pytest.mark.parametrize("key", ITEMS)
def test_source_projection_and_independent_audit(key):
    item = ITEMS[key]
    before = repair.runner.load_yaml(item["before_text"])
    saved = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == saved
    assert after == repair.runner.load_yaml(item["after_text"])
    assert claims == item["claims"] and lineage == item["lineage"]
    assert audit.check(before, after, item)["new_curation_history"] == 1


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "batch_concentration",
        "dose_unit",
        "missing_stock",
        "extra_stock",
        "water",
        "annotation",
        "quote",
        "history",
        "ph",
        "year",
        "preparation",
    ],
)
def test_audit_rejects_bad_edits(key, mutation):
    r = ITEMS[key]
    before, after = (repair.runner.load_yaml(r[x]) for x in ("before_text", "after_text"))
    leaf = next(n for p, n in audit.walk(after) if p[:1] == ("ingredients",) and "evidence" in n)
    if mutation == "batch_concentration":
        leaf["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "dose_unit":
        after["solutions"][0]["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "missing_stock":
        after["solutions"][0]["composition"].pop()
    elif mutation == "extra_stock":
        after["solutions"].append(copy.deepcopy(after["solutions"][0]))
    elif mutation == "water":
        water = next(
            n for p, n in audit.walk(after) if n.get("preferred_term") == "Distilled water"
        )
        water["concentration"]["value"] = "123"
    elif mutation == "annotation":
        leaf["term"] = {"id": "CHEBI:0000000", "label": "deliberately wrong test annotation"}
    elif mutation == "quote":
        leaf["evidence"][0]["snippet"] = "invented"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "overwritten"
    elif mutation == "ph":
        after["ph_value"] = 7.0
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "preparation":
        after["solutions"][-1]["concentration"] = {"value": "10", "unit": "PERCENT_W_V"}
    with pytest.raises(AssertionError):
        audit.check(before, after, r)


@pytest.mark.parametrize("key", ITEMS)
def test_old_claim_cannot_be_dropped(key):
    r = copy.deepcopy(ITEMS[key])
    r["claims"] = [
        c for c in r["claims"] if c["old_pointer"] != ["ingredients", 0, "concentration"]
    ]
    with pytest.raises(AssertionError):
        audit.check(
            repair.runner.load_yaml(r["before_text"]), repair.runner.load_yaml(r["after_text"]), r
        )


@pytest.mark.parametrize("field", ["url", "response_url", "http_status", "sha256"])
def test_capture_drift_refused(field):
    c = repair.frozen()
    c["sources"]["J151"]["metadata"][field] = "changed"
    with pytest.raises(ValueError, match="Capture drift"):
        repair.sources(c)


@pytest.mark.parametrize("key", ITEMS)
def test_baseline_drift_refused(key):
    before = repair.runner.load_yaml(ITEMS[key]["before_text"])
    before["ingredients"][0]["preferred_term"] = "changed"
    with pytest.raises(ValueError, match="baseline"):
        repair.build(before, key, PLAN["created_at"])


def fixture_repo(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    targets = []
    for r in ITEMS.values():
        p = tmp_path / r["path"]
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(r["before_text"])
        targets.append(p)
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    original = subprocess.check_output

    def output(args, **kwargs):
        return (
            PLAN["commit"] + "\n"
            if args == ["git", "rev-parse", "HEAD"]
            else original(args, **kwargs)
        )

    monkeypatch.setattr(subprocess, "check_output", output)
    return targets


def test_guarded_preview_apply_noop(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    original = [p.read_bytes() for p in targets]
    plan = tmp_path / "plan.json"
    repair.process(tmp_path, plan, "preview")
    assert [p.read_bytes() for p in targets] == original
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 6
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 6
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert [p.read_bytes() for p in targets] == after


def test_concurrent_edit_stops_all_writes(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan = tmp_path / "plan.json"
    repair.process(tmp_path, plan, "preview")
    targets[-1].write_text(targets[-1].read_text() + "\n# concurrent edit\n")
    before = [p.read_bytes() for p in targets]
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    assert [p.read_bytes() for p in targets] == before


def test_forged_plan_refused(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan = tmp_path / "plan.json"
    data, _ = repair.process(tmp_path, plan, "preview")
    data["records"][0]["claims"].pop()
    plan.write_text(json.dumps(data))
    with pytest.raises(ValueError, match="Frozen decision drift"):
        repair.process(tmp_path, plan, "apply")
    assert targets[0].read_text() == ITEMS["J151"]["before_text"]
