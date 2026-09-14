#!/usr/bin/env python3
"""Repair KOMODO 2106 Wolfe's mineral elixir from DSMZ Medium 792."""

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
TARGET = Path("bacterial/wolfes_mineral_elixir_medium_792.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:004386"
EXPECTED_MEDIA_TERM = "komodo.medium:2106"

CURATOR = "repair_komodo_2106_wolfes_mineral_elixir_score15.py"
ACTION = "RESOLVED_KOMODO_2106_WOLFES_MINERAL_ELIXIR_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

DSMZ_792_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium792.pdf"
MEDIADIVE_792 = "https://mediadive.dsmz.de/medium/792"
MEDIADIVE_792_REST = "https://mediadive.dsmz.de/rest/medium/792"
REFERENCES = (DSMZ_792_PDF, MEDIADIVE_792, MEDIADIVE_792_REST)

SOURCE = "DSMZ Medium 792 Wolfe's mineral elixir"
TITLE = "Wolfes Mineral Elixir (medium 792)"

Component = tuple[str, str, str]
Term = tuple[str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (("H2SO4", "variable", "VARIABLE"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("MgSO4 x 7 H2O", "30.00", "G_PER_L"),
    ("MnSO4 x H2O", "5.00", "G_PER_L"),
    ("NaCl", "10.00", "G_PER_L"),
    ("FeSO4 x 7 H2O", "1.00", "G_PER_L"),
    ("CoCl2 x 6 H2O", "1.80", "G_PER_L"),
    ("CaCl2 x 2 H2O", "1.00", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "1.80", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.10", "G_PER_L"),
    ("AlK(SO4)2 x 12 H2O", "0.18", "G_PER_L"),
    ("H3BO3", "0.10", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.10", "G_PER_L"),
    ("(NH4)2Ni(SO4)2 x 6 H2O", "2.80", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.10", "G_PER_L"),
    ("Na2SeO4", "0.10", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("H2SO4", "variable", "VARIABLE"),
)

NOTES = (
    "KOMODO Medium 2106 is a SubMedium import for the Wolfe's mineral "
    "elixir printed inside DSMZ Medium 792. DSMZ Medium 792 / MediaDive "
    "solution 1605 lists fourteen salt rows, 1000.00 ml distilled water, "
    "and a pH 1.0 adjustment with diluted H2SO4 for this stock."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    term: Term,
    source_amount: str,
    roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    term_ref = _term(*term)
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": f"{SOURCE} lists {source_amount}.",
        "term": term_ref,
        "mediaingredientmech_chebi_term": copy.deepcopy(term_ref),
    }
    if roles:
        row["nutritional_roles"] = list(roles)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "MgSO4 x 7 H2O",
        "30.00",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        "30.00 g MgSO4 x 7 H2O",
    ),
    _ingredient(
        "MnSO4 x H2O",
        "5.00",
        "G_PER_L",
        ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
        "5.00 g MnSO4 x H2O",
        ("TRACE_ELEMENT",),
    ),
    _ingredient(
        "NaCl",
        "10.00",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        "10.00 g NaCl",
    ),
    _ingredient(
        "FeSO4 x 7 H2O",
        "1.00",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        "1.00 g FeSO4 x 7 H2O",
        ("IRON_SOURCE",),
    ),
    _ingredient(
        "CoCl2 x 6 H2O",
        "1.80",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        "1.80 g CoCl2 x 6 H2O",
        ("TRACE_ELEMENT",),
    ),
    _ingredient(
        "CaCl2 x 2 H2O",
        "1.00",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        "1.00 g CaCl2 x 2 H2O",
    ),
    _ingredient(
        "ZnSO4 x 7 H2O",
        "1.80",
        "G_PER_L",
        ("CHEBI:32312", "zinc sulfate heptahydrate"),
        "1.80 g ZnSO4 x 7 H2O",
        ("TRACE_ELEMENT",),
    ),
    _ingredient(
        "CuSO4 x 5 H2O",
        "0.10",
        "G_PER_L",
        ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
        "0.10 g CuSO4 x 5 H2O",
        ("TRACE_ELEMENT",),
    ),
    _ingredient(
        "AlK(SO4)2 x 12 H2O",
        "0.18",
        "G_PER_L",
        ("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
        "0.18 g AlK(SO4)2 x 12 H2O",
        ("TRACE_ELEMENT",),
    ),
    _ingredient(
        "H3BO3",
        "0.10",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        "0.10 g H3BO3",
        ("TRACE_ELEMENT",),
    ),
    _ingredient(
        "Na2MoO4 x 2 H2O",
        "0.10",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        "0.10 g Na2MoO4 x 2 H2O",
        ("TRACE_ELEMENT",),
    ),
    _ingredient(
        "(NH4)2Ni(SO4)2 x 6 H2O",
        "2.80",
        "G_PER_L",
        ("CHEBI:86149", "ammonium nickel sulfate hexahydrate"),
        "2.80 g (NH4)2Ni(SO4)2 x 6 H2O",
        ("TRACE_ELEMENT",),
    ),
    _ingredient(
        "Na2WO4 x 2 H2O",
        "0.10",
        "G_PER_L",
        ("CHEBI:63939", "sodium tungstate dihydrate"),
        "0.10 g Na2WO4 x 2 H2O",
        ("TRACE_ELEMENT",),
    ),
    _ingredient(
        "Na2SeO4",
        "0.10",
        "G_PER_L",
        ("CHEBI:77775", "sodium selenate"),
        "0.10 g Na2SeO4",
        ("TRACE_ELEMENT",),
    ),
    _ingredient(
        "Distilled water",
        "1000.0",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        "1000.00 ml distilled water",
    ),
    {
        "preferred_term": "H2SO4",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": SOURCE,
        "notes": (
            "DSMZ Medium 792 instructs first adjusting Wolfe's mineral "
            "elixir to pH 1.0 with diluted H2SO4; the amount is retained "
            "as variable because it is titrated to pH."
        ),
        "term": _term("CHEBI:26836", "sulfuric acid"),
        "mediaingredientmech_chebi_term": _term("CHEBI:26836", "sulfuric acid"),
    },
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": (
            "First adjust the Wolfe's mineral elixir stock to pH 1.0 with " "diluted H2SO4."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Add and dissolve the Wolfe's mineral elixir salts in 1000.0 ml " "distilled water."
        ),
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
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}")

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_MEDIA_TERM:
        raise ValueError(
            f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}, " f"found {source_term!r}"
        )

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    }:
        raise ValueError(f"{TARGET}: ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("ingredients_curated", "has_ontology_mappings"):
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
            f"{NOTES} Replaced the imported H2SO4-only pH-buffer stub with "
            "the complete DSMZ Wolfe's mineral elixir formula, corrected "
            "water to 1000.0 ml/L, and grounded the pH-adjustment row."
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
    _put_after(repaired, "record_kind", "SOLUTION", "category")
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_value"] = 1.0
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
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
    for path, doc in sorted(plans.items()):
        if args.apply:
            changed = write_record(path, doc)
        else:
            changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
