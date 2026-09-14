from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load_repair():
    path = REPO_ROOT / "scripts" / "repair_mediadive_public_score30.py"
    spec = importlib.util.spec_from_file_location(
        "repair_mediadive_public_score30",
        path,
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_mediadive_public_score30"] = mod
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
        "ph_value": 5.0,
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


def _solution_by_name(doc: dict, name: str) -> dict:
    return next(solution for solution in doc["solutions"] if solution["preferred_term"] == name)


def _component_by_name(solution: dict, name: str) -> dict:
    return next(
        component for component in solution["composition"] if component["preferred_term"] == name
    )


def _ingredient_by_name(doc: dict, name: str) -> dict:
    return next(
        ingredient for ingredient in doc["ingredients"] if ingredient["preferred_term"] == name
    )


def test_all_reviewed_targets_have_expected_ids_and_source_terms():
    repair = _load_repair()

    assert len(repair.UPDATES) == 7
    assert {update.path for update in repair.UPDATES} == set(repair.EXPECTED_IDS)
    assert set(repair.EXPECTED_IDS) == set(repair.EXPECTED_SOURCE_TERMS)


def test_plan_repairs_adds_haha_agar_recipe(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    haha = plans[root / repair.P1_HAHA]

    assert haha["physical_state"] == "SOLID_AGAR"
    assert haha["ph_value"] == 7.5
    assert len(haha["ingredients"]) == 2
    assert len(haha["solutions"]) == 12

    asw = _solution_by_name(haha, "Artificial sea water (ASW) 2x")
    assert asw["concentration"] == {"value": "500", "unit": "ML_PER_L"}
    assert _component_by_name(asw, "NaHCO3")["concentration"] == {
        "value": "1000",
        "unit": "G_PER_L",
    }

    sl8 = _solution_by_name(haha, "Trace element solution SL-8")
    assert sl8["concentration"] == {"value": "2", "unit": "ML_PER_L"}
    assert _component_by_name(sl8, "H3BO3")["concentration"] == {
        "value": "0.062",
        "unit": "G_PER_L",
    }

    mgso4 = _solution_by_name(haha, "MgSO4 x 7 H2O stock")
    assert mgso4["concentration"] == {"value": "13.5714", "unit": "ML_PER_L"}
    assert mgso4["composition"] == [
        {
            "preferred_term": "MgSO4 x 7 H2O",
            "concentration": {"value": "500", "unit": "G_PER_L"},
            "source": repair.SRC_P1,
            "term": {
                "id": "CHEBI:31795",
                "label": "magnesium sulfate heptahydrate",
            },
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:31795",
                "label": "magnesium sulfate heptahydrate",
            },
        }
    ]


def test_plan_repairs_adds_king_b_recipe(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    king_b = plans[root / repair.P3_KING_B]

    assert "solutions" not in king_b
    assert king_b["physical_state"] == "SOLID_AGAR"
    assert king_b["ingredients"] == [
        {
            "preferred_term": "K2HPO4",
            "concentration": {"value": "1.5", "unit": "G_PER_L"},
            "source": repair.SRC_P3,
            "term": {
                "id": "CHEBI:131527",
                "label": "dipotassium hydrogen phosphate",
            },
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:131527",
                "label": "dipotassium hydrogen phosphate",
            },
        },
        {
            "preferred_term": "MgSO4 x 7 H2O",
            "concentration": {"value": "1.5", "unit": "G_PER_L"},
            "source": repair.SRC_P3,
            "term": {
                "id": "CHEBI:31795",
                "label": "magnesium sulfate heptahydrate",
            },
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:31795",
                "label": "magnesium sulfate heptahydrate",
            },
        },
        {
            "preferred_term": "Proteose peptone no. 3",
            "concentration": {"value": "20", "unit": "G_PER_L"},
            "source": repair.SRC_P3,
            "term": {"id": "MICRO:0000180", "label": "proteose peptone"},
        },
        {
            "preferred_term": "Glycerol",
            "concentration": {"value": "10", "unit": "ML_PER_L"},
            "source": repair.SRC_P3,
            "term": {"id": "CHEBI:17754", "label": "glycerol"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:17754",
                "label": "glycerol",
            },
        },
        {
            "preferred_term": "Agar",
            "concentration": {"value": "15", "unit": "G_PER_L"},
            "source": repair.SRC_P3,
            "term": {"id": "CHEBI:2509", "label": "agar"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:2509",
                "label": "agar",
            },
        },
    ]


