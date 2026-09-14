from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_official_simple_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(target) -> dict:
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


def test_official_simple_repairs_score_only_on_norm_signal() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20")
    scorer = _load_script(SCORER, "score_review_need_for_official_simple")

    for target in repair.TARGETS:
        repaired = repair.repair_record(_minimal_doc(target), target)
        expected = (
            (0, [])
            if target.path
            in {
                repair.JCM_247,
                repair.BACTERIAL_MARINE_CAULOBACTER,
                repair.PBY,
                repair.SEAWATER,
                repair.SPECIALIZED_MARINE_CAULOBACTER,
                repair.TOGO_M1749_AGAR,
                repair.TOMATO_JUICE_MILK,
            }
            else (5, ["no pH and no temperature"])
        )
        assert scorer.score_record(repaired) == expected


def test_bl_maltose_becomes_parent_wrapper() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_bl")
    target = next(target for target in repair.TARGETS if target.path == repair.BL_MALTOSE)

    repaired = repair.repair_record(_minimal_doc(target), target)

    assert repaired["ingredients"][0]["concentration"] == {"value": "5.0", "unit": "G_PER_L"}
    assert repaired["solutions"] == [
        {
            "preferred_term": "BL Agar",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "notes": "JCM Medium 418 uses 1.0 L BL Agar from JCM Medium 13.",
            "culturemech_term": {
                "id": "CultureMech:010107",
                "label": "BL Agar (Glucose Blood Liver Agar)",
            },
        }
    ]
    assert repaired["parent_media"]["path"].endswith(
        "TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml"
    )


def test_brucella_hemin_menadione_use_inline_stock_composition() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_brucella")
    target = next(target for target in repair.TARGETS if target.path == repair.BRUCELLA_JCM)

    repaired = repair.repair_record(_minimal_doc(target), target)

    assert [ingredient["preferred_term"] for ingredient in repaired["ingredients"]] == [
        "Brucella agar (BD-BBL)",
        "Horse blood",
        "Distilled water",
    ]
    assert repaired["ingredients"][1]["concentration"] == {"value": "50.0", "unit": "ML_PER_L"}
    assert [solution["preferred_term"] for solution in repaired["solutions"]] == [
        "Hemin solution",
        "Menadione solution",
    ]
    assert repaired["solutions"][0]["concentration"] == {"value": "10.0", "unit": "ML_PER_L"}
    assert repaired["solutions"][1]["concentration"] == {"value": "10.0", "unit": "ML_PER_L"}
    assert repaired["solutions"][0]["composition"][0]["preferred_term"] == "Hemin"
    assert repaired["solutions"][1]["composition"][0]["preferred_term"] == "Menadione"


def test_blood_agar_repairs_keep_official_blood_volumes() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_blood")
    targets = {target.path: target for target in repair.TARGETS}

    brucella = repair.repair_record(
        _minimal_doc(targets[repair.BRUCELLA_DSMZ]),
        targets[repair.BRUCELLA_DSMZ],
    )
    chocolate = repair.repair_record(
        _minimal_doc(targets[repair.CHOCOLATE_SHEEP_JCM]),
        targets[repair.CHOCOLATE_SHEEP_JCM],
    )
    chocolate_togo = repair.repair_record(
        _minimal_doc(targets[repair.CHOCOLATE_SHEEP_TOGO]),
        targets[repair.CHOCOLATE_SHEEP_TOGO],
    )

    assert brucella["ingredients"] == [
        {
            "preferred_term": "Brucella agar",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": "DSMZ Medium 584",
            "notes": (
                "DSMZ Medium 584 says to prepare Brucella agar, e.g. "
                "from Merck, before adding sheep blood."
            ),
            "term": {"id": "MICRO:0000595", "label": "Brucella agar"},
        },
        {
            "preferred_term": "Sheep blood",
            "concentration": {"value": "100", "unit": "ML_PER_L"},
            "source": "DSMZ Medium 584",
            "notes": "DSMZ Medium 584 adds 100 ml/L sheep blood.",
            "term": {"id": "UBERON:0000178", "label": "blood"},
        },
    ]

    for repaired in (chocolate, chocolate_togo):
        ingredients = {
            ingredient["preferred_term"]: ingredient for ingredient in repaired["ingredients"]
        }

        assert ingredients["Columbia blood agar base (BD-Difco)"]["concentration"] == {
            "value": "44.0",
            "unit": "G_PER_L",
        }
        assert "term" not in ingredients["Columbia blood agar base (BD-Difco)"]
        assert ingredients["Sheep blood"]["concentration"] == {
            "value": "50.0",
            "unit": "ML_PER_L",
        }
        assert ingredients["Distilled water"]["concentration"] == {
            "value": "950.0",
            "unit": "ML_PER_L",
        }


