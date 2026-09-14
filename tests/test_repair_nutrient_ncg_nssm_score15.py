from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nutrient_ncg_nssm_score15.py"
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
    return _load_script(SCRIPT, "repair_nutrient_ncg_nssm_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_nutrient_ncg_nssm")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair) -> dict:
    doc = {
        "id": repair.record_id,
        "name": repair.path.stem,
        "original_name": repair.path.stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair.imported_ingredient_signature
        ],
        "media_term": {
            "preferred_term": repair.source_term,
            "term": {"id": repair.source_term, "label": repair.path.stem},
        },
        "notes": "Source: imported",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }
    if repair.imported_solution_signature:
        doc["solutions"] = [
            _ingredient(name, value, unit)
            for name, value, unit in repair.imported_solution_signature
        ]
    return doc


def _jcm_parent_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:003093",
        "name": "nutrient_agar",
        "original_name": "NUTRIENT AGAR",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "JCM Medium J74",
            "term": {"id": "mediadive.medium:J74", "label": "NUTRIENT AGAR"},
        },
        "ingredients": [],
        "notes": "Source: JCM",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "variant_children": [
            {
                "path": "data/normalized_yaml/bacterial/JCM_J100_ALKALINE_NUTRIENT_AGAR.yaml",
                "relationship": "SUPPLEMENTED_VARIANT",
                "id": "CultureMech:002194",
                "name": "alkaline_nutrient_agar",
            }
        ],
        "references": [{"reference": repair_module.TOGO_M2842}],
    }


def _m2340_parent_doc() -> dict:
    return {
        "id": "CultureMech:008928",
        "name": "nutrient_agar",
        "original_name": "Nutrient Agar",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "TOGO Medium M2340",
            "term": {"id": "TOGO:M2340", "label": "Nutrient Agar"},
        },
        "ingredients": [],
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _rows_by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_top_score_targets_exit_review_ranking(repair_module, scorer_module) -> None:
    for repair in repair_module.REPAIRS:
        repaired = repair_module.repair_target(repair, _doc(repair))

        assert scorer_module.score_parsed([(str(repair.path), repaired)]) == []
        assert "ingredients_curated" in repaired["data_quality_flags"]
        assert "has_ontology_mappings" in repaired["data_quality_flags"]


def test_ncg_keeps_commercial_products_opaque_and_adds_temperature(
    repair_module,
) -> None:
    repair = repair_module.REPAIRS_BY_PATH[repair_module.NCG]
    repaired = repair_module.repair_target(repair, _doc(repair))
    ingredients = _rows_by_name(repaired["ingredients"])

    assert repaired["temperature_value"] == 30.0
    assert "kg_microbe_match" not in repaired
    assert ingredients["glycerol"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17754",
        "label": "glycerol",
    }
    for name in (
        "yeast nitrogen base (BD Difco, Franklin Lakes, NJ, USA)",
        "casamino acid (BD Difco)",
    ):
        assert "term" not in ingredients[name]
        assert "mediaingredientmech_chebi_term" not in ingredients[name]
        assert "retained without an ontology grounding" in ingredients[name]["notes"]


def test_nssm_corrects_artificial_seawater_and_grounds_generic_products(
    repair_module,
) -> None:
    repair = repair_module.REPAIRS_BY_PATH[repair_module.NSSM]
    repaired = repair_module.repair_target(repair, _doc(repair))
    ingredients = _rows_by_name(repaired["ingredients"])

    assert repaired["ph_range"] == {"min": 7.0, "max": 7.2}
    assert ingredients["Artificial seawater"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Casamino acids"]["term"] == {
        "id": "FOODON:03315719",
        "label": "Casamino acids",
    }
    assert ingredients["Bacto Proteose Peptone No. 3 (Difco)"]["term"] == {
        "id": "MICRO:0000180",
        "label": "Proteose Peptone",
    }


def test_sporulation_corrects_water_and_manganese_units(repair_module) -> None:
    repair = repair_module.REPAIRS_BY_PATH[repair_module.SPORULATION]
    repaired = repair_module.repair_target(repair, _doc(repair))
    ingredients = _rows_by_name(repaired["ingredients"])

    assert repaired["ph_value"] == 7.0
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["MnSO4 x H2O"]["concentration"] == {
        "value": "10.0",
        "unit": "MG_PER_L",
    }
    assert repaired["parent_media"] == repair_module.M2341_PARENT
    assert repaired["variant_modifications"] == [
        repair_module.M2341_MODIFICATION
    ]


