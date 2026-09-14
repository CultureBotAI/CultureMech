#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 141 Methanogenium exact and strain variants."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

DSMZ_141 = "archaea/methanogenium_medium_h2_co2.yaml"
KOMODO_141 = "archaea/KOMODO_141_METHANOGENIUM_medium.yaml"
KOMODO_141_3 = "bacterial/for_dsm_2095.yaml"
KOMODO_141_5 = "bacterial/for_dsm_2373.yaml"
KOMODO_141_6 = "bacterial/for_dsm_2831.yaml"
KOMODO_141_7 = "bacterial/for_dsm_4254.yaml"
KOMODO_141_8 = "bacterial/for_dsm_14042.yaml"
KOMODO_141_11 = "bacterial/for_dsm_21626.yaml"

EXPECTED_IDS = {
    DSMZ_141: "CultureMech:000254",
    KOMODO_141: "CultureMech:004144",
    KOMODO_141_3: "CultureMech:004132",
    KOMODO_141_5: "CultureMech:004135",
    KOMODO_141_6: "CultureMech:004136",
    KOMODO_141_7: "CultureMech:004139",
    KOMODO_141_8: "CultureMech:004140",
    KOMODO_141_11: "CultureMech:004124",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_141: "mediadive.medium:141",
    KOMODO_141: "komodo.medium:141",
    KOMODO_141_3: "komodo.medium:141.3",
    KOMODO_141_5: "komodo.medium:141.5",
    KOMODO_141_6: "komodo.medium:141.6",
    KOMODO_141_7: "komodo.medium:141.7",
    KOMODO_141_8: "komodo.medium:141.8",
    KOMODO_141_11: "komodo.medium:141.11",
}

DSMZ_141_REST = "https://mediadive.dsmz.de/rest/medium/141"
DSMZ_141_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"
KOMODO_BASE = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)

CURATOR = "repair_dsmz_141_methanogenium_score15.py"
ACTION = "RESOLVED_DSMZ_KOMODO_141_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"
DATA_QUALITY_FLAGS = [
    "has_ontology_mappings",
    "has_unmapped_ingredients",
    "ingredients_curated",
]
PH_RANGE = {"min": 6.8, "max": 7.0}

BASE_FINAL_CONCENTRATIONS = {
    "MgSO4 x 7 H2O": "3.43535",
    "CaCl2 x 2 H2O": "0.13919",
    "NaCl": "17.7789",
    "Nitrilotriacetic acid": "0.0148075",
    "MnSO4 x H2O": "0.00493583",
    "FeSO4 x 7 H2O": "0.000987167",
    "CoSO4 x 7 H2O": "0.0017769",
    "ZnSO4 x 7 H2O": "0.0017769",
    "CuSO4 x 5 H2O": "0.0000987167",
    "AlK(SO4)2 x 12 H2O": "0.000197433",
    "H3BO3": "0.0000987167",
    "Na2MoO4 x 2 H2O": "0.0000987167",
    "NiCl2 x 6 H2O": "0.00029615",
    "Na2SeO3 x 5 H2O": "0.0000029615",
    "Na2WO4 x 2 H2O": "0.00000394867",
    "Biotin": "0.0000197433",
    "Folic acid": "0.0000197433",
    "Pyridoxine hydrochloride": "0.0000987167",
    "Thiamine HCl": "0.0000493583",
    "Riboflavin": "0.0000493583",
    "Nicotinic acid": "0.0000493583",
    "Calcium D-(+)-pantothenate": "0.0000493583",
    "Vitamin B12": "0.000000987167",
    "p-Aminobenzoic acid": "0.0000493583",
    "(DL)-alpha-Lipoic acid": "0.0000493583",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": (
            "DSMZ Medium 141 notes that, when the medium is used without overpressure, "
            "pH should be adjusted with a small amount of sterile anoxic 1 N HCl if needed."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": (
            "Dissolve ingredients except bicarbonate, vitamins, cysteine, and sulfide; "
            "sparge with 80% H2/20% CO2 for 30-45 min, add bicarbonate and adjust pH "
            "to 6.5, dispense under 80% H2/20% CO2 into anoxic Hungate tubes or serum "
            "vials to 30% of volume, and autoclave."
        ),
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "After sterilization, add cysteine and sulfide from sterile anoxic stocks "
            "autoclaved under 100% N2. Prepare vitamins under 100% N2 and filter-sterilize "
            "them before addition."
        ),
    },
    {
        "step_number": 4,
        "action": "ADJUST_PH",
        "description": (
            "Adjust the complete medium to pH 6.8-7.0 if necessary, and incubate under "
            "sterile 80% H2/20% CO2 at two atmospheres of pressure."
        ),
    },
    {
        "step_number": 5,
        "action": "ADJUST_PH",
        "description": (
            "For the Modified Wolin's mineral solution, first dissolve nitrilotriacetic "
            "acid and adjust pH to 6.5 with KOH, add minerals, and adjust final pH to "
            "7.0 with KOH."
        ),
    },
)


