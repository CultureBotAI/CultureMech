#!/usr/bin/env python3
"""Repair JCM J773 / TOGO M802 Rumen Fluid Medium records."""

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

CURATOR = "repair_jcm_j773_togo_m802_rumen_score15.py"
ACTION = "RESOLVED_JCM_J773_TOGO_M802_RUMEN_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M802 = "https://togomedium.org/medium/M802"
TOGO_API_M802 = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M802"
JCM_773 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=773"
TOGO_M258 = "https://togomedium.org/medium/M258"
TOGO_M142 = "https://togomedium.org/medium/M142"
TOGO_M190 = "https://togomedium.org/medium/M190"

SOURCE = "JCM Medium 773 / TOGO M802"
TITLE = "Rumen Fluid Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term: str
    imported_ingredient_signature: tuple[Component, ...]
    imported_solution_signature: tuple[SolutionSignature, ...]


JCM_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "660", "ML_PER_L"),
    ("MgSO4・7H2O", "0.13", "G_PER_L"),
    ("NaCl", "0.6", "G_PER_L"),
    ("CaCl2・2H2O", "8", "MG_PER_L"),
    ("KH2PO4", "0.3", "G_PER_L"),
    ("K2HPO4", "0.3", "G_PER_L"),
    ("Resazurin", "1", "MG_PER_L"),
    ("Na2S・9H2O", "0.5", "G_PER_L"),
    ("FeSO4・7H2O", "2", "MG_PER_L"),
    ("NaHCO3", "2", "G_PER_L"),
    ("(NH4)2SO4", "0.3", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "1", "G_PER_L"),
    ("L--Cysteine・HCl・H2O", "0.5", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
    ("Hydrogen gas", "variable", "VARIABLE"),
)

