"""Independently invert the three source-backed stock identity withdrawals."""

import copy
import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

import review_solution_concentration_evidence as runner
from curation_identity_fixtures import read_mim_capture
from curation_source_fixtures import read_pdf_capture

from culturemech.validation.recipe_references import literal_match, parse_recipe, recipe_source

ROOT = Path(__file__).resolve().parents[3]
DIAGNOSTIC = (
    ROOT
    / "reports/ingredient_concentration_curation/20261009-solution-evidence-schema/resazurin-grounding-diagnostic.json"
)
DIAGNOSTIC_SHA = "b0e83400d2d5543035953bf609f3eac5e66b8e9f284365e889a8ff4c2770976d"
MIM_SHA = "a36cd4683feb89e2fc2a1721dc15008d1e10c12044e89a36c27b6621a8aaf262"
ACTION = "WITHDREW_UNSUPPORTED_RESAZURIN_STOCK_PRIMARY_IDENTITIES"


def cohort():
    raw = DIAGNOSTIC.read_bytes()
    assert runner.sha(raw) == DIAGNOSTIC_SHA, "Diagnostic drift"
    return json.loads(raw)["records"]


def source_for(spec):
    raw = (ROOT / spec["context"]).read_bytes()
    assert runner.sha(raw) == spec["context_sha256"], "Source context drift"
    matches = [
        s
        for s in json.loads(raw)["sources"].values()
        if s["metadata"]["url"] == spec["source_reference"]
    ]
    assert len(matches) == 1
    source = matches[0]
    meta = source["metadata"]
    assert meta["http_status"] == 200 and meta["response_url"] == meta["url"]
    assert runner.sha(source["raw"].encode()) == meta["sha256"] == spec["source_sha256"]
    assert runner.sha(read_pdf_capture(meta)) == meta["pdf_sha256"] == spec["source_pdf_sha256"]
    content = parse_recipe(recipe_source(meta["url"]), source["raw"], meta).content
    assert literal_match(spec["snippet"], content), "Source does not contain the exact excerpt"
    return source


def check(before, after, item):
    """Accept only a term withdrawal, an evidence extension and one appended event."""
    specs = {s["record"]: s for s in cohort()}
    spec = specs[item["path"]]
    assert before == runner.load_yaml(item["before_text"])
    assert after == runner.load_yaml(item["after_text"])
    assert runner.sha(item["before_text"].encode()) == item["before_sha256"] == spec["sha256"]
    assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
    assert before["id"] == after["id"] == item["id"] == spec["id"]
    assert item["action"] == ACTION
    source_for(spec)
    pointer = spec["pointer"][:-1]
    old = runner.get_node(before, pointer)
    new = runner.get_node(after, pointer)
    assert old["preferred_term"] == new["preferred_term"] == "Sodium resazurin (0.1% w/v)"
    assert old["term"] == spec["old_term"] == {"id": "CHEBI:8806", "label": "Resazurin"}
    assert "term" not in new
    assert old["concentration"] == new["concentration"] == {"value": "0.0005", "unit": "L"}
    assert old["evidence"] == spec["existing_evidence_to_preserve"]
    assert len(old["evidence"]) == len(new["evidence"]) == 1
    evidence = new["evidence"][0]
    assert evidence["reference"] == spec["source_reference"]
    assert evidence["snippet"] == spec["snippet"] and evidence["supports"] == "SUPPORT"
    prefix = old["evidence"][0]["explanation"] + "\n\n"
    assert evidence["explanation"].startswith(prefix)
    extension = evidence["explanation"][len(prefix) :]
    field = runner.field_name(spec["pointer"])
    for required in (
        field,
        "CHEBI:8806",
        "C12H7NO4",
        "sodium-free",
        "No replacement",
        "MIM",
        MIM_SHA,
        "still resolves",
        "publication-time",
        "0.0005 L",
        spec["source_sha256"],
        spec["source_pdf_sha256"],
    ):
        assert required in extension, f"Missing identity disposition: {required}"
    index = read_mim_capture(MIM_SHA)
    for node in (old, new):
        decision = index.resolve(node)
        assert decision.identifier == "CHEBI:8806"
        assert decision.resolution_source == "mim_exact"
    assert item["publication_identity_resolved"] is False
    assert item["resolver_after"] == asdict(index.resolve(new))
    assert item["claims"] == [
        {
            "field": field,
            "ingredient": old["preferred_term"],
            "old": old["term"],
            "new": None,
            "status": "correct",
            "reference": spec["source_reference"],
            "snippet": spec["snippet"],
            "explanation": extension,
        }
    ]
    restored = copy.deepcopy(after)
    target = runner.get_node(restored, pointer)
    target["term"] = copy.deepcopy(old["term"])
    target["evidence"][0]["explanation"] = old["evidence"][0]["explanation"]
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert event["source"] == spec["source_reference"] and event["notes"] == extension
    assert datetime.fromisoformat(event["timestamp"]).tzinfo is not None
    assert json.loads(event["changes"]) == {
        "field": field,
        "old": old["term"],
        "new": None,
        "evidence_extended": runner.field_name(pointer + ["evidence", 0, "explanation"]),
        "all_quantities_preserved": True,
        "publication_identity_resolved": False,
    }
    assert restored == before, "Unrelated data or previous provenance changed"
    return {
        "unsupported_primary_identities_removed": 1,
        "ingredient_evidence_explanations_extended": 1,
        "new_curation_history": 1,
    }
