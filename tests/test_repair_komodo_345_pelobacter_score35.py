from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_345_pelobacter_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_komodo_345_pelobacter_score35")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_345_pelobacter")


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": Path(target.path).stem,
        "original_name": "PELOBACTER ACETYLENICUS MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 345",
            "term": {"id": target.source_term, "label": "PELOBACTER ACETYLENICUS MEDIUM"},
        },
        "notes": "Source: KOMODO ModelSEED",
        "ingredients": [],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc.get("ingredients") or doc.get("composition") or []:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


def _solution(doc: dict, preferred_term: str) -> dict:
    for solution in doc["solutions"]:
        if solution["preferred_term"] == preferred_term:
            return solution
    raise AssertionError(f"missing solution {preferred_term!r}")


def test_repair_expands_empty_pelobacter_medium(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/pelobacter_acetylenicus_medium.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["ph_value"] == 7.2
    assert repaired["incubation_atmosphere"] == "ANAEROBIC"
    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "Distilled water",
        "KH2PO4",
        "NH4Cl",
        "NaCl",
        "MgCl2 x 6H2O",
        "KCl",
        "CaCl2 x 2H2O",
        "Resazurin",
        "NaHCO3",
        "Acetoin",
        "CO2",
        "N2",
    ]
    assert _ingredient(repaired, "Resazurin")["concentration"] == {
        "value": "1",
        "unit": "MG_PER_L",
    }
    assert _ingredient(repaired, "Acetoin")["term"] == {
        "id": "CHEBI:15688",
        "label": "acetoin",
    }
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_inlines_sl10_stock(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/pelobacter_acetylenicus_medium.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    sl10 = _solution(repaired, "Trace element solution SL-10")

    assert sl10["concentration"] == {"value": "1", "unit": "ML_PER_L"}
    assert len(sl10["composition"]) == 10
    assert _ingredient(sl10, "HCl (25%; 7.7 M)")["concentration"] == {
        "value": "10",
        "unit": "ML_PER_L",
    }
    assert _ingredient(sl10, "H3BO3")["concentration"] == {
        "value": "6",
        "unit": "MG_PER_L",
    }
    assert _ingredient(sl10, "CoCl2 x 6H2O")["term"] == {
        "id": "CHEBI:53503",
        "label": "cobalt chloride hexahydrate",
    }
    assert _ingredient(sl10, "NiCl2 x 6H2O")["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }


def test_repair_adds_sulfide_stock_and_source_preparation(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/pelobacter_acetylenicus_medium.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    sulfide = _solution(repaired, "3.6% Na2S x 9H2O solution")

    assert sulfide["concentration"] == {"value": "10", "unit": "ML_PER_L"}
    assert sulfide["composition"] == [
        {
            "preferred_term": "Na2S x 9H2O",
            "concentration": {"value": "36", "unit": "G_PER_L"},
            "source": repair_module.SOURCE_NBRC_1016,
            "notes": (
                "NBRC Medium 1016 lists Na2S x 9H2O as a 3.6% separately "
                "autoclaved solution."
            ),
            "term": {
                "id": "CHEBI:76209",
                "label": "sodium sulfide nonahydrate",
            },
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:76209",
                "label": "sodium sulfide nonahydrate",
            },
        }
    ]
    assert repaired["preparation_steps"][1]["description"].startswith(
        "Dispense the medium into suitable culture vessels under an N2/CO2"
    )
    assert repaired["preparation_steps"][3] == {
        "step_number": 4,
        "action": "FILTER_STERILIZE",
        "description": "Prepare a filter-sterile Acetoin solution.",
    }


def test_solution_compositions_are_flat_ingredients(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/pelobacter_acetylenicus_medium.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    for solution in repaired["solutions"]:
        for component in solution["composition"]:
            assert "composition" not in component
            assert "preparation_notes" not in component


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/pelobacter_acetylenicus_medium.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.KOMODO_345},
        {"reference": repair_module.TOGO_M1791},
        {"reference": repair_module.NBRC_1016},
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": (
                f"{repair_module.KOMODO_345}; {repair_module.TOGO_M1791}; "
                f"{repair_module.NBRC_1016}"
            ),
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
    target = repair_module.TARGET_BY_PATH["bacterial/pelobacter_acetylenicus_medium.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/pelobacter_acetylenicus_medium.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "komodo.medium:999"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/pelobacter_acetylenicus_medium.yaml"]
    doc = _doc(target)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="component signature drifted"):
        repair_module.repair_record(doc, target)
