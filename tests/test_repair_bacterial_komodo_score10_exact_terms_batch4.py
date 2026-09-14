from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_bacterial_komodo_score10_exact_terms_batch4.py"
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
    return _load_script(SCRIPT, "repair_bacterial_komodo_score10_exact_terms_batch4")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(
        SCORER,
        "score_review_need_for_bacterial_komodo_score10_batch4",
    )


def _ingredient(name: str, grounded: bool = False) -> dict:
    row = {"preferred_term": name, "concentration": {"value": "1", "unit": "G_PER_L"}}
    if grounded:
        row["term"] = {"id": "CHEBI:2509", "label": "agar"}
    return row


def _doc(repair_module, target) -> dict:
    return {
        "id": target.record_id,
        "name": target.path.stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium",
            "term": {"id": "komodo.medium:test", "label": target.path.stem},
        },
        "notes": "Source: KOMODO",
        "ph_value": 7.0,
        "ingredients": [
            _ingredient(
                name,
                grounded=name not in target.target_terms,
            )
            for name in target.signature
        ],
        "curation_history": [],
    }


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize(
    "target", tuple(_load_script(SCRIPT, "komodo_bacterial_batch4").TARGETS)
)
def test_score10_exact_records_exit_review_ranking(
    repair_module,
    scorer_module,
    target,
) -> None:
    repaired = repair_module.repair_record(
        target.path,
        _load_yaml(repair_module.NORMALIZED / target.path),
    )

    by_name = {row["preferred_term"]: row for row in repaired["ingredients"]}
    for preferred_term in target.target_terms:
        ingredient = by_name[preferred_term]
        assert ingredient["term"] == repair_module.TERMS[preferred_term]
        assert "mediaingredientmech_chebi_term" not in ingredient

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


@pytest.mark.parametrize(
    ("target_path", "unresolved_names"),
    (
        (
            Path("bacterial/medium_381_modified_for_dsm_12449.yaml"),
            ("Sea Salt",),
        ),
        (
            Path("bacterial/medium_548_modified_for_dsm_41755.yaml"),
            ("N-Z amine",),
        ),
        (
            Path("bacterial/medium_736_modified_for_dsm_22413.yaml"),
            ("Meat extract",),
        ),
    ),
)
def test_intentionally_unresolved_names_remain_unmapped(
    repair_module,
    target_path: Path,
    unresolved_names: tuple[str, ...],
) -> None:
    repaired = repair_module.repair_record(
        target_path,
        _load_yaml(repair_module.NORMALIZED / target_path),
    )
    by_name = {row["preferred_term"]: row for row in repaired["ingredients"]}

    for preferred_term in unresolved_names:
        assert "term" not in by_name[preferred_term]


def test_repair_is_idempotent(repair_module) -> None:
    target = repair_module.TARGETS[0]
    once = repair_module.repair_record(
        target.path,
        _load_yaml(repair_module.NORMALIZED / target.path),
    )
    twice = repair_module.repair_record(target.path, once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)


def test_plan_repairs_targets_current_records(repair_module) -> None:
    expected = {}
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        expected[path] = repair_module.repair_record(target.path, _load_yaml(path))

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(target.path, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0]["preferred_term"] = "Casein peptone"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(target.path, doc)
