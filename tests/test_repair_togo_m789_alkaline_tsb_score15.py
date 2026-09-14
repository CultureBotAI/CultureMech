from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m789_alkaline_tsb_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m789_alkaline_tsb_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_m789")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "alkaline_tryptone_soya_broth_medium",
        "original_name": "Alkaline Tryptone Soya Broth Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": target.physical_state,
        "ph_value": 8.8,
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": "Alkaline TSB"},
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


def test_jcm_j763_becomes_canonical_liquid_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.JCM_J763_PATH)

    assert repaired["physical_state"] == "LIQUID"
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.LIQUID_INGREDIENT_SIGNATURE
    )
    assert (
        repair_module._signature(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTION_SIGNATURE
    )
    assert repaired["ph_range"] == {"min": 8.5, "max": 9.0}
    assert repaired["variant_children"] == [
        repair_module.M789_CHILD,
        repair_module.M790_CHILD,
    ]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m789_links_to_jcm_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M789_PATH)

    assert repaired["physical_state"] == "LIQUID"
    assert repaired["parent_media"] == repair_module.J763_PARENT_SOURCE_DUPLICATE
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M789_CHILD["notes"]]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m790_links_to_jcm_as_solid_physical_variant(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M790_PATH)

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["parent_media"] == repair_module.J763_PARENT_SOLID_VARIANT
    assert repaired["variant_relationship"] == "PHYSICAL_STATE_VARIANT"
    assert repaired["variant_modifications"] == [repair_module.SOLID_VARIANT_NOTE]
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.SOLID_INGREDIENT_SIGNATURE
    )
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_corrects_water_and_nests_sodium_carbonate(
    repair_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M790_PATH)
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Agar"] == {
        "preferred_term": "Agar",
        "concentration": {"value": "20.0", "unit": "G_PER_L"},
        "source": "TOGO M790 / JCM Medium 763",
        "notes": "TOGO M790 / JCM Medium 763 adds 20.0 g/L agar for solid medium.",
        "term": {"id": "CHEBI:2509", "label": "agar"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:2509", "label": "agar"},
        "physicochemical_roles": ["SOLIDIFYING_AGENT"],
    }
    assert solutions["20% sodium carbonate solution"] == {
        "preferred_term": "20% sodium carbonate solution",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": "TOGO M790 / JCM Medium 763",
        "notes": ("TOGO M790 / JCM Medium 763 uses sterile 20% sodium carbonate " "to adjust pH."),
        "composition": [
            {
                "preferred_term": "Na2CO3",
                "concentration": {"value": "20.0", "unit": "PERCENT_W_V"},
                "source": "TOGO M790 / JCM Medium 763",
                "notes": (
                    "TOGO M790 / JCM Medium 763 specifies the pH-adjusting "
                    "sodium carbonate solution as 20.0% w/v."
                ),
                "term": {"id": "CHEBI:29377", "label": "sodium carbonate"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:29377",
                    "label": "sodium carbonate",
                },
                "physicochemical_roles": ["BUFFER"],
            }
        ],
        "preparation_notes": "Autoclave before adjusting the medium pH.",
    }


def test_repair_adds_references_flags_sterilization_and_event_once(
    repair_module,
) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M789_PATH
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
    assert repair_module.MEDIADIVE_J763 in matching_events[0]["source"]
    assert "sodium carbonate" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M789_PATH
    )
    doc = _doc(target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M789_PATH
    )
    doc = _doc(target)
    doc["solutions"][0]["preferred_term"] = "NaHCO3 solution"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)
