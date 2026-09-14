#!/usr/bin/env python3
"""Repair BN agar and its NBRC/TOGO Nutrient Agar/Broth relatives."""

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
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1959_bn_agar_score15.py"
ACTION = "RESOLVED_TOGO_M1959_BN_AGAR_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1959 = "https://togomedium.org/medium/M1959"
NBRC_1236 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1236"
TOGO_M1744 = "https://togomedium.org/medium/M1744"
NBRC_954 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=954"
TOGO_M1570 = "https://togomedium.org/medium/M1570"
NBRC_373 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=373"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term: str
    source: str
    references: tuple[str, ...]
    imported_ingredients: tuple[Component, ...]
    final_ingredients: tuple[Component, ...]
    imported_solutions: tuple[SolutionSignature, ...] = ()
    functional_role: tuple[str, ...] = ()
    parent_media: dict[str, Any] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, Any], ...] = ()
    sterilization: dict[str, Any] | None = None


NUTRIENT_BASE_PATH = "bacterial/nutrient_agar_broth.yaml"
BN_PATH = "bacterial/bn_agar.yaml"
M1570_PATH = "bacterial/togo_medium_m1570.yaml"

NUTRIENT_BASE_PARENT = {
    "path": f"data/normalized_yaml/{NUTRIENT_BASE_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:008307",
    "name": "nutrient_agar_broth",
    "notes": (
        "TOGO M1959 / NBRC Medium 1236 supplements the 13 g/L OXOID "
        "Nutrient Agar/Broth base with filter-sterilized sodium benzoate "
        "and kanamycin."
    ),
}

NUTRIENT_BASE_PARENT_FOR_M1570 = {
    "path": f"data/normalized_yaml/{NUTRIENT_BASE_PATH}",
    "relationship": "CONCENTRATION_VARIANT",
    "id": "CultureMech:008307",
    "name": "nutrient_agar_broth",
    "notes": (
        "NBRC Medium 373 halves Nutrient Broth (OXOID) from 13 g/L to "
        "6.5 g/L while keeping 15 g/L agar if needed."
    ),
}

BN_CHILD = {
    "path": f"data/normalized_yaml/{BN_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:008539",
    "name": "bn_agar",
    "notes": (
        "TOGO M1959 / NBRC Medium 1236 supplements the 13 g/L OXOID "
        "Nutrient Agar/Broth base with 1.44 g/L sodium benzoate and "
        "250 mg/L kanamycin."
    ),
}

M1570_CHILD = {
    "path": f"data/normalized_yaml/{M1570_PATH}",
    "relationship": "CONCENTRATION_VARIANT",
    "id": "CultureMech:008119",
    "name": "togo_medium_m1570",
    "notes": (
        "NBRC Medium 373 decreases Nutrient Broth (OXOID) from 13 g/L to "
        "6.5 g/L and keeps 15 g/L agar if needed."
    ),
}

IMPORTED_BASE_13: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
    ("Nutrient Broth (OXOID)", "13", "G_PER_L"),
)
IMPORTED_BASE_6_5: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
    ("Nutrient Broth (OXOID)", "6.5", "G_PER_L"),
)

FINAL_BASE_13: tuple[Component, ...] = (
    ("Nutrient Broth (OXOID)", "13.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Agar (if needed)", "15.0", "G_PER_L"),
)
FINAL_BASE_6_5: tuple[Component, ...] = (
    ("Nutrient Broth (OXOID)", "6.5", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Agar (if needed)", "15.0", "G_PER_L"),
)

IMPORTED_BN_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Kanamycin*", "250", "G_PER_L", ()),
    ("Sodium benzoate*", "1.44", "G_PER_L", ()),
)

