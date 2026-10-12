#!/usr/bin/env python3
"""Preserve medium 125's alternative carbon preparations and batch water input."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner
from fetch_medium_concentration_sources import read_capture as read_medium
from fetch_solution_concentration_sources import read_capture as read_solution
from inventory_komodo_concentration_sources import MAPPING_URL, read_mapping
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz125-alternatives"
ACTION = "RESTORED_DSMZ125_ALTERNATIVE_CARBON_PREPARATIONS_AND_WATER_INPUT"
MEDIUM = "https://mediadive.dsmz.de/rest/medium/125"
SOLUTION = "https://mediadive.dsmz.de/rest/solution/223"
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium125.pdf"
STEP = "Add 5 ml methanol or incubate under methane-air (4:1). Adjust pH to 6.8."
PH_STEP = "Adjust pH to 6.8."
HASHES = {
    MEDIUM: "2ccb593505b6c8f5cd63fd63bf1ecee7b33357bca201285eb2e958b70aff5ba1",
    SOLUTION: "6f4797edabe8f2eb226a01b58ddc3e4c931f0e5b572ca01843860ecad4eb02ac",
}
MAPPING_META = {
    "reference": MAPPING_URL,
    "http_status": 200,
    "accessed_at": "2026-10-07T13:01:23.350274+00:00",
    "sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a",
}
TARGETS = {
    "dsmz": {
        "path": "data/normalized_yaml/bacterial/methylobacterium_medium.yaml",
        "id": "CultureMech:000718",
        "before_sha256": "06a56a51606291dff6ad45dc6dda946374bcc859051ee7e3f570a7fb86de54bf",
        "target_class": "MediaRecipe",
    },
    "komodo": {
        "path": "data/normalized_yaml/bacterial/KOMODO_125_METHYLOBACTERIUM_MEDIUM.yaml",
        "id": "CultureMech:004018",
        "before_sha256": "457b495125f8596c5f05f8a91651c47a9920ba067adee28079c249b5a9f3b867",
        "target_class": "MediaRecipe",
    },
    "solution": {
        "path": "data/normalized_yaml/bacterial/mediadive_223_Main_sol_125.yaml",
        "id": "CultureMech:011631",
        "before_sha256": "06f75dc8280f54ae6e74e0875af3ad3229d5c22a8fe62d2d2fe2b8892f1a1f3c",
        "target_class": "SolutionRecipe",
    },
}
ROWS = [
    ("KNO3", 191, 1, "g", "1"),
    ("MgSO4 x 7 H2O", 8, 0.2, "g", "0.2"),
    ("CaCl2 x 2 H2O", 7, 0.02, "g", "0.02"),
    ("Na2HPO4", 233, 0.23, "g", "0.23"),
    ("NaH2PO4", 229, 0.07, "g", "0.07"),
    ("FeSO4 x 7 H2O", 12, 1, "mg", "0.001"),
    ("CuSO4 x 5 H2O", 121, 5, "\u00b5g", "0.000005"),
    ("H3BO3", 37, 10, "\u00b5g", "0.00001"),
    ("MnSO4 x 5 H2O", 234, 10, "\u00b5g", "0.00001"),
    ("ZnSO4 x 7 H2O", 35, 70, "\u00b5g", "0.00007"),
    ("MoO3", 235, 10, "\u00b5g", "0.00001"),
    ("Agar", 3, 12, "g", "12"),
    ("Distilled water", 4, 1000, "ml", None),
]
CONTEXT = (
    "Common basal table for two source-listed alternative preparations: add 5 ml methanol "
    "or incubate under methane-air (4:1). Neither alternative is selected or combined here. "
    "The retained g/L entries are provider-declared basal-table rates, not independently "
    "verified final concentrations after choosing a carbon preparation. The 1000 ml water "
    "entry is a batch input, not a measured final volume. Methanol purity, final volume, "
    "methanol final concentration and dissolved methane concentration remain unspecified. "
    "Existing chemical mappings and strain-modified source-duplicate links are preserved, "
    "not newly validated by this recipe evidence."
)
WATER_NOTE = "Batch distilled-water input: 1000 ml = 1 L; not a percentage or a measured final medium volume."


def read_sources(medium_cache, solution_cache, mapping):
    sources = {}
    for reference, reader, cache, sid in (
        (MEDIUM, read_medium, medium_cache, "125"),
        (SOLUTION, read_solution, solution_cache, 223),
    ):
        raw, metadata = reader(cache, sid)
        sources[reference] = {"raw": raw, "metadata": metadata}
    sources["mapping"] = read_mapping(mapping, MAPPING_META)["125"]
    sources["mapping_metadata"] = copy.deepcopy(MAPPING_META)
    check_sources(sources)
    return sources


def check_sources(sources):
    for reference in (MEDIUM, SOLUTION):
        entry = sources[reference]
        runner.require(
            runner.sha(entry["raw"].encode()) == entry["metadata"]["sha256"] == HASHES[reference],
            "Source payload hash drift",
        )
        runner.require(
            entry["metadata"]["url"] == entry["metadata"]["response_url"] == reference
            and entry["metadata"]["http_status"] == 200,
            "Source origin drift",
        )
    medium = json.loads(sources[MEDIUM]["raw"])["data"]
    solution = json.loads(sources[SOLUTION]["raw"])["data"]
    runner.require(
        medium["medium"]
        == {
            "id": 125,
            "name": "METHYLOBACTERIUM MEDIUM",
            "complex_medium": "no",
            "min_pH": 6.8,
            "max_pH": 6.8,
            "source": "DSMZ",
            "link": PDF,
        },
        "Medium identity drift",
    )
    runner.require(len(medium["solutions"]) == 1, "Source topology drift")
    for data in (medium["solutions"][0], solution):
        runner.require(
            data["id"] == 223 and data["name"] == "Main sol. 125", "Solution identity drift"
        )
        runner.require(data["volume"] == 1000 and len(data["recipe"]) == 13, "Recipe basis drift")
        runner.require([r["step"] for r in data["steps"]] == [STEP], "Preparation drift")
        for i, (row, expected) in enumerate(zip(data["recipe"], ROWS, strict=True)):
            name, cid, amount, unit, rate = expected
            runner.require(
                [row["compound"], row["compound_id"], row["amount"], row["unit"]]
                == [name, cid, amount, unit]
                and (None if row.get("g_l") is None else Decimal(str(row["g_l"])))
                == (None if rate is None else Decimal(rate))
                and row["recipe_order"] == i + 1
                and row["optional"] == 0
                and not any(
                    row.get(k) for k in ("condition", "attribute", "solution", "solution_id")
                ),
                "Source ingredient/form/amount drift",
            )
    mapping = sources["mapping"]
    runner.require(
        mapping["medium_id"] == "125"
        and mapping["original_recipe"] == PDF
        and mapping["cells"][:3] == ["125", "METHYLOBACTERIUM MEDIUM", "6.8"],
        "Mapping identity drift",
    )


def build(before, key, sources, timestamp):
    check_sources(sources)
    spec = TARGETS[key]
    solution = key == "solution"
    field = "composition" if solution else "ingredients"
    reference = SOLUTION if solution else MEDIUM
    raw = sources[reference]["raw"]
    base = ["data"] if solution else ["data", "solutions", 0]
    step_locator = "$.data.steps[0].step" if solution else "$.data.solutions[0].steps[0].step"
    runner.require(
        before["id"] == spec["id"] and not runner.errors(before, spec["target_class"]),
        "Record identity/schema drift",
    )
    runner.require(
        not before.get("variants") and not before.get("solutions"), "Unreviewed topology"
    )
    if solution:
        runner.require(
            before["term"] == {"id": "mediadive.solution:223", "label": "Main sol. 125"}
            and before["preparation_notes"] == STEP,
            "Local source/preparation drift",
        )
    else:
        prefix = "komodo" if key == "komodo" else "mediadive"
        runner.require(
            before["media_term"]["term"]
            == {"id": prefix + ".medium:125", "label": "METHYLOBACTERIUM MEDIUM"}
            and before["ph_value"] == 6.8
            and before["physical_state"] == "SOLID_AGAR",
            "Local source/conditions drift",
        )
        expected = (
            []
            if key == "komodo"
            else [{"step_number": 1, "action": "ADJUST_PH", "description": STEP}]
        )
        runner.require(before.get("preparation_steps", []) == expected, "Local preparation drift")
    runner.require(len(before[field]) == (13 if solution else 12), "Local inventory drift")
    after = copy.deepcopy(before)
    claims = []

    def evidence(snippet, explanation):
        runner.require(snippet in raw, "Nonliteral source snippet")
        return {
            "reference": reference,
            "supports": "SUPPORT",
            "snippet": snippet,
            "explanation": explanation
            + f" Retrieved {sources[reference]['metadata']['accessed_at']}; response SHA256={HASHES[reference]}.",
        }

    def claim(path, ingredient, old, new, status, ev, locator):
        claims.append(
            {
                "field": path,
                "ingredient": ingredient,
                "old": old,
                "new": new,
                "status": status,
                "reference": ev["reference"],
                "snippet": ev["snippet"],
                "locator": locator,
                "explanation": ev["explanation"],
            }
        )

    for i, (name, cid, amount, unit, rate) in enumerate(ROWS[:12]):
        node = after[field][i]
        runner.require(
            node["preferred_term"] == name
            and node["concentration"]["unit"] == "G_PER_L"
            and Decimal(str(node["concentration"]["value"])) == Decimal(rate),
            "Local ingredient/rate drift",
        )
        if solution:
            runner.require(
                node["term"]["id"] == f"mediadive.compound:{cid}", "Compound identity drift"
            )
        snippet = json_excerpt(raw, base + ["recipe", i])
        locator = ("$.data.recipe" if solution else "$.data.solutions[0].recipe") + f"[{i}]"
        ev = evidence(
            snippet,
            f"Basal-table evidence for {field}[{i}].concentration ({name}): source input {amount} {unit}, provider-reported {rate} g/L, normalized by the provider's 1000 ml main-preparation field. {CONTEXT} Locator={locator}.",
        )
        if key == "komodo":
            runner.require(not node.get("evidence"), "Unreviewed previous evidence")
            node["evidence"] = [ev]
        else:
            runner.require(
                len(node["evidence"]) == 1
                and node["evidence"][0]["reference"] == reference
                and node["evidence"][0]["snippet"] == snippet,
                "Historical evidence drift",
            )
        claim(
            f"{field}[{i}].concentration",
            name,
            node["concentration"],
            node["concentration"],
            "evidence_only" if key == "komodo" else "verified",
            ev,
            locator,
        )

    if solution:
        water = after[field][12]
        runner.require(
            water["preferred_term"] == "Distilled water"
            and water["term"]["id"] == "mediadive.compound:4"
            and water["concentration"] == {"value": "1000", "unit": "PERCENT_V_V"}
            and not water.get("evidence")
            and not water.get("notes"),
            "Water baseline drift",
        )
    else:
        water = {
            "preferred_term": "Distilled water",
            "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
        }
        after[field].append(water)
    old_water = copy.deepcopy(water.get("concentration"))
    water["concentration"] = {"value": "1", "unit": "L"}
    water["notes"] = WATER_NOTE
    water_ev = evidence(
        json_excerpt(raw, base + ["recipe", 12]),
        f"{field}[12].concentration: {WATER_NOTE} Conversion: 1000 ml / 1000 ml per L = 1 L. The source supplies no water percentage or measured final volume after methanol addition. Chemical mappings retained without new validation.",
    )
    water["evidence"] = [water_ev]
    claim(
        f"{field}[12].concentration",
        "Distilled water",
        old_water,
        water["concentration"],
        "correct" if solution else "add",
        water_ev,
        ("$.data.recipe[12]" if solution else "$.data.solutions[0].recipe[12]"),
    )

    prep_ev = evidence(
        STEP,
        f"Source-listed alternatives, not simultaneous components. {CONTEXT} Locator={step_locator}.",
    )
    if solution:
        runner.require("source_data" not in after, "Unreviewed source provenance")
        after["source_data"] = {"origin": "MediaDive", "evidence": [prep_ev]}
    else:
        runner.require(not after.get("evidence"), "Unreviewed root evidence")
        after["evidence"] = [prep_ev]
        after["preparation_steps"] = [
            {"step_number": 1, "action": "ADJUST_PH", "description": PH_STEP}
        ]
        alternatives = [
            {
                "name": "Methanol preparation option",
                "relationship": "SUPPLEMENTED_VARIANT",
                "description": "Source-listed methanol alternative to methane-air incubation; common basal table unchanged.",
                "modifications": [
                    "Add 5 ml methanol to the source's common basal batch; do not combine this option with the methane-air alternative.",
                    "This is a batch addition, not 5 ml/L or 0.5% final-medium methanol; final volume and methanol purity are not specified.",
                ],
                "purpose": "Represent the source-listed methanol preparation without choosing it for every use.",
                "evidence": [copy.deepcopy(prep_ev)],
            },
            {
                "name": "Methane-air incubation option",
                "relationship": "DERIVED_FROM",
                "description": "Source-listed incubation alternative to methanol addition; common basal table unchanged.",
                "modifications": [
                    "Incubate under methane-air (4:1) as the alternative to adding methanol.",
                    "The gas ratio is not a liquid ingredient dose or a dissolved methane concentration; no gas pressure or total volume is specified.",
                ],
                "purpose": "Represent the source-listed methane-air alternative without asserting a dissolved carbon concentration.",
                "evidence": [copy.deepcopy(prep_ev)],
            },
        ]
        for i, variant in enumerate(alternatives):
            variant["evidence"][0]["explanation"] = (
                f"variants[{i}] ({variant['name']}): " + prep_ev["explanation"]
            )
            claim(
                f"variants[{i}]",
                variant["name"],
                None,
                variant["modifications"],
                "add",
                variant["evidence"][0],
                step_locator,
            )
        after["variants"] = alternatives
        claim(
            "preparation_steps",
            "Common pH instruction",
            before.get("preparation_steps"),
            after["preparation_steps"],
            "add" if key == "komodo" else "correct",
            prep_ev,
            step_locator,
        )
    after["notes"] = (before.get("notes", "") + "\n\n" + CONTEXT).strip()
    if key == "komodo":
        after[
            "notes"
        ] += " The imported 'Aerobic: No' annotation is retained as unverified metadata, not used to select either preparation."
        mapping_ev = {
            "reference": MAPPING_URL,
            "supports": "SUPPORT",
            "snippet": sources["mapping"]["snippet"],
            "explanation": "Exact KOMODO accession 125 links to DSMZ Medium125.pdf and names METHYLOBACTERIUM MEDIUM. Identity only: this table does not verify quantities, strain-modified variants, growth, or atmosphere. Captured "
            + MAPPING_META["accessed_at"]
            + "; SHA256="
            + MAPPING_META["sha256"]
            + ".",
        }
        after["evidence"].append(mapping_ev)
    claim(
        "notes and preparation evidence",
        "Alternative preparation scope",
        before.get("notes"),
        after["notes"],
        "evidence_only",
        prep_ev,
        step_locator,
    )
    references = after.setdefault("references", [])
    if key == "komodo":
        references.append(
            {
                "reference": MEDIUM,
                "title": "MediaDive medium 125: METHYLOBACTERIUM MEDIUM",
                "notes": f"source_type=dataset; discovery_mode=cross_reference; accessed_on=2026-10-07; response_sha256={HASHES[MEDIUM]}; original_recipe={PDF}; individual authors and publication year not supplied.",
            }
        )
        references.append(
            {
                "reference": MAPPING_URL,
                "title": "KOMODO media list: exact accession 125",
                "notes": f"source_type=web_page; discovery_mode=cross_reference; accessed_on=2026-10-07; response_sha256={MAPPING_META['sha256']}; identity mapping only; authors and publication year not supplied.",
            }
        )
    references.append(
        {
            "reference": PDF,
            "title": "DSMZ Medium 125: METHYLOBACTERIUM MEDIUM",
            "notes": "source_type=culture_collection_page; discovery_mode=existing_record_reference; accessed_on=2026-10-07; one-page official recipe manually inspected; basal table and alternative preparation instruction agree with the captured API. No DOI, individual author or publication year supplied; copyright year not used as publication year.",
        }
    )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="; ".join([reference, PDF] + ([MAPPING_URL] if key == "komodo" else [])),
        notes="Preserved basal provider rates and prior evidence. Corrected/restored batch water input and represented alternative carbon preparations without inferring final volume, methane dissolution or methanol concentration. Preserved IDs, chemical mappings, history and source-duplicate links; no growth association added.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'])} -> {json.dumps(c['new'])} ({c['status']})"
            for c in claims
            if c["status"] != "verified"
        ),
    )
    runner.require(not runner.errors(after, spec["target_class"]), "Proposed schema failure")
    return after, claims


def process(root, medium_cache, solution_cache, mapping, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    sources = read_sources(medium_cache, solution_cache, mapping)
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse to overwrite reviewed plan")
        plan = {
            "version": 1,
            "action": ACTION,
            "sources": sources,
            "commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=root, text=True
            ).strip(),
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
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
    for i, (key, spec) in enumerate(TARGETS.items()):
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target")
        current = path.read_bytes()
        before = current if mode == "preview" else plan["records"][i]["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
        after, claims = build(runner.load_yaml(before), key, sources, plan["created_at"])
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
                "claims": claims,
                "claim_resolutions": [],
                "source_sha256": HASHES[SOLUTION if key == "solution" else MEDIUM],
            }
        )
        pending.append((path, current, output))
    if mode != "preview":
        runner.require(items == plan["records"], "Frozen plan/decision drift")
    plan["records"] = items
    runner.safe_targets(root, plan)
    runner.require(
        all(p.read_bytes() == old and not p.is_symlink() for p, old, _ in pending),
        "Concurrent edit before write",
    )
    if mode == "preview":
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        for path, old, output in pending:
            runner.require(
                path.read_bytes() == old and not path.is_symlink(), "Concurrent edit during write"
            )
            if mode == "apply" and old != output:
                path.write_bytes(output)
            runner.require(path.read_bytes() == output, "Result not applied")
    return plan, {
        "mode": mode,
        "records": len(items),
        "changed": sum(old != new for _, old, new in pending) if mode == "apply" else 0,
        "already_applied": sum(old == new for _, old, new in pending),
        "scoped_claims": sum(len(r["claims"]) for r in items),
    }


def reports(folder, plan, applied):
    folder.mkdir(parents=True, exist_ok=True)
    for item in plan["records"]:
        lines = [
            "# Medium 125 Alternatives Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "This hash-linked follow-up supplements the existing per-record report; it adds no unique reviewed path. Validation details and unresolved claims are in README.md and validation.json.",
            "",
            "| Field | Ingredient | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for claim in item["claims"]:
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(claim[k])
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
        if item["key"] == "solution":
            lines += [
                "| ingredients[0].concentration | Legacy placeholder | variable / VARIABLE | unchanged | unsupported | unknown | unknown | unknown | Not composition evidence; preserved with its legacy quality flag. |",
                "",
                "Standalone working dose is unspecified; no receiving-medium concentration is added.",
            ]
        lines += [
            "",
            "Unresolved: measured final volume, methanol final concentration/purity, dissolved methane concentration, gas pressure and total gas volume. The source's 5 ml batch addition is not a final-medium rate. No growth claim or strain-specific variant applicability is inferred.",
        ]
        (folder / (item["key"] + "-followup.md")).write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("medium-cache", "solution-cache", "mapping", "plan"):
        parser.add_argument("--" + name, required=True, type=Path)
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
        reports(args.reports, plan, mode != "preview")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