TOGO_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "660", "G_PER_L"),
    ("MgSO4・7H2O", "0.13", "G_PER_L"),
    ("NaCl", "0.6", "G_PER_L"),
    ("CaCl2・2H2O", "8", "G_PER_L"),
    ("KH2PO4", "0.3", "G_PER_L"),
    ("K2HPO4", "0.3", "G_PER_L"),
    ("Resazurin", "1", "G_PER_L"),
    ("Na2S・9H2O", "0.5", "G_PER_L"),
    ("FeSO4・7H2O", "2", "G_PER_L"),
    ("NaHCO3", "2", "G_PER_L"),
    ("(NH4)2SO4", "0.3", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "1", "G_PER_L"),
    ("L--Cysteine・HCl・H2O", "0.5", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
    ("Hydrogen gas", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "660.0", "ML_PER_L"),
    ("MgSO4 x 7H2O", "0.13", "G_PER_L"),
    ("NaCl", "0.6", "G_PER_L"),
    ("CaCl2 x 2H2O", "8.0", "MG_PER_L"),
    ("KH2PO4", "0.3", "G_PER_L"),
    ("K2HPO4", "0.3", "G_PER_L"),
    ("Resazurin", "1.0", "MG_PER_L"),
    ("Na2S x 9H2O", "0.5", "G_PER_L"),
    ("FeSO4 x 7H2O", "2.0", "MG_PER_L"),
    ("NaHCO3", "2.0", "G_PER_L"),
    ("(NH4)2SO4", "0.3", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1.0", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "1.0", "G_PER_L"),
    ("L-Cysteine HCl H2O", "0.5", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
    ("Hydrogen gas", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURE_ML: tuple[SolutionSignature, ...] = (
    ("Rumen fluid, clarified (see Medium [M258])", "300", "ML_PER_L", ()),
    ("Trace minerals (see Medium [M142])", "10", "ML_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "ML_PER_L", ()),
)

IMPORTED_SOLUTION_SIGNATURE_G: tuple[SolutionSignature, ...] = (
    ("Rumen fluid, clarified (see Medium [M258])", "300", "G_PER_L", ()),
    ("Trace minerals (see Medium [M142])", "10", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("Rumen fluid, clarified (JCM Medium 266)", "300.0", "ML_PER_L", ()),
    ("Trace minerals (JCM Medium 151)", "10.0", "ML_PER_L", ()),
    ("Trace vitamins (JCM Medium 197)", "10.0", "ML_PER_L", ()),
)

TARGETS: tuple[Target, ...] = (
    Target(
        Path("bacterial/rumen_fluid_medium.yaml"),
        "CultureMech:003115",
        "mediadive.medium:J773",
        JCM_IMPORTED_INGREDIENT_SIGNATURE,
        IMPORTED_SOLUTION_SIGNATURE_ML,
    ),
    Target(
        Path("bacterial/TOGO_M802_Rumen_Fluid_Medium.yaml"),
        "CultureMech:010214",
        "TOGO:M802",
        TOGO_IMPORTED_INGREDIENT_SIGNATURE,
        IMPORTED_SOLUTION_SIGNATURE_G,
    ),
)

REFERENCES = (TOGO_M802, TOGO_API_M802, JCM_773, TOGO_M258, TOGO_M142, TOGO_M190)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4 x 7H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Hydrogen gas": ("CHEBI:18276", "dihydrogen"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "L-Cysteine HCl H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "yeast extract"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "(NH4)2SO4": ("NITROGEN_SOURCE",),
    "CaCl2 x 2H2O": ("TRACE_ELEMENT",),
    "FeSO4 x 7H2O": ("TRACE_ELEMENT",),
    "K2HPO4": ("PHOSPHATE_SOURCE",),
    "KH2PO4": ("PHOSPHATE_SOURCE",),
    "MgSO4 x 7H2O": ("TRACE_ELEMENT",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "K2HPO4": ("BUFFER",),
    "KH2PO4": ("BUFFER",),
    "Na2S x 9H2O": ("REDUCING_AGENT",),
    "NaHCO3": ("BUFFER",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "VARIABLE": "variable",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Mix all ingredients except NaHCO3, L-Cysteine HCl H2O, and "
            "Na2S x 9H2O, then adjust the pH to 6.5. Bring the medium to "
            "a boil for 5-10 seconds, cool under H2-CO2 (80:20, v/v), add "
            "NaHCO3, dispense under H2-CO2, seal, and autoclave. Separately "
            "autoclave cysteine HCl and Na2S x 9H2O as 5% solutions under "
            "N2. Before inoculation, aseptically and anaerobically add the "
            "sterile cysteine and sulfide solutions, then pressurize the "
            "inoculated bottles to 200 kPa H2-CO2 (80:20, v/v)."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Prepare clarified rumen fluid by preheating rumen content at "
            "120 C for 15 minutes and using the supernatant after "
            "centrifugation at 25,000 x g for 15 minutes."
        ),
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": "Use JCM Medium 266 without its fatty acid mixture.",
    },
)

NOTES = (
    "TOGO M802 preserves JCM Medium 773 as Rumen Fluid Medium after the JCM "
    "773 page became unavailable. The JCM formula contains 660.0 ml "
    "distilled water, 0.13 g MgSO4 x 7H2O, 0.6 g NaCl, 8.0 mg CaCl2 x "
    "2H2O, 0.3 g KH2PO4, 0.3 g K2HPO4, 1.0 mg resazurin, 0.5 g Na2S x "
    "9H2O, 2.0 mg FeSO4 x 7H2O, 2.0 g NaHCO3, 0.3 g (NH4)2SO4, 1.0 g "
    "Yeast extract from BD-Difco, 1.0 g Trypticase peptone from BD-BBL, "
    "0.5 g L-Cysteine HCl H2O, 300.0 ml clarified rumen fluid from JCM "
    "Medium 266, 10.0 ml Trace minerals from JCM Medium 151, 10.0 ml Trace "
    "vitamins from JCM Medium 197, and H2-CO2/N2 anaerobic gas handling. "
    "JCM Medium 773 omits the JCM Medium 266 fatty acid mixture and adjusts "
    "the medium to pH 6.5."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    if unit == "VARIABLE":
        notes = f"{SOURCE} uses {preferred_term} as a gas-phase component."
    else:
        notes = f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}."

    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    if grounding := GROUNDINGS.get(preferred_term):
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    if nutritional_roles := NUTRITIONAL_ROLES.get(preferred_term):
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles := PHYSICOCHEMICAL_ROLES.get(preferred_term):
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(name, value, unit) for name, value, unit in FINAL_INGREDIENT_SIGNATURE
)


def _stock(preferred_term: str, value: str, source: str, notes: str) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": [],
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock(
        "Rumen fluid, clarified (JCM Medium 266)",
        "300.0",
        "JCM Medium 773 / JCM Medium 266",
        "JCM Medium 773 adds 300.0 ml/L clarified rumen fluid from JCM Medium 266.",
    ),
    _stock(
        "Trace minerals (JCM Medium 151)",
        "10.0",
        "JCM Medium 773 / JCM Medium 151",
        "JCM Medium 773 adds 10.0 ml/L Trace minerals from JCM Medium 151.",
    ),
    _stock(
        "Trace vitamins (JCM Medium 197)",
        "10.0",
        "JCM Medium 773 / JCM Medium 197",
        "JCM Medium 773 adds 10.0 ml/L Trace vitamins from JCM Medium 197.",
    ),
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


def _solution_signature(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
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
                _signature(row.get("composition"), f"{label}.composition"),
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
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.media_term:
        raise ValueError(f"{target.path}: expected media term {target.media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        target.imported_ingredient_signature,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted to {ingredient_signature!r}")

    solution_signature = _solution_signature(doc.get("solutions"), "solutions")
    if solution_signature not in (
        target.imported_solution_signature,
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{target.path}: solution signature drifted to {solution_signature!r}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
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
            "Repaired the JCM Medium 773 formula from TOGO M802, corrected "
            "TOGO g/L import artifacts for water, trace milligram salts, and "
            "stock additions, grounded all direct defined chemicals and gases, "
            "added the pH 6.5 instruction, and preserved the clarified rumen "
            "fluid, trace-mineral, and trace-vitamin external boundaries."
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
    _put_after(repaired, "ph_value", 6.5, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["notes"] = NOTES
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
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
