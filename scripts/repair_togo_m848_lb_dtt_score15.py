#!/usr/bin/env python3
"""Repair MediaDive/TOGO JCM 813 LB plus DTT records."""

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
JCM_J813_PATH = Path("bacterial/lb_luria_bertani_broth_with_1_mm_dtt.yaml")
TOGO_M848_PATH = Path("bacterial/TOGO_M848_LB_Luria-Bertani_Broth_With_1_mM_DTT.yaml")
SOLUTION_4761_PATH = Path("bacterial/mediadive_4761_Main_sol_J813.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m848_lb_dtt_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J813 = "https://mediadive.dsmz.de/medium/J813"
JCM_J813 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=813"
TOGO_M848 = "https://togomedium.org/medium/M848"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class MediumTarget:
    path: Path
    record_id: str
    source_term: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    action: str
    event_notes: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


J813_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Tryptone", "10", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("NaCl", "10", "G_PER_L"),
)

M848_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("NaCl", "10", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "5", "G_PER_L"),
    ("Tryptone (BD-Difco)", "10", "G_PER_L"),
    ("1,4--dithiothreitol (DTT)", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_COMPOSITION: tuple[Component, ...] = (
    ("Tryptone", "10", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("NaCl", "10", "G_PER_L"),
    ("Distilled water", "1000", "PERCENT_V_V"),
)

PLACEHOLDER_INGREDIENTS: tuple[Component, ...] = (
    ("See source for composition", "variable", "VARIABLE"),
)

BASAL_COMPOSITION: tuple[Component, ...] = (
    ("Tryptone (BD-Difco)", "10.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "5.0", "G_PER_L"),
    ("NaCl", "10.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

FINAL_COMPOSITION: tuple[Component, ...] = (
    *BASAL_COMPOSITION,
    ("1,4-dithiothreitol (DTT)", "1.0", "MILLIMOLAR"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Tryptone (BD-Difco)": ("MICRO:0000182", "Tryptone"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "Yeast extract"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Distilled water": ("CHEBI:15377", "water"),
    "1,4-dithiothreitol (DTT)": ("CHEBI:18320", "1,4-dithiothreitol"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Tryptone (BD-Difco)": ("PROTEIN_SOURCE",),
    "Yeast extract (BD-Difco)": ("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "1,4-dithiothreitol (DTT)": ("REDUCING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MILLIMOLAR": "mM",
    "ML_PER_L": "ml/L",
}

SOURCE_NOTE = (
    "MediaDive J813 describes JCM Medium 813 LB (Luria-Bertani) Broth with "
    "1 mM DTT as 10.0 g/L BD-Difco tryptone, 5.0 g/L BD-Difco yeast extract, "
    "10.0 g/L NaCl, and 1.0 mM final 1,4-dithiothreitol in 1000.0 ml/L "
    "distilled water, adjusted to pH 7.0."
)

PREPARATION_STEPS = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Dissolve 10.0 g/L BD-Difco tryptone, 5.0 g/L BD-Difco yeast "
            "extract, and 10.0 g/L NaCl in 1000.0 ml/L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the pH-adjusted basal LB broth.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "After autoclaving, aseptically add 1.0 mM final "
            "1,4-dithiothreitol (DTT)."
        ),
    },
)

M848_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M848_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010263",
    "name": "lb_luria_bertani_broth_with_1_mm_dtt",
    "notes": (
        "TOGO M848 imports the same JCM Medium 813 LB broth with 1 mM "
        "dithiothreitol formulation represented by MediaDive J813."
    ),
}

J813_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J813_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003157",
    "name": "lb_luria_bertani_broth_with_1_mm_dtt",
    "notes": M848_CHILD["notes"],
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(*GROUNDINGS[preferred_term]),
    }

    term_id, term_label = GROUNDINGS[preferred_term]
    if term_id.startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(term_id, term_label)

    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _composition(source: str, components: tuple[Component, ...]) -> list[dict[str, Any]]:
    return [
        _component(name, value, unit, source=source)
        for name, value, unit in components
    ]


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _media_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _term_id(doc: dict[str, Any]) -> str:
    term = doc.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_medium_target(doc: dict[str, Any], target: MediumTarget) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected {target.record_id}, found {doc.get('id')}"
        )
    if _media_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (target.imported_ingredients, FINAL_COMPOSITION):
        raise ValueError(f"{target.path}: ingredient signature drifted")


def _ensure_solution_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:013706":
        raise ValueError(
            f"{SOLUTION_4761_PATH}: expected CultureMech:013706, "
            f"found {doc.get('id')}"
        )
    if _term_id(doc) != "mediadive.solution:4761":
        raise ValueError(f"{SOLUTION_4761_PATH}: expected MediaDive solution 4761")

    composition_signature = _signature(doc.get("composition"), "composition")
    if composition_signature not in (IMPORTED_SOLUTION_COMPOSITION, BASAL_COMPOSITION):
        raise ValueError(f"{SOLUTION_4761_PATH}: composition signature drifted")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (PLACEHOLDER_INGREDIENTS, ()):
        raise ValueError(f"{SOLUTION_4761_PATH}: ingredient signature drifted")


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


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "chebi_term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    components.extend(i for i in doc.get("composition") or [] if isinstance(i, dict))
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        nested = solution.get("composition") or []
        components.extend(i for i in nested if isinstance(i, dict))
    return components


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    components = _composition_components(doc)
    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)
    if any(not _grounded(component) for component in components):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    else:
        while "has_unmapped_ingredients" in flags:
            flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in references:
        if reference not in existing:
            rows.append({"reference": reference})
            existing.add(reference)


def _append_event(
    doc: dict[str, Any],
    *,
    action: str,
    references: tuple[str, ...],
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(references),
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


def repair_medium_record(
    doc: dict[str, Any],
    target: MediumTarget,
) -> dict[str, Any]:
    _ensure_medium_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    _put_after(repaired, "ph_range", {"min": 7.0, "max": 7.0}, "physical_state")
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", SOURCE_NOTE, "media_term")
    repaired["ingredients"] = _composition(target.source_name, FINAL_COMPOSITION)
    repaired.pop("solutions", None)
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "ingredients",
    )

    if target.parent_media:
        _put_after(
            repaired,
            "parent_media",
            copy.deepcopy(target.parent_media),
            "references",
        )
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
        _put_after(
            repaired,
            "variant_modifications",
            [M848_CHILD["notes"]],
            "variant_relationship",
        )
    else:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)

    if target.variant_children:
        repaired["variant_children"] = [
            copy.deepcopy(child) for child in target.variant_children
        ]
    else:
        repaired.pop("variant_children", None)

    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes=target.event_notes,
    )
    return repaired


