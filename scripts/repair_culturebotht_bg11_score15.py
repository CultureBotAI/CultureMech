#!/usr/bin/env python3
"""Mark CultureBotHT BG11-family score-15 formulas as curated."""

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

CURATOR = "repair_culturebotht_bg11_score15.py"
ACTION = "MARKED_CULTUREBOTHT_BG11_SCORE15"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
CULTUREBOTHT_URL = "https://github.com/CultureBotAI/CultureBotHT"

BASE_BG11 = (
    "Sodium nitrate",
    "Potassium phosphate dibasic",
    "Magnesium Sulfate Heptahydrate",
    "Calcium chloride dihydrate",
    "Citric Acid",
    "Ferric ammonium citrate",
    "EDTA (disodium salt)",
    "Sodium carbonate",
    "Boric Acid",
    "Manganese (II) chloride tetrahydrate",
    "Zinc sulfate heptahydrate",
    "Sodium Molybdate Dihydrate",
    "Copper (II) sulfate pentahydrate",
    "Cobalt(II) nitrate hexahydrate",
)

NO_NITRATE_BG11 = tuple(name for name in BASE_BG11 if name != "Sodium nitrate")
NO_BICARB_BG11 = tuple(name for name in BASE_BG11 if name != "Sodium carbonate")
BG11C = (
    *NO_BICARB_BG11[:7],
    "Sodium bicarbonate",
    *NO_BICARB_BG11[7:],
)
TES = "TES"


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    source_id: str
    expected_ingredients: tuple[str, ...]
    ph_value: float | None = None


TARGETS: tuple[Target, ...] = (
    Target("algae/bg11.yaml", "CultureMech:015450", "BG11", BASE_BG11, 7.1),
    Target(
        "algae/bg11_no_bicarb.yaml",
        "CultureMech:015451",
        "BG11 no bicarb",
        NO_BICARB_BG11,
    ),
    Target(
        "algae/bg11_nonitrogen.yaml",
        "CultureMech:015452",
        "BG11 noNitrogen",
        NO_NITRATE_BG11,
        7.1,
    ),
    Target(
        "algae/bg11_tes_no_bicarb.yaml",
        "CultureMech:015453",
        "BG11 TES no bicarb",
        (*NO_BICARB_BG11, TES),
    ),
    Target("algae/bg11c.yaml", "CultureMech:015454", "BG11C", BG11C),
    Target("algae/bg11c_tes.yaml", "CultureMech:015455", "BG11C TES", (*BG11C, TES)),
    Target("algae/bg11r.yaml", "CultureMech:015456", "BG11R", BASE_BG11, 7.1),
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


def _component_names(doc: dict[str, Any]) -> tuple[str, ...]:
    return tuple(
        str(row.get("preferred_term") or "")
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    )


def _has_source(doc: dict[str, Any], source_id: str) -> bool:
    for source in doc.get("sources") or []:
        if not isinstance(source, dict):
            continue
        if source.get("database") == "CultureBotHT" and source.get("database_id") == source_id:
            return True

    source_data = doc.get("source_data")
    return (
        isinstance(source_data, dict)
        and source_data.get("origin") == "CultureBotHT"
        and f"database_id: {source_id};" in str(source_data.get("notes") or "")
    )


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}"
        )
    if not _has_source(doc, target.source_id):
        raise ValueError(f"{target.path}: missing CultureBotHT source {target.source_id!r}")
    if _component_names(doc) != target.expected_ingredients:
        raise ValueError(f"{target.path}: BG11 ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (f"CultureBotHT:{target.source_id}", CULTUREBOTHT_URL):
        if reference not in existing:
            references.append({"reference": reference})


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Marked exact CultureBotHT BG11-family formula as curated",
        "source": f"CultureBotHT:{target.source_id}; {CULTUREBOTHT_URL}",
        "notes": f"CultureBotHT imports {target.source_id} as a BG11-family formula.",
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
    _put_after(
        repaired,
        "media_term",
        {"preferred_term": target.source_id},
        "physical_state",
    )
    if target.ph_value is not None:
        _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _ensure_event(repaired, target)
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
