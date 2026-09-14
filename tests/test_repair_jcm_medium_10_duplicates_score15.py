from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_medium_10_duplicates_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_medium_10_duplicates_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_medium_10")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [],
    }


def _media_term(identifier: str, label: str) -> dict:
    return {"preferred_term": identifier, "term": {"id": identifier, "label": label}}


def _jcm_doc(target) -> dict:
    return {
        "id": target.expected_id,
        "name": target.path.stem,
        "original_name": target.original_name,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": _media_term(target.expected_media_term, target.original_name),
        "notes": "Source: JCM",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.current_ingredient_signature
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "ADJUST_PH",
                "description": "Adjust pH to 6.7--6.8.",
            }
        ],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in target.current_solution_signatures
        ],
    }


def _parent_doc(target) -> dict:
    togo = target.togo_module
    return {
        "id": togo.EXPECTED_ID,
        "name": target.path.stem,
        "original_name": togo.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": target.physical_state,
        "media_term": _media_term(togo.EXPECTED_MEDIA_TERM, togo.TITLE),
        "notes": "Source: TOGO",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in togo.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in togo.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _write_minimal_tree(repair_module, root: Path) -> None:
    for target in repair_module.TARGETS:
        for path, doc in (
            (target.path, _jcm_doc(target)),
            (target.parent_path, _parent_doc(target)),
        ):
            full_path = root / path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(
                yaml.safe_dump(doc, sort_keys=False),
                encoding="utf-8",
            )


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_medium_10_j179_mirrors_togo_m172(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_jcm_record(_jcm_doc(target), target)

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_range"] == {"min": 6.7, "max": 6.8}
    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == target.togo_module.FINAL_INGREDIENT_SIGNATURE
    assert repair_module._solution_signatures(
        repaired,
    ) == target.togo_module.FINAL_SOLUTION_SIGNATURES
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_modified_medium_10_j210_becomes_solid_agar(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[1]
    repaired = repair_module.repair_jcm_record(_jcm_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert solutions["1.0% Hemin solution"]["composition"][0][
        "mediaingredientmech_chebi_term"
    ] == {"id": "CHEBI:50385", "label": "hemin"}
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_grounds_jcm_stock_components(repair_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_jcm_record(_jcm_doc(target), target)
        ingredients = _by_name(repaired["ingredients"])
        solutions = _by_name(repaired["solutions"])

        assert ingredients["Soluble starch"]["mediaingredientmech_chebi_term"] == {
            "id": "CHEBI:28017",
            "label": "starch",
        }
        assert ingredients["Yeast extract (BD-Difco)"]["term"] == {
            "id": "FOODON:03315426",
            "label": "yeast extract",
        }
        assert ingredients["Trypticase peptone (BD-BBL)"]["term"] == {
            "id": "MICRO:0000175",
            "label": "Trypticase peptone",
        }
        assert solutions["4% Na2SO3 solution"]["composition"][0][
            "mediaingredientmech_chebi_term"
        ] == {"id": "CHEBI:86477", "label": "sodium sulfite"}
        assert solutions["25% L--Ascorbic acid solution"]["composition"][0][
            "concentration"
        ] == {"value": "25.0", "unit": "PERCENT_W_V"}
        assert solutions["VFA solution (see Medium [M124])"]["composition"] == []


def test_plan_repairs_links_jcm_duplicates_to_togo_parents(
    repair_module,
    tmp_path: Path,
) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    plans = repair_module.plan_repairs(root)

    for target in repair_module.TARGETS:
        parent = plans[root / target.parent_path]
        child = plans[root / target.path]

        assert child["parent_media"] == {
            "path": f"data/normalized_yaml/{target.parent_path.as_posix()}",
            "relationship": "SOURCE_DUPLICATE",
            "notes": target.source_duplicate_note,
            "id": target.togo_module.EXPECTED_ID,
            "name": target.path.stem,
        }
        assert child["variant_relationship"] == "SOURCE_DUPLICATE"
        assert child["variant_modifications"] == [target.variant_modification]
        assert {
            "path": f"data/normalized_yaml/{target.path.as_posix()}",
            "relationship": "SOURCE_DUPLICATE",
            "notes": target.source_duplicate_note,
            "id": target.expected_id,
            "name": target.path.stem,
        } in parent["variant_children"]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    first = repair_module.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    assert repair_module.plan_repairs(root) == {}


def test_repair_adds_references_and_event_once(repair_module) -> None:
    target = repair_module.TARGETS[0]
    once = repair_module.repair_jcm_record(_jcm_doc(target), target)
    twice = repair_module.repair_jcm_record(once, target)

    assert twice["references"] == [
        {"reference": url} for url in target.togo_module.REFERENCES
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
    assert "represented simple concentration stocks" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _jcm_doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_jcm_record(doc, target)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[1]
    doc = _jcm_doc(target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J9999"

    with pytest.raises(ValueError, match=target.expected_media_term):
        repair_module.repair_jcm_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _jcm_doc(target)
    doc["ingredients"][0] = _ingredient("Water", "850", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_jcm_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGETS[1]
    doc = _jcm_doc(target)
    doc["solutions"][1] = _solution("0.2% Hemin solution", "0.5", "ML_PER_L")

    with pytest.raises(ValueError, match="solution signatures drifted"):
        repair_module.repair_jcm_record(doc, target)


def test_target_records_match_jcm_medium_10_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.expected_id
        assert repair_module._source_term_id(doc) == target.expected_media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in (
            target.current_ingredient_signature,
            target.togo_module.FINAL_INGREDIENT_SIGNATURE,
        )
        assert repair_module._solution_signatures(doc) in (
            target.current_solution_signatures,
            target.togo_module.FINAL_SOLUTION_SIGNATURES,
        )