def repair_solution_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _composition(
        "MediaDive solution 4761 / JCM Medium 813",
        BASAL_COMPOSITION,
    )
    repaired.pop("ingredients", None)
    repaired["preparation_notes"] = "Adjust pH to 7.0."
    _put_after(
        repaired,
        "notes",
        (
            "MediaDive solution 4761 is the pH-adjusted basal LB solution for "
            "JCM Medium 813; 1,4-dithiothreitol is added separately after "
            "autoclaving to a 1.0 mM final concentration."
        ),
        "preparation_notes",
    )

    _ensure_flags(repaired)
    _ensure_references(repaired, (MEDIADIVE_J813,))
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_4761_MAIN_SOL_J813",
        references=(MEDIADIVE_J813,),
        notes=(
            "Corrected the distilled-water quantity from 1000% v/v to 1000.0 "
            "ml/L, restored the BD-Difco basal LB component names from JCM "
            "Medium 813, and removed the placeholder top-level ingredient."
        ),
    )
    return repaired


TARGETS: tuple[MediumTarget, ...] = (
    MediumTarget(
        path=JCM_J813_PATH,
        record_id="CultureMech:003157",
        source_term="mediadive.medium:J813",
        source_name="MediaDive J813 / JCM Medium 813",
        imported_ingredients=J813_IMPORTED_INGREDIENTS,
        action="RESOLVED_JCM_813_LB_DTT",
        event_notes=(
            "Restored the MediaDive J813 source-level BD-Difco tryptone, "
            "BD-Difco yeast extract, NaCl, distilled water, and 1 mM final "
            "dithiothreitol formulation; added the missing distilled water and "
            "post-autoclave dithiothreitol; and linked the TOGO M848 source "
            "duplicate."
        ),
        references=(MEDIADIVE_J813, JCM_J813),
        variant_children=(M848_CHILD,),
    ),
    MediumTarget(
        path=TOGO_M848_PATH,
        record_id="CultureMech:010263",
        source_term="TOGO:M848",
        source_name="TOGO M848 / JCM Medium 813",
        imported_ingredients=M848_IMPORTED_INGREDIENTS,
        action="RESOLVED_TOGO_M848_LB_DTT",
        event_notes=(
            "Restored the source-level BD-Difco tryptone, BD-Difco yeast "
            "extract, NaCl, distilled water, and 1 mM final dithiothreitol "
            "formulation from MediaDive J813 and TOGO M848; corrected "
            "distilled water from 1 g/L to 1000.0 ml/L; corrected "
            "dithiothreitol from a variable placeholder to 1.0 mM; added "
            "pH 7.0; and linked the MediaDive J813 source duplicate."
        ),
        references=(TOGO_M848, MEDIADIVE_J813, JCM_J813),
        parent_media=J813_PARENT,
    ),
)


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_medium_record(_load(path), target)

    solution_path = normalized / SOLUTION_4761_PATH
    plans[solution_path] = repair_solution_record(_load(solution_path))
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write repaired records; by default only report planned changes",
    )
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed: list[Path] = []
    for path, doc in plans.items():
        rendered = dump_record(doc)
        old = path.read_text(encoding="utf-8")
        if old != rendered:
            changed.append(path)
            if args.apply:
                write_record(path, doc)

    action = "wrote" if args.apply else "would write"
    for path in changed:
        print(f"{action} {path.relative_to(REPO)}")
    print(f"{action} {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
