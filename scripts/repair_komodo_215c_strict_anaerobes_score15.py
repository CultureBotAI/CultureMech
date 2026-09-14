#!/usr/bin/env python3
"""Repair the DSMZ/KOMODO Medium 215c strict-anaerobe BHI family."""

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

DSMZ_215C = "bacterial/bhi_medium_for_strict_anaerobes.yaml"
KOMODO_215C = "bacterial/KOMODO_215c_BHI_medium_FOR_STRICT_ANAEROBES.yaml"
KOMODO_215C_1 = "bacterial/for_dsm_10643.yaml"
KOMODO_215C_2 = "bacterial/for_dsm_15692.yaml"
KOMODO_215C_3 = "bacterial/for_dsm_19851.yaml"

EXPECTED_IDS = {
    DSMZ_215C: "CultureMech:001317",
    KOMODO_215C: "CultureMech:004425",
    KOMODO_215C_1: "CultureMech:004422",
    KOMODO_215C_2: "CultureMech:004423",
    KOMODO_215C_3: "CultureMech:004424",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_215C: "mediadive.medium:215c",
    KOMODO_215C: "komodo.medium:215c",
    KOMODO_215C_1: "komodo.medium:215c.1",
    KOMODO_215C_2: "komodo.medium:215c.2",
    KOMODO_215C_3: "komodo.medium:215c.3",
}

DSMZ_215C_REST = "https://mediadive.dsmz.de/rest/medium/215c"
DSMZ_215C_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215c.pdf"
KOMODO_BASE = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)

CURATOR = "repair_komodo_215c_strict_anaerobes_score15.py"
ACTION = "RESOLVED_DSMZ_KOMODO_215C_BHI_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
    "parent_media",
    "variant_relationship",
    "variant_modifications",
    "variant_children",
    "data_quality_flags",
    "references",
)


@dataclass(frozen=True)
class Target:
    path: str
    source_label: str
    source_url: str
    notes: str
    ingredients: tuple[dict[str, Any], ...]
    preparation_steps: tuple[str, ...] = ()
    ph_value: float | None = None
    ph_range: dict[str, float] | None = None
    parent_media: dict[str, str] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, str], ...] = ()


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    source: str,
    notes: str,
    *,
    term: tuple[str, str] | None = None,
    chebi: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term:
        row["term"] = _term(*term)
    if chebi:
        row["mediaingredientmech_chebi_term"] = _term(*chebi)
    return row


def _bhi(value: str, source: str) -> dict[str, Any]:
    return _ingredient(
        "Brain heart infusion",
        value,
        "G_PER_L",
        source,
        f"{source} lists Brain heart infusion at {value} g/L as an opaque rich-meat product.",
        term=("mediadive.compound:186", "Brain heart infusion"),
    )


def _water(source: str) -> dict[str, Any]:
    return _ingredient(
        "Distilled water",
        "1000",
        "ML_PER_L",
        source,
        f"{source} brings the recipe to one liter with distilled water.",
        term=("mediadive.compound:4", "Distilled water"),
        chebi=("CHEBI:15377", "water"),
    )


