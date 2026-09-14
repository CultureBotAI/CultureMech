from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_utex_algae_score10.py"
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
    return _load_script(SCRIPT, "repair_utex_algae_score10")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_utex_algae_score10")


def _soil_extract_doc(repair_module) -> dict:
    return {
        "id": repair_module.SOIL_EXTRACT_ID,
        "name": "soil_extract_medium",
        "category": "algae",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "notes": "UTEX Soil Extract Medium",
        "temperature_range": "15-30 C depending on species",
        "ingredients": [],
        "solutions": [
            {
                "preferred_term": "Bristol Medium",
                "concentration": {"value": "960", "unit": "ML_PER_L"},
                "culturemech_term": {
                    "id": "CultureMech:000037",
                    "label": "Bristol Medium",
                },
            },
            {
                "preferred_term": "Soilwater: GR+ Medium",
                "concentration": {"value": "40", "unit": "ML_PER_L"},
                "culturemech_term": {
                    "id": "CultureMech:000225",
                    "label": "Soilwater: GR+ Medium",
                },
            },
        ],
        "curation_history": [
            {
                "curator": "utex-import",
                "action": "Imported from UTEX Culture Collection",
                "notes": (
                    "Source ID: soil-extract-medium, URL: "
                    "https://utex.org/products/soil-extract-medium"
                ),
            }
        ],
        "references": [
            {"reference": "UTEX:soil-extract-medium"},
            {"reference": "https://utex.org/products/soil-extract-medium"},
        ],
        "data_quality_flags": ["ingredients_curated"],
    }


def _soilwater_peat_doc(repair_module) -> dict:
    return {
        "id": repair_module.SOILWATER_PEAT_ID,
        "name": "soilwater_peat_medium",
        "category": "algae",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "Soilwater: Peat Medium",
            "term": {
                "id": "UTEX:soilwater-peat-medium",
                "label": "Soilwater: Peat Medium",
            },
        },
        "notes": "UTEX prepares Soilwater: Peat Medium",
        "temperature_range": "15-30 C depending on species",
        "ingredients": [
            {
                "preferred_term": "Organic Peat",
                "concentration": {"value": "0.5 tsp per 200 mL", "unit": "VARIABLE"},
            },
            {
                "preferred_term": "Green House Soil",
                "concentration": {"value": "1.5 tsp per 200 mL", "unit": "VARIABLE"},
            },
            {
                "preferred_term": "dH2O",
                "concentration": {"value": "1000", "unit": "ML_PER_L"},
                "term": {"id": "CHEBI:15377", "label": "water"},
            },
        ],
        "curation_history": [],
        "data_quality_flags": ["ingredients_curated"],
    }


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_soil_extract_adds_structured_utex_source(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_soil_extract(_soil_extract_doc(repair_module))

    assert repaired["sources"] == [
        {
            "database": "UTEX",
            "database_id": "soil-extract-medium",
            "url": "https://utex.org/products/soil-extract-medium",
        }
    ]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.SOIL_EXTRACT), repaired)]) == []


def test_soilwater_peat_grounds_green_house_soil(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_soilwater_peat(_soilwater_peat_doc(repair_module))

    assert repaired["ingredients"][1]["term"] == repair_module.GREEN_HOUSE_SOIL_TERM
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.SOILWATER_PEAT), repaired)]) == []


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.repair_soil_extract(_soil_extract_doc(repair_module))
    twice = repair_module.repair_soil_extract(once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)

    once = repair_module.repair_soilwater_peat(_soilwater_peat_doc(repair_module))
    twice = repair_module.repair_soilwater_peat(once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)


def test_plan_repairs_targets_current_records(repair_module) -> None:
    expected = {
        repair_module.NORMALIZED
        / repair_module.SOIL_EXTRACT: repair_module.repair_soil_extract(
            _load_yaml(repair_module.NORMALIZED / repair_module.SOIL_EXTRACT)
        ),
        repair_module.NORMALIZED
        / repair_module.SOILWATER_PEAT: repair_module.repair_soilwater_peat(
            _load_yaml(repair_module.NORMALIZED / repair_module.SOILWATER_PEAT)
        ),
    }

    assert repair_module.plan_repairs() == expected


def test_soil_extract_rejects_mismatched_url(repair_module) -> None:
    doc = _soil_extract_doc(repair_module)
    doc["references"][1]["reference"] = "https://utex.org/products/soilwater-peat-medium"

    with pytest.raises(ValueError, match="does not match utex-import"):
        repair_module.repair_soil_extract(doc)


def test_soilwater_peat_rejects_ingredient_drift(repair_module) -> None:
    doc = _soilwater_peat_doc(repair_module)
    doc["ingredients"][1]["preferred_term"] = "Greenhouse Soil"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_soilwater_peat(doc)
