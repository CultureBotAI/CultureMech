#!/usr/bin/env python3
"""Repair TOGO M1244 NAS-02 Medium."""

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
TARGET = Path("bacterial/TOGO_M1244_NAS-02_Medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1244_score15.py"
ACTION = "RESOLVED_TOGO_M1244_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

RECORD_ID = "CultureMech:007774"
MEDIA_TERM = "TOGO:M1244"

TOGO_M1244 = "https://togomedium.org/medium/M1244"
TOGO_M1072 = "https://togomedium.org/medium/M1072"
TOGO_M190 = "https://togomedium.org/medium/M190"
JCM_1162 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1162"
JCM_1014 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1014"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"
MEDIADIVE_J1162 = "https://mediadive.dsmz.de/rest/medium/J1162"

SOURCE = "JCM Medium 1162 / MediaDive J1162"
JCM_1014_SOURCE = "JCM Medium 1014"
JCM_197_SOURCE = "JCM Medium 197"
MIDDLE_DOT = "\u30fb"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("KH2PO4", "3", "G_PER_L"),
    ("(NH4)2SO4", "0.2", "G_PER_L"),
    (f"Na2S2O3{MIDDLE_DOT}5H2O", "2.5", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)
IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Modified Allen's trace metal solution (see Medium [M1072])", "1", "G_PER_L", ()),
    (f"5% (w/v) CaCl2{MIDDLE_DOT}2H2O solution", "5", "G_PER_L", ()),
    ("10% (w/v) Yeast extract solution", "5", "G_PER_L", ()),
    (f"5% (w/v) MgSO4{MIDDLE_DOT}7H2O solution", "10", "G_PER_L", ()),
    ("130 mM FeCl2 solution", "10", "G_PER_L", ()),
    (f"25 mM L-Cysteine{MIDDLE_DOT}HCl solution", "10", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
)

MAIN_SIGNATURE: tuple[Component, ...] = (
    ("(NH4)2SO4", "0.190295", "G_PER_L"),
    ("KH2PO4", "2.85442", "G_PER_L"),
    ("Na2S2O3 x 5H2O", "2.37869", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
)
MODIFIED_ALLEN_SIGNATURE: tuple[Component, ...] = (
    ("MnCl2 x 4H2O", "1.8", "G_PER_L"),
    ("Na2B4O7 x 10H2O", "4.5", "G_PER_L"),
    ("ZnSO4 x 7H2O", "0.22", "G_PER_L"),
    ("CuCl2 x 2H2O", "0.05", "G_PER_L"),
    ("Na2MoO4 x 2H2O", "0.03", "G_PER_L"),
    ("VOSO4 x nH2O", "0.03", "G_PER_L"),
    ("CoSO4 x 7H2O", "0.01", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)
TRACE_VITAMINS_SIGNATURE: tuple[Component, ...] = (
    ("Biotin", "2.0", "MG_PER_L"),
    ("Folic acid", "2.0", "MG_PER_L"),
    ("Pyridoxine HCl", "10.0", "MG_PER_L"),
    ("Thiamine HCl", "5.0", "MG_PER_L"),
    ("Riboflavin", "5.0", "MG_PER_L"),
    ("Nicotinic acid", "5.0", "MG_PER_L"),
    ("Calcium pantothenate", "5.0", "MG_PER_L"),
    ("Vitamin B12", "0.1", "MG_PER_L"),
    ("p-Aminobenzoic acid", "5.0", "MG_PER_L"),
    ("Lipoic acid", "5.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "CoSO4 x 7H2O": ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    "CuCl2 x 2H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl2": ("CHEBI:30812", "iron dichloride"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "L-Cysteine HCl": ("CHEBI:91247", "L-cysteine hydrochloride"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnCl2 x 4H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "Na2B4O7 x 10H2O": ("CHEBI:131366", "disodium tetraborate decahydrate"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S2O3 x 5H2O": ("CHEBI:32150", "sodium thiosulfate pentahydrate"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "VOSO4 x nH2O": ("CHEBI:87020", "vanadyl sulfate hydrate"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "ZnSO4 x 7H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "MILLIMOLAR": "mM",
    "ML_PER_L": "ml/L",
    "VARIABLE": "variable",
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
    grounding = GROUNDINGS[preferred_term]
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(*grounding),
    }
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _solution(
    preferred_term: str,
    value: str,
    composition: list[dict[str, Any]],
    *,
    source: str = "JCM Medium 1162",
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": composition,
    }


def _main_ingredients() -> list[dict[str, Any]]:
    return [
        _component(
            "(NH4)2SO4",
            "0.190295",
            "G_PER_L",
            source=SOURCE,
            notes="JCM Medium 1162 lists 0.2 g (NH4)2SO4; MediaDive J1162 normalizes this to 0.190295 g/L.",
        ),
        _component(
            "KH2PO4",
            "2.85442",
            "G_PER_L",
            source=SOURCE,
            notes="JCM Medium 1162 lists 3.0 g KH2PO4; MediaDive J1162 normalizes this to 2.85442 g/L.",
        ),
        _component(
            "Na2S2O3 x 5H2O",
            "2.37869",
            "G_PER_L",
            source=SOURCE,
            notes=(
                "JCM Medium 1162 lists 2.5 g Na2S2O3 x 5H2O; MediaDive "
                "J1162 normalizes this to 2.37869 g/L."
            ),
        ),
        _component(
            "Distilled water",
            "1000.0",
            "ML_PER_L",
            source="JCM Medium 1162",
            notes="JCM Medium 1162 lists 1.0 L distilled water before stock additions.",
        ),
        _component(
            "Carbon dioxide gas",
            "variable",
            "VARIABLE",
            source="JCM Medium 1162",
            notes="JCM Medium 1162 autoclaves NAS-02 medium under N2-CO2 (4:1, v/v).",
        ),
        _component(
            "N2",
            "variable",
            "VARIABLE",
            source="JCM Medium 1162",
            notes="JCM Medium 1162 autoclaves NAS-02 medium under N2-CO2 (4:1, v/v).",
        ),
    ]


def _modified_allen() -> dict[str, Any]:
    return _solution(
        "Modified Allen's trace metal solution",
        "1.0",
        [
            _component("MnCl2 x 4H2O", "1.8", "G_PER_L", source=JCM_1014_SOURCE),
            _component("Na2B4O7 x 10H2O", "4.5", "G_PER_L", source=JCM_1014_SOURCE),
            _component("ZnSO4 x 7H2O", "0.22", "G_PER_L", source=JCM_1014_SOURCE),
            _component("CuCl2 x 2H2O", "0.05", "G_PER_L", source=JCM_1014_SOURCE),
            _component("Na2MoO4 x 2H2O", "0.03", "G_PER_L", source=JCM_1014_SOURCE),
            _component("VOSO4 x nH2O", "0.03", "G_PER_L", source=JCM_1014_SOURCE),
            _component("CoSO4 x 7H2O", "0.01", "G_PER_L", source=JCM_1014_SOURCE),
            _component("Distilled water", "1.0", "L", source=JCM_1014_SOURCE),
        ],
        notes=(
            "JCM Medium 1162 adds 1.0 ml/L Modified Allen's trace metal "
            "solution from JCM Medium 1014."
        ),
    )


def _percent_solution(
    preferred_term: str,
    value: str,
    solute: str,
    grams_per_l: str,
) -> dict[str, Any]:
    return _solution(
        preferred_term,
        value,
        [
            _component(
                solute,
                grams_per_l,
                "G_PER_L",
                source="JCM Medium 1162",
                notes=(
                    f"JCM Medium 1162 lists {preferred_term}; this records "
                    f"the stock as {grams_per_l} g/L {solute}."
                ),
            )
        ],
        notes=f"JCM Medium 1162 adds {value} ml/L {preferred_term}.",
    )


def _molar_solution(
    preferred_term: str,
    value: str,
    solute: str,
    millimolar: str,
) -> dict[str, Any]:
    return _solution(
        preferred_term,
        value,
        [
            _component(
                solute,
                millimolar,
                "MILLIMOLAR",
                source="JCM Medium 1162",
                notes=(
                    f"JCM Medium 1162 lists {preferred_term}; this records "
                    f"the stock as {millimolar} mM {solute}."
                ),
            )
        ],
        notes=f"JCM Medium 1162 adds {value} ml/L {preferred_term}.",
    )


def _trace_vitamins() -> dict[str, Any]:
    return _solution(
        "Trace vitamins",
        "10.0",
        [
            _component(name, value, unit, source=JCM_197_SOURCE)
            for name, value, unit in TRACE_VITAMINS_SIGNATURE
        ],
        source=JCM_197_SOURCE,
        notes="JCM Medium 1162 adds 10.0 ml/L filter-sterilized Trace vitamins from JCM Medium 197.",
    )


def _solutions() -> list[dict[str, Any]]:
    return [
        _modified_allen(),
        _percent_solution("5% (w/v) MgSO4 x 7H2O solution", "10.0", "MgSO4 x 7H2O", "50.0"),
        _percent_solution("5% (w/v) CaCl2 x 2H2O solution", "5.0", "CaCl2 x 2H2O", "50.0"),
        _trace_vitamins(),
        _percent_solution("10% (w/v) Yeast extract solution", "5.0", "Yeast extract", "100.0"),
        _molar_solution("25 mM L-Cysteine HCl solution", "10.0", "L-Cysteine HCl", "25.0"),
        _molar_solution("130 mM FeCl2 solution", "10.0", "FeCl2", "130.0"),
    ]


def _notes() -> str:
    return (
        "JCM Medium 1162 defines NAS-02 Medium with thiosulfate, Modified "
        "Allen's trace metal solution from JCM Medium 1014, N2-CO2 "
        "autoclaving at pH 5.2, and anaerobic post-autoclave additions of "
        "calcium, magnesium, trace vitamins, yeast extract, cysteine, and "
        "ferrous chloride stocks."
    )


def _preparation_steps() -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Mix the main salts, Modified Allen's trace metal solution, "
                "sodium thiosulfate, and distilled water thoroughly and adjust "
                "pH to 5.2."
            ),
        },
        {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave the base medium under an N2-CO2 (4:1, v/v) gas mixture.",
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": (
                "After cooling, anaerobically and aseptically add the MgSO4, "
                "CaCl2, Trace vitamins, yeast extract, L-cysteine HCl, and "
                "FeCl2 solutions."
            ),
        },
    ]


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term") or {}
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if not isinstance(rows, list):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration") or {}
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} contains a non-mapping concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions")
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration") or {}
        if not isinstance(concentration, dict):
            raise ValueError("solutions contains a non-mapping concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition") or [], "composition"),
            )
        )
    return tuple(signatures)


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != RECORD_ID:
        raise ValueError(f"{TARGET}: expected id {RECORD_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (IMPORTED_INGREDIENT_SIGNATURE, MAIN_SIGNATURE):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signature = _solution_signatures(doc)
    if solution_signature not in (
        IMPORTED_SOLUTION_SIGNATURES,
        _solution_signatures({"solutions": _solutions()}),
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        composition = solution.get("composition") or []
        nested = [i for i in composition if isinstance(i, dict)] if isinstance(composition, list) else []
        components.extend(nested or [solution])
    return components


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)

    if "has_ontology_mappings" not in flags:
        flags.append("has_ontology_mappings")
    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")
    if all(_grounded(row) for row in _composition_components(doc)):
        if "has_unmapped_ingredients" in flags:
            flags.remove("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")


def _references() -> tuple[str, ...]:
    return (
        TOGO_M1244,
        JCM_1162,
        MEDIADIVE_J1162,
        TOGO_M1072,
        JCM_1014,
        TOGO_M190,
        JCM_197,
    )


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in _references():
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], notes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(_references()),
        "notes": notes,
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


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    notes = _notes()
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_value"] = 5.2
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _main_ingredients()
    repaired["solutions"] = _solutions()
    _put_after(repaired, "preparation_steps", _preparation_steps(), "solutions")
    _put_after(repaired, "notes", notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired, notes)
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
