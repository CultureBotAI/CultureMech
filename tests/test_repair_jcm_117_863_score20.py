from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_117_863_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm_117_863_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_117_863")


def _doc(repair, path: str) -> dict:
    if path == repair.R_AGAR_PARENT:
        ingredients = [{"preferred_term": "Agar"}]
    elif path == repair.ISP4_PARENT:
        ingredients = [{"preferred_term": "Agar"}]
    else:
        update = repair.CHILD_BY_PATH[path]
        ingredients = [{"preferred_term": name} for name in update.accepted_signatures[0]]

    return {
        "id": repair.EXPECTED_IDS[path],
        "name": Path(path).stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {"term": {"id": repair.EXPECTED_SOURCE_TERMS[path]}},
        "ingredients": ingredients,
        "curation_history": [],
    }


def test_repair_j117_models_catalase_as_filtered_supplement(
    repair_module,
    scorer_module,
) -> None:
    update = repair_module.CHILD_BY_PATH[repair_module.R_AGAR_CATALASE]
    repaired = repair_module.repair_child(_doc(repair_module, update.path), update)

    assert repaired["ph_value"] == 7.2
    assert repaired["ingredients"] == [
        {
            "preferred_term": "Catalase (Sigma C-10)",
            "concentration": {"value": "0.06", "unit": "G_PER_L"},
            "notes": (
                "TOGO M109 maps JCM Medium 117 to 60 mg/L Catalase "
                "(Sigma C-10) added to 1 L of R Agar."
            ),
        }
    ]
    assert repaired["solutions"] == [
        {
            "preferred_term": "R agar",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "notes": ("TOGO M109 maps JCM Medium 117 to 1 L of JCM Medium 26 R Agar."),
            "culturemech_term": {
                "id": repair_module.EXPECTED_IDS[repair_module.R_AGAR_PARENT],
                "label": "R Agar",
            },
        }
    ]
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "AUTOCLAVE",
        "FILTER",
        "MIX",
    ]
    assert repaired["parent_media"]["relationship"] == "SUPPLEMENTED_VARIANT"
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_j863_models_isp4_as_salt_variant(
    repair_module,
    scorer_module,
) -> None:
    update = repair_module.CHILD_BY_PATH[repair_module.ISP4_15_NACL]
    repaired = repair_module.repair_child(_doc(repair_module, update.path), update)

    assert "ph_value" not in repaired
    assert repaired["ingredients"] == [
        {
            "preferred_term": "NaCl",
            "concentration": {"value": "150", "unit": "G_PER_L"},
            "term": {"id": "CHEBI:26710", "label": "sodium chloride"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:26710",
                "label": "sodium chloride",
            },
        }
    ]
    assert repaired["solutions"] == [
        {
            "preferred_term": "Inorganic Salts-Starch Agar (ISP-4)",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "notes": ("TOGO M900 maps JCM Medium 863 to 1 L of JCM Medium 58 ISP-4."),
            "culturemech_term": {
                "id": repair_module.EXPECTED_IDS[repair_module.ISP4_PARENT],
                "label": "Inorganic Salts-Starch Agar (ISP-4)",
            },
        }
    ]
    assert repaired["variant_relationship"] == "SALINITY_VARIANT"
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_plan_adds_both_parent_links(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    for path in (
        repair_module.R_AGAR_PARENT,
        repair_module.ISP4_PARENT,
        repair_module.R_AGAR_CATALASE,
        repair_module.ISP4_15_NACL,
    ):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            yaml.safe_dump(_doc(repair_module, path), sort_keys=False),
            encoding="utf-8",
        )

    first = repair_module.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert second == first
    assert {
        row["path"] for row in first[root / repair_module.R_AGAR_PARENT]["variant_children"]
    } == {f"data/normalized_yaml/{repair_module.R_AGAR_CATALASE}"}
    assert {row["path"] for row in first[root / repair_module.ISP4_PARENT]["variant_children"]} == {
        f"data/normalized_yaml/{repair_module.ISP4_15_NACL}"
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    update = repair_module.CHILD_BY_PATH[repair_module.R_AGAR_CATALASE]
    doc = _doc(repair_module, update.path)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_IDS[update.path]):
        repair_module.repair_child(doc, update)


def test_repair_rejects_wrong_source(repair_module) -> None:
    update = repair_module.CHILD_BY_PATH[repair_module.R_AGAR_CATALASE]
    doc = _doc(repair_module, update.path)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J26"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_SOURCE_TERMS[update.path]):
        repair_module.repair_child(doc, update)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    update = repair_module.CHILD_BY_PATH[repair_module.R_AGAR_CATALASE]
    doc = _doc(repair_module, update.path)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_child(doc, update)
