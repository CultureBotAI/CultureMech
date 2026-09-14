from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_parent_wrappers_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(repair, target) -> dict:
    return {
        "id": target.expected_id,
        "name": target.path.rsplit("/", 1)[-1].removesuffix(".yaml"),
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [],
        "media_term": {
            "preferred_term": target.expected_media_term,
            "term": {"id": target.expected_media_term, "label": target.expected_media_term},
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def test_parent_wrappers_score_only_on_norm_signal() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_parent_wrappers_score20")
    scorer = _load_script(SCORER, "score_review_need_for_jcm_parent_wrappers")

    for target in repair.TARGETS:
        repaired = repair.repair_record(_minimal_doc(repair, target), target)

        assert scorer.score_record(repaired) == (5, ["no pH and no temperature"])


def test_lamprobacter_and_allochromatium_preserve_distinct_b12_sources() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_parent_wrappers_score20_b12")
    by_path = {target.path: target for target in repair.TARGETS}

    lamprobacter = repair.repair_record(
        _minimal_doc(repair, by_path[repair.M566_LAMPROBACTER]),
        by_path[repair.M566_LAMPROBACTER],
    )
    allochromatium = repair.repair_record(
        _minimal_doc(repair, by_path[repair.M574_ALLOCHROMATIUM]),
        by_path[repair.M574_ALLOCHROMATIUM],
    )

    assert "2 mg/100 ml" in lamprobacter["solutions"][0]["notes"]
    assert "2 mg/ml" in allochromatium["solutions"][0]["notes"]
    assert lamprobacter["parent_media"] == {
        "path": "data/normalized_yaml/bacterial/TOGO_M565_Thiorhodococcus_Bheemlicum_Medium.yaml",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": "CultureMech:009960",
        "name": "thiorhodococcus_bheemlicum_medium",
        "notes": "Supplements Medium 561 with 1.0 ml/L vitamin B12 solution (2 mg/100 ml).",
    }


def test_modified_gam_agar_keeps_official_nissui_mass() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_parent_wrappers_score20_gam")
    target = next(target for target in repair.TARGETS if target.path == repair.M671_MODIFIED_GAM)

    repaired = repair.repair_record(_minimal_doc(repair, target), target)

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert repaired["ingredients"] == [
        {
            "preferred_term": "GAM agar, modified (Nissui)",
            "concentration": {"value": "56.7", "unit": "G_PER_L"},
            "source": "JCM Medium 655",
            "notes": "JCM Medium 655 lists 56.7 g GAM agar, modified (Nissui).",
        },
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": "JCM Medium 655",
            "notes": "JCM Medium 655 lists 1.0 L distilled water.",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
        },
    ]


def test_plan_repairs_is_idempotent(tmp_path: Path) -> None:
    repair = _load_script(SCRIPT, "repair_jcm_parent_wrappers_score20_idempotent")
    root = tmp_path / "normalized"

    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_minimal_doc(repair, target), sort_keys=False), encoding="utf-8")

    first = repair.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    assert repair.plan_repairs(root) == first
