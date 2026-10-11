#!/usr/bin/env python3
"""Restore source batch inputs and exclusive percent supplements in five records."""

from __future__ import annotations

import argparse
import copy
import datetime
import io
import json
import subprocess
from pathlib import Path

from fetch_medium_concentration_sources import API, read_capture
from fetch_solution_concentration_sources import load_yaml
from repair_komodo12_extraction_evidence import MAPPING_URL, TableRows
from repair_mediadive_stock_concentration_evidence import cell, require, sha
from review_medium_concentration_evidence import json_excerpt
from review_solution_concentration_evidence import field_name, render

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
ACTION = "CORRECTED_DSMZ618_956_BATCH_INPUTS_AND_PERCENT_ALTERNATIVES"
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{}.pdf"
ACCESSED = "2026-10-07"
MAPPING_SHA = "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
SOURCES = {
    "618": {
        "title": "TWEEN 80A MEDIUM",
        "pdf_sha": "cd503969dc2f910a9b50c270952adf4c00eaffb09762b02a50e60c23555d8f20",
        "api_sha": "4411ab3e1786900babbc16b273fca178ad608b211bcd879a8ba82bcb90553012",
        "rows": ["Casitone (Difco) 5.0 g", "Yeast extract (Difco) 3.0 g", "MgSO4 x 7 H2O 2.0 g"],
        "water": "Distilled water 1000.0 ml",
        "preparation": "For solid media add 15.0 g agar. Dissolve ingredients and adjust the pH to 7.2. Sterilize by autoclaving. After sterilization add sterile Tween 80 to a final concentration of 1.0%.",
        "base_preparation": "For solid media add 15.0 g agar. Dissolve ingredients and adjust the pH to 7.2. Sterilize by autoclaving.",
        "labels": ["Casitone", "Yeast extract", "MgSO4 x 7 H2O", "Agar"],
        "amounts": ["5.0", "3.0", "2.0", "15.0"],
    },
    "956": {
        "title": "MEDIUM FOR DSM 14457 AND 14458",
        "pdf_sha": "156fe7f9a826c658bf690c9c892ba7d137848d397f55cf93568c4c3145374f39",
        "api_sha": "f0469cc9f78282a45677521479b2d424c087263db5c6e4f9a19200bba6ec4469",
        "rows": [
            "KH2PO4 2.000 g",
            "(NH4)2SO4 2.000 g",
            "MgSO4 x 7 H2O 0.125 g",
            "NaCl 0.500 g",
            "FeSO4 x 7 H2O 0.002 g",
        ],
        "water": "Distilled water 1000.000 ml",
        "preparation": "pH 7.2. To the sterilised medium add sterile methanol (to a final concentration of 0.5%) or methylamine (to a final concentration of 0.3%).",
        "base_preparation": "pH 7.2. Prepare and sterilise the base before adding the selected supplement; the source does not specify a sterilisation method, temperature, or duration.",
        "labels": ["KH2PO4", "(NH4)2SO4", "MgSO4 x 7 H2O", "NaCl", "FeSO4 x 7 H2O"],
        "amounts": ["2.000", "2.000", "0.125", "0.500", "0.002"],
    },
}
PREFIX = "data/normalized_yaml/bacterial/"
TARGETS = {
    "d618": (
        "tween_80a_medium",
        "CultureMech:001748",
        "618",
        "mediadive",
        "4abfbb6779375a462e0cdad101a6fa193ff4a5e62795f2be5d05698ea7f4b2c2",
        "b02e9b6f10d90b2f8bceecb5d14d2531a8f67329614fe64002fa6d8213f49717",
    ),
    "k618": (
        "KOMODO_618_TWEEN_80A_medium",
        "CultureMech:006112",
        "618",
        "komodo",
        "ad179f4688d8329d58b963e2fe24409460da33df41f6d5ee5f602f59191dc1af",
        "d6039ae77e620431644ce732fbc48bd2043421ff647105dd369bb873baecd480",
    ),
    "d956": (
        "medium_for_dsm_14457_and_14458",
        "CultureMech:002134",
        "956",
        "mediadive",
        "0cae3503c5ac2499a3274dd238689062eef5fbc075620d0f4aef39f374d3d8ed",
        "1aeb8af333aea58b86c4ffae8ea773ee1eb085a58453979f86a43ba5a586c183",
    ),
    "k956": (
        "KOMODO_956_MEDIUM_FOR_DSM_14457_AND_14458",
        "CultureMech:006900",
        "956",
        "komodo",
        "acc3066a55b33b854b0ac536d6970241f4e901e764112dc8623210893f9f588e",
        "954cde0b0bc2745a3a5aa8c13f8291c4b683dc169db07e1dc086847119d31874",
    ),
    "m956": (
        "medium_for_dsm_14457_and_14458_replace_methanol_with_methylamine",
        "CultureMech:006899",
        "956",
        "komodo",
        "05f2582a4ab2937eb154134dd24e07243df719928771051329af6d2e0a4fd590",
        "7da842f5a1669a06017745187195dcfcf72ddff305e2f0ae465d2ef0b15069ce",
    ),
}
WITHDRAWAL = "The former final-medium concentration is withdrawn. The starting water and subsequent percent supplement do not establish the final volume; the source batch mass is preserved in notes, not converted to g/L."
BASE_NOTES = "Curator-described preparation stage, not a separately accessioned stock. Composition records source batch inputs. The 1000 ml water is an input, not an explicit prepared-base or final-medium volume; no absolute base dose is inferred."
PERCENT_NOTE = "The percentage basis, supplement dose volume, and final receiving volume are unspecified. No mass concentration, density, or percent unit is inferred."
FAMILY_NOTE = "DSMZ 956 defines mutually exclusive methanol and methylamine alternatives. This record retains their common base and both options in variants; choose exactly one, not both. The unsupplemented base is not asserted to support growth. The methylamine-specific record is CultureMech:006899."


