#!/usr/bin/env python3
"""Repair DSMZ Medium 1007 trace-element stock source duplicates."""

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

CURATOR = "repair_dsmz_1007_trace_stock_score15.py"
ACTION = "RESOLVED_DSMZ_1007_TRACE_STOCK_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

DSMZ_1007_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1007.pdf"
MEDIADIVE_1007 = "https://mediadive.dsmz.de/medium/1007"
SOURCE = "DSMZ Medium 1007"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_source_term: str
    source_label: str
    revised_original_name: str | None = None


TARGETS: tuple[Target, ...] = (
    Target(
        "bacterial/KOMODO_1007_MINERAL_MEDIUM.yaml",
        "CultureMech:003510",
        "komodo.medium:1007",
        "KOMODO Medium 1007",
    ),
    Target(
        "bacterial/dsm_15672.yaml",
        "CultureMech:003507",
        "komodo.medium:1007.1",
        "KOMODO Medium 1007.1",
        "MINERAL MEDIUM for DSM 15672",
    ),
    Target(
        "bacterial/dsm_15673.yaml",
        "CultureMech:003508",
        "komodo.medium:1007.2",
        "KOMODO Medium 1007.2",
        "MINERAL MEDIUM for DSM 15673",
    ),
    Target(
        "bacterial/dsm_16984_dsm_24478_24479_24480_24481_24492_24493_and_24527.yaml",
        "CultureMech:003509",
        "komodo.medium:1007.3",
        "KOMODO Medium 1007.3",
        (
            "MINERAL MEDIUM for DSM 16984, DSM 24478, DSM 24479, "
            "DSM 24480, DSM 24481, DSM 24492, DSM 24493, and DSM 24527"
        ),
    ),
    Target(
        "bacterial/mineral_medium.yaml",
        "CultureMech:000423",
        "mediadive.medium:1007",
        "DSMZ Medium 1007",
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}
KOMODO_PARENT_PATH = "data/normalized_yaml/bacterial/KOMODO_1007_MINERAL_MEDIUM.yaml"
KOMODO_PARENT_ID = "CultureMech:003510"
KOMODO_PARENT_NAME = "mineral_medium"
MEDIADIVE_PARENT_PATH = "data/normalized_yaml/bacterial/mineral_medium.yaml"
MEDIADIVE_PARENT_ID = "CultureMech:000423"
MEDIADIVE_PARENT_NAME = "mineral_medium"


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


GROUNDINGS: dict[str, tuple[str, str]] = {
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 5 H2O": ("CHEBI:91245", "copper(II) chloride pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "EDTA": ("CHEBI:4735", "ethylenediaminetetraacetic acid"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "KNO3": ("CHEBI:63043", "potassium nitrate"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "Na2MoO4": ("CHEBI:75215", "sodium molybdate (anhydrous)"),
    "NiCl2 x 6 H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}


IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("KNO3", "0.25", "G_PER_L"),
    ("KH2PO4", "0.1", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.05", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.01", "G_PER_L"),
    ("EDTA", "5", "G_PER_L"),
    ("CuCl2 x 5 H2O", "0.1", "G_PER_L"),
    ("FeSO4 x 7 H2O", "2", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.02", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.2", "G_PER_L"),
    ("Na2MoO4", "0.03", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.03", "G_PER_L"),
)


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    notes: str,
) -> dict[str, Any]:
    term = _term(*GROUNDINGS[preferred_term])
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
        "term": term,
        "mediaingredientmech_chebi_term": copy.deepcopy(term),
    }


def _main_note(name: str, amount: str) -> str:
    return f"DSMZ Medium 1007 lists {amount} {name} in the main 1000 ml solution."


def _trace_note(name: str, amount: str) -> str:
    return f"DSMZ Medium 1007 lists {amount} {name} in the trace elements stock."


MAIN_INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component("KNO3", "0.25", "G_PER_L", _main_note("KNO3", "250.0 mg")),
    _component("KH2PO4", "0.1", "G_PER_L", _main_note("KH2PO4", "100.0 mg")),
    _component(
        "MgSO4 x 7 H2O",
        "0.05",
        "G_PER_L",
        _main_note("MgSO4 x 7 H2O", "50.0 mg"),
    ),
    _component(
        "CaCl2 x 2 H2O",
        "0.01",
        "G_PER_L",
        _main_note("CaCl2 x 2 H2O", "10.0 mg"),
    ),
    _component(
        "Distilled water",
        "1000.0",
        "ML_PER_L",
        "DSMZ Medium 1007 makes the main solution with 1000.0 ml distilled water.",
    ),
)

TRACE_COMPONENTS: tuple[dict[str, Any], ...] = (
    _component("EDTA", "5.00", "G_PER_L", _trace_note("EDTA", "5.00 g")),
    _component(
        "CuCl2 x 5 H2O",
        "0.10",
        "G_PER_L",
        _trace_note("CuCl2 x 5 H2O", "0.10 g"),
    ),
    _component(
        "FeSO4 x 7 H2O",
        "2.00",
        "G_PER_L",
        _trace_note("FeSO4 x 7 H2O", "2.00 g"),
    ),
    _component(
        "ZnSO4 x 7 H2O",
        "0.10",
        "G_PER_L",
        _trace_note("ZnSO4 x 7 H2O", "0.10 g"),
    ),
    _component(
        "NiCl2 x 6 H2O",
        "0.02",
        "G_PER_L",
        _trace_note("NiCl2 x 6 H2O", "0.02 g"),
    ),
    _component(
        "CoCl2 x 6 H2O",
        "0.20",
        "G_PER_L",
        _trace_note("CoCl2 x 6 H2O", "0.20 g"),
    ),
    _component("Na2MoO4", "0.03", "G_PER_L", _trace_note("Na2MoO4", "0.03 g")),
    _component(
        "MnCl2 x 4 H2O",
        "0.03",
        "G_PER_L",
        _trace_note("MnCl2 x 4 H2O", "0.03 g"),
    ),
    _component(
        "Distilled water",
        "1000.00",
        "ML_PER_L",
        "DSMZ Medium 1007 makes the trace elements stock with 1000.00 ml distilled water.",
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Trace elements",
        "concentration": {"value": "1.0", "unit": "ML_PER_L"},
        "composition": copy.deepcopy(list(TRACE_COMPONENTS)),
        "source": SOURCE,
        "notes": "DSMZ Medium 1007 adds 1.0 ml/L trace elements stock.",
    },
)

PH_RANGE = {"min": 5.5, "max": 6.0}
PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust the final medium to pH 5.5-6.0.",
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": "Use shaking incubation for strains grown on methane.",
    },
)

