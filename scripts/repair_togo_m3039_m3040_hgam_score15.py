#!/usr/bin/env python3
"""Repair TOGO/NBRC HGAM records."""

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
M3039_PATH = Path("bacterial/hgam.yaml")
M3040_PATH = Path("bacterial/TOGO_M3040_HGAM.yaml")
R2A_PATH = Path("bacterial/r2a_medium_daigo.yaml")
TSB_NA2CO3_PATH = Path("bacterial/tsb_0_2_w_v_na2co3.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m3039_m3040_hgam_score15.py"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M3039 = "https://togomedium.org/medium/M3039"
TOGO_M3040 = "https://togomedium.org/medium/M3040"
NBRC_1509 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1509"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class HgamTarget:
    path: Path
    record_id: str
    source_term: str
    imported_ingredient_signature: tuple[Component, ...]
    final_ingredient_signature: tuple[Component, ...]
    physical_state: str
    source: str
    notes: str
    event_notes: str
    action: str
    references: tuple[str, ...]
    aeration: str | None = None
    preparation_steps: tuple[dict[str, Any], ...] = ()
    sterilization: dict[str, Any] | None = None
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()


@dataclass(frozen=True)
class StaleLinkTarget:
    path: Path
    record_id: str
    action: str


IMPORTED_M3039_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
)

IMPORTED_M3040_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Nissui Modified GAM Broth*", "41.7", "G_PER_L"),
)

M3039_FINAL_INGREDIENTS: tuple[Component, ...] = (
    ("Nissui Modified GAM Broth", "41.7", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Agar (if needed)", "15.0", "G_PER_L"),
)

M3040_FINAL_INGREDIENTS: tuple[Component, ...] = (
    ("Nissui Modified GAM Broth", "41.7", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

M3040_PARENT = {
    "path": f"data/normalized_yaml/{M3039_PATH}",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": "CultureMech:009551",
    "name": "hgam",
    "notes": (
        "TOGO M3040 is the anaerobic liquid form of NBRC Medium 1509 HGAM."
    ),
}

M3040_CHILD = {
    "path": f"data/normalized_yaml/{M3040_PATH}",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": "CultureMech:009553",
    "name": "hgam",
    "notes": (
        "TOGO M3040 is the anaerobic liquid form of NBRC Medium 1509 HGAM."
    ),
}

M3040_VARIANT_MODIFICATION = (
    "Omits optional agar from TOGO M3039 and follows NBRC's anaerobic liquid "
    "dispensing instruction under an N2 atmosphere."
)

M3039_NOTES = (
    "NBRC Medium 1509 HGAM lists 41.7 g Nissui Modified GAM Broth, "
    "15 g agar if needed, 1.0 L distilled water, and pH 7.3. TOGO M3039 "
    "imports the solid agar form from NBRC M1509-1."
)

M3040_NOTES = (
    "NBRC Medium 1509 HGAM lists 41.7 g Nissui Modified GAM Broth and "
    "1.0 L distilled water at pH 7.3; for anaerobic liquid medium it "
    "directs dispensing under an N2 atmosphere into butyl-stoppered culture "
    "vessels before autoclaving at 115 C for 15 min. TOGO M3040 imports "
    "this liquid anaerobic form from NBRC M1509-2."
)

M3039_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Suspend 41.7 g Nissui Modified GAM Broth and 15.0 g agar, if a "
            "solid medium is needed, in 1.0 L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.3.",
    },
)

M3040_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Suspend 41.7 g Nissui Modified GAM Broth in 1.0 L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.3.",
    },
    {
        "step_number": 3,
        "action": "ALIQUOT",
        "description": (
            "Dispense anaerobic liquid medium into suitable culture vessels "
            "under an N2 atmosphere and seal with butyl rubber stoppers."
        ),
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 115 C for 15 min.",
        "temperature": {"value": 115.0, "unit": "CELSIUS"},
        "duration": "15 min",
    },
)

