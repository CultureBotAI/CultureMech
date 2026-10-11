"""Exact-source extraction stages and explicit historical-claim resolution."""

import copy
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_extraction_input_boundaries as repair  # noqa: E402
import review_solution_concentration_evidence as runner  # noqa: E402

PLAN = ROOT / "reports/ingredient_concentration_curation/20261007-extraction-boundaries/plan.json"


@pytest.fixture(params=["12", "657"])
def example(request):
    plan = json.loads(PLAN.read_text())
    item = next(r for r in plan["records"] if r["medium_id"] == request.param)
    before = runner.load_yaml(item["before_text"])
    frozen = runner.load_yaml(item["after_text"])
    nodes = frozen["solutions"][0]["composition"] + frozen["ingredients"]
    rows = ",".join(n["evidence"][0]["snippet"] for n in nodes)
    step = item["claims"][0]["snippet"]
    medium = {
        "id": int(request.param),
        "name": before["original_name"],
        "source": "DSMZ",
        "link": repair.PDF.format(request.param),
    }
    # Frozen literal excerpts give offline source fixtures, not a network claim.
    raw = (
        '{"status":200,"count":1,"data":{"medium":'
        + json.dumps(medium)
        + ',"solutions":[{"id":'
        + str(repair.COHORT[request.param]["solution_id"])
        + ',"name":'
        + json.dumps("Main sol. " + request.param)
        + ',"volume":1000,"recipe":['
        + rows
        + '],"steps":['
        + step
        + "]}]}}"
    )
    meta = {"sha256": runner.sha(raw.encode()), "accessed_at": item["source_accessed_at"]}
    return item, before, raw, meta, plan["created_at"]


def build(example):
    item, before, raw, meta, timestamp = example
    return repair.build(before, raw, meta, item["medium_id"], timestamp)


def test_extraction_inputs_volume_and_recovered_agar_basis(example):
    item, before, _, _, _ = example
    after, claims, resolutions = build(example)
    stock = after["solutions"][0]
    assert [n["preferred_term"] for n in after["ingredients"]] == ["Agar"]
    assert "concentration" not in stock["composition"][0]
    assert stock["composition"][1]["concentration"] == {"value": "1", "unit": "L"}
    assert after["ingredients"][0]["concentration"] == before["ingredients"][2]["concentration"]
    assert "retained solids or dissolved yield" in stock["composition"][0]["notes"]
    assert "term" not in stock
    if item["medium_id"] == "12":
        assert "concentration" not in stock
        assert [r["disposition"] for r in resolutions] == ["withdrawn", "relocated"]
    else:
        assert stock["concentration"] == {"value": "1", "unit": "L"}
        assert [r["disposition"] for r in resolutions] == ["relocated"]
        assert "Make up volume to one liter." in stock["preparation_notes"]
        assert after["preparation_steps"][0]["action"] == "ADD_AGAR"
    full_text = " ".join(
        [stock["preparation_notes"], *[s["description"] for s in after["preparation_steps"]]]
    )
    assert full_text == before["preparation_steps"][0]["description"]
    for key in before.keys() - {
        "ingredients",
        "preparation_steps",
        "references",
        "curation_history",
    }:
        assert after[key] == before[key]
    for c in claims:
        entries = runner.get_node(after, c["evidence_pointer"])["evidence"]
        entry = next(e for e in entries if e["reference"] == c["reference"])
        assert c["field"] in entry["explanation"]
        assert c["snippet"] == entry["snippet"] or c["snippet"] in entry["explanation"]


