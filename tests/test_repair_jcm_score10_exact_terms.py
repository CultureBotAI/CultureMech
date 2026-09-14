from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_score10_exact_terms.py"
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
    return _load_script(SCRIPT, "repair_jcm_score10_exact_terms")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_score10_exact_terms")


def _ingredient(name: str, grounded: bool = False) -> dict:
    row = {"preferred_term": name, "concentration": {"value": "1", "unit": "G_PER_L"}}
    if grounded:
        row["term"] = {"id": "CHEBI:26710", "label": "sodium chloride"}
    return row


def _doc(repair_module, target: Path) -> dict:
    return {
        "id": repair_module.EXPECTED_IDS[target],
        "name": target.stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium",
            "term": {"id": "jcm.grmd:test", "label": target.stem},
        },
        "notes": "Source: JCM",
        "ph_value": 7.0,
        "ingredients": [
            _ingredient(
                name,
                grounded=name not in repair_module.TARGET_TERMS[target],
            )
            for name in repair_module.TARGET_SIGNATURES[target]
        ],
        "curation_history": [],
    }


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


@pytest.mark.parametrize("target", tuple(_load_script(SCRIPT, "jcm_targets").TARGET_SIGNATURES))
def test_score10_exact_records_exit_review_ranking(
    repair_module,
    scorer_module,
    target: Path,
) -> None:
    repaired = repair_module.repair_record(
        target,
        _load_yaml(repair_module.NORMALIZED / target),
    )

    ingredients = _by_name(repaired["ingredients"])
    for preferred_term in repair_module.TARGET_TERMS[target]:
        term = repair_module.TERMS[preferred_term]
        assert ingredients[preferred_term]["term"] == term
        if term["id"].startswith("CHEBI:"):
            assert ingredients[preferred_term]["mediaingredientmech_chebi_term"] == term
        else:
            assert "mediaingredientmech_chebi_term" not in ingredients[preferred_term]

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target), repaired)]) == []


def test_repair_is_idempotent(repair_module) -> None:
    target = next(iter(repair_module.TARGET_SIGNATURES))
    once = repair_module.repair_record(
        target,
        _load_yaml(repair_module.NORMALIZED / target),
    )
    twice = repair_module.repair_record(target, once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)


def test_plan_repairs_targets_current_records(repair_module) -> None:
    expected = {}
    for relative in repair_module.TARGET_SIGNATURES:
        path = repair_module.NORMALIZED / relative
        expected[path] = repair_module.repair_record(relative, _load_yaml(path))

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = next(iter(repair_module.TARGET_SIGNATURES))
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_IDS[target]):
        repair_module.repair_record(target, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = next(iter(repair_module.TARGET_SIGNATURES))
    doc = _doc(repair_module, target)
    doc["ingredients"][0]["preferred_term"] = "Yeast extract"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(target, doc)