def path_for(key):
    return PREFIX + TARGETS[key][0] + ".yaml"


def expected_text(mid):
    spec = SOURCES[mid]
    return " ".join(
        [
            "\u00a9 2007 DSMZ GmbH - All rights reserved",
            f"{mid}. {spec['title']}",
            *spec["rows"],
            spec["water"],
            spec["preparation"],
        ]
    )


def inspect_sources(mid, source):
    spec = SOURCES[mid]
    require(sha(source["pdf"]) == spec["pdf_sha"], "Original PDF hash drift")
    require(
        source["pages"] == 1 and " ".join(source["text"].split()) == expected_text(mid),
        "Original PDF identity, amount or preparation drift",
    )
    raw, meta = source["raw"], source["meta"]
    require(sha(raw.encode()) == meta["sha256"] == spec["api_sha"], "API capture hash drift")
    require(
        meta["http_status"] == 200 and meta["url"] == meta["response_url"] == API + mid,
        "API source identity drift",
    )
    data = json.loads(raw)["data"]
    require(
        data["medium"]["id"] == int(mid)
        and data["medium"]["name"] == spec["title"]
        and data["medium"]["source"] == "DSMZ"
        and data["medium"]["link"] == PDF.format(mid),
        "API original-recipe linkage drift",
    )
    require(
        len(data["solutions"]) == 1
        and data["solutions"][0]["steps"] == [{"step": spec["preparation"]}],
        "API preparation drift",
    )
    main = data["solutions"][0]
    labels = (
        spec["labels"][:3] + ["Distilled water", "Agar", "Tween 80"]
        if mid == "618"
        else spec["labels"] + ["Distilled water", "Methanol", "Methylamine"]
    )
    require(
        main["id"] == (1326 if mid == "618" else 1973)
        and main["name"] == "Main sol. " + mid
        and main["volume"] == 1000
        and [r["compound"] for r in main["recipe"]] == labels,
        "API base inventory drift",
    )
    water = main["recipe"][3 if mid == "618" else 5]
    require(
        water
        == {
            "recipe_order": 4 if mid == "618" else 6,
            "compound": "Distilled water",
            "compound_id": 4,
            "amount": 1000,
            "unit": "ml",
            "optional": 0,
        },
        "API water identity or batch amount drift",
    )
    return data


