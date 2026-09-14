#!/usr/bin/env python3
"""Repair TOGO M984 IRD Marine Clostridia Medium-2."""

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
TARGET = Path("bacterial/ird_marine_clostridia_medium_2.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m984_ird_marine_clostridia_score15.py"
ACTION = "RESOLVED_TOGO_M984_IRD_MARINE_CLOSTRIDIA_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:010411"
EXPECTED_MEDIA_TERM = "TOGO:M984"
TOGO_M984 = "https://togomedium.org/medium/M984"
TOGO_M953 = "https://togomedium.org/medium/M953"
TOGO_M142 = "https://togomedium.org/medium/M142"
JCM_938 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=938"
JCM_909 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=909"
JCM_151 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151"

M984_SOURCE = "TOGO M984 / JCM Medium 938"
M953_SOURCE = "TOGO M953 / JCM Medium 909"
TRACE_SOURCE = "JCM Medium 151 trace minerals"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("sodium acetate", "0.164", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "2", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("IRD MARINE CLOSTRIDA MEDIUM (see Medium [M953])", "1", "G_PER_L", ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("sodium acetate", "0.164", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "2.0", "G_PER_L"),
    ("Distilled water", "940.0", "ML_PER_L"),
    ("KH2PO4", "0.3", "G_PER_L"),
    ("K2HPO4", "0.3", "G_PER_L"),
    ("NH4Cl", "1.0", "G_PER_L"),
    ("NaCl", "23.0", "G_PER_L"),
    ("KCl", "0.1", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.1", "G_PER_L"),
    ("Yeast extract", "0.5", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "0.5", "G_PER_L"),
    ("Resazurin", "1.0", "MG_PER_L"),
)

TRACE_MINERALS_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Nitrilotriacetic acid", "1.5", "G_PER_L"),
    ("MgSO4 x 7 H2O", "3.0", "G_PER_L"),
    ("MnSO4 x n H2O", "0.5", "G_PER_L"),
    ("NaCl", "1.0", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CoSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.1", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.01", "G_PER_L"),
    ("AlK(SO4)2", "0.01", "G_PER_L"),
    ("H3BO3", "0.01", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("Trace minerals", "10.0", "ML_PER_L", TRACE_MINERALS_SIGNATURE),
    ("8% NaHCO3 solution", "25.0", "ML_PER_L", (("NaHCO3", "8.0", "PERCENT_W_V"),)),
    (
        "10% MgCl2 x 6 H2O solution",
        "30.0",
        "ML_PER_L",
        (("MgCl2 x 6 H2O", "10.0", "PERCENT_W_V"),),
    ),
    ("1 M Glucose solution", "5.0", "ML_PER_L", (("Glucose", "1.0", "MOLAR"),)),
    ("5% Na2S x 9 H2O solution", "8.0", "ML_PER_L", (("Na2S x 9 H2O", "5.0", "PERCENT_W_V"),)),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "AlK(SO4)2": ("CHEBI:86463", "potassium aluminium sulfate"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoSO4 x 7 H2O": ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "L-Cysteine HCl x H2O": (
        "CHEBI:91248",
        "L-cysteine hydrochloride hydrate",
    ),
    "MgCl2 x 6 H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnSO4 x n H2O": ("CHEBI:86360", "manganese(II) sulfate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S x 9 H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
    "sodium acetate": ("CHEBI:32954", "sodium acetate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
    "PERCENT_W_V": "% w/v",
}

NOTES = (
    "TOGO M984 imports JCM Medium 938 IRD Marine Clostridia Medium-2, which "
    "uses JCM Medium 909 IRD Marine Clostrida Medium supplemented with 0.164 "
    "g/L sodium acetate and 2.0 g/L Trypticase peptone (BD-BBL). Expanded the "
    "JCM 909 base and its JCM Medium 151 trace-minerals stock."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare JCM Medium 151 Trace minerals by dissolving nitrilotriacetic "
            "acid, adjusting pH to 6.5 with KOH solution, adding minerals, and "
            "adjusting the final stock to pH 7.0."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": (
            "Mix JCM 909 base components and autoclave under an N2-CO2 (4:1, v/v) " "gas mixture."
        ),
    },
    {
        "step_number": 3,
        "action": "FILTER_STERILIZE",
        "description": "Filter-sterilize the 8% NaHCO3 stock before use.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "After cooling, add anaerobic 8% NaHCO3, 10% MgCl2 x 6 H2O, and " "1 M glucose stocks."
        ),
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Aseptically distribute the medium under an N2-CO2 (4:1, v/v) stream; "
            "before inoculation add anaerobic 5% Na2S x 9 H2O stock autoclaved "
            "under N2."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}


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
    *,
    source: str,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _stock(
    preferred_term: str,
    volume: str,
    solute: str,
    value: str,
    unit: str,
    *,
    source: str = M953_SOURCE,
    notes: str,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": volume, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": [
            _component(
                solute,
                value,
                unit,
                source=source,
                notes=(
                    f"{source} uses {preferred_term} containing "
                    f"{value} {UNIT_LABELS[unit]} {solute}."
                ),
            )
        ],
        "name": preferred_term,
    }
    if preparation_notes is not None:
        row["preparation_notes"] = preparation_notes
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component("sodium acetate", "0.164", "G_PER_L", source=M984_SOURCE),
    _component("Trypticase peptone (BD-BBL)", "2.0", "G_PER_L", source=M984_SOURCE),
    _component("Distilled water", "940.0", "ML_PER_L", source=M953_SOURCE),
    _component("KH2PO4", "0.3", "G_PER_L", source=M953_SOURCE),
    _component("K2HPO4", "0.3", "G_PER_L", source=M953_SOURCE),
    _component("NH4Cl", "1.0", "G_PER_L", source=M953_SOURCE),
    _component("NaCl", "23.0", "G_PER_L", source=M953_SOURCE),
    _component("KCl", "0.1", "G_PER_L", source=M953_SOURCE),
    _component("CaCl2 x 2 H2O", "0.1", "G_PER_L", source=M953_SOURCE),
    _component("Yeast extract", "0.5", "G_PER_L", source=M953_SOURCE),
    _component("L-Cysteine HCl x H2O", "0.5", "G_PER_L", source=M953_SOURCE),
    _component("Resazurin", "1.0", "MG_PER_L", source=M953_SOURCE),
)

TRACE_MINERALS = {
    "preferred_term": "Trace minerals",
    "concentration": {"value": "10.0", "unit": "ML_PER_L"},
    "source": M953_SOURCE,
    "notes": "JCM Medium 909 adds 10.0 ml/L JCM Medium 151 Trace minerals.",
    "composition": [
        _component("Distilled water", "1000.0", "ML_PER_L", source=TRACE_SOURCE),
        _component("Nitrilotriacetic acid", "1.5", "G_PER_L", source=TRACE_SOURCE),
        _component("MgSO4 x 7 H2O", "3.0", "G_PER_L", source=TRACE_SOURCE),
        _component("MnSO4 x n H2O", "0.5", "G_PER_L", source=TRACE_SOURCE),
        _component("NaCl", "1.0", "G_PER_L", source=TRACE_SOURCE),
        _component("FeSO4 x 7 H2O", "0.1", "G_PER_L", source=TRACE_SOURCE),
        _component("CoSO4 x 7 H2O", "0.1", "G_PER_L", source=TRACE_SOURCE),
        _component("CaCl2 x 2 H2O", "0.1", "G_PER_L", source=TRACE_SOURCE),
        _component("ZnSO4 x 7 H2O", "0.1", "G_PER_L", source=TRACE_SOURCE),
        _component("CuSO4 x 5 H2O", "0.01", "G_PER_L", source=TRACE_SOURCE),
        _component("AlK(SO4)2", "0.01", "G_PER_L", source=TRACE_SOURCE),
        _component("H3BO3", "0.01", "G_PER_L", source=TRACE_SOURCE),
        _component("Na2MoO4 x 2 H2O", "0.01", "G_PER_L", source=TRACE_SOURCE),
    ],
    "name": "Trace minerals",
    "preparation_notes": (
        "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. "
        "Then proceed to add minerals. Adjust final pH to 7.0."
    ),
}

SOLUTIONS: tuple[dict[str, Any], ...] = (
    TRACE_MINERALS,
    _stock(
        "8% NaHCO3 solution",
        "25.0",
        "NaHCO3",
        "8.0",
        "PERCENT_W_V",
        notes="JCM Medium 909 adds 25.0 ml/L filter-sterilized 8% NaHCO3 solution.",
        preparation_notes="Filter-sterilize before anaerobic post-autoclave addition.",
    ),
    _stock(
        "10% MgCl2 x 6 H2O solution",
        "30.0",
        "MgCl2 x 6 H2O",
        "10.0",
        "PERCENT_W_V",
        notes="JCM Medium 909 adds 30.0 ml/L 10% MgCl2 x 6 H2O solution.",
    ),
    _stock(
        "1 M Glucose solution",
        "5.0",
        "Glucose",
        "1.0",
        "MOLAR",
        notes="JCM Medium 909 adds 5.0 ml/L 1 M glucose solution.",
    ),
    _stock(
        "5% Na2S x 9 H2O solution",
        "8.0",
        "Na2S x 9 H2O",
        "5.0",
        "PERCENT_W_V",
        notes="JCM Medium 909 adds 8.0 ml/L anaerobic 5% Na2S x 9 H2O solution.",
        preparation_notes="Autoclave and store under an N2 atmosphere.",
    ),
)


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


def _solution_signature(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError(f"{label} is not a list")

    signature: list[SolutionSignature] = []
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
                _signature(row.get("composition"), f"{label} composition"),
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signature = _solution_signature(doc.get("solutions"), "solutions")
    if solution_signature not in (
        IMPORTED_SOLUTION_SIGNATURE,
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


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

    for obsolete in (
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
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
    for reference in (TOGO_M984, JCM_938, TOGO_M953, JCM_909, TOGO_M142, JCM_151):
        if reference not in existing:
            references.append({"reference": reference})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": f"{TOGO_M984}; {JCM_938}; {TOGO_M953}; {JCM_909}; {TOGO_M142}; {JCM_151}",
        "notes": (
            f"{NOTES} Replaced the empty M953 cross-reference solution with "
            "JCM 909 ingredients, nested all quantified stock solutions, "
            "and grounded all disclosed chemical components except the "
            "undefined Trypticase peptone."
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
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "notes")
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
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
