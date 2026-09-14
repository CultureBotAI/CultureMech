#!/usr/bin/env python3
"""Repair score-20 JCM/TOGO direct and parent-wrapper records."""

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

CURATOR = "repair_jcm_wrappers_direct_score20.py"
ACTION = "RESOLVED_JCM_WRAPPERS_DIRECT_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

M749_RAVOT_R8 = "bacterial/TOGO_M749_Ravot_Modified_Medium_For_Fervidobacterium_SP._R8.yaml"
M750_RAVOT_G60 = "bacterial/TOGO_M750_Ravot_Modified_Medium_For_Thermosipho_SP._G60.yaml"
M775_DESULFOVIBRIO_MARINE = "bacterial/TOGO_M775_Desulfovibrio_Marine_Medium.yaml"
M777_OPITUTUS = "bacterial/TOGO_M777_Opitutus_Terrae_Medium.yaml"
M828_M_TGE_BROTH = "bacterial/TOGO_M828_m_TGE_Broth_Medium.yaml"
M829_M_TGE_AGAR = "bacterial/TOGO_M829_m_TGE_Broth_Medium.yaml"

TOGO_M384 = "https://togomedium.org/medium/M384"
TOGO_M505 = "https://togomedium.org/medium/M505"
TOGO_M748 = "https://togomedium.org/medium/M748"
TOGO_M749 = "https://togomedium.org/medium/M749"
TOGO_M750 = "https://togomedium.org/medium/M750"
TOGO_M775 = "https://togomedium.org/medium/M775"
TOGO_M777 = "https://togomedium.org/medium/M777"
TOGO_M828 = "https://togomedium.org/medium/M828"
TOGO_M829 = "https://togomedium.org/medium/M829"

JCM_389 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=389"
JCM_504 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=504"
JCM_725 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=725"
JCM_726 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=726"
JCM_727 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=727"
JCM_750 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=750"
JCM_752 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=752"
JCM_795 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=795"

RAVOT_R101 = {
    "id": "CultureMech:010153",
    "label": "Ravot Modified Medium For Thermoanaerovibrio Sp. R101",
}
DESULFOVIBRIO = {"id": "CultureMech:009765", "label": "Desulfovibrio Medium"}
NE23_3 = {"id": "CultureMech:009895", "label": "NE23-3 Medium"}

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
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
    *,
    notes: str,
    culturemech_term: dict[str, str],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": "1000", "unit": "ML_PER_L"},
        "notes": notes,
        "culturemech_term": copy.deepcopy(culturemech_term),
    }


def _water(source: str) -> dict[str, Any]:
    return _ingredient(
        "Distilled water",
        "1000",
        "ML_PER_L",
        source=source,
        notes=f"{source} lists 1.0 L distilled water.",
        term=("CHEBI:15377", "water"),
    )


def _parent_media(
    path: str, relationship: str, term: dict[str, str], name: str, notes: str
) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": term["id"],
        "name": name,
        "notes": notes,
    }


def _nacl(value: str, source: str, notes: str) -> dict[str, Any]:
    return _ingredient(
        "NaCl",
        value,
        "G_PER_L",
        source=source,
        notes=notes,
        term=("CHEBI:26710", "sodium chloride"),
    )


def _glucose(value: str, source: str, notes: str) -> dict[str, Any]:
    return _ingredient(
        "glucose",
        value,
        "G_PER_L",
        source=source,
        notes=notes,
        term=("CHEBI:17234", "glucose"),
    )


M_TGE_BASE_INGREDIENTS = (
    _ingredient(
        "Bacto m TGE broth (BD-Difco)",
        "18.0",
        "G_PER_L",
        source="JCM Medium 795",
        notes="JCM Medium 795 lists 18.0 g Bacto m TGE broth (BD-Difco).",
    ),
    _water("JCM Medium 795"),
)


