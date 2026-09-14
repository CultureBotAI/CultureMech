from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_corn_meal_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def repair():
    return _load_script(SCRIPT, "repair_jcm_corn_meal_score20")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_jcm_corn_meal")


def _preferred_source(repair, target) -> str:
    if target.path.startswith("bacterial/JCM_J150"):
        return "JCM Medium J150"
    if target.path.startswith("bacterial/JCM_J1329"):
        return "JCM Medium J1329"
    if target.path.startswith("bacterial/TOGO_M141"):
        return "TOGO Medium M141"
    if target.path.startswith("bacterial/TOGO_M3004"):
        return "TOGO Medium M3004"
    raise AssertionError(f"unexpected target {target.path}")


def _media_term(identifier: str, preferred_term: str) -> dict:
    return {
        "preferred_term": preferred_term,
        "term": {"id": identifier, "label": "CORN MEAL AGAR"},
    }


def _doc(repair, target) -> dict:
    return {
        "id": repair.EXPECTED_IDS[target.path],
        "name": "corn_meal_agar",
        "original_name": "CORN MEAL AGAR",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": _media_term(
            repair.EXPECTED_SOURCE_TERMS[target.path],
            _preferred_source(repair, target),
        ),
        "notes": "Source",
        "ingredients": [
            {
                "preferred_term": "Corn meal agar",
                "term": {"id": "CHEBI:2509", "label": "agar"},
                "concentration": {"value": "17", "unit": "G_PER_L"},
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
        path.write_text(yaml.safe_dump(_doc(repair, target), sort_keys=False), encoding="utf-8")


def test_repair_record_rebuilds_jcm_150_product_recipe(repair, scorer) -> None:
    target = repair.TARGETS[0]
    once = repair.repair_record(_doc(repair, target), target)
    twice = repair.repair_record(once, target)

    assert once == twice
    assert scorer.score_record(twice) == (5, ["no pH and no temperature"])
    assert once["ingredients"] == [
        {
            "preferred_term": "Corn meal agar (BD-Difco)",
            "concentration": {"value": "17.0", "unit": "G_PER_L"},
            "source": "JCM Medium 150",
            "notes": (
                "JCM Medium 150 lists 17.0 g/L Corn meal agar (BD-Difco); "
                "this is a commercial dehydrated medium and is intentionally "
                "left ungrounded."
            ),
        },
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1.0", "unit": "L"},
            "source": "JCM Medium 150",
            "notes": "JCM Medium 150 lists 1.0 L distilled water.",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
        },
    ]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_record_rebuilds_jcm_1329_product_recipe(repair) -> None:
    target = repair.TARGETS[2]
    repaired = repair.repair_record(_doc(repair, target), target)

    assert repaired["ingredients"][0]["preferred_term"] == "Corn meal agar (Nissui)"
    assert repaired["ingredients"][0]["source"] == "JCM Medium 1329"
    assert repaired["references"] == [{"reference": repair.JCM_1329_URL}]


def test_plan_repairs_links_togo_source_duplicates(repair, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair, root)

    plans = repair.plan_repairs(root)
    parent = plans[root / "bacterial/JCM_J150_CORN_MEAL_AGAR.yaml"]
    child = plans[root / "bacterial/TOGO_M141_Corn_Meal_Agar.yaml"]

    assert parent["variant_children"] == [
        {
            "path": "data/normalized_yaml/bacterial/TOGO_M141_Corn_Meal_Agar.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:007957",
            "name": "corn_meal_agar",
            "notes": "TOGO Medium M141 is a TOGO duplicate of JCM Medium J150.",
        }
    ]
    assert child["parent_media"] == {
        "path": "data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
        "relationship": "SOURCE_DUPLICATE",
        "id": "CultureMech:002509",
        "name": "corn_meal_agar",
        "notes": "TOGO imported the same Corn Meal Agar formula from the reviewed JCM Medium J150 source.",
    }
    assert child["variant_relationship"] == "SOURCE_DUPLICATE"


def test_repair_record_rejects_wrong_id(repair) -> None:
    target = repair.TARGETS[0]
    doc = _doc(repair, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:002509"):
        repair.repair_record(doc, target)


def test_repair_record_rejects_wrong_source(repair) -> None:
    target = repair.TARGETS[1]
    doc = _doc(repair, target)
    doc["media_term"]["term"]["id"] = "TOGO:M3004"

    with pytest.raises(ValueError, match="missing expected media term TOGO:M141"):
        repair.repair_record(doc, target)


def test_target_records_have_reviewed_source_terms(repair) -> None:
    for target in repair.TARGETS:
        path = repair.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == repair.EXPECTED_IDS[target.path]
        assert doc["media_term"]["term"]["id"] == repair.EXPECTED_SOURCE_TERMS[target.path]
