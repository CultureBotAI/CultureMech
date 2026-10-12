#!/usr/bin/env python3
"""Restore five inspected TOGO/JCM reducing-agent and stock preparation scopes."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import re
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_m142_nested_traces as nested
import repair_m689_stocks as prior
import repair_methanogen_stock_boundaries as shared

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import html_recipe_text

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-reducing-stages"
CONTEXT_SHA = "dea2ad0d74d2e1b5a2d5f333ce3ebc0fd368f4181aad51fbd7aaca180795ef67"
ACTION = "RESTORED_REDUCING_AGENT_AND_STOCK_PREPARATION_SCOPES_WITH_EVIDENCE"
NUMBERS = {
    "M225": "232",
    "M229": "237",
    "M234": "242",
    "M236": "244",
    "M243": "251",
    "M142": "151",
    "M190": "197",
}
SIZES = {
    "M225": [20],
    "M229": [11, 11],
    "M234": [21],
    "M236": [15, 10, 6],
    "M243": [17, 2, 6],
    "M142": [10, 12, 14],
    "M190": [17, 11, 11],
}
REDUCERS = {"Na2S\u30fb9H2O", "L--Cysteine\u30fbHCl\u30fbH2O"}
LOCAL = {"M229": {9: 1}, "M236": {8: 1, 10: 2}, "M243": {10: 1, 11: 2}}
HEADINGS = {
    "M229": ["Artificial seawater:"],
    "M236": ["Synthetic seawater (2 x):", "Ni-Se-W solution:"],
    "M243": ["Mineral solution I:", "Mineral solution II:"],
}
# Explicit boundaries select only the inspected recipe's preparation prose.
STARTS = {
    "M225": [
        ("MIX", "Mix ingredients"),
        ("HEAT", "Bring to a boil"),
        ("ALIQUOT", "Dispense the medium"),
        ("STORE", "After autoclaving"),
        ("AUTOCLAVE", "Separately autoclave"),
        ("MIX", "Prior to inoculation"),
    ],
    "M229": [
        ("AUTOCLAVE", "Mix components"),
        ("AUTOCLAVE", "Separately autoclave"),
        ("MIX", "Prior to inoculation"),
    ],
    "M234": [
        ("HEAT", "Mix ingredients"),
        ("COOL", "Cool down"),
        ("ALIQUOT", "Dispense the medium"),
        ("AUTOCLAVE", "Separately autoclave"),
        ("MIX", "Prior to inoculation"),
    ],
    "M236": [
        ("MIX", "Mix ingredients"),
        ("FILTER", "Sterilize the medium"),
        ("HEAT", "Steam sulfur"),
        ("AUTOCLAVE", "Neutralize Na2S"),
        ("ALIQUOT", "Distribute the medium"),
        ("MIX", "Prior to inoculation"),
    ],
    "M243": [
        ("HEAT", "Mix ingredients"),
        ("COOL", "Cool down"),
        ("ALIQUOT", "Dispense the medium"),
        ("STORE", "After autoclaving"),
        ("AUTOCLAVE", "Separately autoclave"),
        ("MIX", "Prior to inoculation"),
    ],
}
REDUCER_STEP = {"M225": 4, "M229": 1, "M234": 3, "M236": 3, "M243": 4}
TRACE_PREPARATION = "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."


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
    return parsed


def preparation(key, text):
    markers = [s for _, s in STARTS[key]]
    end = HEADINGS[key][0] if key == "M229" else "Pressurize"
    bounds = [text.index(s) for s in markers + [end]]
    runner.require(bounds == sorted(set(bounds)), "Preparation order drift")
    steps = [(a, text[bounds[i] : bounds[i + 1]].strip()) for i, (a, _) in enumerate(STARTS[key])]
    pressure = None
    if key != "M229":
        end = HEADINGS.get(key, ["Copyright"])[0]
        pressure = text[bounds[-1] : text.index(end)].strip()
    return steps, pressure


class Review(prior.Review):
    def __init__(self, before, key):
        runner.require(key in STARTS, "Unreviewed record")
        context = frozen()
        shared.Review.__init__(self, before, key, context=context, parsed=sources(context))
        runner.require(not before.get("preparation_steps"), "Existing preparation needs review")
        self.originals = {}
        for field in ("ingredients", "solutions"):
            for i, node in enumerate(before[field]):
                runner.require(
                    node["preferred_term"] not in self.originals, "Ambiguous old identity"
                )
                self.originals[node["preferred_term"]] = [field, i]
        self.after["ingredients"], self.after["solutions"] = [], []
        self.steps, self.pressure = preparation(key, self.data["JCM" + NUMBERS[key]])

    def leaf(self, parent, source, si, ri, *, prepared=False):
        row = self.rows(source, si)[ri]
        if row["component_name"] == "KOH solution":
            return nested.Review.leaf(self, parent, source, si, ri)
        p = stocks.Review.leaf(self, parent, source, si, ri, prepared=prepared)
        _, old = self.clone(row["component_name"], source=source)
        if old and re.search(
            r"\[Merged [23] duplicates:", runner.get_node(self.before, old).get("notes", "")
        ):
            reason = "The earlier duplicate-summing note is superseded: it combined separate preparation scopes and source units. This node carries only the batch input at the cited source row; other occurrences are separate scoped ingredients."
            self.note(runner.get_node(self.after, p), reason)
            self.claim(
                p + ["notes"],
                old + ["notes"],
                source,
                stocks.row_path(source, si, ri),
                "correct",
                "duplicate_scope",
                reason,
                p,
            )
        return p

    def original_amount(self, p, source, si, ri, *, stock=False):
        row = self.rows(source, si)[ri]
        original = "JCM" + NUMBERS[source]
        text = self.data[original]
        if si == 0 and source in STARTS:
            text = text[: text.index(STARTS[source][0][1])]
        elif source in HEADINGS and si > 0:
            headings = HEADINGS[source] + ["Copyright"]
            text = text.split(headings[si - 1], 1)[1].split(headings[si], 1)[0]
        elif (source, si) == ("M142", 2):
            text = text.split("Trace minerals:", 1)[1].split("Dissolve nitrilotriacetic", 1)[0]
        elif (source, si) == ("M190", 1):
            text = text.split("Trace vitamins:", 1)[1].split("Trace mineral solution:", 1)[0]
        else:
            raise ValueError("Unreviewed original table")
        name = (
            row["component_name"]
            .replace("\u30fb", "\u00b7")
            .replace("--", "-")
            .replace("[M142]", "No. 151")
            .replace("[M190]", "No. 197")
        )
        matches = list(
            re.finditer(
                re.escape(name) + r" ([0-9]+(?:\.[0-9]+)?) " + re.escape(row["unit"]) + r"(?= |$)",
                text,
            )
        )
        runner.require(len(matches) == 1, "Original table amount missing or ambiguous")
        match = matches[0]
        runner.require(
            Decimal(match.group(1)) == Decimal(str(row["volume"])), "Source amount conflict"
        )
        self.corroborate(
            p + ["concentration" if stock else "notes"],
            original,
            match.group(),
            "Original table corroborates exact form and batch input at this preparation stage. A water input or stock label does not establish final volume or a per-liter dose.",
            [] if stock else p,
        )

    def direct(self, ri):
        row = self.rows(self.key, 0)[ri]
        original = "JCM" + NUMBERS[self.key]
        if row.get("volume") is not None:
            p = self.leaf(["ingredients"], self.key, 0, ri)
            self.original_amount(p, self.key, 0, ri)
            if self.key == "M236" and row["component_name"] == "Sulfur (powder)":
                reason = (
                    "Sulfur is prepared separately as a solid, not as an inferred stock solution. "
                    + self.steps[2][1]
                )
                self.note(runner.get_node(self.after, p), reason)
                self.corroborate(p + ["notes"], original, self.steps[2][1], reason, p)
            return
        node, old = self.clone(row["component_name"])
        node.pop("concentration")
        acid = row["component_name"] == "H2SO4"
        reason = (
            "Source pH-adjustment reagent with no fixed dose."
            if acid
            else "Source atmosphere context, not a fixed gas input or dissolved concentration."
        ) + " Removed the unsupported VARIABLE placeholder."
        if acid:
            reason += " The later readjustment explicitly uses sterile 1 N H2SO4; initial acid strength is not separately specified. Normality is not converted to molarity or a medium dose."
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
        indexes = (
            [0, 5]
            if acid
            else (
                [REDUCER_STEP[self.key]]
                if row["component_name"] == "N2"
                else [4 if self.key == "M236" else 2]
            )
        )
        for i in indexes:
            self.corroborate(p + ["notes"], original, self.steps[i][1], reason, p)

    def stock(self, ri):
        row = self.rows(self.key, 0)[ri]
        source = row["reference_media_id"]
        runner.require(source in {self.key, "M142", "M190"}, "Unreviewed stock reference")
        si = LOCAL[self.key][ri] if source == self.key else 2 if source == "M142" else 1
        p = stocks.Review.stock(self, ["solutions"], self.key, 0, ri)
        node = runner.get_node(self.after, p)
        self.original_amount(p, self.key, 0, ri, stock=True)
        heading = (
            HEADINGS[self.key][si - 1]
            if source == self.key
            else "Trace minerals:" if source == "M142" else "Trace vitamins:"
        )
        reason = "Expand only this named stock table, not the complete referenced medium or its other stocks/preparation. Stock water is an input, not an established final stock volume; a 2 x label does not supply a volume denominator."
        self.note(node, reason)
        self.corroborate(p + ["notes"], "JCM" + NUMBERS[source], heading, reason, [])
        for i, leaf in enumerate(self.rows(source, si)):
            if leaf["component_name"] == "KOH solution":
                node.setdefault("solutions", [])
                cp = self.leaf(p + ["solutions"], source, si, i)
                self.corroborate(
                    cp + ["notes"],
                    "JCM151",
                    TRACE_PREPARATION,
                    "Unquantified trace-stock titrant only.",
                    [],
                )
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

    def reducer(self, ri):
        row = self.rows(self.key, 0)[ri]
        runner.require(
            row["component_name"] in REDUCERS and row["volume"] == 0.5 and row["unit"] == "g",
            "Reducing-agent drift",
        )
        reason = "Separate reducing-agent preparation; composition notes retain the 0.5 g receiving-batch contribution, not a stock-batch recipe. Stock solvent volume and addition volume are unspecified. The source 5% label has unspecified percentage basis; no numeric stock strength or derived dose is asserted."
        text = self.steps[REDUCER_STEP[self.key]][1]
        p = self.append(
            ["solutions"],
            {
                "preferred_term": row["component_name"] + " separately prepared solution",
                "composition": [],
                "notes": reason,
                "preparation_notes": text,
            },
        )
        self.corroborate(p + ["preparation_notes"], "JCM" + NUMBERS[self.key], text, reason, [])
        self.lineage_node(p, None, self.key, 0, ri, "separate_preparation")
        cp = self.leaf(p + ["composition"], self.key, 0, ri, prepared=True)
        self.original_amount(cp, self.key, 0, ri)
        self.corroborate(cp + ["notes"], "JCM" + NUMBERS[self.key], text, reason, cp)

    def formulate(self):
        for i, row in enumerate(self.rows(self.key, 0)):
            if not row.get("reference_media_id") and row["component_name"] not in REDUCERS:
                self.direct(i)
        for i, row in enumerate(self.rows(self.key, 0)):
            if row.get("reference_media_id"):
                self.stock(i)
        for i, row in enumerate(self.rows(self.key, 0)):
            if row["component_name"] in REDUCERS:
                self.reducer(i)
        self.after["preparation_steps"] = [
            {"step_number": i + 1, "action": a, "description": text}
            for i, (a, text) in enumerate(self.steps)
        ]
        for i, (_, text) in enumerate(self.steps):
            self.corroborate(
                ["preparation_steps", i, "description"],
                "JCM" + NUMBERS[self.key],
                text,
                "Recipe-specific preparation order and stage; no inferred percentage basis, pore size, addition dose or final volume. Example aliquot/vessel sizes are not batch denominators.",
                [],
            )
        if self.pressure:
            self.note(self.after, "Original post-inoculation instruction: " + self.pressure)
            self.corroborate(
                ["notes"],
                "JCM" + NUMBERS[self.key],
                self.pressure,
                "Post-inoculation pressure and gas ratio, not a dissolved-gas concentration.",
                [],
            )

    def finish(self, timestamp):
        for c in self.claims:
            p = c["pointer"]
            c["new"] = copy.deepcopy(runner.get_node(self.after, p[:-1]).get(p[-1]))
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
            notes="Separated collapsed preparation inputs, restored named stock compositions and batch-volume doses, and removed unsupported final-rate and VARIABLE assertions. Preserved exact batch masses, separately prepared reducing agents, annotations and history with evidence. No final volume, percent basis or molar conversion inferred.",
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
            "# Ingredient And Reducing-Agent Preparation Review",
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
