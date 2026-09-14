#!/usr/bin/env python3
"""Repair the JCM Rye-Bran MRS record using local J730 solution imports."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

TARGET = "bacterial/rye_bran_mrs.yaml"
TOGO_SOURCE = "bacterial/TOGO_M753_RYE-Bran_MRS.yaml"
EXPECTED_ID = "CultureMech:003075"
EXPECTED_SOURCE_TERM = "mediadive.medium:J730"
EXPECTED_TOGO_SOURCE_ID = "CultureMech:010159"
EXPECTED_TOGO_SOURCE_TERM = "TOGO:M753"
EXPECTED_INGREDIENTS = (
    "Lactobacilli MRS broth",
    "Rye-bran",
    "Malted wheat meal",
    "Trypsin",
)
EXPECTED_TOGO_INGREDIENTS = (
    "Distilled water",
    "Lactobacilli MRS broth (BD-Difco)",
    "Rye--bran extract (see below)",
    "Malted wheat meal",
    "Rye--bran",
    "Trypsin (Sigma--Aldrich)",
)

CURATOR = "repair_jcm_rye_bran_mrs.py"
ACTION = "RESOLVED_JCM_J730_RYE_BRAN_MRS_GRAPH"
TOGO_ACTION = "RESOLVED_TOGO_M753_RYE_BRAN_MRS_SOURCE_DUPLICATE"
TIMESTAMP = "2026-09-08T00:00:00-07:00"

MRS_BROTH = {"id": "CultureMech:009017", "label": "Lactobacilli MRS Broth"}

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
)

NOTES = (
    "MediaDive JCM J730 and the merged TOGO M753 copy list Rye-Bran MRS as "
    "Lactobacilli MRS broth in a medium containing 900 mL/L Rye-bran extract "
    "and 100 mL/L distilled water; the Rye-bran extract contains rye-bran, "
    "malted wheat meal, trypsin, and distilled water."
)

SOURCE_DUPLICATE_NOTE = (
    "TOGO M753 imports the same JCM Medium 730 Rye-Bran MRS formulation "
    "represented by MediaDive J730."
)

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_SOURCE}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_TOGO_SOURCE_ID,
    "name": "rye_bran_mrs",
    "notes": SOURCE_DUPLICATE_NOTE,
}

JCM_PARENT = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "rye_bran_mrs",
    "notes": SOURCE_DUPLICATE_NOTE,
}

REFERENCE_IDS = (
    "mediadive.medium:J730",
    "mediadive.solution:4656",
    "mediadive.solution:4657",
    "TOGO:M753",
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str] | None = None,
    culturemech_term: dict[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    if culturemech_term is not None:
        row["culturemech_term"] = copy.deepcopy(culturemech_term)
    return row


def _water(value: str, source: str) -> dict[str, Any]:
    return _ingredient(
        "Distilled water",
        value,
        "ML_PER_L",
        source=source,
        notes=f"{source} lists distilled water.",
        term=("CHEBI:15377", "water"),
    )


def _recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(
                "Lactobacilli MRS broth",
                "55",
                "G_PER_L",
                source="MediaDive JCM J730 main solution",
                notes="MediaDive solution 4656 lists 55 g/L Lactobacilli MRS broth.",
                culturemech_term=MRS_BROTH,
            ),
            _water("100.0", "TOGO M753"),
        ],
        "solutions": [
            {
                "preferred_term": "Rye-bran extract",
                "concentration": {"value": "900.0", "unit": "ML_PER_L"},
                "notes": "The merged TOGO M753 copy lists 900 mL Rye-bran extract.",
                "composition": [
                    _ingredient(
                        "Rye-bran",
                        "40",
                        "G_PER_L",
                        source="MediaDive JCM J730 Rye-bran extract",
                        notes="MediaDive solution 4657 lists 40 g/L rye-bran.",
                    ),
                    _ingredient(
                        "Malted wheat meal",
                        "2",
                        "G_PER_L",
                        source="MediaDive JCM J730 Rye-bran extract",
                        notes="MediaDive solution 4657 lists 2 g/L malted wheat meal.",
                    ),
                    _ingredient(
                        "Trypsin",
                        "0.8",
                        "G_PER_L",
                        source="MediaDive JCM J730 Rye-bran extract",
                        notes="MediaDive solution 4657 lists 0.8 g/L trypsin.",
                        term=("CHEBI:9765", "Trypsin"),
                    ),
                    _water("1000", "MediaDive JCM J730 Rye-bran extract"),
                ],
            }
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Prepare Rye-Bran MRS from Lactobacilli MRS broth, 900 mL "
                    "Rye-bran extract, and 100 mL distilled water."
                ),
            },
            {
                "step_number": 2,
                "action": "HEAT",
                "description": (
                    "For the Rye-bran extract, mix the extract components and "
                    "incubate at 50 C for 24 h."
                ),
            },
            {
                "step_number": 3,
                "action": "FILTER",
                "description": (
                    "Clarify the Rye-bran extract by centrifugation at 500 x g "
                    "for 15 min followed by paper filtration."
                ),
            },
        ],
    }


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


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: found id {doc.get('id')!r}, expected {EXPECTED_ID!r}")

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERM:
        raise ValueError(
            f"{TARGET}: found source term {source_term!r}, expected {EXPECTED_SOURCE_TERM!r}"
        )

    ingredients = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    if tuple(i.get("preferred_term") for i in ingredients) not in (
        EXPECTED_INGREDIENTS,
        ("Lactobacilli MRS broth", "Distilled water"),
    ):
        raise ValueError(f"{TARGET}: MediaDive J730 ingredient list drifted")


def _require_togo_source(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_TOGO_SOURCE_ID:
        raise ValueError(
            f"{TOGO_SOURCE}: found id {doc.get('id')!r}, "
            f"expected {EXPECTED_TOGO_SOURCE_ID!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_TOGO_SOURCE_TERM:
        raise ValueError(
            f"{TOGO_SOURCE}: found source term {source_term!r}, "
            f"expected {EXPECTED_TOGO_SOURCE_TERM!r}"
        )

    ingredients = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    if tuple(i.get("preferred_term") for i in ingredients) not in (
        EXPECTED_TOGO_INGREDIENTS,
        ("Lactobacilli MRS broth", "Distilled water"),
    ):
        raise ValueError(f"{TOGO_SOURCE}: TOGO M753 ingredient list drifted")


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
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        nested = solution.get("composition") or []
        nested_components = (
            [i for i in nested if isinstance(i, dict)] if isinstance(nested, list) else []
        )
        components.extend(nested_components or [solution])
    return components


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    components = _composition_components(doc)
    if any(_grounded(component) for component in components):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    has_unmapped = any(not _grounded(component) for component in components)
    if has_unmapped:
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{TARGET}: references is not a list")

    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in REFERENCE_IDS:
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _ensure_event(doc: dict[str, Any], *, action: str, changes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "changes": changes,
        "source": "; ".join(REFERENCE_IDS),
        "notes": NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def _repair_recipe(doc: dict[str, Any]) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    recipe = _recipe()
    for field in RECIPE_FIELDS:
        if field in recipe:
            repaired[field] = copy.deepcopy(recipe[field])
        else:
            repaired.pop(field, None)
    repaired["notes"] = NOTES
    return repaired


def repair_document(doc: dict[str, Any], togo_source: dict[str, Any]) -> dict[str, Any]:
    _require_target(doc)
    _require_togo_source(togo_source)

    repaired = _repair_recipe(doc)
    repaired.pop("parent_media", None)
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
    repaired["variant_children"] = [copy.deepcopy(TOGO_CHILD)]

    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(
        repaired,
        action=ACTION,
        changes="Resolved JCM J730 Rye-Bran MRS solution graph",
    )
    return repaired


def repair_togo_source_document(doc: dict[str, Any]) -> dict[str, Any]:
    _require_togo_source(doc)

    repaired = _repair_recipe(doc)
    repaired["parent_media"] = copy.deepcopy(JCM_PARENT)
    repaired["variant_relationship"] = "SOURCE_DUPLICATE"
    repaired["variant_modifications"] = [SOURCE_DUPLICATE_NOTE]
    repaired.pop("variant_children", None)

    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(
        repaired,
        action=TOGO_ACTION,
        changes="Linked TOGO M753 as a JCM J730 Rye-Bran MRS source duplicate",
    )
    return repaired


def plan_repairs(normalized: Path) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    togo_path = normalized / TOGO_SOURCE
    togo = _load(togo_path)
    return {
        path: repair_document(_load(path), togo),
        togo_path: repair_togo_source_document(togo),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    changed_count = 0
    for path, doc in sorted(plan_repairs(args.normalized_dir).items()):
        if args.apply:
            changed = write_record(path, doc)
            action = "wrote" if changed else "skipped"
        else:
            changed = dump_record(doc).encode("utf-8") != path.read_bytes()
            action = "would write" if changed else "would skip"
        changed_count += int(changed)
        print(f"{action} {path.relative_to(REPO)}")

    print(f"{changed_count} record(s) {'updated' if args.apply else 'would change'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
