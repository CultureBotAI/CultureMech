#!/usr/bin/env python3
"""Repair score-20 JCM/TOGO parent-medium wrappers."""

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

CURATOR = "repair_jcm_parent_wrappers_score20.py"
ACTION = "RESOLVED_JCM_PARENT_WRAPPER_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

M518_MARICHROMATIUM = "bacterial/TOGO_M518_Marichromatium_Imhoffii_Medium.yaml"
M566_LAMPROBACTER = "bacterial/TOGO_M566_Lamprobacter_Roseus_Medium.yaml"
M574_ALLOCHROMATIUM = "bacterial/TOGO_M574_Allochromatium_Renukaii_Medium.yaml"
M636_THERMUS_SV = "bacterial/TOGO_M636_Modified_Thermus_SV_Medium.yaml"
M671_MODIFIED_GAM = "bacterial/TOGO_M671_Modified_GAM_Agar.yaml"

TOGO_M518 = "https://togomedium.org/medium/M518"
TOGO_M566 = "https://togomedium.org/medium/M566"
TOGO_M574 = "https://togomedium.org/medium/M574"
TOGO_M636 = "https://togomedium.org/medium/M636"
TOGO_M671 = "https://togomedium.org/medium/M671"

JCM_517 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=517"
JCM_562 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=562"
JCM_570 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=570"
JCM_625 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=625"
JCM_655 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=655"

JCM_516 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=516"
JCM_561 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=561"
JCM_624 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=624"

RHODOBIUM = {
    "id": "CultureMech:009908",
    "label": "Rhodobium Gokurnum Medium",
}
THIORHODOCOCCUS = {
    "id": "CultureMech:009960",
    "label": "Thiorhodococcus Bheemlicum Medium",
}
THERMUS_3_NACL = {
    "id": "CultureMech:010034",
    "label": "Modified Thermus Medium With 3% NaCl",
}
VITAMIN_B12 = {"id": "mediadive.solution:6105", "label": "Vitamin B12 solution"}

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
    "parent_media",
    "variant_relationship",
    "variant_modifications",
)


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_media_term: str
    recipe: dict[str, Any]
    notes: str
    reference_urls: tuple[str, ...]


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
    return row


