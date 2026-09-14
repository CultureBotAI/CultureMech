#!/usr/bin/env python3
"""Repair Archaeoglobus MCR parent-medium cross-references in the score-20 tier."""

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

CURATOR = "repair_archaeoglobus_mcr_score20.py"
ACTION = "RESOLVED_ARCHAEOGLOBUS_MCR_SCORE20"
LINK_ACTION = "LINKED_ARCHAEOGLOBUS_MCR_SCORE20_CHILDREN"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

TOGO_M1280 = "archaea/TOGO_M1280_Archaeoglobus_MCR_Medium.yaml"
JCM_J1195 = "archaea/archaeoglobus_mcr_medium.yaml"
TOGO_M1279 = "archaea/TOGO_M1279_Methanothermococcus_HHB_Medium.yaml"
JCM_J1194 = "archaea/methanothermococcus_hhb_medium.yaml"

TOGO_M1280_URL = "https://togomedium.org/medium/M1280"

EXPECTED_IDS = {
    TOGO_M1280: "CultureMech:007814",
    JCM_J1195: "CultureMech:002362",
    TOGO_M1279: "CultureMech:007812",
    JCM_J1194: "CultureMech:002361",
}
EXPECTED_SOURCE_TERMS = {
    TOGO_M1280: "TOGO:M1280",
    JCM_J1195: "mediadive.medium:J1195",
    TOGO_M1279: "TOGO:M1279",
    JCM_J1194: "mediadive.medium:J1194",
}

METHANOTHERMOCOCCUS_HHB = (
    "METHANOTHERMOCOCCUS HHB MEDIUM (see Medium [M1279])"
)
RELATIONSHIP = "SUPPLEMENTED_VARIANT"


@dataclass(frozen=True)
class ChildTarget:
    path: str
    parent_path: str
    parent_label: str
    notes: str
    solution_notes: str
    parent_notes: str
    variant_modification: str


