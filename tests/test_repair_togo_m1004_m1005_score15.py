from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1004_m1005_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1004_m1005_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1004_m1005")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module, target) -> dict:
    return {
        "id": target.record_id,
        "name": "modified_growth_medium_with_23_total_salt_concentration",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR"
        if target.source_term == "TOGO:M1005"
        else "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.ingredient_signature
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {target.source_term.removeprefix('TOGO:')}",
            "term": {"id": target.source_term, "label": repair_module.TITLE},
        },
        "notes": "Source: TOGO",
        "curation_history": [],
        "solutions": [
            {
                "preferred_term": "MDS salt water (see Medium [M578])",
                "composition": [],
                "concentration": {"value": "767", "unit": "G_PER_L"},
            }
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_records_add_ph_and_expand_mds_stock(repair_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, target), target)

        assert repaired["ph_value"] == 7.0
        assert repaired["solutions"] == [
            repair_module._mds_salt_water(target.source_label)
        ]

        mds = repaired["solutions"][0]
        assert mds["concentration"] == {"value": "767", "unit": "ML_PER_L"}
        assert repair_module._signature(mds["composition"], "MDS") == (
            repair_module.MDS_SIGNATURE
        )


def test_repair_records_ground_togo_components(repair_module) -> None:
    liquid = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[0]),
        repair_module.TARGETS[0],
    )
    solid = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[1]),
        repair_module.TARGETS[1],
    )

    liquid_ingredients = _by_name(liquid["ingredients"])
    solid_ingredients = _by_name(solid["ingredients"])
    mds = _by_name(liquid["solutions"][0]["composition"])

    assert liquid_ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert liquid_ingredients["Peptone (Oxoid)"]["term"] == {
        "id": "MICRO:0000178",
        "label": "peptone",
    }
    assert "mediaingredientmech_chebi_term" not in liquid_ingredients[
        "Peptone (Oxoid)"
    ]
    assert solid_ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert mds["NaCl"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert mds["1 M CaCl2 solution"]["concentration"] == {
        "value": "5.0",
        "unit": "ML_PER_L",
    }


def test_repair_records_drop_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, target), target)

        assert scorer_module.score_record(repaired) == (0, [])


def test_repair_records_add_references_and_event_once(repair_module) -> None:
    for target in repair_module.TARGETS:
        once = repair_module.repair_record(_doc(repair_module, target), target)
        twice = repair_module.repair_record(once, target)

        assert twice["references"] == [
            {"reference": url} for url in target.references
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


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:007517"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "TOGO:M1005"

    with pytest.raises(ValueError, match="expected media term TOGO:M1004"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0] = _ingredient("Distilled water", "234", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["solutions"][0]["concentration"] = {"value": "833", "unit": "G_PER_L"}

    with pytest.raises(ValueError, match="MDS solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_togo_repair_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        repaired = repair_module.repair_record(doc, target)
        final_ingredient_signature = repair_module._signature(
            target.ingredients,
            "target ingredients",
        )

        assert doc["id"] == target.record_id
        assert repair_module._source_term_id(doc) == target.source_term
        assert repair_module._signature(
            doc["ingredients"],
            "ingredients",
        ) in (target.ingredient_signature, final_ingredient_signature)
        assert repair_module._solution_signatures(doc) in (
            (repair_module.MDS_IMPORTED_SOLUTION,),
            (repair_module.MDS_FINAL_SOLUTION,),
        )
        assert repaired["solutions"][0]["concentration"] == {
            "value": "767",
            "unit": "ML_PER_L",
        }
