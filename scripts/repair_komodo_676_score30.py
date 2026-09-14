#!/usr/bin/env python3
"""Repair empty KOMODO 676 mAB1-MEDIUM."""

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
TARGET = Path("bacterial/mab1_medium.yaml")
EXPECTED_ID = "CultureMech:006272"
EXPECTED_MEDIA_TERM = "komodo.medium:676"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_676_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=676"
)
DSMZ_676_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium676.pdf"
)
DSMZ_293_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium293.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)
DSMZ_141_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"
)
DSMZ_385_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf"
)

SOURCE_676 = "Archived DSMZ Medium 676"
SOURCE_293 = "Archived DSMZ Medium 293"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"
SOURCE_141 = "Archived DSMZ Medium 141 vitamin solution"
SOURCE_385 = "Archived DSMZ Medium 385 selenite/tungstate solution"

CURATOR = "repair_komodo_676_score30.py"
ACTION = "RESOLVED_KOMODO_676_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 676 defines mAB1-MEDIUM as DSMZ Medium 293 "
    "without Na2-succinate, with 3 g/L Na2SO4, additional NaHCO3 and "
    "Na2S x 9 H2O, 20 mL/L DSMZ Medium 141 vitamin solution, 1 mL/L "
    "DSMZ Medium 385 selenite/tungstate solution, yeast extract, sodium "
    "benzoate, and sodium dithionite; this record expands archived DSMZ "
    "Media 676, 293, 320, 141, and 385 into final per-liter components."
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
        f"{SOURCE_293} contributes {source_amount} {name} to the "
        f"1022 mL final formulation, yielding {value} g/L."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_293} adds 1 mL of the {SOURCE_320}; the SL-10 stock "
        f"contains {stock_amount} {name}, yielding {value} g/L in the "
        "1022 mL final formulation."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_676} adds 20 mL/L of the {SOURCE_141}; the vitamin stock "
        f"contains {stock_amount} {name}, yielding {value} g/L in the "
        "1022 mL final formulation."
    )


