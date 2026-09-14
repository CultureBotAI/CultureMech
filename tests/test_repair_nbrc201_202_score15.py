from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc201_202_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
sys.path.insert(0, str(REPO / "src"))
from culturemech.ingredients import resolve_ingredient  # noqa: E402


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_nbrc201_202")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_nbrc201_202")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module, spec) -> dict:
    return {
        "id": spec.expected_id,
        "name": spec.path.stem,
        "original_name": "(Unnamed medium)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in spec.legacy_ingredients
        ],
        "solutions": [
            {
                "preferred_term": name,
                "composition": [],
                "concentration": {"value": value, "unit": unit},
                "name": "Unknown solution",
            }
            for name, value, unit in repair_module.LEGACY_SOLUTIONS
        ],
        "media_term": {
            "preferred_term": spec.expected_media_term,
            "term": {"id": spec.expected_media_term, "label": spec.path.stem},
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_formula_and_exits_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    m201 = repair_module.repair_record(
        _doc(repair_module, repair_module.M201_SPEC),
        repair_module.M201_SPEC,
    )
    m202 = repair_module.repair_record(
        _doc(repair_module, repair_module.M202_SPEC),
        repair_module.M202_SPEC,
    )

    assert "solutions" not in m201
    assert "solutions" not in m202
    assert m201["ph_value"] == 7.0
    assert m202["ph_value"] == 7.0
    assert repair_module._signature(m201["ingredients"], "ingredients") == (
        repair_module.M201_FINAL_INGREDIENTS
    )
    assert repair_module._signature(m202["ingredients"], "ingredients") == (
        repair_module.M202_FINAL_INGREDIENTS
    )
    assert scorer_module.score_record(m201) == (0, [])
    assert scorer_module.score_record(m202) == (0, [])
    assert (
        scorer_module.score_parsed(
            [
                (str(repair_module.M201_PATH), m201),
                (str(repair_module.M202_PATH), m202),
            ]
        )
        == []
    )


def test_repair_adds_grounded_components_and_leaves_opaque_rows_unmapped(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.M202_SPEC),
        repair_module.M202_SPEC,
    )
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["CaCO3"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:3311",
        "label": "calcium carbonate",
    }
    assert ingredients["Glycerol"]["term"] == {
        "id": "CHEBI:17754",
        "label": "glycerol",
    }
    assert ingredients["Glucose"]["term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert ingredients["Agar (if needed)"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]

    unresolved = {
        ingredient["preferred_term"]
        for ingredient in repaired["ingredients"]
        if not resolve_ingredient(ingredient).is_resolved
    }
    assert unresolved == {
        "Potato",
        "Press yeast",
        "Liver infusion",
        "Thioglycolate Medium Dehydrated",
    }


def test_repair_links_nbrc202_as_supplemented_variant(repair_module) -> None:
    m201 = repair_module.repair_record(
        _doc(repair_module, repair_module.M201_SPEC),
        repair_module.M201_SPEC,
    )
    m202 = repair_module.repair_record(
        _doc(repair_module, repair_module.M202_SPEC),
        repair_module.M202_SPEC,
    )

    assert m201["variant_children"] == [
        {
            "path": "data/normalized_yaml/bacterial/togo_medium_m1442.yaml",
            "relationship": "SUPPLEMENTED_VARIANT",
            "id": "CultureMech:007982",
            "name": "togo_medium_m1442",
            "notes": "NBRC Medium 202 adds 15 g/L CaCO3 to NBRC Medium 201.",
        }
    ]
    assert m202["parent_media"] == {
        "path": "data/normalized_yaml/bacterial/togo_medium_m1441.yaml",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": "CultureMech:007981",
        "name": "togo_medium_m1441",
        "notes": "NBRC Medium 202 adds 15 g/L CaCO3 to NBRC Medium 201.",
    }
    assert m202["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert m202["variant_modifications"] == ["Adds 15 g/L CaCO3 to NBRC Medium 201."]


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(
        _doc(repair_module, repair_module.M201_SPEC),
        repair_module.M201_SPEC,
    )
    twice = repair_module.repair_record(once, repair_module.M201_SPEC)

    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.M201_SPEC.references
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert "kg_microbe_match" not in twice
    assert [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": "; ".join(repair_module.M201_SPEC.references),
            "notes": (
                "Curated TOGO:M1441 from TOGO and NBRC Medium 201; corrected the "
                "imported distilled-water unit, moved footnoted potato, liver, "
                "and thioglycolate rows out of empty solution wrappers, added "
                "pH 7.0, grounded disclosed simple components, and linked the "
                "NBRC 202 CaCO3 variant."
            ),
        }
    ]


def test_plan_repairs_both_records(repair_module) -> None:
    expected = {}
    for spec in repair_module.SPECS:
        path = repair_module.NORMALIZED / spec.path
        expected[path] = repair_module.repair_record(
            yaml.safe_load(path.read_text(encoding="utf-8")),
            spec,
        )

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M201_SPEC)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_M201_ID):
        repair_module.repair_record(doc, repair_module.M201_SPEC)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M202_SPEC)
    doc["media_term"]["term"]["id"] = "TOGO:M1441"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_M202_MEDIA_TERM):
        repair_module.repair_record(doc, repair_module.M202_SPEC)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M201_SPEC)
    doc["ingredients"][1] = _ingredient("Ethanol", "15", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, repair_module.M201_SPEC)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M202_SPEC)
    doc["solutions"][2] = _ingredient("Unknown stock", "10", "G_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, repair_module.M202_SPEC)


def test_corpus_records_match_repair_contract(repair_module) -> None:
    for spec in repair_module.SPECS:
        path = repair_module.NORMALIZED / spec.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == spec.expected_id
        assert repair_module._source_term_id(doc) == spec.expected_media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in {
            spec.legacy_ingredients,
            spec.final_ingredients,
        }
        assert repair_module._signature(doc.get("solutions"), "solutions") in {
            (),
            repair_module.LEGACY_SOLUTIONS,
        }
