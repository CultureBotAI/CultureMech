from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_806_gs_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_806_gs_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_806_gs")


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "gs_medium",
        "original_name": "GS MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium J806",
            "term": {
                "id": repair_module.EXPECTED_SOURCE_TERM,
                "label": "GS MEDIUM",
            },
        },
        "notes": "JCM 806",
        "ingredients": [
            {
                "preferred_term": preferred_term,
                "concentration": {"value": value, "unit": unit},
            }
            for preferred_term, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "solutions": [
            {
                "preferred_term": preferred_term,
                "composition": [],
                "concentration": {"value": value, "unit": unit},
            }
            for preferred_term, value, unit in repair_module.IMPORTED_SOLUTION_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": ["resolved_reference"],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_leaves_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_parsed([(repair_module.TARGET, repaired)]) == []


def test_repair_removes_gases_from_ingredients(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert {row["preferred_term"] for row in repaired["ingredients"]} == {
        "KCl",
        "MgCl2 x 6H2O",
        "MgSO4 x 7H2O",
        "NH4Cl",
        "CaCl2 x 2H2O",
        "KH2PO4",
        "NaCl",
        "Fe(NH4)2(SO4)2 x 6H2O",
        "NaHCO3",
        "Glucose",
        "Yeast extract (BD-Difco)",
        "Trypticase peptone (BD-BBL)",
        "Resazurin",
        "Distilled water",
    }


def test_repair_applies_jcm_806_and_262_overrides(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["NaCl"]["concentration"] == {"value": "6.0", "unit": "G_PER_L"}
    assert ingredients["Glucose"]["concentration"] == {
        "value": "1.8",
        "unit": "G_PER_L",
    }
    assert "Sodium acetate" not in ingredients


def test_repair_inlines_wolfes_mineral_solution(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    wolfes = _by_name(repaired["solutions"])["Wolfe's mineral solution"]

    assert [row["preferred_term"] for row in wolfes["composition"]] == [
        "Trace minerals (JCM Medium 151)",
        "NiCl2 x 6H2O",
        "Na2SeO3",
        "Na2WO4 x 2H2O",
    ]
    assert wolfes["composition"][2]["term"] == {
        "id": "CHEBI:48843",
        "label": "disodium selenite",
    }
    assert wolfes["composition"][3]["term"] == {
        "id": "CHEBI:63939",
        "label": "sodium tungstate dihydrate",
    }


def test_repair_inlines_reducing_agent_percent_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert solutions["5% L-Cysteine HCl H2O solution"]["composition"][0]["term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    assert solutions["5% Na2S x 9H2O solution"]["composition"][0]["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }
    for stock in (
        solutions["5% L-Cysteine HCl H2O solution"],
        solutions["5% Na2S x 9H2O solution"],
    ):
        assert stock["composition"][0]["concentration"] == {
            "value": "50.0",
            "unit": "G_PER_L",
        }


def test_repair_keeps_jcm_197_vitamins_opaque(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    trace_vitamins = _by_name(repaired["solutions"])["Trace vitamins (JCM Medium 197)"]

    assert "composition" not in trace_vitamins
    assert "term" not in trace_vitamins


def test_repair_adds_anaerobic_vessel_conditions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["aeration"] == (
        "H2-CO2 (80:20, v/v) during preparation; N2-CO2 (80:20, v/v) for cultivation"
    )
    assert repaired["culture_vessel"] == ("5 ml medium in Hungate tubes with butyl rubber stoppers")
    assert repaired["incubation_atmosphere"] == "ANAEROBIC"


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["data_quality_flags"] == [
        "resolved_reference",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.JCM_806},
        {"reference": repair_module.JCM_262},
        {"reference": repair_module.JCM_265},
        {"reference": repair_module.JCM_151},
        {"reference": repair_module.JCM_197},
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.JCM_806,
            "notes": repair_module.NOTES,
        }
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    path = tmp_path / repair_module.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_doc(repair_module), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert {
        path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "jcm.grmd:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_SOURCE_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_component_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "981"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_reviewed_input(repair_module) -> None:
    doc = yaml.safe_load(
        (repair_module.NORMALIZED / repair_module.TARGET).read_text(encoding="utf-8")
    )

    assert doc["id"] == repair_module.EXPECTED_ID
    assert (
        repair_module._signature(doc["ingredients"], "ingredients"),
        repair_module._signature(doc.get("solutions"), "solutions"),
    ) in {
        (
            repair_module.IMPORTED_INGREDIENT_SIGNATURE,
            repair_module.IMPORTED_SOLUTION_SIGNATURE,
        ),
        (repair_module.FINAL_INGREDIENT_SIGNATURE, repair_module.FINAL_SOLUTION_SIGNATURE),
    }
