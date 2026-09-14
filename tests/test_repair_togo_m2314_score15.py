from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2314_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2314_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2314")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "lb_medium",
        "original_name": "LB medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2314",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "LB medium",
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "references": [
            {
                "reference": "PMID:16628448",
                "year": 2006,
                "notes": "Existing growth evidence.",
            },
            {
                "reference": "NCBI:GCF_000005845.2",
                "notes": "Existing genome evidence.",
            },
        ],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:74",
        "organism_culture_type": "isolate",
        "target_organisms": [
            {
                "preferred_term": "Escherichia coli K-12 MG1655",
                "term": {
                    "id": "NCBITaxon:511145",
                    "label": "Escherichia coli str. K-12 substr. MG1655",
                },
                "evidence": [
                    {
                        "reference": "PMID:16628448",
                        "supports": "SUPPORT",
                        "explanation": "Existing organism-medium evidence.",
                    },
                ],
            },
        ],
        "variant_children": [
            {
                "path": "data/normalized_yaml/bacterial/lb_0_1x.yaml",
                "relationship": "CONCENTRATION_VARIANT",
                "id": "CultureMech:015465",
                "name": "LB_0.1x",
            },
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_grounds_all_lb_miller_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.INGREDIENT_SIGNATURE
    assert ingredients["Tryptone"]["term"] == {
        "id": "MICRO:0000182",
        "label": "tryptone",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Sodium chloride"]["term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert ingredients["Sodium chloride"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }


def test_repair_preserves_growth_evidence_and_variant_child(
    repair_module,
) -> None:
    doc = _doc(repair_module)
    repaired = repair_module.repair_record(doc)

    assert repaired["kg_microbe_match"] == doc["kg_microbe_match"]
    assert repaired["organism_culture_type"] == doc["organism_culture_type"]
    assert repaired["target_organisms"] == doc["target_organisms"]
    assert repaired["variant_children"] == doc["variant_children"]


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [
        {
            "reference": "PMID:16628448",
            "year": 2006,
            "notes": "Existing growth evidence.",
        },
        {
            "reference": "NCBI:GCF_000005845.2",
            "notes": "Existing genome evidence.",
        },
        *[{"reference": url} for url in repair_module.REFERENCES],
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
    assert "Sigma-Aldrich L3522" in matching_events[0]["notes"]


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Peptone", "10.0", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [
        {
            "preferred_term": "LB Broth",
            "concentration": {"value": "1", "unit": "L"},
        }
    ]

    with pytest.raises(ValueError, match="unexpected solutions"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m2314_repair_contract(
    repair_module,
) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") == (
        repair_module.INGREDIENT_SIGNATURE
    )
    assert "solutions" not in doc
