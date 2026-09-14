#!/usr/bin/env python3
"""Repair TOGO M2023 / NBRC Medium 1314 AM3 with nalidixic acid and kanamycin."""

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
TARGET = Path("bacterial/am3_nalidixic_acid_kanamycin_medium.yaml")
PARENT = Path("bacterial/am3_medium.yaml")
EXPECTED_ID = "CultureMech:008611"
EXPECTED_PARENT_ID = "CultureMech:008609"
EXPECTED_MEDIA_TERM = "TOGO:M2023"
EXPECTED_PARENT_MEDIA_TERM = "TOGO:M2021"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2023_am3_antibiotics_score15.py"
ACTION = "RESOLVED_TOGO_M2023_AM3_ANTIBIOTICS"
LINK_ACTION = "LINKED_TOGO_M2023_AM3_ANTIBIOTICS_VARIANT"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2023 = "https://togomedium.org/medium/M2023"
NBRC_1314 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1314"
REFERENCES = (TOGO_M2023, NBRC_1314)
SOURCE = "TOGO M2023 / NBRC Medium 1314"
TITLE = "AM3 + Nalidixic acid, Kanamycin medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "1.5", "G_PER_L"),
    ("NaCl", "3.5", "G_PER_L"),
    ("KH2PO4", "1.32", "G_PER_L"),
    ("K2HPO4", "3.68", "G_PER_L"),
    ("Glucose", "1", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
    ("Beef extract", "1.5", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Beef extract", "1.5", "G_PER_L"),
    ("Yeast extract", "1.5", "G_PER_L"),
    ("Peptone", "5.0", "G_PER_L"),
    ("Glucose", "1.0", "G_PER_L"),
    ("NaCl", "3.5", "G_PER_L"),
    ("K2HPO4", "3.68", "G_PER_L"),
    ("KH2PO4", "1.32", "G_PER_L"),
    ("Agar (if needed)", "15.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

NALIDIXIC_SIGNATURE: tuple[Component, ...] = (
    ("Nalidixic acid", "100.0", "MG_PER_ML"),
)

KANAMYCIN_SIGNATURE: tuple[Component, ...] = (
    ("Kanamycin", "25.0", "MG_PER_ML"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Kanamycin solution (25 mg/ml)*", "1", "G_PER_L", ()),
    ("Nalidixic acid solution (100 mg/ml)*", "1", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Nalidixic acid solution (100 mg/ml)", "1.0", "ML_PER_L", NALIDIXIC_SIGNATURE),
    ("Kanamycin solution (25 mg/ml)", "1.0", "ML_PER_L", KANAMYCIN_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Beef extract": ("FOODON:03302088", "Beef extract"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "Kanamycin": ("CHEBI:6104", "kanamycin"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Nalidixic acid": ("CHEBI:100147", "nalidixic acid"),
    "Peptone": ("MICRO:0000178", "Peptone"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

NOTES = (
    "NBRC Medium 1314 defines AM3 + Nalidixic acid, Kanamycin medium with "
    "1.5 g beef extract, 1.5 g yeast extract, 5 g peptone, 1 g glucose, "
    "3.5 g NaCl, 3.68 g K2HPO4, 1.32 g KH2PO4, 15 g agar if needed, "
    "1 L distilled water, 1 ml Nalidixic acid solution (100 mg/ml), and "
    "1 ml Kanamycin solution (25 mg/ml) per liter. The pH is unadjusted; "
    "the antibiotic solutions are sterilized separately by filtration."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix beef extract, yeast extract, peptone, glucose, NaCl, K2HPO4, "
            "KH2PO4, and agar in distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the basal AM3 medium.",
    },
    {
        "step_number": 3,
        "action": "FILTER_STERILIZE",
        "description": (
            "Filter-sterilize the Nalidixic acid solution (100 mg/ml) and "
            "Kanamycin solution (25 mg/ml) separately."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Aseptically add 1.0 ml/L Nalidixic acid solution and 1.0 ml/L "
            "Kanamycin solution to the autoclaved basal medium."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": (
        "Autoclave the basal AM3 medium and filter-sterilize the nalidixic "
        "acid and kanamycin stock solutions separately before aseptic addition."
    ),
}

PARENT_MEDIA = {
    "path": "data/normalized_yaml/bacterial/am3_medium.yaml",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:008609",
    "name": "am3_medium",
    "notes": (
        "TOGO M2023 / NBRC Medium 1314 supplements AM3 medium with 1 ml/L "
        "Nalidixic acid solution (100 mg/ml) and 1 ml/L Kanamycin solution "
        "(25 mg/ml)."
    ),
}

VARIANT_NOTES = (
    "TOGO M2023 / NBRC Medium 1314 supplements AM3 medium with 1 ml/L "
    "Nalidixic acid solution (100 mg/ml) and 1 ml/L Kanamycin solution "
    "(25 mg/ml)."
)

VARIANT_MODIFICATIONS = [
    "Adds 1 ml/L Nalidixic acid solution (100 mg/ml).",
    "Adds 1 ml/L Kanamycin solution (25 mg/ml).",
]

TOGO_CHILD = {
    "path": "data/normalized_yaml/bacterial/am3_nalidixic_acid_kanamycin_medium.yaml",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_ID,
    "name": "am3_nalidixic_acid_kanamycin_medium",
    "notes": VARIANT_NOTES,
}


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


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
    source: str = SOURCE,
    nutritional_roles: tuple[str, ...] = (),
    physicochemical_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(*GROUNDINGS[preferred_term]),
    }
    if row["term"]["id"].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(row["term"])
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _ingredients() -> list[dict[str, Any]]:
    return [
        _component(
            "Beef extract",
            "1.5",
            "G_PER_L",
            notes=f"{SOURCE} lists 1.5 g/L Beef extract.",
            nutritional_roles=("PROTEIN_SOURCE",),
        ),
        _component(
            "Yeast extract",
            "1.5",
            "G_PER_L",
            notes=f"{SOURCE} lists 1.5 g/L Yeast extract.",
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component(
            "Peptone",
            "5.0",
            "G_PER_L",
            notes=f"{SOURCE} lists 5 g/L Peptone.",
            nutritional_roles=("PROTEIN_SOURCE",),
        ),
        _component(
            "Glucose",
            "1.0",
            "G_PER_L",
            notes=f"{SOURCE} lists 1 g/L Glucose.",
            nutritional_roles=("CARBON_SOURCE",),
        ),
        _component("NaCl", "3.5", "G_PER_L"),
        _component(
            "K2HPO4",
            "3.68",
            "G_PER_L",
            physicochemical_roles=("BUFFER",),
        ),
        _component(
            "KH2PO4",
            "1.32",
            "G_PER_L",
            physicochemical_roles=("BUFFER",),
        ),
        _component(
            "Agar (if needed)",
            "15.0",
            "G_PER_L",
            notes=(
                f"{SOURCE} lists 15 g/L Agar if needed; retained for the "
                "solid agar preparation."
            ),
            physicochemical_roles=("SOLIDIFYING_AGENT",),
        ),
        _component(
            "Distilled water",
            "1000.0",
            "ML_PER_L",
            notes=f"{SOURCE} lists 1 L Distilled water per liter.",
        ),
    ]


def _stock_solution(
    name: str,
    chemical: str,
    value: str,
) -> dict[str, Any]:
    chemical_label = chemical.lower() if chemical == "Kanamycin" else chemical
    return {
        "preferred_term": name,
        "concentration": {"value": "1.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} lists 1 ml/L {name}.",
        "term": _term(*GROUNDINGS[chemical]),
        "mediaingredientmech_chebi_term": _term(*GROUNDINGS[chemical]),
        "composition": [
            _component(
                chemical,
                value,
                "MG_PER_ML",
                notes=(
                    f"NBRC Medium 1314 specifies this stock as {value} mg/ml "
                    f"{chemical_label}."
                ),
            )
        ],
        "preparation_notes": "Sterilize separately by filtration.",
    }


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(_ingredients())
SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock_solution("Nalidixic acid solution (100 mg/ml)", "Nalidixic acid", "100.0"),
    _stock_solution("Kanamycin solution (25 mg/ml)", "Kanamycin", "25.0"),
)


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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signature = _solution_signatures(doc)
    if solution_signature not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")


def _ensure_variant_child(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == TOGO_CHILD["path"]:
            children[index] = copy.deepcopy(TOGO_CHILD)
            return

    children.append(copy.deepcopy(TOGO_CHILD))


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    if "references" not in doc:
        _put_after(doc, "references", [], "notes")

    references = doc["references"]
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_event(doc: dict[str, Any], *, action: str, notes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(REFERENCES),
        "notes": notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
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
    _put_after(repaired, "functional_role", ["SELECTIVE"], "composition_type")
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "notes",
    )
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _ensure_references(repaired)
    _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "references")
    _put_after(repaired, "variant_relationship", "SUPPLEMENTED_VARIANT", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        copy.deepcopy(VARIANT_MODIFICATIONS),
        "variant_relationship",
    )
    _ensure_flags(repaired)
    _append_event(
        repaired,
        action=ACTION,
        notes=(
            "Verified TOGO M2023 against NBRC Medium 1314, corrected "
            "distilled water to 1000 ml/L, converted the nalidixic acid "
            "and kanamycin imports to separately filter-sterilized 1 ml/L "
            "stock solutions, grounded the AM3 base and antibiotic rows, "
            "recorded the pH as unadjusted, and changed the AM3 relationship "
            "from source duplicate to supplemented variant."
        ),
    )
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired)
    _append_event(
        repaired,
        action=LINK_ACTION,
        notes=(
            "Linked TOGO M2023 / NBRC Medium 1314 as a supplemented variant "
            "of AM3 medium."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    parent_path = normalized / PARENT
    return {
        path: repair_record(_load(path)),
        parent_path: repair_parent(_load(parent_path)),
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
