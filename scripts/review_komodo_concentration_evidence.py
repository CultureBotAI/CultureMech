#!/usr/bin/env python3
"""Review mapped KOMODO recipes without transferring base amounts to variants."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from decimal import Decimal
from functools import partial
from html.parser import HTMLParser
from pathlib import Path

import review_medium_concentration_evidence as medium
import review_solution_concentration_evidence as runner
from fetch_medium_concentration_sources import API, identifier, read_capture
from fetch_solution_concentration_sources import select
from inventory_komodo_concentration_sources import MAPPING_URL, read_mapping

ROOT = Path(__file__).resolve().parents[1]
ACTION = "CURATED_KOMODO_CONCENTRATION_SOURCE_EVIDENCE"


def read_source(cache, mid):
    mid = identifier(mid)
    if (cache / f"{mid}.json").exists():
        return read_capture(cache, mid)
    raw = (cache / f"{mid}.unavailable.body").read_bytes()
    meta = json.loads((cache / f"{mid}.unavailable.metadata.json").read_text())
    runner.require(
        meta["url"] == meta["response_url"] == API + mid
        and meta["http_status"] == 404
        and meta["sha256"] == runner.sha(raw),
        "Invalid unavailable-source capture",
    )
    datetime.datetime.fromisoformat(meta["accessed_at"])
    return raw.decode(), meta


def identity_problem(doc, data, item):
    row = item["mapping"]
    sid, name = row["cells"][:2]
    if (
        doc.get("id") != item["id"]
        or doc.get("original_name") != name
        or doc.get("media_term", {}).get("term") != {"id": f"komodo.medium:{sid}", "label": name}
    ):
        return "Exact KOMODO accession/name does not match the inspected mapping row."
    if sid != row["medium_id"] or doc.get("variant_relationship") not in {
        None,
        "SOURCE_DUPLICATE",
    }:
        return (
            "KOMODO variant requires its own formulation evidence; a link to the base "
            "DSMZ recipe or a local SOURCE_DUPLICATE annotation cannot authorize its amounts."
        )
    source = data["medium"]
    if (
        str(source["id"]) != row["medium_id"]
        or source.get("source") != "DSMZ"
        or source.get("link") != row["original_recipe"]
    ):
        return "Mapped original DSMZ accession/link does not match the amount source."
    local_ph = doc.get("ph_range")
    if "ph_value" in doc:
        local_ph = {"min": doc["ph_value"], "max": doc["ph_value"]}
    if local_ph and source.get("min_pH") is not None and source.get("max_pH") is not None:
        if any(
            Decimal(str(local_ph[key])) != Decimal(str(source[key + "_pH"]))
            for key in ("min", "max")
        ):
            return "KOMODO and amount-source pH conditions differ; establish the exact formulation/version before supporting its concentrations."
    if any(
        entry.get("reference") == MAPPING_URL
        for key in ("evidence", "references")
        for entry in doc.get(key, [])
    ):
        return "Existing mapping provenance needs reconciliation; no duplicate reference is added."
    return medium.formulation_problem(doc, data)


def mapping_evidence(item, metadata):
    return {
        "reference": MAPPING_URL,
        "supports": "SUPPORT",
        "snippet": item["mapping"]["snippet"],
        "explanation": (
            f"Source identity only: KOMODO accession {item['komodo_id']} maps to "
            f"{item['mapping']['original_recipe']}; locator=MediaList table row with "
            f"ID={item['komodo_id']}. This row supplies no ingredient amounts and "
            "does not establish equivalence of variants. Concentrations are supported "
            "separately by exact ingredient excerpts from the linked DSMZ dataset recipe. "
            f"Retrieved {metadata['accessed_at']}; response SHA256={metadata['sha256']}."
        ),
    }


class MappingTitle(HTMLParser):
    """Read one document title using the HTML parser's text/entity semantics."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.titles = []
        self.parts = None

    def handle_starttag(self, tag, attrs):
        runner.require(self.parts is None, "Markup inside mapping title")
        if tag == "title":
            self.parts = []

    def handle_data(self, data):
        if self.parts is not None:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == "title":
            runner.require(self.parts is not None, "Unmatched mapping title tag")
            self.titles.append(" ".join("".join(self.parts).split()))
            self.parts = None
        else:
            runner.require(self.parts is None, "Unclosed mapping title")


def captured_mapping_title(path, metadata):
    read_mapping(path, metadata)
    parser = MappingTitle()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    runner.require(
        parser.parts is None and len(parser.titles) == 1 and bool(parser.titles[0]),
        "Expected one nonempty mapping title",
    )
    return parser.titles[0]


def check_mapping_title(path, plan):
    if "mapping_title" in plan:
        runner.require(
            plan["mapping_title"] == captured_mapping_title(path, plan["mapping_source"]),
            "Frozen mapping title differs from captured source",
        )


