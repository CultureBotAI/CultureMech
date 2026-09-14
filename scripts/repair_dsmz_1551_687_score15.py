#!/usr/bin/env python3
"""Repair DSMZ 1551 and 687 score-15 records."""

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

CURATOR = "repair_dsmz_1551_687_score15.py"
ACTION = "RESOLVED_DSMZ_1551_687_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

DSMZ_687 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium687.pdf"
DSMZ_1551 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1551.pdf"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    source_label: str
    imported_signature: tuple[Component, ...]
    ingredients: tuple[dict[str, Any], ...]
    preparation_steps: tuple[dict[str, Any], ...]
    reference_url: str
    notes: str
    ph_value: float | None = None


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


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


def _dsmz_1551_ingredients() -> tuple[dict[str, Any], ...]:
    source = "DSMZ Medium 1551"
    product_source = "DSMZ Medium 1551 / Oxoid nutrient broth"
    return (
        _ingredient(
            "Nutrient broth (Oxoid)",
            "13",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists 13 g of the Oxoid nutrient broth product; the "
                "recipe also discloses the dehydrated product composition."
            ),
        ),
        _ingredient(
            "NaCl",
            "17.5",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 17.5 g additional NaCl outside the Oxoid product.",
            term=("CHEBI:26710", "sodium chloride"),
        ),
        _ingredient(
            "Distilled water",
            "1000",
            "ML_PER_L",
            source=source,
            notes=f"{source} lists 1000 mL distilled water for the final medium.",
            term=("CHEBI:15377", "water"),
        ),
        _ingredient(
            "Lab-Lemco beef extract",
            "1",
            "G_PER_L",
            source=product_source,
            notes="Oxoid nutrient broth contributes 1 g/L Lab-Lemco beef extract.",
            term=("FOODON:03302088", "beef extract"),
        ),
        _ingredient(
            "Yeast extract",
            "2",
            "G_PER_L",
            source=product_source,
            notes="Oxoid nutrient broth contributes 2 g/L yeast extract.",
            term=("FOODON:03315426", "yeast extract"),
        ),
        _ingredient(
            "Peptone",
            "5",
            "G_PER_L",
            source=product_source,
            notes="Oxoid nutrient broth contributes 5 g/L peptone.",
            term=("FOODON:03302071", "peptone"),
        ),
        _ingredient(
            "NaCl",
            "5",
            "G_PER_L",
            source=product_source,
            notes="Oxoid nutrient broth contributes 5 g/L NaCl.",
            term=("CHEBI:26710", "sodium chloride"),
        ),
    )


def _dsmz_687_ingredients() -> tuple[dict[str, Any], ...]:
    source = "DSMZ Medium 687"
    return (
        _ingredient(
            "Bacto Panton (Peptone)",
            "10",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists Bacto Panton as a peptone in the Columbia "
                "Blood Agar Base; the BD product is not reducible to one ChEBI molecule."
            ),
        ),
        _ingredient(
            "Bacto Bitone (Peptone)",
            "10",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists Bacto Bitone as a peptone in the Columbia "
                "Blood Agar Base; the BD product is not reducible to one ChEBI molecule."
            ),
        ),
        _ingredient(
            "Tryptic Digest of beef heart",
            "3",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists tryptic digest of beef heart as part of the "
                "Columbia Blood Agar Base."
            ),
        ),
        _ingredient(
            "Corn starch",
            "1",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 1 g corn starch.",
            term=("CHEBI:28017", "starch"),
        ),
        _ingredient(
            "NaCl",
            "5",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 5 g NaCl.",
            term=("CHEBI:26710", "sodium chloride"),
        ),
        _ingredient(
            "Agar",
            "15",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 15 g agar.",
            term=("CHEBI:2509", "agar"),
        ),
        _ingredient(
            "Deionized water",
            "1000",
            "ML_PER_L",
            source=source,
            notes=f"{source} instructs suspending Columbia Blood Agar Base in 1 L deionized water.",
            term=("CHEBI:15377", "water"),
        ),
        _ingredient(
            "Sterile defibrinated blood",
            "5",
            "PERCENT_V_V",
            source=source,
            notes=f"{source} instructs adding 5% sterile defibrinated blood after cooling.",
            term=("UBERON:0000178", "blood"),
        ),
    )


TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/948_oxoid_nutrient_broth_with_additonal_salt.yaml",
        record_id="CultureMech:001029",
        source_term="mediadive.medium:1551",
        source_label="DSMZ Medium 1551",
        imported_signature=(
            ("NaCl", "22.5", "G_PER_L"),
            ("Lab-Lemco beef extract", "1", "G_PER_L"),
            ("Yeast extract", "2", "G_PER_L"),
            ("Peptone", "5", "G_PER_L"),
        ),
        ingredients=_dsmz_1551_ingredients(),
        preparation_steps=(
            _step(
                1,
                "MIX",
                "Dissolve 13 g Oxoid nutrient broth and 17.5 g NaCl in 1000 mL distilled water.",
            ),
            _step(2, "ADJUST_PH", "Adjust pH to 7.2."),
        ),
        ph_value=7.2,
        reference_url=DSMZ_1551,
        notes=(
            "DSMZ Medium 1551 lists 13 g Nutrient broth (Oxoid), 17.5 g "
            "additional NaCl, 1000 mL distilled water, and pH 7.2; the Oxoid "
            "product composition contributes 1 g Lab-Lemco, 2 g yeast extract, "
            "5 g peptone, and 5 g NaCl per liter."
        ),
    ),
    Target(
        path="bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml",
        record_id="CultureMech:001823",
        source_term="mediadive.medium:687",
        source_label="DSMZ Medium 687",
        imported_signature=(
            ("Defibrinated Blood", "50", "G_PER_L"),
            ("Bacto Panton", "10", "G_PER_L"),
            ("Bacto Bitone", "10", "G_PER_L"),
            ("Tryptic Digest of beef heart", "3", "G_PER_L"),
            ("Corn starch", "1", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        ingredients=_dsmz_687_ingredients(),
        preparation_steps=(
            _step(
                1,
                "DISSOLVE",
                "Suspend 44 g Columbia Blood Agar Base in 1 L deionized water and heat to boiling.",
            ),
            _step(2, "AUTOCLAVE", "Sterilize in an autoclave for 15 min at 121 C."),
            _step(3, "COOL", "Cool to 45 C, add 5% sterile defibrinated blood, and mix well."),
        ),
        reference_url=DSMZ_687,
        notes=(
            "DSMZ Medium 687 lists Columbia Blood Agar Base as Bacto Panton, "
            "Bacto Bitone, tryptic digest of beef heart, corn starch, NaCl, "
            "and agar suspended in 1 L deionized water; after sterilization "
            "and cooling it adds 5% sterile defibrinated blood."
        ),
    ),
)
TARGET_BY_PATH: dict[str, Target] = {target.path: target for target in TARGETS}


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


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
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


def _recipe_signature(target: Target) -> tuple[Component, ...]:
    return _signature(list(target.ingredients), "target ingredients")


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.source_term}, found {source_term!r}"
        )

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in {target.imported_signature, _recipe_signature(target)}:
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


def _ensure_reference(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    if target.reference_url not in existing:
        references.append({"reference": target.reference_url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": target.reference_url,
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
    if target.ph_value is not None:
        _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    repaired["ingredients"] = copy.deepcopy(list(target.ingredients))
    repaired["preparation_steps"] = copy.deepcopy(list(target.preparation_steps))
    _ensure_flags(repaired)
    _ensure_reference(repaired, target)
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
