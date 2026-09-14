from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load_repair():
    path = REPO_ROOT / "scripts" / "repair_dsmz_77_score35.py"
    spec = importlib.util.spec_from_file_location(
        "repair_dsmz_77_score35",
        path,
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_dsmz_77_score35"] = mod
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "liver_broth_oxoid_cm_77",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "DSMZ Medium 77",
            "term": {
                "id": repair.EXPECTED_SOURCE_TERM,
                "label": "LIVER BROTH (Oxoid CM 77)",
            },
        },
        "ingredients": [],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "stale",
            }
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _write_target(repair, root: Path, doc: dict | None = None) -> Path:
    path = root / repair.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(doc or _minimal_doc(repair), sort_keys=False),
        encoding="utf-8",
    )
    return path


def test_plan_repairs_adds_opaque_product_and_n2_atmosphere(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_target(repair, root)

    plans = repair.plan_repairs(root)
    repaired = plans[root / repair.TARGET]

    assert repaired["ingredients"] == [
        {
            "preferred_term": "Liver Broth (Oxoid CM 77)",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "DSMZ Medium 77",
            "notes": (
                "DSMZ Medium 77 identifies Liver Broth (Oxoid CM 77) but "
                "directs users to prepare the medium from the bottle without "
                "stating an amount or the internal formulation."
            ),
        },
        {
            "preferred_term": "N2 gas",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "DSMZ Medium 77",
            "notes": (
                "DSMZ Medium 77 instructs users to prepare the medium under "
                "a 100% N2 gas atmosphere."
            ),
            "term": {"id": "CHEBI:17997", "label": "dinitrogen"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:17997",
                "label": "dinitrogen",
            },
        },
    ]
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare Liver Broth (Oxoid CM 77) according to the bottle "
                "directions under a 100% N2 gas atmosphere."
            ),
        }
    ]


def test_plan_repairs_adds_source_metadata_once(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    target = _write_target(repair, root)

    first = repair.plan_repairs(root)
    target.write_text(
        yaml.safe_dump(first[target], sort_keys=False),
        encoding="utf-8",
    )
    second = repair.plan_repairs(root)
    repaired = second[target]

    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert repaired["references"] == [{"reference": repair.DSMZ_77}]

    matching_events = [
        event
        for event in repaired["curation_history"]
        if (
            event.get("curator") == repair.CURATOR
            and event.get("action") == repair.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == repair.DSMZ_77


def test_plan_repairs_rejects_unexpected_target_id(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    doc = _minimal_doc(repair)
    doc["id"] = "CultureMech:wrong"
    _write_target(repair, root, doc)

    with pytest.raises(ValueError, match="expected 'CultureMech:001915'"):
        repair.plan_repairs(root)
