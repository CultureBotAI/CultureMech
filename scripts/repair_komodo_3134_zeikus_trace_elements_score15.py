#!/usr/bin/env python3
"""Repair KOMODO 3134 Zeikus trace elements solution (medium 1343)."""

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
TARGET = Path("bacterial/zeikus_trace_elements_solution_medium_1343.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_3134_zeikus_trace_elements_score15.py"
ACTION = "RESOLVED_KOMODO_3134_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

EXPECTED_ID = "CultureMech:004982"
EXPECTED_MEDIA_TERM = "komodo.medium:3134"

KOMODO_3134 = (
    "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=3134"
)
DSMZ_1343_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1343.pdf"
MEDIADIVE_1343 = "https://mediadive.dsmz.de/medium/1343"
MEDIADIVE_1343_REST = "https://mediadive.dsmz.de/rest/medium/1343"
MEDIADIVE_SOLUTION_2698_REST = "https://mediadive.dsmz.de/rest/solution/2698"
REFERENCES = (
    DSMZ_1343_PDF,
    KOMODO_3134,
    MEDIADIVE_1343,
    MEDIADIVE_1343_REST,
    MEDIADIVE_SOLUTION_2698_REST,
)

SOURCE = "DSMZ Medium 1343 / MediaDive solution 2698 / KOMODO 3134"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (("KOH", "variable", "VARIABLE"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Nitrilotriacetic acid", "12.5", "G_PER_L"),
    ("KOH", "variable", "VARIABLE"),
    ("FeCl3 x 4 H2O", "0.2", "G_PER_L"),
    ("ZnCl2", "0.1", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("H3BO3", "0.01", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.017", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.02", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.1", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
    ("NaCl", "1.0", "G_PER_L"),
    ("Na2SeO3", "0.02", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl3 x 4 H2O": ("CHEBI:30808", "iron trichloride"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "KOH": ("CHEBI:32035", "potassium hydroxide"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2SeO3": ("CHEBI:48843", "disodium selenite"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "mL/L",
    "VARIABLE": "variable",
}

NOTES = (
    "KOMODO 3134 lists Zeikus trace elements solution (medium 1343) as a defined "
    "submedium at pH 6.5. DSMZ Medium 1343 and MediaDive solution 2698 provide the "
    "complete stock composition: 12.5 g/L Nitrilotriacetic acid, 0.2 g/L "
    "FeCl3 x 4 H2O, 0.1 g/L ZnCl2, 0.1 g/L MnCl2 x 4 H2O, 0.01 g/L H3BO3, "
    "0.017 g/L CoCl2 x 6 H2O, 0.02 g/L CuCl2 x 2 H2O, 0.1 g/L CaCl2 x 2 H2O, "
    "0.01 g/L Na2MoO4 x 2 H2O, 1.0 g/L NaCl, 0.02 g/L Na2SeO3, distilled water "
    "to 1000 mL, and KOH to neutralise the nitrilotriacetic acid to pH 6.5 before "
    "adding the other trace elements. The DSMZ PDF and KOMODO page abbreviate the "
    "borate row as H3BO; MediaDive identifies the same DSMZ compound row as H3BO3."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": (
            "Neutralise the nitrilotriacetic acid to pH 6.5 with KOH before adding "
            "the other trace elements."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Add the iron, zinc, manganese, borate, cobalt, copper, calcium, "
            "molybdate, sodium chloride, and selenite trace elements, then bring "
            "the Zeikus trace elements solution stock to 1 L with distilled water."
        ),
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if preferred_term == "Distilled water":
        row["notes"] = (
            f"{SOURCE} lists 1000 mL distilled water per 1 L Zeikus trace elements "
            "solution stock."
        )
    elif preferred_term == "KOH":
        row["notes"] = (
            f"{SOURCE} lists KOH as needed to neutralise nitrilotriacetic acid to "
            "pH 6.5 before adding the other trace elements."
        )
    elif preferred_term == "H3BO3":
        row["notes"] = (
            f"{SOURCE} identifies the 0.01 g/L borate row as H3BO3; the DSMZ PDF "
            "and KOMODO page abbreviate the label as H3BO."
        )

    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients() -> list[dict[str, Any]]:
    return [
        _component(preferred_term, value, unit)
        for preferred_term, value, unit in FINAL_INGREDIENT_SIGNATURE
    ]


def _signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("ingredients is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("ingredients contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"ingredient {row.get('preferred_term')!r} lacks concentration")
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"))
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    }:
        raise ValueError(f"{TARGET}: ingredient signature drifted to {ingredient_signature!r}")

    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    if solutions:
        raise ValueError(f"{TARGET}: unexpected solutions")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag not in {"extracted_from_notes", "incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {
        row.get("reference")
        for row in references
        if isinstance(row, dict) and isinstance(row.get("reference"), str)
    }
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _set_solution_record_kind(doc: dict[str, Any]) -> None:
    reordered: dict[str, Any] = {}
    inserted = False
    for key, value in doc.items():
        if key == "record_kind":
            continue
        reordered[key] = value
        if key == "category":
            reordered["record_kind"] = "SOLUTION"
            inserted = True
    if not inserted:
        reordered["record_kind"] = "SOLUTION"

    doc.clear()
    doc.update(reordered)


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": KOMODO_3134,
        "notes": (
            "Replaced the KOH-only pH-buffer import with the complete Zeikus trace "
            "elements solution composition from DSMZ Medium 1343 and MediaDive "
            "solution 2698; preserved KOH as the variable pH adjuster; and grounded "
            "all disclosed components through MediaIngredientMech."
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
    _set_solution_record_kind(repaired)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 6.5, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS)),
        "notes",
    )
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
