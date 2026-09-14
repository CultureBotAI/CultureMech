#!/usr/bin/env python3
"""Repair TOGO/JCM Pelagicoccus Agar records."""

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
JCM_J659_PATH = Path("bacterial/pelagicoccus_agar.yaml")
TOGO_M675_PATH = Path("bacterial/TOGO_M675_Pelagicoccus_Agar.yaml")
TOGO_M676_PATH = Path("bacterial/TOGO_M676_Pelagicoccus_Agar.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m675_m676_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M675 = "https://togomedium.org/medium/M675"
TOGO_M676 = "https://togomedium.org/medium/M676"
JCM_659 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=659"
JCM_346 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346"
MEDIADIVE_J659 = "https://mediadive.dsmz.de/medium/J659"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    source: str
    action: str
    notes: str
    event_notes: str
    references: tuple[str, ...]
    physical_state: str
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


JCM_IMPORTED: tuple[Component, ...] = (
    ("Marine agar 2216", "55.1", "G_PER_L"),
    ("R2A agar", "9.1", "G_PER_L"),
    ("NaCl", "24", "G_PER_L"),
    ("MgSO4 x 7 H2O", "7", "G_PER_L"),
    ("MgCl2 x 6 H2O", "5.3", "G_PER_L"),
    ("KCl", "0.7", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.1", "G_PER_L"),
)

TOGO_M675_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "251.0", "G_PER_L"),
    ("Marine agar 2216 (BD-Difco)", "55.1", "G_PER_L"),
    ("R2A agar (BD-Difco)", "9.1", "G_PER_L"),
    ("Artificial seawater (see below)", "750", "G_PER_L"),
    ("MgSO4\u00b77H2O", "7", "G_PER_L"),
    ("NaCl", "24", "G_PER_L"),
    ("CaCl2\u00b72H2O", "0.1", "G_PER_L"),
    ("MgCl2\u00b76H2O", "5.3", "G_PER_L"),
    ("KCl", "0.7", "G_PER_L"),
)

TOGO_M676_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "250", "G_PER_L"),
    ("Marine broth 2216 (BD-Difco)", "37.4", "G_PER_L"),
    ("R2A broth (Daigo)", "1.6", "G_PER_L"),
)

IMPORTED_M676_SOLUTION: tuple[Component, ...] = (
    ("Artificial seawater (see Medium [M675])", "750", "G_PER_L"),
)

AGAR_FINAL: tuple[Component, ...] = (
    ("Marine agar 2216 (BD-Difco)", "55.1", "G_PER_L"),
    ("R2A agar (BD-Difco)", "9.1", "G_PER_L"),
    ("Distilled water", "250.0", "ML_PER_L"),
)

LIQUID_FINAL: tuple[Component, ...] = (
    ("Marine broth 2216 (BD-Difco)", "37.4", "G_PER_L"),
    ("R2A broth (Daigo)", "1.6", "G_PER_L"),
    ("Distilled water", "250.0", "ML_PER_L"),
)

FINAL_SOLUTION: tuple[Component, ...] = (("Artificial seawater", "750.0", "ML_PER_L"),)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MgCl2 x 6 H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "L": "L",
}

AGAR_NOTES = (
    "JCM Medium 659 Pelagicoccus Agar lists 55.1 g Marine agar 2216 "
    "(BD-Difco), 9.1 g R2A agar (BD-Difco), 750.0 ml Artificial seawater, "
    "and 250.0 ml Distilled water, then adjusts pH to 7.5."
)

LIQUID_NOTES = (
    "JCM Medium 659 directs the liquid medium to dissolve 37.4 g/L Marine "
    "Broth 2216 (BD-Difco) and 1.6 g/L R2A broth (Daigo) in the artificial "
    "sea water; TOGO M676 imports that liquid form with 750.0 ml/L "
    "Artificial seawater and 250.0 ml/L Distilled water."
)

M675_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M675_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010079",
    "name": "pelagicoccus_agar",
    "notes": "TOGO M675 imports the same JCM Medium 659 agar formulation.",
}

