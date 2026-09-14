from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_459_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _doc(repair, target) -> dict:
    return {
        "id": target.expected_id,
        "name": "sucrose_peptone_medium",
        "original_name": "SUCROSE-PEPTONE-MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "Medium 459",
            "term": {
                "id": target.expected_media_term,
                "label": "SUCROSE-PEPTONE-MEDIUM",
            },
        },
        "notes": "Source: 459",
        "ingredients": [
            {
                "preferred_term": "Peptone",
                "concentration": {"value": "20", "unit": "G_PER_L"},
            },
            {
                "preferred_term": "Sucrose",
                "term": {"id": "CHEBI:17992", "label": "sucrose"},
                "concentration": {"value": "20", "unit": "G_PER_L"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:17992",
                    "label": "sucrose",
                },
            },
        ],
        "curation_history": [],
    }


@pytest.fixture
def repair():
    return _load_script(SCRIPT, "repair_dsmz_459_score20")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_dsmz_459")


def test_repair_record_grounds_peptone_and_keeps_dsmz_formula(repair, scorer) -> None:
    target = repair.TARGETS[0]
    once = repair.repair_record(_doc(repair, target), target)
    twice = repair.repair_record(once, target)

    assert once == twice
    assert scorer.score_record(twice) == (5, ["no pH and no temperature"])
    assert once["ingredients"] == [
        {
            "preferred_term": "Peptone",
            "concentration": {"value": "20", "unit": "G_PER_L"},
            "source": "DSMZ Medium 459",
            "notes": "DSMZ Medium 459 lists 20.0 g/L peptone.",
            "term": {"id": "MICRO:0000178", "label": "Peptone"},
        },
        {
            "preferred_term": "Sucrose",
            "term": {"id": "CHEBI:17992", "label": "sucrose"},
            "concentration": {"value": "20", "unit": "G_PER_L"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:17992",
                "label": "sucrose",
            },
            "source": "DSMZ Medium 459",
            "notes": "DSMZ Medium 459 lists 20.0 g/L sucrose.",
        },
    ]


def test_repair_record_adds_reference_flags_and_history(repair) -> None:
    target = repair.TARGETS[1]
    repaired = repair.repair_record(_doc(repair, target), target)

    assert repaired["references"] == [{"reference": repair.DSMZ_459_URL}]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair.TIMESTAMP,
            "curator": repair.CURATOR,
            "action": repair.ACTION,
            "source": repair.DSMZ_459_URL,
            "notes": repair.NOTES,
        }
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    target = repair.TARGETS[0]
    doc = _doc(repair, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:001573"):
        repair.repair_record(doc, target)


def test_repair_record_rejects_wrong_source(repair) -> None:
    target = repair.TARGETS[1]
    doc = _doc(repair, target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:459"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:459"):
        repair.repair_record(doc, target)


def test_repair_record_rejects_ingredient_drift(repair) -> None:
    target = repair.TARGETS[0]
    doc = _doc(repair, target)
    doc["ingredients"][0]["concentration"]["value"] = "10"

    with pytest.raises(ValueError, match="ingredient list drifted"):
        repair.repair_record(doc, target)


def test_target_records_match_reviewed_formula(repair) -> None:
    for target in repair.TARGETS:
        path = repair.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        repaired = repair.repair_record(doc, target)

        assert repaired["id"] == target.expected_id
        assert [
            {
                "preferred_term": row["preferred_term"],
                "concentration": row["concentration"],
            }
            for row in repaired["ingredients"]
        ] == repair.EXPECTED_INGREDIENTS
