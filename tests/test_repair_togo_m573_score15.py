from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m573_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m573_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m573")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    original_name = "Yeast Extract-Malt Extract Agar (ISP-2) With Artificial Seawater"
    return {
        "id": target.record_id,
        "name": Path(target.path).stem,
        "original_name": original_name,
        "category": "fungal" if str(target.path).startswith("fungal/") else "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": target.source,
            "term": {"id": target.source_term, "label": original_name},
        },
        "notes": "Source: imported",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_signature
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_togo_m573_gets_jcm_formula_ph_sterilization_and_parent_link(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.TOGO_M573_PATH]
    doc = _doc(target)
    doc["kg_microbe_match"] = "mediadive.medium:7"
    repaired = repair_module.repair_record(doc, target)
    ingredients = _by_name(repaired["ingredients"])

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.JCM_FINAL
    )
    assert repaired["ph_value"] == 7.3
    assert repaired["sterilization"] == repair_module.JCM_STERILIZATION
    assert "kg_microbe_match" not in repaired
    assert ingredients["Artificial seawater"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Malt extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03301056",
        "label": "malt extract",
    }
    assert ingredients["Glucose"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert repaired["parent_media"]["id"] == "CultureMech:010536"
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert scorer_module.score_record(repaired) == (0, [])


def test_nbrc_m1804_keeps_bacto_names_and_removes_stale_match(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.TOGO_M1804_PATH]
    doc = _doc(target)
    doc["kg_microbe_match"] = "mediadive.medium:7"
    repaired = repair_module.repair_record(doc, target)
    ingredients = _by_name(repaired["ingredients"])

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.NBRC_FINAL
    )
    assert "sterilization" not in repaired
    assert "kg_microbe_match" not in repaired
    assert ingredients["Bacto Yeast Extract (Difco)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Artificial seawater"]["notes"].endswith(
        "without a single-compound ontology grounding."
    )
    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M1804},
        {"reference": repair_module.NBRC_1030},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_jcm_j569_fixes_mediadive_water_units_and_links_both_togo_rows(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.JCM_J569_PATH]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.JCM_FINAL
    )
    assert "Sea water" not in ingredients
    assert repaired["references"] == [
        {"reference": repair_module.JCM_569},
        {"reference": repair_module.MEDIADIVE_J569},
    ]
    assert repaired["variant_children"] == [
        repair_module.TOGO_M573_CHILD,
        repair_module.TOGO_M1804_CHILD,
    ]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_is_idempotent_and_records_one_event(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.TOGO_M573_PATH]
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    matching_events = [
        event
        for event in twice["curation_history"]
        if (event.get("curator") == repair_module.CURATOR and event.get("action") == target.action)
    ]
    assert len(matching_events) == 1
    assert "removed the stale MediaDive 7 match" in matching_events[0]["notes"]