@dataclass(frozen=True)
class Target:
    path: str
    source_label: str
    source_url: str
    curation_notes: str
    parent_media: dict[str, str] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, str], ...] = ()
    ph_value: float | None = None
    concentration_overrides: dict[str, str] | None = None
    add_l_histidine: bool = False


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _recipe_ref(path: str, relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": EXPECTED_IDS[path],
        "name": Path(path).stem,
        "notes": notes,
    }


DSMZ_141_PARENT = _recipe_ref(
    DSMZ_141,
    "STRAIN_SPECIFIC_VARIANT",
    "DSMZ Medium 141 is the official Methanogenium medium.",
)

DSMZ_141_SOURCE_PARENT = _recipe_ref(
    DSMZ_141,
    "SOURCE_DUPLICATE",
    "KOMODO Medium 141 is a source-catalogue duplicate of DSMZ Medium 141.",
)


KOMODO_CHILDREN = (
    _recipe_ref(
        KOMODO_141,
        "SOURCE_DUPLICATE",
        "KOMODO Medium 141 is a source-catalogue duplicate of DSMZ Medium 141.",
    ),
    _recipe_ref(
        KOMODO_141_3,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 141.3 applies DSMZ Medium 141 to DSM 2095.",
    ),
    _recipe_ref(
        KOMODO_141_5,
        "STRAIN_SPECIFIC_VARIANT",
        "DSMZ Medium 141 for DSM 2373 increases Trypticase peptone to 6.00 g/L.",
    ),
    _recipe_ref(
        KOMODO_141_6,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 141.6 applies DSMZ Medium 141 to DSM 2831.",
    ),
    _recipe_ref(
        KOMODO_141_7,
        "STRAIN_SPECIFIC_VARIANT",
        "DSMZ Medium 141 for DSM 4254 adds 0.08 g/L L-histidine.",
    ),
    _recipe_ref(
        KOMODO_141_8,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 141.8 applies DSMZ Medium 141 to DSM 14042.",
    ),
    _recipe_ref(
        KOMODO_141_11,
        "STRAIN_SPECIFIC_VARIANT",
        "DSMZ Medium 141 for DSM 21626 reduces NaCl to 6.00 g/L.",
    ),
)

TARGETS = (
    Target(
        path=DSMZ_141,
        source_label="DSMZ Medium 141",
        source_url=DSMZ_141_REST,
        curation_notes=(
            "Resolved diluted Modified Wolin trace-element and Wolin vitamin stock "
            "concentrations and added reviewed KOMODO 141 variants."
        ),
        variant_children=KOMODO_CHILDREN,
    ),
    Target(
        path=KOMODO_141,
        source_label="KOMODO Medium 141",
        source_url=f"{KOMODO_BASE}141",
        curation_notes=(
            "Resolved diluted Modified Wolin trace-element and Wolin vitamin stock "
            "concentrations for the KOMODO Medium 141 source duplicate."
        ),
        parent_media=DSMZ_141_SOURCE_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=("KOMODO source-catalogue duplicate of DSMZ Medium 141.",),
    ),
    Target(
        path=KOMODO_141_3,
        source_label="KOMODO Medium 141.3",
        source_url=f"{KOMODO_BASE}141.3",
        curation_notes="Linked the DSM 2095 KOMODO wrapper under DSMZ Medium 141.",
        parent_media=DSMZ_141_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Applies the DSMZ Medium 141 formulation to DSM 2095.",
        ),
    ),
    Target(
        path=KOMODO_141_5,
        source_label="KOMODO Medium 141.5",
        source_url=f"{KOMODO_BASE}141.5",
        curation_notes="Applied the DSMZ Medium 141 DSM 2373 trypticase increase.",
        parent_media=DSMZ_141_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=("Increases Trypticase peptone to 6.00 g/L for DSM 2373.",),
        ph_value=7.0,
        concentration_overrides={"Trypticase peptone": "6.00"},
    ),
    Target(
        path=KOMODO_141_6,
        source_label="KOMODO Medium 141.6",
        source_url=f"{KOMODO_BASE}141.6",
        curation_notes="Linked the DSM 2831 KOMODO wrapper under DSMZ Medium 141.",
        parent_media=DSMZ_141_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Applies the DSMZ Medium 141 formulation to DSM 2831.",
        ),
    ),
    Target(
        path=KOMODO_141_7,
        source_label="KOMODO Medium 141.7",
        source_url=f"{KOMODO_BASE}141.7",
        curation_notes="Applied the DSMZ Medium 141 DSM 4254 L-histidine supplement.",
        parent_media=DSMZ_141_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=("Adds 0.08 g/L L-histidine for DSM 4254.",),
        add_l_histidine=True,
    ),
    Target(
        path=KOMODO_141_8,
        source_label="KOMODO Medium 141.8",
        source_url=f"{KOMODO_BASE}141.8",
        curation_notes="Linked the DSM 14042 KOMODO wrapper under DSMZ Medium 141.",
        parent_media=DSMZ_141_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Applies the DSMZ Medium 141 formulation to DSM 14042.",
        ),
    ),
    Target(
        path=KOMODO_141_11,
        source_label="KOMODO Medium 141.11",
        source_url=f"{KOMODO_BASE}141.11",
        curation_notes="Applied the DSMZ Medium 141 DSM 21626 NaCl reduction.",
        parent_media=DSMZ_141_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=("Reduces NaCl to 6.00 g/L for DSM 21626.",),
        concentration_overrides={"NaCl": "6.00"},
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value
    doc.clear()
    doc.update(updated)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    term = media_term.get("term") if isinstance(media_term, dict) else {}
    return str(term.get("id") or "") if isinstance(term, dict) else ""


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != EXPECTED_IDS[target.path]:
        raise ValueError(f"{target.path}: found id {doc.get('id')!r}, expected {EXPECTED_IDS[target.path]!r}")
    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[target.path]:
        raise ValueError(
            f"{target.path}: found source term {source_term!r}, expected "
            f"{EXPECTED_SOURCE_TERMS[target.path]!r}"
        )


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    seen = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (target.source_url, DSMZ_141_PDF, DSMZ_141_REST):
        if url not in seen:
            references.append({"reference": url})
            seen.add(url)


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ/KOMODO Medium 141 stock dilution and variant metadata",
        "source": target.source_url,
        "notes": target.curation_notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.path}: curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _add_chebi_mirror(row: dict[str, Any]) -> None:
    term = row.get("term")
    if isinstance(term, dict) and str(term.get("id") or "").startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)


