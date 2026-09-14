from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_pygsw_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_pygsw_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_pygsw")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _target(repair_module, path: Path):
    return next(target for target in repair_module.TARGETS if target.path == path)


def _doc(repair_module, path: Path) -> dict:
    target = _target(repair_module, path)
    return {
        "id": target.record_id,
        "name": target.path.stem,
        "original_name": "PYGSW Agar",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _component(name, value, unit) for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": "TOGO Medium",
            "term": {"id": target.media_term_id, "label": "PYGSW Agar"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": repair_module.FALSE_KG_MATCH,
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _repair(repair_module, path: Path) -> dict:
    target = _target(repair_module, path)
    return repair_module.repair_record(_doc(repair_module, path), target)


@pytest.mark.parametrize(
    "path_attr",
    [
        pytest.param("MODIFIED_PATH", id="modified-pygsw"),
        pytest.param("PYGSW_PATH", id="pygsw"),
    ],
)
def test_repair_restores_source_specific_ingredient_signatures(
    repair_module,
    path_attr: str,
) -> None:
    target_path = getattr(repair_module, path_attr)
    target = _target(repair_module, target_path)
    repaired = _repair(repair_module, target_path)

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients") == target.final_signature
    )
    assert _by_name(repaired["ingredients"])[target.final_signature[1][0]]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }


def test_repair_grounds_defined_ingredients_and_keeps_seawater_opaque(
    repair_module,
) -> None:
    modified = _repair(repair_module, repair_module.MODIFIED_PATH)
    pygsw = _repair(repair_module, repair_module.PYGSW_PATH)

    for repaired, seawater in (
        (modified, repair_module.SEAWATER),
        (pygsw, repair_module.SEAWATER_2_PERCENT),
    ):
        ingredients = _by_name(repaired["ingredients"])
        assert ingredients[repair_module.YEAST_EXTRACT]["term"] == {
            "id": "FOODON:03315426",
            "label": "yeast extract",
        }
        assert "mediaingredientmech_chebi_term" not in ingredients[repair_module.YEAST_EXTRACT]
        assert ingredients[repair_module.PEPTONE]["term"] == {
            "id": "MICRO:0000178",
            "label": "Peptone",
        }
        assert "mediaingredientmech_chebi_term" not in ingredients[repair_module.PEPTONE]
        assert ingredients[repair_module.GLUCOSE]["mediaingredientmech_chebi_term"] == {
            "id": "CHEBI:17234",
            "label": "glucose",
        }
        assert ingredients[repair_module.AGAR]["mediaingredientmech_chebi_term"] == {
            "id": "CHEBI:2509",
            "label": "agar",
        }
        assert "term" not in ingredients[seawater]
        assert "mediaingredientmech_chebi_term" not in ingredients[seawater]


@pytest.mark.parametrize(
    "path_attr",
    [
        pytest.param("MODIFIED_PATH", id="modified-pygsw"),
        pytest.param("PYGSW_PATH", id="pygsw"),
    ],
)
def test_repair_adds_references_removes_false_match_and_scores_below_threshold(
    repair_module,
    scorer_module,
    path_attr: str,
) -> None:
    target_path = getattr(repair_module, path_attr)
    target = _target(repair_module, target_path)
    repaired = _repair(repair_module, target_path)

    assert "kg_microbe_match" not in repaired
    assert "ph_value" not in repaired
    assert "temperature_value" not in repaired
    assert "preparation_steps" not in repaired
    assert "sterilization" not in repaired
    assert repaired["references"] == [
        {"reference": target.togo_url},
        {"reference": target.nbrc_url},
    ]
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(target_path), repaired)]) == []


@pytest.mark.parametrize(
    "path_attr",
    [
        pytest.param("MODIFIED_PATH", id="modified-pygsw"),
        pytest.param("PYGSW_PATH", id="pygsw"),
    ],
)
def test_repair_is_idempotent(repair_module, path_attr: str) -> None:
    target_path = getattr(repair_module, path_attr)
    target = _target(repair_module, target_path)
    repaired = _repair(repair_module, target_path)

    assert repair_module.repair_record(repaired, target) == repaired