def test_dsmz_605_adds_water_and_links_phosphate_variant(repair_module) -> None:
    repair = repair_module.REPAIRS_BY_PATH[repair_module.DSMZ_605_PATH]
    repaired = repair_module.repair_target(repair, _doc(repair))
    linked = repair_module.repair_dsmz_605_parent(repaired)
    ingredients = _rows_by_name(linked["ingredients"])

    assert ingredients["Lab-Lemco beef extract"]["term"] == {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert linked["variant_children"] == [repair_module.DSMZ_605A_CHILD]
    assert "kg_microbe_match" not in linked


def test_dsmz_605a_repairs_dodecahydrate_and_keeps_parent_link(
    repair_module,
) -> None:
    repair = repair_module.REPAIRS_BY_PATH[repair_module.DSMZ_605A_PATH]
    repaired = repair_module.repair_target(repair, _doc(repair))
    ingredients = _rows_by_name(repaired["ingredients"])

    assert ingredients["Na2HPO4 x 12 H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:91259",
        "label": "disodium hydrogenphosphate dodecahydrate",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert repaired["parent_media"] == repair_module.DSMZ_605A_PARENT
    assert repaired["variant_modifications"] == [
        repair_module.DSMZ_605A_MODIFICATION
    ]


def test_m1186_repairs_solution_and_links_to_jcm_74(repair_module) -> None:
    repair = repair_module.REPAIRS_BY_PATH[repair_module.M1186]
    repaired = repair_module.repair_target(repair, _doc(repair))
    parent = repair_module.repair_jcm_j74_parent(_jcm_parent_doc(repair_module))

    assert repaired["solutions"] == [
        {
            "preferred_term": "Nutrient agar (JCM Medium 74)",
            "concentration": {"value": "1.0", "unit": "L"},
            "source": "TOGO M1186 / JCM Medium 1109",
            "notes": (
                "TOGO M1186 and JCM Medium 1109 list 1.0 L Nutrient agar "
                "from JCM Medium 74."
            ),
            "composition": [],
        }
    ]
    assert repaired["parent_media"] == repair_module.JCM_1109_PARENT
    assert repaired["variant_modifications"] == [
        repair_module.JCM_1109_MODIFICATION
    ]
    assert parent["variant_children"][-1] == repair_module.JCM_1109_CHILD
    assert "kg_microbe_match" not in repaired


def test_repair_adds_references_and_events_once(repair_module) -> None:
    repair = repair_module.REPAIRS_BY_PATH[repair_module.NSSM]

    once = repair_module.repair_target(repair, _doc(repair))
    twice = repair_module.repair_target(repair, once)

    assert twice["references"] == [
        {"reference": reference} for reference in repair.references
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair.action
        )
    ]
    assert len(matching_events) == 1


def test_repair_parent_adds_child_once(repair_module) -> None:
    once = repair_module.repair_jcm_j74_parent(_jcm_parent_doc(repair_module))
    twice = repair_module.repair_jcm_j74_parent(once)

    assert twice["variant_children"].count(repair_module.JCM_1109_CHILD) == 1
    assert twice["references"] == [{"reference": repair_module.TOGO_M2842}]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == "LINKED_JCM_1109_SUPPLEMENTED_VARIANT"
        )
    ]
    assert len(matching_events) == 1


def test_repair_m2340_adds_m2341_child_once(repair_module) -> None:
    once = repair_module.repair_togo_m2340_parent(_m2340_parent_doc())
    twice = repair_module.repair_togo_m2340_parent(once)

    assert twice["variant_children"] == [repair_module.M2341_CHILD]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == "LINKED_TOGO_M2341_SOURCE_DUPLICATE"
        )
    ]
    assert len(matching_events) == 1


def test_repair_rejects_wrong_id(repair_module) -> None:
    repair = repair_module.REPAIRS_BY_PATH[repair_module.NCG]
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair.record_id):
        repair_module.repair_target(repair, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    repair = repair_module.REPAIRS_BY_PATH[repair_module.NCG]
    doc = _doc(repair)
    doc["ingredients"][0] = _ingredient("Water", "1000", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(repair, doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    repair = repair_module.REPAIRS_BY_PATH[repair_module.M1186]
    doc = _doc(repair)
    doc["solutions"][0] = _ingredient("Unexpected solution", "1", "L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_target(repair, doc)


def test_target_records_match_repair_contract(repair_module) -> None:
    for repair in repair_module.REPAIRS:
        doc = yaml.safe_load(
            (repair_module.NORMALIZED / repair.path).read_text(encoding="utf-8")
        )

        assert doc["id"] == repair.record_id
        assert repair_module._source_term_id(doc) == repair.source_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in (
            repair.imported_ingredient_signature,
            repair.final_ingredient_signature,
        )
        assert repair_module._signature(doc.get("solutions"), "solutions") in (
            repair.imported_solution_signature,
            repair.final_solution_signature,
        )
