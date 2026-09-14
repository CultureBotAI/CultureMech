from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_culturebotht_bg11_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_culturebotht_bg11_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_culturebotht_bg11")


def _doc(target, *, source_shape: str = "sources") -> dict:
    doc = {
        "id": target.expected_id,
        "name": target.source_id,
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {"preferred_term": preferred_term}
            for preferred_term in target.expected_ingredients
        ],
        "notes": "Source: FEBA media definitions",
        "curation_history": [],
    }
    if source_shape == "sources":
        doc["sources"] = [
            {
                "database": "CultureBotHT",
                "database_id": target.source_id,
                "url": "https://github.com/CultureBotAI/CultureBotHT",
            }
        ]
    else:
        doc["source_data"] = {
            "origin": "CultureBotHT",
            "notes": (
                f"database_id: {target.source_id}; "
                "url: https://github.com/CultureBotAI/CultureBotHT"
            ),
        }
    return doc


def test_repair_adds_media_term_and_ph_when_description_had_ph(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[0]

    repaired = repair_module.repair_record(
        _doc(target, source_shape="source_data"),
        target,
    )

    assert repaired["media_term"] == {"preferred_term": "BG11"}
    assert repaired["ph_value"] == 7.1
    assert repaired["references"] == [
        {"reference": "CultureBotHT:BG11"},
        {"reference": repair_module.CULTUREBOTHT_URL},
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_adds_media_term_without_unsourced_ph(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[1]

    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["media_term"] == {"preferred_term": "BG11 no bicarb"}
    assert "ph_value" not in repaired
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_plan_repair_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    for target in repair_module.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert first == second


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["sources"][0]["database_id"] = "other"

    with pytest.raises(ValueError, match="missing CultureBotHT source"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)
