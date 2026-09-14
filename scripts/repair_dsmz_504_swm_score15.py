#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 504 SWM strain-variant metadata."""

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

DSMZ_504 = "specialized/anaerobic_seawater_swm_medium.yaml"
KOMODO_504 = "bacterial/swm_medium.yaml"
KOMODO_504_1 = "bacterial/for_dsm_5848.yaml"
KOMODO_504_2 = "bacterial/for_dsm_6233.yaml"
KOMODO_504_3 = "bacterial/for_dsm_9705.yaml"
KOMODO_504_4 = "bacterial/for_dsm_12881.yaml"
KOMODO_504_5 = "bacterial/for_dsm_13687.yaml"
KOMODO_504_6 = "bacterial/for_dsm_19335.yaml"

EXPECTED_IDS = {
    DSMZ_504: "CultureMech:015356",
    KOMODO_504: "CultureMech:005693",
    KOMODO_504_1: "CultureMech:005687",
    KOMODO_504_2: "CultureMech:005688",
    KOMODO_504_3: "CultureMech:005689",
    KOMODO_504_4: "CultureMech:005690",
    KOMODO_504_5: "CultureMech:005691",
    KOMODO_504_6: "CultureMech:005692",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_504: "mediadive.medium:504",
    KOMODO_504: "komodo.medium:504",
    KOMODO_504_1: "komodo.medium:504.1",
    KOMODO_504_2: "komodo.medium:504.2",
    KOMODO_504_3: "komodo.medium:504.3",
    KOMODO_504_4: "komodo.medium:504.4",
    KOMODO_504_5: "komodo.medium:504.5",
    KOMODO_504_6: "komodo.medium:504.6",
}

DSMZ_504_REST = "https://mediadive.dsmz.de/rest/medium/504"
DSMZ_504_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium504.pdf"
KOMODO_BASE = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)

CURATOR = "repair_dsmz_504_swm_score15.py"
ACTION = "RESOLVED_DSMZ_KOMODO_504_SWM_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"
PH_RANGE = {"min": 7.2, "max": 7.4}
DATA_QUALITY_FLAGS = ["ingredients_curated", "has_ontology_mappings"]


@dataclass(frozen=True)
class Target:
    path: str
    source_label: str
    source_url: str
    notes: str
    parent_media: dict[str, str] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, str], ...] = ()


def _recipe_ref(path: str, relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": EXPECTED_IDS[path],
        "name": Path(path).stem,
        "notes": notes,
    }


DSMZ_504_PARENT = _recipe_ref(
    DSMZ_504,
    "STRAIN_SPECIFIC_VARIANT",
    "DSMZ Medium 504 is the official ANAEROBIC SEAWATER (SWM) base formulation.",
)

CHILDREN = {
    KOMODO_504: _recipe_ref(
        KOMODO_504,
        "SOURCE_DUPLICATE",
        "KOMODO Medium 504 is a source-catalogue duplicate of DSMZ Medium 504.",
    ),
    KOMODO_504_1: _recipe_ref(
        KOMODO_504_1,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 504.1 applies DSMZ Medium 504 to DSM 5848.",
    ),
    KOMODO_504_2: _recipe_ref(
        KOMODO_504_2,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 504.2 applies DSMZ Medium 504 to DSM 6233.",
    ),
    KOMODO_504_3: _recipe_ref(
        KOMODO_504_3,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 504.3 applies DSMZ Medium 504 to DSM 9705.",
    ),
    KOMODO_504_4: _recipe_ref(
        KOMODO_504_4,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 504.4 applies DSMZ Medium 504 to DSM 12881.",
    ),
    KOMODO_504_5: _recipe_ref(
        KOMODO_504_5,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 504.5 applies DSMZ Medium 504 to DSM 13687.",
    ),
    KOMODO_504_6: _recipe_ref(
        KOMODO_504_6,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 504.6 applies DSMZ Medium 504 to DSM 19335.",
    ),
}