FINAL_BN: tuple[Component, ...] = (
    ("Nutrient Broth (OXOID)", "13.0", "G_PER_L"),
    ("Sodium benzoate", "1.44", "G_PER_L"),
    ("Kanamycin", "250.0", "MG_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Agar (if needed)", "15.0", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Kanamycin": ("CHEBI:6104", "kanamycin"),
    "Sodium benzoate": ("CHEBI:113455", "sodium benzoate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
}

BN_VARIANT_MODIFICATIONS = [
    "Adds 1.44 g/L sodium benzoate.",
    "Adds 250 mg/L kanamycin.",
]

M1570_VARIANT_MODIFICATIONS = [
    "Decreases Nutrient Broth (OXOID) from 13 g/L to 6.5 g/L.",
]

BN_STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": (
        "Autoclave the OXOID Nutrient Agar/Broth base and filter-sterilize "
        "sodium benzoate and kanamycin separately before aseptic addition."
    ),
}

BASE_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Suspend Nutrient Broth (OXOID) and optional agar in distilled "
            "water; the source records pH as unadjusted."
        ),
    },
)

BN_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Suspend Nutrient Broth (OXOID) and optional agar in distilled "
            "water; the source records pH as unadjusted."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Sterilize the OXOID Nutrient Agar/Broth base by autoclaving.",
    },
    {
        "step_number": 3,
        "action": "FILTER_STERILIZE",
        "description": ("Sterilize sodium benzoate and kanamycin separately by filtration."),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Aseptically add filter-sterilized sodium benzoate and kanamycin "
            "to the autoclaved base."
        ),
    },
)

TARGETS: tuple[Target, ...] = (
    Target(
        path=Path(BN_PATH),
        record_id="CultureMech:008539",
        media_term="TOGO:M1959",
        source="TOGO M1959 / NBRC Medium 1236",
        references=(TOGO_M1959, NBRC_1236),
        imported_ingredients=IMPORTED_BASE_13,
        final_ingredients=FINAL_BN,
        imported_solutions=IMPORTED_BN_SOLUTIONS,
        functional_role=("SELECTIVE",),
        parent_media=NUTRIENT_BASE_PARENT,
        variant_relationship="SUPPLEMENTED_VARIANT",
        variant_modifications=tuple(BN_VARIANT_MODIFICATIONS),
        sterilization=BN_STERILIZATION,
    ),
    Target(
        path=Path(NUTRIENT_BASE_PATH),
        record_id="CultureMech:008307",
        media_term="TOGO:M1744",
        source="TOGO M1744 / NBRC Medium 954",
        references=(TOGO_M1744, NBRC_954),
        imported_ingredients=IMPORTED_BASE_13,
        final_ingredients=FINAL_BASE_13,
        variant_children=(BN_CHILD, M1570_CHILD),
    ),
    Target(
        path=Path(M1570_PATH),
        record_id="CultureMech:008119",
        media_term="TOGO:M1570",
        source="TOGO M1570 / NBRC Medium 373",
        references=(TOGO_M1570, NBRC_373),
        imported_ingredients=IMPORTED_BASE_6_5,
        final_ingredients=FINAL_BASE_6_5,
        parent_media=NUTRIENT_BASE_PARENT_FOR_M1570,
        variant_relationship="CONCENTRATION_VARIANT",
        variant_modifications=tuple(M1570_VARIANT_MODIFICATIONS),
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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


def _component(preferred_term: str, value: str, unit: str, source: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if preferred_term == "Nutrient Broth (OXOID)":
        row["notes"] = (
            f"{source} lists {value} {UNIT_LABELS[unit]} Nutrient Broth "
            "(OXOID); retained as an intentionally opaque commercial product."
        )

    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(row["term"])

    if preferred_term == "Agar (if needed)":
        row["notes"] = (
            f"{source} lists {value} {UNIT_LABELS[unit]} agar if needed for " "solid medium."
        )
        row["physicochemical_roles"] = ["SOLIDIFYING_AGENT"]
    elif preferred_term in {"Kanamycin", "Sodium benzoate"}:
        row["notes"] = (
            f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}; "
            "the NBRC footnote marks it for separate filter sterilization."
        )

    return row


def _ingredients(target: Target) -> list[dict[str, Any]]:
    return [
        _component(preferred_term, value, unit, target.source)
        for preferred_term, value, unit in target.final_ingredients
    ]


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


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError("solution row lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition"), "solution composition"),
            )
        )
    return tuple(signatures)


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
    if _source_term_id(doc) != target.media_term:
        raise ValueError(f"{target.path}: expected media term {target.media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (target.imported_ingredients, target.final_ingredients):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    solution_signature = _solution_signatures(doc)
    if solution_signature not in (target.imported_solutions, ()):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_references(doc: dict[str, Any], references_to_add: tuple[str, ...]) -> None:
    if "references" not in doc:
        _put_after(doc, "references", [], "notes")

    references = doc["references"]
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in references_to_add:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ):
        if flag not in flags:
            flags.append(flag)


