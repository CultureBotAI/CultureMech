#!/usr/bin/env python3
"""Repair empty KOMODO 1254 NAUTILIA NITRATIREDUCENS MEDIUM."""

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
from repair_komodo_324_score30 import DSMZ_141_URL, Component, _term  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("bacterial/KOMODO_1254_NAUTILIA_NITRATIREDUCENS_MEDIUM.yaml")
EXPECTED_ID = "CultureMech:004015"
EXPECTED_MEDIA_TERM = "komodo.medium:1254"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_1254_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1254"
)
DSMZ_1254_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1254.pdf"
)

SOURCE_1254 = "Archived DSMZ Medium 1254"
SOURCE_141 = "Archived DSMZ Medium 141"

CURATOR = "repair_komodo_1254_score30.py"
ACTION = "RESOLVED_KOMODO_1254_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 1254 defines NAUTILIA NITRATIREDUCENS MEDIUM as "
    "a defined seawater salts formulation with 10 mL DSMZ Medium 141 trace "
    "elements, resazurin, KNO3, PIPES, and Na2S under 80:20 H2/CO2 at "
    "pH 7.0; this record expands the trace stock into final per-liter "
    "components after the 1.010 L trace-adjusted formulation."
)


def _main_note(name: str, amount: str, value: str) -> str:
    return (
        f"{SOURCE_1254} lists {amount} {name} with 1000 mL water and "
        f"10 mL DSMZ Medium 141 trace elements, yielding {value} g/L "
        "in the 1010 mL trace-adjusted formulation."
    )


def _combined_note(name: str, base: str, stock: str, value: str) -> str:
    return (
        f"{SOURCE_1254} lists {base} {name} in the main recipe and adds "
        f"10 mL of {SOURCE_141} trace elements containing {stock} {name}, "
        f"yielding {value} g/L in the 1010 mL trace-adjusted formulation."
    )


