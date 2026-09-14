from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_j1145_togo_m1227_roseospira_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_j1145_togo_m1227_roseospira_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_roseospira")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _target(repair_module, path: Path):
    return next(target for target in repair_module.TARGETS if target.path == path)


def _doc(repair_module, path: Path) -> dict:
    target = _target(repair_module, path)
    return {
        "id": target.record_id,
        "name": "modified_roseospira_medium",
        "original_name": "Modified Roseospira Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component(name, value, unit) for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": "Modified Roseospira Medium",
            "term": {
                "id": target.media_term_id,
                "label": "Modified Roseospira Medium",
            },
        },
        "notes": "Source: JCM",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _component(name, value, unit) for name, value, unit in target.imported_solutions
        ],
        "data_quality_flags": [
            "incomplete_composition",
            "source_information_unavailable",
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _repair(repair_module, path: Path) -> dict:
    target = _target(repair_module, path)
    return repair_module.repair_record(_doc(repair_module, path), target)


@pytest.mark.parametrize(
    "path_attr",
    [
        pytest.param("JCM_PATH", id="jcm-j1145"),
        pytest.param("TOGO_PATH", id="togo-m1227"),
    ],
)
def test_repair_restores_modified_roseospira_formula(
    repair_module,
    scorer_module,
    path_attr: str,
) -> None:
    target_path = getattr(repair_module, path_attr)
    repaired = _repair(repair_module, target_path)

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENTS
    )
    assert (
        repair_module._signature(repaired["solutions"], "solutions")
        == repair_module.FINAL_SOLUTIONS
    )
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target_path), repaired)]) == []


def test_repair_removes_base_thiosulfate_and_keeps_final_sulfide(
    repair_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module.NA2S2O3 not in ingredients
    assert ingredients[repair_module.NA2S]["concentration"] == {
        "value": "1.0",
        "unit": "MILLIMOLAR",
    }
    assert "instead of" in ingredients[repair_module.NA2S]["notes"]


def test_repair_grounds_defined_salts_and_keeps_stocks_opaque(
    repair_module,
) -> None:
    repaired = _repair(repair_module, repair_module.JCM_PATH)
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert ingredients[repair_module.MGSO4]["term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert ingredients[repair_module.CACL2]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:86158",
        "label": "calcium chloride dihydrate",
    }
    assert ingredients[repair_module.YEAST_EXTRACT]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients[repair_module.YEAST_EXTRACT]

    for name in (
        repair_module.FERRIC_CITRATE,
        repair_module.VITAMIN_B12,
        repair_module.MICRONUTRIENT,
    ):
        assert "term" not in solutions[name]
        assert "mediaingredientmech_chebi_term" not in solutions[name]


def test_repair_adds_source_duplicate_links(repair_module) -> None:
    jcm = _repair(repair_module, repair_module.JCM_PATH)
    togo = _repair(repair_module, repair_module.TOGO_PATH)

    assert jcm["parent_media"] == repair_module.TOGO_PARENT
    assert jcm["variant_relationship"] == "SOURCE_DUPLICATE"
    assert jcm["variant_modifications"] == [repair_module.SOURCE_DUPLICATE_NOTE]
    assert "variant_children" not in jcm

    assert togo["variant_children"] == [repair_module.JCM_CHILD]
    assert "parent_media" not in togo


@pytest.mark.parametrize(
    "path_attr",
    [
        pytest.param("JCM_PATH", id="jcm-j1145"),
        pytest.param("TOGO_PATH", id="togo-m1227"),
    ],
)
def test_repair_adds_references_ph_and_curation_event(
    repair_module,
    path_attr: str,
) -> None:
    target_path = getattr(repair_module, path_attr)
    target = _target(repair_module, target_path)
    repaired = _repair(repair_module, target_path)

    assert repaired["ph_value"] == 6.8
    assert "temperature_value" not in repaired
    assert "sterilization" not in repaired
    assert repaired["preparation_steps"] == repair_module.PREPARATION_STEPS
    assert repaired["references"] == [{"reference": reference} for reference in target.references]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


@pytest.mark.parametrize(
    "path_attr",
    [
        pytest.param("JCM_PATH", id="jcm-j1145"),
        pytest.param("TOGO_PATH", id="togo-m1227"),
    ],
)
def test_repair_is_idempotent(repair_module, path_attr: str) -> None:
    target_path = getattr(repair_module, path_attr)
    target = _target(repair_module, target_path)
    repaired = _repair(repair_module, target_path)

    assert repair_module.repair_record(repaired, target) == repaired
