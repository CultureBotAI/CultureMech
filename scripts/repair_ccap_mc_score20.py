#!/usr/bin/env python3
"""Replace the malformed CCAP MC composition with the official PDF recipe."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = "algae/mc.yaml"
EXPECTED_ID = "CultureMech:000086"
SOURCE_URL = "https://www.ccap.ac.uk/wp-content/uploads/MR_MC.pdf"
SOURCE_NAME = "CCAP Medium MR_MC.pdf"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_ccap_mc_score20.py"
ACTION = "RESOLVED_CCAP_MC_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

NOTES = (
    "CCAP MC lists casein digest, Na2HPO4.7H2O, KH2PO4, Oxoid yeast extract, "
    "D-glucose, and Oxoid liver digest in 900 ml deionised water; after pH "
    "adjustment to 6.9 and 10 psi pressure cooking, it adds sterile foetal calf "
    "serum to a final concentration of 10% and stores the medium at 4 C."
)

PREPARATION_STEPS: list[dict[str, Any]] = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Add casein digest, Na2HPO4.7H2O, KH2PO4, yeast extract, "
            "D-glucose, and liver digest in the order shown to 900 ml "
            "deionized water, allowing each to dissolve completely before "
            "adding the next."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": "Adjust to pH 6.9.",
    },
    {
        "step_number": 3,
        "action": "ALIQUOT",
        "description": "Dispense into 5 x 180 ml aliquots.",
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": "Sterilize by pressure cooking at 10 psi for 15 minutes.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Aseptically add 20 ml sterile foetal calf serum to each aliquot, "
            "giving a final concentration of 10%."
        ),
    },
    {
        "step_number": 6,
        "action": "STORE",
        "description": "Store at 4 C.",
    },
]


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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
        raise ValueError(f"{TARGET}: data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "curation_method:automated_expert_mapping",
    ):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated", "has_unmapped_ingredients"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{TARGET}: references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in ("CCAP:MC", SOURCE_URL):
        if reference not in found:
            references.append({"reference": reference})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Replaced malformed CCAP MC ingredients with the official PDF recipe",
        "source": SOURCE_URL,
        "notes": NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    term: tuple[str, str] | None = None,
    *,
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE_NAME,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}")

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["ingredients"] = [
        _ingredient(
            "Deionized water",
            "900",
            "ML_PER_L",
            ("CHEBI:15377", "water"),
            notes="CCAP instructs adding the first six constituents to 900 ml water.",
        ),
        _ingredient(
            "Casein digest (Casitone, cat. no. 225930)",
            "10",
            "G_PER_L",
            notes="CCAP lists 10.0 g Casitone per liter.",
        ),
        _ingredient(
            "Na2HPO4.7H2O",
            "2.5",
            "G_PER_L",
            notes="CCAP lists 2.5 g sodium phosphate heptahydrate per liter.",
        ),
        _ingredient(
            "KH2PO4",
            "0.8",
            "G_PER_L",
            ("CHEBI:63036", "potassium dihydrogen phosphate"),
            notes="CCAP lists 0.8 g KH2PO4 per liter.",
        ),
        _ingredient(
            "Yeast extract (Oxoid LP0021)",
            "5.0",
            "G_PER_L",
            ("FOODON:03315426", "yeast extract"),
            notes="CCAP lists 5.0 g Oxoid LP0021 yeast extract per liter.",
        ),
        _ingredient(
            "D-glucose",
            "2.5",
            "G_PER_L",
            ("CHEBI:17634", "D-glucose"),
            notes="CCAP lists 2.5 g D-glucose per liter.",
        ),
        _ingredient(
            "Liver digest (Oxoid LP0027)",
            "2.5",
            "G_PER_L",
            notes="CCAP lists 2.5 g Oxoid LP0027 liver digest per liter.",
        ),
        _ingredient(
            "Sterile foetal calf serum (Gamma-Irradiated, cat. no. 10109-155)",
            "100",
            "ML_PER_L",
            notes="CCAP adds 5 x 20 ml sterile foetal calf serum after sterilization.",
        ),
    ]
    _put_after(repaired, "preparation_steps", copy.deepcopy(PREPARATION_STEPS), "ingredients")
    _put_after(repaired, "ph_value", 6.9, "preparation_steps")
    _put_after(
        repaired,
        "sterilization",
        {
            "method": "AUTOCLAVE",
            "pressure": 10.0,
            "duration": "15 minutes",
            "notes": "CCAP instructs pressure cooking at 10 psi for 15 minutes.",
        },
        "ph_value",
    )
    _put_after(
        repaired,
        "storage",
        {"temperature": {"value": 4.0, "unit": "CELSIUS"}},
        "sterilization",
    )
    _put_after(repaired, "notes", NOTES, "physical_state")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


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
    raise SystemExit(main())
