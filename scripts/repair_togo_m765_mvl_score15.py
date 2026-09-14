#!/usr/bin/env python3
"""Repair JCM/TOGO MVL Medium records by nesting JCM 740 stock solutions."""

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
JCM_J740_PATH = Path("bacterial/mvl_medium.yaml")
TOGO_M765_PATH = Path("bacterial/TOGO_M765_MVL_Medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m765_mvl_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

JCM_740 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=740"
MEDIADIVE_J740 = "https://mediadive.dsmz.de/medium/J740"
TOGO_M765 = "https://togomedium.org/medium/M765"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[Component, ...]
    action: str
    event_notes: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


JCM_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Resazurin", "1", "G_PER_L"),
    ("Trypticase peptone", "8.19001", "G_PER_L"),
    ("Yeast extract", "4.095", "G_PER_L"),
    ("Beef extract", "1.638", "G_PER_L"),
    ("Agar", "12.285", "G_PER_L"),
    ("Glucose", "1.638", "G_PER_L"),
    ("Hemin", "10", "G_PER_L"),
    ("Na2CO3", "50", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "10", "G_PER_L"),
    ("K2HPO4", "6", "G_PER_L"),
    ("(NH4)2SO4", "12", "G_PER_L"),
    ("NaCl", "12", "G_PER_L"),
    ("MgSO4 x 7 H2O", "1.2", "G_PER_L"),
    ("CaCl2 x 2 H2O", "1.2", "G_PER_L"),
)

TOGO_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "101.0", "G_PER_L"),
    ("Glucose", "2", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "5", "G_PER_L"),
    ("Beef extract", "2", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "10", "G_PER_L"),
    ("MgSO4・7H2O", "0.12", "G_PER_L"),
    ("NaCl", "1.2", "G_PER_L"),
    ("CaCl2・2H2O", "0.12", "G_PER_L"),
    ("K2HPO4", "0.6", "G_PER_L"),
    ("(NH4)2SO4", "1.2", "G_PER_L"),
)

