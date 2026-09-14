from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_604_bacto_marine_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_604_bacto_marine_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_604")


def _doc(repair, target) -> dict:
    return {
        "id": target.expected_id,
        "name": target.path.stem,
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": str(target.path),
            "term": {
                "id": target.expected_media_term,
                "label": "BACTO MARINE AGAR",
            },
        },
        "notes": "stale import note",
        "ingredients": [
            {
                "preferred_term": "Marine agar 2216",
                "concentration": {"value": "1000", "unit": "G_PER_L"},
                "term": {"id": "CHEBI:2509", "label": "agar"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:2509",
                    "label": "agar",
                },
            }
        ],
        "curation_history": [],
    }


def _write_minimal_tree(repair, root: Path) -> None:
    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(_doc(repair, target), sort_keys=False),
            encoding="utf-8",
        )


def test_repair_replaces_false_agar_with_commercial_product(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["ingredients"] == [
        {
            "preferred_term": "Marine agar 2216 (Difco 0979)",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "DSMZ Medium 604",
            "notes": (
                "DSMZ Medium 604 names Marine Agar 2216 (Difco 0979) as the "
                "only component but does not state an amount."
            ),
            "culturemech_term": repair_module.MARINE_AGAR_2216,
        }
    ]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_repair_adds_reference_flags_and_history(repair_module) -> None:
    target = repair_module.TARGETS[1]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Prepare the Marine Agar 2216 (Difco 0979) product.",
        }
    ]
    assert repaired["references"] == [{"reference": repair_module.DSMZ_604_URL}]
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.DSMZ_604_URL,
            "notes": repair_module.NOTES,
        }
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    first = repair_module.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(root): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006092"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGETS[1]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:12"

    with pytest.raises(ValueError, match="expected media term mediadive.medium:604"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="expected one Marine agar 2216 ingredient"):
        repair_module.repair_record(doc, target)
