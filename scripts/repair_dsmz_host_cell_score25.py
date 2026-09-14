#!/usr/bin/env python3
"""Repair sparse DSMZ host-cell media left in the score-25 band."""

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

CURATOR = "repair_dsmz_host_cell_score25.py"
ACTION = "RESOLVED_DSMZ_HOST_CELL_SCORE25_GRAPH"
TIMESTAMP = "2026-09-09T00:00:00-07:00"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "temperature_value",
    "temperature_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
)

IMDM = ("mediadive.compound:1069", "IMDM-Medium")
MEM = ("mediadive.compound:1377", "MEM-Medium")
FBS = ("mediadive.compound:954", "Fetal bovine serum")
AMINOACIDS = ("mediadive.compound:1070", "Aminoacids")
LEIBOVITZ = ("mediadive.compound:1941", "Leibovitz's L-15 medium")
TRYPT_PHOS = ("mediadive.compound:1165", "Tryptose-phosphate")
GLUTAMINE = ("mediadive.compound:2161", "Glutamine")


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_source: str
    dsmz_number: str
    source_url: str
    notes: str
    recipe: dict[str, Any]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    mediadive_compound: tuple[str, str],
    chebi_term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
        "term": _term(*mediadive_compound),
    }
    if chebi_term is not None:
        row["chebi_term"] = _term(*chebi_term)
    return row


def _stock(
    preferred_term: str,
    value: str,
    *,
    source: str,
    notes: str,
    mediadive_compound: tuple[str, str],
    chebi_term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        "ML_PER_L",
        source=source,
        notes=notes,
        mediadive_compound=mediadive_compound,
        chebi_term=chebi_term,
    )


def _dsmz_50_5ml_recipe(
    *,
    dsmz_number: str,
    basal_name: str,
    basal_term: tuple[str, str],
    cell_line: str,
    temperature_value: float,
) -> dict[str, Any]:
    source = f"DSMZ Medium {dsmz_number}"
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "temperature_value": temperature_value,
        "ingredients": [
            _stock(
                basal_name,
                "891.089109",
                source=source,
                notes=(
                    f"{source} lists 45.0 ml {basal_name} in a 50.5 ml "
                    f"{cell_line} cell-culture medium batch."
                ),
                mediadive_compound=basal_term,
            ),
            _stock(
                "Fetal bovine serum",
                "99.009901",
                source=source,
                notes=(
                    f"{source} lists 5.0 ml fetal bovine serum in a 50.5 ml "
                    f"{cell_line} cell-culture medium batch."
                ),
                mediadive_compound=FBS,
            ),
            _stock(
                "Aminoacids (100 x)",
                "9.90099",
                source=source,
                notes=(
                    f"{source} lists 0.5 ml 100x amino-acid stock in a 50.5 ml "
                    f"{cell_line} cell-culture medium batch."
                ),
                mediadive_compound=AMINOACIDS,
                chebi_term=("CHEBI:33709", "amino acid"),
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    f"Combine 45.0 ml {basal_name}, 5.0 ml fetal bovine serum, "
                    "and 0.5 ml 100x amino acids."
                ),
            },
            {
                "step_number": 2,
                "action": "FILTER_STERILIZE",
                "description": "Filter sterilize through a 0.2 um membrane.",
            },
        ],
        "sterilization": {"method": "FILTER"},
    }


def _xtc_solution(name: str, l15: str, fbs: str) -> dict[str, Any]:
    source = "DSMZ Medium 1311"
    return {
        "preferred_term": name,
        "notes": f"{source} lists this as a 100 ml {name.lower()} formulation.",
        "composition": [
            _stock(
                "Leibovitz's L-15 medium",
                l15,
                source=source,
                notes=f"{source} lists {float(l15) / 10:g} ml Leibovitz 15-Medium.",
                mediadive_compound=LEIBOVITZ,
            ),
            _stock(
                "Fetal bovine serum",
                fbs,
                source=source,
                notes=f"{source} lists {float(fbs) / 10:g} ml fetal bovine serum.",
                mediadive_compound=FBS,
            ),
            _stock(
                "Tryptose-phosphate",
                "20.0",
                source=source,
                notes=f"{source} lists 2.0 ml tryptose-phosphate.",
                mediadive_compound=TRYPT_PHOS,
            ),
            _component(
                "Glutamine",
                "2.0",
                "MILLIMOLAR",
                source=source,
                notes=f"{source} lists 2.0 mM final-concentration glutamine.",
                mediadive_compound=GLUTAMINE,
                chebi_term=("CHEBI:18050", "L-glutamine"),
            ),
        ],
    }


