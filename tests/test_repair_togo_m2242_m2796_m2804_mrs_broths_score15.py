from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2242_m2796_m2804_mrs_broths_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2242_m2796_m2804_mrs_broths")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_mrs_broths")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _target(repair_module, path: Path):
    return next(target for target in repair_module.TARGETS if target.path == path)


def _doc(repair_module, path: Path) -> dict:
    target = _target(repair_module, path)
    return {
        "id": target.record_id,
        "name": path.stem,
        "original_name": "MRS broth",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {target.media_term_id}",
            "term": {"id": target.media_term_id, "label": "MRS broth"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _repair(repair_module, path: Path) -> dict:
    target = _target(repair_module, path)
    return repair_module.repair_record(_doc(repair_module, path), target)


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


@pytest.mark.parametrize(
    "path_name",
    [
        pytest.param("CRITERION_PATH", id="criterion-m2796"),
        pytest.param("OXOID_PATH", id="oxoid-m2242"),
        pytest.param("CYSTEINE_OXOID_PATH", id="cysteine-oxoid-m2804"),
    ],
)
def test_repairs_fix_units_and_clear_review_score(
    repair_module,
    scorer_module,
    path_name: str,
) -> None:
    path = getattr(repair_module, path_name)
    target = _target(repair_module, path)
    repaired = _repair(repair_module, path)

    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == target.final_signature
    assert repaired["ph_range"] == {
        "min": target.ph_range[0],
        "max": target.ph_range[1],
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(path), repaired)]) == []


def test_criterion_m2796_keeps_mrs_product_opaque(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.CRITERION_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients[repair_module.WATER]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients[repair_module.L_CYSTEINE_SIGMA]["term"] == {
        "id": "CHEBI:17561",
        "label": "L-cysteine",
    }
    assert "term" not in ingredients[repair_module.MRS_BROTH_CRITERION]


def test_oxoid_m2242_fixes_sorbitan_unit_and_groundings(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.OXOID_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients[repair_module.SORBITAN]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert "term" not in ingredients[repair_module.SORBITAN]
    assert ingredients[repair_module.MGSO4]["term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert ingredients[repair_module.MNSO4]["term"] == {
        "id": "CHEBI:86358",
        "label": "manganese(II) sulfate tetrahydrate",
    }


def test_m2804_removes_double_counted_mrs_wrapper(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.CYSTEINE_OXOID_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module.MRS_BROTH_OXOID not in ingredients
    assert ingredients[repair_module.CYSTEINE]["concentration"] == {
        "value": "0.05",
        "unit": "PERCENT_W_V",
    }
    assert ingredients[repair_module.CYSTEINE]["term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }


def test_m2242_and_m2804_are_linked_as_variants(repair_module) -> None:
    m2242 = _repair(repair_module, repair_module.OXOID_PATH)
    m2804 = _repair(repair_module, repair_module.CYSTEINE_OXOID_PATH)

    assert m2242["variant_children"] == [repair_module.M2804_CHILD]
    assert "parent_media" not in m2242

    assert m2804["parent_media"] == repair_module.M2242_PARENT
    assert m2804["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert m2804["variant_modifications"] == [
        "Add 0.05% w/v cysteine hydrochloride."
    ]
    assert "variant_children" not in m2804


@pytest.mark.parametrize(
    "path_name",
    [
        pytest.param("CRITERION_PATH", id="criterion-m2796"),
        pytest.param("OXOID_PATH", id="oxoid-m2242"),
        pytest.param("CYSTEINE_OXOID_PATH", id="cysteine-oxoid-m2804"),
    ],
)
def test_repair_is_idempotent(repair_module, path_name: str) -> None:
    path = getattr(repair_module, path_name)
    target = _target(repair_module, path)
    once = repair_module.repair_record(_doc(repair_module, path), target)

    assert repair_module.repair_record(once, target) == once


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.OXOID_PATH)
    doc["ingredients"][0]["preferred_term"] = "Tap water"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(
            doc,
            _target(repair_module, repair_module.OXOID_PATH),
        )
