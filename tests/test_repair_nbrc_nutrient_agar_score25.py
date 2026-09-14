from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_nutrient_agar_score25.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_nbrc_nutrient_agar_score25")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_nbrc_nutrient_agar")


def _doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "nutrient_agar",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            {
                "preferred_term": "Beef extract",
                "concentration": {"value": "3.0", "unit": "G_PER_L"},
            },
            {
                "preferred_term": "Peptone",
                "concentration": {"value": "5.0", "unit": "G_PER_L"},
            },
            {
                "preferred_term": "Agar",
                "concentration": {"value": "15.0", "unit": "G_PER_L"},
                "term": {"id": "CHEBI:2509", "label": "agar"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:2509",
                    "label": "agar",
                },
            },
        ],
        "curation_history": [],
    }


def test_repair_adds_nbrc_identity_and_jcm_reference(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 1",
        "term": {"id": "nbrc.medium:1", "label": "NBRC Medium 1"},
    }
    assert repaired["references"] == [{"reference": repair_module.JCM_74}]
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]


def test_repair_adds_water_and_common_groundings(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ingredients"] == [
        {
            "preferred_term": "Beef extract",
            "concentration": {"value": "3.0", "unit": "G_PER_L"},
            "source": repair_module.SOURCE,
            "notes": "NBRC No. 1 and JCM Medium 74 list 3.0 g/L beef extract.",
            "term": {"id": "FOODON:03302088", "label": "beef extract"},
        },
        {
            "preferred_term": "Peptone",
            "concentration": {"value": "5.0", "unit": "G_PER_L"},
            "source": repair_module.SOURCE,
            "notes": "NBRC No. 1 and JCM Medium 74 list 5.0 g/L peptone.",
            "term": {"id": "MICRO:0000178", "label": "peptone"},
        },
        {
            "preferred_term": "Agar",
            "concentration": {"value": "15.0", "unit": "G_PER_L"},
            "source": repair_module.SOURCE,
            "notes": "NBRC No. 1 and JCM Medium 74 list 15.0 g/L agar.",
            "term": {"id": "CHEBI:2509", "label": "agar"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:2509",
                "label": "agar",
            },
        },
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": repair_module.SOURCE,
            "notes": "NBRC No. 1 and JCM Medium 74 list 1.0 L distilled water.",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:15377",
                "label": "water",
            },
        },
    ]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_repair_adds_history_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0] == {
        "timestamp": repair_module.TIMESTAMP,
        "curator": repair_module.CURATOR,
        "action": repair_module.ACTION,
        "source": repair_module.JCM_74,
        "notes": repair_module.NOTES,
    }


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    path = root / repair_module.PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_doc(repair_module), sort_keys=False))

    first = repair_module.plan_repairs(root)
    for repaired_path, doc in first.items():
        repaired_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="ingredient list drifted"):
        repair_module.repair_record(doc)
