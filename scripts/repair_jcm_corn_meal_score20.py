#!/usr/bin/env python3
"""Repair sparse JCM/TOGO Corn Meal Agar product records."""

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

CURATOR = "repair_jcm_corn_meal_score20.py"
ACTION = "RESOLVED_JCM_CORN_MEAL_SCORE20_GRAPH"
LINK_ACTION = "LINKED_JCM_CORN_MEAL_SCORE20_DUPLICATE"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

JCM_150_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=150"
JCM_1329_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1329"

EXPECTED_IDS = {
    "bacterial/JCM_J150_CORN_MEAL_AGAR.yaml": "CultureMech:002509",
    "bacterial/TOGO_M141_Corn_Meal_Agar.yaml": "CultureMech:007957",
    "bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml": "CultureMech:002492",
    "bacterial/TOGO_M3004_Corn_Meal_Agar.yaml": "CultureMech:009521",
}

EXPECTED_SOURCE_TERMS = {
    "bacterial/JCM_J150_CORN_MEAL_AGAR.yaml": "mediadive.medium:J150",
    "bacterial/TOGO_M141_Corn_Meal_Agar.yaml": "TOGO:M141",
    "bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml": "mediadive.medium:J1329",
    "bacterial/TOGO_M3004_Corn_Meal_Agar.yaml": "TOGO:M3004",
}


@dataclass(frozen=True)
class Target:
    path: str
    jcm_no: str
    source_url: str
    product_name: str
    duplicate_of: str | None = None

    @property
    def source_label(self) -> str:
        return f"JCM Medium {self.jcm_no}"


TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
        jcm_no="150",
        source_url=JCM_150_URL,
        product_name="Corn meal agar (BD-Difco)",
    ),
    Target(
        path="bacterial/TOGO_M141_Corn_Meal_Agar.yaml",
        jcm_no="150",
        source_url=JCM_150_URL,
        product_name="Corn meal agar (BD-Difco)",
        duplicate_of="bacterial/JCM_J150_CORN_MEAL_AGAR.yaml",
    ),
    Target(
        path="bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml",
        jcm_no="1329",
        source_url=JCM_1329_URL,
        product_name="Corn meal agar (Nissui)",
    ),
    Target(
        path="bacterial/TOGO_M3004_Corn_Meal_Agar.yaml",
        jcm_no="1329",
        source_url=JCM_1329_URL,
        product_name="Corn meal agar (Nissui)",
        duplicate_of="bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml",
    ),
)

NOTES_BY_JCM = {
    "150": (
        "JCM Medium 150 defines CORN MEAL AGAR as 17.0 g/L Corn meal agar "
        "(BD-Difco) in 1.0 L distilled water, with default JCM autoclaving at "
        "121 C for 15 minutes."
    ),
    "1329": (
        "JCM Medium 1329 defines CORN MEAL AGAR as 17.0 g/L Corn meal agar "
        "(Nissui) in 1.0 L distilled water, with default JCM autoclaving at "
        "121 C for 15 minutes."
    ),
}


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _check_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != EXPECTED_IDS[target.path]:
        raise ValueError(
            f"{target.path}: expected immutable id {EXPECTED_IDS[target.path]}, "
            f"found {doc.get('id')!r}"
        )

    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{target.path}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != EXPECTED_SOURCE_TERMS[target.path]:
        raise ValueError(
            f"{target.path}: missing expected media term "
            f"{EXPECTED_SOURCE_TERMS[target.path]}"
        )

    if not doc.get("ingredients"):
        raise ValueError(f"{target.path}: missing ingredients")


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


