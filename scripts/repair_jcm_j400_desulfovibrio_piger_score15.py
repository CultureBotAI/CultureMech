#!/usr/bin/env python3
"""Repair JCM J400 Desulfovibrio piger Medium."""

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
TARGET = Path("bacterial/desulfovibrio_piger_medium.yaml")
EXPECTED_ID = "CultureMech:002756"
EXPECTED_MEDIA_TERM = "mediadive.medium:J400"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_j400_desulfovibrio_piger_score15.py"
ACTION = "RESOLVED_JCM_J400_DESULFOVIBRIO_PIGER_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M396 = "https://togomedium.org/medium/M396"
SOURCE = "TOGO M396 / JCM Medium J400"
TITLE = "DESULFOVIBRIO PIGER MEDIUM"

Component = tuple[str, str, str]
Solution = tuple[str, str, str, int]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "L"),
    ("MgSO4・7H2O", "1", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("CaCl2・2H2O", "0.1", "G_PER_L"),
    ("KH2PO4", "0.5", "G_PER_L"),
    ("NH4Cl", "1", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Na2S・9H2O", "75", "MG_PER_L"),
    ("NaHCO3", "2", "G_PER_L"),
    ("Na2SO4", "2", "G_PER_L"),
    ("Sodium lactate", "2.5", "G_PER_L"),
    ("Na2S2O3・5H2O", "1", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("MgSO4・7H2O", "1.0", "G_PER_L"),
    ("Yeast extract", "1.0", "G_PER_L"),
    ("CaCl2・2H2O", "0.1", "G_PER_L"),
    ("KH2PO4", "0.5", "G_PER_L"),
    ("NH4Cl", "1.0", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Na2S・9H2O", "75.0", "MG_PER_L"),
    ("NaHCO3", "2.0", "G_PER_L"),
    ("Na2SO4", "2.0", "G_PER_L"),
    ("Sodium lactate", "2.5", "G_PER_L"),
    ("Na2S2O3・5H2O", "1.0", "G_PER_L"),
)

PREVIOUS_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    *FINAL_INGREDIENT_SIGNATURE,
    ("N2", "variable", "VARIABLE"),
)

SOLUTION_SIGNATURE: tuple[Solution, ...] = (
    ("Trace minerals (see Medium [M142])", "1", "ML_PER_L", 0),
    ("Trace element solution (see Medium [M180])", "1", "ML_PER_L", 0),
    ("Trace vitamins (see Medium [M190])", "10", "ML_PER_L", 0),
)

PH_RANGE = {"min": 7.0, "max": 7.2}
REFERENCES = (TOGO_M396,)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "CaCl2・2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgSO4・7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "Na2S2O3・5H2O": ("CHEBI:32150", "sodium thiosulfate pentahydrate"),
    "Na2S・9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Na2SO4": ("CHEBI:32149", "sodium sulfate"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Sodium lactate": ("CHEBI:75228", "sodium lactate"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

NOTES = (
    "TOGO M396 preserves a JCM Medium J400 snapshot for Desulfovibrio Piger Medium. "
    "The JCM formula lists 1 L distilled water, 1 g MgSO4・7H2O, 1 g yeast "
    "extract, 0.1 g CaCl2・2H2O, 0.5 g KH2PO4, 1 g NH4Cl, 0.5 mg resazurin, "
    "75 mg Na2S・9H2O, 2 g NaHCO3, 2 g Na2SO4, 2.5 g sodium lactate, "
    "1 g Na2S2O3・5H2O, and referenced trace-minerals, trace-element, "
    "and trace-vitamins stocks from JCM media M151, M187, and M197. The "
    "preparation text specifies an N2 gas stream and N2 atmosphere, and states "
    "to check the final pH to be 7.0-7.2."
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
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }

    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Distilled water",
        "1.0",
        "L",
        notes="TOGO M396 lists 1 L distilled water.",
    ),
    _component(
        "MgSO4・7H2O",
        "1.0",
        "G_PER_L",
        notes="TOGO M396 lists 1 g/L MgSO4・7H2O.",
    ),
    _component(
        "Yeast extract",
        "1.0",
        "G_PER_L",
        notes="TOGO M396 lists 1 g/L yeast extract.",
    ),
    _component(
        "CaCl2・2H2O",
        "0.1",
        "G_PER_L",
        notes="TOGO M396 lists 0.1 g/L CaCl2・2H2O.",
    ),
    _component(
        "KH2PO4",
        "0.5",
        "G_PER_L",
        notes="TOGO M396 lists 0.5 g/L KH2PO4.",
    ),
    _component(
        "NH4Cl",
        "1.0",
        "G_PER_L",
        notes="TOGO M396 lists 1 g/L NH4Cl.",
    ),
    _component(
        "Resazurin",
        "0.5",
        "MG_PER_L",
        notes="TOGO M396 lists 0.5 mg/L resazurin.",
    ),
    _component(
        "Na2S・9H2O",
        "75.0",
        "MG_PER_L",
        notes="TOGO M396 lists 75 mg/L Na2S・9H2O.",
    ),
    _component(
        "NaHCO3",
        "2.0",
        "G_PER_L",
        notes="TOGO M396 lists 2 g/L NaHCO3.",
    ),
    _component(
        "Na2SO4",
        "2.0",
        "G_PER_L",
        notes="TOGO M396 lists 2 g/L Na2SO4.",
    ),
    _component(
        "Sodium lactate",
        "2.5",
        "G_PER_L",
        notes="TOGO M396 lists 2.5 g/L sodium lactate.",
    ),
    _component(
        "Na2S2O3・5H2O",
        "1.0",
        "G_PER_L",
        notes="TOGO M396 lists 1 g/L Na2S2O3・5H2O.",
    ),
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


def _solution_signature(rows: Any) -> tuple[Solution, ...]:
    if not isinstance(rows, list):
        raise ValueError("solutions is not a list")

    signature: list[Solution] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = row.get("concentration")
        composition = row.get("composition")
        if not isinstance(concentration, dict):
            raise ValueError(f"solution {row.get('preferred_term')!r} lacks concentration")
        if not isinstance(composition, list):
            raise ValueError(f"solution {row.get('preferred_term')!r} lacks composition")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                len(composition),
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
        PREVIOUS_FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    solution_signature = _solution_signature(doc.get("solutions"))
    if solution_signature != SOLUTION_SIGNATURE:
        raise ValueError(
            f"{TARGET}: solution signature drifted from "
            f"{SOLUTION_SIGNATURE!r} to {solution_signature!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "legacy_source_url_unavailable",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
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
            f"{NOTES} Added the TOGO M396 pH range and grounded the main "
            "JCM J400 salt, yeast extract, redox indicator, and carbon-source "
            "rows."
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
    _put_after(repaired, "ph_range", copy.deepcopy(PH_RANGE), "physical_state")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
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
