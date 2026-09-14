#!/usr/bin/env python3
"""Repair TOGO M2358/M2359 DSMZ Medium 1a records."""

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
PARENT = Path("bacterial/reactivation_with_liquid_medium_1.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2358_m2359_score15.py"
ACTION = "RESOLVED_TOGO_M2358_M2359_SCORE15"
LINK_ACTION = "LINKED_TOGO_M2358_M2359_DSMZ_MEDIUM_1A"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2358 = "https://togomedium.org/medium/M2358"
TOGO_M2359 = "https://togomedium.org/medium/M2359"
DSMZ_1A = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1a.pdf"

EXPECTED_PARENT_ID = "CultureMech:001298"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:1a"
PH_VALUE = 7.0

Component = tuple[str, str, str]

M2358_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000", "G_PER_L"),
    ("Agar, if required", "15", "G_PER_L"),
    ("Meat extract", "3", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
)

M2359_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000", "G_PER_L"),
    ("MnSO4 x H2O", "10", "G_PER_L"),
    ("Agar, if required", "15", "G_PER_L"),
    ("Meat extract", "3", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
)

M2358_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "5.0", "G_PER_L"),
    ("Meat extract", "3.0", "G_PER_L"),
    ("Agar, if required", "15.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

M2359_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "5.0", "G_PER_L"),
    ("Meat extract", "3.0", "G_PER_L"),
    ("MnSO4 x H2O", "10.0", "MG_PER_L"),
    ("Agar, if required", "15.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
)

SPORULATION_STEPS: tuple[dict[str, Any], ...] = (
    *PREPARATION_STEPS,
    {
        "step_number": 2,
        "action": "MIX",
        "description": "Add 10 mg/L MnSO4 x H2O for Bacillus-strain sporulation.",
    },
)


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str
    togo_url: str
    source: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    include_sporulation_manganese: bool
    relationship: str
    child_name: str
    parent_notes: str
    child_notes: str
    variant_modification: str

    @property
    def reference_urls(self) -> tuple[str, ...]:
        return (self.togo_url, DSMZ_1A)


TARGET_M2358 = Target(
    path=Path("bacterial/TOGO_M2358_Reactivation_With_Liquid_Medium_1.yaml"),
    expected_id="CultureMech:008943",
    expected_media_term="TOGO:M2358",
    togo_url=TOGO_M2358,
    source="TOGO M2358 / DSMZ Medium 1a",
    imported_signature=M2358_IMPORTED_INGREDIENT_SIGNATURE,
    final_signature=M2358_FINAL_INGREDIENT_SIGNATURE,
    include_sporulation_manganese=False,
    relationship="SOURCE_DUPLICATE",
    child_name="reactivation_with_liquid_medium_1",
    parent_notes=(
        "TOGO M2358 imports DSMZ Medium 1a and explicitly retains its "
        "distilled-water row."
    ),
    child_notes=(
        "TOGO M2358 imports DSMZ Medium 1a and exactly matches its Nutrient "
        "Agar/Broth formula, with the source distilled-water row retained."
    ),
    variant_modification=(
        "Same ingredient and concentration signature as DSMZ Medium 1a; TOGO "
        "M2358 explicitly retains the source distilled-water row."
    ),
)

TARGET_M2359 = Target(
    path=Path("bacterial/reactivation_with_liquid_medium_1_for_sporulation.yaml"),
    expected_id="CultureMech:008944",
    expected_media_term="TOGO:M2359",
    togo_url=TOGO_M2359,
    source="TOGO M2359 / DSMZ Medium 1a",
    imported_signature=M2359_IMPORTED_INGREDIENT_SIGNATURE,
    final_signature=M2359_FINAL_INGREDIENT_SIGNATURE,
    include_sporulation_manganese=True,
    relationship="SUPPLEMENTED_VARIANT",
    child_name="reactivation_with_liquid_medium_1_for_sporulation",
    parent_notes=(
        "TOGO M2359 imports DSMZ Medium 1a with the 10 mg/L MnSO4 x H2O "
        "Bacillus sporulation supplement."
    ),
    child_notes=(
        "TOGO M2359 imports DSMZ Medium 1a with the source-recommended "
        "10 mg/L MnSO4 x H2O addition for Bacillus-strain sporulation."
    ),
    variant_modification=(
        "Adds 10 mg/L MnSO4 x H2O for Bacillus-strain sporulation."
    ),
)

