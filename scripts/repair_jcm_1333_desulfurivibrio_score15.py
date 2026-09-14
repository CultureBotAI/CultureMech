#!/usr/bin/env python3
"""Repair JCM Medium 1333 Desulfurivibrio AMeS2 Medium."""

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
TARGET = "bacterial/JCM_J1333_DESULFURIVIBRIO_AMeS2_MEDIUM.yaml"
EXPECTED_ID = "CultureMech:015831"
EXPECTED_SOURCE_TERM = "jcm.grmd:1333"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_1333_desulfurivibrio_score15.py"
ACTION = "RESOLVED_JCM_1333_DESULFURIVIBRIO_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

JCM_1333 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1333"
JCM_1079 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1079"
JCM_852 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=852"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"
SOURCE = "JCM Medium 1333"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Na2CO3", "22.0", "G_PER_L"),
    ("NaHCO3", "8.0", "G_PER_L"),
    ("NaCl", "6.0", "G_PER_L"),
    ("K2HPO4", "1.0", "G_PER_L"),
    ("Sulfur", "5.0", "G_PER_L"),
    ("1 M MgCl2 solution", "1.0", "ML_PER_L"),
    ("1 M NH4Cl solution", "4.0", "ML_PER_L"),
    ("Trace element solution (see Medium No. 1079 )", "1.0", "ML_PER_L"),
    ("Se/W solution* (see Medium No. 852 )", "1.0", "ML_PER_L"),
    ("Trace vitamins* (see Medium No. 197 )", "1.0", "ML_PER_L"),
    ("5% Na2S·9H2O solution", "5.0", "ML_PER_L"),
)
IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = ()


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
    source: str = SOURCE,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _solution(
    preferred_term: str,
    value: str,
    *,
    notes: str,
    source: str = SOURCE,
    composition: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
    }
    if composition is not None:
        row["composition"] = copy.deepcopy(composition)
    return row


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Na2CO3",
        "22.0",
        "G_PER_L",
        notes="JCM Medium 1333 lists 22.0 g Na2CO3.",
        term=("CHEBI:29377", "sodium carbonate"),
    ),
    _component(
        "NaHCO3",
        "8.0",
        "G_PER_L",
        notes="JCM Medium 1333 lists 8.0 g NaHCO3.",
        term=("CHEBI:32139", "sodium hydrogencarbonate"),
    ),
    _component(
        "NaCl",
        "6.0",
        "G_PER_L",
        notes="JCM Medium 1333 lists 6.0 g NaCl.",
        term=("CHEBI:26710", "sodium chloride"),
    ),
    _component(
        "K2HPO4",
        "1.0",
        "G_PER_L",
        notes="JCM Medium 1333 lists 1.0 g K2HPO4.",
        term=("CHEBI:131527", "dipotassium hydrogen phosphate"),
    ),
    _component(
        "Sulfur",
        "5.0",
        "G_PER_L",
        notes="JCM Medium 1333 lists 5.0 g sulfur steamed separately before use.",
        term=("CHEBI:26833", "sulfur atom"),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution(
        "1 M MgCl2 solution",
        "1.0",
        notes="JCM Medium 1333 adds 1.0 ml/L autoclaved 1 M MgCl2 solution.",
        composition=[
            _component(
                "MgCl2",
                "1",
                "MOLAR",
                notes="Solute of the 1 M MgCl2 stock added by JCM Medium 1333.",
                term=("CHEBI:6636", "magnesium dichloride"),
            )
        ],
    ),
    _solution(
        "1 M NH4Cl solution",
        "4.0",
        notes="JCM Medium 1333 adds 4.0 ml/L autoclaved 1 M NH4Cl solution.",
        composition=[
            _component(
                "NH4Cl",
                "1",
                "MOLAR",
                notes="Solute of the 1 M NH4Cl stock added by JCM Medium 1333.",
                term=("CHEBI:31206", "ammonium chloride"),
            )
        ],
    ),
    _solution(
        "Trace element solution (JCM Medium 1079)",
        "1.0",
        notes=(
            "JCM Medium 1333 adds 1.0 ml/L autoclaved Trace element solution "
            "from JCM Medium 1079."
        ),
        source=f"{SOURCE} / JCM Medium 1079",
    ),
    _solution(
        "Se/W solution (JCM Medium 852)",
        "1.0",
        notes=(
            "JCM Medium 1333 adds 1.0 ml/L filter-sterilized Se/W solution "
            "from JCM Medium 852."
        ),
        source=f"{SOURCE} / JCM Medium 852",
    ),
    _solution(
        "Trace vitamins (JCM Medium 197)",
        "1.0",
        notes=(
            "JCM Medium 1333 adds 1.0 ml/L filter-sterilized Trace vitamins "
            "from JCM Medium 197."
        ),
        source=f"{SOURCE} / JCM Medium 197",
    ),
    _solution(
        "5% Na2S x 9H2O solution",
        "5.0",
        notes=(
            "JCM Medium 1333 conditionally adds 5.0 ml/L autoclaved 5% "
            "Na2S x 9H2O solution if the inoculum lacks sulfide or polysulfide."
        ),
        composition=[
            _component(
                "Na2S x 9H2O",
                "50.0",
                "G_PER_L",
                notes="Solute of the 5% Na2S x 9H2O stock added by JCM Medium 1333.",
                term=("CHEBI:76209", "sodium sulfide nonahydrate"),
            )
        ],
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    _step(
        1,
        "MIX",
        (
            "Add Na2CO3, NaHCO3, NaCl, and K2HPO4 to distilled water and "
            "bring the base volume to 1.0 L."
        ),
    ),
    _step(2, "AUTOCLAVE", "Autoclave the base in closed bottles."),
    _step(
        3,
        "MIX",
        (
            "After cooling, aseptically add MgCl2, NH4Cl, Trace element, "
            "Se/W, and Trace vitamins stocks at the JCM Medium 1333 "
            "per-liter ratios."
        ),
    ),
    _step(4, "HEAT", "Steam sulfur for 3 hr on each of 3 successive days."),
    _step(
        5,
        "MIX",
        (
            "Aseptically and anaerobically distribute the medium and "
            "sterilized sulfur into culture vessels under an N2 gas stream "
            "and seal with butyl rubber stoppers."
        ),
    ),
    _step(
        6,
        "MIX",
        (
            "If the inoculum does not contain sulfide or polysulfide, add "
            "5.0 ml/L autoclaved 5% Na2S x 9H2O solution stored under N2."
        ),
    ),
)

NOTES = (
    "JCM Medium 1333 lists Na2CO3, NaHCO3, NaCl, K2HPO4, and sulfur as direct "
    "components; after autoclaving the base, add MgCl2, NH4Cl, JCM 1079 Trace "
    "element, JCM 852 Se/W, and JCM 197 Trace vitamins stocks, with 5% "
    "Na2S x 9H2O solution added conditionally if the inoculum lacks sulfide or "
    "polysulfide."
)

FINAL_INGREDIENT_SIGNATURE = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in INGREDIENTS
)
FINAL_SOLUTION_SIGNATURE = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in SOLUTIONS
)


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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERM:
        raise ValueError(
            f"{TARGET}: expected source term {EXPECTED_SOURCE_TERM}, found {source_term!r}"
        )

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    solution_signature = _signature(doc.get("solutions"), "solutions")
    if (ingredient_signature, solution_signature) not in {
        (IMPORTED_INGREDIENT_SIGNATURE, IMPORTED_SOLUTION_SIGNATURE),
        (FINAL_INGREDIENT_SIGNATURE, FINAL_SOLUTION_SIGNATURE),
    }:
        raise ValueError(
            f"{TARGET}: ingredient/solution signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to "
            f"{ingredient_signature!r} / {solution_signature!r}"
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

    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference_url in (JCM_1333, JCM_1079, JCM_852, JCM_197):
        if reference_url not in existing:
            references.append({"reference": reference_url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": JCM_1333,
        "notes": NOTES,
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
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
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