def test_plan_repairs_adds_mta10_recipe(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    mta10 = plans[root / repair.P6_MTA10]

    assert "solutions" not in mta10
    assert mta10["physical_state"] == "LIQUID"
    assert mta10["ph_value"] == 7.2
    assert [ingredient["preferred_term"] for ingredient in mta10["ingredients"]] == [
        "Tryptose",
        "Beef extract",
        "Yeast extract",
        "NaCl",
        "KH2PO4",
        "Na2HPO4",
    ]
    assert _ingredient_by_name(mta10, "Na2HPO4")["concentration"] == {
        "value": "19.3",
        "unit": "G_PER_L",
    }


def test_plan_repairs_adds_n27_recipe_with_sl6(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    n27 = plans[root / repair.P7_N27_RHODOSPIRILLACEAE]

    assert n27["ph_value"] == 6.8
    assert len(n27["ingredients"]) == 9
    assert {solution["preferred_term"] for solution in n27["solutions"]} == {
        "Fe(III) citrate stock",
        "Vitamin B12 stock",
        "Trace element solution SL-6",
    }

    fe_citrate = _solution_by_name(n27, "Fe(III) citrate stock")
    assert fe_citrate["concentration"] == {"value": "5", "unit": "ML_PER_L"}
    assert _component_by_name(fe_citrate, "Fe(III) citrate")["concentration"] == {
        "value": "1",
        "unit": "G_PER_L",
    }

    b12 = _solution_by_name(n27, "Vitamin B12 stock")
    assert b12["concentration"] == {"value": "0.4", "unit": "ML_PER_L"}
    assert _component_by_name(b12, "Vitamin B12")["concentration"] == {
        "value": "0.1",
        "unit": "G_PER_L",
    }

    sl6 = _solution_by_name(n27, "Trace element solution SL-6")
    assert _component_by_name(sl6, "H3BO3")["concentration"] == {
        "value": "0.3",
        "unit": "G_PER_L",
    }


def test_plan_repairs_adds_m9_sng_stocks_without_nan_id(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    m9_sng = plans[root / repair.P8_M9_SNG]

    assert m9_sng["ingredients"] == []
    assert {solution["preferred_term"] for solution in m9_sng["solutions"]} == {
        "MgSO4 stock",
        "CaCl2 stock",
        "Sinigrin stock",
        "M9 stock",
    }
    assert _solution_by_name(m9_sng, "CaCl2 stock")["concentration"] == {
        "value": "1.63934",
        "unit": "ML_PER_L",
    }

    m9 = _solution_by_name(m9_sng, "M9 stock")
    assert [component["preferred_term"] for component in m9["composition"]] == [
        "Na2HPO4",
        "KH2PO4",
        "NaCl",
        "NH4Cl",
    ]
    solution_names = [solution["preferred_term"] for solution in m9_sng["solutions"]]
    component_names = [
        component["preferred_term"]
        for solution in m9_sng["solutions"]
        for component in solution["composition"]
    ]
    assert "NaN" not in solution_names
    assert "NaN" not in component_names


def test_plan_repairs_adds_p9_current_public_recipe(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    p9 = plans[root / repair.P9_PDB_SNG]

    assert p9["notes"].startswith(
        "MediaDive public Medium P9 currently downloads as Modified Medio Azunol"
    )
    assert p9["physical_state"] == "SOLID_AGAR"
    assert p9["ph_range"] == {"min": 6.8, "max": 8.0}
    assert _ingredient_by_name(p9, "Fe(III) citrate")["concentration"] == {
        "value": "1",
        "unit": "MICROG_PER_L",
    }
    assert _ingredient_by_name(p9, "CuSO4")["concentration"] == {
        "value": "1",
        "unit": "MICROG_PER_L",
    }

    assert {solution["preferred_term"] for solution in p9["solutions"]} == {
        "Trace element solution SL-10",
        "Trace element solution SL-6",
    }
    assert _component_by_name(_solution_by_name(p9, "Trace element solution SL-10"), "HCl")[
        "concentration"
    ] == {
        "value": "2.5",
        "unit": "G_PER_L",
    }
    assert "10% CH4 gas" in p9["preparation_steps"][-1]["description"]


def test_plan_repairs_adds_bekisolid_with_variable_trace_stock(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    beki = plans[root / repair.P10_BEKISOLID]

    assert beki["physical_state"] == "SOLID_AGAR"
    assert beki["ph_range"] == {"min": 6.8, "max": 7.4}
    assert _ingredient_by_name(beki, "Na2S2O4")["concentration"] == {
        "value": "0.5",
        "unit": "G_PER_L",
    }

    trace = _solution_by_name(beki, "Elemento traza")
    assert trace["concentration"] == {"value": "variable", "unit": "VARIABLE"}
    assert _component_by_name(trace, "CuSO4 x 5 H2O")["concentration"] == {
        "value": "0.05",
        "unit": "G_PER_L",
    }
    assert "official recipe does not disclose the stock volume" in trace["notes"]


def test_plan_repairs_adds_review_metadata_once(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    targets = _write_targets(repair, root)

    first = repair.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    second = repair.plan_repairs(root)
    p1 = second[root / repair.P1_HAHA]

    assert second == first
    assert p1["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert p1["references"] == [
        {"reference": repair.P1_DOI},
        {"reference": repair.P1_PUBLIC},
    ]

    matching_events = [
        event
        for event in p1["curation_history"]
        if (event.get("curator") == repair.CURATOR and event.get("action") == repair.ACTION)
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == f"{repair.P1_DOI}; {repair.P1_PUBLIC}"

    p3 = second[root / repair.P3_KING_B]
    assert p3["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    assert p3["references"] == [{"reference": repair.P3_PUBLIC}]
    assert all(
        flag not in p3["data_quality_flags"]
        for flag in targets[root / repair.P3_KING_B]["data_quality_flags"]
    )


def test_plan_repairs_rejects_unexpected_target_id(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    docs = _write_targets(repair, root)
    target = root / repair.P8_M9_SNG
    docs[target]["id"] = "CultureMech:wrong"
    target.write_text(yaml.safe_dump(docs[target], sort_keys=False), encoding="utf-8")

    with pytest.raises(ValueError, match="expected 'CultureMech:010438'"):
        repair.plan_repairs(root)
