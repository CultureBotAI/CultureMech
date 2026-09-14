#!/usr/bin/env python3
"""Repair two leftover score-20 JCM wrapper recipes."""

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

CURATOR = "repair_jcm_117_863_score20.py"
ACTION = "RESOLVED_JCM_117_863_SCORE20"
PARENT_ACTION = "LINKED_JCM_117_863_SCORE20_CHILD"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

R_AGAR_PARENT = "bacterial/r_agar.yaml"
ISP4_PARENT = "bacterial/inorganic_salts_starch_agar_isp_4.yaml"
R_AGAR_CATALASE = "bacterial/r_agar_with_catalase.yaml"
ISP4_15_NACL = "bacterial/inorganic_salts_starch_agar_isp_4_with_15_nacl.yaml"

TOGO_M19_URL = "https://togomedium.org/medium/M19"
TOGO_M50_URL = "https://togomedium.org/medium/M50"
TOGO_M109_URL = "https://togomedium.org/medium/M109"
TOGO_M900_URL = "https://togomedium.org/medium/M900"

EXPECTED_IDS = {
    R_AGAR_PARENT: "CultureMech:002627",
    ISP4_PARENT: "CultureMech:002937",
    R_AGAR_CATALASE: "CultureMech:002351",
    ISP4_15_NACL: "CultureMech:003209",
}

EXPECTED_SOURCE_TERMS = {
    R_AGAR_PARENT: "mediadive.medium:J26",
    ISP4_PARENT: "mediadive.medium:J58",
    R_AGAR_CATALASE: "mediadive.medium:J117",
    ISP4_15_NACL: "mediadive.medium:J863",
}


@dataclass(frozen=True)
class ChildRepair:
    path: str
    parent_path: str
    relationship: str
    ingredients: tuple[dict[str, Any], ...]
    solution: dict[str, Any]
    notes: str
    preparation_steps: tuple[dict[str, Any], ...]
    variant_modification: str
    parent_child_notes: str
    references: tuple[str, ...]
    accepted_signatures: tuple[tuple[str, ...], ...]
    ph_value: float | None = None
    data_quality_flags: tuple[str, ...] = (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    )


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _chebi(preferred_term: str, value: str, identifier: str, label: str) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "G_PER_L"},
        "term": _term(identifier, label),
        "mediaingredientmech_chebi_term": _term(identifier, label),
    }


CATALASE_REPAIR = ChildRepair(
    path=R_AGAR_CATALASE,
    parent_path=R_AGAR_PARENT,
    relationship="SUPPLEMENTED_VARIANT",
    ph_value=7.2,
    ingredients=(
        {
            "preferred_term": "Catalase (Sigma C-10)",
            "concentration": {"value": "0.06", "unit": "G_PER_L"},
            "notes": (
                "TOGO M109 maps JCM Medium 117 to 60 mg/L Catalase "
                "(Sigma C-10) added to 1 L of R Agar."
            ),
        },
    ),
    solution={
        "preferred_term": "R agar",
        "concentration": {"value": "1000", "unit": "ML_PER_L"},
        "notes": "TOGO M109 maps JCM Medium 117 to 1 L of JCM Medium 26 R Agar.",
        "culturemech_term": {"id": EXPECTED_IDS[R_AGAR_PARENT], "label": "R Agar"},
    },
    notes=(
        "TOGO M109 records the same JCM Medium 117 wrapper as 1 L of R Agar "
        "plus 60 mg/L filter-sterilized Catalase."
    ),
    preparation_steps=(
        {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Autoclave the JCM Medium 26 R Agar base.",
        },
        {
            "step_number": 2,
            "action": "FILTER",
            "description": "Sterilize catalase separately by filtration.",
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": "Add 60 mg/L sterile catalase to the R Agar base.",
        },
    ),
    variant_modification=(
        "Supplements JCM Medium 26 R Agar with 60 mg/L filter-sterilized catalase."
    ),
    parent_child_notes=(
        "Supplements JCM Medium 26 R Agar with 60 mg/L filter-sterilized catalase."
    ),
    references=(TOGO_M109_URL, TOGO_M19_URL),
    accepted_signatures=(("R agar", "Catalase"), ("Catalase (Sigma C-10)",)),
)

