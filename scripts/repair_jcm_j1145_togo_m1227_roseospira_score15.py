#!/usr/bin/env python3
"""Repair JCM J1145 / TOGO M1227 Modified Roseospira Medium."""

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
JCM_PATH = Path("bacterial/modified_roseospira_medium.yaml")
TOGO_PATH = Path("bacterial/TOGO_M1227_Modified_Roseospira_Medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_j1145_togo_m1227_roseospira_score15.py"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

JCM_1145 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1145"
TOGO_M1227 = "https://togomedium.org/medium/M1227"
TOGO_M572 = "https://togomedium.org/medium/M572"
SOURCE = "JCM Medium 1145 / TOGO M1227"

FERRIC_CITRATE = "Ferric citrate (0.1%, w/v)"
WATER = "Distilled water"
MGSO4 = "MgSO4\u30fb7H2O"
YEAST_EXTRACT = "Yeast extract"
NACL = "NaCl"
CACL2 = "CaCl2\u30fb2H2O"
KH2PO4 = "KH2PO4"
NH4CL = "NH4Cl"
SODIUM_PYRUVATE = "Sodium pyruvate"
NAHCO3 = "NaHCO3"
NA2S = "Na2S\u30fb9H2O"
NA2S2O3 = "Na2S2O3"
VITAMIN_B12 = "vitamin B12 solution"
MICRONUTRIENT = "Micronutrient solution (SL7) (see Medium [M572])"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term_id: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[Component, ...]
    references: tuple[str, ...]
    action: str
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


JCM_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    (WATER, "1", "L"),
    (MGSO4, "1.5", "G_PER_L"),
    (YEAST_EXTRACT, "0.4", "G_PER_L"),
    (NACL, "20", "G_PER_L"),
    (CACL2, "0.15", "G_PER_L"),
    (KH2PO4, "0.5", "G_PER_L"),
    (NH4CL, "0.6", "G_PER_L"),
    (SODIUM_PYRUVATE, "3", "G_PER_L"),
    (NAHCO3, "0.1", "PERCENT_W_V"),
    (NA2S, "1", "MILLIMOLAR"),
    (NA2S2O3, "2", "MILLIMOLAR"),
)

TOGO_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    (FERRIC_CITRATE, "5", "G_PER_L"),
    (WATER, "1", "G_PER_L"),
    (MGSO4, "1.5", "G_PER_L"),
    (YEAST_EXTRACT, "0.4", "G_PER_L"),
    (NACL, "20", "G_PER_L"),
    (CACL2, "0.15", "G_PER_L"),
    (KH2PO4, "0.5", "G_PER_L"),
    (NH4CL, "0.6", "G_PER_L"),
    (SODIUM_PYRUVATE, "3", "G_PER_L"),
    (NAHCO3, "variable", "VARIABLE"),
    (NA2S, "variable", "VARIABLE"),
    (NA2S2O3, "variable", "VARIABLE"),
)

JCM_IMPORTED_SOLUTIONS: tuple[Component, ...] = (
    (FERRIC_CITRATE, "5", "ML_PER_L"),
    (VITAMIN_B12, "1", "ML_PER_L"),
    (MICRONUTRIENT, "1", "ML_PER_L"),
)

TOGO_IMPORTED_SOLUTIONS: tuple[Component, ...] = (
    (VITAMIN_B12, "1", "G_PER_L"),
    (MICRONUTRIENT, "1", "G_PER_L"),
)

FINAL_INGREDIENTS: tuple[Component, ...] = (
    (WATER, "1.0", "L"),
    (MGSO4, "1.5", "G_PER_L"),
    (YEAST_EXTRACT, "0.4", "G_PER_L"),
    (NACL, "20.0", "G_PER_L"),
    (CACL2, "0.15", "G_PER_L"),
    (KH2PO4, "0.5", "G_PER_L"),
    (NH4CL, "0.6", "G_PER_L"),
    (SODIUM_PYRUVATE, "3.0", "G_PER_L"),
    (NAHCO3, "0.1", "PERCENT_W_V"),
    (NA2S, "1.0", "MILLIMOLAR"),
)

