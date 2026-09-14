from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_1007_trace_stock_score15.py"
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
    return _load_script(SCRIPT, "repair_dsmz_1007_trace_stock_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_1007")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target, repair_module) -> dict:
    return {
        "id": target.expected_id,
        "name": Path(target.path).stem,
        "original_name": (
            "DSM 15672" if target.expected_source_term == "komodo.medium:1007.1" else "MINERAL MEDIUM"
        ),
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": target.source_label,
            "term": {
                "id": target.expected_source_term,
                "label": "MINERAL MEDIUM",
            },
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 1007 | DSMZ Medium: 1007 "
            "(mediadive.medium:1007) | Aerobic: No"
        ),
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _solution_by_name(repaired: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in repaired["solutions"]}


def test_repair_nests_trace_elements_stock_and_exits_ranking(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/KOMODO_1007_MINERAL_MEDIUM.yaml"]

    repaired = repair_module.repair_record(_doc(target, repair_module), target)

    assert repaired["ph_range"] == {"min": 5.5, "max": 6.0}
    assert repair_module._ingredient_signature(
        repaired["ingredients"],
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repair_module._solution_signatures(
        repaired["solutions"],
    ) == repair_module.FINAL_SOLUTION_SIGNATURES
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(target.path, repaired)]) == []


def test_repair_grounds_disclosed_main_and_trace_components(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/KOMODO_1007_MINERAL_MEDIUM.yaml"]

    repaired = repair_module.repair_record(_doc(target, repair_module), target)
    main = {row["preferred_term"]: row for row in repaired["ingredients"]}
    trace = {
        row["preferred_term"]: row
        for row in _solution_by_name(repaired)["Trace elements"]["composition"]
    }

    assert main["KNO3"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:63043",
        "label": "potassium nitrate",
    }
    assert trace["NiCl2 x 6 H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }
    assert trace["CoCl2 x 6 H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:53503",
        "label": "cobalt chloride hexahydrate",
    }


def test_repair_keeps_source_duplicate_graph_and_renames_strain_alias(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/dsm_15672.yaml"]

    repaired = repair_module.repair_record(_doc(target, repair_module), target)

    assert repaired["original_name"] == "MINERAL MEDIUM for DSM 15672"
    assert repaired["parent_media"] == {
        "path": repair_module.KOMODO_PARENT_PATH,
        "relationship": "SOURCE_DUPLICATE",
        "id": repair_module.KOMODO_PARENT_ID,
        "name": repair_module.KOMODO_PARENT_NAME,
    }
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_adds_references_flags_preparation_and_single_event(
    repair_module,
) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/mineral_medium.yaml"]
    once = repair_module.repair_record(_doc(target, repair_module), target)
    twice = repair_module.repair_record(once, target)

    assert twice["references"] == [
        {"reference": repair_module.MEDIADIVE_1007},
        {"reference": repair_module.DSMZ_1007_PDF},
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert [step["action"] for step in twice["preparation_steps"]] == [
        "ADJUST_PH",
        "MIX",
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


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    for target in repair_module.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target, repair_module), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(root)
    for repaired_path, doc in first.items():
        repaired_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/KOMODO_1007_MINERAL_MEDIUM.yaml"]
    doc = _doc(target, repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/KOMODO_1007_MINERAL_MEDIUM.yaml"]
    doc = _doc(target, repair_module)
    doc["media_term"]["term"]["id"] = "komodo.medium:1007.1"

    with pytest.raises(ValueError, match=target.expected_source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_imported_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/KOMODO_1007_MINERAL_MEDIUM.yaml"]
    doc = _doc(target, repair_module)
    doc["ingredients"][0] = _ingredient("KNO3", "0.5", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_final_solution_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/KOMODO_1007_MINERAL_MEDIUM.yaml"]
    doc = repair_module.repair_record(_doc(target, repair_module), target)
    doc["solutions"][0]["composition"][0]["concentration"]["value"] = "6.00"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_dsmz_1007_repair_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.expected_id
        assert repair_module._source_term_id(doc) == target.expected_source_term
        signatures = (
            repair_module._ingredient_signature(doc["ingredients"]),
            repair_module._solution_signatures(doc.get("solutions")),
        )
        assert signatures in {
            (
                repair_module.IMPORTED_INGREDIENT_SIGNATURE,
                (),
            ),
            (
                repair_module.FINAL_INGREDIENT_SIGNATURE,
                repair_module.FINAL_SOLUTION_SIGNATURES,
            ),
        }
