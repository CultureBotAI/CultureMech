#!/usr/bin/env python3
"""Restore three inspected filtered media without inventing stock dilution rates."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-filtered-sulfide-media"
CONTEXT_SHA = "9ef2e61a0c079c15a0cc2577004711a46a8d425872737561c8e333a2655490d4"
ACTION = "RESTORED_FILTERED_MEDIA_STOCK_SCOPES_AND_BATCH_AMOUNTS_WITH_EVIDENCE"
NUMBERS = {"M199": "206", "M206": "213", "M207": "214", "M142": "151"}
SIZES = {"M199": [11, 12], "M206": [19], "M207": [21], "M142": [10, 12, 14]}
SULFIDE = "Na2S\u30fb9H2O"
SALT_RATE = (
    "Use Salt base solution of Medium No. 151 with 17.0 g/L (final) NaCl and 2.5 mg/L (final) KI."
)
TRACE_PREPARATION = "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."
STEPS = {
    "M199": [
        (
            "MIX",
            "Mix ingredients, except sulfur and Na2S\u00b79H2O, and adjust pH to 6.5 with H2SO4.",
        ),
        ("FILTER", "Sterilize by filtration while gassing with H2-CO2 (80:20) gas mixture."),
        ("HEAT", "Steam sulfur for 3 hr on each of 3 successive days."),
        (
            "AUTOCLAVE",
            "Neutralize Na2S\u00b79H2O as a 5% solution, and autoclave under a N2 atmosphere.",
        ),
        (
            "MIX",
            "Aseptically and anaerobically add sterile sulfur to the medium under a H2-CO2 (80:20) atmosphere.",
        ),
        ("MIX", "Prior to inoculation, add the sterile Na2S\u00b79H2O solution."),
    ],
    "M206": [
        ("MIX", "Mix ingredients, except Na2S\u00b79H2O, and adjust pH to 6.9 with 1 N H2SO4."),
        ("FILTER", "Sterilize by filtration under a N2-CO2 (80:20) gas mixture."),
        (
            "AUTOCLAVE",
            "Neutralize Na2S\u00b79H2O as a 5% solution and autoclave under a N2 atmosphere.",
        ),
        (
            "MIX",
            "Aseptically and anaerobically add the sterile Na2S\u00b79H2O solution to the medium under a N2-CO2 (80:20) atmosphere, and readjust pH to 6.9, if necessary.",
        ),
    ],
    "M207": [
        ("MIX", "Mix ingredients except Na2S\u00b79H2O and adjust pH to 6.9 with H2SO4."),
        ("FILTER", "Sterilize by filtration under H2-CO2 (80:20) gas mixture."),
        ("AUTOCLAVE", "Neutralize Na2S\u00b79H2O solution and autoclave under a N2 atmosphere."),
        (
            "MIX",
            "Aseptically and anaerobically add the sterile Na2S\u00b79H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary.",
        ),
    ],
}
PRESSURE = {
    "M199": "Pressurize inoculated bottles to 100 kPa H2-CO2 (80:20).",
    "M206": "Pressurize inoculated bottles to 200 kPa N2-CO2 (80:20).",
    "M207": "Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).",
}


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
    for key, steps in STEPS.items():
        text = parsed["JCM" + NUMBERS[key]]
        runner.require(all(literal_match(s, text) for _, s in steps), "Preparation drift")
        runner.require(literal_match(PRESSURE[key], text), "Pressure drift")
    runner.require(literal_match(SALT_RATE, parsed["JCM206"]), "Explicit stock rates drift")
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

    def original_amount(self, pointer, source, si, ri):
        row = self.rows(source, si)[ri]
        original = "JCM" + NUMBERS[source]
        text = self.data[original]
        if si == 0:
            text = text[: text.index("Mix ingredients")]
        elif source == "M142":
            text = (
                text.split("Salt base solution:", 1)[1].split("Trace minerals:", 1)[0]
                if si == 1
                else text.split("Trace minerals:", 1)[1].split("Dissolve nitrilotriacetic", 1)[0]
            )
        else:
            raise ValueError("Unreviewed original table")
        name = row["component_name"].replace("\u30fb", "\u00b7").replace("--", "-")
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
            pointer + ["notes"],
            original,
            match.group(),
            "Original recipe table corroborates this exact chemical form and source batch input; it does not establish a final volume.",
            pointer,
        )

    def direct(self, ri):
        row = self.rows(self.key, 0)[ri]
        if row.get("volume") is not None:
            p = self.leaf(["ingredients"], self.key, 0, ri)
            self.original_amount(p, self.key, 0, ri)
            return
        node, old = self.clone(row["component_name"])
        node.pop("concentration")
        acid = row["component_name"] == "H2SO4"
        reason = (
            "Source pH-adjustment reagent with no fixed dose."
            if acid
            else "Source atmosphere context, not a fixed gas input or dissolved concentration."
        ) + " Removed the unsupported VARIABLE placeholder."
        if acid and self.key == "M206":
            reason += " Original JCM213 specifies 1 N H2SO4 reagent; normality is not converted to molarity or a receiving-medium dose."
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
        quote = STEPS[self.key][0 if acid else (3 if self.key == "M199" else 2)][1]
        if not acid and row["component_name"] not in {"N2", "Nitrogen gas"}:
            quote = STEPS[self.key][1][1]
        self.corroborate(p + ["notes"], "JCM" + NUMBERS[self.key], quote, reason, p)

    def stock(self, ri):
        row = self.rows(self.key, 0)[ri]
        p = stocks.Review.stock(self, ["solutions"], self.key, 0, ri)
        node = runner.get_node(self.after, p)
        salt = row["component_name"].startswith("Salt base")
        quote = (
            "Salt base solution (see below) 1.0 L"
            if salt
            else "Trace minerals (see Medium No. 151) 10.0 ml"
        )
        self.corroborate(
            p + ["concentration"],
            "JCM" + NUMBERS[self.key],
            quote,
            "Prepared-stock input per listed batch; not an established final-medium volume or per-liter dose.",
            [],
        )
        if salt:
            runner.require(self.key == "M199", "Unreviewed salt base")
            self.corroborate(
                p + ["notes"],
                "JCM206",
                SALT_RATE,
                "Expand only the JCM151 salt base with these two source-explicit stock-rate overrides, not the whole parent medium.",
                [],
            )
            for i, leaf in enumerate(self.rows("M199", 1)):
                if leaf["component_name"] in {"NaCl", "KI"}:
                    child, old = self.clone(leaf["component_name"])
                    child["concentration"] = {
                        "value": shared.numeric(leaf["volume"]),
                        "unit": "G_PER_L" if leaf["component_name"] == "NaCl" else "MG_PER_L",
                    }
                    reason = "Original JCM206 explicitly states this final salt-base stock concentration. Relocated from the flattened main medium; this is not a receiving-medium concentration. Other stock rows do not acquire an inferred final-volume denominator."
                    self.note(child, reason)
                    cp = self.append(p + ["composition"], child)
                    self.claim(
                        cp + ["concentration"],
                        old + ["concentration"],
                        self.key,
                        stocks.row_path(self.key, 1, i),
                        "correct",
                        "explicit_stock_rate",
                        reason,
                        cp,
                    )
                    self.lineage_node(cp, old, self.key, 1, i, "explicit_stock_rate")
                    self.corroborate(cp + ["concentration"], "JCM206", SALT_RATE, reason, cp)
                else:
                    cp = self.leaf(p + ["composition"], self.key, 1, i)
                    parent_row = self.rows("M142", 1)[i]
                    runner.require(
                        all(
                            leaf.get(k) == parent_row.get(k)
                            for k in ("component_name", "volume", "unit")
                        ),
                        "Unreviewed inherited stock change",
                    )
                    self.original_amount(cp, "M142", 1, i)
        else:
            for i, leaf in enumerate(self.rows("M142", 2)):
                if leaf["component_name"] == "KOH solution":
                    node.setdefault("solutions", [])
                    self.leaf(p + ["solutions"], "M142", 2, i)
                else:
                    cp = self.leaf(p + ["composition"], "M142", 2, i)
                    self.original_amount(cp, "M142", 2, i)
            node["preparation_notes"] = TRACE_PREPARATION
            self.corroborate(
                p + ["preparation_notes"],
                "JCM151",
                TRACE_PREPARATION,
                "pH 6.5 then 7.0 belongs only to the trace-mineral stock, not the receiving medium.",
                [],
            )

    def sulfide(self, ri):
        row = self.rows(self.key, 0)[ri]
        runner.require(
            row["component_name"] == SULFIDE and row["volume"] == 0.5 and row["unit"] == "g",
            "Sulfide amount drift",
        )
        text = STEPS[self.key][3 if self.key == "M199" else 2][1]
        reason = (
            "Separate sulfide preparation; composition notes retain the 0.5 g receiving-batch contribution, not a stock-batch recipe. Stock solvent volume and addition volume are unspecified. "
            + (
                "The source 5% label has unspecified percentage basis; no numeric stock strength or derived dose is asserted."
                if self.key != "M207"
                else "JCM214 gives no stock strength; do not inherit the 5% label from another medium."
            )
        )
        node = {
            "preferred_term": SULFIDE + " separately prepared solution",
            "composition": [],
            "notes": reason,
            "preparation_notes": text,
        }
        p = self.append(["solutions"], node)
        self.corroborate(p + ["preparation_notes"], "JCM" + NUMBERS[self.key], text, reason, [])
        self.lineage_node(p, None, self.key, 0, ri, "separate_preparation")
        cp = self.leaf(p + ["composition"], self.key, 0, ri, prepared=True)
        self.original_amount(cp, self.key, 0, ri)
        self.corroborate(
            cp + ["notes"],
            "JCM" + NUMBERS[self.key],
            text,
            "The receiving-batch sulfide mass belongs to this separate preparation, not to an invented stock batch or fixed final concentration.",
            cp,
        )

    def formulate(self):
        rows = self.rows(self.key, 0)
        for i, row in enumerate(rows):
            if not row.get("reference_media_id") and row["component_name"] != SULFIDE:
                self.direct(i)
        for i, row in enumerate(rows):
            if row.get("reference_media_id"):
                self.stock(i)
        self.sulfide(next(i for i, row in enumerate(rows) if row["component_name"] == SULFIDE))
        self.after["preparation_steps"] = [
            {"step_number": i + 1, "action": action, "description": text}
            for i, (action, text) in enumerate(STEPS[self.key])
        ]
        for i, (_, text) in enumerate(STEPS[self.key]):
            self.corroborate(
                ["preparation_steps", i, "description"],
                "JCM" + NUMBERS[self.key],
                text,
                "Recipe-specific filtration, separate sterilization and later addition stages. No unspecified pore size, dose, percentage basis or final volume is inferred.",
                [],
            )
        self.note(self.after, "Original post-inoculation instruction: " + PRESSURE[self.key])
        self.corroborate(
            ["notes"],
            "JCM" + NUMBERS[self.key],
            PRESSURE[self.key],
            "Post-inoculation pressure and gas composition, not a dissolved-gas concentration.",
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
                    "notes": f"source_type={'culture_collection_page' if source.startswith('JCM') else 'dataset'}; discovery_mode={'existing_record_reference' if source in {self.key, 'JCM' + NUMBERS[self.key]} else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied. Recipe quantities/preparation only; chemical groundings and growth claims are not recertified.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restored batch inputs, referenced stock composition and separate sulfide preparation. Retained only source-explicit stock rates; removed unsupported final-rate and VARIABLE assertions with exact evidence. Preserved annotations and history; no final volume, percent basis or stock dose inferred.",
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
            "# Filtered Medium Ingredient And Stock Review",
            "",
            f"- Record: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Stock inputs, stock-only rates and receiving-batch masses are distinct. Final volume, unspecified stock strengths/doses and chemical grounding remain unresolved. Terminal checks are recorded in ../validation.json.",
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
