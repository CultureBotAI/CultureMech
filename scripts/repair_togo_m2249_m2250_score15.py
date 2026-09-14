#!/usr/bin/env python3
"""Repair TOGO M2249/M2250 Lactobacilli MRS Agar/Broth records."""

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

CURATOR = "repair_togo_m2249_m2250_score15.py"
ACTION = "RESOLVED_TOGO_M2249_M2250_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2249 = "https://togomedium.org/medium/M2249"
TOGO_M2250 = "https://togomedium.org/medium/M2250"
ATCC_416 = "https://www.atcc.org/~/media/39839AC0CB884212A57DBF6936371D91.ashx"

TITLE = "Lactobacilli MRS Agar/Broth"
PH_RANGE = {"min": 6.3, "max": 6.7}
STERILIZATION = {"method": "AUTOCLAVE"}

Component = tuple[str, str, str]

M2249_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("DI Water", "1000", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Lactobacilli MRS", "55", "G_PER_L"),
    ("Yeast Extract", "5", "G_PER_L"),
    ("Dextrose", "20", "G_PER_L"),
    ("Sodium Acetate", "5", "G_PER_L"),
    ("Na2HPO4", "2", "G_PER_L"),
    ("MnSO4 x H2O", "0.05", "G_PER_L"),
    ("Sorbitan Monooleate", "1", "G_PER_L"),
    ("Ammonium Citrate", "2", "G_PER_L"),
    ("Beef Extract", "10", "G_PER_L"),
    ("Proteose Peptone #3", "10", "G_PER_L"),
)

M2250_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("DI Water", "1000", "G_PER_L"),
    ("Lactobacilli MRS", "55", "G_PER_L"),
    ("Yeast Extract", "5", "G_PER_L"),
    ("Dextrose", "20", "G_PER_L"),
    ("Sodium Acetate", "5", "G_PER_L"),
    ("Na2HPO4", "2", "G_PER_L"),
    ("MnSO4 x H2O", "0.05", "G_PER_L"),
    ("Sorbitan Monooleate", "1", "G_PER_L"),
    ("Ammonium Citrate", "2", "G_PER_L"),
    ("Beef Extract", "10", "G_PER_L"),
    ("Proteose Peptone #3", "10", "G_PER_L"),
)

BROTH_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Proteose Peptone #3", "10.0", "G_PER_L"),
    ("Beef Extract", "10.0", "G_PER_L"),
    ("Yeast Extract", "5.0", "G_PER_L"),
    ("Dextrose", "20.0", "G_PER_L"),
    ("Sorbitan Monooleate", "1.0", "G_PER_L"),
    ("Ammonium Citrate", "2.0", "G_PER_L"),
    ("Sodium Acetate", "5.0", "G_PER_L"),
    ("MnSO4 x H2O", "0.05", "G_PER_L"),
    ("Na2HPO4", "2.0", "G_PER_L"),
    ("DI Water", "1.0", "L"),
)

M2249_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    *BROTH_FINAL_INGREDIENT_SIGNATURE,
    ("Agar", "15.0", "G_PER_L"),
)

M2250_FINAL_INGREDIENT_SIGNATURE = BROTH_FINAL_INGREDIENT_SIGNATURE

AGAR_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "HEAT",
        "description": "Boil to dissolve agar.",
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C.",
    },
)

BROTH_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C.",
    },
)


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str
    source: str
    physical_state: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    preparation_steps: tuple[dict[str, Any], ...]
    reference_urls: tuple[str, ...]


TARGET_M2249 = Target(
    path=Path("bacterial/lactobacilli_mrs_agar_broth.yaml"),
    expected_id="CultureMech:008837",
    expected_media_term="TOGO:M2249",
    source="TOGO M2249 / ATCC Medium 416",
    physical_state="SOLID_AGAR",
    imported_signature=M2249_IMPORTED_INGREDIENT_SIGNATURE,
    final_signature=M2249_FINAL_INGREDIENT_SIGNATURE,
    preparation_steps=AGAR_PREPARATION_STEPS,
    reference_urls=(TOGO_M2249, ATCC_416),
)

