from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m943_microaerophilic_autotrophs_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m943_microaerophilic_autotrophs_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m943")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(signature) -> dict:
    name, value, unit, composition = signature
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [
            _component(component_name, component_value, component_unit)
            for component_name, component_value, component_unit in composition
        ],
    }


def _medium_doc(repair_module, *, togo: bool) -> dict:
    imported_ingredients = (
        repair_module.TOGO_IMPORTED_INGREDIENTS
        if togo
        else repair_module.MEDIADIVE_FLATTENED_INGREDIENTS
    )
    return {
        "id": "CultureMech:010366" if togo else "CultureMech:003251",
        "name": "mj_medium_for_microaerophilic_autotrophs",
        "original_name": "MJ Medium For Microaerophilic Autotrophs",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component(name, value, unit) for name, value, unit in imported_ingredients
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {
                "id": "TOGO:M943" if togo else "mediadive.medium:J902",
                "label": "MJ Medium",
            },
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(signature)
            for signature in (repair_module.TOGO_IMPORTED_SOLUTIONS if togo else ())
        ],
        "data_quality_flags": ["incomplete_composition"],
        "kg_microbe_match": "mediadive.medium:J780",
    }


def _helper_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:013830",
        "preferred_term": "Main sol. J902",
        "term": {"id": "mediadive.solution:4901", "label": "Main sol. J902"},
        "composition": [
            _component(name, value, unit)
            for name, value, unit in repair_module.MEDIADIVE_HELPER_IMPORTED_COMPOSITION
        ],
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.PLACEHOLDER_INGREDIENTS
        ],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
        "category": "bacterial",
    }


def _mj_basal_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:002716",
        "name": "mj_basal_medium",
        "curation_history": [],
        "variant_children": [
            {
                "path": "data/normalized_yaml/bacterial/mj_n_basal_medium.yaml",
                "relationship": "SOURCE_DUPLICATE",
                "id": "CultureMech:002733",
                "name": "mj_n_basal_medium",
                "notes": "Same ingredient and concentration signature.",
            },
            repair_module.MJ_MEDIUM_CHILD,
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_togo_m943_expands_cross_referenced_stocks(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_togo_m943(_medium_doc(repair_module, togo=True))
    solutions = _by_name(repaired["solutions"])

    assert repaired["ph_value"] == 5.5
    assert repaired["incubation_atmosphere"] == "MICROAEROPHILIC"
    assert repaired["aeration"] == "N2-CO2-O2 (76:19:5, v/v) gas atmosphere, 50 kPa"
    assert repair_module._solution_signatures(repaired) == repair_module.FINAL_SOLUTIONS
    assert _by_name(solutions["MJ(-N) synthetic seawater"]["composition"])["Na2SeO3 x 5 H2O"][
        "concentration"
    ] == {"value": "0.5", "unit": "MG_PER_L"}
    assert solutions["8% NaHCO3 solution"]["composition"][0]["concentration"] == {
        "value": "8.0",
        "unit": "PERCENT_W_V",
    }
    assert solutions["8% NaHCO3 solution"]["term"] == {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate",
    }
    assert solutions["8% NaHCO3 solution"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate",
    }
    assert solutions["10% Na2S2O3 x 5 H2O solution"]["term"] == {
        "id": "CHEBI:32150",
        "label": "sodium thiosulfate pentahydrate",
    }
    assert solutions["10% Na2S2O3 x 5 H2O solution"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32150",
        "label": "sodium thiosulfate pentahydrate",
    }
    assert solutions["10% Na2S2O3 x 5 H2O solution"]["composition"][0] == {
        "preferred_term": "Na2S2O3 x 5 H2O",
        "concentration": {"value": "10.0", "unit": "PERCENT_W_V"},
        "source": repair_module.SOURCE_TOGO,
        "notes": (
            "TOGO M943 / JCM Medium 902 specifies the added Na2S2O3 x 5 H2O " "solution as 10% w/v."
        ),
        "term": {
            "id": "CHEBI:32150",
            "label": "sodium thiosulfate pentahydrate",
        },
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:32150",
            "label": "sodium thiosulfate pentahydrate",
        },
        "nutritional_roles": ["SULFUR_SOURCE"],
    }
    assert "Trace minerals" in _by_name(solutions["MJ(-N) synthetic seawater"]["composition"])
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TOGO_M943_PATH), repaired)]) == []


