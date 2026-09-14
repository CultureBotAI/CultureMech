#!/usr/bin/env python3
"""Repair TOGO M2313 minimal media."""

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
TARGET = Path("bacterial/minimal_media.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008900"
EXPECTED_MEDIA_TERM = "TOGO:M2313"

CURATOR = "repair_togo_m2313_minimal_media_score15.py"
ACTION = "RESOLVED_TOGO_M2313_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2313 = "https://togomedium.org/medium/M2313"
SOURCE = "TOGO M2313"
TITLE = "minimal media"
PH_VALUE = 7.8

Component = tuple[str, str, str]
IngredientSpec = tuple[str, str, str, str]

BASE_NOTE_SUFFIX = "in the shared sea-salts/Tris minimal-media base"
ALTERNATIVE_CARBON_NOTE_SUFFIX = "as one of the alternative carbon sources"

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("yeast extract", "0.05", "PERCENT_W_V"),
    ("NH4Cl", "0.05", "PERCENT_W_V"),
    ("D-glucose", "0.2", "PERCENT_W_V"),
    ("N-acetyl-D-glucosamine", "0.2", "PERCENT_W_V"),
    ("Tris-HCl", "50", "MILLIMOLAR"),
    ("D-galactose", "0.2", "PERCENT_W_V"),
    ("D-xylose", "0.2", "PERCENT_W_V"),
    ("D-galacturonic acid", "0.2", "PERCENT_W_V"),
    ("L-arabinose", "0.2", "PERCENT_W_V"),
    ("L-rhamnose", "0.2", "PERCENT_W_V"),
    ("D-mannose", "0.2", "PERCENT_W_V"),
    ("D-trehalose", "0.2", "PERCENT_W_V"),
    ("xylan (oat spelts)", "0.2", "PERCENT_W_V"),
    ("pectin (apple)", "0.2", "PERCENT_W_V"),
    ("pectin (citrus peel)", "0.2", "PERCENT_W_V"),
    ("galatcomannan (Ceratonia siliqua)", "0.2", "PERCENT_W_V"),
    ("mannan (Saccharomyces cerevisiae)", "0.2", "PERCENT_W_V"),
    ("arabinan (sugar beet)", "0.2", "PERCENT_W_V"),
    ("arabinogalactan (larch)", "0.2", "PERCENT_W_V"),
    ("laminarin (brown algae)", "0.2", "PERCENT_W_V"),
    ("chitin (shrimp shells)", "0.2", "PERCENT_W_V"),
    ("sea salts", "2.3", "PERCENT_W_V"),
    ("alginate (brown algae)", "0.2", "PERCENT_W_V"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("yeast extract", "0.05", "PERCENT_W_V"),
    ("NH4Cl", "0.05", "PERCENT_W_V"),
    ("D-glucose", "0.2", "PERCENT_W_V"),
    ("N-acetyl-D-glucosamine", "0.2", "PERCENT_W_V"),
    ("Tris-HCl", "50.0", "MILLIMOLAR"),
    ("D-galactose", "0.2", "PERCENT_W_V"),
    ("D-xylose", "0.2", "PERCENT_W_V"),
    ("D-galacturonic acid", "0.2", "PERCENT_W_V"),
    ("L-arabinose", "0.2", "PERCENT_W_V"),
    ("L-rhamnose", "0.2", "PERCENT_W_V"),
    ("D-mannose", "0.2", "PERCENT_W_V"),
    ("D-trehalose", "0.2", "PERCENT_W_V"),
    ("xylan (oat spelts)", "0.2", "PERCENT_W_V"),
    ("pectin (apple)", "0.2", "PERCENT_W_V"),
    ("pectin (citrus peel)", "0.2", "PERCENT_W_V"),
    ("galatcomannan (Ceratonia siliqua)", "0.2", "PERCENT_W_V"),
    ("mannan (Saccharomyces cerevisiae)", "0.2", "PERCENT_W_V"),
    ("arabinan (sugar beet)", "0.2", "PERCENT_W_V"),
    ("arabinogalactan (larch)", "0.2", "PERCENT_W_V"),
    ("laminarin (brown algae)", "0.2", "PERCENT_W_V"),
    ("chitin (shrimp shells)", "0.2", "PERCENT_W_V"),
    ("sea salts", "2.3", "PERCENT_W_V"),
    ("alginate (brown algae)", "0.2", "PERCENT_W_V"),
)

REFERENCES = (TOGO_M2313,)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "yeast extract": ("FOODON:03315426", "Yeast extract"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "D-glucose": ("CHEBI:17634", "D-glucose"),
    "N-acetyl-D-glucosamine": (
        "CHEBI:8006",
        "Peptidoglycan(N-acetyl-D-glucosamine)",
    ),
    "D-galactose": ("CHEBI:12936", "D-galactose"),
    "D-xylose": ("CHEBI:65327", "D-xylose"),
    "D-galacturonic acid": ("CHEBI:18024", "D-galacturonic acid"),
    "L-arabinose": ("CHEBI:30849", "L-arabinose"),
    "L-rhamnose": ("CHEBI:62345", "L-rhamnose"),
    "D-mannose": ("CHEBI:16024", "D-mannose"),
    "D-trehalose": ("CHEBI:27082", "trehalose"),
}

MEDIAINGREDIENT_CHEBI = frozenset(
    {
        "NH4Cl",
        "D-glucose",
        "N-acetyl-D-glucosamine",
        "D-galactose",
        "D-xylose",
        "D-galacturonic acid",
        "L-rhamnose",
        "D-mannose",
        "D-trehalose",
    }
)

NOTES = (
    "TOGO M2313 describes minimal media containing 2.3% w/v sea salts, "
    "0.05% w/v yeast extract, 0.05% w/v NH4Cl, and 50 mM Tris-HCl at pH "
    "7.8, with a final concentration of 0.2% w/v of one listed carbon source."
)

SOURCE_SPECIFIC_NOTES: dict[str, str] = {
    "Tris-HCl": (
        "TOGO M2313 lists 50 mM Tris-HCl at pH 7.8 in the shared "
        "minimal-media base; this pH-specific buffer is retained without a "
        "single-molecule ontology grounding and remains intentionally unmapped."
    ),
    "xylan (oat spelts)": (
        "TOGO M2313 lists xylan from oat spelts as an alternative carbon "
        "source; this source-qualified polysaccharide remains intentionally "
        "unmapped."
    ),
    "pectin (apple)": (
        "TOGO M2313 lists pectin from apple as an alternative carbon source; "
        "this source-qualified polysaccharide remains intentionally unmapped."
    ),
    "pectin (citrus peel)": (
        "TOGO M2313 lists pectin from citrus peel as an alternative carbon "
        "source; this source-qualified polysaccharide remains intentionally "
        "unmapped."
    ),
    "galatcomannan (Ceratonia siliqua)": (
        "TOGO M2313 lists galatcomannan from Ceratonia siliqua as an "
        "alternative carbon source; this source-qualified locust-bean gum "
        "remains intentionally unmapped."
    ),
    "mannan (Saccharomyces cerevisiae)": (
        "TOGO M2313 lists mannan from Saccharomyces cerevisiae as an "
        "alternative carbon source; this source-qualified yeast mannan remains "
        "intentionally unmapped."
    ),
    "arabinan (sugar beet)": (
        "TOGO M2313 lists arabinan from sugar beet as an alternative carbon "
        "source; this source-qualified polysaccharide remains intentionally "
        "unmapped."
    ),
    "arabinogalactan (larch)": (
        "TOGO M2313 lists arabinogalactan from larch as an alternative carbon "
        "source; this source-qualified polysaccharide remains intentionally "
        "unmapped."
    ),
    "laminarin (brown algae)": (
        "TOGO M2313 lists laminarin from brown algae at 0.2% w/v; this "
        "source-qualified polysaccharide remains intentionally unmapped."
    ),
    "chitin (shrimp shells)": (
        "TOGO M2313 lists chitin from shrimp shells as an alternative carbon "
        "source; this source-qualified chitin remains intentionally unmapped."
    ),
    "sea salts": (
        "TOGO M2313 lists 2.3% w/v sea salts; this heterogeneous salt mixture "
        "remains intentionally unmapped."
    ),
    "alginate (brown algae)": (
        "TOGO M2313 lists alginate from brown algae as an alternative carbon "
        "source; this source-qualified polysaccharide remains intentionally "
        "unmapped."
    ),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _default_notes(name: str, value: str) -> str:
    if name in {"yeast extract", "NH4Cl"}:
        return f"TOGO M2313 lists {value}% w/v {name} {BASE_NOTE_SUFFIX}."
    return (
        f"TOGO M2313 lists {name} {ALTERNATIVE_CARBON_NOTE_SUFFIX} "
        f"tested at a final concentration of {value}% w/v."
    )


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if preferred_term in MEDIAINGREDIENT_CHEBI:
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _build_ingredients() -> tuple[dict[str, Any], ...]:
    return tuple(
        _component(
            name,
            value,
            unit,
            notes=SOURCE_SPECIFIC_NOTES.get(name) or _default_notes(name, value),
        )
        for name, value, unit in FINAL_INGREDIENT_SIGNATURE
    )


INGREDIENTS = _build_ingredients()


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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in (IMPORTED_INGREDIENT_SIGNATURE, FINAL_INGREDIENT_SIGNATURE):
        raise ValueError(f"{TARGET}: ingredient signature drifted")


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
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Added the source pH, grounded yeast extract, and kept "
            "the disclosed source-qualified polysaccharides, Tris-HCl, and "
            "sea salts intentionally unmapped."
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
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired.pop("preparation_steps", None)
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
