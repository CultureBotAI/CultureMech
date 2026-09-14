#!/usr/bin/env python3
"""Repair KOMODO 853 Fusibacter child and duplicate links."""

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

PARENT = Path("bacterial/fusibacter_paucivorans_medium.yaml")
PARENT_ID = "CultureMech:006670"
PARENT_NAME = "fusibacter_paucivorans_medium"
PARENT_SOURCE_TERM = "komodo.medium:853"
PARENT_PH = 7.3

STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"
CONCENTRATION_RELATIONSHIP = "CONCENTRATION_VARIANT"


def _signature(nacl: str) -> tuple[tuple[str, str, str], ...]:
    return (
        ("NH4Cl", "0.990099", "G_PER_L"),
        ("K2HPO4", "0.29703", "G_PER_L"),
        ("KH2PO4", "0.29703", "G_PER_L"),
        ("MgCl2 x 6 H2O", "2.9703", "G_PER_L"),
        ("CaCl2 x 2 H2O", "0.19900990000000002", "G_PER_L"),
        ("KCl", "0.990099", "G_PER_L"),
        ("NaCl", nacl, "G_PER_L"),
        ("Yeast extract", "0.990099", "G_PER_L"),
        ("Trypticase peptone", "0.990099", "G_PER_L"),
        ("Na-acetate x 3 H2O", "0.49505", "G_PER_L"),
        ("Sodium resazurin", "0.00049505", "G_PER_L"),
        ("Na2S2O3 x 5 H2O", "3.12871", "G_PER_L"),
        ("L-Cysteine HCl x H2O", "0.49505", "G_PER_L"),
        ("Na2CO3", "1.48515", "G_PER_L"),
        ("D-Glucose", "3.56436", "G_PER_L"),
        ("Na2S x 9 H2O", "0.29703", "G_PER_L"),
        ("Nitrilotriacetic acid", "1.5", "G_PER_L"),
        ("MgSO4 x 7 H2O", "3", "G_PER_L"),
        ("MnSO4 x H2O", "0.5", "G_PER_L"),
        ("FeSO4 x 7 H2O", "0.1", "G_PER_L"),
        ("CoSO4 x 7 H2O", "0.18", "G_PER_L"),
        ("ZnSO4 x 7 H2O", "0.18", "G_PER_L"),
        ("CuSO4 x 5 H2O", "0.01", "G_PER_L"),
        ("AlK(SO4)2 x 12 H2O", "0.02", "G_PER_L"),
        ("H3BO3", "0.01", "G_PER_L"),
        ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
        ("NiCl2 x 6 H2O", "0.03", "G_PER_L"),
        ("Na2SeO3 x 5 H2O", "0.0003", "G_PER_L"),
        ("Na2WO4 x 2 H2O", "0.0004", "G_PER_L"),
    )


PARENT_SIGNATURE = _signature("70.3069")
LOW_NACL_SIGNATURE = _signature("30.703")


@dataclass(frozen=True)
class Variant:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    relationship: str
    signature: tuple[tuple[str, str, str], ...]
    ph_value: float | None = None
    ph_range: dict[str, float] | None = None


STRAIN_CHILD = Variant(
    Path("bacterial/for_dsm_24436.yaml"),
    "CultureMech:006669",
    "komodo.medium:853.1",
    "KOMODO Medium 853.1",
    STRAIN_RELATIONSHIP,
    PARENT_SIGNATURE,
    ph_value=7.3,
)

VARIANTS = (
    STRAIN_CHILD,
    Variant(
        Path("bacterial/fusibacter_tunisiensis_medium.yaml"),
        "CultureMech:002011",
        "mediadive.medium:853a",
        "DSMZ Medium 853a",
        SOURCE_DUPLICATE_RELATIONSHIP,
        PARENT_SIGNATURE,
        ph_range={"min": 7.2, "max": 7.4},
    ),
    Variant(
        Path("bacterial/fusibacter_medium.yaml"),
        "CultureMech:002010",
        "mediadive.medium:853",
        "DSMZ Medium 853",
        CONCENTRATION_RELATIONSHIP,
        LOW_NACL_SIGNATURE,
        ph_range={"min": 7.2, "max": 7.4},
    ),
)
VARIANT_BY_PATH = {variant.path: variant for variant in VARIANTS}
EXPECTED_VARIANT_COUNT = 3

