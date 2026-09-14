from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2179_ureaplasma_special_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2179_ureaplasma_special_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2179")


def _row(preferred_term: str, value: str, unit: str) -> dict:
    return {"preferred_term": preferred_term, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "ureaplasma_medium_special_modified_formulation",
        "original_name": "Ureaplasma Medium - Special Modified Formulation",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _row(preferred_term, value, unit)
            for preferred_term, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2179",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "Ureaplasma Medium - Special Modified Formulation",
            },
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _row(preferred_term, value, unit) | {"composition": []}
            for preferred_term, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_leaves_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_rebuilds_basal_formula(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert list(ingredients) == [
        repair_module.WATER,
        repair_module.AGAR,
        repair_module.PPLO,
        repair_module.CASEIN_DIGEST,
        repair_module.GELATIN_DIGEST,
        repair_module.CMRL,
        repair_module.UREA,
        repair_module.FBS,
    ]
    assert ingredients[repair_module.WATER]["concentration"] == {
        "value": "705.0",
        "unit": "ML_PER_L",
    }
    assert ingredients[repair_module.AGAR]["physicochemical_roles"] == [
        "SOLIDIFYING_AGENT"
    ]
    assert ingredients[repair_module.UREA]["term"] == {
        "id": "CHEBI:16199",
        "label": "urea",
    }


def test_repair_keeps_vendor_digests_unmapped(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    for preferred_term in (
        repair_module.PPLO,
        repair_module.CASEIN_DIGEST,
        repair_module.GELATIN_DIGEST,
        repair_module.CMRL,
        repair_module.FBS,
    ):
        assert "term" not in ingredients[preferred_term]
        assert "mediaingredientmech_chebi_term" not in ingredients[preferred_term]


def test_repair_rebuilds_stock_solutions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert solutions[repair_module.YEAST_EXTRACT_STOCK]["concentration"] == {
        "value": "35.0",
        "unit": "ML_PER_L",
    }
    yeast = _by_name(solutions[repair_module.YEAST_EXTRACT_STOCK]["composition"])
    assert yeast[repair_module.YEAST_EXTRACT]["concentration"] == {
        "value": "15.0",
        "unit": "PERCENT_W_V",
    }
    assert yeast[repair_module.YEAST_EXTRACT]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }

    yeastolate = _by_name(solutions[repair_module.TC_YEASTOLATE_STOCK]["composition"])
    assert yeastolate[repair_module.TC_YEASTOLATE]["concentration"] == {
        "value": "10.0",
        "unit": "PERCENT_W_V",
    }
    assert "term" not in yeastolate[repair_module.TC_YEASTOLATE]

    phenol = _by_name(solutions[repair_module.PHENOL_RED_STOCK]["composition"])
    assert phenol[repair_module.PHENOL_RED]["term"] == {
        "id": "CHEBI:31991",
        "label": "phenol red",
    }
    assert phenol[repair_module.NAOH]["concentration"] == {
        "value": "200.0",
        "unit": "ML_PER_L",
    }


def test_repair_adds_conditions_and_preparation(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_range"] == {"min": 5.8, "max": 6.2}
    assert "temperature_value" not in repaired
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert "kg_microbe_match" not in repaired


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M2179},
        {"reference": repair_module.ATCC_2616},
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": "; ".join(repair_module.REFERENCES),
            "notes": (
                f"{repair_module.NOTES} Corrected imported milliliter "
                "quantities, split the ATCC stock recipes out of the "
                "flattened ingredient list, and added ATCC pH and "
                "sterilization instructions."
            ),
        }
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    path = tmp_path / repair_module.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_doc(repair_module), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(tmp_path)
    for output_path, doc in first.items():
        output_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert {
        path.relative_to(tmp_path): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(tmp_path): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_component_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][1]["concentration"]["value"] = "806"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_reviewed_input(repair_module) -> None:
    doc = yaml.safe_load(
        (repair_module.NORMALIZED / repair_module.TARGET).read_text(encoding="utf-8")
    )

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in {
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    }
    assert repair_module._solution_signatures(doc) in {
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    }
