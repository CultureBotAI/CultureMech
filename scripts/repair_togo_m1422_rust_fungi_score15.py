#!/usr/bin/env python3
"""Repair TOGO M1422 / NBRC M19 Rust fungi Medium."""

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
TARGET = Path("bacterial/rust_fungi_medium.yaml")
EXPECTED_ID = "CultureMech:007960"
EXPECTED_MEDIA_TERM = "TOGO:M1422"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1422_rust_fungi_score15.py"
ACTION = "RESOLVED_TOGO_M1422_RUST_FUNGI_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1422 = "https://togomedium.org/medium/M1422"
TOGO_API_M1422 = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1422"
NBRC_M19 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=19"

SOURCE = "NBRC Medium 19 / TOGO M1422"
TITLE = "Rust fungi Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water make up to", "1", "G_PER_L"),
    ("Sucrose", "40", "G_PER_L"),
    ("Bacto Agar (Difco)", "20", "G_PER_L"),
    ("Peptic Pepton (USB)", "2", "G_PER_L"),
    ("Lab-Lemco Broth (OXOID)", "2", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("Murashige & Skoog's plant salt mixture*", "1.15", "G_PER_L", ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Murashige and Skoog plant salt mixture (Wako)", "1.15", "G_PER_L"),
    ("Peptic Pepton (USB)", "2.0", "G_PER_L"),
    ("Lab-Lemco Broth (Oxoid)", "2.0", "G_PER_L"),
    ("Sucrose", "40.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("Bacto Agar (Difco)", "20.0", "G_PER_L"),
)

REFERENCES = (TOGO_M1422, TOGO_API_M1422, NBRC_M19)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Bacto Agar (Difco)": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Sucrose": ("CHEBI:17992", "sucrose"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Sucrose": ("CARBON_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Bacto Agar (Difco)": ("SOLIDIFYING_AGENT",),
}

NOTES = (
    "TOGO M1422 imports NBRC Medium 19 as Rust fungi Medium. NBRC Medium 19 "
    "lists 1.15 g Murashige & Skoog's plant salt mixture from Wako Pure "
    "Chemicals, 2 g Peptic Pepton from USB, 2 g Lab-Lemco Broth from Oxoid, "
    "40 g sucrose, distilled water to 1 L, and 20 g Bacto Agar from Difco at "
    "pH 5.8."
)

INGREDIENTS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Murashige and Skoog plant salt mixture (Wako)",
        "concentration": {"value": "1.15", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "NBRC Medium 19 lists 1.15 g/L Murashige & Skoog's plant salt "
            "mixture, with a source footnote naming Wako Pure Chemicals; this "
            "commercial blend is retained as an opaque complex component."
        ),
    },
    {
        "preferred_term": "Peptic Pepton (USB)",
        "concentration": {"value": "2.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "NBRC Medium 19 lists 2.0 g/L Peptic Pepton from USB; this "
            "brand-specific peptone is retained as an opaque complex "
            "component."
        ),
    },
    {
        "preferred_term": "Lab-Lemco Broth (Oxoid)",
        "concentration": {"value": "2.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "NBRC Medium 19 lists 2.0 g/L Lab-Lemco Broth from Oxoid; this "
            "brand-specific broth powder is retained as an opaque complex "
            "component."
        ),
    },
    {
        "preferred_term": "Sucrose",
        "concentration": {"value": "40.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "NBRC Medium 19 lists 40.0 g/L Sucrose.",
        "term": {"id": "CHEBI:17992", "label": "sucrose"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:17992", "label": "sucrose"},
        "nutritional_roles": ["CARBON_SOURCE"],
    },
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1.0", "unit": "L"},
        "source": SOURCE,
        "notes": "NBRC Medium 19 lists Distilled water to 1 L.",
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
    },
    {
        "preferred_term": "Bacto Agar (Difco)",
        "concentration": {"value": "20.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "NBRC Medium 19 lists 20.0 g/L Bacto Agar from Difco.",
        "term": {"id": "CHEBI:2509", "label": "agar"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:2509", "label": "agar"},
        "physicochemical_roles": ["SOLIDIFYING_AGENT"],
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signature(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        composition = row.get("composition") or []
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(composition, f"{label}.composition"),
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
    if ingredient_signature == IMPORTED_INGREDIENT_SIGNATURE:
        solution_signature = _solution_signature(doc.get("solutions"), "solutions")
        if solution_signature != IMPORTED_SOLUTION_SIGNATURE:
            raise ValueError(
                f"{TARGET}: solution signature drifted from "
                f"{IMPORTED_SOLUTION_SIGNATURE!r} to {solution_signature!r}"
            )
        return

    if ingredient_signature == FINAL_INGREDIENT_SIGNATURE:
        if doc.get("solutions"):
            raise ValueError(f"{TARGET}: solution signature drifted")
        return

    raise ValueError(
        f"{TARGET}: ingredient signature drifted from "
        f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
    )


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
            f"{NOTES} Corrected the imported water unit, set pH 5.8, moved "
            "Murashige and Skoog plant salt mixture back from an empty "
            "solution to the ingredient list, grounded exact water, sucrose, "
            "and agar components, and retained the brand-specific complex "
            "powders as unmapped ingredients."
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
    _put_after(repaired, "ph_value", 5.8, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
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
