from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = (
    REPO
    / "scripts"
    / "repair_togo_m1970_m1971_m1972_lb_streptomycin_rifampicin_score15.py"
)
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
    return _load_script(
        SCRIPT,
        "repair_togo_m1970_m1971_m1972_lb_streptomycin_rifampicin_score15",
    )


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1970_m1972")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
        "name": "Unknown solution",
    }


def _target_doc(spec) -> dict:
    return {
        "id": spec.expected_id,
        "name": spec.target.stem,
        "original_name": spec.original_name,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in spec.imported_ingredient_signature
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {spec.togo_id}",
            "term": {
                "id": spec.expected_media_term,
                "label": spec.original_name,
            },
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _composition in spec.imported_solution_signature
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_expands_lb_antibiotic_stocks(
    repair_module,
    scorer_module,
) -> None:
    for spec in repair_module.SPECS:
        repaired = repair_module.repair_target(_target_doc(spec), spec)
        ingredients = _by_name(repaired["ingredients"])

        assert repair_module._signature(repaired["ingredients"], "ingredients") == (
            spec.final_ingredient_signature
        )
        assert repair_module._solution_signature(repaired["solutions"], "solutions") == (
            spec.final_solution_signature
        )
        assert repaired["ph_value"] == 7.0
        assert repaired["composition_type"] == "SEMI_DEFINED"
        assert ingredients["Distilled water"]["concentration"] == {
            "value": spec.water_ml,
            "unit": "ML_PER_L",
        }
        assert ingredients["Yeast extract"]["term"] == {
            "id": "FOODON:03315426",
            "label": "yeast extract",
        }
        assert "term" not in ingredients["Bacto Tryptone (Difco)"]

        solutions = _by_name(repaired["solutions"])
        for stock in spec.final_solution_order:
            solution = solutions[stock.solution_name]
            component = solution["composition"][0]

            assert solution["concentration"] == {
                "value": stock.addition_ml,
                "unit": "ML_PER_L",
            }
            assert component["concentration"] == {
                "value": stock.component_mg,
                "unit": "MG_PER_ML",
            }
            assert component["term"] == repair_module._term(
                *repair_module.GROUNDINGS[stock.component_name]
            )

        assert repaired["preparation_steps"] == list(
            repair_module._preparation_steps(spec)
        )
        assert scorer_module.score_record(repaired) == (0, [])
        assert scorer_module.score_parsed([(str(spec.target), repaired)]) == []


def test_repair_updates_variant_relationships_and_is_idempotent(
    repair_module,
) -> None:
    for spec in repair_module.SPECS:
        target_once = repair_module.repair_target(_target_doc(spec), spec)
        target_twice = repair_module.repair_target(target_once, spec)

        assert target_twice == target_once
        assert target_once["parent_media"] == spec.parent_media
        assert target_once["variant_relationship"] == "SUPPLEMENTED_VARIANT"
        assert target_once["variant_modifications"] == [spec.variant_modifications]

    lb_parent_once = repair_module.repair_lb_parent(
        {
            "id": repair_module.LB_PARENT_ID,
            "variant_children": [
                {
                    "id": "other",
                    "path": "data/normalized_yaml/bacterial/other.yaml",
                    "relationship": "CONCENTRATION_VARIANT",
                }
            ],
        }
    )
    lb_parent_twice = repair_module.repair_lb_parent(lb_parent_once)

    assert lb_parent_twice == lb_parent_once
    for spec in repair_module.SPECS:
        assert spec.variant_child in lb_parent_once["variant_children"]
    assert {
        "id": "other",
        "path": "data/normalized_yaml/bacterial/other.yaml",
        "relationship": "CONCENTRATION_VARIANT",
    } in lb_parent_once["variant_children"]


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    for spec in repair_module.SPECS:
        once = repair_module.repair_target(_target_doc(spec), spec)
        twice = repair_module.repair_target(once, spec)

        assert twice == once
        assert once["data_quality_flags"] == [
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ]
        assert once["references"] == [
            {"reference": spec.togo_url},
            {"reference": spec.nbrc_url},
        ]
        matching_events = [
            event
            for event in once["curation_history"]
            if (
                event.get("curator") == repair_module.CURATOR
                and event.get("action") == repair_module.ACTION
            )
        ]
        assert len(matching_events) == 1


def test_repair_rejects_wrong_id(repair_module) -> None:
    spec = repair_module.SPECS[0]
    doc = _target_doc(spec)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=spec.expected_id):
        repair_module.repair_target(doc, spec)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    spec = repair_module.SPECS[0]
    doc = _target_doc(spec)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=spec.expected_media_term):
        repair_module.repair_target(doc, spec)


def test_repair_rejects_solution_drift(repair_module) -> None:
    spec = repair_module.SPECS[0]
    doc = _target_doc(spec)
    doc["solutions"][0]["preferred_term"] = "Streptomycin"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_target(doc, spec)
