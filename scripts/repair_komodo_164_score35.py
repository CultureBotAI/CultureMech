#!/usr/bin/env python3
"""Repair empty KOMODO 164 Methanosarcina thermophilic medium records."""

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
BASE_TARGET = "archaea/methanosarcina_thermophilic_medium.yaml"
REPLACEMENT_TARGET = (
    "archaea/"
    "methanosarcina_thermophilic_medium_replace_rumen_fluid_clarified_with_"
    "sludge_fluid_medium_119.yaml"
)
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

DSMZ_164_URL = (
    "https://web.archive.org/web/20121030075644id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium164.pdf"
)
DSMZ_120_URL = (
    "https://web.archive.org/web/20121030062128id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf"
)
DSMZ_141_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)
DSMZ_119_URL = (
    "https://web.archive.org/web/20121030071037id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf"
)

SOURCE_164 = "Archived DSMZ Medium 164"
SOURCE_120 = "Archived DSMZ Medium 120"
SOURCE_141 = "Archived DSMZ Medium 141"
SOURCE_320 = "Archived DSMZ Medium 320"

CURATOR = "repair_komodo_164_score35.py"
TIMESTAMP = "2026-09-10T00:00:00-07:00"


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str | None
    unit: str | None
    term: tuple[str, str] | None
    source: str


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_media_term: str
    source_name: str
    action: str
    change_note: str
    notes: str
    components: tuple[Component, ...]


COMMON_COMPONENTS: tuple[Component, ...] = (
    Component(
        "K2HPO4", "0.348", "G_PER_L", ("CHEBI:131527", "dipotassium hydrogen phosphate"), SOURCE_120
    ),
    Component(
        "KH2PO4", "0.227", "G_PER_L", ("CHEBI:63036", "potassium dihydrogen phosphate"), SOURCE_120
    ),
    Component("NH4Cl", "0.500", "G_PER_L", ("CHEBI:31206", "ammonium chloride"), SOURCE_120),
    Component(
        "MgSO4 x 7 H2O",
        "0.500",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_120,
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.250",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_120,
    ),
    Component("NaCl", "2.250", "G_PER_L", ("CHEBI:26710", "sodium chloride"), SOURCE_120),
    Component(
        "FeSO4 x 7 H2O",
        "0.002",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_120,
    ),
    Component("Biotin", "0.00002", "G_PER_L", ("CHEBI:15956", "biotin"), SOURCE_141),
    Component("Folic acid", "0.00002", "G_PER_L", ("CHEBI:27470", "folic acid"), SOURCE_141),
    Component(
        "Pyridoxine-HCl",
        "0.0001",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_141,
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.00005",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_141,
    ),
    Component("Riboflavin", "0.00005", "G_PER_L", ("CHEBI:17015", "riboflavin"), SOURCE_141),
    Component(
        "Nicotinic acid",
        "0.00005",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_141,
    ),
    Component(
        "D-Ca-pantothenate",
        "0.00005",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_141,
    ),
    Component("Vitamin B12", "0.000001", "G_PER_L", ("CHEBI:176843", "vitamin B12"), SOURCE_141),
    Component(
        "p-Aminobenzoic acid",
        "0.00005",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_141,
    ),
    Component("Lipoic acid", "0.00005", "G_PER_L", ("CHEBI:16494", "lipoic acid"), SOURCE_141),
    Component("HCl", "0.0025", "G_PER_L", ("CHEBI:17883", "hydrogen chloride"), SOURCE_320),
    Component(
        "FeCl2 x 4 H2O",
        "0.0015",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
    ),
    Component("ZnCl2", "0.00007", "G_PER_L", ("CHEBI:49976", "zinc dichloride"), SOURCE_320),
    Component(
        "MnCl2 x 4 H2O",
        "0.0001",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
    ),
    Component("H3BO3", "0.000006", "G_PER_L", ("CHEBI:33118", "boric acid"), SOURCE_320),
    Component(
        "CoCl2 x 6 H2O",
        "0.00019",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.000002",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.000024",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.000036",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
    ),
    Component(
        "Yeast extract", "2.000", "G_PER_L", ("FOODON:03315426", "yeast extract"), SOURCE_120
    ),
    Component("Casitone", "2.000", "G_PER_L", None, SOURCE_120),
    Component("Resazurin", "0.001", "G_PER_L", ("CHEBI:8806", "Resazurin"), SOURCE_120),
    Component(
        "NaHCO3", "2.000", "G_PER_L", ("CHEBI:32139", "sodium hydrogencarbonate"), SOURCE_164
    ),
    Component("Methanol", "10.000", "ML_PER_L", ("CHEBI:17790", "methanol"), SOURCE_120),
    Component(
        "Cysteine-HCl x H2O",
        "0.300",
        "G_PER_L",
        ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
        SOURCE_120,
    ),
    Component(
        "Na2S x 9 H2O",
        "0.300",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_120,
    ),
    Component("Distilled water", "1000.000", "ML_PER_L", ("CHEBI:15377", "water"), SOURCE_120),
)