def mapping_reference(metadata, title=None):
    # The old label is retained only to reproduce already-frozen historical plans.
    return {
        "reference": MAPPING_URL,
        "title": title if title is not None else "KOMODO media list: original-recipe mappings",
        "notes": (
            "source_type=dataset; discovery_mode=existing_record_reference; "
            "source_organization=KOMODO; "
            f"accessed_on={metadata['accessed_at'][:10]}; "
            f"response_sha256={metadata['sha256']}; individual authors and "
            "publication year not supplied. Identity mapping only, not concentration evidence."
        ),
    }


def review(doc, raw, meta, timestamp, *, records, metadata, withholdings=(), mapping_title=None):
    item = records[doc["id"]]
    if meta["http_status"] == 404:
        runner.require(
            not any(d["id"] == doc["id"] for d in withholdings), "Veto requires accessible source"
        )
        claims = medium.collect_claims(doc)
        for claim in claims:
            claim.update(
                reference=API + item["medium_id"],
                explanation=(
                    "Mapped DSMZ amount source returned HTTP 404. No ingredient evidence "
                    "was available from this endpoint; the mapping alone cannot support "
                    "a quantity. Original recipe retrieval remains an explicit follow-up."
                ),
            )
        return copy.deepcopy(doc), claims
    after, claims = medium.review(
        doc,
        raw,
        meta,
        timestamp,
        identity_checker=partial(identity_problem, item=item),
        action=ACTION,
        withholdings=withholdings,
    )
    supported = [c for c in claims if c["status"] in runner.SUPPORTED]
    if supported:
        context = (
            f" KOMODO accession {item['komodo_id']} is mapped to the same DSMZ "
            f"accession by {MAPPING_URL}; mapping response SHA256={metadata['sha256']}. "
            "The mapping supports identity only, not ingredient quantities or variants."
        )
        after.setdefault("evidence", []).append(mapping_evidence(item, metadata))
        after["references"].append(mapping_reference(metadata, mapping_title))
        for claim in supported:
            claim["explanation"] += context
            entries = runner.get_node(after, claim["pointer"])["evidence"]
            entries[-1]["explanation"] += context
        after["curation_history"][-1]["notes"] += context
        for reference in after["references"]:
            if reference["reference"] == API + item["medium_id"] and reference not in doc.get(
                "references", []
            ):
                reference["notes"] = reference["notes"].replace(
                    "discovery_mode=existing_record_reference",
                    "discovery_mode=cross_reference",
                )
                reference[
                    "notes"
                ] += " Discovered through the verified KOMODO original-recipe mapping."
    return after, claims


def adapter(records, metadata, withholdings=(), mapping_title=None):
    by_id = {item["id"]: item for item in records}
    runner.require(len(by_id) == len(records), "Duplicate record IDs")
    return runner.ReviewAdapter(
        "medium_id",
        "MediaRecipe",
        read_source,
        partial(
            review,
            records=by_id,
            metadata=metadata,
            withholdings=withholdings,
            mapping_title=mapping_title,
        ),
        medium.collect_claims,
        ("solutions", "variants", "variant_children", "parent_media", "variant_relationship"),
    )


def context(manifest, mapping, records):
    """Check the actual captured HTML, not self-reported mapping flags in a plan."""
    rows = read_mapping(mapping, manifest["mapping_source"])
    frozen = {item["path"]: item for item in manifest["records"]}
    runner.require(len(frozen) == len(manifest["records"]), "Duplicate inventory paths")
    for item in records:
        original = frozen[item["path"]]
        runner.require(
            all(item.get(key) == value for key, value in original.items()),
            "Frozen inventory changed",
        )
        row = rows[item["komodo_id"]]
        runner.require(row == item["mapping"], "Captured mapping row differs from inventory")
        runner.require(item["medium_id"] == row["medium_id"], "Wrong mapped source identifier")


def check_sources(records, cache):
    for item in records:
        _, meta = read_source(cache, item["medium_id"])
        runner.require(
            meta["sha256"] == item["source_sha256"]
            and meta["accessed_at"] == item["source_accessed_at"],
            "Source capture changed, including unchanged targets",
        )


