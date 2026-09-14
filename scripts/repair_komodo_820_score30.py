#!/usr/bin/env python3
"""Repair empty KOMODO 820 AEROPYRUM-JXT medium."""

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
TARGET = Path("archaea/aeropyrum_jxt_medium.yaml")
EXPECTED_ID = "CultureMech:006547"
EXPECTED_MEDIA_TERM = "komodo.medium:820"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_820_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=820"
)
DSMZ_820_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium820.pdf"
)
DSMZ_514_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium514.pdf"
)

SOURCE_820 = "Archived DSMZ Medium 820"
SOURCE_514 = "Archived DSMZ Medium 514"

CURATOR = "repair_komodo_820_score30.py"
ACTION = "RESOLVED_KOMODO_820_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 820 defines AEROPYRUM-JXT MEDIUM as DSMZ Medium "
    "514, with final pH adjusted to 7.0-7.2 and 1.0 g/L sodium thiosulfate "
    "pentahydrate added from a filter-sterilized stock after autoclaving; "
    "DSMZ Medium 514 lists the Bacto Marine Broth 2216 component recipe."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


def _dsmz_514_note(name: str, amount: str) -> str:
    return f"{SOURCE_514} lists {amount} {name} in 1000 mL distilled water."


def _dsmz_514_mg_note(name: str, amount: str, value: str) -> str:
    return (
        f"{SOURCE_514} lists {amount} {name} in 1000 mL distilled water, "
        f"converted to {value} g/L."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "Bacto peptone",
        "5.000000",
        "G_PER_L",
        ("MICRO:0000178", "Bacto peptone"),
        SOURCE_514,
        _dsmz_514_note("Bacto peptone", "5.00 g"),
    ),
    Component(
        "Yeast extract",
        "1.000000",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_514,
        _dsmz_514_note("Bacto yeast extract", "1.00 g"),
    ),
    Component(
        "Fe(III) citrate",
        "0.100000",
        "G_PER_L",
        ("CHEBI:144421", "iron(III) citrate"),
        SOURCE_514,
        _dsmz_514_note("Fe(III) citrate", "0.10 g"),
    ),
    Component(
        "NaCl",
        "19.450000",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_514,
        _dsmz_514_note("NaCl", "19.45 g"),
    ),
    Component(
        "MgCl2",
        "5.900000",
        "G_PER_L",
        ("CHEBI:6636", "magnesium dichloride"),
        SOURCE_514,
        _dsmz_514_note("MgCl2 (anhydrous)", "5.90 g"),
    ),
    Component(
        "Na2SO4",
        "3.240000",
        "G_PER_L",
        ("CHEBI:32149", "sodium sulfate"),
        SOURCE_514,
        _dsmz_514_note("Na2SO4", "3.24 g"),
    ),
    Component(
        "CaCl2",
        "1.800000",
        "G_PER_L",
        ("CHEBI:3312", "calcium dichloride"),
        SOURCE_514,
        _dsmz_514_note("CaCl2", "1.80 g"),
    ),
    Component(
        "KCl",
        "0.550000",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_514,
        _dsmz_514_note("KCl", "0.55 g"),
    ),
    Component(
        "NaHCO3",
        "0.160000",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_514,
        _dsmz_514_note("NaHCO3", "0.16 g"),
    ),
    Component(
        "KBr",
        "0.080000",
        "G_PER_L",
        ("CHEBI:32030", "potassium bromide"),
        SOURCE_514,
        _dsmz_514_note("KBr", "0.08 g"),
    ),
    Component(
        "SrCl2",
        "0.034000",
        "G_PER_L",
        ("CHEBI:36383", "strontium dichloride"),
        SOURCE_514,
        _dsmz_514_mg_note("SrCl2", "34.00 mg", "0.034000"),
    ),
    Component(
        "H3BO3",
        "0.022000",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_514,
        _dsmz_514_mg_note("H3BO3", "22.00 mg", "0.022000"),
    ),
    Component(
        "Na-silicate",
        "0.004000",
        "G_PER_L",
        ("CHEBI:60720", "sodium silicate"),
        SOURCE_514,
        _dsmz_514_mg_note("Na-silicate", "4.00 mg", "0.004000"),
    ),
    Component(
        "NaF",
        "0.002400",
        "G_PER_L",
        ("CHEBI:28741", "sodium fluoride"),
        SOURCE_514,
        _dsmz_514_mg_note("NaF", "2.40 mg", "0.002400"),
    ),
    Component(
        "(NH4)NO3",
        "0.001600",
        "G_PER_L",
        ("CHEBI:63038", "ammonium nitrate"),
        SOURCE_514,
        _dsmz_514_mg_note("(NH4)NO3", "1.60 mg", "0.001600"),
    ),
    Component(
        "Na2HPO4",
        "0.008000",
        "G_PER_L",
        ("CHEBI:34683", "disodium hydrogenphosphate"),
        SOURCE_514,
        _dsmz_514_mg_note("Na2HPO4", "8.00 mg", "0.008000"),
    ),
    Component(
        "Na2S2O3 x 5 H2O",
        "1.000000",
        "G_PER_L",
        ("CHEBI:32150", "sodium thiosulfate pentahydrate"),
        SOURCE_820,
        (
            f"{SOURCE_820} adds 1.0 g/L Na2S2O3 x 5 H2O from a "
            "filter-sterilized stock after autoclaving DSMZ Medium 514."
        ),
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_514,
        f"{SOURCE_514} lists 1000 mL distilled water.",
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _check_source(doc: dict[str, Any]) -> None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{TARGET}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: missing expected media term {EXPECTED_MEDIA_TERM}")


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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{TARGET}: data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)

    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    doc["references"] = [
        {"reference": KOMODO_820_URL},
        {"reference": DSMZ_820_URL},
        {"reference": DSMZ_514_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_820_URL,
        "notes": NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _ingredient(component: Component) -> dict[str, Any]:
    ingredient = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
        "term": _term(*component.term),
    }
    if component.term[0].startswith("CHEBI:"):
        ingredient["mediaingredientmech_chebi_term"] = _term(*component.term)
    return ingredient


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(
            f"{TARGET}: expected immutable id {EXPECTED_ID}, "
            f"found {doc.get('id')!r}"
        )
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_range"] = {"min": 7.0, "max": 7.2}
    repaired["ingredients"] = [_ingredient(component) for component in COMPONENTS]
    _put_after(repaired, "notes", NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
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