TARGET_M2250 = Target(
    path=Path("bacterial/TOGO_M2250_Lactobacilli_MRS_Agar_Broth.yaml"),
    expected_id="CultureMech:008839",
    expected_media_term="TOGO:M2250",
    source="TOGO M2250 / ATCC Medium 416",
    physical_state="LIQUID",
    imported_signature=M2250_IMPORTED_INGREDIENT_SIGNATURE,
    final_signature=M2250_FINAL_INGREDIENT_SIGNATURE,
    preparation_steps=BROTH_PREPARATION_STEPS,
    reference_urls=(TOGO_M2250, ATCC_416),
)

TARGETS = (TARGET_M2249, TARGET_M2250)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Beef Extract": ("FOODON:03302088", "Beef extract"),
    "DI Water": ("CHEBI:15377", "water"),
    "Dextrose": ("CHEBI:17634", "D-glucose"),
    "MnSO4 x H2O": ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
    "Na2HPO4": ("CHEBI:34683", "disodium hydrogenphosphate"),
    "Proteose Peptone #3": ("MICRO:0000180", "Proteose Peptone"),
    "Sodium Acetate": ("CHEBI:32954", "sodium acetate"),
    "Yeast Extract": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
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
        "notes": (
            notes
            or f"ATCC Medium 416 lists {value} {UNIT_LABELS[unit]} {preferred_term}."
        ),
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(target: Target) -> tuple[dict[str, Any], ...]:
    rows = [
        _component("Proteose Peptone #3", "10.0", "G_PER_L", source=target.source),
        _component("Beef Extract", "10.0", "G_PER_L", source=target.source),
        _component("Yeast Extract", "5.0", "G_PER_L", source=target.source),
        _component("Dextrose", "20.0", "G_PER_L", source=target.source),
        _component(
            "Sorbitan Monooleate",
            "1.0",
            "G_PER_L",
            source=target.source,
            notes=(
                "ATCC Medium 416 lists 1 g/L Sorbitan Monooleate in the "
                "Lactobacilli MRS Broth scratch formula; this generic name is "
                "retained without a ChEBI grounding."
            ),
        ),
        _component(
            "Ammonium Citrate",
            "2.0",
            "G_PER_L",
            source=target.source,
            notes=(
                "ATCC Medium 416 lists 2 g/L Ammonium Citrate in the "
                "Lactobacilli MRS Broth scratch formula; this generic name is "
                "retained without choosing a specific ammonium citrate salt."
            ),
        ),
        _component("Sodium Acetate", "5.0", "G_PER_L", source=target.source),
        _component("MnSO4 x H2O", "0.05", "G_PER_L", source=target.source),
        _component("Na2HPO4", "2.0", "G_PER_L", source=target.source),
        _component(
            "DI Water",
            "1.0",
            "L",
            source=target.source,
            notes="ATCC Medium 416 lists 1000 ml DI Water per liter.",
        ),
    ]
    if target is TARGET_M2249:
        rows.append(
            _component(
                "Agar",
                "15.0",
                "G_PER_L",
                source=target.source,
                notes="TOGO M2249 lists 15 g/L Agar for the solid formulation.",
            )
        )
    return tuple(rows)


def _notes(target: Target) -> str:
    formulation = (
        "TOGO M2249 lists the ATCC Medium 416 solid formulation: 15 g/L agar "
        "plus the Lactobacilli MRS Broth scratch formula."
        if target is TARGET_M2249
        else (
            "TOGO M2250 lists the ATCC Medium 416 Lactobacilli MRS Broth "
            "scratch formula."
        )
    )
    return (
        f"{formulation} ATCC Medium 416 lists, per liter, 10 g Proteose "
        "Peptone #3, 10 g Beef Extract, 5 g Yeast Extract, 20 g Dextrose, "
        "1 g Sorbitan Monooleate, 2 g Ammonium Citrate, 5 g Sodium Acetate, "
        "0.05 g MnSO4 x H2O, 2 g Na2HPO4, and 1000 ml DI Water. The final "
        "pH is 6.5 +/- 0.2."
    )


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


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.reference_urls),
        "notes": (
            f"{_notes(target)} Corrected the DI water unit, removed the "
            "duplicate Lactobacilli MRS wrapper from the expanded scratch "
            "formula, added the ATCC final pH range and autoclave "
            "preparation, and marked ambiguous sorbitan monooleate and "
            "ammonium citrate as intentionally unmapped."
        ),
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = target.physical_state
    _put_after(repaired, "ph_range", copy.deepcopy(PH_RANGE), "physical_state")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(_ingredients(target)))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", _notes(target), "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(target.preparation_steps))
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
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
