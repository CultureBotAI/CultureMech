#!/usr/bin/env python3
"""Repair sparse KOMODO aliases of DSMZ/MediaDive stock solutions."""

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

CURATOR = "repair_komodo_dsmz_submedia_score15.py"
ACTION = "RESOLVED_KOMODO_DSMZ_SUBMEDIA_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

DSMZ_1003_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1003.pdf"
DSMZ_1145_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1145.pdf"
DSMZ_829_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium829.pdf"
MEDIADIVE_1003 = "https://mediadive.dsmz.de/medium/1003"
MEDIADIVE_1145 = "https://mediadive.dsmz.de/medium/1145"
MEDIADIVE_829 = "https://mediadive.dsmz.de/medium/829"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_media_term: str
    title: str
    source_label: str
    mediadive_solution: str
    mediadive_solution_label: str
    references: tuple[str, str]
    ph_value: float
    ph_adjuster: str
    ingredients: tuple[dict[str, Any], ...]
    preparation_steps: tuple[dict[str, Any], ...]
    notes: str
    sterilization: dict[str, str] | None = None

    @property
    def final_signature(self) -> tuple[Component, ...]:
        return tuple(
            (
                str(row["preferred_term"]),
                str(row["concentration"]["value"]),
                str(row["concentration"]["unit"]),
            )
            for row in self.ingredients
        )

    @property
    def imported_signature(self) -> tuple[Component, ...]:
        return ((self.ph_adjuster, "variable", "VARIABLE"),)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


GROUNDINGS: dict[str, tuple[str, str]] = {
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "MgCl2 x H2O": ("CHEBI:86355", "magnesium dichloride monohydrate"),
    "MgCl2 x 6 H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "HCl": ("CHEBI:17883", "hydrogen chloride"),
    "Isobutyric acid": ("CHEBI:16135", "isobutyric acid"),
    "Valeric acid": ("CHEBI:17418", "valeric acid"),
    "2-Methylbutyric acid": ("CHEBI:37070", "2-methylbutyric acid"),
    "3-Methylbutyric acid": ("CHEBI:28484", "isovaleric acid"),
    "Caproic acid": ("CHEBI:30776", "hexanoic acid"),
    "Succinic acid": ("CHEBI:15741", "succinic acid"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
}

UNIT_LABELS = {"G_PER_L": "g/L", "ML_PER_L": "ml/L", "VARIABLE": "variable amount of"}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    source: str,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    term = _term(*GROUNDINGS[preferred_term])
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": term,
        "mediaingredientmech_chebi_term": copy.deepcopy(term),
    }


def _ph_adjuster(preferred_term: str, source: str, ph: float) -> dict[str, Any]:
    return _component(
        preferred_term,
        "variable",
        "VARIABLE",
        source,
        notes=(
            f"{source} adjusts the stock to pH {ph:g} with {preferred_term}; "
            "the exact amount is variable."
        ),
    )


SOURCE_1003 = "DSMZ Medium 1003 Solution A"
SOURCE_1145 = "DSMZ Medium 1145 Solution A"
SOURCE_829 = "DSMZ Medium 829 Growth-stimulating factors"

SOLUTION_A_1003: tuple[dict[str, Any], ...] = (
    _component("NH4Cl", "100.00", "G_PER_L", SOURCE_1003),
    _component("MgCl2 x H2O", "100.00", "G_PER_L", SOURCE_1003),
    _component("CaCl2 x 2 H2O", "40.00", "G_PER_L", SOURCE_1003),
    _component("Distilled water", "1000.00", "ML_PER_L", SOURCE_1003),
    _ph_adjuster("HCl", SOURCE_1003, 4.0),
)

SOLUTION_A_1145: tuple[dict[str, Any], ...] = (
    _component("NH4Cl", "100.00", "G_PER_L", SOURCE_1145),
    _component("MgCl2 x 6 H2O", "100.00", "G_PER_L", SOURCE_1145),
    _component("CaCl2 x 2 H2O", "40.00", "G_PER_L", SOURCE_1145),
    _component("Distilled water", "1000.00", "ML_PER_L", SOURCE_1145),
    _ph_adjuster("HCl", SOURCE_1145, 4.0),
)

GROWTH_FACTORS_829: tuple[dict[str, Any], ...] = (
    _component("Isobutyric acid", "5.00", "G_PER_L", SOURCE_829),
    _component("Valeric acid", "5.00", "G_PER_L", SOURCE_829),
    _component("2-Methylbutyric acid", "5.00", "G_PER_L", SOURCE_829),
    _component("3-Methylbutyric acid", "5.00", "G_PER_L", SOURCE_829),
    _component("Caproic acid", "2.00", "G_PER_L", SOURCE_829),
    _component("Succinic acid", "6.00", "G_PER_L", SOURCE_829),
    _component("Distilled water", "1000.00", "ML_PER_L", SOURCE_829),
    _ph_adjuster("NaOH", SOURCE_829, 9.0),
)


PREP_1003: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Dissolve NH4Cl, MgCl2 x H2O, and CaCl2 x 2 H2O in distilled water.",
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust Solution A to pH 4 with HCl.",
    },
)

