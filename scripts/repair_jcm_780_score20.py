#!/usr/bin/env python3
"""Repair JCM 780 Patel/Desulfotomaculum varum score-20 composition."""

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
TARGET = Path("bacterial/patel_laboratory_medium_with_glycerin.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_780_score20.py"
ACTION = "RESOLVED_JCM_780_SCORE20_GRAPH"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"
JCM_684 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684"
JCM_780 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=780"

EXPECTED_ID = "CultureMech:003123"
EXPECTED_MEDIA_TERM = "mediadive.medium:J780"

NOTES = (
    "JCM Medium 780 contains mineral salts, HEPES, 1.0 ml/L Trace vitamins "
    "from JCM Medium 197, 1.0 ml/L Trace mineral solution from JCM Medium "
    "684, 0.2 g/L yeast extract, 2.84 g/L sodium sulfate, 1.0 L distilled "
    "water, and 10.0 ml/L 20% glycerin solution; the pH is adjusted to 7.0."
)

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    term: tuple[str, str],
    *,
    source: str = "JCM Medium 780",
    unit: str = "G_PER_L",
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {unit.lower().replace('_per_l', '/L')}.",
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term) if term[0].startswith("CHEBI:") else None,
    }


def _drop_none(row: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in row.items() if value is not None}


def _stock_component(
    preferred_term: str,
    value: str,
    term: tuple[str, str],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "G_PER_L"},
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


RECIPE: dict[str, Any] = {
    "medium_type": "COMPLEX",
    "composition_type": "UNDEFINED",
    "physical_state": "LIQUID",
    "ph_value": 7.0,
    "ingredients": [
        _drop_none(_ingredient("NH4Cl", "1.0", ("CHEBI:31206", "ammonium chloride"))),
        _drop_none(
            _ingredient(
                "K2HPO4",
                "0.6",
                ("CHEBI:131527", "dipotassium hydrogen phosphate"),
            )
        ),
        _drop_none(_ingredient("KH2PO4", "0.3", ("CHEBI:63036", "potassium dihydrogen phosphate"))),
        _drop_none(
            _ingredient(
                "MgCl2 x 6 H2O",
                "0.1",
                ("CHEBI:86345", "magnesium dichloride hexahydrate"),
            )
        ),
        _drop_none(
            _ingredient(
                "CaCl2 x 2 H2O",
                "0.1",
                ("CHEBI:86158", "calcium chloride dihydrate"),
            )
        ),
        _drop_none(_ingredient("NaCl", "1.0", ("CHEBI:26710", "sodium chloride"))),
        _drop_none(_ingredient("HEPES", "12.0", ("CHEBI:46756", "HEPES"))),
        _drop_none(
            _ingredient(
                "Yeast extract",
                "0.2",
                ("FOODON:03315426", "yeast extract"),
            )
        ),
        _drop_none(_ingredient("Na2SO4", "2.84", ("CHEBI:32149", "sodium sulfate"))),
        _drop_none(
            _ingredient(
                "Distilled water",
                "1000",
                ("CHEBI:15377", "water"),
                unit="ML_PER_L",
            )
        ),
    ],
    "solutions": [
        {
            "preferred_term": "Trace vitamins",
            "concentration": {"value": "1.0", "unit": "ML_PER_L"},
            "notes": "JCM Medium 780 lists 1.0 ml/L Trace vitamins from JCM Medium 197.",
        },
        {
            "preferred_term": "Trace mineral solution",
            "concentration": {"value": "1.0", "unit": "ML_PER_L"},
            "notes": (
                "JCM Medium 780 lists 1.0 ml/L Trace mineral solution from " "JCM Medium 684."
            ),
        },
        {
            "preferred_term": "20% (w/v) Glycerin solution",
            "concentration": {"value": "10.0", "unit": "ML_PER_L"},
            "notes": "JCM Medium 780 adds 10.0 ml/L 20% (w/v) Glycerin solution.",
            "composition": [_stock_component("Glycerol", "200.0", ("CHEBI:17754", "glycerol"))],
            "preparation_notes": (
                "JCM Medium 780 uses a 20% (w/v) stock; the composition is "
                "normalized to g/L of stock."
            ),
        },
    ],
    "preparation_steps": [
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Mix the salts, HEPES, trace solutions, yeast extract, sodium sulfate, and distilled water.",
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 7.0.",
        },
        {
            "step_number": 3,
            "action": "AUTOCLAVE",
            "description": "Autoclave under a N2 atmosphere.",
        },
        {
            "step_number": 4,
            "action": "MIX",
            "description": "After cooling, aseptically and anaerobically add 10.0 ml/L 20% glycerin solution.",
        },
    ],
    "sterilization": {"method": "AUTOCLAVE"},
}


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


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        row
        for rows in (doc.get("ingredients") or [], doc.get("solutions") or [])
        for row in rows
        if isinstance(row, dict)
    ]


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    if any(_grounded(component) for component in _components(doc)):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    if any(not _grounded(component) for component in _components(doc)):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    doc["data_quality_flags"] = list(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in (JCM_780, JCM_197, JCM_684):
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join((JCM_780, JCM_197, JCM_684)),
        "notes": NOTES,
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


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in RECIPE:
            repaired[recipe_field] = copy.deepcopy(RECIPE[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    repaired["notes"] = NOTES
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repair(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repair(args.normalized_dir)
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
    sys.exit(main())
