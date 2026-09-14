from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m783_dethiosulfovibrio_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m783_dethiosulfovibrio_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_m783")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "dethiosulfovibrio_ii_medium",
        "original_name": "Dethiosulfovibrio II Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.8,
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": "Dethiosulfovibrio II"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
            "resolved_reference",
        ],
        "solutions": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_solutions
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _repair(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_record(_doc(target), target)


def test_jcm_j758_becomes_canonical_nested_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.JCM_J758_PATH)

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
    assert repaired["ph_range"] == {"min": 6.7, "max": 6.8}
    assert "ph_value" not in repaired
    assert repaired["variant_children"] == [repair_module.M783_CHILD]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m783_links_to_jcm_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M783_PATH)

    assert repaired["parent_media"] == repair_module.J758_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.J758_PARENT["notes"]]
    assert "variant_children" not in repaired
    assert "N2" not in _by_name(repaired["ingredients"])
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_scales_main_solution_and_nests_jcm_187_stocks(
    repair_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M783_PATH)
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "967.118",
        "unit": "ML_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.483559",
        "unit": "MG_PER_L",
    }
    assert solutions["FeCl2 solution"]["concentration"] == {
        "value": "0.967118",
        "unit": "ML_PER_L",
    }
    assert solutions["FeCl2 solution"]["composition"] == [
        {
            "preferred_term": "HCl",
            "concentration": {"value": "2.5", "unit": "G_PER_L"},
            "source": "JCM Medium 187",
            "notes": "JCM Medium 187 lists 2.5 g/L HCl.",
            "term": {"id": "CHEBI:17883", "label": "hydrogen chloride"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:17883",
                "label": "hydrogen chloride",
            },
        },
        {
            "preferred_term": "FeCl2 x 4 H2O",
            "concentration": {"value": "1.5", "unit": "G_PER_L"},
            "source": "JCM Medium 187",
            "notes": "JCM Medium 187 lists 1.5 g/L FeCl2 x 4 H2O.",
            "term": {
                "id": "CHEBI:86249",
                "label": "iron dichloride tetrahydrate",
            },
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:86249",
                "label": "iron dichloride tetrahydrate",
            },
            "nutritional_roles": ["IRON_SOURCE", "TRACE_ELEMENT"],
        },
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "990.0", "unit": "ML_PER_L"},
            "source": "JCM Medium 187",
            "notes": "JCM Medium 187 makes FeCl2 solution with 990.0 ml water.",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:15377",
                "label": "water",
            },
        },
    ]
    assert solutions["Trace element solution"]["composition"][3] == {
        "preferred_term": "CoCl2 x 6 H2O",
        "concentration": {"value": "190.0", "unit": "MG_PER_L"},
        "source": "JCM Medium 187",
        "notes": "JCM Medium 187 lists 190.0 mg/L CoCl2 x 6 H2O.",
        "term": {"id": "CHEBI:53503", "label": "cobalt chloride hexahydrate"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:53503",
            "label": "cobalt chloride hexahydrate",
        },
        "nutritional_roles": ["TRACE_ELEMENT"],
    }
    assert solutions["12.5% Na2S2O3 x 5 H2O solution"]["composition"][0] == {
        "preferred_term": "Na2S2O3 x 5 H2O",
        "concentration": {"value": "12.5", "unit": "PERCENT_W_V"},
        "source": "TOGO M783 / JCM Medium 758",
        "notes": (
            "TOGO M783 / JCM Medium 758 specifies " "12.5% Na2S2O3 x 5 H2O solution as 12.5% w/v."
        ),
        "term": {
            "id": "CHEBI:32150",
            "label": "sodium thiosulfate pentahydrate",
        },
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:32150",
            "label": "sodium thiosulfate pentahydrate",
        },
        "nutritional_roles": ["SULFUR_SOURCE"],
    }


def test_repair_adds_references_flags_sterilization_and_event_once(
    repair_module,
) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M783_PATH
    )
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert once["references"] == [{"reference": reference} for reference in target.references]
    assert once["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert once["sterilization"] == repair_module.STERILIZATION
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert repair_module.JCM_187 in matching_events[0]["source"]
    assert "N2 placeholder" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M783_PATH
    )
    doc = _doc(target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M783_PATH
    )
    doc = _doc(target)
    doc["solutions"][0]["preferred_term"] = "FeCl3 solution"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)