REFERENCES = (MEDIADIVE_1007, DSMZ_1007_PDF)
NOTES = (
    "DSMZ Medium 1007 defines Mineral Medium with KNO3, KH2PO4, MgSO4 x 7 H2O, "
    "CaCl2 x 2 H2O, 1.0 ml/L trace elements, and distilled water at final pH "
    "5.5-6.0. The trace elements stock contains EDTA, CuCl2 x 5 H2O, FeSO4 x "
    "7 H2O, ZnSO4 x 7 H2O, NiCl2 x 6 H2O, CoCl2 x 6 H2O, Na2MoO4, MnCl2 x "
    "4 H2O, and distilled water per liter."
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in MAIN_INGREDIENTS
)
FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (
        "Trace elements",
        "1.0",
        "ML_PER_L",
        tuple(
            (
                str(row["preferred_term"]),
                str(row["concentration"]["value"]),
                str(row["concentration"]["unit"]),
            )
            for row in TRACE_COMPONENTS
        ),
    ),
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


def _ingredient_signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
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


def _solution_signatures(rows: Any) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in rows:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"solution {solution.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _ingredient_signature(solution.get("composition")),
            )
        )
    return tuple(signatures)


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != target.expected_source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.expected_source_term}, "
            f"found {source_term!r}"
        )

    signatures = (
        _ingredient_signature(doc.get("ingredients")),
        _solution_signatures(doc.get("solutions")),
    )
    if signatures not in {
        (IMPORTED_INGREDIENT_SIGNATURE, ()),
        (FINAL_INGREDIENT_SIGNATURE, FINAL_SOLUTION_SIGNATURES),
    }:
        raise ValueError(
            f"{target.path}: ingredient/solution signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {signatures!r}"
        )


def _put_after(doc: dict[str, Any], key: str, value: Any, after_key: str) -> None:
    rebuilt: dict[str, Any] = {}
    placed = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        rebuilt[existing_key] = existing_value
        if existing_key == after_key:
            rebuilt[key] = value
            placed = True
    if not placed:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


def _child_entry(child: Target) -> dict[str, Any]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": "SOURCE_DUPLICATE",
        "id": child.expected_id,
        "name": Path(child.path).stem,
        "notes": (
            f"{child.source_label} resolves to the same DSMZ Medium 1007 "
            "Mineral Medium formulation."
        ),
    }


def _ensure_links(doc: dict[str, Any], target: Target) -> None:
    if target.expected_id == KOMODO_PARENT_ID:
        doc["variant_children"] = [
            _child_entry(child)
            for child in TARGETS
            if child.expected_id
            in {
                "CultureMech:003507",
                "CultureMech:003508",
                "CultureMech:003509",
            }
        ]
        doc["parent_media"] = {
            "path": MEDIADIVE_PARENT_PATH,
            "relationship": "SOURCE_DUPLICATE",
            "id": MEDIADIVE_PARENT_ID,
            "name": MEDIADIVE_PARENT_NAME,
            "notes": "KOMODO Medium 1007 resolves to official DSMZ Medium 1007.",
        }
        doc["variant_relationship"] = "SOURCE_DUPLICATE"
        doc["variant_modifications"] = [
            "Same DSMZ Medium 1007 formulation in the KOMODO and MediaDive source records."
        ]
        return

    if target.expected_id == MEDIADIVE_PARENT_ID:
        doc["variant_children"] = [
            {
                "path": KOMODO_PARENT_PATH,
                "relationship": "SOURCE_DUPLICATE",
                "id": KOMODO_PARENT_ID,
                "name": KOMODO_PARENT_NAME,
                "notes": "KOMODO Medium 1007 resolves to official DSMZ Medium 1007.",
            }
        ]
        return

    doc["parent_media"] = {
        "path": KOMODO_PARENT_PATH,
        "relationship": "SOURCE_DUPLICATE",
        "id": KOMODO_PARENT_ID,
        "name": KOMODO_PARENT_NAME,
    }
    doc["variant_relationship"] = "SOURCE_DUPLICATE"
    doc["variant_modifications"] = [
        f"{target.source_label} resolves to DSMZ Medium 1007 for the named DSM strain."
    ]


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag
        not in {
            "has_unmapped_ingredients",
            "incomplete_composition",
            "needs_manual_curation",
        }
    ]
    flags.extend(("has_ontology_mappings", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_1007_PDF,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    if target.revised_original_name is not None:
        repaired["original_name"] = target.revised_original_name
    repaired["ph_range"] = copy.deepcopy(PH_RANGE)
    repaired["ingredients"] = copy.deepcopy(list(MAIN_INGREDIENTS))
    _put_after(repaired, "ph_range", repaired.pop("ph_range"), "physical_state")
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "solutions")
    _ensure_links(repaired, target)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
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
