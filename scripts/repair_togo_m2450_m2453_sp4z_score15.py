#!/usr/bin/env python3
"""Repair TOGO M2450-M2453 DSMZ Medium 1076b SP4-Z records."""

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
PARENT = Path("bacterial/sp4_z_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2450_m2453_sp4z_score15.py"
ACTION = "RESOLVED_TOGO_M2450_M2453_SP4Z_SCORE15"
LINK_ACTION = "LINKED_TOGO_M2450_M2453_SP4Z_VARIANTS"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2450 = "https://togomedium.org/medium/M2450"
TOGO_M2451 = "https://togomedium.org/medium/M2451"
TOGO_M2452 = "https://togomedium.org/medium/M2452"
TOGO_M2453 = "https://togomedium.org/medium/M2453"
DSMZ_1076B = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1076b.pdf"

EXPECTED_PARENT_ID = "CultureMech:000510"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:1076b"
PH_VALUE = 7.4

Component = tuple[str, str, str]

LIQUID_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("distilled water", "130", "G_PER_L"),
    ("DNA (fish sperm; SERVA)", "0.04", "G_PER_L"),
    ("Bacto-Peptone (BD)", "1", "G_PER_L"),
    ("Tryptone", "2", "G_PER_L"),
    ("PPLO broth", "0.7", "G_PER_L"),
    ("Fetal bovine serum (heat-inactivated)", "17", "G_PER_L"),
    ("Yeastolate (BD; 2%, autoclaved)", "20", "G_PER_L"),
    ("Swine serum (heat-inactivated)", "17", "G_PER_L"),
    ("CMRL-1066 medium (10x concentrated; GIBCO)", "10", "G_PER_L"),
)

AGAR_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("distilled water", "126", "G_PER_L"),
    ("agar", "2", "G_PER_L"),
    ("DNA (fish sperm; SERVA)", "0.04", "G_PER_L"),
    ("Bacto-Peptone (BD)", "1", "G_PER_L"),
    ("Tryptone", "2", "G_PER_L"),
    ("PPLO broth", "0.7", "G_PER_L"),
    ("Fetal bovine serum (heat-inactivated)", "17", "G_PER_L"),
    ("Yeastolate (BD; 2%, autoclaved)", "20", "G_PER_L"),
    ("Swine serum (heat-inactivated)", "17", "G_PER_L"),
    ("CMRL-1066 medium (10x concentrated; GIBCO)", "10", "G_PER_L"),
)

GLUCOSE_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Glucose (50% aqueous solution)", "2", "G_PER_L"),
)

ARGININE_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Arginine HCl (50% aqueous solution)", "2", "G_PER_L"),
)

LIQUID_COMMON_FINAL_SIGNATURE: tuple[Component, ...] = (
    ("distilled water", "650.0", "ML_PER_L"),
    ("DNA (fish sperm; SERVA)", "0.2", "G_PER_L"),
    ("Bacto-Peptone (BD)", "5.0", "G_PER_L"),
    ("Tryptone", "10.0", "G_PER_L"),
    ("PPLO broth", "3.5", "G_PER_L"),
    ("Fetal bovine serum (heat-inactivated)", "85.0", "ML_PER_L"),
    ("Yeastolate (BD; 2%, autoclaved)", "100.0", "ML_PER_L"),
    ("Swine serum (heat-inactivated)", "85.0", "ML_PER_L"),
    ("CMRL-1066 medium (10x concentrated; GIBCO)", "50.0", "ML_PER_L"),
)

