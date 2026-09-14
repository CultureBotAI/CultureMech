#!/usr/bin/env python3
"""Repair empty KOMODO 313 ACETOBACTERIUM CARBINOLICUM medium."""

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
TARGET = "bacterial/acetobacterium_carbinolicum_medium.yaml"
EXPECTED_ID = "CultureMech:004988"
EXPECTED_MEDIA_TERM = "komodo.medium:313"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_313_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=313"
)
DSMZ_313_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium313.pdf"
)
DSMZ_124_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium124.pdf"
)

SOURCE_313 = "Archived DSMZ Medium 313"
SOURCE_124 = "Archived DSMZ Medium 124"
SOURCE_124_SOLUTION_B = "Archived DSMZ Medium 124 Solution B"
SOURCE_124_TRACE = "Archived DSMZ Medium 124 trace element solution"
SOURCE_124_VITAMINS = "Archived DSMZ Medium 124 vitamin solution"

CURATOR = "repair_komodo_313_score35.py"
ACTION = "RESOLVED_KOMODO_313_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 313 defines ACETOBACTERIUM CARBINOLICUM MEDIUM as "
    "DSMZ Medium 124 with 20 mM ethanol as the substrate; this record expands "
    "the archived DSMZ Medium 124 base, Solution B, trace stock, and vitamin "
    "stock into final per-liter components."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


def _base_note(name: str, source_amount: str, value: str) -> str:
    return (
        f"{SOURCE_124} contributes {source_amount} {name} in a 1012 mL "
        f"final formulation, yielding {value} g/L."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_124} adds 1 mL of the {SOURCE_124_TRACE} per 1012 mL "
        f"final formulation; the trace stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_124} adds 1 mL of the {SOURCE_124_VITAMINS} per 1012 mL "
        f"final formulation; the vitamin stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "NaCl",
        "1.156126",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_124,
        _base_note("NaCl", "1.17 g", "1.156126"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.395257",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_124,
        _base_note("MgCl2 x 6 H2O", "0.40 g", "0.395257"),
    ),
    Component(
        "KCl",
        "0.296443",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_124,
        _base_note("KCl", "0.30 g", "0.296443"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.148221",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_124,
        _base_note("CaCl2 x 2 H2O", "0.15 g", "0.148221"),
    ),
    Component(
        "NH4Cl",
        "0.266798",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_124,
        _base_note("NH4Cl", "0.27 g", "0.266798"),
    ),
    Component(
        "KH2PO4",
        "0.197628",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_124,
        _base_note("KH2PO4", "0.20 g", "0.197628"),
    ),
    Component(
        "Na2SO4",
        "2.806324",
        "G_PER_L",
        ("CHEBI:32149", "sodium sulfate"),
        SOURCE_124,
        _base_note("Na2SO4", "2.84 g", "2.806324"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001482",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_124_TRACE,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001482"),
    ),
    Component(
        "ZnCl2",
        "0.0000672",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_124_TRACE,
        _trace_note("ZnCl2", "0.068 g/L", "0.0000672"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000988",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_124_TRACE,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000988"),
    ),
    Component(
        "H3BO3",
        "0.0000613",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_124_TRACE,
        _trace_note("H3BO3", "0.062 g/L", "0.0000613"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000119",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_124_TRACE,
        _trace_note("CoCl2 x 6 H2O", "0.120 g/L", "0.000119"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.0000168",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_124_TRACE,
        _trace_note("CuCl2 x 2 H2O", "0.017 g/L", "0.0000168"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000237",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_124_TRACE,
        _trace_note("NiCl2 x 6 H2O", "0.024 g/L", "0.0000237"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000237",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_124_TRACE,
        _trace_note("Na2MoO4 x 2 H2O", "0.024 g/L", "0.0000237"),
    ),
    Component(
        "HCl",
        "0.049407",
        "MILLIMOLAR",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_124_TRACE,
        (
            f"{SOURCE_124} adds 1 mL of 0.05 M HCl trace stock per 1012 mL "
            "final formulation, yielding 0.049407 mM HCl."
        ),
    ),
    Component(
        "Na-acetate",
        "1.383399",
        "G_PER_L",
        ("CHEBI:32954", "sodium acetate"),
        SOURCE_124,
        _base_note("Na-acetate", "1.40 g", "1.383399"),
    ),
    Component(
        "Na-butyrate",
        "1.383399",
        "G_PER_L",
        ("CHEBI:64103", "sodium butyrate"),
        SOURCE_124,
        _base_note("Na-butyrate", "1.40 g", "1.383399"),
    ),
    Component(
        "Yeast extract",
        "0.988142",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_124,
        _base_note("Yeast extract", "1.00 g", "0.988142"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.0000395",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_124_VITAMINS,
        _vitamin_note("p-Aminobenzoic acid", "0.040 g/L", "0.0000395"),
    ),
    Component(
        "D(+)-Biotin",
        "0.00000988",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_124_VITAMINS,
        _vitamin_note("D(+)-Biotin", "0.010 g/L", "0.00000988"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.0000988",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_124_VITAMINS,
        _vitamin_note("Thiamine-HCl x 2 H2O", "0.100 g/L", "0.0000988"),
    ),
    Component(
        "Resazurin",
        "0.000494",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_124,
        _base_note("Resazurin", "0.50 mg", "0.000494"),
    ),
    Component(
        "NaHCO3",
        "4.446640",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_124,
        _base_note("NaHCO3", "4.50 g", "4.446640"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.355731",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_124_SOLUTION_B,
        (
            f"{SOURCE_124} adds all 10 mL of {SOURCE_124_SOLUTION_B} per "
            "1012 mL final formulation, yielding 0.355731 g/L Na2S x 9 H2O."
        ),
    ),
    Component(
        "Ethanol",
        "20.000",
        "MILLIMOLAR",
        ("CHEBI:16236", "ethanol"),
        SOURCE_313,
        f"{SOURCE_313} uses DSMZ Medium 124 with 20 mM ethanol as the substrate.",
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_124,
        f"{SOURCE_124} lists 1000 mL distilled water for Solution A.",
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
        "needs_manual_curation",
        "source_information_unavailable",
    ):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{TARGET}: references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (KOMODO_313_URL, DSMZ_313_URL, DSMZ_124_URL):
        if url not in found:
            references.append({"reference": url})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Replaced empty KOMODO 313 composition with archived DSMZ data",
        "source": DSMZ_313_URL,
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
    row: dict[str, Any] = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
        "term": _term(*component.term),
    }
    if component.term[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*component.term)
    return row


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}")
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_range", {"min": 7.0, "max": 7.2}, "physical_state")
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
