from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m938_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m938_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m938")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _m938_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:010360",
        "name": "5_salt_water_growth_medium",
        "original_name": "5% Salt Water Growth Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.M938_IMPORTED_INGREDIENTS
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M938",
            "term": {"id": "TOGO:M938", "label": "5% Salt Water Growth Medium"},
        },
        "notes": "Source: TOGO",
        "curation_history": [],
        "solutions": [
            {
                "preferred_term": "MDS salt water (see Medium [M578])",
                "composition": [],
                "concentration": {"value": "100", "unit": "G_PER_L"},
            }
        ],
    }


def _mds_helper_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:013393",
        "preferred_term": "MDS salt water",
        "term": {"id": "mediadive.solution:4404", "label": "MDS salt water"},
        "composition": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.MDS_IMPORTED_COMPOSITION
        ],
        "preparation_notes": "Add components to distilled water.",
        "curation_history": [],
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.PLACEHOLDER_INGREDIENTS
        ],
        "data_quality_flags": ["incomplete_composition"],
        "category": "bacterial",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_m938_adds_ph_and_expands_mds_stock(repair_module) -> None:
    repaired = repair_module.repair_m938(_m938_doc(repair_module))

    assert repaired["ph_value"] == 7.5
    assert repaired["ingredients"] == [
        repair_module._medium_component("Distilled water", "500.0", "ML_PER_L"),
        repair_module._medium_component("Yeast extract (BD-Difco)", "0.6", "G_PER_L"),
        repair_module._medium_component("Peptone (Oxoid)", "3.0", "G_PER_L"),
    ]
    assert repaired["solutions"] == [repair_module._mds_salt_water()]
    assert repaired["solutions"][0]["concentration"] == {"value": "100.0", "unit": "ML_PER_L"}
    assert (
        repair_module._signature(
            repaired["solutions"][0]["composition"],
            "MDS",
        )
        == repair_module.M938_FINAL_SOLUTION[3]
    )


def test_repair_m938_moves_tris_to_preparation_step(repair_module) -> None:
    repaired = repair_module.repair_m938(_m938_doc(repair_module))

    assert "Tris base" not in _by_name(repaired["ingredients"])
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Mix distilled water, Yeast extract (BD-Difco), Peptone (Oxoid), "
                "and MDS salt water."
            ),
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust to pH 7.5 with 1 M Tris base.",
        },
    ]


def test_repair_m938_grounds_medium_and_mds_components(repair_module) -> None:
    repaired = repair_module.repair_m938(_m938_doc(repair_module))

    ingredients = _by_name(repaired["ingredients"])
    mds = _by_name(repaired["solutions"][0]["composition"])

    assert ingredients["Yeast extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Peptone (Oxoid)"]["term"] == {
        "id": "MICRO:0000178",
        "label": "peptone",
    }
    assert mds["NaCl"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert mds["1 M CaCl2 solution"]["concentration"] == {
        "value": "5.0",
        "unit": "ML_PER_L",
    }


def test_repair_mds_helper_removes_placeholder(repair_module) -> None:
    repaired = repair_module.repair_mds_helper(_mds_helper_doc(repair_module))

    assert "ingredients" not in repaired
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert (
        repair_module._signature(
            repaired["composition"],
            "MDS helper composition",
        )
        == repair_module.M938_FINAL_SOLUTION[3]
    )


def test_repair_m938_drops_out_of_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_m938(_m938_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])


def test_repairs_add_references_and_events_once(repair_module) -> None:
    once = repair_module.repair_m938(_m938_doc(repair_module))
    twice = repair_module.repair_m938(once)

    assert twice["references"] == [
        {"reference": repair_module.TOGO_M938},
        {"reference": repair_module.TOGO_M578},
        {"reference": repair_module.JCM_897},
        {"reference": repair_module.JCM_574},
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION_M938
        )
    ]
    assert len(matching_events) == 1

    once_helper = repair_module.repair_mds_helper(_mds_helper_doc(repair_module))
    twice_helper = repair_module.repair_mds_helper(once_helper)
    assert twice_helper["references"] == [
        {"reference": repair_module.TOGO_M578},
        {"reference": repair_module.JCM_574},
    ]