def mapping_row(key, raw):
    require(sha(raw.encode()) == MAPPING_SHA, "KOMODO mapping hash drift")
    _, _, mid, provider, _, _ = TARGETS[key]
    require(provider == "komodo", "Wrong mapping provider")
    accession = "956_replace_Methanol_with_Methylamine" if key == "m956" else mid
    name = SOURCES[mid]["title"] + ("_replace_Methanol_with_Methylamine" if key == "m956" else "")
    if mid == "618":
        name = "TWEEN 80A medium"
    parser = TableRows()
    parser.feed(raw)
    parser.close()
    require(parser.row is None and parser.cell is None, "Unclosed mapping table")
    rows = [r for r in parser.rows if r["cells"] and r["cells"][0] == accession]
    url = PDF.format(mid).replace("https:", "http:")
    expected = {
        "cells": [
            accession,
            name,
            "7.2",
            "true" if mid == "618" else "false",
            "false",
            "false",
            url,
        ],
        "links": [
            {
                "href": "/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
                + accession
            },
            {"href": url},
        ],
    }
    require(rows == [expected], "KOMODO source ID, formulation or original PDF link drift")
    return expected


def read_sources(folder):
    from pypdf import PdfReader

    result = {}
    for mid in SOURCES:
        pdf = (folder / f"DSMZ_Medium{mid}_scope.pdf").read_bytes()
        reader = PdfReader(io.BytesIO(pdf))
        raw, meta = read_capture(folder / "sources", mid)
        result[mid] = {
            "pdf": pdf,
            "pages": len(reader.pages),
            "text": "\n".join(p.extract_text() for p in reader.pages),
            "raw": raw,
            "meta": meta,
        }
        inspect_sources(mid, result[mid])
    result["mapping"] = (folder / "komodo-media-list.html").read_text()
    for key in ("k618", "k956", "m956"):
        mapping_row(key, result["mapping"])
    return result


