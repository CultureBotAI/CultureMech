#!/usr/bin/env python3
"""Repair source-equivalent JCM Medium 10 duplicate records."""

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
import repair_togo_m172_score15 as togo_m172  # noqa: E402
import repair_togo_m203_score15 as togo_m203  # noqa: E402
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_medium_10_duplicates_score15.py"
ACTION = "RESOLVED_JCM_MEDIUM_10_DUPLICATE_SCORE15"
LINK_ACTION = "LINKED_JCM_MEDIUM_10_SOURCE_DUPLICATE"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Target:
    path: Path
    parent_path: Path
    expected_id: str
    expected_media_term: str
    original_name: str
    physical_state: str
    togo_module: Any
    current_ingredient_signature: tuple[Component, ...]
    current_solution_signatures: tuple[SolutionSignature, ...]
    notes: str
    source_duplicate_note: str
    variant_modification: str


M172_NOTES = (
    "MediaDive JCM J179 duplicates the JCM Medium 179 Medium 10 Broth "
    "formulation preserved by TOGO M172. TOGO M172 records 850 ml distilled "
    "water, 0.5 g each of cellobiose, glucose, soluble starch, and Yeast "
    "extract from BD-Difco, 2 g Trypticase peptone from BD-BBL, 0.5 ml 0.1% "
    "Resazurin solution, 0.5 ml 0.2% Hemin solution, 100 ml 4% Na2SO3 "
    "solution, 2 ml 25% L-Ascorbic acid solution, 10 ml 5% L-Cysteine HCl "
    "H2O solution, and VFA and salt stocks from Medium 10 / TOGO M124, with "
    "pH adjusted to 6.7-6.8. It omits agar and Toray silicone from the JCM "
    "Medium 133 Medium 10 formulation. The current JCM Medium 179 URL no "
    "longer exposes the recipe."
)

M203_NOTES = (
    "MediaDive JCM J210 duplicates the JCM Medium 210 Modified Medium 10 "
    "formulation preserved by TOGO M203. TOGO M203 records 850 ml distilled "
    "water, 0.5 g each of cellobiose, glucose, soluble starch, and Yeast "
    "extract from BD-Difco, 18 g agar, 2 g Trypticase peptone from BD-BBL, "
    "0.5 ml 0.1% Resazurin solution, 1 ml 1.0% Hemin solution, 100 ml 4% "
    "Na2SO3 solution, 2 ml 25% L-Ascorbic acid solution, 10 ml 5% "
    "L-Cysteine HCl H2O solution, and VFA and salt stocks from Medium 10 / "
    "TOGO M124, with pH adjusted to 6.7-6.8. It uses Medium 10 from JCM "
    "Medium 133 with 1 ml/L final 1% hemin solution and omits Toray silicone "
    "solution. The current JCM Medium 210 URL no longer exposes the recipe."
)

