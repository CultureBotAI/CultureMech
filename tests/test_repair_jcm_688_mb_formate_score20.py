from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_688_mb_formate_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm_688_mb_formate")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_688")


def _doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "mb_medium_with_formate",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium J688",
            "term": {
                "id": repair.EXPECTED_SOURCE_TERM,
                "label": "MB MEDIUM WITH FORMATE",
            },
        },
        "notes": "Source: JCM",
        "ingredients": [
            {
                "preferred_term": "Sodium formate",
                "term": {"id": "CHEBI:62965", "label": "sodium formate"},
                "concentration": {"value": "136", "unit": "G_PER_L"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:62965",
                    "label": "sodium formate",
                },
            }
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Use Medium No. 687, replacing Methanol solution with "
                    "Sodium formate solution (see below)."
                ),
            }
        ],
        "curation_history": [],
    }


def _by_name(rows: list[dict], preferred_term: str) -> dict:
    for row in rows:
        if row["preferred_term"] == preferred_term:
            return row
    raise AssertionError(f"missing {preferred_term!r}")


def _solutions(doc: dict) -> dict[str, dict]:
    return {solution["preferred_term"]: solution for solution in doc["solutions"]}


def test_repair_expands_m708_solution_a_and_stocks(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "Distilled water",
        "Yeast extract",
        "NaCl",
        "CaCl2 x 2H2O",
        "NH4Cl",
        "K2HPO4",
        "Resazurin",
        "MgCl2 x 6H2O",
        "KCl",
        "NaHCO3",
        "Trypticase peptone",
        "CO2",
        "N2",
    ]
    assert _by_name(repaired["ingredients"], "Distilled water")["concentration"] == {
        "value": "920",
        "unit": "ML_PER_L",
    }
    assert _by_name(repaired["ingredients"], "Resazurin")["concentration"] == {
        "value": "0.0005",
        "unit": "G_PER_L",
    }
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_repair_adds_togo_cross_referenced_stock_compositions(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _solutions(repaired)

    assert solutions["Trace minerals (TOGO Medium M142)"]["concentration"] == {
        "value": "10",
        "unit": "ML_PER_L",
    }
    assert _by_name(
        solutions["Trace minerals (TOGO Medium M142)"]["composition"],
        "MgSO4 x 7H2O",
    )[
        "concentration"
    ] == {"value": "3", "unit": "G_PER_L"}
    assert _by_name(
        solutions["Selenite--tungstate solution (TOGO Medium M431)"]["composition"],
        "Na2WO4 x 2H2O",
    )["concentration"] == {"value": "0.008", "unit": "G_PER_L"}
    assert _by_name(
        solutions["Trace vitamins (TOGO Medium M190)"]["composition"],
        "Vitamin B12",
    )[
        "concentration"
    ] == {"value": "0.0001", "unit": "G_PER_L"}


def test_repair_preserves_direct_m708_sterile_stock_compositions(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _solutions(repaired)

    assert _by_name(
        solutions["5% Na2S x 9H2O solution"]["composition"],
        "Na2S x 9H2O",
    )[
        "concentration"
    ] == {"value": "50", "unit": "G_PER_L"}
    assert _by_name(
        solutions["5% L-Cysteine x HCl x H2O solution"]["composition"],
        "L-Cysteine x HCl x H2O",
    )["concentration"] == {"value": "50", "unit": "G_PER_L"}
    assert solutions["Sodium formate solution"]["concentration"] == {
        "value": "50",
        "unit": "ML_PER_L",
    }
    assert _by_name(
        solutions["Sodium formate solution"]["composition"],
        "Sodium formate",
    )[
        "concentration"
    ] == {"value": "136", "unit": "G_PER_L"}


def test_repair_adds_references_and_history_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert once["references"] == [
        {"reference": repair_module.JCM_688},
        {"reference": repair_module.TOGO_M708},
        {"reference": repair_module.TOGO_M142},
        {"reference": repair_module.TOGO_M190},
        {"reference": repair_module.TOGO_M431},
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
    assert matching_events[0]["source"] == repair_module.TOGO_M708


def test_plan_repair_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    path = root / repair_module.PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_doc(repair_module), sort_keys=False))

    first = repair_module.plan_repair(root)
    for repaired_path, doc in first.items():
        repaired_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repair(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(root): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M708"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_SOURCE_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="ingredient list drifted"):
        repair_module.repair_record(doc)
