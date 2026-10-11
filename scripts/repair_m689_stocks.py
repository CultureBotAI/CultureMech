#!/usr/bin/env python3
"""Repair the inspected M689 stock graph without assuming final volumes."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_m142_nested_traces as nested
import repair_methanogen_stock_boundaries as shared

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import html_recipe_text, literal_match

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-m689-stocks"
CONTEXT_SHA = "6b81dbac10cc4ea690b661f517aa88968b1945cb6a4a794c1b642a00f87fbc44"
ACTION = "RESTORED_M689_STOCK_DOSES_AND_COMPOSITIONS_WITH_EVIDENCE"
DEFINITIONS = [("M180", 1), ("M180", 2), ("M142", 2), ("M190", 1)]


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    return json.loads(raw)


def sources(context):
    parsed = {}
    for key, capture in context["sources"].items():
        meta, raw = capture["metadata"], capture["raw"]
        url = (
            "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=" + key[3:]
            if key.startswith("JCM")
            else "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=" + key
        )
        runner.require(
            meta["url"] == meta["response_url"] == url
            and meta["http_status"] == 200
            and runner.sha(raw.encode(meta["encoding"])) == meta["sha256"],
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        parsed[key] = html_recipe_text(raw)[0] if key.startswith("JCM") else json.loads(raw)
    for key, number, sizes in [
        ("M689", "670", [6, 5]),
        ("M180", "187", [19, 3, 8]),
        ("M142", "151", [10, 12, 14]),
        ("M190", "197", [17, 11, 11]),
    ]:
        body = parsed[key]
        runner.require(
            body["meta"]["gm"] == "http://togomedium.org/medium/" + key
            and body["meta"]["original_media_id"] == "JCM_M" + number
            and body["meta"]["src_url"] == context["sources"]["JCM" + number]["metadata"]["url"]
            and [len(s["items"]) for s in body["components"]] == sizes
            and f"Search for medium no. = [{number}]." in parsed["JCM" + number],
            "Source identity/topology drift",
        )
    return parsed


class Review(nested.Review):
    def __init__(self, before, key):
        runner.require(key == "M689", "Unreviewed record")
        context = frozen()
        shared.Review.__init__(self, before, key, context=context, parsed=sources(context))
        self.originals = {}
        for field in ("ingredients", "solutions"):
            for i, node in enumerate(before[field]):
                runner.require(node["preferred_term"] not in self.originals, "Ambiguous baseline")
                self.originals[node["preferred_term"]] = [field, i]
        self.after["ingredients"], self.after["solutions"] = [], []
        self.gas_paths = {}

    def claim(
        self,
        pointer,
        old_pointer,
        source,
        source_pointer,
        status,
        kind,
        reason,
        evidence_pointer=None,
        snippet=None,
    ):
        original_reason = reason
        reason = reason.replace(
            " Prior duplicate-collapse notes describe the superseded flattened record.", ""
        )
        if kind == "batch_mass" and old_pointer is None:
            reason = reason.replace(
                "the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
                "the source batch amount is retained without asserting a final concentration.",
            )
            pointer = pointer[:-1] + ["notes"]
            status = "add"
        node = runner.get_node(self.after, pointer[:-1])
        if "notes" in node and original_reason != reason:
            node["notes"] = node["notes"].replace(original_reason, reason)
        return super().claim(
            pointer,
            old_pointer,
            source,
            source_pointer,
            status,
            kind,
            reason,
            evidence_pointer,
            snippet,
        )

    def leaf(self, parent, source, si, ri, *, prepared=False):
        row = self.rows(source, si)[ri]
        if source == "M689" and (si, ri) == (0, 5):
            node, old = self.clone("N2")
            runner.require(row["component_name"] == "N2" and row.get("volume") is None, "Gas drift")
            node.pop("concentration")
            reason = "Source specifies an N2 atmosphere, not a fixed gas input or dissolved concentration. The unsupported VARIABLE quantity placeholder is removed."
            self.note(node, reason)
            p = self.append(parent, node)
            self.claim(
                p + ["concentration"],
                old + ["concentration"],
                source,
                stocks.row_path(source, si, ri),
                "remove_unsupported",
                "unquantified_gas",
                reason,
                p,
            )
            self.comment_claim(p + ["notes"], source, 0, "gas_context", reason, p)
            self.lineage_node(p, old, source, si, ri, "unquantified_gas")
            return p
        return super().leaf(parent, source, si, ri, prepared=prepared)

    def corroborate(self, pointer, source, quote, reason, ep):
        runner.require(literal_match(quote, self.data[source]), "Nonliteral original excerpt")
        self.claim(
            pointer, None, source, None, "evidence_only", "original_support", reason, ep, quote
        )

    def acid(self, parent):
        row = self.rows("M180", 1)[0]
        runner.require(
            row["component_name"] == "25% HCl (7.7 M)" and row["volume"] == 10, "Acid drift"
        )
        reason = "FeCl2-stock-only acid input: 10 ml = 0.01 L per stock batch. The reagent is explicitly 7.7 M; the 25% basis is unspecified. This is not a dose per liter of receiving medium."
        node = {
            "preferred_term": "HCl reagent (7.7 M)",
            "composition": [],
            "concentration": {"value": "0.01", "unit": "L"},
            "notes": reason,
        }
        p = self.append(parent, node)
        self.claim(
            p + ["concentration"],
            None,
            "M180",
            stocks.row_path("M180", 1, 0),
            "add",
            "batch_dose",
            reason,
            [],
        )
        self.lineage_node(p, None, "M180", 1, 0, "batch_dose")
        cp = stocks.Review.leaf(self, p + ["composition"], "M180", 1, 0)
        self.corroborate(cp + ["concentration"], "JCM187", "25% HCl (7.7 M) 10.0 ml", reason, cp)

    def formulate(self):
        for ri in range(6):
            self.leaf(["ingredients"], "M689", 0, ri)
        self.leaf(["ingredients"], "M689", 1, 4)
        for ri, (source, section) in enumerate(DEFINITIONS):
            row = self.rows("M689", 1)[ri]
            runner.require(
                row["reference_media_id"] == source and row["unit"] == "ml", "Link drift"
            )
            node, old = self.clone(row["component_name"])
            node["concentration"] = {"value": shared.numeric(row["volume"]), "unit": "ML_PER_L"}
            reason = f"Explicit receiving-medium addition: {row['volume']} ml per liter, not grams per liter. Expand only the referenced {self.data[source]['components'][section]['subcomponent_name']} stock definition."
            self.note(node, reason)
            p = self.append(["solutions"], node)
            self.claim(
                p + ["concentration"],
                old + ["concentration"],
                "M689",
                stocks.row_path("M689", 1, ri),
                "correct",
                "per_liter_dose",
                reason,
                [],
            )
            self.lineage_node(p, old, "M689", 1, ri, "per_liter_dose")
            self.comment_claim(p + ["concentration"], "M689", 0, "dose_scope", reason, [])
            self.corroborate(
                p + ["concentration"], "JCM670", "add to the medium (per liter):", reason, []
            )
            for i, ingredient in enumerate(self.rows(source, section)):
                if (source, section, i) == ("M180", 1, 0):
                    node["solutions"] = []
                    self.acid(p + ["solutions"])
                elif ingredient["component_name"] == "KOH solution":
                    node.setdefault("solutions", [])
                    self.leaf(p + ["solutions"], source, section, i)
                else:
                    self.leaf(p + ["composition"], source, section, i)
            if source == "M142":
                node["preparation_notes"] = self.data[source]["comments"][1]["comment"]
                self.comment_claim(
                    p + ["preparation_notes"],
                    source,
                    1,
                    "stock_preparation",
                    "pH adjustments apply to this trace-mineral stock, not to the receiving medium.",
                    [],
                )
                self.corroborate(
                    p + ["preparation_notes"],
                    "JCM151",
                    "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution.",
                    "Original trace-mineral stock preparation.",
                    [],
                )
            if source == "M190":
                node["preparation_notes"] = (
                    "Filter-sterilize this vitamin stock under N2 before its 10 ml/L addition; JCM670 marks this row with an asterisk."
                )
                self.corroborate(
                    p + ["preparation_notes"],
                    "JCM670",
                    "Separately autoclave or *filter-sterilize the following solutions under a N2 atmosphere",
                    "The asterisk selects filtration for the vitamin stock only.",
                    [],
                )
                self.corroborate(
                    p + ["preparation_notes"],
                    "JCM670",
                    "Trace vitamins (see Medium No. 197)* 10.0 ml",
                    "Asterisk-linked vitamin preparation and receiving dose.",
                    [],
                )
                self.corroborate(
                    p + ["composition"],
                    "JCM197",
                    "Trace vitamins:",
                    "Only the vitamin table is inherited, not JCM197's separate trace-mineral stock or complete medium.",
                    [],
                )
        self.after["preparation_steps"] = []
        for ci, action in enumerate(("AUTOCLAVE", "ADJUST_PH")):
            self.after["preparation_steps"].append(
                {
                    "step_number": ci + 1,
                    "action": action,
                    "description": self.data["M689"]["comments"][ci]["comment"],
                }
            )
            self.comment_claim(
                ["preparation_steps", ci, "description"],
                "M689",
                ci,
                "preparation_scope",
                "Receiving-medium preparation, staged stock additions and optional final pH adjustment; not an assertion of final volume.",
                [],
            )
        self.corroborate(
            ["ingredients", 1, "notes"],
            "JCM670",
            "Resazurin 0.5 mg",
            "Source mass is 0.5 mg per listed batch, not 0.5 g/L; no final volume is inferred.",
            ["ingredients", 1],
        )

    def finish(self, timestamp):
        for claim in self.claims:
            p = claim["pointer"]
            claim["new"] = copy.deepcopy(runner.get_node(self.after, p[:-1]).get(p[-1]))
        self.after["references"] = []
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            self.after["references"].append(
                {
                    "reference": meta["url"],
                    "title": (
                        "Medium data" if key.startswith("JCM") else self.data[key]["meta"]["name"]
                    ),
                    "notes": f"source_type={'culture_collection_page' if key.startswith('JCM') else 'dataset'}; discovery_mode={'existing_record_reference' if key in {'M689', 'JCM670'} else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied. Recipe quantities/preparation only; no growth or chemical-grounding claim.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"]["M689"]["metadata"]["url"],
            notes="Corrected four stock addition units, expanded the four named stocks at their own preparation stages, and withdrew unsupported batch-to-final concentration assertions. Preserved annotations/history and source batch quantities. Replaced the N2 quantity placeholder with source atmosphere context; chemical groundings remain unverified.",
            changes=json.dumps(
                [
                    {
                        k: c[k]
                        for k in (
                            "old_field",
                            "field",
                            "old",
                            "new",
                            "status",
                            "reference",
                            "snippet",
                        )
                    }
                    for c in self.claims
                    if c["status"] not in {"unsupported", "evidence_only"}
                ],
                ensure_ascii=True,
            ),
        )
        runner.require(not runner.errors(self.after, "MediaRecipe"), "Proposed schema failure")
        return self.after, self.claims, self.lineage


def build(before, key, timestamp):
    review = Review(before, key)
    review.formulate()
    return review.finish(timestamp)


def process(root, plan_path, mode):
    return shared.process(
        root,
        plan_path,
        mode,
        context=frozen(),
        context_sha=CONTEXT_SHA,
        builder=build,
        action=ACTION,
    )


def reports(plan, applied):
    out = HERE / "records"
    out.mkdir(exist_ok=True)
    for item in plan["records"]:
        lines = [
            "# M689 Ingredient And Stock Review",
            "",
            f"- Record: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Every old quantity and each inherited stock row is accounted below. Source amounts remain batch amounts when final volume is not stated. N2 is atmosphere context, not a fixed amount; pre-existing chemical groundings are not recertified. Authors/year are unavailable. See ../validation.json for terminal checks and ../README.md for unresolved gates.",
            "",
            "| Ingredient/context | Old field | Current field | Old | New | Status | DOI/PURL | Exact snippet | Decision and locator |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for claim in item["claims"]:
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(claim[k])
                    for k in (
                        "ingredient",
                        "old_field",
                        "field",
                        "old",
                        "new",
                        "status",
                        "reference",
                        "snippet",
                        "explanation",
                    )
                )
                + " |"
            )
        (out / (item["key"] + ".md")).write_text("\n".join(lines) + "\n")


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
