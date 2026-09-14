from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_296_299_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _doc(repair, recipe) -> dict:
    return {
        "id": recipe.expected_id,
        "name": recipe.target.stem,
        "original_name": recipe.target.stem.upper(),
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": recipe.expected_media_term,
            "term": {
                "id": recipe.expected_media_term,
                "label": recipe.target.stem,
            },
        },
        "notes": "Source: KOMODO ModelSEED",
        "ingredients": [],
        "data_quality_flags": ["incomplete_composition"],
        "curation_history": [],
    }


def _write_minimal_tree(repair, root: Path) -> None:
    for recipe in repair.RECIPES:
        path = root / recipe.target
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(_doc(repair, recipe), sort_keys=False),
            encoding="utf-8",
        )


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


@pytest.fixture(scope="module")
def repair():
    return _load_script(SCRIPT, "repair_komodo_296_299_score35")


@pytest.fixture(scope="module")
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_296_299")


def test_repair_expands_marine_medium_293_variant(repair, scorer) -> None:
    recipe = repair.RECIPES[0]

    repaired = repair.repair_record(_doc(repair, recipe), recipe)

    assert scorer.score_record(repaired) == (0, [])
    assert len(repaired["ingredients"]) == 22
    assert repaired["ph_value"] == 7.2
    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "19.980020",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "2.997003",
        "unit": "G_PER_L",
    }
    assert "Na2-succinate" not in {
        row["preferred_term"] for row in repaired["ingredients"]
    }


def test_repair_expands_freshwater_medium_298_variant(repair, scorer) -> None:
    recipe = repair.RECIPES[1]

    repaired = repair.repair_record(_doc(repair, recipe), recipe)

    assert scorer.score_record(repaired) == (0, [])
    assert len(repaired["ingredients"]) == 22
    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "0.999001",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "0.399600",
        "unit": "G_PER_L",
    }
    assert "2,3-butanediol" not in {
        row["preferred_term"] for row in repaired["ingredients"]
    }


def test_repair_adds_polyethylene_glycol_and_anaerobic_gas(repair) -> None:
    for recipe in repair.RECIPES:
        repaired = repair.repair_record(_doc(repair, recipe), recipe)

        assert _ingredient(repaired, "Polyethylene glycol") == {
            "preferred_term": "Polyethylene glycol",
            "source": recipe.components[17].source,
            "notes": recipe.components[17].notes,
            "concentration": {"value": "1.000000", "unit": "G_PER_L"},
            "term": {
                "id": "CHEBI:46793",
                "label": "Polyethylene glycol",
            },
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:46793",
                "label": "Polyethylene glycol",
            },
        }
        assert _ingredient(repaired, "CO2")["concentration"] == {
            "value": "variable",
            "unit": "VARIABLE",
        }
        assert _ingredient(repaired, "N2")["term"] == {
            "id": "CHEBI:17997",
            "label": "dinitrogen",
        }


def test_repair_record_adds_references_and_flags(repair) -> None:
    expected_base_urls = {
        repair.MARINE_TARGET: repair.DSMZ_293_URL,
        repair.FRESHWATER_TARGET: repair.DSMZ_298_URL,
    }

    for recipe in repair.RECIPES:
        repaired = repair.repair_record(_doc(repair, recipe), recipe)

        assert repaired["references"] == [
            {"reference": recipe.komodo_url},
            {"reference": recipe.dsmz_url},
            {"reference": expected_base_urls[recipe.target]},
            {"reference": repair.DSMZ_320_URL},
        ]
        assert repaired["data_quality_flags"] == [
            "has_ontology_mappings",
            "ingredients_curated",
        ]


def test_plan_repairs_is_idempotent(repair, tmp_path: Path) -> None:
    _write_minimal_tree(repair, tmp_path)

    plans = repair.plan_repairs(tmp_path)
    for path, doc in plans.items():
        path.write_text(repair.dump_record(doc), encoding="utf-8")

    second = repair.plan_repairs(tmp_path)
    assert all(
        path.read_bytes() == repair.dump_record(doc).encode("utf-8")
        for path, doc in second.items()
    )


def test_repair_rejects_wrong_id(repair) -> None:
    recipe = repair.RECIPES[0]
    doc = _doc(repair, recipe)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004760"):
        repair.repair_record(doc, recipe)


def test_repair_rejects_wrong_source(repair) -> None:
    recipe = repair.RECIPES[1]
    doc = _doc(repair, recipe)
    doc["media_term"]["term"]["id"] = "komodo.medium:296"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:299"):
        repair.repair_record(doc, recipe)