def _recipe(target: Target) -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            {
                "preferred_term": target.product_name,
                "concentration": {"value": "17.0", "unit": "G_PER_L"},
                "source": target.source_label,
                "notes": (
                    f"{target.source_label} lists 17.0 g/L "
                    f"{target.product_name}; this is a commercial dehydrated "
                    "medium and is intentionally left ungrounded."
                ),
            },
            {
                "preferred_term": "Distilled water",
                "concentration": {"value": "1.0", "unit": "L"},
                "source": target.source_label,
                "notes": f"{target.source_label} lists 1.0 L distilled water.",
                "term": _term("CHEBI:15377", "water"),
                "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
            },
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "AUTOCLAVE",
                "description": "Autoclave at 121 C for 15 minutes.",
            },
        ],
        "sterilization": {"method": "AUTOCLAVE"},
    }


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)

    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = [
        ref
        for ref in doc.get("references") or []
        if isinstance(ref, dict) and ref.get("reference") != target.source_url
    ]
    references.append({"reference": target.source_url})
    doc["references"] = references


def _ensure_event(doc: dict[str, Any], action: str, source: str, notes: str) -> None:
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
        ):
            history[index] = event
            return
    history.append(event)


def _remove_empty_variant_links(doc: dict[str, Any]) -> None:
    for key in ("parent_media", "variant_children"):
        value = doc.get(key)
        if value == {} or value == []:
            doc.pop(key)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _check_target(doc, target)

    repaired = copy.deepcopy(doc)
    for key, value in _recipe(target).items():
        repaired[key] = value
    _put_after(repaired, "notes", NOTES_BY_JCM[target.jcm_no], "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _ensure_event(repaired, ACTION, target.source_url, NOTES_BY_JCM[target.jcm_no])
    _remove_empty_variant_links(repaired)
    return repaired


def _link_duplicate(parent: dict[str, Any], parent_path: str, child: dict[str, Any]) -> None:
    parent_ref = {
        "path": f"data/normalized_yaml/{parent_path}",
        "relationship": "SOURCE_DUPLICATE",
        "id": str(parent["id"]),
        "name": str(parent["name"]),
        "notes": (
            "TOGO imported the same Corn Meal Agar formula from the reviewed "
            f"{parent['media_term']['preferred_term']} source."
        ),
    }
    child["parent_media"] = parent_ref
    child["variant_relationship"] = "SOURCE_DUPLICATE"
    child["variant_modifications"] = [
        f"TOGO source-catalogue duplicate of {parent['media_term']['preferred_term']}."
    ]

    child_ref = {
        "path": f"data/normalized_yaml/{_relative_path(child)}",
        "relationship": "SOURCE_DUPLICATE",
        "id": str(child["id"]),
        "name": str(child["name"]),
        "notes": (
            f"{child['media_term']['preferred_term']} is a TOGO duplicate of "
            f"{parent['media_term']['preferred_term']}."
        ),
    }
    children = [
        ref
        for ref in parent.get("variant_children") or []
        if isinstance(ref, dict) and ref.get("id") != child_ref["id"]
    ]
    children.append(child_ref)
    parent["variant_children"] = sorted(children, key=lambda row: str(row.get("path")))


def _relative_path(doc: dict[str, Any]) -> str:
    recipe_id = str(doc.get("id"))
    for path, expected_id in EXPECTED_IDS.items():
        if expected_id == recipe_id:
            return path
    raise ValueError(f"unexpected recipe id {recipe_id!r}")


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    docs = {target.path: repair_record(_load(normalized / target.path), target) for target in TARGETS}
    for target in TARGETS:
        if target.duplicate_of is None:
            continue
        _link_duplicate(docs[target.duplicate_of], target.duplicate_of, docs[target.path])
        _ensure_event(
            docs[target.duplicate_of],
            LINK_ACTION,
            target.source_url,
            f"Linked {target.path} as a TOGO SOURCE_DUPLICATE.",
        )
        _ensure_event(
            docs[target.path],
            LINK_ACTION,
            target.source_url,
            f"Linked to {target.duplicate_of} as a JCM SOURCE_DUPLICATE.",
        )
    return {normalized / path: doc for path, doc in docs.items()}


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
