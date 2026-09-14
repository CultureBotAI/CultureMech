#!/usr/bin/env python3
"""Repair empty KOMODO 349 ACETOBACTERIUM 2 medium."""

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
TARGET = "bacterial/acetobacterium_2_medium.yaml"
EXPECTED_ID = "CultureMech:005062"
EXPECTED_MEDIA_TERM = "komodo.medium:349"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_349_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=349"
)
DSMZ_349_URL = (
    "https://web.archive.org/web/20121030084419id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium349.pdf"
)
DSMZ_135_URL = (
    "https://web.archive.org/web/20121030072436id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135.pdf"
)
DSMZ_141_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"
)

SOURCE_349 = "Archived DSMZ Medium 349"
SOURCE_135 = "Archived DSMZ Medium 135"
SOURCE_141_TRACE = "Archived DSMZ Medium 141 trace element solution"
SOURCE_141_VITAMINS = "Archived DSMZ Medium 141 vitamin solution"
SOURCE_DSMZ_KOMODO = "Archived DSMZ 349 and KOMODO MediaInfo 349"

CURATOR = "repair_komodo_349_score35.py"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 349 defines ACETOBACTERIUM 2 MEDIUM as DSMZ Medium "
    "135 supplemented with 20 g/L NaCl and with 1.25 g/L ethylene glycol "
    "replacing fructose; this record expands the archived DSMZ Medium 135 base "
    "and Medium 141 trace and vitamin stocks into final per-liter components."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


def _source_note(name: str, value: str, source: str) -> str:
    if source == SOURCE_135:
        return (
            f"{SOURCE_135} contributes {value} g/L {name} after scaling "
            "the 1040 mL final formulation to one liter."
        )
    if source == SOURCE_141_TRACE:
        return (
            f"{SOURCE_135} adds 20 mL of the {SOURCE_141_TRACE} per "
            f"1040 mL final formulation, yielding {value} g/L {name}."
        )
    if source == SOURCE_141_VITAMINS:
        return (
            f"{SOURCE_135} adds 20 mL of the {SOURCE_141_VITAMINS} per "
            f"1040 mL final formulation, yielding {value} g/L {name}."
        )
    raise ValueError(f"unexpected derived source {source!r}")


