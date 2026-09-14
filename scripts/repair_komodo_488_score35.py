#!/usr/bin/env python3
"""Repair empty KOMODO 488 DESULFOVIBRIO ALCOHOLOVORANS records."""

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

KOMODO_488_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=488"
)
KOMODO_488_REPLACE_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed"
    "?MediaInfo=488_replace_DESULFOVIBRIO%20medium_with_DESULFOBULBUS%20MEDIUM"
)
DSMZ_488_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium488.pdf"
)
DSMZ_63_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium63.pdf"
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

SOURCE_488 = "Archived DSMZ Medium 488"
SOURCE_63 = "Archived DSMZ Medium 63"
SOURCE_194 = "Archived DSMZ Medium 194"
SOURCE_193 = "Archived DSMZ Medium 193"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"
SOURCE_141 = "Archived DSMZ Medium 141 vitamin solution"

CURATOR = "repair_komodo_488_score35.py"
ACTION = "RESOLVED_KOMODO_488_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES_63 = (
    "Archived DSMZ Medium 488 defines DESULFOVIBRIO ALCOHOLOVORANS MEDIUM as "
    "DSMZ Medium 63 or 194 with 1.5 g/L 1,2-propanediol as substrate and "
    "3 micrograms/L Na2SeO3 x 5 H2O; KOMODO Medium 488 expands the DSMZ "
    "Medium 63 branch, so this record expands archived DSMZ Media 488 and 63 "
    "into final per-liter components."
)
NOTES_194 = (
    "Archived DSMZ Medium 488 defines DESULFOVIBRIO ALCOHOLOVORANS MEDIUM as "
    "DSMZ Medium 63 or 194 with 1.5 g/L 1,2-propanediol as substrate and "
    "3 micrograms/L Na2SeO3 x 5 H2O; the KOMODO replacement variant expands "
    "the DSMZ Medium 194 branch, so this record expands archived DSMZ Media "
    "488, 194, 193, 320, and 141 into final per-liter components."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_media_term: str
    medium_type: str
    composition_type: str
    ph_key: str
    ph_value: float | dict[str, float]
    notes: str
    components: tuple[Component, ...]
    references: tuple[str, ...]


def _medium_63_note(name: str, amount: str) -> str:
    return f"{SOURCE_63} lists {amount} {name} in the final 1000 mL medium."


def _base_note(name: str, source_amount: str, value: str) -> str:
    return (
        f"{SOURCE_193} contributes {source_amount} {name} to a 1001 mL "
        f"final formulation, yielding {value} g/L."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_193} adds 1 mL of the {SOURCE_320} to a 1001 mL final "
        f"formulation; the SL-10 stock contains {stock_amount} {name}, yielding "
        f"{value} g/L."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_193} adds 10 mL of the {SOURCE_141} to a 1001 mL final "
        f"formulation; the vitamin stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


