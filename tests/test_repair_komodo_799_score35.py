from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_799_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _doc(target) -> dict:
    return {
        "id": target.expected_id,
        "name": Path(target.path).stem,
        "original_name": "DESULFOVIBRIO INOPINATUS MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 799",
            "term": {
                "id": target.expected_media_term,
                "label": "DESULFOVIBRIO INOPINATUS MEDIUM",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 799 | DSMZ Medium: 799",
        "ingredients": [],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


@pytest.fixture
def repair():
    return _load_script(SCRIPT, "repair_komodo_799_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_799")


def test_repair_record_adds_pyruvate_branch_components(repair, scorer) -> None:
    target = repair.TARGETS[0]

    once = repair.repair_record(_doc(target), target)
    twice = repair.repair_record(once, target)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(once["ingredients"]) == 39
    assert _ingredient(once, "Na2SO4")["concentration"] == {
        "value": "2.976190",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Na-pyruvate")["concentration"] == {
        "value": "2.500000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Na-pyruvate")["term"] == {
        "id": "CHEBI:50144",
        "label": "sodium pyruvate",
    }
    assert _ingredient(once, "Na2WO4 x 2 H2O")["term"] == {
        "id": "CHEBI:63939",
        "label": "sodium tungstate dihydrate",
    }


def test_repair_record_adds_trihydroxybenzene_branch_components(
    repair,
    scorer,
) -> None:
    target = repair.TARGETS[1]

    repaired = repair.repair_record(_doc(target), target)
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert scorer.score_record(repaired) == (0, [])
    assert len(repaired["ingredients"]) == 39
    assert "Na-acetate x 3 H2O" not in names
    assert "Na-pyruvate" not in names
    assert _ingredient(repaired, "Na2SO4")["concentration"] == {
        "value": "2.991027",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "1,2,4-trihydroxybenzene")["concentration"] == {
        "value": "2.000",
        "unit": "MILLIMOLAR",
    }
    assert _ingredient(repaired, "1,2,4-trihydroxybenzene")["term"] == {
        "id": "CHEBI:16971",
        "label": "benzene-1,2,4-triol",
    }
    assert "mediaingredientmech_chebi_term" not in _ingredient(
        repaired,
        "Yeast extract",
    )


def test_repair_record_combines_141_and_503_vitamin_stocks(repair) -> None:
    for target in repair.TARGETS:
        repaired = repair.repair_record(_doc(target), target)

        assert _ingredient(repaired, "D(+)-Biotin")["source"] == repair.SOURCE_503
        assert _ingredient(repaired, "Vitamin B12")["source"] == repair.SOURCE_503
        assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["source"] == repair.SOURCE_385
        assert _ingredient(repaired, "NaOH")["source"] == repair.SOURCE_385


def test_repair_record_adds_branch_specific_references(repair) -> None:
    medium_799 = repair.repair_record(_doc(repair.TARGETS[0]), repair.TARGETS[0])
    replacement = repair.repair_record(_doc(repair.TARGETS[1]), repair.TARGETS[1])

    assert medium_799["references"][0:2] == [
        {"reference": repair.KOMODO_799_URL},
        {"reference": repair.DSMZ_799_URL},
    ]
    assert replacement["references"][0:2] == [
        {"reference": repair.KOMODO_799_REPLACE_URL},
        {"reference": repair.DSMZ_799_URL},
    ]
    assert medium_799["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    target = repair.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006511"):
        repair.repair_record(doc, target)


def test_repair_record_rejects_wrong_source(repair) -> None:
    target = repair.TARGETS[1]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "komodo.medium:799"

    with pytest.raises(
        ValueError,
        match="missing expected media term komodo.medium:799_replace",
    ):
        repair.repair_record(doc, target)
