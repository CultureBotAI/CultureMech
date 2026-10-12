"""Nested source scopes, exceptional strengths and guarded write regressions."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_m142_nested_traces as repair

spec = importlib.util.spec_from_file_location("m142_nested_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}


@pytest.mark.parametrize("key", ITEMS)
def test_projection_and_independent_audit(key):
    item = ITEMS[key]
    before = repair.runner.load_yaml(item["before_text"])
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original
    assert after == repair.runner.load_yaml(item["after_text"])
    assert claims == item["claims"] and lineage == item["lineage"]
    assert audit.check(before, after, item)["new_curation_history"] == 1


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "batch_rate",
        "dose_basis",
        "stock_missing",
        "stock_extra",
        "water",
        "annotation",
        "quote",
        "history",
        "year",
        "root_preparation",
        "nested_preparation",
    ],
)
def test_reject_unreviewed_changes(key, mutation):
    item = ITEMS[key]
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    nodes = [n for p, n in audit.walk(after) if n.get("preferred_term")]
    mass = next(n for n in nodes if "Source batch input:" in n.get("notes", ""))
    if mutation == "batch_rate":
        mass["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "dose_basis":
        after["solutions"][0]["concentration"]["unit"] = "G_PER_L"
    elif mutation == "stock_missing":
        after["solutions"].pop()
    elif mutation == "stock_extra":
        after["solutions"].append(copy.deepcopy(after["solutions"][0]))
    elif mutation == "water":
        next(n for n in nodes if n["preferred_term"] == "Distilled water")["concentration"][
            "value"
        ] = "9"
    elif mutation == "annotation":
        mass["term"] = {"id": "CHEBI:0000000", "label": "deliberately incorrect test term"}
    elif mutation == "quote":
        mass["evidence"][0]["snippet"] = "invented"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "overwritten"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "root_preparation":
        after["preparation_steps"][0]["description"] = "Fill final medium to one liter."
    elif mutation == "nested_preparation":
        next(n for n in nodes if n["preferred_term"] == "Trace minerals (see Medium [M142])")[
            "preparation_notes"
        ] = "Adjust receiving medium pH to 7.0."
    with pytest.raises((AssertionError, KeyError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key, mutation",
    [
        ("M1153", "iron"),
        ("M1153", "acid"),
        ("M1153", "formula"),
        ("M1378", "percent"),
        ("M1378", "dose"),
        ("M933", "nickel"),
    ],
)
def test_exceptional_source_decisions(key, mutation):
    item = ITEMS[key]
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    if mutation == "iron":
        after["solutions"][1]["composition"][0]["concentration"]["value"] = "40"
    elif mutation == "acid":
        after["solutions"][1]["solutions"][0]["concentration"] = {"value": "0.1", "unit": "L"}
    elif mutation == "formula":
        after["solutions"][0]["composition"][2]["notes"] = "Identity verified."
    elif mutation == "percent":
        after["solutions"][0]["composition"][0]["concentration"]["unit"] = "PERCENT_V_V"
    elif mutation == "dose":
        after["solutions"][0]["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "nickel":
        after["solutions"][0]["composition"][8]["notes"] = "Source batch input: 1 g."
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ITEMS)
def test_every_old_quantity_accounted(key):
    item = copy.deepcopy(ITEMS[key])
    item["claims"] = [
        c for c in item["claims"] if c["old_pointer"] != ["ingredients", 0, "concentration"]
    ]
    with pytest.raises(AssertionError):
        audit.check(
            repair.runner.load_yaml(item["before_text"]),
            repair.runner.load_yaml(item["after_text"]),
            item,
        )


def fixture_repo(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    targets = []
    for r in PLAN["records"]:
        path = tmp_path / r["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(r["before_text"])
        targets.append(path)
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
    before = [p.read_bytes() for p in targets]
    plan = tmp_path / "plan.json"
    repair.process(tmp_path, plan, "preview")
    assert [p.read_bytes() for p in targets] == before
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 7
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 7
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
    assert targets[0].read_text() == ITEMS["M933"]["before_text"]
