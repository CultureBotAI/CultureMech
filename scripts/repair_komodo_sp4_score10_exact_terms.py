#!/usr/bin/env python3
"""Ground exact KOMODO SP4 score-10 ingredient mappings."""

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
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

TARGETS = tuple(
    Path(relative)
    for relative in (
        "bacterial/for_ureaplasma.yaml",
        "bacterial/medium_1076_modified_for_dsm_21848.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19104.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19105.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19201.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19202.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19518.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19754.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19755.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19775.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19793.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19816.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19817.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19900.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19901.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19993.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19994.yaml",
        "bacterial/medium_1076b_modified_for_dsm_19995.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21131.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21204.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21430.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21477.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21484.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21588.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21589.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21657.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21780.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21781.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21782.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21833.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21834.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21846.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21865.yaml",
        "bacterial/medium_1076b_modified_for_dsm_21866.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22019.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22020.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22021.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22061.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22062.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22113.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22114.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22144.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22145.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22457.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22551.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22552.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22553.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22601.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22603.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22604.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22631.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22632.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22633.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22781.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22911.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22997.yaml",
        "bacterial/medium_1076b_modified_for_dsm_22998.yaml",
        "bacterial/medium_1076b_modified_for_dsm_23060.yaml",
        "bacterial/medium_1076b_modified_for_dsm_23536.yaml",
        "bacterial/medium_1076b_modified_for_dsm_23537.yaml",
        "bacterial/medium_1076b_modified_for_dsm_23537_replace_glucose_with_arginine.yaml",
        "bacterial/medium_1076b_modified_for_dsm_23978.yaml",
        "bacterial/medium_1076b_modified_for_dsm_23979.yaml",
        "bacterial/medium_1076b_modified_for_dsm_25590.yaml",
        "bacterial/medium_1076b_modified_for_dsm_25592.yaml",
    )
)

TARGET_SIGNATURE = (
    "Tryptone",
    "Peptone",
    "PPLO broth",
    "Fetal bovine serum",
    "CMRL 1066",
    "Yeast extract",
    "Phenol red",
    "L-Glutamine",
)

TARGET_TERMS = (
    "Peptone",
    "Tryptone",
    "Yeast extract",
)

TERMS = {
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Tryptone": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
}

CURATOR = "repair_komodo_sp4_score10_exact_terms.py"
ACTION = "GROUNDED_KOMODO_SP4_SCORE10_EXACT_TERMS"
TIMESTAMP = "2026-09-13T00:00:00-07:00"
EXPECTED_TARGET_COUNT = 65


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _ingredient_signature(doc: dict[str, Any]) -> tuple[str, ...]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")
    return tuple(
        str(row.get("preferred_term") or "")
        for row in ingredients
        if isinstance(row, dict)
    )


def _ensure_event(doc: dict[str, Any], event: dict[str, Any]) -> None:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == event["curator"]
            and existing.get("action") == event["action"]
        ):
            history[index] = event
            return
    history.append(event)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    if not isinstance(media_term, dict):
        raise ValueError("media_term is not a mapping")
    term = media_term.get("term") or {}
    if not isinstance(term, dict):
        raise ValueError("media_term.term is not a mapping")
    return str(term.get("id") or "")


def _require_current_sp4_copy(path: Path, doc: dict[str, Any]) -> None:
    if path not in TARGETS:
        raise ValueError(f"{path}: not a targeted KOMODO SP4 record")
    if not _source_term_id(doc).startswith("komodo.medium:1076"):
        raise ValueError(
            f"{path}: expected KOMODO 1076 source term, found {_source_term_id(doc)!r}"
        )
    if _ingredient_signature(doc) != TARGET_SIGNATURE:
        raise ValueError(
            f"{path}: ingredient signature drifted: {_ingredient_signature(doc)!r}"
        )


def repair_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    _require_current_sp4_copy(path, doc)

    expected_terms = set(TARGET_TERMS)
    grounded_terms: set[str] = set()
    repaired = copy.deepcopy(doc)
    for ingredient in repaired["ingredients"]:
        preferred_term = ingredient["preferred_term"]
        if preferred_term not in expected_terms:
            continue

        ingredient["term"] = copy.deepcopy(TERMS[preferred_term])
        grounded_terms.add(preferred_term)

    if grounded_terms != expected_terms:
        missing = ", ".join(sorted(expected_terms - grounded_terms))
        raise ValueError(f"{path}: missing targeted ingredient(s): {missing}")

    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Grounded exact KOMODO SP4 score-10 ingredients",
            "source": "src/culturemech/data/mediaingredientmech/label_index.csv",
            "notes": "Applied local mappings for Peptone, Tryptone, Yeast extract.",
        },
    )
    return repaired


def _validate_targets() -> None:
    if len(TARGETS) != EXPECTED_TARGET_COUNT or len(TARGETS) != len(set(TARGETS)):
        raise ValueError(
            f"expected {EXPECTED_TARGET_COUNT} unique KOMODO SP4 targets, "
            f"found {len(TARGETS)} total and {len(set(TARGETS))} unique"
        )


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    return {
        normalized / relative: repair_record(relative, _load(normalized / relative))
        for relative in TARGETS
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
