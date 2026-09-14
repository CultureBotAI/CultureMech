#!/usr/bin/env python3
"""Repair KOMODO 1199 K7 medium and its DSM-specific pH variants."""

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

KOMODO_1199_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1199"
)
KOMODO_1199_1_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1199.1"
)
KOMODO_1199_2_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1199.2"
)

CURATOR = "repair_komodo_1199_ph_variants_score20.py"
ACTION = "RESOLVED_KOMODO_1199_PH_VARIANTS_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
SOURCE_1199 = "KOMODO Medium 1199"
SOURCE_1199_1 = "KOMODO Medium 1199.1"
SOURCE_1199_2 = "KOMODO Medium 1199.2"


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    media_term_id: str
    source_url: str
    source_label: str
    ph_value: float | None = None


TARGETS: tuple[Target, ...] = (
    Target(
        "bacterial/KOMODO_1199_K7_medium.yaml",
        "CultureMech:003938",
        "komodo.medium:1199",
        KOMODO_1199_URL,
        SOURCE_1199,
    ),
    Target(
        "bacterial/for_dsm_19966.yaml",
        "CultureMech:003936",
        "komodo.medium:1199.1",
        KOMODO_1199_1_URL,
        SOURCE_1199_1,
        5.5,
    ),
    Target(
        "bacterial/for_dsm_25088.yaml",
        "CultureMech:003937",
        "komodo.medium:1199.2",
        KOMODO_1199_2_URL,
        SOURCE_1199_2,
        6.5,
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}
PARENT_PATH = "data/normalized_yaml/bacterial/KOMODO_1199_K7_medium.yaml"
PARENT_ID = "CultureMech:003938"
PARENT_NAME = "k7_medium"


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    *,
    source: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "source": source,
        "notes": f"{source} lists {value} g/L {preferred_term}.",
        "concentration": {"value": value, "unit": "G_PER_L"},
    }
    if term is not None:
        row["term"] = _term(*term)
        row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _recipe(source: str) -> list[dict[str, Any]]:
    return [
        _ingredient("Yeast extract", "1", source=source),
        {
            "preferred_term": "Distilled water",
            "source": source,
            "notes": f"{source} lists distilled water with null gram and molar amounts.",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "term": _term("CHEBI:15377", "water"),
            "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
        },
        _ingredient(
            "Glucose",
            "1",
            source=source,
            term=("CHEBI:17234", "glucose"),
        ),
        _ingredient("Peptone", "1", source=source),
    ]


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


def _component_names(doc: dict[str, Any]) -> tuple[str, ...]:
    return tuple(
        str(row.get("preferred_term") or "")
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    )


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )
    source_term = _source_term_id(doc)
    if source_term != target.media_term_id:
        raise ValueError(
            f"{target.path}: expected source term {target.media_term_id}, "
            f"found {source_term!r}"
        )
    if _component_names(doc) not in (
        ("Glucose", "Yeast extract", "Peptone"),
        ("Yeast extract", "Distilled water", "Glucose", "Peptone"),
    ):
        raise ValueError(f"{target.path}: K7 ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    for flag in ("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_reference(doc: dict[str, Any], url: str) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    if url not in existing:
        references.append({"reference": url})


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    if target.ph_value is None:
        notes = (
            f"{target.source_label} defines the K7 medium base table with 1 g/L "
            "each of yeast extract, glucose, and peptone plus distilled water."
        )
    else:
        notes = (
            f"{target.source_label} is a pH {target.ph_value:g} K7 medium variant "
            "for the named DSM strain and has the same KOMODO metabolite table."
        )
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": target.source_url,
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


def _child_entry(child: Target) -> dict[str, Any]:
    name = Path(child.path).stem
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": "PH_VARIANT",
        "id": child.record_id,
        "name": name,
        "notes": (
            f"{child.source_label} keeps the KOMODO Medium 1199 metabolite table "
            f"but specifies pH {child.ph_value:g}."
        ),
    }


def _repair_parent(doc: dict[str, Any], target: Target) -> None:
    doc["variant_children"] = [_child_entry(child) for child in TARGETS[1:]]


def _repair_child(doc: dict[str, Any], target: Target) -> None:
    doc["parent_media"] = {
        "path": PARENT_PATH,
        "relationship": "PH_VARIANT",
        "id": PARENT_ID,
        "name": PARENT_NAME,
    }
    doc["variant_relationship"] = "PH_VARIANT"
    doc["variant_modifications"] = [
        f"{target.source_label} specifies pH {target.ph_value:g} for this DSM-specific K7 variant."
    ]
    doc["ph_value"] = target.ph_value


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = _recipe(target.source_label)
    _ensure_flags(repaired)
    _ensure_reference(repaired, target.source_url)
    if target.ph_value is None:
        _repair_parent(repaired, target)
    else:
        _repair_child(repaired, target)
    _ensure_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
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