def _trace_note(name: str, stock: str, value: str) -> str:
    return (
        f"{SOURCE_1254} adds 10 mL of {SOURCE_141} trace elements "
        f"containing {stock} {name}, yielding {value} g/L in the 1010 mL "
        "trace-adjusted formulation."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "NaCl",
        "19.811881",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_1254,
        _combined_note("NaCl", "20.00 g", "1.00 g/L", "19.811881"),
    ),
    Component(
        "MgSO4 x 7 H2O",
        "3.495050",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_1254,
        _combined_note("MgSO4 x 7 H2O", "3.50 g", "3.00 g/L", "3.495050"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "2.722772",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_1254,
        _main_note("MgCl2 x 6 H2O", "2.75 g", "2.722772"),
    ),
    Component(
        "KCl",
        "0.326733",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_1254,
        _main_note("KCl", "0.33 g", "0.326733"),
    ),
    Component(
        "NaBr",
        "0.049505",
        "G_PER_L",
        ("CHEBI:63004", "sodium bromide"),
        SOURCE_1254,
        _main_note("NaBr", "0.05 g", "0.049505"),
    ),
    Component(
        "H3BO3",
        "0.019901",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_1254,
        _combined_note("H3BO3", "0.02 g", "0.01 g/L", "0.019901"),
    ),
    Component(
        "SrCl2 x 6 H2O",
        "0.007426",
        "G_PER_L",
        ("CHEBI:36385", "strontium dichloride hexahydrate"),
        SOURCE_1254,
        _main_note("SrCl2 x 6 H2O", "7.50 mg", "0.007426"),
    ),
    Component(
        "(NH4)2SO4",
        "0.009901",
        "G_PER_L",
        ("CHEBI:62946", "ammonium sulfate"),
        SOURCE_1254,
        _main_note("(NH4)2SO4", "0.01 g", "0.009901"),
    ),
    Component(
        "KI",
        "0.000049505",
        "G_PER_L",
        ("CHEBI:8346", "potassium iodide"),
        SOURCE_1254,
        _main_note("KI", "0.05 mg", "0.000049505"),
    ),
    Component(
        "Na2WO4 x 2 H2O",
        "0.000099",
        "G_PER_L",
        ("CHEBI:63939", "sodium tungstate dihydrate"),
        SOURCE_1254,
        _main_note("Na2WO4 x 2 H2O", "0.10 mg", "0.000099"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.743564",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_1254,
        _combined_note("CaCl2 x 2 H2O", "0.75 g", "0.10 g/L", "0.743564"),
    ),
    Component(
        "KH2PO4",
        "0.495050",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_1254,
        _main_note("KH2PO4", "0.50 g", "0.495050"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.002277",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_1254,
        _combined_note("NiCl2 x 6 H2O", "2.00 mg", "0.03 g/L", "0.002277"),
    ),
    Component(
        "Nitrilotriacetic acid",
        "0.014851",
        "G_PER_L",
        ("CHEBI:44557", "nitrilotriacetic acid"),
        SOURCE_141,
        _trace_note("Nitrilotriacetic acid", "1.50 g/L", "0.014851"),
    ),
    Component(
        "MnSO4 x H2O",
        "0.004950",
        "G_PER_L",
        ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
        SOURCE_141,
        _trace_note("MnSO4 x H2O", "0.50 g/L", "0.004950"),
    ),
    Component(
        "FeSO4 x 7 H2O",
        "0.000990",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("FeSO4 x 7 H2O", "0.10 g/L", "0.000990"),
    ),
    Component(
        "CoSO4 x 7 H2O",
        "0.001782",
        "G_PER_L",
        ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("CoSO4 x 7 H2O", "0.18 g/L", "0.001782"),
    ),
    Component(
        "ZnSO4 x 7 H2O",
        "0.001782",
        "G_PER_L",
        ("CHEBI:32312", "zinc sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("ZnSO4 x 7 H2O", "0.18 g/L", "0.001782"),
    ),
    Component(
        "CuSO4 x 5 H2O",
        "0.000099",
        "G_PER_L",
        ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
        SOURCE_141,
        _trace_note("CuSO4 x 5 H2O", "0.01 g/L", "0.000099"),
    ),
    Component(
        "KAl(SO4)2 x 12 H2O",
        "0.000198",
        "G_PER_L",
        ("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
        SOURCE_141,
        _trace_note("KAl(SO4)2 x 12 H2O", "0.02 g/L", "0.000198"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.000099",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_141,
        _trace_note("Na2MoO4 x 2 H2O", "0.01 g/L", "0.000099"),
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "0.000002970",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_141,
        _trace_note("Na2SeO3 x 5 H2O", "0.30 mg/L", "0.000002970"),
    ),
    Component(
        "KOH",
        "variable",
        "VARIABLE",
        ("CHEBI:32035", "potassium hydroxide"),
        SOURCE_141,
        (
            f"{SOURCE_141} adjusts the trace element solution with KOH; "
            f"{SOURCE_1254} adds 10 mL of that trace solution."
        ),
    ),
    Component(
        "Resazurin",
        "0.000495",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_1254,
        _main_note("Resazurin", "0.50 mg", "0.000495"),
    ),
    Component(
        "KNO3",
        "0.990099",
        "G_PER_L",
        ("CHEBI:63043", "potassium nitrate"),
        SOURCE_1254,
        _main_note("KNO3", "1.00 g", "0.990099"),
    ),
    Component(
        "PIPES",
        "3.762376",
        "G_PER_L",
        ("CHEBI:39033", "PIPES"),
        SOURCE_1254,
        _main_note("PIPES", "3.80 g", "3.762376"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.495050",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_1254,
        _main_note("Na2S x 9 H2O", "0.50 g", "0.495050"),
    ),
    Component(
        "H2",
        "variable",
        "VARIABLE",
        ("CHEBI:18276", "dihydrogen"),
        SOURCE_1254,
        f"{SOURCE_1254} cools and dispenses the medium under 80% H2 plus 20% CO2.",
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_1254,
        f"{SOURCE_1254} cools and dispenses the medium under 80% H2 plus 20% CO2.",
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_1254,
        f"{SOURCE_1254} lists 1000 mL distilled water before stock additions.",
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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
        {"reference": KOMODO_1254_URL},
        {"reference": DSMZ_1254_URL},
        {"reference": DSMZ_141_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_1254_URL,
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
            f"{TARGET}: expected immutable id {EXPECTED_ID}, " f"found {doc.get('id')!r}"
        )
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_value"] = 7.0
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
