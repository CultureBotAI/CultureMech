#!/usr/bin/env python3
"""Repair the TOGO M976 / JCM J930 Leibovitz L-15 FBS duplicate cluster."""

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
TOGO_PATH = Path("bacterial/TOGO_M976_Leibovitz_s_L-15_Medium_With_10_FBS_And_1.5_NaCl.yaml")
J930_PATH = Path("bacterial/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml")
SOLUTION_PATH = Path("bacterial/mediadive_4941_Main_sol_J930.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m976_leibovitz_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M976 = "https://togomedium.org/medium/M976"
MEDIADIVE_J930 = "https://mediadive.dsmz.de/medium/J930"
JCM_930 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=930"
SOURCE = "JCM Medium 930"
TOGO_SOURCE = "TOGO M976 / JCM Medium 930"
MEDIADIVE_SOURCE = "MediaDive J930 / JCM Medium 930"

LEIBOVITZ = ("mediadive.compound:1941", "Leibovitz's L-15 medium")
FBS = ("mediadive.compound:954", "Fetal bovine serum")
NACL_MEDIADIVE = ("mediadive.compound:43", "NaCl")
NACL_CHEBI = ("CHEBI:26710", "sodium chloride")

Component = tuple[str, str, str]

TOGO_IMPORTED: tuple[Component, ...] = (
    ("NaCl", "15", "G_PER_L"),
    ("Fetal bovine serum", "100", "G_PER_L"),
    ("Leibovitz's L--15 medium", "1", "G_PER_L"),
)

J930_IMPORTED: tuple[Component, ...] = (
    ("Leibovitz's L-15 medium", "1000", "G_PER_L"),
    ("Fetal bovine serum", "100", "G_PER_L"),
    ("NaCl", "13.6364", "G_PER_L"),
)

SOLUTION_IMPORTED: tuple[Component, ...] = (
    ("Leibovitz's L-15 medium", "909.090909090909", "PERCENT_V_V"),
    ("Fetal bovine serum", "90.9090909090909", "PERCENT_V_V"),
    ("NaCl", "13.6364", "G_PER_L"),
)

FINAL_SIGNATURE: tuple[Component, ...] = (
    ("Leibovitz's L-15 medium", "1.0", "L"),
    ("Fetal bovine serum", "100.0", "ML_PER_L"),
    ("NaCl", "15.0", "G_PER_L"),
)

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
}


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    solution: bool = False,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if preferred_term == "Leibovitz's L-15 medium":
        row["term"] = _term(*LEIBOVITZ)
    elif preferred_term == "Fetal bovine serum":
        row["term"] = _term(*FBS)
    elif solution:
        row["term"] = _term(*NACL_MEDIADIVE)
        row["chebi_term"] = _term(*NACL_CHEBI)
    else:
        row["term"] = _term(*NACL_CHEBI)
        row["mediaingredientmech_chebi_term"] = _term(*NACL_CHEBI)
        row["physicochemical_roles"] = ["OSMOTIC_AGENT"]
    return row


def _composition(source: str, *, solution: bool = False) -> list[dict[str, Any]]:
    return [
        _component(name, value, unit, source=source, solution=solution)
        for name, value, unit in FINAL_SIGNATURE
    ]


def _prep() -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Combine the JCM Medium 930 Leibovitz L-15, fetal bovine serum, and NaCl components.",
        },
        {
            "step_number": 2,
            "action": "FILTER_STERILIZE",
            "description": "Filter-sterilize with a 0.22 um PES filter.",
        },
    ]


def _sterilization() -> dict[str, str]:
    return {"method": "FILTER", "notes": "0.22 um PES filter"}


def _ensure_media(
    doc: dict[str, Any],
    *,
    expected_id: str,
    media_term: str,
    imported: tuple[Component, ...],
) -> None:
    if doc.get("id") != expected_id:
        raise ValueError(f"expected {expected_id}, found {doc.get('id')}")
    if _source_term_id(doc) != media_term:
        raise ValueError(f"expected media term {media_term}, found {_source_term_id(doc)!r}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        imported,
        FINAL_SIGNATURE,
    ):
        raise ValueError("ingredient signature drifted")


