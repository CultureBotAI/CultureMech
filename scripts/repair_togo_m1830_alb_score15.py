#!/usr/bin/env python3
"""Repair TOGO M1830 / NBRC Medium 1063 ALB Medium."""

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
TARGET_PATH = Path("bacterial/alb_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1830_alb_score15.py"
ACTION = "RESOLVED_TOGO_M1830_ALB_MEDIUM"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1830 = "https://togomedium.org/medium/M1830"
NBRC_1063 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1063"
SOURCE = "NBRC Medium 1063"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("NaCl", "5", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
    ("Tryptone", "10", "G_PER_L"),
    ("CO2", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = (("Na2CO3*", "2", "G_PER_L"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Tryptone", "10.0", "G_PER_L"),
    ("Yeast extract", "5.0", "G_PER_L"),
    ("NaCl", "5.0", "G_PER_L"),
    ("Na2CO3", "2.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Agar (if needed)", "15.0", "G_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = ()

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Tryptone": ("MICRO:0000182", "tryptone"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Agar (if needed)": ("CHEBI:2509", "agar"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Tryptone": ("PROTEIN_SOURCE",),
    "Yeast extract": ("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Na2CO3": ("BUFFER",),
    "Agar (if needed)": ("SOLIDIFYING_AGENT",),
}

COMPONENT_NOTES = {
    "Tryptone": f"{SOURCE} lists 10.0 g/L tryptone.",
    "Yeast extract": f"{SOURCE} lists 5.0 g/L yeast extract.",
    "NaCl": f"{SOURCE} lists 5.0 g/L NaCl.",
    "Na2CO3": (
        f"{SOURCE} lists 2.0 g/L Na2CO3, sterilized separately by "
        "autoclaving and added to the other ingredients."
    ),
    "Distilled water": f"{SOURCE} lists 1 L distilled water as 1000.0 ml/L.",
    "Agar (if needed)": f"{SOURCE} lists 15.0 g/L agar if needed.",
}

PH_RANGE = {
    "min": 8.0,
    "max": 9.0,
    "notes": f"{SOURCE} lists pH 8-9.",
}

SOURCE_NOTE = (
    "TOGO M1830 imports NBRC Medium 1063 ALB Medium: 10.0 g/L tryptone, "
    "5.0 g/L yeast extract, 5.0 g/L NaCl, 2.0 g/L separately autoclaved "
    "Na2CO3, 1000.0 ml/L distilled water, and 15.0 g/L agar if needed, "
    "with final pH 8-9 under air containing 5% CO2."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Dissolve 10.0 g/L tryptone, 5.0 g/L yeast extract, 5.0 g/L "
            "NaCl, and 15.0 g/L agar if needed in 1000.0 ml/L distilled "
            "water."
        ),
    },
    {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "Dissolve 2.0 g/L Na2CO3 separately.",
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "Adjust the final ALB Medium to pH 8-9.",
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": ("Autoclave the basal medium and the Na2CO3 solution separately."),
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": ("Aseptically add sterile Na2CO3 to the autoclaved basal medium."),
    },
    {
        "step_number": 6,
        "action": "MIX",
        "description": "Use ALB Medium under air containing 5% CO2.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": "The basal medium and Na2CO3 solution are autoclaved separately.",
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    identifier, label = GROUNDINGS[preferred_term]
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": COMPONENT_NOTES[preferred_term],
        "term": _term(identifier, label),
    }

    if identifier.startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(identifier, label)

    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _composition() -> list[dict[str, Any]]:
    return [
        _component(preferred_term, value, unit)
        for preferred_term, value, unit in FINAL_INGREDIENT_SIGNATURE
    ]


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:008403":
        raise ValueError(f"{TARGET_PATH}: expected CultureMech:008403")
    if _source_term_id(doc) != "TOGO:M1830":
        raise ValueError(f"{TARGET_PATH}: expected TOGO:M1830")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET_PATH}: ingredient signature drifted")

    solution_signature = _signature(doc.get("solutions"), "solutions")
    if solution_signature not in (
        IMPORTED_SOLUTION_SIGNATURE,
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{TARGET_PATH}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "has_unmapped_ingredients",
        "resolved_reference",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    if "references" not in doc:
        _put_after(doc, "references", [], "notes")

    rows = doc["references"]
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in (TOGO_M1830, NBRC_1063):
        if reference not in existing:
            rows.append({"reference": reference})
            existing.add(reference)


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": f"{TOGO_M1830}; {NBRC_1063}",
        "notes": (
            "Verified TOGO M1830 against NBRC Medium 1063, grounded all "
            "direct components, corrected distilled water to 1000.0 ml/L, "
            "converted the sodium carbonate solution stub into separately "
            "autoclaved 2.0 g/L sodium carbonate, and moved the 5% CO2 gas "
            "phase out of the ingredient list."
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
    repaired.pop("ph_value", None)
    _put_after(repaired, "ph_range", dict(PH_RANGE), "physical_state")
    _put_after(repaired, "aeration", "air containing 5% CO2", "ph_range")
    _put_after(repaired, "incubation_atmosphere", "AEROBIC", "aeration")
    _put_after(repaired, "notes", SOURCE_NOTE, "media_term")
    repaired["ingredients"] = _composition()
    repaired.pop("solutions", None)
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "ingredients",
    )
    _put_after(
        repaired,
        "sterilization",
        copy.deepcopy(STERILIZATION),
        "preparation_steps",
    )

    _ensure_references(repaired)
    _ensure_flags(repaired)
    _append_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / TARGET_PATH: repair_record(_load(normalized / TARGET_PATH)),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in plans.items():
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
