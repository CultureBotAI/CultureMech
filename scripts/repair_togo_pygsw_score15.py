#!/usr/bin/env python3
"""Repair TOGO/NBRC PYGSW Agar imports."""

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
MODIFIED_PATH = Path("bacterial/modified_pygsw_agar.yaml")
PYGSW_PATH = Path("bacterial/pygsw_agar.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_pygsw_score15.py"
TIMESTAMP = "2026-09-12T00:00:00-07:00"
FALSE_KG_MATCH = "mediadive.medium:7"

TOGO_M2058 = "https://togomedium.org/medium/M2058"
TOGO_M1838 = "https://togomedium.org/medium/M1838"
NBRC_1359 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1359"
NBRC_1071 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1071"

YEAST_EXTRACT = "Yeast extract"
SEAWATER = "Seawater"
SEAWATER_2_PERCENT = "Seawater (2% salinity)"
GLUCOSE = "Glucose"
AGAR = "Agar"
PEPTONE = "Peptone"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term_id: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    source_name: str
    togo_url: str
    nbrc_url: str
    action: str
    notes: str

    @property
    def references(self) -> tuple[str, str]:
        return (self.togo_url, self.nbrc_url)


MODIFIED_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (YEAST_EXTRACT, "1.25", "G_PER_L"),
    (SEAWATER, "1", "G_PER_L"),
    (GLUCOSE, "3", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
    (PEPTONE, "1.25", "G_PER_L"),
)

MODIFIED_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (YEAST_EXTRACT, "1.25", "G_PER_L"),
    (SEAWATER, "1.0", "L"),
    (GLUCOSE, "3.0", "G_PER_L"),
    (AGAR, "15.0", "G_PER_L"),
    (PEPTONE, "1.25", "G_PER_L"),
)

PYGSW_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (YEAST_EXTRACT, "1", "G_PER_L"),
    (SEAWATER_2_PERCENT, "1", "G_PER_L"),
    (GLUCOSE, "0.5", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
    (PEPTONE, "1", "G_PER_L"),
)

PYGSW_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (YEAST_EXTRACT, "1.0", "G_PER_L"),
    (SEAWATER_2_PERCENT, "1.0", "L"),
    (GLUCOSE, "0.5", "G_PER_L"),
    (AGAR, "15.0", "G_PER_L"),
    (PEPTONE, "1.0", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
    GLUCOSE: ("CHEBI:17234", "glucose"),
    AGAR: ("CHEBI:2509", "agar"),
    PEPTONE: ("MICRO:0000178", "Peptone"),
}

MEDIAINGREDIENT_CHEBI = frozenset({GLUCOSE, AGAR})

TARGETS: tuple[Target, ...] = (
    Target(
        path=MODIFIED_PATH,
        record_id="CultureMech:008648",
        media_term_id="TOGO:M2058",
        imported_signature=MODIFIED_IMPORTED_INGREDIENT_SIGNATURE,
        final_signature=MODIFIED_FINAL_INGREDIENT_SIGNATURE,
        source_name="TOGO M2058 / NBRC Medium 1359",
        togo_url=TOGO_M2058,
        nbrc_url=NBRC_1359,
        action="RESOLVED_TOGO_M2058_SCORE15",
        notes=(
            "TOGO M2058 / NBRC Medium 1359 lists Modified PYGSW Agar with "
            "1.25 g/L Yeast extract, 1.0 L Seawater, 3.0 g/L Glucose, "
            "15.0 g/L Agar, and 1.25 g/L Peptone. Seawater is retained as "
            "an opaque natural-water component."
        ),
    ),
    Target(
        path=PYGSW_PATH,
        record_id="CultureMech:008411",
        media_term_id="TOGO:M1838",
        imported_signature=PYGSW_IMPORTED_INGREDIENT_SIGNATURE,
        final_signature=PYGSW_FINAL_INGREDIENT_SIGNATURE,
        source_name="TOGO M1838 / NBRC Medium 1071",
        togo_url=TOGO_M1838,
        nbrc_url=NBRC_1071,
        action="RESOLVED_TOGO_M1838_SCORE15",
        notes=(
            "TOGO M1838 / NBRC Medium 1071 lists PYGSW Agar with 1.0 g/L "
            "Yeast extract, 1.0 L Seawater at 2% salinity, 0.5 g/L Glucose, "
            "15.0 g/L Agar, and 1.0 g/L Peptone. Seawater is retained as an "
            "opaque natural-water component."
        ),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient_note(target: Target, preferred_term: str, value: str) -> str:
    if preferred_term == SEAWATER:
        return (
            f"{target.source_name} lists 1 L Seawater; this natural seawater "
            "is retained as an opaque component."
        )
    if preferred_term == SEAWATER_2_PERCENT:
        return (
            f"{target.source_name} lists 1 L Seawater at 2% salinity; this "
            "natural seawater is retained as an opaque component."
        )
    return f"{target.source_name} lists {value} g/L {preferred_term}."


def _component(target: Target, preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": target.source_name,
        "notes": _ingredient_note(target, preferred_term, value),
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if preferred_term in MEDIAINGREDIENT_CHEBI:
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(target: Target) -> tuple[dict[str, Any], ...]:
    return tuple(
        _component(target, name, value, unit) for name, value, unit in target.final_signature
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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
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
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.media_term_id:
        raise ValueError(f"{target.path}: expected media term {target.media_term_id}")

    if _signature(doc.get("ingredients"), "ingredients") not in (
        target.imported_signature,
        target.final_signature,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    kg_match = doc.get("kg_microbe_match")
    if kg_match is not None and kg_match != FALSE_KG_MATCH:
        raise ValueError(f"{target.path}: unexpected kg_microbe_match {kg_match!r}")


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


def _ensure_references(doc: dict[str, Any], wanted: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in wanted:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": target.action,
        "source": "; ".join(target.references),
        "notes": (
            f"{target.notes} Corrected the imported 1 L seawater unit, "
            "grounded yeast extract and peptone, and removed the false "
            "MediaDive 7 match."
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
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(_ingredients(target)))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", target.notes, "media_term")
    repaired.pop("preparation_steps", None)
    repaired.pop("sterilization", None)
    repaired.pop("kg_microbe_match", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _append_curation_event(repaired, target)
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
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
