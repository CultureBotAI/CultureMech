from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1418_m1424_m1678_m1896_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1418_m1424_m1678_m1896_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1418_m1424")


def _row(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    doc = {
        "id": target.record_id,
        "name": target.path.stem,
        "original_name": target.title,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _row(name, value, unit)
            for name, value, unit in target.imported_ingredient_signature
        ],
        "media_term": {
            "preferred_term": target.source_term.replace(":", " "),
            "term": {"id": target.source_term, "label": target.title},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }
    if target.imported_solution_signature:
        doc["solutions"] = [
            {
                "preferred_term": name,
                "composition": [],
                "concentration": {"value": value, "unit": unit},
                "name": "Unknown solution",
            }
            for name, value, unit in target.imported_solution_signature
        ]
    return doc


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


@pytest.mark.parametrize("target_index", [0, 1, 2, 3])
def test_repair_restores_official_nbrc_formulas(
    repair_module,
    scorer_module,
    target_index,
) -> None:
    target = repair_module.TARGETS[target_index]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        target.final_ingredient_signature
    )
    assert "solutions" not in repaired
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


def test_m1418_corrects_v8_seawater_formula(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["ph_value"] == 7.0
    assert ingredients["Vegetable juice"]["concentration"] == {
        "value": "200",
        "unit": "ML_PER_L",
    }
    assert ingredients["Seawater (2% salinity)"]["concentration"] == {
        "value": "800",
        "unit": "ML_PER_L",
    }
    assert ingredients["CaCO3"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:3311",
        "label": "calcium carbonate",
    }
    assert "term" not in ingredients["Vegetable juice"]
    assert repaired["preparation_steps"][1]["action"] == "FILTER"


def test_m1424_flattens_tys_peptone_and_grounds_yeast(repair_module) -> None:
    target = repair_module.TARGETS[1]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert "ph_value" not in repaired
    assert ingredients["Seawater (2% salinity)"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Yeast extract"]
    assert (
        "term"
        not in ingredients["Trypticase Peptone (BBL) or Hipolypepton"]
    )


def test_m1678_flattens_tsb_na2co3_and_adds_alkaline_ph(repair_module) -> None:
    target = repair_module.TARGETS[2]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["ph_value"] == 8.5
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Na2CO3"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:29377",
        "label": "sodium carbonate",
    }
    assert ingredients["Na2CO3"]["physicochemical_roles"] == ["BUFFER"]
    assert "term" not in ingredients["Bacto Tryptic Soy Broth"]
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "AUTOCLAVE",
        "MIX",
    ]


def test_m1896_corrects_distilled_water_and_keeps_difco_opaque(
    repair_module,
) -> None:
    target = repair_module.TARGETS[3]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Agar (if needed)"]["physicochemical_roles"] == [
        "SOLIDIFYING_AGENT"
    ]
    assert "term" not in ingredients["ISP Medium 1 (Difco)"]


def test_repair_adds_flags_references_and_events_once(repair_module) -> None:
    target = repair_module.TARGETS[2]
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert once["references"] == [
        {"reference": reference} for reference in target.references
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == "; ".join(target.references)


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M1417"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[1]
    doc = _doc(target)
    doc["ingredients"][0] = _row("Soy peptone", "1", "G_PER_L")

    with pytest.raises(ValueError, match="component signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGETS[2]
    doc = _doc(target)
    doc["solutions"][0]["preferred_term"] = "Na2CO3"

    with pytest.raises(ValueError, match="component signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_mixed_final_ingredients_with_stale_solutions(
    repair_module,
) -> None:
    target = repair_module.TARGETS[2]
    doc = _doc(target)
    doc["ingredients"] = [
        _row(name, value, unit)
        for name, value, unit in target.final_ingredient_signature
    ]

    with pytest.raises(ValueError, match="component signature drifted"):
        repair_module.repair_record(doc, target)


@pytest.mark.parametrize("target_index", [0, 1, 2, 3])
def test_target_records_match_repair_contract(repair_module, target_index) -> None:
    target = repair_module.TARGETS[target_index]
    doc = yaml.safe_load((repair_module.NORMALIZED / target.path).read_text())

    assert doc["id"] == target.record_id
    assert repair_module._source_term_id(doc) == target.source_term
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        target.imported_ingredient_signature,
        target.final_ingredient_signature,
    )
    assert repair_module._signature(doc.get("solutions"), "solutions") in (
        target.imported_solution_signature,
        (),
    )
