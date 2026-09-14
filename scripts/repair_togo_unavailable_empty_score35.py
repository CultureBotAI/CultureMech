#!/usr/bin/env python3
"""Mark empty TOGO records whose live source payload has no components."""

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

CURATOR = "repair_togo_unavailable_empty_score35.py"
ACTION = "MARKED_SOURCE_UNAVAILABLE_EMPTY"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1550 = "https://togomedium.org/medium/M1550"
TOGO_M241 = "https://togomedium.org/medium/M241"
NBRC_347 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=347"
JCM_249 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=249"
TOGO_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid"


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    source_urls: tuple[str, ...]
    notes: str


TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/nissui_plate_sheep_blood_agar.yaml",
        record_id="CultureMech:008099",
        source_term="TOGO:M1550",
        source_urls=(TOGO_M1550, NBRC_347),
        notes=(
            "TOGO M1550's live gmdb_medium_by_gmid payload has no components and "
            "only preserves the Nissui Pharmaceutical vendor footnote from NBRC "
            "Medium 347."
        ),
    ),
    Target(
        path="bacterial/yeast_extract_medium_ye.yaml",
        record_id="CultureMech:009002",
        source_term="TOGO:M241",
        source_urls=(TOGO_M241, JCM_249),
        notes=(
            "TOGO M241's live gmdb_medium_by_gmid payload has no components and "
            "only preserves JCM Medium 249's unavailable 'Not yet' comment."
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.source_term}, " f"found {source_term!r}"
        )

    for key in ("ingredients", "solutions"):
        values = doc.get(key) or []
        if values:
            raise ValueError(f"{target.path}: {key} unexpectedly has content")


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.source_urls:
        if url not in existing:
            references.append({"reference": url})


def _ensure_flags(doc: dict[str, Any]) -> None:
    data_quality_flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(data_quality_flags, list):
        raise ValueError("data_quality_flags is not a list")
    if "source_information_unavailable" not in data_quality_flags:
        data_quality_flags.append("source_information_unavailable")


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": f"{TOGO_API}?gm_id={target.source_term.removeprefix('TOGO:')}",
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
