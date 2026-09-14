from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_2072_score15.py"
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
    return _load_script(SCRIPT, "repair_komodo_2072_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_2072")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module, target: Path) -> dict:
    expected = repair_module.TARGETS[target]
    return {
        "id": expected["id"],
        "name": target.stem,
        "original_name": "Trace metals solution (Pfennig & Lippert, 1966)",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_range": repair_module.PH_RANGE.copy(),
        "notes": "pH buffer: HCl | Source: KOMODO ModelSEED | ID: 2072",
        "media_term": {
            "preferred_term": "KOMODO Medium 2072",
            "term": {
                "id": expected["media_term"],
                "label": "Trace metals solution (Pfennig & Lippert, 1966)",
            },
        },
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_expands_parent_komodo_2072_record(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(
        repair_module.PRIMARY_TARGET,
        _doc(repair_module, repair_module.PRIMARY_TARGET),
    )
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"]) == (
        repair_module.PARENT_INGREDIENT_SIGNATURE
    )
    assert repaired["record_kind"] == "SOLUTION"
    assert repaired["ph_range"] == {"min": 3.0, "max": 4.0}
    assert "Na2MoO4 x 2 H2O" in ingredients
    assert "NH4MoO4" not in ingredients
    assert ingredients["EDTA"]["concentration"] == {
        "value": "5.00",
        "unit": "G_PER_L",
    }
    assert ingredients["H2O"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.PRIMARY_TARGET), repaired)]) == []


def test_repair_expands_replacement_komodo_2072_record(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(
        repair_module.REPLACEMENT_TARGET,
        _doc(repair_module, repair_module.REPLACEMENT_TARGET),
    )
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"]) == (
        repair_module.REPLACEMENT_INGREDIENT_SIGNATURE
    )
    assert "NH4MoO4" in ingredients
    assert "Na2MoO4 x 2 H2O" not in ingredients
    assert ingredients["NH4MoO4"]["concentration"] == {
        "value": "0.02",
        "unit": "G_PER_L",
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.REPLACEMENT_TARGET), repaired)]) == []


def test_repair_grounds_all_disclosed_components(repair_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(target, _doc(repair_module, target))
        ingredients = _by_name(repaired["ingredients"])

        for name in ingredients:
            identifier, label = repair_module.GROUNDINGS[name]
            assert ingredients[name]["term"] == {"id": identifier, "label": label}
            assert ingredients[name]["mediaingredientmech_chebi_term"] == {
                "id": identifier,
                "label": label,
            }

    replacement = repair_module.repair_record(
        repair_module.REPLACEMENT_TARGET,
        _doc(repair_module, repair_module.REPLACEMENT_TARGET),
    )
    assert _by_name(replacement["ingredients"])["NH4MoO4"]["term"] == {
        "id": "CHEBI:91249",
        "label": "ammonium molybdate",
    }


def test_repair_preserves_hcl_as_process_context(repair_module) -> None:
    repaired = repair_module.repair_record(
        repair_module.PRIMARY_TARGET,
        _doc(repair_module, repair_module.PRIMARY_TARGET),
    )
    ingredients = _by_name(repaired["ingredients"])

    ph_step = repaired["preparation_steps"][1]["description"]
    assert "pH 3.0-4.0" in ph_step
    assert "HCl" in ph_step
    assert ingredients["HCl"]["source"] == repair_module.SOURCE_LABELS[
        repair_module.PRIMARY_TARGET
    ]
    assert "HCl" in repaired["curation_history"][-1]["notes"]


def test_repair_adds_reference_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(
        repair_module.REPLACEMENT_TARGET,
        _doc(repair_module, repair_module.REPLACEMENT_TARGET),
    )
    twice = repair_module.repair_record(repair_module.REPLACEMENT_TARGET, once)

    assert twice == once
    assert once["references"] == [
        {"reference": repair_module.REFERENCES[repair_module.REPLACEMENT_TARGET]}
    ]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1


def test_plan_repairs_target_records(repair_module) -> None:
    expected_targets = {repair_module.NORMALIZED / target for target in repair_module.TARGETS}

    assert set(repair_module.plan_repairs()) == expected_targets


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module, repair_module.PRIMARY_TARGET)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="CultureMech:004349"):
        repair_module.repair_record(repair_module.PRIMARY_TARGET, doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module, repair_module.PRIMARY_TARGET)
    doc["media_term"]["term"]["id"] = "komodo.medium:2070"

    with pytest.raises(ValueError, match="komodo.medium:2072"):
        repair_module.repair_record(repair_module.PRIMARY_TARGET, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.PRIMARY_TARGET)
    doc["ingredients"][0]["preferred_term"] = "KOH"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(repair_module.PRIMARY_TARGET, doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.PRIMARY_TARGET)
    doc["solutions"] = [
        {
            "preferred_term": "Trace metals solution",
            "concentration": {"value": "1", "unit": "ML_PER_L"},
        }
    ]

    with pytest.raises(ValueError, match="unexpected solutions"):
        repair_module.repair_record(repair_module.PRIMARY_TARGET, doc)
