from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_sp4_score10_exact_terms.py"
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
    return _load_script(SCRIPT, "repair_komodo_sp4_score10_exact_terms")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_sp4_score10")


def _ingredient(name: str, grounded: bool = False) -> dict:
    row = {"preferred_term": name, "concentration": {"value": "1", "unit": "G_PER_L"}}
    if grounded:
        row["term"] = {"id": "CHEBI:31991", "label": "phenol red"}
    return row


def _doc(repair_module) -> dict:
    return {
        "id": "CultureMech:test",
        "name": "test_sp4_child",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 1076",
            "term": {"id": "komodo.medium:1076_test", "label": "SP4 copy"},
        },
        "notes": "Source: KOMODO ModelSEED",
        "ph_value": 7.4,
        "ingredients": [
            _ingredient(name, grounded=name not in repair_module.TARGET_TERMS)
            for name in repair_module.TARGET_SIGNATURE
        ],
        "curation_history": [],
    }


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize(
    "target", tuple(_load_script(SCRIPT, "komodo_sp4_batch").TARGETS)
)
def test_score10_sp4_records_exit_review_ranking(
    repair_module,
    scorer_module,
    target: Path,
) -> None:
    repaired = repair_module.repair_record(
        target,
        _load_yaml(repair_module.NORMALIZED / target),
    )

    by_name = {row["preferred_term"]: row for row in repaired["ingredients"]}
    for preferred_term in repair_module.TARGET_TERMS:
        ingredient = by_name[preferred_term]
        assert ingredient["term"] == repair_module.TERMS[preferred_term]
        assert "mediaingredientmech_chebi_term" not in ingredient

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target), repaired)]) == []


def test_intentionally_unresolved_names_remain_unmapped(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(
        target,
        _load_yaml(repair_module.NORMALIZED / target),
    )
    by_name = {row["preferred_term"]: row for row in repaired["ingredients"]}

    for preferred_term in ("CMRL 1066", "Fetal bovine serum", "PPLO broth"):
        assert "term" not in by_name[preferred_term]


def test_repair_is_idempotent(repair_module) -> None:
    target = repair_module.TARGETS[0]
    once = repair_module.repair_record(
        target,
        _load_yaml(repair_module.NORMALIZED / target),
    )
    twice = repair_module.repair_record(target, once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)


def test_plan_repairs_targets_current_records(repair_module) -> None:
    plans = repair_module.plan_repairs()

    assert len(plans) == repair_module.EXPECTED_TARGET_COUNT
    assert set(plans) == {
        repair_module.NORMALIZED / relative for relative in repair_module.TARGETS
    }


def test_repair_rejects_source_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "komodo.medium:909"

    with pytest.raises(ValueError, match="expected KOMODO 1076"):
        repair_module.repair_record(target, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module)
    doc["ingredients"][0]["preferred_term"] = "Casein peptone"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(target, doc)