TARGETS = (TARGET_M2358, TARGET_M2359)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar, if required": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "MnSO4 x H2O": ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
    "Peptone": ("MICRO:0000178", "Peptone"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
}


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
        or f"DSMZ Medium 1a lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(target: Target) -> tuple[dict[str, Any], ...]:
    rows = [
        _component(
            "Peptone",
            "5.0",
            "G_PER_L",
            source=target.source,
            notes="DSMZ Medium 1a lists 5 g/L Peptone.",
        ),
        _component(
            "Meat extract",
            "3.0",
            "G_PER_L",
            source=target.source,
            notes=(
                "DSMZ Medium 1a lists 3 g/L Meat extract; this generic "
                "complex extract is retained without an ontology grounding."
            ),
        ),
    ]
    if target.include_sporulation_manganese:
        rows.append(
            _component(
                "MnSO4 x H2O",
                "10.0",
                "MG_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1a recommends adding 10 mg/L MnSO4 x H2O "
                    "for Bacillus-strain sporulation."
                ),
            )
        )
    rows.extend(
        (
            _component(
                "Agar, if required",
                "15.0",
                "G_PER_L",
                source=target.source,
                notes="DSMZ Medium 1a lists 15 g/L Agar, if required.",
            ),
            _component(
                "Distilled water",
                "1.0",
                "L",
                source=target.source,
                notes="DSMZ Medium 1a lists 1000 ml Distilled water.",
            ),
        )
    )
    return tuple(rows)


def _notes(target: Target) -> str:
    supplement = (
        " TOGO M2359 represents the source-recommended Bacillus sporulation "
        "addition as 10 mg/L MnSO4 x H2O."
        if target.include_sporulation_manganese
        else ""
    )
    return (
        f"{target.source} defines Reactivation With Liquid Medium 1 using DSMZ "
        "Medium 1a. DSMZ Medium 1a lists, per liter, 5 g Peptone, 3 g "
        "Meat extract, 15 g Agar if required, and 1000 ml Distilled water. "
        f"Adjust pH to 7.0.{supplement}"
    )


def _event_notes(target: Target) -> str:
    corrections = (
        "Corrected the imported water and manganese unit artifacts"
        if target.include_sporulation_manganese
        else "Corrected the imported water unit artifact"
    )
    return (
        f"{_notes(target)} {corrections}, grounded the disclosed simple and "
        "protein-hydrolysate components, kept Meat extract intentionally "
        "unmapped, and linked the record to DSMZ Medium 1a."
    )


def _parent_media(target: Target) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": target.relationship,
        "id": EXPECTED_PARENT_ID,
        "name": "reactivation_with_liquid_medium_1",
        "notes": target.child_notes,
    }


def _variant_child(target: Target) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{target.path}",
        "relationship": target.relationship,
        "id": target.expected_id,
        "name": target.child_name,
        "notes": target.parent_notes,
    }


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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, "
            f"found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(
            f"{target.path}: expected media term {target.expected_media_term}"
        )

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        target.imported_signature,
        target.final_signature,
    ):
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.imported_signature!r} to {ingredient_signature!r}"
        )

    if doc.get("solutions"):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(
            f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.reference_urls:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(
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


def _ensure_variant_child(doc: dict[str, Any], target: Target) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    child_ref = _variant_child(target)
    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == target.expected_id or child.get("path") == child_ref["path"]:
            children[index] = child_ref
            return
    children.append(child_ref)


def repair_target(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(_ingredients(target)))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", _notes(target), "media_term")
    repaired["preparation_steps"] = copy.deepcopy(
        list(SPORULATION_STEPS if target.include_sporulation_manganese else PREPARATION_STEPS)
    )
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(
        repaired,
        action=ACTION,
        source="; ".join(target.reference_urls),
        notes=_event_notes(target),
    )
    repaired["parent_media"] = _parent_media(target)
    repaired["variant_relationship"] = target.relationship
    repaired["variant_modifications"] = [target.variant_modification]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    for target in TARGETS:
        _ensure_variant_child(repaired, target)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        source="; ".join((TOGO_M2358, TOGO_M2359, DSMZ_1A)),
        notes=(
            "Linked TOGO M2358 as a source duplicate and TOGO M2359 as a "
            "10 mg/L MnSO4 x H2O supplemented variant of DSMZ Medium 1a."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans = {
        normalized / target.path: repair_target(_load(normalized / target.path), target)
        for target in TARGETS
    }
    parent_path = normalized / PARENT
    plans[parent_path] = repair_parent(_load(parent_path))
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
