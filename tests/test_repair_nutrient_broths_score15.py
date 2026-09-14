from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nutrient_broths_score15.py"
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
    return _load_script(SCRIPT, "repair_nutrient_broths_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_nutrient_broths")


def _component(name: str, value: str, unit: str) -> dict:
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
            _component(name, value, unit)
            for name, value, unit in repair.imported_ingredients
        ],
        "media_term": {
            "preferred_term": repair.source_term,
            "term": {"id": repair.source_term, "label": repair.path.stem},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }
    if repair.imported_solutions:
        doc["solutions"] = [
            {
                "preferred_term": name,
                "composition": [],
                "concentration": {"value": value, "unit": unit},
            }
            for name, value, unit in repair.imported_solutions
        ]
    return doc


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_top_score_targets_exit_review_ranking(repair_module, scorer_module) -> None:
    for repair in repair_module.REPAIRS:
        repaired = repair_module.repair_target(repair, _doc(repair))

        assert scorer_module.score_parsed([(str(repair.path), repaired)]) == []
        assert "ingredients_curated" in repaired["data_quality_flags"]
        assert "has_ontology_mappings" in repaired["data_quality_flags"]


def test_nbrc_carbonate_records_fix_empty_solution_wrappers(
    repair_module,
) -> None:
    m1680 = repair_module.repair_target(
        repair_module.REPAIR_BY_PATH[repair_module.M1680],
        _doc(repair_module.REPAIR_BY_PATH[repair_module.M1680]),
    )
    m1760 = repair_module.repair_target(
        repair_module.REPAIR_BY_PATH[repair_module.M1760],
        _doc(repair_module.REPAIR_BY_PATH[repair_module.M1760]),
    )
    m1680_ingredients = _by_name(m1680["ingredients"])
    m1760_ingredients = _by_name(m1760["ingredients"])

    assert "solutions" not in m1680
    assert m1680["ph_value"] == 10.5
    assert m1680_ingredients["Na2CO3"]["term"] == {
        "id": "CHEBI:29377",
        "label": "sodium carbonate",
    }
    assert m1680_ingredients["Bacto Nutrient Broth (Difco)"][
        "concentration"
    ] == {"value": "8.0", "unit": "G_PER_L"}

    assert "solutions" not in m1760
    assert m1760["ph_value"] == 10.0
    assert m1760_ingredients["NaHCO3"]["term"] == {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate",
    }
    assert m1760_ingredients["Na2CO3"]["concentration"] == {
        "value": "5.3",
        "unit": "G_PER_L",
    }
    assert "has_unmapped_ingredients" in m1760["data_quality_flags"]


def test_nutrient_broth_no_2_adds_ph_range_and_grounds_components(
    repair_module,
) -> None:
    repair = repair_module.REPAIR_BY_PATH[repair_module.M2170]
    repaired = repair_module.repair_target(repair, _doc(repair))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["ph_range"] == {"min": 7.3, "max": 7.7}
    assert "has_unmapped_ingredients" not in repaired["data_quality_flags"]
    assert ingredients["Lab-Lemco powder"]["term"] == {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    }
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }


def test_togo_paper_records_add_temperature_and_curated_opaque_inputs(
    repair_module,
) -> None:
    nbii = repair_module.repair_target(
        repair_module.REPAIR_BY_PATH[repair_module.M2894],
        _doc(repair_module.REPAIR_BY_PATH[repair_module.M2894]),
    )
    nr = repair_module.repair_target(
        repair_module.REPAIR_BY_PATH[repair_module.M3207],
        _doc(repair_module.REPAIR_BY_PATH[repair_module.M3207]),
    )
    nbii_ingredients = _by_name(nbii["ingredients"])
    nr_ingredients = _by_name(nr["ingredients"])

    assert nbii["temperature_value"] == 30.0
    assert "term" not in nbii_ingredients["Peptone from gelatine"]
    assert nbii_ingredients["Peptone from casein"]["term"] == {
        "id": "FOODON:03315719",
        "label": "Casein peptone",
    }

    assert nr["temperature_value"] == 30.0
    assert "term" not in nr_ingredients["Meat extract"]
    assert nr_ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
