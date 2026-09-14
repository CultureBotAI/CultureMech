#!/usr/bin/env python3
"""Repair KOMODO 2073-2075 trace mineral solution records."""

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

FERGUSON_TARGET = Path("bacterial/trace_mineral_solution_ferguson_and_mah_1983.yaml")
MEDIUM_1000_TARGET = Path("bacterial/trace_mineral_solution_medium_1000.yaml")
MEDIUM_1003_TARGET = Path("bacterial/trace_mineral_solution_medium_1003.yaml")

TARGETS: dict[Path, dict[str, str]] = {
    FERGUSON_TARGET: {
        "id": "CultureMech:004350",
        "media_term": "komodo.medium:2073",
        "name": "Trace mineral solution (Ferguson and Mah, 1983)",
    },
    MEDIUM_1000_TARGET: {
        "id": "CultureMech:004351",
        "media_term": "komodo.medium:2074",
        "name": "Trace mineral solution (medium 1000)",
    },
    MEDIUM_1003_TARGET: {
        "id": "CultureMech:004352",
        "media_term": "komodo.medium:2075",
        "name": "Trace mineral solution (medium 1003)",
    },
}
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_2073_2075_score15.py"
ACTION = "RESOLVED_KOMODO_2073_2075_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

KOMODO_ROOT = "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed"
REFERENCES = {
    FERGUSON_TARGET: f"{KOMODO_ROOT}?MediaInfo=2073",
    MEDIUM_1000_TARGET: f"{KOMODO_ROOT}?MediaInfo=2074",
    MEDIUM_1003_TARGET: f"{KOMODO_ROOT}?MediaInfo=2075",
}
SOURCE_LABELS = {
    FERGUSON_TARGET: "KOMODO Medium 2073",
    MEDIUM_1000_TARGET: "KOMODO Medium 2074",
    MEDIUM_1003_TARGET: "KOMODO Medium 2075",
}

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURES: dict[Path, tuple[Component, ...]] = {
    FERGUSON_TARGET: (("HCl", "variable", "VARIABLE"),),
    MEDIUM_1000_TARGET: (),
    MEDIUM_1003_TARGET: (("HCl", "variable", "VARIABLE"),),
}

FINAL_INGREDIENT_SIGNATURES: dict[Path, tuple[Component, ...]] = {
    FERGUSON_TARGET: (
        ("CoCl2 x 6 H2O", "0.15", "G_PER_L"),
        ("HCl", "variable", "VARIABLE"),
        ("AlCl3 x 6 H2O", "0.04", "G_PER_L"),
        ("ZnCl2", "0.10", "G_PER_L"),
        ("H2SeO3", "0.01", "G_PER_L"),
        ("Na2-EDTA x 2 H2O", "0.50", "G_PER_L"),
        ("MnCl2 x 4 H2O", "0.10", "G_PER_L"),
        ("FeSO4 x 7 H2O", "0.10", "G_PER_L"),
        ("CuCl2 x 2 H2O", "0.02", "G_PER_L"),
        ("NiSO4 x 6 H2O", "0.02", "G_PER_L"),
        ("H3BO3", "0.01", "G_PER_L"),
        ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
        ("Na2WO4 x 2 H2O", "0.03", "G_PER_L"),
    ),
    MEDIUM_1000_TARGET: (
        ("KAl(SO4)2 x 12 H2O", "0.02", "G_PER_L"),
        ("MnSO4 x 2 H2O", "0.50", "G_PER_L"),
        ("ZnSO4 x 7 H2O", "0.18", "G_PER_L"),
        ("CuSO4 x 5 H2O", "0.01", "G_PER_L"),
        ("Nitrilotriacetic acid", "1.50", "G_PER_L"),
        ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
        ("H3BO3", "0.01", "G_PER_L"),
        ("CoSO4 x 7 H2O", "0.50", "G_PER_L"),
    ),
    MEDIUM_1003_TARGET: (
        ("CoCl2 x 6 H2O", "0.15", "G_PER_L"),
        ("HCl", "variable", "VARIABLE"),
        ("Na-EDTA x 2 H2O", "0.50", "G_PER_L"),
        ("ZnCl2", "0.10", "G_PER_L"),
        ("AlCl3 x 6 H2O", "0.04", "G_PER_L"),
        ("Selenic acid", "0.01", "G_PER_L"),
        ("Na2WO4 x 2 H2O", "0.03", "G_PER_L"),
        ("MnCl2 x 4 H2O", "0.10", "G_PER_L"),
        ("FeSO4 x 7 H2O", "0.10", "G_PER_L"),
        ("NiSO4 x 6 H2O", "0.02", "G_PER_L"),
        ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
        ("H2O", "1.0", "L"),
        ("H3BO3", "0.01", "G_PER_L"),
        ("CuCl", "0.02", "G_PER_L"),
    ),
}

