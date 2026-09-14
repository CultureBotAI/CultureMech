#!/usr/bin/env python3
"""Repair TOGO M1220 Natronospira Proteinivora Medium."""

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
TARGET = Path("bacterial/TOGO_M1220_Natronospira_Proteinivora_Medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1220_score15.py"
ACTION = "RESOLVED_TOGO_M1220_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

RECORD_ID = "CultureMech:007748"
MEDIA_TERM = "TOGO:M1220"

TOGO_M1220 = "https://togomedium.org/medium/M1220"
JCM_1139 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1139"
JCM_1079 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1079"
MEDIADIVE_J1139 = "https://mediadive.dsmz.de/rest/medium/J1139"

JCM_1139_SOURCE = "JCM Medium 1139"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Basic mineral salt medium 1 (see below)", "500", "G_PER_L"),
    ("Basal medium 2 (see below)", "500", "G_PER_L"),
    ("Distilled water", "102.0", "G_PER_L"),
    ("NaCl", "256.0", "G_PER_L"),
    ("K2HPO4", "4.5", "G_PER_L"),
    ("(NH4)2SO4", "0.5", "G_PER_L"),
    ("NaHCO3", "30", "G_PER_L"),
    ("Na2CO3", "190", "G_PER_L"),
    ("Casein", "5", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
)
IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("10% Tryptone solution (autoclaved)", "15", "G_PER_L", ()),
    ("1.0 Yeast extract solution (autoclaved)", "2", "G_PER_L", ()),
    ("Casein solution", "100", "G_PER_L", ()),
    ("1 M MgCl2 solution", "1", "G_PER_L", ()),
    ("Trace element solution (see Medium [M1148])", "1", "G_PER_L", ()),
    ("2 M NH4Cl solution", "4", "G_PER_L", ()),
    ("1 M MgCl2 solution", "1", "G_PER_L", ()),
    ("Trace element solution (see Medium [M1148])", "2", "G_PER_L", ()),
)

