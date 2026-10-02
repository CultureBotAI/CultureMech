#!/usr/bin/env python3
"""Resolve TOGO/NBRC review findings for M1797 and the M3041/M3042 R2A pair."""

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

CURATOR = "repair_togo_nbrc_water_ph_review_batch.py"
TIMESTAMP = "2026-09-30T00:00:00-07:00"

TOGO_M1797 = "https://togomedium.org/medium/M1797"
NBRC_1022 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1022"
TOGO_M3041 = "https://togomedium.org/medium/M3041"
TOGO_M3042 = "https://togomedium.org/medium/M3042"
NBRC_1520 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1520"

Component = tuple[str, str, str]


M1797_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("MgSO4·7H2O", "5", "G_PER_L"),
    ("NaCl", "20", "G_PER_L"),
    ("K2HPO4", "5", "G_PER_L"),
    ("KCl", "1", "G_PER_L"),
    ("(NH4)2SO4", "3", "G_PER_L"),
    ("Ca(NO3)2", "0.3", "G_PER_L"),
    ("Sodium tetrathionate", "2", "G_PER_L"),
)
M1797_FINAL: tuple[Component, ...] = (("Distilled water", "1.0", "L"),) + M1797_IMPORTED[1:]

M3041_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("MgSO4·7H2O", "0.05", "G_PER_L"),
    ("K2HPO4", "0.3", "G_PER_L"),
    ("Sodium pyruvate", "0.3", "G_PER_L"),
    ("Glucose", "0.5", "G_PER_L"),
    ("Soluble starch", "0.5", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
    ("Bacto Yeast Extract (Difco)", "0.5", "G_PER_L"),
    ("Bacto Proteose Peptone No. 3 (Difco)", "0.5", "G_PER_L"),
    ("Sodium fumarate", "1.4", "G_PER_L"),
    ("Bacto Casamino Acids (Difco)", "0.5", "G_PER_L"),
)
M3041_FINAL: tuple[Component, ...] = (("Distilled water", "1.0", "L"),) + M3041_IMPORTED[1:]

M3042_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("MgSO4·7H2O", "0.05", "G_PER_L"),
    ("K2HPO4", "0.3", "G_PER_L"),
    ("Sodium pyruvate", "0.3", "G_PER_L"),
    ("Glucose", "0.5", "G_PER_L"),
    ("Soluble starch", "0.5", "G_PER_L"),
    ("Bacto Yeast Extract (Difco)", "0.5", "G_PER_L"),
    ("Bacto Proteose Peptone No. 3 (Difco)", "0.5", "G_PER_L"),
    ("Sodium fumarate", "1.4", "G_PER_L"),
    ("Bacto Casamino Acids (Difco)", "0.5", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)
M3042_FINAL: tuple[Component, ...] = (("Distilled water", "1.0", "L"),) + M3042_IMPORTED[1:]

M3041_CHILD = {
    "path": "data/normalized_yaml/bacterial/TOGO_M3042_R2A_fumarate_anaerobic.yaml",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": "CultureMech:009555",
    "name": "r2a_fumarate_anaerobic",
    "notes": (
        "TOGO M3042 is the liquid NBRC Medium 1520 R2A + fumarate "
        "projection that omits the optional 15 g/L agar row."
    ),
}

M3042_PARENT = {
    "path": "data/normalized_yaml/bacterial/r2a_fumarate_anaerobic.yaml",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": "CultureMech:009554",
    "name": "r2a_fumarate_anaerobic",
    "notes": (
        "TOGO M3041 is the solid agar NBRC Medium 1520 R2A + fumarate "
        "projection with the optional 15 g/L agar row."
    ),
}

M3042_VARIANT_MODIFICATION = (
    "Omits the optional 15 g/L agar row from TOGO M3041 and follows NBRC "
    "Medium 1520's anaerobic liquid dispensing instruction under an N2/CO2 "
    "atmosphere."
)

M3042_PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "ALIQUOT",
        "description": "Dispense the liquid medium under an N2/CO2 atmosphere.",
    },
    {
        "step_number": 2,
        "action": "ALIQUOT",
        "description": "Seal the dispensed medium with butyl rubber stoppers.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 20 min.",
    },
]
M3042_STERILIZATION = {"method": "AUTOCLAVE"}

M3042_GAS_NOTES = {
    "Carbon dioxide gas": (
        "NBRC Medium 1520 uses an N2/CO2 atmosphere for anaerobic liquid "
        "dispensing; retained as a variable gas-phase component."
    ),
    "Nitrogen gas": (
        "NBRC Medium 1520 uses an N2/CO2 atmosphere for anaerobic liquid "
        "dispensing; retained as a variable gas-phase component."
    ),
}


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    ph_value: float | None = None
    ph_range: dict[str, float] | None = None
    references: tuple[str, ...] = ()
    action: str = ""
    notes: str = ""


