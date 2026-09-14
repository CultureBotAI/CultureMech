from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1400_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1400_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1400")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "ureaplasma_medium",
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
            "preferred_term": "TOGO Medium M1400",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": repair_module.TITLE},
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


def test_repair_corrects_base_formula_and_conditions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["ph_range"] == {"min": 6.0, "max": 6.2}
    assert repaired["temperature_value"] == 37.0
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )

    ingredients = _by_name(repaired["ingredients"])
    assert ingredients["PPLO broth w/o Crystal Violet (BD-Difco 255420)"] == {
        "preferred_term": "PPLO broth w/o Crystal Violet (BD-Difco 255420)",
        "concentration": {"value": "21.0", "unit": "G_PER_L"},
        "source": repair_module.SOURCE,
        "notes": (
            "JCM Medium 1303 lists 2.1 g PPLO broth w/o Crystal Violet "
            "(BD-Difco 255420) in the 100 ml final recipe; the catalog broth "
            "is not reducible to one ChEBI molecule."
        ),
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "850.0",
        "unit": "ML_PER_L",
    }


def test_repair_expands_phenol_red_stock(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    phenol = solutions["1% Phenol red solution"]

    assert (
        repair_module._solution_signatures(
            repaired,
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert phenol["concentration"] == {"value": "2.0", "unit": "ML_PER_L"}
    assert _by_name(phenol["composition"])["Phenol red"] == {
        "preferred_term": "Phenol red",
        "concentration": {"value": "1.0", "unit": "PERCENT_W_V"},
        "source": repair_module.SOURCE,
        "notes": "TOGO M1400 / JCM Medium 1303 lists 1.0 % w/v Phenol red.",
        "term": {"id": "CHEBI:31991", "label": "phenol red"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:31991",
            "label": "phenol red",
        },
    }
    assert _by_name(phenol["composition"])["NaOH"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }


def test_repair_adds_post_autoclave_serum_and_urea_yeast_stock(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    urea_yeast = _by_name(solutions["1% Urea - 4% yeast extract solution"]["composition"])

    assert solutions["Bovine calf serum (heat-inactivated)"]["concentration"] == {
        "value": "50.0",
        "unit": "ML_PER_L",
    }
    assert solutions["Bovine calf serum (heat-inactivated)"]["composition"] == []
    assert "term" not in solutions["Bovine calf serum (heat-inactivated)"]
    assert urea_yeast["Urea"]["concentration"] == {
        "value": "1.0",
        "unit": "PERCENT_W_V",
    }
    assert urea_yeast["Yeast extract"]["concentration"] == {
        "value": "4.0",
        "unit": "PERCENT_W_V",
    }


def test_repair_adds_preparation_metadata(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["sterilization"] == {
        "method": "AUTOCLAVE",
        "temperature": {"value": 121.0, "unit": "CELSIUS"},
        "duration": "15 min",
        "notes": (
            "Autoclave the base before cooling to 50-55 C and "
            "aseptically adding filter-sterilized bovine calf serum "
            "and 1% Urea - 4% yeast extract solution."
        ),
    }
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "ADJUST_PH",
        "AUTOCLAVE",
        "COOL",
        "MIX",
        "ALIQUOT",
    ]
    assert repaired["culture_vessel"] == "sterilized 15 ml plastic tubes"


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

    assert twice["references"] == [{"reference": url} for url in repair_module.REFERENCES]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "moved the printed stock recipes under solutions" in (matching_events[0]["notes"])


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
    doc["ingredients"][0] = _ingredient("Water", "185.0", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["preferred_term"] = "Phenol red"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m1400_repair_contract(
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