AGAR_COMMON_FINAL_SIGNATURE: tuple[Component, ...] = (
    ("distilled water", "630.0", "ML_PER_L"),
    ("agar", "10.0", "G_PER_L"),
    ("DNA (fish sperm; SERVA)", "0.2", "G_PER_L"),
    ("Bacto-Peptone (BD)", "5.0", "G_PER_L"),
    ("Tryptone", "10.0", "G_PER_L"),
    ("PPLO broth", "3.5", "G_PER_L"),
    ("Fetal bovine serum (heat-inactivated)", "85.0", "ML_PER_L"),
    ("Yeastolate (BD; 2%, autoclaved)", "100.0", "ML_PER_L"),
    ("Swine serum (heat-inactivated)", "85.0", "ML_PER_L"),
    ("CMRL-1066 medium (10x concentrated; GIBCO)", "50.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Arginine HCl (50% aqueous solution)": ("CHEBI:31235", "L-Arginine x HCl"),
    "Bacto-Peptone (BD)": ("MICRO:0000178", "Peptone"),
    "DNA (fish sperm; SERVA)": ("CHEBI:16991", "deoxyribonucleic acid"),
    "Glucose (50% aqueous solution)": ("CHEBI:17234", "glucose"),
    "Tryptone": ("MICRO:0000182", "tryptone"),
    "agar": ("CHEBI:2509", "agar"),
    "distilled water": ("CHEBI:15377", "water"),
}


@dataclass(frozen=True)
class EnergySource:
    preferred_term: str
    role: str
    parent_label: str


GLUCOSE = EnergySource(
    preferred_term="Glucose (50% aqueous solution)",
    role="Carbon source",
    parent_label="glucose",
)

ARGININE = EnergySource(
    preferred_term="Arginine HCl (50% aqueous solution)",
    role="Nitrogen source",
    parent_label="arginine",
)


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str
    togo_url: str
    imported_signature: tuple[Component, ...]
    imported_solution_signature: tuple[Component, ...]
    common_final_signature: tuple[Component, ...]
    physical_state: str
    water_source_amount: str
    energy_source: EnergySource
    parent_notes: str
    child_notes: str
    variant_modification: str

    @property
    def source(self) -> str:
        return f"{self.expected_media_term.replace(':', ' ')} / DSMZ Medium 1076b"

    @property
    def reference_urls(self) -> tuple[str, ...]:
        return (self.togo_url, DSMZ_1076B)

    @property
    def final_signature(self) -> tuple[Component, ...]:
        return (
            *self.common_final_signature,
            (self.energy_source.preferred_term, "10.0", "ML_PER_L"),
        )

    @property
    def is_agar(self) -> bool:
        return self.physical_state == "SOLID_AGAR"


TARGET_M2450 = Target(
    path=Path("bacterial/TOGO_M2450_SP4-Z_Medium.yaml"),
    expected_id="CultureMech:009030",
    expected_media_term="TOGO:M2450",
    togo_url=TOGO_M2450,
    imported_signature=LIQUID_IMPORTED_INGREDIENT_SIGNATURE,
    imported_solution_signature=GLUCOSE_SOLUTION_SIGNATURE,
    common_final_signature=LIQUID_COMMON_FINAL_SIGNATURE,
    physical_state="LIQUID",
    water_source_amount="130 ml",
    energy_source=GLUCOSE,
    parent_notes="TOGO M2450 imports the DSMZ Medium 1076b glucose liquid branch.",
    child_notes="TOGO M2450 records the glucose liquid branch of DSMZ SP4-Z.",
    variant_modification="Selects the glucose energy-source branch without agar.",
)

TARGET_M2451 = Target(
    path=Path("bacterial/TOGO_M2451_SP4-Z_Medium.yaml"),
    expected_id="CultureMech:009031",
    expected_media_term="TOGO:M2451",
    togo_url=TOGO_M2451,
    imported_signature=LIQUID_IMPORTED_INGREDIENT_SIGNATURE,
    imported_solution_signature=ARGININE_SOLUTION_SIGNATURE,
    common_final_signature=LIQUID_COMMON_FINAL_SIGNATURE,
    physical_state="LIQUID",
    water_source_amount="130 ml",
    energy_source=ARGININE,
    parent_notes="TOGO M2451 imports the DSMZ Medium 1076b arginine liquid branch.",
    child_notes="TOGO M2451 records the arginine liquid branch of DSMZ SP4-Z.",
    variant_modification="Selects the arginine energy-source branch without agar.",
)

TARGET_M2452 = Target(
    path=Path("bacterial/TOGO_M2452_SP4-Z_Medium.yaml"),
    expected_id="CultureMech:009032",
    expected_media_term="TOGO:M2452",
    togo_url=TOGO_M2452,
    imported_signature=AGAR_IMPORTED_INGREDIENT_SIGNATURE,
    imported_solution_signature=GLUCOSE_SOLUTION_SIGNATURE,
    common_final_signature=AGAR_COMMON_FINAL_SIGNATURE,
    physical_state="SOLID_AGAR",
    water_source_amount="126 ml",
    energy_source=GLUCOSE,
    parent_notes="TOGO M2452 imports the DSMZ Medium 1076b glucose agar-plate branch.",
    child_notes="TOGO M2452 records the glucose agar-plate branch of DSMZ SP4-Z.",
    variant_modification="Selects the glucose energy-source and agar-plate branches.",
)

TARGET_M2453 = Target(
    path=Path("bacterial/TOGO_M2453_SP4-Z_Medium.yaml"),
    expected_id="CultureMech:009033",
    expected_media_term="TOGO:M2453",
    togo_url=TOGO_M2453,
    imported_signature=AGAR_IMPORTED_INGREDIENT_SIGNATURE,
    imported_solution_signature=ARGININE_SOLUTION_SIGNATURE,
    common_final_signature=AGAR_COMMON_FINAL_SIGNATURE,
    physical_state="SOLID_AGAR",
    water_source_amount="126 ml",
    energy_source=ARGININE,
    parent_notes="TOGO M2453 imports the DSMZ Medium 1076b arginine agar-plate branch.",
    child_notes="TOGO M2453 records the arginine agar-plate branch of DSMZ SP4-Z.",
    variant_modification="Selects the arginine energy-source and agar-plate branches.",
)

TARGETS = (TARGET_M2450, TARGET_M2451, TARGET_M2452, TARGET_M2453)


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
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(target: Target) -> tuple[dict[str, Any], ...]:
    rows = [
        _component(
            "distilled water",
            "630.0" if target.is_agar else "650.0",
            "ML_PER_L",
            source=target.source,
            notes=(
                f"DSMZ Medium 1076b lists {target.water_source_amount} "
                f"distilled water per 200 ml for this SP4-Z branch."
            ),
        ),
    ]
    if target.is_agar:
        rows.append(
            _component(
                "agar",
                "10.0",
                "G_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1076b lists 2 g agar per 200 ml for agar plates; "
                    "normalized to 10.0 g/L."
                ),
            )
        )

    rows.extend(
        (
            _component(
                "DNA (fish sperm; SERVA)",
                "0.2",
                "G_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1076b lists 0.04 g DNA from fish sperm per "
                    "200 ml; normalized to 0.2 g/L."
                ),
            ),
            _component(
                "Bacto-Peptone (BD)",
                "5.0",
                "G_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1076b lists 1.00 g Bacto-Peptone per 200 ml; "
                    "normalized to 5.0 g/L."
                ),
            ),
            _component(
                "Tryptone",
                "10.0",
                "G_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1076b lists 2.00 g Tryptone per 200 ml; " "normalized to 10.0 g/L."
                ),
            ),
            _component(
                "PPLO broth",
                "3.5",
                "G_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1076b lists 0.70 g PPLO broth per 200 ml; "
                    "normalized to 3.5 g/L and retained without an ontology "
                    "grounding as an opaque complex broth product."
                ),
            ),
            _component(
                "Fetal bovine serum (heat-inactivated)",
                "85.0",
                "ML_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1076b lists 17 ml heat-inactivated fetal bovine "
                    "serum per 200 ml; normalized to 85.0 ml/L and retained "
                    "without an ontology grounding."
                ),
            ),
            _component(
                "Yeastolate (BD; 2%, autoclaved)",
                "100.0",
                "ML_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1076b lists 20 ml 2% autoclaved Yeastolate "
                    "per 200 ml; normalized to 100.0 ml/L and retained without "
                    "an ontology grounding as a commercial yeastolate solution."
                ),
            ),
            _component(
                "Swine serum (heat-inactivated)",
                "85.0",
                "ML_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1076b lists 17 ml heat-inactivated swine serum "
                    "per 200 ml; normalized to 85.0 ml/L and retained without "
                    "an ontology grounding."
                ),
            ),
            _component(
                "CMRL-1066 medium (10x concentrated; GIBCO)",
                "50.0",
                "ML_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1076b lists 10 ml 10x CMRL-1066 per 200 ml; "
                    "normalized to 50.0 ml/L and retained without an ontology "
                    "grounding as an opaque commercial basal medium."
                ),
            ),
            _component(
                target.energy_source.preferred_term,
                "10.0",
                "ML_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1076b lists 2 ml of the selected "
                    f"50% {target.energy_source.parent_label} solution per 200 ml; "
                    "normalized to 10.0 ml/L."
                ),
            ),
        )
    )
    return tuple(rows)


