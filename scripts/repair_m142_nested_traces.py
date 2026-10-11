#!/usr/bin/env python3
"""Restore seven source-defined nested trace-stock formulations with evidence."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_methanogen_stock_boundaries as shared
from bs4 import BeautifulSoup

from culturemech.curate.curation_event import record_curation_event

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-m142-nested-traces"
CONTEXT_SHA = "c5f79b827061f21a92b21ae48aca670d408a0efbe88b52b48e0d8ea95923c1aa"
ACTION = "RESTORED_NESTED_M142_TRACE_STOCKS_WITH_EVIDENCE"
SIZES = {
    "M933": [5, 2, 11, 3],
    "M1106": [8, 2, 3, 2],
    "M1124": [16, 4, 3],
    "M1153": [11, 1, 4, 3],
    "M1378": [14, 4],
    "M1389": [4, 1, 10, 4],
    "M1390": [2, 6, 4, 10, 4],
}
# Source-section graph; self references point to a named local stock, not the medium.
LINKS = {
    "M933": {(0, 2): 2, (2, 10): 3},
    "M1106": {(1, 0): 2, (1, 1): 3},
    "M1124": {(0, 13): 2},
    "M1153": {(0, 10): 2, (1, 0): 3},
    "M1378": {(0, 9): 1},
    "M1389": {(0, 1): 2, (2, 9): 3},
    "M1390": {(0, 1): 3, (3, 9): 4},
}
MAIN = {"M933": 2, "M1106": 2, "M1124": 2, "M1153": 2, "M1378": 1, "M1389": 2, "M1390": 3}
PER_LITER = {"M933": {1: 0}, "M1389": {1: 0}, "M1390": {2: 1}}
GASES = {"Carbon dioxide gas", "Nitrogen gas", "N2", "Hydrogen gas", "N2O"}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    return json.loads(raw)


def sources(context):
    parsed = {}
    for key, source in context["sources"].items():
        meta, raw = source["metadata"], source["raw"]
        url = (
            "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=" + key[3:]
            if key.startswith("JCM")
            else "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=" + key
        )
        runner.require(
            meta["url"] == meta["response_url"] == url
            and meta["http_status"] == 200
            and runner.sha(raw.encode(meta["encoding"])) == meta["sha256"],
            "Capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        parsed[key] = (
            " ".join(BeautifulSoup(raw, "html.parser").get_text().split())
            if key.startswith("JCM")
            else json.loads(raw)
        )
    for key, sizes in {**SIZES, "M142": [10, 12, 14]}.items():
        meta = parsed[key]["meta"]
        number = meta["original_media_id"].removeprefix("JCM_M")
        runner.require(
            meta["gm"] == "http://togomedium.org/medium/" + key
            and meta["src_url"] == context["sources"]["JCM" + number]["metadata"]["url"]
            and f"Search for medium no. = [{number}]." in parsed["JCM" + number]
            and [len(s["items"]) for s in parsed[key]["components"]] == sizes,
            "Source identity/topology drift",
        )
    return parsed


class Review(stocks.Review):
    def __init__(self, before, key):
        context = frozen()
        shared.Review.__init__(self, before, key, context=context, parsed=sources(context))
        self.originals = {}
        for field in ("ingredients", "solutions"):
            for i, node in enumerate(before.get(field, [])):
                runner.require(node["preferred_term"] not in self.originals, "Ambiguous baseline")
                self.originals[node["preferred_term"]] = [field, i]
        self.after["ingredients"], self.after["solutions"] = [], []
        self.section_paths, self.gas_paths = {}, {}

    def comment_claim(self, pointer, source, ci, kind, reason, ep):
        sp = ["comments", ci, "comment"]
        self.claim(
            pointer,
            None,
            source,
            sp,
            "evidence_only",
            kind,
            reason,
            ep,
            snippet=runner.get_node(self.data[source], sp),
        )

    def original_claim(self, pointer, snippet, reason, ep):
        source = "JCM" + self.data[self.key]["meta"]["original_media_id"][5:]
        self.claim(
            pointer,
            None,
            source,
            None,
            "evidence_only",
            "original_support",
            reason,
            ep,
            snippet=snippet,
        )

    def lineage_node(self, p, old, source, si, ri, kind):
        self.lineage.append(
            {
                "pointer": p,
                "old_pointer": old,
                "source": source,
                "source_pointer": stocks.row_path(source, si, ri),
                "kind": kind,
            }
        )

    def leaf(self, parent, source, si, ri, *, prepared=False):
        row = self.rows(source, si)[ri]
        name = row["component_name"]
        sp = stocks.row_path(source, si, ri)
        node, old = self.clone(name, source=source)
        if name in GASES:
            runner.require(old is not None and row.get("volume") is None, "Gas drift")
            p = self.gas_paths.get(name)
            if p is None:
                p = self.append(parent, node)
                self.gas_paths[name] = p
                self.lineage_node(p, old, source, si, ri, "gas")
            self.claim(
                p + ["concentration"],
                old + ["concentration"],
                source,
                sp,
                "unsupported",
                "gas",
                "Retained legacy VARIABLE placeholder, not a verified fixed gas amount. Repeated source mentions do not imply duplicate doses.",
            )
            return p
        if source == "M142" and name == "KOH solution":
            node["composition"] = []
            node["notes"] = "Stock pH-adjustment reagent with no fixed dose or numeric strength."
            p = self.append(parent, node)
            self.claim(
                p + ["notes"], None, source, sp, "add", "unquantified_titrant", node["notes"], []
            )
            self.lineage_node(p, None, source, si, ri, "unquantified_titrant")
            return p
        if self.key == "M1153" and source == self.key and si == 3:
            if ri == 0:
                node.pop("concentration", None)
                node["composition"] = []
                reason = "Use 0.1 N H2SO4 as makeup reagent to a final stock volume of 100.0 ml; the actual acid addition volume is unspecified. The extracted 100 ml is not an acid dose. Normality is not converted to molarity."
                kind = "makeup_reagent"
            else:
                runner.require(
                    ri == 1 and row["volume"] == 40 and row["unit"] == "g", "Iron stock drift"
                )
                node["concentration"] = {"value": "400", "unit": "G_PER_L"}
                reason = "Explicit final iron-stock volume: 100.0 ml = 0.1 L. Calculation: 40.0 g / 0.1 L = 400 g/L in this stock only, not the receiving medium."
                kind = "stock_rate"
            self.note(node, reason)
            p = self.append(parent, node)
            ep = [] if ri == 0 else p
            self.claim(
                p + ["concentration"],
                old + ["concentration"],
                source,
                sp,
                "remove_unsupported" if ri == 0 else "correct",
                kind,
                reason,
                ep,
            )
            self.comment_claim(p + ["notes"], source, 1, "final_stock_volume", reason, ep)
            self.original_claim(
                p + ["notes"],
                "40.0 g FeSO4·7H2O in 0.1 N H2SO4 solution and fill up to 100.0 ml.",
                reason,
                ep,
            )
            self.lineage_node(p, old, source, si, ri, kind)
            return p
        if self.key == "M1106" and source == self.key and si == 3 and ri == 0:
            return self.stock(parent, source, si, ri)
        p = super().leaf(parent, source, si, ri, prepared=prepared)
        if old and "[Merged 2 duplicates:" in runner.get_node(self.before, old).get("notes", ""):
            reason = "The earlier duplicate-summing note is superseded: it combined separate preparation scopes and source units. This node carries only the batch input at the cited source row; other occurrences are separate scoped ingredients."
            self.note(runner.get_node(self.after, p), reason)
            self.claim(
                p + ["notes"], old + ["notes"], source, sp, "correct", "duplicate_scope", reason, p
            )
        if self.key == "M1153" and source == self.key and si == 2 and ri == 2:
            reason = "Both TOGO and original JCM1084 print NaWO4. The legacy sodium-tungstate grounding is retained, not recertified; the apparent formula discrepancy is unresolved. No formula normalization or molar conversion is performed."
            self.note(runner.get_node(self.after, p), reason)
            self.claim(
                p + ["notes"],
                old + ["notes"],
                source,
                sp,
                "evidence_only",
                "identity_conflict",
                reason,
                p,
            )
            self.original_claim(p + ["notes"], "NaWO4·2H2O 0.4 mg", reason, p)
        return p

    def stock(self, parent, source, si, ri, definition=None):
        row = self.rows(source, si)[ri]
        sp = stocks.row_path(source, si, ri)
        node, old = self.clone(row["component_name"], source=source)
        amount, unit = row["volume"], row["unit"]
        runner.require(unit in {"L", "ml"}, "Stock volume drift")
        per_liter = source == self.key and si in PER_LITER.get(self.key, {})
        value = Decimal(str(amount)) * (1000 if per_liter and unit == "L" else 1)
        if not per_liter and unit == "ml":
            value /= 1000
        node["composition"] = []
        node["concentration"] = {
            "value": shared.numeric(value),
            "unit": "ML_PER_L" if per_liter else "L",
        }
        reason = (
            f"Source stock addition: {amount} {unit}; explicitly {shared.numeric(value)} ml per receiving-medium liter."
            if per_liter
            else f"Source stock addition: {amount} {unit} = {shared.numeric(value)} L per receiving batch, not grams per liter or a dose per final liter."
        )
        if row.get("conc_unit") == "%":
            reason += " Percentage basis is unspecified; no numeric stock strength is asserted."
        if row.get("conc_unit") == "N":
            reason += f" Source reagent strength: {row['conc_value']} N; normality is not converted to molarity."
        self.note(node, reason)
        p = self.append(parent, node)
        kind = "per_liter_dose" if per_liter else "batch_dose"
        self.claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            source,
            sp,
            "correct" if old else "add",
            kind,
            reason,
            [],
        )
        self.lineage_node(p, old, source, si, ri, kind)
        if per_liter:
            ci = PER_LITER[self.key][si]
            self.comment_claim(p + ["concentration"], source, ci, "dose_scope", reason, [])
            self.original_claim(
                p + ["concentration"], "add per liter the following solution", reason, []
            )
        if definition is not None:
            self.section_paths[definition] = p
            self.fill(p, source, definition)
        elif row.get("reference_media_id") == "M142":
            self.fill(p, "M142", 2)
            text = self.data["M142"]["comments"][1]["comment"]
            node["preparation_notes"] = text
            self.comment_claim(
                p + ["preparation_notes"],
                "M142",
                1,
                "stock_preparation",
                "This pH adjustment belongs only to the innermost M142 trace stock.",
                [],
            )
        return p

    def bicarbonate(self):
        row = self.rows(self.key, 0)[8]
        runner.require(
            row["component_name"] == "NaHCO3" and row["volume"] == 1 and row["unit"] == "g",
            "Bicarbonate drift",
        )
        stock = {
            "preferred_term": "NaHCO3 separately prepared solution",
            "composition": [],
            "concentration": {"value": "0.0125", "unit": "L"},
        }
        reason = "Receiving-batch contribution: 1.0 g NaHCO3 supplied as the explicitly specified 8% (w/v) stock. Calculation: 8 g/100 ml = 0.08 g/ml; 1.0 g / 0.08 g/ml = 12.5 ml = 0.0125 L per batch. This is not a per-final-liter dose."
        stock["notes"] = reason
        p = self.append(["solutions"], stock)
        self.claim(
            p + ["concentration"],
            None,
            self.key,
            stocks.row_path(self.key, 0, 8),
            "add",
            "derived_batch_dose",
            reason,
            [],
        )
        self.comment_claim(p + ["concentration"], self.key, 0, "stock_strength_input", reason, [])
        node, old = self.clone("NaHCO3")
        node["concentration"] = {"value": "8", "unit": "PERCENT_W_V"}
        self.note(
            node,
            reason
            + " Concentration denotes this stock's strength, not the original direct-medium 1 g/L assertion.",
        )
        cp = self.append(p + ["composition"], node)
        self.claim(
            cp + ["concentration"],
            old + ["concentration"],
            self.key,
            stocks.row_path(self.key, 0, 8),
            "correct",
            "stock_strength",
            reason,
            cp,
        )
        self.comment_claim(cp + ["concentration"], self.key, 0, "stock_strength_input", reason, cp)
        for q, ep in [(p, []), (cp, cp)]:
            self.original_claim(q + ["concentration"], "8% (w/v) NaHCO3 solution", reason, ep)
        self.lineage_node(cp, old, self.key, 0, 8, "stock_strength")

    def fill(self, pointer, source, section):
        stock = runner.get_node(self.after, pointer)
        for ri, row in enumerate(self.rows(source, section)):
            name = row["component_name"]
            linked = LINKS[self.key].get((section, ri)) if source == self.key else None
            is_stock = (
                row.get("reference_media_id") or row.get("unit") == "ml" or name == "KOH solution"
            )
            if is_stock:
                stock.setdefault("solutions", [])
                parent = pointer + ["solutions"]
                if (
                    name == "KOH solution"
                    or self.key == "M1153"
                    and source == self.key
                    and section == 3
                    and ri == 0
                ):
                    self.leaf(parent, source, section, ri)
                else:
                    self.stock(parent, source, section, ri, linked)
            else:
                self.leaf(pointer + ["composition"], source, section, ri)

    def formulate(self):
        for si in range(MAIN[self.key]):
            for ri, row in enumerate(self.rows(self.key, si)):
                if self.key == "M1378" and (si, ri) == (0, 8):
                    self.bicarbonate()
                elif (
                    row.get("reference_media_id")
                    or row.get("unit") == "ml"
                    and row["component_name"] != "Distilled water"
                ):
                    self.stock(["solutions"], self.key, si, ri, LINKS[self.key].get((si, ri)))
                else:
                    self.leaf(["ingredients"], self.key, si, ri)
        self.after["preparation_steps"] = []
        for ci, comment in enumerate(self.data[self.key]["comments"]):
            if ci == 1 and self.key in {"M1106", "M1153"}:
                p = self.section_paths[3]
                runner.get_node(self.after, p)["preparation_notes"] = comment["comment"]
                self.comment_claim(
                    p + ["preparation_notes"],
                    self.key,
                    ci,
                    "stock_preparation",
                    "Iron-stock-only preparation and storage instructions.",
                    [],
                )
            elif (self.key == "M933" and ci == 1) or (self.key == "M1390" and ci == 2):
                self.note(self.after, "Post-inoculation instruction: " + comment["comment"])
                self.comment_claim(
                    ["notes"],
                    self.key,
                    ci,
                    "gas_context",
                    "Preserve the source gas/pressure instruction without inventing a dissolved gas concentration.",
                    [],
                )
            else:
                action = "AUTOCLAVE"
                if self.key == "M1124" and ci == 0:
                    action = "HEAT"
                elif self.key == "M1390" and ci == 1:
                    action = "ALIQUOT"
                elif self.key == "M1389" and ci == 1:
                    action = "ADJUST_PH"
                steps = self.after["preparation_steps"]
                steps.append(
                    {
                        "step_number": len(steps) + 1,
                        "action": action,
                        "description": comment["comment"],
                    }
                )
                self.comment_claim(
                    ["preparation_steps", len(steps) - 1, "description"],
                    self.key,
                    ci,
                    "preparation_scope",
                    "Receiving-medium preparation context, including separately staged additions; stock-only preparation is not applied to the medium.",
                    [],
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
                    "notes": f"source_type={'culture_collection_page' if key.startswith('JCM') else 'dataset'}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied. Evidence covers recipe quantities/preparation, not growth or chemical grounding.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restored source-specific nested stocks, batch/per-liter addition bases and explicit stock strengths. Preserved original annotations and history; unsupported final-medium mass concentrations are withdrawn with source batch amounts retained in notes. Gas placeholders and unverified chemical groundings remain unresolved.",
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
    for r in plan["records"]:
        lines = [
            "# Nested Trace-Stock Concentration Review",
            "",
            f"- Record: {r['path']}",
            f"- ID: {r['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {r['before_sha256']}",
            f"- Result SHA256: {r['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "All old quantity fields and new scoped quantities are accounted below. Batch masses remain in source-backed notes when final volume is unstated. Existing chemical mappings and gas placeholders are preserved, not recertified. M190/M401 vitamin compositions are referenced, not expanded or independently reviewed here. Unknown authors/year stay absent. Validation results are in ../validation.json; failed publication gates remain unresolved.",
            "",
            "| Ingredient/context | Old field | Current field | Old | New | Status | DOI/PURL | Exact snippet | Decision and locator |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in r["claims"]:
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
        (out / (r["key"] + ".md")).write_text("\n".join(lines) + "\n")


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
