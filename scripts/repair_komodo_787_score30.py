#!/usr/bin/env python3
"""Repair empty KOMODO 787 ACETOBACTERIUM DEHALOGENANS medium."""

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
TARGET = Path("bacterial/KOMODO_787_ACETOBACTERIUM_DEHALOGENANS_medium.yaml")
EXPECTED_ID = "CultureMech:006488"
EXPECTED_MEDIA_TERM = "komodo.medium:787"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_787_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=787"
)
DSMZ_787_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium787.pdf"
)
DSMZ_135_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135.pdf"
)

SOURCE_787 = "Archived DSMZ Medium 787"
SOURCE_135 = "Archived DSMZ Medium 135"
SOURCE_141 = "Archived DSMZ Medium 141"

CURATOR = "repair_komodo_787_score30.py"
ACTION = "RESOLVED_KOMODO_787_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 787 defines ACETOBACTERIUM DEHALOGENANS MEDIUM "
    "as DSMZ Medium 135 prepared without fructose, sodium sulfide, or "
    "bicarbonate in 900 mL water under 80:20 N2/CO2, with NaHCO3, "
    "Cysteine-HCl x H2O, and Na-syringate added to each 9 mL aliquot from "
    "sterile anaerobic stocks; this record expands the Medium 135 trace and "
    "vitamin stocks into final per-liter components after the 10.32 mL final "
    "aliquot volume."
)


def _base_note(name: str, amount: str, value: str) -> str:
    return (
        f"{SOURCE_787} uses {SOURCE_135} without fructose, bicarbonate, or "
        f"sulfide and lists {amount} {name}; after 9 mL base medium receives "
        f"1.32 mL of stock additions this yields {value} g/L."
    )


def _combined_note(name: str, base: str, stock: str, value: str) -> str:
    return (
        f"{SOURCE_787} uses {SOURCE_135} containing {base} {name} plus 20 mL "
        f"of {SOURCE_141} trace elements containing {stock} {name}; after "
        f"9 mL base medium receives 1.32 mL of stock additions this yields "
        f"{value} g/L."
    )


def _trace_note(name: str, stock: str, value: str) -> str:
    return (
        f"{SOURCE_787} uses 20 mL of {SOURCE_141} trace elements per "
        f"{SOURCE_135}; the trace stock contains {stock} {name}, yielding "
        f"{value} g/L after the DSMZ 787 stock additions."
    )


