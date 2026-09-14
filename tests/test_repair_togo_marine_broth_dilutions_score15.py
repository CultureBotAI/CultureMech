from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_marine_broth_dilutions_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_marine_broth_dilutions_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(
        SCORER,
        "score_review_need_for_togo_marine_broth_dilutions",
    )


def _row(component: tuple[str, str, str]) -> dict:
    preferred_term, value, unit = component
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "notes": "imported",
    }


def _doc(target) -> dict:
    doc = {
        "id": target.record_id,
        "name": Path(target.path).stem,
        "original_name": Path(target.path).stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [_row(row) for row in target.ingredient_signature],
        "media_term": {
            "preferred_term": target.source_term,
            "term": {"id": target.source_term, "label": target.source_term},
        },
        "notes": "Source: TOGO",
        "curation_history": [],
    }
    if target.solution_signature:
        doc["solutions"] = [
            {
                **_row(row),
                "composition": [],
                "name": "Unknown solution",
            }
            for row in target.solution_signature
        ]
    return doc


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for row in doc["ingredients"]:
        if row["preferred_term"] == preferred_term:
            return row
    raise AssertionError(f"missing ingredient {preferred_term!r}")


def test_repairs_ground_agar_and_clear_review_need(repair_module, scorer_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)

        agar = _ingredient(repaired, target.agar_preferred_term)
        agar_value, agar_unit = next(
            (value, unit)
            for preferred_term, value, unit in target.ingredient_signature
            if preferred_term == target.agar_preferred_term
        )
        assert agar == {
            "preferred_term": target.agar_preferred_term,
            "concentration": {"value": agar_value, "unit": agar_unit},
            "source": target.source_label,
            "notes": (
                f"Role: Solidifying component; {target.source_label} lists "
                "agar only as an optional solidifying agent."
            ),
            "term": {"id": "CHEBI:2509", "label": "agar"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:2509", "label": "agar"},
        }
        assert scorer_module.score_parsed([(target.path, repaired)]) == []

        score, reasons = scorer_module.score_record(repaired)
        if target.ph_value is None:
            assert (score, reasons) == (5, ["no pH and no temperature"])
        else:
            assert (score, reasons) == (0, [])


def test_bacto_marine_broth_and_seawater_stay_unmapped(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/1_10_mb_agar.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    artificial_seawater = _ingredient(repaired, "Artificial seawater")
    commercial_broth = _ingredient(repaired, "Bacto Marine Broth 2216 (Difco)")

    assert "term" not in artificial_seawater
    assert "mediaingredientmech_chebi_term" not in artificial_seawater
    assert "term" not in commercial_broth
    assert "mediaingredientmech_chebi_term" not in commercial_broth
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_numeric_ph_is_added_only_when_togo_lists_one(repair_module) -> None:
    by_path = repair_module.TARGET_BY_PATH

    with_ph = repair_module.repair_record(
        _doc(by_path["bacterial/1_5_marine_agar_broth.yaml"]),
        by_path["bacterial/1_5_marine_agar_broth.yaml"],
    )
    without_ph = repair_module.repair_record(
        _doc(by_path["bacterial/1_2_marine_broth_agar.yaml"]),
        by_path["bacterial/1_2_marine_broth_agar.yaml"],
    )

    assert with_ph["ph_value"] == 7.6
    assert "ph_value" not in without_ph


def test_repair_adds_references_and_history(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/1_10_marine_broth_agar.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["references"] == [
        {"reference": url} for url in target.reference_urls
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": "; ".join(target.reference_urls),
            "notes": target.notes,
        }
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    for target in repair_module.TARGETS:
        path = tmp_path / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert {
        path.relative_to(tmp_path): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(tmp_path): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/1_10_marine_broth_agar.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/1_10_marine_broth_agar.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/1_10_marine_broth_agar.yaml"]
    doc = _doc(target)
    doc["ingredients"][1]["concentration"]["value"] = "15.5"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_reviewed_inputs(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load(
            (repair_module.NORMALIZED / target.path).read_text(encoding="utf-8")
        )

        assert doc["id"] == target.record_id
        assert (
            repair_module._component_signature(doc.get("ingredients"), "ingredients")
            == target.ingredient_signature
        )
        assert (
            repair_module._component_signature(doc.get("solutions") or [], "solutions")
            == target.solution_signature
        )
