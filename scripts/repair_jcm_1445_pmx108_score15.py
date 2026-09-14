#!/usr/bin/env python3
"""Repair JCM Medium 1445 PMX.108 Medium."""

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
TARGET = "bacterial/JCM_J1445_PMX_108_MEDIUM.yaml"
EXPECTED_ID = "CultureMech:015869"
EXPECTED_SOURCE_TERM = "jcm.grmd:1445"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_1445_pmx108_score15.py"
ACTION = "RESOLVED_JCM_1445_PMX108_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

JCM_1445 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1445"
JCM_852 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=852"
JCM_284 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=284"
SOURCE = "JCM Medium 1445"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NH4Cl", "0.54", "G_PER_L"),
    ("KH2PO4", "0.14", "G_PER_L"),
    ("MgCl2\u20226H2O", "0.2", "G_PER_L"),
    ("CaCl2\u20222H2O", "0.15", "G_PER_L"),
    ("Sodium aceate\u20223H2O", "1.36", "G_PER_L"),
    ("Yeast extract", "0.09", "G_PER_L"),
    ("Casamino acids (BD-Difico)", "0.5", "G_PER_L"),
    ("Tryptone (BD-Difico)", "1.5", "G_PER_L"),
    ("Trace mineral solution (see Medium No. 852 )", "1.0", "ML_PER_L"),
    ("Se/W solution (see below)", "1.0", "ML_PER_L"),
    ("Trace vitamins solution (see Medium No. 284 )", "2.0", "ML_PER_L"),
    ("Resazurin", "1.0", "MG_PER_L"),
    ("Distilled water", "970.0", "ML_PER_L"),
    ("8% NaHCO3 solution*", "30.0", "ML_PER_L"),
    ("5% L-Cysteine\u2022HCl\u2022H2O solution", "4.0", "ML_PER_L"),
    ("5% Na2S\u20229H2O solution", "4.0", "ML_PER_L"),
    ("Na2SeO3", "2.0", "MG_PER_L"),
    ("Na2WO4\u20222H2O", "1.0", "MG_PER_L"),
    ("Distilled water", "1.0", "ML_PER_L"),
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
        "NH4Cl",
        "0.54",
        "G_PER_L",
        notes="JCM Medium 1445 lists 0.54 g NH4Cl.",
        term=("CHEBI:31206", "ammonium chloride"),
    ),
    _component(
        "KH2PO4",
        "0.14",
        "G_PER_L",
        notes="JCM Medium 1445 lists 0.14 g KH2PO4.",
        term=("CHEBI:63036", "potassium dihydrogen phosphate"),
    ),
    _component(
        "MgCl2 x 6H2O",
        "0.2",
        "G_PER_L",
        notes="JCM Medium 1445 lists 0.2 g MgCl2 x 6H2O.",
    ),
    _component(
        "CaCl2 x 2H2O",
        "0.15",
        "G_PER_L",
        notes="JCM Medium 1445 lists 0.15 g CaCl2 x 2H2O.",
        term=("CHEBI:86158", "calcium chloride dihydrate"),
    ),
    _component(
        "Sodium acetate x 3H2O",
        "1.36",
        "G_PER_L",
        notes="JCM Medium 1445 lists 1.36 g sodium acetate trihydrate.",
        term=("CHEBI:32138", "sodium acetate trihydrate"),
    ),
    _component(
        "Yeast extract",
        "0.09",
        "G_PER_L",
        notes="JCM Medium 1445 lists 0.09 g yeast extract.",
    ),
    _component(
        "Casamino acids (BD-Difico)",
        "0.5",
        "G_PER_L",
        notes="JCM Medium 1445 lists 0.5 g Casamino acids.",
    ),
    _component(
        "Tryptone (BD-Difico)",
        "1.5",
        "G_PER_L",
        notes="JCM Medium 1445 lists 1.5 g tryptone.",
    ),
    _component(
        "Resazurin",
        "1.0",
        "MG_PER_L",
        notes="JCM Medium 1445 lists 1.0 mg resazurin.",
        term=("CHEBI:8806", "Resazurin"),
    ),
    _component(
        "Distilled water",
        "970.0",
        "ML_PER_L",
        notes="JCM Medium 1445 lists 970.0 ml distilled water in the base.",
        term=("CHEBI:15377", "water"),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution(
        "Trace mineral solution (JCM Medium 852)",
        "1.0",
        notes="JCM Medium 1445 adds 1.0 ml/L Trace mineral solution from JCM 852.",
        source=f"{SOURCE} / JCM Medium 852",
    ),
    _solution(
        "Se/W solution",
        "1.0",
        notes="JCM Medium 1445 adds 1.0 ml/L of the Se/W solution listed below it.",
        composition=[
            _component(
                "Na2SeO3",
                "2.0",
                "MG_PER_L",
                notes="JCM Medium 1445 Se/W stock lists 2.0 mg Na2SeO3 per liter.",
                term=("CHEBI:48843", "disodium selenite"),
            ),
            _component(
                "Na2WO4 x 2H2O",
                "1.0",
                "MG_PER_L",
                notes="JCM Medium 1445 Se/W stock lists 1.0 mg Na2WO4 x 2H2O per liter.",
                term=("CHEBI:63939", "sodium tungstate dihydrate"),
            ),
        ],
    ),
    _solution(
        "Trace vitamins solution (JCM Medium 284)",
        "2.0",
        notes="JCM Medium 1445 adds 2.0 ml/L Trace vitamins solution from JCM 284.",
        source=f"{SOURCE} / JCM Medium 284",
    ),
    _solution(
        "8% NaHCO3 solution",
        "30.0",
        notes="JCM Medium 1445 adds 30.0 ml/L filter-sterilized 8% NaHCO3 solution.",
        composition=[
            _component(
                "NaHCO3",
                "80.0",
                "G_PER_L",
                notes="Solute of the 8% NaHCO3 stock added by JCM Medium 1445.",
                term=("CHEBI:32139", "sodium hydrogencarbonate"),
            )
        ],
    ),
    _solution(
        "5% L-Cysteine HCl H2O solution",
        "4.0",
        notes=("JCM Medium 1445 adds 4.0 ml/L autoclaved " "5% L-Cysteine HCl H2O solution."),
        composition=[
            _component(
                "L-Cysteine HCl H2O",
                "50.0",
                "G_PER_L",
                notes=("Solute of the 5% L-Cysteine HCl H2O stock added by " "JCM Medium 1445."),
                term=("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
            )
        ],
    ),
    _solution(
        "5% Na2S x 9H2O solution",
        "4.0",
        notes="JCM Medium 1445 adds 4.0 ml/L autoclaved 5% Na2S x 9H2O solution.",
        composition=[
            _component(
                "Na2S x 9H2O",
                "50.0",
                "G_PER_L",
                notes="Solute of the 5% Na2S x 9H2O stock added by JCM Medium 1445.",
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
            "Mix NH4Cl, KH2PO4, MgCl2 x 6H2O, CaCl2 x 2H2O, sodium acetate "
            "trihydrate, yeast extract, Casamino acids, tryptone, Trace "
            "mineral solution, Se/W solution, Trace vitamins solution, "
            "resazurin, and distilled water."
        ),
    ),
    _step(
        2,
        "HEAT",
        "Bring the mixed base to a boil and cool it under N2-CO2 (4:1, v/v) gas.",
    ),
    _step(
        3,
        "ALIQUOT",
        (
            "Distribute the medium under the same gas mixture, for example "
            "20 ml medium into 60 ml serum bottles, seal with butyl rubber "
            "stoppers, inject 10-20% gas-phase volume of H2, and autoclave."
        ),
    ),
    _step(
        4,
        "MIX",
        (
            "After cooling, aseptically and anaerobically add 8% NaHCO3, "
            "5% L-Cysteine HCl H2O, and 5% Na2S x 9H2O solutions at the "
            "JCM Medium 1445 per-liter ratios."
        ),
    ),
)

NOTES = (
    "JCM Medium 1445 base salts, organic supplements, resazurin, and distilled "
    "water are direct components; before autoclaving, the base also receives "
    "JCM 852 Trace mineral solution, the local Se/W solution, and JCM 284 Trace "
    "vitamins solution under N2-CO2 (4:1, v/v). After autoclaving, add the "
    "bicarbonate, cysteine, and sulfide stocks."
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
    for reference_url in (JCM_1445, JCM_852, JCM_284):
        if reference_url not in existing:
            references.append({"reference": reference_url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": JCM_1445,
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
        "N2-CO2 (4:1, v/v) gas atmosphere with H2 injected after sealing",
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
