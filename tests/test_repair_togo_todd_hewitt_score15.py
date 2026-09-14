from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_todd_hewitt_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_todd_hewitt")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_todd_hewitt")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(spec, signature) -> dict:
    return {
        "id": spec.expected_id,
        "name": spec.target.stem,
        "original_name": spec.target.stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [_ingredient(name, value, unit) for name, value, unit in signature],
        "media_term": {
            "preferred_term": spec.expected_media_term,
            "term": {"id": spec.expected_media_term, "label": spec.target.stem},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_units_and_exits_ranking(repair_module, scorer_module) -> None:
    thy = repair_module.repair_record(
        _doc(repair_module.THY_SPEC, repair_module.THY_LEGACY_SIGNATURE),
        repair_module.THY_SPEC,
    )
    th_blood = repair_module.repair_record(
        _doc(repair_module.TH_BLOOD_SPEC, repair_module.TH_BLOOD_LEGACY_SIGNATURE),
        repair_module.TH_BLOOD_SPEC,
    )

    for repaired, spec in (
        (thy, repair_module.THY_SPEC),
        (th_blood, repair_module.TH_BLOOD_SPEC),
    ):
        assert repaired["temperature_value"] == 37.0
        assert repair_module._signature(repaired["ingredients"], "ingredients") == (
            spec.repaired_signature
        )
        assert repaired["organism_culture_type"] == "isolate"
        assert scorer_module.score_record(repaired) == (0, [])

    assert (
        scorer_module.score_parsed(
            [
                (str(repair_module.THY_PATH), thy),
                (str(repair_module.TH_BLOOD_PATH), th_blood),
            ]
        )
        == []
    )


def test_repair_adds_expected_groundings(repair_module) -> None:
    thy = repair_module.repair_record(
        _doc(repair_module.THY_SPEC, repair_module.THY_LEGACY_SIGNATURE),
        repair_module.THY_SPEC,
    )
    th_blood = repair_module.repair_record(
        _doc(repair_module.TH_BLOOD_SPEC, repair_module.TH_BLOOD_LEGACY_SIGNATURE),
        repair_module.TH_BLOOD_SPEC,
    )

    thy_ingredients = _by_name(thy["ingredients"])
    blood_ingredients = _by_name(th_blood["ingredients"])

    assert thy_ingredients[repair_module.YEAST_NACALAI]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert thy_ingredients[repair_module.CO2]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:16526",
        "label": "carbon dioxide",
    }
    assert blood_ingredients[repair_module.SHEEP_BLOOD]["term"] == {
        "id": "UBERON:0000178",
        "label": "blood",
    }
    assert blood_ingredients[repair_module.AGAR]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert thy_ingredients[repair_module.TODD_BD]["culturemech_term"] == {
        "id": "CultureMech:008070",
        "label": "Todd Hewitt Medium",
    }
    assert blood_ingredients[repair_module.TODD_DIFCO]["culturemech_term"] == {
        "id": "CultureMech:008070",
        "label": "Todd Hewitt Medium",
    }
    assert "term" not in thy_ingredients[repair_module.TODD_BD]
    assert "term" not in blood_ingredients[repair_module.TODD_DIFCO]
    for ingredient in [*thy["ingredients"], *th_blood["ingredients"]]:
        if "culturemech_term" not in ingredient:
            assert resolve_ingredient(ingredient).is_resolved


def test_repair_adds_target_organisms_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(
        _doc(repair_module.TH_BLOOD_SPEC, repair_module.TH_BLOOD_LEGACY_SIGNATURE),
        repair_module.TH_BLOOD_SPEC,
    )
    twice = repair_module.repair_record(once, repair_module.TH_BLOOD_SPEC)

    assert twice["target_organisms"] == [
        {
            "preferred_term": "Streptococcus suis",
            "term": {"id": "NCBITaxon:1307", "label": "Streptococcus suis"},
            "evidence": [
                {
                    "reference": repair_module.ZHANG_DOI,
                    "supports": "SUPPORT",
                    "explanation": repair_module.TH_BLOOD_SPEC.target_organism.evidence,
                }
            ],
        }
    ]
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.TH_BLOOD_SPEC.references
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
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
            "source": "; ".join(repair_module.TH_BLOOD_SPEC.references),
            "notes": (
                "Curated TOGO:M2909 from TOGO and Zhang et al. 2014; corrected "
                "imported percentage units, added 37 C cultivation evidence, and "
                "linked opaque Todd Hewitt broth to a curated CultureMech recipe."
            ),
        }
    ]


def test_plan_repairs_targets_both_todd_hewitt_records(repair_module) -> None:
    expected = {}
    for spec in repair_module.SPECS:
        path = repair_module.NORMALIZED / spec.target
        expected[path] = repair_module.repair_record(
            yaml.safe_load(path.read_text(encoding="utf-8")),
            spec,
        )

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module.THY_SPEC, repair_module.THY_LEGACY_SIGNATURE)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_THY_ID):
        repair_module.repair_record(doc, repair_module.THY_SPEC)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module.TH_BLOOD_SPEC, repair_module.TH_BLOOD_LEGACY_SIGNATURE)
    doc["media_term"]["term"]["id"] = "TOGO:M2908"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_TH_BLOOD_MEDIA_TERM):
        repair_module.repair_record(doc, repair_module.TH_BLOOD_SPEC)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module.THY_SPEC, repair_module.THY_LEGACY_SIGNATURE)
    doc["ingredients"][1] = _ingredient("Peptone", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, repair_module.THY_SPEC)


def test_corpus_records_match_repair_contract(repair_module) -> None:
    for spec in repair_module.SPECS:
        path = repair_module.NORMALIZED / spec.target
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == spec.expected_id
        assert repair_module._source_term_id(doc) == spec.expected_media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in {
            spec.legacy_signature,
            spec.repaired_signature,
        }
