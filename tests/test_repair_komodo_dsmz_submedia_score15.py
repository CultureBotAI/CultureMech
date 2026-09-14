from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_dsmz_submedia_score15.py"
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
    return _load_script(SCRIPT, "repair_komodo_dsmz_submedia_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_dsmz_submedia")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.expected_id,
        "name": Path(target.path).stem,
        "original_name": target.title,
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": target.ph_value,
        "notes": (
            f"pH buffer: {target.ph_adjuster} | Source: KOMODO ModelSEED | "
            f"DSMZ Medium: {target.expected_media_term.removeprefix('komodo.medium:')}"
        ),
        "media_term": {
            "preferred_term": "KOMODO Medium",
            "term": {"id": target.expected_media_term, "label": target.title},
        },
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_signature
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_expands_all_three_submedia_and_exits_ranking(
    repair_module,
    scorer_module,
) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)

        assert repaired["ph_value"] == target.ph_value
        assert repair_module._ingredient_signature(repaired["ingredients"]) == (
            target.final_signature
        )
        assert scorer_module.score_record(repaired) == (0, [])
        assert scorer_module.score_parsed([(target.path, repaired)]) == []


def test_solution_a_1003_keeps_magnesium_chloride_monohydrate(
    repair_module,
) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/solution_a_medium_1003.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["MgCl2 x H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:86355",
        "label": "magnesium dichloride monohydrate",
    }
    assert ingredients["HCl"]["concentration"] == {"value": "variable", "unit": "VARIABLE"}


def test_solution_a_1145_keeps_magnesium_chloride_hexahydrate(
    repair_module,
) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/solution_a_medium_1145.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["MgCl2 x 6 H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    }
    assert ingredients["CaCl2 x 2 H2O"]["concentration"] == {
        "value": "40.00",
        "unit": "G_PER_L",
    }


def test_growth_factors_829_are_grounded_and_autoclaved(
    repair_module,
) -> None:
    target = repair_module.TARGET_BY_PATH[
        "bacterial/solution_of_growth_stimulating_factors_medium_829.yaml"
    ]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["3-Methylbutyric acid"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:28484",
        "label": "isovaleric acid",
    }
    assert ingredients["NaOH"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32145",
        "label": "sodium hydroxide",
    }
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "ADJUST_PH",
        "AUTOCLAVE",
    ]


def test_repair_adds_references_flags_and_single_event(
    repair_module,
) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/solution_a_medium_1003.yaml"]

    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert twice["references"] == [{"reference": url} for url in target.references]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "mediadive.solution:2047" in matching_events[0]["notes"]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    for target in repair_module.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(root)
    for repaired_path, doc in first.items():
        repaired_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(root): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/solution_a_medium_1003.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/solution_a_medium_1003.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "komodo.medium:2026"

    with pytest.raises(ValueError, match=target.expected_media_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_imported_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/solution_a_medium_1003.yaml"]
    doc = _doc(target)
    doc["ingredients"][0] = _ingredient("NaOH", "variable", "VARIABLE")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_final_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/solution_a_medium_1003.yaml"]
    doc = repair_module.repair_record(_doc(target), target)
    doc["ingredients"][0]["concentration"]["value"] = "50.00"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_komodo_dsmz_submedia_repair_contract(
    repair_module,
) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.expected_id
        assert repair_module._source_term_id(doc) == target.expected_media_term
        assert repair_module._ingredient_signature(doc["ingredients"]) in (
            target.imported_signature,
            target.final_signature,
        )
