#!/usr/bin/env python3
"""Repair empty KOMODO 409 SYNTROPHUS BUSWELLII II records."""

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

KOMODO_409_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=409"
)
KOMODO_409_1_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=409.1"
)
DSMZ_409_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium409.pdf"
)
DSMZ_194_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium194.pdf"
)
DSMZ_193_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium193.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)
DSMZ_141_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"
)

SOURCE_409 = "Archived DSMZ Medium 409"
SOURCE_194 = "Archived DSMZ Medium 194"
SOURCE_193 = "Archived DSMZ Medium 193"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"
SOURCE_141 = "Archived DSMZ Medium 141 vitamin solution"

CURATOR = "repair_komodo_409_score35.py"
ACTION = "RESOLVED_KOMODO_409_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
BASE_NOTES = (
    "Archived DSMZ Medium 409 defines SYNTROPHUS BUSWELLII II MEDIUM as DSMZ "
    "Medium 194 with 3.0 g/L sodium benzoate and 1.0 g/L sodium acetate "
    "replacing propionate, 3 microgram/L Na2SeO3 x 5 H2O, 60 mg/L "
    "Na2S x 9 H2O, and 10-20 mg/L sodium dithionite; this record expands "
    "archived DSMZ Media 193, 194, 320, 141, and 409 into final per-liter "
    "components."
)
NO_SULFATE_NOTES = (
    "Archived DSMZ Medium 409 defines the DSM 4156 B/C variant as the "
    "SYNTROPHUS BUSWELLII II MEDIUM formulation with the same benzoate, "
    "acetate, selenite, sulfide, and dithionite amendments and with Na2SO4 "
    "omitted."
)


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    media_term: str
    komodo_url: str
    notes: str
    omit_sulfate: bool


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


TARGETS: tuple[Target, ...] = (
    Target(
        Path("bacterial/syntrophus_buswellii_ii_medium.yaml"),
        "CultureMech:005230",
        "komodo.medium:409",
        KOMODO_409_URL,
        BASE_NOTES,
        False,
    ),
    Target(
        Path("bacterial/dsm_4156_b_and_dsm_4156.yaml"),
        "CultureMech:005229",
        "komodo.medium:409.1",
        KOMODO_409_1_URL,
        f"{BASE_NOTES} {NO_SULFATE_NOTES}",
        True,
    ),
)
TARGETS_BY_ID = {target.expected_id: target for target in TARGETS}


def _base_note(name: str, source_amount: str, value: str) -> str:
    return (
        f"{SOURCE_193} contributes {source_amount} {name} to a 1001 mL "
        f"final formulation, yielding {value} g/L."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_193} adds 1 mL of the {SOURCE_320} to a 1001 mL "
        f"final formulation; the SL-10 stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_193} adds 10 mL of the {SOURCE_141} to a 1001 mL "
        f"final formulation; the vitamin stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


SULFATE = Component(
    "Na2SO4",
    "2.997003",
    "G_PER_L",
    ("CHEBI:32149", "sodium sulfate"),
    SOURCE_193,
    _base_note("Na2SO4", "3.00 g", "2.997003"),
)

