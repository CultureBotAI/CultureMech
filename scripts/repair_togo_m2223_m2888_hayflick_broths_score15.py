#!/usr/bin/env python3
"""Repair TOGO M2223 and M2888 Modified Hayflick broth records."""

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

CURATOR = "repair_togo_m2223_m2888_hayflick_broths_score15.py"
ACTION = "RESOLVED_TOGO_M2223_M2888_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

PHENOL_RED_M2888 = "0.5% phenol red (Flow)"
PHENOL_RED_M2223 = "0.5% Phenol red (Flow)"
WATER = "Distilled water"
D_GLUCOSE_M2888 = "D-glucose"
D_GLUCOSE_M2223 = "D-Glucose"
YEAST = "Liquid yeast extract (Flow)"
FBS = "Fetal bovine serum (Flow), heat-inactivated"
HORSE_SERUM = "heat-inactivated horse serum"
PPLO_M2888 = "PPLO broth base without crystal violet (Difco)"
PPLO_M2223 = "PPLO broth base without crystal violet (Difco\uff09"
PPLO_FINAL = "PPLO broth base without crystal violet (Difco)"
PENICILLIN_M2888 = "Penicillin G (Parke, Davis & Co)"
PENICILLIN_M2223 = "Penicillin G (Parke)"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str
    title: str
    togo_url: str
    phenol_red_name: str
    glucose_name: str
    serum_name: str
    pplo_name: str
    penicillin_name: str
    serum_grounding: tuple[str, str]
    serum_note: str
    imported_signature: tuple[Component, ...]

    @property
    def source(self) -> str:
        return f"TOGO {self.expected_media_term.removeprefix('TOGO:')}"

    @property
    def final_signature(self) -> tuple[Component, ...]:
        return (
            (self.phenol_red_name, "4.0", "ML_PER_L"),
            (WATER, "1.0", "L"),
            (self.glucose_name, "5.0", "G_PER_L"),
            (YEAST, "100.0", "ML_PER_L"),
            (self.serum_name, "200.0", "ML_PER_L"),
            (PPLO_FINAL, "21.0", "G_PER_L"),
            (self.penicillin_name, "variable", "VARIABLE"),
        )


TARGET_M2888 = Target(
    path=Path("bacterial/modified_hayflick_broth_medium_containing_20_fetal_bovine_serum.yaml"),
    expected_id="CultureMech:009423",
    expected_media_term="TOGO:M2888",
    title="Modified Hayflick broth medium containing 20% fetal bovine serum",
    togo_url="https://togomedium.org/medium/M2888",
    phenol_red_name=PHENOL_RED_M2888,
    glucose_name=D_GLUCOSE_M2888,
    serum_name=FBS,
    pplo_name=PPLO_M2888,
    penicillin_name=PENICILLIN_M2888,
    serum_grounding=("", ""),
    serum_note=(
        "TOGO M2888 lists 200 ml/L heat-inactivated fetal bovine serum from Flow; "
        "MIM resolves fetal bovine serum to NCIT:C113696, but NCIT is not an "
        "allowed ingredient prefix in the CultureMech schema, so this serum "
        "remains intentionally unmapped."
    ),
    imported_signature=(
        (PHENOL_RED_M2888, "4", "G_PER_L"),
        (WATER, "1", "G_PER_L"),
        (D_GLUCOSE_M2888, "5", "G_PER_L"),
        (YEAST, "100", "G_PER_L"),
        (FBS, "200", "G_PER_L"),
        (PPLO_M2888, "21", "G_PER_L"),
        (PENICILLIN_M2888, "variable", "VARIABLE"),
    ),
)

TARGET_M2223 = Target(
    path=Path(
        "bacterial/" "modified_hayflick_medium_containing_20_v_v_heat_inactivated_horse_serum.yaml"
    ),
    expected_id="CultureMech:008811",
    expected_media_term="TOGO:M2223",
    title="Modified Hayflick medium containing 20% (v/v) heat-inactivated horse serum",
    togo_url="https://togomedium.org/medium/M2223",
    phenol_red_name=PHENOL_RED_M2223,
    glucose_name=D_GLUCOSE_M2223,
    serum_name=HORSE_SERUM,
    pplo_name=PPLO_M2223,
    penicillin_name=PENICILLIN_M2223,
    serum_grounding=("MICRO:0001235", "Horse serum"),
    serum_note="TOGO M2223 lists 200 ml/L heat-inactivated horse serum.",
    imported_signature=(
        (PHENOL_RED_M2223, "4", "G_PER_L"),
        (WATER, "1", "G_PER_L"),
        (D_GLUCOSE_M2223, "5", "G_PER_L"),
        (YEAST, "100", "G_PER_L"),
        (HORSE_SERUM, "200", "G_PER_L"),
        (PPLO_M2223, "21", "G_PER_L"),
        (PENICILLIN_M2223, "variable", "VARIABLE"),
    ),
)

