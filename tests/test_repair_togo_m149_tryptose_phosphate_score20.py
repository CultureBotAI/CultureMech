from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m149_tryptose_phosphate_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m149_tryptose_phosphate")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m149")


def _doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "tryptose_phosphate_agar",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "JCM Medium J158",
            "term": {"id": repair.EXPECTED_SOURCE_TERM, "label": "TRYPTOSE PHOSPHATE AGAR"},
        },
        "ingredients": [
            {
                "preferred_term": "Tryptose-phosphate",
                "concentration": {"value": "29.5", "unit": "G_PER_L"},
            },
            {
                "preferred_term": "Agar",
                "concentration": {"value": "15", "unit": "G_PER_L"},
                "term": {"id": "CHEBI:2509", "label": "agar"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:2509",
                    "label": "agar",
                },
            },
        ],
        "curation_history": [],
    }


def test_repair_restores_togo_water_and_products(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ingredients"] == [
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": repair_module.SOURCE,
            "notes": "TOGO M149 lists 1.0 L distilled water.",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
        },
        {
            "preferred_term": "Bacto agar (BD-Difco)",
            "concentration": {"value": "15", "unit": "G_PER_L"},
            "source": repair_module.SOURCE,
            "notes": "TOGO M149 lists 15 g/L Bacto agar from BD-Difco.",
        },
        {
            "preferred_term": "Tryptose phosphate broth (BD-Difco)",
            "concentration": {"value": "29.5", "unit": "G_PER_L"},
            "source": repair_module.SOURCE,
            "notes": "TOGO M149 lists 29.5 g/L Tryptose phosphate broth from BD-Difco.",
        },
    ]
    assert repaired["references"] == [{"reference": repair_module.TOGO_M149}]
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])


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
    assert matching_events[0]["source"] == repair_module.TOGO_M149


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
        path.relative_to(root): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(root): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M149"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_SOURCE_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="ingredient list drifted"):
        repair_module.repair_record(doc)
