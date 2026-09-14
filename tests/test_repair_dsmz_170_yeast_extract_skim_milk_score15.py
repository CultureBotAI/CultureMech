from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_170_yeast_extract_skim_milk_score15.py"
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
    return _load_script(SCRIPT, "repair_dsmz_170_yeast_extract_skim_milk")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_170")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module, target) -> dict:
    return {
        "id": repair_module.EXPECTED_IDS[target.path],
        "name": Path(target.path).stem,
        "original_name": target.original_name,
        "category": target.path.split("/", 1)[0],
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": repair_module.EXPECTED_SOURCE_TERMS[target.path],
            "term": {
                "id": repair_module.EXPECTED_SOURCE_TERMS[target.path],
                "label": target.original_name,
            },
        },
        "notes": "Source: DSMZ Medium 170",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_restores_dsmz_170_formula_for_both_records(
    repair_module,
    scorer_module,
) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, target), target)

        assert repaired["medium_type"] == "COMPLEX"
        assert repaired["composition_type"] == "UNDEFINED"
        assert repaired["physical_state"] == "SOLID_AGAR"
        assert (
            repair_module._signature(repaired["ingredients"], "ingredients")
            == repair_module.FINAL_INGREDIENT_SIGNATURE
        )
        assert "kg_microbe_match" not in repaired
        assert repaired["preparation_steps"] == [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Mix 10.0 g Skim milk (Difco), 1.0 g yeast extract, "
                    "15.0 g agar, and 1000.0 ml distilled water."
                ),
            }
        ]
        assert scorer_module.score_parsed([(target.path, repaired)]) == []


def test_repair_keeps_difco_skim_milk_opaque(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[0]),
        repair_module.TARGETS[0],
    )

    assert _by_name(repaired["ingredients"])["Skim milk (Difco)"] == {
        "preferred_term": "Skim milk (Difco)",
        "concentration": {"value": "10.0", "unit": "G_PER_L"},
        "source": repair_module.SOURCE,
        "notes": (
            "DSMZ Medium 170 lists 10.0 g/L Skim milk from Difco; the "
            "commercial milk product is retained as an opaque component."
        ),
    }
    assert "has_unmapped_ingredients" in repaired["data_quality_flags"]


def test_repair_grounds_yeast_extract_agar_and_water(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[0]),
        repair_module.TARGETS[0],
    )
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Yeast extract"]
    assert ingredients["Yeast extract"]["nutritional_roles"] == ["PROTEIN_SOURCE"]
    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Agar"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[0]),
        repair_module.TARGETS[0],
    )
    twice = repair_module.repair_record(once, repair_module.TARGETS[0])

    assert twice["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
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
    assert "Removed a false kg_microbe_match" in (
        matching_events[0]["notes"]
    )


def test_plan_repairs_targets_both_records(repair_module) -> None:
    assert repair_module.plan_repairs() == {
        repair_module.NORMALIZED / target.path: repair_module.repair_record(
            yaml.safe_load(
                (repair_module.NORMALIZED / target.path).read_text(
                    encoding="utf-8"
                )
            ),
            target,
        )
        for target in repair_module.TARGETS
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_IDS[target.path]):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:171"

    with pytest.raises(
        ValueError,
        match=repair_module.EXPECTED_SOURCE_TERMS[target.path],
    ):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0] = _ingredient("Skimmed milk", "10", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)
