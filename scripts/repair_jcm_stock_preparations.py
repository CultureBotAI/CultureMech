#!/usr/bin/env python3
"""Guarded, source-specific stock/preparation repair for J151/J187/J197 and TOGO peers."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from decimal import Decimal
from pathlib import Path

import repair_methanogen_stock_boundaries as shared
from bs4 import BeautifulSoup
from review_medium_concentration_evidence import json_excerpt

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-jcm-stock-preparations"
CONTEXT = shared.HERE / "next-stock-source-context.json"
CONTEXT_SHA = "291cb565a506c5d89690780c758275f68b42dc1895fb629bd5875ec3bbb45752"
ACTION = "RESTORED_JCM_STOCK_PREPARATION_BOUNDARIES_WITH_EVIDENCE"
PAIRS = {"J151": "M142", "J187": "M180", "J197": "M190"}


def frozen():
    raw = CONTEXT.read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    return json.loads(raw)


def sources(context):
    parsed = {}
    for key, source in context["sources"].items():
        meta, raw = source["metadata"], source["raw"]
        url = (
            "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=" + key[3:]
            if key.startswith("JCM")
            else (
                "https://mediadive.dsmz.de/rest/medium/" + key
                if key.startswith("J")
                else "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=" + key
            )
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
    graphs = {
        "J151": ([3802, 3803, 3804], [8, 12, 13]),
        "J187": ([3845, 3846, 3847, 3861], [16, 3, 8, 11]),
        "J197": ([3860, 3861, 3862], [15, 11, 10]),
    }
    sizes = {"M142": [10, 12, 14], "M180": [19, 3, 8], "M190": [17, 11, 11]}
    for j, m in PAIRS.items():
        body = parsed[j]
        meta, stocks = body["data"]["medium"], body["data"]["solutions"]
        url = context["sources"]["JCM" + j[1:]]["metadata"]["url"]
        runner.require(
            body["status"] == 200
            and meta["id"] == j
            and meta["source"] == "JCM"
            and meta["link"] == url
            and [s["id"] for s in stocks] == graphs[j][0]
            and [len(s["recipe"]) for s in stocks] == graphs[j][1]
            and all(
                r.get("optional") == 0 and not r.get("condition")
                for s in stocks
                for r in s["recipe"]
            ),
            "Source graph drift",
        )
        runner.require(
            parsed[m]["meta"]["original_media_id"] == "JCM_M" + j[1:]
            and parsed[m]["meta"]["src_url"] == url
            and [len(s["items"]) for s in parsed[m]["components"]] == sizes[m]
            and f"Search for medium no. = [{j[1:]}]." in parsed["JCM" + j[1:]],
            "TOGO/source identity drift",
        )
    return parsed


def row_path(key, section, row):
    return (
        ["data", "solutions", section, "recipe", row]
        if key.startswith("J")
        else ["components", section, "items", row]
    )


class Review(shared.Review):
    def __init__(self, before, key):
        context = frozen()
        super().__init__(before, key, context=context, parsed=sources(context))
        self.originals = {}
        for field in ("ingredients", "solutions"):
            for i, node in enumerate(before.get(field, [])):
                name = node["preferred_term"]
                runner.require(name not in self.originals, "Ambiguous old identity")
                self.originals[name] = [field, i]
        self.after["ingredients"], self.after["solutions"] = [], []
        self.stock_paths = {}

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
        if snippet is None and source.startswith("M") and source_pointer[:1] == ["components"]:
            excerpt = json_excerpt(self.context["sources"][source]["raw"], source_pointer)
            # Retain the exact amount/strength prefix, not unrelated ontology annotations.
            stops = [excerpt.find('"' + k + '"') for k in ("gmo_id", "roles", "reference_media_id")]
            ends = [i for i in stops if i > 0]
            snippet = excerpt[: min(ends)].rstrip().rstrip(",") if ends else excerpt
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

    def rows(self, key, section):
        return (
            self.data[key]["data"]["solutions"][section]["recipe"]
            if key.startswith("J")
            else self.data[key]["components"][section]["items"]
        )

    def append(self, parent, node):
        target = runner.get_node(self.after, parent)
        path = parent + [len(target)]
        target.append(node)
        return path

    def clone(self, name, *, source=None):
        old = self.originals.get(name) if source in {None, self.key} else None
        return (
            copy.deepcopy(runner.get_node(self.before, old)) if old else {"preferred_term": name}
        ), old

    def leaf(self, parent, source, si, ri, *, prepared=False):
        sp = row_path(source, si, ri)
        row = runner.get_node(self.data[source], sp)
        name = row.get("compound", row.get("component_name"))
        node, old = self.clone(name, source=source)
        amount, unit = row.get("amount", row.get("volume")), row.get("unit")
        kind = "batch_mass"
        if amount is None:
            runner.require(old is not None, "Unreviewed unquantified identity")
            if name in {"N2", "Nitrogen gas", "Carbon dioxide gas"}:
                p = self.append(parent, node)
                self.claim(
                    p + ["concentration"],
                    old + ["concentration"],
                    source,
                    sp,
                    "unsupported",
                    "gas",
                    "Unchanged legacy VARIABLE gas placeholder; no fixed amount verified.",
                )
                return p
            node.pop("concentration", None)
            kind = "unquantified_titrant"
            strength = (
                f" Source reagent strength: {row['conc_value']} {row['conc_unit']}."
                if "conc_value" in row
                else ""
            )
            reason = (
                "pH-adjustment reagent; no fixed dose is specified."
                + strength
                + " Normality is not converted to molarity."
            )
        elif name == "Distilled water":
            runner.require(unit in {"L", "ml"}, "Water unit drift")
            value = Decimal(str(amount)) / (1000 if unit == "ml" else 1)
            node["concentration"] = {"value": shared.numeric(value), "unit": "L"}
            kind = "water"
            reason = f"Source water batch input: {amount} {unit} = {shared.numeric(value)} L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record."
        elif name in {"HCl", "25% HCl (7.7 M)"}:
            runner.require(
                (row.get("attribute") == "7.7 M, 25%" or name == "25% HCl (7.7 M)")
                and unit == "ml",
                "HCl strength drift",
            )
            node["concentration"] = {"value": "7.7", "unit": "MOLAR"}
            kind = "stock_strength"
            reason = "Explicit HCl reagent strength 7.7 M, not a final-medium concentration. The 25% basis is unspecified; the enclosing stock holds the 10 ml batch dose."
        elif source.startswith("J") and si > 0:
            runner.require(unit in {"g", "mg"} and row.get("g_l") is not None, "Stock rate drift")
            node["concentration"] = {"value": shared.numeric(row["g_l"]), "unit": "G_PER_L"}
            kind = "stock_rate"
            reason = f"Source stock batch input: {amount} {unit}. Retain provider-declared stock g_l={row['g_l']} only, not a final-medium concentration or an independently verified final stock volume. Prior duplicate-merge notes describe the superseded flattened record."
        else:
            runner.require(unit in {"g", "mg"}, "Mass row drift")
            node.pop("concentration", None)
            reason = f"Source batch input: {amount} {unit}. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
            if prepared:
                reason += " This is the contribution specified for the receiving medium batch, not the mass for preparing an unspecified volume of stock."
            if row.get("attribute"):
                reason += " Source qualifier: " + row["attribute"] + "."
        self.note(node, reason)
        p = self.append(parent, node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            source,
            sp,
            "remove_unsupported" if "concentration" not in node else "correct" if old else "add",
            kind,
            reason,
            [] if parent[-1] == "solutions" else p,
        )
        self.lineage.append(
            {"pointer": p, "old_pointer": old, "source": source, "source_pointer": sp, "kind": kind}
        )
        return p

    def stock(self, parent, source, si, ri, definition=None):
        sp = row_path(source, si, ri)
        row = runner.get_node(self.data[source], sp)
        name = row.get("solution", row.get("component_name", row.get("compound")))
        is_acid = si > 0
        node, old = (
            ({"preferred_term": "HCl reagent (7.7 M)"}, None) if is_acid else self.clone(name)
        )
        # A legacy ingredient can be a stock descriptor; its annotations survive the move.
        node["composition"] = []
        amount, unit = row.get("amount", row.get("volume")), row["unit"]
        runner.require(unit in {"ml", "L"}, "Stock volume drift")
        value = Decimal(str(amount)) / (1000 if unit == "ml" else 1)
        node["concentration"] = {"value": shared.numeric(value), "unit": "L"}
        if definition is not None:
            d = self.data[source]["data"]["solutions"][definition]
            node["term"] = {"id": "mediadive.solution:" + str(d["id"]), "label": d["name"]}
        reason = f"Source stock addition: {amount} {unit} = {shared.numeric(value)} L per receiving batch, not grams per liter or a dose per final liter."
        self.note(node, reason)
        p = self.append(parent, node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            source,
            sp,
            "correct" if old else "add",
            "batch_dose",
            reason,
            [],
        )
        self.lineage.append(
            {
                "pointer": p,
                "old_pointer": old,
                "source": source,
                "source_pointer": sp,
                "kind": "batch_dose",
            }
        )
        return p

    def preparation(self):
        return (
            ["data", "solutions", 0, "steps", 0, "step"]
            if self.key.startswith("J")
            else ["comments", 0, "comment"]
        )

    def prepared(self, ri):
        row = self.rows(self.key, 0)[ri]
        name = row.get("compound", row.get("component_name"))
        prep = runner.get_node(self.data[self.key], self.preparation())
        node = {
            "preferred_term": name + " separately prepared solution",
            "composition": [],
            "preparation_notes": "Receiving-medium instructions (context only; not a stock-batch recipe): "
            + prep,
            "notes": "The source specifies a separate percentage-labelled preparation but does not establish percentage basis or its addition volume. No numeric stock strength or dose is asserted. Composition notes record the receiving-batch contribution only.",
        }
        p = self.append(["solutions"], node)
        self.claim(
            p + ["preparation_notes"],
            None,
            self.key,
            self.preparation(),
            "add",
            "separate_preparation",
            node["notes"],
            [],
        )
        self.leaf(p + ["composition"], self.key, 0, ri, prepared=True)

    def fill(self, p, source, si):
        for ri, row in enumerate(self.rows(source, si)):
            name = row.get("compound", row.get("component_name"))
            if name in {"HCl", "25% HCl (7.7 M)"}:
                runner.get_node(self.after, p)["solutions"] = []
                acid = self.stock(p + ["solutions"], source, si, ri)
                ap = self.leaf(acid + ["composition"], source, si, ri)
                self.claim(
                    ap + ["concentration"],
                    None,
                    "JCM187",
                    None,
                    "evidence_only",
                    "stock_strength_support",
                    "Original FeCl2 table corroborates the reagent strength and dose.",
                    ap,
                    snippet="25% HCl (7.7 M) 10.0 ml",
                )
            elif self.originals.get(name, [None])[0] == "solutions":
                runner.get_node(self.after, p).setdefault("solutions", [])
                self.leaf(p + ["solutions"], source, si, ri)
            else:
                self.leaf(p + ["composition"], source, si, ri)

    def stages(self):
        main = self.rows(self.key, 0)
        if self.key.startswith("J"):
            ss = self.data[self.key]["data"]["solutions"]
            links = [
                (i, self.key, next(j for j, s in enumerate(ss) if s["id"] == r["solution_id"]))
                for i, r in enumerate(main)
                if r.get("solution_id")
            ]
            separately = {"J151": {6}, "J187": {6, 10, 11, 13}, "J197": {10, 11, 12}}[self.key]
        else:
            links = {
                "M142": [(6, "M142", 1), (7, "M142", 2)],
                "M180": [(13, "M180", 1), (14, "M180", 2), (15, "M190", 1)],
                "M190": [(13, "M190", 2), (14, "M190", 1)],
            }[self.key]
            separately = {"M142": {1}, "M180": {7, 9, 11, 12}, "M190": {6, 7, 11}}[self.key]
        for ri, source, si in links:
            p = self.stock(
                ["solutions"], self.key, 0, ri, definition=si if self.key.startswith("J") else None
            )
            self.stock_paths[si] = p
            self.fill(p, source, si)
        for ri in range(len(main)):
            if ri in {r for r, _, _ in links}:
                continue
            if ri in separately:
                self.prepared(ri)
            else:
                self.leaf(["ingredients"], self.key, 0, ri)

    def procedures(self):
        sp = self.preparation()
        prep = runner.get_node(self.data[self.key], sp)
        action = "FILTER" if self.key in {"J151", "M142"} else "AUTOCLAVE"
        old = self.before.get("preparation_steps", [])
        first = copy.deepcopy(old[0]) if old else {"step_number": 1}
        first.update(action=action, description=prep)
        self.after["preparation_steps"] = [first]
        self.claim(
            ["preparation_steps"],
            ["preparation_steps"] if old else None,
            self.key,
            sp,
            "correct" if old else "add",
            "preparation_scope",
            "Restore the main-medium procedure and keep stock-only pH instructions out of the root sequence. FILTER denotes the explicit filtration; no pore size is inferred.",
            [],
        )
        if self.key in {"J151", "J197", "M142", "M190"}:
            trace = self.stock_paths[2]
            tsp = (
                ["data", "solutions", 2, "steps", 0, "step"]
                if self.key.startswith("J")
                else ["comments", 1, "comment"]
            )
            text = runner.get_node(self.data[self.key], tsp)
            runner.get_node(self.after, trace)["preparation_notes"] = text
            self.claim(
                trace + ["preparation_notes"],
                ["preparation_steps", 1, "description"] if old else None,
                self.key,
                tsp,
                "correct" if old else "add",
                "stock_preparation",
                "Trace-stock-only pH procedure, not receiving-medium pH.",
                [],
            )
            if self.key.startswith("J"):
                self.titrant(trace + ["composition"], "KOH solution", tsp, text)
        if self.key in {"J151", "J187"}:
            self.titrant(["ingredients"], "H2SO4", sp, prep)
        if self.key in {"J187", "M180"}:
            self.after.pop("ph_value", None)
            self.after["ph_range"] = {"min": 6.2, "max": 6.4}
            self.claim(
                ["ph_range"],
                ["ph_value"] if "ph_value" in self.before else None,
                self.key,
                sp,
                "correct" if "ph_value" in self.before else "add",
                "ph",
                "The preparation specifies pH 6.2-6.4; a scalar midpoint is not the source's range.",
                [],
            )
        else:
            self.after["ph_value"] = 6.5 if self.key in {"J151", "M142"} else 6.8
            self.claim(
                ["ph_value"],
                ["ph_value"] if "ph_value" in self.before else None,
                self.key,
                sp,
                "evidence_only" if self.key == "J151" else "correct",
                "ph",
                "Final-medium pH from the preparation; stock pH 7.0 is not the medium pH. MediaDive J197 metadata pH 7 disagrees with its main preparation and is not selected.",
                [],
            )
        if self.key in {"J197", "M190"}:
            p = next(
                lineage["pointer"]
                for lineage in self.lineage
                if lineage["source_pointer"]
                == row_path(self.key, 0, 11 if self.key == "J197" else 6)
            )
            reason = "Unresolved source identity discrepancy: the original JCM197 table spells NaS2, while its preparation spells Na2S. MediaDive normalizes the table to Na2S; TOGO retains NaS2. The existing label/grounding is preserved, not recertified, and no numeric sulfide concentration is asserted."
            self.note(runner.get_node(self.after, p), reason)
            self.claim(
                p + ["notes"],
                None,
                "JCM197",
                None,
                "evidence_only",
                "identity_conflict",
                reason,
                p,
                snippet="NaS2\u00b79H2O 0.5 g",
            )
            self.claim(
                p + ["notes"],
                None,
                self.key,
                sp,
                "evidence_only",
                "identity_conflict",
                "The preparation uses the different Na2S spelling; the discrepancy remains unresolved.",
                p,
            )

    def titrant(self, parent, name, sp, text):
        node = {
            "preferred_term": name,
            "notes": "Source-explicit pH adjustment with no fixed dose. Strength, when stated as 1 N, is retained in preparation text; no molarity is inferred.",
        }
        p = self.append(parent, node)
        self.claim(
            p + ["notes"], None, self.key, sp, "add", "unquantified_titrant", node["notes"], p
        )


def build(before, key, timestamp):
    review = Review(before, key)
    review.stages()
    review.procedures()
    return review.finish(
        timestamp,
        action=ACTION,
        change_suffix="; preparation stages and source-specific pH are supported separately; percentage bases and sulfide spelling disagreement remain unresolved.",
    )


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
        marker = "Follow-up target" if item["key"].startswith("J") else "Record"
        lines = [
            "# Stock Preparation Review",
            "",
            f"- {marker}: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "All old quantity slots and new assertions are accounted below. Unquantified gas placeholders remain unsupported. Provider-declared stock rates are not independent final-volume measurements. Missing percentage basis/dose and normality remain in notes, not guessed values. Existing chemical annotations and unrelated flags are preserved, not recertified. J197/M190 sulfide spelling conflict remains unresolved. Authors/year are unknown. See validation.json for terminal checks.",
            "",
            "| Ingredient | Old field | New field | Old | New | Status | DOI/PURL | Exact snippet | Decision/locator |",
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
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    parser.add_argument("--reports", action="store_true")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    HERE.mkdir(exist_ok=True)
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.plan, mode)
    if args.reports:
        reports(plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