FINAL_SOLUTIONS: tuple[Component, ...] = (
    (FERRIC_CITRATE, "5.0", "ML_PER_L"),
    (VITAMIN_B12, "1.0", "ML_PER_L"),
    (MICRONUTRIENT, "1.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    MGSO4: ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
    NACL: ("CHEBI:26710", "sodium chloride"),
    CACL2: ("CHEBI:86158", "calcium chloride dihydrate"),
    KH2PO4: ("CHEBI:63036", "potassium dihydrogen phosphate"),
    NH4CL: ("CHEBI:31206", "ammonium chloride"),
    SODIUM_PYRUVATE: ("CHEBI:50144", "sodium pyruvate"),
    NAHCO3: ("CHEBI:32139", "sodium hydrogencarbonate"),
    NA2S: ("CHEBI:76209", "sodium sulfide nonahydrate"),
}

MEDIAINGREDIENT_CHEBI = frozenset(set(GROUNDINGS) - {YEAST_EXTRACT})

NOTES = (
    "JCM Medium 1145 / TOGO M1227 records Modified Roseospira Medium as "
    "JCM Medium 568 Roseospira Medium adjusted to pH 6.8, supplemented "
    "with 5.0 ml/L Ferric citrate (0.1%, w/v), 1.0 ml/L vitamin B12 "
    "solution at 2 mg/ml, 1.0 ml/L micronutrient solution SL7 from TOGO "
    "M572, and 0.1% final NaHCO3; the modified formula uses 1.0 mM final "
    "Na2S x 9H2O instead of the 2.0 mM final Na2S2O3 in the base medium."
)

INGREDIENT_NOTES = {
    WATER: f"{SOURCE} lists 1.0 L Distilled water.",
    MGSO4: f"{SOURCE} lists 1.5 g/L MgSO4 x 7H2O.",
    YEAST_EXTRACT: f"{SOURCE} lists 0.4 g/L Yeast extract.",
    NACL: f"{SOURCE} lists 20.0 g/L NaCl.",
    CACL2: f"{SOURCE} lists 0.15 g/L CaCl2 x 2H2O.",
    KH2PO4: f"{SOURCE} lists 0.5 g/L KH2PO4.",
    NH4CL: f"{SOURCE} lists 0.6 g/L NH4Cl.",
    SODIUM_PYRUVATE: f"{SOURCE} lists 3.0 g/L Sodium pyruvate.",
    NAHCO3: f"{SOURCE} lists a final 0.1% NaHCO3 addition.",
    NA2S: (
        f"{SOURCE} lists 1.0 mM final Na2S x 9H2O as the Modified "
        "Roseospira reductant instead of the base-medium Na2S2O3."
    ),
}

SOLUTION_NOTES = {
    FERRIC_CITRATE: f"{SOURCE} lists 5.0 ml/L Ferric citrate (0.1%, w/v).",
    VITAMIN_B12: f"{SOURCE} lists 1.0 ml/L vitamin B12 solution at 2 mg/ml.",
    MICRONUTRIENT: (
        f"{SOURCE} lists 1.0 ml/L micronutrient solution SL7; TOGO M572 "
        "defines that referenced stock."
    ),
}

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare the base with distilled water, Ferric citrate, MgSO4 x "
            "7H2O, yeast extract, NaCl, CaCl2 x 2H2O, KH2PO4, NH4Cl, "
            "sodium pyruvate, and micronutrient solution SL7."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 6.8.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "After autoclaving, add 1.0 ml/L vitamin B12 solution at "
            "2 mg/ml and NaHCO3 to 0.1% final."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Use 1.0 mM final Na2S x 9H2O instead of the 2.0 mM final "
            "Na2S2O3 in Roseospira Medium."
        ),
    },
]

SOURCE_DUPLICATE_NOTE = (
    "TOGO M1227 is a snapshot of the same JCM Medium 1145 Modified "
    "Roseospira Medium formulation represented by MediaDive J1145."
)

JCM_CHILD = {
    "path": f"data/normalized_yaml/{JCM_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:002318",
    "name": "modified_roseospira_medium",
    "notes": SOURCE_DUPLICATE_NOTE,
}

TOGO_PARENT = {
    "path": f"data/normalized_yaml/{TOGO_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:007755",
    "name": "modified_roseospira_medium",
    "notes": SOURCE_DUPLICATE_NOTE,
}

TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_PATH,
        record_id="CultureMech:002318",
        media_term_id="mediadive.medium:J1145",
        imported_ingredients=JCM_IMPORTED_INGREDIENTS,
        imported_solutions=JCM_IMPORTED_SOLUTIONS,
        references=(JCM_1145, TOGO_M1227, TOGO_M572),
        action="RESOLVED_JCM_J1145_ROSEOSPIRA_SCORE15",
        parent_media=TOGO_PARENT,
    ),
    Target(
        path=TOGO_PATH,
        record_id="CultureMech:007755",
        media_term_id="TOGO:M1227",
        imported_ingredients=TOGO_IMPORTED_INGREDIENTS,
        imported_solutions=TOGO_IMPORTED_SOLUTIONS,
        references=(TOGO_M1227, JCM_1145, TOGO_M572),
        action="RESOLVED_TOGO_M1227_ROSEOSPIRA_SCORE15",
        variant_children=(JCM_CHILD,),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(name: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": INGREDIENT_NOTES[name],
    }
    grounding = GROUNDINGS[name]
    row["term"] = _term(*grounding)
    if name in MEDIAINGREDIENT_CHEBI:
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS = tuple(_ingredient(name, value, unit) for name, value, unit in FINAL_INGREDIENTS)


def _solution(name: str, value: str, unit: str) -> dict[str, Any]:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": SOLUTION_NOTES[name],
    }


SOLUTIONS = tuple(_solution(name, value, unit) for name, value, unit in FINAL_SOLUTIONS)


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
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.media_term_id:
        raise ValueError(f"{target.path}: expected media term {target.media_term_id}")

    if _signature(doc.get("ingredients"), "ingredients") not in (
        target.imported_ingredients,
        FINAL_INGREDIENTS,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")
    if _signature(doc.get("solutions"), "solutions") not in (
        target.imported_solutions,
        FINAL_SOLUTIONS,
    ):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
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
            f"{NOTES} Removed the base-medium Na2S2O3 row, corrected stock "
            "solution volumes, grounded the remaining defined salts, and "
            "linked the JCM/TOGO source duplicate."
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
    repaired["physical_state"] = "LIQUID"
    repaired["ph_value"] = 6.8
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(PREPARATION_STEPS)
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    repaired.pop("sterilization", None)

    if target.parent_media:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), "references")
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
        _put_after(
            repaired,
            "variant_modifications",
            [target.parent_media["notes"]],
            "variant_relationship",
        )
    else:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)

    if target.variant_children:
        repaired["variant_children"] = [
            copy.deepcopy(child) for child in target.variant_children
        ]
    else:
        repaired.pop("variant_children", None)

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
