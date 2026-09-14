#!/usr/bin/env python3
"""Repair TOGO M1192 Modified SW-25 and M1198 Ethane-C Medium records."""

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

CURATOR = "repair_togo_m1192_m1198_score15.py"
ACTION = "RESOLVED_TOGO_M1192_M1198_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1191 = "https://togomedium.org/medium/M1191"
TOGO_M1192 = "https://togomedium.org/medium/M1192"
TOGO_M1196 = "https://togomedium.org/medium/M1196"
TOGO_M1198 = "https://togomedium.org/medium/M1198"
JCM_1114 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1114"
JCM_1118 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1118"
JCM_1120 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1120"
MEDIADIVE_J1114 = "https://mediadive.dsmz.de/rest/medium/J1114"
MEDIADIVE_J1120 = "https://mediadive.dsmz.de/rest/medium/J1120"

SW25_SOURCE = "JCM Medium 1114 / MediaDive J1114"
ETHANE_SOURCE = "JCM Medium 1120 / MediaDive J1120"
SULFURIMONAS_SOURCE = "JCM Medium 1118"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term: str
    title: str


M1192 = Target(
    Path("bacterial/TOGO_M1192_Modified_SW-25_Medium.yaml"),
    "CultureMech:007718",
    "TOGO:M1192",
    "Modified SW-25 Medium",
)
M1198 = Target(
    Path("bacterial/TOGO_M1198_Ethane-C_Medium.yaml"),
    "CultureMech:007723",
    "TOGO:M1198",
    "Ethane-C Medium",
)
TARGETS = (M1192, M1198)

M1192_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract", "1", "G_PER_L"),
    ("agar", "20", "G_PER_L"),
    ("Casamino acids (BD-Difco)", "1", "G_PER_L"),
)
M1192_IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("SW--25 solution (see Medium [M1191])", "1", "G_PER_L", ()),
)

M1198_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("KH2PO4", "0.01", "G_PER_L"),
    ("NH4NO3", "0.1", "G_PER_L"),
    ("Fe(III)\u30fbEDTA", "2.5", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
)
M1198_IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Vitamin mixture (see Medium [M1196])", "2.5", "G_PER_L", ()),
    ("Metal mixture (see Medium [M1196])", "1", "G_PER_L", ()),
    ("Artificial seawater (see Medium [M1196])", "1", "G_PER_L", ()),
)

SW25_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "195.0", "G_PER_L"),
    ("MgCl2 x 6H2O", "32.5", "G_PER_L"),
    ("MgSO4 x 7H2O", "51.0", "G_PER_L"),
    ("KCl", "5.0", "G_PER_L"),
    ("NaBr", "0.6", "G_PER_L"),
    ("NaHCO3", "0.16", "G_PER_L"),
    ("CaCl2 x 2H2O", "0.8", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)