TARGETS = (TARGET_M2223, TARGET_M2888)

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    D_GLUCOSE_M2223: ("CHEBI:17634", "D-glucose"),
    D_GLUCOSE_M2888: ("CHEBI:17634", "D-glucose"),
    YEAST: ("FOODON:03315426", "Yeast extract"),
    HORSE_SERUM: TARGET_M2223.serum_grounding,
    PENICILLIN_M2223: ("CHEBI:51765", "benzylpenicillin sodium"),
    PENICILLIN_M2888: ("CHEBI:51765", "benzylpenicillin sodium"),
}

MEDIAINGREDIENT_CHEBI = frozenset(
    {
        WATER,
        D_GLUCOSE_M2223,
        D_GLUCOSE_M2888,
    }
)

NOTES = {
    TARGET_M2223.expected_media_term: (
        "TOGO M2223 records Modified Hayflick medium containing 20% v/v "
        "heat-inactivated horse serum as 4 ml/L 0.5% Phenol red, 1 L "
        "distilled water, 5 g/L D-Glucose, 100 ml/L Liquid yeast extract "
        "(Flow), 200 ml/L heat-inactivated horse serum, 21 g/L PPLO broth "
        "base without crystal violet from Difco, Penicillin G, pH 7.8, and "
        "growth at 37 C."
    ),
    TARGET_M2888.expected_media_term: (
        "TOGO M2888 records Modified Hayflick broth medium containing 20% "
        "fetal bovine serum as 4 ml/L 0.5% phenol red, 1 L distilled water, "
        "5 g/L D-glucose, 100 ml/L Liquid yeast extract (Flow), 200 ml/L "
        "heat-inactivated fetal bovine serum from Flow, 21 g/L PPLO broth "
        "base without crystal violet from Difco, 5 x 10^5 U/L Penicillin G, "
        "pH 7.8, and growth at 37 C."
    ),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient_notes(target: Target, name: str) -> str:
    if name == target.phenol_red_name:
        return f"{target.source} lists 4 ml/L of 0.5% Phenol red solution from Flow."
    if name == WATER:
        return f"{target.source} lists 1 L Distilled water."
    if name == target.glucose_name:
        return f"{target.source} lists 5 g/L D-glucose."
    if name == YEAST:
        return f"{target.source} lists 100 ml/L Liquid yeast extract from Flow."
    if name == target.serum_name:
        return target.serum_note
    if name == PPLO_FINAL:
        return (
            f"{target.source} lists 21 g/L PPLO broth base without crystal violet "
            "from Difco; this catalog broth is retained as an opaque component."
        )
    if name == target.penicillin_name:
        return (
            f"{target.source} lists Penicillin G without a schema-compatible mass "
            "concentration; the antibiotic identity is grounded but its amount is "
            "retained as variable."
        )
    raise KeyError(name)


def _component(
    target: Target,
    preferred_term: str,
    value: str,
    unit: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": target.source,
        "notes": _ingredient_notes(target, preferred_term),
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if preferred_term in MEDIAINGREDIENT_CHEBI:
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(target: Target) -> list[dict[str, Any]]:
    return [_component(target, name, value, unit) for name, value, unit in target.final_signature]


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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(f"{target.path}: expected media term {target.expected_media_term}")

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in (target.imported_signature, target.final_signature):
        raise ValueError(f"{target.path}: ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
    ):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    if not any(
        isinstance(row, dict) and row.get("reference") == target.togo_url for row in references
    ):
        references.append({"reference": target.togo_url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": target.togo_url,
        "notes": (
            f"{NOTES[target.expected_media_term]} Corrected the imported ml/L and "
            "water units, added pH 7.8 and 37 C, grounded the serum, Liquid "
            "yeast extract, D-glucose, and Penicillin G, and retained the PPLO "
            "broth product and phenol-red stock solution as intentionally unmapped."
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.8, "physical_state")
    _put_after(repaired, "temperature_value", 37.0, "ph_value")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(target)
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES[target.expected_media_term], "media_term")
    repaired.pop("preparation_steps", None)
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
        for target in TARGETS
    }


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