TARGETS: tuple[Target, ...] = (
    Target(
        path=M749_RAVOT_R8,
        expected_id="CultureMech:010154",
        expected_media_term="TOGO:M749",
        notes=(
            "TOGO M749 mirrors JCM Medium 726: Medium 725 with 5.0 g/L NaCl "
            "and pH adjusted to 6.3."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 6.3,
            "ingredients": [
                _nacl(
                    "5.0",
                    "JCM Medium 726",
                    "JCM Medium 726 uses Medium 725 with 5.0 g/L NaCl.",
                )
            ],
            "solutions": [
                _solution(
                    "Ravot Modified Medium For Thermoanaerovibrio SP. R101",
                    notes="JCM Medium 726 uses Medium 725 as the prepared base.",
                    culturemech_term=RAVOT_R101,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Use Medium No. 725 with 5.0 g/L NaCl.",
                },
                {
                    "step_number": 2,
                    "action": "ADJUST_PH",
                    "description": "Adjust pH to 6.3.",
                },
            ],
            "parent_media": _parent_media(
                "bacterial/TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101.yaml",
                "SALINITY_VARIANT",
                RAVOT_R101,
                "ravot_modified_medium_for_thermoanaerovibrio_sp_r101",
                "Uses Medium 725 with 5.0 g/L NaCl and pH adjusted to 6.3.",
            ),
            "variant_relationship": "SALINITY_VARIANT",
            "variant_modifications": [
                "Uses Medium 725 with 5.0 g/L NaCl.",
                "Adjusts pH to 6.3.",
            ],
        },
        reference_urls=(TOGO_M749, JCM_726, TOGO_M748, JCM_725),
    ),
    Target(
        path=M750_RAVOT_G60,
        expected_id="CultureMech:010156",
        expected_media_term="TOGO:M750",
        notes=(
            "TOGO M750 mirrors JCM Medium 727: Medium 725 with 20.0 g/L NaCl "
            "and pH adjusted to 7.0."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 7.0,
            "ingredients": [
                _nacl(
                    "20.0",
                    "JCM Medium 727",
                    "JCM Medium 727 uses Medium 725 with 20.0 g/L NaCl.",
                )
            ],
            "solutions": [
                _solution(
                    "Ravot Modified Medium For Thermoanaerovibrio SP. R101",
                    notes="JCM Medium 727 uses Medium 725 as the prepared base.",
                    culturemech_term=RAVOT_R101,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Use Medium No. 725 with 20.0 g/L NaCl.",
                },
                {
                    "step_number": 2,
                    "action": "ADJUST_PH",
                    "description": "Adjust pH to 7.0.",
                },
            ],
            "parent_media": _parent_media(
                "bacterial/TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101.yaml",
                "SALINITY_VARIANT",
                RAVOT_R101,
                "ravot_modified_medium_for_thermoanaerovibrio_sp_r101",
                "Uses Medium 725 with 20.0 g/L NaCl and pH adjusted to 7.0.",
            ),
            "variant_relationship": "SALINITY_VARIANT",
            "variant_modifications": [
                "Uses Medium 725 with 20.0 g/L NaCl.",
                "Adjusts pH to 7.0.",
            ],
        },
        reference_urls=(TOGO_M750, JCM_727, TOGO_M748, JCM_725),
    ),
    Target(
        path=M775_DESULFOVIBRIO_MARINE,
        expected_id="CultureMech:010183",
        expected_media_term="TOGO:M775",
        notes=("TOGO M775 mirrors JCM Medium 750: Medium 389 supplemented " "with 25.0 g/L NaCl."),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _nacl(
                    "25.0",
                    "JCM Medium 750",
                    "JCM Medium 750 supplements Medium 389 with 25.0 g/L NaCl.",
                )
            ],
            "solutions": [
                _solution(
                    "Desulfovibrio Medium",
                    notes="JCM Medium 750 uses Medium 389 as the prepared base.",
                    culturemech_term=DESULFOVIBRIO,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Use Medium No. 389 supplemented with 25.0 g/L NaCl.",
                }
            ],
            "parent_media": _parent_media(
                "bacterial/TOGO_M384_Desulfovibrio_Medium.yaml",
                "SALINITY_VARIANT",
                DESULFOVIBRIO,
                "desulfovibrio_medium",
                "Supplements Medium 389 with 25.0 g/L NaCl.",
            ),
            "variant_relationship": "SALINITY_VARIANT",
            "variant_modifications": ["Supplements Medium 389 with 25.0 g/L NaCl."],
        },
        reference_urls=(TOGO_M775, JCM_750, TOGO_M384, JCM_389),
    ),
    Target(
        path=M777_OPITUTUS,
        expected_id="CultureMech:010185",
        expected_media_term="TOGO:M777",
        notes="TOGO M777 mirrors JCM Medium 752: Medium 504 with 0.72 g/L glucose.",
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _glucose(
                    "0.72",
                    "JCM Medium 752",
                    "JCM Medium 752 uses Medium 504 with 0.72 g/L glucose.",
                )
            ],
            "solutions": [
                _solution(
                    "NE23-3 Medium",
                    notes="JCM Medium 752 uses Medium 504 as the prepared base.",
                    culturemech_term=NE23_3,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Use Medium No. 504 with 0.72 g/L glucose.",
                }
            ],
            "parent_media": _parent_media(
                "bacterial/TOGO_M505_NE23-3_Medium.yaml",
                "SUPPLEMENTED_VARIANT",
                NE23_3,
                "ne23_3_medium",
                "Supplements Medium 504 with 0.72 g/L glucose.",
            ),
            "variant_relationship": "SUPPLEMENTED_VARIANT",
            "variant_modifications": ["Supplements Medium 504 with 0.72 g/L glucose."],
        },
        reference_urls=(TOGO_M777, JCM_752, TOGO_M505, JCM_504),
    ),
    Target(
        path=M828_M_TGE_BROTH,
        expected_id="CultureMech:010241",
        expected_media_term="TOGO:M828",
        notes=(
            "TOGO M828 mirrors the liquid JCM Medium 795 recipe: 18.0 g "
            "Bacto m TGE broth (BD-Difco) in 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": list(M_TGE_BASE_INGREDIENTS),
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Suspend 18.0 g Bacto m TGE broth (BD-Difco) in 1.0 L distilled water.",
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(TOGO_M828, JCM_795),
    ),
    Target(
        path=M829_M_TGE_AGAR,
        expected_id="CultureMech:010242",
        expected_media_term="TOGO:M829",
        notes=(
            "TOGO M829 mirrors the solid JCM Medium 795 preparation: 18.0 g "
            "Bacto m TGE broth (BD-Difco), 15.0 g/L agar, and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                *M_TGE_BASE_INGREDIENTS,
                _ingredient(
                    "agar",
                    "15.0",
                    "G_PER_L",
                    source="JCM Medium 795",
                    notes="JCM Medium 795 adds 15.0 g/L agar for solid medium.",
                    term=("CHEBI:2509", "agar"),
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Suspend 18.0 g Bacto m TGE broth (BD-Difco) and 15.0 g agar in 1.0 L distilled water.",
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(TOGO_M829, JCM_795),
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
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}"
        )
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
