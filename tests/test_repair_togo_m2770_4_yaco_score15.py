from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2770_4_yaco_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2770_4_yaco_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2770_4_yaco")


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "4_yaco_media",
        "original_name": "4-YACo media",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": preferred_term,
                "concentration": {"value": value, "unit": unit},
            }
            for preferred_term, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2770",
            "term": {
                "id": repair_module.EXPECTED_SOURCE_TERM,
                "label": "4-YACo media",
            },
        },
        "notes": "Source: https://togomedium.org/medium/M2770",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_leaves_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_parsed([(repair_module.TARGET, repaired)]) == []


def test_repair_collapses_nested_supplement_rows(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert set(ingredients) == {
        "yeast autolysate",
        "maltose",
        "H2",
        "CO2",
        "biotin",
        "Vitamin B6 supplement",
        "Vitamin B12/corrinoid supplement",
        "L-tryptophan",
    }
    assert "solutions" not in repaired
    assert ingredients["Vitamin B6 supplement"]["concentration"] == {
        "value": "24-40",
        "unit": "MG_PER_L",
    }
    assert ingredients["Vitamin B12/corrinoid supplement"]["concentration"] == {
        "value": "6-10",
        "unit": "MG_PER_L",
    }


def test_repair_converts_per_tube_supplements(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["maltose"]["concentration"] == {
        "value": "20",
        "unit": "MILLIMOLAR",
    }
    assert ingredients["biotin"]["concentration"] == {
        "value": "60-100",
        "unit": "MICROG_PER_L",
    }
    assert ingredients["L-tryptophan"]["concentration"] == {
        "value": "12-20",
        "unit": "MG_PER_L",
    }


def test_repair_adds_gas_phase_conditions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["H2"]["concentration"] == {"value": "80", "unit": "PERCENT_V_V"}
    assert ingredients["CO2"]["concentration"] == {"value": "20", "unit": "PERCENT_V_V"}
    assert repaired["temperature_range"] == "room temperature"
    assert repaired["aeration"] == "80% H2 and 20% CO2 Balch-tube headspace"
    assert repaired["culture_vessel"] == (
        "5 ml culture in a 25 ml Balch tube with a crimp-top stopper"
    )
    assert repaired["incubation_atmosphere"] == "ANAEROBIC"


def test_repair_keeps_ambiguous_supplement_families_unmapped(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    for preferred_term in (
        "yeast autolysate",
        "Vitamin B6 supplement",
        "Vitamin B12/corrinoid supplement",
    ):
        assert "term" not in ingredients[preferred_term]
        assert "mediaingredientmech_chebi_term" not in ingredients[preferred_term]


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M2770},
        {"reference": repair_module.ROSENTHAL_2011_DOI},
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.TOGO_M2770,
            "notes": repair_module.NOTES,
        }
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    path = tmp_path / repair_module.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_doc(repair_module), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert {
        path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_SOURCE_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_component_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "3"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_reviewed_input(repair_module) -> None:
    doc = yaml.safe_load(
        (repair_module.NORMALIZED / repair_module.TARGET).read_text(encoding="utf-8")
    )

    assert doc["id"] == repair_module.EXPECTED_ID
    assert (
        repair_module._signature(doc["ingredients"], "ingredients"),
        repair_module._signature(doc.get("solutions"), "solutions"),
    ) in {
        (
            repair_module.IMPORTED_INGREDIENT_SIGNATURE,
            repair_module.IMPORTED_SOLUTION_SIGNATURE,
        ),
        (repair_module.FINAL_INGREDIENT_SIGNATURE, repair_module.FINAL_SOLUTION_SIGNATURE),
    }
