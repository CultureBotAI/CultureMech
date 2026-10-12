#!/usr/bin/env python3
"""Restore medium 265 preparation stages with source-pinned, preview-first edits."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from pathlib import Path

import review_solution_concentration_evidence as runner
from fetch_medium_concentration_sources import read_capture as read_medium
from fetch_solution_concentration_sources import read_capture as read_solution
from inventory_komodo_concentration_sources import MAPPING_URL, read_mapping
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz265-preparations"
ACTION = "RESTORED_DSMZ265_STOCK_STAGES_AND_ORIGINAL_SOURCE_DOSES"
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium265.pdf"
MEDIUM = "https://mediadive.dsmz.de/rest/medium/265"
SOLUTION = "https://mediadive.dsmz.de/rest/solution/531"
HASHES = {
    PDF: "904a0973cffadca97f2da8c6b8cd2a89f5f842d53bdb98212d27aa86741ab173",
    MEDIUM: "f2c57ed580e65928e82bad4eb0a6d48371d2c6fc60b0bb2f2369754570306dea",
    SOLUTION: "3f2e0a5b8cfb664ba312b538b1f8e9b06c8d172ed4a4405c47d944b6297e70e0",
}
TEXT_HASH = "9a228b1b3720116ac4de25b0f9bfb78ac8cc3b39600e3fe8ba62c4ee138f8790"
MAPPING_META = {
    "reference": MAPPING_URL,
    "http_status": 200,
    "accessed_at": "2026-10-07T13:01:23.350274+00:00",
    "sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a",
}
TARGETS = {
    "dsmz": {
        "path": "data/normalized_yaml/archaea/thermofilum_pendens_medium.yaml",
        "id": "CultureMech:001364",
        "before_sha256": "2ea7604ed61df938212f42917ded9f9afa28cf451a74ec3a388b2c2a004fe918",
        "target_class": "MediaRecipe",
    },
    "komodo": {
        "path": "data/normalized_yaml/archaea/KOMODO_265_THERMOFILUM_PENDENS_medium.yaml",
        "id": "CultureMech:004668",
        "before_sha256": "fbe47f63dc43877d88a7559138ac4cdf3db62db9a82076ff7700388f71cf01f7",
        "target_class": "MediaRecipe",
    },
    "solution": {
        "path": "data/normalized_yaml/bacterial/mediadive_531_Main_sol_265.yaml",
        "id": "CultureMech:014231",
        "before_sha256": "7e9ccb218390e0b60038448c2ba75d23f533bac1666e672e6199d7d0c543f6a7",
        "target_class": "SolutionRecipe",
    },
}
SALTS = [
    "(NH4)2SO4",
    "KH2PO4",
    "MgSO4 x 7 H2O",
    "CaCl2 x 2 H2O",
    "FeCl3 x 6 H2O",
    "MnCl2 x 4 H2O",
    "Na2B4O7 x 10 H2O",
    "ZnSO4 x 7 H2O",
    "CuCl2 x 2 H2O",
    "Na2MoO4 x 2 H2O",
    "VOSO4 x 2 H2O",
    "CoSO4 x 7 H2O",
]
SUPPLEMENTS = ["Yeast extract", "Sucrose", "Sulfur", "Polar lipid fraction", "Na2S x 9 H2O"]
PREPARATION = "prepared separately and added to the autoclaved mineral salt solution:"
STOCKS = [
    (
        "Yeast extract",
        "10",
        "0.02",
        "Yeast extract (20 \nml of 10% w/v solution)-boiled for few minutes, not autoclaved",
    ),
    ("Sucrose", "10", "0.02", "sucrose (20 ml of 10% \nw/v solution)-filter-sterilized"),
    (
        "Na2S x 9 H2O",
        "3",
        "0.01",
        "Na2S x 9 H2O (10 ml of 3% w/v \nsolution)-autoclaved under nitrogen atmosphere.",
    ),
]
SULFUR_QUOTE = "sulfur (10 g)-sterilized by steaming for 3 h on each of \nthree successive days"
LIPID_QUOTE = "aqueous suspension 6 - 12.00 ml"


def read_sources(medium_cache, solution_cache, mapping, pdf, text):
    sources = {}
    for ref, reader, cache, sid in (
        (MEDIUM, read_medium, medium_cache, "265"),
        (SOLUTION, read_solution, solution_cache, 531),
    ):
        raw, meta = reader(cache, sid)
        sources[ref] = {"raw": raw, "metadata": meta}
    runner.require(runner.sha(pdf.read_bytes()) == HASHES[PDF], "PDF changed")
    raw = text.read_text()
    runner.require(runner.sha(raw.encode()) == TEXT_HASH, "PDF extraction changed")
    sources[PDF] = {
        "raw": raw,
        "metadata": {
            "reference": PDF,
            "sha256": HASHES[PDF],
            "text_sha256": TEXT_HASH,
            "accessed_on": "2026-10-07",
            "pages": 1,
            "inspection": "Complete page visually inspected; pypdf text checked against rendered PDF.",
        },
    }
    sources["mapping"] = read_mapping(mapping, MAPPING_META)["265"]
    sources["mapping_metadata"] = copy.deepcopy(MAPPING_META)
    check_sources(sources)
    return sources


def check_sources(sources):
    for ref in (MEDIUM, SOLUTION):
        runner.require(
            runner.sha(sources[ref]["raw"].encode())
            == HASHES[ref]
            == sources[ref]["metadata"]["sha256"],
            "API source drift",
        )
    text = sources[PDF]["raw"]
    runner.require(runner.sha(text.encode()) == TEXT_HASH, "PDF text drift")
    runner.require(sources[PDF]["metadata"]["sha256"] == HASHES[PDF], "PDF identity drift")
    for quote in [PREPARATION, SULFUR_QUOTE, LIPID_QUOTE, "Distilled water 1000.00 ml"] + [
        s[3] for s in STOCKS
    ]:
        runner.require(quote in text, "Inexact original-source quotation")
    medium = json.loads(sources[MEDIUM]["raw"])["data"]
    solution = json.loads(sources[SOLUTION]["raw"])["data"]
    runner.require(
        medium["medium"]["id"] == 265 and medium["medium"]["link"] == PDF, "Medium identity drift"
    )
    runner.require(len(medium["solutions"]) == 1, "Source topology drift")
    for data in (medium["solutions"][0], solution):
        runner.require(
            data["id"] == 531 and data["name"] == "Main sol. 265" and data["volume"] == 1000,
            "Solution identity/basis drift",
        )
        runner.require(
            [r["compound"] for r in data["recipe"]] == SALTS + ["Distilled water"] + SUPPLEMENTS,
            "Source ingredient drift",
        )
        runner.require(
            data["recipe"][13]["amount"] == 20 and data["recipe"][13]["unit"] == "mg/l",
            "Yeast conflict drift",
        )
        runner.require(PREPARATION in data["steps"][1]["step"], "Preparation drift")
    mapping = sources["mapping"]
    runner.require(
        mapping["medium_id"] == "265"
        and mapping["original_recipe"] == PDF
        and mapping["cells"][0] == "265",
        "KOMODO identity drift",
    )


def build(before, key, sources, timestamp):
    check_sources(sources)
    spec = TARGETS[key]
    stock_record = key == "solution"
    field = "composition" if stock_record else "ingredients"
    ref = SOLUTION if stock_record else MEDIUM
    base = ["data"] if stock_record else ["data", "solutions", 0]
    data = runner.get_node(json.loads(sources[ref]["raw"]), base)
    rows = before[field]
    runner.require(
        before["id"] == spec["id"] and not runner.errors(before, spec["target_class"]),
        "Baseline identity/schema drift",
    )
    runner.require(
        not before.get("solutions") and not before.get("variants"), "Unreviewed topology"
    )
    runner.require(
        [r["preferred_term"] for r in rows]
        == SALTS + (["Distilled water"] if stock_record else []) + SUPPLEMENTS,
        "Local ingredient drift",
    )
    by_name = {n["preferred_term"]: (i, n) for i, n in enumerate(rows)}
    for i, node in enumerate(rows[:12]):
        runner.require(
            node["concentration"] == {"value": str(data["recipe"][i]["g_l"]), "unit": "G_PER_L"},
            "Basal amount drift",
        )
    expected = ["0.02", "2", "10", "10", "0.3"]
    for label, value in zip(SUPPLEMENTS, expected, strict=True):
        unit = "PERCENT_V_V" if stock_record and label == "Polar lipid fraction" else "G_PER_L"
        runner.require(
            by_name[label][1]["concentration"] == {"value": value, "unit": unit},
            "Supplement baseline drift",
        )

    after = copy.deepcopy(before)
    nodes = {n["preferred_term"]: n for n in after[field]}
    sulfur = nodes["Sulfur"]
    after[field] = [sulfur]
    after["solutions"] = [
        {
            "preferred_term": "Mineral salt preparation for medium 265",
            "composition": [nodes[n] for n in SALTS],
            "source": PDF,
            "preparation_notes": "Prepare the mineral salt base anaerobically under 100% nitrogen and autoclave before separately prepared supplements are added.",
            "notes": "1000 ml distilled water is a batch input, not final-volume makeup. The retained basal g/L values are provider-reported rates on the API's 1000 ml basis, not measured final stock or complete-medium concentrations. No base addition volume is inferred.",
        }
    ]
    if stock_record:
        runner.require("source_data" not in after, "Existing provenance needs reconciliation")
        after["source_data"] = {"origin": "MediaDive"}
    evidence_root = ["source_data"] if stock_record else []
    claims, resolutions = [], []

    def claim(
        pointer,
        old_pointer,
        status,
        reference,
        snippet,
        explanation,
        evidence_pointer,
        ingredient,
        source_pointer=None,
    ):
        runner.require(snippet in sources[reference]["raw"], "Inexact claim snippet")
        item = {
            "pointer": pointer,
            "old_pointer": old_pointer,
            "field": runner.field_name(pointer),
            "ingredient": ingredient,
            "old": (
                copy.deepcopy(runner.get_node(before, old_pointer))
                if old_pointer is not None
                else None
            ),
            "new": copy.deepcopy(runner.get_node(after, pointer)),
            "status": status,
            "reference": reference,
            "snippet": snippet,
            "source_pointer": source_pointer,
            "locator": (
                "page 1, recipe/preparation"
                if reference == PDF
                else "$." + runner.field_name(source_pointer)
            ),
            "explanation": explanation,
            "evidence_pointer": evidence_pointer,
        }
        claims.append(item)
        return item

    step_pointer = base + ["steps", 1]
    step_quote = json_excerpt(sources[ref]["raw"], step_pointer)
    for index, label in enumerate(SALTS):
        pointer = ["solutions", 0, "composition", index]
        node = runner.get_node(after, pointer)
        row = data["recipe"][index]
        node["notes"] = (
            f"Mineral-base batch input: {row['amount']} {row['unit']}. Retained {row['g_l']} g/L is the provider-declared 1000 ml normalization, not a verified concentration after supplement addition or a measured final base volume."
        )
        reason = "Relocate the source-reported mineral rate to its basal preparation; no complete-medium concentration is inferred."
        c = claim(
            pointer + ["concentration"],
            [field, index, "concentration"],
            "relocate",
            ref,
            json_excerpt(sources[ref]["raw"], base + ["recipe", index]),
            reason + " " + node["notes"] + " Additional exact preparation excerpt: " + step_quote,
            pointer,
            label,
            base + ["recipe", index],
        )
        if key != "komodo":
            resolutions.append(
                {
                    "from_pointer": [field, index],
                    "to_pointer": pointer,
                    "reference": ref,
                    "disposition": "relocated",
                    "old_concentration": copy.deepcopy(rows[index]["concentration"]),
                    "new_field": c["field"],
                    "source_pointer": step_pointer,
                    "source_snippet": step_quote,
                    "reason": reason,
                }
            )
    water = (
        nodes["Distilled water"]
        if stock_record
        else {
            "preferred_term": "Distilled water",
            "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
        }
    )
    if stock_record:
        runner.require(
            water["concentration"] == {"value": "1000", "unit": "PERCENT_V_V"},
            "Water baseline drift",
        )
    water["concentration"] = {"value": "1", "unit": "L"}
    water["notes"] = (
        "1000 ml distilled-water input per mineral-base batch, not a final-volume instruction."
    )
    after["solutions"][0]["composition"].append(water)
    claim(
        ["solutions", 0, "composition", 12, "concentration"],
        [field, 12, "concentration"] if stock_record else None,
        "correct" if stock_record else "add",
        PDF,
        "Distilled water 1000.00 ml",
        "1000 ml / 1000 ml per L = 1 L input. Supports the water label and input-basis note; not a percentage or final volume.",
        ["solutions", 0, "composition", 12],
        "Distilled water",
    )
    for stock_index, (label, strength, dose, quote) in enumerate(STOCKS, 1):
        node = nodes[label]
        old_index = by_name[label][0]
        node["concentration"] = {"value": strength, "unit": "PERCENT_W_V"}
        node["notes"] = (
            f"{strength}% w/v in the separately prepared stock, not the former imported final-medium rate. "
            + (
                "Original source: 20 ml stock contains 2 g yeast extract; the API's 20 mg/l and former 0.02 g/L disagree. The PDF calls for boiling, not autoclaving; its instruction does not add a separate yeast filtration step."
                if label == "Yeast extract"
                else "Receiving-medium concentration is unresolved because its final volume is not established."
            )
        )
        stock = {
            "preferred_term": f"{label} stock ({strength}% w/v)",
            "composition": [
                node,
                {
                    "preferred_term": "Water",
                    "notes": "Stock solvent according to the API attribute; no fixed carrier volume is specified.",
                },
            ],
            "concentration": {"value": dose, "unit": "L"},
            "source": PDF,
            "preparation_notes": " ".join(quote.split()),
            "notes": "Original-recipe batch addition, not liters per liter of final medium. Stock strength and batch dose are separate claims; the stock solvent amount and final receiving volume are not inferred.",
        }
        after["solutions"].append(stock)
        p = ["solutions", stock_index]
        claim(
            p + ["composition", 0, "concentration"],
            [field, old_index, "concentration"],
            "correct_stock_basis",
            PDF,
            quote,
            f"The original source explicitly specifies {strength}% w/v. This replaces a flattened rate with stock strength; it is not a numerical correction of a measured complete-medium concentration. Supports stock name and preparation scope too.",
            p + ["composition", 0],
            label,
        )
        claim(
            p + ["concentration"],
            None,
            "add_stock_dose",
            PDF,
            quote,
            f"Source batch dose converted from ml to {dose} L by dividing by 1000; no final-volume denominator. Supports separate stock boundary and preparation.",
            evidence_root,
            label + " stock dose",
        )
        source_index = next(i for i, row in enumerate(data["recipe"]) if row["compound"] == label)
        source_pointer = base + ["recipe", source_index]
        attribute = data["recipe"][source_index]["attribute"]
        runner.require("water" in attribute, "Unverified stock carrier")
        claim(
            p + ["composition", 1, "notes"],
            None,
            "restore_carrier",
            ref,
            json_excerpt(sources[ref]["raw"], source_pointer),
            "The source attribute explicitly identifies water. It does not specify a solvent input volume. No water concentration is invented.",
            p + ["composition", 1],
            label + " stock solvent",
            source_pointer,
        )
        if label == "Yeast extract":
            claim(
                p + ["composition", 0, "notes"],
                [field, old_index, "notes"],
                "retain_conflict",
                ref,
                json_excerpt(sources[ref]["raw"], source_pointer),
                "Counterevidence is retained in this explanation: API amount=20 mg/l and g_l=0.02 conflict with its own 20 ml of 10% w/v preparation and the original PDF's 2 g input. SUPPORT here applies only to documenting that source disagreement, not to endorsing the old concentration.",
                p + ["composition", 0],
                label + " source disagreement",
                source_pointer,
            )

    sulfur.pop("concentration")
    sulfur["notes"] = (
        "Source batch input: 10 g powdered sulfur, sterilized separately by steaming for 3 h on each of three successive days and added to the autoclaved mineral salt preparation. The former 10 g/L is not retained as a final-medium concentration; final volume is unspecified."
    )
    claim(
        [field, 0, "notes"],
        [field, by_name["Sulfur"][0], "concentration"],
        "withdraw_rate",
        PDF,
        SULFUR_QUOTE,
        "Retain the explicit 10 g batch input and separate sterilization, without asserting g/L. Additional exact table excerpt: Sulfur, powdered 10.00 g. Chemical mapping is unchanged.",
        [field, 0],
        "Sulfur",
    )
    lipid = nodes["Polar lipid fraction"]
    lipid.pop("concentration")
    lipid["notes"] = (
        "Source material: aqueous polar-lipid suspension prepared from Thermoproteus tenax (DSM 2078) or another archaebacterium. Composition, extraction yield and lipid mass concentration are not specified. Former mass/percentage encoding is withdrawn."
    )
    after["solutions"].append(
        {
            "preferred_term": "Polar lipid aqueous suspension",
            "composition": [lipid],
            "concentration": {"value": "0.006-0.012", "unit": "L"},
            "source": PDF,
            "preparation_notes": "Use the separately prepared polar lipid fraction described in the original recipe. The cited Zillig procedure was not inspected and its detailed extraction is not inferred.",
            "notes": "Original PDF batch dose: 6-12 ml. The API alternatively lists 10 ml/l and a modified biomass extraction procedure; that version is retained in evidence, not silently substituted for the original range or used to calculate final lipid concentration.",
        }
    )
    claim(
        ["solutions", 4, "composition", 0, "notes"],
        [field, by_name["Polar lipid fraction"][0], "concentration"],
        "withdraw_rate",
        PDF,
        "Polar lipid fraction prepared from \n Thermoproteus tenax (DSM 2078) \n or from any other archaebacterium, \n aqueous suspension 6 - 12.00 ml",
        "A suspension volume does not support the old g/L or percent encoding. Preserve material identity without invented chemical mapping, composition or extraction yield.",
        ["solutions", 4, "composition", 0],
        "Polar lipid fraction",
    )
    claim(
        ["solutions", 4, "concentration"],
        None,
        "add_stock_dose",
        PDF,
        LIPID_QUOTE,
        "6-12 ml / 1000 ml per L = 0.006-0.012 L per source batch. Preserve the range; do not choose its midpoint or infer a per-liter dose.",
        evidence_root,
        "Polar lipid batch dose",
    )
    claim(
        ["solutions", 4, "notes"],
        None,
        "retain_version_difference",
        ref,
        json_excerpt(sources[ref]["raw"], base + ["recipe", 16]),
        "The dataset lists a 10 ml/l aqueous suspension. This records the disagreement with the PDF's 6-12 ml batch range; it does not endorse a hybrid formulation or the old mass/percentage amount.",
        ["solutions", 4, "composition", 0],
        "Lipid dose version difference",
        base + ["recipe", 16],
    )

    after["notes"] = (
        before.get("notes", "")
        + "\n\n"
        + "Original-source preparation scope: mineral salt base plus separately prepared yeast-extract, sucrose, sulfur, polar-lipid and sulfide additions under 100% nitrogen. Historical aerobic/import annotations are not endorsed. Basal rates remain provider-declared 1000 ml normalizations only. The original PDF supplies stock strengths and batch doses; its lipid range differs from the API's modified protocol. Neither source establishes a measured final receiving volume. Chemical mappings, parent/variant links and prior curation history are preserved, not independently revalidated."
    ).lstrip()
    claim(
        ["notes"],
        ["notes"] if "notes" in before else None,
        "correct_scope",
        PDF,
        "Prepare the medium anaerobically under 100% nitrogen.",
        "Qualify source stages, historical import annotations and unresolved final-volume/version scope.",
        evidence_root,
        "Recipe preparation scope",
    )
    for i, stock in enumerate(after["solutions"]):
        claim(
            ["solutions", i, "source"],
            None,
            "restore_stock_boundary",
            PDF,
            PREPARATION,
            "Original recipe explicitly separates the mineral base and supplements. Descriptor labels are curator labels, not new source accessions. Stock metadata must be read with its separately evidenced quantity and preparation notes.",
            evidence_root,
            stock["preferred_term"],
        )
    if key == "dsmz":
        runner.require(
            after["preparation_steps"][1]["description"] == data["steps"][1]["step"],
            "Preparation baseline drift",
        )
        after["preparation_steps"][1]["action"] = "MIX"
        after["preparation_steps"][3][
            "description"
        ] = "Autoclave the mineral salt preparation at 121 \u00b0C for 15 min; prepare the supplements separately as specified."
        claim(
            ["preparation_steps", 1, "action"],
            ["preparation_steps", 1, "action"],
            "correct_scope",
            ref,
            step_quote,
            "The compound instruction assembles separately treated supplements; AUTOCLAVE must not imply autoclaving yeast or the complete supplemented medium.",
            evidence_root,
            "Separate preparation action",
            step_pointer,
        )
        claim(
            ["preparation_steps", 3, "description"],
            ["preparation_steps", 3, "description"],
            "correct_scope",
            ref,
            json_excerpt(sources[ref]["raw"], base + ["steps", 3]),
            "Scope this API autoclave instruction to the mineral base using the explicit separate-supplement instruction. Additional exact excerpt: "
            + step_quote,
            evidence_root,
            "Mineral-base autoclaving",
            base + ["steps", 3],
        )
    if key == "komodo":
        text = sources[PDF]["raw"]
        paragraph = text[text.index("Prepare the medium anaerobically") :].strip()
        after["preparation_steps"] = [
            {"step_number": 1, "action": "ADJUST_PH", "description": "Adjust final pH to 5.2."},
            {"step_number": 2, "action": "MIX", "description": " ".join(paragraph.split())},
        ]
        claim(
            ["preparation_steps"],
            None,
            "restore_preparation",
            PDF,
            paragraph,
            "Restore the original recipe's separate-preparation instruction and explicit pH. Additional exact source excerpt: Adjust final pH to 5.2. No incubation or growth assertion is added; no detailed lipid extraction procedure is invented.",
            evidence_root,
            "Original preparation",
        )

    groups = {}
    for c in claims:
        groups.setdefault((tuple(c["evidence_pointer"]), c["reference"]), []).append(c)
    for (pointer, reference), group in groups.items():
        node = runner.get_node(after, pointer)
        entries = [e for e in node.get("evidence", []) if e["reference"] == reference]
        runner.require(len(entries) <= 1, "Duplicate prior evidence")
        explanation = (
            " ".join(
                f"{c['field']} ({c['status']}), locator={c['locator']}: {c['explanation']}"
                + (
                    f" Additional exact excerpt: {c['snippet']}"
                    if i and c["snippet"] != group[0]["snippet"]
                    else ""
                )
                for i, c in enumerate(group)
            )
            + f" Source SHA256={HASHES[reference]}; accessed_on=2026-10-07. Ingredient ontology mappings remain unchanged."
        )
        if entries:
            runner.require(entries[0]["snippet"] == group[0]["snippet"], "Historical snippet drift")
            entries[0]["explanation"] = (
                explanation
                + " Historical explanation (superseded where stage/scope differs): "
                + entries[0]["explanation"]
            )
        else:
            node.setdefault("evidence", []).append(
                {
                    "reference": reference,
                    "supports": "SUPPORT",
                    "snippet": group[0]["snippet"],
                    "explanation": explanation,
                }
            )
    refs = [
        (PDF, "DSMZ 265. THERMOFILUM PENDENS MEDIUM", "culture_collection_page"),
        (
            ref,
            (
                "MediaDive solution 531: Main sol. 265"
                if stock_record
                else "MediaDive medium 265: THERMOFILUM PENDENS MEDIUM"
            ),
            "dataset",
        ),
    ]
    if key == "komodo":
        after.setdefault("evidence", []).append(
            {
                "reference": MAPPING_URL,
                "supports": "SUPPORT",
                "snippet": sources["mapping"]["snippet"],
                "explanation": f"Identity only: KOMODO 265 links the original DSMZ 265 recipe at {PDF}. Mapping SHA256={MAPPING_META['sha256']}; accessed_at={MAPPING_META['accessed_at']}. No amounts, growth or variant equivalence are inferred from the mapping.",
            }
        )
        refs.append((MAPPING_URL, "KOMODO media list: original recipe mappings", "dataset"))
    for reference, title, kind in refs:
        if not any(r["reference"] == reference for r in after.get("references", [])):
            after.setdefault("references", []).append(
                {
                    "reference": reference,
                    "title": title,
                    "notes": f"source_type={kind}; discovery_mode={'cross_reference' if key == 'komodo' else 'existing_record_reference'}; accessed_on=2026-10-07; source_sha256={HASHES.get(reference, MAPPING_META['sha256'])}; individual authors and publication year not established. PDF copyright/creation years are not treated as publication year. Original PDF and API differences are explicitly retained.",
                }
            )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="; ".join(r[0] for r in refs),
        notes="Restored mineral base, three percentage stocks and lipid suspension; corrected water input and yeast stock basis; withdrew unsupported sulfur/lipid rates. Preserved original-source/API disagreement, all prior snippets, history, IDs, chemical mappings and variant links. No growth association or final receiving concentration inferred.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'])} -> {json.dumps(c['new'])} ({c['status']})"
            for c in claims
        ),
    )
    runner.require(not runner.errors(after, spec["target_class"]), "Proposed schema failure")
    return after, claims, resolutions


def process(root, sources, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    check_sources(sources)
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse to overwrite plan")
        plan = {
            "version": 1,
            "action": ACTION,
            "commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=root, text=True
            ).strip(),
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "sources": sources,
        }
    else:
        plan = json.loads(plan_path.read_text())
        runner.require(
            plan["version"] == 1 and plan["action"] == ACTION and plan["sources"] == sources,
            "Frozen plan/source drift",
        )
        runner.require([r["key"] for r in plan["records"]] == list(TARGETS), "Frozen targets drift")
    records, pending = [], []
    for index, (key, spec) in enumerate(TARGETS.items()):
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target")
        current = path.read_bytes()
        before = current if mode == "preview" else plan["records"][index]["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
        after, claims, resolutions = build(
            runner.load_yaml(before), key, sources, plan["created_at"]
        )
        output = runner.render(before.decode(), after)
        runner.require(current in (before, output), "Concurrent edit")
        records.append(
            {
                **spec,
                "key": key,
                "action": ACTION,
                "before_text": before.decode(),
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "source_sha256": HASHES[SOLUTION if key == "solution" else MEDIUM],
                "claims": claims,
                "claim_resolutions": resolutions,
            }
        )
        pending.append((path, current, output))
    if mode != "preview":
        runner.require(records == plan["records"], "Frozen decision drift")
    plan["records"] = records
    runner.safe_targets(root, plan)
    runner.require(
        all(p.read_bytes() == current and not p.is_symlink() for p, current, _ in pending),
        "Concurrent edit before apply",
    )
    if mode == "preview":
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        for path, current, output in pending:
            runner.require(
                path.read_bytes() == current and not path.is_symlink(),
                "Concurrent edit during apply",
            )
            if mode == "apply" and current != output:
                path.write_bytes(output)
            runner.require(path.read_bytes() == output, "Unapplied result")
    return plan, {
        "mode": mode,
        "records": len(records),
        "changed": sum(c != o for _, c, o in pending) if mode == "apply" else 0,
        "already_applied": sum(c == o for _, c, o in pending),
        "scoped_claims": sum(len(r["claims"]) for r in records),
    }


def report(plan, folder, applied):
    folder.mkdir(parents=True, exist_ok=True)
    for item in plan["records"]:
        lines = [
            "# Medium 265 Preparation Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Hash-linked successor to an existing per-record report, not an additional unique reviewed path. Baseline and proposed schemas pass. Validation outcomes and remaining source gaps are in README.md and validation.json.",
            "",
            "| Field | Ingredient | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in item["claims"]:
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(c[k])
                    for k in (
                        "field",
                        "ingredient",
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
        lines += [
            "",
            "Unresolved: measured base/receiving final volume, detailed lipid composition/extraction yield, the API/original lipid-protocol difference and independent chemical-identity verification. No new growth association is asserted.",
            "",
        ]
        (folder / (item["key"] + "-followup.md")).write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--medium-cache", type=Path, required=True)
    parser.add_argument("--solution-cache", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--text", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    sources = read_sources(
        args.medium_cache, args.solution_cache, args.mapping, args.pdf, args.text
    )
    plan, result = process(
        ROOT, sources, args.plan, "apply" if args.apply else "verify" if args.verify else "preview"
    )
    if args.reports:
        report(plan, args.reports, args.apply or args.verify)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
