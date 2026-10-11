#!/usr/bin/env python3
"""Preview a source-pinned separation of HCl stock strength and batch dose."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from pathlib import Path

import review_solution_concentration_evidence as runner
from bs4 import BeautifulSoup
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-fecl2-stock"
CONTEXT_SHA = "69856244cbba01ade9dbbd724063cd5c7b02cb9dac0d60353d67e5bcfbf34689"
ACTION = "SEPARATED_FECL2_STOCK_ACID_STRENGTH_AND_BATCH_DOSE_WITH_EVIDENCE"
QUOTE = "25% HCl (7.7 M) 10.0 ml"


def frozen():
    raw = (HERE / "inspected-context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    return json.loads(raw)


def sources(context):
    urls = {
        "S3846": "https://mediadive.dsmz.de/rest/solution/3846",
        "J187": "https://mediadive.dsmz.de/rest/medium/J187",
        "JCM187": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
    }
    runner.require(set(context["sources"]) == set(urls), "Source inventory drift")
    parsed = {}
    for key, source in context["sources"].items():
        meta, raw = source["metadata"], source["raw"]
        runner.require(
            meta["url"] == meta["response_url"] == urls[key]
            and meta["http_status"] == 200
            and runner.sha(raw.encode(meta["encoding"])) == meta["sha256"],
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        parsed[key] = (
            " ".join(BeautifulSoup(raw, "html.parser").get_text().split())
            if key == "JCM187"
            else json.loads(raw)
        )
    stock, medium = parsed["S3846"], parsed["J187"]
    runner.require(stock["status"] == medium["status"] == 200, "API status drift")
    stock, medium = stock["data"], medium["data"]
    runner.require(
        (stock["id"], stock["name"], stock["volume"], stock["steps"])
        == (3846, "FeCl2 solution", 1000, [])
        and medium["medium"]["id"] == "J187"
        and medium["medium"]["source"] == "JCM"
        and medium["medium"]["link"] == urls["JCM187"],
        "Source identity drift",
    )
    keys = ("compound_id", "compound", "amount", "unit", "attribute", "g_l", "optional")
    expected = [
        (68, "HCl", 10, "ml", "7.7 M, 25%", 2.5, 0),
        (260, "FeCl2 x 4 H2O", 1.5, "g", None, 1.5, 0),
        (4, "Distilled water", 990, "ml", None, None, 0),
    ]
    runner.require(
        [tuple(r.get(k) for k in keys) for r in stock["recipe"]] == expected
        and all(not r.get("condition") and not r.get("solution_id") for r in stock["recipe"]),
        "Stock formulation drift",
    )
    linked = [s for s in medium["solutions"] if s["id"] == 3846]
    runner.require(
        len(linked) == 1
        and linked[0]["name"] == stock["name"]
        and [tuple(r.get(k) for k in keys) for r in linked[0]["recipe"]] == expected
        and medium["solutions"][0]["recipe"][7]["solution_id"] == 3846,
        "Original-source link drift",
    )
    text = parsed["JCM187"]
    runner.require(
        "187 DESULFUROCOCCUS AMYLOLYTICUS MEDIUM" in text
        and "FeCl2 solution: " + QUOTE + " FeCl2\u00b74H2O 1.5 g Distilled water 990.0 ml" in text,
        "Original stock table drift",
    )
    return parsed


def build(before, timestamp):
    context = frozen()
    spec = context["record"]
    runner.require(
        before == runner.load_yaml(spec["before_text"])
        and before["id"] == spec["id"] == "CultureMech:012919"
        and before["term"]["id"] == "mediadive.solution:3846",
        "Unreviewed baseline",
    )
    runner.require(not runner.errors(before, "SolutionRecipe"), "Baseline schema failure")
    runner.require(
        not any(k in before for k in ("solutions", "source_data", "notes")), "Existing context"
    )
    sources(context)
    after = copy.deepcopy(before)
    acid = after["composition"].pop(0)
    runner.require(
        acid["concentration"] == {"value": "2.5", "unit": "G_PER_L"}, "Old acid value drift"
    )
    acid["concentration"] = {"value": "7.7", "unit": "MOLAR"}
    acid["notes"] = (
        "Strength of the HCl stock reagent, not of the prepared FeCl2 solution. "
        "The source also labels this stock 25%, without stating the percentage basis. "
        "The former 2.5 g/L provider-derived value is not retained as an asserted "
        "prepared-stock concentration; neither density nor measured final volume is supplied."
    )
    after["solutions"] = [
        {
            "preferred_term": "HCl stock (7.7 M)",
            "composition": [acid],
            "concentration": {"value": "0.01", "unit": "L"},
            "source": context["sources"]["S3846"]["metadata"]["url"],
            "notes": "10 ml of the 7.7 M HCl reagent per FeCl2 preparation batch, not 10 ml per liter of receiving medium. The 25% label has unspecified basis; no percentage conversion is asserted.",
        }
    ]
    after["source_data"] = {
        "origin": "MediaDive",
        "notes": "Provenance for the existing mediadive.solution:3846 import, recovered from its recipe API. Evidence is attached during curation; no new import date or original curation date is inferred.",
    }
    claims = []

    def claim(pointer, old_pointer, status, key, snippet, locator, reason, evidence_pointer=None):
        field = runner.field_name(pointer)
        meta = context["sources"][key]["metadata"]
        text = context["sources"][key]["raw"]
        if key == "JCM187":
            text = " ".join(BeautifulSoup(text, "html.parser").get_text().split())
        runner.require(snippet in text, "Nonliteral quote")
        explanation = f"{field}: {reason} Locator={locator}; accessed={meta['accessed_at']}; capture SHA256={meta['sha256']}."
        claims.append(
            {
                "pointer": pointer,
                "old_pointer": old_pointer,
                "field": field,
                "ingredient": runner.get_node(after, pointer[:-1])["preferred_term"],
                "old": copy.deepcopy(runner.get_node(before, old_pointer)) if old_pointer else None,
                "new": copy.deepcopy(runner.get_node(after, pointer)),
                "status": status,
                "reference": meta["url"],
                "snippet": snippet,
                "locator": locator,
                "explanation": explanation,
            }
        )
        if evidence_pointer is not None:
            runner.get_node(after, evidence_pointer).setdefault("evidence", []).append(
                {
                    "reference": meta["url"],
                    "supports": "SUPPORT",
                    "snippet": snippet,
                    "explanation": explanation,
                }
            )

    pointer = ["solutions", 0, "composition", 0]
    claim(
        pointer + ["concentration"],
        ["composition", 0, "concentration"],
        "correct",
        "JCM187",
        QUOTE,
        "FeCl2 solution table, HCl row",
        "Rebase the HCl assertion from provider-derived 2.5 g/L in the prepared FeCl2 stock to the explicitly stated 7.7 M reagent strength. No dilution, percent-basis or density inference.",
        pointer,
    )
    api_quote = json_excerpt(context["sources"]["S3846"]["raw"], ["data", "recipe", 0])
    api_meta = context["sources"]["S3846"]["metadata"]
    acid["evidence"].append(
        {
            "reference": context["sources"]["S3846"]["metadata"]["url"],
            "supports": "SUPPORT",
            "snippet": api_quote,
            "explanation": f"solutions[0].composition[0].concentration: the attribute explicitly states 7.7 M for the added HCl reagent. The same row's g_l=2.5 remains visible in this quote as a provider-derived output, not the reagent strength or a newly validated final concentration. Locator=$.data.recipe[0]; compound_id=68; accessed={api_meta['accessed_at']}; capture SHA256={api_meta['sha256']}. The separately cited original JCM187 table corroborates the stock strength.",
        }
    )
    claim(
        ["solutions", 0, "concentration"],
        None,
        "add",
        "S3846",
        api_quote,
        "$.data.recipe[0]",
        "Stock batch dose: 10 ml / 1000 ml per L = 0.01 L. This is an absolute preparation input, not a final-volume concentration. The original JCM187 FeCl2 table independently states the same reagent strength and dose; its URL and snippet are attached to the nested HCl component.",
        ["source_data"],
    )
    for index, name in enumerate(("FeCl2 x 4 H2O", "Distilled water")):
        node = after["composition"][index]
        runner.require(node["preferred_term"] == name, "Retained ingredient drift")
        current = f"composition[{index}].concentration"
        reason = f"Current locator after HCl stock separation: {current} ({name}); the earlier composition[{index + 1}] locator in this preserved evidence describes the pre-separation layout. Quantity, source snippet and qualification are unchanged."
        node["evidence"][0]["explanation"] += " " + reason
        quote = json_excerpt(context["sources"]["S3846"]["raw"], ["data", "recipe", index + 1])
        claim(
            ["composition", index, "concentration"],
            ["composition", index + 1, "concentration"],
            "verified",
            "S3846",
            quote,
            f"$.data.recipe[{index + 1}]",
            reason
            + (
                " Provider-declared 1.5 g/L only, not an independently measured final volume."
                if index == 0
                else " Batch water input 990 ml / 1000 = 0.99 L, not final volume."
            ),
        )
    claims.append(
        {
            "pointer": ["ingredients", 0, "concentration"],
            "old_pointer": ["ingredients", 0, "concentration"],
            "field": "ingredients[0].concentration",
            "ingredient": "See source for composition",
            "old": before["ingredients"][0]["concentration"],
            "new": after["ingredients"][0]["concentration"],
            "status": "unsupported",
            "reference": None,
            "snippet": None,
            "locator": None,
            "explanation": "Legacy import placeholder, not a reagent or verified VARIABLE amount. Preserved outside authoritative composition; not counted as concentration evidence.",
        }
    )
    meta = context["sources"]["JCM187"]["metadata"]
    after["references"].append(
        {
            "reference": meta["url"],
            "title": "Medium data",
            "notes": f"source_type=culture_collection_page; discovery_mode=cross_reference; accessed_on={meta['accessed_at'][:10]}; source_organization=JCM; recipe=187 DESULFUROCOCCUS AMYLOLYTICUS MEDIUM; locator=FeCl2 solution table; capture_sha256={meta['sha256']}. MediaDive medium J187 links this original recipe and solution 3846. Individual authors and publication year are not supplied; copyright year is not publication year.",
        }
    )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=meta["url"],
        notes="Source-linked stock strength and batch dose separated. Prior chemical annotations, evidence snippets and history preserved; relocated evidence receives current field locators. FeCl2 g/L remains provider-qualified. No final-volume, density, percent-basis or organism growth claim inferred.",
        changes="; ".join(
            f"{runner.field_name(c['old_pointer']) if c['old_pointer'] else 'new'} -> {c['field']}: {c['old']} -> {c['new']} ({c['status']})"
            for c in claims
        ),
    )
    runner.require(not runner.errors(after, "SolutionRecipe"), "Proposed schema failure")
    return after, claims


def process(root, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    context = frozen()
    spec = context["record"]
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    runner.require(head == context["commit"], "Reviewed commit drift")
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse plan overwrite")
        plan = {
            "version": 1,
            "commit": head,
            "context_sha256": CONTEXT_SHA,
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
    else:
        plan = json.loads(plan_path.read_text())
        runner.require(
            plan["context_sha256"] == CONTEXT_SHA and plan["commit"] == head, "Plan drift"
        )
    before = spec["before_text"].encode()
    runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
    after, claims = build(runner.load_yaml(before), plan["created_at"])
    output = runner.render(before.decode(), after)
    item = {
        **spec,
        "action": ACTION,
        "after_text": output.decode(),
        "after_sha256": runner.sha(output),
        "claims": claims,
    }
    if mode != "preview":
        runner.require(plan["records"] == [item], "Frozen decision drift")
    plan["records"] = [item]
    runner.safe_targets(root, plan)
    path = root / spec["path"]
    current = path.read_bytes()
    runner.require(current in (before, output), "Concurrent edit")
    if mode == "preview":
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        runner.require(
            not path.is_symlink() and path.read_bytes() == current, "Concurrent edit before write"
        )
        if mode == "apply" and current != output:
            path.write_bytes(output)
        runner.require(path.read_bytes() == output, "Result not applied")
    return plan, {
        "mode": mode,
        "records": 1,
        "changed": int(mode == "apply" and current != output),
        "already_applied": int(current == output),
        "claims": len(claims),
    }


def report(plan, applied):
    r = plan["records"][0]
    lines = [
        "# FeCl2 Stock Concentration Review",
        "",
        f"- Follow-up target: {r['path']}",
        f"- ID: {r['id']}",
        f"- Reviewed commit: {plan['commit']}",
        f"- Before SHA256: {r['before_sha256']}",
        f"- Result SHA256: {r['after_sha256']}",
        f"- State: {'applied locally' if applied else 'preview'}",
        "",
        "This supplements the existing exact-path record report; it does not count as another unique reviewed record. Every old and new amount slot is covered below. Field indices are scoped to the resulting record; old pointers are retained in plan.json. Source authors/year are unknown. Source identity is traced through MediaDive J187 to solution 3846 and the original JCM table. See baseline.json and validation.json for terminal validation results. No receiving-medium dose or final-volume concentration is inferred.",
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
    (HERE / "record.md").write_text("\n".join(lines) + "\n")


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
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
