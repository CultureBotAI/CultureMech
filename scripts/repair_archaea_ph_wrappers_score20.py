#!/usr/bin/env python3
"""Repair score-20 archaeal TOGO pH wrappers over parent media."""

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

CURATOR = "repair_archaea_ph_wrappers_score20.py"
ACTION = "RESOLVED_ARCHAEA_PH_WRAPPER_SCORE20"
LINK_ACTION = "LINKED_ARCHAEA_PH_WRAPPER_SCORE20_CHILDREN"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

M165 = "archaea/TOGO_M165_Sulfolobus_Medium_B.yaml"
M345 = "archaea/TOGO_M345_Thermococcus_Medium_pH_6.0.yaml"
M156 = "archaea/TOGO_M156_Sulfolobus_Medium.yaml"
M273 = "archaea/TOGO_M273_Thermococcus_Medium.yaml"

TOGO_M165 = "https://togomedium.org/medium/M165"
TOGO_M345 = "https://togomedium.org/medium/M345"
TOGO_M156 = "https://togomedium.org/medium/M156"
TOGO_M273 = "https://togomedium.org/medium/M273"

EXPECTED_IDS = {
    M165: "CultureMech:008217",
    M345: "CultureMech:009724",
    M156: "CultureMech:008118",
    M273: "CultureMech:009290",
}
EXPECTED_SOURCE_TERMS = {
    M165: "TOGO:M165",
    M345: "TOGO:M345",
    M156: "TOGO:M156",
    M273: "TOGO:M273",
}

RELATIONSHIP = "PH_VARIANT"


@dataclass(frozen=True)
class ChildTarget:
    path: str
    parent_path: str
    source_url: str
    parent_source_url: str
    parent_solution_name: str
    parent_label: str
    h2so4_normality: str
    ph_value: float
    notes: str
    solution_notes: str
    parent_notes: str
    preparation_description: str
    variant_modification: str


TARGETS: tuple[ChildTarget, ...] = (
    ChildTarget(
        path=M165,
        parent_path=M156,
        source_url=TOGO_M165,
        parent_source_url=TOGO_M156,
        parent_solution_name="Sulfolobus medium (see Medium [M156])",
        parent_label="Sulfolobus Medium",
        h2so4_normality="10 N",
        ph_value=3.5,
        notes=(
            "TOGO M165 uses one liter of TOGO M156 Sulfolobus Medium and "
            "adjusts it to pH 3.5 with 10 N H2SO4."
        ),
        solution_notes=(
            "TOGO M165 uses one liter of TOGO M156 Sulfolobus Medium as "
            "the base medium."
        ),
        parent_notes=(
            "TOGO M165 uses TOGO M156 Sulfolobus Medium and adjusts it to "
            "pH 3.5 with 10 N H2SO4."
        ),
        preparation_description=(
            "Use one liter of Sulfolobus Medium from TOGO M156 and adjust "
            "to pH 3.5 with 10 N H2SO4."
        ),
        variant_modification=(
            "Adjusts TOGO M156 Sulfolobus Medium to pH 3.5 with 10 N H2SO4."
        ),
    ),
    ChildTarget(
        path=M345,
        parent_path=M273,
        source_url=TOGO_M345,
        parent_source_url=TOGO_M273,
        parent_solution_name="Thermococcus medium (see Medium [M273])",
        parent_label="Thermococcus Medium",
        h2so4_normality="1 N",
        ph_value=6.0,
        notes=(
            "TOGO M345 uses one liter of TOGO M273 Thermococcus Medium and "
            "readjusts the reduced medium to pH 6.0 with 1.0 N H2SO4."
        ),
        solution_notes=(
            "TOGO M345 uses one liter of TOGO M273 Thermococcus Medium as "
            "the base medium."
        ),
        parent_notes=(
            "TOGO M345 uses TOGO M273 Thermococcus Medium and readjusts the "
            "reduced medium to pH 6.0 with 1.0 N H2SO4."
        ),
        preparation_description=(
            "Use one liter of Thermococcus Medium from TOGO M273 and, after "
            "reduction, readjust to pH 6.0 with 1.0 N H2SO4."
        ),
        variant_modification=(
            "Readjusts TOGO M273 Thermococcus Medium to pH 6.0 with 1.0 N "
            "H2SO4 after reduction."
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


def _component_rows(doc: dict[str, Any], preferred_term: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for key in ("ingredients", "solutions"):
        for row in doc.get(key) or []:
            if isinstance(row, dict) and row.get("preferred_term") == preferred_term:
                rows.append(row)
    return rows


def _require_child(doc: dict[str, Any], target: ChildTarget) -> None:
    _require_source(doc, target.path)

    rows = _component_rows(doc, "H2SO4")
    if len(rows) != 1:
        raise ValueError(f"{target.path}: expected exactly one H2SO4 row")

    parent_media = doc.get("parent_media")
    if isinstance(parent_media, dict) and parent_media.get("id") == EXPECTED_IDS[
        target.parent_path
    ]:
        return

    if len(_component_rows(doc, target.parent_solution_name)) != 1:
        raise ValueError(f"{target.path}: missing {target.parent_label} component")


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


def _h2so4(target: ChildTarget) -> dict[str, Any]:
    return {
        "preferred_term": "H2SO4",
        "concentration": {"value": target.h2so4_normality, "unit": "VARIABLE"},
        "source": f"TOGO Medium {EXPECTED_SOURCE_TERMS[target.path].split(':')[1]}",
        "notes": (
            f"TOGO lists {target.h2so4_normality} H2SO4 for final pH "
            "adjustment. Normality is retained verbatim because the schema "
            "has no normality unit."
        ),
        "term": _term("CHEBI:26836", "sulfuric acid"),
        "mediaingredientmech_chebi_term": _term("CHEBI:26836", "sulfuric acid"),
    }


def _parent_solution(target: ChildTarget, parent: dict[str, Any]) -> dict[str, Any]:
    return {
        "preferred_term": target.parent_solution_name,
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


def _ensure_references(doc: dict[str, Any], target: ChildTarget) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (target.source_url, target.parent_source_url):
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


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
    source: str,
    changes: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "changes": changes,
        "source": source,
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
    repaired["ph_value"] = target.ph_value
    repaired["ingredients"] = [_h2so4(target)]
    repaired["solutions"] = [_parent_solution(target, parent)]
    repaired["preparation_steps"] = [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": target.preparation_description,
        }
    ]
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
    _ensure_references(repaired, target)
    _append_event(
        repaired,
        path=target.path,
        action=ACTION,
        source=target.source_url,
        changes="Resolved archaeal pH parent-medium wrapper",
        notes=target.variant_modification,
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
        source=target.source_url,
        changes="Linked archaeal pH child variant to its base parent",
        notes=f"Added or refreshed reciprocal pH-variant link for {child_path}.",
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
