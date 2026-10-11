#!/usr/bin/env python3
"""Restore inspected albumin preparations in M194/M213/M244/J252."""

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
from culturemech.validation.recipe_references import html_recipe_text

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-albumin-counterparts"
CONTEXT_SHA = "a4853a8d073e506bf37fb1952d47551a3b84a94f5429b687c33b13f1340cd7f8"
ACTION = "RESTORED_ALBUMIN_COUNTERPART_IDENTITIES_AND_STOCK_CONCENTRATIONS_WITH_EVIDENCE"
LB = {"M194": [7, 8, 9], "M213": [2, 3, 4], "M244": [10, 11, 12], "J252": [1, 2, 3]}
NUMBER = {"M194": "201", "M213": "220", "M244": "252", "J252": "252"}
ALBUMIN_ROW = {"M194": 7, "M213": 2, "M244": 10, "J252": 1}
DIRECT = {
    "M194": [1, 2, 3, 4, 5, 6, 7, 8, 10],
    "M213": [3, 4, 5, 6, 8, 9],
    "M244": [0, 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 14, 15],
    "J252": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14],
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
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        parsed[key] = html_recipe_text(raw)[0] if key.startswith("JCM") else json.loads(raw)
    runner.require(
        context["source_issues"] == {"JCM201": "source_unavailable: JCM returned no recipe"}
        and "Nothing found." in parsed["JCM201"],
        "Original availability drift",
    )
    for key, size in (("M194", 12), ("M213", 10), ("M244", 16)):
        data = parsed[key]
        runner.require(
            data["meta"]["gm"] == "http://togomedium.org/medium/" + key
            and data["meta"]["original_media_id"] == "JCM_M" + NUMBER[key]
            and data["meta"]["src_url"]
            == context["sources"]["JCM" + NUMBER[key]]["metadata"]["url"]
            and len(data["components"]) == 1
            and len(data["components"][0]["items"]) == size,
            "TOGO source identity/topology drift",
        )
    data = parsed["J252"]
    runner.require(
        data["status"] == 200
        and data["data"]["medium"]["id"] == "J252"
        and data["data"]["medium"]["source"] == "JCM"
        and data["data"]["medium"]["link"] == context["sources"]["JCM252"]["metadata"]["url"]
        and len(data["data"]["solutions"]) == 1
        and data["data"]["solutions"][0]["id"] == 3938
        and len(data["data"]["solutions"][0]["recipe"]) == 15
        and all(
            r["optional"] == 0 and not r.get("condition")
            for r in data["data"]["solutions"][0]["recipe"]
        ),
        "J252 source identity/topology drift",
    )
    return parsed