def _cysteine(source: str) -> dict[str, Any]:
    return _ingredient(
        "L-Cysteine HCl x H2O",
        "0.25",
        "G_PER_L",
        source,
        f"{source} lists 0.25 g/L L-Cysteine HCl x H2O.",
        term=("mediadive.compound:770", "L-Cysteine HCl x H2O"),
        chebi=("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    )


def _sulfide(source: str) -> dict[str, Any]:
    return _ingredient(
        "Na2S x 9 H2O",
        "0.25",
        "G_PER_L",
        source,
        f"{source} lists 0.25 g/L Na2S x 9 H2O.",
        term=("mediadive.compound:54", "Na2S x 9 H2O"),
        chebi=("CHEBI:76209", "sodium sulfide nonahydrate"),
    )


def _gas(preferred_term: str, source: str, term: tuple[str, str]) -> dict[str, Any]:
    return _ingredient(
        preferred_term,
        "variable",
        "VARIABLE",
        source,
        f"{source} lists {preferred_term} without a gram or molar amount.",
        term=term,
        chebi=term,
    )


def _glycerol(source: str) -> dict[str, Any]:
    return _ingredient(
        "glycerol",
        "8.70",
        "G_PER_L",
        source,
        f"{source} adds 8.70 g/L glycerol to the DSMZ Medium 215c base.",
        term=("CHEBI:17754", "glycerol"),
        chebi=("CHEBI:17754", "glycerol"),
    )


def _nahco3(source: str) -> dict[str, Any]:
    return _ingredient(
        "NaHCO3",
        "variable",
        "VARIABLE",
        source,
        f"{source} records NaHCO3 in the pH 7.2 buffer context without a gram amount.",
        term=("CHEBI:32139", "sodium hydrogencarbonate"),
        chebi=("CHEBI:32139", "sodium hydrogencarbonate"),
    )


def _ethanol(source: str) -> dict[str, Any]:
    return _ingredient(
        "ethanol",
        "variable",
        "VARIABLE",
        source,
        f"{source} lists ethanol without a gram or molar amount.",
        term=("CHEBI:16236", "ethanol"),
        chebi=("CHEBI:16236", "ethanol"),
    )


def _vitamin_k1(source: str) -> dict[str, Any]:
    return _ingredient(
        "Vitamin K1",
        "variable",
        "VARIABLE",
        source,
        f"{source} lists Vitamin K1 without a gram or molar amount.",
        term=("CHEBI:18067", "phylloquinone"),
        chebi=("CHEBI:18067", "phylloquinone"),
    )


def _haemin(source: str) -> dict[str, Any]:
    return _ingredient(
        "haemin",
        "variable",
        "VARIABLE",
        source,
        f"{source} lists haemin without a gram or molar amount.",
        term=("CHEBI:50385", "hemin"),
        chebi=("CHEBI:50385", "hemin"),
    )


def _recipe_ref(
    path: str,
    relationship: str,
    notes: str,
) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": EXPECTED_IDS[path],
        "name": Path(path).stem,
        "notes": notes,
    }


DSMZ_PARENT = _recipe_ref(
    DSMZ_215C,
    "SOURCE_DUPLICATE",
    "DSMZ Medium 215c is the official source formulation duplicated by KOMODO Medium 215c.",
)
DSMZ_CHILD = _recipe_ref(
    KOMODO_215C,
    "SOURCE_DUPLICATE",
    "KOMODO Medium 215c cites DSMZ Medium 215c and preserves its formulation.",
)
KOMODO_PARENT = _recipe_ref(
    KOMODO_215C,
    "STRAIN_SPECIFIC_VARIANT",
    "KOMODO Medium 215c is the parent BHI strict-anaerobe formulation.",
)
KOMODO_10643_CHILD = _recipe_ref(
    KOMODO_215C_1,
    "STRAIN_SPECIFIC_VARIANT",
    "KOMODO Medium 215c.1 applies DSMZ Medium 215c to DSM 10643 and adds glycerol.",
)
KOMODO_15692_CHILD = _recipe_ref(
    KOMODO_215C_2,
    "STRAIN_SPECIFIC_VARIANT",
    "KOMODO Medium 215c.2 applies DSMZ Medium 215c to DSM 15692 and records pH 7.2 with bicarbonate and CO2.",
)
KOMODO_19851_CHILD = _recipe_ref(
    KOMODO_215C_3,
    "STRAIN_SPECIFIC_VARIANT",
    "KOMODO Medium 215c.3 applies DSMZ Medium 215c to DSM 19851 and adds haemin, Vitamin K1, and ethanol.",
)

DSMZ_SOURCE = "DSMZ Medium 215c"
KOMODO_SOURCE = "KOMODO Medium 215c"
KOMODO_10643_SOURCE = "KOMODO Medium 215c.1"
KOMODO_15692_SOURCE = "KOMODO Medium 215c.2"
KOMODO_19851_SOURCE = "KOMODO Medium 215c.3"

TARGETS: tuple[Target, ...] = (
    Target(
        path=DSMZ_215C,
        source_label=DSMZ_SOURCE,
        source_url=DSMZ_215C_REST,
        notes=(
            "MediaDive and DSMZ Medium 215c list BHI Medium for Strict Anaerobes as "
            "37 g/L Brain heart infusion, 0.25 g/L L-Cysteine HCl x H2O, "
            "0.25 g/L Na2S x 9 H2O, and distilled water, prepared anoxically "
            "under 100% N2 with the reducing agents added from sterile anoxic "
            "solutions after autoclaving."
        ),
        ingredients=(
            _bhi("37", DSMZ_SOURCE),
            _cysteine(DSMZ_SOURCE),
            _sulfide(DSMZ_SOURCE),
            _water(DSMZ_SOURCE),
        ),
        ph_range={"min": 7.2, "max": 7.6},
        preparation_steps=(
            "Prepare the medium anoxically under 100% N2 gas atmosphere.",
            "Add L-Cysteine HCl x H2O and Na2S x 9 H2O after autoclaving from "
            "sterile anoxic solutions prepared under N2.",
        ),
        variant_children=(DSMZ_CHILD,),
    ),
    Target(
        path=KOMODO_215C,
        source_label=KOMODO_SOURCE,
        source_url=f"{KOMODO_BASE}215c",
        notes=(
            "KOMODO Medium 215c cites DSMZ Medium 215c and records the same "
            "37 g/L Brain heart infusion, 0.25 g/L Na2S x 9 H2O, 0.25 g/L "
            "Cysteine-HCl x H2O, distilled water, and N2 gas atmosphere."
        ),
        ingredients=(
            _bhi("37", KOMODO_SOURCE),
            _sulfide(KOMODO_SOURCE),
            _water(KOMODO_SOURCE),
            _cysteine(KOMODO_SOURCE),
            _gas("N2", KOMODO_SOURCE, ("CHEBI:17997", "dinitrogen")),
        ),
        parent_media=DSMZ_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(
            "KOMODO source-catalogue duplicate of DSMZ Medium 215c.",
        ),
        variant_children=(
            KOMODO_10643_CHILD,
            KOMODO_15692_CHILD,
            KOMODO_19851_CHILD,
        ),
    ),
    Target(
        path=KOMODO_215C_1,
        source_label=KOMODO_10643_SOURCE,
        source_url=f"{KOMODO_BASE}215c.1",
        notes=(
            "KOMODO Medium 215c.1 records a DSM 10643 strain-specific DSMZ "
            "Medium 215c derivative with 37 g/L Brain heart infusion, "
            "0.25 g/L Na2S x 9 H2O, 8.70 g/L glycerol, distilled water, "
            "0.25 g/L Cysteine-HCl x H2O, and N2 gas."
        ),
        ingredients=(
            _bhi("37", KOMODO_10643_SOURCE),
            _sulfide(KOMODO_10643_SOURCE),
            _glycerol(KOMODO_10643_SOURCE),
            _water(KOMODO_10643_SOURCE),
            _cysteine(KOMODO_10643_SOURCE),
            _gas("N2", KOMODO_10643_SOURCE, ("CHEBI:17997", "dinitrogen")),
        ),
        parent_media=KOMODO_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "KOMODO Medium 215c.1 adds 8.70 g/L glycerol to the DSMZ Medium 215c base for DSM 10643.",
        ),
    ),
    Target(
        path=KOMODO_215C_2,
        source_label=KOMODO_15692_SOURCE,
        source_url=f"{KOMODO_BASE}215c.2",
        notes=(
            "KOMODO Medium 215c.2 records a DSM 15692 strain-specific DSMZ "
            "Medium 215c derivative at pH 7.2 with NaHCO3, N2, and CO2 gas "
            "context."
        ),
        ingredients=(
            _bhi("37", KOMODO_15692_SOURCE),
            _sulfide(KOMODO_15692_SOURCE),
            _water(KOMODO_15692_SOURCE),
            _gas("CO2", KOMODO_15692_SOURCE, ("CHEBI:16526", "carbon dioxide")),
            _cysteine(KOMODO_15692_SOURCE),
            _gas("N2", KOMODO_15692_SOURCE, ("CHEBI:17997", "dinitrogen")),
            _nahco3(KOMODO_15692_SOURCE),
        ),
        ph_value=7.2,
        parent_media=KOMODO_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "KOMODO Medium 215c.2 records pH 7.2 and a variable NaHCO3 and CO2 buffer context for DSM 15692.",
        ),
    ),
    Target(
        path=KOMODO_215C_3,
        source_label=KOMODO_19851_SOURCE,
        source_url=f"{KOMODO_BASE}215c.3",
        notes=(
            "KOMODO Medium 215c.3 records a DSM 19851 strain-specific DSMZ "
            "Medium 215c derivative with 36.63 g/L Brain heart infusion plus "
            "variable ethanol, Vitamin K1, and haemin."
        ),
        ingredients=(
            _bhi("36.63", KOMODO_19851_SOURCE),
            _ethanol(KOMODO_19851_SOURCE),
            _sulfide(KOMODO_19851_SOURCE),
            _water(KOMODO_19851_SOURCE),
            _vitamin_k1(KOMODO_19851_SOURCE),
            _cysteine(KOMODO_19851_SOURCE),
            _haemin(KOMODO_19851_SOURCE),
            _gas("N2", KOMODO_19851_SOURCE, ("CHEBI:17997", "dinitrogen")),
        ),
        parent_media=KOMODO_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "KOMODO Medium 215c.3 uses 36.63 g/L Brain heart infusion and lists variable ethanol, Vitamin K1, and haemin for DSM 19851.",
        ),
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True

    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term") or {}
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != EXPECTED_IDS[target.path]:
        raise ValueError(
            f"{target.path}: found id {doc.get('id')!r}, "
            f"expected {EXPECTED_IDS[target.path]!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[target.path]:
        raise ValueError(
            f"{target.path}: found source term {source_term!r}, "
            f"expected {EXPECTED_SOURCE_TERMS[target.path]!r}"
        )


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    rows = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    has_grounded = any(_grounded(row) for row in rows)
    has_unmapped = any(not _grounded(row) for row in rows)

    if has_grounded and "has_ontology_mappings" not in flags:
        flags.append("has_ontology_mappings")
    elif not has_grounded and "has_ontology_mappings" in flags:
        flags.remove("has_ontology_mappings")

    if has_unmapped and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")
    elif not has_unmapped and "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    if flags:
        doc["data_quality_flags"] = flags
    else:
        doc.pop("data_quality_flags", None)


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    for url in (target.source_url, DSMZ_215C_PDF):
        if url not in {row.get("reference") for row in references if isinstance(row, dict)}:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ/KOMODO Medium 215c BHI strict-anaerobe formulation",
        "source": target.source_url,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        repaired.pop(field, None)

    _put_after(repaired, "medium_type", "COMPLEX", "category")
    _put_after(repaired, "composition_type", "UNDEFINED", "medium_type")
    _put_after(repaired, "physical_state", "LIQUID", "composition_type")

    anchor = "physical_state"
    if target.ph_value is not None:
        _put_after(repaired, "ph_value", target.ph_value, anchor)
        anchor = "ph_value"
    if target.ph_range is not None:
        _put_after(repaired, "ph_range", copy.deepcopy(target.ph_range), anchor)
        anchor = "ph_range"

    _put_after(repaired, "notes", target.notes, "media_term")
    _put_after(
        repaired,
        "ingredients",
        [copy.deepcopy(row) for row in target.ingredients],
        "notes",
    )
    if target.preparation_steps:
        _put_after(
            repaired,
            "preparation_steps",
            [
                {"step_number": index, "action": "MIX", "description": description}
                for index, description in enumerate(target.preparation_steps, start=1)
            ],
            "ingredients",
        )

    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)

    after = "data_quality_flags"
    _put_after(repaired, "data_quality_flags", repaired["data_quality_flags"], "preparation_steps")
    _put_after(repaired, "references", repaired["references"], "data_quality_flags")

    if target.parent_media is not None:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), "references")
        after = "parent_media"
    if target.variant_relationship is not None:
        _put_after(repaired, "variant_relationship", target.variant_relationship, after)
        after = "variant_relationship"
    if target.variant_modifications:
        _put_after(
            repaired,
            "variant_modifications",
            list(target.variant_modifications),
            after,
        )
        after = "variant_modifications"
    if target.variant_children:
        _put_after(
            repaired,
            "variant_children",
            [copy.deepcopy(child) for child in target.variant_children],
            after,
        )

    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        plans[normalized / target.path] = repair_record(
            _load(normalized / target.path),
            target,
        )
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
