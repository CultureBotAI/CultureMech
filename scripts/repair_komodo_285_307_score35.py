#!/usr/bin/env python3
"""Repair empty KOMODO 285 and 307 DSMZ Medium 212 variants."""

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

KOMODO_BASE_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)
DSMZ_285_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium285.pdf"
)
DSMZ_307_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium307.pdf"
)
DSMZ_212_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium212.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)

SOURCE_285 = "Archived DSMZ Medium 285"
SOURCE_307 = "Archived DSMZ Medium 307"
SOURCE_212 = "Archived DSMZ Medium 212"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"

CURATOR = "repair_komodo_285_307_score35.py"
TIMESTAMP = "2026-09-10T00:00:00-07:00"


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str] | None
    source: str
    notes: str


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str
    komodo_id: str
    dsmz_url: str
    action: str
    notes: str
    substrate: Component
    include_sulfate: bool

    @property
    def komodo_url(self) -> str:
        return f"{KOMODO_BASE_URL}{self.komodo_id}"


def _mineral_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_212} adds 50 mL of its mineral solution per 1006 mL final "
        f"formulation; the mineral stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


def _base_note(name: str, source_amount: str, value: str) -> str:
    return (
        f"{SOURCE_212} contributes {source_amount} {name} to the 1006 mL "
        f"final formulation, yielding {value} g/L."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_212} adds 1 mL of the {SOURCE_320} per 1006 mL final "
        f"formulation; the SL-10 stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_212} adds 5 mL of its vitamin solution per 1006 mL final "
        f"formulation; the vitamin stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


