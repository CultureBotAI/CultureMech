#!/usr/bin/env python3
"""Repair score-30 CultureBotHT omitted-component variants."""

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

CURATOR = "repair_culturebotht_omissions_score30.py"
ACTION = "RESOLVED_CULTUREBOTHT_OMISSION_SCORE30"
LINK_ACTION = "LINKED_CULTUREBOTHT_OMISSION_SCORE30"
TIMESTAMP = "2026-09-07T00:00:00-07:00"
CULTUREBOTHT_URL = "https://github.com/CultureBotAI/CultureBotHT"


@dataclass(frozen=True)
class Parent:
    path: str
    expected_id: str


@dataclass(frozen=True)
class OmissionTarget:
    path: str
    expected_id: str
    source_id: str
    base_token: str


PARENTS: dict[str, Parent] = {
    "Dv_base_medium": Parent(
        "specialized/dv_base_medium.yaml",
        "CultureMech:015516",
    ),
    "Dv_base_Y_medium": Parent(
        "specialized/dv_base_y_medium.yaml",
        "CultureMech:015520",
    ),
    "MoLS4": Parent(
        "specialized/mols4.yaml",
        "CultureMech:015607",
    ),
    "MoYLS4": Parent(
        "specialized/moyls4.yaml",
        "CultureMech:015634",
    ),
    "ZMB": Parent(
        "specialized/zmb.yaml",
        "CultureMech:015791",
    ),
    "ZMB_ALS": Parent(
        "specialized/zmb_als.yaml",
        "CultureMech:015792",
    ),
}

