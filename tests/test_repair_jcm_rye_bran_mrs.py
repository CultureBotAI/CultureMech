from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "repair_jcm_rye_bran_mrs.py"
SCORER = REPO_ROOT / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _component(rows: list[dict], preferred_term: str) -> dict:
    return next(row for row in rows if row["preferred_term"] == preferred_term)


def test_rye_bran_mrs_uses_rye_bran_extract_as_solution() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_rye_bran_mrs")
    scorer = _load_script(SCORER, "score_review_need_rye_bran")
    doc = repair._load(repair.NORMALIZED / repair.TARGET)
    togo_source = repair._load(repair.NORMALIZED / repair.TOGO_SOURCE)

    repaired = repair.repair_document(doc, togo_source)

    assert len(repaired["ingredients"]) == 2
    assert _component(repaired["ingredients"], "Lactobacilli MRS broth")[
        "culturemech_term"
    ] == {
        "id": "CultureMech:009017",
        "label": "Lactobacilli MRS Broth",
    }
    assert _component(repaired["ingredients"], "Distilled water")["concentration"] == {
        "value": "100.0",
        "unit": "ML_PER_L",
    }

    rye_bran_extract = repaired["solutions"][0]
    assert rye_bran_extract["preferred_term"] == "Rye-bran extract"
    assert rye_bran_extract["concentration"] == {
        "value": "900.0",
        "unit": "ML_PER_L",
    }
    assert _component(rye_bran_extract["composition"], "Trypsin")[
        "mediaingredientmech_chebi_term"
    ] == {
        "id": "CHEBI:9765",
        "label": "Trypsin",
    }
    assert _component(rye_bran_extract["composition"], "Distilled water")[
        "concentration"
    ] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert scorer.score_record(repaired) == (5, ["no pH and no temperature"])
    assert repaired["variant_children"] == [repair.TOGO_CHILD]
    assert "parent_media" not in repaired


def test_togo_m753_links_to_jcm_source_duplicate() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_rye_bran_mrs_togo")
    scorer = _load_script(SCORER, "score_review_need_rye_bran_togo")
    doc = repair._load(repair.NORMALIZED / repair.TOGO_SOURCE)

    repaired = repair.repair_togo_source_document(doc)

    assert len(repaired["ingredients"]) == 2
    assert _component(repaired["ingredients"], "Lactobacilli MRS broth")[
        "culturemech_term"
    ] == {
        "id": "CultureMech:009017",
        "label": "Lactobacilli MRS Broth",
    }
    assert repaired["solutions"][0]["preferred_term"] == "Rye-bran extract"
    assert repaired["solutions"][0]["concentration"] == {
        "value": "900.0",
        "unit": "ML_PER_L",
    }
    assert repaired["parent_media"] == repair.JCM_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair.SOURCE_DUPLICATE_NOTE]
    assert "variant_children" not in repaired
    assert scorer.score_record(repaired) == (5, ["no pH and no temperature"])


def test_repair_adds_references_flags_and_history() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_rye_bran_mrs_metadata")
    doc = repair._load(repair.NORMALIZED / repair.TARGET)
    togo_source = repair._load(repair.NORMALIZED / repair.TOGO_SOURCE)

    repaired = repair.repair_document(doc, togo_source)

    references = {ref["reference"] for ref in repaired["references"]}
    assert references.issuperset(repair.REFERENCE_IDS)
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert "has_ontology_mappings" in repaired["data_quality_flags"]
    assert "has_unmapped_ingredients" in repaired["data_quality_flags"]
    assert repaired["curation_history"][-1]["action"] == repair.ACTION
    assert repaired["curation_history"][-1]["timestamp"] == "2026-09-08T00:00:00-07:00"


def test_repair_is_idempotent_for_parent_and_togo_source() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_rye_bran_mrs_idempotent")
    parent = repair._load(repair.NORMALIZED / repair.TARGET)
    togo = repair._load(repair.NORMALIZED / repair.TOGO_SOURCE)

    parent_once = repair.repair_document(parent, togo)
    togo_once = repair.repair_togo_source_document(togo)

    assert repair.repair_document(parent_once, togo_once) == parent_once
    assert repair.repair_togo_source_document(togo_once) == togo_once