TARGETS: tuple[Target, ...] = (
    Target(
        "bacterial/cultivation_medium_for_chlamydiae.yaml",
        "CultureMech:000636",
        "mediadive.medium:1193",
        "1193",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1193.pdf",
        (
            "DSMZ Medium 1193 prepares a 50.5 ml L929/HeLa cell-culture medium "
            "from 45.0 ml IMDM, 5.0 ml fetal bovine serum, and 0.5 ml 100x "
            "amino-acid stock, then filter-sterilizes it before Chlamydiae "
            "cultivation at 37 C plus 5% CO2."
        ),
        _dsmz_50_5ml_recipe(
            dsmz_number="1193",
            basal_name="IMDM-Medium",
            basal_term=IMDM,
            cell_line="L929/HeLa",
            temperature_value=37.0,
        ),
    ),
    Target(
        "bacterial/cultivation_medium_for_chlamydophila_pecorum.yaml",
        "CultureMech:000973",
        "mediadive.medium:1503",
        "1503",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1503.pdf",
        (
            "DSMZ Medium 1503 prepares a 50.5 ml CACO-2 cell-culture medium "
            "from 45.0 ml MEM, 5.0 ml fetal bovine serum, and 0.5 ml 100x "
            "amino-acid stock, then filter-sterilizes it before Chlamydophila "
            "pecorum cultivation at 37 C plus 5% CO2."
        ),
        _dsmz_50_5ml_recipe(
            dsmz_number="1503",
            basal_name="MEM-Medium",
            basal_term=MEM,
            cell_line="CACO-2",
            temperature_value=37.0,
        ),
    ),
    Target(
        "bacterial/vero_b4_medium.yaml",
        "CultureMech:000641",
        "mediadive.medium:1198",
        "1198",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1198.pdf",
        (
            "DSMZ Medium 1198 prepares a 50.5 ml Vero B4 cell-culture medium "
            "from 45.0 ml IMDM, 5.0 ml fetal bovine serum, and 0.5 ml 100x "
            "amino-acid stock, then filter-sterilizes it before Rickettsia "
            "cultivation at 28 C."
        ),
        _dsmz_50_5ml_recipe(
            dsmz_number="1198",
            basal_name="IMDM-Medium",
            basal_term=IMDM,
            cell_line="Vero B4",
            temperature_value=28.0,
        ),
    ),
    Target(
        "bacterial/xtc_2_medium.yaml",
        "CultureMech:000773",
        "mediadive.medium:1311",
        "1311",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1311.pdf",
        (
            "DSMZ Medium 1311 defines separate 100 ml XTC-2 culture and "
            "Diplorickettsia infection media; both use Leibovitz 15 medium, "
            "fetal bovine serum, tryptose-phosphate, and 2 mM final "
            "glutamine, with lower serum and higher Leibovitz 15 in the "
            "infection medium."
        ),
        {
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "temperature_value": 28.0,
            "ingredients": [],
            "solutions": [
                _xtc_solution("XTC-2 cell culture medium", "930.0", "50.0"),
                _xtc_solution("XTC-2 infection medium", "960.0", "20.0"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Prepare the XTC-2 cell culture medium with 93.0 ml "
                        "Leibovitz 15-Medium, 5.0 ml fetal bovine serum, "
                        "2.0 ml tryptose-phosphate, and 2.0 mM glutamine."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "FILTER_STERILIZE",
                    "description": "Filter sterilize through a 0.2 um membrane.",
                },
                {
                    "step_number": 3,
                    "action": "MIX",
                    "description": (
                        "Exchange to the XTC-2 infection medium made with "
                        "96.0 ml Leibovitz 15-Medium, 2.0 ml fetal bovine "
                        "serum, 2.0 ml tryptose-phosphate, and 2.0 mM "
                        "glutamine for Diplorickettsia cultivation."
                    ),
                },
            ],
            "sterilization": {"method": "FILTER"},
        },
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str | None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return None
    term = media_term.get("term")
    if not isinstance(term, dict):
        return None
    term_id = term.get("id")
    return str(term_id) if term_id else None


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


def _grounded(row: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = row.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        composition = solution.get("composition") or []
        if isinstance(composition, list):
            components.extend(row for row in composition if isinstance(row, dict))
    return components


def _ensure_flags(doc: dict[str, Any], target: Target) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{target.path}: data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    components = _components(doc)
    has_grounding = any(_grounded(row) for row in components)
    has_unmapped = any(not _grounded(row) for row in components)

    if has_grounding and "has_ontology_mappings" not in flags:
        flags.append("has_ontology_mappings")
    elif not has_grounding and "has_ontology_mappings" in flags:
        flags.remove("has_ontology_mappings")

    if has_unmapped and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")
    elif not has_unmapped and "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    if not has_grounding:
        raise ValueError(f"{target.path}: repaired recipe has no grounded components")


def _ensure_reference(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    if not any(
        isinstance(row, dict) and row.get("reference") == target.source_url for row in references
    ):
        references.append({"reference": target.source_url})


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": f"Resolved DSMZ Medium {target.dsmz_number} host-cell recipe",
        "source": target.source_url,
        "notes": target.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.path}: curation_history is not a list")

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
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: found id {doc.get('id')!r}, " f"expected {target.expected_id!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.expected_source:
        raise ValueError(
            f"{target.path}: found source term {source_term!r}, "
            f"expected {target.expected_source!r}"
        )

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in target.recipe:
            repaired[field] = copy.deepcopy(target.recipe[field])
        else:
            repaired.pop(field, None)

    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired, target)
    _ensure_reference(repaired, target)
    _ensure_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        repaired = repair_record(_load(path), target)
        if path.read_bytes() != dump_record(repaired).encode("utf-8"):
            plans[path] = repaired
    return plans


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    plans = plan_repairs()
    if args.dry_run:
        for path in plans:
            print(f"would update {path.relative_to(REPO)}")
        print(f"would update {len(plans)} DSMZ host-cell score-25 records")
        return

    changed = 0
    for path, doc in plans.items():
        if write_record(path, doc):
            changed += 1
    print(f"updated {changed} DSMZ host-cell score-25 records")


if __name__ == "__main__":
    main()