COMPONENTS: tuple[Component, ...] = (
    Component(
        "NH4Cl",
        "0.961538",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_135,
        _source_note("NH4Cl", "0.961538", SOURCE_135),
    ),
    Component(
        "KH2PO4",
        "0.317308",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_135,
        _source_note("KH2PO4", "0.317308", SOURCE_135),
    ),
    Component(
        "K2HPO4",
        "0.432692",
        "G_PER_L",
        ("CHEBI:131527", "dipotassium hydrogen phosphate"),
        SOURCE_135,
        _source_note("K2HPO4", "0.432692", SOURCE_135),
    ),
    Component(
        "MgSO4 x 7 H2O",
        "0.153846",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_DSMZ_KOMODO,
        (
            "Archived DSMZ Medium 349 inherits 0.10 g MgSO4 x 7 H2O from "
            "Medium 135 and 20 mL of a 3.00 g/L Medium 141 trace stock per "
            "1040 mL final formulation, yielding 0.153846 g/L total."
        ),
    ),
    Component(
        "Nitrilotriacetic acid",
        "0.028846",
        "G_PER_L",
        ("CHEBI:44557", "nitrilotriacetic acid"),
        SOURCE_141_TRACE,
        _source_note("Nitrilotriacetic acid", "0.028846", SOURCE_141_TRACE),
    ),
    Component(
        "MnSO4 x H2O",
        "0.009615",
        "G_PER_L",
        ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
        SOURCE_141_TRACE,
        _source_note("MnSO4 x H2O", "0.009615", SOURCE_141_TRACE),
    ),
    Component(
        "NaCl",
        "20.019231",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_DSMZ_KOMODO,
        (
            "Archived DSMZ Medium 349 adds 20 g/L NaCl and Archived DSMZ "
            "Medium 135 adds 20 mL of a 1.00 g/L Medium 141 trace stock per "
            "1040 mL final formulation, yielding 20.019231 g/L total."
        ),
    ),
    Component(
        "FeSO4 x 7 H2O",
        "0.001923",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_141_TRACE,
        _source_note("FeSO4 x 7 H2O", "0.001923", SOURCE_141_TRACE),
    ),
    Component(
        "CoSO4 x 7 H2O",
        "0.003462",
        "G_PER_L",
        ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
        SOURCE_141_TRACE,
        _source_note("CoSO4 x 7 H2O", "0.003462", SOURCE_141_TRACE),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.001923",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_141_TRACE,
        _source_note("CaCl2 x 2 H2O", "0.001923", SOURCE_141_TRACE),
    ),
    Component(
        "ZnSO4 x 7 H2O",
        "0.003462",
        "G_PER_L",
        ("CHEBI:32312", "zinc sulfate heptahydrate"),
        SOURCE_141_TRACE,
        _source_note("ZnSO4 x 7 H2O", "0.003462", SOURCE_141_TRACE),
    ),
    Component(
        "CuSO4 x 5 H2O",
        "0.000192",
        "G_PER_L",
        ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
        SOURCE_141_TRACE,
        _source_note("CuSO4 x 5 H2O", "0.000192", SOURCE_141_TRACE),
    ),
    Component(
        "KAl(SO4)2 x 12 H2O",
        "0.000385",
        "G_PER_L",
        ("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
        SOURCE_141_TRACE,
        _source_note("KAl(SO4)2 x 12 H2O", "0.000385", SOURCE_141_TRACE),
    ),
    Component(
        "H3BO3",
        "0.000192",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_141_TRACE,
        _source_note("H3BO3", "0.000192", SOURCE_141_TRACE),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.000192",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_141_TRACE,
        _source_note("Na2MoO4 x 2 H2O", "0.000192", SOURCE_141_TRACE),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.000577",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_141_TRACE,
        _source_note("NiCl2 x 6 H2O", "0.000577", SOURCE_141_TRACE),
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "0.00000577",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_141_TRACE,
        _source_note("Na2SeO3 x 5 H2O", "0.00000577", SOURCE_141_TRACE),
    ),
    Component(
        "Biotin",
        "0.000038",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_141_VITAMINS,
        _source_note("Biotin", "0.000038", SOURCE_141_VITAMINS),
    ),
    Component(
        "Folic acid",
        "0.000038",
        "G_PER_L",
        ("CHEBI:27470", "folic acid"),
        SOURCE_141_VITAMINS,
        _source_note("Folic acid", "0.000038", SOURCE_141_VITAMINS),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.000192",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_141_VITAMINS,
        _source_note("Pyridoxine-HCl", "0.000192", SOURCE_141_VITAMINS),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.000096",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_141_VITAMINS,
        _source_note("Thiamine-HCl x 2 H2O", "0.000096", SOURCE_141_VITAMINS),
    ),
    Component(
        "Riboflavin",
        "0.000096",
        "G_PER_L",
        ("CHEBI:17015", "riboflavin"),
        SOURCE_141_VITAMINS,
        _source_note("Riboflavin", "0.000096", SOURCE_141_VITAMINS),
    ),
    Component(
        "Nicotinic acid",
        "0.000096",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_141_VITAMINS,
        _source_note("Nicotinic acid", "0.000096", SOURCE_141_VITAMINS),
    ),
    Component(
        "D-Ca-pantothenate",
        "0.000096",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_141_VITAMINS,
        _source_note("D-Ca-pantothenate", "0.000096", SOURCE_141_VITAMINS),
    ),
    Component(
        "Vitamin B12",
        "0.00000192",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        SOURCE_141_VITAMINS,
        _source_note("Vitamin B12", "0.00000192", SOURCE_141_VITAMINS),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.000096",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_141_VITAMINS,
        _source_note("p-Aminobenzoic acid", "0.000096", SOURCE_141_VITAMINS),
    ),
    Component(
        "Lipoic acid",
        "0.000096",
        "G_PER_L",
        ("CHEBI:16494", "lipoic acid"),
        SOURCE_141_VITAMINS,
        _source_note("Lipoic acid", "0.000096", SOURCE_141_VITAMINS),
    ),
    Component(
        "Yeast extract",
        "1.923077",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_135,
        _source_note("Yeast extract", "1.923077", SOURCE_135),
    ),
    Component(
        "Resazurin",
        "0.000962",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_135,
        _source_note("Resazurin", "0.000962", SOURCE_135),
    ),
    Component(
        "NaHCO3",
        "9.615385",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_135,
        _source_note("NaHCO3", "9.615385", SOURCE_135),
    ),
    Component(
        "Ethylene glycol",
        "1.250000",
        "G_PER_L",
        ("CHEBI:30742", "ethylene glycol"),
        SOURCE_349,
        "Archived DSMZ Medium 349 replaces fructose with 1.25 g/L ethylene glycol.",
    ),
    Component(
        "Cysteine-HCl x H2O",
        "0.480769",
        "G_PER_L",
        ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
        SOURCE_135,
        _source_note("Cysteine-HCl x H2O", "0.480769", SOURCE_135),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.480769",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_135,
        _source_note("Na2S x 9 H2O", "0.480769", SOURCE_135),
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_135,
        "Archived DSMZ Medium 135 lists 1000 mL distilled water.",
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
        raise ValueError("data_quality_flags is not a list")

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
        raise ValueError("references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (KOMODO_349_URL, DSMZ_349_URL, DSMZ_135_URL, DSMZ_141_URL):
        if url not in found:
            references.append({"reference": url})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": "RESOLVED_KOMODO_349_SCORE35",
        "changes": "Replaced empty KOMODO 349 composition with archived DSMZ data",
        "source": DSMZ_349_URL,
        "notes": NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == event["action"]
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
        raise ValueError(
            f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}"
        )
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
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