class Review(prior.Review):
    def __init__(self, before, key):
        self.context = frozen()
        self.spec = next(r for r in self.context["records"] if r["key"] == key)
        runner.require(
            before == runner.load_yaml(self.spec["before_text"])
            and before["id"] == self.spec["id"],
            "Unreviewed baseline",
        )
        runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
        runner.require(
            not any(before.get(k) for k in ("evidence", "references", "variants", "solutions")),
            "Existing provenance needs reconciliation",
        )
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.data = sources(self.context)
        self.claims, self.lineage, self.used, self.originals = [], [], [], {}
        # Supplier provenance disambiguates J252's genuine and false yeast nodes.
        for i, name in zip(LB[key], ("Tryptone", "Yeast extract", "Sodium chloride"), strict=True):
            node = before["ingredients"][i]
            runner.require(
                node["preferred_term"] == name
                and "LB Medium" in node["supplier_catalog"]["supplier_name"],
                "Product identity drift",
            )
        for i, node in enumerate(before["ingredients"]):
            if i not in LB[key]:
                name = node["preferred_term"]
                runner.require(name not in self.originals, "Ambiguous retained identity")
                self.originals[name] = ["ingredients", i]
        self.after["ingredients"], self.after["solutions"] = [], []

    def source_row(self, ri):
        return stocks.row_path(self.key, 0, ri)

    def original_amount(self, pointer, ri, ep):
        if self.key == "M194":
            return
        row = self.rows(self.key, 0)[ri]
        name = row.get("compound", row.get("component_name"))
        name = (
            name.replace("\u30fb", "\u00b7")
            .replace(" x ", "\u00b7")
            .replace(" H2O", "H2O")
            .replace("nH2O", "xH2O")
        )
        name = {"Yeast extract": "Yeast extract (BD-Difco)", "Na2-EDTA": "EDTA\u00b72Na"}.get(
            name, name
        )
        original = "JCM" + NUMBER[self.key]
        text = self.data[original]
        table = text[: text.index("Adjust pH" if self.key == "M213" else "Mix components")]
        matches = list(
            re.finditer(re.escape(name) + r" ([0-9]+(?:\.[0-9]+)?) (mg|g|ml|L)(?= |$)", table)
        )
        runner.require(len(matches) == 1, "Missing/ambiguous original row")
        match = matches[0]
        amount, unit = Decimal(str(row.get("amount", row.get("volume")))), row["unit"]
        if unit == "ml" and match.group(2) == "L":
            amount, unit = amount / 1000, "L"
        runner.require(
            amount == Decimal(match.group(1)) and unit == match.group(2),
            "Original/provider amount conflict",
        )
        self.corroborate(
            pointer,
            original,
            match.group(),
            "Original recipe corroborates this exact batch input and material. Water input does not establish final-medium volume.",
            ep,
        )

    def direct(self, ri):
        row = self.rows(self.key, 0)[ri]
        if row.get("component_name") == "N2":
            node, old = self.clone("N2")
            runner.require(row.get("volume") is None, "Gas amount drift")
            node.pop("concentration")
            reason = "Nitrogen is preparation-atmosphere context, not a quantified dissolved ingredient. Remove the unsupported VARIABLE placeholder; no fixed gas dose is supplied."
            self.note(node, reason)
            p = self.append(["ingredients"], node)
            self.claim(
                p + ["concentration"],
                old + ["concentration"],
                self.key,
                self.source_row(ri),
                "remove_unsupported",
                "unquantified_gas",
                reason,
                p,
            )
            self.lineage_node(p, old, self.key, 0, ri, "unquantified_gas")
            self.corroborate(
                p + ["notes"],
                "JCM252",
                "Bring to a boil for 5-10 sec and flush with N2.",
                reason,
                p,
            )
            return
        p = stocks.Review.leaf(self, ["ingredients"], self.key, 0, ri)
        self.original_amount(p + ["notes"], ri, p)

    def dose(self, ri, label=None, *, retained_descriptor=True):
        row = self.rows(self.key, 0)[ri]
        name = row.get("compound", row.get("component_name"))
        node, old = (
            self.clone(name)
            if retained_descriptor
            else ({"preferred_term": label}, self.originals.get(name))
        )
        amount, unit = row.get("amount", row.get("volume")), row["unit"]
        runner.require(unit in {"ml", "L"}, "Dose unit drift")
        value = shared.numeric(Decimal(str(amount)) / (1000 if unit == "ml" else 1))
        node.update(composition=[], concentration={"value": value, "unit": "L"})
        reason = f"Source batch dose: {amount} {unit} = {value} L per receiving batch, not g/L or a dose per final liter."
        self.note(node, reason)
        p = self.append(["solutions"], node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            self.key,
            self.source_row(ri),
            "correct" if old else "add",
            "batch_dose",
            reason,
            [],
        )
        self.lineage_node(p, old if retained_descriptor else None, self.key, 0, ri, "batch_dose")
        self.original_amount(p + ["concentration"], ri, [])
        return p

    def m194(self):
        p = self.dose(0, "7% gelatin solution", retained_descriptor=False)
        node, old = self.clone("gelatin")
        node.pop("concentration")
        reason = "Source label is 7% gelatin, with unspecified percentage basis and no stock preparation mass. The enclosing descriptor holds the single 200 ml batch dose; the row and comment are the same addition."
        self.note(node, reason)
        cp = self.append(p + ["composition"], node)
        self.claim(
            cp + ["notes"],
            None,
            self.key,
            self.source_row(0),
            "evidence_only",
            "unquantified_strength",
            reason,
            cp,
        )
        self.lineage_node(cp, old, self.key, 0, 0, "unquantified_strength")
        p = self.dose(9)
        reason = "CMRL 1066 (Gibco 330--1540) is a product input; its composition and stock strength are not supplied. Do not invent an expanded formulation."
        self.note(runner.get_node(self.after, p), reason)
        self.claim(
            p + ["notes"],
            None,
            self.key,
            self.source_row(9),
            "evidence_only",
            "product_context",
            reason,
            [],
        )
        node, old = self.clone("sterile rabbit serum")
        node.pop("concentration")
        node["composition"] = []
        reason = "Source specifies final 6% sterile rabbit serum without a percentage basis or fixed addition volume. Remove the unsupported VARIABLE placeholder; no 6% v/v strength or fixed dose is asserted. Serum is added after medium filtration."
        self.note(node, reason)
        p = self.append(["solutions"], node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"],
            self.key,
            self.source_row(11),
            "remove_unsupported",
            "unquantified_serum",
            reason,
            [],
        )
        self.lineage_node(p, old, self.key, 0, 11, "unquantified_serum")
        quote = "Add sterile rabbit serum to final concentration of 6%."
        node["preparation_notes"] = quote
        self.claim(
            p + ["preparation_notes"],
            None,
            self.key,
            ["comments", 0, "comment"],
            "add",
            "late_preparation",
            reason,
            [],
            snippet=quote,
        )
        self.note(
            self.after,
            "The original JCM201 endpoint returned no recipe in the pinned capture. This formulation is TOGO-provider-backed, not original-page corroborated.",
        )

    def m213(self):
        for ri, label in (
            (0, "Glucose"),
            (1, "Cysteine"),
            (2, "Bovine serum albumin, fraction V"),
            (7, "Hemin"),
        ):
            p = self.dose(ri)
            row = self.rows(self.key, 0)[ri]
            reason = f"Source preparation label: {row['component_name']}. Percentage basis is unspecified; no numeric stock strength, stock-batch mass or final-medium concentration is asserted. The enclosing descriptor holds the batch volume."
            cp = self.append(p + ["composition"], {"preferred_term": label, "notes": reason})
            self.claim(
                cp + ["notes"],
                None,
                self.key,
                self.source_row(ri),
                "add",
                "unquantified_strength",
                reason,
                cp,
            )
            self.lineage_node(cp, None, self.key, 0, ri, "unquantified_strength")
            self.original_amount(cp + ["notes"], ri, cp)
            node = runner.get_node(self.after, p)
            if ri != 7:
                quote = self.data[self.key]["comments"][1]["comment"]
                node["preparation_notes"] = quote
                self.claim(
                    p + ["preparation_notes"],
                    None,
                    self.key,
                    ["comments", 1, "comment"],
                    "add",
                    "separate_filtration",
                    "Filter these three named stocks separately and add aseptically; no pore size is supplied.",
                    [],
                    snippet=quote,
                )
                self.corroborate(
                    p + ["preparation_notes"],
                    "JCM220",
                    quote,
                    "Original separate filtration instruction.",
                    [],
                )
            else:
                reason = "Hemin-stock solvent is 0.05 N NaOH. No solvent dose or stock preparation volume is supplied; normality is not converted to molarity. The source does not assign the separate three-stock filtration instruction to hemin."
                node["solutions"] = [
                    {
                        "preferred_term": "NaOH solution (0.05 N)",
                        "notes": reason,
                        "composition": [{"preferred_term": "NaOH", "notes": reason}],
                    }
                ]
                for pointer, ep in (
                    (p + ["solutions", 0, "notes"], []),
                    (
                        p + ["solutions", 0, "composition", 0, "notes"],
                        p + ["solutions", 0, "composition", 0],
                    ),
                ):
                    self.claim(
                        pointer,
                        None,
                        self.key,
                        self.source_row(ri),
                        "add",
                        "stock_solvent",
                        reason,
                        ep,
                    )
                    self.original_amount(pointer, ri, ep)

    def prepared252(self):
        original = self.data["JCM252"]
        autoclave = original[
            original.index("Separately autoclave") : original.index("Filter-sterilize bovine")
        ].strip()
        filtered = original[
            original.index("Filter-sterilize bovine") : original.index("Before inoculation")
        ].strip()
        late = original[original.index("Before inoculation") : original.index("Copyright")].strip()
        rows = (13, 10, 4) if self.key == "M244" else (0, 1, 12)
        for ri, label, albumin in zip(
            rows,
            (
                "10% yeast extract solution",
                "10% (w/v) bovine serum albumin solution",
                "5% neutralized sodium sulfide nonahydrate solution",
            ),
            (False, True, False),
            strict=True,
        ):
            node = {
                "preferred_term": label,
                "composition": [],
                "preparation_notes": (filtered if albumin else autoclave) + " " + late,
            }
            reason = "Separate stock preparation added aseptically and anaerobically under N2 before inoculation. The source table mass is its contribution to the receiving batch, not a mass for preparing an unspecified stock volume."
            if not albumin:
                reason += " The stock percentage basis and fixed dose are unspecified."
            node["notes"] = reason
            p = self.append(["solutions"], node)
            self.claim(
                p + ["notes"],
                None,
                self.key,
                self.source_row(ri),
                "add",
                "stock_boundary",
                reason,
                [],
            )
            self.corroborate(
                p + ["preparation_notes"], "JCM252", filtered if albumin else autoclave, reason, []
            )
            self.corroborate(
                p + ["preparation_notes"],
                "JCM252",
                late,
                "Explicit order and anaerobic addition.",
                [],
            )
            cp = stocks.Review.leaf(self, p + ["composition"], self.key, 0, ri, prepared=True)
            self.original_amount(cp + ["notes"], ri, cp)
            if albumin:
                component = runner.get_node(self.after, cp)
                component["concentration"] = {"value": "10", "unit": "PERCENT_W_V"}
                reason = "Explicit albumin-stock strength is 10% (w/v) = 10 g per 100 ml = 100 g/L. This is not the receiving-medium concentration."
                self.note(component, reason)
                self.corroborate(cp + ["concentration"], "JCM252", filtered, reason, cp)
                row = self.rows(self.key, 0)[ri]
                runner.require(
                    row.get("amount", row.get("volume")) == 1
                    and row["unit"] == "g"
                    and "10% (w/v)" in filtered,
                    "Albumin calculation input drift",
                )
                node["concentration"] = {
                    "value": shared.numeric(Decimal("1") / Decimal("100")),
                    "unit": "L",
                }
                reason = "Derived receiving-batch dose: source contribution 1 g / explicit stock strength (10 g / 0.1 L = 100 g/L) = 0.01 L (10 ml). Both inputs describe this recipe's separately filtered albumin stock. No final-medium volume is needed or inferred; the dose is calculated, not directly printed in the source."
                self.note(node, reason)
                self.claim(
                    p + ["concentration"],
                    None,
                    self.key,
                    self.source_row(ri),
                    "add",
                    "derived_batch_dose",
                    reason,
                    [],
                )
                self.original_amount(p + ["concentration"], ri, [])
                self.corroborate(p + ["concentration"], "JCM252", filtered, reason, [])

    def preparation(self):
        if self.key in {"M244", "J252"}:
            source, sp = "JCM252", None
            text = self.data[source]
            starts = [
                "Mix components",
                "Bring to a boil",
                "Adjust pH",
                "After cooling",
                "Separately autoclave",
                "Filter-sterilize bovine",
                "Before inoculation",
                "Copyright",
            ]
            bounds = [text.index(s) for s in starts]
            runner.require(bounds == sorted(set(bounds)), "Preparation order drift")
            descriptions = [text[bounds[i] : bounds[i + 1]].strip() for i in range(7)]
            actions = ["MIX", "HEAT", "ADJUST_PH", "AUTOCLAVE", "AUTOCLAVE", "FILTER", "MIX"]
            ph, ph_quote = 7.6, "Adjust pH to 7.6 at 80-90C."
        elif self.key == "M194":
            source, sp = self.key, ["comments", 0, "comment"]
            descriptions = [
                "Mix all ingredients in a beaker with a stir bar.",
                "Adjust pH to 7.6.",
                "Add 200 ml of 7% gelatin.",
                "Filter--sterilize entire medium.",
                "Add sterile rabbit serum to final concentration of 6%.",
            ]
            runner.require(
                " ".join(descriptions) == self.data[self.key]["comments"][0]["comment"],
                "M194 preparation drift",
            )
            actions, ph, ph_quote = (
                ["MIX", "ADJUST_PH", "MIX", "FILTER", "MIX"],
                7.6,
                "Adjust pH to 7.6.",
            )
        else:
            source, sp = self.key, ["comments"]
            descriptions = [c["comment"] for c in self.data[self.key]["comments"]]
            actions, ph, ph_quote = ["ADJUST_PH", "FILTER"], 6.6, "Adjust pH to 6.6."
        self.after["preparation_steps"] = []
        for i, (action, description) in enumerate(zip(actions, descriptions, strict=True)):
            self.after["preparation_steps"].append(
                {"step_number": i + 1, "action": action, "description": description}
            )
            self.claim(
                ["preparation_steps", i, "description"],
                None,
                source,
                sp,
                "add",
                "preparation_scope",
                "Exact source sequence and preparation stage; FILTER does not assert an unspecified pore size.",
                [],
                snippet=description,
            )
        self.after["ph_value"] = ph
        self.claim(
            ["ph_value"],
            ["ph_value"] if "ph_value" in self.before else None,
            source,
            sp,
            "evidence_only" if "ph_value" in self.before else "add",
            "ph_scope",
            "Source preparation pH; retain its stated temperature context in the preparation step, not an assumed room-temperature measurement.",
            [],
            snippet=ph_quote,
        )

    def formulate(self):
        marker = "\n\nCommercial Product:"
        runner.require(marker in self.before["notes"], "Historical provenance drift")
        self.after["notes"] = self.before["notes"].replace(
            marker,
            "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product:",
            1,
        )
        reason = "The exact recipe specifies albumin, not LB broth. Remove only the three reviewed LB supplier nodes and restore albumin at its source-defined preparation stage. Genuine yeast extract and unrelated annotations are preserved."
        self.note(self.after, reason)
        for i in LB[self.key]:
            self.claim(
                ["notes"],
                ["ingredients", i, "concentration"],
                self.key,
                self.source_row(ALBUMIN_ROW[self.key]),
                "correct",
                "wrong_product_removed",
                reason,
                [],
            )
        for ri in DIRECT[self.key]:
            self.direct(ri)
        if self.key == "M194":
            self.m194()
        elif self.key == "M213":
            self.m213()
        else:
            self.prepared252()
        self.preparation()
        if self.key == "M244":
            runner.require(self.after.pop("high_metal") is True, "Flag baseline drift")
            reason = "Withdraw the unsupported high_metal classification, not replace it with false. Its schema definition requires total metal concentration >=1049.84 mM. Source quantities include milligram batch inputs, one liter of water, and later stocks; a final-volume denominator and all molecular-form conversions are not established. The former g/L fields cannot support this classification."
            self.note(self.after, reason)
            self.claim(
                ["high_metal"],
                ["high_metal"],
                self.key,
                self.source_row(5),
                "remove_unsupported",
                "unsupported_flag",
                reason,
                [],
            )
            self.original_amount(["high_metal"], 0, [])

    def finish(self, timestamp):
        for claim in self.claims:
            p = claim["pointer"]
            claim["new"] = copy.deepcopy(runner.get_node(self.after, p[:-1]).get(p[-1]))
        self.after["references"] = []
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            notes = f"source_type={'culture_collection_page' if key.startswith('JCM') else 'dataset'}; discovery_mode=existing_record_reference; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied. Batch inputs and stock strengths are scoped separately; chemical groundings and growth claims are not recertified."
            if self.key == "M194":
                missing = self.context["sources"]["JCM201"]["metadata"]
                notes += f" Original-source access gap: {missing['url']} returned 'Nothing found.'; accessed={missing['accessed_at']}; capture_sha256={missing['sha256']}. This is an access-status observation, not formulation evidence."
            title = (
                "Medium data"
                if key.startswith("JCM")
                else (
                    self.data[key]["meta"]["name"]
                    if key.startswith("M")
                    else self.data[key]["data"]["medium"]["name"]
                )
            )
            self.after["references"].append(
                {"reference": meta["url"], "title": title, "notes": notes}
            )
        event_notes = "Restore albumin and remove false LB constituents; correct mass/dose and stock/receiving-batch scopes. Retain exact source batch masses without assumed final volume. Unspecified percentage bases remain unknown. No growth claims or new chemical IDs are inferred."
        if self.key in {"M244", "J252"}:
            event_notes += (
                " JCM252 supports 10% w/v albumin stock and a calculated 10 ml batch dose."
            )
        if self.key == "M244":
            event_notes += " Withdraw the unsupported high_metal flag without setting it false."
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes=event_notes,
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
    out.mkdir(exist_ok=True)
    for item in plan["records"]:
        lines = [
            "# Albumin And Stock Concentration Review",
            "",
            f"- {'Follow-up target' if item['key'] == 'J252' else 'Record'}: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Every old quantity field and source row is accounted below. Source batch amounts are not assumed final concentrations. Unknown authors/year and percentage bases remain unknown. J252's historical canonical report is unchanged. See validation.json for actual terminal checks; report presence is not corpus completion.",
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
    plan, result = process(ROOT, args.plan, mode)
    if args.reports:
        reports(plan, mode != "preview")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