TARGETS: tuple[Target, ...] = (
    Target(
        path=Path("bacterial/togo_medium_m1797.yaml"),
        record_id="CultureMech:008365",
        source_term="TOGO:M1797",
        imported_signature=M1797_IMPORTED,
        final_signature=M1797_FINAL,
        ph_value=4.0,
        references=(TOGO_M1797, NBRC_1022),
        action="RESOLVED_TOGO_M1797_NBRC1022_REVIEW",
        notes=(
            "Corrected TOGO/NBRC Distilled water from the imported 1 g/L to "
            "the source 1 L final-volume row and restored the NBRC 1022 pH 4."
        ),
    ),
    Target(
        path=Path("bacterial/r2a_fumarate_anaerobic.yaml"),
        record_id="CultureMech:009554",
        source_term="TOGO:M3041",
        imported_signature=M3041_IMPORTED,
        final_signature=M3041_FINAL,
        ph_range={"min": 6.0, "max": 7.0},
        references=(TOGO_M3041, NBRC_1520),
        action="RESOLVED_TOGO_M3041_NBRC1520_REVIEW",
        notes=(
            "Corrected TOGO/NBRC Distilled water from the imported 1 g/L to "
            "the source 1 L final-volume row, restored the NBRC 1520 pH 6-7 "
            "range, and linked TOGO M3042 as the liquid physical-state "
            "variant."
        ),
    ),
    Target(
        path=Path("bacterial/TOGO_M3042_R2A_fumarate_anaerobic.yaml"),
        record_id="CultureMech:009555",
        source_term="TOGO:M3042",
        imported_signature=M3042_IMPORTED,
        final_signature=M3042_FINAL,
        ph_range={"min": 6.0, "max": 7.0},
        references=(TOGO_M3042, NBRC_1520),
        action="RESOLVED_TOGO_M3042_NBRC1520_REVIEW",
        notes=(
            "Corrected TOGO/NBRC Distilled water from the imported 1 g/L to "
            "the source 1 L final-volume row, restored the NBRC 1520 pH 6-7 "
            "range, preserved the N2/CO2 butyl-stopper autoclave instruction, "
            "and linked TOGO M3041 as the solid physical-state variant."
        ),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        del doc[key]

    items = list(doc.items())
    doc.clear()
    inserted = False
    for existing_key, existing_value in items:
        doc[existing_key] = existing_value
        if existing_key == after:
            doc[key] = value
            inserted = True
    if not inserted:
        doc[key] = value


def _signature(rows: Any) -> tuple[Component, ...]:
    if not isinstance(rows, (list, tuple)):
        raise ValueError("ingredients is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("ingredients contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"ingredient {row.get('preferred_term')!r} lacks concentration")
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
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")

    signature = _signature(doc.get("ingredients"))
    if signature not in (target.imported_signature, target.final_signature):
        raise ValueError(f"{target.path}: ingredient signature drifted")


def _ingredient_by_name(doc: dict[str, Any], name: str) -> dict[str, Any]:
    rows = doc.get("ingredients")
    if not isinstance(rows, list):
        raise ValueError("ingredients is not a list")

    matches = [row for row in rows if isinstance(row, dict) and row.get("preferred_term") == name]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one {name!r} ingredient, found {len(matches)}")
    return matches[0]


def _correct_distilled_water(doc: dict[str, Any]) -> None:
    water = _ingredient_by_name(doc, "Distilled water")
    water["concentration"] = {"value": "1.0", "unit": "L"}


def _restore_ph(doc: dict[str, Any], target: Target) -> None:
    doc.pop("ph_value", None)
    doc.pop("ph_range", None)

    if target.ph_value is not None:
        _put_after(doc, "ph_value", target.ph_value, "physical_state")
    if target.ph_range is not None:
        _put_after(doc, "ph_range", dict(target.ph_range), "physical_state")


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in target.references:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)

    if "references" in doc:
        _put_after(doc, "references", references, "applications")


def _append_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": target.action,
        "source": "; ".join(target.references),
        "notes": target.notes,
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


def _set_r2a_links(doc: dict[str, Any], target: Target) -> None:
    if target.record_id == "CultureMech:009554":
        existing = doc.get("variant_children")
        if existing is not None and existing != [M3041_CHILD]:
            raise ValueError(f"{target.path}: variant_children drifted")
        _put_after(doc, "variant_children", [copy.deepcopy(M3041_CHILD)], "curation_history")
    elif target.record_id == "CultureMech:009555":
        existing_parent = doc.get("parent_media")
        if existing_parent is not None and existing_parent != M3042_PARENT:
            raise ValueError(f"{target.path}: parent_media drifted")

        existing_relationship = doc.get("variant_relationship")
        if existing_relationship is not None and existing_relationship != "PHYSICAL_STATE_VARIANT":
            raise ValueError(f"{target.path}: variant_relationship drifted")

        existing_modifications = doc.get("variant_modifications")
        if existing_modifications is not None and existing_modifications != [
            M3042_VARIANT_MODIFICATION
        ]:
            raise ValueError(f"{target.path}: variant_modifications drifted")

        _put_after(doc, "parent_media", copy.deepcopy(M3042_PARENT), "curation_history")
        _put_after(doc, "variant_relationship", "PHYSICAL_STATE_VARIANT", "parent_media")
        _put_after(
            doc, "variant_modifications", [M3042_VARIANT_MODIFICATION], "variant_relationship"
        )


def _restore_m3042_anaerobic_preparation(doc: dict[str, Any]) -> None:
    for gas, note in M3042_GAS_NOTES.items():
        _ingredient_by_name(doc, gas)["notes"] = note

    _put_after(doc, "preparation_steps", copy.deepcopy(M3042_PREPARATION_STEPS), "ingredients")
    _put_after(doc, "sterilization", copy.deepcopy(M3042_STERILIZATION), "preparation_steps")


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    _correct_distilled_water(repaired)
    _restore_ph(repaired, target)

    if target.record_id == "CultureMech:009555":
        _restore_m3042_anaerobic_preparation(repaired)

    _ensure_references(repaired, target)
    _append_event(repaired, target)
    _set_r2a_links(repaired, target)
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