TARGETS: tuple[OmissionTarget, ...] = (
    OmissionTarget(
        "specialized/dv_base_medium_no_mo.yaml",
        "CultureMech:015517",
        "Dv base medium no Mo",
        "Dv_base_medium",
    ),
    OmissionTarget(
        "specialized/dv_base_medium_no_mo_no_w.yaml",
        "CultureMech:015518",
        "Dv base medium no Mo no W",
        "Dv_base_medium",
    ),
    OmissionTarget(
        "specialized/dv_base_medium_no_w.yaml",
        "CultureMech:015519",
        "Dv base medium no W",
        "Dv_base_medium",
    ),
    OmissionTarget(
        "specialized/dv_base_y_medium_no_fe.yaml",
        "CultureMech:015521",
        "Dv base Y medium no Fe",
        "Dv_base_Y_medium",
    ),
    OmissionTarget(
        "specialized/mols4_no_ammonium.yaml",
        "CultureMech:015609",
        "MoLS4 no ammonium",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_ammonium_no_mo.yaml",
        "CultureMech:015610",
        "MoLS4 no ammonium no Mo",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_ammonium_no_mo_no_w.yaml",
        "CultureMech:015611",
        "MoLS4 no ammonium no Mo no W",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_ammonium_no_w.yaml",
        "CultureMech:015612",
        "MoLS4 no ammonium no W",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_b12.yaml",
        "CultureMech:015614",
        "MoLS4 no B12",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_biotin.yaml",
        "CultureMech:015615",
        "MoLS4 no Biotin",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_choline_chloride.yaml",
        "CultureMech:015616",
        "MoLS4 no Choline chloride",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_folic_acid.yaml",
        "CultureMech:015617",
        "MoLS4 no Folic acid",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_lipoic_acid.yaml",
        "CultureMech:015619",
        "MoLS4 no lipoic acid",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_mo.yaml",
        "CultureMech:015620",
        "MoLS4 no Mo",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_mo_no_w.yaml",
        "CultureMech:015621",
        "MoLS4 no Mo no W",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_nicotinic_acid.yaml",
        "CultureMech:015622",
        "MoLS4 no nicotinic acid",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_pantothenic_acid.yaml",
        "CultureMech:015623",
        "MoLS4 no Pantothenic acid",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_pyridoxine.yaml",
        "CultureMech:015624",
        "MoLS4 no Pyridoxine",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_sulfide.yaml",
        "CultureMech:015625",
        "MoLS4 no sulfide",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_thiamine.yaml",
        "CultureMech:015626",
        "MoLS4 no thiamine",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/mols4_no_w.yaml",
        "CultureMech:015628",
        "MoLS4 no W",
        "MoLS4",
    ),
    OmissionTarget(
        "specialized/moyls4_no_iron.yaml",
        "CultureMech:015635",
        "MoYLS4 no iron",
        "MoYLS4",
    ),
    OmissionTarget(
        "specialized/zmb_nofolicacid.yaml",
        "CultureMech:015830",
        "ZMB noFolicAcid",
        "ZMB",
    ),
    OmissionTarget(
        "specialized/zmb_als_noadenine.yaml",
        "CultureMech:015795",
        "ZMB ALS noAdenine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noalanine.yaml",
        "CultureMech:015796",
        "ZMB ALS noAlanine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noarginine.yaml",
        "CultureMech:015797",
        "ZMB ALS noArginine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noasparagine.yaml",
        "CultureMech:015798",
        "ZMB ALS noAsparagine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noasparticacid.yaml",
        "CultureMech:015799",
        "ZMB ALS noAsparticAcid",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nobiotin.yaml",
        "CultureMech:015800",
        "ZMB ALS noBiotin",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nocyanocobalamin.yaml",
        "CultureMech:015801",
        "ZMB ALS noCyanocobalamin",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nocysteine.yaml",
        "CultureMech:015802",
        "ZMB ALS noCysteine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nocytosine.yaml",
        "CultureMech:015803",
        "ZMB ALS noCytosine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noglutamine.yaml",
        "CultureMech:015805",
        "ZMB ALS noGlutamine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noglutathione.yaml",
        "CultureMech:015806",
        "ZMB ALS noGlutathione",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noglycine.yaml",
        "CultureMech:015807",
        "ZMB ALS noGlycine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noguanine.yaml",
        "CultureMech:015808",
        "ZMB ALS noGuanine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nohistidine.yaml",
        "CultureMech:015809",
        "ZMB ALS noHistidine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noisoleucine.yaml",
        "CultureMech:015810",
        "ZMB ALS noIsoleucine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noleucine.yaml",
        "CultureMech:015811",
        "ZMB ALS noLeucine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nolipoicacid.yaml",
        "CultureMech:015812",
        "ZMB ALS noLipoicAcid",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nolysine.yaml",
        "CultureMech:015813",
        "ZMB ALS noLysine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nomethionine.yaml",
        "CultureMech:015814",
        "ZMB ALS noMethionine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nonicotinicacic.yaml",
        "CultureMech:015815",
        "ZMB ALS noNicotinicAcic",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nopantothenate.yaml",
        "CultureMech:015816",
        "ZMB ALS noPantothenate",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nophenylalanine.yaml",
        "CultureMech:015817",
        "ZMB ALS noPhenylalanine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noproline.yaml",
        "CultureMech:015818",
        "ZMB ALS noProline",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nopyridoxamine.yaml",
        "CultureMech:015819",
        "ZMB ALS noPyridoxamine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noriboflavin.yaml",
        "CultureMech:015820",
        "ZMB ALS noRiboflavin",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_noserine.yaml",
        "CultureMech:015821",
        "ZMB ALS noSerine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nothiamine.yaml",
        "CultureMech:015822",
        "ZMB ALS noThiamine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nothreonine.yaml",
        "CultureMech:015823",
        "ZMB ALS noThreonine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_notryptophan.yaml",
        "CultureMech:015824",
        "ZMB ALS noTryptophan",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_notyrosine.yaml",
        "CultureMech:015825",
        "ZMB ALS noTyrosine",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_nouracil.yaml",
        "CultureMech:015826",
        "ZMB ALS noUracil",
        "ZMB_ALS",
    ),
    OmissionTarget(
        "specialized/zmb_als_novaline.yaml",
        "CultureMech:015827",
        "ZMB ALS noValine",
        "ZMB_ALS",
    ),
)


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8", errors="replace") as stream:
        doc = yaml.load(stream, Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _require_id(doc: dict[str, Any], expected_id: str, relative_path: str) -> None:
    if doc.get("id") != expected_id:
        raise ValueError(
            f"{relative_path}: expected immutable id {expected_id}, found {doc.get('id')!r}"
        )


def _require_source(doc: dict[str, Any], update: OmissionTarget) -> None:
    sources = doc.get("sources") or []
    if not isinstance(sources, list):
        raise ValueError(f"{update.path}: sources is not a list")

    for source in sources:
        if not isinstance(source, dict):
            continue
        if (
            source.get("database") == "CultureBotHT"
            and source.get("database_id") == update.source_id
        ):
            return
    raise ValueError(f"{update.path}: missing CultureBotHT source {update.source_id!r}")


def _omitted_components(
    doc: dict[str, Any],
    update: OmissionTarget,
) -> list[str]:
    ingredients = doc.get("ingredients")
    if not isinstance(ingredients, list) or not ingredients:
        raise ValueError(f"{update.path}: expected base and omitted ingredient rows")

    base = ingredients[0]
    if not isinstance(base, dict) or base.get("preferred_term") != update.base_token:
        raise ValueError(f"{update.path}: expected base row {update.base_token!r}")

    omitted = [
        str(row.get("preferred_term"))
        for row in ingredients[1:]
        if (
            isinstance(row, dict)
            and isinstance(row.get("concentration"), dict)
            and row["concentration"].get("value") == "-"
            and row.get("preferred_term")
        )
    ]
    if not omitted:
        raise ValueError(f"{update.path}: expected at least one omitted ingredient")
    return omitted


def _existing_variant_modification(
    doc: dict[str, Any],
    update: OmissionTarget,
    parent_info: Parent,
) -> str | None:
    if doc.get("variant_relationship") != "OMITTED_COMPONENT_VARIANT":
        return None

    solutions = doc.get("solutions")
    if not isinstance(solutions, list) or not solutions:
        raise ValueError(f"{update.path}: resolved variant is missing parent solution")
    parent_ids = {
        row.get("culturemech_term", {}).get("id")
        for row in solutions
        if isinstance(row, dict) and isinstance(row.get("culturemech_term"), dict)
    }
    if parent_info.expected_id not in parent_ids:
        raise ValueError(
            f"{update.path}: resolved variant is not linked to {parent_info.expected_id}"
        )

    modifications = doc.get("variant_modifications")
    if not isinstance(modifications, list) or not modifications:
        raise ValueError(f"{update.path}: resolved variant has no modification note")
    return str(modifications[0])


def _join_omissions(omitted: list[str]) -> str:
    if len(omitted) == 1:
        return omitted[0]
    if len(omitted) == 2:
        return f"{omitted[0]} and {omitted[1]}"
    return f"{', '.join(omitted[:-1])}, and {omitted[-1]}"


def _prepared_parent(
    parent: dict[str, Any],
    parent_info: Parent,
    base_token: str,
) -> dict[str, Any]:
    parent_name = str(parent.get("name") or base_token)
    return {
        "preferred_term": parent_name,
        "concentration": {"value": "1", "unit": "FOLD_DILUTION"},
        "culturemech_term": _term(parent_info.expected_id, parent_name),
        "notes": f"CultureBotHT lists {base_token} at one-fold final strength.",
    }


def _recipe_ref(
    doc: dict[str, Any],
    relative_path: str,
    notes: str,
) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{relative_path}",
        "relationship": "OMITTED_COMPONENT_VARIANT",
        "id": str(doc.get("id") or ""),
        "name": str(doc.get("name") or ""),
        "notes": notes,
    }


