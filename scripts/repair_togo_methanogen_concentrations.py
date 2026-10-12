#!/usr/bin/env python3
"""Repair three pinned methanogen recipes without conflating batch and final volumes."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner
from bs4 import BeautifulSoup
from repair_togo_first_pair_concentrations import amount_excerpt
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-togo-methanogens"
CONTEXT_SHA = "d0e73bcc4d7c33b87dd5dcf26115e244c2d90d72fc17e3bb66252674931580c5"
ACTION = "REPAIRED_METHANOGEN_STOCK_DOSES_AND_BASE_REFERENCE_WITH_EVIDENCE"
SUPPLEMENT = "Use Medium No. 265 supplemented with 3.0 g/L trimethylamine\u00b7HCl"
SCOPE = (
    "Recipe-specific source evidence; batch inputs are not final-medium concentrations. "
    "No final volume, unspecified percentage basis, ontology grounding or growth claim is inferred."
)


def frozen():
    raw = (HERE / "inspected-context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    runner.require(
        [r["key"] for r in context["records"]] == ["M1038", "M1039", "J986"], "Inventory drift"
    )
    return context


def html_text(raw):
    return " ".join(BeautifulSoup(raw, "html.parser").get_text().split())


def sources(context):
    result = {}
    for key, source in context["sources"].items():
        meta, raw = source["metadata"], source["raw"]
        url = (
            "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=" + key[3:]
            if key.startswith("JCM")
            else (
                "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=" + key
                if key.startswith("M")
                else "https://mediadive.dsmz.de/rest/medium/" + key
            )
        )
        runner.require(
            meta["url"] == meta["response_url"] == url
            and meta["http_status"] == 200
            and runner.sha(raw.encode(meta["encoding"])) == meta["sha256"],
            "Capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        result[key] = html_text(raw) if key.startswith("JCM") else json.loads(raw)
    for key, number in [("M1038", 985), ("M1039", 986), ("M257", 265)]:
        meta = result[key]["meta"]
        runner.require(
            meta["gm"] == "http://togomedium.org/medium/" + key
            and meta["original_media_id"] == f"JCM_M{number}"
            and meta["src_url"] == context["sources"][f"JCM{number}"]["metadata"]["url"],
            "TOGO identity drift",
        )
    m38, m39 = result["M1038"], result["M1039"]
    runner.require(
        [(g["paragraph_index"], len(g["items"])) for g in m38["components"]]
        == [(1, 10), (3, 8), (5, 1)],
        "Preparation topology drift",
    )
    runner.require(
        [(r.get("volume"), r.get("unit")) for r in m38["components"][0]["items"]]
        == [
            (960, "ml"),
            (1, "g"),
            (0.1, "g"),
            (0.2, "g"),
            (0.5, "g"),
            (1, "mg"),
            (0.4, "g"),
            (0.5, "g"),
            (None, None),
            (None, None),
        ],
        "Batch amount drift",
    )
    runner.require(
        [(r.get("volume"), r.get("unit")) for r in m38["components"][1]["items"]]
        == [
            (20, "ml"),
            (10, "ml"),
            (10, "ml"),
            (1, "ml"),
            (1, "ml"),
            (1, "ml"),
            (None, None),
            (None, None),
        ],
        "Stock dose drift",
    )
    runner.require(
        m38["comments"][0]["paragraph_index"] == 2
        and "After cooling, add the following solutions" in m38["comments"][0]["comment"]
        and m38["comments"][1]["paragraph_index"] == 4
        and "Finally, add per liter the following solution" in m38["comments"][1]["comment"]
        and m38["components"][2]["items"][0]["volume"] == 8
        and m38["components"][2]["items"][0]["unit"] == "ml",
        "Per-liter preparation drift",
    )
    runner.require(
        [(r.get("volume"), r.get("unit")) for r in m39["components"][0]["items"]]
        == [(3, "g/L"), (1, "L"), (None, None), (None, None)],
        "Supplement/base dose drift",
    )
    runner.require(
        SUPPLEMENT in result["JCM986"] and "Nothing found." in result["JCM985"],
        "Original source drift",
    )
    runner.require("265 METHANOGENIUM MEDIUM" in result["JCM265"], "Base identity drift")
    for key in ("J985", "J986", "J265"):
        d = result[key]
        runner.require(
            d["status"] == 200
            and d["count"] == 1
            and d["data"]["medium"]["id"] == key
            and d["data"]["medium"]["source"] == "JCM"
            and d["data"]["medium"]["link"]
            == context["sources"]["JCM" + key[1:]]["metadata"]["url"],
            "MediaDive identity drift",
        )
    row = result["J985"]["data"]["solutions"][0]["recipe"][12]
    runner.require(
        (row["compound_id"], row["attribute"], row["amount"], row["unit"])
        == (383, "*, 30%", 10, "ml")
        and m38["components"][1]["items"][1]["conc_value"] == 3,
        "Strength conflict drift",
    )
    sol = result["J986"]["data"]["solutions"]
    runner.require(
        len(sol) == 1
        and sol[0]["id"] == 5016
        and not sol[0].get("recipe")
        and SUPPLEMENT.replace("\u00b7", " x ") in sol[0]["steps"][0]["step"],
        "Base instruction drift",
    )
    return result


def build(before, key, timestamp):
    context = frozen()
    spec = next(r for r in context["records"] if r["key"] == key)
    runner.require(
        before == runner.load_yaml(spec["before_text"]) and before["id"] == spec["id"],
        "Unreviewed baseline",
    )
    runner.require(
        runner.infer_target_class(before) == "MediaRecipe"
        and not runner.errors(before, "MediaRecipe"),
        "Baseline schema failure",
    )
    runner.require(
        not any(before.get(k) for k in ("references", "evidence", "variants")),
        "Provenance/topology drift",
    )
    data = sources(context)
    after, claims, used = copy.deepcopy(before), [], []

    def quote(source, pointer, amount=False):
        raw = context["sources"][source]["raw"]
        return (amount_excerpt if amount else json_excerpt)(raw, pointer)

    def claim(
        pointer,
        old_pointer,
        status,
        source,
        snippet,
        locator,
        reason,
        evidence_pointer=None,
        ingredient=None,
    ):
        old = (
            runner.get_node(before, old_pointer[:-1]).get(old_pointer[-1]) if old_pointer else None
        )
        new = runner.get_node(after, pointer[:-1]).get(pointer[-1]) if pointer else None
        label = (
            runner.field_name(pointer)
            if pointer
            else runner.field_name(old_pointer) + " -> solutions[0] reference"
        )
        meta = context["sources"][source]["metadata"]
        runner.require(
            snippet
            and snippet
            in (data[source] if source.startswith("JCM") else context["sources"][source]["raw"]),
            "Nonliteral snippet",
        )
        explanation = f"{label}: {reason} {SCOPE} Locator={locator}; accessed={meta['accessed_at']}; capture SHA256={meta['sha256']}."
        claims.append(
            {
                "pointer": pointer,
                "old_pointer": old_pointer,
                "field": label,
                "old_field": runner.field_name(old_pointer) if old_pointer else None,
                "ingredient": ingredient
                or (
                    runner.get_node(after, pointer[:-1]).get("preferred_term", "preparation")
                    if pointer
                    else runner.get_node(before, old_pointer[:-1])["preferred_term"]
                ),
                "old": copy.deepcopy(old),
                "new": copy.deepcopy(new),
                "status": status,
                "reference": meta["url"],
                "snippet": snippet,
                "locator": locator,
                "explanation": explanation,
                "evidence_pointer": evidence_pointer,
            }
        )
        if evidence_pointer is None:
            return
        if source not in used:
            used.append(source)
        ev = runner.get_node(after, evidence_pointer).setdefault("evidence", [])
        matching = [e for e in ev if e["reference"] == meta["url"]]
        if matching:
            runner.require(len(matching) == 1, "Evidence collision")
            matching[0]["explanation"] += (
                "\n\nAdditional exact excerpt: " + snippet + "\n" + explanation
            )
        else:
            ev.append(
                {
                    "reference": meta["url"],
                    "supports": "SUPPORT",
                    "snippet": snippet,
                    "explanation": explanation,
                }
            )

    def note(node, text):
        node["notes"] = (node.get("notes", "") + "\n\n" + text).strip()

    if key == "M1038":
        body = data[key]
        rows = body["components"][0]["items"]
        runner.require(
            [n["preferred_term"] for n in before["ingredients"]]
            == [r["component_name"] for r in rows],
            "Ingredient identity drift",
        )
        for i, node in enumerate(after["ingredients"]):
            pointer = ["ingredients", i, "concentration"]
            row = rows[i]
            if i >= 8:
                claim(
                    pointer,
                    pointer,
                    "unsupported",
                    key,
                    body["comments"][0]["comment"],
                    "$.comments[0].comment",
                    "The gas mixture is stated, but absolute gas amount is not. Retained legacy VARIABLE is not newly verified.",
                )
                continue
            if i == 0:
                node["concentration"] = {"value": "0.96", "unit": "L"}
                reason, status = (
                    "Water input: 960 ml / 1000 ml per L = 0.96 L per batch, not final-medium volume.",
                    "correct",
                )
            else:
                del node["concentration"]
                reason, status = (
                    f"Source batch amount: {row['volume']} {row['unit']}. Withdraw unsupported G_PER_L encoding; final-medium volume is unreported. This evidence supports the batch-mass note only.",
                    "remove_unsupported",
                )
            note(node, reason)
            claim(
                pointer,
                pointer,
                status,
                key,
                quote(key, ["components", 0, "items", i], True),
                f"$.components[0].items[{i}]",
                reason,
                pointer[:-1],
            )
        stock_rows = body["components"][1]["items"][:6] + body["components"][2]["items"]
        runner.require(
            [s["preferred_term"] for s in after["solutions"]]
            == [r["component_name"] for r in stock_rows],
            "Stock identity drift",
        )
        for i, (node, row) in enumerate(zip(after["solutions"], stock_rows, strict=True)):
            pointer = ["solutions", i, "concentration"]
            sp = ["components", 2 if i == 6 else 1, "items", 0 if i == 6 else i]
            node["concentration"] = (
                {"value": "8", "unit": "ML_PER_L"}
                if i == 6
                else {"value": str(Decimal(str(row["volume"])) / 1000), "unit": "L"}
            )
            prep = body["comments"][1 if i == 6 else 0]["comment"]
            reason = (
                "Source explicitly says add per liter: 8 ml/L stock working dose, not an 8 ml batch input."
                if i == 6
                else f"Source stock input: {row['volume']} ml / 1000 ml per L = {node['concentration']['value']} L per recipe batch, not a dose per final liter."
            )
            if "conc_value" in row:
                reason += f" The source label says {row['conc_value']}%, but the percentage basis is unspecified; no numeric stock strength or dilution is asserted."
            reason += " Stock composition and final-medium concentrations remain unresolved."
            note(node, reason)
            claim(
                pointer,
                pointer,
                "correct",
                key,
                quote(key, sp, True),
                "$." + runner.field_name(sp),
                reason + f' Additional exact preparation excerpt: "{prep}".',
                [],
            )
        conflict = "TOGO M1038 labels this stock 3%, whereas MediaDive J985 labels it 30%. Preserve the TOGO label and the disagreement; neither a common stock strength nor a variant is inferred. Both transcriptions specify a 10 ml addition. Original JCM985 returned Nothing found."
        note(after["solutions"][1], conflict)
        claim(
            ["solutions", 1, "notes"],
            None,
            "conflict",
            "J985",
            quote("J985", ["data", "solutions", 0, "recipe", 12]),
            "$.data.solutions[0].recipe[12]",
            conflict,
            [],
        )
        for i, source, group in [(2, "M190", 1), (3, "M180", 1), (4, "M180", 2), (5, "M431", 3)]:
            claim(
                ["solutions", i, "composition"],
                ["solutions", i, "composition"],
                "unsupported",
                source,
                quote(source, ["components", group, "items", 0], True),
                f"$.components[{group}]",
                "Linked stock recipe inspected together with its original JCM page. Its batch quantities do not independently establish final stock or receiving-medium volume. Inline composition is not expanded or certified by this dose repair.",
            )
        for i in (0, 1, 6):
            sp = ["components", 2 if i == 6 else 1, "items", 0 if i == 6 else i]
            claim(
                ["solutions", i, "composition"],
                ["solutions", i, "composition"],
                "unsupported",
                key,
                quote(key, sp),
                "$." + runner.field_name(sp),
                "Unspecified percentage basis prevents an asserted stock concentration; the 3% versus 30% trimethylamine conflict also remains unresolved.",
            )
        after["preparation_steps"] = [
            {"step_number": i + 1, "action": action, "description": body["comments"][i]["comment"]}
            for i, action in enumerate(("AUTOCLAVE", "ALIQUOT"))
        ]
        for i in range(2):
            claim(
                ["preparation_steps", i, "description"],
                None,
                "add_stage",
                key,
                body["comments"][i]["comment"],
                f"$.comments[{i}].comment",
                "Restore preparation order, sterilization and the separate per-liter stock-addition instruction.",
                [],
            )
    else:
        base_key = "M257" if key == "M1039" else "J265"
        dep = next(d for d in context["dependencies"] if d["key"] == base_key)
        base = runner.load_yaml(dep["before_text"])
        runner.require(
            base["id"] == dep["id"]
            and base["name"] == "methanogenium_medium"
            and base["media_term"]["term"]["id"]
            == ("TOGO:M257" if key == "M1039" else "mediadive.medium:J265"),
            "Base dependency identity drift",
        )
        if key == "J986":
            runner.require(
                len(before["ingredients"]) == len(base["ingredients"]) == 37,
                "Copied inventory drift",
            )
            for node, origin in zip(before["ingredients"], base["ingredients"], strict=True):
                runner.require(
                    "Copied from" in node["notes"] and "265" in node["notes"],
                    "Copied provenance drift",
                )
                runner.require(
                    {k: v for k, v in node.items() if k != "notes"}
                    == {k: v for k, v in origin.items() if k != "notes"},
                    "Copied formulation drift",
                )
            after["ingredients"] = [
                {
                    "preferred_term": "Trimethylamine hydrochloride",
                    "concentration": {"value": "3", "unit": "G_PER_L"},
                }
            ]
            after["solutions"] = [
                {"preferred_term": "METHANOGENIUM MEDIUM (JCM 265)", "composition": []}
            ]
            reason = "Restore the source's base-medium reference instead of 37 flattened copied concentrations, which conflate stock stages and include duplicate sums. The base constituents are not excluded from the medium: they remain in the linked base recipe. Its inherited concentrations remain unverified. JCM986 specifies no numeric base working dose here; none is inferred from TOGO M1039."
            note(after["solutions"][0], reason)
            for i in range(37):
                claim(
                    None,
                    ["ingredients", i, "concentration"],
                    "replace_with_reference",
                    "JCM986",
                    SUPPLEMENT,
                    "JCM986 recipe instruction",
                    reason,
                    [],
                )
            claim(
                ["solutions", 0, "concentration"],
                None,
                "not_quantified",
                "JCM986",
                SUPPLEMENT,
                "JCM986 recipe instruction",
                reason,
                [],
            )
        else:
            rows = data[key]["components"][0]["items"]
            runner.require(
                before["ingredients"][0]["preferred_term"] == rows[0]["component_name"]
                and before["solutions"][0]["preferred_term"] == rows[1]["component_name"],
                "M1039 identity drift",
            )
            after["solutions"][0]["concentration"] = {"value": "1", "unit": "L"}
            reason = "TOGO specifies 1 L of referenced M257 base medium as a recipe input, not 1 g/L or a measured final-medium volume. This dose is dataset-specific; inherited base concentrations remain unverified."
            note(after["solutions"][0], reason)
            claim(
                ["solutions", 0, "concentration"],
                ["solutions", 0, "concentration"],
                "correct",
                key,
                quote(key, ["components", 0, "items", 1], True),
                "$.components[0].items[1]",
                reason,
                [],
            )
            claim(
                ["ingredients", 0, "concentration"],
                ["ingredients", 0, "concentration"],
                "evidence_only",
                key,
                quote(key, ["components", 0, "items", 0], True),
                "$.components[0].items[0]",
                "Explicit 3 g/L trimethylamine hydrochloride supplement, not an inferred stock dilution.",
                ["ingredients", 0],
            )
            step = data[key]["comments"][1]["comment"]
            after["preparation_steps"] = [
                {"step_number": 1, "action": "ADJUST_PH", "description": step}
            ]
            claim(
                ["preparation_steps", 0, "description"],
                None,
                "add_stage",
                key,
                step,
                "$.comments[1].comment",
                "Restore source-specific base/supplement, pH and gas instructions; do not inherit the base medium's different gas mixture.",
                [],
            )
            for i in (1, 2):
                p = ["ingredients", i, "concentration"]
                claim(
                    p,
                    p,
                    "unsupported",
                    key,
                    step,
                    "$.comments[1].comment",
                    "Absolute gas amount is not specified. Retained legacy VARIABLE is not newly verified.",
                )
        after["solutions"][0]["culturemech_term"] = {"id": base["id"], "label": base["name"]}
        claim(
            ["solutions", 0, "culturemech_term"],
            None,
            "add_reference",
            "JCM986",
            SUPPLEMENT,
            "JCM986 recipe instruction",
            f"Reference to JCM265, matched to tracked {dep['path']} ({base['id']}). This establishes base identity, not validation of copied concentrations.",
            [],
        )
        base_pointer = ["meta"] if key == "M1039" else ["data", "medium"]
        claim(
            ["solutions", 0, "culturemech_term"],
            None,
            "evidence_only",
            base_key,
            quote(base_key, base_pointer),
            "$." + runner.field_name(base_pointer),
            "Cross-reference source accession and name verify the linked base recipe identity only.",
            [],
        )
        p = ["ingredients", 0, "concentration"]
        claim(
            p,
            p if key == "M1039" else None,
            "evidence_only" if key == "M1039" else "add",
            "JCM986",
            SUPPLEMENT,
            "JCM986 recipe instruction",
            "The original collection recipe explicitly requires 3.0 g/L trimethylamine hydrochloride. This is the supplement, not a concentration inferred from the base recipe.",
            ["ingredients", 0],
        )
        if key == "J986":
            step = data[key]["data"]["solutions"][0]["steps"][0]["step"]
            runner.require(
                before["preparation_steps"][0]["description"] == step, "Existing preparation drift"
            )
            claim(
                p,
                None,
                "evidence_only",
                key,
                step,
                "$.data.solutions[0].steps[0].step",
                "The exact MediaDive J986 transcription also specifies the supplement and base reference; it contains no inline recipe to justify the flattened copied quantities.",
                ["ingredients", 0],
            )
        claim(
            ["solutions", 0, "composition"],
            ["solutions", 0, "composition"] if key == "M1039" else None,
            "unsupported",
            "JCM986",
            SUPPLEMENT,
            "JCM986 recipe instruction",
            "Referenced JCM265 and its stocks require separate source-aware curation. Empty inline composition means reference-only, not ingredient-free or fully verified.",
        )

    after["references"] = []
    for source_key in used:
        src = context["sources"][source_key]
        meta = src["metadata"]
        title = (
            "Medium data"
            if source_key.startswith("JCM")
            else (
                data[source_key]["meta"]["name"]
                if source_key.startswith("M")
                else data[source_key]["data"]["medium"]["name"]
            )
        )
        kind = "culture_collection_page" if source_key.startswith("JCM") else "dataset"
        mode = "existing_record_reference" if source_key in (key, "JCM986") else "cross_reference"
        after["references"].append(
            {
                "reference": meta["url"],
                "title": title,
                "notes": f"source_type={kind}; discovery_mode={mode}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied; page copyright year is not publication metadata.",
            }
        )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=context["sources"]["JCM986" if key == "J986" else key]["metadata"]["url"],
        notes="Corrected recipe-specific quantities and provenance; preserved stock-strength conflicts and unresolved final-volume/base-composition claims. Existing history, conditions and organism claims unchanged.",
        changes="; ".join(
            f"{c['old_field']} -> {c['field']}: {c['old']} -> {c['new']} ({c['status']})"
            for c in claims
        ),
    )
    runner.require(not runner.errors(after, "MediaRecipe"), "Proposed schema failure")
    return after, claims


def process(root, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    context = frozen()
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse plan overwrite")
        plan = {
            "version": 1,
            "action": ACTION,
            "context_sha256": CONTEXT_SHA,
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
            and plan["context_sha256"] == CONTEXT_SHA,
            "Plan drift",
        )
    # Reference identity and copied-formulation comparisons must still match the inspected dependencies.
    for dep in context["dependencies"]:
        path = root / dep["path"]
        runner.require(
            not path.is_symlink() and runner.sha(path.read_bytes()) == dep["before_sha256"],
            "Dependency drift",
        )
    records, pending = [], []
    for spec in context["records"]:
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target")
        current, before = path.read_bytes(), spec["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
        after, claims = build(runner.load_yaml(before), spec["key"], plan["created_at"])
        output = runner.render(before.decode(), after)
        runner.require(current in (before, output), "Concurrent edit")
        records.append(
            {
                **spec,
                "action": ACTION,
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "claims": claims,
            }
        )
        pending.append((path, current, output))
    if mode != "preview":
        runner.require(records == plan["records"], "Frozen decision drift")
    plan["records"] = records
    runner.safe_targets(root, plan)
    runner.safe_targets(
        root,
        {
            "version": 1,
            "records": [
                {**d, "claims": [], "after_sha256": d["before_sha256"]}
                for d in context["dependencies"]
            ],
        },
    )
    runner.require(
        all(p.read_bytes() == c and not p.is_symlink() for p, c, _ in pending),
        "Concurrent edit before write",
    )
    runner.require(
        all(
            not (root / d["path"]).is_symlink()
            and runner.sha((root / d["path"]).read_bytes()) == d["before_sha256"]
            for d in context["dependencies"]
        ),
        "Dependency drift before write",
    )
    if mode == "preview":
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


def reports(plan, applied):
    for r in plan["records"]:
        marker = "Follow-up target" if r["key"] == "J986" else "Record"
        lines = [
            "# Methanogen Concentration Review",
            "",
            f"- {marker}: {r['path']}",
            f"- ID: {r['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {r['before_sha256']}",
            f"- Result SHA256: {r['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Every prior concentration slot is reported, including unverified placeholders and withdrawn copied claims. Source type and discovery are in YAML references; authors/year unknown. Schema checks pass at build time; see validation.json for terminal checks. Missing inline stocks, unresolved final volumes and conflicting strengths remain open. J986 supplements its existing exact-path report; its base constituents are referenced, not excluded.",
            "",
            "| Field | Ingredient | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in r["claims"]:
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
        path = HERE / "records" / (r["key"] + ".md")
        path.parent.mkdir(exist_ok=True)
        path.write_text("\n".join(lines) + "\n")


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
        reports(plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
