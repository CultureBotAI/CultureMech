from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_672_score40.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_672_score40")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_672")


def _media_term(identifier: str) -> dict:
    return {"preferred_term": identifier, "term": {"id": identifier, "label": identifier}}


def _doc(repair, path: str) -> dict:
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": repair.RECIPE_NAMES[path],
        "original_name": "HALF STRENGTH NUTRIENT BROTH OR AGAR",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": _media_term(repair.EXPECTED_SOURCE_TERMS[path]),
        "ingredients": [
            {
                "preferred_term": "Difco 0001",
                "concentration": {"value": "1000", "unit": "G_PER_L"},
            },
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Difco 0003 or Difco 0001",
            },
        ],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
            "has_ontology_mappings",
        ],
    }


def _write_minimal_tree(repair, root: Path) -> None:
    for path in repair.EXPECTED_IDS:
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            yaml.safe_dump(_doc(repair, path), sort_keys=False),
            encoding="utf-8",
        )


def test_repair_record_replaces_1000_g_per_l_artifact(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.DSMZ_PARENT),
        repair_module.DSMZ_PARENT,
    )

    assert repaired["ingredients"] == [
        {
            "preferred_term": "Difco 0003 or Difco 0001",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "DSMZ Medium 672",
            "notes": repair_module.NOTES,
        },
    ]
    assert "preparation_steps" not in repaired
    assert "sterilization" not in repaired
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]
    assert repaired["references"] == [{"reference": repair_module.DSMZ_672_URL}]
    assert scorer_module.score_record(repaired) == (
        25,
        [
            "no composition component is grounded",
            "no pH and no temperature",
        ],
    )


def test_plan_repairs_links_komodo_source_duplicate(
    repair_module,
    tmp_path: Path,
) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    plans = repair_module.plan_repairs(root)

    parent = plans[root / repair_module.DSMZ_PARENT]
    child = plans[root / repair_module.KOMODO_CHILD]

    assert parent["variant_children"] == [
        {
            "path": (
                "data/normalized_yaml/bacterial/"
                "KOMODO_672_HALF_STRENGTH_NUTRIENT_BROTH_OR_AGAR.yaml"
            ),
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:006268",
            "name": "half_strength_nutrient_broth_or_agar",
            "notes": ("KOMODO Medium 672 is a source-catalogue duplicate of " "DSMZ Medium 672."),
        },
    ]
    assert child["parent_media"] == {
        "path": ("data/normalized_yaml/bacterial/" "half_strength_nutrient_broth_or_agar.yaml"),
        "relationship": "SOURCE_DUPLICATE",
        "id": "CultureMech:001813",
        "name": "half_strength_nutrient_broth_or_agar",
        "notes": "KOMODO Medium 672 is a source-catalogue duplicate of DSMZ Medium 672.",
    }
    assert child["variant_relationship"] == "SOURCE_DUPLICATE"
    assert child["variant_modifications"] == [
        "KOMODO source-catalogue duplicate of DSMZ Medium 672."
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    first = repair_module.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    assert repair_module.plan_repairs(root) == {}


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module, repair_module.DSMZ_PARENT)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:001813'"):
        repair_module.repair_record(doc, repair_module.DSMZ_PARENT)


def test_repair_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module, repair_module.KOMODO_CHILD)
    doc["media_term"]["term"]["id"] = "komodo.medium:9999"

    with pytest.raises(ValueError, match="expected 'komodo.medium:672'"):
        repair_module.repair_record(doc, repair_module.KOMODO_CHILD)
