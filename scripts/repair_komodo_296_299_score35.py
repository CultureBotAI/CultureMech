#!/usr/bin/env python3
"""Repair empty KOMODO 296/299 PELOBACTER VENETIANUS variants."""

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

MARINE_TARGET = Path("bacterial/pelobacter_venetianus_marine_medium.yaml")
FRESHWATER_TARGET = Path("bacterial/pelobacter_venetianus_fresh_water_medium.yaml")

KOMODO_296_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=296"
)
KOMODO_299_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=299"
)
DSMZ_296_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium296.pdf"
)
DSMZ_299_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium299.pdf"
)
DSMZ_293_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium293.pdf"
)
DSMZ_298_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium298.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)

SOURCE_296 = "Archived DSMZ Medium 296"
SOURCE_299 = "Archived DSMZ Medium 299"
SOURCE_293 = "Archived DSMZ Medium 293"
SOURCE_298 = "Archived DSMZ Medium 298"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"

CURATOR = "repair_komodo_296_299_score35.py"
ACTION = "RESOLVED_KOMODO_296_299_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


@dataclass(frozen=True)
class Recipe:
    target: Path
    expected_id: str
    expected_media_term: str
    komodo_url: str
    dsmz_url: str
    notes: str
    components: tuple[Component, ...]


def _base_note(source: str, name: str, source_amount: str, value: str) -> str:
    return (
        f"{source} contributes {source_amount} {name} to a 1001 mL "
        f"formulation, yielding {value} g/L."
    )


