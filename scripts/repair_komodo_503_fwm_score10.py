#!/usr/bin/env python3
"""Repair KOMODO 503 FWM exact strain child links."""

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

PARENT = Path("bacterial/fwm_medium.yaml")
PARENT_ID = "CultureMech:005678"
PARENT_NAME = "fwm_medium"
PARENT_SOURCE_TERM = "komodo.medium:503"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
SUPPLEMENTED_RELATIONSHIP = "SUPPLEMENTED_VARIANT"

INGREDIENT_SIGNATURE = (
    ("KH2PO4", "0.212314", "G_PER_L"),
    ("NH4Cl", "0.265393", "G_PER_L"),
    ("NaCl", "1.06157", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.424628", "G_PER_L"),
    ("KCl", "0.530786", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.159236", "G_PER_L"),
    ("Sodium resazurin", "0.000530786", "G_PER_L"),
    ("Na2CO3", "50", "G_PER_L"),
    ("D-Glucose", "250", "G_PER_L"),
    ("Na2S x 9 H2O", "30", "G_PER_L"),
    ("HCl", "2.5", "G_PER_L"),
    ("ZnCl2", "0.07", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("H3BO3", "0.006", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.19", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.002", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.024", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.036", "G_PER_L"),
    ("NaOH", "0.5", "G_PER_L"),
    ("Na2SeO3 x 5 H2O", "0.003", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.004", "G_PER_L"),
    ("p-Aminobenzoic acid", "0.08", "G_PER_L"),
    ("D-(+)-biotin", "0.02", "G_PER_L"),
    ("Calcium pantothenate", "0.1", "G_PER_L"),
)
H2SO4_ADJUSTED_INGREDIENT_SIGNATURE = INGREDIENT_SIGNATURE + (("H2SO4", "variable", "VARIABLE"),)
SOLUTION_COMPONENT_SIGNATURE = (
    (
        "Trace element solution SL-10",
        (("FeCl2 x 4 H2O", "1.5", "G_PER_L"),),
    ),
    (
        "Seven vitamins solution",
        (
            ("Vitamin B12", "0.1", "G_PER_L"),
            ("Nicotinic acid", "0.2", "G_PER_L"),
            ("Pyridoxine hydrochloride", "0.3", "G_PER_L"),
            ("Thiamine-HCl x 2 H2O", "0.2", "G_PER_L"),
        ),
    ),
)
PARENT_SOLUTION_VOLUME_SIGNATURE = (
    ("Trace element solution SL-10", ("1", "ML_PER_L"), ()),
    ("Seven vitamins solution", ("1", "ML_PER_L"), ()),
)
CHILD_SOLUTION_VOLUME_SIGNATURE = (
    (
        "Trace element solution SL-10",
        ("", ""),
        (("1", "ML_PER_L", "CROSS_MEDIUM_INFERENCE", "apply_cocktail_nesting.py"),),
    ),
    (
        "Seven vitamins solution",
        ("", ""),
        (("1", "ML_PER_L", "CROSS_MEDIUM_INFERENCE", "apply_cocktail_nesting.py"),),
    ),
)


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    notes: str
    relationship: str = STRAIN_RELATIONSHIP
    ingredient_signature: tuple[tuple[str, str, str], ...] = INGREDIENT_SIGNATURE


CHILDREN = (
    Child(
        Path("bacterial/for_dsm_5847.yaml"),
        "CultureMech:005669",
        "komodo.medium:503.1",
        "KOMODO Medium 503.1",
        "KOMODO Medium 503.1 applies KOMODO Medium 503 to DSM 5847.",
    ),
    Child(
        Path("bacterial/for_dsm_5849.yaml"),
        "CultureMech:005670",
        "komodo.medium:503.2",
        "KOMODO Medium 503.2",
        "KOMODO Medium 503.2 applies KOMODO Medium 503 to DSM 5849.",
    ),
    Child(
        Path("bacterial/for_dsm_5651.yaml"),
        "CultureMech:005671",
        "komodo.medium:503.3",
        "KOMODO Medium 503.3",
        "KOMODO Medium 503.3 applies KOMODO Medium 503 to DSM 5651.",
    ),
    Child(
        Path("bacterial/for_dsm_6779.yaml"),
        "CultureMech:005672",
        "komodo.medium:503.4",
        "KOMODO Medium 503.4",
        "KOMODO Medium 503.4 applies KOMODO Medium 503 to DSM 6779.",
    ),
    Child(
        Path("bacterial/for_dsm_11046.yaml"),
        "CultureMech:005673",
        "komodo.medium:503.5",
        "KOMODO Medium 503.5",
        "KOMODO Medium 503.5 applies KOMODO Medium 503 to DSM 11046.",
    ),
    Child(
        Path("bacterial/for_dsm_11261.yaml"),
        "CultureMech:005674",
        "komodo.medium:503.6",
        "KOMODO Medium 503.6",
        "KOMODO Medium 503.6 applies KOMODO Medium 503 to DSM 11261.",
    ),
    Child(
        Path("bacterial/for_dsm_11262.yaml"),
        "CultureMech:005675",
        "komodo.medium:503.7",
        "KOMODO Medium 503.7",
        "KOMODO Medium 503.7 applies KOMODO Medium 503 to DSM 11262.",
    ),
    Child(
        Path("bacterial/for_dsm_11263_and_dsm_11489.yaml"),
        "CultureMech:005676",
        "komodo.medium:503.8",
        "KOMODO Medium 503.8",
        "KOMODO Medium 503.8 applies KOMODO Medium 503 to DSM 11263 and DSM 11489.",
    ),
    Child(
        Path("bacterial/for_dsm_14424.yaml"),
        "CultureMech:005677",
        "komodo.medium:503.9",
        "KOMODO Medium 503.9",
        "KOMODO Medium 503.9 applies KOMODO Medium 503 to DSM 14424.",
    ),
    Child(
        Path("bacterial/for_dsm_15206.yaml"),
        "CultureMech:005661",
        "komodo.medium:503.11",
        "KOMODO Medium 503.11",
        "KOMODO Medium 503.11 applies KOMODO Medium 503 to DSM 15206.",
    ),
    Child(
        Path("bacterial/for_dsm_15970.yaml"),
        "CultureMech:005663",
        "komodo.medium:503.12",
        "KOMODO Medium 503.12",
        "KOMODO Medium 503.12 applies KOMODO Medium 503 to DSM 15970.",
    ),
    Child(
        Path("bacterial/for_dsm_15978.yaml"),
        "CultureMech:005664",
        "komodo.medium:503.13",
        "KOMODO Medium 503.13",
        "KOMODO Medium 503.13 applies KOMODO Medium 503 to DSM 15978.",
    ),
    Child(
        Path("bacterial/for_dsm_16082.yaml"),
        "CultureMech:005665",
        "komodo.medium:503.14",
        "KOMODO Medium 503.14",
        "KOMODO Medium 503.14 applies KOMODO Medium 503 to DSM 16082 with "
        "variable H2SO4 pH adjustment.",
        SUPPLEMENTED_RELATIONSHIP,
        H2SO4_ADJUSTED_INGREDIENT_SIGNATURE,
    ),
    Child(
        Path("bacterial/for_dsm_19636.yaml"),
        "CultureMech:005666",
        "komodo.medium:503.15",
        "KOMODO Medium 503.15",
        "KOMODO Medium 503.15 applies KOMODO Medium 503 to DSM 19636.",
    ),
    Child(
        Path("bacterial/for_dsm_21662.yaml"),
        "CultureMech:005667",
        "komodo.medium:503.16",
        "KOMODO Medium 503.16",
        "KOMODO Medium 503.16 applies KOMODO Medium 503 to DSM 21662.",
    ),
    Child(
        Path("bacterial/for_dsm_14691.yaml"),
        "CultureMech:005668",
        "komodo.medium:503.17",
        "KOMODO Medium 503.17",
        "KOMODO Medium 503.17 applies KOMODO Medium 503 to DSM 14691.",
    ),
    Child(
        Path("bacterial/medium_503_modified_for_dsm_11045.yaml"),
        "CultureMech:005658",
        "komodo.medium:503_11045",
        "KOMODO Medium 503_11045",
        "KOMODO Medium 503_11045 applies KOMODO Medium 503 to DSM 11045.",
    ),
    Child(
        Path("bacterial/medium_503_modified_for_dsm_11480.yaml"),
        "CultureMech:005659",
        "komodo.medium:503_11480",
        "KOMODO Medium 503_11480",
        "KOMODO Medium 503_11480 applies KOMODO Medium 503 to DSM 11480.",
    ),
    Child(
        Path("bacterial/medium_503_modified_for_dsm_11493.yaml"),
        "CultureMech:005660",
        "komodo.medium:503_11493",
        "KOMODO Medium 503_11493",
        "KOMODO Medium 503_11493 applies KOMODO Medium 503 to DSM 11493.",
    ),
    Child(
        Path("bacterial/medium_503_modified_for_dsm_12018.yaml"),
        "CultureMech:005662",
        "komodo.medium:503_12018",
        "KOMODO Medium 503_12018",
        "KOMODO Medium 503_12018 applies KOMODO Medium 503 to DSM 12018.",
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_CHILD_COUNT = 20

CURATOR = "repair_komodo_503_fwm_score10.py"
ACTION = "RESOLVED_KOMODO_503_FWM_TOPOLOGY"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    term = media_term.get("term") if isinstance(media_term, dict) else {}
    return str(term.get("id") or "") if isinstance(term, dict) else ""


def _concentration_signature(row: dict[str, Any]) -> tuple[str, str]:
    concentration = row.get("concentration") or {}
    if not isinstance(concentration, dict):
        concentration = {}
    return (
        str(concentration.get("value") or ""),
        str(concentration.get("unit") or ""),
    )


def _ingredient_row_signature(row: dict[str, Any]) -> tuple[str, str, str]:
    return (str(row.get("preferred_term") or ""), *_concentration_signature(row))


def _ingredient_signature(doc: dict[str, Any]) -> tuple[tuple[str, str, str], ...]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")

    return tuple(_ingredient_row_signature(row) for row in ingredients if isinstance(row, dict))


def _solution_component_signature(
    doc: dict[str, Any],
) -> tuple[tuple[str, tuple[tuple[str, str, str], ...]], ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signature: list[tuple[str, tuple[tuple[str, str, str], ...]]] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            continue
        composition = solution.get("composition") or []
        if not isinstance(composition, list):
            raise ValueError("solution composition is not a list")
        signature.append(
            (
                str(solution.get("preferred_term") or ""),
                tuple(
                    _ingredient_row_signature(row) for row in composition if isinstance(row, dict)
                ),
            )
        )
    return tuple(signature)


def _candidate_signature(candidate: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(candidate.get("value") or ""),
        str(candidate.get("unit") or ""),
        str(candidate.get("basis") or ""),
        str(candidate.get("proposed_by") or ""),
    )


def _solution_volume_signature(
    doc: dict[str, Any],
) -> tuple[tuple[str, tuple[str, str], tuple[tuple[str, str, str, str], ...]], ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signature: list[tuple[str, tuple[str, str], tuple[tuple[str, str, str, str], ...]]] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            continue
        candidates = solution.get("concentration_candidates") or []
        if not isinstance(candidates, list):
            raise ValueError("solution concentration_candidates is not a list")
        signature.append(
            (
                str(solution.get("preferred_term") or ""),
                _concentration_signature(solution),
                tuple(
                    _candidate_signature(candidate)
                    for candidate in candidates
                    if isinstance(candidate, dict)
                ),
            )
        )
    return tuple(signature)


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value
    doc.clear()
    doc.update(updated)


def _upsert_event(doc: dict[str, Any], event: dict[str, Any]) -> None:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == event["curator"]
            and existing.get("action") == event["action"]
        ):
            history[index] = event
            return
    history.append(event)


def _ensure_ingredients_curated(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")


def _validate_targets() -> None:
    if len(CHILDREN) != EXPECTED_CHILD_COUNT or len(CHILDREN) != len(CHILD_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_CHILD_COUNT} unique children, found "
            f"{len(CHILDREN)} total and {len(CHILD_BY_PATH)} unique"
        )


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": child.relationship,
        "id": child.record_id,
        "name": child.path.stem,
        "notes": child.notes,
    }


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": child.relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": child.notes,
    }


def _require_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
    ingredient_signature: tuple[tuple[str, str, str], ...],
    solution_volume_signature: tuple[
        tuple[str, tuple[str, str], tuple[tuple[str, str, str, str], ...]], ...
    ],
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if _ingredient_signature(doc) != ingredient_signature:
        raise ValueError(f"{relative_path}: ingredient signature drifted")
    if _solution_component_signature(doc) != SOLUTION_COMPONENT_SIGNATURE:
        raise ValueError(f"{relative_path}: solution component signature drifted")
    if _solution_volume_signature(doc) != solution_volume_signature:
        raise ValueError(f"{relative_path}: solution volume evidence drifted")


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(
        doc,
        PARENT,
        PARENT_ID,
        PARENT_SOURCE_TERM,
        INGREDIENT_SIGNATURE,
        PARENT_SOLUTION_VOLUME_SIGNATURE,
    )


def _require_child(child: Child, doc: dict[str, Any]) -> None:
    _require_record(
        doc,
        child.path,
        child.record_id,
        child.source_term,
        child.ingredient_signature,
        CHILD_SOLUTION_VOLUME_SIGNATURE,
    )


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_parent(doc)

    repaired = copy.deepcopy(doc)
    repaired.pop("parent_media", None)
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "variant_children",
        [_child_entry(child) for child in CHILDREN],
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked KOMODO Medium 503 exact and H2SO4-adjusted DSM strain wrappers",
            "source": "KOMODO Medium 503, exact 503 strain wrappers, and KOMODO Medium 503.14",
            "notes": (
                "Included KOMODO Medium 503.14 as a supplemented pH-adjustment "
                "variant because its post-nesting signature is the base FWM "
                "signature plus variable H2SO4."
            ),
        },
    )
    return repaired


def repair_child(relative_path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    child = CHILD_BY_PATH.get(relative_path)
    if child is None:
        raise ValueError(f"unexpected child path {relative_path}")
    _require_child(child, doc)

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", child.relationship, "parent_media")
    _put_after(repaired, "variant_modifications", [child.notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO Medium 503 as STRAIN_SPECIFIC_VARIANT",
            "source": child.source_label,
            "notes": child.notes,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    plans = {normalized / PARENT: repair_parent(_load(normalized / PARENT))}
    for child in CHILDREN:
        plans[normalized / child.path] = repair_child(
            child.path,
            _load(normalized / child.path),
        )
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