TARGETS: tuple[ChildTarget, ...] = (
    ChildTarget(
        path=TOGO_M1280,
        parent_path=TOGO_M1279,
        parent_label="Methanothermococcus HHB Medium",
        notes=(
            "TOGO M1280 is a supplemented parent-medium cross-reference: "
            "one liter of TOGO M1279 Methanothermococcus HHB Medium "
            "supplemented with 2.8 g/L Na2SO4. The M1279 base remains a "
            "CultureMech parent-media link instead of being flattened into "
            "this record."
        ),
        solution_notes=(
            "TOGO M1280 uses one liter of TOGO M1279 Methanothermococcus HHB "
            "Medium as the base medium."
        ),
        parent_notes=(
            "TOGO M1280 uses TOGO M1279 Methanothermococcus HHB Medium and "
            "supplements it with 2.8 g/L Na2SO4."
        ),
        variant_modification=(
            "Supplements TOGO M1279 Methanothermococcus HHB Medium with "
            "2.8 g/L Na2SO4."
        ),
    ),
    ChildTarget(
        path=JCM_J1195,
        parent_path=JCM_J1194,
        parent_label="METHANOTHERMOCOCCUS HHB MEDIUM",
        notes=(
            "JCM Medium J1195 is a supplemented parent-medium "
            "cross-reference: one liter of JCM Medium J1194 "
            "Methanothermococcus HHB Medium supplemented with 2.8 g/L "
            "Na2SO4. CultureMech recovered the J1195 row from the "
            "source-equivalent TOGO M1280 snapshot and keeps the J1194 base "
            "as a CultureMech parent-media link instead of flattening it into "
            "this record."
        ),
        solution_notes=(
            "JCM Medium J1195 uses one liter of JCM Medium J1194 "
            "Methanothermococcus HHB Medium as the base medium; "
            "CultureMech recovered this J1195 row from the "
            "source-equivalent TOGO M1280 snapshot."
        ),
        parent_notes=(
            "JCM Medium J1195 uses JCM Medium J1194 Methanothermococcus HHB "
            "Medium and supplements it with 2.8 g/L Na2SO4; CultureMech "
            "recovered the J1195 row from the source-equivalent TOGO M1280 "
            "snapshot."
        ),
        variant_modification=(
            "Supplements JCM Medium J1194 Methanothermococcus HHB Medium "
            "with 2.8 g/L Na2SO4."
        ),
    ),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term") or {}
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _require_source(doc: dict[str, Any], path: str) -> None:
    if doc.get("id") != EXPECTED_IDS[path]:
        raise ValueError(
            f"{path}: found id {doc.get('id')!r}, expected {EXPECTED_IDS[path]!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[path]:
        raise ValueError(
            f"{path}: found source term {source_term!r}, "
            f"expected {EXPECTED_SOURCE_TERMS[path]!r}"
        )


def _require_child(doc: dict[str, Any], target: ChildTarget) -> None:
    _require_source(doc, target.path)

    sulfate_rows = [
        row
        for row in doc.get("ingredients") or []
        if isinstance(row, dict) and row.get("preferred_term") == "Na2SO4"
    ]
    if len(sulfate_rows) != 1:
        raise ValueError(f"{target.path}: expected exactly one Na2SO4 row")
    if sulfate_rows[0].get("concentration") != {
        "value": "2.8",
        "unit": "G_PER_L",
    }:
        raise ValueError(f"{target.path}: Na2SO4 concentration drifted")

    parent_media = doc.get("parent_media")
    if isinstance(parent_media, dict) and parent_media.get("id") == EXPECTED_IDS[
        target.parent_path
    ]:
        return

    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        if solution.get("preferred_term") == METHANOTHERMOCOCCUS_HHB:
            return
    raise ValueError(f"{target.path}: missing Methanothermococcus HHB base medium")


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
    components = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        nested = solution.get("composition") or []
        nested_components = (
            [row for row in nested if isinstance(row, dict)]
            if isinstance(nested, list)
            else []
        )
        components.extend(nested_components or [solution])
    return components


def _sodium_sulfate() -> dict[str, Any]:
    return {
        "preferred_term": "Na2SO4",
        "concentration": {"value": "2.8", "unit": "G_PER_L"},
        "source": "TOGO Medium M1280",
        "notes": (
            "TOGO M1280 supplements one liter of Methanothermococcus HHB "
            "Medium with 2.8 g/L Na2SO4."
        ),
        "term": _term("CHEBI:32149", "sodium sulfate"),
        "mediaingredientmech_chebi_term": _term("CHEBI:32149", "sodium sulfate"),
    }


def _parent_solution(target: ChildTarget, parent: dict[str, Any]) -> dict[str, Any]:
    return {
        "preferred_term": METHANOTHERMOCOCCUS_HHB,
        "composition": [],
        "concentration": {"value": "1", "unit": "L"},
        "notes": target.solution_notes,
        "culturemech_term": _term(str(parent.get("id") or ""), target.parent_label),
    }


def _recipe_ref(
    doc: dict[str, Any],
    path: str,
    relationship: str,
    notes: str,
) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": str(doc.get("id") or ""),
        "name": str(doc.get("name") or ""),
        "notes": notes,
    }


def _upsert_ref(refs: list[Any], new_ref: dict[str, str]) -> None:
    for index, existing in enumerate(refs):
        if not isinstance(existing, dict):
            continue
        if existing.get("path") == new_ref["path"]:
            refs[index] = new_ref
            return
    refs.append(new_ref)


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "needs_manual_curation",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")
    if any(_grounded(component) for component in _composition_components(doc)):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    has_unmapped = any(
        not _grounded(component) for component in _composition_components(doc)
    )
    if has_unmapped:
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    if flags:
        doc["data_quality_flags"] = list(dict.fromkeys(flags))
    else:
        doc.pop("data_quality_flags", None)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    if TOGO_M1280_URL not in found:
        references.append({"reference": TOGO_M1280_URL})


def _history(doc: dict[str, Any], path: str) -> list[Any]:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{path}: curation_history is not a list")
    return history


def _append_event(
    doc: dict[str, Any],
    *,
    path: str,
    action: str,
    changes: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "changes": changes,
        "source": TOGO_M1280_URL,
        "notes": notes,
    }
    history = _history(doc, path)
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def repair_child(
    doc: dict[str, Any],
    target: ChildTarget,
    parent: dict[str, Any],
) -> dict[str, Any]:
    _require_child(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = [_sodium_sulfate()]
    repaired["solutions"] = [_parent_solution(target, parent)]
    repaired["notes"] = target.notes
    repaired["parent_media"] = _recipe_ref(
        parent,
        target.parent_path,
        RELATIONSHIP,
        target.parent_notes,
    )
    repaired["variant_relationship"] = RELATIONSHIP
    repaired["variant_modifications"] = [target.variant_modification]
    repaired.pop("variant_children", None)

    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(
        repaired,
        path=target.path,
        action=ACTION,
        changes="Resolved Archaeoglobus MCR parent-medium cross-reference",
        notes=(
            "Grounded the Methanothermococcus HHB parent-medium wrapper and "
            "preserved the sparse supplemented-variant graph."
        ),
    )
    return repaired


def repair_parent(
    doc: dict[str, Any],
    parent_path: str,
    child_path: str,
    child: dict[str, Any],
    target: ChildTarget,
) -> dict[str, Any]:
    _require_source(doc, parent_path)

    repaired = copy.deepcopy(doc)
    children = repaired.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError(f"{parent_path}: variant_children is not a list")
    _upsert_ref(
        children,
        _recipe_ref(child, child_path, RELATIONSHIP, target.variant_modification),
    )
    children.sort(key=lambda row: row.get("path", "") if isinstance(row, dict) else "")
    _append_event(
        repaired,
        path=parent_path,
        action=LINK_ACTION,
        changes="Linked Archaeoglobus MCR child variant to its HHB base parent",
        notes=f"Added or refreshed reciprocal supplemented-variant link for {child_path}.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        parent = _load(normalized / target.parent_path)
        child = _load(normalized / target.path)

        repaired_child = repair_child(child, target, parent)
        repaired_parent = repair_parent(
            parent,
            target.parent_path,
            target.path,
            repaired_child,
            target,
        )

        plans[normalized / target.parent_path] = repaired_parent
        plans[normalized / target.path] = repaired_child

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
    sys.exit(main())
