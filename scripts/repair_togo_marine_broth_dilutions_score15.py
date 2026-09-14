#!/usr/bin/env python3
"""Repair score-15 TOGO/NBRC diluted Marine Broth agar records."""

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

CURATOR = "repair_togo_marine_broth_dilutions_score15.py"
ACTION = "RESOLVED_TOGO_MARINE_BROTH_DILUTION_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1774 = "https://togomedium.org/medium/M1774"
TOGO_M1916 = "https://togomedium.org/medium/M1916"
TOGO_M2017 = "https://togomedium.org/medium/M2017"
TOGO_M2164 = "https://togomedium.org/medium/M2164"

NBRC_990 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=990"
NBRC_1180 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1180"
NBRC_1306 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1306"
NBRC_1542 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1542"

AGAR_TERM = {"id": "CHEBI:2509", "label": "agar"}

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    source_label: str
    agar_preferred_term: str
    ingredient_signature: tuple[Component, ...]
    reference_urls: tuple[str, ...]
    notes: str
    solution_signature: tuple[Component, ...] = field(default_factory=tuple)
    ph_value: float | None = None


TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/1_10_marine_broth_agar.yaml",
        record_id="CultureMech:008340",
        source_term="TOGO:M1774",
        source_label="TOGO M1774",
        agar_preferred_term="Agar  (if needed)",
        ingredient_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Agar  (if needed)", "15", "G_PER_L"),
            ("Bacto Marine Broth 2216 (Difco)", "3.7", "G_PER_L"),
        ),
        reference_urls=(TOGO_M1774, NBRC_990),
        notes=(
            "TOGO M1774 mirrors NBRC Medium 990 and lists agar only as the "
            "optional solidifying agent; Bacto Marine Broth 2216 remains a "
            "source-disclosed opaque Difco product. TOGO states pH unadjusted."
        ),
    ),
    Target(
        path="bacterial/1_10_mb_agar.yaml",
        record_id="CultureMech:008604",
        source_term="TOGO:M2017",
        source_label="TOGO M2017",
        agar_preferred_term="Agar (if needed)",
        ingredient_signature=(
            ("Distilled water", "250", "G_PER_L"),
            ("Artificial seawater", "750", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Bacto Marine Broth 2216 (Difco)", "3.74", "G_PER_L"),
        ),
        ph_value=7.6,
        reference_urls=(TOGO_M2017, NBRC_1306),
        notes=(
            "TOGO M2017 mirrors NBRC Medium 1306 and lists agar only as the "
            "optional solidifying agent. TOGO reports pH 7.6; Artificial "
            "seawater and Bacto Marine Broth 2216 remain source-disclosed "
            "opaque components."
        ),
    ),
    Target(
        path="bacterial/1_5_marine_agar_broth.yaml",
        record_id="CultureMech:008494",
        source_term="TOGO:M1916",
        source_label="TOGO M1916",
        agar_preferred_term="Agar (if needed)",
        ingredient_signature=(
            ("Distilled water", "200", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Bacto Marine Broth 2216 (Difco)", "7", "G_PER_L"),
        ),
        solution_signature=(("Sea water*", "800", "G_PER_L"),),
        ph_value=7.6,
        reference_urls=(TOGO_M1916, NBRC_1180),
        notes=(
            "TOGO M1916 mirrors NBRC Medium 1180 and lists agar only as the "
            "optional solidifying agent. TOGO reports pH 7.6 and preserves "
            "the source footnote identifying Sea water as filtered aged "
            "seawater or Daigo artificial seawater."
        ),
    ),
    Target(
        path="bacterial/1_2_marine_broth_agar.yaml",
        record_id="CultureMech:008758",
        source_term="TOGO:M2164",
        source_label="TOGO M2164",
        agar_preferred_term="Agar (if needed)",
        ingredient_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Bacto Marine Broth 2216 (Difco)", "18.7", "G_PER_L"),
        ),
        reference_urls=(TOGO_M2164, NBRC_1542),
        notes=(
            "TOGO M2164 mirrors NBRC Medium 1542 and lists agar only as the "
            "optional solidifying agent; Bacto Marine Broth 2216 remains a "
            "source-disclosed opaque Difco product. TOGO states pH unadjusted."
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


def _component_signature(rows: Any, label: str) -> tuple[Component, ...]:
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.source_term}, " f"found {source_term!r}"
        )

    signature = _component_signature(doc.get("ingredients"), "ingredients")
    if signature != target.ingredient_signature:
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.ingredient_signature!r} to {signature!r}"
        )

    solution_signature = _component_signature(doc.get("solutions") or [], "solutions")
    if solution_signature != target.solution_signature:
        raise ValueError(
            f"{target.path}: solution signature drifted from "
            f"{target.solution_signature!r} to {solution_signature!r}"
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


def _ensure_agar_grounding(doc: dict[str, Any], target: Target) -> None:
    ingredients = doc["ingredients"]
    for index, row in enumerate(ingredients):
        if row.get("preferred_term") != target.agar_preferred_term:
            continue

        ingredients[index] = {
            "preferred_term": target.agar_preferred_term,
            "concentration": copy.deepcopy(row["concentration"]),
            "source": target.source_label,
            "notes": (
                f"Role: Solidifying component; {target.source_label} lists "
                "agar only as an optional solidifying agent."
            ),
            "term": copy.deepcopy(AGAR_TERM),
            "mediaingredientmech_chebi_term": copy.deepcopy(AGAR_TERM),
        }
        return

    raise ValueError(f"{target.path}: missing {target.agar_preferred_term!r} row")


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
    for url in target.reference_urls:
        if url not in existing:
            references.append({"reference": url})


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
    if target.ph_value is not None:
        _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    _ensure_agar_grounding(repaired, target)
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