def build(doc, key, sources, timestamp):
    _, identifier, mid, provider, _, semantic_sha = TARGETS[key]
    spec, source = SOURCES[mid], sources[mid]
    inspect_sources(mid, source)
    mapping = mapping_row(key, sources["mapping"]) if provider == "komodo" else None
    semantic = json.dumps(doc, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    require(sha(semantic.encode()) == semantic_sha, "Unreviewed local formulation drift")
    require(
        doc["id"] == identifier and not list(validate_recipe(doc, target_class="MediaRecipe")),
        "Baseline identity/schema failure",
    )
    reference = PDF.format(mid)
    context = f"Original DSMZ {mid}, PDF page 1; capture SHA256={spec['pdf_sha']}; accessed_on={ACCESSED}. Display whitespace normalized; source quantities and chemical forms checked visually. Ontology annotations are preserved where their ingredient remains, not independently re-grounded."
    after = copy.deepcopy(doc)
    nodes = after["ingredients"]
    base_count = len(spec["labels"])
    require(
        [n["preferred_term"] for n in nodes[:base_count]] == spec["labels"],
        "Ingredient order drift",
    )
    claims, resolutions = [], []

    def claim(
        pointer,
        old_pointer,
        old,
        new,
        status,
        snippet,
        explanation,
        evidence_pointer,
        ref=reference,
    ):
        entry = {
            "pointer": pointer,
            "old_pointer": old_pointer,
            "field": field_name(pointer),
            "old_field": field_name(old_pointer) if old_pointer else None,
            "old": copy.deepcopy(old),
            "new": copy.deepcopy(new),
            "status": status,
            "reference": ref,
            "snippet": snippet,
            "locator": (
                "PDF page 1, ingredient table/preparation"
                if ref == reference
                else "KOMODO table row " + mapping["cells"][0]
            ),
            "explanation": explanation + " " + context,
            "evidence_pointer": evidence_pointer,
        }
        claims.append(entry)
        return entry

    def evidence(entry):
        return {
            "reference": entry["reference"],
            "supports": "SUPPORT",
            "snippet": entry["snippet"],
            "explanation": entry["explanation"],
        }

    step_pointer = ["data", "solutions", 0, "steps", 0]
    step_quote = json_excerpt(source["raw"], step_pointer)
    for index, (node, amount) in enumerate(zip(nodes[:base_count], spec["amounts"], strict=True)):
        pointer = ["solutions", 0, "composition", index]
        old = node.pop("concentration")
        quote = (
            spec["rows"][index] if index < len(spec["rows"]) else "For solid media add 15.0 g agar."
        )
        prior_notes = node.get("notes", "")
        note = f"Source batch input: {amount} g; {quote} The recipe starts with 1000 ml distilled water before supplementation. No prepared-base or final-medium mass concentration is asserted."
        node["notes"] = (prior_notes + " " + note).strip()
        entry = claim(
            pointer + ["concentration"],
            ["ingredients", index, "concentration"],
            old,
            None,
            "remove_unsupported",
            quote,
            f"Relocates ingredients[{index}] to {field_name(pointer)} and withdraws its g/L encoding. {field_name(pointer + ['notes'])} preserves the original batch amount. {WITHDRAWAL} Additional exact source water row: {spec['water']}. Agar is retained for the existing solid record only; Difco product attributes are retained in the corresponding source notes.",
            pointer,
        )
        prior = node.get("evidence", [])
        if prior:
            require(
                len(prior) == 1
                and prior[0]["reference"] == API + mid
                and prior[0]["supports"] == "SUPPORT",
                "Unreviewed prior evidence",
            )
            prior[0][
                "explanation"
            ] = f"Historical provider-declared nominal rate only; this entry no longer supports a final-medium concentration. Scope correction to {field_name(pointer + ['notes'])}: {WITHDRAWAL} Original PDF batch excerpt: {quote}. Exact dataset preparation excerpt: {step_quote}. The earlier dataset row/snippet is preserved, not promoted over the original recipe. Response SHA256={source['meta']['sha256']}; retrieved {source['meta']['accessed_at']}."
            resolutions.append(
                {
                    "from_pointer": ["ingredients", index],
                    "to_pointer": pointer,
                    "reference": API + mid,
                    "old_concentration": old,
                    "disposition": "withdrawn",
                    "new_field": field_name(pointer + ["notes"]),
                    "source_pointer": step_pointer,
                    "source_snippet": step_quote,
                    "reason": WITHDRAWAL,
                }
            )
        node.setdefault("evidence", []).append(evidence(entry))

    water_pointer = ["solutions", 0, "composition", base_count]
    water = {
        "preferred_term": "Distilled water",
        "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
        "concentration": {"value": "1", "unit": "L"},
        "notes": "Starting-water batch amount: 1000 ml / 1000 ml per L = 1 L. Not a final-volume make-up instruction or a mass concentration.",
    }
    water_entry = claim(
        water_pointer,
        None,
        None,
        water,
        "add",
        spec["water"],
        f"Adds the source's omitted starting-water input at {field_name(water_pointer)}. The volume is a batch input only; the dataset identifies distilled water as compound 4.",
        water_pointer,
    )
    water["evidence"] = [evidence(water_entry)]
    after["solutions"] = [
        {
            "preferred_term": f"DSMZ {mid} base preparation",
            "source": reference,
            "notes": BASE_NOTES,
            "composition": nodes[:base_count] + [water],
            "preparation_notes": spec["base_preparation"],
        }
    ]
    after["ingredients"] = []
    root_claims = [
        claim(
            ["solutions", 0, "preparation_notes"],
            None,
            None,
            spec["base_preparation"],
            "add_stage",
            spec["preparation"],
            "Separates the pre-supplement base in solutions[0]; its name is a curator stage description, not a new source accession. Composition holds input masses in notes and the explicit water input. Neither base concentration nor recovered/final volume is asserted. "
            + BASE_NOTES,
            [],
        )
    ]

    def supplement(node, old_index, percent, selected=False):
        old = node.pop("concentration")
        node["notes"] = (
            f"After sterilisation add sterile {node['preferred_term']} to the source-stated final concentration of {percent}%. {PERCENT_NOTE}"
        )
        if selected:
            node[
                "notes"
            ] += " This source-specific variant selects methylamine and excludes methanol."
        pointer = ["ingredients", 0]
        entry = claim(
            pointer + ["concentration"],
            ["ingredients", old_index, "concentration"],
            old,
            None,
            "remove_unsupported",
            spec["preparation"],
            f"Removes the unsupported g/L encoding, relocates the supplement to {field_name(pointer)}, and preserves the source percent in {field_name(pointer + ['notes'])}. "
            + PERCENT_NOTE,
            pointer,
        )
        node["evidence"] = [evidence(entry)]
        after["ingredients"] = [node]

    if mid == "618":
        supplement(nodes[4], 4, "1.0")
    elif key == "m956":
        supplement(nodes[6], 6, "0.3", selected=True)
        root_claims.append(
            claim(
                ["ingredients"],
                ["ingredients", 5],
                doc["ingredients"][5],
                None,
                "remove_alternative",
                mapping["cells"][1],
                "The exact KOMODO source accession explicitly replaces methanol with methylamine. Remove methanol from this branch; the original DSMZ recipe independently states the supplements are alternatives. No methanol or co-supplementation is retained. The removed node, including its historical ontology annotations, is preserved in the append-only change event.",
                [],
                MAPPING_URL,
            )
        )
        parent = {
            "path": path_for("d956"),
            "id": TARGETS["d956"][1],
            "name": "medium_for_dsm_14457_and_14458",
            "relationship": "SUPPLEMENTED_VARIANT",
            "notes": "Selects the methylamine option of DSMZ 956's common base; excludes methanol. Percentage basis is unspecified. The parent describes both exclusive options, not a methanol-plus-methylamine mixture.",
        }
        after["parent_media"] = parent
        after["variant_relationship"] = "SUPPLEMENTED_VARIANT"
        after["variant_modifications"] = [
            "Select the methylamine alternative (source final concentration 0.3%, basis unspecified); do not add methanol."
        ]
        root_claims.append(
            claim(
                ["parent_media"],
                None,
                None,
                parent,
                "add_variant_link",
                spec["preparation"],
                "Links the existing methylamine-specific ID to the shared-base family, with variant_relationship and variant_modifications describing the selected option. The original recipe states the alternative; the separately verified KOMODO accession selects it. No new record or ID is created.",
                [],
            )
        )
    else:
        after["variants"] = []
        for offset, percent in enumerate(("0.5", "0.3")):
            index = 5 + offset
            label = nodes[index]["preferred_term"]
            other = "methylamine" if offset == 0 else "methanol"
            variant = {
                "name": label + " alternative",
                "relationship": "SUPPLEMENTED_VARIANT",
                "description": "One of two mutually exclusive source-supported supplements to the common base; not an assertion that the unsupplemented base supports growth.",
                "modifications": [
                    f"After sterilisation add sterile {label.lower()} to a final concentration of {percent}% (percentage basis unspecified).",
                    f"Use this alternative instead of {other}; do not add both.",
                ],
                "purpose": "Select one supplementation branch of the original DSMZ 956 recipe.",
            }
            if offset == 1:
                variant[
                    "description"
                ] += " The separately accessioned methylamine branch is CultureMech:006899."
            pointer = ["variants", offset]
            entry = claim(
                pointer,
                ["ingredients", index],
                doc["ingredients"][index],
                variant,
                "move_to_variant",
                spec["preparation"],
                f"Moves {label} from the apparent combined ingredient list to {field_name(pointer)}. Withdraws the unsupported {doc['ingredients'][index]['concentration']['value']} g/L encoding. The source percent has no defined basis, so no numeric percent or mass concentration slot is added. The removed node's ontology annotations remain in the append-only change event, not as a new grounding claim.",
                pointer,
            )
            variant["evidence"] = [evidence(entry)]
            after["variants"].append(variant)
        after["notes"] += " " + FAMILY_NOTE
        root_claims.append(
            claim(
                ["notes"],
                ["notes"],
                doc["notes"],
                after["notes"],
                "correct_scope",
                spec["preparation"],
                "Clarifies the source OR relationship, shared-base scope, and existing methylamine record; neither branch is silently selected as a default.",
                [],
            )
        )
        if key == "d956":
            child = {
                "path": path_for("m956"),
                "id": TARGETS["m956"][1],
                "name": TARGETS["m956"][0],
                "relationship": "SUPPLEMENTED_VARIANT",
                "notes": "Existing source-specific record for the methylamine option of this common base; final 0.3% has unspecified basis and methanol is excluded.",
            }
            after["variant_children"].append(child)
            root_claims.append(
                claim(
                    ["variant_children", 1],
                    None,
                    None,
                    child,
                    "add_variant_link",
                    spec["preparation"],
                    "Reuses the existing methylamine-specific record rather than creating a duplicate parent or assigning a new ID. The original recipe and separately verified KOMODO source row support the selected branch.",
                    [],
                )
            )

    if "preparation_steps" not in after:
        description = (
            spec["preparation"]
            if key != "m956"
            else "pH 7.2. After sterilising the base, add sterile methylamine to a final concentration of 0.3% (percentage basis unspecified). Do not add methanol in this variant."
        )
        after["preparation_steps"] = [
            {"step_number": 1, "action": "MIX", "description": description}
        ]
        root_claims.append(
            claim(
                ["preparation_steps"],
                None,
                None,
                after["preparation_steps"],
                "add_stage",
                spec["preparation"],
                "Adds the source preparation context; no unreported sterilisation parameters are inferred. The KOMODO methylamine accession selects that branch where applicable.",
                [],
            )
        )
    after["evidence"] = [
        {
            "reference": reference,
            "supports": "SUPPORT",
            "snippet": spec["preparation"],
            "explanation": " ".join(
                c["explanation"] for c in root_claims if c["reference"] == reference
            )
            + " Fields: "
            + ", ".join(c["field"] for c in root_claims if c["reference"] == reference),
        }
    ]
    after.setdefault("references", []).append(
        {
            "reference": reference,
            "title": f"DSMZ {mid}: {spec['title']}",
            "notes": f"source_type=culture_collection_page; discovery_mode=existing_record_reference; source_organization=DSMZ; accessed_on={ACCESSED}; capture_sha256={spec['pdf_sha']}; locator=complete one-page ingredient table and preparation. Individual authors and recipe publication year not supplied; the 2007 copyright notice is not treated as a publication year. Percent basis and final volume are not specified.",
        }
    )
    if mapping:
        mapping_quote = " ".join(mapping["cells"])
        mapping_explanation = (
            f"Exact source-identity linkage for media_term and this recipe's ingredients, solutions, preparation and variant selection. KOMODO accession {mapping['cells'][0]} links the original DSMZ {mid} PDF; quantities come from that inspected PDF, not another curated record. Capture SHA256={MAPPING_SHA}; accessed_on={ACCESSED}; locator=HTML table row with exact first cell {mapping['cells'][0]}. Visible cell whitespace normalized. No phenotype is inferred from table flags. "
            + " ".join(c["explanation"] for c in root_claims if c["reference"] == MAPPING_URL)
        )
        after["evidence"].append(
            {
                "reference": MAPPING_URL,
                "supports": "SUPPORT",
                "snippet": mapping_quote,
                "explanation": mapping_explanation,
            }
        )
        after["references"].append(
            {
                "reference": MAPPING_URL,
                "title": "KOMODO - the Known Media Database",
                "notes": f"source_type=dataset; discovery_mode=existing_record_reference; source_organization=KOMODO; accessed_on={ACCESSED}; capture_sha256={MAPPING_SHA}; locator=exact accession {mapping['cells'][0]}. Individual authors and publication year not established. Supports original-recipe linkage and named variant, not numeric concentrations.",
            }
        )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        source=reference,
        timestamp=timestamp,
        notes="Original PDF, preparation and exact source accession verified. Restored batch-input scope; withdrew unsupported final mass concentrations and preserved source amounts/percentages without guessing bases or final volume. Existing source-specific methylamine record reused. Prior history, IDs and unrelated metadata preserved; source-specific removed nodes remain explicit in this change event.",
        changes="; ".join(
            f"{c['old_field']} -> {c['field']}: {json.dumps(c['old'], sort_keys=True)} -> {json.dumps(c['new'], sort_keys=True)} ({c['status']})"
            for c in claims
        ),
    )
    require(not list(validate_recipe(after, target_class="MediaRecipe")), "Proposed schema failure")
    return after, claims, resolutions


