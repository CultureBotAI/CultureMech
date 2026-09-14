from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m935_microaerophilic_thermus_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
PLACEHOLDER_INGREDIENTS = (("See source for composition", "variable", "VARIABLE"),)


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m935_microaerophilic_thermus_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_m935")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(signature) -> dict:
    name, value, unit, composition, solutions = signature
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [
            _ingredient(component_name, component_value, component_unit)
            for component_name, component_value, component_unit in composition
        ],
        "solutions": [_solution(row) for row in solutions],
    }


def _medium_doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "microaerophilic_thermus_medium",
        "original_name": "Microaerophilic Thermus Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_ingredients
        ],
        "solutions": [_solution(row) for row in target.imported_solutions],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": target.source_name},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition", "resolved_reference"],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _solution_doc(target) -> dict:
    return {
        "id": target.record_id,
        "preferred_term": "solution",
        "term": {"id": target.solution_term, "label": "solution"},
        "composition": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_composition
        ],
        "solutions": [_solution(row) for row in target.imported_solutions],
        "preparation_notes": "Original MediaDive step",
        "curation_history": [],
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in PLACEHOLDER_INGREDIENTS
        ],
        "data_quality_flags": ["incomplete_composition"],
        "category": "bacterial",
    }


def _repair_medium(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_medium_record(_medium_doc(target), target)


def _repair_solution(repair_module, path: Path) -> dict:
    target = next(
        target for target in repair_module.SOLUTION_TARGETS if target.path == path
    )
    return repair_module.repair_solution_record(_solution_doc(target), target)


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_j276_becomes_castenholz_parent(repair_module, scorer_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.J276_PATH)

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.CASTENHOLZ_MEDIUM_INGREDIENTS
    assert repair_module._solution_signature(
        repaired["solutions"],
        "solutions",
    ) == repair_module.FINAL_CASTENHOLZ_SOLUTION
    assert repaired["ph_value"] == 8.2
    assert repaired["variant_children"] == [
        repair_module.J894_CHILD,
        repair_module.M269_CHILD,
    ]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.J276_PATH), repaired)]) == []


def test_j894_is_ph_and_atmosphere_variant(repair_module, scorer_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.J894_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["parent_media"] == repair_module.J276_PARENT
    assert repaired["variant_relationship"] == "PH_VARIANT"
    assert repaired["variant_children"] == [repair_module.M935_CHILD]
    assert repaired["ph_value"] == 8.0
    assert repaired["incubation_atmosphere"] == "MICROAEROPHILIC"
    assert repaired["aeration"] == "N2-O2 (99:1, v/v) gas atmosphere"
    assert ingredients["Nitrogen gas"]["term"] == {
        "id": "CHEBI:17997",
        "label": "dinitrogen",
    }
    assert ingredients["Oxygen gas"]["term"] == {
        "id": "CHEBI:15379",
        "label": "dioxygen",
    }
    assert scorer_module.score_record(repaired) == (0, [])


def test_m935_corrects_togo_units_and_links_to_j894(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.M935_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["parent_media"] == repair_module.J894_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M935_CHILD["notes"]]
    assert "variant_children" not in repaired
    assert "kg_microbe_match" not in repaired
    assert "NaOH" not in ingredients
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "900.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Yeast extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Tryptone (BD-Difco)"]["term"] == {
        "id": "MICRO:0000182",
        "label": "tryptone",
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.M935_PATH), repaired)]) == []


def test_castenholz_solution_expands_fecl3_and_nitsch_stocks(repair_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.M935_PATH)
    castenholz = repaired["solutions"][0]
    castenholz_components = _by_name(castenholz["composition"])
    castenholz_solutions = _by_name(castenholz["solutions"])
    nitsch = _by_name(castenholz_solutions["Nitsch's trace elements"]["composition"])
    fecl3 = _by_name(
        castenholz_solutions["FeCl3 x 6 H2O solution (0.03%)"]["composition"]
    )

    assert castenholz["term"] == {
        "id": "mediadive.solution:3963",
        "label": "Castenholz basal salt solution",
    }
    assert castenholz["culturemech_term"] == {
        "id": "CultureMech:013022",
        "label": "Castenholz basal salt solution",
    }
    assert castenholz_components["NaNO3"]["concentration"] == {
        "value": "6.89",
        "unit": "G_PER_L",
    }
    assert castenholz_components["Na2HPO4"]["physicochemical_roles"] == ["BUFFER"]
    assert fecl3["FeCl3 x 6 H2O"]["concentration"] == {
        "value": "0.03",
        "unit": "PERCENT_W_V",
    }
    assert nitsch["CoCl2 x 6 H2O"]["term"] == {
        "id": "CHEBI:53503",
        "label": "cobalt chloride hexahydrate",
    }
    assert nitsch["H2SO4"]["concentration"] == {
        "value": "0.5",
        "unit": "ML_PER_L",
    }


def test_solution_helpers_correct_false_percent_rows(repair_module) -> None:
    castenholz = _repair_solution(repair_module, repair_module.CASTENHOLZ_3963_PATH)
    nitsch = _repair_solution(repair_module, repair_module.NITSCH_3964_PATH)

    assert "ingredients" not in castenholz
    assert "ingredients" not in nitsch
    assert repair_module._signature(
        castenholz["composition"],
        "composition",
    ) == repair_module.CASTENHOLZ_COMPOSITION
    assert repair_module._solution_signature(
        castenholz["solutions"],
        "solutions",
    ) == repair_module.CASTENHOLZ_SOLUTIONS
    assert repair_module._signature(
        nitsch["composition"],
        "composition",
    ) == repair_module.NITSCH_COMPOSITION
    assert _by_name(castenholz["composition"])["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert _by_name(nitsch["composition"])["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.M935_PATH
    )
    once = repair_module.repair_medium_record(_medium_doc(target), target)
    twice = repair_module.repair_medium_record(once, target)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in target.references
    ]
    assert once["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert "NaOH" in matching_events[0]["notes"]


def test_nested_solution_components_are_scored_recursively(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.M935_PATH)
    components = scorer_module.composition_components(repaired)

    assert "Nitsch's trace elements" not in _by_name(components)
    assert "CoCl2 x 6 H2O" in _by_name(components)
    assert "FeCl3 x 6 H2O" in _by_name(components)


def test_repair_rejects_wrong_medium_id(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.M935_PATH
    )
    doc = _medium_doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_medium_solution_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.M935_PATH
    )
    doc = _medium_doc(target)
    doc["solutions"][0]["preferred_term"] = "wrong"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = next(
        target
        for target in repair_module.SOLUTION_TARGETS
        if target.path == repair_module.CASTENHOLZ_3963_PATH
    )
    doc = _solution_doc(target)
    doc["composition"].pop()

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_solution_record(doc, target)