TOGO_IMPORTED_SOLUTIONS: tuple[Component, ...] = (
    ("8.0% Na2CO3 solution", "50", "G_PER_L"),
    ("0.1% Resazurin solution", "1", "G_PER_L"),
    ("0.07% Hemin solution", "10", "G_PER_L"),
    ("3.0% L--Cysteine・HCl・H2O solution", "10", "G_PER_L"),
    ("Mineral solution 1 (see below)", "75", "G_PER_L"),
    ("Mineral solution 2 (see below)", "75", "G_PER_L"),
    ("KH2PO4 solution", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Trypticase peptone", "8.19001", "G_PER_L"),
    ("Yeast extract", "4.095", "G_PER_L"),
    ("Beef extract", "1.638", "G_PER_L"),
    ("Agar", "12.285", "G_PER_L"),
    ("Glucose", "1.638", "G_PER_L"),
    ("Distilled water", "819.001", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Mineral solution 1", "61.4251", "ML_PER_L"),
    ("Mineral solution 2", "61.4251", "ML_PER_L"),
    ("0.1% Resazurin solution", "0.819001", "ML_PER_L"),
    ("0.07% Hemin solution", "8.19001", "ML_PER_L"),
    ("8% Na2CO3 solution", "40.95", "ML_PER_L"),
    ("3% L-Cysteine HCl x H2O solution", "8.19001", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Agar": ("CHEBI:2509", "agar"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Hemin": ("CHEBI:50385", "hemin"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "L-Cysteine HCl x H2O": (
        "CHEBI:91248",
        "L-cysteine hydrochloride hydrate",
    ),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Yeast extract": ("NITROGEN_SOURCE",),
    "Glucose": ("CARBON_SOURCE",),
    "(NH4)2SO4": ("NITROGEN_SOURCE", "SULFUR_SOURCE"),
    "MgSO4 x 7 H2O": ("SULFUR_SOURCE", "TRACE_ELEMENT"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Agar": ("SOLIDIFYING_AGENT",),
    "Resazurin": ("REDOX_INDICATOR",),
    "Na2CO3": ("BUFFER",),
    "K2HPO4": ("BUFFER",),
    "KH2PO4": ("BUFFER",),
    "L-Cysteine HCl x H2O": ("REDUCING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

M765_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M765_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010172",
    "name": "mvl_medium",
    "notes": (
        "TOGO M765 imports the same JCM Medium 740 MVL Medium formulation "
        "represented by MediaDive J740."
    ),
}

J740_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J740_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003083",
    "name": "mvl_medium",
    "notes": (
        "TOGO M765 imports the same JCM Medium 740 MVL Medium formulation "
        "represented by MediaDive J740."
    ),
}

SOURCE_NOTE = (
    "JCM Medium 740, MediaDive J740, and TOGO M765 describe MVL Medium as "
    "a 1.221 L main solution containing 1.0 L distilled water, 75.0 ml each "
    "of Mineral solution 1 and Mineral solution 2, 1.0 ml of 0.1% resazurin, "
    "50.0 ml of 8% Na2CO3, 10.0 ml each of 0.07% hemin and 3% L-Cysteine "
    "HCl x H2O stocks, Trypticase peptone, yeast extract, beef extract, "
    "glucose, and agar."
)

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare the main MVL Medium from 819.001 ml/L distilled water, "
            "61.4251 ml/L each of Mineral solution 1 and Mineral solution 2, "
            "0.819001 ml/L 0.1% Resazurin solution, 40.95 ml/L 8% Na2CO3 "
            "solution, 8.19001 ml/L each of 0.07% Hemin solution and 3% "
            "L-Cysteine HCl x H2O solution, Trypticase peptone, yeast "
            "extract, beef extract, glucose, and agar."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
    },
]

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
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
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }

    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)

    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _direct_ingredients(source: str) -> list[dict[str, Any]]:
    return [
        _component("Trypticase peptone", "8.19001", "G_PER_L", source=source),
        _component("Yeast extract", "4.095", "G_PER_L", source=source),
        _component("Beef extract", "1.638", "G_PER_L", source=source),
        _component("Agar", "12.285", "G_PER_L", source=source),
        _component("Glucose", "1.638", "G_PER_L", source=source),
        _component(
            "Distilled water",
            "819.001",
            "ML_PER_L",
            source=source,
            notes=f"{source} contributes 819.001 ml/L distilled water.",
        ),
    ]


def _percent_solution(
    preferred_term: str,
    volume: str,
    solute: str,
    percent: str,
    source: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": volume, "unit": "ML_PER_L"},
        "source": source,
        "notes": f"{source} adds {volume} ml/L {preferred_term}.",
        "composition": [
            _component(
                solute,
                percent,
                "PERCENT_W_V",
                source=source,
                notes=f"{source} specifies {preferred_term} as {percent}% w/v.",
            )
        ],
    }


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        {
            "preferred_term": "Mineral solution 1",
            "concentration": {"value": "61.4251", "unit": "ML_PER_L"},
            "source": source,
            "notes": f"{source} adds 61.4251 ml/L Mineral solution 1.",
            "composition": [
                _component(
                    "KH2PO4",
                    "0.6",
                    "PERCENT_W_V",
                    source=source,
                    notes=f"{source} describes Mineral solution 1 as 0.6% KH2PO4.",
                )
            ],
        },
        {
            "preferred_term": "Mineral solution 2",
            "concentration": {"value": "61.4251", "unit": "ML_PER_L"},
            "source": source,
            "notes": f"{source} adds 61.4251 ml/L Mineral solution 2.",
            "composition": [
                _component("K2HPO4", "6.0", "G_PER_L", source=source),
                _component("(NH4)2SO4", "12.0", "G_PER_L", source=source),
                _component("NaCl", "12.0", "G_PER_L", source=source),
                _component("MgSO4 x 7 H2O", "1.2", "G_PER_L", source=source),
                _component("CaCl2 x 2 H2O", "1.2", "G_PER_L", source=source),
                _component(
                    "Distilled water",
                    "1000.0",
                    "ML_PER_L",
                    source=source,
                    notes=f"{source} makes Mineral solution 2 up with 100.0 ml water.",
                ),
            ],
        },
        _percent_solution("0.1% Resazurin solution", "0.819001", "Resazurin", "0.1", source),
        _percent_solution("0.07% Hemin solution", "8.19001", "Hemin", "0.07", source),
        _percent_solution("8% Na2CO3 solution", "40.95", "Na2CO3", "8.0", source),
        _percent_solution(
            "3% L-Cysteine HCl x H2O solution",
            "8.19001",
            "L-Cysteine HCl x H2O",
            "3.0",
            source,
        ),
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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')}")
    if _source_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        target.imported_ingredients,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    solution_signature = _signature(doc.get("solutions"), "solutions")
    if solution_signature not in (
        target.imported_solutions,
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{target.path}: solution signature drifted")


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
    for key in ("term", "mediaingredientmech_term", "mediaingredientmech_chebi_term"):
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
        components.extend(i for i in nested if isinstance(i, dict))
    return components


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation", "resolved_reference"):
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", SOURCE_NOTE, "media_term")
    repaired["ingredients"] = _direct_ingredients(target.source_name)
    _put_after(repaired, "solutions", _solutions(target.source_name), "ingredients")
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "solutions",
    )
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")

    if target.parent_media:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), "references")
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
        _put_after(
            repaired,
            "variant_modifications",
            [J740_PARENT["notes"]],
            "variant_relationship",
        )
    else:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)

    if target.variant_children:
        repaired["variant_children"] = [copy.deepcopy(child) for child in target.variant_children]
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


TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_J740_PATH,
        record_id="CultureMech:003083",
        source_term="mediadive.medium:J740",
        source_name="MediaDive J740 / JCM Medium 740",
        imported_ingredients=JCM_IMPORTED_INGREDIENTS,
        imported_solutions=(),
        action="RESOLVED_JCM_740_MVL_MEDIUM",
        event_notes=(
            "Moved Mineral solution 1, Mineral solution 2, 0.1% Resazurin, "
            "0.07% Hemin, 8% Na2CO3, and 3% L-Cysteine HCl x H2O stocks "
            "into nested solution entries, restored main distilled water, "
            "and linked the TOGO M765 source duplicate."
        ),
        references=(MEDIADIVE_J740, JCM_740),
        variant_children=(M765_CHILD,),
    ),
    Target(
        path=TOGO_M765_PATH,
        record_id="CultureMech:010172",
        source_term="TOGO:M765",
        source_name="TOGO M765 / JCM Medium 740",
        imported_ingredients=TOGO_IMPORTED_INGREDIENTS,
        imported_solutions=TOGO_IMPORTED_SOLUTIONS,
        action="RESOLVED_TOGO_M765_MVL_MEDIUM",
        event_notes=(
            "Moved Mineral solution 1, Mineral solution 2, 0.1% Resazurin, "
            "0.07% Hemin, 8% Na2CO3, 3% L-Cysteine HCl x H2O, and KH2PO4 "
            "from empty solution stubs into structured solution entries, "
            "corrected main and stock water units, and linked the MediaDive "
            "J740 source duplicate."
        ),
        references=(TOGO_M765, JCM_740, MEDIADIVE_J740),
        parent_media=J740_PARENT,
    ),
)


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
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