def verify_mapping(root, plan, successors=()):
    checked = 0
    for item in plan["records"]:
        if item["before_sha256"] == item["after_sha256"]:
            continue
        raw = (root / item["path"]).read_bytes()
        expected_hash, depth = runner.followup_result_hash(item, successors)
        doc = runner.load_yaml(raw)
        for key, expected in (
            ("evidence", mapping_evidence(item, plan["mapping_source"])),
            ("references", mapping_reference(plan["mapping_source"], plan.get("mapping_title"))),
        ):
            entries = [e for e in doc[key] if e["reference"] == MAPPING_URL]
            runner.require(entries == [expected], "Persisted mapping provenance mismatch")
        runner.require(runner.sha(raw) == expected_hash, "Mapping record hash mismatch")
        if depth:
            chain = runner.followup_chain(item, successors)
            prior = runner.load_yaml(chain[0]["before_text"])["curation_history"]
            runner.require(
                prior[-1]["action"] == ACTION
                and prior[-1]["timestamp"] == plan["created_at"]
                and doc["curation_history"][: len(prior)] == prior,
                "Historical curation event lost",
            )
            for record in chain:
                runner.require(
                    runner.sha(record["after_text"].encode()) == record["after_sha256"],
                    "Successor result hash mismatch",
                )
        else:
            runner.require(doc["curation_history"][-1]["action"] == ACTION, "Wrong curation event")
        checked += 1
    return {"verified_mapping_snippets": checked}


def reports(folder, plan, applied):
    runner.reports(folder, plan, applied, source_api=API, source_id_key="medium_id", title="KOMODO")
    for item in plan["records"]:
        path = folder / (item["path"].removeprefix("data/normalized_yaml/") + ".md")
        text = path.read_text().replace(
            "discovery: existing record source ID", "discovery: verified KOMODO cross-reference"
        )
        text = text.replace(
            "Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer.",
            "Exact mapping identities and source-access status were checked. Amount quotations and arithmetic were checked for accepted claims only; unresolved records were not endorsed.",
        )
        text += (
            "\n## Source Mapping\n\n"
            f"KOMODO accession `{item['komodo_id']}`; original recipe: {item['mapping']['original_recipe']}.\n\n"
            f"Mapping source: {MAPPING_URL}; SHA256 `{plan['mapping_source']['sha256']}`; "
            f"retrieved {plan['mapping_source']['accessed_at']}. Exact captured row:\n\n"
            f"```html\n{item['mapping']['snippet']}\n```\n\n"
            "This is identity evidence only. A variant's link to a base recipe does not "
            "support the variant's quantities. The complete claim table above includes "
            "unchanged and unresolved results; a report is not scientific completion.\n"
        )
        path.write_text(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", required=True, type=Path)
    parser.add_argument("--mapping", required=True, type=Path)
    parser.add_argument("--cache", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--reports", type=Path)
    parser.add_argument("--withholdings", type=Path)
    parser.add_argument(
        "--followup-plan",
        type=Path,
        action="append",
        default=[],
        help="Explicit later curation plan; verify only, without rewriting historical reports",
    )
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=0)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    runner.require(
        not args.followup_plan or (args.verify and not args.reports),
        "Follow-ups require verification without report rewriting",
    )
    successors = [r for p in args.followup_plan for r in json.loads(p.read_text())["records"]]
    manifest = json.loads(args.inventory.read_text())
    digest = runner.sha(args.inventory.read_bytes())
    if args.apply or args.verify:
        runner.require(not args.withholdings, "Withholdings are frozen at preview")
        plan = json.loads(args.plan.read_text())
        runner.require(plan["inventory_sha256"] == digest, "Frozen inventory hash changed")
        runner.require(
            plan["mapping_source"] == manifest["mapping_source"], "Mapping metadata drift"
        )
        context(manifest, args.mapping, plan["records"])
        check_mapping_title(args.mapping, plan)
        check_sources(plan["records"], args.cache)
        decisions = plan.get("withholdings", [])
        medium.check_withholdings(ROOT, plan["records"], args.cache, decisions, successors)
        reviewer = adapter(
            plan["records"], plan["mapping_source"], decisions, plan.get("mapping_title")
        )
        if args.apply:
            outcome = runner.apply(ROOT, plan, args.cache, adapter=reviewer)
        else:
            outcome = runner.verify(ROOT, plan, args.cache, successors, adapter=reviewer)
        outcome.update(verify_mapping(ROOT, plan, successors))
    else:
        runner.require(not args.plan.exists(), "Refuse to overwrite frozen preview")
        records = select(manifest, args.offset, args.limit)
        context(manifest, args.mapping, records)
        title = captured_mapping_title(args.mapping, manifest["mapping_source"])
        decisions = json.loads(args.withholdings.read_text()) if args.withholdings else []
        medium.check_withholdings(ROOT, records, args.cache, decisions)
        plan = runner.preview(
            ROOT,
            records,
            args.cache,
            manifest["commit"],
            adapter=adapter(records, manifest["mapping_source"], decisions, title),
        )
        plan.update(
            inventory_sha256=digest,
            mapping_source=manifest["mapping_source"],
            mapping_title=title,
            withholdings=decisions,
        )
        args.plan.parent.mkdir(parents=True, exist_ok=True)
        args.plan.write_text(json.dumps(plan, indent=2) + "\n")
        outcome = {}
    if args.reports:
        reports(args.reports, plan, args.apply or args.verify)
    print(json.dumps({**runner.summary(plan), **outcome}), flush=True)
    return 1 if runner.summary(plan)["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