PREP_1145: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare Solution A with anaerobic double distilled water under constant "
            "nitrogen gassing."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust Solution A to pH 4 with HCl.",
    },
)

PREP_829: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Dissolve the organic acids in distilled water.",
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the growth-stimulating factors stock to pH 9.0 with NaOH.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the pH-adjusted stock under 100% N2 gas.",
    },
)

NOTES_1003 = (
    "KOMODO Medium 2025 is Solution A from DSMZ Medium 1003. DSMZ Medium 1003 "
    "defines this 100x stock with 100.00 g NH4Cl, 100.00 g MgCl2 x H2O, "
    "40.00 g CaCl2 x 2 H2O, and 1000.00 ml Distilled water, adjusted to pH 4 "
    "with HCl. MediaDive imports the same stock as mediadive.solution:2047."
)
NOTES_1145 = (
    "KOMODO Medium 2026 is Solution A from DSMZ Medium 1145. DSMZ Medium 1145 "
    "defines this stock with 100.00 g NH4Cl, 100.00 g MgCl2 x 6 H2O, 40.00 g "
    "CaCl2 x 2 H2O, and 1000.00 ml Distilled water, adjusted to pH 4 with HCl. "
    "MediaDive imports the same stock as mediadive.solution:2298."
)
NOTES_829 = (
    "KOMODO Medium 2027 is the Growth-stimulating factors stock from DSMZ "
    "Medium 829. DSMZ Medium 829 defines the stock with 5.00 g each of "
    "Isobutyric acid, Valeric acid, 2-Methylbutyric acid, and 3-Methylbutyric "
    "acid, 2.00 g Caproic acid, 6.00 g Succinic acid, and 1000.00 ml "
    "Distilled water, adjusted to pH 9.0 with NaOH and autoclaved under 100% "
    "N2 gas. MediaDive imports the same stock as mediadive.solution:1680."
)

TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/solution_a_medium_1003.yaml",
        expected_id="CultureMech:004292",
        expected_media_term="komodo.medium:2025",
        title="Solution A (medium 1003)",
        source_label=SOURCE_1003,
        mediadive_solution="mediadive.solution:2047",
        mediadive_solution_label="Solution A (100x solution)",
        references=(DSMZ_1003_PDF, MEDIADIVE_1003),
        ph_value=4.0,
        ph_adjuster="HCl",
        ingredients=SOLUTION_A_1003,
        preparation_steps=PREP_1003,
        notes=NOTES_1003,
    ),
    Target(
        path="bacterial/solution_a_medium_1145.yaml",
        expected_id="CultureMech:004293",
        expected_media_term="komodo.medium:2026",
        title="Solution A (medium 1145)",
        source_label=SOURCE_1145,
        mediadive_solution="mediadive.solution:2298",
        mediadive_solution_label="Solution A",
        references=(DSMZ_1145_PDF, MEDIADIVE_1145),
        ph_value=4.0,
        ph_adjuster="HCl",
        ingredients=SOLUTION_A_1145,
        preparation_steps=PREP_1145,
        notes=NOTES_1145,
    ),
    Target(
        path="bacterial/solution_of_growth_stimulating_factors_medium_829.yaml",
        expected_id="CultureMech:004294",
        expected_media_term="komodo.medium:2027",
        title="Solution of growth-stimulating factors (medium 829)",
        source_label=SOURCE_829,
        mediadive_solution="mediadive.solution:1680",
        mediadive_solution_label="Growth-stimulating factors",
        references=(DSMZ_829_PDF, MEDIADIVE_829),
        ph_value=9.0,
        ph_adjuster="NaOH",
        ingredients=GROWTH_FACTORS_829,
        preparation_steps=PREP_829,
        notes=NOTES_829,
        sterilization={"method": "AUTOCLAVE"},
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after_key: str) -> None:
    rebuilt: dict[str, Any] = {}
    placed = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        rebuilt[existing_key] = existing_value
        if existing_key == after_key:
            rebuilt[key] = value
            placed = True
    if not placed:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ingredient_signature(rows: Any) -> tuple[Component, ...]:
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


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.expected_media_term:
        raise ValueError(
            f"{target.path}: expected source term {target.expected_media_term}, "
            f"found {source_term!r}"
        )

    signature = _ingredient_signature(doc.get("ingredients"))
    if signature not in (target.imported_signature, target.final_signature):
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.imported_signature!r} to {signature!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag
        not in {
            "has_unmapped_ingredients",
            "incomplete_composition",
            "needs_manual_curation",
        }
    ]
    flags.extend(("has_ontology_mappings", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.references:
        if url not in existing:
            references.append({"reference": url})
            existing.add(url)


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
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
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(target.ingredients))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", target.notes, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(target.preparation_steps)),
        "ingredients",
    )
    if target.sterilization is None:
        repaired.pop("sterilization", None)
    else:
        repaired["sterilization"] = copy.deepcopy(target.sterilization)
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _ensure_event(repaired, target)
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
    for path, doc in sorted(plans.items()):
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
