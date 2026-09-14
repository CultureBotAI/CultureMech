#!/usr/bin/env python3
"""Repair ATCC Medium 35 Bordet Gengou Agar/Broth TOGO records."""

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

CURATOR = "repair_togo_m2307_m2308_bordet_atcc_score15.py"
ACTION = "RESOLVED_TOGO_M2307_M2308_BORDET_ATCC_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

ATCC_35 = "https://www.atcc.org/~/media/4A3EC418D3294A4E9678D5BFA6473F4A.ashx"
TOGO_M2307 = "https://togomedium.org/medium/M2307"
TOGO_M2308 = "https://togomedium.org/medium/M2308"
SOURCE = "ATCC Medium 35"
PH_VALUE = 6.7

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term: str
    source: str
    togo_url: str
    imported_ingredients: tuple[Component, ...]
    final_ingredients: tuple[dict[str, Any], ...]
    preparation_steps: tuple[dict[str, Any], ...]
    notes: str
    final_solutions: tuple[dict[str, Any], ...] = ()

    @property
    def references(self) -> tuple[str, str]:
        return (self.togo_url, ATCC_35)


IMPORTED_M2307: tuple[Component, ...] = (
    ("Glycerol", "10", "G_PER_L"),
    ("DI Water", "840", "G_PER_L"),
    ("Proteose Peptone", "10", "G_PER_L"),
    ("Bordet-Gengou Agar Base (BD 248200)", "30", "G_PER_L"),
    ("Sterile Defibrinated Rabbit Blood", "150", "G_PER_L"),
)

IMPORTED_M2308: tuple[Component, ...] = (
    ("Glycerol", "10", "G_PER_L"),
    ("Proteose Peptone", "10", "G_PER_L"),
    ("Bordet-Gengou Broth Base (see below)", "840", "G_PER_L"),
    ("Sterile Defibrinated Rabbit Blood", "150", "G_PER_L"),
    ("NaCl", "5.5", "G_PER_L"),
    ("DI Water", "1000", "G_PER_L"),
    ("Potato", "125", "G_PER_L"),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    notes: str,
    *,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


def _blood(source: str) -> dict[str, Any]:
    return _ingredient(
        "Sterile Defibrinated Rabbit Blood",
        "15",
        "PERCENT_V_V",
        f"{source} lists 150 ml sterile defibrinated rabbit blood per liter.",
        term=("UBERON:0000178", "blood"),
    )


AGAR_INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "Bordet-Gengou Agar Base (BD 248200)",
        "30.0",
        "G_PER_L",
        ("ATCC Medium 35 lists 30.0 g/L commercial Bordet-Gengou Agar Base " "(BD 248200)."),
    ),
    _ingredient(
        "Glycerol",
        "10.0",
        "ML_PER_L",
        "ATCC Medium 35 lists 10.0 ml/L glycerol.",
        term=("CHEBI:17754", "glycerol"),
    ),
    _ingredient(
        "Proteose Peptone",
        "10.0",
        "G_PER_L",
        "ATCC Medium 35 lists 10.0 g/L Proteose Peptone.",
        term=("MICRO:0000180", "Proteose Peptone"),
    ),
    _ingredient(
        "DI Water",
        "840.0",
        "ML_PER_L",
        "ATCC Medium 35 lists 840 ml/L DI Water in the agar base.",
        term=("CHEBI:15377", "water"),
    ),
    _blood("ATCC Medium 35"),
)

BROTH_BASE_COMPOSITION: tuple[dict[str, Any], ...] = (
    _ingredient(
        "Potato",
        "125.0",
        "G_PER_L",
        "ATCC Medium 35 boils 125 g potato while preparing Bordet-Gengou Broth Base.",
    ),
    _ingredient(
        "NaCl",
        "5.5",
        "G_PER_L",
        "ATCC Medium 35 lists 5.5 g/L NaCl in Bordet-Gengou Broth Base.",
        term=("CHEBI:26710", "sodium chloride"),
    ),
    _ingredient(
        "DI Water",
        "1000.0",
        "ML_PER_L",
        "ATCC Medium 35 brings Bordet-Gengou Broth Base back to 1000 ml.",
        term=("CHEBI:15377", "water"),
    ),
)

BROTH_INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "Glycerol",
        "10.0",
        "ML_PER_L",
        "ATCC Medium 35 lists 10.0 ml/L glycerol.",
        term=("CHEBI:17754", "glycerol"),
    ),
    _ingredient(
        "Proteose Peptone",
        "10.0",
        "G_PER_L",
        "ATCC Medium 35 lists 10.0 g/L Proteose Peptone.",
        term=("MICRO:0000180", "Proteose Peptone"),
    ),
    _blood("ATCC Medium 35"),
)

BROTH_SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Bordet-Gengou Broth Base",
        "concentration": {"value": "840.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": "ATCC Medium 35 adds 840 ml/L prepared Bordet-Gengou Broth Base.",
        "composition": list(copy.deepcopy(BROTH_BASE_COMPOSITION)),
        "preparation_notes": (
            "Cut and boil 125 g of potato, filter the potato broth through "
            "cheesecloth, filter again, and bring the volume back to 1000 ml."
        ),
    },
)

