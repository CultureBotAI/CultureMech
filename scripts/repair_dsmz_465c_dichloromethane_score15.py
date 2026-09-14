#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 465c dichloromethane mineral-medium variants."""

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

DSMZ_465C = "bacterial/mineral_medium_with_dichloromethane.yaml"
KOMODO_465C = "bacterial/KOMODO_465c_MINERAL_MEDIUM_WITH_DICHLOROMETHANE.yaml"
KOMODO_465C_1 = "bacterial/for_dsm_6813.yaml"
KOMODO_465 = "bacterial/KOMODO_465_MINERAL_MEDIUM_PH_7.25.yaml"

EXPECTED_IDS = {
    DSMZ_465C: "CultureMech:001588",
    KOMODO_465C: "CultureMech:005571",
    KOMODO_465C_1: "CultureMech:005570",
    KOMODO_465: "CultureMech:005566",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_465C: "mediadive.medium:465c",
    KOMODO_465C: "komodo.medium:465c",
    KOMODO_465C_1: "komodo.medium:465c.1",
    KOMODO_465: "komodo.medium:465",
}

DSMZ_465C_REST = "https://mediadive.dsmz.de/rest/medium/465c"
DSMZ_465C_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium465c.pdf"
KOMODO_BASE = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)

CURATOR = "repair_dsmz_465c_dichloromethane_score15.py"
ACTION = "RESOLVED_DSMZ_KOMODO_465C_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"
DATA_QUALITY_FLAGS = [
    "has_ontology_mappings",
    "ingredients_curated",
]
PH_VALUE = 7.25

MAIN_CONCENTRATIONS = {
    "Na2HPO4 x 2 H2O": "3.5",
    "KH2PO4": "1",
    "(NH4)2SO4": "0.5",
    "MgCl2 x 6 H2O": "0.1",
    "Ca(NO3)2 x 4 H2O": "0.05",
}

STANDARD_SL4_CONCENTRATIONS = {
    "Na2-EDTA": "0.0005",
    "FeSO4 x 7 H2O": "0.0002",
    "ZnSO4 x 7 H2O": "0.0001",
    "MnCl2 x 4 H2O": "0.00003",
    "H3BO3": "0.0003",
    "CoCl2 x 6 H2O": "0.0002",
    "CuCl2 x 2 H2O": "0.00001",
    "NiCl2 x 6 H2O": "0.00002",
    "Na2MoO4 x 2 H2O": "0.00003",
}

DSM_6813_SL4_CONCENTRATIONS = {
    "Na2-EDTA": "0.005",
    "FeSO4 x 7 H2O": "0.002",
    "ZnSO4 x 7 H2O": "0.001",
    "MnCl2 x 4 H2O": "0.0003",
    "H3BO3": "0.003",
    "CoCl2 x 6 H2O": "0.002",
    "CuCl2 x 2 H2O": "0.0001",
    "NiCl2 x 6 H2O": "0.0002",
    "Na2MoO4 x 2 H2O": "0.0003",
}

TERMS = {
    "Na2HPO4 x 2 H2O": ("CHEBI:91258", "disodium hydrogenphosphate dihydrate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "MgCl2 x 6 H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "Ca(NO3)2 x 4 H2O": ("CHEBI:86159", "calcium nitrate tetrahydrate"),
    "Bromothymol blue": ("CHEBI:86155", "bromothymol blue"),
    "Na2-EDTA": ("CHEBI:64734", "EDTA disodium salt (anhydrous)"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "NiCl2 x 6 H2O": ("CHEBI:34887", "nickel dichloride"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
}

BROMOTHYMOL_BLUE = {"Bromothymol blue": "0.05"}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Prepare medium 465 with optional 50 mg/l bromothymol blue as pH "
            "indicator and autoclave. For DSM 6813, add 10 ml/l instead of "
            "1 ml/l trace element solution SL-4."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Grow cells in medium 465 with methanol supplied via incubation "
            "atmosphere up to 10 ml methanol per liter medium, then feed "
            "dichloromethane via the incubation atmosphere at 2 mmol/l or less."
        ),
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": (
            "Maintain pH 7.25 and readjust the culture with sterile 1 M NaOH " "if necessary."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Rehydrate lyophilized cells in the appropriate complex medium and "
            "then cultivate on mineral medium with the appropriate carbon source."
        ),
    },
    {
        "step_number": 5,
        "action": "ADJUST_PH",
        "description": (
            "For trace element solution SL-4, first dissolve EDTA in distilled "
            "water and adjust to pH 7.0 with 2 N NaOH, then add the other compounds."
        ),
    },
)


