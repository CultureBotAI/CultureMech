from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_sparse_siblings_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm_sparse_siblings_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_sparse_siblings")


def _doc(repair, target) -> dict:
    doc = {
        "id": target.expected_id,
        "name": target.path.stem,
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": str(target.path),
            "term": {
                "id": target.expected_media_term,
                "label": target.path.stem,
            },
        },
        "notes": "stale import note",
        "ingredients": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
        ],
        "curation_history": [],
    }

    if target.path == repair.ME_AGAR:
        doc["ingredients"] = [
            {
                "preferred_term": "Malt extract agar",
                "term": {"id": "CHEBI:2509", "label": "agar"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:2509",
                    "label": "agar",
                },
                "concentration": {"value": "50", "unit": "G_PER_L"},
            }
        ]
        doc["preparation_steps"] = [
            {
                "step_number": 1,
                "action": "AUTOCLAVE",
                "description": "Autoclave at 115C for 10 min.",
            }
        ]
    else:
        doc["medium_type"] = "DEFINED"
        doc["composition_type"] = "DEFINED"
        doc["physical_state"] = "LIQUID"
        doc["ingredients"] = [
            {
                "preferred_term": "Thioglycolate",
                "term": {"id": "CHEBI:30066", "label": "thioglycolate(1-)"},
                "mediaingredientmech_term": {
                    "id": "MediaIngredientMech:000649",
                    "label": "Thioglycolate",
                },
                "concentration": {"value": "29.8", "unit": "G_PER_L"},
            }
        ]
        doc["preparation_steps"] = [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Comment: The medium is semisolid. For strain JCM 13596, "
                    "prepare the medium anaerobically (under N2)."
                ),
            }
        ]

    return doc


def _write_minimal_tree(repair, root: Path) -> None:
    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(_doc(repair, target), sort_keys=False),
            encoding="utf-8",
        )


def _target(repair, path: Path):
    for target in repair.TARGETS:
        if target.path == path:
            return target
    raise AssertionError(f"unknown target: {path}")


def test_all_reviewed_targets_are_guarded(repair_module) -> None:
    assert {target.path for target in repair_module.TARGETS} == {
        repair_module.ME_AGAR,
        repair_module.THIOGLYCOLLATE,
    }
    assert {target.expected_id for target in repair_module.TARGETS} == {
        "CultureMech:002616",
        "CultureMech:002878",
    }
    assert {target.expected_media_term for target in repair_module.TARGETS} == {
        "mediadive.medium:J258",
        "mediadive.medium:J529",
    }


def test_me_agar_adds_water_and_preserves_opaque_oxoid_product(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.ME_AGAR)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ingredients"] == [
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": "TOGO M250/JCM Medium 258 snapshot",
            "notes": "TOGO M250 snapshots JCM_M258 and lists 1.0 L distilled water.",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:15377",
                "label": "water",
            },
        },
        {
            "preferred_term": "Malt extract agar (Oxoid)",
            "concentration": {"value": "50", "unit": "G_PER_L"},
            "source": "TOGO M250/JCM Medium 258 snapshot",
            "notes": (
                "TOGO M250 snapshots JCM_M258 and lists 50 g/L Malt extract " "agar from Oxoid."
            ),
        },
    ]
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 115 C for 10 min.",
        }
    ]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_thioglycollate_restores_undefined_semisolid_product(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.THIOGLYCOLLATE)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "SEMISOLID"
    assert repaired["ingredients"][1] == {
        "preferred_term": "Thioglycollate medium (Sigma)",
        "concentration": {"value": "29.8", "unit": "G_PER_L"},
        "source": "TOGO M530/JCM Medium 529 snapshot",
        "notes": (
            "TOGO M530 snapshots JCM_M529 and lists 29.8 g/L " "Thioglycollate medium from Sigma."
        ),
    }
    assert "preparation_steps" not in repaired
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_repair_adds_togo_references_flags_and_history_once(
    repair_module,
) -> None:
    target = _target(repair_module, repair_module.THIOGLYCOLLATE)

    once = repair_module.repair_record(_doc(repair_module, target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["references"] == [{"reference": repair_module.TOGO_M530}]
    assert twice["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
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
    assert matching_events[0] == {
        "timestamp": repair_module.TIMESTAMP,
        "curator": repair_module.CURATOR,
        "action": repair_module.ACTION,
        "source": repair_module.TOGO_M530,
        "notes": target.notes,
    }


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    first = repair_module.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(root): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = _target(repair_module, repair_module.ME_AGAR)
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:002616"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = _target(repair_module, repair_module.THIOGLYCOLLATE)
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:529"

    with pytest.raises(ValueError, match="expected media term mediadive.medium:J529"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = _target(repair_module, repair_module.ME_AGAR)
    doc = _doc(repair_module, target)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="expected one of"):
        repair_module.repair_record(doc, target)