AGAR_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    _step(
        1,
        "MIX",
        ("Suspend Bordet-Gengou Agar Base, glycerol, and Proteose Peptone " "in 840 ml DI Water."),
    ),
    _step(2, "ADJUST_PH", "Adjust to pH 6.7 +/- 0.2."),
    _step(3, "AUTOCLAVE", "Autoclave the base at 121 C."),
    _step(
        4,
        "COOL",
        "Cool the base to 45-50 C and add 150 ml sterile defibrinated rabbit blood.",
    ),
)

BROTH_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    _step(
        1,
        "MIX",
        ("Mix glycerol and Proteose Peptone into 840 ml prepared " "Bordet-Gengou Broth Base."),
    ),
    _step(2, "ADJUST_PH", "Adjust to pH 6.7 +/- 0.2."),
    _step(3, "AUTOCLAVE", "Autoclave the base at 121 C."),
    _step(
        4,
        "COOL",
        "Cool the base to 45-50 C and add 150 ml sterile defibrinated rabbit blood.",
    ),
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": (
        "ATCC Medium 35 autoclaves the base at 121 C, then cools it to 45-50 C "
        "before adding sterile defibrinated rabbit blood."
    ),
}

AGAR_NOTES = (
    "TOGO M2307 imports ATCC Medium 35 Bordet Gengou Agar Medium. ATCC Medium 35 "
    "prepares the agar from 30.0 g Bordet-Gengou Agar Base (BD 248200), 10.0 ml "
    "glycerol, 10.0 g Proteose Peptone, and 840 ml DI Water, adjusts to pH "
    "6.7 +/- 0.2, autoclaves at 121 C, cools the base to 45-50 C, and adds "
    "150 ml sterile defibrinated rabbit blood."
)

BROTH_NOTES = (
    "TOGO M2308 imports ATCC Medium 35 Bordet Gengou Broth Medium. ATCC Medium 35 "
    "prepares the broth from 10.0 ml glycerol, 10.0 g Proteose Peptone, 840 ml "
    "Bordet-Gengou Broth Base, and 150 ml sterile defibrinated rabbit blood. "
    "The broth base is prepared from 125 g potato, 5.5 g NaCl, and DI Water "
    "brought back to 1000 ml."
)

TARGETS: tuple[Target, ...] = (
    Target(
        path=Path("bacterial/bordet_gengou_agar_medium.yaml"),
        record_id="CultureMech:008893",
        media_term="TOGO:M2307",
        source="TOGO M2307 / ATCC Medium 35",
        togo_url=TOGO_M2307,
        imported_ingredients=IMPORTED_M2307,
        final_ingredients=AGAR_INGREDIENTS,
        preparation_steps=AGAR_PREPARATION_STEPS,
        notes=AGAR_NOTES,
    ),
    Target(
        path=Path("bacterial/bordet_gengou_broth_medium.yaml"),
        record_id="CultureMech:008894",
        media_term="TOGO:M2308",
        source="TOGO M2308 / ATCC Medium 35",
        togo_url=TOGO_M2308,
        imported_ingredients=IMPORTED_M2308,
        final_ingredients=BROTH_INGREDIENTS,
        final_solutions=BROTH_SOLUTIONS,
        preparation_steps=BROTH_PREPARATION_STEPS,
        notes=BROTH_NOTES,
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}


def _component_signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
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


def _solution_signatures(solutions: Any) -> tuple[SolutionSignature, ...]:
    if solutions is None:
        solutions = []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"solution {solution.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _component_signature(solution.get("composition"), "solutions.composition"),
            )
        )
    return tuple(signatures)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _final_solution_signature(target: Target) -> tuple[SolutionSignature, ...]:
    return _solution_signatures(list(copy.deepcopy(target.final_solutions)))


def _final_ingredient_signature(target: Target) -> tuple[Component, ...]:
    return _component_signature(list(copy.deepcopy(target.final_ingredients)), "ingredients")


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.media_term:
        raise ValueError(
            f"{target.path}: expected media term {target.media_term}, "
            f"found {_source_term_id(doc)!r}"
        )

    ingredient_signature = _component_signature(doc.get("ingredients"), "ingredients")
    solution_signature = _solution_signatures(doc.get("solutions"))
    if (ingredient_signature, solution_signature) not in {
        (target.imported_ingredients, ()),
        (_final_ingredient_signature(target), _final_solution_signature(target)),
    }:
        raise ValueError(
            f"{target.path}: ingredient/solution signature drifted from "
            f"{target.imported_ingredients!r} to "
            f"{ingredient_signature!r} / {solution_signature!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
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
    for reference in target.references:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.references),
        "notes": target.notes,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["ph_value"] = PH_VALUE
    repaired["notes"] = target.notes
    repaired["ingredients"] = copy.deepcopy(list(target.final_ingredients))
    if target.final_solutions:
        repaired["solutions"] = copy.deepcopy(list(target.final_solutions))
    else:
        repaired.pop("solutions", None)
    repaired["preparation_steps"] = copy.deepcopy(list(target.preparation_steps))
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
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