TARGETS: tuple[Target, ...] = (
    Target(
        path=BASE_TARGET,
        expected_id="CultureMech:004191",
        expected_media_term="komodo.medium:164",
        source_name="DSMZ/KOMODO Medium 164",
        action="RESOLVED_KOMODO_164_SCORE35",
        change_note="Replaced empty KOMODO 164 composition with archived DSMZ data",
        notes=(
            "Archived DSMZ Medium 164 defines METHANOSARCINA (thermophilic) "
            "MEDIUM as DSMZ Medium 120 supplemented with 5% (v/v) clarified "
            "rumen fluid or sludge fluid from DSMZ Medium 119 and with NaHCO3 "
            "increased to 2 g/L; this KOMODO base record uses clarified rumen "
            "fluid."
        ),
        components=(
            *COMMON_COMPONENTS,
            Component("Rumen fluid, clarified", "50.000", "ML_PER_L", None, SOURCE_164),
        ),
    ),
    Target(
        path=REPLACEMENT_TARGET,
        expected_id="CultureMech:004190",
        expected_media_term=(
            "komodo.medium:164_replace_Rumen fluid, clarified_with_Sludge " "fluid (medium 119)"
        ),
        source_name="DSMZ/KOMODO Medium 164 sludge variant",
        action="RESOLVED_KOMODO_164_SLUDGE_SCORE35",
        change_note=(
            "Replaced empty KOMODO 164 sludge-fluid replacement composition "
            "with archived DSMZ data"
        ),
        notes=(
            "Archived DSMZ Medium 164 defines METHANOSARCINA (thermophilic) "
            "MEDIUM as DSMZ Medium 120 supplemented with 5% (v/v) clarified "
            "rumen fluid or sludge fluid from DSMZ Medium 119 and with NaHCO3 "
            "increased to 2 g/L; this KOMODO replacement record uses sludge "
            "fluid from DSMZ Medium 119."
        ),
        components=(
            *COMMON_COMPONENTS,
            Component("Sludge fluid (medium 119)", "50.000", "ML_PER_L", None, SOURCE_164),
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
        raise ValueError(f"{target.path}: missing expected media term {target.expected_media_term}")


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
    for flag in ("has_ontology_mappings", "ingredients_curated", "has_unmapped_ingredients"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (DSMZ_164_URL, DSMZ_120_URL, DSMZ_141_URL, DSMZ_320_URL, DSMZ_119_URL):
        if url not in found:
            references.append({"reference": url})


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": target.action,
        "changes": target.change_note,
        "source": DSMZ_164_URL,
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


def _source_note(target: Target, component: Component) -> str:
    if component.source == SOURCE_164:
        return (
            f"{target.source_name} applies {component.value} {component.unit} "
            f"{component.preferred_term}."
        )
    if component.source == SOURCE_141:
        return (
            f"{target.source_name} adds 10 mL/L of the {SOURCE_141} vitamin stock, "
            f"yielding {component.value} g/L {component.preferred_term}."
        )
    if component.source == SOURCE_320:
        return (
            f"{target.source_name} adds 1 mL/L of the {SOURCE_320} SL-10 stock, "
            f"yielding {component.value} g/L {component.preferred_term}."
        )
    return (
        f"{target.source_name} derives {component.value} {component.unit} "
        f"{component.preferred_term} from {component.source}."
    )


def _ingredient(component: Component, target: Target) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": _source_note(target, component),
    }
    if component.value is not None and component.unit is not None:
        row["concentration"] = {"value": component.value, "unit": component.unit}
    if component.term is not None:
        row["term"] = _term(*component.term)
        if component.term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*component.term)
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
    repaired["ingredients"] = [_ingredient(component, target) for component in target.components]
    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
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