def _ensure_solution(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:013867":
        raise ValueError(f"expected CultureMech:013867, found {doc.get('id')}")
    term = doc.get("term")
    if not isinstance(term, dict) or term.get("id") != "mediadive.solution:4941":
        raise ValueError("expected mediadive.solution:4941")
    if _signature(doc.get("composition"), "composition") not in (
        SOLUTION_IMPORTED,
        FINAL_SIGNATURE,
    ):
        raise ValueError("solution composition signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
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


def _append_event(
    doc: dict[str, Any],
    *,
    action: str,
    references: tuple[str, ...],
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(references),
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


def _repair_base(doc: dict[str, Any], *, source: str) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ingredients"] = _composition(source)
    repaired["preparation_steps"] = _prep()
    repaired["sterilization"] = _sterilization()
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("kg_microbe_match", None)
    _put_after(
        repaired,
        "notes",
        (
            "JCM Medium 930 lists 1.0 L Leibovitz's L-15 medium, 100.0 ml "
            "Fetal bovine serum, and 15.0 g NaCl; filter-sterilize with a "
            "0.22 um PES filter."
        ),
        "media_term",
    )
    _ensure_flags(repaired)
    return repaired


def repair_togo(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_media(
        doc,
        expected_id="CultureMech:010402",
        media_term="TOGO:M976",
        imported=TOGO_IMPORTED,
    )
    repaired = _repair_base(doc, source=TOGO_SOURCE)
    _put_after(
        repaired,
        "parent_media",
        {
            "path": f"data/normalized_yaml/{J930_PATH}",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:003278",
            "name": "leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl",
            "notes": (
                "TOGO M976 imports the same JCM Medium 930 Leibovitz L-15 "
                "with 10% FBS and 1.5% NaCl formulation represented by "
                "MediaDive J930."
            ),
        },
        "sterilization",
    )
    repaired["variant_relationship"] = "SOURCE_DUPLICATE"
    repaired["variant_modifications"] = [
        "TOGO M976 imports the same JCM Medium 930 formulation represented by MediaDive J930."
    ]
    _ensure_references(repaired, (TOGO_M976, JCM_930))
    _append_event(
        repaired,
        action="RESOLVED_TOGO_M976_LEIBOVITZ_FBS",
        references=(TOGO_M976, JCM_930),
        notes=(
            "Corrected the TOGO M976 volume imports, fixed the L-15 medium "
            "name, grounded NaCl to CHEBI, linked the disclosed L-15 and FBS "
            "products to MediaDive compound IDs, and linked MediaDive J930 as "
            "the source duplicate parent."
        ),
    )
    return repaired


def repair_j930(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_media(
        doc,
        expected_id="CultureMech:003278",
        media_term="mediadive.medium:J930",
        imported=J930_IMPORTED,
    )
    repaired = _repair_base(doc, source=MEDIADIVE_SOURCE)
    _put_after(
        repaired,
        "variant_children",
        [
            {
                "path": f"data/normalized_yaml/{TOGO_PATH}",
                "relationship": "SOURCE_DUPLICATE",
                "id": "CultureMech:010402",
                "name": "leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl",
                "notes": (
                    "TOGO M976 imports the same JCM Medium 930 Leibovitz "
                    "L-15 with 10% FBS and 1.5% NaCl formulation represented "
                    "by MediaDive J930."
                ),
            }
        ],
        "sterilization",
    )
    _ensure_references(repaired, (MEDIADIVE_J930, JCM_930))
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_J930_LEIBOVITZ_FBS",
        references=(MEDIADIVE_J930, JCM_930),
        notes=(
            "Corrected MediaDive J930 volume scaling, grounded NaCl to CHEBI, "
            "linked the disclosed L-15 and FBS products to MediaDive compound "
            "IDs, removed the stale MediaDive 74 KG match, and linked TOGO "
            "M976 as a source duplicate."
        ),
    )
    return repaired


def repair_solution(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution(doc)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _composition(MEDIADIVE_SOURCE, solution=True)
    repaired.pop("ingredients", None)
    repaired.pop("data_quality_flags", None)
    repaired["preparation_notes"] = "Filter-sterilize with a 0.22 um PES filter."
    repaired["notes"] = (
        "MediaDive solution 4941 is the JCM Medium 930 main-solution import "
        "for Leibovitz's L-15 Medium With 10% FBS And 1.5% NaCl."
    )
    _ensure_references(repaired, (MEDIADIVE_J930, JCM_930))
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_4941_LEIBOVITZ_FBS",
        references=(MEDIADIVE_J930, JCM_930),
        notes=(
            "Replaced the rescaled PERCENT_V_V MediaDive J930 stock import "
            "and stale placeholder ingredient with the official JCM Medium "
            "930 quantities."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / TOGO_PATH: repair_togo(_load(normalized / TOGO_PATH)),
        normalized / J930_PATH: repair_j930(_load(normalized / J930_PATH)),
        normalized / SOLUTION_PATH: repair_solution(_load(normalized / SOLUTION_PATH)),
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
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