@pytest.mark.parametrize(
    "damage",
    ["amount", "unit", "optional", "condition", "identity", "preparation", "notes", "variant"],
)
def test_ambiguous_or_drifted_inputs_fail_before_mutation(example, damage):
    item, before, raw, meta, timestamp = example
    data = json.loads(raw)
    row = data["data"]["solutions"][0]["recipe"][0]
    if damage == "amount":
        row["amount"] += 1
    elif damage == "unit":
        row["unit"] = "ml"
    elif damage == "optional":
        row["optional"] = 1
    elif damage == "condition":
        row["condition"] = "only for a variant"
    elif damage == "identity":
        data["data"]["medium"]["id"] = 999
    elif damage == "preparation":
        data["data"]["solutions"][0]["steps"][0]["step"] += " Different extraction."
    elif damage == "notes":
        before["ingredients"][0]["notes"] = "Another formulation"
    else:
        before["variants"] = [{"name": "different", "modifications": ["Use another input"]}]
    with pytest.raises(ValueError):
        repair.build(before, json.dumps(data), meta, item["medium_id"], timestamp)


def resolution_case(example):
    item, before, raw, meta, _ = example
    after, _, resolutions = build(example)
    before_text = item["before_text"]
    after_text = runner.render(before_text, after).decode()
    successor = {
        **item,
        "after_text": after_text,
        "after_sha256": runner.sha(after_text.encode()),
        "claim_resolutions": resolutions,
        "source_sha256": meta["sha256"],
    }
    original = {"path": item["path"], "id": item["id"], "after_sha256": item["before_sha256"]}
    resolution = resolutions[0]
    node = runner.get_node(before, resolution["from_pointer"])
    claim = {
        "pointer": resolution["from_pointer"],
        "field": runner.field_name(resolution["from_pointer"] + ["concentration"]),
        "ingredient": node["preferred_term"],
        "reference": resolution["reference"],
        "new": node["concentration"],
        "snippet": node["evidence"][0]["snippet"],
    }
    return original, claim, successor, raw


def test_explicit_resolution_retains_quotes_and_distinguishes_withdrawal(example):
    original, claim, successor, raw = resolution_case(example)
    pointer, field, withdrawn = runner.resolved_claim(original, claim, [successor], raw)
    expected = successor["claim_resolutions"][0]
    assert pointer == expected["to_pointer"] and field == expected["new_field"]
    assert withdrawn == (successor["medium_id"] == "12")


@pytest.mark.parametrize(
    "damage",
    [
        "quantity",
        "identity",
        "snippet",
        "scope",
        "source_quote",
        "source_pointer",
        "source_hash",
        "old_quantity",
        "disposition",
        "duplicate",
        "result_hash",
    ],
)
def test_resolution_cannot_hide_unsupported_changes(example, damage):
    original, claim, successor, raw = resolution_case(example)
    successor = copy.deepcopy(successor)
    r = successor["claim_resolutions"][0]
    after = runner.load_yaml(successor["after_text"])
    node = runner.get_node(after, r["to_pointer"])
    if damage == "quantity":
        node["concentration"] = {"value": "999", "unit": "G_PER_L"}
    elif damage == "identity":
        node["preferred_term"] = "Unrelated material"
    elif damage == "snippet":
        node["evidence"][0]["snippet"] = "fabricated"
    elif damage == "scope":
        node["evidence"][0]["explanation"] = "Unscoped evidence"
    elif damage == "source_quote":
        r["source_snippet"] = "{}"
    elif damage == "source_pointer":
        r["source_pointer"] = ["data", "medium"]
    elif damage == "source_hash":
        successor["source_sha256"] = "0" * 64
    elif damage == "old_quantity":
        r["old_concentration"] = {"value": "123", "unit": "G_PER_L"}
    elif damage == "disposition":
        r["disposition"] = "silently_fixed"
    elif damage == "duplicate":
        successor["claim_resolutions"].append(copy.deepcopy(r))
    successor["after_text"] = runner.render(successor["after_text"], after).decode()
    if damage != "result_hash":
        successor["after_sha256"] = runner.sha(successor["after_text"].encode())
    else:
        successor["after_sha256"] = "f" * 64
    with pytest.raises(ValueError):
        runner.resolved_claim(original, claim, [successor], raw)


def test_applied_records_match_the_frozen_guarded_plan():
    for item in json.loads(PLAN.read_text())["records"]:
        assert runner.sha((ROOT / item["path"]).read_bytes()) == item["after_sha256"]
        assert runner.sha(item["before_text"].encode()) == item["before_sha256"]
        assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