M676_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M676_PATH}",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": "CultureMech:010080",
    "name": "pelagicoccus_agar",
    "notes": "TOGO M676 represents the liquid JCM Medium 659 formulation.",
}

JCM_J659_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J659_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003004",
    "name": "pelagicoccus_agar",
    "notes": "TOGO M675 imports the same JCM Medium 659 agar formulation.",
}

JCM_J659_LIQUID_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J659_PATH}",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": "CultureMech:003004",
    "name": "pelagicoccus_agar",
    "notes": "TOGO M676 represents the liquid JCM Medium 659 formulation.",
}

M675_VARIANT_MODIFICATION = (
    "Same JCM Medium 659 Pelagicoccus Agar formulation as the MediaDive J659 " "source record."
)

M676_VARIANT_MODIFICATION = (
    "Substitutes 37.4 g/L Marine broth 2216 and 1.6 g/L R2A broth for the "
    "solidifying agar products in JCM Medium 659."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Combine the listed commercial medium components with 750.0 ml "
            "Artificial seawater and 250.0 ml distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.5.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}

TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_J659_PATH,
        record_id="CultureMech:003004",
        source_term="mediadive.medium:J659",
        imported_signature=JCM_IMPORTED,
        final_signature=AGAR_FINAL,
        source="MediaDive J659 / JCM Medium 659",
        action="RESOLVED_JCM_659_PELAGICOCCUS_AGAR",
        notes=AGAR_NOTES,
        event_notes=(
            "Restored JCM Medium 659 as the printed agar recipe, represented "
            "Artificial seawater as a 750.0 ml/L stock solution instead of "
            "flattening its salt recipe into the medium, de-grounded the "
            "commercial Marine agar and R2A agar products, and linked TOGO "
            "M675 and M676."
        ),
        references=(JCM_659, MEDIADIVE_J659),
        physical_state="SOLID_AGAR",
        variant_children=(M675_CHILD, M676_CHILD),
    ),
    Target(
        path=TOGO_M675_PATH,
        record_id="CultureMech:010079",
        source_term="TOGO:M675",
        imported_signature=TOGO_M675_IMPORTED,
        final_signature=AGAR_FINAL,
        source="TOGO M675 / JCM Medium 659",
        action="RESOLVED_TOGO_M675_SCORE15",
        notes=AGAR_NOTES,
        event_notes=(
            "Corrected the imported distilled-water and Artificial seawater "
            "units, moved Artificial seawater from flattened ingredients to a "
            "750.0 ml/L inline stock solution, added pH 7.5, de-grounded the "
            "commercial Marine agar and R2A agar products, and linked the "
            "JCM 659 source duplicate."
        ),
        references=(TOGO_M675, JCM_659, MEDIADIVE_J659),
        physical_state="SOLID_AGAR",
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(M675_VARIANT_MODIFICATION,),
        parent_media=JCM_J659_PARENT,
    ),
    Target(
        path=TOGO_M676_PATH,
        record_id="CultureMech:010080",
        source_term="TOGO:M676",
        imported_signature=TOGO_M676_IMPORTED,
        final_signature=LIQUID_FINAL,
        source="TOGO M676 / JCM Medium 659 liquid form",
        action="RESOLVED_TOGO_M676_SCORE15",
        notes=LIQUID_NOTES,
        event_notes=(
            "Corrected the imported distilled-water and Artificial seawater "
            "units, replaced the empty Artificial seawater cross-reference "
            "with a 750.0 ml/L inline stock solution, added pH 7.5, kept the "
            "commercial Marine broth and R2A broth products ungrounded, and "
            "linked the JCM 659 agar parent as a physical-state variant."
        ),
        references=(TOGO_M676, JCM_659, MEDIADIVE_J659, JCM_346),
        physical_state="LIQUID",
        variant_relationship="PHYSICAL_STATE_VARIANT",
        variant_modifications=(M676_VARIANT_MODIFICATION,),
        parent_media=JCM_J659_LIQUID_PARENT,
    ),
)


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
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _medium_product(
    preferred_term: str,
    value: str,
    source: str,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        "G_PER_L",
        source=source,
        notes=(
            f"{source} lists {value} g/L {preferred_term}; this commercial "
            "medium product is retained as an opaque complex component."
        ),
    )