def _upsert_ref(refs: list[Any], new_ref: dict[str, str]) -> None:
    for index, existing in enumerate(refs):
        if isinstance(existing, dict) and existing.get("path") == new_ref["path"]:
            refs[index] = new_ref
            return
    refs.append(new_ref)


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


def _history(doc: dict[str, Any]) -> list[Any]:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    return history


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
    ):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], update: OmissionTarget) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{update.path}: references is not a list")

    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in (f"CultureBotHT:{update.source_id}", CULTUREBOTHT_URL):
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _append_curation_event(
    doc: dict[str, Any],
    update: OmissionTarget,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved score-30 CultureBotHT omitted-component variant",
        "source": f"CultureBotHT:{update.source_id}; {CULTUREBOTHT_URL}",
        "notes": notes,
    }
    history = _history(doc)
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _append_link_event(doc: dict[str, Any], child_path: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": LINK_ACTION,
        "changes": "Linked CultureBotHT omitted-component child medium",
        "notes": f"Added or refreshed reciprocal parent-child link for {child_path}.",
    }
    history = _history(doc)
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == LINK_ACTION
            and existing.get("notes") == event["notes"]
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(
    doc: dict[str, Any],
    update: OmissionTarget,
    parent: dict[str, Any],
) -> dict[str, Any]:
    _require_source(doc, update)
    parent_info = PARENTS[update.base_token]
    existing_variant_modification = _existing_variant_modification(
        doc,
        update,
        parent_info,
    )
    if existing_variant_modification is not None:
        repaired = copy.deepcopy(doc)
        _ensure_flags(repaired)
        _ensure_references(repaired, update)
        return repaired

    omitted = _omitted_components(doc, update)
    parent_name = str(parent.get("name") or update.base_token)
    omission_text = _join_omissions(omitted)
    variant_modification = f"Omits {omission_text} from {parent_name}."
    notes = (
        f"CultureBotHT imports {update.source_id} as {parent_name} with "
        f"{omission_text} omitted."
    )

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "media_term", {"preferred_term": update.source_id}, "physical_state")
    _put_after(repaired, "notes", notes, "description")
    repaired["ingredients"] = []
    _put_after(
        repaired,
        "solutions",
        [_prepared_parent(parent, parent_info, update.base_token)],
        "ingredients",
    )
    _put_after(
        repaired,
        "preparation_steps",
        [
            {
                "step_number": 1,
                "action": "MIX",
                "description": f"Prepare {parent_name} without {omission_text}.",
            }
        ],
        "solutions",
    )
    repaired["parent_media"] = _recipe_ref(parent, parent_info.path, variant_modification)
    repaired["variant_relationship"] = "OMITTED_COMPONENT_VARIANT"
    repaired["variant_modifications"] = [variant_modification]

    _ensure_flags(repaired)
    _ensure_references(repaired, update)
    _append_curation_event(repaired, update, notes)
    return repaired


