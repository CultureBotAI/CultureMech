#!/usr/bin/env python3
"""Restore the inspected M208/M209 stock boundaries and source batch amounts."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import re
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_m689_stocks as prior
import repair_methanogen_stock_boundaries as shared

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import html_recipe_text, literal_match

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-marine-stock-pair"
CONTEXT = HERE.parent / "20261008-filtered-sulfide-media/next-marine-pair-context.json"
CONTEXT_SHA = "03204b85c0510e83182322363d7722b7a492f333ed3d3f1e13b8c3f9d6c034c1"
ACTION = "RESTORED_MARINE_STOCK_SCOPES_AND_BATCH_AMOUNTS_WITH_EVIDENCE"
NUMBERS = {"M208": "215", "M209": "216", "M142": "151", "M190": "197"}
SIZES = {"M208": [16, 15], "M209": [23, 9], "M142": [10, 12, 14], "M190": [17, 11, 11]}
SULFIDE = "Na2S\u30fb9H2O"
TRACE_PREPARATION = "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."
STEPS = {
    "M208": [
        ("FILTER", "Adjust pH to 7.0 with 1 N H2SO4, and sterilize by filtration."),
        ("ALIQUOT", "Dispense the medium into bottles under a N2-CO2-O2 (80:20:1) atmosphere."),
    ],
    "M209": [
        ("MIX", "Mix ingredients, except Na2S\u00b79H2O, adjust pH to 6.0 with H2SO4."),
        ("FILTER", "Sterilize by filtration while gassing with H2-CO2 (80:20) gas mixture."),
        ("AUTOCLAVE", "Autoclave Na2S\u00b79H2O as a 5% solution under a N2 atmosphere."),
        (
            "MIX",
            "Prior to inoculation, anaerobically add the sterile Na2S\u00b79H2O solution, and readjust pH to 6.5 with sterile H2SO4.",
        ),
    ],
}
PRESSURE = {
    "M208": "Pressurize inoculated bottles to 200 kPa N2-CO2-O2 (80:20:1).",
    "M209": "Pressurize the inoculated bottle to 200 kPa H2-CO2 (80:20).",
}
LOCAL_HEADINGS = {
    "M208": "Marine medium/Synthetic seawater mix solution:",
    "M209": "Marine trace elements solution:",
}


def frozen():
    raw = CONTEXT.read_bytes()
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
    for key, number in NUMBERS.items():
        body = parsed[key]
        runner.require(
            body["meta"]["gm"] == "http://togomedium.org/medium/" + key
            and body["meta"]["original_media_id"] == "JCM_M" + number
            and body["meta"]["src_url"] == context["sources"]["JCM" + number]["metadata"]["url"]
            and [len(s["items"]) for s in body["components"]] == SIZES[key]
            and f"Search for medium no. = [{number}]." in parsed["JCM" + number],
            "Source identity/topology drift",
        )
    for key, steps in STEPS.items():
        text = parsed["JCM" + NUMBERS[key]]
        runner.require(all(literal_match(s, text) for _, s in steps), "Preparation drift")
        runner.require(literal_match(PRESSURE[key], text), "Pressure drift")
    return parsed


class Review(prior.Review):
    def __init__(self, before, key):
        runner.require(key in STEPS, "Unreviewed record")
        context = frozen()
        shared.Review.__init__(self, before, key, context=context, parsed=sources(context))
        runner.require(not before.get("preparation_steps"), "Existing preparation needs review")
        self.originals = {}
        for field in ("ingredients", "solutions"):
            for i, node in enumerate(before[field]):
                name = node["preferred_term"]
                runner.require(name not in self.originals, "Ambiguous old identity")
                self.originals[name] = [field, i]
        self.after["ingredients"], self.after["solutions"] = [], []
        self.gas_paths = {}

    def original_amount(self, pointer, source, si, ri, *, stock=False):
        row = self.rows(source, si)[ri]
        original = "JCM" + NUMBERS[source]
        text = self.data[original]
        if si == 0 and source in STEPS:
            text = text[: text.index(STEPS[source][0][1])]
        elif source in LOCAL_HEADINGS and si == 1:
            text = text.split(LOCAL_HEADINGS[source], 1)[1].split(" Copyright", 1)[0]
        elif (source, si) == ("M142", 2):
            text = text.split("Trace minerals:", 1)[1].split("Dissolve nitrilotriacetic", 1)[0]
        elif (source, si) == ("M190", 1):
            text = text.split("Trace vitamins:", 1)[1].split("Trace mineral solution:", 1)[0]
        else:
            raise ValueError("Unreviewed original table")
        name = row["component_name"].replace("\u30fb", "\u00b7").replace("--", "-")
        name = name.replace("[M142]", "No. 151").replace("[M190]", "No. 197")
        found = list(
            re.finditer(
                re.escape(name) + r" ([0-9]+(?:\.[0-9]+)?) " + re.escape(row["unit"]) + r"(?= |$)",
                text,
            )
        )
        runner.require(len(found) == 1, "Original table amount missing or ambiguous")
        match = found[0]
        runner.require(
            Decimal(match.group(1)) == Decimal(str(row["volume"])), "Source amount conflict"
        )
        self.corroborate(
            pointer + ["concentration" if stock else "notes"],
            original,
            match.group(),
            "Original table corroborates the exact form and batch input at this preparation stage; neither a final volume nor a per-liter dose is established.",
            [] if stock else pointer,
        )

    def direct(self, ri):
        row = self.rows(self.key, 0)[ri]
        if row.get("volume") is not None:
            p = self.leaf(["ingredients"], self.key, 0, ri)
            self.original_amount(p, self.key, 0, ri)
            if self.key == "M208" and row["component_name"] == "NaWO4\u30fb2H2O":
                reason = "Both TOGO and original JCM215 print NaWO4. The legacy sodium-tungstate grounding is retained, not recertified; the formula discrepancy is unresolved. No formula normalization or molar conversion is performed."
                self.note(runner.get_node(self.after, p), reason)
                self.corroborate(p + ["notes"], "JCM215", "NaWO4\u00b72H2O 0.1 mg", reason, p)
            return
        node, old = self.clone(row["component_name"])
        node.pop("concentration")
        acid = row["component_name"] == "H2SO4"
        reason = (
            "Source pH-adjustment reagent with no fixed dose."
            if acid
            else "Source atmosphere context, not a fixed gas input or dissolved concentration."
        ) + " Removed the unsupported VARIABLE placeholder."
        if acid and self.key == "M208":
            reason += " Original JCM215 specifies 1 N H2SO4 reagent; normality is not converted to molarity or a receiving-medium dose."
        if self.key == "M208" and not acid:
            reason += (
                " The 80:20:1 gas ratio is retained as written, not normalized to percentages."
            )
        self.note(node, reason)
        p = self.append(["ingredients"], node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"],
            self.key,
            stocks.row_path(self.key, 0, ri),
            "remove_unsupported",
            "unquantified_input",
            reason,
            p,
        )
        self.lineage_node(p, old, self.key, 0, ri, "unquantified_input")
        step = 0 if acid else 2 if self.key == "M209" and row["component_name"] == "N2" else 1
        self.corroborate(
            p + ["notes"], "JCM" + NUMBERS[self.key], STEPS[self.key][step][1], reason, p
        )

    def stock(self, ri):
        row = self.rows(self.key, 0)[ri]
        source = row["reference_media_id"]
        runner.require(source in {self.key, "M142", "M190"}, "Unreviewed stock reference")
        si = 2 if source == "M142" else 1
        p = stocks.Review.stock(self, ["solutions"], self.key, 0, ri)
        node = runner.get_node(self.after, p)
        self.original_amount(p, self.key, 0, ri, stock=True)
        heading = {"M142": "Trace minerals:", "M190": "Trace vitamins:"}.get(
            source, LOCAL_HEADINGS[self.key]
        )
        reason = "Expand only this named stock table, not the complete referenced medium or its other stocks/preparation instructions. Stock water is an input, not an established final stock volume."
        self.note(node, reason)
        self.corroborate(p + ["notes"], "JCM" + NUMBERS[source], heading, reason, [])
        for i, leaf in enumerate(self.rows(source, si)):
            if leaf["component_name"] == "KOH solution":
                node.setdefault("solutions", [])
                self.leaf(p + ["solutions"], source, si, i)
            else:
                cp = self.leaf(p + ["composition"], source, si, i)
                self.original_amount(cp, source, si, i)
        if source == "M142":
            node["preparation_notes"] = TRACE_PREPARATION
            self.corroborate(
                p + ["preparation_notes"],
                "JCM151",
                TRACE_PREPARATION,
                "pH 6.5 then 7.0 belongs only to the trace-mineral stock, not the receiving medium.",
                [],
            )

    def sulfide(self):
        ri = 9
        row = self.rows(self.key, 0)[ri]
        runner.require(
            self.key == "M209"
            and row["component_name"] == SULFIDE
            and row["volume"] == 0.5
            and row["unit"] == "g",
            "Sulfide drift",
        )
        reason = "Separate sulfide preparation; composition notes retain the 0.5 g receiving-batch contribution, not a stock-batch recipe. Stock solvent volume and addition volume are unspecified. The source 5% label has unspecified percentage basis; no numeric stock strength or derived dose is asserted."
        text = STEPS["M209"][2][1]
        p = self.append(
            ["solutions"],
            {
                "preferred_term": SULFIDE + " separately prepared solution",
                "composition": [],
                "notes": reason,
                "preparation_notes": text,
            },
        )
        self.corroborate(p + ["preparation_notes"], "JCM216", text, reason, [])
        self.lineage_node(p, None, self.key, 0, ri, "separate_preparation")
        cp = self.leaf(p + ["composition"], self.key, 0, ri, prepared=True)
        self.original_amount(cp, self.key, 0, ri)
        self.corroborate(cp + ["notes"], "JCM216", text, reason, cp)

    def formulate(self):
        for i, row in enumerate(self.rows(self.key, 0)):
            if not row.get("reference_media_id") and row["component_name"] != SULFIDE:
                self.direct(i)
        for i, row in enumerate(self.rows(self.key, 0)):
            if row.get("reference_media_id"):
                self.stock(i)
        if self.key == "M209":
            self.sulfide()
        self.after["preparation_steps"] = [
            {"step_number": i + 1, "action": action, "description": text}
            for i, (action, text) in enumerate(STEPS[self.key])
        ]
        for i, (_, text) in enumerate(STEPS[self.key]):
            self.corroborate(
                ["preparation_steps", i, "description"],
                "JCM" + NUMBERS[self.key],
                text,
                "Recipe-specific preparation order, atmosphere and pH stages; no unspecified pore size, percentage basis, dose or final volume is inferred.",
                [],
            )
        self.note(self.after, "Original post-inoculation instruction: " + PRESSURE[self.key])
        self.corroborate(
            ["notes"],
            "JCM" + NUMBERS[self.key],
            PRESSURE[self.key],
            "Post-inoculation pressure and gas ratio, not a dissolved-gas concentration.",
            [],
        )

    def finish(self, timestamp):
        for claim in self.claims:
            p = claim["pointer"]
            claim["new"] = copy.deepcopy(runner.get_node(self.after, p[:-1]).get(p[-1]))
        self.after["references"] = []
        for source in self.used:
            meta = self.context["sources"][source]["metadata"]
            self.after["references"].append(
                {
                    "reference": meta["url"],
                    "title": (
                        "Medium data"
                        if source.startswith("JCM")
                        else self.data[source]["meta"]["name"]
                    ),
                    "notes": f"source_type={'culture_collection_page' if source.startswith('JCM') else 'dataset'}; discovery_mode={'existing_record_reference' if source in {self.key, 'JCM' + NUMBERS[self.key]} else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied. Recipe quantities/preparation only; chemical groundings, legacy quality flags and growth claims are not recertified.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Separated collapsed main/stock water, restored named stock compositions and batch-volume inputs, and removed unsupported final-rate and VARIABLE assertions. Preserved exact batch masses, preparation, annotations and history with evidence. No final volume, percentage basis or molar conversion inferred.",
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
    out.mkdir(parents=True, exist_ok=True)
    for item in plan["records"]:
        lines = [
            "# Marine Stock And Ingredient Review",
            "",
            f"- Record: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Batch amounts, stock doses and preparation stages are distinct. Final volumes, unspecified strengths/doses, chemical grounding and legacy quality flags remain unresolved. Authors/year are unknown. See ../validation.json for actual terminal checks; report presence is not all-claim completion.",
            "",
            "| Ingredient/context | Old field | Current field | Old | New | Status | DOI/PURL | Exact snippet | Decision and locator |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in item["claims"]:
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(c[k])
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
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    parser.add_argument("--reports", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    args.plan.parent.mkdir(parents=True, exist_ok=True)
    plan, result = process(ROOT, args.plan, mode)
    if args.reports:
        reports(plan, mode != "preview")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