def test_jcm_69_becomes_parent_salt_wrapper() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_jcm69")
    targets = [
        target for target in repair.TARGETS if target.path in {repair.JCM_69, repair.JCM_69_TOGO}
    ]

    assert len(targets) == 2

    for target in targets:
        repaired = repair.repair_record(_minimal_doc(target), target)

        assert repaired["ingredients"] == [
            {
                "preferred_term": "NaCl",
                "concentration": {"value": "50.0", "unit": "G_PER_L"},
                "source": "JCM Medium 69",
                "notes": (
                    "JCM Medium 69 supplements 1.0 L GYP-sodium acetate-mineral "
                    "salts broth with 50.0 g NaCl."
                ),
                "term": {"id": "CHEBI:26710", "label": "sodium chloride"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:26710",
                    "label": "sodium chloride",
                },
            }
        ]
        assert repaired["solutions"][0]["culturemech_term"] == {
            "id": "CultureMech:003035",
            "label": "GYP-Sodium Acetate-Mineral Salts Broth",
        }
        assert repaired["parent_media"]["path"].endswith(
            "gyp_sodium_acetate_mineral_salts_broth.yaml"
        )
        assert repaired["variant_relationship"] == "SALINITY_VARIANT"


def test_dsmz_1619_glycerol_is_milliliters() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_isp7")
    target = next(target for target in repair.TARGETS if target.path == repair.ISP_7)

    repaired = repair.repair_record(_minimal_doc(target), target)

    assert repaired["ingredients"][1] == {
        "preferred_term": "Glycerol",
        "concentration": {"value": "15.00", "unit": "ML_PER_L"},
        "source": "DSMZ Medium 1619",
        "notes": "DSMZ Medium 1619 lists 15.00 ml glycerol.",
        "term": {"id": "CHEBI:17754", "label": "glycerol"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:17754", "label": "glycerol"},
    }
    assert repaired["ingredients"][2]["concentration"] == {
        "value": "1000.00",
        "unit": "ML_PER_L",
    }


def test_jcm_247_sets_explicit_ph_range() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_jcm247")
    target = next(target for target in repair.TARGETS if target.path == repair.JCM_247)

    repaired = repair.repair_record(_minimal_doc(target), target)

    assert repaired["ph_range"] == {
        "min": 6.8,
        "max": 7.0,
        "notes": "JCM Medium 247 states pH 6.8-7.0.",
    }
    assert [ingredient["preferred_term"] for ingredient in repaired["ingredients"]] == [
        "Yeast extract",
        "Glucose",
        "Distilled water",
    ]


def test_togo_nbrc_simple_recipes_keep_liter_water_units() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_togo_nbrc")
    targets = {target.path: target for target in repair.TARGETS}

    skim_milk = repair.repair_record(
        _minimal_doc(targets[repair.TOGO_M1446_SKIM_MILK]),
        targets[repair.TOGO_M1446_SKIM_MILK],
    )
    agar = repair.repair_record(
        _minimal_doc(targets[repair.TOGO_M1749_AGAR]),
        targets[repair.TOGO_M1749_AGAR],
    )

    assert [ingredient["preferred_term"] for ingredient in skim_milk["ingredients"]] == [
        "Skim milk",
        "Distilled water",
    ]
    assert skim_milk["ingredients"][0]["concentration"] == {
        "value": "100",
        "unit": "G_PER_L",
    }
    assert skim_milk["ingredients"][1]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert [ingredient["preferred_term"] for ingredient in agar["ingredients"]] == [
        "Agar",
        "Distilled water",
    ]
    assert agar["ingredients"][1]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert agar["ph_value"] == 5.5


def test_direct_agar_powder_recipes_include_water() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_agar_powders")
    targets = {target.path: target for target in repair.TARGETS}

    m05 = repair.repair_record(_minimal_doc(targets[repair.M05]), targets[repair.M05])
    reinforced = repair.repair_record(
        _minimal_doc(targets[repair.REINFORCED_CLOSTRIDIAL]),
        targets[repair.REINFORCED_CLOSTRIDIAL],
    )
    oatmeal = repair.repair_record(
        _minimal_doc(targets[repair.WEAK_OATMEAL]),
        targets[repair.WEAK_OATMEAL],
    )

    assert [ingredient["preferred_term"] for ingredient in m05["ingredients"]] == [
        "Malt extract powder",
        "Water",
        "Agar",
    ]
    assert [ingredient["preferred_term"] for ingredient in reinforced["ingredients"]] == [
        "Reinforced clostridial medium (BD-Difco)",
        "Agar",
        "Distilled water",
    ]
    assert [ingredient["preferred_term"] for ingredient in oatmeal["ingredients"]] == [
        "Oatmeal agar (BD-Difco)",
        "Agar",
        "Distilled water",
    ]
    assert m05["ingredients"][1]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert reinforced["ingredients"][2]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert oatmeal["ingredients"][2]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }


