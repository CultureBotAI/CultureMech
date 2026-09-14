from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1959_bn_agar_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1959_bn_agar_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_bn_agar")


def _component(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": target.path.stem,
        "original_name": "BN agar",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _component(name, value, unit) for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": target.media_term,
            "term": {"id": target.media_term, "label": target.source},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit) for name, value, unit, _ in target.imported_solutions
        ],
        "parent_media": {
            "path": "data/normalized_yaml/bacterial/bn_agar.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:008539",
            "name": "bn_agar",
        },
        "variant_relationship": "SOURCE_DUPLICATE",
        "variant_modifications": [
            "Same ingredient and concentration signature; review as possible "
            "duplicate source record."
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_bn_converts_selective_additives_to_grounded_direct_rows(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH[Path("bacterial/bn_agar.yaml")]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["functional_role"] == ["SELECTIVE"]
    assert "ph_value" not in repaired
    assert "solutions" not in repaired
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_BN
    )
    assert ingredients["Sodium benzoate"]["concentration"] == {
        "value": "1.44",
        "unit": "G_PER_L",
    }
    assert ingredients["Sodium benzoate"]["term"] == {
        "id": "CHEBI:113455",
        "label": "sodium benzoate",
    }
    assert ingredients["Kanamycin"]["concentration"] == {
        "value": "250.0",
        "unit": "MG_PER_L",
    }
    assert ingredients["Kanamycin"]["term"] == {
        "id": "CHEBI:6104",
        "label": "kanamycin",
    }
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


def test_repair_base_records_fix_water_agar_and_variant_topology(
    repair_module,
    scorer_module,
) -> None:
    nutrient_target = repair_module.TARGET_BY_PATH[Path("bacterial/nutrient_agar_broth.yaml")]
    m1570_target = repair_module.TARGET_BY_PATH[Path("bacterial/togo_medium_m1570.yaml")]

    nutrient = repair_module.repair_record(_doc(nutrient_target), nutrient_target)
    m1570 = repair_module.repair_record(_doc(m1570_target), m1570_target)

    assert repair_module._signature(nutrient["ingredients"], "ingredients") == (
        repair_module.FINAL_BASE_13
    )
    assert repair_module._signature(m1570["ingredients"], "ingredients") == (
        repair_module.FINAL_BASE_6_5
    )
    assert "parent_media" not in nutrient
    assert nutrient["variant_children"] == [
        repair_module.BN_CHILD,
        repair_module.M1570_CHILD,
    ]
    assert m1570["parent_media"] == repair_module.NUTRIENT_BASE_PARENT_FOR_M1570
    assert m1570["variant_relationship"] == "CONCENTRATION_VARIANT"
    assert m1570["variant_modifications"] == (repair_module.M1570_VARIANT_MODIFICATIONS)
    assert (
        scorer_module.score_parsed(
            [
                (str(nutrient_target.path), nutrient),
                (str(m1570_target.path), m1570),
            ]
        )
        == []
    )


def test_repair_adds_preparation_references_flags_and_event_once(
    repair_module,
) -> None:
    target = repair_module.TARGET_BY_PATH[Path("bacterial/bn_agar.yaml")]
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert [step["action"] for step in twice["preparation_steps"]] == [
        "MIX",
        "AUTOCLAVE",
        "FILTER_STERILIZE",
        "MIX",
    ]
    assert twice["sterilization"] == repair_module.BN_STERILIZATION
    assert twice["parent_media"] == repair_module.NUTRIENT_BASE_PARENT
    assert twice["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert twice["variant_modifications"] == repair_module.BN_VARIANT_MODIFICATIONS
    assert twice["references"] == [{"reference": reference} for reference in target.references]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == "; ".join(target.references)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[Path("bacterial/bn_agar.yaml")]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M1958"

    with pytest.raises(ValueError, match="expected media term TOGO:M1959"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[Path("bacterial/bn_agar.yaml")]
    doc = _doc(target)
    doc["solutions"][0]["preferred_term"] = "Kanamycin"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_repair_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.record_id
        assert repair_module._source_term_id(doc) == target.media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in (
            target.imported_ingredients,
            target.final_ingredients,
        )
        assert repair_module._solution_signatures(doc) in (
            target.imported_solutions,
            (),
        )
