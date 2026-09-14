from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_2070_score15.py"
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
    return _load_script(SCRIPT, "repair_komodo_2070_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_2070")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module, target: Path) -> dict:
    expected = repair_module.TARGETS[target]
    return {
        "id": expected["id"],
        "name": target.stem,
        "original_name": "Trace metal solution (Kelly solution T)",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": repair_module.PH_VALUE,
        "notes": "pH buffer: NaOH | Source: KOMODO ModelSEED | ID: 2070",
        "media_term": {
            "preferred_term": "KOMODO Medium 2070",
            "term": {
                "id": expected["media_term"],
                "label": "Trace metal solution (Kelly solution T)",
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


def test_repair_expands_both_komodo_2070_records(repair_module, scorer_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(target, _doc(repair_module, target))
        ingredients = _by_name(repaired["ingredients"])

        assert repair_module._signature(repaired["ingredients"]) == (
            repair_module.FINAL_INGREDIENT_SIGNATURE
        )
        assert repaired["record_kind"] == "SOLUTION"
        assert repaired["ph_value"] == 6.0
        assert set(ingredients) == {
            name for name, _value, _unit in repair_module.FINAL_INGREDIENT_SIGNATURE
        }
        assert ingredients["NaOH"]["concentration"] == {
            "value": "9.00",
            "unit": "G_PER_L",
        }
        assert ingredients["EDTA"]["concentration"] == {
            "value": "50.00",
            "unit": "G_PER_L",
        }
        assert ingredients["CaCl2 x 2 H2O"]["concentration"] == {
            "value": "5.00",
            "unit": "G_PER_L",
        }
        assert ingredients["H2O"]["concentration"] == {
            "value": "1.0",
            "unit": "L",
        }
        assert scorer_module.score_record(repaired) == (0, [])
        assert scorer_module.score_parsed([(str(target), repaired)]) == []


def test_repair_grounds_all_disclosed_components(repair_module) -> None:
    repaired = repair_module.repair_record(
        repair_module.PRIMARY_TARGET,
        _doc(repair_module, repair_module.PRIMARY_TARGET),
    )
    ingredients = _by_name(repaired["ingredients"])

    for name, (identifier, label) in repair_module.GROUNDINGS.items():
        assert ingredients[name]["term"] == {"id": identifier, "label": label}
        assert ingredients[name]["mediaingredientmech_chebi_term"] == {
            "id": identifier,
            "label": label,
        }

    assert ingredients["Ammonium molybdate"]["term"] == {
        "id": "CHEBI:91249",
        "label": "ammonium molybdate",
    }
    assert ingredients["EDTA"]["term"] == {
        "id": "CHEBI:4735",
        "label": "ethylenediaminetetraacetic acid",
    }


def test_repair_preserves_naoh_as_process_context(repair_module) -> None:
    repaired = repair_module.repair_record(
        repair_module.PRIMARY_TARGET,
        _doc(repair_module, repair_module.PRIMARY_TARGET),
    )
    ingredients = _by_name(repaired["ingredients"])

    ph_step = repaired["preparation_steps"][1]["description"]
    assert "pH 6.0" in ph_step
    assert "NaOH" in ph_step
    assert ingredients["NaOH"]["source"] == repair_module.SOURCE
    assert "NaOH" in repaired["curation_history"][-1]["notes"]


def test_repair_adds_reference_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(
        repair_module.REPLACEMENT_TARGET,
        _doc(repair_module, repair_module.REPLACEMENT_TARGET),
    )
    twice = repair_module.repair_record(repair_module.REPLACEMENT_TARGET, once)

    assert twice == once
    assert once["references"] == [{"reference": repair_module.KOMODO_2070}]
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

    with pytest.raises(ValueError, match="CultureMech:004346"):
        repair_module.repair_record(repair_module.PRIMARY_TARGET, doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module, repair_module.PRIMARY_TARGET)
    doc["media_term"]["term"]["id"] = "komodo.medium:3096"

    with pytest.raises(ValueError, match="komodo.medium:2070"):
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
            "preferred_term": "Trace metal solution",
            "concentration": {"value": "1", "unit": "ML_PER_L"},
        }
    ]

    with pytest.raises(ValueError, match="unexpected solutions"):
        repair_module.repair_record(repair_module.PRIMARY_TARGET, doc)