def _vitamin_note(name: str, stock: str, value: str) -> str:
    return (
        f"{SOURCE_787} uses 20 mL of {SOURCE_141} vitamin solution per "
        f"{SOURCE_135}; the vitamin stock contains {stock} {name}, yielding "
        f"{value} g/L after the DSMZ 787 stock additions."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "NH4Cl",
        "0.927759",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_135,
        _base_note("NH4Cl", "1.00 g", "0.927759"),
    ),
    Component(
        "KH2PO4",
        "0.306160",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_135,
        _base_note("KH2PO4", "0.33 g", "0.306160"),
    ),
    Component(
        "K2HPO4",
        "0.417491",
        "G_PER_L",
        ("CHEBI:131527", "dipotassium hydrogen phosphate"),
        SOURCE_135,
        _base_note("K2HPO4", "0.45 g", "0.417491"),
    ),
    Component(
        "MgSO4 x 7 H2O",
        "0.145101",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_135,
        _combined_note("MgSO4 x 7 H2O", "0.10 g", "3.00 g/L", "0.145101"),
    ),
    Component(
        "Yeast extract",
        "1.855517",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_135,
        _base_note("Yeast extract", "2.00 g", "1.855517"),
    ),
    Component(
        "Resazurin",
        "0.000928",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_135,
        _base_note("Resazurin", "1.00 mg", "0.000928"),
    ),
    Component(
        "Nitrilotriacetic acid",
        "0.026163",
        "G_PER_L",
        ("CHEBI:44557", "nitrilotriacetic acid"),
        SOURCE_141,
        _trace_note("Nitrilotriacetic acid", "1.50 g/L", "0.026163"),
    ),
    Component(
        "MnSO4 x H2O",
        "0.008721",
        "G_PER_L",
        ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
        SOURCE_141,
        _trace_note("MnSO4 x H2O", "0.50 g/L", "0.008721"),
    ),
    Component(
        "NaCl",
        "0.017442",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_141,
        _trace_note("NaCl", "1.00 g/L", "0.017442"),
    ),
    Component(
        "FeSO4 x 7 H2O",
        "0.001744",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("FeSO4 x 7 H2O", "0.10 g/L", "0.001744"),
    ),
    Component(
        "CoSO4 x 7 H2O",
        "0.003140",
        "G_PER_L",
        ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("CoSO4 x 7 H2O", "0.18 g/L", "0.003140"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.001744",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_141,
        _trace_note("CaCl2 x 2 H2O", "0.10 g/L", "0.001744"),
    ),
    Component(
        "ZnSO4 x 7 H2O",
        "0.003140",
        "G_PER_L",
        ("CHEBI:32312", "zinc sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("ZnSO4 x 7 H2O", "0.18 g/L", "0.003140"),
    ),
    Component(
        "CuSO4 x 5 H2O",
        "0.000174",
        "G_PER_L",
        ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
        SOURCE_141,
        _trace_note("CuSO4 x 5 H2O", "0.01 g/L", "0.000174"),
    ),
    Component(
        "KAl(SO4)2 x 12 H2O",
        "0.000349",
        "G_PER_L",
        ("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
        SOURCE_141,
        _trace_note("KAl(SO4)2 x 12 H2O", "0.02 g/L", "0.000349"),
    ),
    Component(
        "H3BO3",
        "0.000174",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_141,
        _trace_note("H3BO3", "0.01 g/L", "0.000174"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.000174",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_141,
        _trace_note("Na2MoO4 x 2 H2O", "0.01 g/L", "0.000174"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.000523",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_141,
        _trace_note("NiCl2 x 6 H2O", "0.03 g/L", "0.000523"),
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "0.000005233",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_141,
        _trace_note("Na2SeO3 x 5 H2O", "0.30 mg/L", "0.000005233"),
    ),
    Component(
        "KOH",
        "variable",
        "VARIABLE",
        ("CHEBI:32035", "potassium hydroxide"),
        SOURCE_141,
        (
            f"{SOURCE_141} adjusts the trace element solution with KOH; "
            f"{SOURCE_787} uses 20 mL of that trace solution via Medium 135."
        ),
    ),
    Component(
        "Biotin",
        "0.000034884",
        "G_PER_L",
        ("CHEBI:15956", "Biotin"),
        SOURCE_141,
        _vitamin_note("Biotin", "2.00 mg/L", "0.000034884"),
    ),
    Component(
        "Folic acid",
        "0.000034884",
        "G_PER_L",
        ("CHEBI:27470", "Folic acid"),
        SOURCE_141,
        _vitamin_note("Folic acid", "2.00 mg/L", "0.000034884"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.000174419",
        "G_PER_L",
        ("CHEBI:30961", "Pyridoxine hydrochloride"),
        SOURCE_141,
        _vitamin_note("Pyridoxine-HCl", "10.00 mg/L", "0.000174419"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.000087209",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_141,
        _vitamin_note("Thiamine-HCl x 2 H2O", "5.00 mg/L", "0.000087209"),
    ),
    Component(
        "Riboflavin",
        "0.000087209",
        "G_PER_L",
        ("CHEBI:17015", "Riboflavin"),
        SOURCE_141,
        _vitamin_note("Riboflavin", "5.00 mg/L", "0.000087209"),
    ),
    Component(
        "Nicotinic acid",
        "0.000087209",
        "G_PER_L",
        ("CHEBI:15940", "Nicotinic acid"),
        SOURCE_141,
        _vitamin_note("Nicotinic acid", "5.00 mg/L", "0.000087209"),
    ),
    Component(
        "Calcium pantothenate",
        "0.000087209",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_141,
        _vitamin_note("D-Ca-pantothenate", "5.00 mg/L", "0.000087209"),
    ),
    Component(
        "Vitamin B12",
        "0.000001744",
        "G_PER_L",
        ("CHEBI:176843", "Vitamin B12"),
        SOURCE_141,
        _vitamin_note("Vitamin B12", "0.10 mg/L", "0.000001744"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.000087209",
        "G_PER_L",
        ("CHEBI:30753", "p-Aminobenzoic acid"),
        SOURCE_141,
        _vitamin_note("p-Aminobenzoic acid", "5.00 mg/L", "0.000087209"),
    ),
    Component(
        "(DL)-alpha-Lipoic acid",
        "0.000087209",
        "G_PER_L",
        ("CHEBI:16494", "(DL)-alpha-Lipoic acid"),
        SOURCE_141,
        _vitamin_note("Lipoic acid", "5.00 mg/L", "0.000087209"),
    ),
    Component(
        "NaHCO3",
        "9.689922",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_787,
        f"{SOURCE_787} adds 1.00 mL of 10% w/v NaHCO3 stock per 9 mL base medium.",
    ),
    Component(
        "Cysteine-HCl x H2O",
        "0.494186",
        "G_PER_L",
        ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
        SOURCE_787,
        (
            f"{SOURCE_787} adds 0.17 mL of 3% w/v Cysteine-HCl x H2O stock "
            "per 9 mL base medium."
        ),
    ),
    Component(
        "Na-syringate",
        "0.872093",
        "G_PER_L",
        ("CHEBI:132110", "sodium syringate"),
        SOURCE_787,
        f"{SOURCE_787} adds 0.15 mL of 6% w/v Na-syringate stock per 9 mL base medium.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_787,
        f"{SOURCE_787} prepares the base medium under 80% N2 plus 20% CO2.",
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_787,
        f"{SOURCE_787} prepares the base medium under 80% N2 plus 20% CO2.",
    ),
    Component(
        "Distilled water",
        "900.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_787,
        f"{SOURCE_787} dissolves the modified Medium 135 ingredients in 900 mL water.",
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
        {"reference": KOMODO_787_URL},
        {"reference": DSMZ_787_URL},
        {"reference": DSMZ_135_URL},
        {"reference": DSMZ_141_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_787_URL,
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
    repaired["ph_value"] = 7.4
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
