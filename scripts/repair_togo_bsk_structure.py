#!/usr/bin/env python3
"""Restore the four stock-solution boundaries in TOGO M2366 BSK medium.

The legacy TOGO importer flattened Solutions A-D into final ingredients, treated
bare millilitre amounts as g/L, and omitted bovine serum albumin. Later enrichment
also attached three unrelated LB constituents. The checked-in TOGO payload retains
the complete nested recipe and preparation text from DSMZ Medium 403:

https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium403.pdf

This migration is dry-run by default. It requires exact reviewed signatures for
both the raw payload and the pre-repair normalized record before writing.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from importlib import import_module
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import write_record  # noqa: E402

TogoImporter = import_module("culturemech.import.togo_importer").TogoImporter

RAW_FILE = REPO / "data" / "raw" / "togo" / "togo_media.json"
NORMALIZED_FILE = (
    REPO / "data" / "normalized_yaml" / "bacterial" / "TOGO_M2366_BSK-Medium.yaml"
)
SOURCE_ID = "M2366"
MEDIA_TERM_ID = "TOGO:M2366"
ACTION = "RESTORED_TOGO_STOCK_SOLUTION_BOUNDARIES"

PRE_INGREDIENTS = (
    ("Aqua bidest. filter-sterilized", "900", "G_PER_L"),
    ("Glucose (\u03b1-, D+)", "3", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.3", "G_PER_L"),
    ("Na-pyruvate", "0.8", "G_PER_L"),
    ("Na-citrate", "0.7", "G_PER_L"),
    ("N-Acetylglucosamine", "0.4", "G_PER_L"),
    ("Proteose yeastolate (TC) (DIFCO 5577-15)", "1", "G_PER_L"),
    ("HEPES buffer (acid) (SIGMA H3375)", "6", "G_PER_L"),
    ("L-Glutamine", "0.1", "G_PER_L"),
    ("Proteose tryptone (DIFCO 0123-01)", "1", "G_PER_L"),
    ("CMRL 1066/10 x Glutamin (GIBCO 042-1545)", "100", "G_PER_L"),
    ("Proteose peptone No 2 (DIFCO 0121-01-3)", "5", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
    ("gelatine", "14", "G_PER_L"),
    ("bidest. Water", "343.0", "G_PER_L"),
    ("Tryptone", "10.0", "G_PER_L"),
    ("Yeast extract", "5.0", "G_PER_L"),
    ("Sodium chloride", "10.0", "G_PER_L"),
    ("Rabbit serum, inactivated(GIBCO 037-06120M)", "86", "G_PER_L"),
)

PRE_SOLUTIONS = (
    ("Solution A:", "1000", "G_PER_L", 0),
    ("Solution B:", "200", "G_PER_L", 0),
    ("Solution C:", "143", "G_PER_L", 0),
    ("Solution D:", "86", "G_PER_L", 0),
)

RAW_SIGNATURE = (
    (
        "",
        (
            ("Solution A:", "1000", "ml", "", "", SOURCE_ID),
            ("Solution B:", "200", "ml", "", "", SOURCE_ID),
            ("Solution C:", "143", "ml", "", "", SOURCE_ID),
            ("Solution D:", "86", "ml", "", "", SOURCE_ID),
        ),
    ),
    (
        "Solution A",
        (
            ("Aqua bidest. filter-sterilized", "900", "ml", "", "", ""),
            ("Glucose (\u03b1-, D+)", "3", "g", "", "", ""),
            ("MgCl2 x 6 H2O", "0.3", "g", "", "", ""),
            ("Na-pyruvate", "0.8", "g", "", "", ""),
            ("Na-citrate", "0.7", "g", "", "", ""),
            ("N-Acetylglucosamine", "0.4", "g", "", "", ""),
            ("Proteose yeastolate (TC) (DIFCO 5577-15)", "1", "g", "", "", ""),
            ("HEPES buffer (acid) (SIGMA H3375)", "6", "g", "", "", ""),
            ("L-Glutamine", "0.1", "g", "", "", ""),
            ("Proteose tryptone (DIFCO 0123-01)", "1", "g", "", "", ""),
            ("CMRL 1066/10 x Glutamin (GIBCO 042-1545)", "100", "ml", "", "", ""),
            ("Proteose peptone No 2 (DIFCO 0121-01-3)", "5", "g", "", "", ""),
            ("NaOH", "", "", "5", "M", ""),
        ),
    ),
    (
        "Solution B",
        (
            ("gelatine", "14", "g", "", "", ""),
            ("bidest. Water", "200", "ml", "", "", ""),
        ),
    ),
    (
        "Solution C",
        (
            ("bidest. Water", "143", "ml", "", "", ""),
            (
                "bovine serum albumine, fract. V (important: Sigma No A9647)",
                "50.05",
                "g",
                "",
                "",
                "",
            ),
        ),
    ),
    (
        "Solution D",
        (("Rabbit serum, inactivated(GIBCO 037-06120M)", "86", "ml", "", "", ""),),
    ),
)

EXPECTED_SOLUTIONS = (
    (
        "Solution A",
        "699.790",
        (
            ("Aqua bidest. filter-sterilized", "900", "ML_PER_L"),
            ("Glucose (\u03b1-, D+)", "3", "G_PER_L"),
            ("MgCl2 x 6 H2O", "0.3", "G_PER_L"),
            ("Na-pyruvate", "0.8", "G_PER_L"),
            ("Na-citrate", "0.7", "G_PER_L"),
            ("N-Acetylglucosamine", "0.4", "G_PER_L"),
            ("Proteose yeastolate (TC) (DIFCO 5577-15)", "1", "G_PER_L"),
            ("HEPES buffer (acid) (SIGMA H3375)", "6", "G_PER_L"),
            ("L-Glutamine", "0.1", "G_PER_L"),
            ("Proteose tryptone (DIFCO 0123-01)", "1", "G_PER_L"),
            ("CMRL 1066/10 x Glutamin (GIBCO 042-1545)", "100", "ML_PER_L"),
            ("Proteose peptone No 2 (DIFCO 0121-01-3)", "5", "G_PER_L"),
        ),
    ),
    (
        "Solution B",
        "139.958",
        (("gelatine", "70", "G_PER_L"), ("bidest. Water", "1000", "ML_PER_L")),
    ),
    (
        "Solution C",
        "100.070",
        (
            ("bidest. Water", "1000", "ML_PER_L"),
            (
                "bovine serum albumine, fract. V (important: Sigma No A9647)",
                "350",
                "G_PER_L",
            ),
        ),
    ),
    (
        "Solution D",
        "60.182",
        (("Rabbit serum, inactivated(GIBCO 037-06120M)", "1000", "ML_PER_L"),),
    ),
)

SOURCE_COMMENTS = (
    "Stir slowly at 4 -10\u00b0C for 3 hours, adjust pH to 7.6 with 5 M NaOH. "
    "Filter sterilize.",
    "Dissolve 14.0 g gelatine in 200 ml bidest. water, autoclave 15 minutes at 115\u00b0C.",
    "Dissolve 50.05 g bovine serum albumine, fract. V (important: Sigma No A9647) "
    "in 143 ml bidest. water, or use BSA-solution Sigma A7409.",
    "Combine the warm (37\u00b0C) solutions A, B, C, D, and filter-sterilize the warm "
    "medium. Solution B can also be added after filtration.",
    "Alternatively, buy supplemented or un-supplementedBSK-H medium (Fa. Bio&SELLor "
    "Sigma) and supplement the medium according to manufacturer\u2019s advice. Sterilize "
    "the mixed and warm (37\u00b0C) medium by filtration.",
)

IDENTITY_FIELDS = (
    "term",
    "mediaingredientmech_term",
    "mediaingredientmech_chebi_term",
    "supplier_catalog",
    "synonyms",
)

WATER_IDENTITY = {
    "term": {"id": "CHEBI:15377", "label": "water"},
    "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
}


def _value(value: object) -> str:
    return "" if value in (None, "") else str(value)


def media_term_id(doc: dict[str, Any]) -> str:
    return _value(((doc.get("media_term") or {}).get("term") or {}).get("id"))


def ingredient_signature(rows: list[dict[str, Any]]) -> tuple[tuple[str, str, str], ...]:
    return tuple(
        (
            _value(row.get("preferred_term")),
            _value((row.get("concentration") or {}).get("value")),
            _value((row.get("concentration") or {}).get("unit")),
        )
        for row in rows
    )


def solution_stub_signature(
    rows: list[dict[str, Any]],
) -> tuple[tuple[str, str, str, int], ...]:
    return tuple(
        (
            _value(row.get("preferred_term")),
            _value((row.get("concentration") or {}).get("value")),
            _value((row.get("concentration") or {}).get("unit")),
            len(row.get("composition") or []),
        )
        for row in rows
    )


def raw_signature(payload: dict[str, Any]) -> tuple[Any, ...]:
    return tuple(
        (
            _value(section.get("subcomponent_name")),
            tuple(
                (
                    _value(item.get("component_name")),
                    _value(item.get("volume")),
                    _value(item.get("unit")),
                    _value(item.get("conc_value")),
                    _value(item.get("conc_unit")),
                    _value(item.get("reference_media_id")),
                )
                for item in section.get("items", [])
            ),
        )
        for section in payload.get("components", [])
    )


def structured_solution_signature(rows: list[dict[str, Any]]) -> tuple[Any, ...]:
    return tuple(
        (
            _value(row.get("preferred_term")),
            _value((row.get("concentration") or {}).get("value")),
            ingredient_signature(row.get("composition") or []),
        )
        for row in rows
    )


def validate_payload(payload: dict[str, Any]) -> None:
    gm_id = _value((payload.get("meta") or {}).get("gm")).split("/")[-1]
    if gm_id != SOURCE_ID:
        raise ValueError(f"raw payload id is {gm_id!r}, expected {SOURCE_ID}")
    signature = raw_signature(payload)
    if signature != RAW_SIGNATURE:
        raise ValueError("TOGO M2366 component signature drifted from the reviewed payload")
    comments = tuple(
        _value(row.get("comment")).strip()
        for row in payload.get("comments", [])
        if _value(row.get("comment")).strip()
    )
    if comments != SOURCE_COMMENTS:
        raise ValueError("TOGO M2366 preparation comments drifted from the reviewed payload")


def _importer() -> Any:
    return TogoImporter.__new__(TogoImporter)


def _history_has_action(doc: dict[str, Any]) -> bool:
    return any(
        isinstance(row, dict) and row.get("action") == ACTION
        for row in doc.get("curation_history", [])
    )


def _apply_identity_links(
    solutions: list[dict[str, Any]], current_ingredients: list[dict[str, Any]]
) -> None:
    current_by_name = {
        _value(row.get("preferred_term")): row for row in current_ingredients
    }
    for solution in solutions:
        for ingredient in solution.get("composition", []):
            name = _value(ingredient.get("preferred_term"))
            current = current_by_name.get(name, {})
            for field in IDENTITY_FIELDS:
                if current.get(field) is not None:
                    ingredient[field] = copy.deepcopy(current[field])
            if name in {"Aqua bidest. filter-sterilized", "bidest. Water"}:
                ingredient.update(copy.deepcopy(WATER_IDENTITY))


def repair_document(
    doc: dict[str, Any], payload: dict[str, Any]
) -> tuple[dict[str, Any], bool]:
    """Return a guarded repaired copy and whether it differs from an applied record."""
    validate_payload(payload)
    if media_term_id(doc) != MEDIA_TERM_ID:
        raise ValueError(f"expected {MEDIA_TERM_ID}, found {media_term_id(doc)!r}")

    solutions = _importer()._extract_assembled_solutions(payload)
    if structured_solution_signature(solutions) != EXPECTED_SOLUTIONS:
        raise ValueError("TOGO importer did not reproduce the reviewed BSK solution structure")

    current_ingredients = [row for row in doc.get("ingredients", []) if isinstance(row, dict)]
    current_solutions = [row for row in doc.get("solutions", []) if isinstance(row, dict)]
    if _history_has_action(doc):
        if current_ingredients or structured_solution_signature(current_solutions) != EXPECTED_SOLUTIONS:
            raise ValueError("applied BSK repair no longer has the reviewed solution structure")
        return doc, False

    if ingredient_signature(current_ingredients) != PRE_INGREDIENTS:
        raise ValueError("normalized BSK ingredient signature drifted from the reviewed record")
    if solution_stub_signature(current_solutions) != PRE_SOLUTIONS:
        raise ValueError("normalized BSK solution-stub signature drifted from the reviewed record")

    _apply_identity_links(solutions, current_ingredients)
    solutions[0]["preparation_notes"] = (
        "Stir slowly at 4-10 C for 3 hours. Adjust to pH 7.6 with 5 M NaOH, then "
        "filter-sterilize."
    )
    solutions[1]["preparation_notes"] = (
        "Dissolve 14.0 g gelatin in 200 ml double-distilled water; autoclave for "
        "15 minutes at 115 C."
    )
    solutions[2]["preparation_notes"] = (
        "Dissolve 50.05 g bovine serum albumin fraction V (Sigma A9647) in 143 ml "
        "double-distilled water, or use Sigma A7409 BSA solution."
    )
    solutions[3].pop("preparation_notes", None)

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = []
    repaired["solutions"] = solutions
    repaired["ph_value"] = 7.6
    repaired["sterilization"] = {"method": "FILTER"}
    repaired["preparation_steps"] = [
        {
            "step_number": 1,
            "action": "HEAT",
            "description": "Warm Solutions A, B, C, and D to 37 C.",
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": (
                "Combine warm Solutions A, B, C, and D. Solution B may instead be "
                "added after filtration."
            ),
        },
        {
            "step_number": 3,
            "action": "FILTER_STERILIZE",
            "description": "Filter-sterilize the mixed medium while warm.",
        },
    ]
    repaired["notes"] = (
        "Source: https://togomedium.org/medium/M2366\n"
        "Original URL: "
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium403.pdf"
    )
    history = repaired.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("BSK curation_history is not a list")
    history.append(
        {
            "timestamp": "2026-08-25T00:00:00-07:00",
            "curator": "repair_togo_bsk_structure.py",
            "action": ACTION,
            "changes": "ingredients 19 -> 0; solution stubs 4 -> 4 inline solution recipes",
            "notes": (
                "Rebuilt TOGO M2366 from the checked-in TOGO payload and DSMZ Medium "
                "403. Restored Solutions A-D, bovine serum albumin, source units and "
                "preparation instructions; removed three unrelated LB constituents. "
                "Normalized the 1429 ml source batch to ml/L."
            ),
        }
    )
    return repaired, True


def load_payload(path: Path) -> dict[str, Any]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(rows, dict):
        rows = rows.get("data", [])
    for row in rows:
        gm_id = _value((row.get("meta") or {}).get("gm")).split("/")[-1]
        if gm_id == SOURCE_ID:
            return row
    raise ValueError(f"{path}: missing TOGO {SOURCE_ID}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-file", type=Path, default=RAW_FILE)
    parser.add_argument("--record", type=Path, default=NORMALIZED_FILE)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    payload = load_payload(args.raw_file)
    doc = yaml.safe_load(args.record.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise SystemExit(f"{args.record}: expected a YAML mapping")
    repaired, changed = repair_document(doc, payload)
    print(f"{'fix' if changed else 'skip':4s}  {args.record.relative_to(REPO)}: {SOURCE_ID}")
    if args.apply and changed:
        write_record(args.record, repaired)
    print(f"\n{'updated' if args.apply else 'would update'} {int(changed)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