BASE_BEFORE_SULFATE: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.497018",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_212,
        _mineral_note("KH2PO4", "10.00 g/L", "0.497018"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.328032",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_212,
        _mineral_note("MgCl2 x 6 H2O", "6.60 g/L", "0.328032"),
    ),
    Component(
        "NaCl",
        "0.397614",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_212,
        _mineral_note("NaCl", "8.00 g/L", "0.397614"),
    ),
    Component(
        "NH4Cl",
        "0.397614",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_212,
        _mineral_note("NH4Cl", "8.00 g/L", "0.397614"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.049702",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_212,
        _mineral_note("CaCl2 x 2 H2O", "1.00 g/L", "0.049702"),
    ),
    Component(
        "HCl",
        "0.002485",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note("HCl", "2.50 g/L", "0.002485"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001491",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001491"),
    ),
    Component(
        "ZnCl2",
        "0.0000696",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note("ZnCl2", "0.070 g/L", "0.0000696"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000994",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000994"),
    ),
    Component(
        "H3BO3",
        "0.00000596",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note("H3BO3", "0.006 g/L", "0.00000596"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000189",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
        _trace_note("CoCl2 x 6 H2O", "0.190 g/L", "0.000189"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000199",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note("CuCl2 x 2 H2O", "0.002 g/L", "0.00000199"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000239",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
        _trace_note("NiCl2 x 6 H2O", "0.024 g/L", "0.0000239"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000358",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note("Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000358"),
    ),
    Component(
        "Trypticase",
        "0.994036",
        "G_PER_L",
        None,
        SOURCE_212,
        _base_note("Trypticase", "1.00 g", "0.994036"),
    ),
    Component(
        "Rumen fluid, clarified",
        "49.701789",
        "ML_PER_L",
        None,
        SOURCE_212,
        (
            f"{SOURCE_212} contributes 50 mL clarified rumen fluid to the "
            "1006 mL final formulation, yielding 49.701789 mL/L."
        ),
    ),
)

SULFATE = Component(
    "Na2SO4",
    "2.783300",
    "G_PER_L",
    ("CHEBI:32149", "sodium sulfate"),
    SOURCE_212,
    _base_note("Na2SO4", "2.80 g", "2.783300"),
)

BASE_AFTER_SUBSTRATE: tuple[Component, ...] = (
    Component(
        "Cysteine-HCl x H2O",
        "0.298211",
        "G_PER_L",
        ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
        SOURCE_212,
        _base_note("Cysteine-HCl x H2O", "0.30 g", "0.298211"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.298211",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_212,
        _base_note("Na2S x 9 H2O", "0.30 g", "0.298211"),
    ),
    Component(
        "Biotin",
        "0.00000124",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_212,
        _vitamin_note("Biotin", "0.25 mg/L", "0.00000124"),
    ),
    Component(
        "Nicotinic acid",
        "0.0000124",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_212,
        _vitamin_note("Nicotinic acid", "2.50 mg/L", "0.0000124"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.00000621",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_212,
        _vitamin_note("Thiamine-HCl x 2 H2O", "1.25 mg/L", "0.00000621"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.00000621",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_212,
        _vitamin_note("p-Aminobenzoic acid", "1.25 mg/L", "0.00000621"),
    ),
    Component(
        "Pantothenic acid",
        "0.00000308",
        "G_PER_L",
        ("CHEBI:7916", "pantothenic acid"),
        SOURCE_212,
        _vitamin_note("Pantothenic acid", "0.62 mg/L", "0.00000308"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.0000308",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_212,
        _vitamin_note("Pyridoxine-HCl", "6.20 mg/L", "0.0000308"),
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_212,
        f"{SOURCE_212} prepares solutions A and B under 80% N2 and 20% CO2.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_212,
        f"{SOURCE_212} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "Distilled water",
        "900.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_212,
        (
            f"{SOURCE_212} lists 900 mL direct distilled water across "
            "solutions A-D before adding mineral, trace, vitamin, and "
            "rumen-fluid stocks."
        ),
    ),
)

RESAZURIN = Component(
    "Resazurin",
    "0.000994",
    "G_PER_L",
    ("CHEBI:8806", "Resazurin"),
    SOURCE_212,
    _base_note("Resazurin", "1 mg", "0.000994"),
)
NAHCO3 = Component(
    "NaHCO3",
    "3.479125",
    "G_PER_L",
    ("CHEBI:32139", "sodium hydrogencarbonate"),
    SOURCE_212,
    _base_note("NaHCO3", "3.50 g", "3.479125"),
)

TARGETS: tuple[Target, ...] = (
    Target(
        path=Path("bacterial/syntrophus_medium_sulfate_free.yaml"),
        expected_id="CultureMech:004742",
        expected_media_term="komodo.medium:285",
        komodo_id="285",
        dsmz_url=DSMZ_285_URL,
        action="RESOLVED_KOMODO_285_SCORE35",
        notes=(
            "Archived DSMZ Medium 285 defines SYNTROPHUS MEDIUM - SULFATE "
            "FREE as DSMZ Medium 212 without Na2SO4 and with 2.0 g/L sodium "
            "benzoate replacing butyric acid; this record expands archived "
            "DSMZ Media 212, 285, and 320 into final per-liter components."
        ),
        substrate=Component(
            "sodium benzoate",
            "2.000000",
            "G_PER_L",
            ("CHEBI:113455", "sodium benzoate"),
            SOURCE_285,
            f"{SOURCE_285} replaces butyric acid with 2.0 g/L sodium benzoate.",
        ),
        include_sulfate=False,
    ),
    Target(
        path=Path("bacterial/syntrophobacter_wolinii_medium.yaml"),
        expected_id="CultureMech:004866",
        expected_media_term="komodo.medium:307",
        komodo_id="307",
        dsmz_url=DSMZ_307_URL,
        action="RESOLVED_KOMODO_307_SCORE35",
        notes=(
            "Archived DSMZ Medium 307 defines SYNTROPHOBACTER WOLINII "
            "MEDIUM as DSMZ Medium 212 with 1.5 g/L sodium propionate "
            "replacing butyric acid; this record expands archived DSMZ "
            "Media 212, 307, and 320 into final per-liter components."
        ),
        substrate=Component(
            "sodium propionate",
            "1.500000",
            "G_PER_L",
            ("CHEBI:132106", "sodium propionate"),
            SOURCE_307,
            f"{SOURCE_307} replaces butyric acid with 1.5 g/L sodium propionate.",
        ),
        include_sulfate=True,
    ),
)


def _components(target: Target) -> list[Component]:
    components = [*BASE_BEFORE_SULFATE]
    if target.include_sulfate:
        components.append(SULFATE)
    components.extend((RESAZURIN, NAHCO3, target.substrate, *BASE_AFTER_SUBSTRATE))
    return components


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
            f"{target.path}: missing expected media term {target.expected_media_term}"
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
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)

    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    doc["references"] = [
        {"reference": target.komodo_url},
        {"reference": target.dsmz_url},
        {"reference": DSMZ_212_URL},
        {"reference": DSMZ_320_URL},
    ]


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": target.action,
        "source": target.dsmz_url,
        "notes": target.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.path}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == target.action
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
    }
    if component.term is not None:
        term = _term(*component.term)
        row["term"] = term
        row["mediaingredientmech_chebi_term"] = term
    return row


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected immutable id {target.expected_id}, "
            f"found {doc.get('id')!r}"
        )
    _check_source(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
    repaired["ingredients"] = [
        _ingredient(component) for component in _components(target)
    ]
    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired, target)
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
