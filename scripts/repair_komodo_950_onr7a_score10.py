#!/usr/bin/env python3
"""Repair KOMODO 950 ONR7a strain and replacement child links."""

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

PARENT = Path("bacterial/KOMODO_950_ONR7a_MEDIUM.yaml")
PARENT_ID = "CultureMech:006893"
PARENT_NAME = "onr7a_medium"
PARENT_SOURCE_TERM = "komodo.medium:950"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
SUBSTITUTED_RELATIONSHIP = "SUBSTITUTED_COMPONENT_VARIANT"

INGREDIENT_SIGNATURE = (
    ("NaCl", "45.58", "G_PER_L"),
    ("Na2SO4", "7.96", "G_PER_L"),
    ("KCl", "1.44", "G_PER_L"),
    ("NaBr", "0.166", "G_PER_L"),
    ("NaHCO3", "0.062", "G_PER_L"),
    ("H3BO3", "0.054", "G_PER_L"),
    ("NaF", "0.0052", "G_PER_L"),
    ("NH4Cl", "0.54", "G_PER_L"),
    ("Na2HPO4 x 7 H2O", "0.178", "G_PER_L"),
    ("TAPSO", "2.6", "G_PER_L"),
    ("Agar", "30", "G_PER_L"),
    ("Agarose", "24", "G_PER_L"),
    ("MgCl2 x 6 H2O", "24.8444", "G_PER_L"),
    ("CaCl2 x 2 H2O", "3.24444", "G_PER_L"),
    ("SrCl2 x 6 H2O", "0.0533333", "G_PER_L"),
    ("FeCl2 x 4 H2O", "0.04", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
)


@dataclass(frozen=True)
class StrainChild:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    target: str


@dataclass(frozen=True)
class SubstitutedChild:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    target: str
    replaced: str
    replacement: str


STRAIN_CHILDREN = (
    StrainChild(
        Path("bacterial/dsm_13489.yaml"),
        "CultureMech:006889",
        "komodo.medium:950.1",
        "KOMODO Medium 950.1",
        "DSM 13489",
    ),
    StrainChild(
        Path("bacterial/dsm_14919.yaml"),
        "CultureMech:006892",
        "komodo.medium:950.2",
        "KOMODO Medium 950.2",
        "DSM 14919",
    ),
)
SUBSTITUTED_CHILDREN = (
    SubstitutedChild(
        Path("bacterial/dsm_14919_replace_sodium_acetate_with_tetradecane.yaml"),
        "CultureMech:006891",
        "komodo.medium:950.2_replace_Sodium acetate_with_tetradecane",
        "KOMODO Medium 950.2_replace_Sodium acetate_with_tetradecane",
        "DSM 14919",
        "Sodium acetate",
        "tetradecane",
    ),
    SubstitutedChild(
        Path("bacterial/dsm_14919_replace_sodium_acetate_with_tween_80.yaml"),
        "CultureMech:006890",
        "komodo.medium:950.2_replace_Sodium acetate_with_Tween 80",
        "KOMODO Medium 950.2_replace_Sodium acetate_with_Tween 80",
        "DSM 14919",
        "Sodium acetate",
        "Tween 80",
    ),
)
STRAIN_CHILD_BY_PATH = {child.path: child for child in STRAIN_CHILDREN}
SUBSTITUTED_CHILD_BY_PATH = {child.path: child for child in SUBSTITUTED_CHILDREN}
EXPECTED_STRAIN_CHILD_COUNT = 2
EXPECTED_SUBSTITUTED_CHILD_COUNT = 2

CURATOR = "repair_komodo_950_onr7a_score10.py"
ACTION = "RESOLVED_KOMODO_950_ONR7A_TOPOLOGY"
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


def _ingredient_signature(doc: dict[str, Any]) -> tuple[tuple[str, str, str], ...]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")

    signature: list[tuple[str, str, str]] = []
    for row in ingredients:
        if not isinstance(row, dict):
            continue
        concentration = row.get("concentration") or {}
        if not isinstance(concentration, dict):
            concentration = {}
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
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
    if len(STRAIN_CHILDREN) != EXPECTED_STRAIN_CHILD_COUNT or len(
        STRAIN_CHILDREN
    ) != len(STRAIN_CHILD_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_STRAIN_CHILD_COUNT} unique strain children, "
            f"found {len(STRAIN_CHILDREN)} total and {len(STRAIN_CHILD_BY_PATH)} unique"
        )
    if len(SUBSTITUTED_CHILDREN) != EXPECTED_SUBSTITUTED_CHILD_COUNT or len(
        SUBSTITUTED_CHILDREN
    ) != len(SUBSTITUTED_CHILD_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_SUBSTITUTED_CHILD_COUNT} unique substituted "
            f"children, found {len(SUBSTITUTED_CHILDREN)} total and "
            f"{len(SUBSTITUTED_CHILD_BY_PATH)} unique"
        )


