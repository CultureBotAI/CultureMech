#!/usr/bin/env python3
"""Repair TOGO M2214 Modified M17 medium."""

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
TARGET = Path("bacterial/modified_m17_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008804"
EXPECTED_MEDIA_TERM = "TOGO:M2214"

CURATOR = "repair_togo_m2214_modified_m17_score15.py"
ACTION = "RESOLVED_TOGO_M2214_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2214 = "https://togomedium.org/medium/M2214"
PMID_IL1403 = "PMID:6087394"
PMID_M17 = "PMID:16350018"
SOURCE = "TOGO M2214"
TITLE = "Modified M17 medium"

MGSO4_STOCK = "1.0 M MgSO4.7H2O (May and Baker)"
MGSO4 = "MgSO4.7H2O"
WATER = "Distilled water"
ASCORBIC_ACID = "Ascorbic acid (Sigma)"
GLYCEROPHOSPHATE = "Sodium beta-glycerophosphate"
GLUCOSE = "Glucose"
YEAST_EXTRACT = "Yeast extract (BBL)"
BEEF_EXTRACT = "Beef extract (BBL)"
POLYPEPTONE = "Polypeptone (BBL)"
PHYTONE_PEPTONE = "Phytone peptone (BBL)"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (MGSO4_STOCK, "1", "G_PER_L"),
    (WATER, "1000", "G_PER_L"),
    (ASCORBIC_ACID, "0.5", "G_PER_L"),
    ("\u03b2-Disodium glycerophosphate (grade II, Sigma)", "19", "G_PER_L"),
    (GLUCOSE, "5", "G_PER_L"),
    (YEAST_EXTRACT, "2.5", "G_PER_L"),
    (BEEF_EXTRACT, "5", "G_PER_L"),
    (POLYPEPTONE, "5", "G_PER_L"),
    (PHYTONE_PEPTONE, "5", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = ()

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "1000.0", "ML_PER_L"),
    (ASCORBIC_ACID, "0.5", "G_PER_L"),
    (GLYCEROPHOSPHATE, "19.0", "G_PER_L"),
    (GLUCOSE, "5.0", "G_PER_L"),
    (YEAST_EXTRACT, "2.5", "G_PER_L"),
    (BEEF_EXTRACT, "5.0", "G_PER_L"),
    (POLYPEPTONE, "5.0", "G_PER_L"),
    (PHYTONE_PEPTONE, "5.0", "G_PER_L"),
)

MGSO4_STOCK_SIGNATURE: tuple[Component, ...] = (
    (MGSO4, "1.0", "MOLAR"),
)

FINAL_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    (MGSO4_STOCK, "1.0", "ML_PER_L", MGSO4_STOCK_SIGNATURE),
)

REFERENCES = (TOGO_M2214, PMID_IL1403, PMID_M17)

GROUNDINGS: dict[str, tuple[str, str]] = {
    MGSO4: ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    WATER: ("CHEBI:15377", "water"),
    ASCORBIC_ACID: ("CHEBI:22652", "Ascorbic acid"),
    GLYCEROPHOSPHATE: ("CHEBI:132089", "sodium glycerol 2-phosphate"),
    GLUCOSE: ("CHEBI:17234", "glucose"),
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
    BEEF_EXTRACT: ("FOODON:03302088", "Beef extract"),
    POLYPEPTONE: ("FOODON:03315306", "Polypeptone"),
    PHYTONE_PEPTONE: ("FOODON:03315720", "Soy peptone"),
}

MEDIAINGREDIENT_CHEBI = frozenset(
    {MGSO4, WATER, ASCORBIC_ACID, GLYCEROPHOSPHATE, GLUCOSE}
)