INTERMEDIATE_INGREDIENT_SIGNATURES: dict[Path, tuple[Component, ...]] = {
    MEDIUM_1003_TARGET: tuple(
        (
            ("Se-acid", value, unit)
            if preferred_term == "Selenic acid"
            else (preferred_term, value, unit)
        )
        for preferred_term, value, unit in FINAL_INGREDIENT_SIGNATURES[MEDIUM_1003_TARGET]
    ),
}

GROUNDINGS: dict[str, tuple[str, str]] = {
    "AlCl3 x 6 H2O": ("CHEBI:30115", "aluminium trichloride hexahydrate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CoSO4 x 7 H2O": ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    "CuCl": ("CHEBI:53472", "copper(I) chloride"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "H2O": ("CHEBI:15377", "water"),
    "H2SeO3": ("CHEBI:26642", "selenous acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "HCl": ("CHEBI:17883", "hydrogen chloride"),
    "KAl(SO4)2 x 12 H2O": ("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "MnSO4 x 2 H2O": ("CHEBI:86356", "manganese(II) sulfate dihydrate"),
    "Na-EDTA x 2 H2O": ("CHEBI:64758", "EDTA disodium salt dihydrate"),
    "Na2-EDTA x 2 H2O": ("CHEBI:64758", "EDTA disodium salt dihydrate"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2WO4 x 2 H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NiSO4 x 6 H2O": ("CHEBI:53437", "nickel sulfate hexahydrate"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "Selenic acid": ("CHEBI:18170", "selenic acid"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

SOURCE_SPELLINGS = {
    (FERGUSON_TARGET, "Na2MoO4 x 2 H2O"): "NaMoO4 x 2 H2O",
    (MEDIUM_1003_TARGET, "Selenic acid"): "Se-acid",
    (MEDIUM_1003_TARGET, "Na2WO4 x 2 H2O"): "Na-tungstate x 2 H2O",
    (MEDIUM_1003_TARGET, "NiSO4 x 6 H2O"): "Ni2SO4 x 6 H2O",
    (MEDIUM_1003_TARGET, "H3BO3"): "HBO3",
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "VARIABLE": "variable",
}

PH_VALUES: dict[Path, float] = {
    FERGUSON_TARGET: 3.0,
    MEDIUM_1003_TARGET: 3.0,
}

NOTES = {
    FERGUSON_TARGET: (
        "KOMODO 2073 lists Trace mineral solution (Ferguson and Mah, 1983) as a "
        "defined submedium at pH 3.0. Its metabolite table contains 0.50 g/L "
        "Na2-EDTA x 2 H2O, 0.15 g/L CoCl2 x 6 H2O, 0.10 g/L ZnCl2, 0.10 g/L "
        "MnCl2 x 4 H2O, 0.10 g/L FeSO4 x 7 H2O, 0.04 g/L AlCl3 x 6 H2O, "
        "0.03 g/L Na2WO4 x 2 H2O, 0.02 g/L CuCl2 x 2 H2O, 0.02 g/L "
        "NiSO4 x 6 H2O, 0.01 g/L H2SeO3, 0.01 g/L H3BO3, 0.01 g/L "
        "NaMoO4 x 2 H2O, and variable HCl."
    ),
    MEDIUM_1000_TARGET: (
        "KOMODO 2074 lists Trace mineral solution (medium 1000) as a defined "
        "submedium. Its metabolite table contains 1.50 g/L nitrilotriacetic acid, "
        "0.50 g/L MnSO4 x 2 H2O, 0.50 g/L CoSO4 x 7 H2O, 0.18 g/L "
        "ZnSO4 x 7 H2O, 0.02 g/L KAl(SO4)2 x 12 H2O, 0.01 g/L "
        "CuSO4 x 5 H2O, 0.01 g/L Na2MoO4 x 2 H2O, and 0.01 g/L H3BO3."
    ),
    MEDIUM_1003_TARGET: (
        "KOMODO 2075 lists Trace mineral solution (medium 1003) as a defined "
        "submedium at pH 3.0. Its metabolite table contains 0.50 g/L "
        "Na-EDTA x 2 H2O, 0.15 g/L CoCl2 x 6 H2O, 0.10 g/L ZnCl2, "
        "0.10 g/L MnCl2 x 4 H2O, 0.10 g/L FeSO4 x 7 H2O, 0.04 g/L "
        "AlCl3 x 6 H2O, 0.03 g/L Na-tungstate x 2 H2O, 0.02 g/L "
        "Ni2SO4 x 6 H2O, 0.02 g/L CuCl, 0.01 g/L Se-acid, 0.01 g/L "
        "Na2MoO4 x 2 H2O, 0.01 g/L HBO3, variable HCl, and H2O."
    ),
}

PREPARATION_STEPS = {
    FERGUSON_TARGET: (
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare the 1 L Ferguson and Mah trace mineral stock from HCl, "
                "Na2-EDTA, the cobalt, aluminum, zinc, selenium, manganese, "
                "iron, copper, nickel, borate, molybdate, and tungstate salts "
                "listed by KOMODO."
            ),
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust the Ferguson and Mah trace mineral stock to pH 3.0 with HCl.",
        },
    ),
    MEDIUM_1000_TARGET: (
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare the trace mineral stock from nitrilotriacetic acid and "
                "the potassium aluminum, manganese, zinc, copper, molybdate, "
                "borate, and cobalt salts listed by KOMODO."
            ),
        },
    ),
    MEDIUM_1003_TARGET: (
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare the 1 L medium 1003 trace mineral stock from HCl, H2O, "
                "Na-EDTA, the cobalt, zinc, aluminum, selenium, tungstate, "
                "manganese, iron, nickel, molybdate, borate, and copper salts "
                "listed by KOMODO."
            ),
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust the medium 1003 trace mineral stock to pH 3.0 with HCl.",
        },
    ),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    target: Path, source: str, preferred_term: str, value: str, unit: str
) -> dict[str, Any]:
    source_name = SOURCE_SPELLINGS.get((target, preferred_term), preferred_term)
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {UNIT_LABELS[unit]} {source_name}.",
    }
    if preferred_term == "H2O":
        row["notes"] = (
            f"{source} lists H2O without a gram amount; normalized here as "
            "the solvent for 1 L of the medium 1003 trace mineral stock."
        )
    elif preferred_term == "HCl":
        row["notes"] = (
            f"{source} lists HCl without a gram amount and also identifies "
            "HCl as the pH adjuster for pH 3.0."
        )
    elif source_name != preferred_term:
        row["notes"] = (
            f"{source} lists {value} {UNIT_LABELS[unit]} {source_name}; "
            f"normalized here as {preferred_term}."
        )

    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(target: Path) -> list[dict[str, Any]]:
    source = SOURCE_LABELS[target]
    return [
        _component(target, source, preferred_term, value, unit)
        for preferred_term, value, unit in FINAL_INGREDIENT_SIGNATURES[target]
    ]


