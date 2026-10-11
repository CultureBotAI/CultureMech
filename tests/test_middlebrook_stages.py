"""Challenge Middlebrook units, stock boundaries, sources and guarded application."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_middlebrook_stages as repair

spec = importlib.util.spec_from_file_location("middlebrook_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}


def records(key):
    item = copy.deepcopy(ITEMS[key])
    return (
        item,
        repair.runner.load_yaml(item["before_text"]),
        repair.runner.load_yaml(item["after_text"]),
    )


@pytest.mark.parametrize("key", ITEMS)
def test_independent_source_projection_and_complete_accounting(key):
    item, before, expected = records(key)
    snapshot = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == snapshot and after == expected
    assert claims == item["claims"] and lineage == item["lineage"]
    assert audit.check(before, after, item)["old_quantity_slots"] >= 8


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "mass",
        "flatten",
        "duplicate",
        "history",
        "mapping",
        "snippet",
        "claim",
        "lineage",
        "title",
        "year",
        "provenance",
        "old_amount",
    ],
)
def test_independent_audit_rejects_corruption(key, mutation):
    item, before, after = records(key)
    stock = after["solutions"][-1]
    node = stock["composition"][0]
    if mutation == "mass":
        node["concentration"] = {"value": "100", "unit": "G_PER_L"}
    elif mutation == "flatten":
        after["ingredients"].append(stock["composition"].pop())
    elif mutation == "duplicate":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif mutation == "mapping":
        node["term"] = {"id": "CHEBI:123", "label": "fabricated"}
    elif mutation == "snippet":
        node["evidence"][0]["snippet"] = "fabricated"
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "title":
        after["references"][0]["title"] = "Different medium"
    elif mutation == "year":
        after["references"][0]["year"] = 2007
    elif mutation == "provenance":
        after["notes"] = "Corrected."
    else:
        item["claims"][0]["old"] = {"value": "1000", "unit": "G_PER_L"}
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


def test_source_specific_catalase_and_percent_bases():
    _, _, d = records("D857")
    assert d["solutions"][0]["composition"][2]["concentration"] == {
        "value": "0.003",
        "unit": "G_PER_L",
    }
    _, _, m = records("M2403")
    assert m["solutions"][1]["concentration"] == {"value": "10", "unit": "PERCENT_V_V"}
    assert all("concentration" not in n for n in m["ingredients"])
    cat = m["solutions"][1]["composition"][3]
    assert "concentration" not in cat and "3 mg" in cat["notes"]


def test_preserves_genuine_casein_and_salt_but_not_lb_substitutions():
    for key in ("M1946", "M2407"):
        _, _, after = records(key)
        assert any("pancreatic digest" in n["preferred_term"].lower() for n in after["ingredients"])
        assert after["solutions"][0]["composition"][1]["preferred_term"] == "Sodium chloride"
        assert not any(
            "LB Medium" in n.get("supplier_catalog", {}).get("supplier_name", "")
            for p, n in audit.walk(after)
        )


def test_half_scale_powder_details_are_not_extra_finished_medium_ingredients():
    for key, amount in (("M2400", "2.35"), ("M2401", "10.25")):
        _, _, after = records(key)
        assert len(after["ingredients"]) == 2
        assert len(after["solutions"]) == 2
        base = after["solutions"][0]
        assert amount + " g" in base["notes"] and "concentration" not in base
        assert all("concentration" not in n for n in base["composition"])


def fixture_repo(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    targets = []
    for item in ITEMS.values():
        target = tmp_path / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(item["before_text"])
        targets.append(target)
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    original = subprocess.check_output
    monkeypatch.setattr(
        subprocess,
        "check_output",
        lambda args, **kwargs: (
            PLAN["commit"] + "\n"
            if args == ["git", "rev-parse", "HEAD"]
            else original(args, **kwargs)
        ),
    )
    return targets


def test_preview_apply_verify_noop(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan = tmp_path / "plan.json"
    before = [p.read_bytes() for p in targets]
    repair.process(tmp_path, plan, "preview")
    assert [p.read_bytes() for p in targets] == before
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 13
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 13
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert [p.read_bytes() for p in targets] == after


def test_concurrent_edit_prevents_all_writes(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan = tmp_path / "plan.json"
    repair.process(tmp_path, plan, "preview")
    targets[-1].write_text(targets[-1].read_text() + "# concurrent\n")
    before = [p.read_bytes() for p in targets]
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    assert [p.read_bytes() for p in targets] == before
