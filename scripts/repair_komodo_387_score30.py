#!/usr/bin/env python3
"""Repair empty KOMODO 387 THERMOPHILIC METHANOSAETA MEDIUM."""

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
TARGET = Path("archaea/thermophilic_methanosaeta_medium.yaml")
EXPECTED_ID = "CultureMech:005164"
EXPECTED_MEDIA_TERM = "komodo.medium:387"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_387_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=387"
)
DSMZ_387_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium387.pdf"
)

SOURCE_387 = "Archived DSMZ Medium 387"
SOURCE_141 = "Archived DSMZ Medium 141"

CURATOR = "repair_komodo_387_score30.py"
ACTION = "RESOLVED_KOMODO_387_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 387 defines THERMOPHILIC METHANOSAETA MEDIUM as "
    "940 mL distilled water with NH4Cl, K2HPO4, MgCl2, resazurin, and "
    "DSMZ Medium 141 trace elements, followed after autoclaving by anoxic "
    "NaHCO3, CaCl2, Na-acetate, DSMZ Medium 141 vitamins, Coenzyme M, and "
    "Na2S stocks; this record expands the trace and vitamin stocks into "
    "final per-liter components after the 1.015 L final volume."
)


def _base_note(name: str, amount: str, value: str) -> str:
    return (
        f"{SOURCE_387} lists {amount} {name} in 940 mL water with 10 mL "
        f"trace elements and 65 mL of post-autoclave stocks, yielding "
        f"{value} g/L in the 1015 mL final formulation."
    )


