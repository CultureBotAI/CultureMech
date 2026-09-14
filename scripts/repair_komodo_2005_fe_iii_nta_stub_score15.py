#!/usr/bin/env python3
"""Retype the orphaned KOMODO Fe(III)NTA stock from DSMZ Medium 1001."""

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
TARGET = Path("bacterial/fe_iii_nta_solution_medium_1001.yaml")
EXPECTED_ID = "CultureMech:004271"
EXPECTED_MEDIA_TERM = "komodo.medium:2005"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_2005_fe_iii_nta_stub_score15.py"
ACTION = "RETYPE_ORPHANED_FE_III_NTA_STUB"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

DSMZ_1001_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1001.pdf"
MEDIADIVE_1001 = "https://mediadive.dsmz.de/medium/1001"
REFERENCES = (MEDIADIVE_1001, DSMZ_1001_PDF)

IMPORTED_SIGNATURE = (("NaOH", "variable", "VARIABLE"),)
FINAL_SIGNATURE: tuple[tuple[str, str, str], ...] = ()

NOTES = (
    "KOMODO imported this entry as a SubMedium named Fe(III)NTA solution from "
    "DSMZ Medium 1001, but the live DSMZ Medium 1001 recipe contains Mineral "
    "mixture, Wolin's vitamin solution, and FeCl3 x 6 H2O stock, with no "
    "Fe(III)NTA stock. The imported NaOH row was a pH-buffer note rather than "
    "a disclosed stock-solution component."
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


def _signature(rows: Any) -> tuple[tuple[str, str, str], ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("ingredients is not a list")

    signature: list[tuple[str, str, str]] = []
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(
            f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}, "
            f"found {_source_term_id(doc)!r}"
        )

    signature = _signature(doc.get("ingredients"))
    if signature not in {IMPORTED_SIGNATURE, FINAL_SIGNATURE}:
        raise ValueError(f"{TARGET}: composition signature drifted to {signature!r}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    if "source_information_unavailable" not in flags:
        flags.append("source_information_unavailable")


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_1001_PDF,
        "notes": NOTES,
        "changes": (
            "Retyped orphaned Fe(III)NTA stock as a solution stub and removed "
            "the imported NaOH pH-buffer pseudo-ingredient."
        ),
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


def _set_solution_record_kind(doc: dict[str, Any]) -> None:
    reordered: dict[str, Any] = {}
    inserted = False
    for key, value in doc.items():
        if key == "record_kind":
            continue
        reordered[key] = value
        if key == "category":
            reordered["record_kind"] = "SOLUTION"
            inserted = True
    if not inserted:
        reordered["record_kind"] = "SOLUTION"

    doc.clear()
    doc.update(reordered)


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    _set_solution_record_kind(repaired)
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired["notes"] = NOTES
    repaired["ingredients"] = []
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


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
