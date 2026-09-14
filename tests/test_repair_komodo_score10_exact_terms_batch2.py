from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_score10_exact_terms_batch2.py"
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
    return _load_script(SCRIPT, "repair_komodo_score10_exact_terms_batch2")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_score10_batch2")


def _ingredient(name: str, grounded: bool = False) -> dict:
    row = {"preferred_term": name, "concentration": {"value": "1", "unit": "G_PER_L"}}
    if grounded:
        row["term"] = {"id": "CHEBI:2509", "label": "agar"}
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
            "preferred_term": "KOMODO Medium",
            "term": {"id": "komodo.medium:test", "label": target.stem},
        },
        "notes": "Source: KOMODO",
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


@pytest.mark.parametrize(
    "target", tuple(_load_script(SCRIPT, "komodo_batch2").TARGET_SIGNATURES)
)
def test_score10_exact_records_exit_review_ranking(
    repair_module,
    scorer_module,
    target: Path,
) -> None:
    repaired = repair_module.repair_record(
        target,
        _load_yaml(repair_module.NORMALIZED / target),
    )

    by_name = {row["preferred_term"]: row for row in repaired["ingredients"]}
    for preferred_term in repair_module.TARGET_TERMS[target]:
        ingredient = by_name[preferred_term]
        assert ingredient["term"] == repair_module.TERMS[preferred_term]
        assert "mediaingredientmech_chebi_term" not in ingredient

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target), repaired)]) == []


@pytest.mark.parametrize(
    ("target", "unresolved_names"),
    (
        (
            Path("bacterial/KOMODO_381_LB_Luria-Bertani_medium.yaml"),
            ("Sea Salt",),
        ),
        (
            Path("bacterial/KOMODO_435_KDM-2_medium.yaml"),
            ("Activated charcoal", "Fetal bovine serum"),
        ),
        (
            Path("bacterial/KOMODO_581_GLYCEROL_CORNSTEEP_AGAR.yaml"),
            ("Corn steep powder",),
        ),
        (
            Path("bacterial/KOMODO_948_OXOID_NUTRIENT_BROTH.yaml"),
            ("Nutrient broth",),
        ),
    ),
)
def test_intentionally_unresolved_names_remain_unmapped(
    repair_module,
    target: Path,
    unresolved_names: tuple[str, ...],
) -> None:
    repaired = repair_module.repair_record(
        target,
        _load_yaml(repair_module.NORMALIZED / target),
    )
    by_name = {row["preferred_term"]: row for row in repaired["ingredients"]}

    for preferred_term in unresolved_names:
        assert "term" not in by_name[preferred_term]


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
    doc["ingredients"][0]["preferred_term"] = "Casein peptone"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(target, doc)