def test_late_jcm_direct_recipes_keep_official_amounts() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_late_jcm")
    targets = {target.path: target for target in repair.TARGETS}

    todd_hewitt = repair.repair_record(
        _minimal_doc(targets[repair.TODD_HEWITT_AGAR]),
        targets[repair.TODD_HEWITT_AGAR],
    )
    mrs_fructose = repair.repair_record(
        _minimal_doc(targets[repair.MRS_FRUCTOSE]),
        targets[repair.MRS_FRUCTOSE],
    )
    quarter_marine = repair.repair_record(
        _minimal_doc(targets[repair.QUARTER_MARINE]),
        targets[repair.QUARTER_MARINE],
    )
    modified_gam = repair.repair_record(
        _minimal_doc(targets[repair.MODIFIED_GAM]),
        targets[repair.MODIFIED_GAM],
    )
    modified_gam_agar = repair.repair_record(
        _minimal_doc(targets[repair.MODIFIED_GAM_AGAR]),
        targets[repair.MODIFIED_GAM_AGAR],
    )
    pby = repair.repair_record(_minimal_doc(targets[repair.PBY]), targets[repair.PBY])

    assert todd_hewitt["ingredients"][0]["concentration"] == {
        "value": "30.0",
        "unit": "G_PER_L",
    }
    assert mrs_fructose["ingredients"][0]["concentration"] == {
        "value": "55.0",
        "unit": "G_PER_L",
    }
    assert quarter_marine["ingredients"][0]["concentration"] == {
        "value": "9.35",
        "unit": "G_PER_L",
    }
    assert modified_gam["ingredients"][0]["concentration"] == {
        "value": "41.7",
        "unit": "G_PER_L",
    }
    assert [ingredient["preferred_term"] for ingredient in modified_gam_agar["ingredients"]] == [
        "GAM agar, modified (Nissui)",
        "Distilled water",
    ]
    assert modified_gam_agar["ingredients"][0]["concentration"] == {
        "value": "56.7",
        "unit": "G_PER_L",
    }
    assert [ingredient["preferred_term"] for ingredient in pby["ingredients"]] == [
        "Bacto peptone",
        "Beef extract",
        "Yeast extract",
        "Distilled water",
    ]
    assert pby["ingredients"][0]["term"] == {
        "id": "MICRO:0000178",
        "label": "Bacto peptone",
    }
    assert pby["ingredients"][1]["term"] == {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    }
    assert pby["ph_value"] == 7.0
    assert quarter_marine["parent_media"] == {
        "path": "data/normalized_yaml/bacterial/TOGO_M33_Marine_Broth_2216.yaml",
        "relationship": "CONCENTRATION_VARIANT",
        "id": "CultureMech:009718",
        "name": "marine_broth_2216",
        "notes": (
            "Uses one-quarter-strength Marine broth 2216 at 9.35 g/L instead of "
            "the full 37.4 g/L."
        ),
    }


