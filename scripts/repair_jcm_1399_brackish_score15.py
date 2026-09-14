#!/usr/bin/env python3
"""Repair JCM Medium 1399 Artificial Brackish Water Medium 2."""

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
TARGET = "bacterial/JCM_J1399_ARTIFICIAL_BRACKISH_WATER_MEDIUM_2.yaml"
EXPECTED_ID = "CultureMech:015853"
EXPECTED_SOURCE_TERM = "jcm.grmd:1399"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_1399_brackish_score15.py"
ACTION = "RESOLVED_JCM_1399_BRACKISH_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

JCM_1399 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1399"
JCM_439 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439"
JCM_431 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431"
JCM_403 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403"
SOURCE = "JCM Medium 1399"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "13.2", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("KCl", "0.5", "G_PER_L"),
    ("Na2SO4", "4.0", "G_PER_L"),
    ("Trace element solution (see Medium No. 439 )", "1.0", "ML_PER_L"),
    ("Selenite tungstate solution (see Medium No. 431 )", "1.0", "ML_PER_L"),
    ("Resazurin", "1.0", "MG_PER_L"),
    ("Distilled water", "940.0", "ML_PER_L"),
    ("8% NaHCO3 solution*", "30.0", "ML_PER_L"),
    ("1 M MgCl2·6H2O solution", "17.0", "ML_PER_L"),
    ("1 M CaCl2·2H2O solution", "1.0", "ML_PER_L"),
    ("Vitamin solution (see Medium No. 403 )*", "1.0", "ML_PER_L"),
    ("Thiamine solution (see Medium No. 403 )*", "1.0", "ML_PER_L"),
    ("Vitamin B12 solution (see Medium No. 403 )*", "1.0", "ML_PER_L"),
    ("1 M Sodium formate solution", "5.0", "ML_PER_L"),
    ("1 M Sodium acetate solution", "2.0", "ML_PER_L"),
    ("5% Na2S·9H2O solution", "6.0", "ML_PER_L"),
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
        "NaCl",
        "13.2",
        "G_PER_L",
        notes="JCM Medium 1399 lists 13.2 g NaCl.",
        term=("CHEBI:26710", "sodium chloride"),
    ),
    _component(
        "KH2PO4",
        "0.2",
        "G_PER_L",
        notes="JCM Medium 1399 lists 0.2 g KH2PO4.",
        term=("CHEBI:63036", "potassium dihydrogen phosphate"),
    ),
    _component(
        "NH4Cl",
        "0.25",
        "G_PER_L",
        notes="JCM Medium 1399 lists 0.25 g NH4Cl.",
        term=("CHEBI:31206", "ammonium chloride"),
    ),
    _component(
        "KCl",
        "0.5",
        "G_PER_L",
        notes="JCM Medium 1399 lists 0.5 g KCl.",
        term=("CHEBI:32588", "potassium chloride"),
    ),
    _component(
        "Na2SO4",
        "4.0",
        "G_PER_L",
        notes="JCM Medium 1399 lists 4.0 g Na2SO4.",
        term=("CHEBI:32149", "sodium sulfate"),
    ),
    _component(
        "Resazurin",
        "1.0",
        "MG_PER_L",
        notes="JCM Medium 1399 lists 1.0 mg resazurin.",
        term=("CHEBI:8806", "Resazurin"),
    ),
    _component(
        "Distilled water",
        "940.0",
        "ML_PER_L",
        notes="JCM Medium 1399 lists 940.0 ml distilled water in the base.",
        term=("CHEBI:15377", "water"),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution(
        "Trace element solution (JCM Medium 439)",
        "1.0",
        notes="JCM Medium 1399 adds 1.0 ml/L Trace element solution from JCM 439.",
        source=f"{SOURCE} / JCM Medium 439",
    ),
    _solution(
        "Selenite-tungstate solution (JCM Medium 431)",
        "1.0",
        notes=(
            "JCM Medium 1399 adds 1.0 ml/L Selenite-tungstate solution from "
            "JCM 431."
        ),
        source=f"{SOURCE} / JCM Medium 431",
    ),
    _solution(
        "8% NaHCO3 solution",
        "30.0",
        notes="JCM Medium 1399 adds 30.0 ml/L filter-sterilized 8% NaHCO3 solution.",
        composition=[
            _component(
                "NaHCO3",
                "80.0",
                "G_PER_L",
                notes="Solute of the 8% NaHCO3 stock added by JCM Medium 1399.",
                term=("CHEBI:32139", "sodium hydrogencarbonate"),
            )
        ],
    ),
    _solution(
        "1 M MgCl2 x 6H2O solution",
        "17.0",
        notes=(
            "JCM Medium 1399 adds 17.0 ml/L anaerobic 1 M MgCl2 x 6H2O "
            "solution."
        ),
    ),
    _solution(
        "1 M CaCl2 x 2H2O solution",
        "1.0",
        notes=(
            "JCM Medium 1399 adds 1.0 ml/L anaerobic 1 M CaCl2 x 2H2O "
            "solution."
        ),
    ),
    _solution(
        "Vitamin solution (JCM Medium 403)",
        "1.0",
        notes="JCM Medium 1399 adds 1.0 ml/L filter-sterilized Vitamin solution.",
        source=f"{SOURCE} / JCM Medium 403",
    ),
    _solution(
        "Thiamine solution (JCM Medium 403)",
        "1.0",
        notes="JCM Medium 1399 adds 1.0 ml/L filter-sterilized Thiamine solution.",
        source=f"{SOURCE} / JCM Medium 403",
    ),
    _solution(
        "Vitamin B12 solution (JCM Medium 403)",
        "1.0",
        notes="JCM Medium 1399 adds 1.0 ml/L filter-sterilized Vitamin B12 solution.",
        source=f"{SOURCE} / JCM Medium 403",
    ),
    _solution(
        "1 M Sodium formate solution",
        "5.0",
        notes="JCM Medium 1399 adds 5.0 ml/L anaerobic 1 M Sodium formate solution.",
    ),
    _solution(
        "1 M Sodium acetate solution",
        "2.0",
        notes="JCM Medium 1399 adds 2.0 ml/L anaerobic 1 M Sodium acetate solution.",
    ),
    _solution(
        "5% Na2S x 9H2O solution",
        "6.0",
        notes=(
            "JCM Medium 1399 adds 6.0 ml/L autoclaved 5% Na2S x 9H2O "
            "solution before use to reduce the medium."
        ),
        composition=[
            _component(
                "Na2S x 9H2O",
                "50.0",
                "G_PER_L",
                notes="Solute of the 5% Na2S x 9H2O stock added by JCM Medium 1399.",
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
            "Mix NaCl, KH2PO4, NH4Cl, KCl, Na2SO4, Trace element solution, "
            "Selenite-tungstate solution, resazurin, and distilled water."
        ),
    ),
    _step(
        2,
        "AUTOCLAVE",
        "Autoclave the base under an N2-CO2 (4:1, v/v) gas atmosphere.",
    ),
    _step(
        3,
        "MIX",
        (
            "After cooling, add bicarbonate, MgCl2 x 6H2O, CaCl2 x 2H2O, "
            "vitamin, thiamine, vitamin B12, sodium formate, and sodium "
            "acetate stocks at the JCM Medium 1399 per-liter ratios."
        ),
    ),
    _step(
        4,
        "ALIQUOT",
        (
            "Aseptically and anaerobically distribute 20 ml medium into 60 ml "
            "serum bottles under the same N2-CO2 gas mixture and seal with "
            "butyl rubber stoppers."
        ),
    ),
    _step(
        5,
        "MIX",
        (
            "Prior to use, add 6.0 ml/L autoclaved 5% Na2S x 9H2O solution "
            "stored under N2 to reduce the medium."
        ),
    ),
)

NOTES = (
    "JCM Medium 1399 base salts, resazurin, and distilled water are direct "
    "components; after autoclaving the base under N2-CO2 (4:1, v/v), add "
    "JCM 439 Trace element, JCM 431 Selenite-tungstate, JCM 403 vitamin, "
    "thiamine, and vitamin B12 stocks plus bicarbonate, magnesium chloride, "
    "calcium chloride, sodium formate, sodium acetate, and sulfide stocks."
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
    for reference_url in (JCM_1399, JCM_439, JCM_431, JCM_403):
        if reference_url not in existing:
            references.append({"reference": reference_url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": JCM_1399,
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
    _put_after(
        repaired,
        "aeration",
        "N2-CO2 (4:1, v/v) gas atmosphere",
        "physical_state",
    )
    _put_after(
        repaired,
        "culture_vessel",
        "20 ml medium in 60 ml serum bottles with butyl rubber stoppers",
        "aeration",
    )
    _put_after(repaired, "incubation_atmosphere", "ANAEROBIC", "applications")
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