def _append_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.references),
        "notes": (
            f"Verified {target.source}, converted the imported 1 L water row "
            "to 1000 ml/L, grounded water and agar, retained the OXOID product "
            "as an intentionally unmapped commercial ingredient, recorded the "
            "pH as unadjusted, and repaired the Nutrient Agar/Broth variant "
            "links."
        ),
    }
    if target.path == Path(BN_PATH):
        event["notes"] = (
            "Verified TOGO M1959 against NBRC Medium 1236, converted the "
            "imported sodium benzoate and kanamycin solution wrappers into "
            "direct filter-sterilized ingredients, grounded those selective "
            "agents, recorded the pH as unadjusted, and repaired the "
            "Nutrient Agar/Broth supplemented-variant relationship."
        )

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


def _base_notes(target: Target) -> str:
    if target.path == Path(M1570_PATH):
        amount = "6.5 g"
    else:
        amount = "13 g"
    return (
        f"{target.source} lists {amount} Nutrient Broth (OXOID), 1 L "
        "distilled water, and 15 g agar if needed per liter; pH is "
        "unadjusted. Nutrient Broth (OXOID) is retained as a commercial "
        "complex product."
    )


def _bn_notes() -> str:
    return (
        "TOGO M1959 / NBRC Medium 1236 lists 13 g Nutrient Broth (OXOID), "
        "1.44 g sodium benzoate, 250 mg kanamycin, 1 L distilled water, and "
        "15 g agar if needed per liter; pH is unadjusted. The NBRC footnote "
        "marks the starred sodium benzoate and kanamycin rows for separate "
        "filter sterilization before addition to the autoclaved base."
    )


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    if target.functional_role:
        _put_after(
            repaired,
            "functional_role",
            list(target.functional_role),
            "composition_type",
        )
    else:
        repaired.pop("functional_role", None)

    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired["ingredients"] = _ingredients(target)
    repaired.pop("solutions", None)
    _put_after(
        repaired,
        "notes",
        _bn_notes() if target.path == Path(BN_PATH) else _base_notes(target),
        "media_term",
    )

    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(
            list(BN_PREPARATION_STEPS if target.path == Path(BN_PATH) else BASE_PREPARATION_STEPS)
        ),
        "notes",
    )
    if target.sterilization is None:
        repaired.pop("sterilization", None)
    else:
        _put_after(
            repaired,
            "sterilization",
            copy.deepcopy(target.sterilization),
            "preparation_steps",
        )

    _ensure_references(repaired, target.references)
    if target.parent_media is None:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)
    else:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), "references")
        _put_after(
            repaired,
            "variant_relationship",
            target.variant_relationship,
            "parent_media",
        )
        _put_after(
            repaired,
            "variant_modifications",
            list(target.variant_modifications),
            "variant_relationship",
        )

    if target.variant_children:
        _put_after(
            repaired,
            "variant_children",
            [copy.deepcopy(child) for child in target.variant_children],
            "data_quality_flags",
        )
    else:
        repaired.pop("variant_children", None)

    _ensure_flags(repaired)
    _append_event(repaired, target)
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
