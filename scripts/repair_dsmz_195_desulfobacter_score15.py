#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 195 Desulfobacter stock dilution and DSM 4661 variant."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

DSMZ_195 = "bacterial/desulfobacter_curvatus_medium.yaml"
KOMODO_195 = "bacterial/desulfobacter_sp_medium.yaml"
KOMODO_195_1 = "bacterial/for_dsm_4661.yaml"

EXPECTED_IDS = {
    DSMZ_195: "CultureMech:001291",
    KOMODO_195: "CultureMech:004252",
    KOMODO_195_1: "CultureMech:004246",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_195: "mediadive.medium:195",
    KOMODO_195: "komodo.medium:195",
    KOMODO_195_1: "komodo.medium:195.1",
}

DSMZ_195_REST = "https://mediadive.dsmz.de/rest/medium/195"
DSMZ_195_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium195.pdf"
KOMODO_BASE = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)

CURATOR = "repair_dsmz_195_desulfobacter_score15.py"
ACTION = "RESOLVED_DSMZ_KOMODO_195_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"
DATA_QUALITY_FLAGS = [
    "has_ontology_mappings",
    "has_unmapped_ingredients",
    "ingredients_curated",
]
PH_RANGE = {"min": 7.1, "max": 7.4}

COMMON_FINAL_CONCENTRATIONS = {
    "Na2SO4": "2.99103",
    "KH2PO4": "0.199402",
    "NH4Cl": "0.299103",
    "NaCl": "20.9372",
    "MgCl2 x 6 H2O": "2.99103",
    "KCl": "0.498504",
    "CaCl2 x 2 H2O": "0.149551",
    "Sodium resazurin": "0.000498504",
    "Na2S x 9 H2O": "0.398804",
    "NaOH": "0.000498504",
    "Na2SeO3 x 5 H2O": "0.00000299103",
    "Na2WO4 x 2 H2O": "0.00000398804",
    "HCl": "0.00249252",
    "FeCl2 x 4 H2O": "0.00149551",
    "ZnCl2": "0.0000697906",
    "MnCl2 x 4 H2O": "0.0000997009",
    "H3BO3": "0.00000598205",
    "CoCl2 x 6 H2O": "0.000189431",
    "CuCl2 x 2 H2O": "0.00000199402",
    "NiCl2 x 6 H2O": "0.0000239282",
    "Na2MoO4 x 2 H2O": "0.0000358923",
    "Biotin": "0.0000199402",
    "Folic acid": "0.0000199402",
    "Pyridoxine hydrochloride": "0.0000997009",
    "Thiamine HCl": "0.0000498504",
    "Riboflavin": "0.0000498504",
    "Nicotinic acid": "0.0000498504",
    "Calcium D-(+)-pantothenate": "0.0000498504",
    "Vitamin B12": "0.000000997009",
    "p-Aminobenzoic acid": "0.0000498504",
    "(DL)-alpha-Lipoic acid": "0.0000498504",
}

DSMZ_FINAL_CONCENTRATIONS = COMMON_FINAL_CONCENTRATIONS | {
    "Na2CO3": "1.49551",
    "Na-acetate x 3 H2O": "2.49252",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Sparge Solution A with 80% N2/20% CO2 to pH below 6 for at least "
            "30 min, distribute it under the same gas in anoxic Hungate tubes or "
            "serum vials, and autoclave."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": (
            "Autoclave Solutions C and E separately under 100% N2. Autoclave "
            "Solution B under 80% N2/20% CO2."
        ),
    },
    {
        "step_number": 3,
        "action": "FILTER_STERILIZE",
        "description": (
            "Prepare Solution D under 100% N2 and filter-sterilize it; add "
            "Solutions B to E to sterile Solution A in the listed sequence."
        ),
    },
    {
        "step_number": 4,
        "action": "ADJUST_PH",
        "description": "Adjust the final medium to pH 7.1-7.4.",
    },
    {
        "step_number": 5,
        "action": "DISSOLVE",
        "description": (
            "For trace element solution SL-10, first dissolve FeCl2 in HCl, "
            "dilute in water, add and dissolve the other salts, and bring the "
            "solution to 1000 ml."
        ),
    },
)


