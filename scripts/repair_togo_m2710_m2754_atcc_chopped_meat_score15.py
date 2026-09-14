#!/usr/bin/env python3
"""Repair TOGO ATCC 593/735 chopped-meat score-15 records."""

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

BASE = Path("bacterial/TOGO_M2710_Chopped_meat_medium.yaml")
GLUCOSE = Path("bacterial/chopped_meat_medium_with_1_glucose.yaml")

BASE_ID = "CultureMech:009262"
GLUCOSE_ID = "CultureMech:009305"

CURATOR = "repair_togo_m2710_m2754_atcc_chopped_meat_score15.py"
ACTION = "RESOLVED_TOGO_ATCC_CHOPPED_MEAT_SCORE15"
LINK_ACTION = "LINKED_M2754_TO_M2710_SUPPLEMENTED_VARIANT"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2710 = "https://togomedium.org/medium/M2710"
TOGO_M2754 = "https://togomedium.org/medium/M2754"
ATCC_593 = "https://www.atcc.org/~/media/2BF00161B1BA47E1A67EBC2003E4AA3D.ashx"
ATCC_735 = "https://www.atcc.org/~/media/0AB039CD914D4A9BAC9CAB709196F694.ashx"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str
    togo_url: str
    atcc_url: str
    atcc_medium: str
    name: str
    has_glucose: bool = False

    @property
    def source(self) -> str:
        return f"{self.expected_media_term} / ATCC Medium {self.atcc_medium}"

    @property
    def references(self) -> tuple[str, str]:
        return (self.togo_url, self.atcc_url)


TARGETS: tuple[Target, ...] = (
    Target(
        path=BASE,
        expected_id=BASE_ID,
        expected_media_term="TOGO:M2710",
        togo_url=TOGO_M2710,
        atcc_url=ATCC_593,
        atcc_medium="593",
        name="chopped_meat_medium",
    ),
    Target(
        path=GLUCOSE,
        expected_id=GLUCOSE_ID,
        expected_media_term="TOGO:M2754",
        togo_url=TOGO_M2754,
        atcc_url=ATCC_735,
        atcc_medium="735",
        name="chopped_meat_medium_with_1_glucose",
        has_glucose=True,
    ),
)

