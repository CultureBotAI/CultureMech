from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_1445_pmx108_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_1445_pmx108_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_1445_pmx108")


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "pmx_108_medium",
        "original_name": "PMX.108 MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium J1445",
            "term": {
                "id": repair_module.EXPECTED_SOURCE_TERM,
                "label": "PMX.108 MEDIUM",
            },
        },
        "notes": "JCM 1445",
        "ingredients": [
            {
                "preferred_term": preferred_term,
                "concentration": {"value": value, "unit": unit},
            }
            for preferred_term, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_leaves_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_parsed([(repair_module.TARGET, repaired)]) == []


def test_repair_splits_stock_solutions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert set(ingredients) == {
        "NH4Cl",
        "KH2PO4",
        "MgCl2 x 6H2O",
        "CaCl2 x 2H2O",
        "Sodium acetate x 3H2O",
        "Yeast extract",
        "Casamino acids (BD-Difico)",
        "Tryptone (BD-Difico)",
        "Resazurin",
        "Distilled water",
    }
    assert set(solutions) == {
        "Trace mineral solution (JCM Medium 852)",
        "Se/W solution",
        "Trace vitamins solution (JCM Medium 284)",
        "8% NaHCO3 solution",
        "5% L-Cysteine HCl H2O solution",
        "5% Na2S x 9H2O solution",
    }


def test_repair_inlines_jcm_1445_se_w_stock(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert solutions["Se/W solution"]["composition"] == [
        {
            "preferred_term": "Na2SeO3",
            "concentration": {"value": "2.0", "unit": "MG_PER_L"},
            "source": repair_module.SOURCE,
            "notes": "JCM Medium 1445 Se/W stock lists 2.0 mg Na2SeO3 per liter.",
            "term": {"id": "CHEBI:48843", "label": "disodium selenite"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:48843",
                "label": "disodium selenite",
            },
        },
        {
            "preferred_term": "Na2WO4 x 2H2O",
            "concentration": {"value": "1.0", "unit": "MG_PER_L"},
            "source": repair_module.SOURCE,
            "notes": "JCM Medium 1445 Se/W stock lists 1.0 mg Na2WO4 x 2H2O per liter.",
            "term": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:63939",
                "label": "sodium tungstate dihydrate",
            },
        },
    ]


def test_repair_inlines_unambiguous_percent_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    bicarbonate = solutions["8% NaHCO3 solution"]
    assert bicarbonate["composition"][0]["term"] == {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate",
    }
    cysteine = solutions["5% L-Cysteine HCl H2O solution"]
    assert cysteine["composition"][0]["term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    sulfide = solutions["5% Na2S x 9H2O solution"]
    assert sulfide["composition"][0]["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }


def test_repair_keeps_shared_stocks_opaque(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    for preferred_term in (
        "Trace mineral solution (JCM Medium 852)",
        "Trace vitamins solution (JCM Medium 284)",
    ):
        assert "composition" not in solutions[preferred_term]
        assert "term" not in solutions[preferred_term]


def test_repair_adds_anaerobic_vessel_conditions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["aeration"] == (
        "N2-CO2 (4:1, v/v) gas atmosphere with H2 injected after sealing"
    )
    assert repaired["culture_vessel"] == (
        "20 ml medium in 60 ml serum bottles with butyl rubber stoppers"
    )
    assert repaired["incubation_atmosphere"] == "ANAEROBIC"
    assert "10-20% gas-phase volume of H2" in repaired["preparation_steps"][2]["description"]


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.JCM_1445},
        {"reference": repair_module.JCM_852},
        {"reference": repair_module.JCM_284},
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.JCM_1445,
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
    doc["ingredients"][0]["concentration"]["value"] = "0.50"

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
