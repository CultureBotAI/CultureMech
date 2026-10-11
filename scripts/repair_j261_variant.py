#!/usr/bin/env python3
"""Restore the source-defined JCM261 variant and its TOGO wrapper, with evidence."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_methanogen_stock_boundaries as shared
from bs4 import BeautifulSoup

from culturemech.curate.curation_event import record_curation_event

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-j261-variant"
CONTEXT = stocks.HERE / "next-j261-context.json"
CONTEXT_SHA = "da25a5f492f0fcc0bf1fdeca5f4cb0c80a261b7387c2c9acb83efdcc7b31b53c"
ACTION = "RESTORED_JCM261_VARIANT_FORMULATION_WITH_EVIDENCE"
PAIRS = {"J261": "J151", "M253": "M142"}
MODIFICATIONS = [
    "Set final yeast extract to 2.0 g/L, replacing the parent amount.",
    "Set final peptone to 2.0 g/L, replacing the parent amount.",
    "Add sodium thiosulfate pentahydrate at 1.0 g/L.",
    "Omit elemental sulfur and its preparation/addition steps.",
    "Adjust receiving-medium pH to 7.0 instead of 6.5.",
]


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
    for child, parent in PAIRS.items():
        for key, number in ((child, "261"), (parent, "151")):
            body = parsed[key]
            url = context["sources"]["JCM" + number]["metadata"]["url"]
            if key.startswith("J"):
                meta = body["data"]["medium"]
                runner.require(
                    body["status"] == 200
                    and meta["id"] == key
                    and meta["source"] == "JCM"
                    and meta["link"] == url,
                    "MediaDive identity drift",
                )
            else:
                runner.require(
                    body["meta"]["original_media_id"] == "JCM_M" + number
                    and body["meta"]["src_url"] == url,
                    "TOGO identity drift",
                )
    runner.require(
        [s["id"] for s in parsed["J151"]["data"]["solutions"]] == [3802, 3803, 3804]
        and [len(s["recipe"]) for s in parsed["J151"]["data"]["solutions"]] == [8, 12, 13]
        and [len(s["items"]) for s in parsed["M142"]["components"]] == [10, 12, 14]
        and len(parsed["M253"]["components"]) == 1
        and len(parsed["M253"]["components"][0]["items"]) == 10
        and parsed["J261"]["data"]["solutions"][0]["id"] == 3947
        and not parsed["J261"]["data"]["solutions"][0].get("recipe"),
        "Source graph drift",
    )
    runner.require(
        "Search for medium no. = [261]." in parsed["JCM261"]
        and "Search for medium no. = [151]." in parsed["JCM151"],
        "Original recipe identity drift",
    )
    for key in ("J261", "M253", "JCM261"):
        text = (
            parsed[key]
            if key.startswith("JCM")
            else (
                parsed[key]["data"]["solutions"][0]["steps"][0]["step"]
                if key == "J261"
                else parsed[key]["comments"][2]["comment"]
            )
        )
        runner.require(
            all(
                t in text
                for t in (
                    "2.0 g/L (final) yeast extract",
                    "2.0 g/L (final) peptone",
                    "omit sulfur",
                    "Adjust pH to 7.0.",
                )
            ),
            "Variant override drift",
        )
    return parsed


class Review(stocks.Review):
    def __init__(self, before, key):
        self.context = frozen()
        self.spec = next(r for r in self.context["records"] if r["key"] == key)
        runner.require(before == runner.load_yaml(self.spec["before_text"]), "Unreviewed baseline")
        runner.require(before["id"] == self.spec["id"], "Identity drift")
        runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
        self.data = sources(self.context)
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.claims, self.lineage, self.used = [], [], []
        self.originals = {}
        for field in ("ingredients", "solutions"):
            for i, node in enumerate(before.get(field, [])):
                runner.require(
                    node["preferred_term"] not in self.originals, "Ambiguous old identity"
                )
                self.originals[node["preferred_term"]] = [field, i]
        if key in PAIRS:
            runner.require(
                not before.get("evidence") and not before.get("references"),
                "Child provenance needs reconciliation",
            )
            self.after["ingredients"], self.after["solutions"] = [], []

    def clone(self, name, *, source=None):
        # Only J261 inherited flattened J151 nodes; never transfer parent annotations.
        allowed = {None, self.key, "J151"} if self.key == "J261" else {None, self.key}
        old = self.originals.get(name) if source in allowed else None
        return (
            copy.deepcopy(runner.get_node(self.before, old)) if old else {"preferred_term": name}
        ), old

    def variant_claim(self, pointer, old_pointer, status, kind, reason, evidence_pointer):
        child = (
            self.key if self.key in PAIRS else next(k for k, v in PAIRS.items() if v == self.key)
        )
        sp = (
            ["data", "solutions", 0, "steps", 0, "step"]
            if child == "J261"
            else ["comments", 2, "comment"]
        )
        self.claim(
            pointer,
            old_pointer,
            child,
            sp,
            status,
            kind,
            reason,
            evidence_pointer,
            snippet=runner.get_node(self.data[child], sp),
        )
        original = self.data["JCM261"]
        quote = original[
            original.index("Use Medium No. 151") : original.index("Adjust pH to 7.0.")
            + len("Adjust pH to 7.0.")
        ]
        self.claim(
            pointer,
            old_pointer,
            "JCM261",
            None,
            "evidence_only",
            kind,
            "Original JCM261 corroborates the explicit variant instruction. " + reason,
            evidence_pointer,
            snippet=quote,
        )

    def leaf(self, parent, source, si, ri, *, prepared=False):
        row = self.rows(source, si)[ri]
        name = row.get("compound", row.get("component_name"))
        old = self.clone(name, source=source)[1]
        if row.get("amount", row.get("volume")) is None and old is None:
            node = {
                "preferred_term": name,
                "notes": "Source names this preparation reagent without a fixed dose. No numeric concentration is asserted.",
            }
            p = self.append(parent, node)
            self.claim(
                p + ["notes"],
                None,
                source,
                stocks.row_path(source, si, ri),
                "add",
                "unquantified_titrant",
                node["notes"],
                p,
            )
            self.lineage.append(
                {
                    "pointer": p,
                    "old_pointer": None,
                    "source": source,
                    "source_pointer": stocks.row_path(source, si, ri),
                    "kind": "unquantified_titrant",
                }
            )
            return p
        p = super().leaf(parent, source, si, ri, prepared=prepared)
        if old is None and "concentration" not in runner.get_node(self.after, p):
            node = runner.get_node(self.after, p)
            node["notes"] = node["notes"].replace(
                "the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration",
                "no g/L concentration is inferred from an assumed one-liter final volume",
            )
            for c in self.claims:
                if c["pointer"] == p + ["concentration"]:
                    c["status"] = "not_quantified"
                    c["explanation"] = c["explanation"].replace(
                        "the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration",
                        "no g/L concentration is inferred from an assumed one-liter final volume",
                    )
            for e in node.get("evidence", []):
                e["explanation"] = e["explanation"].replace(
                    "the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration",
                    "no g/L concentration is inferred from an assumed one-liter final volume",
                )
        if source != self.key:
            self.variant_claim(
                p + ["notes"],
                None,
                "evidence_only",
                "inheritance",
                "This unchanged constituent belongs to the explicitly referenced base formulation, at its stated preparation stage, not an additive copy of the whole parent medium.",
                p,
            )
        return p

    def final_rate(self, name, value):
        node, old = self.clone(name)
        node["concentration"] = {"value": value, "unit": "G_PER_L"}
        reason = "Explicit final variant concentration; replaces the parent's amount, not added on top of it. No inferred final-volume arithmetic."
        self.note(node, reason)
        p = self.append(["ingredients"], node)
        self.variant_claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            (
                "correct"
                if old
                and node["concentration"] != runner.get_node(self.before, old).get("concentration")
                else "evidence_only" if old else "add"
            ),
            "final_rate",
            reason,
            p,
        )
        self.lineage.append(
            {
                "pointer": p,
                "old_pointer": old,
                "source": self.key,
                "source_pointer": None,
                "kind": "final_rate",
            }
        )

    def stages(self):
        jcm = self.key == "J261"
        base = PAIRS[self.key]
        for si, ri in ((1, 0 if jcm else 6), (2, 1 if jcm else 7)):
            source = base if jcm else self.key
            p = self.stock(["solutions"], source, 0, ri, definition=si if jcm else None)
            self.variant_claim(
                p + ["notes"],
                None,
                "evidence_only",
                "inheritance",
                "Retain the referenced base stock as its own preparation; its batch dose is not a final concentration.",
                [],
            )
            for index in range(len(self.rows(base, si))):
                self.leaf(p + ["composition"], base, si, index)
            if si == 2:
                sp = (
                    ["data", "solutions", 2, "steps", 0, "step"]
                    if jcm
                    else ["comments", 1, "comment"]
                )
                text = runner.get_node(self.data[base], sp)
                runner.get_node(self.after, p)["preparation_notes"] = text
                self.claim(
                    p + ["preparation_notes"],
                    None,
                    base,
                    sp,
                    "add",
                    "stock_preparation",
                    "Trace-stock-only preparation; its pH instructions do not reset the receiving-medium variant pH.",
                    [],
                    snippet=text,
                )
                if jcm:
                    kp = self.append(
                        p + ["composition"],
                        {
                            "preferred_term": "KOH solution",
                            "notes": "Source-explicit stock pH adjustment; no fixed dose.",
                        },
                    )
                    self.claim(
                        kp + ["notes"],
                        None,
                        base,
                        sp,
                        "add",
                        "unquantified_titrant",
                        "KOH is used only to adjust the trace-stock pH; no fixed quantity given.",
                        kp,
                        snippet=text,
                    )
        for ri in ((2, 7) if jcm else (0, 5, 8, 9)):
            self.leaf(["ingredients"], base if jcm else self.key, 0, ri)
        self.final_rate("Yeast extract" if jcm else "Yeast extract (BD-Difco)", "2")
        self.final_rate("Bacto peptone" if jcm else "Bacto peptone (BD-Difco)", "2")
        self.final_rate("Na2S2O3 x 5H2O" if jcm else "Na2S2O3\u30fb5H2O", "1")
        source = base if jcm else self.key
        sp = ["data", "solutions", 0, "steps", 0, "step"] if jcm else ["comments", 0, "comment"]
        prep = runner.get_node(self.data[source], sp)
        excerpt = prep[prep.index("Neutralize") : prep.index("Aseptically")].strip()
        p = self.append(
            ["solutions"],
            {
                "preferred_term": "Sodium sulfide separately prepared solution",
                "composition": [],
                "preparation_notes": excerpt,
                "notes": "The source's 5% label has no specified percentage basis or stock addition volume. Neither is inferred. Composition notes describe the receiving-batch contribution, not an unspecified stock-batch recipe.",
            },
        )
        self.claim(
            p + ["preparation_notes"],
            None,
            source,
            sp,
            "add",
            "separate_preparation",
            runner.get_node(self.after, p)["notes"],
            [],
            snippet=excerpt,
        )
        self.leaf(p + ["composition"], source, 0, 6 if jcm else 1, prepared=True)
        if jcm:
            for name in ("H2SO4", "N2"):
                ip = self.append(
                    ["ingredients"],
                    {
                        "preferred_term": name,
                        "notes": "Inherited preparation reagent; no fixed dose specified. Receiving-medium pH is overridden to 7.0.",
                    },
                )
                self.claim(
                    ip + ["notes"],
                    None,
                    source,
                    sp,
                    "add",
                    "unquantified_reagent",
                    "Retain the inherited titrant/atmosphere without a numeric amount; parent pH 6.5 is overridden, not inherited.",
                    ip,
                    snippet=prep[: prep.index("Steam sulfur")].strip(),
                )
            old = self.originals["Sulfur"]
            self.variant_claim(
                ["variant_modifications"],
                old + ["concentration"],
                "remove_omitted",
                "sulfur_omission",
                "Remove the copied elemental-sulfur node, including its quantity, from active composition. Full old node is archived in this curation event, not erased from history.",
                [],
            )

    def procedures(self):
        source = "J151" if self.key == "J261" else "M253"
        sp = (
            ["data", "solutions", 0, "steps", 0, "step"]
            if source == "J151"
            else ["comments", 0, "comment"]
        )
        parent_text = runner.get_node(self.data[source], sp)
        variant = (
            self.data["J261"]["data"]["solutions"][0]["steps"][0]["step"]
            if self.key == "J261"
            else self.data["M253"]["comments"][2]["comment"]
        )
        first = copy.deepcopy(self.before.get("preparation_steps", [{"step_number": 1}])[0])
        first.update(action="ADJUST_PH", description=variant)
        self.after["preparation_steps"] = [
            first,
            {
                "step_number": 2,
                "action": "FILTER",
                "description": "Apply the base-medium filtration under N2, with sulfur omitted and sodium sulfide prepared separately. The variant overrides receiving-medium pH to 7.0.",
            },
            {
                "step_number": 3,
                "action": "MIX",
                "description": "Before inoculation, add the separately prepared sterile sodium sulfide solution. Apply the variant's pH 7.0 override. No sulfur preparation or addition is performed.",
            },
        ]
        self.claim(
            ["preparation_steps"],
            ["preparation_steps"] if self.before.get("preparation_steps") else None,
            source,
            sp,
            "correct" if self.before.get("preparation_steps") else "add",
            "preparation_scope",
            "Effective procedure is a curator synthesis of the inherited preparation and explicit variant overrides, not a verbatim quotation. Parent sulfur steps and receiving-medium pH 6.5 are superseded.",
            [],
            snippet=parent_text,
        )
        self.variant_claim(
            ["preparation_steps"],
            None,
            "evidence_only",
            "preparation_override",
            "Explicit sulfur omission and receiving-medium pH override control the effective preparation; inherited conflicting text is retained only in cited context.",
            [],
        )
        self.after["ph_value"] = 7.0
        self.variant_claim(
            ["ph_value"],
            ["ph_value"] if "ph_value" in self.before else None,
            "evidence_only" if "ph_value" in self.before else "add",
            "ph",
            "Explicit variant final pH, not inherited pH 6.5.",
            [],
        )

    def relationship(self):
        child = (
            self.key if self.key in PAIRS else next(k for k, v in PAIRS.items() if v == self.key)
        )
        target = PAIRS[child] if self.key == child else child
        spec = next(r for r in self.context["records"] if r["key"] == target)
        record = runner.load_yaml(spec["before_text"])
        if self.key == child:
            pointer = ["parent_media"]
            self.after.setdefault("parent_media", {})
        else:
            links = self.after.setdefault("variant_children", [])
            hits = [i for i, link in enumerate(links) if link.get("id") == record["id"]]
            runner.require(len(hits) <= 1, "Duplicate child relation")
            if not hits:
                links.append({})
            pointer = ["variant_children", hits[0] if hits else len(links) - 1]
        link = runner.get_node(self.after, pointer)
        link.update(
            id=record["id"], name=record["name"], path=spec["path"], relationship="DERIVED_FROM"
        )
        self.note(
            link,
            "Source-defined composite variant: final yeast extract/peptone overrides, thiosulfate addition, sulfur omission and pH 7.0. DERIVED_FROM covers the combined modifications; this is not a SOURCE_DUPLICATE. Earlier duplicate-candidate notes are superseded.",
        )
        old = (
            pointer
            if self.key == child
            and self.before.get("parent_media")
            or self.key != child
            and self.before.get("variant_children")
            else None
        )
        claim_pointer = pointer if self.key == child else ["variant_children"]
        self.variant_claim(
            claim_pointer,
            claim_pointer if old else None,
            "correct" if old else "add",
            "variant_link",
            "Correct exact tracked parent/child identity and classify the explicit combined variant; preserve the parent's formulation.",
            pointer,
        )
        if self.key == child:
            self.after["variant_relationship"] = "DERIVED_FROM"
            self.after["variant_modifications"] = MODIFICATIONS.copy()
            self.variant_claim(
                ["variant_relationship"],
                ["variant_relationship"] if "variant_relationship" in self.before else None,
                "correct" if "variant_relationship" in self.before else "add",
                "variant_link",
                "Composite formulation variant, not an exact duplicate.",
                [],
            )
            self.variant_claim(
                ["variant_modifications"],
                ["variant_modifications"] if "variant_modifications" in self.before else None,
                "correct" if "variant_modifications" in self.before else "add",
                "variant_modifications",
                "The final concentrations replace parent quantities and sulfur is excluded; no additive parent copy is retained.",
                [],
            )

    def finish(self, timestamp):
        for claim in self.claims:
            path = claim["pointer"]
            claim["new"] = copy.deepcopy(runner.get_node(self.after, path[:-1]).get(path[-1]))
        refs = self.after.setdefault("references", [])
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            if any(r["reference"] == meta["url"] for r in refs):
                continue
            title = (
                "Medium data"
                if key.startswith("JCM")
                else (
                    self.data[key]["data"]["medium"]["name"]
                    if key.startswith("J")
                    else self.data[key]["meta"]["name"]
                )
            )
            refs.append(
                {
                    "reference": meta["url"],
                    "title": title,
                    "notes": f"source_type={'culture_collection_page' if key.startswith('JCM') else 'dataset'}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied; access/copyright year is not publication year. Formulation evidence only, not growth evidence.",
                }
            )
        changes = [
            {
                k: c[k]
                for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")
            }
            for c in self.claims
            if c["status"] not in {"evidence_only", "unsupported"}
        ]
        if self.key == "J261":
            changes.append(
                {
                    "omitted_node": copy.deepcopy(self.before["ingredients"][3]),
                    "reason": "Source explicitly says omit sulfur; archived here, not active composition.",
                    "reference": self.context["sources"]["JCM261"]["metadata"]["url"],
                    "snippet": "and omit sulfur.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"]["JCM261"]["metadata"]["url"],
            notes="Source-defined variant overrides and reciprocal links restored. Parent formulations and prior history preserved. Batch amounts and stock composition are not final-medium concentrations. Unknown percentage basis/dose remains unresolved; chemical annotations preserved, not recertified.",
            changes=json.dumps(changes, ensure_ascii=True),
        )
        runner.require(
            not runner.errors(self.after, "MediaRecipe"),
            "Proposed schema failure: " + str(runner.errors(self.after, "MediaRecipe")),
        )
        return self.after, self.claims, self.lineage


def build(before, key, timestamp):
    review = Review(before, key)
    review.relationship()
    if key in PAIRS:
        review.stages()
        review.procedures()
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
        marker = "Record" if item["key"] == "M253" else "Follow-up target"
        lines = [
            "# JCM261 Variant Review",
            "",
            f"- {marker}: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Child formulation: final rates override the parent, sulfur is omitted, stock and batch boundaries remain explicit. Parent records: relationship-only follow-up; all prior ingredient claims are unchanged, not newly recertified. Missing final volumes, percentage basis and stock dose remain unknown. Prior annotations/history are retained; the removed sulfur node is archived in the event. Authors/year are unknown. Validation and unresolved gates are recorded separately in validation.json.",
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