def _strain_notes(child: StrainChild) -> str:
    return f"{child.source_label} applies ONR7a medium to {child.target}."


def _substitution_notes(child: SubstitutedChild) -> str:
    return (
        f"{child.source_label} records a {child.target} ONR7a derivative with "
        f"{child.replaced} replaced by {child.replacement}."
    )


def _child_entry(
    child: StrainChild | SubstitutedChild,
    relationship: str,
    notes: str,
) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": relationship,
        "id": child.record_id,
        "name": child.path.stem,
        "notes": notes,
    }


def _parent_ref(relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": notes,
    }


def _require_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)


def _require_strain_child(child: StrainChild, doc: dict[str, Any]) -> None:
    _require_record(doc, child.path, child.record_id, child.source_term)


def _require_substituted_child(
    child: SubstitutedChild,
    doc: dict[str, Any],
) -> None:
    _require_record(doc, child.path, child.record_id, child.source_term)


def _strain_entry(child: StrainChild) -> dict[str, str]:
    return _child_entry(child, STRAIN_RELATIONSHIP, _strain_notes(child))


def _substitution_entry(child: SubstitutedChild) -> dict[str, str]:
    return _child_entry(
        child,
        SUBSTITUTED_RELATIONSHIP,
        _substitution_notes(child),
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
        [
            *[_strain_entry(child) for child in STRAIN_CHILDREN],
            *[_substitution_entry(child) for child in SUBSTITUTED_CHILDREN],
        ],
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Resolved KOMODO Medium 950 ONR7a child topology",
            "source": (
                "KOMODO Medium 950.1, 950.2, "
                "950.2_replace_Sodium acetate_with_tetradecane, and "
                "950.2_replace_Sodium acetate_with_Tween 80"
            ),
            "notes": (
                "Moved exact-signature DSM-specific KOMODO 950 ONR7a wrappers and "
                "source-token sodium acetate replacement variants under the KOMODO "
                "Medium 950 ONR7a base."
            ),
        },
    )
    return repaired


def repair_strain_child(relative_path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    child = STRAIN_CHILD_BY_PATH.get(relative_path)
    if child is None:
        raise ValueError(f"unexpected strain child path {relative_path}")
    _require_strain_child(child, doc)

    notes = _strain_notes(child)
    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "parent_media",
        _parent_ref(STRAIN_RELATIONSHIP, notes),
        "curation_history",
    )
    _put_after(repaired, "variant_relationship", STRAIN_RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked as a KOMODO Medium 950 strain-specific variant",
            "source": child.source_label,
            "notes": notes,
        },
    )
    return repaired


def repair_substituted_child(
    relative_path: Path,
    doc: dict[str, Any],
) -> dict[str, Any]:
    child = SUBSTITUTED_CHILD_BY_PATH.get(relative_path)
    if child is None:
        raise ValueError(f"unexpected substituted child path {relative_path}")
    _require_substituted_child(child, doc)

    notes = _substitution_notes(child)
    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "parent_media",
        _parent_ref(SUBSTITUTED_RELATIONSHIP, notes),
        "curation_history",
    )
    _put_after(
        repaired,
        "variant_relationship",
        SUBSTITUTED_RELATIONSHIP,
        "parent_media",
    )
    _put_after(repaired, "variant_modifications", [notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked as a KOMODO Medium 950 source-token substitution variant",
            "source": child.source_label,
            "notes": notes,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    plans = {normalized / PARENT: repair_parent(_load(normalized / PARENT))}
    for child in STRAIN_CHILDREN:
        plans[normalized / child.path] = repair_strain_child(
            child.path,
            _load(normalized / child.path),
        )
    for child in SUBSTITUTED_CHILDREN:
        plans[normalized / child.path] = repair_substituted_child(
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