@dataclass(frozen=True)
class Target:
    path: str
    source_url: str
    final_concentrations: dict[str, str]
    curation_notes: str
    replacements: dict[str, dict[str, Any]] = field(default_factory=dict)
    parent_media: dict[str, str] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, str], ...] = ()


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    term: tuple[str, str] | None,
    source: str,
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "source": source,
        "notes": notes,
        "concentration": {"value": value, "unit": "G_PER_L"},
    }
    if term is not None:
        term_mapping = _term(*term)
        row["term"] = copy.deepcopy(term_mapping)
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(term_mapping)
    return row


def _recipe_ref(path: str, relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": EXPECTED_IDS[path],
        "name": Path(path).stem,
        "notes": notes,
    }


KOMODO_BASE_PARENT = _recipe_ref(
    DSMZ_195,
    "SUBSTITUTED_COMPONENT_VARIANT",
    "KOMODO Medium 195 uses the DSMZ Medium 195 base with NaHCO3 in place of Na2CO3.",
)

KOMODO_195_1_PARENT = _recipe_ref(
    DSMZ_195,
    "SUBSTITUTED_COMPONENT_VARIANT",
    "KOMODO Medium 195.1 uses the DSMZ Medium 195 base with resorcinol for DSM 4661.",
)

DESULFOBACTER_MEDIUM_PARENT = {
    "path": "data/normalized_yaml/bacterial/desulfobacter_medium.yaml",
    "relationship": "CONCENTRATION_VARIANT",
    "id": "CultureMech:001285",
    "name": "desulfobacter_medium",
    "notes": (
        "Reviewed Desulfobacter curvatus medium as a concentration variant of "
        "Desulfobacter medium with salinity and acetate concentration axes."
    ),
}

