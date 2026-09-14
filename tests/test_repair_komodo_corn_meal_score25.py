from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_corn_meal_score25.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_komodo_corn_meal_score25")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_corn_meal")


def _media_term(identifier: str) -> dict:
    return {"preferred_term": identifier, "term": {"id": identifier, "label": identifier}}


def _original_name(repair, path: str) -> str:
    names = {
        repair.KOMODO_DSM_25720: "For DSM 25720",
        repair.KOMODO_DSM_25939: "For DSM 25939",
        repair.KOMODO_DSM_25945: "For DSM 25945",
    }
    return names.get(path, "CORN MEAL AGAR")


def _doc(repair, path: str) -> dict:
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": repair.RECIPE_NAMES[path],
        "original_name": _original_name(repair, path),
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": _media_term(repair.EXPECTED_SOURCE_TERMS[path]),
        "ingredients": [
            {
                "preferred_term": "Corn meal",
                "concentration": {"value": "50", "unit": "G_PER_L"},
            }
        ],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
            "has_unmapped_ingredients",
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


def test_repair_record_grounds_corn_meal_and_agar(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target.path), target)

    assert repaired["ph_value"] == 6.0
    assert repaired["ingredients"] == [
        {
            "preferred_term": "Corn meal",
            "concentration": {"value": "50.0", "unit": "G_PER_L"},
            "source": "DSMZ Medium 191",
            "notes": (
                "DSMZ Medium 191 blends 50.0 g corn meal in 800 ml distilled "
                "water, leaves it overnight in the refrigerator, heats it at "
                "60 C for one hour, filters it, and brings the filtrate to 1 L."
            ),
            "term": {"id": "mediadive.compound:2087", "label": "Corn meal"},
        },
        {
            "preferred_term": "Agar",
            "term": {"id": "CHEBI:2509", "label": "agar"},
            "concentration": {"value": "10.0", "unit": "G_PER_L"},
            "source": "DSMZ Medium 191",
            "notes": (
                "DSMZ Medium 191 adds 10.0 g agar after bringing the corn-meal "
                "filtrate to 1 L and heats to dissolve it before autoclaving."
            ),
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:2509",
                "label": "agar",
            },
        },
    ]
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_plan_repairs_links_komodo_variants_to_dsmz_parent(
    repair_module,
    scorer_module,
    tmp_path: Path,
) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    plans = repair_module.plan_repairs(root)

    parent = plans[root / repair_module.DSMZ_PARENT]
    assert parent["variant_children"] == [
        {
            "path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:004218",
            "name": "corn_meal_agar",
            "notes": "KOMODO Medium 191 is a source-catalogue duplicate of DSMZ Medium 191.",
        },
        {
            "path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml",
            "relationship": "PH_VARIANT",
            "id": "CultureMech:004217",
            "name": "for_dsm_25939",
            "notes": (
                "KOMODO Medium 191.4 preserves DSMZ Medium 191 components and "
                "concentrations but records pH 7.2 for DSM 25939."
            ),
        },
        {
            "path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml",
            "relationship": "PH_VARIANT",
            "id": "CultureMech:004216",
            "name": "for_dsm_25945",
            "notes": (
                "KOMODO Medium 191.3 preserves DSMZ Medium 191 components and "
                "concentrations but records pH 7.4 for DSM 25945."
            ),
        },
        {
            "path": "data/normalized_yaml/bacterial/for_dsm_25720.yaml",
            "relationship": "PH_VARIANT",
            "id": "CultureMech:004215",
            "name": "for_dsm_25720",
            "notes": (
                "KOMODO Medium 191.2 preserves DSMZ Medium 191 components and "
                "concentrations but records pH 7.5 for DSM 25720."
            ),
        },
    ]

    dsm_25720 = plans[root / repair_module.KOMODO_DSM_25720]
    assert dsm_25720["ph_value"] == 7.5
    assert dsm_25720["parent_media"] == {
        "path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml",
        "relationship": "PH_VARIANT",
        "id": "CultureMech:001283",
        "name": "corn_meal_agar",
        "notes": (
            "KOMODO Medium 191.2 preserves DSMZ Medium 191 components and "
            "concentrations but records pH 7.5 for DSM 25720."
        ),
    }
    assert dsm_25720["variant_relationship"] == "PH_VARIANT"
    assert dsm_25720["references"] == [
        {"reference": repair_module.DSMZ_191_URL}
    ]
    assert scorer_module.score_record(dsm_25720) == (0, [])

    dsm_25939 = plans[root / repair_module.KOMODO_DSM_25939]
    assert dsm_25939["ph_value"] == 7.2
    assert dsm_25939["parent_media"] == {
        "path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml",
        "relationship": "PH_VARIANT",
        "id": "CultureMech:001283",
        "name": "corn_meal_agar",
        "notes": (
            "KOMODO Medium 191.4 preserves DSMZ Medium 191 components and "
            "concentrations but records pH 7.2 for DSM 25939."
        ),
    }
    assert dsm_25939["variant_relationship"] == "PH_VARIANT"
    assert dsm_25939["references"] == [
        {"reference": repair_module.DSMZ_191_URL}
    ]
    assert scorer_module.score_record(dsm_25939) == (0, [])


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    first = repair_module.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    assert repair_module.plan_repairs(root) == {}


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target.path)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:001283'"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target.path)
    doc["media_term"]["term"]["id"] = "mediadive.medium:9999"

    with pytest.raises(ValueError, match="expected 'mediadive.medium:191'"):
        repair_module.repair_record(doc, target)
