#!/usr/bin/env python3
"""Repair TOGO MRS Criterion/Oxoid broth imports."""

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
CRITERION_PATH = Path(
    "bacterial/mrs_broth_criterion_usa_containing_0_5_l_cysteine_sigma_usa.yaml"
)
OXOID_PATH = Path("bacterial/mrs_broth_oxoid.yaml")
CYSTEINE_OXOID_PATH = Path(
    "bacterial/mrs_broth_with_0_05_w_v_cysteine_hydrochloride.yaml"
)
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2242_m2796_m2804_mrs_broths_score15.py"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2796 = "https://togomedium.org/medium/M2796"
TOGO_M2242 = "https://togomedium.org/medium/M2242"
TOGO_M2804 = "https://togomedium.org/medium/M2804"

WATER = "Distilled water"
MGSO4 = "Magnesium sulphate 7H2O"
YEAST_EXTRACT = "Yeast extract"
K2HPO4 = "Dipotassium hydrogen phosphate"
MNSO4 = "Manganese sulphate 4H2O"
SORBITAN = "Sorbitan mono-oleate"
TRIAMMONIUM_CITRATE = "Triammonium citrate"
SODIUM_ACETATE = "Sodium acetate 3H2O"
GLUCOSE = "Glucose"
LAB_LEMCO_IMPORTED = "`Lab-Lemco\u2019 powder"
LAB_LEMCO = "Lab-Lemco powder (Oxoid)"
PEPTONE = "Peptone"
CYSTEINE = "Cysteine hydrochloride"
L_CYSTEINE_SIGMA = "L-cysteine (Sigma)"
MRS_BROTH_OXOID = "MRS broth (Oxoid)"
MRS_BROTH_CRITERION = "MRS broth (Criterion)"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term_id: str
    source_name: str
    source_url: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    ph_range: tuple[float, float]
    action: str
    notes: str
    step_description: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, Any], ...] = ()


OXOID_IMPORTED_SIGNATURE: tuple[Component, ...] = (
    (WATER, "1", "G_PER_L"),
    (MGSO4, "0.2", "G_PER_L"),
    (YEAST_EXTRACT, "4", "G_PER_L"),
    (K2HPO4, "2", "G_PER_L"),
    (MNSO4, "0.05", "G_PER_L"),
    (SORBITAN, "1", "G_PER_L"),
    (TRIAMMONIUM_CITRATE, "2", "G_PER_L"),
    (SODIUM_ACETATE, "5", "G_PER_L"),
    (GLUCOSE, "20", "G_PER_L"),
    (LAB_LEMCO_IMPORTED, "8", "G_PER_L"),
    (PEPTONE, "10", "G_PER_L"),
)

OXOID_FINAL_SIGNATURE: tuple[Component, ...] = (
    (WATER, "1.0", "L"),
    (MGSO4, "0.2", "G_PER_L"),
    (YEAST_EXTRACT, "4.0", "G_PER_L"),
    (K2HPO4, "2.0", "G_PER_L"),
    (MNSO4, "0.05", "G_PER_L"),
    (SORBITAN, "1.0", "ML_PER_L"),
    (TRIAMMONIUM_CITRATE, "2.0", "G_PER_L"),
    (SODIUM_ACETATE, "5.0", "G_PER_L"),
    (GLUCOSE, "20.0", "G_PER_L"),
    (LAB_LEMCO, "8.0", "G_PER_L"),
    (PEPTONE, "10.0", "G_PER_L"),
)

CRITERION_IMPORTED_SIGNATURE: tuple[Component, ...] = (
    (WATER, "1", "G_PER_L"),
    (L_CYSTEINE_SIGMA, "0.5", "PERCENT_W_V"),
    (MRS_BROTH_CRITERION, "55", "G_PER_L"),
)

CRITERION_FINAL_SIGNATURE: tuple[Component, ...] = (
    (WATER, "1.0", "L"),
    (L_CYSTEINE_SIGMA, "0.5", "PERCENT_W_V"),
    (MRS_BROTH_CRITERION, "55.0", "G_PER_L"),
)

CYSTEINE_OXOID_IMPORTED_SIGNATURE: tuple[Component, ...] = (
    (CYSTEINE, "0.05", "G_PER_L"),
    (MRS_BROTH_OXOID, "1", "G_PER_L"),
    *OXOID_IMPORTED_SIGNATURE,
)

