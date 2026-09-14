#!/usr/bin/env python3
"""Repair TOGO M2056 / NBRC 1357 B-CYE alpha agar."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("bacterial/b_cye_agar_medium.yaml")
EXPECTED_ID = "CultureMech:008646"
EXPECTED_MEDIA_TERM = "TOGO:M2056"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2056_bcye_score15.py"
ACTION = "RESOLVED_TOGO_M2056_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2056 = "https://togomedium.org/medium/M2056"
NBRC_1357 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1357"

SOURCE = "TOGO M2056 / NBRC Medium 1357"
TITLE = "B-CYE\u03b1 agar medium"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "10", "G_PER_L"),
    ("Activated carbon", "2", "G_PER_L"),
    ("ACES (N-(2-Acetamido)-2-aminoethanesulfonic acid)", "10", "G_PER_L"),
    ("Soluble iron pyrophosphate", "0.25", "G_PER_L"),
    ("\u03b1-Ketoglutarate potassium", "1", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("L-Cysteine hydrochloride", "0.4", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract", "10.0", "G_PER_L"),
    ("L-Cysteine hydrochloride", "0.4", "G_PER_L"),
    ("Soluble iron pyrophosphate", "0.25", "G_PER_L"),
    ("Activated carbon", "2.0", "G_PER_L"),
    ("ACES (N-(2-Acetamido)-2-aminoethanesulfonic acid)", "10.0", "G_PER_L"),
    ("\u03b1-Ketoglutarate potassium", "1.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

REFERENCES = (TOGO_M2056, NBRC_1357)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "ACES (N-(2-Acetamido)-2-aminoethanesulfonic acid)": ("CHEBI:39061", "ACES"),
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "L-Cysteine hydrochloride": ("CHEBI:91247", "L-cysteine hydrochloride"),
    "Soluble iron pyrophosphate": ("CHEBI:132767", "ferric pyrophosphate"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
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
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes
        or f"NBRC Medium 1357 lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component("Yeast extract", "10.0", "G_PER_L"),
    _component("L-Cysteine hydrochloride", "0.4", "G_PER_L"),
    _component("Soluble iron pyrophosphate", "0.25", "G_PER_L"),
    _component(
        "Activated carbon",
        "2.0",
        "G_PER_L",
        notes=(
            "NBRC Medium 1357 lists 2 g/L activated carbon; this adsorbent "
            "material is retained as an opaque protective component."
        ),
    ),
    _component("ACES (N-(2-Acetamido)-2-aminoethanesulfonic acid)", "10.0", "G_PER_L"),
    _component(
        "\u03b1-Ketoglutarate potassium",
        "1.0",
        "G_PER_L",
        notes=(
            "NBRC Medium 1357 lists 1 g/L alpha-Ketoglutarate potassium; "
            "this row is left ungrounded because ChEBI has no exact term for "
            "the potassium salt."
        ),
    ),
    _component("Agar", "15.0", "G_PER_L"),
    _component(
        "Distilled water",
        "1.0",
        "L",
        notes="NBRC Medium 1357 lists 1 L distilled water.",
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 6.9.",
    },
)

NOTES = (
    "TOGO M2056 imports NBRC Medium 1357 as B-CYE alpha agar medium. NBRC "
    "1357 lists 10 g yeast extract, 0.4 g L-Cysteine hydrochloride, 0.25 g "
    "soluble iron pyrophosphate, 2 g activated carbon, 10 g ACES, 1 g "
    "alpha-Ketoglutarate potassium, 15 g agar, 1 L distilled water, and "
    "pH 6.9. NBRC 1357 notes that the prepared E-MP96 medium is available "
    "from Eiken Chemical Co., Ltd."
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    if doc.get("solutions"):
        raise ValueError(f"{TARGET}: solution signature drifted")


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


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected the imported water g/L artifact, added the "
            "NBRC pH, and marked the NBRC formula as curated."
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


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired["ph_value"] = 6.9
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


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
