#!/usr/bin/env python3
"""Repair TOGO/JCM Modified Thermus Medium with 3% NaCl records."""

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
JCM_J624_PATH = Path("bacterial/modified_thermus_medium_with_3_nacl.yaml")
TOGO_M634_PATH = Path("bacterial/TOGO_M634_Modified_Thermus_Medium_With_3_NaCl.yaml")
TOGO_M635_PATH = Path("bacterial/TOGO_M635_Modified_Thermus_Medium_With_3_NaCl.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m634_m635_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M634 = "https://togomedium.org/medium/M634"
TOGO_M635 = "https://togomedium.org/medium/M635"
TOGO_M636 = "https://togomedium.org/medium/M636"
JCM_624 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=624"
JCM_625 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=625"
JCM_273 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=273"
MEDIADIVE_J624 = "https://mediadive.dsmz.de/medium/J624"
MEDIADIVE_J273 = "https://mediadive.dsmz.de/medium/J273"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    action: str
    source: str
    notes: str
    event_notes: str
    references: tuple[str, ...]
    physical_state: str = "LIQUID"
    extra_ingredients: tuple[str, ...] = ()
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()


JCM_IMPORTED: tuple[Component, ...] = (
    ("Peptone", "2.9703", "G_PER_L"),
    ("Yeast extract", "0.990099", "G_PER_L"),
    ("Sodium glutamate monohydrate", "0.990099", "G_PER_L"),
    ("NaCl", "29.7814314", "G_PER_L"),
    ("Nitrilotriacetic acid", "0.980392", "G_PER_L"),
    ("CaSO4 x 2 H2O", "0.588235", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.980392", "G_PER_L"),
    ("KNO3", "1.0098", "G_PER_L"),
    ("NaNO3", "6.7549", "G_PER_L"),
    ("Na2HPO4", "1.08824", "G_PER_L"),
    ("FeCl3 x 6 H2O", "10", "G_PER_L"),
)

TOGO_M634_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("NaCl", "30", "G_PER_L"),
    ("Sodium glutamate・H2O", "1", "G_PER_L"),
    ("Peptone", "3", "G_PER_L"),
)

TOGO_M635_IMPORTED: tuple[Component, ...] = (
    *TOGO_M634_IMPORTED[:4],
    ("agar", "20", "G_PER_L"),
    ("Peptone", "3", "G_PER_L"),
)

IMPORTED_SOLUTION: tuple[Component, ...] = (
    ("Castenholz basal salt solution (see Medium [M266])", "10", "G_PER_L"),
)

BASE_FINAL: tuple[Component, ...] = (
    ("Peptone", "3.0", "G_PER_L"),
    ("Yeast extract", "1.0", "G_PER_L"),
    ("Sodium glutamate x H2O", "1.0", "G_PER_L"),
    ("NaCl", "30.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

AGAR_FINAL: tuple[Component, ...] = (
    *BASE_FINAL,
    ("Agar", "20.0", "G_PER_L"),
)

FINAL_SOLUTION: tuple[Component, ...] = (
    ("Castenholz basal salt solution (see Medium No. 273)", "10.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Peptone": ("MICRO:0000178", "peptone"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "Sodium glutamate x H2O": ("CHEBI:232425", "monosodium L-glutamate hydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Agar": ("CHEBI:2509", "agar"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "CaSO4 x 2 H2O": ("CHEBI:32583", "calcium sulfate dihydrate"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "KNO3": ("CHEBI:63043", "potassium nitrate"),
    "NaNO3": ("CHEBI:63005", "sodium nitrate"),
    "Na2HPO4": ("CHEBI:34683", "disodium hydrogenphosphate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "L": "L",
}

BASE_NOTES = (
    "JCM Medium 624 Modified Thermus Medium with 3% NaCl lists 3.0 g "
    "Peptone, 1.0 g Yeast extract, 1.0 g Sodium glutamate-H2O, 30.0 g "
    "NaCl, 10.0 ml Castenholz basal salt solution from JCM Medium 273, "
    "and 1.0 L Distilled water, then adjusts pH to 7.8."
)

AGAR_NOTES = (
    "JCM Medium 624 Modified Thermus Medium with 3% NaCl lists the same "
    "liquid base and directs agar plates to be prepared with 20.0 g/L agar."
)

BASE_VARIANT_MODIFICATION = (
    "Same JCM Medium 624 Modified Thermus Medium with 3% NaCl formulation."
)

AGAR_VARIANT_MODIFICATION = "Adds 20.0 g/L agar for JCM Medium 624 agar plates."

M634_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M634_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010034",
    "name": "modified_thermus_medium_with_3_nacl",
    "notes": "TOGO M634 imports the same JCM Medium 624 liquid formulation.",
}

M635_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M635_PATH}",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": "CultureMech:010035",
    "name": "modified_thermus_medium_with_3_nacl",
    "notes": "TOGO M635 represents the JCM Medium 624 agar-plate formulation.",
}

M636_CHILD = {
    "path": "data/normalized_yaml/bacterial/TOGO_M636_Modified_Thermus_SV_Medium.yaml",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:010036",
    "name": "modified_thermus_sv_medium",
    "notes": "JCM Medium 625 supplements JCM Medium 624 with 3.0 g/L L-proline.",
}

JCM_J624_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J624_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:002970",
    "name": "modified_thermus_medium_with_3_nacl",
    "notes": "TOGO M634 imports the same JCM Medium 624 liquid formulation.",
}

JCM_J624_AGAR_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J624_PATH}",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": "CultureMech:002970",
    "name": "modified_thermus_medium_with_3_nacl",
    "notes": "TOGO M635 represents the JCM Medium 624 agar-plate formulation.",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Add the base components and 10.0 ml Castenholz basal salt solution to 1.0 L distilled water.",
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.8.",
    },
)

AGAR_STEP = {
    "step_number": 3,
    "action": "MIX",
    "description": "For agar plates, add 20.0 g/L agar.",
}

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}

TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_J624_PATH,
        record_id="CultureMech:002970",
        source_term="mediadive.medium:J624",
        imported_signature=JCM_IMPORTED,
        final_signature=BASE_FINAL,
        action="RESOLVED_JCM_624_THERMUS_3_NACL",
        source="MediaDive J624 / JCM Medium 624",
        notes=BASE_NOTES,
        event_notes=(
            "Restored the printed JCM Medium 624 base recipe, represented "
            "Castenholz basal salt solution as a 10.0 ml/L stock from JCM "
            "Medium 273 instead of flattening stock concentrations into the "
            "final medium, grounded the disclosed solutes, and linked TOGO "
            "M634 and M635."
        ),
        references=(JCM_624, MEDIADIVE_J624, JCM_273, MEDIADIVE_J273),
        variant_children=(M634_CHILD, M635_CHILD),
    ),
    Target(
        path=TOGO_M634_PATH,
        record_id="CultureMech:010034",
        source_term="TOGO:M634",
        imported_signature=TOGO_M634_IMPORTED,
        final_signature=BASE_FINAL,
        action="RESOLVED_TOGO_M634_SCORE15",
        source="TOGO M634 / JCM Medium 624",
        notes=BASE_NOTES,
        event_notes=(
            "Corrected the imported distilled-water and Castenholz-stock "
            "units, added pH 7.8, grounded Peptone, Yeast extract, and "
            "Sodium glutamate-H2O, linked the JCM 624 source duplicate, and "
            "added the existing TOGO M636 supplemented child backlink."
        ),
        references=(TOGO_M634, JCM_624, MEDIADIVE_J624, JCM_273, MEDIADIVE_J273),
        parent_media=JCM_J624_PARENT,
        variant_children=(M636_CHILD,),
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(BASE_VARIANT_MODIFICATION,),
    ),
    Target(
        path=TOGO_M635_PATH,
        record_id="CultureMech:010035",
        source_term="TOGO:M635",
        imported_signature=TOGO_M635_IMPORTED,
        final_signature=AGAR_FINAL,
        action="RESOLVED_TOGO_M635_SCORE15",
        source="TOGO M635 / JCM Medium 624 agar plate",
        notes=AGAR_NOTES,
        event_notes=(
            "Corrected the imported distilled-water and Castenholz-stock "
            "units, added pH 7.8, grounded Peptone, Yeast extract, "
            "Sodium glutamate-H2O, and Agar, represented M635 as the "
            "JCM Medium 624 agar-plate variant, and linked the JCM 624 parent."
        ),
        references=(TOGO_M635, JCM_624, MEDIADIVE_J624, JCM_273, MEDIADIVE_J273),
        physical_state="SOLID_AGAR",
        extra_ingredients=("Agar",),
        parent_media=JCM_J624_AGAR_PARENT,
        variant_relationship="PHYSICAL_STATE_VARIANT",
        variant_modifications=(AGAR_VARIANT_MODIFICATION,),
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
    nutritional_roles: tuple[str, ...] = (),
    physicochemical_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _base_ingredients(source: str) -> list[dict[str, Any]]:
    return [
        _component("Peptone", "3.0", "G_PER_L", source=source),
        _component(
            "Yeast extract",
            "1.0",
            "G_PER_L",
            source=source,
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component(
            "Sodium glutamate x H2O",
            "1.0",
            "G_PER_L",
            source=source,
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component("NaCl", "30.0", "G_PER_L", source=source),
        _component(
            "Distilled water",
            "1.0",
            "L",
            source=source,
            notes=f"{source} lists 1.0 L Distilled water.",
        ),
    ]


def _castenholz_solution(source: str) -> dict[str, Any]:
    return {
        "preferred_term": "Castenholz basal salt solution (see Medium No. 273)",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": source,
        "notes": (
            "JCM Medium 624 adds 10.0 ml/L Castenholz basal salt solution "
            "from JCM Medium 273."
        ),
        "culturemech_term": {
            "id": "CultureMech:013022",
            "label": "Castenholz basal salt solution",
        },
        "composition": [
            _component("Nitrilotriacetic acid", "1.0", "G_PER_L", source="JCM Medium 273"),
            _component("CaSO4 x 2 H2O", "0.6", "G_PER_L", source="JCM Medium 273"),
            _component("MgSO4 x 7 H2O", "1.0", "G_PER_L", source="JCM Medium 273"),
            _component("NaCl", "0.08", "G_PER_L", source="JCM Medium 273"),
            _component("KNO3", "1.03", "G_PER_L", source="JCM Medium 273"),
            _component("NaNO3", "6.89", "G_PER_L", source="JCM Medium 273"),
            _component(
                "Na2HPO4",
                "1.11",
                "G_PER_L",
                source="JCM Medium 273",
                physicochemical_roles=("BUFFER",),
            ),
            {
                "preferred_term": "FeCl3 x 6 H2O solution (0.03%)",
                "concentration": {"value": "10.0", "unit": "ML_PER_L"},
                "source": "JCM Medium 273",
                "notes": "JCM Medium 273 adds 10.0 ml/L FeCl3 x 6 H2O solution (0.03%).",
            },
            {
                "preferred_term": "Nitsch's trace elements",
                "concentration": {"value": "10.0", "unit": "ML_PER_L"},
                "source": "JCM Medium 273",
                "notes": "JCM Medium 273 adds 10.0 ml/L Nitsch's trace elements.",
            },
            _component(
                "Distilled water",
                "1.0",
                "L",
                source="JCM Medium 273",
                notes="JCM Medium 273 lists 1.0 L Distilled water in the stock solution.",
            ),
        ],
        "preparation_notes": "Adjust pH to 8.2.",
    }


def _ingredients(target: Target) -> list[dict[str, Any]]:
    rows = _base_ingredients(target.source)
    if "Agar" in target.extra_ingredients:
        rows.append(
            _component(
                "Agar",
                "20.0",
                "G_PER_L",
                source=target.source,
                notes="JCM Medium 624 instructs agar plates to add 20.0 g/L agar.",
                physicochemical_roles=("SOLIDIFYING_AGENT",),
            )
        )
    return rows


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
    if solution_signature and solution_signature != FINAL_SOLUTION:
        if target.path == JCM_J624_PATH:
            raise ValueError(f"{target.path}: unexpected pre-repair solutions")
        if solution_signature != IMPORTED_SOLUTION:
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
    _put_after(repaired, "ph_value", 7.8, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(target)
    _put_after(repaired, "notes", target.notes, "media_term")
    _put_after(repaired, "solutions", [_castenholz_solution(target.source)], "notes")
    steps = list(PREPARATION_STEPS)
    if "Agar" in target.extra_ingredients:
        steps.append(AGAR_STEP)
    _put_after(repaired, "preparation_steps", steps, "solutions")
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
