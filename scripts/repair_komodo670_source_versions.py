#!/usr/bin/env python3
"""Curate pinned KOMODO 670 strain formulations without blending source versions."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from pathlib import Path

import review_solution_concentration_evidence as runner
from inventory_komodo_concentration_sources import MAPPING_URL

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "reports/ingredient_concentration_curation"
HERE = BASE / "20261007-komodo670-source-versions"
PREVIOUS = BASE / "20261007-dsmz546-659-670-stocks"
ACTION = "CURATED_KOMODO670_STRAIN_RECIPES_WITH_SEPARATE_SOURCE_VERSIONS"
DOI = "doi:10.13145/bacdive4303.20170829.2"
ARCHIVE = "https://bacdive.dsmz.de/pdf/4303?doi=10.13145%2Fbacdive4303.20170829.2"
CURRENT = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium670.pdf"
RELATION = "STRAIN_SPECIFIC_VARIANT"
STRAINS = ("9463", "9466", "9467", "9468")
PINS = {
    PREVIOUS
    / "next-variant-handoff.json": "ca8a5bb485e4cc985e2ef7ad52173a0a19251a1d7398c472ce9f740b2c5dcbd8",
    PREVIOUS / "plan.json": "3cd5480368b89753710871a2aeed202dd7014e8a00082953d7ab21542584ad2e",
    HERE
    / "source-captures.json": "c8023885299b84010701934109560f7ce3fa4b90f77c49ef890499bbb67caace",
}
SCOPE = (
    "Curated formulation: the explicitly named DSM strain instructions in BacDive 4303 "
    "archive version 2 (2017), not the current DSMZ 670 formulation. The archive agrees "
    "with the KOMODO pH profile, but that agreement does not prove which recipe version "
    "KOMODO originally imported. Current DSMZ differences are a separate inline variant. "
    "The BacDive biological record is DSM 2392; only its reproduced, explicitly named "
    "recipe instructions are used here, not its growth, temperature or taxonomic claims. "
    "Batch mass, unspecified percent basis, normality and final-volume gaps remain explicit. "
    "New ingredient labels are source labels, not independently resolved ontology mappings."
)


def pinned(path):
    raw = path.read_bytes()
    runner.require(runner.sha(raw) == PINS[path], "Pinned artifact drift: " + str(path))
    return json.loads(raw)


def frozen():
    handoff = pinned(PREVIOUS / "next-variant-handoff.json")
    old = pinned(PREVIOUS / "plan.json")
    capture = pinned(HERE / "source-captures.json")
    pdf_raw = Path(handoff["pdf_captures"]).read_bytes()
    runner.require(runner.sha(pdf_raw) == handoff["pdf_captures_sha256"], "PDF capture drift")
    sources = {s["key"]: s for s in capture["sources"]}
    sources["current"] = next(s for s in json.loads(pdf_raw)["sources"] if s["medium_id"] == "670")
    sources["mapping_source"] = handoff["mapping_source"]
    targets = {}
    for r in handoff["records"]:
        if r["source_medium"] != "670":
            continue
        strain = r["record"]["name"].removeprefix("for_dsm_")
        runner.require(strain in STRAINS, "Unexpected strain")
        targets[strain] = {
            "path": r["path"],
            "id": r["id"],
            "before_sha256": r["sha256"],
            "snapshot": r["record"],
            "target_class": "MediaRecipe",
        }
        sources[strain] = r["mapping"]
    r = next(r for r in old["records"] if r["key"] == "670-komodo")
    targets["parent"] = {
        "path": r["path"],
        "id": r["id"],
        "before_sha256": r["after_sha256"],
        "snapshot": runner.load_yaml(r["after_text"]),
        "target_class": "MediaRecipe",
    }
    runner.require(tuple(targets) == (*STRAINS, "parent"), "Target inventory drift")
    return targets, sources


def check_sources(sources):
    runner.require(sources == frozen()[1], "Pinned source drift")
    for key in ("bacdive4303", "doi4303", "datacite4303", "current"):
        runner.require(sources[key]["http_status"] == 200, "Failed source capture")
    attrs = sources["datacite4303"]["data"]["data"]["attributes"]
    runner.require(
        attrs["doi"] == DOI.removeprefix("doi:") and attrs["publicationYear"] == 2017,
        "Wrong archive metadata",
    )
    html = sources["doi4303"]["text"]
    runner.require(
        "Archive BacDiveID:10.13145/bacdive4303.20170829.2" in html
        and 'src="/pdf/4303?doi=10.13145%2Fbacdive4303.20170829.2"' in html
        and 'class="text-center">version&nbsp;2</div>' in html,
        "Archive version not confirmed",
    )
    for strain in STRAINS:
        row = sources[strain]
        runner.require(row["original_recipe"] == CURRENT, "Wrong original recipe")
        runner.require("DSM " + strain in " ".join(row["cells"]), "Wrong strain mapping")


def paragraphs(sources):
    old = sources["bacdive4303"]["pages"][1]["text"]
    new = sources["current"]["pages"][0]["text"]
    result = {}
    endings = {
        "9463": "For DSM 2392",
        "9466": "For DSM 9467",
        "9467": "For DSM 9468",
        "9468": "\nTemperatures",
    }
    for strain in STRAINS:
        start = old.index("For DSM " + strain + ":")
        result[strain] = old[start : old.index(endings[strain], start)].strip()
        start = new.index("For DSM " + strain + ":")
        stop = new.find("\nFor DSM ", start + 1)
        if stop == -1:
            stop = new.index("\n\u00a9", start)
        result["current-" + strain] = new[start:stop].strip()
    return result


def bibliography(sources):
    attrs = sources["datacite4303"]["data"]["data"]["attributes"]
    metadata = {
        "title": attrs["titles"][0]["title"],
        "authors": "; ".join(c["name"] for c in attrs["creators"]),
        "year": attrs["publicationYear"],
    }
    notes = (
        "source_type=dataset; discovery_mode=manual_web_search; accessed_on="
        + sources["bacdive4303"]["accessed_at"][:10]
        + "; version=2; DOI="
        + DOI
        + "; locator=PDF page 2, Ref. 1071 culture medium composition; "
        "bibliography verified via DataCite; archive landing page resolves this exact PDF; "
        "named strain recipe instructions only, not growth metadata for those strains."
    )
    return [
        {"reference": ARCHIVE, **metadata, "notes": notes},
        {"reference": DOI, **metadata, "notes": notes + " PDF=" + ARCHIVE},
        {
            "reference": CURRENT,
            "title": "670: ACIDIFERROBACTER (MS) MEDIUM",
            "notes": "source_type=culture_collection_page; discovery_mode=cross_reference; accessed_on="
            + sources["current"]["accessed_at"][:10]
            + "; response_sha256="
            + sources["current"]["sha256"]
            + "; current-source alternative only; no individual authors or publication year supplied; copyright year is not a publication date.",
        },
        {
            "reference": MAPPING_URL,
            "title": "KOMODO - the Known Media Database",
            "notes": "source_type=dataset; discovery_mode=cross_reference; accessed_on="
            + sources["mapping_source"]["accessed_at"][:10]
            + "; strain/accession and pH mapping only; no concentration or archived-version identity inferred.",
        },
    ]


def build(before, key, sources, timestamp):
    targets, expected = frozen()
    runner.require(sources == expected, "Pinned source drift")
    runner.require(before == targets[key]["snapshot"], "Unreviewed baseline")
    runner.require(not runner.errors(before, "MediaRecipe"), "Invalid baseline")
    after, claims = copy.deepcopy(before), []
    paras = paragraphs(sources)
    page = sources["bacdive4303"]["pages"][1]["text"]
    base_quote = (
        "(NH4)2SO4 2.00 g MgSO4 x 7 H2O 0.25 g K2HPO4 0.10 g KCl 0.10 g\nDistilled water 1000.00 ml"
    )
    runner.require(base_quote in page, "Base recipe drift")

    def claim(pointer, old_pointer, status, snippet, explanation, ep=(), ref=ARCHIVE):
        src = sources["current"] if ref == CURRENT else sources["bacdive4303"]
        text = src["pages"][0 if ref == CURRENT else 1]["text"]
        locator = "PDF page " + (
            "1" if ref == CURRENT else "2, Ref. 1071 culture medium composition"
        )
        if ref == MAPPING_URL:
            text = sources[key]["snippet"]
            locator = "KOMODO table row " + sources[key]["medium_id"]
        runner.require(snippet and snippet in text, "Snippet does not occur in source")
        value = runner.get_node(after, pointer) if pointer else None
        old_value = runner.get_node(before, old_pointer) if old_pointer else None
        field = runner.field_name(pointer or old_pointer)
        c = {
            "pointer": list(pointer),
            "old_pointer": list(old_pointer),
            "field": field,
            "old": copy.deepcopy(old_value),
            "new": copy.deepcopy(value),
            "status": status,
            "reference": ref,
            "snippet": snippet,
            "locator": locator,
            "explanation": explanation,
            "evidence_pointer": list(ep),
        }
        claims.append(c)
        evidence = runner.get_node(after, ep).setdefault("evidence", [])
        message = field + " (" + status + "): " + explanation + " Locator: " + locator + "."
        entry = next((e for e in evidence if e["reference"] == ref), None)
        if entry:
            entry["explanation"] += " " + message
            if entry["snippet"] != snippet:
                entry["explanation"] += " Additional exact excerpt: " + snippet
        else:
            evidence.append(
                {
                    "reference": ref,
                    "supports": "SUPPORT",
                    "snippet": snippet,
                    "explanation": message,
                }
            )

    def current_variant(strain):
        modifications = [
            "Current DSMZ 670 base table uses 950 ml distilled-water input, not the archive's 1000 ml; this is not a stated final volume.",
            "Current base preparation is autoclaving for 15 min at 121 C; incubate statically without shaking. These instructions are not imported into the historical formulation.",
        ]
        if strain in {"9463", "9466"}:
            modifications += [
                "Omit FeSO4 x 7 H2O; add 5.00 g/L powdered sulfur sterilized by steaming in a boiling water bath for 3 hours on each of 3 successive days."
            ]
        if strain == "9466":
            modifications += [
                "Current source: pH 3.0 using 1 N H2SO4, versus archived pH 3.5. Add 0.20 g/L yeast extract from a sterile stock; its strength, dose and sterilization method are unspecified."
            ]
        elif strain == "9467":
            modifications += [
                "Current source: pH 3.0 with 1 N H2SO4, not archived 2 N acid; omit iron. Add 2.00 g/L D-glucose and 0.1 g/L yeast extract from filter-sterilized stocks of unspecified strength/dose, rather than the archived stock specifications."
            ]
        elif strain == "9468":
            modifications += [
                "Current source: pH 1.6 with 4 N H2SO4 and 50 ml of 40% w/v FeSO4 x 7 H2O stock per recipe batch. Stock is made in 0.2 N H2SO4 and filter-sterilized under 100% N2; the old per-5-ml-base ratio and autoclaving alternative are not asserted for this version."
            ]
        else:
            modifications += ["Current source retains pH 3.5 using 1 N H2SO4 before autoclaving."]
        after["variants"] = [
            {
                "name": "DSM " + strain + " current DSMZ 670 source formulation",
                "relationship": "DERIVED_FROM",
                "description": "Separate recipe version; not applied to the asserted archived formulation.",
                "modifications": modifications,
            }
        ]
        claim(
            ["variants", 0, "modifications"],
            [],
            "separate_source_version",
            paras["current-" + strain],
            "Current-source changes apply only to this inline alternative; they do not repair the archive by substitution.",
            ["variants", 0],
            CURRENT,
        )
        current_base = sources["current"]["pages"][0]["text"].split("\nFor DSM ")[0]
        claim(
            ["variants", 0, "description"],
            [],
            "separate_source_version",
            current_base,
            "The same current-source base table and preparation qualify this alternative; final volume remains unstated.",
            ["variants", 0],
            CURRENT,
        )

    if key == "parent":
        for index, strain in enumerate(STRAINS, 2):
            node = after["variant_children"][index]
            runner.require(node["id"] == targets[strain]["id"], "Child link order drift")
            node["relationship"] = RELATION
            node["notes"] = (
                "DSM "
                + strain
                + ": archived 2017 strain-specific formulation; source-version, supplement and preparation differences are not pH-only. The child retains a separate current-DSMZ alternative."
            )
            claim(
                ["variant_children", index, "relationship"],
                ["variant_children", index, "relationship"],
                "correct",
                paras[strain],
                node["notes"],
                ["variant_children", index],
            )
        after[
            "notes"
        ] += "\n\nFour DSM 9463/9466/9467/9468 children now carry explicitly archived formulations and separate current-source alternatives. Their relationship is strain-specific, not pH-only. This does not re-curate the other two duplicate-source links."
        claim(
            ["notes"],
            ["notes"],
            "clarify_scope",
            base_quote,
            "Archived 1000 ml water input and strain-specific additions differ from this parent's current-source preparation.",
        )
    else:
        strain, para = key, paras[key]
        runner.require(
            not any(
                k in before
                for k in ("solutions", "references", "evidence", "variants", "preparation_steps")
            ),
            "Unexpected topology",
        )
        after["ingredients"] = copy.deepcopy(before["ingredients"][:4])
        for i, mass in enumerate(("2.00", "0.25", "0.10", "0.10")):
            node = after["ingredients"][i]
            node.pop("concentration")
            node["notes"] = (
                "Archived batch input: "
                + mass
                + " g in a recipe with 1000 ml distilled-water input. No final volume is stated; mass-only grams have no schema unit. The former G_PER_L assertion is withdrawn, not rounded or interpreted as a measured final concentration."
            )
            claim(
                [],
                ["ingredients", i, "concentration"],
                "remove_unsupported",
                base_quote,
                node["notes"],
                ["ingredients", i],
            )
            claim(
                ["ingredients", i, "notes"],
                [],
                "schema_gap",
                base_quote,
                "Preserve the exact source batch mass and denominator limitation.",
                ["ingredients", i],
            )
        water = {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1", "unit": "L"},
            "notes": "1000 ml distilled-water input per archived recipe batch, not the final medium volume.",
        }
        after["ingredients"].append(water)
        claim(
            ["ingredients", 4, "concentration"],
            [],
            "add",
            "Distilled water 1000.00 ml",
            water["notes"] + " Conversion: 1000 ml / 1000 = 1 L.",
            ["ingredients", 4],
        )
        acid = (
            copy.deepcopy(before["ingredients"][5])
            if strain != "9468"
            else {"preferred_term": "H2SO4"}
        )
        acid.pop("concentration", None)
        normality = {"9463": "1", "9466": "1", "9467": "2", "9468": "4"}[strain]
        acid["notes"] = (
            f"Archived pH-adjustment reagent: {normality} N sulfuric acid, added to reach pH {before['ph_value']} before autoclaving. Dose is unquantified. Normality is preserved in text because the concentration enum has no NORMAL unit; it is not a final-medium concentration."
        )
        after["ingredients"].append(acid)
        if strain != "9468":
            claim(
                [],
                ["ingredients", 5, "concentration"],
                "remove_placeholder",
                para,
                "Withdraw the schema-default variable placeholder; the source specifies titration to pH, not a dose or final concentration.",
                ["ingredients", 5],
            )
            claim(
                [],
                ["ingredients", 4],
                "remove_copied_ingredient",
                para,
                "The archived base contains only the four salts and water, and this named-strain instruction adds no iron. The current-source instruction independently says to omit FeSO4 x 7 H2O.",
            )
            claim(
                [],
                ["ingredients", 4],
                "corroborate_omission",
                paras["current-" + strain],
                "Only iron omission is corroborated across versions; other current-source values are not applied here.",
                ref=CURRENT,
            )
        claim(
            ["ingredients", 5, "notes"],
            ["ingredients", 5, "notes"] if strain != "9468" else [],
            "not_quantified",
            para,
            acid["notes"],
            ["ingredients", 5],
        )

        if strain in {"9463", "9466"}:
            sulfur = {
                "preferred_term": "Powdered sulfur",
                "concentration": {"value": "5", "unit": "G_PER_L"},
                "notes": "Source-explicit receiving-medium target; add sterile powdered sulfur before use. The archive does not specify its sterilization method.",
            }
            after["ingredients"].append(sulfur)
            claim(
                ["ingredients", 6, "concentration"],
                [],
                "add",
                para,
                sulfur["notes"],
                ["ingredients", 6],
            )
        if strain == "9466":
            yeast = {
                "preferred_term": "Yeast extract",
                "concentration": {"value": "0.2", "unit": "G_PER_L"},
                "notes": "Source-explicit receiving-medium target, added before use from a sterile, autoclaved stock. Stock strength and addition volume are unspecified; 0.2 g/L is not the stock strength.",
            }
            after["ingredients"].append(yeast)
            claim(
                ["ingredients", 7, "concentration"],
                [],
                "add",
                para,
                yeast["notes"],
                ["ingredients", 7],
            )
        if strain == "9467":
            after["solutions"] = [
                {
                    "preferred_term": "Archived glucose stock",
                    "source": ARCHIVE,
                    "composition": [
                        {
                            "preferred_term": "Glucose",
                            "concentration": {"value": "10", "unit": "PERCENT_W_V"},
                            "notes": "Archived stock strength is explicitly 10% w/v. Final target is reported as 0.2% without a percent basis; it is not normalized to g/L. Stock dose is unspecified; the archive does not specify glucose stereochemistry.",
                        }
                    ],
                    "notes": "Filter-sterilized stock; add before use. No dose is inferred from the ambiguous final percent.",
                },
                {
                    "preferred_term": "Archived yeast extract stock",
                    "source": ARCHIVE,
                    "composition": [
                        {
                            "preferred_term": "Yeast extract",
                            "notes": "Archived stock strength is 1% without a stated percent basis; final target is 0.01%, also without a stated basis. No structured concentration or dilution calculation is asserted.",
                        }
                    ],
                    "notes": "Autoclaved stock; add before use. Stock addition volume is unspecified.",
                },
            ]
            claim(
                ["solutions", 0, "composition", 0, "concentration"],
                [],
                "add",
                para,
                after["solutions"][0]["composition"][0]["notes"],
                ["solutions", 0, "composition", 0],
            )
            claim(
                ["solutions", 1, "composition", 0, "notes"],
                [],
                "schema_gap",
                para,
                after["solutions"][1]["composition"][0]["notes"],
                ["solutions", 1, "composition", 0],
            )
            for i in range(2):
                claim(
                    ["solutions", i, "notes"],
                    [],
                    "not_quantified",
                    para,
                    after["solutions"][i]["notes"]
                    + " Solution names are curator labels, not new accessions.",
                )
        if strain == "9468":
            iron = copy.deepcopy(before["ingredients"][4])
            iron["concentration"] = {"value": "40", "unit": "PERCENT_W_V"}
            iron["notes"] = "Archived stock composition, not a final-medium 20 g/L concentration."
            carrier = {
                "preferred_term": "H2SO4",
                "notes": "Stock solvent is 0.2 N H2SO4; its amount is unstated. Normality remains text (schema gap), separate from the 4 N pH-adjustment reagent.",
            }
            after["solutions"] = [
                {
                    "preferred_term": "Archived FeSO4 x 7 H2O stock",
                    "source": ARCHIVE,
                    "composition": [iron, carrier],
                    "concentration": {
                        "value": "50",
                        "unit": "ML_PER_L",
                        "per_volume": "per liter of prepared MS-medium before iron-stock addition",
                    },
                    "notes": "Add 0.25 ml stock per 5 ml prepared MS-medium before use. Filter sterilization OR autoclaving under N2 are source alternatives; no incubation atmosphere is inferred. This ratio does not establish the final volume or a 50 ml absolute batch dose.",
                }
            ]
            claim(
                ["solutions", 0, "composition", 0, "concentration"],
                ["ingredients", 4, "concentration"],
                "correct_stock_basis",
                para,
                iron["notes"],
                ["solutions", 0, "composition", 0],
            )
            claim(
                ["solutions", 0, "composition", 1, "notes"],
                [],
                "schema_gap",
                para,
                carrier["notes"],
                ["solutions", 0, "composition", 1],
            )
            claim(
                ["solutions", 0, "concentration"],
                [],
                "add",
                para,
                "Dose ratio: 0.25 ml stock / 5 ml receiving base * 1000 ml/L = 50 ml per liter of prepared receiving base, not per liter of final medium. No final concentration is calculated.",
            )
            claim(
                ["solutions", 0, "notes"],
                [],
                "add_preparation",
                para,
                after["solutions"][0]["notes"],
            )

        if strain in {"9466", "9467"}:
            after["medium_type"], after["composition_type"] = "COMPLEX", "UNDEFINED"
            for field in ("medium_type", "composition_type"):
                claim(
                    [field],
                    [field],
                    "correct_classification",
                    para,
                    "Curator classification: source-required yeast extract prevents an entirely chemically defined formulation.",
                )
        after["ph_value"] = before["ph_value"]
        claim(
            ["ph_value"],
            ["ph_value"],
            "evidence_only",
            para,
            "Retain the archived named-strain pH, not an averaged or substituted value.",
        )
        after["preparation_steps"] = [
            {"step_number": 1, "action": "ADJUST_PH", "description": " ".join(para.split())}
        ]
        claim(
            ["preparation_steps"],
            [],
            "add_preparation",
            para,
            "Retain the complete historical strain instruction, including ordered additions and alternative stock sterilization, without importing current-source parameters.",
        )
        after["notes"] += "\n\n" + SCOPE
        claim(["notes"], ["notes"], "clarify_scope", base_quote, SCOPE)
        after["data_quality_flags"] = ["pending_curation"]
        claim(
            ["data_quality_flags"],
            ["data_quality_flags"],
            "correct_review_status",
            para,
            "Withdraw the inherited ingredients_curated flag: unresolved volume/normality/identity gaps and source-version attribution still need curation.",
        )
        after["variant_relationship"] = RELATION
        after["parent_media"]["relationship"] = RELATION
        after["parent_media"]["notes"] = (
            "Archived DSM "
            + strain
            + " formulation related to the current-source MS-MEDIUM parent; source version and preparation differ, not only pH."
        )
        after["variant_modifications"] = [
            "Historical 1000 ml water-input recipe; separate current-source formulation is in variants.",
            " ".join(para.split()),
        ]
        for pointer in (
            ["variant_relationship"],
            ["variant_modifications"],
            ["parent_media", "relationship"],
            ["parent_media", "notes"],
        ):
            claim(
                pointer, pointer, "correct", para, after["parent_media"]["notes"], ["parent_media"]
            )
        claim(
            ["media_term"],
            ["media_term"],
            "identity_only",
            sources[strain]["snippet"],
            "Exact KOMODO strain/accession mapping; this row does not date or prove identity with the archived recipe.",
            ref=MAPPING_URL,
        )
        current_variant(strain)

    for reference in bibliography(sources):
        if reference["reference"] not in {r["reference"] for r in after.get("references", [])}:
            after.setdefault("references", []).append(reference)
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=ARCHIVE,
        notes="Explicit archived formulation curation with separate current-source alternatives; no new organism-growth association. Prior history is preserved, not endorsed.",
        changes="; ".join(
            c["field"]
            + ": "
            + json.dumps(c["old"])
            + " -> "
            + json.dumps(c["new"])
            + " ("
            + c["status"]
            + ")"
            for c in claims
        ),
    )
    runner.require(
        not runner.errors(after, "MediaRecipe"),
        "Invalid proposed record: " + str(runner.errors(after, "MediaRecipe")),
    )
    return after, claims


def process(root, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    targets, sources = frozen()
    check_sources(sources)
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse plan overwrite")
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
            plan["action"] == ACTION
            and plan["version"] == 1
            and plan["sources"] == sources
            and [r["key"] for r in plan["records"]] == list(targets),
            "Plan drift",
        )
    records, pending = [], []
    for i, (key, spec) in enumerate(targets.items()):
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target")
        current = path.read_bytes()
        before = current if mode == "preview" else plan["records"][i]["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
        after, claims = build(runner.load_yaml(before), key, sources, plan["created_at"])
        output = runner.render(before.decode(), after)
        runner.require(current in (before, output), "Concurrent edit")
        records.append(
            {
                **{k: v for k, v in spec.items() if k != "snapshot"},
                "key": key,
                "action": ACTION,
                "before_text": before.decode(),
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "source_sha256": sources["bacdive4303"]["sha256"],
                "claims": claims,
                "claim_resolutions": [],
            }
        )
        pending.append((path, current, output))
    if mode != "preview":
        runner.require(records == plan["records"], "Frozen decisions drift")
    plan["records"] = records
    runner.safe_targets(root, plan)
    runner.require(
        all(p.read_bytes() == c and not p.is_symlink() for p, c, _ in pending),
        "Concurrent edit before write",
    )
    if mode == "preview":
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        for path, current, output in pending:
            runner.require(
                path.read_bytes() == current and not path.is_symlink(),
                "Concurrent edit during write",
            )
            if mode == "apply" and current != output:
                path.write_bytes(output)
            runner.require(path.read_bytes() == output, "Result not applied")
    return plan, {
        "mode": mode,
        "records": len(records),
        "changed": sum(c != o for _, c, o in pending) if mode == "apply" else 0,
        "already_applied": sum(c == o for _, c, o in pending),
        "claims": sum(len(r["claims"]) for r in records),
    }


def report(plan, applied):
    for item in plan["records"]:
        before = runner.load_yaml(item["before_text"])
        after = runner.load_yaml(item["after_text"])

        def ingredient(claim, before, after):
            for doc, pointer in (
                (after, claim["evidence_pointer"]),
                (after, claim["pointer"][:-1]),
                (before, claim["old_pointer"]),
                (before, claim["old_pointer"][:-1]),
            ):
                if not pointer:
                    continue
                node = runner.get_node(doc, pointer)
                if isinstance(node, dict) and (node.get("preferred_term") or node.get("name")):
                    return node.get("preferred_term") or node["name"]
            return after["name"]

        lines = [
            "# KOMODO 670 Source-Version Follow-Up",
            "",
            "- Follow-up target: " + item["path"],
            "- ID: " + item["id"],
            "- Reviewed commit: " + plan["commit"],
            "- Before SHA256: " + item["before_sha256"],
            "- Result SHA256: " + item["after_sha256"],
            "- State: " + ("applied locally" if applied else "preview"),
            "",
            "Hash-linked supplement to the existing exact-path report, not a second unique review.",
            "",
            "| Field | Ingredient/Context | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in item["claims"]:
            rendered = dict(c, ingredient=ingredient(c, before, after))
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(rendered[k])
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
        claimed_fields = {c["field"] for c in item["claims"]}
        for c in item["claims"]:
            if c["status"] not in {"schema_gap", "not_quantified"} or c["pointer"][-1:] != [
                "notes"
            ]:
                continue
            field = runner.field_name(c["pointer"][:-1] + ["concentration"])
            if field in claimed_fields:
                continue
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(v)
                    for v in (
                        field,
                        ingredient(c, before, after),
                        None,
                        None,
                        c["status"],
                        c["reference"],
                        c["snippet"],
                        c["locator"],
                        c["explanation"],
                    )
                )
                + " |"
            )
            claimed_fields.add(field)
        lines += [
            "",
            "## Unresolved Scope",
            "",
            SCOPE,
            "",
            "All normalized numeric fields introduced here are scoped to their source version. Missing stock doses, normality units, batch-mass units and unspecified percent bases are not filled with guesses. Existing chemical mappings and legacy aerobic notes were not independently validated. Validation results are recorded separately; the preview checks baseline and proposed schema shape only.",
            "",
        ]
        if item["key"] == "parent":
            lines += [
                "Parent ingredients, quantities and preparation are unchanged and retain their prior nine-record batch review; this follow-up reviews links and their evidence only.",
                "",
            ]
        (HERE / (item["key"] + "-followup.md")).write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    parser.add_argument("--reports", action="store_true")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.plan, mode)
    if args.reports:
        report(plan, mode != "preview")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