CYSTEINE_OXOID_FINAL_SIGNATURE: tuple[Component, ...] = (
    (CYSTEINE, "0.05", "PERCENT_W_V"),
    *OXOID_FINAL_SIGNATURE,
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    MGSO4: ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
    K2HPO4: ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    MNSO4: ("CHEBI:86358", "manganese(II) sulfate tetrahydrate"),
    TRIAMMONIUM_CITRATE: ("CHEBI:63037", "triammonium citrate"),
    SODIUM_ACETATE: ("CHEBI:32138", "sodium acetate trihydrate"),
    GLUCOSE: ("CHEBI:17234", "glucose"),
    PEPTONE: ("MICRO:0000178", "Peptone"),
    CYSTEINE: ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    L_CYSTEINE_SIGMA: ("CHEBI:17561", "L-cysteine"),
}

MEDIAINGREDIENT_CHEBI = frozenset(
    {
        WATER,
        MGSO4,
        K2HPO4,
        MNSO4,
        TRIAMMONIUM_CITRATE,
        SODIUM_ACETATE,
        GLUCOSE,
        CYSTEINE,
        L_CYSTEINE_SIGMA,
    }
)

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    MGSO4: ("TRACE_ELEMENT",),
    YEAST_EXTRACT: ("PROTEIN_SOURCE",),
    K2HPO4: ("PHOSPHATE_SOURCE",),
    MNSO4: ("TRACE_ELEMENT",),
    SORBITAN: ("CARBON_SOURCE",),
    TRIAMMONIUM_CITRATE: ("NITROGEN_SOURCE",),
    GLUCOSE: ("CARBON_SOURCE",),
    LAB_LEMCO: ("PROTEIN_SOURCE",),
    PEPTONE: ("PROTEIN_SOURCE",),
    CYSTEINE: ("AMINO_ACID_SOURCE", "NITROGEN_SOURCE", "SULFUR_SOURCE"),
    L_CYSTEINE_SIGMA: ("AMINO_ACID_SOURCE", "NITROGEN_SOURCE", "SULFUR_SOURCE"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    K2HPO4: ("BUFFER",),
    SORBITAN: ("SURFACTANT",),
    TRIAMMONIUM_CITRATE: ("BUFFER",),
    SODIUM_ACETATE: ("BUFFER",),
    CYSTEINE: ("REDUCING_AGENT",),
    L_CYSTEINE_SIGMA: ("REDUCING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

M2804_VARIANT_NOTE = (
    "TOGO M2804 supplements the TOGO M2242 MRS broth (Oxoid) formulation "
    "with 0.05% w/v cysteine hydrochloride."
)

M2804_CHILD = {
    "path": f"data/normalized_yaml/{CYSTEINE_OXOID_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:009352",
    "name": "mrs_broth_with_0_05_w_v_cysteine_hydrochloride",
    "notes": M2804_VARIANT_NOTE,
}

M2242_PARENT = {
    "path": f"data/normalized_yaml/{OXOID_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:008831",
    "name": "mrs_broth_oxoid",
    "notes": M2804_VARIANT_NOTE,
}

TARGETS: tuple[Target, ...] = (
    Target(
        path=CRITERION_PATH,
        record_id="CultureMech:009344",
        media_term_id="TOGO:M2796",
        source_name="TOGO M2796",
        source_url=TOGO_M2796,
        imported_signature=CRITERION_IMPORTED_SIGNATURE,
        final_signature=CRITERION_FINAL_SIGNATURE,
        ph_range=(6.3, 6.7),
        action="RESOLVED_TOGO_M2796_MRS_CRITERION_SCORE15",
        notes=(
            "TOGO M2796 lists 55.0 g/L MRS broth from Criterion with "
            "0.5% w/v L-cysteine from Sigma in 1.0 L distilled water at "
            "pH 6.5 +/- 0.2."
        ),
        step_description=(
            "Dissolve 55.0 g MRS broth (Criterion) and 0.5% w/v L-cysteine "
            "in 1.0 L distilled water, then adjust pH to 6.5 +/- 0.2."
        ),
        references=(TOGO_M2796,),
    ),
    Target(
        path=OXOID_PATH,
        record_id="CultureMech:008831",
        media_term_id="TOGO:M2242",
        source_name="TOGO M2242",
        source_url=TOGO_M2242,
        imported_signature=OXOID_IMPORTED_SIGNATURE,
        final_signature=OXOID_FINAL_SIGNATURE,
        ph_range=(6.0, 6.4),
        action="RESOLVED_TOGO_M2242_MRS_OXOID_SCORE15",
        notes=(
            "TOGO M2242 expands one liter of MRS broth (Oxoid) with the "
            "source-listed salts, glucose, yeast extract, Lab-Lemco powder, "
            "peptone, and 1.0 ml/L sorbitan mono-oleate at pH 6.2 +/- 0.2."
        ),
        step_description=(
            "Prepare one liter of MRS broth (Oxoid) from the listed "
            "components and adjust pH to 6.2 +/- 0.2 at 25 C."
        ),
        references=(TOGO_M2242, TOGO_M2804),
        variant_children=(M2804_CHILD,),
    ),
    Target(
        path=CYSTEINE_OXOID_PATH,
        record_id="CultureMech:009352",
        media_term_id="TOGO:M2804",
        source_name="TOGO M2804",
        source_url=TOGO_M2804,
        imported_signature=CYSTEINE_OXOID_IMPORTED_SIGNATURE,
        final_signature=CYSTEINE_OXOID_FINAL_SIGNATURE,
        ph_range=(6.0, 6.4),
        action="RESOLVED_TOGO_M2804_MRS_CYSTEINE_SCORE15",
        notes=(
            "TOGO M2804 lists the TOGO M2242 MRS broth (Oxoid) formula "
            "supplemented with 0.05% w/v cysteine hydrochloride at pH "
            "6.2 +/- 0.2."
        ),
        step_description=(
            "Prepare the MRS broth (Oxoid) components, add 0.05% w/v "
            "cysteine hydrochloride, and adjust pH to 6.2 +/- 0.2 at 25 C."
        ),
        references=(TOGO_M2804, TOGO_M2242),
        parent_media=M2242_PARENT,
        variant_relationship="SUPPLEMENTED_VARIANT",
        variant_modifications=("Add 0.05% w/v cysteine hydrochloride.",),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        doc[key] = value
        return

    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _component(target: Target, name: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "source": target.source_name,
        "notes": f"{target.source_name} lists {value} {UNIT_LABELS[unit]} {name}.",
    }

    grounding = GROUNDINGS.get(name)
    if grounding:
        row["term"] = _term(*grounding)
        if name in MEDIAINGREDIENT_CHEBI:
            row["mediaingredientmech_chebi_term"] = _term(*grounding)

    nutritional_roles = NUTRITIONAL_ROLES.get(name)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(name)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _composition(target: Target) -> list[dict[str, Any]]:
    return [_component(target, *row) for row in target.final_signature]


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.media_term_id:
        raise ValueError(f"{target.path}: expected media term {target.media_term_id}")

    if _signature(doc.get("ingredients"), "ingredients") not in (
        target.imported_signature,
        target.final_signature,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], references_to_add: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in references_to_add:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": target.action,
        "source": "; ".join(target.references),
        "notes": (
            f"{target.notes} Corrected imported one-liter water units, "
            "normalized source gram and milliliter quantities, added the "
            "source pH range, and grounded unambiguous components."
        ),
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == target.action
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_range"] = {"min": target.ph_range[0], "max": target.ph_range[1]}
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _composition(target)
    _put_after(repaired, "notes", target.notes, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        [
            {
                "step_number": 1,
                "action": "MIX",
                "description": target.step_description,
            }
        ],
        "ingredients",
    )

    if target.parent_media:
        _put_after(
            repaired,
            "parent_media",
            copy.deepcopy(target.parent_media),
            "references",
        )
        _put_after(
            repaired,
            "variant_relationship",
            target.variant_relationship,
            "parent_media",
        )
        _put_after(
            repaired,
            "variant_modifications",
            list(target.variant_modifications),
            "variant_relationship",
        )
    else:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)

    if target.variant_children:
        repaired["variant_children"] = [
            copy.deepcopy(child) for child in target.variant_children
        ]
    else:
        repaired.pop("variant_children", None)

    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _ensure_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in plans.items():
        if args.apply:
            changed = write_record(path, doc)
        else:
            changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