TARGETS = (
    Target(
        path=DSMZ_195,
        source_url=DSMZ_195_REST,
        final_concentrations=DSMZ_FINAL_CONCENTRATIONS,
        curation_notes=(
            "Resolved final DSMZ Medium 195 concentrations after mixing Solutions "
            "A-E and diluted SL-10, selenite-tungstate, and Wolin vitamin stocks."
        ),
        variant_children=(
            _recipe_ref(
                KOMODO_195,
                "SUBSTITUTED_COMPONENT_VARIANT",
                "KOMODO Medium 195 substitutes 5.00 g/L NaHCO3 for DSMZ Na2CO3.",
            ),
            _recipe_ref(
                KOMODO_195_1,
                "SUBSTITUTED_COMPONENT_VARIANT",
                "KOMODO Medium 195.1 substitutes 2.50 g/L resorcinol for acetate.",
            ),
        ),
        parent_media=DESULFOBACTER_MEDIUM_PARENT,
        variant_relationship="CONCENTRATION_VARIANT",
        variant_modifications=(
            "Reviewed Desulfobacter/Desulfobacter curvatus pair; child keeps the "
            "same defined sulfate-reducer base, carbonate, sulfide, trace elements, "
            "and vitamins but raises NaCl, MgCl2, and sodium acetate concentrations.",
        ),
    ),
    Target(
        path=KOMODO_195,
        source_url=f"{KOMODO_BASE}195",
        final_concentrations=COMMON_FINAL_CONCENTRATIONS
        | {
            "NaHCO3": "5.00",
            "Na-acetate x 3 H2O": "2.50",
        },
        replacements={
            "Na2CO3": _component(
                "NaHCO3",
                "5.00",
                ("CHEBI:32139", "sodium hydrogencarbonate"),
                "KOMODO Medium 195",
                "KOMODO Medium 195 lists 5.00 g/L NaHCO3.",
            ),
            "Na-propionate": _component(
                "Na-acetate x 3 H2O",
                "2.50",
                ("CHEBI:32138", "sodium acetate trihydrate"),
                "KOMODO Medium 195",
                "KOMODO Medium 195 lists 2.50 g/L Na-acetate x 3 H2O.",
            ),
        },
        curation_notes=(
            "Resolved stock dilution and restored the KOMODO Medium 195 NaHCO3 "
            "and acetate rows."
        ),
        parent_media=KOMODO_BASE_PARENT,
        variant_relationship="SUBSTITUTED_COMPONENT_VARIANT",
        variant_modifications=(
            "Substitutes 5.00 g/L NaHCO3 for the DSMZ Medium 195 Na2CO3 stock.",
        ),
    ),
    Target(
        path=KOMODO_195_1,
        source_url=f"{KOMODO_BASE}195.1",
        final_concentrations=COMMON_FINAL_CONCENTRATIONS
        | {
            "NaHCO3": "5.00",
            "resorcinol": "2.50",
        },
        replacements={
            "Na2CO3": _component(
                "NaHCO3",
                "5.00",
                ("CHEBI:32139", "sodium hydrogencarbonate"),
                "KOMODO Medium 195.1",
                "KOMODO Medium 195.1 lists 5.00 g/L NaHCO3.",
            ),
            "Na-propionate": _component(
                "resorcinol",
                "2.50",
                None,
                "KOMODO Medium 195.1",
                "KOMODO Medium 195.1 lists 2.50 g/L resorcinol for DSM 4661.",
            ),
        },
        curation_notes=(
            "Resolved stock dilution and restored the KOMODO Medium 195.1 "
            "DSM 4661 resorcinol variant."
        ),
        parent_media=KOMODO_195_1_PARENT,
        variant_relationship="SUBSTITUTED_COMPONENT_VARIANT",
        variant_modifications=(
            "Substitutes 5.00 g/L NaHCO3 for the DSMZ Medium 195 Na2CO3 stock.",
            "Substitutes 2.50 g/L resorcinol for acetate for DSM 4661.",
        ),
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


def _add_chebi_mirror(row: dict[str, Any]) -> None:
    term = row.get("term")
    if isinstance(term, dict) and str(term.get("id") or "").startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)


def _repair_ingredients(doc: dict[str, Any], target: Target) -> list[dict[str, Any]]:
    expected_names = set(target.final_concentrations)
    expected_names.update(
        str(row["preferred_term"]) for row in target.replacements.values()
    )
    seen: set[str] = set()
    repaired: list[dict[str, Any]] = []

    for original in doc.get("ingredients", []):
        if not isinstance(original, dict):
            continue

        preferred_term = str(original.get("preferred_term") or "")
        if preferred_term in target.replacements:
            row = copy.deepcopy(target.replacements[preferred_term])
            seen.add(str(row["preferred_term"]))
        else:
            row = copy.deepcopy(original)
            value = target.final_concentrations.get(preferred_term)
            if value is not None:
                concentration = row.setdefault("concentration", {})
                if not isinstance(concentration, dict):
                    raise ValueError(f"{target.path}: {preferred_term} has malformed concentration")
                concentration["value"] = value
                concentration["unit"] = "G_PER_L"
                seen.add(preferred_term)
            _add_chebi_mirror(row)
        repaired.append(row)

    missing = expected_names - seen
    if missing:
        raise ValueError(f"{target.path}: missing expected ingredient(s): {sorted(missing)}")
    return repaired


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    seen = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (target.source_url, DSMZ_195_PDF, DSMZ_195_REST):
        if url not in seen:
            references.append({"reference": url})
            seen.add(url)


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ/KOMODO Medium 195 stock dilution and variant metadata",
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


def _set_variant_fields(repaired: dict[str, Any], target: Target) -> None:
    for field_name in ("parent_media", "variant_relationship", "variant_modifications", "variant_children"):
        repaired.pop(field_name, None)

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
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ingredients"] = _repair_ingredients(repaired, target)

    repaired.pop("ph_value", None)
    _put_after(repaired, "ph_range", copy.deepcopy(PH_RANGE), "physical_state")
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
