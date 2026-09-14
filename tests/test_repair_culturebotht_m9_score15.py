from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_culturebotht_m9_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_culturebotht_m9_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m9")


def _component(
    name: str,
    value: str,
    unit: str,
    term: tuple[str, str] | None = None,
) -> dict:
    row = {"preferred_term": name, "concentration": {"value": value, "unit": unit}}
    if term is not None:
        row["term"] = {"id": term[0], "label": term[1]}
    return row


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "M9",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component("D-Glucose", "4", "G_PER_L", ("CHEBI:17634", "D-glucose")),
            _component(
                "Magnesium sulfate",
                "2",
                "MILLIMOLAR",
                ("CHEBI:32599", "magnesium sulfate"),
            ),
            _component(
                "Calcium chloride",
                "0.1",
                "MILLIMOLAR",
                ("CHEBI:86158", "calcium chloride dihydrate"),
            ),
            _component("Sodium phosphate dibasic heptahydrate", "12.8", "G_PER_L"),
            _component(
                "Potassium phosphate monobasic",
                "3",
                "G_PER_L",
                ("CHEBI:63036", "potassium dihydrogen phosphate"),
            ),
            _component("Sodium Chloride", "0.5", "G_PER_L", ("CHEBI:26710", "sodium chloride")),
            _component(
                "Ammonium chloride",
                "1",
                "G_PER_L",
                ("CHEBI:31206", "ammonium chloride"),
            ),
        ],
        "description": "E. coli defined media",
        "notes": "Source: FEBA media definitions",
        "category": "specialized",
        "source_data": {
            "origin": "CultureBotHT",
            "notes": "database_id: M9; url: https://github.com/CultureBotAI/CultureBotHT",
        },
        "curation_history": [],
        "data_quality_flags": ["has_unmapped_ingredients"],
    }


def test_m9_exits_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["sources"] == [
        {
            "database": "CultureBotHT",
            "database_id": "M9",
            "url": "https://github.com/CultureBotAI/CultureBotHT",
        }
    ]
    assert repaired["references"] == [
        {"reference": "CultureBotHT:M9"},
        {"reference": "https://github.com/CultureBotAI/CultureBotHT"},
    ]


def test_m9_repair_is_idempotent(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1


def test_plan_repairs_target_record(repair_module) -> None:
    target_path = repair_module.NORMALIZED / repair_module.TARGET
    expected_target = repair_module.repair_record(
        yaml.safe_load(target_path.read_text(encoding="utf-8"))
    )

    assert repair_module.plan_repairs() == {target_path: expected_target}


def test_m9_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_m9_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["preferred_term"] = "Glucose"

    with pytest.raises(ValueError, match="ingredient list drifted"):
        repair_module.repair_record(doc)


def test_m9_repair_requires_culturebotht_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["source_data"] = {"origin": "other", "notes": "database_id: M9"}

    with pytest.raises(ValueError, match="missing CultureBotHT source"):
        repair_module.repair_record(doc)