def test_mediadive_j902_becomes_source_duplicate_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_mediadive_parent(_medium_doc(repair_module, togo=False))

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENTS
    )
    assert repaired["variant_children"] == [repair_module.M943_CHILD]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m943_links_to_mediadive_j902_and_drops_stale_match(
    repair_module,
) -> None:
    repaired = repair_module.repair_togo_m943(_medium_doc(repair_module, togo=True))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["parent_media"] == repair_module.J902_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M943_CHILD["notes"]]
    assert "variant_children" not in repaired
    assert "kg_microbe_match" not in repaired
    assert ingredients["Oxygen gas"]["term"] == {
        "id": "CHEBI:15379",
        "label": "dioxygen",
    }


def test_mediadive_4901_helper_replaces_flattened_placeholder(
    repair_module,
) -> None:
    repaired = repair_module.repair_main_helper(_helper_doc(repair_module))

    assert repaired["composition"] == [
        {
            "preferred_term": "NH4Cl",
            "concentration": {"value": "0.25", "unit": "G_PER_L"},
            "source": repair_module.SOURCE_MEDIADIVE,
            "notes": "MediaDive J902 / JCM Medium 902 lists 0.25 g/L NH4Cl.",
            "term": {"id": "CHEBI:31206", "label": "ammonium chloride"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:31206",
                "label": "ammonium chloride",
            },
            "nutritional_roles": ["NITROGEN_SOURCE"],
        }
    ]
    assert repair_module._solution_signatures(repaired) == repair_module.FINAL_SOLUTIONS
    assert "ingredients" not in repaired


def test_mj_basal_drops_stale_concentration_variant_child(
    repair_module,
) -> None:
    repaired = repair_module.repair_mj_basal(_mj_basal_doc(repair_module))

    assert repaired["variant_children"] == [
        {
            "path": "data/normalized_yaml/bacterial/mj_n_basal_medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:002733",
            "name": "mj_n_basal_medium",
            "notes": "Same ingredient and concentration signature.",
        }
    ]


def test_repairs_are_idempotent_and_append_events_once(repair_module) -> None:
    records = (
        (
            repair_module.repair_mediadive_parent,
            _medium_doc(repair_module, togo=False),
            "RESOLVED_MEDIADIVE_J902_MICROAEROPHILIC_AUTOTROPHS",
        ),
        (
            repair_module.repair_togo_m943,
            _medium_doc(repair_module, togo=True),
            "RESOLVED_TOGO_M943_MICROAEROPHILIC_AUTOTROPHS",
        ),
        (
            repair_module.repair_main_helper,
            _helper_doc(repair_module),
            "RESOLVED_MEDIADIVE_4901_MAIN_SOL_J902",
        ),
        (
            repair_module.repair_mj_basal,
            _mj_basal_doc(repair_module),
            "REMOVED_STALE_J902_VARIANT_EDGE",
        ),
    )

    for function, doc, action in records:
        once = function(doc)
        twice = function(once)
        assert twice == once
        matching_events = [
            event
            for event in twice["curation_history"]
            if event.get("curator") == repair_module.CURATOR and event.get("action") == action
        ]
        assert len(matching_events) == 1


def test_repair_rejects_wrong_m943_id(repair_module) -> None:
    doc = _medium_doc(repair_module, togo=True)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="CultureMech:010366"):
        repair_module.repair_togo_m943(doc)


def test_repair_rejects_togo_solution_drift(repair_module) -> None:
    doc = _medium_doc(repair_module, togo=True)
    doc["solutions"][0]["preferred_term"] = "MJ synthetic seawater"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_togo_m943(doc)


def test_repair_rejects_mediadive_helper_placeholder_drift(repair_module) -> None:
    doc = _helper_doc(repair_module)
    doc["ingredients"][0]["preferred_term"] = "Unknown"

    with pytest.raises(ValueError, match="placeholder signature drifted"):
        repair_module.repair_main_helper(doc)