@dataclass(frozen=True)
class Target:
    path: str
    source_url: str
    final_concentrations: dict[str, str]
    curation_notes: str
    parent_media: dict[str, str] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, str], ...] = ()
    note_suffix: str = ""


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


KOMODO_465C_PARENT = _recipe_ref(
    DSMZ_465C,
    "SUPPLEMENTED_VARIANT",
    (
        "KOMODO Medium 465c follows DSMZ Medium 465c and includes the "
        "recommended 0.05 g/L Bromothymol blue pH indicator."
    ),
)

KOMODO_465C_1_PARENT = _recipe_ref(
    DSMZ_465C,
    "STRAIN_SPECIFIC_VARIANT",
    (
        "KOMODO Medium 465c.1 applies DSMZ Medium 465c for DSM 6813 with "
        "10 ml/L trace element solution SL-4."
    ),
)

KOMODO_CHILDREN = (
    _recipe_ref(
        KOMODO_465C,
        "SUPPLEMENTED_VARIANT",
        (
            "KOMODO Medium 465c follows DSMZ Medium 465c and includes the "
            "recommended 0.05 g/L Bromothymol blue pH indicator."
        ),
    ),
    _recipe_ref(
        KOMODO_465C_1,
        "STRAIN_SPECIFIC_VARIANT",
        (
            "KOMODO Medium 465c.1 applies DSMZ Medium 465c for DSM 6813 with "
            "10 ml/L trace element solution SL-4."
        ),
    ),
)

STANDARD_RECIPE = MAIN_CONCENTRATIONS | STANDARD_SL4_CONCENTRATIONS
KOMODO_465C_RECIPE = MAIN_CONCENTRATIONS | BROMOTHYMOL_BLUE | STANDARD_SL4_CONCENTRATIONS
DSM_6813_RECIPE = MAIN_CONCENTRATIONS | BROMOTHYMOL_BLUE | DSM_6813_SL4_CONCENTRATIONS

