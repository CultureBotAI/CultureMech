#!/usr/bin/env python3
"""Restore stock-solution boundaries for MediaDive J935 and J1053.

The legacy MediaDive importer traversed every solution attached to a medium and
flattened each stock's internal recipe into the final ``ingredients`` list. Three
malformed upstream rows also carried an empty compound label. Deduplication later
summed the two blank J935 additions (5 + 20 ml) into one unnamed 25 g/L row.

The checked-in MediaDive API payload retains the primary recipe, stock references,
and addition volumes. The JCM source pages independently show the same formulation:

* https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=935
* https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1053

This migration keeps the already curated direct-ingredient rows, removes the
flattened stock contents, and rebuilds ``solutions`` from the primary API recipe.
It is dry-run by default and refuses source or record shapes outside the two
reviewed signatures.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import write_record  # noqa: E402

MediaDiveImporter = import_module("culturemech.import.mediadive_importer").MediaDiveImporter

NORMALIZED = REPO / "data" / "normalized_yaml"
API_FILE = REPO / "data" / "raw" / "mediadive_api" / "mediadive_api_media.json"


@dataclass(frozen=True)
class Target:
    path: str
    direct_ingredients: tuple[str, ...]
    solutions: tuple[tuple[str, str, str | None], ...]
    merged_blank_value: str


TARGETS = {
    "J935": Target(
        path="archaea/fervidicoccus_fontis_medium.yaml",
        direct_ingredients=(
            "NH4Cl",
            "KH2PO4",
            "KCl",
            "CaCl2 x 2 H2O",
            "MgCl2 x 6 H2O",
            "NaCl",
            "NaHCO3",
            "Resazurin",
        ),
        solutions=(
            ("FeCl2 solution", "1", "mediadive.solution:3846"),
            ("Trace element solution", "1", "mediadive.solution:3847"),
            ("10% (w/v) Yeast extract (BD-Difco) solution", "5", None),
            ("10% (w/v) Trypticase peptone (BD-BBL) solution", "20", None),
            ("Trace vitamins", "10", "mediadive.solution:3861"),
            ("5% (w/v) Na2S x 9 H2O solution", "10", None),
        ),
        merged_blank_value="25.0",
    ),
    "J1053": Target(
        path="bacterial/deferrisoma_paleochrorii_medium.yaml",
        direct_ingredients=(
            "NaCl",
            "MgCl2 x 6 H2O",
            "KCl",
            "CaCl2 x 2 H2O",
            "(NH4)2SO4",
        ),
        solutions=(
            ("FeCl2 solution", "1", "mediadive.solution:3846"),
            ("Trace element solution", "1", "mediadive.solution:3847"),
            ("Selenite-tungstate solution", "0.5", "mediadive.solution:4172"),
            ("3.3% KH2PO4 solution", "10", None),
            ("Trace vitamins", "10", "mediadive.solution:3861"),
            ("8% NaHCO3 solution", "10", None),
            ("20% (w/v) MES (pH 6.0) solution", "10", None),
            ("Iron(III) citrate solution", "100", "mediadive.solution:5059"),
        ),
        merged_blank_value="10",
    ),
}


def media_term_id(doc: dict[str, Any]) -> str:
    return str((((doc.get("media_term") or {}).get("term") or {}).get("id")) or "")


def solution_signature(solution: dict[str, Any]) -> tuple[str, str, str | None]:
    concentration = solution.get("concentration") or {}
    term = solution.get("term") or {}
    return (
        str(solution.get("preferred_term") or ""),
        str(concentration.get("value") or ""),
        str(term.get("id")) if term.get("id") else None,
    )


def _importer_for(payload: dict[str, Any]) -> Any:
    importer = MediaDiveImporter.__new__(MediaDiveImporter)
    importer.mediadive_dir = REPO / "data" / "raw" / "mediadive"
    importer.ingredients_by_name = {}
    importer._api_data_cache = {"data": [payload]}
    return importer


def repair_document(
    doc: dict[str, Any], payload: dict[str, Any], source_id: str
) -> tuple[dict[str, Any], bool]:
    """Return a guarded repaired copy and whether it differs from an applied record."""
    target = TARGETS[source_id]
    expected_term = f"mediadive.medium:{source_id}"
    if media_term_id(doc) != expected_term:
        raise ValueError(f"{target.path}: expected {expected_term}, found {media_term_id(doc)!r}")
    payload_id = str((payload.get("medium") or {}).get("id") or "")
    if payload_id != source_id:
        raise ValueError(f"{target.path}: API payload id is {payload_id!r}, expected {source_id}")

    importer = _importer_for(payload)
    parsed_ingredients = importer._parse_api_composition(source_id) or []
    parsed_solutions = importer._parse_api_solutions(source_id) or []
    parsed_names = tuple(str(row.get("preferred_term") or "") for row in parsed_ingredients)
    parsed_solution_signatures = tuple(solution_signature(row) for row in parsed_solutions)
    if parsed_names != target.direct_ingredients:
        raise ValueError(f"{target.path}: direct-ingredient signature drifted: {parsed_names!r}")
    if parsed_solution_signatures != target.solutions:
        raise ValueError(
            f"{target.path}: stock-solution signature drifted: " f"{parsed_solution_signatures!r}"
        )

    current_ingredients = [row for row in (doc.get("ingredients") or []) if isinstance(row, dict)]
    current_names = tuple(str(row.get("preferred_term") or "") for row in current_ingredients)
    current_solution_signatures = tuple(
        solution_signature(row) for row in (doc.get("solutions") or []) if isinstance(row, dict)
    )
    if (
        current_names == target.direct_ingredients
        and current_solution_signatures == target.solutions
    ):
        return doc, False
    if doc.get("solutions"):
        raise ValueError(f"{target.path}: unexpected pre-existing solutions block")

    blank_rows = [
        row for row in current_ingredients if not str(row.get("preferred_term") or "").strip()
    ]
    if len(blank_rows) != 1:
        raise ValueError(f"{target.path}: expected exactly one merged blank row")
    blank_value = str((blank_rows[0].get("concentration") or {}).get("value") or "")
    if blank_value != target.merged_blank_value:
        raise ValueError(
            f"{target.path}: expected merged blank value {target.merged_blank_value}, "
            f"found {blank_value!r}"
        )

    rows_by_name: dict[str, list[dict[str, Any]]] = {}
    for row in current_ingredients:
        rows_by_name.setdefault(str(row.get("preferred_term") or ""), []).append(row)
    kept: list[dict[str, Any]] = []
    for name in target.direct_ingredients:
        matches = rows_by_name.get(name, [])
        if len(matches) != 1:
            raise ValueError(
                f"{target.path}: expected one existing {name!r} row, found {len(matches)}"
            )
        kept.append(copy.deepcopy(matches[0]))

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = kept
    repaired["solutions"] = copy.deepcopy(parsed_solutions)
    history = repaired.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.path}: curation_history is not a list")
    history.append(
        {
            "timestamp": "2026-08-25T00:00:00-07:00",
            "curator": "repair_mediadive_jcm_structure.py",
            "action": "RESTORED_STOCK_SOLUTION_BOUNDARIES",
            "changes": (
                f"ingredients {len(current_ingredients)} -> {len(kept)}; "
                f"added {len(parsed_solutions)} source-asserted stock additions"
            ),
            "notes": (
                f"Rebuilt {source_id} from the checked-in MediaDive API primary recipe "
                f"and JCM GRMD {source_id.removeprefix('J')}. Removed stock-strength "
                "components flattened into final ingredients and restored each stock's "
                "asserted ml/L addition volume."
            ),
        }
    )
    return repaired, True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--api-file", type=Path, default=API_FILE)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    api = json.loads(args.api_file.read_text(encoding="utf-8"))
    payloads = {
        str((row.get("medium") or {}).get("id") or ""): row for row in (api.get("data") or [])
    }

    plans: list[tuple[Path, dict[str, Any]]] = []
    for source_id, target in TARGETS.items():
        if source_id not in payloads:
            raise SystemExit(f"API payload missing {source_id}")
        path = args.normalized_dir / target.path
        try:
            import yaml

            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise SystemExit(f"Could not load {path}: {exc}") from exc
        if not isinstance(doc, dict):
            raise SystemExit(f"{path}: expected a YAML mapping")
        repaired, changed = repair_document(doc, payloads[source_id], source_id)
        status = "fix" if changed else "skip"
        print(f"{status:4s}  {target.path}: {source_id}")
        if changed:
            plans.append((path, repaired))

    if args.apply:
        for path, repaired in plans:
            write_record(path, repaired)
    mode = "updated" if args.apply else "would update"
    print(f"\n{mode} {len(plans)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
