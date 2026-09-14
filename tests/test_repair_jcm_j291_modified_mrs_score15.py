from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_j291_modified_mrs_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_j291_modified_mrs_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_j291")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _target(repair_module, path: Path):
    return next(target for target in repair_module.TARGETS if target.path == path)


def _doc(repair_module, path: Path) -> dict:
    target = _target(repair_module, path)
    return {
        "id": target.record_id,
        "name": "modified_mrs_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.5,
        "ingredients": [
            _component(name, value, unit) for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": "JCM Medium J291",
            "term": {
                "id": target.media_term_id,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: JCM",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _repair(repair_module, path: Path) -> dict:
    target = _target(repair_module, path)
    return repair_module.repair_record(_doc(repair_module, path), target)


@pytest.mark.parametrize(
    "path",
    [
        pytest.param(
            "JCM_J291_PATH",
            id="mediadive-j291",
        ),
        pytest.param(
            "TOGO_M285_PATH",
            id="togo-m285",
        ),
    ],
)
def test_repair_restores_water_and_scores_cleanly(
    repair_module,
    scorer_module,
    path: str,
) -> None:
    repaired = _repair(repair_module, getattr(repair_module, path))
    ingredients = _by_name(repaired["ingredients"])

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients[repair_module.WATER]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(getattr(repair_module, path)), repaired)]) == []


def test_repair_keeps_commercial_mrs_broth_opaque(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.JCM_J291_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert "term" not in ingredients[repair_module.MRS_BROTH]
    assert ingredients[repair_module.CYSTEINE]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    assert ingredients[repair_module.WATER]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }


def test_repair_adds_jcm_autoclave_evidence(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.JCM_J291_PATH)

    assert repaired["preparation_steps"] == repair_module.PREPARATION_STEPS
    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert repaired["references"] == [{"reference": repair_module.JCM_291}]


def test_repair_links_source_duplicates(repair_module) -> None:
    j291 = _repair(repair_module, repair_module.JCM_J291_PATH)
    m285 = _repair(repair_module, repair_module.TOGO_M285_PATH)

    assert j291["parent_media"] == repair_module.TOGO_M285_PARENT
    assert j291["variant_relationship"] == "SOURCE_DUPLICATE"
    assert j291["variant_modifications"] == [repair_module.TOGO_M285_PARENT["notes"]]
    assert "variant_children" not in j291

    assert m285["variant_children"] == [repair_module.JCM_J291_CHILD]
    assert "parent_media" not in m285


def test_togo_m285_gets_togo_and_jcm_references(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M285_PATH)

    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M285},
        {"reference": repair_module.JCM_291},
    ]


@pytest.mark.parametrize(
    "path",
    [
        pytest.param("JCM_J291_PATH", id="mediadive-j291"),
        pytest.param("TOGO_M285_PATH", id="togo-m285"),
    ],
)
def test_repair_is_idempotent(repair_module, path: str) -> None:
    target_path = getattr(repair_module, path)
    repaired = _repair(repair_module, target_path)

    assert repair_module.repair_record(repaired, _target(repair_module, target_path)) == repaired