TARGETS: tuple[Target, ...] = (
    Target(
        path=Path("bacterial/medium_10_broth.yaml"),
        parent_path=togo_m172.TARGET,
        expected_id="CultureMech:002539",
        expected_media_term="mediadive.medium:J179",
        original_name="MEDIUM 10 BROTH",
        physical_state="LIQUID",
        togo_module=togo_m172,
        current_ingredient_signature=(
            ("Distilled water", "850", "ML_PER_L"),
            ("Cellobiose", "0.5", "G_PER_L"),
            ("Glucose", "0.5", "G_PER_L"),
            ("Soluble starch", "0.5", "G_PER_L"),
            ("Yeast extract (BD-Difco)", "0.5", "G_PER_L"),
            ("Trypticase peptone (BD-BBL)", "2", "G_PER_L"),
        ),
        current_solution_signatures=(
            ("0.1% Resazurin solution", "0.5", "ML_PER_L", ()),
            ("0.2% Hemin solution", "0.5", "ML_PER_L", ()),
            ("4% Na2SO3 solution", "100", "ML_PER_L", ()),
            ("25% L--Ascorbic acid solution", "2", "ML_PER_L", ()),
            ("5% L--Cysteine\u30fbHCl\u30fbH2O solution", "10", "ML_PER_L", ()),
            ("VFA solution (see Medium [M124])", "3.1", "ML_PER_L", ()),
            ("Salt solution No. 1 (see Medium [M124])", "37.5", "ML_PER_L", ()),
            ("Salt solution No. 2 (see Medium [M124])", "37.5", "ML_PER_L", ()),
        ),
        notes=M172_NOTES,
        source_duplicate_note=(
            "MediaDive JCM J179 is a source-catalogue duplicate of TOGO M172 "
            "for JCM Medium 179 Medium 10 Broth."
        ),
        variant_modification=(
            "Same JCM Medium 179 Medium 10 Broth formulation as the TOGO M172 "
            "source record."
        ),
    ),
    Target(
        path=Path("bacterial/modified_medium_10.yaml"),
        parent_path=togo_m203.TARGET,
        expected_id="CultureMech:002572",
        expected_media_term="mediadive.medium:J210",
        original_name="MODIFIED MEDIUM 10",
        physical_state="SOLID_AGAR",
        togo_module=togo_m203,
        current_ingredient_signature=(
            ("Distilled water", "850", "ML_PER_L"),
            ("Cellobiose", "0.5", "G_PER_L"),
            ("Glucose", "0.5", "G_PER_L"),
            ("Soluble starch", "0.5", "G_PER_L"),
            ("Agar", "18", "G_PER_L"),
            ("Yeast extract (BD-Difco)", "0.5", "G_PER_L"),
            ("Trypticase peptone (BD-BBL)", "2", "G_PER_L"),
        ),
        current_solution_signatures=(
            ("0.1% Resazurin solution", "0.5", "ML_PER_L", ()),
            ("1.0% Hemin solution", "1", "ML_PER_L", ()),
            ("4% Na2SO3 solution", "100", "ML_PER_L", ()),
            ("25% L--Ascorbic acid solution", "2", "ML_PER_L", ()),
            ("5% L--Cysteine\u30fbHCl\u30fbH2O solution", "10", "ML_PER_L", ()),
            ("VFA solution (see Medium [M124])", "3.1", "ML_PER_L", ()),
            ("Salt solution No. 1 (see Medium [M124])", "37.5", "ML_PER_L", ()),
            ("Salt solution No. 2 (see Medium [M124])", "37.5", "ML_PER_L", ()),
        ),
        notes=M203_NOTES,
        source_duplicate_note=(
            "MediaDive JCM J210 is a source-catalogue duplicate of TOGO M203 "
            "for JCM Medium 210 Modified Medium 10."
        ),
        variant_modification=(
            "Same JCM Medium 210 Modified Medium 10 formulation as the TOGO M203 "
            "source record."
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


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    signatures: list[SolutionSignature] = []
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"solution {solution.get('preferred_term')!r} lacks concentration"
            )
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition"), "solution composition"),
            )
        )
    return tuple(signatures)


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
            f"{target.path}: expected id {target.expected_id}, "
            f"found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(
            f"{target.path}: expected media term {target.expected_media_term}"
        )

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        target.current_ingredient_signature,
        target.togo_module.FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.current_ingredient_signature!r} to {ingredient_signature!r}"
        )

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        target.current_solution_signatures,
        target.togo_module.FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(
            f"{target.path}: solution signatures drifted from "
            f"{target.current_solution_signatures!r} to {solution_signatures!r}"
        )


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
    for url in target.togo_module.REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _upsert_history(doc: dict[str, Any], event: dict[str, Any]) -> None:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == event["action"]
        ):
            history[index] = event
            return
    history.append(event)


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    _upsert_history(
        doc,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "source": "; ".join(target.togo_module.REFERENCES),
            "notes": (
                f"{target.notes} Added the source-equivalent TOGO pH range, "
                "represented simple concentration stocks, grounded the stock "
                "components, linked the TOGO duplicate, and marked the formula "
                "as curated."
            ),
        },
    )


def _append_link_event(doc: dict[str, Any], target: Target) -> None:
    _upsert_history(
        doc,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": LINK_ACTION,
            "source": "; ".join(target.togo_module.REFERENCES),
            "notes": f"Added or refreshed the reciprocal SOURCE_DUPLICATE link for {target.path}.",
        },
    )


def _recipe_ref(path: Path, doc: dict[str, Any], notes: str) -> dict[str, str]:
    ref = {
        "path": f"data/normalized_yaml/{path.as_posix()}",
        "relationship": "SOURCE_DUPLICATE",
        "notes": notes,
    }
    if doc.get("id"):
        ref["id"] = str(doc["id"])
    if doc.get("name"):
        ref["name"] = str(doc["name"])
    return ref


def _upsert_ref(refs: list[Any], new_ref: dict[str, str]) -> None:
    for index, existing in enumerate(refs):
        if isinstance(existing, dict) and existing.get("path") == new_ref["path"]:
            refs[index] = new_ref
            return
    refs.append(new_ref)


def repair_jcm_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = target.physical_state
    _put_after(repaired, "ph_range", copy.deepcopy(togo_m172.PH_RANGE), "physical_state")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(target.togo_module.INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(target.togo_module.SOLUTIONS))
    _put_after(repaired, "notes", target.notes, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(
        list(target.togo_module.PREPARATION_STEPS)
    )
    repaired.pop("sterilization", None)
    repaired.pop("variant_children", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
    return repaired


def _link_source_duplicate(
    parent: dict[str, Any],
    child: dict[str, Any],
    target: Target,
) -> None:
    _put_after(
        child,
        "parent_media",
        _recipe_ref(target.parent_path, parent, target.source_duplicate_note),
        "references",
    )
    _put_after(child, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
    _put_after(
        child,
        "variant_modifications",
        [target.variant_modification],
        "variant_relationship",
    )

    children = parent.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError(f"{target.parent_path}: variant_children is not a list")
    _upsert_ref(children, _recipe_ref(target.path, child, target.source_duplicate_note))
    _append_link_event(parent, target)


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        parent_path = normalized / target.parent_path
        child_path = normalized / target.path
        parent = target.togo_module.repair_record(_load(parent_path))
        child = repair_jcm_record(_load(child_path), target)
        _link_source_duplicate(parent, child, target)

        for path, doc in ((parent_path, parent), (child_path, child)):
            if path.read_bytes() != dump_record(doc).encode("utf-8"):
                plans[path] = doc
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    for path in sorted(plans):
        print(path.relative_to(args.normalized_dir))

    if args.apply:
        changed = sum(write_record(path, doc) for path, doc in plans.items())
        print(f"Wrote {changed} record(s).")
    else:
        print(f"Dry run planned {len(plans)} record write(s). Pass --apply to write.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