def _l_histidine() -> dict[str, Any]:
    term = _term("CHEBI:15971", "L-histidine")
    return {
        "preferred_term": "L-histidine",
        "term": copy.deepcopy(term),
        "source": "DSMZ Medium 141; KOMODO Medium 141.7",
        "notes": "DSMZ Medium 141 specifies adding L-histidine to 80 mg/L for DSM 4254.",
        "concentration": {
            "value": "0.08",
            "unit": "G_PER_L",
        },
        "mediaingredientmech_chebi_term": copy.deepcopy(term),
    }


def _repair_ingredients(doc: dict[str, Any], target: Target) -> list[dict[str, Any]]:
    overrides = target.concentration_overrides or {}
    expected_names = set(BASE_FINAL_CONCENTRATIONS) | set(overrides)
    seen = set()
    repaired = []

    for original in doc.get("ingredients", []):
        if not isinstance(original, dict):
            continue
        if original.get("preferred_term") == "L-histidine":
            continue

        row = copy.deepcopy(original)
        preferred_term = str(row.get("preferred_term") or "")
        value = overrides.get(preferred_term, BASE_FINAL_CONCENTRATIONS.get(preferred_term))
        if value is not None:
            concentration = row.setdefault("concentration", {})
            if not isinstance(concentration, dict):
                raise ValueError(f"{target.path}: {preferred_term} has malformed concentration")
            concentration["value"] = value
            concentration["unit"] = "G_PER_L"
            row.pop("notes", None)
            seen.add(preferred_term)
        _add_chebi_mirror(row)

        repaired.append(row)
        if target.add_l_histidine and preferred_term == "CuSO4 x 5 H2O":
            repaired.append(_l_histidine())

    missing = expected_names - seen
    if missing:
        raise ValueError(f"{target.path}: missing expected ingredient(s): {sorted(missing)}")
    return repaired


def _set_variant_fields(repaired: dict[str, Any], target: Target) -> None:
    for field in ("parent_media", "variant_relationship", "variant_modifications", "variant_children"):
        repaired.pop(field, None)

    after = "references"
    if target.parent_media is not None:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), after)
        after = "parent_media"
    if target.variant_relationship is not None:
        _put_after(repaired, "variant_relationship", target.variant_relationship, after)
        after = "variant_relationship"
    if target.variant_modifications:
        _put_after(repaired, "variant_modifications", list(target.variant_modifications), after)
        after = "variant_modifications"
    if target.variant_children:
        _put_after(repaired, "variant_children", [copy.deepcopy(row) for row in target.variant_children], after)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ingredients"] = _repair_ingredients(repaired, target)

    if target.ph_value is None:
        repaired.pop("ph_value", None)
        _put_after(repaired, "ph_range", copy.deepcopy(PH_RANGE), "physical_state")
    else:
        repaired.pop("ph_range", None)
        _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "ingredients")
    _put_after(repaired, "data_quality_flags", list(DATA_QUALITY_FLAGS), "preparation_steps")

    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
    _put_after(repaired, "references", repaired["references"], "data_quality_flags")
    _set_variant_fields(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
        for target in TARGETS
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
        if args.apply:
            changed = write_record(path, doc)
        else:
            changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