M3040_STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 115.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": (
        "NBRC Medium 1509 directs anaerobic liquid HGAM to be dispensed "
        "under N2 and autoclaved at 115 C for 15 min."
    ),
}

HGAM_TARGETS: tuple[HgamTarget, ...] = (
    HgamTarget(
        path=M3039_PATH,
        record_id="CultureMech:009551",
        source_term="TOGO:M3039",
        imported_ingredient_signature=IMPORTED_M3039_INGREDIENTS,
        final_ingredient_signature=M3039_FINAL_INGREDIENTS,
        physical_state="SOLID_AGAR",
        source="TOGO M3039 / NBRC Medium 1509",
        notes=M3039_NOTES,
        event_notes=(
            "Restored the opaque Nissui Modified GAM Broth component from "
            "NBRC Medium 1509, corrected the imported water unit to 1.0 L, "
            "grounded optional agar, added pH 7.3, and replaced unrelated "
            "sparse-signature SOURCE_DUPLICATE children with the true TOGO "
            "M3040 anaerobic liquid variant."
        ),
        action="RESOLVED_TOGO_M3039_HGAM_SCORE15",
        references=(TOGO_M3039, NBRC_1509),
        preparation_steps=M3039_PREPARATION_STEPS,
        variant_children=(M3040_CHILD,),
    ),
    HgamTarget(
        path=M3040_PATH,
        record_id="CultureMech:009553",
        source_term="TOGO:M3040",
        imported_ingredient_signature=IMPORTED_M3040_INGREDIENTS,
        final_ingredient_signature=M3040_FINAL_INGREDIENTS,
        physical_state="LIQUID",
        source="TOGO M3040 / NBRC Medium 1509",
        notes=M3040_NOTES,
        event_notes=(
            "Restored the opaque Nissui Modified GAM Broth component from "
            "NBRC Medium 1509, corrected the imported water unit to 1.0 L, "
            "moved N2 from a pseudo-ingredient to the aeration/preparation "
            "description, added pH 7.3 and 115 C for 15 min anaerobic-liquid "
            "sterilization, and linked TOGO M3039 as the solid HGAM parent."
        ),
        action="RESOLVED_TOGO_M3040_HGAM_SCORE15",
        references=(TOGO_M3040, NBRC_1509),
        aeration="N2 atmosphere during anaerobic liquid dispensing",
        preparation_steps=M3040_PREPARATION_STEPS,
        sterilization=M3040_STERILIZATION,
        parent_media=M3040_PARENT,
        variant_relationship="PHYSICAL_STATE_VARIANT",
        variant_modifications=(M3040_VARIANT_MODIFICATION,),
    ),
)

STALE_PARENT = {
    "path": f"data/normalized_yaml/{M3039_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:009551",
    "name": "hgam",
}

STALE_VARIANT_MODIFICATIONS = (
    "Same ingredient and concentration signature; review as possible duplicate "
    "source record.",
)

