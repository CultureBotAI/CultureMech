#!/usr/bin/env python3
"""Restore four source-defined basal-makeup and later supplementation stages."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-basal-makeup"
CONTEXT_SHA = "e2970bd6a1ebf9d9ba9c900aa1666cf7e8c15aac8c2bb2739c40bc4506492198"
ACTION = "RESTORED_BASAL_MAKEUP_AND_SUPPLEMENT_STAGES_WITH_EVIDENCE"
SIZES = {
    "M809": [10, 2, 3],
    "M823": [14, 3],
    "M853": [14, 3],
    "M975": [13, 4],
    "M142": [10, 12, 14],
    "M190": [17, 11, 11],
}
NUMBERS = {"M809": "779", "M823": "791", "M853": "818", "M975": "929", "M142": "151", "M190": "197"}
MAKEUP = "Add components to distilled water and bring volume to 1.0 L."
BASE_LABEL = "Basal preparation at the 1 L makeup stage"
VARIANT = "Use JCM Medium No. 791 with 5.0 g/L MgSO4\u00b77H2O instead of CaCl2\u00b72H2O. Adjust pH to 7.5."
MODIFICATIONS = [
    "Replace basal calcium chloride dihydrate with the specified 5.0 g/L magnesium sulfate heptahydrate.",
    "Adjust pH to 7.5 instead of the parent's 7.0.",
]


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
    for key, sizes in SIZES.items():
        body = parsed[key]
        number = NUMBERS[key]
        runner.require(
            body["meta"]["gm"] == "http://togomedium.org/medium/" + key
            and body["meta"]["original_media_id"] == "JCM_M" + number
            and body["meta"]["src_url"] == context["sources"]["JCM" + number]["metadata"]["url"]
            and [len(s["items"]) for s in body["components"]] == sizes
            and f"Search for medium no. = [{number}]." in parsed["JCM" + number],
            "Source identity/topology drift",
        )
    for key in NUMBERS.keys() - {"M142", "M190"}:
        original = "JCM791" if key == "M853" else "JCM" + NUMBERS[key]
        runner.require(
            MAKEUP in parsed[key]["comments"][0]["comment"]
            and literal_match(MAKEUP, parsed[original]),
            "Makeup stage drift",
        )
    runner.require(literal_match(VARIANT, parsed["JCM818"]), "Variant source drift")
    return parsed


class Review(prior.Review):
    def __init__(self, before, key):
        context = frozen()
        runner.require(key in {"M809", "M823", "M853", "M975"}, "Unreviewed record")
        shared.Review.__init__(self, before, key, context=context, parsed=sources(context))
        self.originals = {}
        for field in ("ingredients", "solutions"):
            for i, node in enumerate(before[field]):
                runner.require(node["preferred_term"] not in self.originals, "Ambiguous baseline")
                self.originals[node["preferred_term"]] = [field, i]
        runner.require(
            not any(
                before.get(k)
                for k in (
                    "parent_media",
                    "variant_children",
                    "variant_relationship",
                    "variant_modifications",
                    "ph_value",
                    "preparation_steps",
                )
            ),
            "Existing curation needs reconciliation",
        )
        self.after["ingredients"], self.after["solutions"] = [], []
        self.gas_paths = {}

    def base_support(self, p, ep, reason):
        original = "JCM791" if self.key == "M853" else "JCM" + NUMBERS[self.key]
        self.comment_claim(p, self.key, 0, "makeup_stage", reason, ep)
        self.corroborate(p, original, MAKEUP, reason, ep)

    def basal_leaf(self, ri):
        row = self.rows(self.key, 0)[ri]
        node, old = self.clone(row["component_name"])
        name, amount, unit = row["component_name"], row.get("volume"), row.get("unit")
        kind = "basal_rate"
        if name == "Distilled water":
            node.pop("concentration")
            kind = "makeup_water"
            reason = "Water is the makeup reagent for the explicitly stated 1.0 L basal stage, not a fixed 1 L water input or a final supplemented-medium volume. Its actual addition amount is unspecified."
            if self.key == "M809":
                reason += " The historical duplicate-summing note combined basal makeup and reducing-stock water; that interpretation is superseded."
            if self.key == "M975":
                reason += " The original table also lists 1.0 L water; this conflicts with treating that value as a fixed input to the separate 1.0 L makeup instruction. Both statements are preserved as source context; no numeric water dose is asserted."
        elif amount is None:
            node.pop("concentration")
            kind = "unquantified_input"
            reason = (
                "Source atmosphere context, not a fixed gas input or dissolved concentration."
                if name in {"N2", "Nitrogen gas", "Carbon dioxide gas"}
                else "Source pH-adjustment reagent with no fixed dose."
            ) + " Removed the unsupported VARIABLE placeholder."
        else:
            runner.require(unit in {"g", "mg", "g/L"}, "Basal mass unit drift")
            node["concentration"] = {
                "value": shared.numeric(amount),
                "unit": "MG_PER_L" if unit == "mg" else "G_PER_L",
            }
            reason = (
                (
                    f"Source-explicit variant rate: {amount} g/L in the inherited basal formulation."
                    if unit == "g/L"
                    else f"Source basal batch amount: {amount} {unit}; explicitly made up to 1.0 L at this stage. Calculation: {amount} {unit} / 1.0 L = {amount} {unit}/L."
                )
                + " This concentration applies at basal makeup, before subsequent pH adjustment, heating and supplements; it is not a final supplemented-medium rate."
            )
        self.note(node, reason)
        p = self.append(["solutions", 0, "composition"], node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"],
            self.key,
            stocks.row_path(self.key, 0, ri),
            "correct" if "concentration" in node else "remove_unsupported",
            kind,
            reason,
            p,
        )
        self.lineage_node(p, old, self.key, 0, ri, kind)
        self.base_support(p + ["notes"], p, reason)
        if self.key == "M853" and ri == 1:
            self.corroborate(
                p + ["concentration"],
                "JCM818",
                VARIANT,
                "Explicit salt substitution replaces, not supplements, the parent's calcium-chloride component.",
                p,
            )
        return p

    def titrant_stock(self, ri):
        row = self.rows(self.key, 0)[ri]
        runner.require(
            self.key == "M975"
            and row["component_name"] == "KOH"
            and row["conc_value"] == 10
            and row["conc_unit"] == "M"
            and row.get("volume") is None,
            "KOH reagent drift",
        )
        reason = "Use the source-explicit 10 M KOH reagent to adjust basal pH to 8.3. The addition volume is unspecified; 10 M describes the reagent, not the basal or final medium."
        descriptor = {"preferred_term": "KOH reagent (10 M)", "composition": [], "notes": reason}
        p = self.append(["solutions", 0, "solutions"], descriptor)
        self.claim(
            p + ["notes"],
            None,
            self.key,
            stocks.row_path(self.key, 0, ri),
            "add",
            "titrant_stock",
            reason,
            [],
        )
        self.lineage_node(p, None, self.key, 0, ri, "titrant_stock")
        node, old = self.clone("KOH")
        node["concentration"] = {"value": "10", "unit": "MOLAR"}
        self.note(node, reason)
        q = self.append(p + ["composition"], node)
        self.claim(
            q + ["concentration"],
            old + ["concentration"],
            self.key,
            stocks.row_path(self.key, 0, ri),
            "correct",
            "stock_strength",
            reason,
            q,
        )
        self.lineage_node(q, old, self.key, 0, ri, "stock_strength")
        self.corroborate(
            q + ["concentration"], "JCM929", "Adjust pH to 8.3 with 10 M KOH.", reason, q
        )

    def stock(self, parent, si, ri):
        row = self.rows(self.key, si)[ri]
        node, old = self.clone(row["component_name"])
        runner.require(row["unit"] == "ml", "Stock dose unit drift")
        per_liter = si == 1 and self.key != "M809"
        value = Decimal(str(row["volume"])) / (1 if per_liter else 1000)
        node["concentration"] = {
            "value": shared.numeric(value),
            "unit": "ML_PER_L" if per_liter else "L",
        }
        reason = (
            f"Source-explicit post-autoclave addition: {row['volume']} ml per liter of receiving basal medium; not a final-mixture volume measurement."
            if per_liter
            else f"Source liquid input: {row['volume']} ml = {shared.numeric(value)} L per {'basal makeup' if si == 0 else 'receiving'} batch, not grams per liter."
        )
        if row.get("conc_unit") == "%":
            reason += f" Stock label is {row['conc_value']}%; its percentage basis is unspecified, so no numeric strength or final concentration is inferred."
        self.note(node, reason)
        p = self.append(parent, node)
        kind = "per_liter_dose" if per_liter else "batch_dose"
        self.claim(
            p + ["concentration"],
            old + ["concentration"],
            self.key,
            stocks.row_path(self.key, si, ri),
            "correct",
            kind,
            reason,
            [],
        )
        self.lineage_node(p, old, self.key, si, ri, kind)
        self.comment_claim(p + ["concentration"], self.key, 0, "dose_stage", reason, [])
        if per_liter:
            original = "JCM791" if self.key in {"M823", "M853"} else "JCM929"
            quote = (
                "After cooling, add per liter the following solutions from anaerobic stocks"
                if original == "JCM791"
                else "into the medium (per liter):"
            )
            self.corroborate(p + ["concentration"], original, quote, reason, [])
        ref = row.get("reference_media_id")
        if ref in {"M142", "M190"}:
            section = 2 if ref == "M142" else 1
            for i, ingredient in enumerate(self.rows(ref, section)):
                if ingredient["component_name"] == "KOH solution":
                    node.setdefault("solutions", [])
                    self.leaf(p + ["solutions"], ref, section, i)
                else:
                    self.leaf(p + ["composition"], ref, section, i)
            if ref == "M142":
                node["preparation_notes"] = self.data[ref]["comments"][1]["comment"]
                self.comment_claim(
                    p + ["preparation_notes"],
                    ref,
                    1,
                    "stock_preparation",
                    "This preparation belongs only to the nested trace-mineral stock.",
                    [],
                )
                self.corroborate(
                    p + ["preparation_notes"],
                    "JCM151",
                    "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution.",
                    "Original trace-mineral stock preparation, not basal pH.",
                    [],
                )
            else:
                self.corroborate(
                    p + ["notes"],
                    "JCM197",
                    "Trace vitamins:",
                    "Inherit only the vitamin table, not the whole referenced medium.",
                    [],
                )
        elif ref == "M809":
            for i in range(3):
                self.leaf(p + ["composition"], self.key, 2, i)
            node["preparation_notes"] = self.data[self.key]["comments"][3]["comment"]
            self.comment_claim(
                p + ["preparation_notes"],
                self.key,
                3,
                "stock_preparation",
                "Reducing-stock-only preparation and filtration.",
                [],
            )
        elif row["component_name"] == "1 M Glucose solution":
            ingredient = {
                "preferred_term": "Glucose",
                "concentration": {"value": "1", "unit": "MOLAR"},
                "notes": "Explicit 1 M stock strength, not a receiving-medium concentration. No final dilution is calculated.",
            }
            q = self.append(p + ["composition"], ingredient)
            self.claim(
                q + ["concentration"],
                None,
                self.key,
                stocks.row_path(self.key, si, ri),
                "add",
                "stock_strength",
                ingredient["notes"],
                q,
            )
            self.lineage_node(q, None, self.key, si, ri, "stock_strength")
        return p

    def clone(self, name, *, source=None):
        # M809's merged water annotation belongs to basal makeup, not the separate reducer.
        if self.key == "M809" and getattr(self, "in_reducer", False) and name == "Distilled water":
            return {"preferred_term": name}, None
        return super().clone(name, source=source)

    def leaf(self, parent, source, si, ri, *, prepared=False):
        self.in_reducer = source == "M809" and si == 2
        try:
            return super().leaf(parent, source, si, ri, prepared=prepared)
        finally:
            self.in_reducer = False

    def relationship(self):
        if self.key not in {"M823", "M853"}:
            return
        target = "M823" if self.key == "M853" else "M853"
        spec = next(r for r in self.context["records"] if r["key"] == target)
        record = runner.load_yaml(spec["before_text"])
        link = {
            "id": record["id"],
            "name": record["name"],
            "path": spec["path"],
            "relationship": "DERIVED_FROM",
            "notes": "Source-defined salt-substitution and pH variant; not an exact duplicate or an additional copy of the parent medium.",
        }
        if self.key == "M853":
            self.after["parent_media"] = link
            p = ["parent_media"]
            self.after["variant_relationship"] = "DERIVED_FROM"
            self.after["variant_modifications"] = MODIFICATIONS.copy()
            self.after["ph_value"] = 7.5
            for key in ("variant_relationship", "variant_modifications", "ph_value"):
                self.corroborate(
                    [key],
                    "JCM818",
                    VARIANT,
                    "Explicit child overrides; the parent formulation remains separate.",
                    [],
                )
        else:
            self.after["variant_children"] = [link]
            p = ["variant_children", 0]
        self.corroborate(
            p + ["notes"],
            "JCM818",
            VARIANT,
            "Source relationship resolved to the exact tracked sibling ID and path.",
            p,
        )

    def formulate(self):
        base = {
            "preferred_term": BASE_LABEL,
            "composition": [],
            "solutions": [],
            "notes": "This is the explicitly made-up basal preparation before later supplements. Composition rates apply at the 1.0 L makeup stage only. No fixed dose of the subsequently titrated/heated basal preparation or final supplemented-medium volume is asserted.",
        }
        self.after["solutions"].append(base)
        self.base_support(["solutions", 0, "notes"], [], base["notes"])
        for ri, row in enumerate(self.rows(self.key, 0)):
            if row.get("reference_media_id"):
                self.stock(["solutions", 0, "solutions"], 0, ri)
            elif self.key == "M975" and row["component_name"] == "KOH":
                self.titrant_stock(ri)
            else:
                self.basal_leaf(ri)
        for ri in range(len(self.rows(self.key, 1))):
            self.stock(["solutions"], 1, ri)
        text = self.data[self.key]["comments"][0]["comment"]
        if self.key == "M853":
            runner.require(text.count("Adjust pH to 7.0 with KOH") == 1, "Inherited pH drift")
            text = text.replace("Adjust pH to 7.0 with KOH", "Adjust pH to 7.5 with KOH")
        self.after["preparation_steps"] = [
            {"step_number": 1, "action": "AUTOCLAVE", "description": text}
        ]
        self.comment_claim(
            ["preparation_steps", 0, "description"],
            self.key,
            0,
            "preparation_scope",
            "Keep basal makeup and later supplements distinct. For M853 only, the explicit child pH 7.5 replaces inherited pH 7.0 in the effective instructions; the original inherited text remains in this quotation.",
            [],
        )
        if self.key == "M853":
            self.corroborate(
                ["preparation_steps", 0, "description"],
                "JCM818",
                VARIANT,
                "The child's pH override applies at the inherited adjustment stage, not as an extra adjustment after following the conflicting parent pH.",
                [],
            )
        if self.key == "M809":
            self.after["preparation_steps"].append(
                {
                    "step_number": 2,
                    "action": "ADJUST_PH",
                    "description": self.data[self.key]["comments"][1]["comment"],
                }
            )
            self.comment_claim(
                ["preparation_steps", 1, "description"],
                self.key,
                1,
                "preparation_scope",
                "Optional post-supplement pH readjustment, not a fixed titrant dose.",
                [],
            )
        self.relationship()

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
                    "notes": f"source_type={'culture_collection_page' if source.startswith('JCM') else 'dataset'}; discovery_mode={'existing_record_reference' if source in {self.key, 'JCM' + NUMBERS[self.key]} else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied. Recipe amounts and preparation only; existing chemical groundings are not recertified.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restored explicit basal-makeup and later supplementation boundaries, scoped ingredient quantities and original preparation. Preserved chemical annotations and prior history; no final supplemented-medium volume or unspecified percentage basis is inferred. Source-defined M823/M853 variant links preserve the salt substitution and pH override.",
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
            "# Basal Makeup And Supplement Concentration Review",
            "",
            f"- Record: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Rates inside the basal preparation apply only at its explicit makeup stage. Later additions and nested stocks have separate quantities. Final supplemented volume and unspecified percentage bases are unresolved; no chemical grounding or growth claim is inferred. See ../validation.json for terminal gate results.",
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
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    parser.add_argument("--reports", action="store_true")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--apply", action="store_true")
    group.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.plan, mode)
    if args.reports:
        reports(plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
