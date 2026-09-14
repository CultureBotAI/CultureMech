from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m6_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m6_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m6")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _doc_for_agar(repair_module, target) -> dict:
    return {
        "id": target.record_id,
        "name": "bl_agar_glucose_blood_liver_agar",
        "original_name": "BL Agar (Glucose Blood Liver Agar)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": "BL Agar"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_solutions
        ],
        "high_metal": True,
    }


def _doc_for_maltose(target) -> dict:
    return {
        "id": target.record_id,
        "name": "bl_with_0_5_maltose",
        "original_name": "BL With 0.5% Maltose",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [_ingredient("Maltose", "5.0", "G_PER_L")],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": "BL With 0.5% Maltose"},
        },
        "notes": "JCM Medium 418 contains 1.0 L BL Agar with 5.0 g/L maltose.",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            {
                "preferred_term": "BL Agar",
                "concentration": {"value": "1000", "unit": "ML_PER_L"},
                "notes": "JCM Medium 418 uses 1.0 L BL Agar from JCM Medium 13.",
                "culturemech_term": {
                    "id": "CultureMech:010107",
                    "label": "BL Agar (Glucose Blood Liver Agar)",
                },
            }
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Use 1.0 L BL Agar with 5.0 g/L maltose.",
            }
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _repair_agar(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.AGAR_TARGETS if target.path == path)
    return repair_module.repair_agar_record(_doc_for_agar(repair_module, target), target)


def test_jcm_parent_restores_bl_agar_recipe_and_variant_children(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_agar(repair_module, repair_module.JCM_J13_PATH)

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert (
        repair_module._signature(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTION_SIGNATURE
    )
    assert repaired["ph_value"] == 7.2
    assert "parent_media" not in repaired
    assert "high_metal" not in repaired
    assert repaired["variant_children"] == [
        repair_module.M6_CHILD,
        repair_module.BACTERIAL_MALTOSE_CHILD,
        repair_module.FUNGAL_MALTOSE_CHILD,
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m6_links_to_jcm_source_duplicate(repair_module, scorer_module) -> None:
    repaired = _repair_agar(repair_module, repair_module.TOGO_M6_PATH)

    assert repaired["ph_value"] == 7.2
    assert repaired["parent_media"] == repair_module.JCM_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M6_VARIANT_MODIFICATION]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_moves_flattened_stock_components_to_solutions(repair_module) -> None:
    repaired = _repair_agar(repair_module, repair_module.TOGO_M6_PATH)
    solutions = _by_name(repaired["solutions"])
    solution_a = _by_name(solutions["Solution A"]["composition"])
    solution_b = _by_name(solutions["Solution B"]["composition"])

    assert "K2HPO4" not in _by_name(repaired["ingredients"])
    assert solution_a["K2HPO4"]["concentration"] == {
        "value": "100.0",
        "unit": "G_PER_L",
    }
    assert solution_b["FeSO4 x 7 H2O"]["term"] == {
        "id": "CHEBI:75836",
        "label": "iron(2+) sulfate heptahydrate",
    }
    assert "term" not in solution_b["MnSO4 x n H2O"]
    assert solutions["5% L-Cysteine HCl x H2O solution"]["composition"][0]["concentration"] == {
        "value": "5.0",
        "unit": "PERCENT_W_V",
    }


def test_repair_grounds_direct_components_and_roles(repair_module) -> None:
    repaired = _repair_agar(repair_module, repair_module.TOGO_M6_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Lab-Lemco powder (Oxoid)"]["term"] == {
        "id": "FOODON:03302088",
        "label": "beef extract",
    }
    assert ingredients["Proteose peptone No. 3 (BD-Difco)"]["term"] == {
        "id": "MICRO:0000180",
        "label": "proteose peptone",
    }
    assert ingredients["Horse blood"]["term"] == {
        "id": "UBERON:0000178",
        "label": "blood",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Horse blood"]
    assert ingredients["Glucose"]["nutritional_roles"] == ["CARBON_SOURCE"]
    assert ingredients["Tween 80"]["physicochemical_roles"] == ["SURFACTANT"]


def test_maltose_children_relink_to_canonical_jcm_parent(repair_module) -> None:
    for target in repair_module.MALTOSE_TARGETS:
        repaired = repair_module.repair_maltose_record(_doc_for_maltose(target), target)

        assert repaired["solutions"][0]["culturemech_term"] == (repair_module.BL_AGAR_JCM_TERM)
        assert repaired["parent_media"] == repair_module.JCM_SUPPLEMENT_PARENT
        assert repaired["variant_relationship"] == "SUPPLEMENTED_VARIANT"


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    target = next(
        target for target in repair_module.AGAR_TARGETS if target.path == repair_module.JCM_J13_PATH
    )
    once = repair_module.repair_agar_record(_doc_for_agar(repair_module, target), target)
    twice = repair_module.repair_agar_record(once, target)

    assert once["references"] == [{"reference": reference} for reference in target.references]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert "Liver extract" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.AGAR_TARGETS[0]
    doc = _doc_for_agar(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_agar_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.AGAR_TARGETS[0]
    doc = _doc_for_agar(repair_module, target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_agar_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = repair_module.AGAR_TARGETS[1]
    doc = _doc_for_agar(repair_module, target)
    doc["solutions"][0]["preferred_term"] = "Cysteine"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_agar_record(doc, target)
