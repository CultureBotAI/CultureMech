#!/usr/bin/env python3
"""Repair JCM Medium 1305 Helicobacter Medium source duplicates."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_1305_helicobacter_score15.py"
ACTION = "RESOLVED_JCM_1305_HELICOBACTER_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

JCM_1305 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1305"
TOGO_M1402 = "https://togomedium.org/medium/M1402"
SOURCE = "JCM Medium 1305"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    imported_signature: tuple[Component, ...]
    reference_urls: tuple[str, ...]
    notes: str
    parent_media: dict[str, Any] | None = None
    variant_relationship: str | None = None
    variant_children: tuple[dict[str, Any], ...] = field(default_factory=tuple)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "Brucella broth (BD-BBL)",
        "28",
        "G_PER_L",
        notes=(
            "JCM Medium 1305 lists 2.8 g Brucella broth (BD-BBL) in an "
            "80 ml distilled-water base; this row is normalized 10x to "
            "one liter and the BD-BBL product is not reducible to one "
            "ChEBI molecule."
        ),
    ),
    _ingredient(
        "Distilled water",
        "800",
        "ML_PER_L",
        notes=(
            "JCM Medium 1305 lists 80.0 ml distilled water in the source "
            "batch; this row is normalized 10x to one liter."
        ),
        term=("CHEBI:15377", "water"),
    ),
    _ingredient(
        "Conc. HCl",
        "1.35",
        "ML_PER_L",
        notes=(
            "JCM Medium 1305 adds 135 microliter concentrated HCl after "
            "autoclaving; this row is normalized 10x to one liter."
        ),
        term=("CHEBI:17883", "hydrogen chloride"),
    ),
    _ingredient(
        "Fetal bovine serum (Biowest; heat inactivated)",
        "200",
        "ML_PER_L",
        notes=(
            "JCM Medium 1305 aseptically adds 20.0 ml heat-inactivated "
            "fetal bovine serum from Biowest; this row is normalized 10x "
            "to one liter."
        ),
    ),
    _ingredient(
        "Vitox (Oxoid)",
        "20",
        "ML_PER_L",
        notes=(
            "JCM Medium 1305 aseptically adds 2.0 ml Vitox prepared from "
            "one Oxoid vial in 10 ml rehydration fluid; this row is "
            "normalized 10x to one liter."
        ),
    ),
    _ingredient(
        "Skirrow supplement (Oxoid)",
        "4",
        "ML_PER_L",
        notes=(
            "JCM Medium 1305 aseptically adds 0.4 ml Skirrow supplement "
            "prepared from one Oxoid vial in 2 ml sterile purified water; "
            "this row is normalized 10x to one liter."
        ),
    ),
    _ingredient(
        "Amphotericin B (5 mg/ml DMSO)",
        "1",
        "ML_PER_L",
        notes=(
            "JCM Medium 1305 aseptically adds 100 microliter of the "
            "5 mg/ml amphotericin B in DMSO stock; this row is normalized "
            "10x to one liter and represents a stock solution, not neat "
            "amphotericin B."
        ),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    _step(
        1,
        "AUTOCLAVE",
        "Autoclave Brucella broth in distilled water and cool to 50 C.",
    ),
    _step(
        2,
        "MIX",
        (
            "Aseptically add concentrated HCl, heat-inactivated fetal "
            "bovine serum, Vitox, Skirrow supplement, and amphotericin B "
            "in DMSO at the JCM Medium 1305 proportions."
        ),
    ),
    _step(
        3,
        "MIX",
        (
            "For stable culture, incubate 5 ml broth in a 25 cm2 "
            "polystyrene culture flask at 37 C under 5% O2 and 12% CO2 "
            "with shaking at 50 rpm."
        ),
    ),
)

NOTES = (
    "JCM Medium 1305 lists an 80 ml Brucella broth base acidified with "
    "135 microliter concentrated HCl after autoclaving, then aseptic "
    "addition of 20 ml heat-inactivated fetal bovine serum, 2 ml Vitox, "
    "0.4 ml Skirrow supplement, and 100 microliter amphotericin B stock; "
    "amounts are normalized 10x from the source batch."
)
TOGO_NOTES = (
    "TOGO M1402 mirrors JCM Medium 1305: an 80 ml Brucella broth base "
    "acidified with 135 microliter concentrated HCl after autoclaving, "
    "then aseptic addition of 20 ml heat-inactivated fetal bovine serum, "
    "2 ml Vitox, 0.4 ml Skirrow supplement, and 100 microliter "
    "amphotericin B stock; amounts are normalized 10x from the source batch."
)

JCM_TARGET = Target(
    path="bacterial/JCM_J1305_HELICOBACTER_MEDIUM.yaml",
    record_id="CultureMech:002469",
    source_term="mediadive.medium:J1305",
    imported_signature=(
        ("Brucella Broth", "27.451", "G_PER_L"),
        ("Fetal bovine serum", "20", "G_PER_L"),
        ("Vitox", "2", "G_PER_L"),
        ("Skirrow supplement", "0.4", "G_PER_L"),
        ("Amphotericin B", "100", "G_PER_L"),
    ),
    reference_urls=(JCM_1305,),
    notes=NOTES,
    variant_children=(
        {
            "path": "data/normalized_yaml/bacterial/TOGO_M1402_Helicobacter_Medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:007939",
            "name": "helicobacter_medium",
            "notes": "TOGO M1402 mirrors the same JCM Medium 1305 formula.",
        },
    ),
)

TOGO_TARGET = Target(
    path="bacterial/TOGO_M1402_Helicobacter_Medium.yaml",
    record_id="CultureMech:007939",
    source_term="TOGO:M1402",
    imported_signature=(
        ("Distilled water", "80", "G_PER_L"),
        ("Brucella broth (BD-BBL)", "2.8", "G_PER_L"),
        ("Fetal bovine serum (Biowest; heat inactivated)", "20", "G_PER_L"),
        ("Vitox (Oxoid) (1 vial/10 ml of rehydration fluid)", "2", "G_PER_L"),
        ("Amphotericin B (5 mg/ml DMSO)", "100", "G_PER_L"),
        ("Skirrow supplement (Oxoid) (1 vial/2 ml of sterile, purified water)", "0.4", "G_PER_L"),
    ),
    reference_urls=(TOGO_M1402, JCM_1305),
    notes=TOGO_NOTES,
    parent_media={
        "path": "data/normalized_yaml/bacterial/JCM_J1305_HELICOBACTER_MEDIUM.yaml",
        "relationship": "SOURCE_DUPLICATE",
        "id": "CultureMech:002469",
        "name": "helicobacter_medium",
        "notes": "TOGO M1402 mirrors the same JCM Medium 1305 formula.",
    },
    variant_relationship="SOURCE_DUPLICATE",
)

TARGETS: tuple[Target, ...] = (JCM_TARGET, TOGO_TARGET)
TARGET_BY_PATH: dict[str, Target] = {target.path: target for target in TARGETS}
FINAL_SIGNATURE = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in INGREDIENTS
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


def _signature(rows: Any) -> tuple[Component, ...]:
    if not isinstance(rows, list):
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.source_term}, found {source_term!r}"
        )

    signature = _signature(doc.get("ingredients"))
    if signature not in {target.imported_signature, FINAL_SIGNATURE}:
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.imported_signature!r} to {signature!r}"
        )


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
    for reference_url in target.reference_urls:
        if reference_url not in existing:
            references.append({"reference": reference_url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
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
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "temperature_value", 37.0, "physical_state")
    _put_after(repaired, "incubation_atmosphere", "MICROAEROPHILIC", "temperature_value")
    _put_after(repaired, "aeration", "5% O2, 12% CO2, shaking at 50 rpm", "incubation_atmosphere")
    _put_after(repaired, "culture_vessel", "25 cm2 polystyrene culture flask", "aeration")
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "ingredients")
    if target.parent_media is None:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
    else:
        repaired["parent_media"] = copy.deepcopy(target.parent_media)
        repaired["variant_relationship"] = target.variant_relationship
    if target.variant_children:
        repaired["variant_children"] = copy.deepcopy(list(target.variant_children))
    else:
        repaired.pop("variant_children", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
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
