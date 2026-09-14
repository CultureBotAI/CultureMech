from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load_repair():
    path = REPO_ROOT / "scripts" / "repair_culturebotht_omissions_score30.py"
    spec = importlib.util.spec_from_file_location(
        "repair_culturebotht_omissions_score30",
        path,
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_culturebotht_omissions_score30"] = mod
    spec.loader.exec_module(mod)
    return mod


def _doc(
    recipe_id: str,
    source_id: str,
    base_token: str,
    omitted: tuple[str, ...],
) -> dict:
    ingredients = [
        {
            "preferred_term": base_token,
            "concentration": {"value": "1", "unit": "FOLD_DILUTION"},
        }
    ]
    ingredients.extend(
        {
            "preferred_term": name,
            "concentration": {"value": "-", "unit": "G_PER_L"},
        }
        for name in omitted
    )
    return {
        "id": recipe_id,
        "name": source_id,
        "category": "specialized",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": ingredients,
        "preparation_steps": [],
        "curation_history": [],
        "sources": [
            {
                "database": "CultureBotHT",
                "database_id": source_id,
                "url": "https://github.com/CultureBotAI/CultureBotHT",
            }
        ],
        "data_quality_flags": ["has_unmapped_ingredients"],
    }


def _parent(recipe_id: str, name: str) -> dict:
    return {
        "id": recipe_id,
        "name": name,
        "category": "specialized",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [],
        "preparation_steps": [],
        "curation_history": [],
    }


def _updates_by_path(repair) -> dict[str, object]:
    return {update.path: update for update in repair.TARGETS}


def test_targets_cover_curated_culturebotht_omission_families():
    repair = _load_repair()

    assert len(repair.TARGETS) == 55
    assert {target.base_token for target in repair.TARGETS} == {
        "Dv_base_medium",
        "Dv_base_Y_medium",
        "MoLS4",
        "MoYLS4",
        "ZMB",
        "ZMB_ALS",
    }
    assert repair.PARENTS["MoLS4"].path == "specialized/mols4.yaml"


def test_repair_record_converts_single_omission_to_parent_variant():
    repair = _load_repair()
    updates = _updates_by_path(repair)

    repaired = repair.repair_record(
        _doc(
            "CultureMech:015521",
            "Dv base Y medium no Fe",
            "Dv_base_Y_medium",
            ("Iron (II) chloride tetrahydrate",),
        ),
        updates["specialized/dv_base_y_medium_no_fe.yaml"],
        _parent("CultureMech:015520", "Dv base Y medium"),
    )

    assert repaired["media_term"] == {"preferred_term": "Dv base Y medium no Fe"}
    assert repaired["ingredients"] == []
    assert repaired["solutions"] == [
        {
            "preferred_term": "Dv base Y medium",
            "concentration": {"value": "1", "unit": "FOLD_DILUTION"},
            "culturemech_term": {
                "id": "CultureMech:015520",
                "label": "Dv base Y medium",
            },
            "notes": "CultureBotHT lists Dv_base_Y_medium at one-fold final strength.",
        }
    ]
    assert repaired["parent_media"] == {
        "path": "data/normalized_yaml/specialized/dv_base_y_medium.yaml",
        "relationship": "OMITTED_COMPONENT_VARIANT",
        "id": "CultureMech:015520",
        "name": "Dv base Y medium",
        "notes": "Omits Iron (II) chloride tetrahydrate from Dv base Y medium.",
    }
    assert repaired["variant_modifications"] == [
        "Omits Iron (II) chloride tetrahydrate from Dv base Y medium."
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_formats_multiple_omissions():
    repair = _load_repair()
    updates = _updates_by_path(repair)

    repaired = repair.repair_record(
        _doc(
            "CultureMech:015611",
            "MoLS4 no ammonium no Mo no W",
            "MoLS4",
            ("Ammonium chloride", "Sodium molybdate", "Sodium tungstate dihydrate"),
        ),
        updates["specialized/mols4_no_ammonium_no_mo_no_w.yaml"],
        _parent("CultureMech:015607", "MoLS4"),
    )

    assert repaired["notes"] == (
        "CultureBotHT imports MoLS4 no ammonium no Mo no W as MoLS4 with "
        "Ammonium chloride, Sodium molybdate, and Sodium tungstate dihydrate "
        "omitted."
    )
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare MoLS4 without Ammonium chloride, Sodium molybdate, "
                "and Sodium tungstate dihydrate."
            ),
        }
    ]