BASIC_MINERAL_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "240.0", "G_PER_L"),
    ("K2HPO4", "2.5", "G_PER_L"),
    ("(NH4)2SO4", "0.5", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("1 M K2HPO4 solution", "variable", "VARIABLE"),
    ("1 M MgCl2 solution", "1.0", "ML_PER_L"),
    ("Trace element solution", "1.0", "ML_PER_L"),
)
BASAL_SIGNATURE: tuple[Component, ...] = (
    ("Na2CO3", "190.0", "G_PER_L"),
    ("NaHCO3", "30.0", "G_PER_L"),
    ("NaCl", "16.0", "G_PER_L"),
    ("K2HPO4", "2.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("2 M NH4Cl solution", "4.0", "ML_PER_L"),
    ("1 M MgCl2 solution", "1.0", "ML_PER_L"),
    ("Trace element solution", "2.0", "ML_PER_L"),
)
TRYPTONE_SIGNATURE: tuple[Component, ...] = (("Tryptone", "100.0", "G_PER_L"),)
YEAST_SIGNATURE: tuple[Component, ...] = (("Yeast extract", "10.0", "G_PER_L"),)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "1 M K2HPO4 solution": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "1 M MgCl2 solution": ("CHEBI:6636", "magnesium dichloride"),
    "2 M NH4Cl solution": ("CHEBI:31206", "ammonium chloride"),
    "Distilled water": ("CHEBI:15377", "water"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Tryptone": ("MICRO:0000182", "Tryptone"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
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
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _solution(
    preferred_term: str,
    value: str,
    composition: list[dict[str, Any]],
    *,
    notes: str,
    preparation_notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": JCM_1139_SOURCE,
        "notes": notes,
        "composition": composition,
        "preparation_notes": preparation_notes,
    }


def _basic_mineral_salt_medium() -> dict[str, Any]:
    source = JCM_1139_SOURCE
    return _solution(
        "Basic mineral salt medium 1",
        "500.0",
        [
            _component("NaCl", "240.0", "G_PER_L", source=source),
            _component("K2HPO4", "2.5", "G_PER_L", source=source),
            _component("(NH4)2SO4", "0.5", "G_PER_L", source=source),
            _component("Distilled water", "1.0", "L", source=source),
            _component(
                "1 M K2HPO4 solution",
                "variable",
                "VARIABLE",
                source=source,
                notes=(
                    "JCM Medium 1139 adjusts Basic mineral salt medium 1 to "
                    "pH 6.8-6.9 with 1 M K2HPO4; the volume is not specified."
                ),
            ),
            _component(
                "1 M MgCl2 solution",
                "1.0",
                "ML_PER_L",
                source=source,
                notes=(
                    "JCM Medium 1139 adds 1.0 ml 1 M MgCl2 solution after "
                    "autoclaving Basic mineral salt medium 1."
                ),
            ),
            _component(
                "Trace element solution",
                "1.0",
                "ML_PER_L",
                source=source,
                notes=(
                    "JCM Medium 1139 adds 1.0 ml JCM 1079 Trace element "
                    "solution after autoclaving Basic mineral salt medium 1."
                ),
                term=False,
            ),
        ],
        notes="JCM Medium 1139 adds 500.0 ml Basic mineral salt medium 1.",
        preparation_notes=(
            "Add NaCl, K2HPO4, and (NH4)2SO4 to distilled water and bring the "
            "volume to 1.0 L. Adjust pH to 6.8-6.9 with 1 M K2HPO4, autoclave, "
            "cool, then add the autoclaved 1 M MgCl2 and JCM 1079 Trace element "
            "solutions."
        ),
    )


def _basal_medium() -> dict[str, Any]:
    source = JCM_1139_SOURCE
    return _solution(
        "Basal medium 2",
        "500.0",
        [
            _component("Na2CO3", "190.0", "G_PER_L", source=source),
            _component("NaHCO3", "30.0", "G_PER_L", source=source),
            _component("NaCl", "16.0", "G_PER_L", source=source),
            _component("K2HPO4", "2.0", "G_PER_L", source=source),
            _component("Distilled water", "1.0", "L", source=source),
            _component(
                "2 M NH4Cl solution",
                "4.0",
                "ML_PER_L",
                source=source,
                notes=(
                    "JCM Medium 1139 adds 4.0 ml/L 2 M NH4Cl solution after "
                    "Basal medium 2 is autoclaved and decanted."
                ),
            ),
            _component(
                "1 M MgCl2 solution",
                "1.0",
                "ML_PER_L",
                source=source,
                notes=(
                    "JCM Medium 1139 adds 1.0 ml/L 1 M MgCl2 solution after "
                    "Basal medium 2 is autoclaved and decanted."
                ),
            ),
            _component(
                "Trace element solution",
                "2.0",
                "ML_PER_L",
                source=source,
                notes=(
                    "JCM Medium 1139 adds 2.0 ml/L JCM 1079 Trace element "
                    "solution after Basal medium 2 is autoclaved and decanted."
                ),
                term=False,
            ),
        ],
        notes="JCM Medium 1139 adds 500.0 ml Basal medium 2.",
        preparation_notes=(
            "Add Na2CO3, NaHCO3, NaCl, and K2HPO4 to distilled water and bring "
            "the volume to 1.0 L. Check pH at 9.9-10.0, autoclave, let stand "
            "for 3 days, decant the clear solution into a sterile bottle, then "
            "aseptically add autoclaved 2 M NH4Cl, 1 M MgCl2, and JCM 1079 "
            "Trace element solutions."
        ),
    )


def _tryptone_solution() -> dict[str, Any]:
    return _solution(
        "10% Tryptone solution",
        "15.0",
        [
            _component(
                "Tryptone",
                "100.0",
                "G_PER_L",
                source=JCM_1139_SOURCE,
                notes=(
                    "JCM Medium 1139 lists a 10% Tryptone solution; this "
                    "records the stock as 100.0 g/L."
                ),
            )
        ],
        notes="JCM Medium 1139 adds 15.0 ml 10% Tryptone solution.",
        preparation_notes="Autoclave the 10% Tryptone solution separately.",
    )


def _yeast_extract_solution() -> dict[str, Any]:
    return _solution(
        "1.0% Yeast extract solution",
        "2.0",
        [
            _component(
                "Yeast extract",
                "10.0",
                "G_PER_L",
                source=JCM_1139_SOURCE,
                notes=(
                    "JCM Medium 1139 lists a 1.0% Yeast extract solution; "
                    "this records the stock as 10.0 g/L."
                ),
            )
        ],
        notes="JCM Medium 1139 adds 2.0 ml 1.0% Yeast extract solution.",
        preparation_notes="Autoclave the 1.0% Yeast extract solution separately.",
    )


def _solutions() -> list[dict[str, Any]]:
    return [
        _basic_mineral_salt_medium(),
        _basal_medium(),
        _tryptone_solution(),
        _yeast_extract_solution(),
    ]


def _notes() -> str:
    return (
        "JCM Medium 1139 defines Natronospira Proteinivora Medium as equal "
        "volumes of separately autoclaved Basic mineral salt medium 1 and Basal "
        "medium 2 plus autoclaved 10% tryptone and 1.0% yeast extract stocks. "
        "JCM Medium 1139 also prints a Casein solution subrecipe, but gives no "
        "Casein solution addition in the main recipe, so this record omits "
        "casein from the final medium."
    )


def _preparation_steps() -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare Basic mineral salt medium 1, bring it to 1.0 L, adjust "
                "pH to 6.8-6.9 with 1 M K2HPO4, autoclave, cool, then add "
                "autoclaved MgCl2 and JCM 1079 Trace element solutions."
            ),
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": (
                "Prepare Basal medium 2, bring it to 1.0 L, confirm pH "
                "9.9-10.0, autoclave, let stand for 3 days, decant the clear "
                "solution, then add autoclaved NH4Cl, MgCl2, and JCM 1079 "
                "Trace element solutions."
            ),
        },
        {
            "step_number": 3,
            "action": "AUTOCLAVE",
            "description": "Autoclave the 10% Tryptone and 1.0% Yeast extract solutions.",
        },
        {
            "step_number": 4,
            "action": "MIX",
            "description": (
                "Aseptically combine 500 ml Basic mineral salt medium 1, 500 ml "
                "Basal medium 2, 15 ml 10% Tryptone solution, and 2 ml 1.0% "
                "Yeast extract solution."
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
    if ingredient_signature not in (IMPORTED_INGREDIENT_SIGNATURE, ()):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signature = _solution_signatures(doc)
    if solution_signature not in (
        IMPORTED_SOLUTION_SIGNATURES,
        _solution_signatures({"solutions": _solutions()}),
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


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


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        composition = solution.get("composition") or []
        nested = (
            [i for i in composition if isinstance(i, dict)] if isinstance(composition, list) else []
        )
        components.extend(nested or [solution])
    return components


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

    if all(_grounded(row) for row in _composition_components(doc)):
        flags.remove("has_unmapped_ingredients")


def _references() -> tuple[str, ...]:
    return (TOGO_M1220, JCM_1139, JCM_1079, MEDIADIVE_J1139)


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
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = []
    repaired["solutions"] = _solutions()
    _put_after(repaired, "preparation_steps", _preparation_steps(), "solutions")
    _put_after(repaired, "notes", notes, "media_term")
    repaired["high_metal"] = True
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
