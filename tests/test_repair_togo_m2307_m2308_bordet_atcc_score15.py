from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2307_m2308_bordet_atcc_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2307_m2308_bordet_atcc_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2307_m2308_bordet")


def _component(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": target.path.stem,
        "original_name": "Bordet Gengou Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": target.source,
            "term": {"id": target.media_term, "label": target.source},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_agar_fixes_atcc_volume_rows_and_ph(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[
        Path("bacterial/bordet_gengou_agar_medium.yaml")
    ]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["ph_value"] == 6.7
    assert "solutions" not in repaired
    assert repair_module._component_signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module._final_ingredient_signature(target)
    assert ingredients["Glycerol"]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["DI Water"]["concentration"] == {
        "value": "840.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Sterile Defibrinated Rabbit Blood"]["concentration"] == {
        "value": "15",
        "unit": "PERCENT_V_V",
    }


def test_repair_broth_moves_base_components_to_solution(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH[
        Path("bacterial/bordet_gengou_broth_medium.yaml")
    ]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])
    solution = repaired["solutions"][0]
    composition = _by_name(solution["composition"])

    assert list(ingredients) == [
        "Glycerol",
        "Proteose Peptone",
        "Sterile Defibrinated Rabbit Blood",
    ]
    assert solution["preferred_term"] == "Bordet-Gengou Broth Base"
    assert solution["concentration"] == {
        "value": "840.0",
        "unit": "ML_PER_L",
    }
    assert composition["DI Water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert composition["NaCl"]["term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


def test_repair_scores_both_records_clean(repair_module, scorer_module) -> None:
    records = [
        (str(target.path), repair_module.repair_record(_doc(target), target))
        for target in repair_module.TARGETS
    ]

    assert scorer_module.score_parsed(records) == []


def test_repair_adds_preparation_sterilization_flags_references_and_event_once(
    repair_module,
) -> None:
    target = repair_module.TARGET_BY_PATH[
        Path("bacterial/bordet_gengou_agar_medium.yaml")
    ]
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Suspend Bordet-Gengou Agar Base, glycerol, and Proteose "
                "Peptone in 840 ml DI Water."
            ),
        },
        {"step_number": 2, "action": "ADJUST_PH", "description": "Adjust to pH 6.7 +/- 0.2."},
        {"step_number": 3, "action": "AUTOCLAVE", "description": "Autoclave the base at 121 C."},
        {
            "step_number": 4,
            "action": "COOL",
            "description": (
                "Cool the base to 45-50 C and add 150 ml sterile "
                "defibrinated rabbit blood."
            ),
        },
    ]
    assert twice["sterilization"] == repair_module.STERILIZATION
    assert twice["references"] == [
        {"reference": reference} for reference in target.references
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
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


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[
        Path("bacterial/bordet_gengou_agar_medium.yaml")
    ]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M2309"

    with pytest.raises(ValueError, match="expected media term TOGO:M2307"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[
        Path("bacterial/bordet_gengou_broth_medium.yaml")
    ]
    doc = _doc(target)
    doc["ingredients"][-1]["concentration"]["value"] = "126"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_repair_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.record_id
        assert repair_module._source_term_id(doc) == target.media_term
        assert (
            repair_module._component_signature(doc["ingredients"], "ingredients"),
            repair_module._solution_signatures(doc.get("solutions")),
        ) in {
            (target.imported_ingredients, ()),
            (
                repair_module._final_ingredient_signature(target),
                repair_module._final_solution_signature(target),
            ),
        }