def _steps(source: str) -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": (
                f"{source} sparges Solution A with an 80% N2 and 20% CO2 gas "
                "mixture, distributes it under the same gas atmosphere, and "
                "autoclaves it; Solution B is autoclaved separately under "
                "80% N2 and 20% CO2, and Solution E is autoclaved under 100% N2."
            ),
        },
        {
            "step_number": 2,
            "action": "FILTER_STERILIZE",
            "description": (
                f"{source} prepares Solutions C and D under 100% N2 and "
                "sterilizes them by filtration before adding Solutions B to E "
                "to sterile Solution A in sequence."
            ),
        },
        {
            "step_number": 3,
            "action": "ADJUST_PH",
            "description": f"{source} adjusts the complete medium to pH 7.2-7.4 if necessary.",
        },
    ]


TARGETS: tuple[Target, ...] = (
    Target(
        path=DSMZ_504,
        source_label="DSMZ Medium 504",
        source_url=DSMZ_504_REST,
        notes=(
            "MediaDive and DSMZ Medium 504 define ANAEROBIC SEAWATER (SWM) "
            "MEDIUM as a modified DSMZ Medium 503 formulation with 20 g/L NaCl "
            "and 3 g/L MgCl2 x 6 H2O."
        ),
        variant_children=tuple(CHILDREN.values()),
    ),
    Target(
        path=KOMODO_504,
        source_label="KOMODO Medium 504",
        source_url=f"{KOMODO_BASE}504",
        notes="KOMODO Medium 504 cites the DSMZ Medium 504 SWM formulation.",
        parent_media=_recipe_ref(
            DSMZ_504,
            "SOURCE_DUPLICATE",
            "DSMZ Medium 504 is the official ANAEROBIC SEAWATER (SWM) formulation.",
        ),
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=("KOMODO source-catalogue duplicate of DSMZ Medium 504.",),
    ),
    Target(
        path=KOMODO_504_1,
        source_label="KOMODO Medium 504.1",
        source_url=f"{KOMODO_BASE}504.1",
        notes=(
            "KOMODO Medium 504.1 records the DSMZ Medium 504 DSM 5848 variant "
            "with Na2-succinate substrate and 0.05% yeast extract."
        ),
        parent_media=DSMZ_504_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Uses 2.5 g/L Na2-succinate as substrate and adds 0.05% yeast extract for DSM 5848.",
        ),
    ),
    Target(
        path=KOMODO_504_2,
        source_label="KOMODO Medium 504.2",
        source_url=f"{KOMODO_BASE}504.2",
        notes=(
            "KOMODO Medium 504.2 records the DSMZ Medium 504 DSM 6233 variant "
            "with 2 mL/L SL-10 trace elements and pyrogallol substrate."
        ),
        parent_media=DSMZ_504_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Uses 2 mL/L Trace element solution SL-10 and 0.5 g/L pyrogallol for DSM 6233.",
        ),
    ),
    Target(
        path=KOMODO_504_3,
        source_label="KOMODO Medium 504.3",
        source_url=f"{KOMODO_BASE}504.3",
        notes=(
            "KOMODO Medium 504.3 records the DSMZ Medium 504 DSM 9705 variant "
            "with added sulfate, sodium glycolate substrate, and "
            "selenite/tungstate solution."
        ),
        parent_media=DSMZ_504_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Adds 3 g/L Na2SO4 to Solution A, uses 1 g/L sodium glycolate as substrate, "
            "and adds 1 mL/L Selenite-tungstate solution for DSM 9705.",
        ),
    ),
    Target(
        path=KOMODO_504_4,
        source_label="KOMODO Medium 504.4",
        source_url=f"{KOMODO_BASE}504.4",
        notes=(
            "KOMODO Medium 504.4 records the DSMZ Medium 504 DSM 12881 variant "
            "with glucose and yeast extract substrates."
        ),
        parent_media=DSMZ_504_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=("Uses 2 g/L glucose and 0.5 g/L yeast extract for DSM 12881.",),
    ),
    Target(
        path=KOMODO_504_5,
        source_label="KOMODO Medium 504.5",
        source_url=f"{KOMODO_BASE}504.5",
        notes=(
            "KOMODO Medium 504.5 records the DSMZ Medium 504 DSM 13687 variant "
            "with added sulfate and Na2-fumarate substrate."
        ),
        parent_media=DSMZ_504_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=("Adds 1.5 g/L Na2SO4 to Solution A and uses 1.6 g/L Na2-fumarate for DSM 13687.",),
    ),
    Target(
        path=KOMODO_504_6,
        source_label="KOMODO Medium 504.6",
        source_url=f"{KOMODO_BASE}504.6",
        notes=(
            "KOMODO Medium 504.6 records the DSMZ Medium 504 DSM 19335 variant "
            "with maltose and yeast extract substrates."
        ),
        parent_media=DSMZ_504_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=("Uses 2.5 g/L maltose and 2.0 g/L yeast extract for DSM 19335.",),
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value
    doc.clear()
    doc.update(updated)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    term = media_term.get("term") if isinstance(media_term, dict) else {}
    return str(term.get("id") or "") if isinstance(term, dict) else ""


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != EXPECTED_IDS[target.path]:
        raise ValueError(f"{target.path}: found id {doc.get('id')!r}, expected {EXPECTED_IDS[target.path]!r}")
    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[target.path]:
        raise ValueError(
            f"{target.path}: found source term {source_term!r}, expected {EXPECTED_SOURCE_TERMS[target.path]!r}"
        )


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    seen = {row.get("reference") for row in references if isinstance(row, dict)}
    urls = [target.source_url, DSMZ_504_PDF]
    if target.path != DSMZ_504:
        urls.append(DSMZ_504_REST)

    for url in urls:
        if url not in seen:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ/KOMODO Medium 504 SWM strain-variant metadata",
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


def _resolve_solution_concentrations(doc: dict[str, Any], target: Target) -> None:
    if target.path in {DSMZ_504, KOMODO_504}:
        return

    trace_value = "2" if target.path == KOMODO_504_2 else "1"
    resolved = {
        "Trace element solution SL-10": (
            trace_value,
            f"DSMZ Medium 504 adds {trace_value} mL/L Trace element solution SL-10 for "
            + ("DSM 6233." if target.path == KOMODO_504_2 else "its SWM base formulation."),
        ),
        "Seven vitamins solution": (
            "1",
            "DSMZ Medium 504 adds 1 mL/L Seven vitamins solution to the SWM base formulation.",
        ),
    }

    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        preferred_term = solution.get("preferred_term")
        if preferred_term not in resolved:
            continue
        value, notes = resolved[preferred_term]
        solution["concentration"] = {"value": value, "unit": "ML_PER_L"}
        solution.pop("concentration_candidates", None)
        solution["preparation_notes"] = notes


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    _resolve_solution_concentrations(repaired, target)
    _put_after(repaired, "ph_range", copy.deepcopy(PH_RANGE), "physical_state")
    _put_after(repaired, "preparation_steps", _steps(target.source_label), "solutions")
    _put_after(repaired, "data_quality_flags", list(DATA_QUALITY_FLAGS), "preparation_steps")

    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
    _put_after(repaired, "references", repaired["references"], "data_quality_flags")

    for field in ("parent_media", "variant_relationship", "variant_modifications", "variant_children"):
        repaired.pop(field, None)

    after = "references"
    if target.parent_media is not None:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), after)
        after = "parent_media"
    if target.variant_relationship is not None:
        _put_after(repaired, "variant_relationship", target.variant_relationship, after)
        after = "variant_relationship"
    if target.variant_modifications:
        _put_after(repaired, "variant_modifications", list(target.variant_modifications), after)
        after = "variant_modifications"
    if target.variant_children:
        _put_after(repaired, "variant_children", [copy.deepcopy(row) for row in target.variant_children], after)

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