MEDIUM_63_COMPONENTS: tuple[Component, ...] = (
    Component(
        "K2HPO4",
        "0.50",
        "G_PER_L",
        ("CHEBI:131527", "dipotassium hydrogen phosphate"),
        SOURCE_63,
        _medium_63_note("K2HPO4", "0.50 g"),
    ),
    Component(
        "NH4Cl",
        "1.00",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_63,
        _medium_63_note("NH4Cl", "1.00 g"),
    ),
    Component(
        "Na2SO4",
        "1.00",
        "G_PER_L",
        ("CHEBI:32149", "sodium sulfate"),
        SOURCE_63,
        _medium_63_note("Na2SO4", "1.00 g"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.10",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_63,
        _medium_63_note("CaCl2 x 2 H2O", "0.10 g"),
    ),
    Component(
        "MgSO4 x 7 H2O",
        "2.00",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_63,
        _medium_63_note("MgSO4 x 7 H2O", "2.00 g"),
    ),
    Component(
        "DL-Na-lactate",
        "2.00",
        "G_PER_L",
        ("CHEBI:75228", "sodium lactate"),
        SOURCE_63,
        _medium_63_note("DL-Na-lactate", "2.00 g"),
    ),
    Component(
        "Yeast extract",
        "1.00",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_63,
        _medium_63_note("Yeast extract", "1.00 g"),
    ),
    Component(
        "Resazurin",
        "0.001000",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_63,
        _medium_63_note("Resazurin", "1.00 mg"),
    ),
    Component(
        "FeSO4 x 7 H2O",
        "0.50",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_63,
        _medium_63_note("FeSO4 x 7 H2O", "0.50 g"),
    ),
    Component(
        "Na-thioglycolate",
        "0.10",
        "G_PER_L",
        ("CHEBI:86481", "sodium thioglycolate"),
        SOURCE_63,
        _medium_63_note("Na-thioglycolate", "0.10 g"),
    ),
    Component(
        "Ascorbic acid",
        "0.10",
        "G_PER_L",
        ("CHEBI:22652", "ascorbic acid"),
        SOURCE_63,
        _medium_63_note("Ascorbic acid", "0.10 g"),
    ),
    Component(
        "1,2-propanediol",
        "1.50",
        "G_PER_L",
        ("CHEBI:16997", "propane-1,2-diol"),
        SOURCE_488,
        f"{SOURCE_488} adds 1.5 g/L 1,2-propanediol as the substrate.",
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "3.0",
        "MICROG_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_488,
        f"{SOURCE_488} adds 3 micrograms/L Na2SeO3 x 5 H2O.",
    ),
    Component(
        "NaOH",
        "variable",
        "VARIABLE",
        ("CHEBI:32145", "sodium hydroxide"),
        SOURCE_63,
        f"{SOURCE_63} adjusts the final pH to 7.8 with NaOH.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_63,
        f"{SOURCE_63} gasses the medium with oxygen-free N2.",
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_63,
        (
            f"{SOURCE_63} combines 980 mL distilled water in Solution A, "
            "10 mL in Solution B, and 10 mL in Solution C."
        ),
    ),
)

MEDIUM_194_COMPONENTS: tuple[Component, ...] = (
    Component(
        "Na2SO4",
        "2.997003",
        "G_PER_L",
        ("CHEBI:32149", "sodium sulfate"),
        SOURCE_193,
        _base_note("Na2SO4", "3.00 g", "2.997003"),
    ),
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
        "Sodium propionate",
        "1.500000",
        "G_PER_L",
        ("CHEBI:132106", "sodium propionate"),
        SOURCE_194,
        f"{SOURCE_194} replaces sodium acetate with 1.5 g/L sodium propionate.",
    ),
    Component(
        "1,2-propanediol",
        "1.50",
        "G_PER_L",
        ("CHEBI:16997", "propane-1,2-diol"),
        SOURCE_488,
        f"{SOURCE_488} adds 1.5 g/L 1,2-propanediol as the substrate.",
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
        "0.399600",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_193,
        _base_note("Na2S x 9 H2O", "0.40 g", "0.399600"),
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "3.0",
        "MICROG_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_488,
        f"{SOURCE_488} adds 3 micrograms/L Na2SeO3 x 5 H2O.",
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
            f"{SOURCE_488} adds 1,2-propanediol and Na2SeO3 x 5 H2O."
        ),
    ),
)

TARGETS: tuple[Target, ...] = (
    Target(
        "bacterial/desulfovibrio_alcoholovorans_medium.yaml",
        "CultureMech:005613",
        "komodo.medium:488",
        "COMPLEX",
        "UNDEFINED",
        "ph_value",
        7.8,
        NOTES_63,
        MEDIUM_63_COMPONENTS,
        (KOMODO_488_URL, DSMZ_488_URL, DSMZ_63_URL),
    ),
    Target(
        (
            "bacterial/desulfovibrio_alcoholovorans_medium_replace_"
            "desulfovibrio_medium_with_desulfobulbus_medium.yaml"
        ),
        "CultureMech:005612",
        "komodo.medium:488_replace_DESULFOVIBRIO medium_with_DESULFOBULBUS MEDIUM",
        "DEFINED",
        "DEFINED",
        "ph_range",
        {"min": 7.1, "max": 7.4},
        NOTES_194,
        MEDIUM_194_COMPONENTS,
        (
            KOMODO_488_REPLACE_URL,
            DSMZ_488_URL,
            DSMZ_194_URL,
            DSMZ_193_URL,
            DSMZ_320_URL,
            DSMZ_141_URL,
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


def _check_source(doc: dict[str, Any], target: Target) -> None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{target.path}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != target.expected_media_term:
        raise ValueError(
            f"{target.path}: missing expected media term " f"{target.expected_media_term}"
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


def _ensure_flags(doc: dict[str, Any], target: Target) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{target.path}: data_quality_flags is not a list")

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


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.references:
        if url not in found:
            references.append({"reference": url})


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Replaced empty KOMODO 488 composition with archived DSMZ data",
        "source": DSMZ_488_URL,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected immutable id {target.expected_id}, "
            f"found {doc.get('id')!r}"
        )
    _check_source(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = target.medium_type
    repaired["composition_type"] = target.composition_type
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, target.ph_key, target.ph_value, "physical_state")
    repaired["ingredients"] = [_ingredient(component) for component in target.components]
    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired, target)
    _ensure_references(repaired, target)
    _ensure_event(repaired, target)
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