def _ingredients(target: Target) -> list[dict[str, Any]]:
    if target.physical_state == "LIQUID":
        return [
            _medium_product("Marine broth 2216 (BD-Difco)", "37.4", target.source),
            _medium_product("R2A broth (Daigo)", "1.6", target.source),
            _component("Distilled water", "250.0", "ML_PER_L", source=target.source),
        ]

    return [
        _medium_product("Marine agar 2216 (BD-Difco)", "55.1", target.source),
        _medium_product("R2A agar (BD-Difco)", "9.1", target.source),
        _component("Distilled water", "250.0", "ML_PER_L", source=target.source),
    ]


def _artificial_seawater_solution() -> dict[str, Any]:
    return {
        "preferred_term": "Artificial seawater",
        "concentration": {"value": "750.0", "unit": "ML_PER_L"},
        "source": "JCM Medium 659",
        "notes": (
            "JCM Medium 659 adds 750.0 ml/L Artificial seawater prepared "
            "from the printed subrecipe."
        ),
        "culturemech_term": {
            "id": "CultureMech:013514",
            "label": "Artificial seawater",
        },
        "composition": [
            _component("NaCl", "24.0", "G_PER_L", source="JCM Medium 659"),
            _component("MgSO4 x 7 H2O", "7.0", "G_PER_L", source="JCM Medium 659"),
            _component("MgCl2 x 6 H2O", "5.3", "G_PER_L", source="JCM Medium 659"),
            _component("KCl", "0.7", "G_PER_L", source="JCM Medium 659"),
            _component("CaCl2 x 2 H2O", "0.1", "G_PER_L", source="JCM Medium 659"),
            _component(
                "Distilled water",
                "1.0",
                "L",
                source="JCM Medium 659",
                notes=(
                    "JCM Medium 659 lists 1.0 L Distilled water in the "
                    "Artificial seawater stock solution."
                ),
            ),
        ],
    }


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
    if _signature(doc.get("ingredients"), "ingredients") not in (
        target.imported_signature,
        target.final_signature,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")
    solution_signature = _signature(doc.get("solutions"), "solutions")
    if solution_signature and solution_signature not in (
        IMPORTED_M676_SOLUTION,
        FINAL_SOLUTION,
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
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in references:
        if reference not in existing:
            rows.append({"reference": reference})
            existing.add(reference)


def _append_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": target.action,
        "source": "; ".join(target.references),
        "notes": target.event_notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == target.action
        ):
            history[index] = event
            return
    history.append(event)


def _set_variant_children(
    doc: dict[str, Any],
    children: tuple[dict[str, Any], ...],
) -> None:
    if children:
        doc["variant_children"] = [copy.deepcopy(child) for child in children]
    else:
        doc.pop("variant_children", None)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = target.physical_state
    _put_after(repaired, "ph_value", 7.5, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(target)
    _put_after(repaired, "notes", target.notes, "media_term")
    _put_after(repaired, "solutions", [_artificial_seawater_solution()], "notes")
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "solutions",
    )
    _put_after(
        repaired,
        "sterilization",
        copy.deepcopy(STERILIZATION),
        "preparation_steps",
    )
    if target.parent_media is None:
        repaired.pop("parent_media", None)
    else:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), "references")
    _set_variant_children(repaired, target.variant_children)
    if target.variant_relationship:
        _put_after(
            repaired,
            "variant_relationship",
            target.variant_relationship,
            "parent_media",
        )
    else:
        repaired.pop("variant_relationship", None)
    if target.variant_modifications:
        _put_after(
            repaired,
            "variant_modifications",
            list(target.variant_modifications),
            "variant_relationship",
        )
    else:
        repaired.pop("variant_modifications", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _append_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in plans.items():
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
