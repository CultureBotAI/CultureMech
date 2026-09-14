#!/usr/bin/env python3
"""Repair KOMODO 2110 Hutner's salts from DSMZ/MediaDive Medium 590."""

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
TARGET = Path("bacterial/hutners_salts_medium_590.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_2110_hutners_salts_score15.py"
ACTION = "RESOLVED_KOMODO_2110_HUTNERS_SALTS_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:004392"
EXPECTED_MEDIA_TERM = "komodo.medium:2110"
MEDIADIVE_590 = "https://mediadive.dsmz.de/medium/590"
DSMZ_590 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium590.pdf"
SOURCE = "DSMZ Medium 590 Hutner's salts"
METALS_SOURCE = "DSMZ Medium 590 Metals 44"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (("NaOH", "variable", "VARIABLE"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "950.0", "ML_PER_L"),
    ("Nitrilotriacetic acid", "10.0", "G_PER_L"),
    ("MgSO4 x 7 H2O", "29.7", "G_PER_L"),
    ("CaCl2 x 2 H2O", "3.335", "G_PER_L"),
    ("(NH4)6Mo7O24 x 4 H2O", "9.25", "MG_PER_L"),
    ("FeSO4 x 7 H2O", "99.0", "MG_PER_L"),
)

METALS_44_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Na-EDTA", "250.0", "MG_PER_L"),
    ("ZnSO4 x 7 H2O", "1095.0", "MG_PER_L"),
    ("FeSO4 x 7 H2O", "500.0", "MG_PER_L"),
    ("MnSO4 x H2O", "154.0", "MG_PER_L"),
    ("CuSO4 x 5 H2O", "39.2", "MG_PER_L"),
    ("Co(NO3)2 x 6 H2O", "24.8", "MG_PER_L"),
    ("Na2B4O7 x 10 H2O", "17.7", "MG_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ('"Metals 44"', "50.0", "ML_PER_L", METALS_44_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)6Mo7O24 x 4 H2O": ("CHEBI:91249", "ammonium molybdate"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Co(NO3)2 x 6 H2O": ("CHEBI:86214", "cobalt dinitrate hexahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnSO4 x H2O": ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
    "Na-EDTA": ("CHEBI:64734", "EDTA disodium salt (anhydrous)"),
    "Na2B4O7 x 10 H2O": ("CHEBI:131366", "disodium tetraborate decahydrate"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "VARIABLE": "variable",
}

NOTES = (
    "KOMODO 2110 records the Hutner's salts stock from DSMZ/MediaDive Medium 590. "
    "DSMZ Medium 590 defines Hutner's salts as 10.0 g/L nitrilotriacetic acid, "
    "29.7 g/L MgSO4 x 7 H2O, 3.335 g/L CaCl2 x 2 H2O, 9.25 mg/L "
    "(NH4)6Mo7O24 x 4 H2O, 99.0 mg/L FeSO4 x 7 H2O, 50.0 ml/L Metals 44, "
    "and 950.0 ml/L distilled water adjusted to pH 6.8."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Dissolve nitrilotriacetic acid.",
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0 with about 7.3 g KOH.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": "Dissolve MgSO4, CaCl2, ammonium molybdate, and FeSO4 separately.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": "Combine the dissolved salts with 50.0 ml/L Metals 44.",
    },
    {
        "step_number": 5,
        "action": "ADJUST_PH",
        "description": "Adjust the final Hutner's salts stock to pH 6.8 with NaOH or H2SO4.",
    },
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
    source: str = SOURCE,
    notes: str | None = None,
) -> dict[str, Any]:
    row = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": (notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}."),
    }
    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component("Distilled water", "950.0", "ML_PER_L"),
    _component("Nitrilotriacetic acid", "10.0", "G_PER_L"),
    _component("MgSO4 x 7 H2O", "29.7", "G_PER_L"),
    _component("CaCl2 x 2 H2O", "3.335", "G_PER_L"),
    _component("(NH4)6Mo7O24 x 4 H2O", "9.25", "MG_PER_L"),
    _component("FeSO4 x 7 H2O", "99.0", "MG_PER_L"),
)

METALS_44 = {
    "preferred_term": '"Metals 44"',
    "concentration": {"value": "50.0", "unit": "ML_PER_L"},
    "source": SOURCE,
    "notes": f"{SOURCE} adds 50.0 ml/L Metals 44.",
    "composition": [
        _component("Distilled water", "1000.0", "ML_PER_L", source=METALS_SOURCE),
        _component("Na-EDTA", "250.0", "MG_PER_L", source=METALS_SOURCE),
        _component("ZnSO4 x 7 H2O", "1095.0", "MG_PER_L", source=METALS_SOURCE),
        _component("FeSO4 x 7 H2O", "500.0", "MG_PER_L", source=METALS_SOURCE),
        _component("MnSO4 x H2O", "154.0", "MG_PER_L", source=METALS_SOURCE),
        _component("CuSO4 x 5 H2O", "39.2", "MG_PER_L", source=METALS_SOURCE),
        _component("Co(NO3)2 x 6 H2O", "24.8", "MG_PER_L", source=METALS_SOURCE),
        _component("Na2B4O7 x 10 H2O", "17.7", "MG_PER_L", source=METALS_SOURCE),
    ],
    "name": '"Metals 44"',
    "preparation_notes": (
        "Dissolve EDTA and add a few drops of concentrated H2SO4 to retard "
        "precipitation of the heavy metal ions."
    ),
}


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
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{label} composition"),
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
        raise ValueError(f"{TARGET}: expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signature = _solution_signature(doc.get("solutions"), "solutions")
    if solution_signature not in ((), FINAL_SOLUTION_SIGNATURE):
        raise ValueError(f"{TARGET}: solution signature drifted")


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
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (MEDIADIVE_590, DSMZ_590):
        if reference not in existing:
            references.append({"reference": reference})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": f"{MEDIADIVE_590}; {DSMZ_590}",
        "notes": (
            f"{NOTES} Replaced the NaOH-only KOMODO note extraction with the "
            "complete DSMZ Hutner's salts stock, nested the Metals 44 stock, "
            "and grounded all quantified chemical components."
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
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 6.8, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS)),
        "notes",
    )
    _put_after(repaired, "solutions", [copy.deepcopy(METALS_44)], "preparation_steps")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
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