def _notes(target: Target) -> str:
    agar = (
        " This agar-plate branch uses 126 ml distilled water per 200 ml, adds "
        "2 g agar, and is held at 55 degrees C before supplements are added."
        if target.is_agar
        else " This liquid branch uses 130 ml distilled water per 200 ml."
    )
    return (
        f"{target.source} records the DSMZ Medium 1076b SP4-Z branch using "
        f"{target.energy_source.parent_label} as its energy source. DSMZ "
        "Medium 1076b is a 200 ml formula that replaces yeast extract from "
        "normal SP4 with fish-sperm DNA, adjusts pH to 7.4, autoclaves at "
        "121 degrees C for 15 minutes, aseptically adds CMRL-1066, autoclaved "
        "Yeastolate, heat-inactivated fetal bovine serum, and heat-inactivated "
        "swine serum, and then adds either glucose or arginine HCl; the two "
        f"energy sources should not be combined.{agar}"
    )


def _event_notes(target: Target) -> str:
    return (
        f"{_notes(target)} Corrected TOGO's 200 ml source amounts that had been "
        "imported as per-liter concentrations, moved the energy-source solution "
        "into the ingredient list as a 10.0 ml/L addition, grounded disclosed "
        "simple components and protein hydrolysates, kept opaque product and "
        "serum additions intentionally unmapped, and linked the record to DSMZ "
        "Medium 1076b SP4-Z."
    )


