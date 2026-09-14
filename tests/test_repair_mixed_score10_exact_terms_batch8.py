from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_mixed_score10_exact_terms_batch8.py"
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
    return _load_script(SCRIPT, "repair_mixed_score10_exact_terms_batch8")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_mixed_score10_batch8")


def _ingredient(name: str, grounded: bool = False) -> dict:
    row = {"preferred_term": name, "concentration": {"value": "1", "unit": "G_PER_L"}}
    if grounded:
        row["term"] = {"id": "CHEBI:2509", "label": "agar"}
    return row


def _doc(repair_module, target) -> dict:
    return {
        "id": target.record_id,
        "name": target.path.stem,
        "category": target.path.parts[0],
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "DSMZ Medium",
            "term": {"id": "mediadive.medium:test", "label": target.path.stem},
        },
        "notes": "Source: DSMZ",
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


@pytest.mark.parametrize("target", tuple(_load_script(SCRIPT, "mixed_batch8").TARGETS))
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
            Path("bacterial/mc.yaml"),
            ("Calf serum", "Liver digest"),
        ),
        (
            Path("bacterial/methanosaeta_brevibacterium_medium.yaml"),
            ("CaCl2\u30fb2H2O", "L--Cysteine\u30fbHCl\u30fbH2O", "peptone"),
        ),
        (
            Path("fungal/maltose_bennetts_agar.yaml"),
            ("N-Z amine",),
        ),
        (
            Path("fungal/sea_salts_yeast_extract_peptone_medium.yaml"),
            ("Sea Salt",),
        ),
        (
            Path("fungal/trypticase_soy_yeast_extract_medium.yaml"),
            ("Trypticase soy broth",),
        ),
        (
            Path("specialized/modified_bacto_marine_broth.yaml"),
            ("Difco marine broth",),
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
    doc["ingredients"][0]["preferred_term"] = "Peptone"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(target.path, doc)
