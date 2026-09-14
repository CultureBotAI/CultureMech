#!/usr/bin/env python3
"""Repair two one-component KOMODO acidophile media."""

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

KOMODO_184_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=184"
)
KOMODO_723_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=723"
)
DSMZ_184_PDF = "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium184.pdf"
DSMZ_723_PDF = "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium723.pdf"

CURATOR = "repair_komodo_184_723_score15.py"
ACTION = "RESOLVED_KOMODO_184_723_SCORE15"
TIMESTAMP = "2026-09-10T00:00:00-07:00"


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    media_term_id: str
    source_label: str
    source_url: str
    dsmz_pdf: str
    ingredients: tuple[dict[str, Any], ...]
    accepted_signatures: tuple[tuple[str, ...], ...]
    notes: str


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    *,
    source: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "source": source,
        "notes": f"{source} lists {value} g/L {preferred_term}.",
        "concentration": {"value": value, "unit": "G_PER_L"},
    }
    if term is not None:
        row["term"] = _term(*term)
        row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _variable(
    preferred_term: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "source": source,
        "notes": notes,
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


def _desulfurococcus_recipe() -> tuple[dict[str, Any], ...]:
    source = "KOMODO Medium 184"
    return (
        _ingredient("Sulfur", "5.00", source=source, term=("CHEBI:26833", "sulfur atom")),
        _ingredient(
            "KH2PO4",
            "0.28",
            source=source,
            term=("CHEBI:63036", "potassium dihydrogen phosphate"),
        ),
        _ingredient(
            "VOSO4 x 2 H2O",
            "0.000030",
            source=source,
            term=("CHEBI:87009", "vanadyl sulfate dihydrate"),
        ),
        _ingredient("Yeast extract (Difco)", "1.00", source=source),
        _ingredient(
            "CaCl2 x 2 H2O",
            "0.07",
            source=source,
            term=("CHEBI:86158", "calcium chloride dihydrate"),
        ),
        _ingredient(
            "Na2S x 9 H2O",
            "0.50",
            source=source,
            term=("CHEBI:76209", "sodium sulfide nonahydrate"),
        ),
        _ingredient("Yeast extract", "1.00", source=source),
        _ingredient(
            "MnCl2 x 4 H2O",
            "0.00180",
            source=source,
            term=("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        ),
        _ingredient(
            "CuCl2 x 2 H2O",
            "0.000050",
            source=source,
            term=("CHEBI:86318", "copper(II) chloride dihydrate"),
        ),
        _ingredient(
            "(NH4)2SO4",
            "1.30",
            source=source,
            term=("CHEBI:62946", "ammonium sulfate"),
        ),
        _variable(
            "N2",
            source=source,
            notes=f"{source} lists nitrogen without gram or molar amounts.",
            term=("CHEBI:17997", "dinitrogen"),
        ),
        _ingredient(
            "Na2MoO4 x 2 H2O",
            "0.000030",
            source=source,
            term=("CHEBI:75213", "sodium molybdate dihydrate"),
        ),
        _ingredient(
            "FeCl3 x 6 H2O",
            "0.02",
            source=source,
            term=("CHEBI:86254", "iron trichloride hexahydrate"),
        ),
        _ingredient(
            "MgSO4 x 7 H2O",
            "0.25",
            source=source,
            term=("CHEBI:31795", "magnesium sulfate heptahydrate"),
        ),
        _variable(
            "H2O",
            source=source,
            notes=f"{source} lists water without gram or molar amounts.",
            term=("CHEBI:15377", "water"),
        ),
        _ingredient(
            "ZnSO4 x 7 H2O",
            "0.000220",
            source=source,
            term=("CHEBI:32312", "zinc sulfate heptahydrate"),
        ),
        _ingredient("Resazurin", "0.00100", source=source, term=("CHEBI:8806", "Resazurin")),
        _ingredient(
            "Na2B4O7 x 10 H2O",
            "0.00450",
            source=source,
            term=("CHEBI:131366", "disodium tetraborate decahydrate"),
        ),
        _ingredient(
            "CoSO4",
            "0.000010",
            source=source,
            term=("CHEBI:53470", "cobalt(II) sulfate"),
        ),
        _variable(
            "H2SO4",
            source=source,
            notes=f"{source} lists H2SO4 as the variable pH 5.5 acid.",
            term=("CHEBI:26836", "sulfuric acid"),
        ),
    )


def _picrophilus_recipe() -> tuple[dict[str, Any], ...]:
    source = "KOMODO Medium 723"
    return (
        _ingredient(
            "KH2PO4",
            "0.28",
            source=source,
            term=("CHEBI:63036", "potassium dihydrogen phosphate"),
        ),
        _ingredient(
            "VOSO4 x 2 H2O",
            "0.000030",
            source=source,
            term=("CHEBI:87009", "vanadyl sulfate dihydrate"),
        ),
        _ingredient(
            "CaCl2 x 2 H2O",
            "0.07",
            source=source,
            term=("CHEBI:86158", "calcium chloride dihydrate"),
        ),
        _ingredient("Yeast extract", "3.00", source=source),
        _ingredient(
            "MnCl2 x 4 H2O",
            "0.00180",
            source=source,
            term=("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        ),
        _ingredient(
            "CuCl2 x 2 H2O",
            "0.000050",
            source=source,
            term=("CHEBI:86318", "copper(II) chloride dihydrate"),
        ),
        _ingredient(
            "(NH4)2SO4",
            "1.30",
            source=source,
            term=("CHEBI:62946", "ammonium sulfate"),
        ),
        _ingredient(
            "Na2MoO4 x 2 H2O",
            "0.000030",
            source=source,
            term=("CHEBI:75213", "sodium molybdate dihydrate"),
        ),
        _ingredient(
            "FeCl3 x 6 H2O",
            "0.02",
            source=source,
            term=("CHEBI:86254", "iron trichloride hexahydrate"),
        ),
        _ingredient(
            "MgSO4 x 7 H2O",
            "0.25",
            source=source,
            term=("CHEBI:31795", "magnesium sulfate heptahydrate"),
        ),
        _ingredient(
            "ZnSO4 x 7 H2O",
            "0.000220",
            source=source,
            term=("CHEBI:32312", "zinc sulfate heptahydrate"),
        ),
        _variable(
            "H2O",
            source=source,
            notes=f"{source} lists water without gram or molar amounts.",
            term=("CHEBI:15377", "water"),
        ),
        _ingredient(
            "Na2B4O7 x 10 H2O",
            "0.00450",
            source=source,
            term=("CHEBI:131366", "disodium tetraborate decahydrate"),
        ),
        _ingredient(
            "CoSO4",
            "0.000010",
            source=source,
            term=("CHEBI:53470", "cobalt(II) sulfate"),
        ),
        _variable(
            "H2SO4",
            source=source,
            notes=f"{source} lists H2SO4 as the variable pH 1 acid.",
            term=("CHEBI:26836", "sulfuric acid"),
        ),
    )


DESULFUROCOCCUS_INGREDIENTS = _desulfurococcus_recipe()
PICROPHILUS_INGREDIENTS = _picrophilus_recipe()

TARGETS: tuple[Target, ...] = (
    Target(
        path="archaea/KOMODO_184_DESULFUROCOCCUS_medium.yaml",
        record_id="CultureMech:004208",
        media_term_id="komodo.medium:184",
        source_label="KOMODO Medium 184",
        source_url=KOMODO_184_URL,
        dsmz_pdf=DSMZ_184_PDF,
        ingredients=DESULFUROCOCCUS_INGREDIENTS,
        accepted_signatures=(
            ("H2SO4",),
            tuple(row["preferred_term"] for row in DESULFUROCOCCUS_INGREDIENTS),
        ),
        notes=(
            "KOMODO Medium 184 expands DSMZ Medium 184 into its metabolite table, "
            "including sulfur, salts, trace metals, water, yeast extract, "
            "resazurin, nitrogen, and variable H2SO4 for pH 5.5."
        ),
    ),
    Target(
        path="archaea/KOMODO_723_PICROPHILUS_medium.yaml",
        record_id="CultureMech:006366",
        media_term_id="komodo.medium:723",
        source_label="KOMODO Medium 723",
        source_url=KOMODO_723_URL,
        dsmz_pdf=DSMZ_723_PDF,
        ingredients=PICROPHILUS_INGREDIENTS,
        accepted_signatures=(
            ("H2SO4",),
            tuple(row["preferred_term"] for row in PICROPHILUS_INGREDIENTS),
        ),
        notes=(
            "KOMODO Medium 723 expands DSMZ Medium 723 into its metabolite table, "
            "including salts, trace metals, water, yeast extract, and variable "
            "H2SO4 for pH 1."
        ),
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _component_names(doc: dict[str, Any]) -> tuple[str, ...]:
    return tuple(
        str(row.get("preferred_term") or "")
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    )


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.media_term_id:
        raise ValueError(
            f"{target.path}: expected source term {target.media_term_id}, "
            f"found {source_term!r}"
        )

    if _component_names(doc) not in target.accepted_signatures:
        raise ValueError(f"{target.path}: KOMODO ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    flags.extend(
        (
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        )
    )
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (target.source_url, target.dsmz_pdf):
        if reference not in existing:
            references.append({"reference": reference})


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": target.source_url,
        "notes": (
            f"Replaced the one-row H2SO4 placeholder with the "
            f"{target.source_label} metabolite table and kept the DSMZ PDF "
            "linked from KOMODO as a reference."
        ),
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = copy.deepcopy(list(target.ingredients))
    repaired["notes"] = target.notes
    _ensure_flags(repaired)
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
