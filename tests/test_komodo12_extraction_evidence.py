"""Offline exact-source linkage, preservation, and additive-retention guards."""

import copy
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_komodo12_extraction_evidence as repair  # noqa: E402
from review_solution_concentration_evidence import get_node  # noqa: E402

HERE = ROOT / "reports/ingredient_concentration_curation/20261007-komodo12-extraction"
spec = importlib.util.spec_from_file_location("komodo12_retention", HERE / "check_retention.py")
retention_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(retention_module)


@pytest.fixture
def example():
    plan = json.loads((HERE / "plan.json").read_text())
    item = plan["records"][0]
    previous = json.loads((ROOT / repair.PREVIOUS / "plan.json").read_text())
    parent = next(r for r in previous["records"] if r["medium_id"] == "12")
    before = repair.load_yaml(item["before_text"])
    source_before = repair.load_yaml(parent["before_text"])
    prepared = repair.load_yaml(parent["after_text"])
    nodes = prepared["solutions"][0]["composition"] + prepared["ingredients"]
    # Literal frozen excerpts inside an offline fixture, not a network result.
    rows = ",".join(n["evidence"][0]["snippet"] for n in nodes)
    raw = (
        '{"data":{"medium":{"id":12,"name":"SOIL EXTRACT MEDIUM","source":"DSMZ","link":'
        + json.dumps(repair.PDF)
        + '},"solutions":[{"id":15,"name":"Main sol. 12","volume":1000,"recipe":['
        + rows
        + '],"steps":['
        + item["claims"][0]["snippet"]
        + "]}]}}"
    )
    meta = {"sha256": repair.sha(raw.encode()), "accessed_at": item["source_accessed_at"]}
    handoff = json.loads((ROOT / repair.PREVIOUS / "komodo12-source-handoff.json").read_text())
    mapping = handoff["source_row"]["snippet"]
    handoff["sha256"] = repair.sha(mapping.encode())
    return before, source_before, raw, meta, mapping, handoff, plan["created_at"]


def test_rebuild_from_linked_source_preserves_identity_and_unknown_yield(example):
    before = example[0]
    after, claims = repair.build(*example)
    assert len(claims) == 10
    assert after["ingredients"][0]["concentration"] == {"value": "15", "unit": "G_PER_L"}
    stock = after["solutions"][0]
    assert "concentration" not in stock and "term" not in stock
    assert "concentration" not in stock["composition"][0]
    assert "400 g in 1000 ml" in stock["composition"][0]["notes"]
    assert stock["composition"][1]["concentration"] == {"value": "1", "unit": "L"}
    assert len(after["references"]) == 3 and len(after["evidence"]) == 2
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["curator"] == "codex"
    for key in before.keys() - {"ingredients", "curation_history"}:
        assert after[key] == before[key]
    for c in claims:
        assert c["old"] == (get_node(before, c["old_pointer"]) if c["old_pointer"] else None)
        if c["new"] is None:
            assert c["pointer"][-1] not in get_node(after, c["pointer"][:-1])
        else:
            assert get_node(after, c["pointer"]) == c["new"]
        entry = next(
            e
            for e in get_node(after, c["evidence_pointer"])["evidence"]
            if e["reference"] == c["reference"]
        )
        assert c["field"] in entry["explanation"]
        assert c["snippet"] == entry["snippet"] or c["snippet"] in entry["explanation"]