def _parent_media(target: Target) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": "DERIVED_FROM",
        "id": EXPECTED_PARENT_ID,
        "name": "sp4_z_medium",
        "notes": target.child_notes,
    }


def _variant_child(target: Target) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{target.path}",
        "relationship": "DERIVED_FROM",
        "id": target.expected_id,
        "name": "sp4_z_medium",
        "notes": target.parent_notes,
    }


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
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, " f"found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(f"{target.path}: expected media term {target.expected_media_term}")

    signatures = (
        _signature(doc.get("ingredients"), "ingredients"),
        _signature(doc.get("solutions"), "solutions"),
    )
    expected_signatures = (
        (target.imported_signature, target.imported_solution_signature),
        (target.final_signature, ()),
    )
    if signatures not in expected_signatures:
        raise ValueError(
            f"{target.path}: ingredient/solution signature drifted from "
            f"{expected_signatures!r} to {signatures!r}"
        )


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.reference_urls:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(
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
        ):
            history[index] = event
            return
    history.append(event)


def _ensure_variant_child(doc: dict[str, Any], target: Target) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    child_ref = _variant_child(target)
    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == target.expected_id or child.get("path") == child_ref["path"]:
            children[index] = child_ref
            return
    children.append(child_ref)


def repair_target(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = target.physical_state
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(_ingredients(target)))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", _notes(target), "media_term")
    repaired["preparation_steps"] = [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 7.4.",
        },
        {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 degrees C for 15 minutes.",
        },
    ]
    if target.is_agar:
        repaired["preparation_steps"].append(
            {
                "step_number": 3,
                "action": "HEAT",
                "description": ("Hold agar medium at 55 degrees C before adding supplements."),
            }
        )
    repaired["preparation_steps"].append(
        {
            "step_number": len(repaired["preparation_steps"]) + 1,
            "action": "MIX",
            "description": (
                "Add CMRL-1066 medium, autoclaved Yeastolate, heat-inactivated "
                "fetal bovine serum, heat-inactivated swine serum, and the "
                f"{target.energy_source.parent_label} energy source aseptically."
            ),
        }
    )
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(
        repaired,
        action=ACTION,
        source="; ".join(target.reference_urls),
        notes=_event_notes(target),
    )
    repaired["parent_media"] = _parent_media(target)
    repaired["variant_relationship"] = "DERIVED_FROM"
    repaired["variant_modifications"] = [target.variant_modification]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    for target in TARGETS:
        _ensure_variant_child(repaired, target)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        source="; ".join((*[target.togo_url for target in TARGETS], DSMZ_1076B)),
        notes=(
            "Linked TOGO M2450-M2453 as source-derived glucose/arginine and "
            "liquid/agar branches of DSMZ Medium 1076b SP4-Z."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans = {
        normalized / target.path: repair_target(_load(normalized / target.path), target)
        for target in TARGETS
    }
    parent_path = normalized / PARENT
    plans[parent_path] = repair_parent(_load(parent_path))
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