def test_repair_m938_rejects_drift(repair_module) -> None:
    wrong_id = _m938_doc(repair_module)
    wrong_id["id"] = "CultureMech:wrong"
    with pytest.raises(ValueError, match="expected id CultureMech:010360"):
        repair_module.repair_m938(wrong_id)

    wrong_media_term = _m938_doc(repair_module)
    wrong_media_term["media_term"]["term"]["id"] = "TOGO:M937"
    with pytest.raises(ValueError, match="expected media term TOGO:M938"):
        repair_module.repair_m938(wrong_media_term)

    ingredient_drift = _m938_doc(repair_module)
    ingredient_drift["ingredients"][0] = _ingredient("Distilled water", "501", "G_PER_L")
    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_m938(ingredient_drift)

    solution_drift = _m938_doc(repair_module)
    solution_drift["solutions"][0]["concentration"] = {"value": "99", "unit": "G_PER_L"}
    with pytest.raises(ValueError, match="MDS solution signature drifted"):
        repair_module.repair_m938(solution_drift)


def test_repair_mds_helper_rejects_drift(repair_module) -> None:
    wrong_solution = _mds_helper_doc(repair_module)
    wrong_solution["term"]["id"] = "mediadive.solution:wrong"
    with pytest.raises(ValueError, match="expected mediadive solution 4404"):
        repair_module.repair_mds_helper(wrong_solution)

    composition_drift = _mds_helper_doc(repair_module)
    composition_drift["composition"][0] = _ingredient("NaCl", "241", "G_PER_L")
    with pytest.raises(ValueError, match="MDS helper composition drifted"):
        repair_module.repair_mds_helper(composition_drift)

    ingredient_drift = _mds_helper_doc(repair_module)
    ingredient_drift["ingredients"][0] = _ingredient("Unknown", "variable", "VARIABLE")
    with pytest.raises(ValueError, match="MDS helper ingredients drifted"):
        repair_module.repair_mds_helper(ingredient_drift)


def test_target_records_match_togo_repair_contract(repair_module) -> None:
    m938 = yaml.safe_load(
        (repair_module.NORMALIZED / repair_module.M938_PATH).read_text(encoding="utf-8")
    )
    repaired_m938 = repair_module.repair_m938(m938)

    assert m938["id"] == "CultureMech:010360"
    assert repair_module._source_term_id(m938) == "TOGO:M938"
    assert repair_module._signature(m938["ingredients"], "ingredients") in (
        repair_module.M938_IMPORTED_INGREDIENTS,
        repair_module.M938_INGREDIENTS,
    )
    assert repair_module._solution_signatures(m938) in (
        (repair_module.M938_IMPORTED_SOLUTION,),
        (repair_module.M938_FINAL_SOLUTION,),
    )
    assert repaired_m938["ph_value"] == 7.5

    mds = yaml.safe_load(
        (repair_module.NORMALIZED / repair_module.MDS_HELPER_PATH).read_text(encoding="utf-8")
    )
    repaired_mds = repair_module.repair_mds_helper(mds)

    assert mds["id"] == "CultureMech:013393"
    assert repair_module._signature(mds["composition"], "MDS helper composition") in (
        repair_module.MDS_IMPORTED_COMPOSITION,
        repair_module.M938_FINAL_SOLUTION[3],
    )
    assert repair_module._signature(mds.get("ingredients"), "MDS helper ingredients") in (
        repair_module.PLACEHOLDER_INGREDIENTS,
        (),
    )
    assert (
        repair_module._signature(
            repaired_mds["composition"],
            "MDS helper composition",
        )
        == repair_module.M938_FINAL_SOLUTION[3]
    )
