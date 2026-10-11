#!/usr/bin/env python3
"""Repair M258's false LB substitution and M260's nested seawater stock."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-m258-m260-stocks"
CONTEXT_SHA = "b8e92ccde02abf688c54a0dc916142a971f6336216f3be270c84d88c9886b926"
ACTION = "REPAIRED_M258_IDENTITY_AND_M260_NESTED_STOCK_WITH_EVIDENCE"
NUMBERS = {"M258": "266", "M260": "268", "M142": "151", "M190": "197"}
SIZES = {"M258": [21, 1, 6], "M260": [8, 11], "M142": [10, 12, 14], "M190": [17, 11, 11]}
REDUCERS = {"Na2S\u30fb9H2O", "L--Cysteine\u30fbHCl\u30fbH2O"}
HEADINGS = {
    "M258": ["To prepare the clarified rumen fluid,", "Fatty acid mixture:"],
    "M260": ["MJ(-N) synthetic seawater:"],
}
STARTS = {
    "M258": [
        ("MIX", "Mix ingredients"),
        ("HEAT", "Bring to a boil"),
        ("ALIQUOT", "Dispense the medium"),
        ("STORE", "After autoclaving"),
        ("AUTOCLAVE", "Separately autoclave"),
        ("MIX", "Prior to inoculation"),
    ],
    "M260": [("ADJUST_PH", "Adjust pH to 7.5.")],
}
REDUCER_STEP = {"M258": 4}
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
    end = HEADINGS[key][0] if key == "M260" else "Pressurize"
    bounds = [text.index(s) for s in markers + [end]]
    runner.require(bounds == sorted(set(bounds)), "Preparation order drift")
    steps = [(a, text[bounds[i] : bounds[i + 1]].strip()) for i, (a, _) in enumerate(STARTS[key])]
    pressure = None
    if key != "M260":
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
        if row.get("volume") is not None:
            p = self.leaf(["ingredients"], self.key, 0, ri)
            self.original_amount(p, self.key, 0, ri)
            return
        runner.require(self.key == "M258" and ri in {18, 19, 20}, "Unreviewed gas")
        node, old = self.clone(row["component_name"])
        node.pop("concentration")
        reason = "Source atmosphere context, not a fixed gas input or dissolved concentration. Removed the unsupported VARIABLE placeholder."
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
        step = self.steps[4 if ri == 19 else 2][1]
        self.corroborate(p + ["notes"], "JCM266", step, reason, p)

    def dose(self, parent, source, si, ri):
        row = self.rows(source, si)[ri]
        node, old = self.clone(row["component_name"], source=source)
        runner.require(row["unit"] == "ml", "Unreviewed dose unit")
        value = shared.numeric(Decimal(str(row["volume"])) / 1000)
        node["composition"] = []
        node["concentration"] = {"value": value, "unit": "L"}
        reason = f"Source stock addition: {row['volume']} ml = {value} L per receiving batch, not grams per liter or a dose per final liter."
        if si > 0:
            reason += " This dose belongs to the enclosing stock preparation, not directly to the final medium."
        self.note(node, reason)
        p = self.append(parent, node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            source,
            stocks.row_path(source, si, ri),
            "correct" if old else "add",
            "batch_dose",
            reason,
            [],
        )
        self.lineage_node(p, old, source, si, ri, "batch_dose")
        self.original_amount(p, source, si, ri, stock=True)
        return p

    def unquantified_local(self, parent, si, ri):
        row = self.rows(self.key, si)[ri]
        node, old = self.clone(row["component_name"])
        runner.require(old is not None and row.get("volume") is None, "Local context drift")
        node.pop("concentration")
        titrant = row["component_name"] == "NaOH"
        if titrant:
            node["composition"] = []
        reason = (
            "Concentrated NaOH adjusts only the fatty-acid stock to pH 7.5; no fixed dose or numeric strength is given."
            if titrant
            else "Unquantified clarified-fluid product description, not an additional independent dose. The enclosing stock descriptor alone holds the 300 ml receiving-batch input."
        ) + " Removed the unsupported VARIABLE placeholder."
        self.note(node, reason)
        p = self.append(parent, node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"],
            self.key,
            stocks.row_path(self.key, si, ri),
            "remove_unsupported",
            "unquantified_titrant" if titrant else "unquantified_product",
            reason,
            [] if titrant else p,
        )
        self.lineage_node(
            p, old, self.key, si, ri, "unquantified_titrant" if titrant else "unquantified_product"
        )
        self.corroborate(
            p + ["notes"], "JCM266", self.local_preparation(si), reason, [] if titrant else p
        )

    def local_preparation(self, si):
        text = self.data["JCM266"]
        if si == 1:
            return text[text.index(HEADINGS["M258"][0]) : text.index(HEADINGS["M258"][1])].strip()
        return text[
            text.index("Adjust pH to 7.5 with concentrated NaOH solution.") : text.index(
                "Copyright"
            )
        ].strip()

    def stock(self, parent, source, si, ri):
        p = self.dose(parent, source, si, ri)
        row = self.rows(source, si)[ri]
        target = row["reference_media_id"]
        section = (
            ({14: 1, 17: 2}[ri] if self.key == "M258" else 1)
            if target == self.key
            else 2 if target == "M142" else 1
        )
        runner.require(target in {self.key, "M142", "M190"}, "Unreviewed stock")
        node = runner.get_node(self.after, p)
        heading = (
            HEADINGS[self.key][section - 1]
            if target == self.key
            else "Trace minerals:" if target == "M142" else "Trace vitamins:"
        )
        reason = "Expand only this named preparation, not the complete referenced medium. Water input does not establish final stock volume; no final-medium rate is inferred."
        self.note(node, reason)
        self.corroborate(p + ["notes"], "JCM" + NUMBERS[target], heading, reason, [])
        for i, leaf in enumerate(self.rows(target, section)):
            if leaf.get("reference_media_id"):
                runner.require(
                    (self.key, target, section, i) == ("M260", "M260", 1, 10), "Nested link drift"
                )
                node.setdefault("solutions", [])
                self.stock(p + ["solutions"], target, section, i)
            elif leaf["component_name"] == "KOH solution":
                node.setdefault("solutions", [])
                cp = self.leaf(p + ["solutions"], target, section, i)
                self.corroborate(
                    cp + ["notes"],
                    "JCM151",
                    TRACE_PREPARATION,
                    "Unquantified trace-stock titrant only.",
                    [],
                )
            elif leaf.get("volume") is None:
                parent = p + ["solutions" if leaf["component_name"] == "NaOH" else "composition"]
                node.setdefault(parent[-1], [])
                self.unquantified_local(parent, section, i)
            else:
                cp = self.leaf(p + ["composition"], target, section, i)
                self.original_amount(cp, target, section, i)
        if target == "M142":
            prep = TRACE_PREPARATION
        elif target == "M258":
            prep = self.local_preparation(section)
        else:
            prep = None
        if prep:
            node["preparation_notes"] = prep
            self.corroborate(
                p + ["preparation_notes"],
                "JCM" + NUMBERS[target],
                prep,
                "This preparation belongs only to the named stock, not the receiving medium.",
                [],
            )

    def remove_wrong_product(self):
        marker = "\n\nCommercial Product:"
        runner.require(marker in self.before["notes"], "Product provenance drift")
        self.after["notes"] = self.before["notes"].replace(
            marker,
            "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product:",
            1,
        )
        reason = "The earlier LB commercial-product expansion was incorrect for M258/JCM266: three unrelated LB constituents are removed and alpha-methylbutyric acid is restored in the fatty-acid stock at the source batch amount, 0.5 g. The historical supplier paragraph above is retained only as superseded provenance. No chemical grounding is assigned to the restored ingredient."
        self.note(self.after, reason)
        for i, name in [(23, "Tryptone"), (24, "Yeast extract"), (25, "Sodium chloride")]:
            runner.require(
                self.before["ingredients"][i]["preferred_term"] == name,
                "Wrong-product baseline drift",
            )
            self.claim(
                ["notes"],
                ["ingredients", i, "concentration"],
                "JCM266",
                None,
                "correct",
                "wrong_product_removed",
                reason + " Removed node: " + name + ".",
                [],
                snippet="\u03b1-Methylbutyric acid 0.5 g",
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
        if self.key == "M258":
            self.remove_wrong_product()
        for i, row in enumerate(self.rows(self.key, 0)):
            if not row.get("reference_media_id") and row["component_name"] not in REDUCERS:
                self.direct(i)
        for i, row in enumerate(self.rows(self.key, 0)):
            if row.get("reference_media_id"):
                self.stock(["solutions"], self.key, 0, i)
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
            notes="Corrected stock boundaries and unsupported quantity assertions with exact batch-amount evidence. M258 supersedes its erroneous LB expansion and restores alpha-methylbutyric acid, rumen/fatty-acid preparations and separate reducing agents. M260 nests the trace-mineral dose inside MJ(-N) seawater. Preserved unrelated annotations and append-only history. No final volume, percent basis or chemical grounding inferred.",
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
            "# Ingredient Identity And Nested Stock Review",
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