BASE_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("N NaOH", "25", "G_PER_L"),
    ("Ground beef (free of fat)", "500", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("K2HPO4", "5", "G_PER_L"),
    ("Peptone", "30", "G_PER_L"),
    ("L-cysteine . HCl", "0.5", "G_PER_L"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Hydrogen gas", "variable", "VARIABLE"),
)

GLUCOSE_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("N NaOH", "25", "G_PER_L"),
    ("Ground beef (free of fat)", "500", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("K2HPO4", "5", "G_PER_L"),
    ("Glucose", "10", "G_PER_L"),
    ("Peptone", "30", "G_PER_L"),
    ("L-cysteine . HCl", "0.5", "G_PER_L"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Hydrogen gas", "variable", "VARIABLE"),
)

IMPORTED_SOLUTIONS: tuple[Component, ...] = (
    ("0.025% Resazurin solution", "4", "G_PER_L"),
)

BASE_FINAL_INGREDIENTS: tuple[Component, ...] = (
    ("Ground beef (free of fat)", "500.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Peptone", "30.0", "G_PER_L"),
    ("Yeast extract", "5.0", "G_PER_L"),
    ("K2HPO4", "5.0", "G_PER_L"),
    ("L-cysteine . HCl", "0.5", "G_PER_L"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Hydrogen gas", "variable", "VARIABLE"),
)

GLUCOSE_FINAL_INGREDIENTS: tuple[Component, ...] = (
    ("Ground beef (free of fat)", "500.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Peptone", "30.0", "G_PER_L"),
    ("Yeast extract", "5.0", "G_PER_L"),
    ("K2HPO4", "5.0", "G_PER_L"),
    ("Glucose", "10.0", "G_PER_L"),
    ("L-cysteine . HCl", "0.5", "G_PER_L"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Hydrogen gas", "variable", "VARIABLE"),
)

FINAL_SOLUTIONS: tuple[Component, ...] = (
    ("N NaOH", "25.0", "ML_PER_L"),
    ("0.025% Resazurin solution", "4.0", "ML_PER_L"),
)

IMPORTED_SIGNATURES: dict[Path, tuple[tuple[Component, ...], tuple[Component, ...]]] = {
    BASE: (BASE_IMPORTED_INGREDIENTS, IMPORTED_SOLUTIONS),
    GLUCOSE: (GLUCOSE_IMPORTED_INGREDIENTS, IMPORTED_SOLUTIONS),
}

FINAL_SIGNATURES: dict[Path, tuple[tuple[Component, ...], tuple[Component, ...]]] = {
    BASE: (BASE_FINAL_INGREDIENTS, FINAL_SOLUTIONS),
    GLUCOSE: (GLUCOSE_FINAL_INGREDIENTS, FINAL_SOLUTIONS),
}

GROUNDINGS: dict[str, tuple[str, str, bool]] = {
    "0.025% Resazurin solution": ("CHEBI:8806", "Resazurin", True),
    "Distilled water": ("CHEBI:15377", "water", True),
    "Glucose": ("CHEBI:17234", "glucose", True),
    "Hydrogen gas": ("CHEBI:18276", "dihydrogen", False),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate", True),
    "L-cysteine . HCl": ("CHEBI:91247", "L-cysteine hydrochloride", True),
    "N NaOH": ("CHEBI:32145", "sodium hydroxide", True),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen", False),
    "Peptone": ("MICRO:0000178", "peptone", False),
    "Yeast extract": ("FOODON:03315426", "yeast extract", False),
}

COMPONENT_NOTES: dict[str, str] = {
    "0.025% Resazurin solution": (
        "ATCC Medium {m} adds 4.0 ml/L 0.025% resazurin solution."
    ),
    "Distilled water": (
        "ATCC Medium {m} starts with 1.0 L distilled water and restores the "
        "filtrate to a final 1.0 L volume."
    ),
    "Glucose": "ATCC Medium {m} adds 10.0 g/L glucose.",
    "Ground beef (free of fat)": (
        "ATCC Medium {m} lists 500.0 g/L fat-free ground beef."
    ),
    "Hydrogen gas": (
        "ATCC Medium {m} uses 97% nitrogen / 3% hydrogen while dispensing."
    ),
    "K2HPO4": "ATCC Medium {m} lists 5.0 g/L K2HPO4.",
    "L-cysteine . HCl": "ATCC Medium {m} adds 0.5 g/L L-cysteine HCl.",
    "N NaOH": (
        "ATCC Medium {m} lists 25.0 ml/L N NaOH for the boiled meat extraction."
    ),
    "Nitrogen gas": (
        "ATCC Medium {m} uses 97% nitrogen / 3% hydrogen while dispensing."
    ),
    "Peptone": "ATCC Medium {m} lists 30.0 g/L peptone.",
    "Yeast extract": "ATCC Medium {m} lists 5.0 g/L yeast extract.",
}

NOTES = {
    BASE: (
        "TOGO M2710 imports ATCC Medium 593 Chopped meat medium. ATCC 593 lists "
        "500.0 g fat-free ground beef, 1.0 L distilled water, 25.0 ml N NaOH, "
        "30.0 g peptone, 5.0 g yeast extract, 5.0 g K2HPO4, 4.0 ml 0.025% "
        "resazurin solution, and 0.5 g L-cysteine HCl, adjusts the medium to "
        "pH 7.0, and dispenses it under 97% nitrogen / 3% hydrogen."
    ),
    GLUCOSE: (
        "TOGO M2754 imports ATCC Medium 735 Chopped meat medium with 1% glucose. "
        "ATCC 735 follows ATCC Medium 593 and adds 10.0 g glucose before the "
        "0.025% resazurin solution addition."
    ),
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "HEAT",
        "description": (
            "Use lean beef or horse meat; remove fat and connective tissue before "
            "grinding. Mix meat, distilled water, and N NaOH and bring to a boil "
            "while stirring."
        ),
    },
    {
        "step_number": 2,
        "action": "FILTER",
        "description": (
            "Cool to room temperature, skim fat off the surface, and filter, "
            "retaining both meat particles and filtrate. Add enough distilled "
            "water to restore 1.0 L of filtrate."
        ),
    },
    {
        "step_number": 3,
        "action": "HEAT",
        "description": (
            "Add peptone, yeast extract, K2HPO4, any glucose supplement, and "
            "0.025% resazurin solution to the filtrate, then boil and cool."
        ),
    },
    {
        "step_number": 4,
        "action": "ADJUST_PH",
        "description": "Add L-cysteine HCl and adjust to pH 7.0.",
    },
    {
        "step_number": 5,
        "action": "AUTOCLAVE",
        "description": (
            "Under 97% nitrogen / 3% hydrogen, dispense 7 ml medium over one part "
            "meat particles to four to five parts fluid per tube. Cap with butyl "
            "rubber stoppers under N2/H2 and autoclave for 15 minutes under fast "
            "exhaust."
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


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    target: Target,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": target.source,
        "notes": COMPONENT_NOTES[preferred_term].format(m=target.atcc_medium),
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        identifier, label, add_chebi_link = grounding
        row["term"] = _term(identifier, label)
        if add_chebi_link:
            row["mediaingredientmech_chebi_term"] = _term(identifier, label)
    return row


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(
            f"{target.path}: expected media term {target.expected_media_term}"
        )

    signatures = (
        _signature(doc.get("ingredients"), "ingredients"),
        _signature(doc.get("solutions"), "solutions"),
    )
    expected = (IMPORTED_SIGNATURES[target.path], FINAL_SIGNATURES[target.path])
    if signatures not in expected:
        raise ValueError(
            f"{target.path}: ingredient/solution signature drifted from "
            f"{expected!r} to {signatures!r}"
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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.references:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(
    doc: dict[str, Any],
    *,
    action: str,
    source: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": source,
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


def _ingredients(target: Target) -> list[dict[str, Any]]:
    rows = GLUCOSE_FINAL_INGREDIENTS if target.has_glucose else BASE_FINAL_INGREDIENTS
    return [
        _component(name, value, unit, target)
        for name, value, unit in rows
    ]


def _solutions(target: Target) -> list[dict[str, Any]]:
    return [
        _component(name, value, unit, target)
        for name, value, unit in FINAL_SOLUTIONS
    ]


def _variant_child() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{GLUCOSE}",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": GLUCOSE_ID,
        "name": "chopped_meat_medium_with_1_glucose",
        "notes": "ATCC Medium 735 adds 10.0 g/L glucose to ATCC Medium 593.",
    }


def _parent_media() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{BASE}",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": BASE_ID,
        "name": "chopped_meat_medium",
        "notes": "ATCC Medium 735 is ATCC Medium 593 supplemented with 10.0 g/L glucose.",
    }


def _ensure_variant_child(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    child_ref = _variant_child()
    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == GLUCOSE_ID or child.get("path") == child_ref["path"]:
            children[index] = child_ref
            return
    children.append(child_ref)


def repair_target(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(target)
    repaired["solutions"] = _solutions(target)
    _put_after(repaired, "notes", NOTES[target.path], "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(
        repaired,
        action=ACTION,
        source="; ".join(target.references),
        notes=(
            f"{NOTES[target.path]} Corrected imported water, N NaOH, and "
            "0.025% resazurin volumes to ml/L units; retained the anaerobic "
            "N2/H2 headspace gases as variable gas-phase ingredients; grounded "
            "the disclosed chemical and extract ingredients; and left fat-free "
            "ground beef intentionally unmapped."
        ),
    )

    if target.path == BASE:
        _ensure_variant_child(repaired)
        _append_curation_event(
            repaired,
            action=LINK_ACTION,
            source="; ".join((TOGO_M2710, TOGO_M2754, ATCC_593, ATCC_735)),
            notes="Linked ATCC Medium 735 as a glucose-supplemented ATCC Medium 593 variant.",
        )
    else:
        repaired["parent_media"] = _parent_media()
        repaired["variant_relationship"] = "SUPPLEMENTED_VARIANT"
        repaired["variant_modifications"] = [
            "Adds 10.0 g/L glucose to ATCC Medium 593 Chopped meat medium.",
        ]
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_target(_load(path), target)
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
