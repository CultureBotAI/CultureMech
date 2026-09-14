from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_220_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
sys.path.insert(0, str(REPO / "src"))
from culturemech.ingredients import resolve_ingredient  # noqa: E402


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_nbrc_220_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_nbrc_220")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(
    name: str,
    value: str,
    unit: str,
    composition: list[dict] | None = None,
) -> dict:
    return {
        "preferred_term": name,
        "term": {
            "id": "mediadive.solution:5555",
            "label": "Soil extract",
        },
        "concentration": {"value": value, "unit": unit},
        "composition": list(composition or []),
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "togo_medium_m1448",
        "original_name": "(Unnamed medium)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in repair_module.LEGACY_INGREDIENTS
        ],
        "solutions": [
            _solution(name, value, unit, list(composition))
            for name, value, unit, composition in repair_module.LEGACY_SOLUTIONS
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1448",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "TOGO Medium M1448",
            },
        },
        "notes": "Source: NBRC - NBRC_M220",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_formula_and_exits_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])
    soil_extract = solutions["Soil extract"]

    assert repaired["ph_value"] == 7.4
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENTS
    )
    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTIONS
    )
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "950",
        "unit": "ML_PER_L",
    }
    assert soil_extract["concentration"] == {"value": "50", "unit": "ML_PER_L"}
    assert "term" not in soil_extract
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_defined_components_and_leaves_farm_soil_unmapped(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    soil_extract = repaired["solutions"][0]
    soil_components = _by_name(soil_extract["composition"])

    assert ingredients["Sodium acetate"]["term"] == {
        "id": "CHEBI:32954",
        "label": "sodium acetate",
    }
    assert ingredients["Distilled water"]["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["Agar (if needed)"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Agar (if needed)"]["physicochemical_roles"] == [
        "SOLIDIFYING_AGENT",
    ]
    assert soil_components["Distilled water"]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert "term" not in ingredients["Yeast extract"]
    assert "term" not in ingredients["Bacto Tryptone (Difco)"]
    assert "term" not in soil_components["Farm soil"]

    unresolved = {
        ingredient["preferred_term"]
        for ingredient in [*repaired["ingredients"], *soil_extract["composition"]]
        if not resolve_ingredient(ingredient).is_resolved
    }
    assert unresolved == {"Farm soil"}


def test_repair_adds_preparation_references_flags_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]

    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert matching_events == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": "; ".join(repair_module.REFERENCES),
            "notes": (
                "Curated TOGO:M1448 from TOGO and NBRC Medium 220; "
                "corrected the Distilled water and Soil extract volume "
                "units, moved farm soil to the source-specific nested Soil "
                "extract, added pH 7.4, grounded Sodium acetate, Distilled "
                "water, and agar, and removed the false "
                "mediadive.solution:5555 Soil extract link."
            ),
        }
    ]


def test_plan_repairs_target_record(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    expected = repair_module.repair_record(yaml.safe_load(path.read_text(encoding="utf-8")))

    assert repair_module.plan_repairs() == {path: expected}


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1447"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][1] = _ingredient("Yeast extract", "3", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0] = _solution("Soil extract*", "50", "ML_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_corpus_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in {
        repair_module.LEGACY_INGREDIENTS,
        repair_module.FINAL_INGREDIENTS,
    }
    assert repair_module._solution_signatures(doc.get("solutions"), "solutions") in {
        repair_module.LEGACY_SOLUTIONS,
        repair_module.FINAL_SOLUTIONS,
    }