def test_repair_record_supports_plain_zmb_omissions():
    repair = _load_repair()
    updates = _updates_by_path(repair)

    repaired = repair.repair_record(
        _doc(
            "CultureMech:015830",
            "ZMB noFolicAcid",
            "ZMB",
            ("Folic Acid",),
        ),
        updates["specialized/zmb_nofolicacid.yaml"],
        _parent("CultureMech:015791", "ZMB"),
    )

    assert repaired["solutions"] == [
        {
            "preferred_term": "ZMB",
            "concentration": {"value": "1", "unit": "FOLD_DILUTION"},
            "culturemech_term": {
                "id": "CultureMech:015791",
                "label": "ZMB",
            },
            "notes": "CultureBotHT lists ZMB at one-fold final strength.",
        }
    ]
    assert repaired["parent_media"] == {
        "path": "data/normalized_yaml/specialized/zmb.yaml",
        "relationship": "OMITTED_COMPONENT_VARIANT",
        "id": "CultureMech:015791",
        "name": "ZMB",
        "notes": "Omits Folic Acid from ZMB.",
    }


def test_repair_record_keeps_previously_resolved_variants_idempotent():
    repair = _load_repair()
    updates = _updates_by_path(repair)
    original = {
        "id": "CultureMech:015800",
        "name": "ZMB ALS noBiotin",
        "category": "specialized",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [],
        "solutions": [
            {
                "preferred_term": "ZMB ALS",
                "concentration": {"value": "1", "unit": "FOLD_DILUTION"},
                "culturemech_term": {
                    "id": "CultureMech:015792",
                    "label": "ZMB ALS",
                },
            },
        ],
        "parent_media": _parent("CultureMech:015792", "ZMB ALS"),
        "variant_relationship": "OMITTED_COMPONENT_VARIANT",
        "variant_modifications": ["Omits biotin from ZMB ALS."],
        "sources": [
            {
                "database": "CultureBotHT",
                "database_id": "ZMB ALS noBiotin",
                "url": "https://github.com/CultureBotAI/CultureBotHT",
            }
        ],
        "references": [],
        "curation_history": [],
        "data_quality_flags": [],
    }

    repaired = repair.repair_record(
        original,
        updates["specialized/zmb_als_nobiotin.yaml"],
        _parent("CultureMech:015792", "ZMB ALS"),
    )

    assert repaired["ingredients"] == []
    assert repaired["variant_modifications"] == ["Omits biotin from ZMB ALS."]
    assert repaired["references"] == [
        {"reference": "CultureBotHT:ZMB ALS noBiotin"},
        {"reference": repair.CULTUREBOTHT_URL},
    ]


def test_repair_record_adds_references_idempotently():
    repair = _load_repair()
    updates = _updates_by_path(repair)
    original = _doc(
        "CultureMech:015795",
        "ZMB ALS noAdenine",
        "ZMB_ALS",
        ("Adenine hydrochloride hydrate",),
    )

    once = repair.repair_record(
        original,
        updates["specialized/zmb_als_noadenine.yaml"],
        _parent("CultureMech:015792", "ZMB ALS"),
    )
    twice = repair.repair_record(
        original | {"references": once["references"]},
        updates["specialized/zmb_als_noadenine.yaml"],
        _parent("CultureMech:015792", "ZMB ALS"),
    )

    assert once["references"] == [
        {"reference": "CultureBotHT:ZMB ALS noAdenine"},
        {"reference": repair.CULTUREBOTHT_URL},
    ]
    assert twice["references"] == once["references"]


def test_plan_repairs_writes_parent_and_children(tmp_path: Path):
    repair = _load_repair()

    for base_token, parent in repair.PARENTS.items():
        path = tmp_path / parent.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(_parent(parent.expected_id, base_token.replace("_", " "))),
            encoding="utf-8",
        )

    for update in repair.TARGETS:
        path = tmp_path / update.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(
                _doc(
                    update.expected_id,
                    update.source_id,
                    update.base_token,
                    ("omitted",),
                )
            ),
            encoding="utf-8",
        )

    plans = repair.plan_repairs(tmp_path)

    assert len(plans) == len(repair.TARGETS) + len(repair.PARENTS)
    assert sorted(
        child["path"]
        for child in plans[tmp_path / "specialized/zmb_als.yaml"]["variant_children"]
    ) == sorted(
        f"data/normalized_yaml/{target.path}"
        for target in repair.TARGETS
        if target.base_token == "ZMB_ALS"
    )
