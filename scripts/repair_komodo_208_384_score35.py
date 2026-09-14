#!/usr/bin/env python3
"""Repair empty KOMODO 208/384 Desulfovibrio records."""

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

KOMODO_208_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=208"
)
KOMODO_384_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=384"
)
DSMZ_208_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium208.pdf"
)
DSMZ_384_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium384.pdf"
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

SOURCE_208 = "Archived DSMZ Medium 208"
SOURCE_384 = "Archived DSMZ Medium 384"
SOURCE_194 = "Archived DSMZ Medium 194"
SOURCE_193 = "Archived DSMZ Medium 193"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"
SOURCE_141 = "Archived DSMZ Medium 141 vitamin solution"

CURATOR = "repair_komodo_208_384_score35.py"
ACTION = "RESOLVED_KOMODO_208_384_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES_208 = (
    "Archived DSMZ Medium 208 defines DESULFOVIBRIO BAARSII MEDIUM as DSMZ "
    "Medium 193 with NaCl set to 7 g/L, MgCl2 x 6 H2O set to 0.6 g/L, and "
    "sodium acetate replaced with Na-butyrate, Na-caproate, and Na-octanoate; "
    "this record expands archived DSMZ Media 193, 208, 320, and 141 into "
    "final per-liter components."
)
NOTES_384 = (
    "Archived DSMZ Medium 384 defines DESULFOVIBRIO CARBINOLICUS MEDIUM as "
    "DSMZ Medium 194 with ethanol replacing sodium propionate and optional "
    "0.1 g/L yeast extract and casamino acids; KOMODO Medium 384 includes "
    "both optional complex nutrients, so this record expands archived DSMZ "
    "Media 193, 194, 384, 320, and 141 into final per-liter components."
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
    primary_source: str
    notes: str
    components: tuple[Component, ...]
    references: tuple[str, ...]


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
        f"{SOURCE_193} adds 10 mL of the {SOURCE_141} to a 1001 mL final "
        f"formulation; the vitamin stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


BASE_PREFIX_1001 = (
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
)

BASE_SUFFIX_1001 = (
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
)

TRACE_1001 = (
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
)

NAHCO3_1001 = Component(
    "NaHCO3",
    "4.995005",
    "G_PER_L",
    ("CHEBI:32139", "sodium hydrogencarbonate"),
    SOURCE_193,
    _base_note("NaHCO3", "5.00 g", "4.995005"),
)

VITAMINS_1001 = (
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
)

BASE_END_1001 = (
    Component(
        "Na2S x 9 H2O",
        "0.399600",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_193,
        _base_note("Na2S x 9 H2O", "0.40 g", "0.399600"),
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
)

MEDIUM_208_COMPONENTS: tuple[Component, ...] = (
    *BASE_PREFIX_1001,
    Component(
        "NaCl",
        "7.000000",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_208,
        f"{SOURCE_208} sets the DSMZ Medium 193 NaCl amount to 7 g/L.",
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.600000",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_208,
        f"{SOURCE_208} sets the DSMZ Medium 193 MgCl2 x 6 H2O amount to 0.6 g/L.",
    ),
    *BASE_SUFFIX_1001,
    *TRACE_1001,
    NAHCO3_1001,
    Component(
        "Na-butyrate",
        "0.700000",
        "G_PER_L",
        ("CHEBI:64103", "sodium butyrate"),
        SOURCE_208,
        f"{SOURCE_208} replaces sodium acetate with 0.70 g/L Na-butyrate.",
    ),
    Component(
        "Na-caproate",
        "0.300000",
        "G_PER_L",
        ("CHEBI:114126", "sodium hexanoate"),
        SOURCE_208,
        f"{SOURCE_208} replaces sodium acetate with 0.30 g/L Na-caproate.",
    ),
    Component(
        "Na-octanoate",
        "0.150000",
        "G_PER_L",
        ("CHEBI:132100", "sodium octanoate"),
        SOURCE_208,
        f"{SOURCE_208} replaces sodium acetate with 0.15 g/L Na-octanoate.",
    ),
    *VITAMINS_1001,
    *BASE_END_1001,
    Component(
        "Distilled water",
        "990.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_193,
        (
            f"{SOURCE_193} lists 990 mL direct distilled water across "
            "solutions A, C, D, and F before stock additions and before "
            f"{SOURCE_208} replaces sodium acetate with fatty acid salts."
        ),
    ),
)

MEDIUM_384_COMPONENTS: tuple[Component, ...] = (
    *BASE_PREFIX_1001,
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
    *BASE_SUFFIX_1001,
    *TRACE_1001,
    NAHCO3_1001,
    Component(
        "Ethanol",
        "0.700000",
        "G_PER_L",
        ("CHEBI:16236", "ethanol"),
        SOURCE_384,
        f"{SOURCE_384} replaces sodium propionate with 0.7 g/L ethanol.",
    ),
    Component(
        "Yeast extract",
        "0.100000",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_384,
        (
            f"{SOURCE_384} allows 0.1 g/L yeast extract; KOMODO Medium 384 "
            "includes this optional component."
        ),
    ),
    Component(
        "Casamino acid",
        "0.100000",
        "G_PER_L",
        ("FOODON:03315719", "mammalian milk protein (hydrolyzed)"),
        SOURCE_384,
        (
            f"{SOURCE_384} allows 0.1 g/L casamino acids; KOMODO Medium 384 "
            "includes this optional component."
        ),
    ),
    *VITAMINS_1001,
    *BASE_END_1001,
    Component(
        "Distilled water",
        "990.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_193,
        (
            f"{SOURCE_193} lists 990 mL direct distilled water across "
            "solutions A, C, D, and F before stock additions and before "
            f"{SOURCE_384} replaces sodium propionate with ethanol."
        ),
    ),
)

TARGETS: tuple[Target, ...] = (
    Target(
        "bacterial/desulfovibrio_baarsii_medium.yaml",
        "CultureMech:004368",
        "komodo.medium:208",
        "DEFINED",
        "DEFINED",
        DSMZ_208_URL,
        NOTES_208,
        MEDIUM_208_COMPONENTS,
        (KOMODO_208_URL, DSMZ_208_URL, DSMZ_193_URL, DSMZ_320_URL, DSMZ_141_URL),
    ),
    Target(
        "bacterial/desulfovibrio_carbinolicus_medium.yaml",
        "CultureMech:005160",
        "komodo.medium:384",
        "COMPLEX",
        "UNDEFINED",
        DSMZ_384_URL,
        NOTES_384,
        MEDIUM_384_COMPONENTS,
        (
            KOMODO_384_URL,
            DSMZ_384_URL,
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
            f"{target.path}: missing expected media term "
            f"{target.expected_media_term}"
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
        "changes": "Replaced empty KOMODO 208/384 compositions with archived DSMZ data",
        "source": target.primary_source,
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
    _put_after(repaired, "ph_range", {"min": 7.1, "max": 7.4}, "physical_state")
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