NOTES = (
    "TOGO M2214 describes Modified M17 medium with glucose replacing lactose: "
    "1000 ml distilled water, 1 ml 1.0 M MgSO4.7H2O, 0.5 g ascorbic acid, "
    "19 g beta-disodium glycerophosphate, 5 g glucose, 2.5 g BBL yeast "
    "extract, 5 g BBL beef extract, 5 g BBL Polypeptone, and 5 g BBL "
    "Phytone peptone per liter. The broth is autoclaved at 121 C for "
    "15 min and has pH 7.15 +/- 0.05 at 22 to 25 C."
)

INGREDIENT_NOTES = {
    MGSO4: (
        "TOGO M2214 adds 1 ml/L of 1.0 M MgSO4.7H2O from May and Baker."
    ),
    WATER: "TOGO M2214 lists 1000 ml/L Distilled water.",
    ASCORBIC_ACID: "TOGO M2214 lists 0.5 g/L Ascorbic acid from Sigma.",
    GLYCEROPHOSPHATE: (
        "TOGO M2214 lists 19 g/L beta-Disodium glycerophosphate grade II "
        "from Sigma."
    ),
    GLUCOSE: "TOGO M2214 lists 5 g/L Glucose.",
    YEAST_EXTRACT: "TOGO M2214 lists 2.5 g/L Yeast extract from BBL.",
    BEEF_EXTRACT: "TOGO M2214 lists 5 g/L Beef extract from BBL.",
    POLYPEPTONE: "TOGO M2214 lists 5 g/L Polypeptone from BBL.",
    PHYTONE_PEPTONE: "TOGO M2214 lists 5 g/L Phytone peptone from BBL.",
}

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare the broth from 1000 ml distilled water, 1 ml of "
            "1.0 M MgSO4.7H2O stock, ascorbic acid, beta-disodium "
            "glycerophosphate, glucose, yeast extract, beef extract, "
            "Polypeptone, and Phytone peptone."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "duration": "15 min",
        "description": "Dispense 10 ml portions and autoclave at 121 C for 15 min.",
    },
]

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "TOGO M2214 autoclaves 10 ml broth portions at 121 C for 15 min.",
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
    source: str = SOURCE,
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    if preferred_term in MEDIAINGREDIENT_CHEBI:
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS = tuple(
    _component(
        name,
        value,
        unit,
        notes=INGREDIENT_NOTES[name],
    )
    for name, value, unit in FINAL_INGREDIENT_SIGNATURE
)

MGSO4_SOLUTION = {
    "preferred_term": MGSO4_STOCK,
    "concentration": {"value": "1.0", "unit": "ML_PER_L"},
    "source": SOURCE,
    "notes": INGREDIENT_NOTES[MGSO4],
    "composition": [
        _component(
            MGSO4,
            "1.0",
            "MOLAR",
            source=f"{SOURCE} MgSO4.7H2O stock",
            notes="TOGO M2214 identifies the magnesium stock as 1.0 M MgSO4.7H2O.",
        )
    ],
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
        if not isinstance(concentration, dict):
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), "solution.composition"),
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
    solution_signature = _solution_signature(doc.get("solutions"), "solutions")
    if (
        ingredient_signature == IMPORTED_INGREDIENT_SIGNATURE
        and solution_signature == IMPORTED_SOLUTION_SIGNATURE
    ):
        return
    if (
        ingredient_signature == FINAL_INGREDIENT_SIGNATURE
        and solution_signature == FINAL_SOLUTION_SIGNATURE
    ):
        return
    raise ValueError(f"{TARGET}: ingredient or solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    if "has_ontology_mappings" not in flags:
        flags.append("has_ontology_mappings")
    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")


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
            f"{NOTES} Restored MgSO4.7H2O as a 1 ml/L 1.0 M stock, corrected "
            "the water row to ml/L, normalized beta-disodium glycerophosphate, "
            "grounded all disclosed components, and added pH and autoclave "
            "evidence."
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
    _put_after(repaired, "ph_range", {"min": 7.1, "max": 7.2}, "physical_state")
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = [copy.deepcopy(MGSO4_SOLUTION)]
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(PREPARATION_STEPS)
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
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
