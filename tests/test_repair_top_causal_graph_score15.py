from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_top_causal_graph_score15.py"
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
    return _load_script(SCRIPT, "repair_top_causal_graph_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_top_causal_graph")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    doc = {
        "id": target.record_id,
        "name": target.path.stem,
        "original_name": target.path.stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": target.physical_state,
        "media_term": {
            "preferred_term": target.media_term_id,
            "term": {"id": target.media_term_id, "label": target.media_term_id},
        },
        "notes": "Source",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in target.imported_ingredients
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
            "resolved_reference",
        ],
    }
    if target.imported_solutions:
        doc["solutions"] = [
            {**_component(name, value, unit), "composition": []}
            for name, value, unit in target.imported_solutions
        ]
    if target.path == Path("bacterial/my20_agar.yaml"):
        doc["parent_media"] = {
            "path": "data/normalized_yaml/bacterial/ym_agar.yaml",
            "relationship": "CONCENTRATION_VARIANT",
            "id": "CultureMech:002617",
            "name": "ym_agar",
            "notes": (
                "Reviewed MY20 as a YM Agar concentration variant with glucose "
                "as the curated concentration axis."
            ),
        }
        doc["variant_relationship"] = "CONCENTRATION_VARIANT"
        doc["variant_modifications"] = [
            (
                "Reviewed YM Agar/MY20 Agar pair; child keeps peptone, "
                "yeast extract, malt extract, and agar unchanged but "
                "increases glucose from 10 g/L to 200 g/L."
            )
        ]
    return doc


def _target(repair_module, path: str):
    return repair_module.TARGET_BY_PATH[Path(path)]


def _repair(repair_module, path: str) -> dict:
    target = _target(repair_module, path)
    return repair_module.repair_record(_doc(target), target)


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_all_targets_leave_review_ranking(repair_module, scorer_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)

        assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


def test_my20_adds_distilled_water_and_keeps_ym_parent(repair_module) -> None:
    repaired = _repair(repair_module, "bacterial/my20_agar.yaml")
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module._composition_signature(_target(
        repair_module,
        "bacterial/my20_agar.yaml",
    ).final_ingredients)
    assert ingredients["Peptone"]["term"] == {"id": "MICRO:0000178", "label": "Peptone"}
    assert ingredients["Malt extract"]["term"] == {
        "id": "FOODON:03301056",
        "label": "malt extract",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }

    assert repaired["parent_media"]["path"] == "data/normalized_yaml/bacterial/ym_agar.yaml"
    assert repaired["variant_relationship"] == "CONCENTRATION_VARIANT"
    assert repaired["sterilization"] == repair_module.JCM_STERILIZATION


def test_my75s_splits_seawater_and_deionised_water(repair_module) -> None:
    repaired = _repair(repair_module, "bacterial/my75s.yaml")
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Natural filtered seawater"]["concentration"] == {
        "value": "750.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Natural filtered seawater"]["term"] == {
        "id": "ENVO:00002149",
        "label": "sea water",
    }
    assert ingredients["Deionised water"]["concentration"] == {
        "value": "250.0",
        "unit": "ML_PER_L",
    }
    assert "kg_microbe_match" not in repaired


def test_m2227_rebuilds_heat_sensitive_solutions(repair_module) -> None:
    repaired = _repair(
        repair_module,
        "bacterial/mycoplasma_medium_atcc_243_with_sucrose.yaml",
    )
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert ingredients["Distilled deionized water"]["concentration"] == {
        "value": "450.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Horse serum"]["concentration"] == {
        "value": "200.0",
        "unit": "ML_PER_L",
    }
    assert solutions["Yeast extract solution (15%)"]["concentration"] == {
        "value": "150.0",
        "unit": "ML_PER_L",
    }
    assert solutions["Yeast extract solution (15%)"]["composition"] == [
        {
            "preferred_term": "Yeast extract",
            "concentration": {"value": "15.0", "unit": "PERCENT_W_V"},
            "source": "TOGO M2227 / ATCC Medium 1161",
            "notes": (
                "ATCC Medium 1161 specifies the yeast extract solution as "
                "15.0% w/v."
            ),
            "term": {"id": "FOODON:03315426", "label": "yeast extract"},
            "nutritional_roles": ["PROTEIN_SOURCE", "VITAMIN_SOURCE"],
        }
    ]
    assert solutions["Sucrose solution"]["composition"][0]["concentration"] == {
        "value": "200.0",
        "unit": "G_PER_L",
    }
    assert repaired["ph_range"] == {"min": 7.2, "max": 7.6}
    assert "kg_microbe_match" not in repaired


def test_m1575_restores_one_liter_water_and_ph(repair_module) -> None:
    repaired = _repair(repair_module, "bacterial/na_0_5_yeast_extract.yaml")
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Pepton"]["term"] == {"id": "MICRO:0000178", "label": "Peptone"}
    assert ingredients["Beef extract"]["term"] == {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert repaired["ph_value"] == 7.0


def test_repair_adds_references_flags_and_history_once(repair_module) -> None:
    target = _target(
        repair_module,
        "bacterial/mycoplasma_medium_atcc_243_with_sucrose.yaml",
    )
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in target.references
    ]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]

    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert repair_module.ATCC_1161 in matching_events[0]["source"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = _target(repair_module, "bacterial/my75s.yaml")
    doc = _doc(target)
    doc["ingredients"][0]["concentration"]["value"] = "751"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = _target(
        repair_module,
        "bacterial/mycoplasma_medium_atcc_243_with_sucrose.yaml",
    )
    doc = _doc(target)
    doc["solutions"].append(_component("Horse serum", "200", "G_PER_L"))

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)
