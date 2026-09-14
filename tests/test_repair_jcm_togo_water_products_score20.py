from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_togo_water_products_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm_togo_water_products_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_togo_water")


def _doc(target) -> dict:
    if target.expected_source_term.endswith("J105"):
        ingredients = [
            {"preferred_term": "Heart Infusion Broth"},
            {"preferred_term": "Agar"},
        ]
    elif target.expected_source_term == "TOGO:M97":
        ingredients = [
            {"preferred_term": "Distilled water"},
            {"preferred_term": "Agar"},
            {"preferred_term": "Heart infusion broth (BD-Difco)"},
        ]
    elif target.expected_source_term.endswith("J248"):
        ingredients = [
            {"preferred_term": "Cow manure"},
            {"preferred_term": "Agar"},
        ]
    else:
        ingredients = [
            {"preferred_term": "Distilled water"},
            {"preferred_term": "Cow manure"},
            {"preferred_term": "Agar"},
        ]

    return {
        "id": target.expected_id,
        "name": target.path.stem,
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": str(target.path),
            "term": {
                "id": target.expected_source_term,
                "label": target.path.stem,
            },
        },
        "notes": "stale import note",
        "ingredients": ingredients,
        "curation_history": [],
    }


def _target(repair, path: Path):
    for target in repair.TARGETS:
        if target.path == path:
            return target
    raise AssertionError(f"unknown target: {path}")


def _write_minimal_tree(repair, root: Path) -> None:
    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target), sort_keys=False))


def test_repair_adds_missing_jcm_105_water(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.HIA_JCM)

    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["ingredients"] == [
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": repair_module.M97_SOURCE,
            "notes": "TOGO M97/JCM Medium 105 snapshot lists 1.0 L distilled water.",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:15377",
                "label": "water",
            },
        },
        {
            "preferred_term": "Agar",
            "concentration": {"value": "15", "unit": "G_PER_L"},
            "source": repair_module.M97_SOURCE,
            "notes": "TOGO M97/JCM Medium 105 snapshot lists 15 g/L agar.",
            "term": {"id": "CHEBI:2509", "label": "agar"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:2509",
                "label": "agar",
            },
        },
        {
            "preferred_term": "Heart infusion broth (BD-Difco)",
            "concentration": {"value": "12.5", "unit": "G_PER_L"},
            "source": repair_module.M97_SOURCE,
            "notes": (
                "TOGO M97/JCM Medium 105 snapshot lists 12.5 g/L Heart "
                "infusion broth from BD-Difco."
            ),
        },
    ]
    assert repaired["references"] == [{"reference": repair_module.TOGO_M97}]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_repair_corrects_togo_240_water_unit_and_keeps_cow_manure_opaque(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.COW_MANURE_TOGO)

    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["ingredients"][0] == {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1000", "unit": "ML_PER_L"},
        "source": repair_module.M240_SOURCE,
        "notes": "TOGO M240/JCM Medium 248 snapshot lists 1.0 L distilled water.",
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:15377",
            "label": "water",
        },
    }
    assert repaired["ingredients"][1] == {
        "preferred_term": "Cow manure",
        "concentration": {"value": "50", "unit": "G_PER_L"},
        "source": repair_module.M240_SOURCE,
        "notes": "TOGO M240/JCM Medium 248 snapshot lists 50 g/L dry cow manure.",
    }
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Suspend 50.0 g of dry cow manure in 1.0 L distilled water, "
                "boil for 1 hr, filter first through cheesecloth and then "
                "paper, and make up the volume to 1.0 L."
            ),
        },
    ]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_repair_adds_flags_and_history_once(repair_module) -> None:
    target = _target(repair_module, repair_module.COW_MANURE_JCM)

    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == repair_module.TOGO_M240


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
    target = _target(repair_module, repair_module.HIA_TOGO)
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = _target(repair_module, repair_module.HIA_JCM)
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M97"

    with pytest.raises(ValueError, match=target.expected_source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = _target(repair_module, repair_module.COW_MANURE_TOGO)
    doc = _doc(target)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="ingredient list drifted"):
        repair_module.repair_record(doc, target)
