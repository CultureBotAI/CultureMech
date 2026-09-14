#!/usr/bin/env python3
"""Repair TOGO M1176-M1178 Anaerobic Natural Seawater Medium records."""

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

CURATOR = "repair_togo_m1176_m1178_score15.py"
ACTION = "RESOLVED_TOGO_M1176_M1178_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M190 = "https://togomedium.org/medium/M190"
JCM_1102 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1102"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"

SOURCE = "JCM Medium 1102"
TITLE = "Anaerobic Natural Seawater Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term: str
    togo_url: str
    include_resazurin: bool
    include_reducers: bool
    include_pyruvate: bool
    include_vitamins: bool
    variant_note: str


TARGETS: tuple[Target, ...] = (
    Target(
        Path("bacterial/TOGO_M1176_Anaerobic_Natural_Seawater_Medium.yaml"),
        "CultureMech:007701",
        "TOGO:M1176",
        "https://togomedium.org/medium/M1176",
        include_resazurin=True,
        include_reducers=True,
        include_pyruvate=True,
        include_vitamins=False,
        variant_note="JCM 32399 variant supplemented with 10 mM sodium pyruvate",
    ),
    Target(
        Path("bacterial/TOGO_M1177_Anaerobic_Natural_Seawater_Medium.yaml"),
        "CultureMech:007702",
        "TOGO:M1177",
        "https://togomedium.org/medium/M1177",
        include_resazurin=False,
        include_reducers=False,
        include_pyruvate=False,
        include_vitamins=False,
        variant_note="JCM 33129 variant omitting resazurin and reducing agents",
    ),
    Target(
        Path("bacterial/TOGO_M1178_Anaerobic_Natural_Seawater_Medium.yaml"),
        "CultureMech:007703",
        "TOGO:M1178",
        "https://togomedium.org/medium/M1178",
        include_resazurin=True,
        include_reducers=True,
        include_pyruvate=False,
        include_vitamins=True,
        variant_note="JCM 33131 variant supplemented with trace vitamins",
    ),
)

