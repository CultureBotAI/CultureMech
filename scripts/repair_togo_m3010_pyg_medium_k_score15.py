#!/usr/bin/env python3
"""Repair TOGO M3010 / JCM Medium 1338 PYG Medium (K)."""

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
TARGET = Path("bacterial/pyg_medium_k.yaml")
EXPECTED_ID = "CultureMech:009528"
EXPECTED_MEDIA_TERM = "TOGO:M3010"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m3010_pyg_medium_k_score15.py"
ACTION = "RESOLVED_TOGO_M3010_PYG_MEDIUM_K_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M3010 = "https://togomedium.org/medium/M3010"
TOGO_M695 = "https://togomedium.org/medium/M695"
TOGO_M470 = "https://togomedium.org/medium/M470"
JCM_1338 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1338"
JCM_676 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=676"
JCM_469 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469"
REFERENCES = (TOGO_M3010, JCM_1338, TOGO_M695, JCM_676, TOGO_M470, JCM_469)

SOURCE = "TOGO M3010 / JCM Medium 1338"
SALT_SOURCE = "TOGO M695 / JCM Medium 676"
HM_SOURCE = "TOGO M470 / JCM Medium 469"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "940", "G_PER_L"),
    ("Yeast extract", "10", "G_PER_L"),
    ("KH2PO4", "2", "G_PER_L"),
    ("Resazurin", "1", "G_PER_L"),
    ("Trypticase peptone", "5", "G_PER_L"),
    ("L-Cysteine·HCl·H2O", "0.5", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

SALT_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("CaCl2 x 2H2O", "0.25", "G_PER_L"),
    ("MgSO4 x 7H2O", "0.5", "G_PER_L"),
    ("K2HPO4", "1.0", "G_PER_L"),
    ("KH2PO4", "1.0", "G_PER_L"),
    ("NaHCO3", "10.0", "G_PER_L"),
    ("NaCl", "2.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

HEMIN_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Hemin", "0.5", "G_PER_L"),
    ("1 N NaOH", "10.0", "ML_PER_L"),
)

MENADIONE_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Menadione", "0.05", "G_PER_L"),
    ("Ethanol", "10.0", "ML_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Salt solution (see Medium [M695])", "40", "G_PER_L", ()),
    ("Hemin solution (see Medium [M470])", "10", "G_PER_L", ()),
    ("Menadione solution (see Medium [M470])", "10", "G_PER_L", ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Trypticase peptone", "5.0", "G_PER_L"),
    ("Peptone", "5.0", "G_PER_L"),
    ("Yeast extract", "10.0", "G_PER_L"),
    ("KH2PO4", "2.0", "G_PER_L"),
    ("L-Cysteine x HCl x H2O", "0.5", "G_PER_L"),
    ("Resazurin", "1.0", "MG_PER_L"),
    ("Distilled water", "940.0", "ML_PER_L"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Salt solution", "40.0", "ML_PER_L", SALT_SOLUTION_SIGNATURE),
    ("Hemin solution", "10.0", "ML_PER_L", HEMIN_SOLUTION_SIGNATURE),
    ("Menadione solution", "10.0", "ML_PER_L", MENADIONE_SOLUTION_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "1 N NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Ethanol": ("CHEBI:16236", "ethanol"),
    "Hemin": ("CHEBI:50385", "hemin"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "L-Cysteine x HCl x H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "Menadione": ("CHEBI:28869", "menadione"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "Peptone": ("MICRO:0000178", "Peptone"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Trypticase peptone": ("MICRO:0000175", "Trypticase peptone"),
    "Yeast extract": ("FOODON:03315426", "Yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "VARIABLE": "variable",
}

NOTES = (
    "TOGO M3010 imports JCM Medium 1338 PYG Medium (K). JCM Medium 1338 lists "
    "5 g trypticase peptone, 5 g peptone, 10 g yeast extract, 2 g KH2PO4, "
    "0.5 g L-Cysteine HCl H2O, 1 mg resazurin, 40 ml salt solution from JCM "
    "Medium 676, and 940 ml distilled water, then instructs anaerobic addition "
    "of 10 ml hemin solution and 10 ml menadione solution from JCM Medium 469 "
    "after autoclaving under N2."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Mix the basal PYG Medium (K) components thoroughly.",
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the basal medium under a nitrogen atmosphere.",
    },
    {
        "step_number": 3,
        "action": "COOL",
        "description": "Cool the autoclaved basal medium.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Aseptically and anaerobically add autoclaved hemin solution and "
            "menadione solution."
        ),
    },
    {
        "step_number": 5,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0-7.2, if necessary.",
    },
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str | None = None,
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
    return row


def _solution(
    preferred_term: str,
    value: str,
    *,
    source: str,
    notes: str,
    composition: tuple[dict[str, Any], ...],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": copy.deepcopy(list(composition)),
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component("Trypticase peptone", "5.0", "G_PER_L", source=SOURCE),
    _component("Peptone", "5.0", "G_PER_L", source=SOURCE),
    _component("Yeast extract", "10.0", "G_PER_L", source=SOURCE),
    _component("KH2PO4", "2.0", "G_PER_L", source=SOURCE),
    _component("L-Cysteine x HCl x H2O", "0.5", "G_PER_L", source=SOURCE),
    _component("Resazurin", "1.0", "MG_PER_L", source=SOURCE),
    _component("Distilled water", "940.0", "ML_PER_L", source=SOURCE),
    _component(
        "Nitrogen gas",
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes="JCM Medium 1338 instructs autoclaving the basal medium under N2.",
    ),
)

SALT_SOLUTION: tuple[dict[str, Any], ...] = tuple(
    _component(*component, source=SALT_SOURCE)
    for component in SALT_SOLUTION_SIGNATURE
)

HEMIN_SOLUTION: tuple[dict[str, Any], ...] = (
    _component(
        "Hemin",
        "0.5",
        "G_PER_L",
        source=HM_SOURCE,
        notes=(
            "JCM Medium 469 dissolves 50 mg hemin in 1 ml of 1 N NaOH and "
            "adjusts to 100 ml."
        ),
    ),
    _component(
        "1 N NaOH",
        "10.0",
        "ML_PER_L",
        source=HM_SOURCE,
        notes=(
            "JCM Medium 469 dissolves hemin in 1 ml of 1 N NaOH before "
            "adjusting the hemin solution to 100 ml."
        ),
    ),
)

MENADIONE_SOLUTION: tuple[dict[str, Any], ...] = (
    _component(
        "Menadione",
        "0.05",
        "G_PER_L",
        source=HM_SOURCE,
        notes=(
            "JCM Medium 469 dissolves 5 mg menadione in 1 ml ethanol and "
            "adjusts to 100 ml."
        ),
    ),
    _component(
        "Ethanol",
        "10.0",
        "ML_PER_L",
        source=HM_SOURCE,
        notes=(
            "JCM Medium 469 dissolves menadione in 1 ml ethanol before "
            "adjusting the menadione solution to 100 ml."
        ),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution(
        "Salt solution",
        "40.0",
        source=SALT_SOURCE,
        notes="JCM Medium 1338 adds 40.0 ml/L salt solution from JCM Medium 676.",
        composition=SALT_SOLUTION,
    ),
    _solution(
        "Hemin solution",
        "10.0",
        source=HM_SOURCE,
        notes="JCM Medium 1338 adds 10.0 ml/L hemin solution from JCM Medium 469.",
        composition=HEMIN_SOLUTION,
    ),
    _solution(
        "Menadione solution",
        "10.0",
        source=HM_SOURCE,
        notes=(
            "JCM Medium 1338 adds 10.0 ml/L menadione solution from JCM "
            "Medium 469."
        ),
        composition=MENADIONE_SOLUTION,
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
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


def _solution_signatures(rows: Any) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("solutions contains a non-mapping row")
        row_signature = _signature([row], "solutions")[0]
        signatures.append(
            (
                row_signature[0],
                row_signature[1],
                row_signature[2],
                _signature(row.get("composition"), "solution composition"),
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

    signature = (
        _signature(doc.get("ingredients"), "ingredients"),
        _solution_signatures(doc.get("solutions")),
    )
    allowed = (
        (IMPORTED_INGREDIENT_SIGNATURE, IMPORTED_SOLUTION_SIGNATURES),
        (FINAL_INGREDIENT_SIGNATURE, FINAL_SOLUTION_SIGNATURES),
    )
    if signature not in allowed:
        raise ValueError(f"{TARGET}: recipe signature drifted")


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    doc.pop(key, None)
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

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "has_unmapped_ingredients",
    ):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
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
            existing.add(reference)


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Corrected TOGO M3010 ml and mg imports, added pH 7.0-7.2, "
            "expanded the salt, hemin, and menadione stocks from JCM "
            "cross-references, and grounded all disclosed PYG Medium (K) "
            "ingredients and stock components."
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
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_range", {"min": 7.0, "max": 7.2}, "physical_state")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
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
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
