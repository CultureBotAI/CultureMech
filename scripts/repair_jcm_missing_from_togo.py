#!/usr/bin/env python3
"""Recover 28 empty JCM recipes from matching TOGO source payloads.

MediaDive imported these JCM records with a cross-reference instruction but no
composition. The locally fetched TOGO snapshot has source-equivalent records whose
``original_media_id`` is the same JCM medium number. This migration restores only
the final recipe layer: direct components stay in ``ingredients`` and stock
additions stay in ``solutions``. Locally defined stocks are nested only when their
source volumes establish a defensible batch basis.

The exact records, raw source projections, and reviewed importer outputs are
fingerprinted below. Validation of every target completes before any file is
written. J249/M241 and J867/M904 are deliberately excluded because their TOGO
payloads contain no composition, only the same "See source" placeholder.

The TOGO JSON is a fetched, gitignored input. Run the repository's TOGO fetch task
before this migration. The command is dry-run by default; pass ``--apply`` to write.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import write_record  # noqa: E402

TogoImporter = import_module("culturemech.import.togo_importer").TogoImporter

RAW_FILE = REPO / "data" / "raw" / "togo" / "togo_media.json"
NORMALIZED = REPO / "data" / "normalized_yaml"
ACTION = "RECOVERED_JCM_COMPOSITION_FROM_TOGO"
TIMESTAMP = "2026-08-25T00:00:00-07:00"
REMOVED_FLAGS = {"incomplete_composition", "source_information_unavailable"}
PLACEHOLDER = re.compile(r"see\s+source\s+for\s+composition", re.I)


@dataclass(frozen=True)
class Target:
    jcm_id: str
    togo_id: str
    relative_path: str
    raw_sha256: str
    output_sha256: str
    ingredient_count: int
    solution_count: int
    preparation_step_count: int


TARGETS = (
    Target(
        "J94",
        "M86",
        "bacterial/smy_medium.yaml",
        "b2747efb066aab1276ed598fd69402f2e9f59722a52595553997fdc8d7e8990f",
        "fb6a4476a66582edcb39cc8acb66e5e5393ad8173502627de632c58c37ddfd98",
        6,
        2,
        3,
    ),
    Target(
        "J179",
        "M172",
        "bacterial/medium_10_broth.yaml",
        "e0fe7cca24dfcc1f294e2498bfd2a93631978c321eb143e37c2a7f6433869459",
        "958a3cda96a54696bbbc77a6a4fc5a0bfd5e183f27269e2b02354417cc584119",
        6,
        8,
        2,
    ),
    Target(
        "J210",
        "M203",
        "bacterial/modified_medium_10.yaml",
        "41e8fc4d841ffa850bb253c1d7c111900646ec311cc6200d4a4a12b7d26fddf2",
        "2ebedbeee6c92c21f5d1a8f81003a7a3c7922aa06241808152e019cf43b8a4dd",
        7,
        8,
        2,
    ),
    Target(
        "J260",
        "M252",
        "bacterial/eg_medium_with_10_nacl.yaml",
        "56aebf808c35950b1bbf4062f37cb9dedbf7a2cbf9bf4c1649fbd2a4b0b63382",
        "f1aad5728309d94ed339649ddc755ee067329d87db7dffc210dc161de42b3d73",
        11,
        1,
        2,
    ),
    Target(
        "J313",
        "M308",
        "bacterial/jcm_medium_no_313.yaml",
        "915fee995311f9b3e956ccae78de8e18fd7c18573cc02ecc09e351bca4da6414",
        "25d4029b9fceba6bf2dc68df7f33b74a9ee7f49c91f76190e350448cfcd97c99",
        5,
        4,
        2,
    ),
    Target(
        "J361",
        "M355",
        "archaea/methanocaldococcus_indiensis_medium.yaml",
        "3c3d16f466af57587920040661fca2726429f5aab23db74d54b2decff552fd60",
        "bee17fdc77a6451b6ba3fa4b750af6740504d7289e6a696a4c7ef32d642e6265",
        18,
        3,
        2,
    ),
    Target(
        "J376",
        "M370",
        "specialized/marine_medium_with_thiosulfate.yaml",
        "79c5ff681040222dfb5bc23425de4118c5634b879b76526c45d547ff026b93e5",
        "91b9365ad1e767d4b6f584987599309b0ecf303af11914d26fdbcecbc046e500",
        14,
        0,
        2,
    ),
    Target(
        "J382",
        "M377",
        "bacterial/agc2_medium.yaml",
        "cb48a65f9288eae1658e86ce38d86bf12689d915e6c346f5157618a815e27a05",
        "10bd03b22973ec2bf2bf0dc7649a183f60c1fae249f34e8f119bd939b210ca17",
        1,
        2,
        2,
    ),
    Target(
        "J390",
        "M385",
        "bacterial/ji_medium.yaml",
        "098189d37902380603491a036976ea9395b0308e830c72359febbb6ad88f2e07",
        "3ed2a8c84fadbaaa526b69ddff09db2966f83c64fb61acb67a0bc14eb272254a",
        1,
        4,
        6,
    ),
    Target(
        "J400",
        "M396",
        "bacterial/desulfovibrio_piger_medium.yaml",
        "bc2cc5c57c739ff8e6e6996a7e701268dd132ee5ce9b988c48dbbfb0551b47e5",
        "89854f6905e9e8ebbacaea35d5b64bfa4b61ab13e193e0af4f328928f14a1e1f",
        13,
        3,
        2,
    ),
    Target(
        "J426",
        "M426",
        "bacterial/beer_medium.yaml",
        "f9416a6b25f469d9870b222a464fce5f5535103bfd74cfa385281a644f0ed960",
        "3a7dae0656b4e64dcb93213579dcbd13eb6c22bdd35ae59f79e1429e184fca5f",
        11,
        0,
        1,
    ),
    Target(
        "J477",
        "M478",
        "bacterial/methanosaeta_brevibacterium_medium.yaml",
        "99f1bd189978be792b60588a020bfab7de064496f2fc55bd3761551572767880",
        "902ebcef4106a448ef686dabac3ec239efe2af052b71ded0762dd8c0703c2de9",
        16,
        2,
        3,
    ),
    Target(
        "J490",
        "M491",
        "bacterial/mg50_medium.yaml",
        "0dff7546e5b4194e83a74d473f47e0bf255a8040986ff50725508575aa023112",
        "8e433ea15b24358f9a9275dbfa1e674abdfc4140637e4c181ef9d6e3cf064b3b",
        0,
        4,
        4,
    ),
    Target(
        "J522",
        "M523",
        "bacterial/xylanobacter_medium.yaml",
        "aeac469e10c3b31a1d0b064bd25a455e09a84f76d04893e1cc9f05494de14bb3",
        "8529a855553011bb64b91e756a8339474623d6a5aa08f6c547d7a09aeb19ceaf",
        0,
        1,
        1,
    ),
    Target(
        "J630",
        "M643",
        "archaea/thermoproteus_medium_c.yaml",
        "72f470525f0e66e4d782fdd291da1dd4d4eab4715ca87e1817e6287ce1d1ab67",
        "5b3f9a636dd5e6fb4fb10a95cc8db2e7849ebe1e6575da7a1576d7ad03dd46e6",
        0,
        1,
        1,
    ),
    Target(
        "J635",
        "M649",
        "bacterial/clostridium_bovis_medium.yaml",
        "7bce3be035f50be151866d364faccae6596c1b1088e62ade6cf9fc613a144f91",
        "38f9522f782d2f911e909c5756e21982a3d0a47d666984ddb94bd2b3d0be53d8",
        14,
        0,
        2,
    ),
    Target(
        "J703",
        "M725",
        "archaea/methanobacterium_medium_ii_with_formae.yaml",
        "20b445e5400583a1ff3cf05cb3afc526fe0429493ddd0e36bf381b6145a308bb",
        "ca1aac75833ea86163d62870a324fd565c03e43d0e20d07743b55396104c2d47",
        15,
        4,
        3,
    ),
    Target(
        "J738",
        "M763",
        "bacterial/bm_for_tepidanaerobacter_acetoxydans.yaml",
        "cbff92a4a1e81181a1d76babcff52424abb120e04d6fe8cc5b0a3b0232eec3c5",
        "f32527e89f4fd18d016cc568409f5c2e4f3f46cf73492177e96c09ad704830a4",
        9,
        7,
        2,
    ),
    Target(
        "J773",
        "M802",
        "bacterial/rumen_fluid_medium.yaml",
        "fe80ba90d6f5fc5cf01975ca391242deb944366b02f812365c958310bee5832c",
        "057139b758d577bf5c3573974de049a0a02ada85494df9e16c6d7cea7316c618",
        17,
        3,
        3,
    ),
    Target(
        "J792",
        "M824",
        "bacterial/lind_8a_medium.yaml",
        "c78dc02eaf42bd83a286d19815c349c7aee2326bdf2aeb6d89ccbe011fdcc51d",
        "8bdf79a4eed055554d28101bdc8c22234ba83b77327c864ed8939c02e97658b2",
        14,
        3,
        2,
    ),
    Target(
        "J806",
        "M841",
        "bacterial/JCM_J806_GS_MEDIUM.yaml",
        "ac7f294442315bca7be877ff65db609840f0f78624d32279c0c7efb792ca2fbb",
        "28b832df84ad3a4fe579454c5b3456a938adb5bcae8f989b2f6a6cd6e8b596a4",
        17,
        4,
        3,
    ),
    Target(
        "J816",
        "M851",
        "bacterial/diluted_asm_medium.yaml",
        "0136c16bb28efa4bb51675c2482d9153969dac94c9215e85064541079d883451",
        "64a49427fb224d7399cb64be24ddafeb3f39775545847d95143a654517e5bca6",
        0,
        1,
        1,
    ),
    Target(
        "J856",
        "M892",
        "bacterial/thermovenbulum_medium.yaml",
        "753f7e9c3c7483096510fa22d1f619c28a6bd8de572df600207298e4eb2f7b61",
        "b0ed88cfec2ffb8392acd4999f5b687ff3eb8f7840b4113e2c65bea36aed6a21",
        14,
        4,
        2,
    ),
    Target(
        "J939",
        "M985",
        "archaea/modified_halosimplex_medium.yaml",
        "4ccea7f06a2a20061eb1dd7684950f4498603604f9f9adc3cf579f7f2744ef60",
        "8a08fe0c67ae2b352e5c73d68a74fdfd4e64e4fe21ff1bd4a29d02e5f51fb2ae",
        8,
        1,
        3,
    ),
    Target(
        "J1145",
        "M1227",
        "bacterial/modified_roseospira_medium.yaml",
        "f0402260e5c7710c4606a53088664707ba64419fc730049848d446ec0cd03ae6",
        "6e4dfa6d564cf2ede26d6f393c9a0df8d45cbbae1d3d32d435a7d27aa7d78630",
        11,
        3,
        3,
    ),
    Target(
        "J1195",
        "M1280",
        "archaea/archaeoglobus_mcr_medium.yaml",
        "23bb61abf59933b3575d4ab4ecf685e5d59e9d8c727dba934624c2bf272e4fba",
        "c6e6f63456f9fe76c0a5b8531bfa12e31361a6b5691edd45367bb04a8e343dc0",
        1,
        1,
        1,
    ),
    Target(
        "J1224",
        "M1316",
        "bacterial/widdel_freshwater_medium_with_glycerin.yaml",
        "205ee3ebbc57604b03ac77d857cf3ef674bd69739e186489de19079ac217876b",
        "e55589665e8a6319a04216cf9d5b870d6e3b5084ede0b94f596297d1812163c6",
        10,
        7,
        3,
    ),
    Target(
        "J1225",
        "M1317",
        "bacterial/widdel_freshwater_medium_with_pyruvate.yaml",
        "626ba5693d1a4256b830ec10c1123c39c2f514392de7a16e698fa741d472caad",
        "b437ed3167c7109c74efc51bfd62c6b8dd7c545e00be486976caa2ed26cbc0ce",
        10,
        7,
        3,
    ),
)


def canonical_hash(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
        "utf-8"
    )
    return hashlib.sha256(encoded).hexdigest()


def raw_projection(payload: dict[str, Any]) -> dict[str, Any]:
    meta = payload.get("meta") or {}
    return {
        "gm_id": str(meta.get("gm") or "").rsplit("/", 1)[-1],
        "original_media_id": meta.get("original_media_id"),
        "components": payload.get("components") or [],
        "comments": payload.get("comments") or [],
    }


def descriptor_projection(row: dict[str, Any]) -> dict[str, Any]:
    """Project importer-owned fields while allowing later ontology enrichment."""
    projected = {
        key: copy.deepcopy(row[key])
        for key in ("preferred_term", "concentration", "notes", "preparation_notes")
        if key in row
    }
    if "composition" in row:
        projected["composition"] = [
            descriptor_projection(component) for component in row.get("composition") or []
        ]
    return projected


def output_projection(output: dict[str, Any]) -> dict[str, Any]:
    return {
        "ingredients": [descriptor_projection(row) for row in output.get("ingredients") or []],
        "solutions": [descriptor_projection(row) for row in output.get("solutions") or []],
        "preparation_steps": copy.deepcopy(output.get("preparation_steps") or []),
    }


def extract_payload(payload: dict[str, Any]) -> dict[str, Any]:
    importer = TogoImporter.__new__(TogoImporter)
    assembled = importer._extract_assembled_solutions(payload)
    if assembled:
        ingredients, solutions = [], assembled
    else:
        primary = importer._extract_primary_components(payload)
        if primary is None:
            ingredients, solutions = [], []
        else:
            ingredients, solutions = primary
    return {
        "ingredients": ingredients,
        "solutions": solutions,
        "preparation_steps": importer._extract_preparation_steps(payload),
    }


def _all_descriptors(output: dict[str, Any]) -> list[dict[str, Any]]:
    rows = list(output.get("ingredients") or []) + list(output.get("solutions") or [])
    nested = [
        component
        for solution in output.get("solutions") or []
        for component in solution.get("composition") or []
    ]
    return rows + nested


def validate_payload(payload: dict[str, Any], target: Target) -> dict[str, Any]:
    projection = raw_projection(payload)
    if projection["gm_id"] != target.togo_id:
        raise ValueError(
            f"{target.jcm_id}: TOGO id {projection['gm_id']!r}, expected {target.togo_id}"
        )
    expected_original = f"JCM_M{target.jcm_id.removeprefix('J')}"
    if projection["original_media_id"] != expected_original:
        raise ValueError(
            f"{target.jcm_id}: original_media_id "
            f"{projection['original_media_id']!r}, expected {expected_original!r}"
        )
    if canonical_hash(projection) != target.raw_sha256:
        raise ValueError(f"{target.jcm_id}: TOGO source projection drifted")

    output = extract_payload(payload)
    counts = (
        len(output["ingredients"]),
        len(output["solutions"]),
        len(output["preparation_steps"]),
    )
    expected_counts = (
        target.ingredient_count,
        target.solution_count,
        target.preparation_step_count,
    )
    if counts != expected_counts:
        raise ValueError(f"{target.jcm_id}: extracted counts {counts}, expected {expected_counts}")
    if not output["ingredients"] and not output["solutions"]:
        raise ValueError(f"{target.jcm_id}: source has no usable composition")
    if any(
        PLACEHOLDER.search(str(row.get("preferred_term") or "")) for row in _all_descriptors(output)
    ):
        raise ValueError(f"{target.jcm_id}: source extraction contains a placeholder")
    if any(not row.get("concentration") for row in output["solutions"]):
        raise ValueError(f"{target.jcm_id}: source extraction has an amountless stock")
    if canonical_hash(output_projection(output)) != target.output_sha256:
        raise ValueError(f"{target.jcm_id}: reviewed importer output drifted")
    return output


def media_term_id(doc: dict[str, Any]) -> str:
    return str((((doc.get("media_term") or {}).get("term") or {}).get("id")) or "")


def history_has_action(doc: dict[str, Any]) -> bool:
    return any(
        isinstance(row, dict) and row.get("action") == ACTION
        for row in doc.get("curation_history") or []
    )


def provenance_note(target: Target) -> str:
    return (
        f"Composition recovery source: https://togomedium.org/medium/{target.togo_id} "
        f"(TOGO snapshot of JCM medium {target.jcm_id})."
    )


def _assert_applied(doc: dict[str, Any], target: Target) -> None:
    if canonical_hash(output_projection(doc)) != target.output_sha256:
        raise ValueError(f"{target.jcm_id}: applied composition drifted")
    flags = doc.get("data_quality_flags") or []
    if any(flag in REMOVED_FLAGS for flag in flags):
        raise ValueError(f"{target.jcm_id}: obsolete quality flag returned")
    if provenance_note(target) not in str(doc.get("notes") or ""):
        raise ValueError(f"{target.jcm_id}: applied record lost recovery provenance")


def repair_document(
    doc: dict[str, Any], payload: dict[str, Any], target: Target
) -> tuple[dict[str, Any], bool]:
    output = validate_payload(payload, target)
    expected_term = f"mediadive.medium:{target.jcm_id}"
    if media_term_id(doc) != expected_term:
        raise ValueError(
            f"{target.jcm_id}: media term {media_term_id(doc)!r}, expected {expected_term!r}"
        )
    if history_has_action(doc):
        _assert_applied(doc, target)
        return doc, False

    current_ingredients = doc.get("ingredients") or []
    current_solutions = doc.get("solutions") or []
    if current_ingredients or current_solutions:
        raise ValueError(f"{target.jcm_id}: normalized record is no longer empty")
    flags = doc.get("data_quality_flags") or []
    if not isinstance(flags, list):
        raise ValueError(f"{target.jcm_id}: data_quality_flags is not a list")
    if "incomplete_composition" not in flags:
        raise ValueError(f"{target.jcm_id}: missing incomplete_composition precondition")

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = copy.deepcopy(output["ingredients"])
    if output["solutions"]:
        repaired["solutions"] = copy.deepcopy(output["solutions"])
    else:
        repaired.pop("solutions", None)
    repaired["preparation_steps"] = copy.deepcopy(output["preparation_steps"])

    kept_flags = [flag for flag in flags if flag not in REMOVED_FLAGS]
    if kept_flags:
        repaired["data_quality_flags"] = kept_flags
    else:
        repaired.pop("data_quality_flags", None)

    source_note = provenance_note(target)
    current_notes = str(repaired.get("notes") or "").rstrip()
    repaired["notes"] = f"{current_notes}\n{source_note}" if current_notes else source_note

    history = repaired.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.jcm_id}: curation_history is not a list")
    old_step_count = len(doc.get("preparation_steps") or [])
    history.append(
        {
            "timestamp": TIMESTAMP,
            "curator": "repair_jcm_missing_from_togo.py",
            "action": ACTION,
            "changes": (
                f"ingredients 0 -> {target.ingredient_count}; solutions 0 -> "
                f"{target.solution_count}; preparation_steps {old_step_count} -> "
                f"{target.preparation_step_count}; removed obsolete composition/source flags"
            ),
            "notes": (
                f"Recovered JCM {target.jcm_id} from source-equivalent TOGO "
                f"{target.togo_id}. Preserved final ingredients and stock-solution "
                "boundaries; did not flatten referenced media or stocks."
            ),
        }
    )
    _assert_applied(repaired, target)
    return repaired, True


def load_payloads(path: Path) -> dict[str, dict[str, Any]]:
    if not path.is_file():
        raise ValueError(f"missing fetched TOGO input: {path}")
    rows = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(rows, dict):
        rows = rows.get("data", [])
    if not isinstance(rows, list):
        raise ValueError(f"{path}: expected a JSON list or data list")
    wanted_ids = {target.togo_id for target in TARGETS}
    by_id = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        togo_id = str((row.get("meta") or {}).get("gm") or "").rsplit("/", 1)[-1]
        if togo_id in wanted_ids:
            if togo_id in by_id:
                raise ValueError(f"{path}: duplicate TOGO id {togo_id}")
            by_id[togo_id] = row
    return by_id


def _validate_inventory() -> None:
    for field in ("jcm_id", "togo_id", "relative_path"):
        values = [getattr(target, field) for target in TARGETS]
        if len(values) != len(set(values)):
            raise ValueError(f"duplicate target {field}")
    if len(TARGETS) != 28:
        raise ValueError(f"expected 28 reviewed targets, found {len(TARGETS)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-file", type=Path, default=RAW_FILE)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    _validate_inventory()
    payloads = load_payloads(args.raw_file)
    pending = []
    for target in TARGETS:
        payload = payloads.get(target.togo_id)
        if payload is None:
            raise ValueError(f"{args.raw_file}: missing TOGO {target.togo_id}")
        path = args.normalized_dir / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: expected a YAML mapping")
        repaired, changed = repair_document(doc, payload, target)
        pending.append((path, repaired, changed, target))
        print(
            f"{'fix' if changed else 'skip':4s}  "
            f"{path.relative_to(REPO) if path.is_relative_to(REPO) else path}: "
            f"{target.jcm_id} <- {target.togo_id}"
        )

    changed_count = sum(changed for _, _, changed, _ in pending)
    if args.apply:
        for path, repaired, changed, _ in pending:
            if changed:
                write_record(path, repaired)
    verb = "updated" if args.apply else "would update"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
