from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_commercial_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture
def repair():
    return _load_script(SCRIPT, "repair_togo_commercial_score20")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_togo_commercial")


def _minimal_doc(target) -> dict:
    components = [
        {
            "preferred_term": name,
            "concentration": {"value": value, "unit": unit},
        }
        for name, value, unit in target.imported_signature
    ]
    return {
        "id": target.expected_id,
        "name": target.path.rsplit("/", 1)[-1].removesuffix(".yaml"),
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": components,
        "media_term": {
            "preferred_term": target.expected_media_term,
            "term": {"id": target.expected_media_term, "label": target.expected_media_term},
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _write_minimal_tree(repair, root: Path) -> None:
    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_minimal_doc(target), sort_keys=False), encoding="utf-8")


def test_marine_broth_expands_atcc_scratch_formula_without_agar(repair, scorer) -> None:
    target = next(t for t in repair.TARGETS if t.path == repair.M33_MARINE_BROTH)

    repaired = repair.repair_record(_minimal_doc(target), target)

    assert scorer.score_record(repaired) == (5, ["no pH and no temperature"])
    assert {
        row["preferred_term"]: row["concentration"]["value"] for row in repaired["ingredients"]
    } == {
        "Peptone": "5.0",
        "Yeast Extract": "1.0",
        "Ferric Citrate": "0.1",
        "Sodium Chloride": "19.45",
        "Magnesium Chloride": "8.8",
        "Sodium Sulfate": "3.24",
        "Calcium Chloride": "1.8",
        "Potassium Chloride": "0.55",
        "Sodium Bicarbonate": "0.16",
        "Potassium Bromide": "0.08",
        "Strontium Chloride": "0.034",
        "Boric Acid": "0.022",
        "Sodium Silicate": "0.004",
        "Sodium Fluoride": "0.0024",
        "Ammonium Nitrate": "0.0016",
        "Disodium Phosphate": "0.008",
        "Distilled water": "1000.0",
    }


def test_marine_agar_adds_atcc_agar_to_broth_formula(repair) -> None:
    target = next(t for t in repair.TARGETS if t.path == repair.M1547_MARINE_AGAR)

    repaired = repair.repair_record(_minimal_doc(target), target)

    assert len(repaired["ingredients"]) == 18
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert repaired["ingredients"][-2] == {
        "preferred_term": "Agar",
        "concentration": {"value": "15.0", "unit": "G_PER_L"},
        "source": "ATCC Medium 2",
        "notes": (
            "ATCC Medium 2 prints 15.0 g agar in the Difco Marine Agar 2216 " "scratch formulation."
        ),
        "term": {"id": "CHEBI:2509", "label": "agar"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:2509", "label": "agar"},
    }


def test_nbrc_commercial_recipes_keep_official_pH(repair, scorer) -> None:
    by_path = {target.path: target for target in repair.TARGETS}

    todd = repair.repair_record(
        _minimal_doc(by_path[repair.M1524_TODD_HEWITT]), by_path[repair.M1524_TODD_HEWITT]
    )
    gam = repair.repair_record(_minimal_doc(by_path[repair.M1525_GAM]), by_path[repair.M1525_GAM])

    assert todd["ph_value"] == 7.3
    assert gam["ph_value"] == 7.3
    assert scorer.score_record(todd) == (0, [])
    assert scorer.score_record(gam) == (0, [])


def test_db_variant_and_distilled_water_are_curated_sparse_recipes(repair, scorer) -> None:
    by_path = {target.path: target for target in repair.TARGETS}

    db_variant = repair.repair_record(
        _minimal_doc(by_path[repair.M1125_DB_SEA_SALTS]),
        by_path[repair.M1125_DB_SEA_SALTS],
    )
    distilled_water = repair.repair_record(
        _minimal_doc(by_path[repair.M682_DISTILLED_WATER]),
        by_path[repair.M682_DISTILLED_WATER],
    )

    assert db_variant["parent_media"]["id"] == "CultureMech:009974"
    assert distilled_water["ingredients"] == [
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": "JCM Medium 664",
            "notes": "JCM Medium 664 consists of autoclaved distilled water.",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
        }
    ]
    assert scorer.score_record(db_variant) == (5, ["no pH and no temperature"])
    assert scorer.score_record(distilled_water) == (5, ["no pH and no temperature"])


def test_plan_repairs_is_idempotent_and_removes_false_gam_water_links(
    repair, tmp_path: Path
) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair, root)

    gam_path = root / repair.M1525_GAM
    gam = yaml.safe_load(gam_path.read_text(encoding="utf-8"))
    gam["variant_children"] = [{"path": f"data/normalized_yaml/{repair.M682_DISTILLED_WATER}"}]
    gam_path.write_text(yaml.safe_dump(gam, sort_keys=False), encoding="utf-8")

    water_path = root / repair.M682_DISTILLED_WATER
    water = yaml.safe_load(water_path.read_text(encoding="utf-8"))
    water["parent_media"] = {"path": f"data/normalized_yaml/{repair.M1525_GAM}"}
    water["variant_relationship"] = "SOURCE_DUPLICATE"
    water["variant_modifications"] = ["Same ingredient and concentration signature"]
    water_path.write_text(yaml.safe_dump(water, sort_keys=False), encoding="utf-8")

    first = repair.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    second = repair.plan_repairs(root)

    assert second == first
    assert "variant_children" not in first[root / repair.M1525_GAM]
    assert "parent_media" not in first[root / repair.M682_DISTILLED_WATER]
    assert "variant_relationship" not in first[root / repair.M682_DISTILLED_WATER]


def test_repair_record_rejects_wrong_id(repair) -> None:
    target = repair.TARGETS[0]
    doc = _minimal_doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=f"expected immutable id {target.expected_id}"):
        repair.repair_record(doc, target)


def test_repair_record_rejects_component_drift(repair) -> None:
    target = next(t for t in repair.TARGETS if t.path == repair.M20_TRYPTO_SOYA)
    doc = _minimal_doc(target)
    doc["ingredients"][1]["concentration"]["value"] = "20"

    with pytest.raises(ValueError, match="component signature drifted"):
        repair.repair_record(doc, target)


def test_target_records_match_reviewed_inputs(repair) -> None:
    for target in repair.TARGETS:
        path = repair.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.expected_id
        assert repair._signature(doc) in {
            target.imported_signature,
            repair._recipe_signature(target.recipe),
        }
