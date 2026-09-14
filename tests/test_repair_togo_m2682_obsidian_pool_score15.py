from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2682_obsidian_pool_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2682_obsidian_pool")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2682")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "obsidian_pool_fermentor_opf_medium_modified_from_m_b_allen_1959",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2682",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: https://togomedium.org/medium/M2682",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "high_metal": True,
        "solutions": [
            {
                "preferred_term": "Wolfe's Vitamin Solution (1,000X_x0008_)",
                "composition": [],
                "concentration": {"value": "1", "unit": "G_PER_L"},
                "notes": "Role: Growth factor; Properties: Complex component",
                "name": "Unknown solution",
            },
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_stock_units_and_nests_mixed_stock(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert (
        repair_module._ingredient_signature(
            repaired["ingredients"],
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )

    assert ingredients["Na2MoO4 x 2 H2O"]["concentration"] == {
        "value": "0.03",
        "unit": "MG_PER_L",
    }
    assert ingredients["Na2B4O7 x 10 H2O"]["concentration"] == {
        "value": "4.5",
        "unit": "MG_PER_L",
    }
    assert "LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) (1 mg/ml each)" not in ingredients
    assert _by_name(solutions["LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) stock"]["composition"])["LiCl"][
        "concentration"
    ] == {
        "value": "1.0",
        "unit": "G_PER_L",
    }
    assert "Distilled water" not in _by_name(
        solutions["LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) stock"]["composition"]
    )


def test_repair_adds_conditions_and_clears_high_metal(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["temperature_value"] == 85.0
    assert repaired["aeration"] == "N2/CO2 (80:20) bubbled at 20 ml/min"
    assert repaired["incubation_atmosphere"] == "ANAEROBIC"
    assert "high_metal" not in repaired


def test_repair_grounds_source_supported_components(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    stock = _by_name(repaired["solutions"])["LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) stock"]
    stock_components = _by_name(stock["composition"])

    assert ingredients["Na2S x 9 H2O"]["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }
    assert ingredients["Na2S2O3"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:132112",
        "label": "sodium thiosulfate",
    }
    assert stock_components["Na2SeO3"]["term"] == {
        "id": "CHEBI:48843",
        "label": "disodium selenite",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Yeast Extract"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Peptone"]
    assert "term" not in stock_components["Ni(NH4)2(SO4)"]


def test_repair_record_exits_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
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
    assert matching_events[0]["source"] == "; ".join(repair_module.REFERENCES)


def test_repair_record_accepts_legacy_nested_stock_solvent(repair_module) -> None:
    legacy = repair_module.repair_record(_doc(repair_module))
    stock = _by_name(legacy["solutions"])["LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) stock"]
    stock["composition"].insert(
        0,
        repair_module._component(
            "Distilled water",
            "1000.0",
            "ML_PER_L",
            "TOGO M2682 defines the Li/W/Se/Ni stock in 1 ml distilled water.",
        ),
    )

    repaired = repair_module.repair_record(legacy)
    stock = _by_name(repaired["solutions"])["LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) stock"]

    assert "Distilled water" not in _by_name(stock["composition"])


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:009237"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1470"

    with pytest.raises(ValueError, match="expected media term TOGO:M2682"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_signature_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "31"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc)
