from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_1850_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_1850_score35")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_1850")


def _doc(repair) -> dict:
    return {
        "id": repair.TARGET_ID,
        "name": "cultivation_medium_for_sf1ep_cells_for_treponema_pallidum",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "DSMZ Medium 1850",
            "term": {
                "id": repair.TARGET_SOURCE,
                "label": "Cultivation Medium for Sf1Ep cells for Treponema pallidum",
            },
        },
        "ingredients": [],
        "references": [{"reference": "doi: 10.1002/cpz1.44"}],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for row in doc["ingredients"]:
        if row["preferred_term"] == preferred_term:
            return row
    raise AssertionError(f"missing ingredient {preferred_term!r}")


def test_repair_adds_explicit_sf1ep_medium_components(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["temperature_value"] == 37.0
    assert "solutions" not in repaired
    assert len(repaired["ingredients"]) == 5

    assert _ingredient(repaired, "Eagle's MEM") == {
        "preferred_term": "Eagle's MEM",
        "concentration": {"value": "884.956", "unit": "ML_PER_L"},
        "source": "DSMZ Medium 1850",
        "notes": (
            "DSMZ Medium 1850 lists 500 ml Eagle's MEM (Sigma M4655) in "
            "a 565 ml Sf1Ep medium batch."
        ),
        "supplier_catalog": {
            "supplier_name": "Sigma",
            "catalog_number": "M4655",
        },
    }
    assert _ingredient(repaired, "MEM Non-Essential Amino Acids")["supplier_catalog"] == {
        "supplier_name": "Gibco",
        "catalog_number": "11140-050",
    }
    assert _ingredient(repaired, "L-glutamine solution")["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:18050",
        "label": "L-glutamine",
    }
    assert _ingredient(repaired, "Sodium pyruvate solution")["term"] == {
        "id": "CHEBI:50144",
        "label": "sodium pyruvate",
    }
    assert _ingredient(
        repaired,
        "Fetal bovine serum, heat inactivated",
    )[
        "concentration"
    ] == {"value": "88.4956", "unit": "ML_PER_L"}

    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "FILTER_STERILIZE",
        "STORE",
    ]
    assert repaired["sterilization"] == {"method": "FILTER"}
    assert scorer_module.score_record(repaired) == (0, [])


def test_plan_repairs_adds_source_and_review_metadata(
    repair_module,
    tmp_path: Path,
) -> None:
    root = tmp_path / "normalized"
    path = root / repair_module.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_doc(repair_module), sort_keys=False))

    plans = repair_module.plan_repairs(root)

    assert set(plans) == {path}
    repaired = plans[path]
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert repaired["references"] == [
        {"reference": "doi: 10.1002/cpz1.44"},
        {"reference": repair_module.DSMZ_1850},
    ]
    assert repaired["curation_history"][-1]["action"] == repair_module.ACTION
    assert repaired["curation_history"][-1]["source"] == repair_module.DSMZ_1850


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    path = root / repair_module.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_doc(repair_module), sort_keys=False))

    first = repair_module.plan_repairs(root)
    for target, doc in first.items():
        target.write_text(repair_module.dump_record(doc), encoding="utf-8")

    assert repair_module.plan_repairs(root) == {}


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:001271'"):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:18"

    with pytest.raises(ValueError, match="expected 'mediadive.medium:1850'"):
        repair_module.repair_record(doc)
