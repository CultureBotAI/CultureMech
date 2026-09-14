from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_351_score15.py"
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
    return _load_script(SCRIPT, "repair_nbrc_351_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_nbrc_351")


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
        "name": "togo_medium_m1552",
        "original_name": "(Unnamed medium)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in repair_module.LEGACY_INGREDIENTS
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1552",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "TOGO Medium M1552",
            },
        },
        "notes": "Source: NBRC - NBRC_M351",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _composition in repair_module.LEGACY_SOLUTIONS
        ],
        "parent_media": {
            "path": "data/normalized_yaml/bacterial/TOGO_M1553_Methylobacterium_Medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": repair_module.EXPECTED_PARENT_ID,
            "name": "methylobacterium_medium",
        },
        "variant_relationship": "SOURCE_DUPLICATE",
        "variant_modifications": [
            "Same ingredient and concentration signature; review as possible duplicate source record.",
        ],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "methylobacterium_medium",
        "original_name": "Methylobacterium Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "SEMI_DEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "TOGO Medium M1553",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "Methylobacterium Medium",
            },
        },
        "ingredients": [],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "variant_children": [
            {
                "path": "data/normalized_yaml/bacterial/togo_medium_m1552.yaml",
                "relationship": "SOURCE_DUPLICATE",
                "id": repair_module.EXPECTED_ID,
                "name": "togo_medium_m1552",
            },
            {
                "path": "data/normalized_yaml/bacterial/togo_medium_m1603.yaml",
                "relationship": "SOURCE_DUPLICATE",
                "id": "CultureMech:008156",
                "name": "togo_medium_m1603",
            },
            {
                "path": "data/normalized_yaml/bacterial/togo_medium_m1529.yaml",
                "relationship": "SUBSTITUTED_COMPONENT_VARIANT",
                "id": "CultureMech:008075",
                "name": "togo_medium_m1529",
            },
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_formula_and_exits_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ph_value"] == 7.0
    assert "solutions" not in repaired
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENTS
    )
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_corrects_n_acetylglucosamine_to_mg_per_l_and_grounds_formula(
    repair_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["N-Acetyl glucosamine**"]["concentration"] == {
        "value": "30",
        "unit": "MG_PER_L",
    }
    assert ingredients["N-Acetyl glucosamine**"]["term"] == {
        "id": "CHEBI:59640",
        "label": "N-Acetylglucosamine",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Agar (if needed)"]["physicochemical_roles"] == [
        "SOLIDIFYING_AGENT",
    ]


def test_repair_keeps_hipolypepton_as_sourced_opaque_component(
    repair_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredient = _by_name(repaired["ingredients"])["Hipolypepton*"]

    assert "term" not in ingredient
    assert "Wako Pure Chemical Industries" in ingredient["notes"]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_source_stated_filtration_and_ph_step(
    repair_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)


def test_repair_relinks_target_as_substituted_component_variant(
    repair_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["parent_media"] == repair_module.PARENT_MEDIA
    assert repaired["variant_relationship"] == "SUBSTITUTED_COMPONENT_VARIANT"
    assert repaired["variant_modifications"] == list(repair_module.VARIANT_MODIFICATIONS)


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

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
    assert "30 g/L to 30 mg/L" in matching_events[0]["notes"]


def test_repair_parent_updates_only_togo_child_once(repair_module) -> None:
    once = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(once)

    assert twice["variant_children"] == [
        repair_module.TOGO_CHILD,
        {
            "path": "data/normalized_yaml/bacterial/togo_medium_m1603.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:008156",
            "name": "togo_medium_m1603",
        },
        {
            "path": "data/normalized_yaml/bacterial/togo_medium_m1529.yaml",
            "relationship": "SUBSTITUTED_COMPONENT_VARIANT",
            "id": "CultureMech:008075",
            "name": "togo_medium_m1529",
        },
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert len(matching_events) == 1


def test_plan_repairs_target_and_parent_records(repair_module) -> None:
    target_path = repair_module.NORMALIZED / repair_module.TARGET
    parent_path = repair_module.NORMALIZED / repair_module.PARENT
    expected_target = repair_module.repair_target(
        yaml.safe_load(target_path.read_text(encoding="utf-8"))
    )
    expected_parent = repair_module.repair_parent(
        yaml.safe_load(parent_path.read_text(encoding="utf-8"))
    )

    assert repair_module.plan_repairs() == {
        target_path: expected_target,
        parent_path: expected_parent,
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1553"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Distilled water", "1.0", "L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0] = _solution("N-Acetyl glucosamine", "30", "MG_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_target(doc)


def test_target_record_matches_repair_contract(repair_module) -> None:
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
