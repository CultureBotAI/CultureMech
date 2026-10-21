"""Independent semantic diff with explicit inversion of reviewed stock repairs."""

import collections
import copy
import hashlib
import importlib.util
import io
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
PLAN = Path(__file__).with_name("plan.json")
DSMZ2_PLAN = PLAN.parent.parent / "20261007-dsmz2-stock-boundary/plan.json"
STOCK_BATCH_PLAN = PLAN.parent.parent / "20261007-medium-stock-boundaries/plan.json"
DSMZ13_PLAN = PLAN.parent.parent / "20261007-dsmz13-stock-only/plan.json"
EXTRACTION_PLAN = PLAN.parent.parent / "20261007-extraction-boundaries/plan.json"
KOMODO12_PLAN = PLAN.parent.parent / "20261007-komodo12-extraction/plan.json"
JCM896_PLAN = PLAN.parent.parent / "20261007-jcm896-final-volume/plan.json"
JCM1105_PLAN = PLAN.parent.parent / "20261007-jcm1105-stock-boundary/plan.json"
PERCENT_PLAN = PLAN.parent.parent / "20261007-percent-supplements/plan.json"
PUBLIC_STOCK_PLAN = PLAN.parent.parent / "20261007-public-stocks/plan.json"
PUBLIC_INPUT_PLAN = PLAN.parent.parent / "20261007-public-input-basis/plan.json"
RS_PLAN = PLAN.parent.parent / "20261007-rs-stock-boundaries/plan.json"
DSMZ111_PLAN = PLAN.parent.parent / "20261007-dsmz111-preparation/plan.json"
DSMZ125_PLAN = PLAN.parent.parent / "20261007-dsmz125-alternatives/plan.json"
DSMZ265_PLAN = PLAN.parent.parent / "20261007-dsmz265-preparations/plan.json"
DSMZ467_469_PLAN = PLAN.parent.parent / "20261007-dsmz467-469-inputs/plan.json"
DSMZ489_PLAN = PLAN.parent.parent / "20261007-dsmz489-stocks/plan.json"
KOMODO_PREPARATIONS_PLAN = PLAN.parent.parent / "20261007-komodo650-752-762-preparations/plan.json"
DSMZ_PREPARATIONS_PLAN = PLAN.parent.parent / "20261007-dsmz650-752-762-preparations/plan.json"
DSMZ_STOCK_STAGES_PLAN = PLAN.parent.parent / "20261007-dsmz546-659-670-stocks/plan.json"
KOMODO670_VERSIONS_PLAN = PLAN.parent.parent / "20261007-komodo670-source-versions/plan.json"
WATER803_PLAN = PLAN.parent.parent / "20261008-dsmz803-1046-1065-water/plan.json"
STOCK1157_PLAN = PLAN.parent.parent / "20261008-dsmz1157-1164-stocks/plan.json"
TOGO_PAIRS_PLAN = PLAN.parent.parent / "20261008-togo-first-pairs/applied-plan.json"
JCM973_PLAN = PLAN.parent.parent / "20261008-jcm973-preparations/plan.json"
METHANOGEN_PLAN = PLAN.parent.parent / "20261008-togo-methanogens/plan.json"
FECL2_PLAN = PLAN.parent.parent / "20261008-fecl2-stock/plan.json"
METHANOGEN_BOUNDARIES_PLAN = PLAN.parent.parent / "20261008-methanogen-boundaries/plan.json"
JCM_STOCK_PREPARATIONS_PLAN = PLAN.parent.parent / "20261008-jcm-stock-preparations/plan.json"
J261_PLAN = PLAN.parent.parent / "20261008-j261-variant/plan.json"
M142_NESTED_PLAN = PLAN.parent.parent / "20261008-m142-nested-traces/plan.json"
EXCERPT_PLAN = PLAN.parent.parent / "20261008-recipe-reference-validator/excerpt-plan.json"
M689_PLAN = PLAN.parent.parent / "20261008-m689-stocks/plan.json"
BASAL_MAKEUP_PLAN = PLAN.parent.parent / "20261008-basal-makeup/plan.json"
PYRODICTIUM_PLAN = PLAN.parent.parent / "20261008-pyrodictium-variants/plan.json"
FILTERED_MEDIA_PLAN = PLAN.parent.parent / "20261008-filtered-sulfide-media/plan.json"
MARINE_PAIR_PLAN = PLAN.parent.parent / "20261008-marine-stock-pair/plan.json"
REDUCING_STAGES_PLAN = PLAN.parent.parent / "20261008-reducing-stages/plan.json"
M258_M260_PLAN = PLAN.parent.parent / "20261008-m258-m260-stocks/plan.json"
JCM_LB_ACIDS_PLAN = PLAN.parent.parent / "20261008-jcm-lb-acids/plan.json"
JCM_ALBUMIN_PLAN = PLAN.parent.parent / "20261008-jcm-albumin-inputs/plan.json"
ALBUMIN_COUNTERPARTS_PLAN = PLAN.parent.parent / "20261008-albumin-counterparts/plan.json"
DSMZ_ALBUMIN_PLAN = PLAN.parent.parent / "20261008-dsmz-albumin-preparations/plan.json"
BSK_FORMULATIONS_PLAN = PLAN.parent.parent / "20261008-bsk-formulations/plan.json"
LACTALBUMIN_PLAN = PLAN.parent.parent / "20261008-lactalbumin-formulations/plan.json"
MIDDLEBROOK_PLAN = PLAN.parent.parent / "20261009-middlebrook-stages/plan.json"
LINKED_MIDDLEBROOK_PLAN = PLAN.parent.parent / "20261009-middlebrook-linked/plan.json"
ALLISONELLA_PLAN = PLAN.parent.parent / "20261009-allisonella-acids/plan.json"
METHANOBACTERIUM_PLAN = PLAN.parent.parent / "20261009-methanobacterium-family/plan.json"
DESULFUROBACTERIUM_PLAN = PLAN.parent.parent / "20261009-desulfurobacterium-family/plan-v2.json"
OTEB_PLAN = PLAN.parent.parent / "20261009-oteb-family/plan.json"
RUMINOCOCCUS_PLAN = PLAN.parent.parent / "20261009-ruminococcus-albus-family/plan.json"
RUMEN_PLAN = PLAN.parent.parent / "20261009-rumen-bacteria-family/plan.json"
METHANOFOLLIS_PLAN = PLAN.parent.parent / "20261009-methanofollis-family/plan.json"
SYNTHROPHOMONAS_PLAN = PLAN.parent.parent / "20261009-synthrophomonas-family/applied-plan.json"
HALOBACTERIA_PLAN = PLAN.parent.parent / "20261009-halobacteria-family/applied-plan.json"
HALOBACTERIA_VARIANTS_PLAN = PLAN.parent.parent / "20261009-halobacteria-variants/applied-plan.json"
RESAZURIN_IDENTITY_PLAN = PLAN.parent.parent / "20261009-resazurin-stock-identity/plan.json"
MEDIUM323_PLAN = PLAN.parent.parent / "20261009-medium323/plan-v2.json"
MEDIADB_EXCEPTIONS_PLAN = PLAN.parent.parent / "20261009-mediadb-exceptions/plan.json"
KAMINSKYJ_PLAN = PLAN.parent.parent / "20261009-kaminskyj-stocks/plan.json"
M63_PLAN = PLAN.parent.parent / "20261009-m63-primary/plan-v3.json"
GEOBACTER_PLAN = PLAN.parent.parent / "20261009-geobacter-primary/plan-v2.json"
UTEX_CHEV_PLAN = PLAN.parent.parent / "20261009-utex-chev/plan.json"
UTEX_F2_PLAN = PLAN.parent.parent / "20261010-utex-f2/plan.json"
UTEX_ES_PLAN = PLAN.parent.parent / "20261010-utex-es/plan-v3.json"
UTEX_F2_FOLLOWUP_PLAN = PLAN.parent.parent / "20261010-utex-f2-followup/plan-v2.json"
UTEX_BRISTOL_BBM_PLAN = PLAN.parent.parent / "20261010-utex-bristol-bbm/plan.json"
HAJJAJ_PLAN = PLAN.parent.parent / "20261010-hajjaj-ingredients/plan.json"
YEAST_MINERAL_PLAN = PLAN.parent.parent / "20261010-yeast-mineral-ingredients/plan.json"
YEAST_CHEBI_URL_PLAN = PLAN.parent.parent / "20261010-yeast-chebi-urls/plan.json"
UTEX_MIGRATED_STOCK_PLAN = PLAN.parent.parent / "20261010-utex-migrated-stocks/plan.json"
UTEX_SEVEN_STOCK_PLAN = PLAN.parent.parent / "20261010-utex-seven-stocks/plan.json"
UTEX_J_DAS_PLAN = PLAN.parent.parent / "20261010-utex-j-das/plan.json"
UTEX_SOIL_SEAWATER_PLAN = PLAN.parent.parent / "20261010-utex-soil-seawater/plan.json"
UTEX_ORGANIC_FIVE_PLAN = PLAN.parent.parent / "20261010-utex-organic-five/plan.json"
UTEX_SIX_BLENDS_PLAN = PLAN.parent.parent / "20261010-utex-six-blends/plan.json"
UTEX_VOLVOCACEAN_BG11_PLAN = PLAN.parent.parent / "20261010-utex-volvocacean-bg11/plan-v2.json"
PAPER_CITATION_PLAN = PLAN.parent.parent / "20261015-paper-citation-successors/plan.json"
STAGE5_REMEDIATION_PLAN = (
    PLAN.parent.parent / "20261021-stage5-review-remediation-successors/plan.json"
)
counts = collections.Counter()