def _stock_note(name: str, stock: str, volume: str, value: str) -> str:
    return (
        f"{SOURCE_387} adds {volume} of an anoxic sterile {stock} {name} "
        f"stock per liter medium after autoclaving, yielding {value} g/L "
        "in the 1015 mL final formulation."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_387} adds 10 mL of {SOURCE_141} trace elements containing "
        f"{stock_amount} {name}, yielding {value} g/L in the 1015 mL final "
        "formulation."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_387} adds 10 mL of {SOURCE_141} vitamin solution containing "
        f"{stock_amount} {name}, yielding {value} g/L in the 1015 mL final "
        "formulation."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "NH4Cl",
        "0.492611",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_387,
        _base_note("NH4Cl", "0.5 g", "0.492611"),
    ),
    Component(
        "K2HPO4",
        "0.394089",
        "G_PER_L",
        ("CHEBI:131527", "dipotassium hydrogen phosphate"),
        SOURCE_387,
        _base_note("K2HPO4", "0.4 g", "0.394089"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.098522",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_387,
        _base_note("MgCl2 x 6 H2O", "0.1 g", "0.098522"),
    ),
    Component(
        "Resazurin",
        "0.000493",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_387,
        _base_note("Resazurin", "0.5 mg", "0.000493"),
    ),
    Component(
        "MgSO4 x 7 H2O",
        "0.029557",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("MgSO4 x 7 H2O", "3.00 g/L", "0.029557"),
    ),
    Component(
        "NaCl",
        "0.009852",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_141,
        _trace_note("NaCl", "1.00 g/L", "0.009852"),
    ),
    Component(
        "Nitrilotriacetic acid",
        "0.014778",
        "G_PER_L",
        ("CHEBI:44557", "nitrilotriacetic acid"),
        SOURCE_141,
        _trace_note("Nitrilotriacetic acid", "1.50 g/L", "0.014778"),
    ),
    Component(
        "MnSO4 x H2O",
        "0.004926",
        "G_PER_L",
        ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
        SOURCE_141,
        _trace_note("MnSO4 x H2O", "0.50 g/L", "0.004926"),
    ),
    Component(
        "FeSO4 x 7 H2O",
        "0.000985",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("FeSO4 x 7 H2O", "0.10 g/L", "0.000985"),
    ),
    Component(
        "CoSO4 x 7 H2O",
        "0.001773",
        "G_PER_L",
        ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("CoSO4 x 7 H2O", "0.18 g/L", "0.001773"),
    ),
    Component(
        "ZnSO4 x 7 H2O",
        "0.001773",
        "G_PER_L",
        ("CHEBI:32312", "zinc sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("ZnSO4 x 7 H2O", "0.18 g/L", "0.001773"),
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
        "0.000197",
        "G_PER_L",
        ("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
        SOURCE_141,
        _trace_note("KAl(SO4)2 x 12 H2O", "0.02 g/L", "0.000197"),
    ),
    Component(
        "H3BO3",
        "0.000099",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_141,
        _trace_note("H3BO3", "0.01 g/L", "0.000099"),
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
        "NiCl2 x 6 H2O",
        "0.000296",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_141,
        _trace_note("NiCl2 x 6 H2O", "0.03 g/L", "0.000296"),
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "0.000002956",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_141,
        _trace_note("Na2SeO3 x 5 H2O", "0.30 mg/L", "0.000002956"),
    ),
    Component(
        "KOH",
        "variable",
        "VARIABLE",
        ("CHEBI:32035", "potassium hydroxide"),
        SOURCE_141,
        (
            f"{SOURCE_141} adjusts the trace element solution with KOH; "
            f"{SOURCE_387} adds 10 mL of that trace solution."
        ),
    ),
    Component(
        "NaHCO3",
        "0.985222",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_387,
        _stock_note("NaHCO3", "5% w/v", "20 mL", "0.985222"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.099507",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_387,
        (
            f"{SOURCE_387} adds 10 mL of 1% w/v CaCl2 x 2 H2O stock and "
            f"10 mL of {SOURCE_141} trace elements containing 0.10 g/L "
            "CaCl2 x 2 H2O, yielding 0.099507 g/L in the 1015 mL final "
            "formulation."
        ),
    ),
    Component(
        "Na-acetate",
        "3.251232",
        "G_PER_L",
        ("CHEBI:32954", "Na-acetate"),
        SOURCE_387,
        _stock_note("Na-acetate", "33% w/v", "10 mL", "3.251232"),
    ),
    Component(
        "Biotin",
        "0.000019704",
        "G_PER_L",
        ("CHEBI:15956", "Biotin"),
        SOURCE_141,
        _vitamin_note("Biotin", "2.00 mg/L", "0.000019704"),
    ),
    Component(
        "Folic acid",
        "0.000019704",
        "G_PER_L",
        ("CHEBI:27470", "Folic acid"),
        SOURCE_141,
        _vitamin_note("Folic acid", "2.00 mg/L", "0.000019704"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.000098522",
        "G_PER_L",
        ("CHEBI:30961", "Pyridoxine hydrochloride"),
        SOURCE_141,
        _vitamin_note("Pyridoxine-HCl", "10.00 mg/L", "0.000098522"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.000049261",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_141,
        _vitamin_note("Thiamine-HCl x 2 H2O", "5.00 mg/L", "0.000049261"),
    ),
    Component(
        "Riboflavin",
        "0.000049261",
        "G_PER_L",
        ("CHEBI:17015", "Riboflavin"),
        SOURCE_141,
        _vitamin_note("Riboflavin", "5.00 mg/L", "0.000049261"),
    ),
    Component(
        "Nicotinic acid",
        "0.000049261",
        "G_PER_L",
        ("CHEBI:15940", "Nicotinic acid"),
        SOURCE_141,
        _vitamin_note("Nicotinic acid", "5.00 mg/L", "0.000049261"),
    ),
    Component(
        "Calcium pantothenate",
        "0.000049261",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_141,
        _vitamin_note("D-Ca-pantothenate", "5.00 mg/L", "0.000049261"),
    ),
    Component(
        "Vitamin B12",
        "0.000000985",
        "G_PER_L",
        ("CHEBI:176843", "Vitamin B12"),
        SOURCE_141,
        _vitamin_note("Vitamin B12", "0.10 mg/L", "0.000000985"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.000049261",
        "G_PER_L",
        ("CHEBI:30753", "p-Aminobenzoic acid"),
        SOURCE_141,
        _vitamin_note("p-Aminobenzoic acid", "5.00 mg/L", "0.000049261"),
    ),
    Component(
        "(DL)-alpha-Lipoic acid",
        "0.000049261",
        "G_PER_L",
        ("CHEBI:16494", "(DL)-alpha-Lipoic acid"),
        SOURCE_141,
        _vitamin_note("Lipoic acid", "5.00 mg/L", "0.000049261"),
    ),
    Component(
        "Coenzyme M",
        "0.139901",
        "G_PER_L",
        ("CHEBI:17905", "coenzyme M"),
        SOURCE_387,
        _stock_note("Coenzyme M", "1.42% w/v", "10 mL", "0.139901"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.246305",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_387,
        _stock_note("Na2S x 9 H2O", "5% w/v", "5 mL", "0.246305"),
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_387,
        (
            f"{SOURCE_387} cools and dispenses the medium under an 80% N2 "
            "plus 20% CO2 atmosphere before adding extra CO2."
        ),
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_387,
        (
            f"{SOURCE_387} cools and dispenses the medium under 80:20 N2/CO2 "
            "and then adds CO2 by syringe to bring the gas atmosphere to 30% CO2."
        ),
    ),
    Component(
        "Distilled water",
        "940.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_387,
        f"{SOURCE_387} lists 940 mL distilled water before stock additions.",
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
        {"reference": KOMODO_387_URL},
        {"reference": DSMZ_387_URL},
        {"reference": DSMZ_141_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_387_URL,
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
    repaired["ph_value"] = 6.5
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
