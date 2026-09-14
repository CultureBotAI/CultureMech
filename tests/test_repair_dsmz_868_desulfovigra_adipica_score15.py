from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_868_desulfovigra_adipica_score15.py"
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
    return _load_script(SCRIPT, "repair_dsmz_868_desulfovigra_adipica_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_868")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_range": {"min": 7.0, "max": 7.2},
        "notes": (
            "pH buffer: Na2CO3 | Source: KOMODO ModelSEED | ID: 868 | "
            "DSMZ Medium: 868 (mediadive.medium:868) | Aerobic: Yes"
        ),
        "media_term": {
            "preferred_term": "KOMODO Medium 868",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "ingredients": [_ingredient("Na2CO3", "variable", "VARIABLE")],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:634c",
    }


def _solution_by_name(repaired: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in repaired["solutions"]}


def test_repair_reconstructs_archived_dsmz_868_and_exits_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_range"] == {"min": 7.0, "max": 7.2}
    assert repaired["ingredients"] == []
    assert repair_module._solution_signatures(
        repaired["solutions"],
    ) == repair_module.FINAL_SOLUTION_SIGNATURES
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_disclosed_dsmz_stock_solutes(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _solution_by_name(repaired)

    sulfate = solutions["10% (w/v) Na2SO4 solution"]["composition"][0]
    yeast = solutions["10% (w/v) Yeast extract solution"]["composition"][0]
    propanol = solutions["10% (v/v) Propanol solution"]["composition"][0]
    sulfide = solutions["3% (w/v) Na2S x 9H2O solution"]["composition"][0]

    assert sulfate["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32149",
        "label": "sodium sulfate",
    }
    assert yeast["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert propanol["term"] == {
        "id": "CHEBI:28831",
        "label": "Propan-1-ol",
    }
    assert sulfide["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }


def test_repair_keeps_referenced_dsmz_stocks_opaque(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _solution_by_name(repaired)

    assert (
        solutions["Trace element solution SL-10 (DSMZ Medium 320)"]["composition"]
        == []
    )
    assert (
        solutions["Selenite-tungstate solution (DSMZ Medium 385)"]["composition"]
        == []
    )
    assert solutions["Vitamin solution (DSMZ Medium 141)"]["composition"] == []


def test_repair_adds_preparation_source_and_removes_stale_kg_match(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert "kg_microbe_match" not in twice
    assert twice["references"] == [{"reference": repair_module.ARCHIVED_DSMZ_868}]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert [step["action"] for step in twice["preparation_steps"]] == [
        "MIX",
        "ADJUST_PH",
        "MIX",
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


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:868"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_imported_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Na2CO3", "5", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_final_solution_drift(repair_module) -> None:
    doc = repair_module.repair_record(_doc(repair_module))
    doc["solutions"][0]["concentration"]["value"] = "8.0"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_dsmz_868_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._ingredient_signature(doc["ingredients"]) in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    if repair_module._ingredient_signature(doc["ingredients"]) == ():
        assert (
            repair_module._solution_signatures(doc["solutions"])
            == repair_module.FINAL_SOLUTION_SIGNATURES
        )
