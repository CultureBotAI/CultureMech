from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_sag_sources_score10.py"
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
    return _load_script(SCRIPT, "repair_sag_sources_score10")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_sag_sources")


def _doc() -> dict:
    pdf_url = "http://sagdb.uni-goettingen.de/culture_media/Test Medium.pdf"
    return {
        "id": "CultureMech:test",
        "name": "test_medium",
        "category": "algae",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "notes": f"Full recipe available at {pdf_url}",
        "temperature_range": "15-30 C depending on species",
        "data_quality_flags": ["ingredients_curated"],
        "ingredients": [
            {
                "preferred_term": "NaCl",
                "term": {"id": "CHEBI:26710", "label": "sodium chloride"},
                "concentration": {"value": "1", "unit": "G_PER_L"},
            }
        ],
        "curation_history": [
            {
                "curator": "sag-import",
                "action": "Imported from SAG Culture Collection",
                "notes": f"Source ID: Test, PDF URL: {pdf_url}",
            }
        ],
        "references": [
            {"reference": "SAG:Test"},
            {"reference": pdf_url},
        ],
    }


def test_repair_adds_structured_sag_source(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(Path("algae/test_medium.yaml"), _doc())

    assert repaired["sources"] == [
        {
            "database": "SAG",
            "database_id": "Test",
            "url": "http://sagdb.uni-goettingen.de/culture_media/Test Medium.pdf",
        }
    ]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([("algae/test_medium.yaml", repaired)]) == []


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.repair_record(Path("algae/test_medium.yaml"), _doc())
    twice = repair_module.repair_record(Path("algae/test_medium.yaml"), once)

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


def test_plan_repairs_finds_current_sag_cohort(repair_module) -> None:
    plans = repair_module.plan_repairs()

    assert len(plans) == repair_module.EXPECTED_TARGET_COUNT
    assert repair_module.NORMALIZED / "algae" / "artificial_seawater.yaml" in plans


def test_repair_rejects_mismatched_pdf(repair_module) -> None:
    doc = _doc()
    doc["references"][1]["reference"] = (
        "http://sagdb.uni-goettingen.de/culture_media/Other Medium.pdf"
    )

    with pytest.raises(ValueError, match="does not match sag-import"):
        repair_module.repair_record(Path("algae/test_medium.yaml"), doc)


def test_repair_rejects_missing_sag_import(repair_module) -> None:
    doc = _doc()
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="expected one sag-import"):
        repair_module.repair_record(Path("algae/test_medium.yaml"), doc)
