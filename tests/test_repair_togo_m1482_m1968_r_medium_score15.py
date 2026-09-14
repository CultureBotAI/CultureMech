from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1482_m1968_r_medium_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1482_m1968_r_medium")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1482_m1968")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": target.path.stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {target.media_term.removeprefix('TOGO:')}",
            "term": {"id": target.media_term, "label": target.path.stem},
        },
        "notes": "Source: NBRC",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_base_corrects_water_adds_ph_and_grounds_components(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.BASE_TARGET),
        repair_module.BASE_TARGET,
    )
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.BASE_FINAL
    assert repaired["ph_value"] == 7.0
    assert "ph_range" not in repaired
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Bacto Casamino Acids (Difco)"]["term"] == {
        "id": "FOODON:03315719",
        "label": "mammalian milk protein (hydrolyzed)",
    }
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }
    assert ingredients["Malt extract"]["term"] == {
        "id": "FOODON:03301056",
        "label": "malt extract",
    }
    assert ingredients["MgSO4 x 7 H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_child_adds_nacl_and_salinity_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.CHILD_TARGET),
        repair_module.CHILD_TARGET,
    )
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.CHILD_FINAL
    assert ingredients["NaCl"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert ingredients["NaCl"]["physicochemical_roles"] == ["OSMOTIC_AGENT"]
    assert repaired["ph_value"] == 7.0
    assert repaired["parent_media"] == repair_module.PARENT_MEDIA
    assert repaired["variant_relationship"] == "SALINITY_VARIANT"
    assert repaired["variant_modifications"] == [
        repair_module.CHILD_VARIANT_NOTES,
    ]
    assert scorer_module.score_parsed([(str(repair_module.CHILD), repaired)]) == []


def test_repair_adds_preparation_references_and_events_once(repair_module) -> None:
    once = repair_module.repair_record(
        _doc(repair_module.BASE_TARGET),
        repair_module.BASE_TARGET,
    )
    twice = repair_module.repair_record(once, repair_module.BASE_TARGET)

    assert twice["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert twice["references"] == [
        {"reference": reference}
        for reference in repair_module.BASE_TARGET.references
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION_M1482
        )
    ]
    link_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert len(matching_events) == 1
    assert len(link_events) == 1


def test_base_link_to_child_is_reciprocal_and_idempotent(repair_module) -> None:
    once = repair_module.repair_record(
        _doc(repair_module.BASE_TARGET),
        repair_module.BASE_TARGET,
    )
    twice = repair_module.repair_record(once, repair_module.BASE_TARGET)

    assert twice["variant_children"] == [repair_module.CHILD_REFERENCE]


def test_plan_repairs_targets_the_r_medium_pair(repair_module) -> None:
    plans = repair_module.plan_repairs()

    assert set(plans) == {
        repair_module.NORMALIZED / repair_module.PARENT,
        repair_module.NORMALIZED / repair_module.CHILD,
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module.BASE_TARGET)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:008026"):
        repair_module.repair_record(doc, repair_module.BASE_TARGET)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module.CHILD_TARGET)
    doc["media_term"]["term"]["id"] = "TOGO:M1482"

    with pytest.raises(ValueError, match="expected media term TOGO:M1968"):
        repair_module.repair_record(doc, repair_module.CHILD_TARGET)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module.BASE_TARGET)
    doc["ingredients"][0] = _ingredient("Water", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, repair_module.BASE_TARGET)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module.BASE_TARGET)
    doc["solutions"] = [{"preferred_term": "Unexpected stock"}]

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, repair_module.BASE_TARGET)


def test_corpus_records_match_repair_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.record_id
        assert repair_module._source_term_id(doc) == target.media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in (
            target.imported_signature,
            target.final_signature,
        )
        assert "solutions" not in doc
