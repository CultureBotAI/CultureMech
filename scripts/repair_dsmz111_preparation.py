#!/usr/bin/env python3
"""Restore medium 111's glucose preparation without inventing final volumes."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz111-preparation"
ACTION = "RESTORED_DSMZ111_GLUCOSE_STOCK_AND_INPUT_BASES"
MEDIUM = "https://mediadive.dsmz.de/rest/medium/111"
SOLUTION = "https://mediadive.dsmz.de/rest/solution/190"
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf"
HASHES = {
    MEDIUM: "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b",
    SOLUTION: "37e247b4ac27dd60eddd8185e4ff45fb86dd4bf7d4c0406bb20203df7a79f3c9",
}
MAPPING_META = {
    "reference": MAPPING_URL,
    "http_status": 200,
    "accessed_at": "2026-10-07T13:01:23.350274+00:00",
    "sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a",
}
STEP = "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling."
GLUCOSE_STEP = "Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling."
TARGETS = {
    "dsmz": {
        "path": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "id": "CultureMech:000556",
        "before_sha256": "01ead4d30e8caa21abc37da645b39e5b502de62be10cc4fdbd3f7763a90cbc7e",
        "target_class": "MediaRecipe",
    },
    "komodo": {
        "path": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "id": "CultureMech:003822",
        "before_sha256": "f2030c44fd81edda9e86e1e80f3aec734f8983f82bdb26b261148c51bd6417c7",
        "target_class": "MediaRecipe",
    },
    "solution": {
        "path": "data/normalized_yaml/bacterial/mediadive_190_Main_sol_111.yaml",
        "id": "CultureMech:011325",
        "before_sha256": "588ea1e378113ec926ca7c79a4541a80be8c8ab79d1124dfb72f29c16046f7d0",
        "target_class": "SolutionRecipe",
    },
}
ROWS = [
    ("Glucose", 5, 10, "g", "10.5263"),
    ("K2HPO4", 10, 0.8, "g", "0.842105"),
    ("KH2PO4", 11, 0.2, "g", "0.210526"),
    ("MgSO4 x 7 H2O", 8, 0.1, "g", "0.105263"),
    ("FeSO4 x 7 H2O", 12, 20, "mg", "0.0210526"),
    ("MnSO4 x 6 H2O", 216, 2, "mg", "0.00210526"),
    ("ZnSO4 x 6 H2O", 217, 5, "mg", "0.00526316"),
    ("CuSO4 x 6 H2O", 218, 4, "mg", "0.00421053"),
    ("Na2MoO4 x 2 H2O", 9, 5, "mg", "0.00526316"),
    ("Agar", 3, 15, "g", "15.7895"),
    ("Distilled water", 4, 950, "ml", None),
]


def read_sources(medium_cache, solution_cache, mapping):
    sources = {}
    for reference, reader, cache, sid in (
        (MEDIUM, read_medium, medium_cache, "111"),
        (SOLUTION, read_solution, solution_cache, 190),
    ):
        raw, meta = reader(cache, sid)
        runner.require(meta["sha256"] == HASHES[reference], "Unreviewed source hash")
        sources[reference] = {"raw": raw, "metadata": meta}
    sources["mapping"] = read_mapping(mapping, MAPPING_META)["111"]
    sources["mapping_metadata"] = copy.deepcopy(MAPPING_META)
    check_sources(sources)
    return sources


def check_sources(sources):
    for reference in (MEDIUM, SOLUTION):
        source = sources[reference]
        runner.require(
            runner.sha(source["raw"].encode()) == HASHES[reference] == source["metadata"]["sha256"],
            "Source payload hash drift",
        )
    medium = json.loads(sources[MEDIUM]["raw"])["data"]
    solution = json.loads(sources[SOLUTION]["raw"])["data"]
    runner.require(
        medium["medium"]
        == {
            "id": 111,
            "name": "BEIJERINCKIA MEDIUM",
            "complex_medium": "no",
            "min_pH": 6.5,
            "max_pH": 6.5,
            "source": "DSMZ",
            "link": PDF,
        },
        "Medium identity/conditions drift",
    )
    runner.require(len(medium["solutions"]) == 1, "Medium topology drift")
    for data in (medium["solutions"][0], solution):
        runner.require(
            data["id"] == 190 and data["name"] == "Main sol. 111", "Solution identity drift"
        )
        runner.require(data["volume"] == 950 and len(data["recipe"]) == 11, "Recipe basis drift")
        runner.require([s["step"] for s in data["steps"]] == [STEP], "Preparation drift")
        for index, (row, expected) in enumerate(zip(data["recipe"], ROWS, strict=True)):
            name, cid, amount, unit, rate = expected
            runner.require(
                [row["compound"], row["compound_id"], row["amount"], row["unit"]]
                == [name, cid, amount, unit]
                and (None if row.get("g_l") is None else str(row["g_l"])) == rate
                and row["recipe_order"] == index + 1
                and row["optional"] == 0
                and not any(
                    row.get(k) for k in ("condition", "attribute", "solution", "solution_id")
                ),
                "Source ingredient/form/amount drift",
            )
    mapping = sources["mapping"]
    runner.require(
        mapping["medium_id"] == "111"
        and mapping["original_recipe"] == PDF
        and mapping["cells"][:3] == ["111", "BEIJERINCKIA MEDIUM", "6.5"],
        "Mapping identity drift",
    )


def build(before, key, sources, timestamp):
    check_sources(sources)
    spec = TARGETS[key]
    is_solution = key == "solution"
    root_field = "composition" if is_solution else "ingredients"
    reference = SOLUTION if is_solution else MEDIUM
    raw = sources[reference]["raw"]
    base = ["data"] if is_solution else ["data", "solutions", 0]
    step_pointer = base + ["steps", 0]
    step_quote = json_excerpt(raw, step_pointer)
    runner.require(before["id"] == spec["id"], "Record identity drift")
    runner.require(not runner.errors(before, spec["target_class"]), "Baseline schema failure")
    runner.require(
        not before.get("solutions") and not before.get("variants"), "Unreviewed topology"
    )
    if is_solution:
        runner.require(
            before["term"] == {"id": "mediadive.solution:190", "label": "Main sol. 111"},
            "Local source drift",
        )
        runner.require(
            before["preparation_notes"] == STEP + "\n\nOriginal volume: 950 mL",
            "Local preparation drift",
        )
    else:
        prefix = "komodo" if key == "komodo" else "mediadive"
        runner.require(
            before["media_term"]["term"]
            == {"id": prefix + ".medium:111", "label": "BEIJERINCKIA MEDIUM"},
            "Local source drift",
        )
        runner.require(
            before["ph_value"] == 6.5 and before["physical_state"] == "SOLID_AGAR",
            "Local conditions drift",
        )
        expected_steps = (
            []
            if key == "komodo"
            else [{"step_number": 1, "action": "ADJUST_PH", "description": STEP}]
        )
        runner.require(
            before.get("preparation_steps", []) == expected_steps, "Local preparation drift"
        )
    rows = before[root_field]
    runner.require(len(rows) == (11 if is_solution else 10), "Local inventory drift")
    for node, expected in zip(rows[:10], ROWS[:10], strict=True):
        runner.require(
            node["preferred_term"] == expected[0]
            and node["concentration"] == {"value": expected[4], "unit": "G_PER_L"},
            "Local ingredient/amount drift",
        )
        runner.require("notes" not in node, "Existing ingredient context needs reconciliation")

    after = copy.deepcopy(before)
    glucose = after[root_field].pop(0)
    glucose.pop("concentration")
    glucose["notes"] = (
        "Source batch input: 10 g glucose in 50 ml H2O, sterilized separately and mixed after cooling. "
        "The former 10.5263 g/L divides by the unrelated 950 ml basal-water input and is withdrawn. "
        "No 200 g/L stock strength or 10 g/L final-medium concentration is asserted: neither final volume is specified."
    )
    after["solutions"] = [
        {
            "preferred_term": "Separately sterilized glucose preparation",
            "composition": [glucose],
            "preparation_notes": GLUCOSE_STEP,
            "notes": "Mix the separately prepared glucose with the cooled basal preparation. The 50 ml is water input, not a measured stock volume or a per-liter dose; no numeric stock addition concentration is asserted.",
            "source": reference,
        }
    ]
    if is_solution:
        runner.require("source_data" not in after, "Existing provenance needs reconciliation")
        after["source_data"] = {"origin": "MediaDive"}
    evidence_root = ["source_data"] if is_solution else []
    claims, resolutions = [], []

    def claim(
        pointer, old_pointer, status, source_pointer, explanation, evidence_pointer, ingredient
    ):
        value = runner.get_node(after, pointer)
        old = runner.get_node(before, old_pointer) if old_pointer is not None else None
        item = {
            "pointer": pointer,
            "old_pointer": old_pointer,
            "field": runner.field_name(pointer),
            "ingredient": ingredient,
            "old": copy.deepcopy(old),
            "new": copy.deepcopy(value),
            "status": status,
            "reference": reference,
            "source_pointer": source_pointer,
            "snippet": json_excerpt(raw, source_pointer),
            "locator": "$." + runner.field_name(source_pointer),
            "explanation": explanation,
            "evidence_pointer": evidence_pointer,
        }
        claims.append(item)
        return item

    for index, expected in enumerate(ROWS[:10]):
        pointer = ["solutions", 0, "composition", 0] if index == 0 else [root_field, index - 1]
        node = runner.get_node(after, pointer)
        if index:
            node["notes"] = (
                f"Source batch input: {expected[2]} {expected[3]}. The retained {expected[4]} g/L is the "
                "provider-declared rate normalized to its 950 ml main-preparation field, not an independently "
                "verified concentration after adding the separately prepared glucose. No final volume is inferred."
            )
        field = pointer + ["notes" if index == 0 else "concentration"]
        reason = (
            "Withdraw the table-derived glucose rate and retain the supported mass at its separate preparation stage."
            if index == 0
            else "Retain the provider-declared basal rate with its batch input and preparation-stage limitation; reindex the evidence scope."
        )
        c = claim(
            field,
            [root_field, index, "concentration"],
            "withdraw" if index == 0 else "evidence_only",
            base + ["recipe", index],
            reason + " " + node["notes"],
            pointer,
            expected[0],
        )
        c["extra_excerpts"] = [
            {"snippet": step_quote, "locator": "$." + runner.field_name(step_pointer)}
        ]
        c["explanation"] += (
            " Additional exact preparation excerpt at $."
            + runner.field_name(step_pointer)
            + ": "
            + step_quote
        )
        if key != "komodo":
            resolutions.append(
                {
                    "from_pointer": [root_field, index],
                    "to_pointer": pointer,
                    "reference": reference,
                    "disposition": "withdrawn" if index == 0 else "relocated",
                    "old_concentration": copy.deepcopy(rows[index]["concentration"]),
                    "new_field": c["field"],
                    "source_pointer": step_pointer,
                    "source_snippet": step_quote,
                    "reason": reason,
                }
            )

    if is_solution:
        water = after[root_field][-1]
        runner.require(
            water["preferred_term"] == "Distilled water"
            and water["concentration"] == {"value": "1000.0", "unit": "PERCENT_V_V"},
            "Local water drift",
        )
    else:
        water = {
            "preferred_term": "Distilled water",
            "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
        }
        after[root_field].append(water)
    water["concentration"] = {"value": "0.95", "unit": "L"}
    water["notes"] = (
        "950 ml distilled-water input per basal batch, not a final-volume makeup instruction."
    )
    claim(
        [root_field, 9, "concentration"],
        [root_field, 10, "concentration"] if is_solution else None,
        "correct" if is_solution else "add",
        base + ["recipe", 10],
        "950 ml / 1000 ml per L = 0.95 L water input per prepared batch; no percentage or final volume inferred. Supports the water label and input-basis note too.",
        [root_field, 9],
        "Distilled water",
    )
    stock_water = {
        "preferred_term": "Water",
        "concentration": {"value": "0.05", "unit": "L"},
        "notes": "50 ml H2O input for the separately sterilized glucose; water purity and final stock volume are not specified.",
    }
    after["solutions"][0]["composition"].append(stock_water)
    claim(
        ["solutions", 0, "composition", 1, "concentration"],
        None,
        "add",
        step_pointer,
        "50 ml / 1000 ml per L = 0.05 L water input, not 0.05 L of final stock or a 50 ml/L dose. H2O does not establish distilled-water purity.",
        ["solutions", 0, "composition", 1],
        "Water",
    )
    after["notes"] = (
        before.get("notes", "")
        + "\n\n"
        + "Preparation scope: basal input is 950 ml distilled water plus the listed salts and agar; glucose (10 g in 50 ml H2O) is sterilized separately and mixed after cooling. "
        "The retained basal g/L values are provider-reported normalizations, not final-medium concentrations. "
        "The two water inputs do not establish a measured 1 L final volume. Historical import annotations and ontology mappings are retained, not revalidated."
    ).lstrip()
    claim(
        ["notes"],
        ["notes"] if "notes" in before else None,
        "correct_scope",
        step_pointer,
        "Preparation-stage qualification for the parent record; water input amount is independently quoted on its ingredient.",
        evidence_root,
        "Preparation scope",
    )
    for field in ("preferred_term", "preparation_notes", "notes", "source"):
        claim(
            ["solutions", 0, field],
            None,
            "restore_stock",
            step_pointer,
            "Source-explicit separate glucose preparation; its name is a curator label, not a new source accession. No numeric stock dose, sterilization method, temperature or final volume is inferred.",
            evidence_root,
            "Glucose preparation",
        )
    if key == "komodo":
        after["preparation_steps"] = [
            {"step_number": 1, "action": "ADJUST_PH", "description": STEP}
        ]
        claim(
            ["preparation_steps"],
            None,
            "restore_preparation",
            step_pointer,
            "Restore the linked recipe's verbatim instruction, including pH and separate glucose sterilization; no sterilization method is supplied.",
            evidence_root,
            "Preparation",
        )

    grouped = {}
    for c in claims:
        grouped.setdefault(tuple(c["evidence_pointer"]), []).append(c)
    for pointer, group in grouped.items():
        node = runner.get_node(after, pointer)
        entries = [e for e in node.get("evidence", []) if e["reference"] == reference]
        runner.require(len(entries) <= 1, "Duplicate evidence")
        explanations = [
            f"{c['field']} ({c['status']}), locator={c['locator']}: {c['explanation']}"
            + (
                f" Additional exact excerpt: {c['snippet']}"
                if i and c["snippet"] != group[0]["snippet"]
                else ""
            )
            for i, c in enumerate(group)
        ]
        explanations.append(
            f"Retrieved {sources[reference]['metadata']['accessed_at']}; response SHA256={HASHES[reference]}. Original DSMZ 111 PDF inspected separately. Chemical mappings are unchanged, not independently validated."
        )
        if entries:
            entry = entries[0]
            runner.require(entry["snippet"] == group[0]["snippet"], "Historical quote drift")
            historical = entry["explanation"]
            entry["explanation"] = (
                " ".join(explanations)
                + " Historical explanation (superseded where its stage/scope differs): "
                + historical
            )
        else:
            node.setdefault("evidence", []).append(
                {
                    "reference": reference,
                    "supports": "SUPPORT",
                    "snippet": group[0]["snippet"],
                    "explanation": " ".join(explanations),
                }
            )
    references = [
        (
            reference,
            (
                "MediaDive solution 190: Main sol. 111"
                if is_solution
                else "MediaDive medium 111: BEIJERINCKIA MEDIUM"
            ),
            "dataset",
        ),
        (PDF, "DSMZ 111. BEIJERINCKIA MEDIUM", "culture_collection_page"),
    ]
    if key == "komodo":
        after.setdefault("evidence", []).append(
            {
                "reference": MAPPING_URL,
                "supports": "SUPPORT",
                "snippet": sources["mapping"]["snippet"],
                "explanation": f"Identity only: KOMODO 111 maps to {PDF}; locator=MediaList row ID 111. No ingredient amounts or growth claims are inferred from this mapping. Retrieved {MAPPING_META['accessed_at']}; response SHA256={MAPPING_META['sha256']}.",
            }
        )
        references.append((MAPPING_URL, "KOMODO media list: original-recipe mappings", "dataset"))
    for ref, title, kind in references:
        if any(r["reference"] == ref for r in after.get("references", [])):
            continue
        after.setdefault("references", []).append(
            {
                "reference": ref,
                "title": title,
                "notes": f"source_type={kind}; discovery_mode={'cross_reference' if key == 'komodo' else 'existing_record_reference'}; accessed_on=2026-10-07; individual authors and publication year not established; PDF copyright year is not a publication date. "
                + (
                    f"response_sha256={HASHES[ref]}"
                    if ref in HASHES
                    else (
                        f"response_sha256={MAPPING_META['sha256']}"
                        if ref == MAPPING_URL
                        else "Original one-page recipe inspected; table and separate-glucose instruction agree with the captured API."
                    )
                ),
            }
        )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="; ".join([reference, PDF] + ([MAPPING_URL] if key == "komodo" else [])),
        notes="Restored separate glucose preparation, withdrew its wrongly staged 10.5263 g/L slot, and distinguished water inputs from final volumes. Preserved all previous history, source snippets, identifiers, mappings and variant links. Basal provider rates remain explicitly scoped; no growth association added.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'])} -> {json.dumps(c['new'])} ({c['status']})"
            for c in claims
        ),
    )
    runner.require(not runner.errors(after, spec["target_class"]), "Proposed schema failure")
    return after, claims, resolutions


def process(root, medium_cache, solution_cache, mapping, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    sources = read_sources(medium_cache, solution_cache, mapping)
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse to overwrite reviewed plan")
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
            plan["version"] == 1
            and plan["action"] == ACTION
            and plan["sources"] == sources
            and [r["key"] for r in plan["records"]] == list(TARGETS),
            "Frozen plan/source drift",
        )
    items, pending = [], []
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
        items.append(
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
        runner.require(items == plan["records"], "Frozen plan/decision drift")
    plan["records"] = items
    runner.safe_targets(root, plan)
    runner.require(
        all(p.read_bytes() == current and not p.is_symlink() for p, current, _ in pending),
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
        "records": len(items),
        "changed": sum(c != o for _, c, o in pending) if mode == "apply" else 0,
        "already_applied": sum(c == o for _, c, o in pending),
        "scoped_claims": sum(len(r["claims"]) for r in items),
    }


def report(folder, plan, applied):
    for item in plan["records"]:
        lines = [
            "# Medium 111 Preparation Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "This hash-linked correction supplements the existing per-record report; it adds no unique reviewed path. Baseline/proposed schema checks pass. Wider validation and limitations are in README.md and validation.json.",
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
        reference = SOLUTION if item["key"] == "solution" else MEDIUM
        for field, ingredient in (
            ("solutions[0].composition[0].concentration", "Glucose stock strength"),
            ("solutions[0].concentration", "Glucose stock addition dose"),
        ):
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(v)
                    for v in (
                        field,
                        ingredient,
                        None,
                        None,
                        "unsupported",
                        reference,
                        STEP,
                        (
                            "$.data.steps[0]"
                            if item["key"] == "solution"
                            else "$.data.solutions[0].steps[0]"
                        ),
                        "Source gives mass and water input, not final stock volume or a per-liter working dose; left unasserted.",
                    )
                )
                + " |"
            )
        if item["key"] == "solution":
            lines.append(
                "| ingredients[0].concentration | Legacy placeholder | variable / VARIABLE | variable / VARIABLE | unsupported | unknown | unknown | unknown | Unchanged import placeholder, not verified composition. |"
            )
        lines += [
            "",
            "Final stock volume, numeric stock dose, final-medium volume and final-medium concentrations remain unverified. Retained basal rates quote the provider, not an independently measured final preparation.",
        ]
        if item["key"] == "solution":
            lines += [
                "The legacy ingredients[0] placeholder (variable / VARIABLE) and incomplete_composition flag remain unchanged and unsupported; authoritative chemical composition is in composition and solutions. No evidence is claimed for the placeholder."
            ]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / (item["key"] + "-followup.md")).write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--medium-cache", type=Path, required=True)
    parser.add_argument("--solution-cache", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    flags = parser.add_mutually_exclusive_group()
    flags.add_argument("--apply", action="store_true")
    flags.add_argument("--verify", action="store_true")
    flags.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(
        ROOT, args.medium_cache, args.solution_cache, args.mapping, args.plan, mode
    )
    if args.reports:
        report(args.reports, plan, mode != "preview")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
