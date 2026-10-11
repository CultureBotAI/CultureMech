#!/usr/bin/env python3
"""Repair three source-defined Pyrodictium formulations and their stock scopes."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_m689_stocks as prior
import repair_methanogen_stock_boundaries as shared

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import html_recipe_text, literal_match

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-pyrodictium-variants"
CONTEXT = HERE.parent / "20261008-basal-makeup/next-pyrodictium-context.json"
CONTEXT_SHA = "09b7f63c7eff389cfce01e637008468bf4558ed2ca0a294e70d5d5c5d1b1615a"
ACTION = "RESTORED_PYRODICTIUM_VARIANT_AMOUNTS_AND_STOCK_SCOPES_WITH_EVIDENCE"
NUMBERS = {"M196": "203", "M197": "204", "M198": "205", "M142": "151"}
SIZES = {"M196": [10, 2], "M197": [10], "M198": [11], "M142": [10, 12, 14]}
SULFIDE = "5% Na2S\u00b79H2O solution (pH 7.0)"
VARIANTS = {
    "M197": "Use Medium No. 203 with 0.2 g/L (final) yeast extract.",
    "M198": "Use Medium No. 203 with 0.5 g/L (final) yeast extract and 0.1 mg/L Na2WO4\u00b72H2O, and omit citric acid.",
}
MODIFICATIONS = {
    "M197": ["Use the source-explicit 0.2 g/L final yeast-extract concentration."],
    "M198": [
        "Use the source-explicit 0.5 g/L final yeast-extract concentration.",
        "Use the source-explicit 0.1 mg/L sodium tungstate dihydrate concentration.",
        "Omit citric acid as instructed by JCM205; none is introduced from the parent or its two referenced stock tables.",
    ],
}
STEPS = [
    (
        "AUTOCLAVE",
        "Mix components except sulfur, adjust pH to 5.5 with H2SO4 and autoclave under a N2 gas atmosphere.",
    ),
    ("HEAT", "Steam sulfur for 3 hr on each of 3 successive days."),
    (
        "ALIQUOT",
        "Aseptically distribute the medium and sulfur into culture vessels (e.g., 20 ml of the medium and 0.6 g sulfur in 120 ml serum bottles) under a stream of a H2-CO2 (80:20, v/v) gas mixture and seal with butyl rubber stoppers.",
    ),
    (
        "MIX",
        "Prior to inoculation, add per litter the following solution (autoclave and stored under a N2 atmosphere): 5% Na2S\u00b79H2O solution (pH 7.0) 10.0 ml",
    ),
    ("ADJUST_PH", "Readjust pH to 5.5, if necessary."),
]
PRESSURE = "Pressurize inoculated vessels to 200kPa H2 -CO2 (80:20, v/v)."


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
    for key, quote in VARIANTS.items():
        runner.require(
            literal_match(quote, parsed["JCM" + NUMBERS[key]]), "Variant instruction drift"
        )
    runner.require(
        all(literal_match(text, parsed["JCM203"]) for _, text in STEPS)
        and literal_match(PRESSURE, parsed["JCM203"]),
        "Preparation text drift",
    )
    return parsed


class Review(prior.Review):
    def __init__(self, before, key):
        runner.require(key in {"M196", "M197", "M198"}, "Unreviewed record")
        context = frozen()
        shared.Review.__init__(self, before, key, context=context, parsed=sources(context))
        runner.require(
            not any(
                before.get(k)
                for k in (
                    "parent_media",
                    "variant_children",
                    "variant_relationship",
                    "variant_modifications",
                    "preparation_steps",
                )
            ),
            "Existing curation needs reconciliation",
        )
        self.originals = {}
        for field in ("ingredients", "solutions"):
            for i, node in enumerate(before[field]):
                name = node["preferred_term"]
                if name in self.originals:
                    runner.require(
                        key == "M196"
                        and name == SULFIDE
                        and self.originals[name] == ["solutions", 2]
                        and (field, i) == ("solutions", 3),
                        "Unreviewed duplicate",
                    )
                    old = before["solutions"][2]
                    runner.require(
                        {k: v for k, v in node.items() if k != "notes"} == old,
                        "Conflicting duplicate annotations",
                    )
                self.originals[name] = [field, i]
        self.after["ingredients"], self.after["solutions"] = [], []
        self.gas_paths = {}

    def direct(self, ri):
        row = self.rows(self.key, 0)[ri]
        name = row["component_name"]
        explicit_rate = self.key in VARIANTS and name in {
            "Yeast extract (BD-Difco)",
            "Na2WO4\u30fb2H2O",
        }
        if not explicit_rate and row.get("volume") is not None:
            return self.leaf(["ingredients"], self.key, 0, ri)
        node, old = self.clone(name)
        if explicit_rate:
            node["concentration"] = {
                "value": shared.numeric(row["volume"]),
                "unit": "MG_PER_L" if name.startswith("Na2WO4") else "G_PER_L",
            }
            kind = "explicit_medium_rate"
            reason = "Retain only the original JCM variant's explicit medium concentration, not a conversion of TOGO's extracted batch-unit field. No final volume is inferred for the inherited parent or other ingredients."
        else:
            runner.require(row.get("volume") is None, "Unquantified context drift")
            node.pop("concentration")
            kind = "unquantified_input"
            reason = (
                "Source pH-adjustment reagent with no fixed dose."
                if name == "H2SO4"
                else "Source atmosphere context, not a fixed gas input or dissolved concentration."
            ) + " Removed the unsupported VARIABLE placeholder."
        self.note(node, reason)
        p = self.append(["ingredients"], node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"],
            self.key,
            stocks.row_path(self.key, 0, ri),
            "correct" if explicit_rate else "remove_unsupported",
            kind,
            reason,
            p,
        )
        self.lineage_node(p, old, self.key, 0, ri, kind)
        if explicit_rate:
            self.corroborate(
                p + ["concentration"], "JCM" + NUMBERS[self.key], VARIANTS[self.key], reason, p
            )
        else:
            quote = (
                STEPS[0][1]
                if name in {"H2SO4", "N2"}
                else "under a stream of a H2-CO2 (80:20, v/v) gas mixture"
            )
            self.corroborate(
                p + ["notes"],
                "JCM203",
                quote,
                "Original inherited preparation identifies reagent/atmosphere context without specifying a fixed amount.",
                p,
            )
        return p

    def stock(self, ri):
        row = self.rows(self.key, 0)[ri]
        name = row["component_name"]
        node, old = self.clone(name)
        sulfide = name == SULFIDE
        value = Decimal(str(row["volume"])) / (1000 if row["unit"] == "ml" and not sulfide else 1)
        runner.require(row["unit"] in {"L", "ml"}, "Stock input drift")
        node["concentration"] = {
            "value": shared.numeric(value),
            "unit": "ML_PER_L" if sulfide else "L",
        }
        kind = "per_liter_dose" if sulfide else "batch_dose"
        reason = (
            "Original JCM203 specifies one later 10 ml per-liter addition before inoculation (source spells 'liter' as 'litter'). This is not a fixed final dilution or mass rate. The 5% label has unspecified percentage basis; stock pH is 7.0, not the receiving medium pH."
            if sulfide
            else f"Source prepared-stock input: {row['volume']} {row['unit']} = {shared.numeric(value)} L per receiving batch, not grams per liter. This input volume does not establish final supplemented-medium volume."
        )
        if sulfide and self.key == "M196":
            reason += " Consolidated the duplicate extracted descriptor and self-reference into this single source-supported addition; no quantities are summed and no self-nested stock is created."
        self.note(node, reason)
        p = self.append(["solutions"], node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"],
            self.key,
            stocks.row_path(self.key, 0, ri),
            "correct",
            kind,
            reason,
            [],
        )
        self.lineage_node(p, old, self.key, 0, ri, kind)
        if sulfide:
            self.corroborate(p + ["concentration"], "JCM203", STEPS[3][1], reason, [])
            node["preparation_notes"] = (
                "Autoclave and store this stock under N2; add once at 10 ml per liter before inoculation. The source gives no percentage basis or final receiving-medium volume."
            )
            self.corroborate(
                p + ["preparation_notes"],
                "JCM203",
                STEPS[3][1],
                "Stock-only preparation and later addition; not a second stock dose.",
                [],
            )
            if self.key == "M196":
                self.claim(
                    p + ["concentration"],
                    ["solutions", 2, "concentration"],
                    self.key,
                    stocks.row_path(self.key, 1, 0),
                    "correct",
                    "duplicate_stock_member",
                    "Remove the extra descriptor, retaining its supported dose once on this descriptor. Original JCM203 has one later sulfide addition, not two. The original annotated duplicate supplies this node's preserved metadata.",
                    [],
                )
                self.lineage_node(p, ["solutions", 2], self.key, 1, 0, "duplicate_stock_member")
                gas = next(
                    i
                    for i, n in enumerate(self.after["ingredients"])
                    if n["preferred_term"] == "N2"
                )
                self.claim(
                    ["ingredients", gas, "notes"],
                    None,
                    self.key,
                    stocks.row_path(self.key, 1, 1),
                    "evidence_only",
                    "stock_atmosphere",
                    "This repeated N2 mention is sulfide-stock atmosphere context, not an additional gas dose or a second ingredient.",
                    ["ingredients", gas],
                )
            return
        section = 1 if name.startswith("Salt base") else 2
        runner.require(row["reference_media_id"] == "M142", "Stock reference drift")
        for i, ingredient in enumerate(self.rows("M142", section)):
            if ingredient["component_name"] == "KOH solution":
                node.setdefault("solutions", [])
                self.leaf(p + ["solutions"], "M142", section, i)
            else:
                self.leaf(p + ["composition"], "M142", section, i)
        quote = (
            "Salt base solution (see Medium No. 151) 1.0 L"
            if section == 1
            else "Trace minerals (see Medium No. 151) 10.0 ml"
        )
        self.corroborate(
            p + ["concentration"],
            "JCM203",
            quote,
            "Original inherited stock identity and batch input; only the named M142 stock section is expanded.",
            [],
        )
        self.corroborate(
            p + ["notes"],
            "JCM151",
            "Salt base solution:" if section == 1 else "Trace minerals:",
            "Use the named stock table, not the complete Pyrococcus medium.",
            [],
        )
        if section == 2:
            node["preparation_notes"] = self.data["M142"]["comments"][1]["comment"]
            self.comment_claim(
                p + ["preparation_notes"],
                "M142",
                1,
                "stock_preparation",
                "pH 6.5 then 7.0 applies only to this trace-mineral stock, not the receiving medium.",
                [],
            )
            self.corroborate(
                p + ["preparation_notes"],
                "JCM151",
                "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.",
                "Original stock-only preparation.",
                [],
            )

    def relationships(self):
        children = ["M197", "M198"] if self.key == "M196" else [self.key]
        for child in children:
            target = child if self.key == "M196" else "M196"
            spec = next(r for r in self.context["records"] if r["key"] == target)
            data = runner.load_yaml(spec["before_text"])
            link = {
                "id": data["id"],
                "name": data["name"],
                "path": spec["path"],
                "relationship": "DERIVED_FROM",
                "notes": "Original JCM variant directive resolved to the exact tracked parent/child record. Explicit child rates do not establish a final volume for the parent.",
            }
            if self.key == "M196":
                self.after.setdefault("variant_children", []).append(link)
                p = ["variant_children", len(self.after["variant_children"]) - 1]
            else:
                self.after["parent_media"] = link
                p = ["parent_media"]
                self.after["variant_relationship"] = "DERIVED_FROM"
                self.after["variant_modifications"] = MODIFICATIONS[child].copy()
                for field in ("variant_relationship", "variant_modifications"):
                    self.corroborate(
                        [field],
                        "JCM" + NUMBERS[child],
                        VARIANTS[child],
                        "Source-explicit child formulation; no parent quantity is overwritten.",
                        [],
                    )
            self.corroborate(
                p + ["notes"],
                "JCM" + NUMBERS[child],
                VARIANTS[child],
                "Original source defines this variant relationship; source IDs are reconciled to the current exact tracked sibling paths.",
                p,
            )

    def formulate(self):
        rows = self.rows(self.key, 0)
        for i, row in enumerate(rows):
            if row["component_name"] in self.old_indices:
                self.direct(i)
        # Preserve the source's initial-stock/later-stock boundary even in expanded variants.
        for name in (
            "Salt base solution (see Medium [M142])",
            "Trace minerals (see Medium [M142])",
            SULFIDE,
        ):
            i = next(i for i, row in enumerate(rows) if row["component_name"] == name)
            self.stock(i)
        self.after["preparation_steps"] = [
            {"step_number": i + 1, "action": action, "description": text}
            for i, (action, text) in enumerate(STEPS)
        ]
        for i, (_, text) in enumerate(STEPS):
            self.corroborate(
                ["preparation_steps", i, "description"],
                "JCM203",
                text,
                "Original inherited preparation with separate initial medium, sulfur, aliquoting, later sulfide dose and optional pH readjustment stages.",
                [],
            )
        note = (
            "Source discrepancy: TOGO's inherited preparation says H2-CO4, while original JCM203 specifies H2-CO2. Effective preparation follows JCM203; the inconsistent TOGO wording remains quoted as discrepancy evidence. Post-inoculation instruction: "
            + PRESSURE
        )
        if self.key == "M198":
            note += " JCM205 instructs omission of citric acid. The inspected JCM203 main table and the two inherited JCM151 stock tables contain no citric-acid row; the omission is retained as source context, not an invented ingredient deletion."
        self.note(self.after, note)
        self.claim(
            ["notes"],
            ["notes"],
            self.key,
            ["comments", 0, "comment"],
            "correct",
            "source_discrepancy",
            "Record the source discrepancy, not an assertion that the erroneous H2-CO4 transcription is the actual atmosphere.",
            [],
            self.data[self.key]["comments"][0]["comment"],
        )
        self.corroborate(
            ["notes"],
            "JCM203",
            STEPS[2][1],
            "Original H2-CO2 atmosphere supports resolving the TOGO discrepancy.",
            [],
        )
        self.corroborate(
            ["notes"],
            "JCM203",
            PRESSURE,
            "Post-inoculation source pressure instruction, not a dissolved-gas concentration.",
            [],
        )
        if self.key in VARIANTS:
            self.corroborate(
                ["notes"],
                "JCM" + NUMBERS[self.key],
                VARIANTS[self.key],
                "Original variant directive supports explicit child rates and any stated omissions, without importing the referenced stocks' parent medium.",
                [],
            )
        self.relationships()

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
                    "notes": f"source_type={'culture_collection_page' if source.startswith('JCM') else 'dataset'}; discovery_mode={'existing_record_reference' if source in {self.key, 'JCM' + NUMBERS[self.key]} else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied. Source recipe quantities and preparation only; chemical mappings and growth claims are not recertified.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restored source-specific stock doses, compositions, preparation, and parent/variant links. Consolidated M196's duplicate sulfide descriptor without summing. Retained explicit child rates separately from unverified inherited final concentrations. Preserved prior history and chemical annotations; no percentage basis or final volume inferred.",
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
            "# Pyrodictium Ingredient And Stock Review",
            "",
            f"- Record: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Explicit child medium rates are kept separate from inherited batch masses. Stock doses are not final dilution denominators. Percent basis, final parent/stock volumes and chemical grounding remain unresolved. See ../validation.json for terminal gates.",
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