CURATOR = "repair_komodo_853_fusibacter_score10.py"
ACTION = "RESOLVED_KOMODO_853_FUSIBACTER_TOPOLOGY"
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
    if len(VARIANTS) != EXPECTED_VARIANT_COUNT or len(VARIANTS) != len(VARIANT_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_VARIANT_COUNT} unique variants, found "
            f"{len(VARIANTS)} total and {len(VARIANT_BY_PATH)} unique"
        )


def _variant_notes(variant: Variant) -> str:
    if variant.relationship == STRAIN_RELATIONSHIP:
        return f"{variant.source_label} applies FUSIBACTER PAUCIVORANS medium to DSM 24436."
    if variant.relationship == CONCENTRATION_RELATIONSHIP:
        return (
            f"{variant.source_label} shares the KOMODO Medium 853 ingredient "
            "set with 30.703 g/L NaCl instead of 70.3069 g/L."
        )
    return (
        f"{variant.source_label} has the same high-salt 29-component "
        "Fusibacter signature as KOMODO Medium 853."
    )


def _variant_entry(variant: Variant) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{variant.path}",
        "relationship": variant.relationship,
        "id": variant.record_id,
        "name": variant.path.stem,
        "notes": _variant_notes(variant),
    }


def _parent_ref(variant: Variant) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": variant.relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": _variant_notes(variant),
    }


def _require_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
    signature: tuple[tuple[str, str, str], ...],
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if _ingredient_signature(doc) != signature:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM, PARENT_SIGNATURE)
    if doc.get("ph_value") != PARENT_PH:
        raise ValueError(f"{PARENT}: expected pH {PARENT_PH!r}")


def _require_variant(variant: Variant, doc: dict[str, Any]) -> None:
    _require_record(doc, variant.path, variant.record_id, variant.source_term, variant.signature)
    if variant.ph_value is not None and doc.get("ph_value") != variant.ph_value:
        raise ValueError(f"{variant.path}: expected pH {variant.ph_value!r}")
    if variant.ph_range is not None and doc.get("ph_range") != variant.ph_range:
        raise ValueError(f"{variant.path}: expected pH range {variant.ph_range!r}")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_parent(doc)

    repaired = copy.deepcopy(doc)
    repaired.pop("parent_media", None)
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
    _put_after(
        repaired,
        "variant_children",
        [_variant_entry(variant) for variant in VARIANTS],
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Promoted KOMODO Medium 853 as the Fusibacter parent",
            "source": "KOMODO Medium 853 and 853.1; DSMZ Media 853 and 853a",
            "notes": (
                "Moved KOMODO Medium 853.1 and DSMZ Medium 853a under the "
                "KOMODO Medium 853 Fusibacter base and kept DSMZ Medium 853 "
                "as a lower-NaCl concentration variant."
            ),
        },
    )
    return repaired


def repair_variant(relative_path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    variant = VARIANT_BY_PATH.get(relative_path)
    if variant is None:
        raise ValueError(f"unexpected variant path {relative_path}")
    _require_variant(variant, doc)

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(variant), "curation_history")
    _put_after(repaired, "variant_relationship", variant.relationship, "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [_variant_notes(variant)],
        "variant_relationship",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO Medium 853",
            "source": variant.source_label,
            "notes": _variant_notes(variant),
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    plans = {normalized / PARENT: repair_parent(_load(normalized / PARENT))}
    for variant in VARIANTS:
        plans[normalized / variant.path] = repair_variant(
            variant.path,
            _load(normalized / variant.path),
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
