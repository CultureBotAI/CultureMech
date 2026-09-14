from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_915_920_score15.py"
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
    return _load_script(SCRIPT, "repair_nbrc_915_920_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_nbrc_915_920")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [],
    }


def _doc(spec) -> dict:
    return {
        "id": spec.expected_id,
        "name": spec.target.stem,
        "original_name": "(Unnamed medium)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in spec.imported_ingredient_signature
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {spec.togo_id}",
            "term": {
                "id": spec.expected_media_term,
                "label": f"TOGO Medium {spec.togo_id}",
            },
        },
        "notes": f"Source: NBRC - NBRC_M{spec.nbrc_no}",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _composition in spec.imported_solution_signature
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_every_official_formula_and_exits_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    for spec in repair_module.SPECS:
        repaired = repair_module.repair_record(_doc(spec), spec)

        assert repaired["composition_type"] == "SEMI_DEFINED"
        assert repaired["ph_value"] == 7.0
        assert (
            repair_module._signature(
                repaired["ingredients"],
                "ingredients",
            )
            == spec.final_ingredient_signature
        )
        assert (
            repair_module._solution_signatures(
                repaired["solutions"],
                "solutions",
            )
            == spec.final_solution_signature
        )
        assert scorer_module.score_record(repaired) == (0, [])
        assert scorer_module.score_parsed([(str(spec.target), repaired)]) == []


def test_repair_nests_500_ug_ml_antibiotic_stocks(repair_module) -> None:
    spec = repair_module.SPECS[3]
    repaired = repair_module.repair_record(_doc(spec), spec)

    assert [solution["preferred_term"] for solution in repaired["solutions"]] == [
        "Kanamycin solution (500 ug/ml)",
        "Rifampicin solution (500 ug/ml)",
        "Spectinomycin solution (500 ug/ml)",
    ]
    for solution in repaired["solutions"]:
        components = _by_name(solution["composition"])
        assert solution["concentration"] == {"value": "100", "unit": "ML_PER_L"}
        assert len(components) == 1
        component = next(iter(components.values()))
        assert component["concentration"] == {
            "value": "0.5",
            "unit": "MG_PER_ML",
        }
        assert component["mediaingredientmech_chebi_term"]["id"].startswith("CHEBI:")
        assert solution["preparation_notes"] == "Sterilize separately by filtration."


def test_repair_keeps_bacto_tryptone_as_opaque_component(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.SPECS[0]),
        repair_module.SPECS[0],
    )
    ingredients = _by_name(repaired["ingredients"])

    assert "term" not in ingredients["Bacto Tryptone (Difco)"]
    assert "source-disclosed complex digest" in ingredients["Bacto Tryptone (Difco)"]["notes"]
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["CaCl2·2H2O"]["term"] == {
        "id": "CHEBI:86158",
        "label": "calcium chloride dihydrate",
    }
    assert ingredients["Agar (if needed)"]["physicochemical_roles"] == [
        "SOLIDIFYING_AGENT",
    ]


def test_repair_adds_source_stated_preparation_steps(repair_module) -> None:
    spec = repair_module.SPECS[0]
    repaired = repair_module.repair_record(_doc(spec), spec)

    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert repaired["preparation_steps"] == repair_module._preparation_steps(spec)


def test_repair_links_children_to_m1708_parent(repair_module) -> None:
    for spec in repair_module.CHILD_SPECS:
        repaired = repair_module.repair_record(_doc(spec), spec)

        assert repaired["parent_media"] == spec.parent_media
        assert repaired["variant_relationship"] == spec.relationship
        assert repaired["variant_modifications"] == [spec.variant_notes]


def test_repair_parent_replaces_stale_children_once(repair_module) -> None:
    parent = _doc(repair_module.SPECS[0])
    parent["variant_children"] = [
        {
            "path": "data/normalized_yaml/bacterial/togo_medium_m1710.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:008273",
            "name": "togo_medium_m1710",
        }
    ]

    once = repair_module.repair_parent(parent)
    twice = repair_module.repair_parent(once)

    assert twice["variant_children"] == [spec.variant_child for spec in repair_module.CHILD_SPECS]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    spec = repair_module.SPECS[0]
    once = repair_module.repair_record(_doc(spec), spec)
    twice = repair_module.repair_record(once, spec)

    assert twice["references"] == [{"reference": reference} for reference in spec.references]
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
    assert len(matching_events) == 1
    assert "500 ug/ml antibiotic stocks" in matching_events[0]["notes"]


def test_plan_repairs_targets_all_six_and_parent_links(repair_module) -> None:
    expected: dict[Path, dict] = {}
    for spec in repair_module.SPECS:
        path = repair_module.NORMALIZED / spec.target
        expected[path] = repair_module.repair_record(
            yaml.safe_load(path.read_text(encoding="utf-8")),
            spec,
        )
    parent_path = repair_module.NORMALIZED / repair_module.PARENT
    expected[parent_path] = repair_module.repair_parent(expected[parent_path])

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_id(repair_module) -> None:
    spec = repair_module.SPECS[0]
    doc = _doc(spec)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=spec.expected_id):
        repair_module.repair_record(doc, spec)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    spec = repair_module.SPECS[0]
    doc = _doc(spec)
    doc["media_term"]["term"]["id"] = "TOGO:M1710"

    with pytest.raises(ValueError, match=spec.expected_media_term):
        repair_module.repair_record(doc, spec)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    spec = repair_module.SPECS[0]
    doc = _doc(spec)
    doc["ingredients"][0] = _ingredient("Distilled water", "800", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, spec)


def test_repair_rejects_solution_drift(repair_module) -> None:
    spec = repair_module.SPECS[0]
    doc = _doc(spec)
    doc["solutions"][0] = _solution(
        repair_module.RIFAMPICIN.final_name,
        "100",
        "ML_PER_L",
    )

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, spec)


def test_current_records_match_repair_contract(repair_module) -> None:
    for spec in repair_module.SPECS:
        path = repair_module.NORMALIZED / spec.target
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == spec.expected_id
        assert repair_module._source_term_id(doc) == spec.expected_media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in {
            spec.imported_ingredient_signature,
            spec.final_ingredient_signature,
        }
        assert repair_module._solution_signatures(doc.get("solutions"), "solutions") in {
            spec.imported_solution_signature,
            spec.final_solution_signature,
        }