def walk(old, new, path):
    if old == new:
        return
    if isinstance(old, dict) and isinstance(new, dict):
        for key in old.keys() | new.keys():
            before, after = old.get(key), new.get(key)
            if key in {"evidence", "references", "curation_history"}:
                before, after = before or [], after or []
                assert after[: len(before)] == before, (
                    path,
                    key,
                    "prior provenance changed",
                )
                counts["new_" + key] += len(after) - len(before)
            elif key == "concentration":
                counts["quantity_corrections"] += before != after
            else:
                assert key in old and key in new, (path, key, "unexpected field change")
                walk(before, after, path + "." + key)
    elif isinstance(old, list) and isinstance(new, list):
        assert len(old) == len(new), (path, "unreviewed membership change")
        for index, (before, after) in enumerate(zip(old, new, strict=True)):
            walk(before, after, f"{path}[{index}]")
    else:
        raise AssertionError((path, old, new))


def provenance_counts(node):
    result = collections.Counter()
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"evidence", "references", "curation_history"}:
                result["new_" + key] += len(value)
            else:
                result.update(provenance_counts(value))
    elif isinstance(node, list):
        for value in node:
            result.update(provenance_counts(value))
    return result


def invert_review(before, after, item):
    if item.get("action") == "REGISTERED_STAGE5_REVIEW_REMEDIATION_SUCCESSOR":
        from audit_stage5_review_remediation_successor import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "REGISTERED_PAPER_CITATION_SUCCESSOR":
        from audit_paper_citation_successor import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_VOLVOCACEAN_BG11_CONCENTRATION_EVIDENCE":
        from review_utex_volvocacean_bg11 import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_SOIL_SEAWATER_INPUT_AMOUNTS_AND_OPTIONAL_CARBONATE":
        from review_utex_soil_seawater import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_ORGANIC_MEDIUM_INPUT_BASES_AND_CONCENTRATION_EVIDENCE":
        from review_utex_organic_five import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_PREPARED_BLEND_CONCENTRATION_EVIDENCE":
        from review_utex_six_blends import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_J_DAS_RECEIVING_MEDIA_EVIDENCE":
        from review_utex_j_das import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_SEVEN_STOCK_AMOUNTS_FORMS_AND_BOUNDARIES":
        from review_utex_seven_stocks import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_MIGRATED_STOCK_CONCENTRATION_EVIDENCE":
        from review_utex_migrated_stocks import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CORRECTED_CHEBI_REFERENCE_URL_ENCODING":
        from repair_yeast_chebi_references import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_YEAST_MINERAL_SOURCED_INGREDIENTS":
        from review_yeast_mineral_ingredients import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_HAJJAJ_SOURCED_INGREDIENT_AMOUNTS_AND_FORMS":
        from review_hajjaj_ingredients import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_BRISTOL_BBM_INGREDIENT_AND_PREPARATION_EVIDENCE":
        from review_utex_bristol_bbm import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_F2_VARIANT_FORMULATION_AND_NH4_RELATIONSHIP_EVIDENCE":
        from review_utex_f2_followup import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_ES_NESTED_STOCKS_AND_INGREDIENT_EVIDENCE":
        from review_utex_es_concentrations import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_F2_INGREDIENT_AND_STOCK_STAGE_EVIDENCE":
        from review_utex_f2_concentrations import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_UTEX_CHEV_BATCH_INPUTS_AND_SCOPED_EVIDENCE":
        from review_utex_chev_concentrations import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_GEOBACTER_PRIMARY_BASAL_INPUTS_AND_DONOR_EVIDENCE":
        from review_geobacter_primary_concentrations import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "CURATED_M63_PRIMARY_AMOUNTS_AND_CHEMICAL_FORMS":
        from review_m63_primary_concentrations import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "RESTORED_KAMINSKYJ_PRIMARY_RECIPE_STOCK_BOUNDARIES":
        from repair_kaminskyj_stocks import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "RESTORED_MEDIADB_INGREDIENT_MEMBERSHIP_AND_UNKNOWN_AMOUNTS":
        from repair_mediadb_ingredient_exceptions import check

        counts.update(check(before, after, item))
        return
    if item.get("action") == "RESTORED_MEDIUM323_SOURCE_SPECIFIC_INGREDIENTS":
        spec = importlib.util.spec_from_file_location(
            "medium323_ingredient_audit", MEDIUM323_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "WITHDREW_UNSUPPORTED_RESAZURIN_STOCK_PRIMARY_IDENTITIES":
        spec = importlib.util.spec_from_file_location(
            "resazurin_stock_identity_audit", RESAZURIN_IDENTITY_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CURATED_HALOBACTERIA_VARIANT_CONCENTRATIONS_AND_PREPARATION_STAGES":
        spec = importlib.util.spec_from_file_location(
            "halobacteria_variant_audit", HALOBACTERIA_VARIANTS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        assert before == yaml.load(item["before_text"], Loader=yaml.CSafeLoader)
        assert after == yaml.load(item["after_text"], Loader=yaml.CSafeLoader)
        module.check(item, applied=True, current_text=item["after_text"])
        old, new = provenance_counts(before), provenance_counts(after)
        for key in {"new_evidence", "new_references", "new_curation_history"}:
            assert new[key] >= old[key], "Prior provenance removed"
            counts[key] += new[key] - old[key]
        return
    if item.get("action") == "CURATED_HALOBACTERIA_SOURCE_CONCENTRATIONS":
        spec = importlib.util.spec_from_file_location(
            "halobacteria_audit", HALOBACTERIA_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        assert before == yaml.load(item["before_text"], Loader=yaml.CSafeLoader)
        assert after == yaml.load(item["after_text"], Loader=yaml.CSafeLoader)
        module.check(item, applied=True, current_text=item["after_text"])
        old, new = provenance_counts(before), provenance_counts(after)
        for key in {"new_evidence", "new_references", "new_curation_history"}:
            assert new[key] >= old[key], "Prior provenance removed"
            counts[key] += new[key] - old[key]
        return
    if item.get("action") == "RESTORED_SYNTHROPHOMONAS_SOURCE_FORMULATIONS_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "synthrophomonas_audit", SYNTHROPHOMONAS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.check(before, after, item)
        old, new = provenance_counts(before), provenance_counts(after)
        for key in {"new_evidence", "new_references", "new_curation_history"}:
            assert new[key] >= old[key], "Prior provenance removed"
            counts[key] += new[key] - old[key]
        return
    if item.get("action") == "RESTORED_METHANOFOLLIS_SOURCE_FORMULATIONS_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "methanofollis_audit", METHANOFOLLIS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k in {"new_evidence", "new_references", "new_curation_history"}
            }
        )
        return
    if item.get("action") == "RESTORED_RUMEN_BACTERIA_SOURCE_FORMULATIONS_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "rumen_audit", RUMEN_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k in {"new_evidence", "new_references", "new_curation_history"}
            }
        )
        return
    if item.get("action") == "RESTORED_RUMINOCOCCUS_ALBUS_SOURCE_FORMULATIONS_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "ruminococcus_albus_audit", RUMINOCOCCUS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k in {"new_evidence", "new_references", "new_curation_history"}
            }
        )
        return
    if item.get("action") == "RESTORED_OTEB_SOURCE_FORMULATIONS_AND_STOCK_SCOPES_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location("oteb_audit", OTEB_PLAN.with_name("audit.py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k in {"new_evidence", "new_references", "new_curation_history"}
            }
        )
        return
    if (
        item.get("action")
        == "RESTORED_MEDIUM_829_SOURCE_FORMULATIONS_AND_STOCK_SCOPES_WITH_EVIDENCE"
    ):
        spec = importlib.util.spec_from_file_location(
            "desulfurobacterium_audit", DESULFUROBACTERIUM_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k in {"new_evidence", "new_references", "new_curation_history"}
            }
        )
        return
    if (
        item.get("action")
        == "RESTORED_MEDIUM_119_SOURCE_FORMULATIONS_AND_STOCK_SCOPES_WITH_EVIDENCE"
    ):
        spec = importlib.util.spec_from_file_location(
            "methanobacterium_audit", METHANOBACTERIUM_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_nodes"}
            }
        )
        return
    if item.get("action") == "RESTORED_ALLISONELLA_ACID_IDENTITIES_AND_STOCK_SCOPES_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "allisonella_audit", ALLISONELLA_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_nodes"}
            }
        )
        return
    if (
        item.get("action")
        == "RESTORED_LINKED_MIDDLEBROOK_FORMULATIONS_AND_VARIANT_SCOPES_WITH_EVIDENCE"
    ):
        spec = importlib.util.spec_from_file_location(
            "linked_middlebrook_audit", LINKED_MIDDLEBROOK_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_nodes"}
            }
        )
        return
    if item.get("action") == "RESTORED_MIDDLEBROOK_INGREDIENT_AND_STOCK_SCOPES_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "middlebrook_audit", MIDDLEBROOK_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_nodes"}
            }
        )
        return
    if item.get("action") == "RESTORED_SOURCE_SPECIFIC_HYDROLYSATE_FORMULATIONS_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "lactalbumin_audit", LACTALBUMIN_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "RESTORED_SOURCE_SPECIFIC_BSK_FORMULATIONS_WITH_INGREDIENT_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "bsk_formulation_audit", BSK_FORMULATIONS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if (
        item.get("action")
        == "RESTORED_DSMZ_ALBUMIN_PREPARATIONS_AND_CONCENTRATION_SCOPES_WITH_EVIDENCE"
    ):
        spec = importlib.util.spec_from_file_location(
            "dsmz_albumin_audit", DSMZ_ALBUMIN_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if (
        item.get("action")
        == "RESTORED_ALBUMIN_COUNTERPART_IDENTITIES_AND_STOCK_CONCENTRATIONS_WITH_EVIDENCE"
    ):
        spec = importlib.util.spec_from_file_location(
            "albumin_counterparts_audit", ALBUMIN_COUNTERPARTS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "RESTORED_JCM_ALBUMIN_IDENTITIES_AND_REAGENT_INPUTS_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "jcm_albumin_audit", JCM_ALBUMIN_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "RESTORED_JCM_ACID_IDENTITIES_AND_PREPARATION_SCOPES_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "jcm_lb_acids_audit", JCM_LB_ACIDS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "REPAIRED_M258_IDENTITY_AND_M260_NESTED_STOCK_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "m258_m260_audit", M258_M260_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "RESTORED_REDUCING_AGENT_AND_STOCK_PREPARATION_SCOPES_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "reducing_stages_audit", REDUCING_STAGES_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "RESTORED_MARINE_STOCK_SCOPES_AND_BATCH_AMOUNTS_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "marine_pair_audit", MARINE_PAIR_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "RESTORED_FILTERED_MEDIA_STOCK_SCOPES_AND_BATCH_AMOUNTS_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "filtered_media_audit", FILTERED_MEDIA_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "RESTORED_PYRODICTIUM_VARIANT_AMOUNTS_AND_STOCK_SCOPES_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "pyrodictium_audit", PYRODICTIUM_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "RESTORED_BASAL_MAKEUP_AND_SUPPLEMENT_STAGES_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "basal_makeup_audit", BASAL_MAKEUP_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "RESTORED_M689_STOCK_DOSES_AND_COMPOSITIONS_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location("m689_audit", M689_PLAN.with_name("audit.py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "EXPANDED_LITERAL_RECIPE_EVIDENCE_EXCERPT":
        spec = importlib.util.spec_from_file_location(
            "excerpt_repair_audit", EXCERPT_PLAN.with_name("repair_excerpts.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "RESTORED_NESTED_M142_TRACE_STOCKS_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "m142_nested_audit", M142_NESTED_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims", "source_rows"}
            }
        )
        return
    if item.get("action") == "RESTORED_JCM261_VARIANT_FORMULATION_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location("j261_audit", J261_PLAN.with_name("audit.py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(
            {
                k: v
                for k, v in module.check(before, after, item).items()
                if k not in {"old_quantity_slots", "claims"}
            }
        )
        return
    if item.get("action") == "RESTORED_JCM_STOCK_PREPARATION_BOUNDARIES_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "jcm_stock_preparations_audit", JCM_STOCK_PREPARATIONS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.check(before, after, item)
        counts.update(
            {
                k: v
                for k, v in result.items()
                if k not in {"old_quantity_slots", "claims", "quantity_contexts_reviewed"}
            }
        )
        return
    if item.get("action") == "RESTORED_METHANOGEN_STOCK_BOUNDARIES_AND_DOSE_BASES_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "methanogen_boundaries_audit", METHANOGEN_BOUNDARIES_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "SEPARATED_FECL2_STOCK_ACID_STRENGTH_AND_BATCH_DOSE_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "fecl2_audit", FECL2_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "REPAIRED_METHANOGEN_STOCK_DOSES_AND_BASE_REFERENCE_WITH_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "methanogen_audit", METHANOGEN_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "RESTORED_JCM973_PREPARATION_STAGES_WITH_DATASET_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "jcm973_audit", JCM973_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_TOGO_JCM954_INPUT_VOLUMES_AND_STOCK_STRENGTH":
        spec = importlib.util.spec_from_file_location(
            "togo_pairs_audit", TOGO_PAIRS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_DSMZ1157_1164_STOCK_STAGES_AND_INPUTS":
        spec = importlib.util.spec_from_file_location(
            "stock1157_audit", STOCK1157_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_DSMZ803_1046_1065_WATER_INPUT_UNITS":
        spec = importlib.util.spec_from_file_location(
            "water803_audit", WATER803_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CURATED_KOMODO670_STRAIN_RECIPES_WITH_SEPARATE_SOURCE_VERSIONS":
        spec = importlib.util.spec_from_file_location(
            "komodo670_versions_audit", KOMODO670_VERSIONS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_DSMZ546_659_670_STOCK_STAGES":
        spec = importlib.util.spec_from_file_location(
            "dsmz_stock_stage_audit", DSMZ_STOCK_STAGES_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_DSMZ650_752_762_MEDIUM_AND_SOLUTION_PREPARATIONS":
        spec = importlib.util.spec_from_file_location(
            "dsmz_preparations_audit", DSMZ_PREPARATIONS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_KOMODO650_752_762_AMOUNTS_AND_PREPARATION_STAGES":
        spec = importlib.util.spec_from_file_location(
            "komodo_preparations_audit", KOMODO_PREPARATIONS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_DSMZ489_STOCK_BOUNDARIES_AND_WATER_INPUT":
        spec = importlib.util.spec_from_file_location(
            "dsmz489_semantic_audit", DSMZ489_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_DSMZ467_WATER_AND_DSMZ469_FILTERED_PREPARATIONS":
        spec = importlib.util.spec_from_file_location(
            "dsmz467_469_semantic_audit", DSMZ467_469_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "RESTORED_DSMZ265_STOCK_STAGES_AND_ORIGINAL_SOURCE_DOSES":
        spec = importlib.util.spec_from_file_location(
            "dsmz265_semantic_audit", DSMZ265_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "RESTORED_DSMZ125_ALTERNATIVE_CARBON_PREPARATIONS_AND_WATER_INPUT":
        spec = importlib.util.spec_from_file_location(
            "dsmz125_semantic_audit", DSMZ125_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "RESTORED_DSMZ111_GLUCOSE_STOCK_AND_INPUT_BASES":
        spec = importlib.util.spec_from_file_location(
            "dsmz111_semantic_audit", DSMZ111_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "RESTORED_RS_STOCK_BOUNDARIES_CARRIERS_AND_SOURCE_CONFLICTS":
        spec = importlib.util.spec_from_file_location(
            "rs_stock_semantic_audit", RS_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_PUBLIC_RECIPE_INPUT_BASES_WITH_SCOPED_EVIDENCE":
        spec = importlib.util.spec_from_file_location(
            "public_input_semantic_audit", PUBLIC_INPUT_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CURATED_PUBLIC_STOCK_CONCENTRATIONS_FROM_SCOPED_SOURCES":
        spec = importlib.util.spec_from_file_location(
            "public_stock_semantic_audit", PUBLIC_STOCK_PLAN.with_name("audit.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_DSMZ618_956_BATCH_INPUTS_AND_PERCENT_ALTERNATIVES":
        spec = importlib.util.spec_from_file_location(
            "percent_semantic_audit", PERCENT_PLAN.with_name("audit_repair.py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts.update(module.check(before, after, item))
        return
    if item.get("action") == "CORRECTED_JCM1105_ORIGINAL_RECIPE_STOCK_BOUNDARY":
        return invert_jcm1105(before, after, item)
    if item.get("action") == "CORRECTED_JCM896_ORIGINAL_RECIPE_FINAL_VOLUME":
        return invert_jcm896(before, after, item)
    if item.get("action") == "CORRECTED_KOMODO12_EXTRACTION_FROM_VERIFIED_SOURCE_LINK":
        return invert_komodo12(before, after, item)
    if item.get("action") == "CORRECTED_EXTRACTION_INPUT_BOUNDARIES":
        return invert_extraction(before, after, item)
    if "medium_id" in item:
        return invert_stock_batch(before, after, item)
    if item["id"] == "CultureMech:001399":
        return invert_dsmz2(before, after, item)
    restored = copy.deepcopy(after)
    assert restored["curation_history"][:-1] == before["curation_history"]
    assert (
        restored["curation_history"][-1]["action"]
        == "RESTORED_DSMZ1399_STOCK_BOUNDARY_AND_DROP_DOSE"
    )
    restored["curation_history"].pop()
    assert restored["references"][:-2] == before.get("references", [])
    del restored["references"][-2:]
    if "references" not in before:
        restored.pop("references")
    medium = item["id"] == "CultureMech:000252"
    if medium:
        assert len(restored["solutions"]) == 1 and len(restored["ingredients"]) == 5
        solution = restored.pop("solutions")[0]
        assert set(solution) == {
            "preferred_term",
            "term",
            "composition",
            "concentration",
        }
        assert solution["term"] == {
            "id": "mediadive.solution:2838",
            "label": "Total Salts",
        }
        assert solution["concentration"] == {"value": "0.666", "unit": "L"}
        assert len(solution["composition"]) == 9
        for water, value in (
            (restored["ingredients"].pop(), "0.333"),
            (solution["composition"].pop(), "1"),
        ):
            assert water["preferred_term"] == "Distilled water"
            assert water["concentration"] == {"value": value, "unit": "L"}
            assert water["term"] == {
                "id": "mediadive.compound:4",
                "label": "Distilled water",
            }
        restored["ingredients"][0].pop("notes")
        for node in restored["ingredients"] + solution["composition"]:
            assert len(node.pop("evidence")) == 1
        iron = solution["composition"][7]
        assert (
            "concentration" not in iron and "9 drops" in iron["notes"] and "0,5 %" in iron["notes"]
        )
        iron.pop("notes")
        iron["concentration"] = {"value": "9", "unit": "G_PER_L"}
        restored["ingredients"].extend(solution["composition"])
        assert len(restored.pop("evidence")) == 1
        counts["stock_nodes_relocated"] += 8
        counts["new_quantity_slots"] += 3
    else:
        iron = restored["composition"][7]
        assert (
            "concentration" not in iron and "9 drops" in iron["notes"] and "0,5 %" in iron["notes"]
        )
        assert len(iron.pop("evidence")) == 1
        iron.pop("notes")
        iron["concentration"] = {"value": "9", "unit": "VARIABLE"}
    counts["unsupported_quantity_slots_removed"] += 1
    assert restored == before, item["path"]
    delta = provenance_counts(after)
    delta.subtract(provenance_counts(before))
    counts.update(delta)


def invert_dsmz2(before, after, item):
    restored = copy.deepcopy(after)
    assert restored["curation_history"][:-1] == before["curation_history"]
    assert (
        restored["curation_history"].pop()["action"]
        == "RESTORED_DSMZ2_BASE_MEDIUM_AND_PREPARATION_STAGE"
    )
    assert restored["references"][:-4] == before.get("references", [])
    del restored["references"][-4:]
    if "references" not in before:
        restored.pop("references")
    assert len(restored["ingredients"]) == len(restored["solutions"]) == 1
    stock = restored.pop("solutions")[0]
    assert set(stock) == {
        "preferred_term",
        "term",
        "composition",
        "concentration",
        "preparation_notes",
    }
    assert stock["preferred_term"] == "Main sol. 1"
    assert stock["term"] == {"id": "mediadive.solution:1", "label": "Main sol. 1"}
    assert stock["concentration"] == {"value": "1", "unit": "L"}
    assert stock["preparation_notes"] == "\n\n".join(
        s["description"] for s in before["preparation_steps"][2:]
    )
    assert len(stock["composition"]) == 4
    water = stock["composition"].pop()
    assert water["preferred_term"] == "Distilled water"
    assert water["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
    assert water["concentration"] == {"value": "1", "unit": "L"}
    assert len(water["evidence"]) == 1
    restored["ingredients"].extend(stock["composition"])
    for node in restored["ingredients"]:
        assert len(node.pop("evidence")) == 1
    assert len(restored.pop("evidence")) == 1
    expected = copy.deepcopy(before["preparation_steps"][:2])
    expected[0]["action"] = "MIX"
    assert restored["preparation_steps"] == expected
    restored["preparation_steps"] = copy.deepcopy(before["preparation_steps"])
    assert restored == before, item["path"]
    counts["stock_nodes_relocated"] += 3
    counts["new_quantity_slots"] += 2
    counts["preparation_steps_relocated"] += 2
    counts["preparation_actions_corrected"] += 1
    delta = provenance_counts(after)
    delta.subtract(provenance_counts(before))
    counts.update(delta)


def invert_stock_batch(before, after, item):
    """Independently enforce a bijection of old ingredients and scoped new nodes."""
    from decimal import Decimal

    def get(pointer):
        node = after
        for key in pointer:
            node = node[key]
        return node

    reference = "https://mediadive.dsmz.de/rest/medium/" + item["medium_id"]
    originals, new_nodes, doses, stages = set(), set(), set(), []
    for claim in item["claims"]:
        pointer = claim["pointer"]
        assert get(pointer) == claim["new"]
        node = get(claim["evidence_pointer"])
        entries = [e for e in node["evidence"] if e["reference"] == reference]
        assert len(entries) == 1 and entries[0]["supports"] == "SUPPORT"
        assert claim["field"] in entries[0]["explanation"]
        assert (
            claim["snippet"] == entries[0]["snippet"]
            or claim["snippet"] in entries[0]["explanation"]
        )
        assert item["source_sha256"] in entries[0]["explanation"]
        row = json.loads(claim["snippet"])
        if claim["status"] == "correct_stage":
            assert pointer[:1] == ["solutions"] and pointer[-1] == "preparation_notes"
            assert claim["new"] == "\n\n".join(s["step"] for s in row)
            assert [s["description"] for s in claim["old"]] == [s["step"] for s in row]
            stages.extend(claim["old"])
            continue
        assert pointer[-1] == "concentration"
        if claim["status"] in {"relocate", "evidence_only"}:
            old_pointer = claim["old_pointer"]
            assert old_pointer[0] == "ingredients" and old_pointer[2:] == ["concentration"]
            index = old_pointer[1]
            assert index not in originals
            originals.add(index)
            actual = copy.deepcopy(get(pointer[:-1]))
            assert len(actual.pop("evidence")) == 1
            assert actual == before["ingredients"][index]
            assert claim["old"] == claim["new"] == actual["concentration"]
            assert actual["preferred_term"] == row["compound"]
            assert Decimal(claim["new"]["value"]) == Decimal(str(row["g_l"]))
            si = claim["source_pointer"][2]
            if claim["status"] == "relocate":
                assert pointer[:3] == ["solutions", si - 1, "composition"]
                counts["stock_nodes_relocated"] += 1
            else:
                assert si == 0 and pointer[0] == "ingredients"
            new_nodes.add(tuple(pointer[:-1]))
        else:
            assert claim["status"] == "add" and claim["old"] is None
            assert row["unit"] == "ml"
            assert claim["new"]["unit"] == "L"
            assert Decimal(claim["new"]["value"]) == Decimal(str(row["amount"])) / 1000
            if pointer[0] == "solutions" and len(pointer) == 3:
                stock = after["solutions"][pointer[1]]
                assert stock["preferred_term"] == row["solution"]
                assert stock["term"] == {
                    "id": f"mediadive.solution:{row['solution_id']}",
                    "label": row["solution"],
                }
                allowed = {"preferred_term", "term", "concentration", "composition"}
                if "preparation_notes" in stock:
                    allowed.add("preparation_notes")
                    assert any(
                        c["pointer"] == pointer[:-1] + ["preparation_notes"] for c in item["claims"]
                    )
                assert set(stock) == allowed
                assert pointer[1] not in doses
                doses.add(pointer[1])
            else:
                water = get(pointer[:-1])
                assert (row["compound_id"], row["compound"]) in {
                    (4, "Distilled water"),
                    (754, "Water"),
                }
                assert water == {
                    "preferred_term": row["compound"],
                    "term": {
                        "id": f"mediadive.compound:{row['compound_id']}",
                        "label": row["compound"],
                    },
                    "concentration": claim["new"],
                    "evidence": water["evidence"],
                }
                assert len(water["evidence"]) == 1
                new_nodes.add(tuple(pointer[:-1]))
            counts["new_quantity_slots"] += 1
    assert originals == set(range(len(before["ingredients"])))
    assert doses == set(range(len(after["solutions"])))
    actual_nodes = {("ingredients", i) for i in range(len(after["ingredients"]))}
    actual_nodes.update(
        ("solutions", si, "composition", i)
        for si, stock in enumerate(after["solutions"])
        for i in range(len(stock["composition"]))
    )
    assert new_nodes == actual_nodes
    restored = copy.deepcopy(after)
    restored["ingredients"] = copy.deepcopy(before["ingredients"])
    restored.pop("solutions")
    assert after.get("preparation_steps", []) + stages == before.get("preparation_steps", [])
    counts["preparation_steps_relocated"] += len(stages)
    if "preparation_steps" in before:
        restored["preparation_steps"] = copy.deepcopy(before["preparation_steps"])
    assert restored["evidence"][:-1] == before.get("evidence", [])
    restored["evidence"].pop()
    if "evidence" not in before:
        restored.pop("evidence")
    original_refs = before.get("references", [])
    assert restored["references"][: len(original_refs)] == original_refs
    added = restored["references"][len(original_refs) :]
    assert added and added[0]["reference"] == reference
    assert all(
        r["reference"].startswith("https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium")
        for r in added[1:]
    )
    if "references" in before:
        restored["references"] = copy.deepcopy(original_refs)
    else:
        restored.pop("references")
    event = restored["curation_history"].pop()
    assert (
        event["action"] == "RESTORED_REVIEWED_MEDIUM_STOCK_BOUNDARIES"
        and event["curator"] == "codex"
    )
    assert restored == before, item["path"]
    delta = provenance_counts(after)
    delta.subtract(provenance_counts(before))
    counts.update(delta)


def invert_extraction(before, after, item):
    restored = copy.deepcopy(after)
    mid = item["medium_id"]
    assert mid in {"12", "657"}
    assert len(restored["ingredients"]) == len(restored["solutions"]) == 1
    stock = restored.pop("solutions")[0]
    expected_keys = {
        "preferred_term",
        "source",
        "notes",
        "composition",
        "preparation_notes",
    }
    if mid == "657":
        expected_keys.add("concentration")
        assert stock["concentration"] == {"value": "1", "unit": "L"}
        assert "Make up volume to one liter." in stock["preparation_notes"]
        counts["new_quantity_slots"] += 1
    assert set(stock) == expected_keys
    assert stock["source"] == f"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{mid}.pdf"
    assert len(stock["composition"]) == 2
    restored["ingredients"] = stock["composition"] + restored["ingredients"]
    assert "concentration" not in restored["ingredients"][0]
    assert restored["ingredients"][1]["concentration"] == {"value": "1", "unit": "L"}
    assert restored["ingredients"][2]["concentration"] == before["ingredients"][2]["concentration"]
    for i, node in enumerate(restored["ingredients"]):
        prior = before["ingredients"][i]
        assert "notes" not in prior and node["notes"]
        if i == 0:
            assert "no numeric extract concentration is asserted" in node["notes"]
        assert len(node["evidence"]) == 1
        entry = node["evidence"][0]
        assert entry["reference"] == f"https://mediadive.dsmz.de/rest/medium/{mid}"
        assert entry["supports"] == "SUPPORT"
        assert json.loads(entry["snippet"])["compound"] == node["preferred_term"]
        if prior.get("evidence"):
            assert len(prior["evidence"]) == 1
            assert entry["snippet"] == prior["evidence"][0]["snippet"]
            assert entry["explanation"] != prior["evidence"][0]["explanation"]
            counts["evidence_scopes_corrected"] += 1
        for key in ("concentration", "notes", "evidence"):
            node.pop(key, None)
            if key in prior:
                node[key] = copy.deepcopy(prior[key])
        assert node == prior
    assert (
        " ".join(
            [
                stock["preparation_notes"],
                *[s["description"] for s in after["preparation_steps"]],
            ]
        )
        == before["preparation_steps"][0]["description"]
    )
    assert after["preparation_steps"][0]["action"] == "ADD_AGAR"
    assert len(after["preparation_steps"]) == (2 if mid == "12" else 1)
    restored["preparation_steps"] = copy.deepcopy(before["preparation_steps"])
    assert not before.get("evidence") and len(restored.pop("evidence")) == 1
    assert restored["references"][:-1] == before["references"]
    assert restored["references"].pop()["reference"] == stock["source"]
    assert restored["curation_history"][:-1] == before["curation_history"]
    assert restored["curation_history"].pop()["action"] == "CORRECTED_EXTRACTION_INPUT_BOUNDARIES"
    assert restored == before, item["path"]
    counts["stock_nodes_relocated"] += 2
    counts["quantity_corrections"] += 1
    counts["unsupported_quantity_slots_removed"] += 1
    counts["extraction_preparations_restructured"] += 1
    delta = provenance_counts(after)
    delta.subtract(provenance_counts(before))
    counts.update(delta)


def invert_komodo12(before, after, item):
    restored = copy.deepcopy(after)
    assert before["id"] == after["id"] == "CultureMech:004048"
    assert all(
        k not in before for k in ("solutions", "preparation_steps", "evidence", "references")
    )
    assert len(restored["ingredients"]) == len(restored["solutions"]) == 1
    stock = restored.pop("solutions")[0]
    assert set(stock) == {
        "preferred_term",
        "source",
        "notes",
        "composition",
        "preparation_notes",
    }
    assert stock["preferred_term"] == "Clarified soil extract"
    assert stock["source"] == "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium12.pdf"
    assert len(stock["composition"]) == 2
    restored["ingredients"] = stock["composition"] + restored["ingredients"]
    assert "concentration" not in restored["ingredients"][0]
    assert "400 g in 1000 ml" in restored["ingredients"][0]["notes"]
    assert restored["ingredients"][1]["concentration"] == {"value": "1", "unit": "L"}
    assert restored["ingredients"][2]["concentration"] == before["ingredients"][2]["concentration"]
    for node, prior in zip(restored["ingredients"], before["ingredients"], strict=True):
        assert "notes" not in prior and "evidence" not in prior and node["notes"]
        assert len(node["evidence"]) == 1
        entry = node.pop("evidence")[0]
        assert entry["supports"] == "SUPPORT"
        assert entry["reference"] == "https://mediadive.dsmz.de/rest/medium/12"
        assert json.loads(entry["snippet"])["compound"] == prior["preferred_term"]
        node.pop("notes")
        node["concentration"] = copy.deepcopy(prior["concentration"])
        assert node == prior
    steps = restored.pop("preparation_steps")
    assert [s["action"] for s in steps] == ["ADD_AGAR", "ADJUST_PH"]
    original_step = json.loads(item["claims"][0]["snippet"])["step"]
    assert (
        " ".join([stock["preparation_notes"], *[s["description"] for s in steps]]) == original_step
    )
    entries = restored.pop("evidence")
    assert len(entries) == 2 and len({e["reference"] for e in entries}) == 2
    assert all(e["supports"] == "SUPPORT" and e["snippet"] for e in entries)
    assert json.loads(entries[0]["snippet"])["step"] == original_step
    assert (
        entries[1]["reference"].endswith("?MediaList")
        and "DSMZ_Medium12.pdf" in entries[1]["snippet"]
    )
    assert len(restored.pop("references")) == 3
    assert restored["curation_history"][:-1] == before["curation_history"]
    assert restored["curation_history"].pop()["action"] == item["action"]
    assert restored == before
    counts["stock_nodes_relocated"] += 2
    counts["quantity_corrections"] += 1
    counts["unsupported_quantity_slots_removed"] += 1
    counts["extraction_preparations_added"] += 1
    delta = provenance_counts(after)
    delta.subtract(provenance_counts(before))
    counts.update(delta)


def invert_jcm896(before, after, item):
    restored = copy.deepcopy(after)
    reference = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=896"
    source_sha = "c6e814a8bff1580ddd42179b7d401a204ae19469786fdafd140408d1522f03c8"
    assert item["id"] == "CultureMech:003244" and item["source_sha256"] == source_sha
    assert len(restored["ingredients"]) == 11 and len(item["claims"]) == 13
    amounts = [
        "3.0",
        "0.35",
        "2.5",
        "0.4",
        "0.2",
        "1.1",
        "5.2",
        "1.0",
        "25.0",
        "2.5",
        "40.0",
    ]
    for index, amount in enumerate(amounts):
        node = restored["ingredients"][index]
        expected = {
            "value": format(Decimal(amount) / Decimal("0.584"), ".6g"),
            "unit": "ML_PER_L" if index == 10 else "G_PER_L",
        }
        assert node["concentration"] == expected
        entries = node.pop("evidence")
        assert len(entries) == 1
        evidence = entries[0]
        assert evidence["reference"] == reference and evidence["supports"] == "SUPPORT"
        assert evidence["snippet"].endswith(f" {amount} " + ("ml" if index == 10 else "g"))
        assert f"ingredients[{index}].concentration" in evidence["explanation"]
        assert "fill up to 584 ml with distilled water" in evidence["explanation"]
        assert source_sha in evidence["explanation"]
        node["concentration"] = copy.deepcopy(before["ingredients"][index]["concentration"])
        if index == 7:
            assert node["preferred_term"] == "TC Yeastolate (BD-Difco)"
            assert evidence["snippet"] == "TC Yeastolate (BD-Difco) 1.0 g"
            assert "ingredients[7].preferred_term" in evidence["explanation"]
            node["preferred_term"] = before["ingredients"][index]["preferred_term"]
    expected_preparation = (
        "Adjust pH to 7.2 with NaOH, fill up to 584 ml with distilled water "
        "and filter-sterilize with 0.22 \u00b5m PES filter."
    )
    assert restored["preparation_steps"][0]["description"] == expected_preparation
    restored["preparation_steps"][0]["description"] = before["preparation_steps"][0]["description"]
    entries = restored.pop("evidence")
    assert len(entries) == 1 and entries[0]["reference"] == reference
    assert entries[0]["snippet"] == expected_preparation and entries[0]["supports"] == "SUPPORT"
    assert "preparation_steps[0].description" in entries[0]["explanation"]
    references = restored.pop("references")
    assert len(references) == 1 and references[0]["reference"] == reference
    assert source_sha in references[0]["notes"]
    assert restored["curation_history"][:-1] == before["curation_history"]
    event = restored["curation_history"].pop()
    assert event["action"] == item["action"] and event["curator"] == "codex"
    assert restored == before
    counts["quantity_corrections"] += 11
    counts["ingredient_labels_corrected"] += 1
    counts["preparation_text_encodings_corrected"] += 1
    delta = provenance_counts(after)
    delta.subtract(provenance_counts(before))
    assert (
        delta["new_evidence"] == 12
        and delta["new_references"] == delta["new_curation_history"] == 1
    )
    counts.update(delta)


def invert_jcm1105(before, after, item):
    restored = copy.deepcopy(after)
    reference = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1105"
    source_sha = "2c7d8a4ae523578495afb0f7de58f4185a15a9cd5a489e938f46602d714356f8"
    makeup = "Add components to distilled water and bring volume to 1.0 L."
    optional = "For preparation of solid medium, add 20.0 g/L agar."
    addition = "After autoclaving, add the following solution (autoclaved):"
    assert item["id"] == "CultureMech:002283" and item["source_sha256"] == source_sha
    assert item["path"] == "data/normalized_yaml/bacterial/virgibacillus_merv_medium.yaml"
    assert len(item["claims"]) == 11
    assert collections.Counter(c["status"] for c in item["claims"]) == {
        "correct": 5,
        "remove_unsupported": 1,
        "add": 2,
        "correct_stage": 2,
        "add_stage": 1,
    }
    assert restored["ingredients"] == []
    base, carbonate = restored.pop("solutions")
    components = base.pop("composition")
    stock_nodes = carbonate.pop("composition")
    assert len(components) == 5 and len(stock_nodes) == 1
    assert base == {
        "preferred_term": "JCM 1105 base solution",
        "concentration": {"value": "1", "unit": "L"},
        "notes": "The complete 1.0 L prepared base is used per recipe batch; this is not a final-medium volume or per-liter working dose.",
        "preparation_notes": f"{makeup} {optional}",
    }
    assert carbonate == {
        "preferred_term": "10% Na2CO3 solution",
        "concentration": {"value": "0.010", "unit": "L"},
        "notes": "Add 10.0 ml per recipe batch after autoclaving the 1.0 L base. The percentage basis and final-medium volume are not specified.",
        "preparation_notes": "Autoclave the carbonate solution before adding it to the autoclaved base.",
    }
    quotes = [
        "Yeast extract 10.0 g",
        "Trisodium citrate\u00b73H2O 3.0 g",
        "MgSO4\u00b77H2O 1.0 g",
        "KCl 3.0 g",
        "NaCl 100.0 g",
    ]
    for index, (node, amount) in enumerate(
        zip(components, ("10", "3", "1", "3", "100"), strict=True)
    ):
        assert node["concentration"] == {"value": amount, "unit": "G_PER_L"}
        assert Decimal(amount) * Decimal("1.0") == Decimal(quotes[index].split()[-2])
        (evidence,) = node.pop("evidence")
        assert evidence["reference"] == reference and evidence["supports"] == "SUPPORT"
        assert evidence["snippet"] == quotes[index]
        assert f"solutions[0].composition[{index}].concentration" in evidence["explanation"]
        assert makeup in evidence["explanation"] and source_sha in evidence["explanation"]
        node["concentration"] = copy.deepcopy(before["ingredients"][index]["concentration"])
        assert node == before["ingredients"][index]
    node = stock_nodes[0]
    assert "concentration" not in node
    assert node.pop("notes") == (
        "Original JCM 1105 specifies a 10% Na2CO3 solution without its percentage basis. "
        "The 10.0 ml addition is a stock dose, not 10 g/L carbonate. No numeric stock "
        "or final-medium carbonate concentration is asserted."
    )
    (evidence,) = node.pop("evidence")
    assert evidence["reference"] == reference and evidence["supports"] == "SUPPORT"
    assert evidence["snippet"] == "10% Na2CO3 solution 10.0 ml"
    assert "solutions[1].composition[0].concentration" in evidence["explanation"]
    assert "solutions[1].composition[0].notes" in evidence["explanation"]
    assert source_sha in evidence["explanation"]
    node["concentration"] = copy.deepcopy(before["ingredients"][5]["concentration"])
    assert node == before["ingredients"][5]
    restored["ingredients"] = components + stock_nodes
    assert restored["preparation_steps"][0]["description"] == (
        "Autoclave the prepared 1.0 L base. After autoclaving, add 10.0 ml of the "
        "autoclaved 10% Na2CO3 solution."
    )
    restored["preparation_steps"][0]["description"] = before["preparation_steps"][0]["description"]
    (evidence,) = restored.pop("evidence")
    assert evidence["reference"] == reference and evidence["supports"] == "SUPPORT"
    assert evidence["snippet"] == makeup and source_sha in evidence["explanation"]
    assert f"{makeup} {optional} {addition}" in evidence["explanation"]
    assert "10% Na2CO3 solution 10.0 ml" in evidence["explanation"]
    for field in (
        "solutions[0].concentration",
        "solutions[1].concentration",
        "solutions[0].preparation_notes",
        "solutions[1].preparation_notes",
        "preparation_steps[0].description",
    ):
        assert field in evidence["explanation"]
    (ref,) = restored.pop("references")
    assert ref["reference"] == reference and ref["title"] == "JCM 1105: VIRGIBACILLUS MERV MEDIUM"
    assert source_sha in ref["notes"] and "source_type=culture_collection_page" in ref["notes"]
    event = restored["curation_history"].pop()
    assert event["action"] == item["action"] and event["curator"] == "codex"
    assert restored == before
    counts["quantity_corrections"] += 5
    counts["stock_nodes_relocated"] += 6
    counts["unsupported_quantity_slots_removed"] += 1
    counts["new_quantity_slots"] += 2
    counts["preparation_steps_relocated"] += 1
    counts["preparation_descriptions_corrected"] += 1
    counts["stock_preparation_notes_added"] += 1
    delta = provenance_counts(after)
    delta.subtract(provenance_counts(before))
    assert (
        delta["new_evidence"] == 7 and delta["new_references"] == delta["new_curation_history"] == 1
    )
    counts.update(delta)


def invert_chain(raw, items):
    """Invert every applied, hash-linked repair; reject disconnected or ambiguous history."""
    edges = {}
    for item in items:
        after = item["after_sha256"]
        assert after not in edges, "Ambiguous repair result"
        if "after_text" in item:
            assert hashlib.sha256(item["after_text"].encode()).hexdigest() == after
        assert hashlib.sha256(item["before_text"].encode()).hexdigest() == item["before_sha256"]
        assert after != item["before_sha256"], "No-op repair edge"
        edges[after] = item
    seen = set()
    current = yaml.load(raw, Loader=yaml.CSafeLoader)
    while hashlib.sha256(raw).hexdigest() in edges:
        digest = hashlib.sha256(raw).hexdigest()
        assert digest not in seen, "Cyclic repair history"
        seen.add(digest)
        item = edges[digest]
        assert current["id"] == item["id"], "Repair identity drift"
        before = yaml.load(item["before_text"], Loader=yaml.CSafeLoader)
        assert before["id"] == current["id"], "Repair baseline identity drift"
        invert_review(before, current, item)
        raw, current = item["before_text"].encode(), before
    assert len(seen) == len(items), "Unapplied or disconnected repair history"
    return current


def review_plans():
    """Applied repair registry shared by cumulative and batch provenance checks."""
    return (
        PLAN,
        DSMZ2_PLAN,
        STOCK_BATCH_PLAN,
        DSMZ13_PLAN,
        EXTRACTION_PLAN,
        KOMODO12_PLAN,
        JCM896_PLAN,
        JCM1105_PLAN,
        PERCENT_PLAN,
        PUBLIC_STOCK_PLAN,
        PUBLIC_INPUT_PLAN,
        RS_PLAN,
        DSMZ111_PLAN,
        DSMZ125_PLAN,
        DSMZ265_PLAN,
        DSMZ467_469_PLAN,
        DSMZ489_PLAN,
        KOMODO_PREPARATIONS_PLAN,
        DSMZ_PREPARATIONS_PLAN,
        DSMZ_STOCK_STAGES_PLAN,
        KOMODO670_VERSIONS_PLAN,
        WATER803_PLAN,
        STOCK1157_PLAN,
        TOGO_PAIRS_PLAN,
        JCM973_PLAN,
        METHANOGEN_PLAN,
        FECL2_PLAN,
        METHANOGEN_BOUNDARIES_PLAN,
        JCM_STOCK_PREPARATIONS_PLAN,
        J261_PLAN,
        M142_NESTED_PLAN,
        EXCERPT_PLAN,
        M689_PLAN,
        BASAL_MAKEUP_PLAN,
        PYRODICTIUM_PLAN,
        FILTERED_MEDIA_PLAN,
        MARINE_PAIR_PLAN,
        REDUCING_STAGES_PLAN,
        M258_M260_PLAN,
        JCM_LB_ACIDS_PLAN,
        JCM_ALBUMIN_PLAN,
        ALBUMIN_COUNTERPARTS_PLAN,
        DSMZ_ALBUMIN_PLAN,
        BSK_FORMULATIONS_PLAN,
        LACTALBUMIN_PLAN,
        MIDDLEBROOK_PLAN,
        LINKED_MIDDLEBROOK_PLAN,
        ALLISONELLA_PLAN,
        METHANOBACTERIUM_PLAN,
        DESULFUROBACTERIUM_PLAN,
        OTEB_PLAN,
        RUMINOCOCCUS_PLAN,
        RUMEN_PLAN,
        METHANOFOLLIS_PLAN,
        SYNTHROPHOMONAS_PLAN,
        HALOBACTERIA_PLAN,
        HALOBACTERIA_VARIANTS_PLAN,
        RESAZURIN_IDENTITY_PLAN,
        MEDIUM323_PLAN,
        MEDIADB_EXCEPTIONS_PLAN,
        KAMINSKYJ_PLAN,
        M63_PLAN,
        GEOBACTER_PLAN,
        UTEX_CHEV_PLAN,
        UTEX_F2_PLAN,
        UTEX_ES_PLAN,
        UTEX_F2_FOLLOWUP_PLAN,
        UTEX_BRISTOL_BBM_PLAN,
        HAJJAJ_PLAN,
        YEAST_MINERAL_PLAN,
        YEAST_CHEBI_URL_PLAN,
        UTEX_MIGRATED_STOCK_PLAN,
        UTEX_SEVEN_STOCK_PLAN,
        UTEX_J_DAS_PLAN,
        UTEX_SOIL_SEAWATER_PLAN,
        UTEX_ORGANIC_FIVE_PLAN,
        UTEX_SIX_BLENDS_PLAN,
        UTEX_VOLVOCACEAN_BG11_PLAN,
        PAPER_CITATION_PLAN,
        STAGE5_REMEDIATION_PLAN,
    )


def main():
    followups = collections.defaultdict(list)
    for p in review_plans():
        for record in json.loads(p.read_text())["records"]:
            followups[record["path"]].append(record)
    paths = [
        p
        for p in subprocess.check_output(
            ["git", "diff", "--name-only", "-z", "--", "data/normalized_yaml"], cwd=ROOT
        )
        .decode()
        .split("\0")
        if p.endswith(".yaml")
    ]
    stream = io.BytesIO(
        subprocess.check_output(
            ["git", "cat-file", "--batch"],
            cwd=ROOT,
            input="".join("HEAD:" + p + "\n" for p in paths).encode(),
        )
    )
    for path in paths:
        _, kind, size = stream.readline().split()
        assert kind == b"blob"
        original = stream.read(int(size))
        assert stream.read(1) == b"\n"
        old = yaml.load(original, Loader=yaml.CSafeLoader)
        raw = (ROOT / path).read_bytes()
        current = yaml.load(raw, Loader=yaml.CSafeLoader)
        if path in followups:
            before = invert_chain(raw, followups[path])
            walk(old, before, path)
        else:
            walk(old, current, path)
    assert stream.read() == b""
    counts["edited_records"] = len(paths)
    print(json.dumps(dict(counts), indent=2))


if __name__ == "__main__":
    main()
