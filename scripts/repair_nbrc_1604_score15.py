#!/usr/bin/env python3
"""Repair the score-15 NBRC Medium 1604 TOGO import."""

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
TARGET = Path("bacterial/togo_medium_m3052.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009566"
EXPECTED_MEDIA_TERM = "TOGO:M3052"

CURATOR = "repair_nbrc_1604_score15.py"
ACTION = "RESOLVED_NBRC_1604_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M3052_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3052"
NBRC_1604 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1604"
SOURCE = "TOGO M3052 / NBRC Medium 1604"

CASITONE = "Casitone"
YEAST_EXTRACT = "Yeast extract"
SODIUM_CARBONATE = "NaCO3"
DIPOTASSIUM_PHOSPHATE = "K2HPO4"
POTASSIUM_PHOSPHATE = "KH2PO4"
SODIUM_CHLORIDE = "NaCl"
MAGNESIUM_SULFATE = "MgSO4 7H2O"
CALCIUM_CHLORIDE = "CaCl2"
CYSTEINE = "Cysteine"
HAEMIN = "Haemin"
AGAR = "Agar"
DISTILLED_WATER = "Distilled water"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Stock:
    legacy_name: str
    final_name: str
    addition_value: str
    component_name: str
    component_value: str

    @property
    def legacy_signature(self) -> Component:
        return (self.legacy_name, "variable", "VARIABLE")

    @property
    def final_signature(self) -> SolutionSignature:
        return (
            self.final_name,
            self.addition_value,
            "ML_PER_L",
            ((self.component_name, self.component_value, "MG_PER_ML"),),
        )


RESAZURIN_STOCK = Stock(
    "Resazurin (1 mg/L)",
    "Resazurin (1 mg/L)",
    "0.1",
    "Resazurin",
    "0.001",
)
BIOTIN_STOCK = Stock(
    "Biotin (1 \u03bcg/\u03bcL)",
    "Biotin (1 ug/uL)",
    "0.01",
    "Biotin",
    "1",
)
COBALAMIN_STOCK = Stock(
    "Cobalamin (1 \u03bcg/\u03bcL)",
    "Cobalamin (1 ug/uL)",
    "0.01",
    "Cobalamin",
    "1",
)
PABA_STOCK = Stock(
    "p-aminobenzoic acid (0.3 \u03bcg/\u03bcL)",
    "p-aminobenzoic acid (0.3 ug/uL)",
    "0.01",
    "p-Aminobenzoic acid",
    "0.3",
)
FOLIC_ACID_STOCK = Stock(
    "Folic acid (5 \u03bcg/\u03bcL)",
    "Folic acid (5 ug/uL)",
    "0.01",
    "Folic acid",
    "5",
)
PYRIDOXAMINE_STOCK = Stock(
    "Pyridoxamine (15 \u03bcg/\u03bcL)",
    "Pyridoxamine (15 ug/uL)",
    "0.01",
    "Pyridoxamine",
    "15",
)
BIOTIN_LATE_STOCKS = (
    RESAZURIN_STOCK,
    BIOTIN_STOCK,
    COBALAMIN_STOCK,
    PABA_STOCK,
    FOLIC_ACID_STOCK,
    PYRIDOXAMINE_STOCK,
)
THIAMINE_STOCK = Stock(
    "Thiamine (0.05 \u03bcg/mL)",
    "Thiamine (0.05 ug/mL)",
    "0.1",
    "Thiamine",
    "0.00005",
)
RIBOFLAVIN_STOCK = Stock(
    "Riboflavin (0.05 \u03bcg/mL)",
    "Riboflavin (0.05 ug/mL)",
    "1",
    "Riboflavin",
    "0.00005",
)
GLUCOSE_STOCK = Stock(
    "Glucose (0.1981 g/mL)",
    "Glucose (0.1981 g/mL)",
    "20",
    "Glucose",
    "198.1",
)
POST_AUTOCLAVE_STOCKS = (THIAMINE_STOCK, RIBOFLAVIN_STOCK, GLUCOSE_STOCK)

LEGACY_INGREDIENTS: tuple[Component, ...] = (
    (DISTILLED_WATER, "1", "G_PER_L"),
    (MAGNESIUM_SULFATE, "0.09", "G_PER_L"),
    (YEAST_EXTRACT, "2.5", "G_PER_L"),
    (SODIUM_CHLORIDE, "0.9", "G_PER_L"),
    (POTASSIUM_PHOSPHATE, "0.45", "G_PER_L"),
    (DIPOTASSIUM_PHOSPHATE, "0.5", "G_PER_L"),
    (SODIUM_CARBONATE, "4", "G_PER_L"),
    (CALCIUM_CHLORIDE, "0.09", "G_PER_L"),
    (HAEMIN, "0.01", "G_PER_L"),
    (CYSTEINE, "1", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
    (CASITONE, "10", "G_PER_L"),
    COBALAMIN_STOCK.legacy_signature,
    RESAZURIN_STOCK.legacy_signature,
    PABA_STOCK.legacy_signature,
    FOLIC_ACID_STOCK.legacy_signature,
    PYRIDOXAMINE_STOCK.legacy_signature,
    BIOTIN_STOCK.legacy_signature,
    ("Glucose (0.1981 g/mL)", "20", "G_PER_L"),
    ("Riboflavin (0.05 \u03bcg/mL)", "1", "G_PER_L"),
    THIAMINE_STOCK.legacy_signature,
)

FINAL_INGREDIENTS: tuple[Component, ...] = (
    (CASITONE, "10", "G_PER_L"),
    (YEAST_EXTRACT, "2.5", "G_PER_L"),
    (SODIUM_CARBONATE, "4", "G_PER_L"),
    (DIPOTASSIUM_PHOSPHATE, "0.5", "G_PER_L"),
    (POTASSIUM_PHOSPHATE, "0.45", "G_PER_L"),
    (SODIUM_CHLORIDE, "0.9", "G_PER_L"),
    (MAGNESIUM_SULFATE, "0.09", "G_PER_L"),
    (CALCIUM_CHLORIDE, "0.09", "G_PER_L"),
    (CYSTEINE, "1.0", "G_PER_L"),
    (HAEMIN, "0.01", "G_PER_L"),
    (DISTILLED_WATER, "1.0", "L"),
    (AGAR, "15", "G_PER_L"),
)

FINAL_SOLUTIONS: tuple[SolutionSignature, ...] = (
    *(stock.final_signature for stock in BIOTIN_LATE_STOCKS),
    *(stock.final_signature for stock in POST_AUTOCLAVE_STOCKS),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    AGAR: ("CHEBI:2509", "agar"),
    BIOTIN_STOCK.component_name: ("CHEBI:15956", "Biotin"),
    CALCIUM_CHLORIDE: ("CHEBI:3312", "calcium dichloride"),
    COBALAMIN_STOCK.component_name: ("CHEBI:30411", "Cobalamine"),
    CYSTEINE: ("CHEBI:15356", "cysteine"),
    DIPOTASSIUM_PHOSPHATE: ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    DISTILLED_WATER: ("CHEBI:15377", "water"),
    FOLIC_ACID_STOCK.component_name: ("CHEBI:27470", "Folic acid"),
    GLUCOSE_STOCK.component_name: ("CHEBI:17234", "glucose"),
    HAEMIN: ("CHEBI:50385", "hemin"),
    MAGNESIUM_SULFATE: ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    PABA_STOCK.component_name: ("CHEBI:30753", "p-Aminobenzoic acid"),
    POTASSIUM_PHOSPHATE: ("CHEBI:63036", "potassium dihydrogen phosphate"),
    PYRIDOXAMINE_STOCK.component_name: ("CHEBI:16410", "Pyridoxamine"),
    RESAZURIN_STOCK.component_name: ("CHEBI:8806", "Resazurin"),
    RIBOFLAVIN_STOCK.component_name: ("CHEBI:17015", "Riboflavin"),
    SODIUM_CARBONATE: ("CHEBI:29377", "sodium carbonate"),
    SODIUM_CHLORIDE: ("CHEBI:26710", "sodium chloride"),
    THIAMINE_STOCK.component_name: ("CHEBI:18385", "Thiamine"),
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    AGAR: ("SOLIDIFYING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_ML": "mg/ml",
    "ML_PER_L": "ml/L",
}

REFERENCES = (TOGO_M3052_API, NBRC_1604)

RECIPE_NOTES = (
    "TOGO M3052 imports NBRC Medium 1604. NBRC 1604 lists Casitone, "
    "yeast extract, NaCO3, K2HPO4, KH2PO4, NaCl, MgSO4 7H2O, CaCl2, "
    "Cysteine, Haemin, Resazurin, Biotin, Cobalamin, p-aminobenzoic "
    "acid, Folic acid, Pyridoxamine, and Agar. TOGO adds the 1 L "
    "Distilled water solvent row. NBRC instructs Thiamine, Riboflavin, "
    "and Glucose stock additions after the medium is autoclaved, with all "
    "components added aseptically."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Combine the NBRC 1604 basal ingredients with 1 L Distilled water and add 15 g/L Agar."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Add the NBRC-listed Resazurin, Biotin, Cobalamin, "
            "p-aminobenzoic acid, Folic acid, and Pyridoxamine stocks."
        ),
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the medium.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "After autoclaving, aseptically add the Thiamine, Riboflavin, and Glucose stocks."
        ),
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _put_after(doc: dict[str, Any], key: str, value: Any, after_key: str) -> None:
    if key in doc:
        doc[key] = value
        return

    rebuilt: dict[str, Any] = {}
    placed = False
    for existing_key, existing_value in doc.items():
        rebuilt[existing_key] = existing_value
        if existing_key == after_key:
            rebuilt[key] = value
            placed = True
    if not placed:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


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


def _solution_signatures(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signatures: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{label} composition"),
            )
        )
    return tuple(signatures)


def _notes(preferred_term: str, value: str, unit: str) -> str:
    if preferred_term == CASITONE:
        return (
            f"{SOURCE} lists 10 g/L Casitone; this peptone product is "
            "retained as an opaque complex component."
        )
    if preferred_term == DISTILLED_WATER:
        return "TOGO M3052 lists 1 L Distilled water for NBRC Medium 1604."
    return f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}."


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or _notes(preferred_term, value, unit),
    }
    if preferred_term == DISTILLED_WATER:
        row["source"] = "TOGO M3052"
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles is not None:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _ingredients() -> list[dict[str, Any]]:
    return [_component(name, value, unit) for name, value, unit in FINAL_INGREDIENTS]