def _trace_note(base_source: str, name: str, stock_amount: str, value: str) -> str:
    return (
        f"{base_source} adds 1 mL of the {SOURCE_320} to a 1001 mL "
        f"formulation; the SL-10 stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


def _peg_note(source: str, replaced: str) -> str:
    return (
        f"{source} replaces {replaced} with 1 g/L polyethylene glycol "
        "of molecular weight 106-20000."
    )


MEDIUM_293_COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.199800",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_293,
        _base_note(SOURCE_293, "KH2PO4", "0.20 g", "0.199800"),
    ),
    Component(
        "NH4Cl",
        "0.249750",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_293,
        _base_note(SOURCE_293, "NH4Cl", "0.25 g", "0.249750"),
    ),
    Component(
        "NaCl",
        "19.980020",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_293,
        _base_note(SOURCE_293, "NaCl", "20.00 g", "19.980020"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "2.997003",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_293,
        _base_note(SOURCE_293, "MgCl2 x 6 H2O", "3.00 g", "2.997003"),
    ),
    Component(
        "KCl",
        "0.499500",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_293,
        _base_note(SOURCE_293, "KCl", "0.50 g", "0.499500"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.149850",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_293,
        _base_note(SOURCE_293, "CaCl2 x 2 H2O", "0.15 g", "0.149850"),
    ),
    Component(
        "HCl",
        "0.002498",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note(SOURCE_293, "HCl", "2.50 g/L", "0.002498"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001499",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note(SOURCE_293, "FeCl2 x 4 H2O", "1.50 g/L", "0.001499"),
    ),
    Component(
        "ZnCl2",
        "0.0000699",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note(SOURCE_293, "ZnCl2", "0.070 g/L", "0.0000699"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000999",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note(SOURCE_293, "MnCl2 x 4 H2O", "0.100 g/L", "0.0000999"),
    ),
    Component(
        "H3BO3",
        "0.00000599",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note(SOURCE_293, "H3BO3", "0.006 g/L", "0.00000599"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000190",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
        _trace_note(SOURCE_293, "CoCl2 x 6 H2O", "0.190 g/L", "0.000190"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000200",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note(SOURCE_293, "CuCl2 x 2 H2O", "0.002 g/L", "0.00000200"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000240",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
        _trace_note(SOURCE_293, "NiCl2 x 6 H2O", "0.024 g/L", "0.0000240"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000360",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note(SOURCE_293, "Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000360"),
    ),
    Component(
        "Resazurin",
        "0.000999",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_293,
        _base_note(SOURCE_293, "Resazurin", "1.00 mg", "0.000999"),
    ),
    Component(
        "NaHCO3",
        "2.497502",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_293,
        _base_note(SOURCE_293, "NaHCO3", "2.50 g", "2.497502"),
    ),
    Component(
        "Polyethylene glycol",
        "1.000000",
        "G_PER_L",
        ("CHEBI:46793", "Polyethylene glycol"),
        SOURCE_296,
        _peg_note(SOURCE_296, "Na2-succinate"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.359640",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_293,
        _base_note(SOURCE_293, "Na2S x 9 H2O", "0.36 g", "0.359640"),
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_293,
        f"{SOURCE_293} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_293,
        f"{SOURCE_293} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_293,
        (
            f"{SOURCE_293} lists 1000 mL distilled water before adding the "
            "SL-10 trace solution and later anaerobic stock solutions."
        ),
    ),
)

MEDIUM_298_COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.199800",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_298,
        _base_note(SOURCE_298, "KH2PO4", "0.20 g", "0.199800"),
    ),
    Component(
        "NH4Cl",
        "0.249750",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_298,
        _base_note(SOURCE_298, "NH4Cl", "0.25 g", "0.249750"),
    ),
    Component(
        "NaCl",
        "0.999001",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_298,
        _base_note(SOURCE_298, "NaCl", "1.00 g", "0.999001"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.399600",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_298,
        _base_note(SOURCE_298, "MgCl2 x 6 H2O", "0.40 g", "0.399600"),
    ),
    Component(
        "KCl",
        "0.499500",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_298,
        _base_note(SOURCE_298, "KCl", "0.50 g", "0.499500"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.149850",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_298,
        _base_note(SOURCE_298, "CaCl2 x 2 H2O", "0.15 g", "0.149850"),
    ),
    Component(
        "HCl",
        "0.002498",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note(SOURCE_298, "HCl", "2.50 g/L", "0.002498"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001499",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note(SOURCE_298, "FeCl2 x 4 H2O", "1.50 g/L", "0.001499"),
    ),
    Component(
        "ZnCl2",
        "0.0000699",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note(SOURCE_298, "ZnCl2", "0.070 g/L", "0.0000699"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000999",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note(SOURCE_298, "MnCl2 x 4 H2O", "0.100 g/L", "0.0000999"),
    ),
    Component(
        "H3BO3",
        "0.00000599",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note(SOURCE_298, "H3BO3", "0.006 g/L", "0.00000599"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000190",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
        _trace_note(SOURCE_298, "CoCl2 x 6 H2O", "0.190 g/L", "0.000190"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000200",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note(SOURCE_298, "CuCl2 x 2 H2O", "0.002 g/L", "0.00000200"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000240",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
        _trace_note(SOURCE_298, "NiCl2 x 6 H2O", "0.024 g/L", "0.0000240"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000360",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note(SOURCE_298, "Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000360"),
    ),
    Component(
        "Resazurin",
        "0.000999",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_298,
        _base_note(SOURCE_298, "Resazurin", "1.00 mg", "0.000999"),
    ),
    Component(
        "NaHCO3",
        "2.497502",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_298,
        _base_note(SOURCE_298, "NaHCO3", "2.50 g", "2.497502"),
    ),
    Component(
        "Polyethylene glycol",
        "1.000000",
        "G_PER_L",
        ("CHEBI:46793", "Polyethylene glycol"),
        SOURCE_299,
        _peg_note(SOURCE_299, "2,3-butanediol"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.359640",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_298,
        _base_note(SOURCE_298, "Na2S x 9 H2O", "0.36 g", "0.359640"),
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_298,
        f"{SOURCE_298} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_298,
        f"{SOURCE_298} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_298,
        (
            f"{SOURCE_298} lists 1000 mL distilled water before adding the "
            "SL-10 trace solution and later anaerobic stock solutions."
        ),
    ),
)

RECIPES = (
    Recipe(
        target=MARINE_TARGET,
        expected_id="CultureMech:004760",
        expected_media_term="komodo.medium:296",
        komodo_url=KOMODO_296_URL,
        dsmz_url=DSMZ_296_URL,
        notes=(
            "Archived DSMZ Medium 296 defines PELOBACTER VENETIANUS "
            "(marine) MEDIUM as DSMZ Medium 293 with Na2-succinate "
            "replaced by 1 g/L polyethylene glycol of molecular weight "
            "106-20000; this record expands archived DSMZ Media 296, "
            "293, and 320 into final per-liter components."
        ),
        components=MEDIUM_293_COMPONENTS,
    ),
    Recipe(
        target=FRESHWATER_TARGET,
        expected_id="CultureMech:004774",
        expected_media_term="komodo.medium:299",
        komodo_url=KOMODO_299_URL,
        dsmz_url=DSMZ_299_URL,
        notes=(
            "Archived DSMZ Medium 299 defines PELOBACTER VENETIANUS "
            "(fresh water) MEDIUM as DSMZ Medium 298 with 2,3-butanediol "
            "replaced by 1 g/L polyethylene glycol of molecular weight "
            "106-20000; this record expands archived DSMZ Media 299, "
            "298, and 320 into final per-liter components."
        ),
        components=MEDIUM_298_COMPONENTS,
    ),
)

BASE_URLS = {
    SOURCE_293: DSMZ_293_URL,
    SOURCE_298: DSMZ_298_URL,
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _check_source(doc: dict[str, Any], recipe: Recipe) -> None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{recipe.target}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != recipe.expected_media_term:
        raise ValueError(
            f"{recipe.target}: missing expected media term "
            f"{recipe.expected_media_term}"
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


def _ensure_flags(doc: dict[str, Any], recipe: Recipe) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{recipe.target}: data_quality_flags is not a list")

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


def _ensure_references(doc: dict[str, Any], recipe: Recipe) -> None:
    base_sources = sorted(
        {
            component.source
            for component in recipe.components
            if component.source in BASE_URLS
        }
    )
    doc["references"] = [
        {"reference": recipe.komodo_url},
        {"reference": recipe.dsmz_url},
        *({"reference": BASE_URLS[source]} for source in base_sources),
        {"reference": DSMZ_320_URL},
    ]


def _ensure_event(doc: dict[str, Any], recipe: Recipe) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": recipe.komodo_url,
        "notes": recipe.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{recipe.target}: curation_history is not a list")
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


def repair_record(doc: dict[str, Any], recipe: Recipe) -> dict[str, Any]:
    if doc.get("id") != recipe.expected_id:
        raise ValueError(
            f"{recipe.target}: expected immutable id {recipe.expected_id}, "
            f"found {doc.get('id')!r}"
        )
    _check_source(doc, recipe)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
    repaired["ingredients"] = [
        _ingredient(component) for component in recipe.components
    ]
    _put_after(repaired, "notes", recipe.notes, "media_term")
    _ensure_flags(repaired, recipe)
    _ensure_references(repaired, recipe)
    _ensure_event(repaired, recipe)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / recipe.target: repair_record(
            _load(normalized / recipe.target),
            recipe,
        )
        for recipe in RECIPES
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