def _signature(rows: Any) -> tuple[Component, ...]:
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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


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


def _ensure_target(target: Path, doc: dict[str, Any]) -> None:
    expected = TARGETS[target]
    if doc.get("id") != expected["id"]:
        raise ValueError(f"{target}: expected id {expected['id']}, found {doc.get('id')!r}")
    if _source_term_id(doc) != expected["media_term"]:
        raise ValueError(f"{target}: expected media term {expected['media_term']}")

    ingredient_signature = _signature(doc.get("ingredients"))
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURES[target],
        FINAL_INGREDIENT_SIGNATURES[target],
        INTERMEDIATE_INGREDIENT_SIGNATURES.get(target, ()),
    }:
        raise ValueError(f"{target}: ingredient signature drifted to {ingredient_signature!r}")

    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    if solutions:
        raise ValueError(f"{target}: unexpected solutions")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag not in {"extracted_from_notes", "incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(target: Path, doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    reference = REFERENCES[target]
    if not any(row.get("reference") == reference for row in references if isinstance(row, dict)):
        references.append({"reference": reference})


def _set_solution_record_kind(doc: dict[str, Any]) -> None:
    reordered: dict[str, Any] = {}
    inserted = False
    for key, value in doc.items():
        if key == "record_kind":
            continue
        reordered[key] = value
        if key == "category":
            reordered["record_kind"] = "SOLUTION"
            inserted = True
    if not inserted:
        reordered["record_kind"] = "SOLUTION"

    doc.clear()
    doc.update(reordered)


def _append_event(target: Path, doc: dict[str, Any]) -> None:
    source = SOURCE_LABELS[target]
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": REFERENCES[target],
        "notes": (
            f"Replaced the incomplete {source} import with the complete KOMODO "
            "metabolite table, preserved HCl as a variable pH adjuster where "
            "KOMODO lists one, and grounded disclosed components through "
            "MediaIngredientMech."
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


def repair_record(target: Path, doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(target, doc)

    repaired = copy.deepcopy(doc)
    _set_solution_record_kind(repaired)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    if target in PH_VALUES:
        _put_after(repaired, "ph_value", PH_VALUES[target], "physical_state")
        repaired.pop("ph_range", None)
    else:
        repaired.pop("ph_value", None)
        repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(target)
    _put_after(repaired, "notes", NOTES[target], "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS[target])),
        "notes",
    )
    _ensure_flags(repaired)
    _ensure_references(target, repaired)
    _append_event(target, repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target
        plans[path] = repair_record(target, _load(path))
    return plans


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