def plan_repairs(normalized: Path) -> dict[Path, dict[str, Any]]:
    parent_by_token = {
        base_token: _load(normalized / parent.path) for base_token, parent in PARENTS.items()
    }
    for base_token, parent in PARENTS.items():
        _require_id(parent_by_token[base_token], parent.expected_id, parent.path)

    plans = {
        normalized / parent.path: copy.deepcopy(parent_by_token[base_token])
        for base_token, parent in PARENTS.items()
    }
    for update in TARGETS:
        parent_info = PARENTS[update.base_token]
        parent_path = normalized / parent_info.path
        parent = plans[parent_path]
        doc = _load(normalized / update.path)
        _require_id(doc, update.expected_id, update.path)
        repaired = repair_record(doc, update, parent)
        plans[normalized / update.path] = repaired

        children = parent.setdefault("variant_children", [])
        if not isinstance(children, list):
            raise ValueError(f"{parent_info.path}: variant_children is not a list")
        _upsert_ref(
            children,
            _recipe_ref(
                repaired,
                update.path,
                repaired["variant_modifications"][0],
            ),
        )
        children.sort(key=lambda row: row.get("path", "") if isinstance(row, dict) else "")
        _append_link_event(parent, update.path)

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
            changed_count += int(changed)
            status = "wrote" if changed else "skip"
        else:
            changed = path.read_bytes() != dump_record(doc).encode("utf-8")
            changed_count += int(changed)
            status = "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
