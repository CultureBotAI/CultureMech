"""Source overrides, annotation retention and guarded writes for JCM261."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_j261_variant as repair

spec = importlib.util.spec_from_file_location("j261_independent_audit", repair.HERE / "audit.py")
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


@pytest.mark.parametrize("key", ["J261", "M253"])
@pytest.mark.parametrize(
    "mutation",
    [
        "batch_rate",
        "dose_unit",
        "stock_missing",
        "stock_extra",
        "water",
        "annotation",
        "quote",
        "history",
        "ph",
        "year",
        "percentage",
        "final_rate",
        "sulfur",
        "parent_path",
        "relationship",
        "inherited_ph",
        "double_parent",
        "stock_prep",
    ],
)
def test_audit_rejects_bad_child_edits(key, mutation):
    item = ITEMS[key]
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    leaf = after["ingredients"][0]
    if mutation == "batch_rate":
        leaf["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "dose_unit":
        after["solutions"][0]["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "stock_missing":
        after["solutions"][0]["composition"].pop()
    elif mutation == "stock_extra":
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
        after["ph_value"] = 6.5
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "percentage":
        after["solutions"][2]["concentration"] = {"value": "5", "unit": "PERCENT_W_V"}
    elif mutation == "final_rate":
        next(n for n in after["ingredients"] if n["preferred_term"].startswith("Yeast"))[
            "concentration"
        ]["value"] = "3"
    elif mutation == "sulfur":
        after["ingredients"].append(
            {"preferred_term": "Sulfur", "concentration": {"value": "30", "unit": "G_PER_L"}}
        )
    elif mutation == "parent_path":
        after["parent_media"][
            "path"
        ] = "data/normalized_yaml/bacterial/JCM_J151_PYROCOCCUS_MEDIUM.yaml"
    elif mutation == "relationship":
        after["variant_relationship"] = "SOURCE_DUPLICATE"
    elif mutation == "inherited_ph":
        after["preparation_steps"][2]["description"] = "Readjust receiving-medium pH to 6.5."
    elif mutation == "double_parent":
        after["solutions"].append({"preferred_term": "Entire parent medium", "composition": []})
    elif mutation == "stock_prep":
        after["solutions"][1]["preparation_notes"] = "Use final-medium pH 6.5."
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ["J151", "M142"])
@pytest.mark.parametrize("field", ["ingredients", "solutions", "evidence", "ph_value"])
def test_parent_scientific_claims_unchanged(key, field):
    item = ITEMS[key]
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    after.pop(field)
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ["J261", "M253"])
def test_old_claim_cannot_be_dropped(key):
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
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 4
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 4
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
    assert targets[0].read_text() == ITEMS["J261"]["before_text"]
