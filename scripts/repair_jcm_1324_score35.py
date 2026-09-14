#!/usr/bin/env python3
"""Repair JCM Medium 1324 from its imported main-solution fragment."""

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

JCM_1324 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1324"

SOURCE = "JCM Medium 1324 / Main sol. 1324"

CURATOR = "repair_jcm_1324_score35.py"
ACTION = "RESOLVED_JCM_1324_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "L": "L",
}

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
)


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    recipe: dict[str, Any]
    references: tuple[str, ...]
    notes: str
    accepted_signatures: frozenset[frozenset[str]]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
    term: tuple[str, str],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


def _recipe() -> dict[str, Any]:
    return {
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.8,
        "ingredients": [
            _component("Distilled water", "1.0", "L", term=("CHEBI:15377", "water")),
            _component("NH4Cl", "0.5", "G_PER_L", term=("CHEBI:31206", "ammonium chloride")),
            _component(
                "K2HPO4",
                "0.7",
                "G_PER_L",
                term=("CHEBI:131527", "dipotassium hydrogen phosphate"),
            ),
            _component(
                "KH2PO4",
                "0.54",
                "G_PER_L",
                term=("CHEBI:63036", "potassium dihydrogen phosphate"),
            ),
            _component(
                "MgSO4 x 6 H2O",
                "1",
                "G_PER_L",
                term=("CHEBI:32599", "magnesium sulfate"),
            ),
            _component(
                "CaCl2 x 2 H2O",
                "0.2",
                "G_PER_L",
                term=("CHEBI:86158", "calcium chloride dihydrate"),
            ),
            _component(
                "FeSO4 x 7 H2O",
                "0.004",
                "G_PER_L",
                term=("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
            ),
            _component(
                "Methanol",
                "5",
                "ML_PER_L",
                notes=(
                    "JCM Medium 1324 / Main sol. 1324 adds sterile methanol "
                    "to a 0.5% final concentration in the sterile medium."
                ),
                term=("CHEBI:17790", "methanol"),
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Mix the salts in distilled water for the main solution; "
                    "withhold methanol until after sterilization."
                ),
            },
            {
                "step_number": 2,
                "action": "ADJUST_PH",
                "description": "Adjust pH to 6.8.",
            },
            {
                "step_number": 3,
                "action": "AUTOCLAVE",
                "description": "Sterilize the main solution.",
            },
            {
                "step_number": 4,
                "action": "MIX",
                "description": (
                    "Add sterile methanol to a final concentration of 0.5% "
                    "in the sterile medium."
                ),
            },
        ],
    }


def _signature(recipe: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "")
        for key in ("ingredients", "solutions")
        for row in recipe.get(key, [])
        if isinstance(row, dict)
    )


RECIPE = _recipe()

TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/jcm_medium_no_1324.yaml",
        record_id="CultureMech:002488",
        source_term="mediadive.medium:J1324",
        recipe=RECIPE,
        references=(JCM_1324,),
        notes=(
            "JCM Medium 1324 was repaired from its imported Main sol. 1324 "
            "fragment: defined salts in 1 L distilled water, 0.5% sterile "
            "methanol added after sterilization, and pH 6.8."
        ),
        accepted_signatures=frozenset({frozenset(), _signature(RECIPE)}),
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


def _top_level_signature(doc: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "")
        for key in ("ingredients", "solutions")
        for row in doc.get(key) or []
        if isinstance(row, dict)
    )


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.source_term}, "
            f"found {source_term!r}"
        )

    if _top_level_signature(doc) not in target.accepted_signatures:
        raise ValueError(f"{target.path}: component signature drifted")


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.references:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
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
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in target.recipe:
            repaired[recipe_field] = copy.deepcopy(target.recipe[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    repaired["notes"] = target.notes
    repaired["data_quality_flags"] = ["has_ontology_mappings", "ingredients_curated"]
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
