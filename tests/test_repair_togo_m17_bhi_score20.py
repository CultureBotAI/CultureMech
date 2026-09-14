from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m17_bhi_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m17_bhi_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m17_bhi")


def _doc(repair, update) -> dict:
    return {
        "id": repair.EXPECTED_IDS[update.path],
        "name": Path(update.path).stem,
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": ingredient["preferred_term"],
                "concentration": {"value": "1", "unit": "G_PER_L"},
            }
            for ingredient in update.ingredients
        ],
        "media_term": {
            "preferred_term": update.source_label,
            "term": {"id": repair.EXPECTED_SOURCE_TERMS[update.path]},
        },
        "curation_history": [],
    }


def _target(repair, path: str):
    return repair.UPDATE_BY_PATH[path]


def _write_minimal_tree(repair, root: Path) -> None:
    for update in repair.UPDATES:
        path = root / update.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(_doc(repair, update), sort_keys=False),
            encoding="utf-8",
        )


@pytest.mark.parametrize(
    ("path", "temperature"),
    [
        ("M2230_M17_LACTOSE", 42.0),
        ("M2492_M17_GLUCOSE", 37.0),
        ("M2493_M17_LACTOSE", 37.0),
        ("M2830_BHI_GLUCOSE", 36.0),
        ("M2882_M17_DIFCO_GLUCOSE", 30.0),
        ("M2951_GM17_OXOID", 30.0),
    ],
)
def test_togo_wrappers_become_curated_two_component_recipes(
    repair_module,
    scorer_module,
    path: str,
    temperature: float,
) -> None:
    update = _target(repair_module, getattr(repair_module, path))

    repaired = repair_module.repair_wrapper(_doc(repair_module, update), update)

    assert repaired["temperature_value"] == temperature
    assert repaired["ingredients"][1]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_gm17_uses_half_percent_glucose_not_half_gram_per_liter(
    repair_module,
) -> None:
    update = _target(repair_module, repair_module.M2951_GM17_OXOID)

    repaired = repair_module.repair_wrapper(_doc(repair_module, update), update)

    assert repaired["ingredients"][0] == {
        "preferred_term": "glucose",
        "concentration": {"value": "0.5", "unit": "PERCENT_W_V"},
        "source": "TOGO M2951",
        "notes": "TOGO M2951 lists glucose at 0.5% w/v.",
        "term": {"id": "CHEBI:17234", "label": "glucose"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:17234",
            "label": "glucose",
        },
    }


def test_m17_scharlau_keeps_lactose_as_twenty_grams_per_liter(
    repair_module,
) -> None:
    update = _target(repair_module, repair_module.M2230_M17_LACTOSE)

    repaired = repair_module.repair_wrapper(_doc(repair_module, update), update)

    assert repaired["ingredients"][0]["preferred_term"] == "Lactose"
    assert repaired["ingredients"][0]["concentration"] == {
        "value": "20",
        "unit": "G_PER_L",
    }
    assert repaired["preparation_steps"][-1] == {
        "step_number": 2,
        "action": "MIX",
        "description": "Cultivate anaerobically at 42 C.",
    }


def test_repair_preserves_existing_variant_children(repair_module) -> None:
    update = _target(repair_module, repair_module.M2492_M17_GLUCOSE)
    doc = _doc(repair_module, update)
    child = {
        "path": "data/normalized_yaml/bacterial/m17_broth_containing_lactose.yaml",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": "CultureMech:009067",
        "name": "m17_broth_containing_lactose",
    }
    doc["variant_children"] = [child]

    repaired = repair_module.repair_wrapper(doc, update)

    assert repaired["variant_children"] == [child]


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
    update = _target(repair_module, repair_module.M2492_M17_GLUCOSE)
    doc = _doc(repair_module, update)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:009066'"):
        repair_module.repair_wrapper(doc, update)


def test_repair_rejects_wrong_source(repair_module) -> None:
    update = _target(repair_module, repair_module.M2493_M17_LACTOSE)
    doc = _doc(repair_module, update)
    doc["media_term"]["term"]["id"] = "TOGO:M2492"

    with pytest.raises(ValueError, match="expected 'TOGO:M2493'"):
        repair_module.repair_wrapper(doc, update)


def test_repair_rejects_wrong_components(repair_module) -> None:
    update = _target(repair_module, repair_module.M2951_GM17_OXOID)
    doc = _doc(repair_module, update)
    doc["ingredients"][1]["preferred_term"] = "M17 broth"

    with pytest.raises(ValueError, match="expected"):
        repair_module.repair_wrapper(doc, update)
