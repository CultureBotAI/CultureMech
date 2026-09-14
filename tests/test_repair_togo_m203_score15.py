from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m203_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m203_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m203")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [],
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "modified_medium_10",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M203",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_units_and_adds_ph_range(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ph_range"] == {"min": 6.7, "max": 6.8}
    assert "ph_value" not in repaired
    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repair_module._solution_signatures(
        repaired,
    ) == repair_module.FINAL_SOLUTION_SIGNATURES


def test_repair_grounds_medium_10_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "850.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Yeast extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Trypticase peptone (BD-BBL)"]["term"] == {
        "id": "MICRO:0000175",
        "label": "Trypticase peptone",
    }


def test_repair_represents_modified_hemin_stock(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert solutions["1.0% Hemin solution"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert solutions["1.0% Hemin solution"]["composition"] == [
        {
            "preferred_term": "Hemin",
            "concentration": {"value": "1.0", "unit": "PERCENT_W_V"},
            "source": repair_module.SOURCE,
            "notes": "TOGO M203 / JCM Medium 210 identifies the growth-factor stock as 1.0% Hemin.",
            "term": {"id": "CHEBI:50385", "label": "hemin"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:50385", "label": "hemin"},
        }
    ]


def test_repair_represents_other_simple_stock_solutes(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert solutions["0.1% Resazurin solution"]["composition"][0]["term"] == {
        "id": "CHEBI:8806",
        "label": "Resazurin",
    }
    assert solutions["4% Na2SO3 solution"]["composition"][0][
        "mediaingredientmech_chebi_term"
    ] == {"id": "CHEBI:86477", "label": "sodium sulfite"}
    assert solutions["25% L--Ascorbic acid solution"]["composition"][0][
        "concentration"
    ] == {"value": "25.0", "unit": "PERCENT_W_V"}
    assert solutions["5% L--Cysteine\u30fbHCl\u30fbH2O solution"]["composition"][
        0
    ]["term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }


def test_repair_keeps_m124_cross_reference_stocks_opaque(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert solutions["VFA solution (see Medium [M124])"]["composition"] == []
    assert (
        "TOGO M124 / JCM Medium 133 defines the source stock"
        in solutions["Salt solution No. 1 (see Medium [M124])"]["notes"]
    )
    assert (
        "TOGO M124 / JCM Medium 133 defines the source stock"
        in solutions["Salt solution No. 2 (see Medium [M124])"]["notes"]
    )


def test_repair_adds_only_source_stated_ph_and_medium_10_steps(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert "sterilization" not in repaired
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 6.7-6.8.",
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": (
                "Use Medium 10 from JCM Medium 133 with 1.0 ml/L final 1% "
                "hemin solution, and omit Toray silicone solution."
            ),
        },
    ]


def test_repair_record_drops_out_of_review_ranking(
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
        {"reference": url} for url in repair_module.REFERENCES
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
    assert "Corrected imported ml additions" in matching_events[0]["notes"]


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Water", "850", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][1] = _solution("0.2% Hemin solution", "0.5", "G_PER_L")

    with pytest.raises(ValueError, match="solution signatures drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m203_repair_contract(
    repair_module,
) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert repair_module._solution_signatures(doc) in (
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )
