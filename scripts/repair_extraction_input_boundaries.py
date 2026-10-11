#!/usr/bin/env python3
"""Separate two verified extraction preparations from their recovered media."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from pathlib import Path

from fetch_medium_concentration_sources import API, read_capture
from fetch_solution_concentration_sources import load_yaml
from repair_mediadive_stock_concentration_evidence import require, sha
from repair_reviewed_medium_stock_boundaries import PDF, reports
from review_medium_concentration_evidence import json_excerpt
from review_solution_concentration_evidence import field_name, get_node, render

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
REPORTS = Path("reports/ingredient_concentration_curation")
ACTION = "CORRECTED_EXTRACTION_INPUT_BOUNDARIES"
COHORT = {
    "12": {
        "batch": "0000-0500",
        "plan_sha": "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c",
        "pdf_sha": "1b4394336f7ace4e09c66fc67ed2e745e3c633b725e436d94335b99289243580",
        "solution_id": 15,
        "input": (2083, "air-dried garden soil", 400),
        "agar": 15,
        "stock_name": "Clarified soil extract",
        "split": "Add 15.0 g agar per 1000 ml to the clear supernatant solution thus obtained.",
    },
    "657": {
        "batch": "0500-1000",
        "plan_sha": "bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147",
        "pdf_sha": "eb788e7b0ce8da48e2699a178dac7fdc2f6b0a49742fb69e3e7595b8c1624930",
        "solution_id": 1388,
        "input": (2131, "Dry cow-manure", 50),
        "agar": 20,
        "stock_name": "Filtered manure extract",
        "split": "Add 20 g agar.",
    },
}
WITHDRAWAL = "The former main-medium concentration is withdrawn; the source supports an extraction input amount, not a finished-medium concentration or dissolved yield."
AGAR_SCOPE = "The agar concentration is retained and relocated, with its denominator scoped to recovered extract rather than the extraction starting water."


def build(doc, raw, meta, mid, timestamp):
    require(mid in COHORT, "Unreviewed extraction source")
    spec = COHORT[mid]
    require(not list(validate_recipe(doc, target_class="MediaRecipe")), "Baseline schema failure")
    data = json.loads(raw)["data"]
    medium, solutions = data["medium"], data["solutions"]
    require(str(medium["id"]) == mid and medium["source"] == "DSMZ", "Source identity drift")
    require(medium["link"] == PDF.format(mid), "Original source link drift")
    require(
        doc["original_name"] == medium["name"]
        and doc["media_term"]["term"] == {"id": "mediadive.medium:" + mid, "label": medium["name"]},
        "Local source identity drift",
    )
    require(medium["link"] in doc["notes"], "Local source link drift")
    require(not doc.get("solutions") and not doc.get("variants"), "Unreviewed stocks/variants")
    require(
        len(solutions) == 1
        and solutions[0]["id"] == spec["solution_id"]
        and solutions[0]["name"] == "Main sol. " + mid,
        "Source recipe boundary drift",
    )
    main = solutions[0]
    rows = main["recipe"]
    expected = [spec["input"], (322, "Tap water", 1000), (3, "Agar", spec["agar"])]
    require(len(rows) == len(doc["ingredients"]) == 3, "Ingredient inventory drift")
    for i, (row, (cid, label, amount)) in enumerate(zip(rows, expected, strict=True)):
        require(
            (row["compound_id"], row["compound"], row["amount"]) == (cid, label, amount),
            "Source ingredient/amount drift",
        )
        require(
            row["unit"] == ("ml" if i == 1 else "g")
            and row.get("optional") == 0
            and not any(row.get(k) for k in ("attribute", "condition", "solution_id")),
            "Ambiguous source row",
        )
        node = doc["ingredients"][i]
        require(
            node["preferred_term"] == label
            and node.get("concentration") == {"value": str(amount), "unit": "G_PER_L"},
            "Local ingredient/quantity drift",
        )
        require(not node.get("notes") and not node.get("modifier"), "Unreviewed ingredient context")
    require(
        main["volume"] == 1000 and len(main["steps"]) == len(doc["preparation_steps"]) == 1,
        "Preparation inventory drift",
    )
    text = main["steps"][0]["step"]
    require(text == doc["preparation_steps"][0]["description"], "Local/source preparation mismatch")
    prefix, separator, tail = text.partition(spec["split"])
    require(separator and text.count(separator) == 1, "Ambiguous preparation split")
    if mid == "12":
        require(
            "Centrifuge the supernatant." in prefix
            and tail.strip() == "Adjust pH to 6.8 - 7.0 and sterilize.",
            "Unreviewed soil extraction",
        )
    else:
        require(
            "Filter, first through cheesecloth and then paper. Make up volume to one liter."
            in prefix
            and not tail.strip(),
            "Unreviewed filtration/make-up",
        )
    after = copy.deepcopy(doc)
    solid, water, agar = after["ingredients"]
    solid.pop("concentration")
    solid["notes"] = (
        f"Extraction starting material: {spec['input'][2]} g in 1000 ml tap water. "
        "Solids are separated before the recovered extract is used. The source does not quantify retained solids or dissolved yield; no numeric extract concentration is asserted."
    )
    water["concentration"] = {"value": "1", "unit": "L"}
    water["notes"] = (
        "Initial extraction-water addition: 1000 ml / 1000 ml per L = 1 L, not a mass concentration or a measured recovered volume."
    )
    if mid == "657":
        water[
            "notes"
        ] += " The later make-up to one liter is a separate final-volume instruction; its additional water amount is unspecified."
    agar["notes"] = (
        "15 g per liter of clarified supernatant, not per liter of the starting soil suspension."
        if mid == "12"
        else "20 g added after the filtered extract is made up to one liter; no soil/manure concentration or extraction yield is inferred."
    )
    stock = {
        "preferred_term": spec["stock_name"],
        "source": PDF.format(mid),
        "notes": "Curator-described extraction stage, not a separately accessioned stock. Composition lists preparation inputs, not retained solutes. "
        + (
            "Recovered volume and an absolute extract dose are not specified; agar is dosed per liter of clarified supernatant."
            if mid == "12"
            else "The filtered extract is made up to one liter before agar is added. This is the prepared extract volume, not an extraction yield or a final agar-medium volume measurement."
        ),
        "composition": [solid, water],
        "preparation_notes": prefix.strip(),
    }
    if mid == "657":
        stock["concentration"] = {"value": "1", "unit": "L"}
    after["ingredients"] = [agar]
    after["solutions"] = [stock]
    after["preparation_steps"] = [
        {"step_number": 1, "action": "ADD_AGAR", "description": separator}
    ]
    if tail.strip():
        after["preparation_steps"].append(
            {"step_number": 2, "action": "ADJUST_PH", "description": tail.strip()}
        )
    reference = API + mid
    source_pointer = ["data", "solutions", 0, "steps", 0]
    step_quote = json_excerpt(raw, source_pointer)
    soil_path, water_path, agar_path = (
        ["solutions", 0, "composition", 0],
        ["solutions", 0, "composition", 1],
        ["ingredients", 0],
    )
    claims = []

    def claim(pointer, old_pointer, evidence_pointer, status, explanation, *, missing=False):
        claims.append(
            {
                "pointer": pointer,
                "old_pointer": old_pointer,
                "field": field_name(pointer),
                "old": copy.deepcopy(get_node(doc, old_pointer)) if old_pointer else None,
                "new": None if missing else copy.deepcopy(get_node(after, pointer)),
                "status": status,
                "reference": reference,
                "snippet": step_quote,
                "source_pointer": source_pointer,
                "locator": "$." + field_name(source_pointer),
                "evidence_pointer": evidence_pointer,
                "explanation": explanation,
            }
        )

    claim(
        soil_path + ["concentration"],
        ["ingredients", 0, "concentration"],
        soil_path,
        "correct",
        WITHDRAWAL,
        missing=True,
    )
    claim(
        soil_path + ["notes"],
        None,
        soil_path,
        "add",
        "The explicit starting mass is retained in notes because the schema has no absolute-mass unit; no extract concentration is invented.",
    )
    claim(
        water_path + ["concentration"],
        ["ingredients", 1, "concentration"],
        water_path,
        "correct",
        "1000 ml / 1000 ml per L = 1 L of initial preparation water; no density or final volume assumed.",
    )
    claim(
        water_path + ["notes"],
        None,
        water_path,
        "add",
        "Distinguish initial water from recovered liquid and any later make-up water.",
    )
    claim(
        agar_path + ["concentration"],
        ["ingredients", 2, "concentration"],
        agar_path,
        "verified",
        AGAR_SCOPE,
    )
    claim(
        agar_path + ["notes"],
        None,
        agar_path,
        "add",
        "The source identifies the preparation-stage denominator for agar.",
    )
    claim(
        ["solutions", 0, "preparation_notes"],
        ["preparation_steps", 0, "description"],
        [],
        "correct",
        "Move the exact extraction-stage text ahead of agar addition; preserve all source instructions.",
    )
    claim(
        ["solutions", 0, "notes"],
        None,
        [],
        "add",
        "Explicit preparation boundary; no invented stock accession or recovered-solute concentration.",
    )
    claim(
        ["preparation_steps"],
        ["preparation_steps"],
        [],
        "correct",
        "Separate extraction from agar addition; filtration through cloth/paper is not asserted to be sterile filtration.",
    )
    if mid == "657":
        claim(
            ["solutions", 0, "concentration"],
            None,
            [],
            "add",
            "The source explicitly makes the filtered extract up to one liter before adding agar. This is not inferred from starting water volume.",
        )

    resolutions = []
    for old_index, pointer, reason in [
        (0, soil_path, WITHDRAWAL),
        (1, water_path, "Initial extraction-water volume only."),
        (2, agar_path, AGAR_SCOPE),
    ]:
        node = get_node(after, pointer)
        prior = doc["ingredients"][old_index].get("evidence", [])
        require(
            len(prior) == (1 if old_index == 2 or (old_index == 0 and mid == "12") else 0),
            "Unreviewed existing evidence",
        )
        row_quote = json_excerpt(raw, ["data", "solutions", 0, "recipe", old_index])
        if prior:
            require(
                prior[0]["reference"] == reference and prior[0]["snippet"] == row_quote,
                "Prior evidence source drift",
            )
        fields = [c["field"] for c in claims if c["evidence_pointer"] == pointer]
        explanation = f"Extraction follow-up evidence for {', '.join(fields)}. {reason} "
        explanation += " ".join(
            c["explanation"]
            for c in claims
            if c["evidence_pointer"] == pointer and c["explanation"] != reason
        )
        explanation += f" Exact preparation excerpt at $.data.solutions[0].steps[0]: {step_quote}. Retrieved {meta['accessed_at']}; response SHA256={meta['sha256']}."
        node["evidence"] = [
            {
                "reference": reference,
                "supports": "SUPPORT",
                "snippet": row_quote,
                "explanation": explanation,
            }
        ]
        if prior:
            disposition = "withdrawn" if old_index == 0 else "relocated"
            resolutions.append(
                {
                    "from_pointer": ["ingredients", old_index],
                    "to_pointer": pointer,
                    "reference": reference,
                    "old_concentration": doc["ingredients"][old_index]["concentration"],
                    "disposition": disposition,
                    "new_field": field_name(
                        pointer + ["notes" if disposition == "withdrawn" else "concentration"]
                    ),
                    "source_pointer": source_pointer,
                    "source_snippet": step_quote,
                    "reason": reason,
                }
            )
    require(not after.get("evidence"), "Unreviewed root evidence")
    root_claims = [c for c in claims if not c["evidence_pointer"]]
    after["evidence"] = [
        {
            "reference": reference,
            "supports": "SUPPORT",
            "snippet": step_quote,
            "explanation": "Extraction-stage evidence for "
            + ", ".join(c["field"] for c in root_claims)
            + ". "
            + " ".join(c["explanation"] for c in root_claims)
            + f" Source locator=$.data.solutions[0].steps[0]; retrieved {meta['accessed_at']}; SHA256={meta['sha256']}.",
        }
    ]
    require(
        not any(r["reference"] == PDF.format(mid) for r in after.get("references", [])),
        "Existing original-recipe bibliography needs reconciliation",
    )
    after.setdefault("references", []).append(
        {
            "reference": PDF.format(mid),
            "title": f"DSMZ medium {mid}: {medium['name']}",
            "notes": f"source_type=culture_collection_page; discovery_mode=existing_record_reference; source_organization=DSMZ; accessed_on=2026-10-07; locator=page 1, complete recipe; PDF SHA256={spec['pdf_sha']}. Visually verified extraction stage against the exact API preparation text. Individual authors/publication year not established; copyright year is not used as publication year.",
        }
    )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        source=reference,
        timestamp=timestamp,
        notes="Original recipe visually verified. Removed unsupported extract-solids concentration; retained starting mass in notes; corrected initial water volume; reconciled earlier evidence scopes. No dissolved yield, density, or unspecified recovered volume inferred.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'], sort_keys=True)} -> {json.dumps(c['new'], sort_keys=True)} ({c['status']})"
            for c in claims
        ),
    )
    require(not list(validate_recipe(after, target_class="MediaRecipe")), "Proposed schema failure")
    return after, claims, resolutions


def process(root, source_dir, plan_path, mode):
    selected = []
    for mid, spec in COHORT.items():
        original = (
            root / REPORTS / f"20261007-mediadive-media-{spec['batch']}/plan.json"
        ).read_bytes()
        require(sha(original) == spec["plan_sha"], "Historical plan drift")
        matches = [r for r in json.loads(original)["records"] if r["medium_id"] == mid]
        require(len(matches) == 1, "Missing/duplicate historical target")
        selected.extend(matches)
        require(
            sha((source_dir / f"DSMZ_Medium{mid}.pdf").read_bytes()) == spec["pdf_sha"],
            "PDF capture drift",
        )
    tracked = set(
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root)
        .decode()
        .split("\0")
    )
    if mode == "preview":
        require(not plan_path.exists(), "Refuse to overwrite a reviewed plan")
        plan = {
            "version": 1,
            "action": ACTION,
            "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root)
            .decode()
            .strip(),
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "records": [],
        }
    else:
        plan = json.loads(plan_path.read_text())
        require(plan["version"] == 1 and plan["action"] == ACTION, "Wrong plan")
        require(
            [r["path"] for r in plan["records"]] == [r["path"] for r in selected],
            "Plan target drift",
        )
    rebuilt, writes = [], []
    for index, original in enumerate(selected):
        path, mid = root / original["path"], original["medium_id"]
        require(
            original["path"] in tracked and not path.is_symlink(), "Non-exact or symlink target"
        )
        current = path.read_bytes()
        before = current if mode == "preview" else plan["records"][index]["before_text"].encode()
        require(sha(before) == original["after_sha256"], "Unreviewed baseline drift")
        raw, meta = read_capture(source_dir / "sources", mid)
        require(meta["sha256"] == original["source_sha256"], "Source capture drift")
        doc = load_yaml(before)
        require(doc["id"] == original["id"], "Stable ID drift")
        after, claims, resolutions = build(doc, raw, meta, mid, plan["created_at"])
        output = render(before.decode(), after)
        rebuilt.append(
            {
                "path": original["path"],
                "id": original["id"],
                "medium_id": mid,
                "before_text": before.decode(),
                "before_sha256": sha(before),
                "after_text": output.decode(),
                "after_sha256": sha(output),
                "source_sha256": meta["sha256"],
                "source_accessed_at": meta["accessed_at"],
                "claims": claims,
                "claim_resolutions": resolutions,
                "action": ACTION,
            }
        )
        require(current in (before, output), "Concurrent edit")
        require(mode != "verify" or current == output, "Repair not applied")
        writes.append((path, current, output))
    if mode == "preview":
        plan["records"] = rebuilt
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        require(rebuilt == plan["records"], "Plan/source/decision drift")
        for path, current, _ in writes:
            require(path.read_bytes() == current, "Concurrent edit before write")
        for path, current, output in writes:
            require(path.read_bytes() == current, "Concurrent edit during write")
            if mode == "apply" and current != output:
                path.write_bytes(output)
            require(path.read_bytes() == output, "Persisted result differs")
    return plan, {
        "mode": mode,
        "records": len(writes),
        "changed": sum(a != b for _, a, b in writes) if mode == "apply" else 0,
        "already_applied": sum(a == b for _, a, b in writes),
        "scoped_claims": sum(len(r["claims"]) for r in rebuilt),
    }


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
        reports(args.reports, plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
