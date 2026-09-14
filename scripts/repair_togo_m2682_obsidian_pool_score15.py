#!/usr/bin/env python3
"""Repair TOGO M2682 Obsidian Pool fermentor medium."""

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
TARGET = Path("bacterial/obsidian_pool_fermentor_opf_medium_modified_from_m_b_allen_1959.yaml")
EXPECTED_ID = "CultureMech:009237"
EXPECTED_MEDIA_TERM = "TOGO:M2682"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2682_obsidian_pool_score15.py"
ACTION = "RESOLVED_TOGO_M2682_OBSIDIAN_POOL_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2682 = "https://togomedium.org/medium/M2682"
ELKINS_2008 = "https://doi.org/10.1073/pnas.0801980105"
REFERENCES = (TOGO_M2682, ELKINS_2008)

SOURCE = "TOGO M2682 / Elkins et al. 2008"
TITLE = "Obsidian Pool fermentor (OPF) medium (modified from M. B. Allen, 1959)"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Na2MoO4 x2H2O (1 mg/ml)", "30", "G_PER_L"),
    ("MnCl2 x4H2O (10 mg/ml)", "180", "G_PER_L"),
    ("ZnSO4 x7H2O (10 mg/ml)", "22", "G_PER_L"),
    ("CuCl2 x2H2O (10 mg/ml)", "5", "G_PER_L"),
    ("CoSO4 x7H2O (1 mg/ml)", "10", "G_PER_L"),
    ("Na2B4O7 x 10 H2O (25 mg/ml)", "180", "G_PER_L"),
    ("VOSO4 x5H2O (1 mg/ml)", "30", "G_PER_L"),
    ("Distilled H2O", "1000", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.25", "G_PER_L"),
    ("Yeast Extract", "0.1", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.07", "G_PER_L"),
    ("KH2PO4", "0.28", "G_PER_L"),
    ("Na2Sx6H2O", "0.13", "G_PER_L"),
    ("(NH4)2SO4", "1.3", "G_PER_L"),
    ("FeCl3 x 6 H2O", "0.02", "G_PER_L"),
    ("Na2SO4", "0.07", "G_PER_L"),
    ("KNO3", "0.1", "G_PER_L"),
    ("CaSO4 x 2 H2O", "0.17", "G_PER_L"),
    ("Na2S2O3", "0.78", "G_PER_L"),
    ("Peptone", "0.5", "G_PER_L"),
    ("LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) (1 mg/ml each)", "10", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Distilled water", "1", "G_PER_L"),
    ("Na2WO4", "1", "G_PER_L"),
    ("NaSeO3", "1", "G_PER_L"),
    ("LiCl", "1", "G_PER_L"),
    ("Ni(NH4)2(SO4)", "1", "G_PER_L"),
)
IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Wolfe's Vitamin Solution (1,000X_x0008_)", "1", "G_PER_L", ()),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CaSO4 x 2 H2O": ("CHEBI:32583", "calcium sulfate dihydrate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "CoSO4 x 7 H2O": ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl3 x 6 H2O": ("CHEBI:86254", "iron trichloride hexahydrate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "KNO3": ("CHEBI:63043", "potassium nitrate"),
    "LiCl": ("CHEBI:48607", "lithium chloride"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "Na2B4O7 x 10 H2O": ("CHEBI:131366", "disodium tetraborate decahydrate"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S x 9 H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Na2S2O3": ("CHEBI:132112", "sodium thiosulfate"),
    "Na2SeO3": ("CHEBI:48843", "disodium selenite"),
    "Na2SO4": ("CHEBI:32149", "sodium sulfate"),
    "Na2WO4": ("CHEBI:63940", "sodium tungstate"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "Peptone": ("MICRO:0000178", "Peptone"),
    "VOSO4 x 5 H2O": ("CHEBI:132758", "vanadyl sulfate pentahydrate"),
    "Yeast Extract": ("FOODON:03315426", "Yeast extract"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

NOTES = (
    "TOGO M2682 imports the Obsidian Pool fermentor medium from Elkins et al. "
    "2008. The source lists 1000 ml distilled water, modified Allen salts and "
    "organics, 1 ml Wolfe's Vitamin Solution (1000X), 10 uL/L "
    "LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) stock, and N2/CO2 (80:20) gas bubbling "
    "at 85 C."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    notes: str,
    *,
    ground: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    if ground:
        term = _term(*GROUNDINGS[preferred_term])
        row["term"] = term
        if term["id"].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    return row


def _main_note(preferred_term: str, amount: str) -> str:
    return f"TOGO M2682 lists {amount} {preferred_term} in the final liter."


def _ul_stock_note(
    preferred_term: str,
    volume: str,
    stock_concentration: str,
    final_amount: str,
) -> str:
    return (
        f"TOGO M2682 adds {volume} uL of {stock_concentration} {preferred_term} "
        f"per liter, equivalent to {final_amount}."
    )


MAIN_INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Na2MoO4 x 2 H2O",
        "0.03",
        "MG_PER_L",
        _ul_stock_note("Na2MoO4 x 2 H2O", "30", "1 mg/ml", "0.03 mg/L"),
    ),
    _component(
        "MnCl2 x 4 H2O",
        "1.8",
        "MG_PER_L",
        _ul_stock_note("MnCl2 x 4 H2O", "180", "10 mg/ml", "1.8 mg/L"),
    ),
    _component(
        "ZnSO4 x 7 H2O",
        "0.22",
        "MG_PER_L",
        _ul_stock_note("ZnSO4 x 7 H2O", "22", "10 mg/ml", "0.22 mg/L"),
    ),
    _component(
        "CuCl2 x 2 H2O",
        "0.05",
        "MG_PER_L",
        _ul_stock_note("CuCl2 x 2 H2O", "5", "10 mg/ml", "0.05 mg/L"),
    ),
    _component(
        "CoSO4 x 7 H2O",
        "0.01",
        "MG_PER_L",
        _ul_stock_note("CoSO4 x 7 H2O", "10", "1 mg/ml", "0.01 mg/L"),
    ),
    _component(
        "Na2B4O7 x 10 H2O",
        "4.5",
        "MG_PER_L",
        _ul_stock_note("Na2B4O7 x 10 H2O", "180", "25 mg/ml", "4.5 mg/L"),
    ),
    _component(
        "VOSO4 x 5 H2O",
        "0.03",
        "MG_PER_L",
        _ul_stock_note("VOSO4 x 5 H2O", "30", "1 mg/ml", "0.03 mg/L"),
    ),
    _component(
        "Distilled water",
        "1000.0",
        "ML_PER_L",
        "TOGO M2682 makes the final medium with 1000 ml distilled water.",
    ),
    _component("MgSO4 x 7 H2O", "0.25", "G_PER_L", _main_note("MgSO4 x 7 H2O", "0.25 g")),
    _component("Yeast Extract", "0.1", "G_PER_L", _main_note("Yeast Extract", "0.1 g")),
    _component("CaCl2 x 2 H2O", "0.07", "G_PER_L", _main_note("CaCl2 x 2 H2O", "0.07 g")),
    _component("KH2PO4", "0.28", "G_PER_L", _main_note("KH2PO4", "0.28 g")),
    _component("Na2S x 9 H2O", "0.13", "G_PER_L", _main_note("Na2S x 9 H2O", "0.13 g")),
    _component("(NH4)2SO4", "1.3", "G_PER_L", _main_note("(NH4)2SO4", "1.3 g")),
    _component("FeCl3 x 6 H2O", "0.02", "G_PER_L", _main_note("FeCl3 x 6 H2O", "0.02 g")),
    _component("Na2SO4", "0.07", "G_PER_L", _main_note("Na2SO4", "0.07 g")),
    _component("KNO3", "0.1", "G_PER_L", _main_note("KNO3", "0.1 g")),
    _component("CaSO4 x 2 H2O", "0.17", "G_PER_L", _main_note("CaSO4 x 2 H2O", "0.17 g")),
    _component("Na2S2O3", "0.78", "G_PER_L", _main_note("Na2S2O3", "0.78 g")),
    _component("Peptone", "0.5", "G_PER_L", _main_note("Peptone", "0.5 g")),
    _component(
        "Carbon dioxide gas",
        "variable",
        "VARIABLE",
        "TOGO M2682 lists CO2 gas; source comments specify N2/CO2 (80:20) bubbling.",
    ),
    _component(
        "Nitrogen gas",
        "variable",
        "VARIABLE",
        "TOGO M2682 lists N2 gas; source comments specify N2/CO2 (80:20) bubbling.",
    ),
)

MIXED_STOCK_COMPONENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Na2WO4",
        "1.0",
        "G_PER_L",
        "TOGO M2682 defines the Li/W/Se/Ni stock with 1 mg/ml Na2WO4.",
    ),
    _component(
        "Na2SeO3",
        "1.0",
        "G_PER_L",
        "TOGO M2682 defines the Li/W/Se/Ni stock with 1 mg/ml Na2SeO3.",
    ),
    _component(
        "LiCl",
        "1.0",
        "G_PER_L",
        "TOGO M2682 defines the Li/W/Se/Ni stock with 1 mg/ml LiCl.",
    ),
    _component(
        "Ni(NH4)2(SO4)",
        "1.0",
        "G_PER_L",
        (
            "TOGO M2682 defines the Li/W/Se/Ni stock with 1 mg/ml "
            "Ni(NH4)2(SO4). This source formula is retained ungrounded because "
            "it does not specify nickel sulfate stoichiometry or hydrate state."
        ),
        ground=False,
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Wolfe's Vitamin Solution (1000X)",
        "concentration": {"value": "1.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "TOGO M2682 adds 1.0 ml/L Wolfe's Vitamin Solution (1000X); "
            "this source does not disclose its composition."
        ),
        "composition": [],
    },
    {
        "preferred_term": "LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) stock",
        "concentration": {"value": "0.01", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "TOGO M2682 adds 10 uL/L of a stock containing 1 mg/ml each "
            "LiCl, Na2WO4, NaSeO3, and Ni(NH4)2(SO4)."
        ),
        "composition": copy.deepcopy(list(MIXED_STOCK_COMPONENTS)),
    },
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in MAIN_INGREDIENTS
)
FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (
        "Wolfe's Vitamin Solution (1000X)",
        "1.0",
        "ML_PER_L",
        (),
    ),
    (
        "LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) stock",
        "0.01",
        "ML_PER_L",
        tuple(
            (
                str(row["preferred_term"]),
                str(row["concentration"]["value"]),
                str(row["concentration"]["unit"]),
            )
            for row in MIXED_STOCK_COMPONENTS
        ),
    ),
)
LEGACY_FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    FINAL_SOLUTION_SIGNATURES[0],
    (
        "LiCl/Na2WO4/NaSeO3/Ni(NH4)2(SO4) stock",
        "0.01",
        "ML_PER_L",
        (
            ("Distilled water", "1000.0", "ML_PER_L"),
            *FINAL_SOLUTION_SIGNATURES[1][3],
        ),
    ),
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


def _solution_signatures(rows: Any) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in rows:
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
                _ingredient_signature(solution.get("composition")),
            )
        )
    return tuple(signatures)


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    signature = (
        _ingredient_signature(doc.get("ingredients")),
        _solution_signatures(doc.get("solutions")),
    )
    if signature not in {
        (IMPORTED_INGREDIENT_SIGNATURE, IMPORTED_SOLUTION_SIGNATURES),
        (FINAL_INGREDIENT_SIGNATURE, FINAL_SOLUTION_SIGNATURES),
        (FINAL_INGREDIENT_SIGNATURE, LEGACY_FINAL_SOLUTION_SIGNATURES),
    }:
        raise ValueError(f"{TARGET}: ingredient/solution signature drifted")


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
        while obsolete in flags:
            flags.remove(obsolete)
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
            "Corrected microliter stock additions from g/L to mg/L final "
            "concentrations, moved the LiCl/Na2WO4/NaSeO3/Ni stock solutes "
            "under an inline stock solution, fixed Na2S2O3 and hydrated salt "
            "groundings, and added the 85 C N2/CO2 incubation conditions."
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
    _put_after(repaired, "temperature_value", 85.0, "physical_state")
    _put_after(repaired, "aeration", "N2/CO2 (80:20) bubbled at 20 ml/min", "temperature_value")
    repaired["ingredients"] = copy.deepcopy(list(MAIN_INGREDIENTS))
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(repaired, "incubation_atmosphere", "ANAEROBIC", "applications")
    repaired.pop("high_metal", None)
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
