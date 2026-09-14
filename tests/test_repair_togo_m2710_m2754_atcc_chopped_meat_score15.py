from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2710_m2754_atcc_chopped_meat_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m2710_m2754_atcc_chopped_meat_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2710_m2754")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module, target) -> dict:
    imported, imported_solutions = repair_module.IMPORTED_SIGNATURES[target.path]
    return {
        "id": target.expected_id,
        "name": target.name,
        "original_name": "Chopped meat medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [_component(name, value, unit) for name, value, unit in imported],
        "media_term": {
            "preferred_term": f"TOGO Medium {target.expected_media_term[5:]}",
            "term": {
                "id": target.expected_media_term,
                "label": "Chopped meat medium",
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [_component(name, value, unit) for name, value, unit in imported_solutions],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_base_repair_corrects_volume_units_and_moves_solutions(
    repair_module,
) -> None:
    repaired = repair_module.repair_target(
        _doc(repair_module, repair_module.TARGETS[0]),
        repair_module.TARGETS[0],
    )

    assert repaired["ph_value"] == 7.0
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.BASE_FINAL_INGREDIENTS
    )
    assert (
        repair_module._signature(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTIONS
    )
    assert "N NaOH" not in _by_name(repaired["ingredients"])
    assert _by_name(repaired["solutions"])["N NaOH"]["concentration"] == {
        "value": "25.0",
        "unit": "ML_PER_L",
    }
    assert _by_name(repaired["solutions"])["0.025% Resazurin solution"]["concentration"] == {
        "value": "4.0",
        "unit": "ML_PER_L",
    }


def test_glucose_repair_keeps_glucose_and_links_parent(repair_module) -> None:
    repaired = repair_module.repair_target(
        _doc(repair_module, repair_module.TARGETS[1]),
        repair_module.TARGETS[1],
    )

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.GLUCOSE_FINAL_INGREDIENTS
    )
    assert _by_name(repaired["ingredients"])["Glucose"]["term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert repaired["parent_media"] == repair_module._parent_media()
    assert repaired["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert repaired["variant_modifications"] == [
        "Adds 10.0 g/L glucose to ATCC Medium 593 Chopped meat medium.",
    ]


def test_repair_grounds_machine_usable_components(repair_module) -> None:
    repaired = repair_module.repair_target(
        _doc(repair_module, repair_module.TARGETS[0]),
        repair_module.TARGETS[0],
    )
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "peptone",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["L-cysteine . HCl"]["term"] == {
        "id": "CHEBI:91247",
        "label": "L-cysteine hydrochloride",
    }
    assert solutions["0.025% Resazurin solution"]["term"] == {
        "id": "CHEBI:8806",
        "label": "Resazurin",
    }
    assert solutions["N NaOH"]["term"] == {
        "id": "CHEBI:32145",
        "label": "sodium hydroxide",
    }
    assert "term" not in ingredients["Ground beef (free of fat)"]


def test_repair_adds_atcc_preparation_steps(repair_module) -> None:
    repaired = repair_module.repair_target(
        _doc(repair_module, repair_module.TARGETS[0]),
        repair_module.TARGETS[0],
    )

    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert "sterilization" not in repaired


def test_repaired_records_drop_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = [
        (
            str(target.path),
            repair_module.repair_target(_doc(repair_module, target), target),
        )
        for target in repair_module.TARGETS
    ]

    assert [scorer_module.score_record(doc) for _, doc in repaired] == [
        (0, []),
        (0, []),
    ]
    assert scorer_module.score_parsed(repaired) == []
    assert repaired[0][1]["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]


def test_repair_adds_references_and_events_once(repair_module) -> None:
    target = repair_module.TARGETS[0]
    once = repair_module.repair_target(_doc(repair_module, target), target)
    twice = repair_module.repair_target(once, target)

    assert twice["references"] == [{"reference": url} for url in target.references]
    repair_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    link_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert len(repair_events) == 1
    assert len(link_events) == 1
    assert "fat-free ground beef intentionally unmapped" in repair_events[0]["notes"]


def test_base_repair_adds_glucose_child_once(repair_module) -> None:
    target = repair_module.TARGETS[0]
    once = repair_module.repair_target(_doc(repair_module, target), target)
    twice = repair_module.repair_target(once, target)

    assert twice["variant_children"] == [repair_module._variant_child()]


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_target(doc, target)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=target.expected_media_term):
        repair_module.repair_target(doc, target)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["solutions"][0] = _component("0.025% Resazurin solution", "4.0", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_target(doc, target)


@pytest.mark.parametrize("index", [0, 1])
def test_live_target_records_match_repair_contract(repair_module, index) -> None:
    target = repair_module.TARGETS[index]
    path = repair_module.NORMALIZED / target.path
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == target.expected_id
    assert repair_module._source_term_id(doc) == target.expected_media_term
    assert (
        repair_module._signature(doc["ingredients"], "ingredients"),
        repair_module._signature(doc["solutions"], "solutions"),
    ) in (
        repair_module.IMPORTED_SIGNATURES[target.path],
        repair_module.FINAL_SIGNATURES[target.path],
    )