VITAMIN_SIGNATURE: tuple[Component, ...] = (
    ("Vitamin B12", "1.1", "MG_PER_L"),
    ("Biotin", "1.0", "MG_PER_L"),
    ("Thiamine HCl", "200.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)
METAL_SIGNATURE: tuple[Component, ...] = (
    ("EDTA x 2Na", "0.372", "G_PER_L"),
    ("CuSO4 x 5H2O", "0.25", "MG_PER_L"),
    ("ZnSO4 x 7H2O", "5.75", "MG_PER_L"),
    ("MnCl2 x 6H2O", "4.55", "MG_PER_L"),
    ("CoCl2 x 6H2O", "0.6", "MG_PER_L"),
    ("(NH4)6Mo7O24 x 4H2O", "0.27", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)
ARTIFICIAL_SEAWATER_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "26.3", "G_PER_L"),
    ("CaCl2 x 2H2O", "1.54", "G_PER_L"),
    ("KBr", "0.1", "G_PER_L"),
    ("KF", "0.004", "G_PER_L"),
    ("KCl", "0.7", "G_PER_L"),
    ("H3BO3", "30.0", "MG_PER_L"),
    ("MgSO4 x 7H2O", "7.0", "G_PER_L"),
    ("KHCO3", "0.24", "G_PER_L"),
    ("SrCl2 x 6H2O", "17.0", "MG_PER_L"),
    ("MgCl2 x 6H2O", "5.2", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)6Mo7O24 x 4H2O": ("CHEBI:91249", "ammonium molybdate"),
    "Agar": ("CHEBI:2509", "agar"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoCl2 x 6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuSO4 x 5H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "EDTA x 2Na": ("CHEBI:64734", "EDTA disodium salt (anhydrous)"),
    "Fe(III)-EDTA": ("CHEBI:30729", "ethylenediaminetetraacetatoferrate(1-)"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "KBr": ("CHEBI:32030", "potassium bromide"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KF": ("CHEBI:66872", "potassium fluoride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "KHCO3": ("CHEBI:81862", "potassium hydrogencarbonate"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "NaBr": ("CHEBI:63004", "sodium bromide"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "NH4NO3": ("CHEBI:63038", "ammonium nitrate"),
    "SrCl2 x 6H2O": ("CHEBI:36385", "strontium dichloride hexahydrate"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "ZnSO4 x 7H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "PERCENT_V_V": "% v/v",
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
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _components(
    signature: tuple[Component, ...],
    *,
    source: str,
    ungrounded: frozenset[str] = frozenset(),
) -> list[dict[str, Any]]:
    return [
        _component(
            preferred_term,
            value,
            unit,
            source=source,
            term=preferred_term not in ungrounded,
        )
        for preferred_term, value, unit in signature
    ]


def _solution(
    preferred_term: str,
    value: str,
    composition: list[dict[str, Any]],
    *,
    source: str,
    notes: str,
    preparation_notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": composition,
        "preparation_notes": preparation_notes,
    }


def _sw25_solution() -> dict[str, Any]:
    return _solution(
        "SW-25 solution",
        "1000.0",
        _components(SW25_SIGNATURE, source=SW25_SOURCE),
        source=SW25_SOURCE,
        notes="JCM Medium 1114 adds 1000 ml SW-25 solution to the main recipe.",
        preparation_notes="Add components to distilled water and bring volume to 1.0 L.",
    )


def _vitamin_mixture() -> dict[str, Any]:
    return _solution(
        "Vitamin mixture",
        "2.5",
        _components(VITAMIN_SIGNATURE, source=ETHANE_SOURCE),
        source=ETHANE_SOURCE,
        notes="JCM Medium 1120 adds 2.5 ml Vitamin mixture to the main solution.",
        preparation_notes="JCM Medium 1120 prints the Vitamin mixture subrecipe per liter.",
    )


def _metal_mixture() -> dict[str, Any]:
    return _solution(
        "Metal mixture",
        "1.0",
        _components(
            METAL_SIGNATURE,
            source=ETHANE_SOURCE,
            ungrounded=frozenset({"MnCl2 x 6H2O"}),
        ),
        source=ETHANE_SOURCE,
        notes="JCM Medium 1120 adds 1.0 ml Metal mixture to the main solution.",
        preparation_notes="JCM Medium 1120 prints the Metal mixture subrecipe per liter.",
    )


def _artificial_seawater() -> dict[str, Any]:
    return _solution(
        "Artificial seawater",
        "1000.0",
        _components(ARTIFICIAL_SEAWATER_SIGNATURE, source=ETHANE_SOURCE),
        source=ETHANE_SOURCE,
        notes=("JCM Medium 1120 adds 1000 ml Artificial seawater to the main " "solution."),
        preparation_notes=(
            "Artificial seawater can be replaced with natural seawater that is "
            "filtered and boiled, then filtered again through a 0.45 um filter "
            "after cooling."
        ),
    )


def _m1192_ingredients() -> list[dict[str, Any]]:
    return [
        _component(
            "Casamino acids (BD-Difco)",
            "1.0",
            "G_PER_L",
            source=SW25_SOURCE,
            notes="JCM Medium 1114 lists 1.0 g/L Casamino acids with BD-Difco attribute.",
            term=False,
        ),
        _component(
            "Yeast extract",
            "1.0",
            "G_PER_L",
            source=SW25_SOURCE,
            term=False,
        ),
        _component("Agar", "20.0", "G_PER_L", source=SW25_SOURCE),
    ]


def _m1198_ingredients() -> list[dict[str, Any]]:
    return [
        _component(
            "NH4NO3",
            "0.0996016",
            "G_PER_L",
            source=ETHANE_SOURCE,
            notes=(
                "JCM Medium 1120 lists 0.1 g NH4NO3 in the 1004 ml main "
                "solution; MediaDive normalizes this to 0.0996016 g/L."
            ),
        ),
        _component(
            "KH2PO4",
            "0.00996016",
            "G_PER_L",
            source=ETHANE_SOURCE,
            notes=(
                "JCM Medium 1120 lists 0.01 g KH2PO4 in the 1004 ml main "
                "solution; MediaDive normalizes this to 0.00996016 g/L."
            ),
        ),
        _component(
            "Fe(III)-EDTA",
            "0.00249004",
            "G_PER_L",
            source=ETHANE_SOURCE,
            notes=(
                "JCM Medium 1120 lists 2.5 mg Fe(III)-EDTA in the 1004 ml "
                "main solution; MediaDive normalizes this to 0.00249004 g/L."
            ),
        ),
        _component(
            "NaOH",
            "variable",
            "VARIABLE",
            source=ETHANE_SOURCE,
            notes="JCM Medium 1120 adjusts the main solution to pH 8.0 with NaOH.",
        ),
        _component(
            "Ethane",
            "10-50",
            "PERCENT_V_V",
            source=ETHANE_SOURCE,
            notes="JCM Medium 1120 adds ethane to 10-50% of the gas phase by volume.",
            term=False,
        ),
    ]


def _ingredients(target: Target) -> list[dict[str, Any]]:
    if target == M1192:
        return _m1192_ingredients()
    if target == M1198:
        return _m1198_ingredients()
    raise ValueError(f"{target.path}: no ingredient repair configured")


def _solutions(target: Target) -> list[dict[str, Any]]:
    if target == M1192:
        return [_sw25_solution()]
    if target == M1198:
        return [_vitamin_mixture(), _metal_mixture(), _artificial_seawater()]
    raise ValueError(f"{target.path}: no solution repair configured")


def _m1192_preparation_steps() -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Mix SW-25 solution, Casamino acids, yeast extract, and agar.",
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust to pH 7.5.",
        },
        {
            "step_number": 3,
            "action": "AUTOCLAVE",
            "description": "Autoclave the solid medium.",
        },
    ]


def _m1198_preparation_steps() -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Mix NH4NO3, KH2PO4, Fe(III)-EDTA, Vitamin mixture, Metal "
                "mixture, and Artificial seawater."
            ),
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust to pH 8.0 with NaOH.",
        },
        {
            "step_number": 3,
            "action": "ALIQUOT",
            "description": (
                "Distribute 20-50 ml aliquots into 120 ml serum bottles and "
                "seal with butyl rubber stoppers."
            ),
        },
        {
            "step_number": 4,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 110 degrees C for 5 min.",
        },
        {
            "step_number": 5,
            "action": "MIX",
            "description": (
                "Allow the autoclaved medium to stand overnight, then add "
                "ethane to 10-50% of the gas phase by volume."
            ),
        },
    ]


def _preparation_steps(target: Target) -> list[dict[str, Any]]:
    if target == M1192:
        return _m1192_preparation_steps()
    if target == M1198:
        return _m1198_preparation_steps()
    raise ValueError(f"{target.path}: no preparation repair configured")


def _notes(target: Target) -> str:
    if target == M1192:
        return (
            "TOGO M1192 records JCM_M1114-2 as a solid-agar Modified SW-25 "
            "Medium variant. JCM Medium 1114 / MediaDive J1114 supplies the "
            "complete SW-25 solution composition, 1.0 g/L each yeast extract "
            "and Casamino acids, pH 7.5, and a 20.0 g/L agar supplement for "
            "solid medium."
        )
    if target == M1198:
        return (
            "TOGO M1198 records JCM_M1120 as Ethane-C Medium. MediaDive J1120 "
            "supplies the complete main solution at pH 8.0, the Vitamin "
            "mixture, Metal mixture, and Artificial seawater compositions "
            "cross-referenced from TOGO M1196, 110 degrees C autoclaving for "
            "5 min, overnight standing after sterilization, and 10-50% v/v "
            "ethane in the gas phase."
        )
    raise ValueError(f"{target.path}: no notes repair configured")


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


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError("solution row lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition"), "solution composition"),
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


def _imported_ingredient_signature(target: Target) -> tuple[Component, ...]:
    if target == M1192:
        return M1192_IMPORTED_INGREDIENT_SIGNATURE
    if target == M1198:
        return M1198_IMPORTED_INGREDIENT_SIGNATURE
    raise ValueError(f"{target.path}: no imported ingredient signature configured")


def _imported_solution_signatures(target: Target) -> tuple[SolutionSignature, ...]:
    if target == M1192:
        return M1192_IMPORTED_SOLUTION_SIGNATURES
    if target == M1198:
        return M1198_IMPORTED_SOLUTION_SIGNATURES
    raise ValueError(f"{target.path}: no imported solution signature configured")


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.media_term:
        raise ValueError(f"{target.path}: expected media term {target.media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        _imported_ingredient_signature(target),
        _signature(_ingredients(target), "final ingredients"),
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        _imported_solution_signatures(target),
        _solution_signatures({"solutions": _solutions(target)}),
    ):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _references(target: Target) -> tuple[str, ...]:
    if target == M1192:
        return (TOGO_M1192, JCM_1114, MEDIADIVE_J1114, TOGO_M1191)
    if target == M1198:
        return (
            TOGO_M1198,
            JCM_1120,
            MEDIADIVE_J1120,
            TOGO_M1196,
            JCM_1118,
        )
    raise ValueError(f"{target.path}: no references configured")


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in _references(target):
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target, notes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(_references(target)),
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    notes = _notes(target)
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX" if target == M1192 else "DEFINED"
    repaired["composition_type"] = "SEMI_DEFINED" if target == M1192 else "DEFINED"
    repaired["physical_state"] = "SOLID_AGAR" if target == M1192 else "LIQUID"
    _put_after(repaired, "ph_value", 7.5 if target == M1192 else 8.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(target)
    repaired["solutions"] = _solutions(target)
    _put_after(repaired, "preparation_steps", _preparation_steps(target), "solutions")
    if target == M1198:
        _put_after(
            repaired,
            "sterilization",
            {
                "method": "AUTOCLAVE",
                "temperature": {"value": 110.0, "unit": "CELSIUS"},
                "duration": "5 min",
                "notes": "JCM Medium 1120 autoclaves the sealed medium at 110 C for 5 min.",
            },
            "preparation_steps",
        )
    _put_after(repaired, "notes", notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target, notes)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
        for target in TARGETS
    }


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
