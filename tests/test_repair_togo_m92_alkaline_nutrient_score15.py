from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m92_alkaline_nutrient_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
PLACEHOLDER_INGREDIENTS = (("See source for composition", "variable", "VARIABLE"),)


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m92_alkaline_nutrient_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_m92")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(signature) -> dict:
    name, value, unit, composition = signature
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [
            _ingredient(component_name, component_value, component_unit)
            for component_name, component_value, component_unit in composition
        ],
    }


def _medium_doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "nutrient_agar",
        "original_name": "Nutrient Agar",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_ingredients
        ],
        "solutions": [_solution(row) for row in target.imported_solutions],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": target.source_name},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition", "resolved_reference"],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _solution_doc(target) -> dict:
    return {
        "id": target.record_id,
        "preferred_term": "Main sol.",
        "term": {
            "id": target.solution_term,
            "label": "Main sol.",
        },
        "composition": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_composition
        ],
        "preparation_notes": "Original MediaDive step",
        "curation_history": [],
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in PLACEHOLDER_INGREDIENTS
        ],
        "data_quality_flags": ["incomplete_composition"],
        "category": "bacterial",
    }


def _repair_medium(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_medium_record(_medium_doc(target), target)


def _repair_solution(repair_module, path: Path) -> dict:
    target = next(
        target for target in repair_module.SOLUTION_TARGETS if target.path == path
    )
    return repair_module.repair_solution_record(_solution_doc(target), target)


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_jcm_j74_becomes_canonical_nutrient_agar_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.JCM_J74_PATH)

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.NUTRIENT_AGAR_COMPOSITION
    assert "solutions" not in repaired
    assert repaired["ph_value"] == 7.0
    assert repaired["variant_children"] == [
        repair_module.M65_CHILD,
        repair_module.J100_CHILD,
        repair_module.NBRC_CHILD,
    ]
    assert "parent_media" not in repaired
    assert "kg_microbe_match" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed(
        [("bacterial/JCM_J74_NUTRIENT_AGAR.yaml", repaired)]
    ) == []


def test_togo_m65_links_to_j74_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M65_PATH)

    assert repaired["parent_media"] == repair_module.J74_PARENT_SOURCE_DUPLICATE
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M65_CHILD["notes"]]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed(
        [("bacterial/TOGO_M65_Nutrient_Agar.yaml", repaired)]
    ) == []


def test_jcm_j100_links_to_j74_supplemented_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.JCM_J100_PATH)

    assert repaired["parent_media"] == repair_module.J74_PARENT_SUPPLEMENTED
    assert repaired["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert repaired["variant_modifications"] == [repair_module.J100_CHILD["notes"]]
    assert repaired["variant_children"] == [repair_module.M92_CHILD]
    assert scorer_module._grounded(repaired["solutions"][0]["composition"][0])
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed(
        [("bacterial/JCM_J100_ALKALINE_NUTRIENT_AGAR.yaml", repaired)]
    ) == []


def test_togo_m92_links_to_j100_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M92_PATH)

    assert repaired["parent_media"] == repair_module.J100_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M92_CHILD["notes"]]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed(
        [("bacterial/TOGO_M92_Alkaline_Nutrient_Agar.yaml", repaired)]
    ) == []


def test_repair_corrects_units_groundings_and_roles(repair_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M92_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }
    assert ingredients["Beef extract"]["term"] == {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    }
    assert ingredients["Agar"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]


def test_repair_nests_variable_sodium_carbonate_solution(repair_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M92_PATH)
    solutions = _by_name(repaired["solutions"])

    assert solutions["10% Na2CO3 solution"] == {
        "preferred_term": "10% Na2CO3 solution",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": "TOGO M92 / JCM Medium 100",
        "notes": (
            "TOGO M92 / JCM Medium 100 uses sterile 10% Na2CO3 solution to "
            "adjust the final medium to pH 10.0; the source does not "
            "specify a fixed addition volume."
        ),
        "composition": [
            {
                "preferred_term": "Na2CO3",
                "concentration": {"value": "10.0", "unit": "PERCENT_W_V"},
                "source": "TOGO M92 / JCM Medium 100",
                "notes": (
                    "TOGO M92 / JCM Medium 100 specifies the pH-adjusting "
                    "sodium carbonate solution as 10.0% w/v."
                ),
                "term": {"id": "CHEBI:29377", "label": "sodium carbonate"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:29377",
                    "label": "sodium carbonate",
                },
                "physicochemical_roles": ["BUFFER"],
            }
        ],
        "preparation_notes": "Sterilize before adjusting the basal medium to pH 10.0.",
    }


def test_solution_helpers_correct_false_percent_water(repair_module) -> None:
    repaired = _repair_solution(repair_module, repair_module.SOLUTION_3730_PATH)
    composition = _by_name(repaired["composition"])

    assert "ingredients" not in repaired
    assert repair_module._signature(
        repaired["composition"],
        "composition",
    ) == repair_module.MEDIADIVE_MAIN_SOLUTION_COMPOSITION
    assert composition["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }
    assert composition["Beef extract"]["term"] == {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    }
    assert composition["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M92_PATH
    )
    once = repair_module.repair_medium_record(_medium_doc(target), target)
    twice = repair_module.repair_medium_record(once, target)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in target.references
    ]
    assert once["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert repair_module.TOGO_M92 in matching_events[0]["source"]
    assert "Na2CO3" in matching_events[0]["notes"]


def test_repair_rejects_wrong_medium_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _medium_doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_medium_ingredient_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M92_PATH
    )
    doc = _medium_doc(target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_medium_solution_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M92_PATH
    )
    doc = _medium_doc(target)
    doc["solutions"][0]["preferred_term"] = "wrong"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_solution_composition_drift(repair_module) -> None:
    target = next(
        target
        for target in repair_module.SOLUTION_TARGETS
        if target.path == repair_module.SOLUTION_3730_PATH
    )
    doc = _solution_doc(target)
    doc["composition"].pop()

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_solution_record(doc, target)