ISP4_15_NACL_REPAIR = ChildRepair(
    path=ISP4_15_NACL,
    parent_path=ISP4_PARENT,
    relationship="SALINITY_VARIANT",
    ingredients=(_chebi("NaCl", "150", "CHEBI:26710", "sodium chloride"),),
    solution={
        "preferred_term": "Inorganic Salts-Starch Agar (ISP-4)",
        "concentration": {"value": "1000", "unit": "ML_PER_L"},
        "notes": "TOGO M900 maps JCM Medium 863 to 1 L of JCM Medium 58 ISP-4.",
        "culturemech_term": {
            "id": EXPECTED_IDS[ISP4_PARENT],
            "label": "Inorganic Salts-Starch Agar (ISP-4)",
        },
    },
    notes=(
        "TOGO M900 records the same JCM Medium 863 wrapper as 1 L of JCM "
        "Medium 58 ISP-4 plus 150 g/L NaCl."
    ),
    preparation_steps=(
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Add 150 g/L NaCl to 1 L of JCM Medium 58 ISP-4.",
        },
        {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C for 15 min.",
        },
    ),
    variant_modification="Adds 150 g/L NaCl to JCM Medium 58 ISP-4.",
    parent_child_notes="Adds 150 g/L NaCl to JCM Medium 58 ISP-4.",
    references=(TOGO_M900_URL, TOGO_M50_URL),
    accepted_signatures=(
        ("Inorganic salts-starch agar", "NaCl"),
        ("NaCl",),
    ),
    data_quality_flags=("has_ontology_mappings", "ingredients_curated"),
)

CHILD_REPAIRS = (CATALASE_REPAIR, ISP4_15_NACL_REPAIR)
CHILD_BY_PATH = {repair.path: repair for repair in CHILD_REPAIRS}


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


def _require_record(doc: dict[str, Any], path: str) -> None:
    expected_id = EXPECTED_IDS[path]
    if doc.get("id") != expected_id:
        raise ValueError(f"{path}: expected id {expected_id}, found {doc.get('id')!r}")

    expected_source_term = EXPECTED_SOURCE_TERMS[path]
    source_term = _source_term_id(doc)
    if source_term != expected_source_term:
        raise ValueError(
            f"{path}: expected source term {expected_source_term}, " f"found {source_term!r}"
        )


def _require_child(doc: dict[str, Any], repair: ChildRepair) -> None:
    _require_record(doc, repair.path)
    if _component_names(doc) not in repair.accepted_signatures:
        raise ValueError(f"{repair.path}: JCM wrapper ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any], flags_to_add: tuple[str, ...]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    flags.extend(flags_to_add)
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], urls: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in urls:
        if url not in existing:
            references.append({"reference": url})


def _ensure_event(
    doc: dict[str, Any],
    *,
    action: str,
    source: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": source,
        "notes": notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
            and existing.get("source") == source
        ):
            history[index] = event
            return
    history.append(event)


def repair_child(doc: dict[str, Any], repair: ChildRepair) -> dict[str, Any]:
    _require_child(doc, repair)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    if repair.ph_value is None:
        repaired.pop("ph_value", None)
    else:
        repaired["ph_value"] = repair.ph_value
    repaired["ingredients"] = [copy.deepcopy(row) for row in repair.ingredients]
    repaired["solutions"] = [copy.deepcopy(repair.solution)]
    repaired["notes"] = repair.notes
    repaired["preparation_steps"] = [copy.deepcopy(step) for step in repair.preparation_steps]
    repaired["parent_media"] = {
        "path": f"data/normalized_yaml/{repair.parent_path}",
        "relationship": repair.relationship,
        "id": EXPECTED_IDS[repair.parent_path],
        "name": Path(repair.parent_path).stem,
        "notes": repair.parent_child_notes,
    }
    repaired["variant_relationship"] = repair.relationship
    repaired["variant_modifications"] = [repair.variant_modification]
    repaired.pop("variant_children", None)

    _ensure_flags(repaired, repair.data_quality_flags)
    _ensure_references(repaired, repair.references)
    _ensure_event(
        repaired,
        action=ACTION,
        source="; ".join(repair.references),
        notes=repair.notes,
    )
    return repaired


def _child_entry(repair: ChildRepair) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{repair.path}",
        "relationship": repair.relationship,
        "id": EXPECTED_IDS[repair.path],
        "name": Path(repair.path).stem,
        "notes": repair.parent_child_notes,
    }


def repair_parent(doc: dict[str, Any], repair: ChildRepair) -> dict[str, Any]:
    _require_record(doc, repair.parent_path)

    repaired = copy.deepcopy(doc)
    children = repaired.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError(f"{repair.parent_path}: variant_children is not a list")

    entry = _child_entry(repair)
    by_path = {
        row.get("path"): row for row in children if isinstance(row, dict) and row.get("path")
    }
    by_path[entry["path"]] = entry
    repaired["variant_children"] = [
        by_path[path] for path in sorted(by_path) if path.startswith("data/")
    ]

    _ensure_event(
        repaired,
        action=PARENT_ACTION,
        source="; ".join(repair.references),
        notes=f"Added or refreshed reciprocal link for {repair.path}.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for repair in CHILD_REPAIRS:
        child_path = normalized / repair.path
        parent_path = normalized / repair.parent_path
        plans[child_path] = repair_child(_load(child_path), repair)
        parent_doc = copy.deepcopy(plans.get(parent_path) or _load(parent_path))
        plans[parent_path] = repair_parent(parent_doc, repair)
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
