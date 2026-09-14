#!/usr/bin/env python3
"""Repair score-20 TOGO commercial products and one-component wrappers."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_commercial_score20.py"
ACTION = "RESOLVED_TOGO_COMMERCIAL_SCORE20_GRAPH"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

M1125_DB_SEA_SALTS = "bacterial/TOGO_M1125_DB_Characterization_Medium_NO.2_With_1_Sea_Salts.yaml"
M1524_TODD_HEWITT = "bacterial/TOGO_M1524_Todd_Hewitt_Medium.yaml"
M1525_GAM = "bacterial/TOGO_M1525_GAM_Medium.yaml"
M1547_MARINE_AGAR = "bacterial/TOGO_M1547_Marine_Agar_2216.yaml"
M1721_PDA = "bacterial/TOGO_M1721_Potato_Dextrose_Agar.yaml"
M20_TRYPTO_SOYA = "bacterial/TOGO_M20_Trypto-Soya_Agar.yaml"
M33_MARINE_BROTH = "bacterial/TOGO_M33_Marine_Broth_2216.yaml"
M682_DISTILLED_WATER = "bacterial/TOGO_M682_Distilled_Water.yaml"

TOGO_M1125 = "https://togomedium.org/medium/M1125"
TOGO_M1524 = "https://togomedium.org/medium/M1524"
TOGO_M1525 = "https://togomedium.org/medium/M1525"
TOGO_M1547 = "https://togomedium.org/medium/M1547"
TOGO_M1721 = "https://togomedium.org/medium/M1721"
TOGO_M20 = "https://togomedium.org/medium/M20"
TOGO_M33 = "https://togomedium.org/medium/M33"
TOGO_M682 = "https://togomedium.org/medium/M682"

JCM_27 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=27"
JCM_41 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=41"
JCM_574 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=574"
JCM_664 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=664"
JCM_1058 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1058"

NBRC_311 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=311"
NBRC_312 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=312"
NBRC_340 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=340"
NBRC_930 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=930"

ATCC_MEDIUM_2 = "https://www.atcc.org/~/media/B5025AB990724A91B4491C391E054448.ashx"

DB_CHARACTERIZATION = {"id": "CultureMech:009974", "label": "DB Characterization Medium NO. 2"}

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
)

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_media_term: str
    imported_signature: tuple[Component, ...]
    recipe: dict[str, Any]
    notes: str
    reference_urls: tuple[str, ...]
    drop_fields: tuple[str, ...] = field(default_factory=tuple)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str] | None = None,
    culturemech_term: dict[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    if culturemech_term is not None:
        row["culturemech_term"] = copy.deepcopy(culturemech_term)
    return row


def _solution(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
    culturemech_term: dict[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "notes": notes,
    }
    if culturemech_term is not None:
        row["culturemech_term"] = copy.deepcopy(culturemech_term)
    return row


def _water(source: str) -> dict[str, Any]:
    return _ingredient(
        "Distilled water",
        "1000",
        "ML_PER_L",
        source=source,
        notes=f"{source} lists 1.0 L distilled water.",
        term=("CHEBI:15377", "water"),
    )


def _atcc_water() -> dict[str, Any]:
    return _ingredient(
        "Distilled water",
        "1000.0",
        "ML_PER_L",
        source="ATCC Medium 2",
        notes="ATCC Medium 2 prints 1000.0 mL distilled water in the scratch formulation.",
        term=("CHEBI:15377", "water"),
    )


def _marine_component(
    preferred_term: str,
    value: str,
    term: tuple[str, str],
    notes: str = "ATCC Medium 2 prints this component in the Difco Marine Agar/Broth 2216 scratch formulation.",
) -> dict[str, Any]:
    return _ingredient(
        preferred_term,
        value,
        "G_PER_L",
        source="ATCC Medium 2",
        notes=notes,
        term=term,
    )


def _marine_agar_broth_components(*, include_agar: bool) -> list[dict[str, Any]]:
    components = [
        _marine_component("Peptone", "5.0", ("MICRO:0000178", "peptone")),
        _marine_component("Yeast Extract", "1.0", ("FOODON:03315426", "yeast extract")),
        _marine_component("Ferric Citrate", "0.1", ("CHEBI:144421", "iron(III) citrate")),
        _marine_component("Sodium Chloride", "19.45", ("CHEBI:26710", "sodium chloride")),
        _marine_component("Magnesium Chloride", "8.8", ("CHEBI:6636", "magnesium dichloride")),
        _marine_component("Sodium Sulfate", "3.24", ("CHEBI:32149", "sodium sulfate")),
        _marine_component("Calcium Chloride", "1.8", ("CHEBI:3312", "calcium dichloride")),
        _marine_component("Potassium Chloride", "0.55", ("CHEBI:32588", "potassium chloride")),
        _marine_component(
            "Sodium Bicarbonate",
            "0.16",
            ("CHEBI:32139", "sodium hydrogencarbonate"),
        ),
        _marine_component("Potassium Bromide", "0.08", ("CHEBI:32030", "potassium bromide")),
        _marine_component(
            "Strontium Chloride",
            "0.034",
            ("CHEBI:36383", "strontium dichloride"),
        ),
        _marine_component("Boric Acid", "0.022", ("CHEBI:33118", "boric acid")),
        _marine_component("Sodium Silicate", "0.004", ("CHEBI:60720", "sodium silicate")),
        _marine_component("Sodium Fluoride", "0.0024", ("CHEBI:28741", "sodium fluoride")),
        _marine_component(
            "Ammonium Nitrate",
            "0.0016",
            ("CHEBI:63038", "ammonium nitrate"),
        ),
        _marine_component(
            "Disodium Phosphate",
            "0.008",
            ("CHEBI:34683", "disodium hydrogenphosphate"),
        ),
    ]
    if include_agar:
        components.append(
            _marine_component(
                "Agar",
                "15.0",
                ("CHEBI:2509", "agar"),
                "ATCC Medium 2 prints 15.0 g agar in the Difco Marine Agar 2216 scratch formulation.",
            )
        )
    components.append(_atcc_water())
    return components


def _marine_broth_recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": _marine_agar_broth_components(include_agar=False),
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Prepare Marine Broth 2216 from the Difco Marine Agar/Broth "
                    "2216 scratch formulation in 1000 mL distilled water, omitting agar."
                ),
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Autoclave at 121 C.",
            },
        ],
        "sterilization": {"method": "AUTOCLAVE"},
    }


def _marine_agar_recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": _marine_agar_broth_components(include_agar=True),
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Prepare Marine Agar 2216 from the Difco Marine Agar/Broth "
                    "2216 scratch formulation in 1000 mL distilled water, including 15.0 g agar."
                ),
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Autoclave at 121 C.",
            },
        ],
        "sterilization": {"method": "AUTOCLAVE"},
    }


TARGETS: tuple[Target, ...] = (
    Target(
        path=M1125_DB_SEA_SALTS,
        expected_id="CultureMech:007646",
        expected_media_term="TOGO:M1125",
        imported_signature=(
            ("Sea salts (Sigma)", "10", "G_PER_L"),
            ("DB Characterization Medium NO. 2", "1000", "ML_PER_L"),
        ),
        notes=(
            "TOGO M1125 mirrors JCM Medium 1058: use JCM Medium 574 DB "
            "Characterization Medium No. 2 supplemented with 10.0 g/L sea salts (Sigma)."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "Sea salts (Sigma)",
                    "10",
                    "G_PER_L",
                    source="JCM Medium 1058",
                    notes="JCM Medium 1058 supplements Medium 574 with 10.0 g/L sea salts (Sigma).",
                    term=None,
                )
            ],
            "solutions": [
                _solution(
                    "DB Characterization Medium NO. 2",
                    "1000",
                    "ML_PER_L",
                    notes="JCM Medium 1058 uses JCM Medium 574 as the prepared base medium.",
                    culturemech_term=DB_CHARACTERIZATION,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Prepare DB Characterization Medium No. 2 from JCM Medium 574 "
                        "and supplement it with 10.0 g/L sea salts (Sigma)."
                    ),
                }
            ],
            "parent_media": {
                "path": "data/normalized_yaml/bacterial/TOGO_M578_DB_Characterization_Medium_NO._2.yaml",
                "relationship": "SUPPLEMENTED_VARIANT",
                "id": "CultureMech:009974",
                "name": "db_characterization_medium_no_2",
                "notes": "Supplements JCM Medium 574 with 10.0 g/L sea salts (Sigma).",
            },
            "variant_relationship": "SUPPLEMENTED_VARIANT",
            "variant_modifications": ["Supplements JCM Medium 574 with 10.0 g/L sea salts (Sigma)."],
        },
        reference_urls=(TOGO_M1125, JCM_1058, JCM_574),
    ),
    Target(
        path=M1524_TODD_HEWITT,
        expected_id="CultureMech:008070",
        expected_media_term="TOGO:M1524",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Bacto Todd Hewitt Broth (Difco)", "30", "G_PER_L"),
        ),
        notes=(
            "TOGO M1524 mirrors NBRC Medium 311: 30 g Bacto Todd Hewitt Broth "
            "(Difco) in 1 L distilled water at pH 7.3."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 7.3,
            "ingredients": [
                _ingredient(
                    "Bacto Todd Hewitt Broth (Difco)",
                    "30",
                    "G_PER_L",
                    source="NBRC Medium 311",
                    notes="NBRC Medium 311 lists 30 g Bacto Todd Hewitt Broth (Difco).",
                ),
                _water("NBRC Medium 311"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Dissolve 30 g Bacto Todd Hewitt Broth (Difco) in 1 L distilled water.",
                }
            ],
        },
        reference_urls=(TOGO_M1524, NBRC_311),
    ),
    Target(
        path=M1525_GAM,
        expected_id="CultureMech:008071",
        expected_media_term="TOGO:M1525",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Nissui GAM Broth*", "59", "G_PER_L"),
        ),
        notes=(
            "TOGO M1525 mirrors NBRC Medium 312: 59 g Nissui GAM Broth in "
            "1 L distilled water at pH 7.3."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 7.3,
            "ingredients": [
                _ingredient(
                    "Nissui GAM Broth*",
                    "59",
                    "G_PER_L",
                    source="NBRC Medium 312",
                    notes=(
                        "NBRC Medium 312 lists 59 g Nissui GAM Broth; "
                        "the footnote identifies Nissui Pharmaceutical Co. Ltd., Tokyo, Japan."
                    ),
                ),
                _water("NBRC Medium 312"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Dissolve 59 g Nissui GAM Broth in 1 L distilled water.",
                }
            ],
        },
        reference_urls=(TOGO_M1525, NBRC_312),
        drop_fields=("variant_children",),
    ),
    Target(
        path=M1547_MARINE_AGAR,
        expected_id="CultureMech:008095",
        expected_media_term="TOGO:M1547",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Bacto Marine Agar 2216 (Difco)", "55.1", "G_PER_L"),
        ),
        notes=(
            "TOGO M1547 mirrors NBRC Medium 340, which lists 55.1 g "
            "Bacto Marine Agar 2216 (Difco) in 1 L distilled water and "
            "states pH unadjusted; ATCC Medium 2 confirms the same 55.1 g "
            "Marine Agar 2216 commercial product and prints the scratch Difco "
            "Marine Agar/Broth 2216 formulation with agar."
        ),
        recipe=_marine_agar_recipe(),
        reference_urls=(TOGO_M1547, NBRC_340, ATCC_MEDIUM_2),
    ),
    Target(
        path=M1721_PDA,
        expected_id="CultureMech:008284",
        expected_media_term="TOGO:M1721",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Nissui Potato Dextrose Agar", "39", "G_PER_L"),
        ),
        notes=(
            "TOGO M1721 mirrors NBRC Medium 930: 39 g Nissui Potato "
            "Dextrose Agar in 1 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Nissui Potato Dextrose Agar",
                    "39",
                    "G_PER_L",
                    source="NBRC Medium 930",
                    notes="NBRC Medium 930 lists 39 g Nissui Potato Dextrose Agar.",
                ),
                _water("NBRC Medium 930"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Suspend 39 g Nissui Potato Dextrose Agar in 1 L distilled water.",
                }
            ],
        },
        reference_urls=(TOGO_M1721, NBRC_930),
    ),
    Target(
        path=M20_TRYPTO_SOYA,
        expected_id="CultureMech:008691",
        expected_media_term="TOGO:M20",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Trypto--soya agar (Nissui)", "40", "G_PER_L"),
        ),
        notes=(
            "TOGO M20 mirrors JCM Medium 27: 40.0 g Trypto-soya agar "
            "(Nissui) in 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Trypto-soya agar (Nissui)",
                    "40.0",
                    "G_PER_L",
                    source="JCM Medium 27",
                    notes="JCM Medium 27 lists 40.0 g Trypto-soya agar (Nissui).",
                ),
                _water("JCM Medium 27"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Dissolve 40.0 g Trypto-soya agar (Nissui) in 1.0 L distilled water.",
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(TOGO_M20, JCM_27),
    ),
    Target(
        path=M33_MARINE_BROTH,
        expected_id="CultureMech:009718",
        expected_media_term="TOGO:M33",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Marine broth 2216 (BD-Difco)", "37.4", "G_PER_L"),
        ),
        notes=(
            "TOGO M33 mirrors JCM Medium 41, which lists 37.4 g Marine "
            "broth 2216 (BD-Difco) in 1.0 L distilled water; ATCC Medium 2 "
            "confirms the same 37.4 g Marine Broth 2216 product and prints "
            "the scratch Difco Marine Agar/Broth 2216 formulation with agar omitted."
        ),
        recipe=_marine_broth_recipe(),
        reference_urls=(TOGO_M33, JCM_41, ATCC_MEDIUM_2),
    ),
    Target(
        path=M682_DISTILLED_WATER,
        expected_id="CultureMech:010087",
        expected_media_term="TOGO:M682",
        imported_signature=(("Distilled water", "1", "G_PER_L"),),
        notes="TOGO M682 mirrors JCM Medium 664, which consists of autoclaved distilled water.",
        recipe={
            "medium_type": "DEFINED",
            "composition_type": "DEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "Distilled water",
                    "1000",
                    "ML_PER_L",
                    source="JCM Medium 664",
                    notes="JCM Medium 664 consists of autoclaved distilled water.",
                    term=("CHEBI:15377", "water"),
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave distilled water at 121 C for 15 min.",
                }
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(TOGO_M682, JCM_664),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _iter_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    components.extend(row for row in doc.get("solutions") or [] if isinstance(row, dict))
    return components


def _signature(doc: dict[str, Any]) -> tuple[Component, ...]:
    signature: list[Component] = []
    for row in _iter_components(doc):
        concentration = row.get("concentration") or {}
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _recipe_signature(recipe: dict[str, Any]) -> tuple[Component, ...]:
    pseudo_doc = {
        "ingredients": recipe.get("ingredients") or [],
        "solutions": recipe.get("solutions") or [],
    }
    return _signature(pseudo_doc)


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


def _check_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected immutable id {target.expected_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(
            f"{target.path}: expected media term {target.expected_media_term}, "
            f"found {_source_term_id(doc)!r}"
        )

    accepted_signatures = {target.imported_signature, _recipe_signature(target.recipe)}
    if _signature(doc) not in accepted_signatures:
        raise ValueError(f"{target.path}: component signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    components = _iter_components(doc)
    has_ontology = any(_grounded(component) for component in components)
    has_unmapped = any(not _grounded(component) for component in components)

    if has_ontology and "has_ontology_mappings" not in flags:
        flags.append("has_ontology_mappings")
    elif not has_ontology and "has_ontology_mappings" in flags:
        flags.remove("has_ontology_mappings")

    if has_unmapped and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")
    elif not has_unmapped and "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    doc["data_quality_flags"] = list(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], reference_urls: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in reference_urls:
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.reference_urls),
        "notes": target.notes,
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
    _check_target(doc, target)

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in target.recipe:
            repaired[recipe_field] = copy.deepcopy(target.recipe[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    for drop_field in target.drop_fields:
        repaired.pop(drop_field, None)

    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, target.reference_urls)
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
    sys.exit(main())