STALE_LINK_TARGETS: tuple[StaleLinkTarget, ...] = (
    StaleLinkTarget(
        path=R2A_PATH,
        record_id="CultureMech:008718",
        action="REMOVED_STALE_HGAM_PARENT_FROM_R2A_DAIGO",
    ),
    StaleLinkTarget(
        path=TSB_NA2CO3_PATH,
        record_id="CultureMech:008236",
        action="REMOVED_STALE_HGAM_PARENT_FROM_TSB_NA2CO3",
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(target: HgamTarget) -> list[dict[str, Any]]:
    rows = [
        _component(
            "Nissui Modified GAM Broth",
            "41.7",
            "G_PER_L",
            source=target.source,
            notes=(
                f"{target.source} lists 41.7 g/L Nissui Modified GAM Broth; "
                "this commercial medium product is retained as an opaque "
                "complex component."
            ),
        ),
        _component(
            "Distilled water",
            "1000.0",
            "ML_PER_L",
            source=target.source,
            notes=f"{target.source} lists 1.0 L distilled water.",
        ),
    ]
    if target.path == M3039_PATH:
        rows.append(
            _component(
                "Agar (if needed)",
                "15.0",
                "G_PER_L",
                source=target.source,
                notes=f"{target.source} lists 15.0 g/L agar if needed.",
            )
        )
    return rows


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_hgam_target(doc: dict[str, Any], target: HgamTarget) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')}")
    if _source_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        target.imported_ingredient_signature,
        target.final_ingredient_signature,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    solution_signature = _signature(doc.get("solutions"), "solutions")
    if solution_signature not in (IMPORTED_SOLUTION_SIGNATURE, ()):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_stale_link_target(doc: dict[str, Any], target: StaleLinkTarget) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')}")

    parent_media = doc.get("parent_media")
    if parent_media is not None and parent_media != STALE_PARENT:
        raise ValueError(f"{target.path}: parent_media drifted")

    relationship = doc.get("variant_relationship")
    if relationship is not None and relationship != "SOURCE_DUPLICATE":
        raise ValueError(f"{target.path}: variant_relationship drifted")

    modifications = doc.get("variant_modifications")
    if (
        modifications is not None
        and tuple(modifications) != STALE_VARIANT_MODIFICATIONS
    ):
        raise ValueError(f"{target.path}: variant_modifications drifted")


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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in references:
        if reference not in existing:
            rows.append({"reference": reference})
            existing.add(reference)


def _append_event(
    doc: dict[str, Any],
    *,
    action: str,
    source: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": source,
        "notes": notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def repair_hgam_record(doc: dict[str, Any], target: HgamTarget) -> dict[str, Any]:
    _ensure_hgam_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = target.physical_state
    if target.aeration is None:
        repaired.pop("aeration", None)
    else:
        _put_after(repaired, "aeration", target.aeration, "physical_state")
    _put_after(repaired, "ph_value", 7.3, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(target)
    _put_after(repaired, "notes", target.notes, "media_term")
    repaired.pop("solutions", None)
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in target.preparation_steps],
        "notes",
    )
    if target.sterilization is None:
        repaired.pop("sterilization", None)
    else:
        _put_after(
            repaired,
            "sterilization",
            copy.deepcopy(target.sterilization),
            "preparation_steps",
        )
    if target.parent_media is None:
        repaired.pop("parent_media", None)
    else:
        _put_after(
            repaired,
            "parent_media",
            copy.deepcopy(target.parent_media),
            "references",
        )
    if target.variant_children:
        repaired["variant_children"] = [
            copy.deepcopy(child) for child in target.variant_children
        ]
    else:
        repaired.pop("variant_children", None)
    if target.variant_relationship is None:
        repaired.pop("variant_relationship", None)
    else:
        _put_after(
            repaired,
            "variant_relationship",
            target.variant_relationship,
            "parent_media",
        )
    if target.variant_modifications:
        _put_after(
            repaired,
            "variant_modifications",
            list(target.variant_modifications),
            "variant_relationship",
        )
    else:
        repaired.pop("variant_modifications", None)

    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _append_event(
        repaired,
        action=target.action,
        source="; ".join(target.references),
        notes=target.event_notes,
    )
    return repaired


def repair_stale_link_record(
    doc: dict[str, Any],
    target: StaleLinkTarget,
) -> dict[str, Any]:
    _ensure_stale_link_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired.pop("parent_media", None)
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
    _append_event(
        repaired,
        action=target.action,
        source=f"{TOGO_M3039}; {TOGO_M3040}; {NBRC_1509}",
        notes=(
            "Removed a stale SOURCE_DUPLICATE parent link to HGAM that was "
            "created from the old sparse water/agar/empty-solution signature; "
            "NBRC Medium 1509 HGAM has a distinct Nissui Modified GAM Broth "
            "formula."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in HGAM_TARGETS:
        path = normalized / target.path
        plans[path] = repair_hgam_record(_load(path), target)
    for target in STALE_LINK_TARGETS:
        path = normalized / target.path
        plans[path] = repair_stale_link_record(_load(path), target)
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
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