def _solution(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
    term: dict[str, str] | None = None,
    culturemech_term: dict[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "notes": notes,
    }
    if term is not None:
        row["term"] = copy.deepcopy(term)
    if culturemech_term is not None:
        row["culturemech_term"] = copy.deepcopy(culturemech_term)
    return row


def _water(source: str) -> dict[str, Any]:
    return _ingredient(
        "Distilled water",
        "1000",
        "ML_PER_L",
        source=source,
        notes=f"{source} lists 1.0 L distilled water.",
        term=("CHEBI:15377", "water"),
    )


def _parent_media(path: str, relationship: str, term: dict[str, str], name: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": term["id"],
        "name": name,
        "notes": notes,
    }


TARGETS: tuple[Target, ...] = (
    Target(
        path=M518_MARICHROMATIUM,
        expected_id="CultureMech:009909",
        expected_media_term="TOGO:M518",
        notes=(
            "TOGO M518 mirrors JCM Medium 517: Rhodobium gokurnum medium "
            "supplemented with 0.5 to 1.0 mM Na2S."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "Na2S",
                    "0.5-1.0",
                    "MILLIMOLAR",
                    source="JCM Medium 517",
                    notes="JCM Medium 517 supplements Rhodobium gokurnum medium with 0.5 to 1.0 mM Na2S.",
                    term=("CHEBI:76208", "sodium sulfide (anhydrous)"),
                )
            ],
            "solutions": [
                _solution(
                    "Rhodobium Gokurnum Medium",
                    "1000",
                    "ML_PER_L",
                    notes="JCM Medium 517 uses Rhodobium gokurnum medium as the prepared base.",
                    culturemech_term=RHODOBIUM,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Use Rhodobium gokurnum medium with 0.5 to 1.0 mM Na2S.",
                }
            ],
            "parent_media": _parent_media(
                "bacterial/TOGO_M517_Rhodobium_Gokurnum_Medium.yaml",
                "SUPPLEMENTED_VARIANT",
                RHODOBIUM,
                "rhodobium_gokurnum_medium",
                "Supplements Rhodobium gokurnum medium with 0.5 to 1.0 mM Na2S.",
            ),
            "variant_relationship": "SUPPLEMENTED_VARIANT",
            "variant_modifications": [
                "Supplements Rhodobium gokurnum medium with 0.5 to 1.0 mM Na2S."
            ],
        },
        reference_urls=(TOGO_M518, JCM_517, JCM_516),
    ),
    Target(
        path=M566_LAMPROBACTER,
        expected_id="CultureMech:009961",
        expected_media_term="TOGO:M566",
        notes=(
            "TOGO M566 mirrors JCM Medium 562: Medium 561 supplemented with "
            "1.0 ml/L vitamin B12 solution at 2 mg/100 ml."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [],
            "solutions": [
                _solution(
                    "Vitamin B12 solution",
                    "1.0",
                    "ML_PER_L",
                    notes="JCM Medium 562 supplements Medium 561 with 1.0 ml/L vitamin B12 solution (2 mg/100 ml).",
                    term=VITAMIN_B12,
                ),
                _solution(
                    "Thiorhodococcus Bheemlicum Medium",
                    "1000",
                    "ML_PER_L",
                    notes="JCM Medium 562 uses Medium 561 as the prepared base.",
                    culturemech_term=THIORHODOCOCCUS,
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Use Medium No. 561 supplemented with 1.0 ml/L vitamin B12 solution (2 mg/100 ml).",
                }
            ],
            "parent_media": _parent_media(
                "bacterial/TOGO_M565_Thiorhodococcus_Bheemlicum_Medium.yaml",
                "SUPPLEMENTED_VARIANT",
                THIORHODOCOCCUS,
                "thiorhodococcus_bheemlicum_medium",
                "Supplements Medium 561 with 1.0 ml/L vitamin B12 solution (2 mg/100 ml).",
            ),
            "variant_relationship": "SUPPLEMENTED_VARIANT",
            "variant_modifications": [
                "Supplements Medium 561 with 1.0 ml/L vitamin B12 solution (2 mg/100 ml)."
            ],
        },
        reference_urls=(TOGO_M566, JCM_562, JCM_561),
    ),
    Target(
        path=M574_ALLOCHROMATIUM,
        expected_id="CultureMech:009970",
        expected_media_term="TOGO:M574",
        notes=(
            "TOGO M574 mirrors JCM Medium 570: Medium 561 supplemented with "
            "1.0 ml/L vitamin B12 solution at 2 mg/ml."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [],
            "solutions": [
                _solution(
                    "Vitamin B12 solution",
                    "1.0",
                    "ML_PER_L",
                    notes="JCM Medium 570 supplements Medium 561 with 1.0 ml/L vitamin B12 solution (2 mg/ml).",
                    term=VITAMIN_B12,
                ),
                _solution(
                    "Thiorhodococcus Bheemlicum Medium",
                    "1000",
                    "ML_PER_L",
                    notes="JCM Medium 570 uses Medium 561 as the prepared base.",
                    culturemech_term=THIORHODOCOCCUS,
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Use Medium No. 561 supplemented with 1.0 ml/L vitamin B12 solution (2 mg/ml).",
                }
            ],
            "parent_media": _parent_media(
                "bacterial/TOGO_M565_Thiorhodococcus_Bheemlicum_Medium.yaml",
                "SUPPLEMENTED_VARIANT",
                THIORHODOCOCCUS,
                "thiorhodococcus_bheemlicum_medium",
                "Supplements Medium 561 with 1.0 ml/L vitamin B12 solution (2 mg/ml).",
            ),
            "variant_relationship": "SUPPLEMENTED_VARIANT",
            "variant_modifications": [
                "Supplements Medium 561 with 1.0 ml/L vitamin B12 solution (2 mg/ml)."
            ],
        },
        reference_urls=(TOGO_M574, JCM_570, JCM_561),
    ),
    Target(
        path=M636_THERMUS_SV,
        expected_id="CultureMech:010036",
        expected_media_term="TOGO:M636",
        notes=(
            "TOGO M636 mirrors JCM Medium 625: Medium 624 supplemented with "
            "3.0 g/L L-proline."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "L-proline",
                    "3.0",
                    "G_PER_L",
                    source="JCM Medium 625",
                    notes="JCM Medium 625 supplements Medium 624 with 3.0 g/L L-proline.",
                    term=("CHEBI:17203", "L-proline"),
                )
            ],
            "solutions": [
                _solution(
                    "Modified Thermus Medium With 3% NaCl",
                    "1000",
                    "ML_PER_L",
                    notes="JCM Medium 625 uses Medium 624 as the prepared base.",
                    culturemech_term=THERMUS_3_NACL,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Use Medium No. 624 supplemented with 3.0 g/L L-proline.",
                }
            ],
            "parent_media": _parent_media(
                "bacterial/TOGO_M634_Modified_Thermus_Medium_With_3_NaCl.yaml",
                "SUPPLEMENTED_VARIANT",
                THERMUS_3_NACL,
                "modified_thermus_medium_with_3_nacl",
                "Supplements Medium 624 with 3.0 g/L L-proline.",
            ),
            "variant_relationship": "SUPPLEMENTED_VARIANT",
            "variant_modifications": ["Supplements Medium 624 with 3.0 g/L L-proline."],
        },
        reference_urls=(TOGO_M636, JCM_625, JCM_624),
    ),
    Target(
        path=M671_MODIFIED_GAM,
        expected_id="CultureMech:010075",
        expected_media_term="TOGO:M671",
        notes=(
            "TOGO M671 mirrors JCM Medium 655: 56.7 g GAM agar, "
            "modified (Nissui), in 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "GAM agar, modified (Nissui)",
                    "56.7",
                    "G_PER_L",
                    source="JCM Medium 655",
                    notes="JCM Medium 655 lists 56.7 g GAM agar, modified (Nissui).",
                ),
                _water("JCM Medium 655"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Suspend 56.7 g GAM agar, modified (Nissui), in 1.0 L distilled water.",
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(TOGO_M671, JCM_655),
    ),
)


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


def _components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        row
        for rows in (doc.get("ingredients") or [], doc.get("solutions") or [])
        for row in rows
        if isinstance(row, dict)
    ]


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

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    if any(_grounded(component) for component in _components(doc)):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    if any(not _grounded(component) for component in _components(doc)):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    doc["data_quality_flags"] = list(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], reference_urls: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in reference_urls:
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.reference_urls),
        "notes": target.notes,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    if doc.get("id") != target.expected_id:
        raise ValueError(f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(f"{target.path}: expected media term {target.expected_media_term}")

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in target.recipe:
            repaired[recipe_field] = copy.deepcopy(target.recipe[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    repaired["notes"] = target.notes
    _ensure_flags(repaired)
    _ensure_references(repaired, target.reference_urls)
    _ensure_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
        for target in TARGETS
    }


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