@pytest.mark.parametrize(
    "damage",
    [
        "identity",
        "source_term",
        "parent",
        "ph",
        "amount",
        "ingredient",
        "extra_ingredient",
        "notes",
        "existing_evidence",
        "existing_preparation",
        "stocks",
        "variants",
        "optional",
        "source_amount",
        "source_unit",
        "source_medium",
        "source_link",
        "source_step",
        "mapping_hash",
        "mapping_excerpt",
        "mapping_link",
        "mapping_variant",
        "duplicate_mapping",
    ],
)
def test_ambiguity_and_source_drift_are_rejected(example, damage):
    doc, parent, raw, meta, mapping, handoff, timestamp = copy.deepcopy(example)
    source = json.loads(raw)
    row = source["data"]["solutions"][0]["recipe"][0]
    if damage == "identity":
        doc["id"] = "CultureMech:000001"
    elif damage == "source_term":
        doc["media_term"]["term"]["id"] = "komodo.medium:12.1"
    elif damage == "parent":
        doc["parent_media"]["id"] = "CultureMech:000001"
    elif damage == "ph":
        doc["ph_range"]["min"] = 5.0
    elif damage == "amount":
        doc["ingredients"][0]["concentration"]["value"] = "200"
    elif damage == "ingredient":
        doc["ingredients"][0]["preferred_term"] = "Another extract"
    elif damage == "extra_ingredient":
        doc["ingredients"].append(copy.deepcopy(doc["ingredients"][0]))
    elif damage == "notes":
        doc["ingredients"][0]["notes"] = "Changed formulation"
    elif damage == "existing_evidence":
        doc["evidence"] = []
    elif damage == "existing_preparation":
        doc["preparation_steps"] = []
    elif damage == "stocks":
        doc["solutions"] = []
    elif damage == "variants":
        doc["variants"] = []
    elif damage == "optional":
        row["optional"] = 1
    elif damage == "source_amount":
        row["amount"] = 300
    elif damage == "source_unit":
        row["unit"] = "ml"
    elif damage == "source_medium":
        source["data"]["medium"]["id"] = 13
    elif damage == "source_link":
        source["data"]["medium"]["link"] = repair.PDF.replace("12.pdf", "13.pdf")
    elif damage == "source_step":
        source["data"]["solutions"][0]["steps"][0]["step"] += " Modified formulation."
    elif damage == "mapping_hash":
        handoff["sha256"] = "0" * 64
    elif damage == "mapping_excerpt":
        handoff["source_row"]["snippet"] = "not the quoted row"
    elif damage in {"mapping_link", "mapping_variant"}:
        field, value = (
            (6, repair.PDF.replace("12.pdf", "13.pdf")) if damage == "mapping_link" else (5, "true")
        )
        handoff["source_row"]["cells"][field] = value
    elif damage == "duplicate_mapping":
        mapping += mapping
        handoff["sha256"] = repair.sha(mapping.encode())
    with pytest.raises(ValueError):
        repair.build(doc, parent, json.dumps(source), meta, mapping, handoff, timestamp)


def test_added_provenance_is_retention_not_loss():
    original = json.loads((ROOT / repair.PREVIOUS / "plan.json").read_text())["records"][0]
    parent = repair.load_yaml(original["after_text"])
    after = repair.load_yaml(
        json.loads((HERE / "plan.json").read_text())["records"][0]["after_text"]
    )
    assert all(retention_module.retention(after, parent).values())
    assert len(after["references"]) == len(parent["references"]) + 1
    assert len(after["evidence"]) == len(parent["evidence"]) + 1


@pytest.mark.parametrize(
    "field",
    [
        "ingredients",
        "solutions",
        "preparation_steps",
        "physical_state",
        "ph_range",
        "evidence",
        "references",
    ],
)
def test_retention_does_not_accept_removed_or_changed_claims(field):
    doc = repair.load_yaml(json.loads((HERE / "plan.json").read_text())["records"][0]["after_text"])
    merged = copy.deepcopy(doc)
    merged.pop(field)
    assert not retention_module.retention(merged, doc)[field]


@pytest.mark.parametrize("damage", ["snippet", "supports", "explanation", "duplicate"])
def test_retention_keeps_complete_evidence_not_just_reference(damage):
    doc = repair.load_yaml(json.loads((HERE / "plan.json").read_text())["records"][0]["after_text"])
    merged = copy.deepcopy(doc)
    if damage == "duplicate":
        merged["evidence"].append(copy.deepcopy(merged["evidence"][0]))
    else:
        merged["evidence"][0][damage] = "changed"
    assert not retention_module.retention(merged, doc)["evidence"]


def test_applied_record_and_report_match_frozen_plan():
    item = json.loads((HERE / "plan.json").read_text())["records"][0]
    assert repair.sha((ROOT / item["path"]).read_bytes()) == item["after_sha256"]
    assert repair.sha(item["before_text"].encode()) == item["before_sha256"]
    assert repair.sha(item["after_text"].encode()) == item["after_sha256"]
    lines = (HERE / "12.md").read_text().splitlines()
    assert [line for line in lines if line.startswith("- Record:")] == [
        f"- Record: {repair.TARGET}"
    ]
    assert "- State: applied locally" in lines
