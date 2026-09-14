#!/usr/bin/env python3
"""Repair score-35 JCM/NBRC opaque medium records."""

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

CURATOR = "repair_jcm_nbrc_score35.py"
ACTION = "RESOLVED_JCM_NBRC_SCORE35_GRAPH"
TIMESTAMP = "2026-09-08T00:00:00-07:00"

JCM_1087_POREMEDIA = "bacterial/poremedia_b_cye_945_agar_medium.yaml"
TOGO_M1770_SEAWATER_PORPHYRA = "bacterial/seawater_with_porphyra.yaml"

EXPECTED_IDS = {
    JCM_1087_POREMEDIA: "CultureMech:002267",
    TOGO_M1770_SEAWATER_PORPHYRA: "CultureMech:008336",
}

EXPECTED_SOURCE_TERMS = {
    JCM_1087_POREMEDIA: "mediadive.medium:J1087",
    TOGO_M1770_SEAWATER_PORPHYRA: "TOGO:M1770",
}

JCM_1087 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1087"
TOGO_M1770 = "https://togomedium.org/medium/M1770"
NBRC_M985 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=985"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
    "salinity",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
    "parent_media",
    "variant_relationship",
    "variant_modifications",
    "variant_children",
)


@dataclass(frozen=True)
class RecipeUpdate:
    path: str
    notes: str
    recipe: dict[str, Any]
    reference_urls: tuple[str, ...]


def _ingredient(
    preferred_term: str,
    *,
    source: str,
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": source,
        "notes": notes,
    }


UPDATES = (
    RecipeUpdate(
        path=JCM_1087_POREMEDIA,
        notes=(
            "JCM Medium 1087 instructs users to use POREMEDIA B-CYE alpha "
            "Agar Medium from Eiken Chemical; the source does not disclose "
            "an amount or internal formulation."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "POREMEDIA B-CYE alpha Agar Medium (Eiken Chemical)",
                    source="JCM Medium 1087",
                    notes=(
                        "JCM Medium 1087 names an Eiken Chemical commercial "
                        "POREMEDIA B-CYE alpha Agar Medium product without "
                        "stating its amount or internal formulation."
                    ),
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Use the commercially available POREMEDIA B-CYE "
                        "alpha Agar Medium manufactured by Eiken Chemical."
                    ),
                },
            ],
        },
        reference_urls=(JCM_1087,),
    ),
    RecipeUpdate(
        path=TOGO_M1770_SEAWATER_PORPHYRA,
        notes=(
            "NBRC Medium 985 and TOGO M1770 record sterilized natural "
            "seawater with Porphyra thalli; the sources do not disclose "
            "the Porphyra amount or any seawater chemistry."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "salinity": "marine (natural seawater)",
            "ingredients": [
                _ingredient(
                    "Sterilized natural seawater",
                    source="NBRC Medium 985 / TOGO Medium M1770",
                    notes=(
                        "NBRC Medium 985 and TOGO M1770 list sterilized "
                        "natural seawater without specifying an amount."
                    ),
                ),
                _ingredient(
                    "Porphyra thalli",
                    source="NBRC Medium 985 / TOGO Medium M1770",
                    notes=(
                        "NBRC Medium 985 and TOGO M1770 list Porphyra "
                        "thalli without specifying an amount."
                    ),
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Use sterilized natural seawater with Porphyra thalli."
                    ),
                },
            ],
        },
        reference_urls=(TOGO_M1770, NBRC_M985),
    ),
)


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


def _require_target(doc: dict[str, Any], relative_path: str) -> None:
    expected_id = EXPECTED_IDS[relative_path]
    if doc.get("id") != expected_id:
        raise ValueError(
            f"{relative_path}: found id {doc.get('id')!r}, expected {expected_id!r}"
        )

    expected_source_term = EXPECTED_SOURCE_TERMS[relative_path]
    if _source_term_id(doc) != expected_source_term:
        raise ValueError(
            f"{relative_path}: found source term {_source_term_id(doc)!r}, "
            f"expected {expected_source_term!r}"
        )


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
            [i for i in nested if isinstance(i, dict)]
            if isinstance(nested, list)
            else []
        )
        components.extend(nested_components or [solution])
    return components


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
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

    if flags:
        doc["data_quality_flags"] = flags
    else:
        doc.pop("data_quality_flags", None)


def _ensure_references(doc: dict[str, Any], update: RecipeUpdate) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{update.path}: references is not a list")

    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in update.reference_urls:
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _append_curation_event(doc: dict[str, Any], update: RecipeUpdate) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved score-35 JCM/NBRC opaque medium graph",
        "source": "; ".join(update.reference_urls),
        "notes": update.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{update.path}: curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _repair_with_recipe(doc: dict[str, Any], update: RecipeUpdate) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in update.recipe:
            repaired[field] = copy.deepcopy(update.recipe[field])
        else:
            repaired.pop(field, None)
    repaired["notes"] = update.notes
    _ensure_flags(repaired)
    _ensure_references(repaired, update)
    _append_curation_event(repaired, update)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for update in UPDATES:
        path = normalized / update.path
        doc = _load(path)
        _require_target(doc, update.path)
        plans[path] = _repair_with_recipe(doc, update)
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
            changed = dump_record(doc) != path.read_text(encoding="utf-8")
        if changed:
            changed_count += 1
            print(path.relative_to(args.normalized_dir))

    action = "Updated" if args.apply else "Would update"
    print(f"{action} {changed_count} JCM/NBRC score-35 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