TARGETS = (
    Target(
        path=DSMZ_465C,
        source_url=DSMZ_465C_REST,
        final_concentrations=STANDARD_RECIPE,
        curation_notes=(
            "Resolved final DSMZ Medium 465c concentrations after 1:1000 "
            "dilution of trace element solution SL-4."
        ),
        variant_children=KOMODO_CHILDREN,
    ),
    Target(
        path=KOMODO_465C,
        source_url=f"{KOMODO_BASE}465c",
        final_concentrations=KOMODO_465C_RECIPE,
        curation_notes=(
            "Removed non-source complex-medium contaminant rows and resolved "
            "standard DSMZ Medium 465c trace element solution SL-4 dilution."
        ),
        parent_media=KOMODO_465C_PARENT,
        variant_relationship="SUPPLEMENTED_VARIANT",
        variant_modifications=(
            "Adds 0.05 g/L Bromothymol blue pH indicator recommended by DSMZ Medium 465c.",
        ),
        note_suffix=" | DSMZ Medium: 465c (mediadive.medium:465c) | Aerobic: No",
    ),
    Target(
        path=KOMODO_465C_1,
        source_url=f"{KOMODO_BASE}465c.1",
        final_concentrations=DSM_6813_RECIPE,
        curation_notes=(
            "Removed non-source complex-medium contaminant rows and applied "
            "the DSM 6813 10 ml/L trace element solution SL-4 variant."
        ),
        parent_media=KOMODO_465C_1_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Adds 0.05 g/L Bromothymol blue pH indicator recommended by DSMZ Medium 465c.",
            "Uses 10 ml/L trace element solution SL-4 instead of 1 ml/L for DSM 6813.",
        ),
        note_suffix=" | DSMZ Medium: 465c (mediadive.medium:465c) | Aerobic: No",
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


def _require_path(doc: dict[str, Any], path: str) -> None:
    if doc.get("id") != EXPECTED_IDS[path]:
        raise ValueError(f"{path}: found id {doc.get('id')!r}, expected {EXPECTED_IDS[path]!r}")
    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[path]:
        raise ValueError(
            f"{path}: found source term {source_term!r}, expected "
            f"{EXPECTED_SOURCE_TERMS[path]!r}"
        )


def _component(preferred_term: str, value: str) -> dict[str, Any]:
    term = _term(*TERMS[preferred_term])
    return {
        "preferred_term": preferred_term,
        "term": copy.deepcopy(term),
        "concentration": {"value": value, "unit": "G_PER_L"},
        "mediaingredientmech_chebi_term": copy.deepcopy(term),
    }


def _build_ingredients(final_concentrations: dict[str, str]) -> list[dict[str, Any]]:
    return [
        _component(preferred_term, value) for preferred_term, value in final_concentrations.items()
    ]


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    seen = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (target.source_url, DSMZ_465C_PDF, DSMZ_465C_REST):
        if url not in seen:
            references.append({"reference": url})
            seen.add(url)


def _append_curation_event(doc: dict[str, Any], path: str, source: str, notes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ/KOMODO Medium 465c ingredient and variant metadata",
        "source": source,
        "notes": notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{path}: curation_history is not a list")

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
    for field_name in (
        "parent_media",
        "variant_relationship",
        "variant_modifications",
        "variant_children",
    ):
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
        _put_after(
            repaired,
            "variant_children",
            [copy.deepcopy(row) for row in target.variant_children],
            after,
        )


def _notes(target: Target) -> str:
    source_id = EXPECTED_SOURCE_TERMS[target.path].removeprefix("komodo.medium:")
    if target.path == DSMZ_465C:
        return f"Source: DSMZ | Link: {DSMZ_465C_PDF}"
    return f"Source: KOMODO ModelSEED | ID: {source_id}{target.note_suffix}"


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_path(doc, target.path)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_range", None)
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired["notes"] = _notes(target)
    repaired["ingredients"] = _build_ingredients(target.final_concentrations)
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "ingredients")
    _put_after(repaired, "data_quality_flags", list(DATA_QUALITY_FLAGS), "preparation_steps")

    _ensure_references(repaired, target)
    _append_curation_event(repaired, target.path, target.source_url, target.curation_notes)
    _put_after(repaired, "references", repaired["references"], "data_quality_flags")
    _set_variant_fields(repaired, target)
    return repaired


def _is_stale_465_child(child: dict[str, Any]) -> bool:
    return (
        child.get("path") == f"data/normalized_yaml/{KOMODO_465C_1}"
        or child.get("id") == EXPECTED_IDS[KOMODO_465C_1]
        or child.get("name") == Path(KOMODO_465C_1).stem
    )


def repair_komodo_465_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_path(doc, KOMODO_465)

    repaired = copy.deepcopy(doc)
    variant_children = repaired.get("variant_children") or []
    if not isinstance(variant_children, list):
        raise ValueError(f"{KOMODO_465}: variant_children is not a list")

    repaired["variant_children"] = [
        child
        for child in variant_children
        if not (isinstance(child, dict) and _is_stale_465_child(child))
    ]
    _append_curation_event(
        repaired,
        KOMODO_465,
        f"{KOMODO_BASE}465",
        "Moved KOMODO Medium 465c.1 from KOMODO Medium 465 to DSMZ Medium 465c.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans = {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
        for target in TARGETS
    }
    plans[normalized / KOMODO_465] = repair_komodo_465_parent(_load(normalized / KOMODO_465))
    return plans


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
