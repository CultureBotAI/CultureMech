from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load_repair():
    path = REPO_ROOT / "scripts" / "repair_jcm_nbrc_score35.py"
    spec = importlib.util.spec_from_file_location(
        "repair_jcm_nbrc_score35",
        path,
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_jcm_nbrc_score35"] = mod
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(repair, update) -> dict:
    return {
        "id": repair.EXPECTED_IDS[update.path],
        "name": Path(update.path).stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [],
        "solutions": [
            {
                "preferred_term": "stale solution",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
        "media_term": {
            "preferred_term": repair.EXPECTED_SOURCE_TERMS[update.path],
            "term": {
                "id": repair.EXPECTED_SOURCE_TERMS[update.path],
                "label": repair.EXPECTED_SOURCE_TERMS[update.path],
            },
        },
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
            "source_information_unavailable",
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _write_targets(repair, root: Path) -> dict[Path, dict]:
    docs = {}
    for update in repair.UPDATES:
        path = root / update.path
        path.parent.mkdir(parents=True, exist_ok=True)
        docs[path] = _minimal_doc(repair, update)
        path.write_text(
            yaml.safe_dump(docs[path], sort_keys=False),
            encoding="utf-8",
        )
    return docs


def test_all_reviewed_targets_have_expected_ids_and_source_terms():
    repair = _load_repair()

    assert len(repair.UPDATES) == 2
    assert {update.path for update in repair.UPDATES} == set(repair.EXPECTED_IDS)
    assert set(repair.EXPECTED_IDS) == set(repair.EXPECTED_SOURCE_TERMS)


def test_plan_repairs_adds_poremedia_product(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    poremedia = plans[root / repair.JCM_1087_POREMEDIA]

    assert "solutions" not in poremedia
    assert poremedia["physical_state"] == "SOLID_AGAR"
    assert poremedia["ingredients"] == [
        {
            "preferred_term": "POREMEDIA B-CYE alpha Agar Medium (Eiken Chemical)",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "JCM Medium 1087",
            "notes": (
                "JCM Medium 1087 names an Eiken Chemical commercial "
                "POREMEDIA B-CYE alpha Agar Medium product without stating "
                "its amount or internal formulation."
            ),
        }
    ]
    assert poremedia["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Use the commercially available POREMEDIA B-CYE alpha Agar "
                "Medium manufactured by Eiken Chemical."
            ),
        }
    ]


def test_plan_repairs_adds_seawater_porphyra_materials(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    seawater = plans[root / repair.TOGO_M1770_SEAWATER_PORPHYRA]

    assert "solutions" not in seawater
    assert seawater["physical_state"] == "LIQUID"
    assert seawater["salinity"] == "marine (natural seawater)"
    assert seawater["ingredients"] == [
        {
            "preferred_term": "Sterilized natural seawater",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "NBRC Medium 985 / TOGO Medium M1770",
            "notes": (
                "NBRC Medium 985 and TOGO M1770 list sterilized natural "
                "seawater without specifying an amount."
            ),
        },
        {
            "preferred_term": "Porphyra thalli",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "NBRC Medium 985 / TOGO Medium M1770",
            "notes": (
                "NBRC Medium 985 and TOGO M1770 list Porphyra thalli "
                "without specifying an amount."
            ),
        },
    ]
    assert seawater["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Use sterilized natural seawater with Porphyra thalli.",
        }
    ]


def test_plan_repairs_adds_review_metadata_once(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    targets = _write_targets(repair, root)

    first = repair.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    second = repair.plan_repairs(root)
    seawater = second[root / repair.TOGO_M1770_SEAWATER_PORPHYRA]

    assert second == first
    assert seawater["data_quality_flags"] == [
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]
    assert seawater["references"] == [
        {"reference": repair.TOGO_M1770},
        {"reference": repair.NBRC_M985},
    ]

    matching_events = [
        event
        for event in seawater["curation_history"]
        if (
            event.get("curator") == repair.CURATOR
            and event.get("action") == repair.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == f"{repair.TOGO_M1770}; {repair.NBRC_M985}"

    poremedia = second[root / repair.JCM_1087_POREMEDIA]
    assert poremedia["data_quality_flags"] == [
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]
    assert poremedia["references"] == [{"reference": repair.JCM_1087}]
    assert all(
        flag not in poremedia["data_quality_flags"]
        for flag in targets[root / repair.JCM_1087_POREMEDIA]["data_quality_flags"]
    )


def test_plan_repairs_rejects_unexpected_target_id(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    docs = _write_targets(repair, root)
    target = root / repair.JCM_1087_POREMEDIA
    docs[target]["id"] = "CultureMech:wrong"
    target.write_text(yaml.safe_dump(docs[target], sort_keys=False), encoding="utf-8")

    with pytest.raises(ValueError, match="expected 'CultureMech:002267'"):
        repair.plan_repairs(root)
