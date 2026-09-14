#!/usr/bin/env python3
"""Repair JCM 479 Thermodesulfovibrio score-20 composition."""

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
TARGET = Path("bacterial/thermodesulfovibrio_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_479_score20.py"
ACTION = "RESOLVED_JCM_479_SCORE20_GRAPH"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
JCM_479 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=479"
JCM_284 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=284"

EXPECTED_ID = "CultureMech:002828"
EXPECTED_MEDIA_TERM = "mediadive.medium:J479"

NOTES = (
    "JCM Medium 479 uses JCM Medium 284 Solution A without yeast extract, "
    "0.05 volume each of sodium lactate Solution B and sodium sulfate "
    "Solution C, and 0.01 volume each of 3% L-cysteine hydrochloride hydrate "
    "and 3% sodium sulfide nonahydrate stocks."
)

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    term: tuple[str, str],
    *,
    source: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {unit.lower().replace('_per_l', '/L')}.",
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


def _solution(
    preferred_term: str,
    value: str,
    notes: str,
    composition: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "notes": notes,
        "composition": copy.deepcopy(composition),
    }


def _jcm284(
    preferred_term: str,
    value: str,
    unit: str,
    term: tuple[str, str],
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        term,
        source="JCM Medium 284 Solution A",
    )


def _stock_component(
    preferred_term: str,
    value: str,
    unit: str,
    term: tuple[str, str],
    *,
    source: str,
) -> dict[str, Any]:
    return _component(preferred_term, value, unit, term, source=source)


TRACE_VITAMINS: list[dict[str, Any]] = [
    _stock_component(
        "Biotin",
        "0.0049",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
    _stock_component(
        "Folic acid",
        "0.0088",
        "G_PER_L",
        ("CHEBI:27470", "folic acid"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
    _stock_component(
        "Pyridoxine x HCl",
        "0.0041",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
    _stock_component(
        "Thiamine x HCl",
        "0.0067",
        "G_PER_L",
        ("CHEBI:49105", "thiamine hydrochloride"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
    _stock_component(
        "Riboflavin",
        "0.0075",
        "G_PER_L",
        ("CHEBI:17015", "riboflavin"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
    _stock_component(
        "Nicotinic acid",
        "0.0025",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
    _stock_component(
        "DL-Calcium pantothenate",
        "0.0095",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
    _stock_component(
        "Vitamin B12",
        "0.0271",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
    _stock_component(
        "p-Aminobenzoic acid",
        "0.0027",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
    _stock_component(
        "Lipoic acid",
        "0.0041",
        "G_PER_L",
        ("CHEBI:16494", "lipoic acid"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
    _stock_component(
        "Distilled water",
        "1000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        source="JCM Medium 284 Trace vitamins solution",
    ),
]

TRACE_ELEMENTS: list[dict[str, Any]] = [
    _stock_component(
        "Nitrilotriacetic acid",
        "12.8",
        "G_PER_L",
        ("CHEBI:44557", "nitrilotriacetic acid"),
        source="JCM Medium 284 Trace element solution",
    ),
    _stock_component(
        "FeCl3 x 6 H2O",
        "1.35",
        "G_PER_L",
        ("CHEBI:86254", "iron trichloride hexahydrate"),
        source="JCM Medium 284 Trace element solution",
    ),
    _stock_component(
        "MnCl2 x 4 H2O",
        "0.1",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        source="JCM Medium 284 Trace element solution",
    ),
    _stock_component(
        "CoCl2 x 6 H2O",
        "0.024",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        source="JCM Medium 284 Trace element solution",
    ),
    _stock_component(
        "CaCl2 x 2 H2O",
        "0.1",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        source="JCM Medium 284 Trace element solution",
    ),
    _stock_component(
        "ZnCl2",
        "0.1",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        source="JCM Medium 284 Trace element solution",
    ),
    _stock_component(
        "CuCl2 x 2 H2O",
        "0.025",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        source="JCM Medium 284 Trace element solution",
    ),
    _stock_component(
        "H3BO3",
        "0.01",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        source="JCM Medium 284 Trace element solution",
    ),
    _stock_component(
        "Na2MoO4 x 2 H2O",
        "0.024",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        source="JCM Medium 284 Trace element solution",
    ),
    _stock_component(
        "NiCl2 x 6 H2O",
        "0.12",
        "G_PER_L",
        ("CHEBI:34887", "nickel dichloride"),
        source="JCM Medium 284 Trace element solution",
    ),
    _stock_component(
        "Distilled water",
        "1000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        source="JCM Medium 284 Trace element solution",
    ),
]

SE_W: list[dict[str, Any]] = [
    _stock_component(
        "Na2SeO3 x 5 H2O",
        "0.004",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        source="JCM Medium 284 Se/W solution",
    ),
    _stock_component(
        "Na2WO4 x 2 H2O",
        "0.004",
        "G_PER_L",
        ("CHEBI:63939", "sodium tungstate dihydrate"),
        source="JCM Medium 284 Se/W solution",
    ),
    _stock_component(
        "Distilled water",
        "1000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        source="JCM Medium 284 Se/W solution",
    ),
]

RECIPE: dict[str, Any] = {
    "medium_type": "DEFINED",
    "composition_type": "DEFINED",
    "physical_state": "LIQUID",
    "ingredients": [
        _jcm284("KH2PO4", "0.14", "G_PER_L", ("CHEBI:63036", "potassium dihydrogen phosphate")),
        _jcm284(
            "MgCl2 x 6 H2O",
            "0.2",
            "G_PER_L",
            ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        ),
        _jcm284(
            "CaCl2 x 2 H2O",
            "0.15",
            "G_PER_L",
            ("CHEBI:86158", "calcium chloride dihydrate"),
        ),
        _jcm284("NH4Cl", "0.54", "G_PER_L", ("CHEBI:31206", "ammonium chloride")),
        _jcm284(
            "NaHCO3",
            "2.5",
            "G_PER_L",
            ("CHEBI:32139", "sodium hydrogencarbonate"),
        ),
        _jcm284("Resazurin", "0.001", "G_PER_L", ("CHEBI:8806", "Resazurin")),
        _jcm284("Distilled water", "900", "ML_PER_L", ("CHEBI:15377", "water")),
    ],
    "solutions": [
        _solution(
            "Trace vitamins solution",
            "2.0",
            "JCM Medium 284 Solution A lists 2.0 ml/L Trace vitamins solution.",
            TRACE_VITAMINS,
        ),
        _solution(
            "Trace element solution",
            "1.0",
            "JCM Medium 284 Solution A lists 1.0 ml/L Trace element solution.",
            TRACE_ELEMENTS,
        ),
        _solution(
            "Se/W solution",
            "1.0",
            "JCM Medium 284 Solution A lists 1.0 ml/L Se/W solution.",
            SE_W,
        ),
        _solution(
            "Solution B",
            "50.0",
            "JCM Medium 479 adds 0.05 volume of the 44 g/L sodium lactate Solution B.",
            [
                _stock_component(
                    "Sodium lactate",
                    "44.0",
                    "G_PER_L",
                    ("CHEBI:75228", "sodium lactate"),
                    source="JCM Medium 479 Solution B",
                )
            ],
        ),
        _solution(
            "Solution C",
            "50.0",
            "JCM Medium 479 adds 0.05 volume of the 56 g/L Na2SO4 Solution C.",
            [
                _stock_component(
                    "Na2SO4",
                    "56.0",
                    "G_PER_L",
                    ("CHEBI:32149", "sodium sulfate"),
                    source="JCM Medium 479 Solution C",
                )
            ],
        ),
        _solution(
            "3% L-Cysteine x HCl x H2O solution",
            "10.0",
            "JCM Medium 479 adds 0.01 volume of a 3% L-Cysteine x HCl x H2O solution.",
            [
                _stock_component(
                    "L-Cysteine x HCl x H2O",
                    "30.0",
                    "G_PER_L",
                    ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
                    source="JCM Medium 479 3% reductant stock",
                )
            ],
        ),
        _solution(
            "3% Na2S x 9H2O solution",
            "10.0",
            "JCM Medium 479 adds 0.01 volume of a 3% Na2S x 9H2O solution.",
            [
                _stock_component(
                    "Na2S x 9H2O",
                    "30.0",
                    "G_PER_L",
                    ("CHEBI:76209", "sodium sulfide nonahydrate"),
                    source="JCM Medium 479 3% reductant stock",
                )
            ],
        ),
    ],
    "preparation_steps": [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare JCM Medium 284 Solution A without yeast extract by "
                "mixing salts, trace stocks, resazurin, and 900 ml distilled "
                "water."
            ),
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust Solution A to pH 6.5 before bicarbonate addition.",
        },
        {
            "step_number": 3,
            "action": "HEAT",
            "description": "Bring Solution A to a boil and cool under N2-CO2 (80:20, v/v).",
        },
        {
            "step_number": 4,
            "action": "AUTOCLAVE",
            "description": (
                "Add bicarbonate to Solution A, distribute into culture vessels "
                "under N2-CO2, seal with butyl rubber stoppers, autoclave, and "
                "stand overnight."
            ),
        },
        {
            "step_number": 5,
            "action": "AUTOCLAVE",
            "description": "Autoclave Solutions B and C under a N2 atmosphere.",
        },
        {
            "step_number": 6,
            "action": "MIX",
            "description": (
                "Aseptically add Solution B, Solution C, L-cysteine stock, and "
                "Na2S stock to the culture vessels under anaerobic conditions."
            ),
        },
    ],
    "sterilization": {"method": "AUTOCLAVE"},
}


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


def _components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        row
        for rows in (doc.get("ingredients") or [], doc.get("solutions") or [])
        for row in rows
        if isinstance(row, dict)
    ]


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    if any(_grounded(component) for component in _components(doc)):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    if any(not _grounded(component) for component in _components(doc)):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    doc["data_quality_flags"] = list(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in (JCM_479, JCM_284):
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join((JCM_479, JCM_284)),
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
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in RECIPE:
            repaired[recipe_field] = copy.deepcopy(RECIPE[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    repaired["notes"] = NOTES
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repair(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repair(args.normalized_dir)
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
    sys.exit(main())
