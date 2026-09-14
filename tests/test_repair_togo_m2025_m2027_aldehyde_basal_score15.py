from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2025_m2027_aldehyde_basal_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2025_m2027")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2025_m2027")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
        "name": "Unknown solution",
    }


def _doc(repair_module, spec) -> dict:
    return {
        "id": spec.expected_id,
        "name": spec.path.stem,
        "original_name": spec.title,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {spec.media_term[5:]}",
            "term": {
                "id": spec.media_term,
                "label": spec.title,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _composition in spec.imported_solutions
        ],
        "variant_relationship": "SOURCE_DUPLICATE",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_all_three_aldehyde_media(repair_module) -> None:
    for spec in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, spec), spec)

        assert repaired["composition_type"] == "SEMI_DEFINED"
        assert repaired["ph_value"] == 7.0
        assert "solutions" not in repaired
        assert "variant_relationship" not in repaired
        assert repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        ) == repair_module.final_ingredient_signature(spec)


def test_repair_grounds_aldehydes_as_ml_per_l_components(repair_module) -> None:
    expected = {
        "Acetaldehyde**": ("1.0", "CHEBI:15343", "acetaldehyde"),
        "Benzaldehyde**": ("0.5", "CHEBI:17169", "benzaldehyde"),
        "Formaldehyde**": ("0.5", "CHEBI:16842", "formaldehyde"),
    }

    for spec in repair_module.TARGETS:
        ingredients = _by_name(
            repair_module.repair_record(_doc(repair_module, spec), spec)["ingredients"]
        )
        value, chebi_id, label = expected[spec.aldehyde]

        assert ingredients[spec.aldehyde]["concentration"] == {
            "value": value,
            "unit": "ML_PER_L",
        }
        assert ingredients[spec.aldehyde]["term"] == {
            "id": chebi_id,
            "label": label,
        }


def test_repair_keeps_hipolypepton_opaque(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[0]),
        repair_module.TARGETS[0],
    )
    hipolypepton = _by_name(repaired["ingredients"])["Hipolypepton*"]

    assert hipolypepton["concentration"] == {"value": "10.0", "unit": "G_PER_L"}
    assert "term" not in hipolypepton
    assert "Wako Pure Chemical Industries" in hipolypepton["notes"]


def test_repair_adds_only_filter_sterilization_step(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[2]),
        repair_module.TARGETS[2],
    )

    assert "temperature_value" not in repaired
    assert "sterilization" not in repaired
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "FILTER_STERILIZE",
            "description": "Sterilize Formaldehyde separately by filtration.",
        }
    ]


def test_repair_records_drop_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    records = []
    for spec in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, spec), spec)
        assert scorer_module.score_record(repaired) == (0, [])
        records.append((str(spec.path), repaired))

    assert scorer_module.score_parsed(records) == []


def test_repair_adds_record_specific_references_once(repair_module) -> None:
    spec = repair_module.TARGETS[1]

    once = repair_module.repair_record(_doc(repair_module, spec), spec)
    twice = repair_module.repair_record(once, spec)

    assert twice["references"] == [{"reference": url} for url in spec.references]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert spec.aldehyde[:-2] in matching_events[0]["notes"]


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    spec = repair_module.TARGETS[0]
    doc = _doc(repair_module, spec)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id"):
        repair_module.repair_record(doc, spec)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    spec = repair_module.TARGETS[0]
    doc = _doc(repair_module, spec)
    doc["solutions"][0]["preferred_term"] = "Acetate"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, spec)


def test_script_is_idempotent_on_dumped_yaml(tmp_path: Path, repair_module) -> None:
    normalized = tmp_path / "normalized"
    for spec in repair_module.TARGETS:
        target = normalized / spec.path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(yaml.safe_dump(_doc(repair_module, spec), sort_keys=False))

    first = repair_module.plan_repairs(normalized)
    for target, doc in first.items():
        target.write_text(yaml.safe_dump(doc, sort_keys=False))

    second = repair_module.plan_repairs(normalized)

    assert second == first
