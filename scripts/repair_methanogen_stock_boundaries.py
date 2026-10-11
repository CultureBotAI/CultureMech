#!/usr/bin/env python3
"""Guarded source-backed repair of J985, J265 and TOGO M257 stock boundaries."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner
from bs4 import BeautifulSoup
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-methanogen-boundaries"
CONTEXT_SHA = "4f83dadbef9fe726b997d4291bdc2ce2e0f0558a611421ec33748f4e822f9078"
ACTION = "RESTORED_METHANOGEN_STOCK_BOUNDARIES_AND_DOSE_BASES_WITH_EVIDENCE"


def frozen():
    raw = (HERE / "inspected-context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    return json.loads(raw)


def sources(context):
    parsed = {}
    for key, s in context["sources"].items():
        m, raw = s["metadata"], s["raw"]
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
            m["url"] == m["response_url"] == url
            and m["http_status"] == 200
            and runner.sha(raw.encode(m["encoding"])) == m["sha256"],
            "Capture drift",
        )
        datetime.datetime.fromisoformat(m["accessed_at"])
        parsed[key] = (
            " ".join(BeautifulSoup(raw, "html.parser").get_text().split())
            if key.startswith("JCM")
            else json.loads(raw)
        )
    for key, ids, sizes in [
        ("J985", [5015, 3861, 3846, 3847, 4172], [15, 11, 3, 8, 4]),
        ("J265", [3951, 3952, 3861, 3804], [18, 4, 11, 13]),
    ]:
        body = parsed[key]
        medium = body["data"]["medium"]
        ss = body["data"]["solutions"]
        runner.require(
            body["status"] == 200
            and medium["id"] == key
            and medium["source"] == "JCM"
            and medium["link"] == context["sources"]["JCM" + key[1:]]["metadata"]["url"]
            and [s["id"] for s in ss] == ids
            and [len(s["recipe"]) for s in ss] == sizes,
            "Source graph drift",
        )
        runner.require(
            all(r.get("optional") == 0 and not r.get("condition") for s in ss for r in s["recipe"]),
            "Conditional formulation",
        )
    for key, number in [("M257", "265"), ("M1038", "985")]:
        meta = parsed[key]["meta"]
        runner.require(
            meta["original_media_id"] == "JCM_M" + number
            and meta["src_url"] == context["sources"]["JCM" + number]["metadata"]["url"],
            "TOGO identity drift",
        )
    runner.require(
        [(s["paragraph_index"], len(s["items"])) for s in parsed["M257"]["components"]]
        == [(1, 19), (3, 2), (5, 4)],
        "TOGO topology drift",
    )
    runner.require(
        "add per liter the following solutions" in parsed["M257"]["comments"][0]["comment"]
        and "add per liter the following solutions" in parsed["JCM265"],
        "Reducer basis drift",
    )
    runner.require(
        "Finally, add per liter" in parsed["J985"]["data"]["solutions"][0]["steps"][1]["step"]
        and parsed["J985"]["data"]["solutions"][0]["recipe"][12]["attribute"] == "*, 30%"
        and parsed["M1038"]["components"][1]["items"][1]["conc_value"] == 3
        and "Nothing found." in parsed["JCM985"],
        "J985 scope/conflict drift",
    )
    runner.require("25% HCl (7.7 M) 10.0 ml" in parsed["JCM187"], "HCl strength drift")
    runner.require(
        "265 METHANOGENIUM MEDIUM" in parsed["JCM265"]
        and "151 PYROCOCCUS MEDIUM" in parsed["JCM151"]
        and "197" in parsed["JCM197"],
        "Original recipe identity drift",
    )
    return parsed


def numeric(value):
    return format(Decimal(str(value)).normalize(), "f")


class Review:
    def __init__(self, before, key, *, context=None, parsed=None):
        self.context = frozen() if context is None else context
        self.spec = next(r for r in self.context["records"] if r["key"] == key)
        runner.require(
            before == runner.load_yaml(self.spec["before_text"])
            and before["id"] == self.spec["id"],
            "Unreviewed baseline",
        )
        runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
        runner.require(
            not any(before.get(k) for k in ("evidence", "references", "variants")),
            "Existing provenance needs reconciliation",
        )
        self.data = sources(self.context) if parsed is None else parsed
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.claims, self.lineage, self.used = [], [], []
        self.old_indices = {n["preferred_term"]: i for i, n in enumerate(before["ingredients"])}
        runner.require(
            len(self.old_indices) == len(before["ingredients"]),
            "Duplicate labels need explicit mapping",
        )

    def note(self, node, text):
        previous = node.get("notes", "")
        node["notes"] = previous + "\n\n" + text if previous else text

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
        raw = self.context["sources"][source]["raw"]
        meta = self.context["sources"][source]["metadata"]
        snippet = snippet if snippet is not None else json_excerpt(raw, source_pointer)
        text = self.data[source] if source.startswith("JCM") else raw
        runner.require(snippet and snippet in text, "Nonliteral source excerpt")
        field = runner.field_name(pointer)
        parent = runner.get_node(self.after, pointer[:-1])
        label = parent.get("preferred_term", "Recipe preparation/context")
        old = (
            runner.get_node(self.before, old_pointer[:-1]).get(old_pointer[-1])
            if old_pointer
            else None
        )
        new = runner.get_node(self.after, pointer[:-1]).get(pointer[-1])
        explanation = f"{field}: {reason} No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator={runner.field_name(source_pointer) if source_pointer else 'original recipe text'}; accessed={meta['accessed_at']}; capture SHA256={meta['sha256']}."
        c = {
            "pointer": pointer,
            "old_pointer": old_pointer,
            "field": field,
            "ingredient": label,
            "old_field": runner.field_name(old_pointer) if old_pointer else None,
            "old": copy.deepcopy(old),
            "new": copy.deepcopy(new),
            "status": status,
            "kind": kind,
            "source": source,
            "source_pointer": source_pointer,
            "reference": meta["url"],
            "snippet": snippet,
            "explanation": explanation,
            "evidence_pointer": evidence_pointer,
        }
        self.claims.append(c)
        if evidence_pointer is not None:
            if source not in self.used:
                self.used.append(source)
            entries = runner.get_node(self.after, evidence_pointer).setdefault("evidence", [])
            existing = [e for e in entries if e["reference"] == meta["url"]]
            if existing:
                runner.require(len(existing) == 1, "Evidence collision")
                existing[0]["explanation"] += (
                    "\n\nAdditional exact excerpt: " + snippet + "\n" + explanation
                )
            else:
                entries.append(
                    {
                        "reference": meta["url"],
                        "supports": "SUPPORT",
                        "snippet": snippet,
                        "explanation": explanation,
                    }
                )

    def component(self, parent, row, source_pointer, kind, old_index=None, source=None):
        source = source or self.key
        old_pointer = ["ingredients", old_index] if old_index is not None else None
        name = row.get("compound", row.get("component_name"))
        node = (
            copy.deepcopy(self.before["ingredients"][old_index])
            if old_index is not None
            else {"preferred_term": name}
        )
        runner.require(node["preferred_term"] == name, "Ingredient identity drift")
        amount = row.get("amount", row.get("volume"))
        unit = row.get("unit")
        if kind == "batch_mass":
            runner.require(unit in {"g", "mg"}, "Nonmass source row")
            node.pop("concentration", None)
            reason = f"Source batch input: {amount} {unit}. The former g/L assertion is withdrawn because final preparation volume is not independently established. Evidence supports this batch-amount note, not a calculated concentration."
            if row.get("attribute"):
                reason += " Source material qualifier: " + row["attribute"] + "."
        elif kind == "stock_rate":
            runner.require(row.get("g_l") is not None, "No provider stock rate")
            node["concentration"] = {"value": numeric(row["g_l"]), "unit": "G_PER_L"}
            volume = self.data[source]["data"]["solutions"][source_pointer[2]]["volume"]
            reason = f"Source stock input: {amount} {unit}. Retain only the provider-declared stock g_l={row['g_l']} (source volume field={volume} ml), not a receiving-medium concentration or independently measured final stock volume. This restores the preparation boundary; any prior merged-duplicate note describes the superseded flattened record."
        elif kind == "stock_strength":
            runner.require(row["attribute"] == "7.7 M, 25%", "Acid strength drift")
            node["concentration"] = {"value": "7.7", "unit": "MOLAR"}
            reason = "Rebase HCl to the explicit 7.7 M reagent strength, not its provider-derived 2.5 g/L in the FeCl2 stock. The 25% label has unspecified basis; the batch dose is stored on the enclosing HCl solution."
        elif kind == "liquid_reagent":
            runner.require(unit == "ml" and "%" in row["attribute"], "Liquid-stock row drift")
            node.pop("concentration", None)
            reason = f"Source reagent label: {row['attribute']}. The former {amount} g/L encodes a liquid addition as mass concentration and is withdrawn. Stock percentage basis is unspecified; the supported volume dose is on the enclosing solution."
        elif kind == "water":
            runner.require(unit == "ml", "Water input unit drift")
            node["concentration"] = {"value": numeric(Decimal(str(amount)) / 1000), "unit": "L"}
            reason = f"Water batch input: {amount} ml / 1000 ml per L = {node['concentration']['value']} L, not a measured final volume."
        else:
            raise ValueError(kind)
        self.note(node, reason)
        target = runner.get_node(self.after, parent)
        pointer = parent + [len(target)]
        target.append(node)
        status = (
            "remove_unsupported"
            if kind in {"batch_mass", "liquid_reagent"}
            else "correct" if old_pointer else "add"
        )
        self.claim(
            pointer + ["concentration"],
            old_pointer + ["concentration"] if old_pointer else None,
            source,
            source_pointer,
            status,
            kind,
            reason,
            pointer,
        )
        self.lineage.append(
            {
                "pointer": pointer,
                "old_pointer": old_pointer,
                "source": source,
                "source_pointer": source_pointer,
                "kind": kind,
            }
        )
        return pointer

    def descriptor(
        self,
        parent,
        row,
        source_pointer,
        *,
        old_index=None,
        per_liter=False,
        name=None,
        definition=None,
        step_pointer=None,
    ):
        node = (
            copy.deepcopy(self.before["solutions"][old_index])
            if old_index is not None
            else {
                "preferred_term": name
                or row.get("solution")
                or row.get("component_name")
                or row["compound"] + " stock",
                "composition": [],
            }
        )
        old_pointer = ["solutions", old_index, "concentration"] if old_index is not None else None
        amount, unit = row.get("amount", row.get("volume")), row["unit"]
        runner.require(unit in {"ml", "L"}, "Stock addition unit drift")
        if per_liter:
            runner.require(
                unit == "ml" and step_pointer is not None, "Missing per-liter dose context"
            )
            node["concentration"] = {"value": numeric(amount), "unit": "ML_PER_L"}
            reason = f"The preparation explicitly prescribes {amount} ml per liter at this stage, not {amount} g/L or an absolute batch dose."
        else:
            value = Decimal(str(amount)) / 1000 if unit == "ml" else Decimal(str(amount))
            node["concentration"] = {"value": numeric(value), "unit": "L"}
            reason = f"Source batch stock input: {amount} {unit} = {numeric(value)} L, not a dose per final liter."
        if definition:
            node["term"] = {
                "id": "mediadive.solution:" + str(definition["id"]),
                "label": definition["name"],
            }
        self.note(
            node,
            reason
            + " Stock composition, where given, belongs to this preparation and is not a direct receiving-medium ingredient list.",
        )
        target = runner.get_node(self.after, parent)
        pointer = parent + [len(target)]
        target.append(node)
        self.claim(
            pointer + ["concentration"],
            old_pointer,
            self.key,
            source_pointer,
            "correct" if old_pointer else "add",
            "per_liter_dose" if per_liter else "batch_dose",
            reason,
            [],
        )
        if step_pointer:
            self.claim(
                pointer + ["concentration"],
                old_pointer,
                self.key,
                step_pointer,
                "evidence_only",
                "dose_scope",
                "Preparation context establishing the batch/per-liter and sterilization stage for the separately quoted dose.",
                [],
            )
        return pointer

    def media_dive(self):
        ss = self.data[self.key]["data"]["solutions"]
        self.after["ingredients"], self.after["solutions"] = [], []
        rows = ss[0]["recipe"]
        for i, row in enumerate(rows):
            if row.get("compound") and row["unit"] in {"g", "mg"}:
                self.component(
                    ["ingredients"],
                    row,
                    ["data", "solutions", 0, "recipe", i],
                    "batch_mass",
                    self.old_indices[row["compound"]],
                )
            elif row.get("compound") == "Distilled water":
                self.component(["ingredients"], row, ["data", "solutions", 0, "recipe", i], "water")
        for i, row in enumerate(rows):
            sp = ["data", "solutions", 0, "recipe", i]
            if row.get("solution_id"):
                si, definition = next(
                    (j, s) for j, s in enumerate(ss) if s["id"] == row["solution_id"]
                )
                pointer = self.descriptor(
                    ["solutions"],
                    row,
                    sp,
                    definition=definition,
                    step_pointer=(
                        ["data", "solutions", 0, "steps", 0] if self.key == "J985" else None
                    ),
                )
                self.fill_stock(pointer, si)
            elif row.get("compound") != "Distilled water" and row["unit"] == "ml":
                per_liter = self.key == "J265" or row["compound_id"] == 54
                step = 0 if self.key == "J265" or not per_liter else 1
                pointer = self.descriptor(
                    ["solutions"],
                    row,
                    sp,
                    per_liter=per_liter,
                    step_pointer=["data", "solutions", 0, "steps", step],
                )
                cp = self.component(
                    pointer + ["composition"],
                    row,
                    sp,
                    "liquid_reagent",
                    self.old_indices[row["compound"]],
                )
                if self.key == "J985" and row["compound_id"] == 383:
                    reason = "Unresolved source disagreement: MediaDive labels this reagent 30%, while TOGO M1038 labels it 3%. Both lack percentage basis; neither is selected as a numeric strength and the original JCM985 page returns Nothing found. This is not evidence that the two versions are identical."
                    self.note(runner.get_node(self.after, cp), reason)
                    self.claim(
                        cp + ["notes"],
                        None,
                        "M1038",
                        ["components", 1, "items", 1],
                        "evidence_only",
                        "conflict",
                        reason,
                        cp,
                    )
        if self.key == "J985":
            self.after["preparation_steps"][1]["action"] = "ALIQUOT"
            self.claim(
                ["preparation_steps", 1, "action"],
                ["preparation_steps", 1, "action"],
                self.key,
                ["data", "solutions", 0, "steps", 1],
                "correct",
                "preparation_scope",
                "This step distributes medium into vessels and adds the per-liter sulfide stock; its legacy AUTOCLAVE action was over-scoped.",
                [],
            )
        else:
            old_step = self.after["preparation_steps"].pop()
            trace = self.after["solutions"][0]["solutions"][0]
            runner.require(
                old_step["description"] == ss[3]["steps"][0]["step"], "Stock preparation drift"
            )
            trace["preparation_notes"] = old_step["description"]
            self.claim(
                ["solutions", 0, "solutions", 0, "preparation_notes"],
                ["preparation_steps", 2, "description"],
                self.key,
                ["data", "solutions", 3, "steps", 0],
                "correct",
                "preparation_scope",
                "Move the trace-mineral pH adjustment to its nested stock; pH 7.0 is not a final-medium pH change.",
                [],
            )
            koh = {
                "preferred_term": "KOH solution",
                "notes": "Add to adjust trace-mineral preparation pH; the source gives no fixed amount or stock strength.",
            }
            trace["composition"].append(koh)
            kp = ["solutions", 0, "solutions", 0, "composition", len(trace["composition"]) - 1]
            self.claim(
                kp + ["notes"],
                None,
                self.key,
                ["data", "solutions", 3, "steps", 0],
                "add",
                "unquantified_reagent",
                "Explicit stock-only pH-adjustment reagent, not a guessed quantity or a direct-medium addition. No new chemical identifier is assigned.",
                kp,
            )

    def fill_stock(self, pointer, si):
        ss = self.data[self.key]["data"]["solutions"]
        definition = ss[si]
        for ri, row in enumerate(definition["recipe"]):
            sp = ["data", "solutions", si, "recipe", ri]
            node = runner.get_node(self.after, pointer)
            if row.get("solution_id"):
                child_si, child_def = next(
                    (j, s) for j, s in enumerate(ss) if s["id"] == row["solution_id"]
                )
                node.setdefault("solutions", [])
                child = self.descriptor(pointer + ["solutions"], row, sp, definition=child_def)
                self.fill_stock(child, child_si)
            elif row["compound"] == "Distilled water":
                self.component(pointer + ["composition"], row, sp, "water")
            elif row["compound"] == "HCl":
                node.setdefault("solutions", [])
                child = self.descriptor(pointer + ["solutions"], row, sp, name="HCl stock (7.7 M)")
                cp = self.component(
                    child + ["composition"], row, sp, "stock_strength", self.old_indices["HCl"]
                )
                self.claim(
                    cp + ["concentration"],
                    ["ingredients", self.old_indices["HCl"], "concentration"],
                    "JCM187",
                    None,
                    "evidence_only",
                    "stock_strength_support",
                    "Original FeCl2 stock table corroborates the explicitly stated HCl reagent strength and batch dose, not a final-medium concentration.",
                    cp,
                    snippet="25% HCl (7.7 M) 10.0 ml",
                )
            else:
                self.component(
                    pointer + ["composition"],
                    row,
                    sp,
                    "stock_rate",
                    self.old_indices[row["compound"]],
                )

    def togo(self):
        body = self.data[self.key]
        self.after["ingredients"], self.after["solutions"] = [], []
        for old_index, old in enumerate(self.before["ingredients"][:17]):
            ri, row = next(
                (i, r)
                for i, r in enumerate(body["components"][0]["items"])
                if r["component_name"] == old["preferred_term"]
            )
            sp = ["components", 0, "items", ri]
            if row.get("volume") is None:
                self.after["ingredients"].append(copy.deepcopy(old))
                self.claim(
                    ["ingredients", len(self.after["ingredients"]) - 1, "concentration"],
                    ["ingredients", old_index, "concentration"],
                    self.key,
                    sp,
                    "unsupported",
                    "gas",
                    "Legacy VARIABLE is not a measured gas amount; unchanged.",
                )
            else:
                self.component(
                    ["ingredients"], row, sp, "water" if ri == 0 else "batch_mass", old_index
                )
        for old_index, section, ri in [(0, 0, 14), (1, 0, 15), (2, 1, 0), (3, 1, 1)]:
            row = body["components"][section]["items"][ri]
            runner.require(
                self.before["solutions"][old_index]["preferred_term"] == row["component_name"],
                "Stock identity drift",
            )
            p = self.descriptor(
                ["solutions"],
                row,
                ["components", section, "items", ri],
                old_index=old_index,
                per_liter=section == 1,
                step_pointer=["comments", 0] if section == 1 else None,
            )
            if section == 1:
                reason = "Source 5% reagent label has unspecified percentage basis. The asserted numeric value is its per-liter addition volume only, not its mass concentration or an inferred stock strength."
                self.note(runner.get_node(self.after, p), reason)
                self.claim(
                    p + ["notes"],
                    None,
                    self.key,
                    ["components", section, "items", ri],
                    "evidence_only",
                    "stock_label",
                    reason,
                    [],
                )
        wolfe = self.after["solutions"][0]
        for old_index in range(17, 20):
            old = self.before["ingredients"][old_index]
            ri, row = next(
                (i, r)
                for i, r in enumerate(body["components"][2]["items"])
                if r["component_name"] == old["preferred_term"]
            )
            self.component(
                ["solutions", 0, "composition"],
                row,
                ["components", 2, "items", ri],
                "batch_mass",
                old_index,
            )
        wolfe["solutions"] = []
        self.descriptor(
            ["solutions", 0, "solutions"],
            body["components"][2]["items"][3],
            ["components", 2, "items", 3],
            old_index=4,
        )
        self.after["preparation_steps"] = [
            {"step_number": 1, "action": "AUTOCLAVE", "description": body["comments"][0]["comment"]}
        ]
        self.claim(
            ["preparation_steps"],
            None,
            self.key,
            ["comments", 0],
            "add",
            "preparation_scope",
            "Restore the source preparation, including the later per-liter reducer additions; this instruction does not establish a measured final volume.",
            [],
        )
        self.note(
            self.after, "Post-inoculation source instruction: " + body["comments"][1]["comment"]
        )
        self.claim(
            ["notes"],
            ["notes"],
            self.key,
            ["comments", 1],
            "evidence_only",
            "preparation_scope",
            "Preserve the separately stated gas/pressure instruction as text; the preparation action enum has no pressure action.",
            [],
        )

    def finish(self, timestamp, *, action=ACTION, change_suffix=None):
        self.after.setdefault("references", [])
        for key in self.used:
            m = self.context["sources"][key]["metadata"]
            title = (
                "Medium data"
                if key.startswith("JCM")
                else "TOGO Medium " + key if key.startswith("M") else "MediaDive medium " + key
            )
            self.after["references"].append(
                {
                    "reference": m["url"],
                    "title": title,
                    "notes": f"source_type={'culture_collection_page' if key.startswith('JCM') else 'dataset'}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={m['accessed_at'][:10]}; capture_sha256={m['sha256']}. Authors and publication year not supplied; source access/copyright year is not publication year. Source-specific preparation and quantity evidence, not organism-growth evidence.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=action,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restored preparation boundaries and explicit stock-dose bases. Preserved source-specific conflicts, chemical annotations and earlier history. Batch-mass notes do not assert final concentrations; provider-declared stock rates remain qualified. No growth or identity equivalence claim inferred.",
            changes="; ".join(
                f"{c['old_field']} -> {c['field']}: {c['old']} -> {c['new']} ({c['status']}; {c['reference']})"
                for c in self.claims
                if c["status"] not in {"evidence_only", "unsupported"}
            )
            + (
                change_suffix
                if change_suffix is not None
                else "; gas/pressure instructions and source disagreement remain in separately supported notes."
            ),
        )
        runner.require(not runner.errors(self.after, "MediaRecipe"), "Proposed schema failure")
        return self.after, self.claims, self.lineage


def build(before, key, timestamp):
    review = Review(before, key)
    review.togo() if key == "M257" else review.media_dive()
    return review.finish(timestamp)


def process(
    root, plan_path, mode, *, context=None, context_sha=CONTEXT_SHA, builder=build, action=ACTION
):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    context = frozen() if context is None else context
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    runner.require(head == context["commit"], "Reviewed commit drift")
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse plan overwrite")
        plan = {
            "version": 1,
            "commit": head,
            "context_sha256": context_sha,
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
    else:
        plan = json.loads(plan_path.read_text())
        runner.require(
            plan["context_sha256"] == context_sha and plan["commit"] == head, "Plan drift"
        )
    records, pending = [], []
    for item in context["records"]:
        path = root / item["path"]
        before = item["before_text"].encode()
        runner.require(
            runner.sha(before) == item["before_sha256"] and not path.is_symlink(),
            "Baseline/symlink drift",
        )
        after, claims, lineage = builder(runner.load_yaml(before), item["key"], plan["created_at"])
        output = runner.render(before.decode(), after)
        current = path.read_bytes()
        runner.require(current in (before, output), "Concurrent edit")
        records.append(
            {
                **item,
                "action": action,
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "claims": claims,
                "lineage": lineage,
            }
        )
        pending.append((path, current, output))
    if mode != "preview":
        runner.require(records == plan["records"], "Frozen decision drift")
    plan["records"] = records
    runner.safe_targets(root, plan)
    runner.require(
        all(not p.is_symlink() and p.read_bytes() == c for p, c, o in pending),
        "Concurrent edit before write",
    )
    if mode == "preview":
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        for path, current, output in pending:
            runner.require(
                not path.is_symlink() and path.read_bytes() == current,
                "Concurrent edit during write",
            )
            if mode == "apply" and current != output:
                path.write_bytes(output)
            runner.require(path.read_bytes() == output, "Result not applied")
    return plan, {
        "mode": mode,
        "records": len(records),
        "changed": sum(c != o for p, c, o in pending) if mode == "apply" else 0,
        "already_applied": sum(c == o for p, c, o in pending),
        "claims": sum(len(r["claims"]) for r in records),
    }


def reports(plan, applied):
    out = HERE / "records"
    out.mkdir(exist_ok=True)
    for r in plan["records"]:
        marker = "Record" if r["key"] == "M257" else "Follow-up target"
        lines = [
            "# Methanogen Stock-Boundary Review",
            "",
            f"- {marker}: {r['path']}",
            f"- ID: {r['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {r['before_sha256']}",
            f"- Result SHA256: {r['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "All prior quantity slots and new amount assertions are accounted below, including unverified gas placeholders. Stock rates are provider-qualified, not final-medium concentrations; batch masses remain in supported notes when final volume is unknown. Existing chemical mappings are preserved, not recertified. Authors/year are unknown. J985/J265 supplement their existing exact-path reports. See validation.json for actual terminal gates.",
            "",
            "| Ingredient/context | Old field | Current field | Old | New | Status | DOI/PURL | Exact snippet | Decision |",
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
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--plan", type=Path, default=HERE / "plan.json")
    p.add_argument("--reports", action="store_true")
    modes = p.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    args = p.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.plan, mode)
    if args.reports:
        reports(plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
