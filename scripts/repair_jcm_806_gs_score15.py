#!/usr/bin/env python3
"""Repair JCM Medium 806 GS Medium."""

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
TARGET = "bacterial/JCM_J806_GS_MEDIUM.yaml"
EXPECTED_ID = "CultureMech:003151"
EXPECTED_SOURCE_TERM = "mediadive.medium:J806"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_806_gs_score15.py"
ACTION = "RESOLVED_JCM_806_GS_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

JCM_806 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=806"
JCM_262 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=262"
JCM_265 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=265"
JCM_151 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"
SOURCE = "JCM Medium 806 / 262 / 265"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "980", "ML_PER_L"),
    ("MgSO4\u30fb7H2O", "3.45", "G_PER_L"),
    ("NaCl", "6", "G_PER_L"),
    ("CaCl2\u30fb2H2O", "0.14", "G_PER_L"),
    ("KH2PO4", "0.14", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("Resazurin", "1", "MG_PER_L"),
    ("MgCl2\u30fb6H2O", "4", "G_PER_L"),
    ("KCl", "0.355", "G_PER_L"),
    ("NaHCO3", "5", "G_PER_L"),
    ("Fe(NH4)2(SO4)2\u30fb6H2O", "2", "MG_PER_L"),
    ("glucose", "1", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "2", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "2", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
    ("Hydrogen gas", "variable", "VARIABLE"),
)
IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Wolfe's mineral solution (see Medium [M257])", "10", "ML_PER_L"),
    ("Trace vitamins (see Medium [M190])", "10", "ML_PER_L"),
    ("5% Na2S\u30fb9H2O solution", "10", "ML_PER_L"),
    ("5% L-Cysteine\u30fbHCl\u30fbH2O solution", "10", "ML_PER_L"),
)


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
        "KCl",
        "0.355",
        "G_PER_L",
        notes="JCM Medium 265 lists 0.355 g KCl.",
        term=("CHEBI:32588", "potassium chloride"),
    ),
    _component(
        "MgCl2 x 6H2O",
        "4.0",
        "G_PER_L",
        notes="JCM Medium 265 lists 4.0 g MgCl2 x 6H2O.",
        term=("CHEBI:86345", "magnesium dichloride hexahydrate"),
    ),
    _component(
        "MgSO4 x 7H2O",
        "3.45",
        "G_PER_L",
        notes="JCM Medium 265 lists 3.45 g MgSO4 x 7H2O.",
        term=("CHEBI:31795", "magnesium sulfate heptahydrate"),
    ),
    _component(
        "NH4Cl",
        "0.25",
        "G_PER_L",
        notes="JCM Medium 265 lists 0.25 g NH4Cl.",
        term=("CHEBI:31206", "ammonium chloride"),
    ),
    _component(
        "CaCl2 x 2H2O",
        "0.14",
        "G_PER_L",
        notes="JCM Medium 265 lists 0.14 g CaCl2 x 2H2O.",
        term=("CHEBI:86158", "calcium chloride dihydrate"),
    ),
    _component(
        "KH2PO4",
        "0.14",
        "G_PER_L",
        notes="JCM Medium 265 lists 0.14 g KH2PO4.",
        term=("CHEBI:63036", "potassium dihydrogen phosphate"),
    ),
    _component(
        "NaCl",
        "6.0",
        "G_PER_L",
        notes="JCM Medium 262 uses JCM 265 with 6.0 g/L final NaCl.",
        term=("CHEBI:26710", "sodium chloride"),
    ),
    _component(
        "Fe(NH4)2(SO4)2 x 6H2O",
        "2.0",
        "MG_PER_L",
        notes="JCM Medium 265 lists 2.0 mg Fe(NH4)2(SO4)2 x 6H2O.",
        term=("CHEBI:76181", "ferrous ammonium sulfate hexahydrate"),
    ),
    _component(
        "NaHCO3",
        "5.0",
        "G_PER_L",
        notes="JCM Medium 265 lists 5.0 g NaHCO3.",
        term=("CHEBI:32139", "sodium hydrogencarbonate"),
    ),
    _component(
        "Glucose",
        "1.8",
        "G_PER_L",
        notes="JCM Medium 806 replaces JCM 265 sodium acetate with 1.8 g/L glucose.",
        term=("CHEBI:17234", "glucose"),
    ),
    _component(
        "Yeast extract (BD-Difco)",
        "2.0",
        "G_PER_L",
        notes="JCM Medium 265 lists 2.0 g yeast extract.",
    ),
    _component(
        "Trypticase peptone (BD-BBL)",
        "2.0",
        "G_PER_L",
        notes="JCM Medium 265 lists 2.0 g Trypticase peptone.",
    ),
    _component(
        "Resazurin",
        "1.0",
        "MG_PER_L",
        notes="JCM Medium 265 lists 1.0 mg resazurin.",
        term=("CHEBI:8806", "Resazurin"),
    ),
    _component(
        "Distilled water",
        "980.0",
        "ML_PER_L",
        notes="JCM Medium 265 lists 980.0 ml distilled water.",
        term=("CHEBI:15377", "water"),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution(
        "Wolfe's mineral solution",
        "10.0",
        notes="JCM Medium 265 adds 10.0 ml/L of its Wolfe's mineral solution.",
        composition=[
            _component(
                "Trace minerals (JCM Medium 151)",
                "1000.0",
                "ML_PER_L",
                notes="JCM Medium 265 Wolfe's mineral solution uses 1.0 L trace minerals.",
                source=f"{SOURCE} / JCM Medium 151",
            ),
            _component(
                "NiCl2 x 6H2O",
                "0.02",
                "G_PER_L",
                notes="JCM Medium 265 Wolfe's mineral solution lists 0.02 g NiCl2 x 6H2O.",
            ),
            _component(
                "Na2SeO3",
                "0.001",
                "G_PER_L",
                notes="JCM Medium 265 Wolfe's mineral solution lists 0.001 g Na2SeO3.",
                term=("CHEBI:48843", "disodium selenite"),
            ),
            _component(
                "Na2WO4 x 2H2O",
                "0.01",
                "G_PER_L",
                notes=(
                    "JCM Medium 265 Wolfe's mineral solution lists 0.01 g "
                    "Na2WO4 x 2H2O."
                ),
                term=("CHEBI:63939", "sodium tungstate dihydrate"),
            ),
        ],
    ),
    _solution(
        "Trace vitamins (JCM Medium 197)",
        "10.0",
        notes="JCM Medium 265 adds 10.0 ml/L Trace vitamins from JCM 197.",
        source=f"{SOURCE} / JCM Medium 197",
    ),
    _solution(
        "5% L-Cysteine HCl H2O solution",
        "10.0",
        notes=(
            "JCM Medium 265 adds 10.0 ml/L autoclaved "
            "5% L-Cysteine HCl H2O solution."
        ),
        composition=[
            _component(
                "L-Cysteine HCl H2O",
                "50.0",
                "G_PER_L",
                notes=(
                    "Solute of the 5% L-Cysteine HCl H2O stock added by "
                    "JCM Medium 265."
                ),
                term=("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
            )
        ],
    ),
    _solution(
        "5% Na2S x 9H2O solution",
        "10.0",
        notes="JCM Medium 265 adds 10.0 ml/L autoclaved 5% Na2S x 9H2O solution.",
        composition=[
            _component(
                "Na2S x 9H2O",
                "50.0",
                "G_PER_L",
                notes="Solute of the 5% Na2S x 9H2O stock added by JCM Medium 265.",
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
            "Mix JCM Medium 265 base components except NaHCO3, with 6.0 g/L "
            "final NaCl from JCM Medium 262 and 1.8 g/L glucose replacing "
            "sodium acetate for JCM Medium 806."
        ),
    ),
    _step(2, "ADJUST_PH", "Adjust to pH 6.5 before adding NaHCO3."),
    _step(
        3,
        "HEAT",
        (
            "Bring the medium to a boil for 5-10 sec, cool under "
            "H2-CO2 (80:20, v/v), and add NaHCO3."
        ),
    ),
    _step(
        4,
        "AUTOCLAVE",
        (
            "Dispense the medium into Hungate tubes under H2-CO2 (80:20, v/v), "
            "seal with butyl rubber stoppers, autoclave, and stand overnight."
        ),
    ),
    _step(
        5,
        "MIX",
        (
            "Aseptically and anaerobically add 5% L-Cysteine HCl H2O and "
            "5% Na2S x 9H2O solutions stored under N2 at the JCM Medium 265 "
            "per-liter ratios."
        ),
    ),
    _step(
        6,
        "MIX",
        "Cultivate JCM Medium 806 under an N2-CO2 (80:20, v/v) gas mixture.",
    ),
)

NOTES = (
    "JCM Medium 806 wraps JCM Medium 262, which wraps JCM Medium 265. This record "
    "uses the JCM 265 base with 6.0 g/L final NaCl from JCM 262, replaces sodium "
    "acetate with 1.8 g/L glucose for JCM 806, moves gas-phase H2, CO2, and N2 "
    "out of the ingredient list, and restores Wolfe's mineral, JCM 197 Trace "
    "vitamins, cysteine, and sulfide as stock solutions."
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
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} / {IMPORTED_SOLUTION_SIGNATURE!r} to "
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
    for reference_url in (JCM_806, JCM_262, JCM_265, JCM_151, JCM_197):
        if reference_url not in existing:
            references.append({"reference": reference_url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": JCM_806,
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
        "H2-CO2 (80:20, v/v) during preparation; N2-CO2 (80:20, v/v) for cultivation",
        "physical_state",
    )
    _put_after(
        repaired,
        "culture_vessel",
        "5 ml medium in Hungate tubes with butyl rubber stoppers",
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