def _stock(stock: Stock, after_autoclave: bool) -> dict[str, Any]:
    timing = " after autoclaving" if after_autoclave else ""
    return {
        "preferred_term": stock.final_name,
        "concentration": {"value": stock.addition_value, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (f"{SOURCE} lists {stock.addition_value} ml/L {stock.final_name}{timing}."),
        "term": _term(*GROUNDINGS[stock.component_name]),
        "mediaingredientmech_chebi_term": _term(*GROUNDINGS[stock.component_name]),
        "composition": [
            _component(
                stock.component_name,
                stock.component_value,
                "MG_PER_ML",
                notes=f"NBRC Medium 1604 specifies this stock as {stock.final_name}.",
            )
        ],
        "name": stock.final_name,
        "preparation_notes": "Add aseptically." if after_autoclave else None,
    }


def _solutions() -> list[dict[str, Any]]:
    return [
        *[_stock(stock, after_autoclave=False) for stock in BIOTIN_LATE_STOCKS],
        *[_stock(stock, after_autoclave=True) for stock in POST_AUTOCLAVE_STOCKS],
    ]


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {LEGACY_INGREDIENTS, FINAL_INGREDIENTS}:
        raise ValueError(f"{TARGET}: ingredient signature drifted to {ingredient_signature!r}")

    solution_signatures = _solution_signatures(doc.get("solutions"), "solutions")
    if solution_signatures not in {(), FINAL_SOLUTIONS}:
        raise ValueError(f"{TARGET}: solution signature drifted to {solution_signatures!r}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag for flag in flags if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Curated TOGO:M3052 from TOGO and NBRC Medium 1604; nested "
            "the Resazurin, Biotin, Cobalamin, p-aminobenzoic acid, "
            "Folic acid, Pyridoxamine, Thiamine, Riboflavin, and Glucose "
            "stocks with their active components, grounded resolvable "
            "salts, cofactors, water, and agar, and retained Casitone as "
            "a sourced opaque component."
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


def _clean_solution(solution: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in solution.items() if value is not None}


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    _put_after(repaired, "solutions", [_clean_solution(s) for s in _solutions()], "ingredients")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "solutions")
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    return {target_path: repair_target(_load(target_path))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
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