COMMON_COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.199800",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_193,
        _base_note("KH2PO4", "0.20 g", "0.199800"),
    ),
    Component(
        "NH4Cl",
        "0.299700",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_193,
        _base_note("NH4Cl", "0.30 g", "0.299700"),
    ),
    Component(
        "NaCl",
        "1.000000",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_194,
        f"{SOURCE_194} lowers the DSMZ Medium 193 NaCl amount to 1.0 g/L.",
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.400000",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_194,
        f"{SOURCE_194} lowers the DSMZ Medium 193 MgCl2 x 6 H2O amount to 0.4 g/L.",
    ),
    Component(
        "KCl",
        "0.499500",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_193,
        _base_note("KCl", "0.50 g", "0.499500"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.149850",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_193,
        _base_note("CaCl2 x 2 H2O", "0.15 g", "0.149850"),
    ),
    Component(
        "Resazurin",
        "0.000999",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_193,
        _base_note("Resazurin", "1.00 mg", "0.000999"),
    ),
    Component(
        "HCl",
        "0.002498",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note("HCl", "2.50 g/L", "0.002498"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001499",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001499"),
    ),
    Component(
        "ZnCl2",
        "0.0000699",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note("ZnCl2", "0.070 g/L", "0.0000699"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000999",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000999"),
    ),
    Component(
        "H3BO3",
        "0.00000599",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note("H3BO3", "0.006 g/L", "0.00000599"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000190",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
        _trace_note("CoCl2 x 6 H2O", "0.190 g/L", "0.000190"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000200",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note("CuCl2 x 2 H2O", "0.002 g/L", "0.00000200"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000240",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
        _trace_note("NiCl2 x 6 H2O", "0.024 g/L", "0.0000240"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000360",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note("Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000360"),
    ),
    Component(
        "NaHCO3",
        "4.995005",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_193,
        _base_note("NaHCO3", "5.00 g", "4.995005"),
    ),
    Component(
        "sodium benzoate",
        "3.000000",
        "G_PER_L",
        ("CHEBI:113455", "sodium benzoate"),
        SOURCE_409,
        f"{SOURCE_409} replaces sodium propionate with 3.0 g/L sodium benzoate.",
    ),
    Component(
        "Sodium acetate",
        "1.000000",
        "G_PER_L",
        ("CHEBI:32954", "sodium acetate"),
        SOURCE_409,
        f"{SOURCE_409} adds 1.0 g/L sodium acetate as a second substrate.",
    ),
    Component(
        "Biotin",
        "0.0000200",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_141,
        _vitamin_note("Biotin", "0.002 g/L", "0.0000200"),
    ),
    Component(
        "Folic acid",
        "0.0000200",
        "G_PER_L",
        ("CHEBI:27470", "folic acid"),
        SOURCE_141,
        _vitamin_note("Folic acid", "0.002 g/L", "0.0000200"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.0000999",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_141,
        _vitamin_note("Pyridoxine-HCl", "0.010 g/L", "0.0000999"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.0000500",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_141,
        _vitamin_note("Thiamine-HCl x 2 H2O", "0.005 g/L", "0.0000500"),
    ),
    Component(
        "Riboflavin",
        "0.0000500",
        "G_PER_L",
        ("CHEBI:17015", "riboflavin"),
        SOURCE_141,
        _vitamin_note("Riboflavin", "0.005 g/L", "0.0000500"),
    ),
    Component(
        "Nicotinic acid",
        "0.0000500",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_141,
        _vitamin_note("Nicotinic acid", "0.005 g/L", "0.0000500"),
    ),
    Component(
        "D-Ca-pantothenate",
        "0.0000500",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_141,
        _vitamin_note("D-Ca-pantothenate", "0.005 g/L", "0.0000500"),
    ),
    Component(
        "Vitamin B12",
        "0.000000999",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        SOURCE_141,
        _vitamin_note("Vitamin B12", "0.0001 g/L", "0.000000999"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.0000500",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_141,
        _vitamin_note("p-Aminobenzoic acid", "0.005 g/L", "0.0000500"),
    ),
    Component(
        "Lipoic acid",
        "0.0000500",
        "G_PER_L",
        ("CHEBI:16494", "lipoic acid"),
        SOURCE_141,
        _vitamin_note("Lipoic acid", "0.005 g/L", "0.0000500"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.060000",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_409,
        f"{SOURCE_409} reduces the Na2S x 9 H2O amount to 60 mg/L medium.",
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "0.00000300",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_409,
        f"{SOURCE_409} supplements the medium with 3 microgram/L Na2SeO3 x 5 H2O.",
    ),
    Component(
        "Na2S2O4",
        "0.010-0.020",
        "G_PER_L",
        ("CHEBI:66870", "sodium dithionite"),
        SOURCE_409,
        f"{SOURCE_409} adds 10-20 mg/L sodium dithionite as reducing agent.",
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_193,
        f"{SOURCE_193} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_193,
        f"{SOURCE_193} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "Distilled water",
        "990.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_193,
        (
            f"{SOURCE_193} lists 990 mL direct distilled water across "
            "solutions A, C, D, and F before stock additions and before "
            f"{SOURCE_409} replaces the substrate and reduces the sulfide."
        ),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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


def _target_for(doc: dict[str, Any]) -> Target:
    target = TARGETS_BY_ID.get(doc.get("id"))
    if target is None:
        expected = ", ".join(sorted(TARGETS_BY_ID))
        raise ValueError(f"expected immutable id in {{{expected}}}, found {doc.get('id')!r}")

    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{target.path}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != target.media_term:
        raise ValueError(f"{target.path}: missing expected media term {target.media_term}")
    return target


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

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


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    doc["references"] = [
        {"reference": target.komodo_url},
        {"reference": DSMZ_409_URL},
        {"reference": DSMZ_194_URL},
        {"reference": DSMZ_193_URL},
        {"reference": DSMZ_320_URL},
        {"reference": DSMZ_141_URL},
    ]


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": target.komodo_url,
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


def _ingredient(component: Component) -> dict[str, Any]:
    term = _term(*component.term)
    return {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
        "term": term,
        "mediaingredientmech_chebi_term": term,
    }


def _components(target: Target) -> list[Component]:
    components = list(COMMON_COMPONENTS)
    if not target.omit_sulfate:
        components.insert(0, SULFATE)
    return components


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    target = _target_for(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_range", {"min": 7.1, "max": 7.4}, "physical_state")
    repaired["ingredients"] = [_ingredient(component) for component in _components(target)]
    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _ensure_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path))
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