NA2S_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Na2S x 9H2O", "5.0", "PERCENT_W_V"),
)
CYSTEINE_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("L-Cysteine HCl H2O", "5.0", "PERCENT_W_V"),
)
VITAMIN_SIGNATURE: tuple[Component, ...] = (
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
    "Biotin": ("CHEBI:15956", "biotin"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "L-Cysteine HCl H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "sodium pyruvate": ("CHEBI:50144", "sodium pyruvate"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "MILLIMOLAR": "mM",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
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
    notes: str,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _listed_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str = SOURCE,
    term: bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _stock(
    preferred_term: str,
    value: str,
    composition: list[dict[str, Any]],
    *,
    source: str,
    notes: str,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": composition,
    }
    if preparation_notes is not None:
        row["preparation_notes"] = preparation_notes
    return row


def _percent_stock(
    preferred_term: str,
    value: str,
    solute: str,
    percent: str,
) -> dict[str, Any]:
    return _stock(
        preferred_term,
        value,
        [
            _component(
                solute,
                percent,
                "PERCENT_W_V",
                source=SOURCE,
                notes=(
                    f"{preferred_term} is represented from the stock label as "
                    f"{percent}% w/v {solute}."
                ),
            )
        ],
        source=SOURCE,
        notes=f"JCM Medium 1102 adds {value} ml/L {preferred_term}.",
        preparation_notes="Autoclave and store under an N2 gas atmosphere.",
    )


def _trace_vitamins() -> dict[str, Any]:
    source = "JCM Medium 197"
    return _stock(
        "Trace vitamins",
        "10.0",
        [
            _listed_component(name, value, unit, source=source)
            for name, value, unit in VITAMIN_SIGNATURE
        ],
        source=SOURCE,
        notes="JCM Medium 1102 supplements the JCM 33131 variant with 10.0 ml/L Trace vitamins.",
        preparation_notes="JCM Medium 197 prints the Trace vitamins subrecipe per liter.",
    )


def _imported_ingredient_signature(target: Target) -> tuple[Component, ...]:
    rows: list[Component] = [
        ("Distilled water", "250", "G_PER_L"),
        ("Yeast extract", "1", "G_PER_L"),
    ]
    if target.include_resazurin:
        rows.append(("Resazurin", "0.5", "G_PER_L"))
    rows.extend(
        [
            ("Natural seawater (filtrated)", "750", "G_PER_L"),
            ("Tryptone", "5", "G_PER_L"),
            ("N2", "variable", "VARIABLE"),
        ]
    )
    if target.include_pyruvate:
        rows.append(("sodium pyruvate", "variable", "VARIABLE"))
    return tuple(rows)


def _ingredients(target: Target) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = [
        _listed_component("Tryptone", "5.0", "G_PER_L", term=False),
        _listed_component("Yeast extract", "1.0", "G_PER_L", term=False),
    ]
    if target.include_resazurin:
        rows.append(_listed_component("Resazurin", "0.5", "MG_PER_L"))
    rows.extend(
        [
            _listed_component(
                "Natural seawater (filtrated)",
                "750.0",
                "ML_PER_L",
                term=False,
            ),
            _listed_component("Distilled water", "250.0", "ML_PER_L"),
            _component(
                "N2",
                "variable",
                "VARIABLE",
                source=SOURCE,
                notes=(
                    "JCM Medium 1102 cools the boiled base, distributes the "
                    "medium, and stores reducing stocks under an N2 gas "
                    "atmosphere."
                ),
            ),
        ]
    )
    if target.include_pyruvate:
        rows.append(
            _component(
                "sodium pyruvate",
                "10.0",
                "MILLIMOLAR",
                source=SOURCE,
                notes="JCM Medium 1102 supplements strain JCM 32399 with 10 mM sodium pyruvate.",
            )
        )
    return rows


def _solutions(target: Target) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if target.include_reducers:
        rows.extend(
            [
                _percent_stock(
                    "5% L-Cysteine HCl H2O solution",
                    "6.0",
                    "L-Cysteine HCl H2O",
                    "5.0",
                ),
                _percent_stock(
                    "5% Na2S x 9H2O solution",
                    "6.0",
                    "Na2S x 9H2O",
                    "5.0",
                ),
            ]
        )
    if target.include_vitamins:
        rows.append(_trace_vitamins())
    return rows


def _imported_solution_signatures(target: Target) -> tuple[SolutionSignature, ...]:
    rows: list[SolutionSignature] = []
    if target.include_reducers:
        rows.extend(
            [
                ("5% Na2S\u30fb9H2O solution", "6", "G_PER_L", ()),
                ("5% L-Cysteine\u30fbHCl\u30fbH2O solution", "6", "G_PER_L", ()),
            ]
        )
    if target.include_vitamins:
        rows.append(("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()))
    return tuple(rows)


def _base_preparation_steps(target: Target) -> list[dict[str, Any]]:
    base_components = "tryptone, yeast extract, natural seawater, and distilled water"
    if target.include_resazurin:
        base_components = (
            "tryptone, yeast extract, resazurin, natural seawater, and "
            "distilled water"
        )

    steps: list[dict[str, Any]] = [
        {
            "step_number": 1,
            "action": "MIX",
            "description": f"Mix {base_components}.",
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust to pH 7.0.",
        },
        {
            "step_number": 3,
            "action": "COOL",
            "description": "Bring the medium to a boil and cool under an N2 gas atmosphere.",
        },
        {
            "step_number": 4,
            "action": "ALIQUOT",
            "description": (
                "Distribute the medium in culture vessels under N2 and seal "
                "with butyl rubber stoppers."
            ),
        },
        {
            "step_number": 5,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 degrees C for 15 min.",
        },
    ]

    if target.include_reducers:
        steps.append(
            {
                "step_number": len(steps) + 1,
                "action": "MIX",
                "description": (
                    "After cooling, aseptically and anaerobically add "
                    "6.0 ml/L each 5% L-Cysteine HCl H2O and 5% Na2S x "
                    "9H2O solutions autoclaved and stored under N2."
                ),
            }
        )
    if target.include_pyruvate:
        steps.append(
            {
                "step_number": len(steps) + 1,
                "action": "MIX",
                "description": "Supplement the JCM 32399 variant with 10 mM sodium pyruvate.",
            }
        )
    if target.include_vitamins:
        steps.append(
            {
                "step_number": len(steps) + 1,
                "action": "MIX",
                "description": (
                    "Supplement the JCM 33131 variant with 10.0 ml/L Trace "
                    "vitamins from JCM Medium 197."
                ),
            }
        )
    return steps


def _notes(target: Target) -> str:
    notes = (
        "TOGO {media_number} records JCM Medium 1102 as an anaerobic natural "
        "seawater base containing tryptone, yeast extract, {resazurin}"
        "filtered natural seawater, distilled water, and an N2 atmosphere; "
        "the source adjusts the base to pH 7.0. "
    ).format(
        media_number=target.media_term.removeprefix("TOGO:"),
        resazurin="resazurin, " if target.include_resazurin else "",
    )
    if target.include_reducers:
        notes += (
            "After autoclaving and cooling, the source adds 6.0 ml/L each "
            "5% L-Cysteine HCl H2O and 5% Na2S x 9H2O solutions. "
        )
    else:
        notes += (
            "For strain JCM 33129, the source omits resazurin and the "
            "L-Cysteine HCl H2O and Na2S x 9H2O reducing agents. "
        )
    if target.include_pyruvate:
        notes += "For strain JCM 32399, the source supplements 10 mM sodium pyruvate. "
    if target.include_vitamins:
        notes += (
            "For strain JCM 33131, the source supplements 10.0 ml/L Trace "
            "vitamins from JCM Medium 197. "
        )
    notes += target.variant_note + "."
    return notes


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
    references = [target.togo_url, JCM_1102]
    if target.include_vitamins:
        references.extend([TOGO_M190, JCM_197])
    return tuple(references)


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
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_value"] = 7.0
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(target)
    solutions = _solutions(target)
    if solutions:
        repaired["solutions"] = solutions
    else:
        repaired.pop("solutions", None)
    _put_after(repaired, "preparation_steps", _base_preparation_steps(target), "solutions")
    _put_after(
        repaired,
        "sterilization",
        {
            "method": "AUTOCLAVE",
            "temperature": {"value": 121.0, "unit": "CELSIUS"},
            "duration": "15 min",
            "notes": (
                "JCM's default sterilization is autoclaving at 121 degrees C "
                "for 15 min; JCM Medium 1102 autoclaves the anaerobic base "
                "after distribution under N2."
            ),
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