def test_dsmz_353_and_1752_keep_ml_base_liquids() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_dsmz_liquids")
    targets = {target.path: target for target in repair.TARGETS}

    seawater = repair.repair_record(
        _minimal_doc(targets[repair.SEAWATER]),
        targets[repair.SEAWATER],
    )
    tomato = repair.repair_record(
        _minimal_doc(targets[repair.TOMATO_JUICE_MILK]),
        targets[repair.TOMATO_JUICE_MILK],
    )

    seawater_ingredients = {
        ingredient["preferred_term"]: ingredient for ingredient in seawater["ingredients"]
    }
    tomato_ingredients = {
        ingredient["preferred_term"]: ingredient for ingredient in tomato["ingredients"]
    }

    assert seawater_ingredients["Biomaris Seawater"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert seawater_ingredients["Bacto Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Bacto peptone",
    }
    assert tomato_ingredients["Tomato juice"]["concentration"] == {
        "value": "100.0",
        "unit": "ML_PER_L",
    }
    assert tomato_ingredients["Tomato juice"]["term"] == {
        "id": "FOODON:03301454",
        "label": "Tomato juice",
    }
    assert tomato_ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert tomato["ph_value"] == 7.0


def test_dsmz_601_repairs_duplicate_marine_caulobacter_imports() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_dsmz601")
    targets = {target.path: target for target in repair.TARGETS}

    bacterial = repair.repair_record(
        _minimal_doc(targets[repair.BACTERIAL_MARINE_CAULOBACTER]),
        targets[repair.BACTERIAL_MARINE_CAULOBACTER],
    )
    specialized = repair.repair_record(
        _minimal_doc(targets[repair.SPECIALIZED_MARINE_CAULOBACTER]),
        targets[repair.SPECIALIZED_MARINE_CAULOBACTER],
    )

    for repaired in (bacterial, specialized):
        ingredients = {
            ingredient["preferred_term"]: ingredient for ingredient in repaired["ingredients"]
        }

        assert repaired["ph_range"] == {
            "min": 7.2,
            "max": 7.4,
            "notes": "DSMZ Medium 601 states pH 7.2-7.4.",
        }
        assert ingredients["Yeast extract"]["term"] == {
            "id": "FOODON:03315426",
            "label": "Yeast extract",
        }
        assert ingredients["Proteose peptone (Difco 0120)"]["term"] == {
            "id": "MICRO:0000180",
            "label": "Proteose Peptone",
        }
        assert ingredients["Artificial sea water"]["concentration"] == {
            "value": "1000.0",
            "unit": "ML_PER_L",
        }


def test_non_bacterial_duplicates_and_marine_specialized_repairs() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_non_bacterial")
    targets = {target.path: target for target in repair.TARGETS}

    fungal_bl = repair.repair_record(
        _minimal_doc(targets[repair.FUNGAL_BL_MALTOSE]),
        targets[repair.FUNGAL_BL_MALTOSE],
    )
    fungal_malt = repair.repair_record(
        _minimal_doc(targets[repair.FUNGAL_DILUTE_MALT]),
        targets[repair.FUNGAL_DILUTE_MALT],
    )
    brewer = repair.repair_record(
        _minimal_doc(targets[repair.BREWER_NACL]),
        targets[repair.BREWER_NACL],
    )
    marine_cellobiose = repair.repair_record(
        _minimal_doc(targets[repair.MARINE_CELLOBIOSE]),
        targets[repair.MARINE_CELLOBIOSE],
    )

    assert fungal_bl["solutions"][0]["preferred_term"] == "BL Agar"
    assert fungal_bl["parent_media"]["id"] == "CultureMech:010107"
    assert fungal_malt["ingredients"][0]["concentration"] == {
        "value": "5.0",
        "unit": "G_PER_L",
    }
    assert brewer["ingredients"][1]["concentration"] == {
        "value": "20.0",
        "unit": "G_PER_L",
    }
    assert marine_cellobiose["ingredients"][1]["concentration"] == {
        "value": "1.0",
        "unit": "G_PER_L",
    }


def test_fungal_isp_wrappers_and_sabouraud_use_official_recipes() -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_fungal_isp")
    targets = {target.path: target for target in repair.TARGETS}

    oatmeal = repair.repair_record(
        _minimal_doc(targets[repair.FUNGAL_OATMEAL_YEAST]),
        targets[repair.FUNGAL_OATMEAL_YEAST],
    )
    isp4 = repair.repair_record(
        _minimal_doc(targets[repair.FUNGAL_ISP4_YEAST]),
        targets[repair.FUNGAL_ISP4_YEAST],
    )
    sabouraud = repair.repair_record(
        _minimal_doc(targets[repair.FUNGAL_SABOURAUD]),
        targets[repair.FUNGAL_SABOURAUD],
    )

    assert oatmeal["ingredients"] == [
        {
            "preferred_term": "Yeast extract",
            "concentration": {"value": "1.0", "unit": "G_PER_L"},
            "source": "JCM Medium 51",
            "notes": (
                "JCM Medium 51 supplements 1.0 L Oatmeal agar "
                "(ISP-3) with 1.0 g Yeast extract (BD-Difco)."
            ),
            "term": {"id": "FOODON:03315426", "label": "yeast extract"},
        }
    ]
    assert oatmeal["solutions"][0]["culturemech_term"] == {
        "id": "CultureMech:009815",
        "label": "Oatmeal Agar (ISP-3)",
    }
    assert oatmeal["parent_media"] == {
        "path": "data/normalized_yaml/bacterial/TOGO_M42_Oatmeal_Agar_ISP-3.yaml",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": "CultureMech:009815",
        "name": "oatmeal_agar_isp_3",
        "notes": (
            "Supplements 1.0 L Oatmeal agar (ISP-3) with 1.0 g/L " "Yeast extract (BD-Difco)."
        ),
    }

    assert isp4["ingredients"][0]["concentration"] == {
        "value": "0.5",
        "unit": "G_PER_L",
    }
    assert isp4["solutions"][0]["culturemech_term"] == {
        "id": "CultureMech:009900",
        "label": "Inorganic Salts-Starch Agar (ISP-4)",
    }
    assert isp4["parent_media"] == {
        "path": "data/normalized_yaml/bacterial/TOGO_M50_Inorganic_Salts-Starch_Agar_ISP-4.yaml",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": "CultureMech:009900",
        "name": "inorganic_salts_starch_agar_isp_4",
        "notes": (
            "Supplements 1.0 L Inorganic salts-starch agar (ISP-4) " "with 0.5 g/L Yeast extract."
        ),
    }

    assert [ingredient["preferred_term"] for ingredient in sabouraud["ingredients"]] == [
        "SABOURAUD-2% Glucose-Bouillon (Merck 108339)",
        "Agar",
        "Distilled water",
    ]
    assert sabouraud["ingredients"][2]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }


def test_plan_repairs_is_idempotent(tmp_path: Path) -> None:
    repair = _load_script(SCRIPT, "repair_official_simple_score20_idempotent")
    root = tmp_path / "normalized"

    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_minimal_doc(target), sort_keys=False), encoding="utf-8")

    first = repair.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    assert repair.plan_repairs(root) == first