def process(root, source_dir, plan_path, mode):
    require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    tracked = set(
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root)
        .decode()
        .split("\0")
    )
    sources = read_sources(source_dir)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root).decode().strip()
    if mode == "preview":
        require(not plan_path.exists(), "Refuse to overwrite a reviewed plan")
        plan = {
            "version": 1,
            "action": ACTION,
            "commit": commit,
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
    else:
        plan = json.loads(plan_path.read_text())
        require(
            plan["version"] == 1
            and plan["action"] == ACTION
            and [r["key"] for r in plan["records"]] == list(TARGETS),
            "Wrong plan",
        )
    items, writes = [], []
    for index, (key, spec) in enumerate(TARGETS.items()):
        target = path_for(key)
        path = root / target
        require(target in tracked and not path.is_symlink(), "Non-exact or symlink target")
        current = path.read_bytes()
        before = current if mode == "preview" else plan["records"][index]["before_text"].encode()
        require(sha(before) == spec[4], "Unreviewed baseline hash drift")
        after, claims, resolutions = build(load_yaml(before), key, sources, plan["created_at"])
        output = render(before.decode(), after)
        item = {
            "key": key,
            "path": target,
            "id": spec[1],
            "medium_id": spec[2],
            "action": ACTION,
            "before_text": before.decode(),
            "before_sha256": sha(before),
            "after_text": output.decode(),
            "after_sha256": sha(output),
            "source_sha256": SOURCES[spec[2]]["api_sha"],
            "pdf_sha256": SOURCES[spec[2]]["pdf_sha"],
            "mapping_sha256": MAPPING_SHA if spec[3] == "komodo" else None,
            "claims": claims,
            "claim_resolutions": resolutions,
        }
        require(current in (before, output), "Concurrent edit")
        items.append(item)
        writes.append((path, current, output))
    if mode == "preview":
        plan["records"] = items
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        require(items == plan["records"], "Plan/source/decision drift")
        require(
            all(p.read_bytes() == current for p, current, _ in writes),
            "Concurrent edit before write",
        )
        if mode == "apply":
            for path, current, output in writes:
                require(path.read_bytes() == current, "Concurrent edit during write")
                if current != output:
                    path.write_bytes(output)
        require(
            all(p.read_bytes() == output for p, _, output in writes),
            "Repair not applied or result differs",
        )
    return plan, {
        "mode": mode,
        "records": len(items),
        "changed": (
            sum(current != output for _, current, output in writes) if mode == "apply" else 0
        ),
        "already_applied": sum(current == output for _, current, output in writes),
        "scoped_claims": sum(len(r["claims"]) for r in items),
    }


def report(folder, plan, applied):
    for item in plan["records"]:
        marker = "Follow-up target" if item["key"].startswith("d") else "Record"
        lines = [
            "# Original-Source Percent Supplement Repair",
            "",
            f"- {marker}: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: `{plan['commit']}`",
            f"- Before SHA256: `{item['before_sha256']}`",
            f"- Result SHA256: `{item['after_sha256']}`",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Existing DSMZ cohort reports remain historical and are explicitly superseded. The three KOMODO records have their own exact-path reports. Unknown percentage bases and final volumes remain unresolved, not guessed. See README.md and validation.json for verification and scope.",
            "",
            "| Field | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for claim in item["claims"]:
            lines.append(
                "| "
                + " | ".join(
                    cell(claim[k])
                    for k in (
                        "field",
                        "old",
                        "new",
                        "status",
                        "reference",
                        "snippet",
                        "locator",
                        "explanation",
                    )
                )
                + " |"
            )
        dest = folder / "records" / (item["path"].removeprefix("data/normalized_yaml/") + ".md")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    modes.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.source_dir, args.plan, mode)
    if args.reports:
        report(args.reports, plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