def _selenite_tungstate_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_676} adds 1 mL/L of the {SOURCE_385}; the stock contains "
        f"{stock_amount} {name}, yielding {value} g/L in the 1022 mL final "
        "formulation."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.195695",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_293,
        _base_note("KH2PO4", "0.20 g", "0.195695"),
    ),
    Component(
        "NH4Cl",
        "0.244618",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_293,
        _base_note("NH4Cl", "0.25 g", "0.244618"),
    ),
    Component(
        "NaCl",
        "19.569472",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_293,
        _base_note("NaCl", "20.00 g", "19.569472"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "2.935421",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_293,
        _base_note("MgCl2 x 6 H2O", "3.00 g", "2.935421"),
    ),
    Component(
        "KCl",
        "0.489237",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_293,
        _base_note("KCl", "0.50 g", "0.489237"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.146771",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_293,
        _base_note("CaCl2 x 2 H2O", "0.15 g", "0.146771"),
    ),
    Component(
        "HCl",
        "0.002446",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note("HCl", "2.50 g/L", "0.002446"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001468",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001468"),
    ),
    Component(
        "ZnCl2",
        "0.0000685",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note("ZnCl2", "0.070 g/L", "0.0000685"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000978",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000978"),
    ),
    Component(
        "H3BO3",
        "0.00000587",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note("H3BO3", "0.006 g/L", "0.00000587"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000186",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
        _trace_note("CoCl2 x 6 H2O", "0.190 g/L", "0.000186"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000196",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note("CuCl2 x 2 H2O", "0.002 g/L", "0.00000196"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000235",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
        _trace_note("NiCl2 x 6 H2O", "0.024 g/L", "0.0000235"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000352",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note("Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000352"),
    ),
    Component(
        "Resazurin",
        "0.000978",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_293,
        _base_note("Resazurin", "1.00 mg", "0.000978"),
    ),
    Component(
        "Na2SO4",
        "2.935421",
        "G_PER_L",
        ("CHEBI:32149", "sodium sulfate"),
        SOURCE_676,
        (
            f"{SOURCE_676} adds 3 g/L Na2SO4 to DSMZ Medium 293 without "
            "Na2-succinate, yielding 2.935421 g/L in the 1022 mL final "
            "formulation."
        ),
    ),
    Component(
        "NaHCO3",
        "4.892368",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_676,
        (
            f"{SOURCE_293} and {SOURCE_676} each contribute 2.5 g/L NaHCO3, "
            "yielding 4.892368 g/L in the 1022 mL final formulation."
        ),
    ),
    Component(
        "Biotin",
        "0.0000391",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_141,
        _vitamin_note("Biotin", "0.002 g/L", "0.0000391"),
    ),
    Component(
        "Folic acid",
        "0.0000391",
        "G_PER_L",
        ("CHEBI:27470", "folic acid"),
        SOURCE_141,
        _vitamin_note("Folic acid", "0.002 g/L", "0.0000391"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.000196",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_141,
        _vitamin_note("Pyridoxine-HCl", "0.010 g/L", "0.000196"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.0000978",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_141,
        _vitamin_note("Thiamine-HCl x 2 H2O", "0.005 g/L", "0.0000978"),
    ),
    Component(
        "Riboflavin",
        "0.0000978",
        "G_PER_L",
        ("CHEBI:17015", "riboflavin"),
        SOURCE_141,
        _vitamin_note("Riboflavin", "0.005 g/L", "0.0000978"),
    ),
    Component(
        "Nicotinic acid",
        "0.0000978",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_141,
        _vitamin_note("Nicotinic acid", "0.005 g/L", "0.0000978"),
    ),
    Component(
        "D-Ca-pantothenate",
        "0.0000978",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_141,
        _vitamin_note("D-Ca-pantothenate", "0.005 g/L", "0.0000978"),
    ),
    Component(
        "Vitamin B12",
        "0.00000196",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        SOURCE_141,
        _vitamin_note("Vitamin B12", "0.0001 g/L", "0.00000196"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.0000978",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_141,
        _vitamin_note("p-Aminobenzoic acid", "0.005 g/L", "0.0000978"),
    ),
    Component(
        "Lipoic acid",
        "0.0000978",
        "G_PER_L",
        ("CHEBI:16494", "lipoic acid"),
        SOURCE_141,
        _vitamin_note("Lipoic acid", "0.005 g/L", "0.0000978"),
    ),
    Component(
        "Yeast extract",
        "0.195695",
        "G_PER_L",
        ("CHEBI:86075", "yeast extract"),
        SOURCE_676,
        (
            f"{SOURCE_676} adds 0.2 g/L yeast extract, yielding "
            "0.195695 g/L in the 1022 mL final formulation."
        ),
    ),
    Component(
        "NaOH",
        "0.000489",
        "G_PER_L",
        ("CHEBI:32145", "sodium hydroxide"),
        SOURCE_385,
        _selenite_tungstate_note("NaOH", "0.500 g/L", "0.000489"),
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "0.00000294",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_385,
        _selenite_tungstate_note("Na2SeO3 x 5 H2O", "0.003 g/L", "0.00000294"),
    ),
    Component(
        "Na2WO4 x 2 H2O",
        "0.00000391",
        "G_PER_L",
        ("CHEBI:63939", "sodium tungstate dihydrate"),
        SOURCE_385,
        _selenite_tungstate_note("Na2WO4 x 2 H2O", "0.004 g/L", "0.00000391"),
    ),
    Component(
        "sodium benzoate",
        "0.146771",
        "G_PER_L",
        ("CHEBI:113455", "sodium benzoate"),
        SOURCE_676,
        (
            f"{SOURCE_676} adds 0.15 g/L sodium benzoate, yielding "
            "0.146771 g/L in the 1022 mL final formulation."
        ),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.645793",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_676,
        (
            f"{SOURCE_293} contributes 0.36 g/L Na2S x 9 H2O and "
            f"{SOURCE_676} adds 0.3 g/L, yielding 0.645793 g/L in the "
            "1022 mL final formulation."
        ),
    ),
    Component(
        "sodium dithionite",
        "0.009785",
        "G_PER_L",
        ("CHEBI:66870", "sodium dithionite"),
        SOURCE_676,
        (
            f"{SOURCE_676} lists 10.0-25.0 mg/L sodium dithionite; the "
            "KOMODO record uses the lower endpoint, yielding 0.009785 g/L "
            "in the 1022 mL final formulation."
        ),
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
            f"{SOURCE_293} lists 1000 mL distilled water before the SL-10 "
            f"trace solution; {SOURCE_676} omits the succinate substrate "
            "and adds vitamin and selenite/tungstate stocks."
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
        {"reference": KOMODO_676_URL},
        {"reference": DSMZ_676_URL},
        {"reference": DSMZ_293_URL},
        {"reference": DSMZ_320_URL},
        {"reference": DSMZ_141_URL},
        {"reference": DSMZ_385_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_676_URL,
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
    return {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
        "term": _term(*component.term),
        "mediaingredientmech_chebi_term": _term(*component.term),
    }


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(
            f"{TARGET}: expected immutable id {EXPECTED_ID}, " f"found {doc.get('id')!r}"
        )
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
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
