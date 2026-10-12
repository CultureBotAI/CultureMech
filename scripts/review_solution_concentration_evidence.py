#!/usr/bin/env python3
"""Preview and apply source-backed solution concentration curation.

An explicit --apply consumes a previously generated, hash-pinned plan. Numeric
conflicts, source/formulation drift, stock strengths, conditional rows, and
water make-up instructions remain unresolved, never inferred. This pass is not
equivalent to complete scientific review of every record or its receiving media.
"""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import re
import subprocess
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

import yaml
from fetch_solution_concentration_sources import API, load_yaml, read_capture, select
from record_io import DUMP_KWARGS
from repair_mediadive_stock_concentration_evidence import (
    EvidenceDumper,
    cell,
    exact_object,
    number,
    preserve_unchanged,
    require,
    sha,
)

from culturemech.curate.curation_event import record_curation_event
from culturemech.merge.fingerprint import RecipeFingerprinter
from culturemech.validation.write_validated import infer_target_class, validate_recipe

ROOT = Path(__file__).resolve().parents[1]
ACTION = "CURATED_SOLUTION_CONCENTRATION_SOURCE_EVIDENCE"
MASS = {
    "g": Decimal(1),
    "mg": Decimal("0.001"),
    "ug": Decimal("0.000001"),
    "\u00b5g": Decimal("0.000001"),
    "\u03bcg": Decimal("0.000001"),
}
SUPPORTED = {"correct", "add", "evidence_only"}


def field_name(pointer):
    text = ""
    for key in pointer:
        text += f"[{key}]" if isinstance(key, int) else ("." if text else "") + key
    return text


def all_claims(doc):
    """Every stored concentration, plus missing ingredient concentrations."""
    claims = []

    def walk(node, pointer, ancestors):
        if not isinstance(node, (dict, list)):
            return
        require(id(node) not in ancestors, "Cyclic recipe structure")
        parents = ancestors | {id(node)}
        if isinstance(node, dict):
            ingredient = len(pointer) >= 2 and pointer[-2] in {"composition", "ingredients"}
            if "concentration" in node or ingredient:
                claims.append(
                    {
                        "pointer": pointer,
                        "field": field_name(pointer + ["concentration"]),
                        "ingredient": node.get("preferred_term", "working stock dose"),
                        "old": copy.deepcopy(node.get("concentration")),
                        "new": None,
                        "status": "unsupported",
                        "reference": None,
                        "snippet": None,
                        "locator": None,
                        "explanation": "Outside direct composition matching; unchanged.",
                    }
                )
            for key, value in node.items():
                if key not in {"concentration", "evidence", "references", "curation_history"}:
                    walk(value, pointer + [key], parents)
        else:
            for index, value in enumerate(node):
                walk(value, pointer + [index], parents)

    walk(doc, [], set())
    return claims


def get_node(doc, pointer):
    for key in pointer:
        doc = doc[key]
    return doc


def rounded_equal(computed, reported):
    """Allow source rounding, never a unit-scale discrepancy."""
    if computed == reported:
        return True
    quantum = Decimal(1).scaleb(reported.as_tuple().exponent)
    tolerance = min(abs(computed) * Decimal("0.000005"), quantum / 2)
    return abs(computed - reported) <= tolerance


def decide(source, row, old):
    if row.get("optional") != 0 or row.get("condition"):
        return (
            None,
            "unsupported",
            "Optional/conditional source row needs separate formulation review.",
        )
    if row.get("attribute"):
        return (
            None,
            "unsupported",
            "Source attribute may encode stock strength, material grade, or preparation context; not discarded.",
        )
    try:
        amount = number(row.get("amount"))
        if amount == 0:
            return (
                None,
                "unsupported",
                "Source zero may encode an unquantified addition; preparation context needs review.",
            )
        volume = number(source.get("volume"))
        require(volume > 0, "No positive provider-declared stock volume")
        if old is not None:
            require(
                set(old) == {"value", "unit"},
                "Existing denominator or quantity metadata needs review",
            )
        if row.get("unit") in MASS:
            reported = number(row.get("g_l"))
            calculated = amount * MASS[row["unit"]] / (volume / 1000)
            if not rounded_equal(calculated, reported):
                return None, "conflict", "Source g_l disagrees with amount/unit/volume"
            proposed = {"value": str(row["g_l"]), "unit": "G_PER_L"}
            if old is not None:
                if old["unit"] != "G_PER_L" or number(old["value"]) != reported:
                    return (
                        None,
                        "conflict",
                        "Existing mass concentration conflicts with current source; no automatic replacement",
                    )
                proposed = copy.deepcopy(old)
            return (
                proposed,
                "add" if old is None else "evidence_only",
                (
                    f"Provider explicitly reports g_l={row['g_l']}. Arithmetic check: {amount} {row['unit']} "
                    f"* {MASS[row['unit']]} g/{row['unit']} / ({volume} ml / 1000 ml per L) "
                    f"= {calculated} g/L, consistent with the reported value at its precision. "
                    "Evidence supports the provider-declared concentration within this solution, "
                    "not a concentration in a receiving medium or an independently measured final volume. "
                    "Water addition alone is not used to infer a final volume."
                ),
            )
        if (
            row.get("compound_id") == 4
            and row.get("compound") == "Distilled water"
            and row.get("unit") == "ml"
        ):
            if not isinstance(source.get("steps"), list):
                return (
                    None,
                    "unsupported",
                    "Source preparation-step list is missing or malformed; water interpretation needs review.",
                )
            if source.get("steps"):
                return (
                    None,
                    "unsupported",
                    "Preparation steps may specify make-up volume; manual water review required",
                )
            require(row.get("g_l") is None, "Unexpected water mass conversion")
            proposed = {"value": format(amount / 1000, "f"), "unit": "L"}
            if old is not None:
                if old["unit"] == "L" and number(old["value"]) == amount / 1000:
                    proposed = copy.deepcopy(old)
                else:
                    legacy = amount * 1000 / volume
                    if not (
                        old["unit"] == "PERCENT_V_V"
                        and abs(number(old["value"]) - legacy)
                        <= max(abs(legacy) * Decimal("1e-12"), Decimal("1e-15"))
                    ):
                        return (
                            None,
                            "conflict",
                            "Old water value does not match the diagnosed importer error",
                        )
            return (
                proposed,
                "add" if old is None else "evidence_only" if old == proposed else "correct",
                (
                    f"Source water addition is {amount} ml per prepared batch: {amount} / 1000 = {amount / 1000} L. "
                    "No source preparation step gives a competing make-up instruction. This is a batch dose, "
                    "not a volume percentage; no final-volume or solvent-density assumption is made."
                ),
            )
        return (
            None,
            "unsupported",
            "Unit or liquid/stock context requires source-specific review; no conversion guessed.",
        )
    except (ValueError, ArithmeticError, KeyError) as exc:
        return None, "unsupported", str(exc)


def review(doc, raw, meta, timestamp):
    source = json.loads(raw)["data"]
    claims = all_claims(doc)
    after = copy.deepcopy(doc)
    sid = source["id"]
    reference = API + str(sid)
    rows = source.get("recipe", [])
    compound_rows = [r for r in rows if r.get("compound_id") is not None]
    reason = None
    if (
        doc.get("term") != {"id": f"mediadive.solution:{sid}", "label": source["name"]}
        or doc.get("preferred_term") != source["name"]
    ):
        reason = "Exact solution ID/name mismatch; do not substitute a similar formulation."
    old_ids = [n.get("term", {}).get("id") for n in doc.get("composition", [])]
    new_ids = [f"mediadive.compound:{r['compound_id']}" for r in compound_rows]
    if Counter(old_ids) != Counter(new_ids):
        reason = "Direct ingredient inventory differs from source; source drift or missing/extra ingredients need review."
    by_id = {}
    for index, row in enumerate(rows):
        if row.get("compound_id") is not None:
            by_id.setdefault(f"mediadive.compound:{row['compound_id']}", []).append((index, row))
    for claim in claims:
        if reason:
            claim.update(status="conflict", explanation=reason, reference=reference)
            continue
        pointer = claim["pointer"]
        if len(pointer) != 2 or pointer[0] != "composition":
            continue
        node = get_node(after, pointer)
        matches = by_id.get(node.get("term", {}).get("id"), [])
        if len(matches) != 1:
            claim.update(
                status="conflict",
                explanation="Ambiguous source rows for this compound ID.",
                reference=reference,
            )
            continue
        index, row = matches[0]
        snippet = exact_object(raw, row)
        locator = f"$.data.recipe[{index}] (compound_id={row['compound_id']})"
        claim.update(reference=reference, snippet=snippet, locator=locator)
        if (
            node["preferred_term"] != row.get("compound")
            or node["term"].get("label") != row.get("compound")
            or row.get("solution_id") is not None
        ):
            claim.update(
                status="conflict",
                explanation="Exact compound label/form or compound-versus-stock identity mismatch.",
            )
            continue
        if any(e.get("reference") == reference for e in node.get("evidence", [])):
            claim["explanation"] = (
                "Existing same-source evidence retained; reconcile its scope manually rather than duplicate or replace it."
            )
            continue
        if row.get("compound_id") == 4 and not source.get("steps"):
            notes = doc.get("preparation_notes", "")
            original_volume = re.fullmatch(r"Original volume: (\d+(?:\.\d+)?) mL", notes)
            notes_agree = not notes or (
                original_volume is not None
                and number(original_volume[1]) == number(source.get("volume"))
            )
            if not notes_agree or node.get("notes") or doc.get("notes"):
                claim["explanation"] = (
                    "Existing local preparation context needs review before changing water quantity."
                )
                continue
        proposed, status, explanation = decide(source, row, claim["old"])
        claim.update(new=proposed, status=status, explanation=explanation)
        if proposed is None:
            continue
        node["concentration"] = proposed
        volume_excerpt = f'"volume": {source["volume"]}'
        require(volume_excerpt in raw, "Source volume excerpt is not exact")
        explanation += f" Additional exact excerpt at $.data.volume: {volume_excerpt}."
        claim["explanation"] = explanation
        node.setdefault("evidence", []).append(
            {
                "reference": reference,
                "supports": "SUPPORT",
                "snippet": snippet,
                "explanation": f"Concentration evidence for {claim['field']} ({node['preferred_term']}) "
                f"in MediaDive solution {sid}; locator={locator}. {explanation} "
                f"Retrieved {meta['accessed_at']}; response SHA256={meta['sha256']}.",
            }
        )
    # Source-only additions are not silently dropped or mistaken for compound amounts.
    for index, row in enumerate(rows):
        if (
            row.get("solution_id") is not None
            or f"mediadive.compound:{row.get('compound_id')}" not in old_ids
        ):
            claims.append(
                {
                    "pointer": None,
                    "field": f"source.recipe[{index}]",
                    "ingredient": row.get("solution") or row.get("compound"),
                    "old": None,
                    "new": None,
                    "status": "unsupported",
                    "reference": reference,
                    "snippet": exact_object(raw, row),
                    "locator": f"$.data.recipe[{index}]",
                    "explanation": "Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution.",
                }
            )
    changed = [c for c in claims if c["status"] in SUPPORTED]
    if changed:
        refs = after.setdefault("references", [])
        if not any(r["reference"] == reference for r in refs):
            refs.append(
                {
                    "reference": reference,
                    "title": f"MediaDive solution {sid}: {source['name']}",
                    "notes": f"source_type=dataset; discovery_mode=existing_record_reference; "
                    f"accessed_on={meta['accessed_at'][:10]}; source_organization=DSMZ; "
                    f"locator=$.data; response_sha256={meta['sha256']}; "
                    "individual authors and publication year not supplied. Provider-declared solution amounts, not receiving-medium concentrations.",
                }
            )
        record_curation_event(
            after,
            curator="codex",
            action=ACTION,
            source=reference,
            timestamp=timestamp,
            notes="Source review decision captured at plan timestamp. Exact source IDs, labels, snippets, and arithmetic checked. "
            "Unsupported rows retained; no receiving-medium concentration inferred.",
            changes="; ".join(
                f"{c['field']}: {json.dumps(c['old'], sort_keys=True)} -> {json.dumps(c['new'], sort_keys=True)} ({c['status']})"
                for c in changed
            ),
        )
    return after, claims


def render(before, after):
    result = preserve_unchanged(before, yaml.dump(after, Dumper=EvidenceDumper, **DUMP_KWARGS))
    require(load_yaml(result) == after, "Serialization changed data")
    return result.encode()


@dataclass(frozen=True)
class ReviewAdapter:
    source_id_key: str
    target_class: str
    reader: Callable
    reviewer: Callable
    collect_claims: Callable
    unchanged_fields: tuple[str, ...]


def solution_adapter():
    return ReviewAdapter(
        "solution_id",
        "SolutionRecipe",
        read_capture,
        review,
        all_claims,
        ("ingredients", "solutions"),
    )


def errors(doc, target_class="SolutionRecipe"):
    return [e.message for e in validate_recipe(doc, target_class=target_class)]


def check_merge_inputs(doc, after, adapter):
    require(
        infer_target_class(doc) == infer_target_class(after) == adapter.target_class,
        "Root record class changed or does not match review scope",
    )
    for key in adapter.unchanged_fields:
        require(
            (key in doc) == (key in after) and doc.get(key) == after.get(key),
            "Merge input fields changed",
        )
    if adapter.target_class == "MediaRecipe" and doc.get("ingredients"):
        fingerprinter = RecipeFingerprinter()
        require(
            fingerprinter.fingerprint(doc) == fingerprinter.fingerprint(after),
            "Ingredient identity fingerprint changed",
        )


def preview(root, records, cache, commit, *, adapter=None):
    adapter = adapter or solution_adapter()
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    plan = {"version": 1, "commit": commit, "created_at": timestamp, "records": []}
    if adapter.target_class != "SolutionRecipe":
        plan["target_class"] = adapter.target_class
    for index, item in enumerate(records, 1):
        path = root / item["path"]
        before = path.read_bytes()
        require(sha(before) == item["before_sha256"], f"Inventory drift: {path}")
        doc = load_yaml(before)
        require(doc["id"] == item["id"], "Stable ID drift")
        claims = adapter.collect_claims(doc)
        result = {
            **item,
            "after_sha256": sha(before),
            "source_sha256": None,
            "claims": claims,
            "baseline_errors": errors(doc, adapter.target_class),
            "post_errors": [],
            "failure": None,
            "merge_fingerprint_unchanged": True,
            "merge_fingerprint_scope": (
                "outside_medium_scope" if adapter.target_class == "SolutionRecipe" else "medium"
            ),
        }
        try:
            raw, meta = adapter.reader(cache, item[adapter.source_id_key])
            result["source_sha256"] = meta["sha256"]
            result["source_accessed_at"] = meta["accessed_at"]
            after, claims = adapter.reviewer(doc, raw, meta, timestamp)
            result["claims"] = claims
            if result["baseline_errors"]:
                for claim in claims:
                    if claim["status"] in SUPPORTED:
                        claim.update(
                            status="schema_gap",
                            new=None,
                            explanation="Baseline schema errors block mutation.",
                        )
                result["post_errors"] = result["baseline_errors"]
            else:
                result["post_errors"] = errors(after, adapter.target_class)
                require(
                    not result["post_errors"], "Proposed record failed closed-schema validation"
                )
                check_merge_inputs(doc, after, adapter)
                output = render(before.decode(), after) if after != doc else before
                result["after_sha256"] = sha(output)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            result["failure"] = str(exc)
            for claim in result["claims"]:
                if claim["status"] in SUPPORTED:
                    claim.update(
                        status="unsupported",
                        new=None,
                        explanation=f"Record preflight failed: {exc}",
                    )
        plan["records"].append(result)
        if index % 25 == 0:
            print(json.dumps({"reviewed": index, "selected": len(records)}), flush=True)
    return plan


def safe_targets(root, plan):
    require(plan.get("version") == 1, "Unsupported plan version")
    tracked = set(
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root)
        .decode()
        .split("\0")
    )
    paths = [p["path"] for p in plan["records"]]
    require(len(paths) == len(set(paths)), "Duplicate target in plan")
    for p in paths:
        require(
            p in tracked and p.startswith("data/normalized_yaml/") and p.endswith(".yaml"),
            "Non-authoritative or non-exact target",
        )
        require(not (root / p).is_symlink(), "Symlink target refused")
    for item in plan["records"]:
        require(
            any(c["status"] in SUPPORTED for c in item["claims"])
            == (item["before_sha256"] != item["after_sha256"]),
            "Plan change count disagrees with supported claims",
        )


def apply(root, plan, cache, *, adapter=None):
    adapter = adapter or solution_adapter()
    require(
        plan.get("target_class", "SolutionRecipe") == adapter.target_class,
        "Wrong plan target class",
    )
    safe_targets(root, plan)
    pending = []
    already_applied = 0
    for item in plan["records"]:
        path = root / item["path"]
        current = path.read_bytes()
        digest = sha(current)
        require(digest in {item["before_sha256"], item["after_sha256"]}, f"Concurrent edit: {path}")
        if item["before_sha256"] == item["after_sha256"]:
            continue
        raw, meta = adapter.reader(cache, item[adapter.source_id_key])
        require(meta["sha256"] == item["source_sha256"], "Source changed since preview")
        require(
            meta["accessed_at"] == item["source_accessed_at"], "Source capture metadata changed"
        )
        if digest == item["after_sha256"]:
            already_applied += 1
            continue
        require(
            not item["failure"] and not item["baseline_errors"] and not item["post_errors"],
            "Failed proposal cannot apply",
        )
        doc = load_yaml(current)
        require(doc["id"] == item["id"], "Stable ID mismatch")
        after, claims = adapter.reviewer(doc, raw, meta, plan["created_at"])
        require(claims == item["claims"], "Preview claims changed")
        check_merge_inputs(doc, after, adapter)
        require(not errors(after, adapter.target_class), "Write-time closed-schema failure")
        output = render(current.decode(), after)
        require(sha(output) == item["after_sha256"], "Preview result changed")
        pending.append((path, current, output))
    for path, before, _ in pending:
        require(path.read_bytes() == before, "Concurrent edit before write")
    for path, before, output in pending:
        require(path.read_bytes() == before, "Concurrent edit during apply")
        path.write_bytes(output)
    return {"changed": len(pending), "already_applied": already_applied}


def followup_chain(item, successors=()):
    """Follow explicit hash-linked curation, never an arbitrary later history event."""
    edges = {}
    for record in successors:
        if record["path"] != item["path"]:
            continue
        require(record["id"] == item["id"], "Successor ID mismatch")
        before, after = record["before_sha256"], record["after_sha256"]
        require(
            all(re.fullmatch(r"[0-9a-f]{64}", h) for h in (before, after)), "Invalid successor hash"
        )
        require(before != after and before not in edges, "Ambiguous successor chain")
        require(sha(record["before_text"].encode()) == before, "Successor baseline hash mismatch")
        edges[before] = record
    digest = item["after_sha256"]
    seen = set()
    chain = []
    while digest in edges:
        require(digest not in seen, "Cyclic successor chain")
        seen.add(digest)
        record = edges[digest]
        chain.append(record)
        digest = record["after_sha256"]
    return chain


def followup_result_hash(item, successors=()):
    chain = followup_chain(item, successors)
    return (chain[-1]["after_sha256"] if chain else item["after_sha256"]), len(chain)


def resolved_claim(item, claim, successors, source):
    """Require exact before/after and source evidence for relocated/withdrawn claims."""
    pointer, field, withdrawn = claim["pointer"], claim["field"], False
    for record in followup_chain(item, successors):
        resolutions = record.get("claim_resolutions", [])
        keys = [(tuple(r["from_pointer"]), r["reference"]) for r in resolutions]
        require(len(keys) == len(set(keys)), "Duplicate claim resolution")
        matches = [
            r
            for r in resolutions
            if r["from_pointer"] == pointer and r["reference"] == claim["reference"]
        ]
        if not matches:
            continue
        require(not withdrawn, "A withdrawn claim cannot be silently reactivated")
        r = matches[0]
        require(r["disposition"] in {"relocated", "withdrawn"}, "Unknown claim resolution")
        require(
            sha(record["after_text"].encode()) == record["after_sha256"],
            "Resolution result hash mismatch",
        )
        before = get_node(load_yaml(record["before_text"]), pointer)
        after = get_node(load_yaml(record["after_text"]), r["to_pointer"])
        require(
            before.get("concentration") == r["old_concentration"] == claim["new"]
            and before["preferred_term"] == after["preferred_term"] == claim["ingredient"],
            "Resolution changed claim identity/baseline",
        )
        old_entries = [e for e in before.get("evidence", []) if e["reference"] == r["reference"]]
        new_entries = [e for e in after.get("evidence", []) if e["reference"] == r["reference"]]
        require(
            len(old_entries) == len(new_entries) == 1
            and old_entries[0]["snippet"] == new_entries[0]["snippet"] == claim["snippet"]
            and new_entries[0]["supports"] == "SUPPORT",
            "Resolution lost the historical source snippet",
        )
        require(
            sha(source.encode()) == record["source_sha256"]
            and r["source_snippet"] in source
            and json.loads(r["source_snippet"])
            == get_node(json.loads(source), r["source_pointer"]),
            "Resolution source excerpt mismatch",
        )
        withdrawn = r["disposition"] == "withdrawn"
        require(
            (
                "concentration" not in after
                if withdrawn
                else after.get("concentration") == claim["new"]
            ),
            "Resolution quantity mismatch",
        )
        pointer = r["to_pointer"]
        field = field_name(pointer + ["notes" if withdrawn else "concentration"])
        require(
            field == r["new_field"]
            and field in new_entries[0]["explanation"]
            and r["source_snippet"] in new_entries[0]["explanation"]
            and bool(r["reason"])
            and r["reason"] in new_entries[0]["explanation"],
            "Resolution lacks scoped replacement evidence",
        )
        if withdrawn:
            require(bool(after.get("notes")), "Withdrawal lacks the supported input amount/context")
    return pointer, field, withdrawn


def verify(root, plan, cache, successors=(), *, adapter=None):
    adapter = adapter or solution_adapter()
    require(
        plan.get("target_class", "SolutionRecipe") == adapter.target_class,
        "Wrong plan target class",
    )
    safe_targets(root, plan)
    evidence_count = 0
    superseded = 0
    withdrawn_count = 0
    relocated_count = 0
    for item in plan["records"]:
        raw_record = (root / item["path"]).read_bytes()
        expected, depth = followup_result_hash(item, successors)
        require(sha(raw_record) == expected, f"Result hash mismatch: {item['path']}")
        superseded += bool(depth)
        if item["before_sha256"] == item["after_sha256"]:
            continue
        doc = load_yaml(raw_record)
        require(not errors(doc, adapter.target_class), "Post-apply schema failure")
        source, meta = adapter.reader(cache, item[adapter.source_id_key])
        require(meta["sha256"] == item["source_sha256"], "Source hash mismatch")
        for claim in item["claims"]:
            if claim["status"] not in SUPPORTED:
                continue
            pointer, field, withdrawn = resolved_claim(item, claim, successors, source)
            node = get_node(doc, pointer)
            require(
                (
                    "concentration" not in node
                    if withdrawn
                    else node.get("concentration") == claim["new"]
                ),
                "Wrong persisted quantity",
            )
            entries = [e for e in node.get("evidence", []) if e["reference"] == claim["reference"]]
            require(
                len(entries) == 1
                and entries[0]["snippet"] == claim["snippet"]
                and claim["snippet"] in source,
                "Missing, duplicate, or inexact persisted source snippet",
            )
            require(field in entries[0]["explanation"], "Evidence claim scope lost")
            evidence_count += not withdrawn
            withdrawn_count += withdrawn
            relocated_count += pointer != claim["pointer"] and not withdrawn
    result = {
        "checked_record_hashes": len(plan["records"]),
        "verified_new_snippets": evidence_count,
    }
    if successors:
        result["superseded_record_hashes"] = superseded
    if withdrawn_count:
        result["withdrawn_concentration_claims"] = withdrawn_count
        result["verified_withdrawn_snippets"] = withdrawn_count
    if relocated_count:
        result["relocated_concentration_claims"] = relocated_count
    return result


def summary(plan):
    return {
        "records": len(plan["records"]),
        "proposed_changed": sum(r["before_sha256"] != r["after_sha256"] for r in plan["records"]),
        "failed": sum(bool(r["failure"]) for r in plan["records"]),
        "schema_blocked": sum(bool(r["baseline_errors"]) for r in plan["records"]),
        "claims": dict(Counter(c["status"] for r in plan["records"] for c in r["claims"])),
    }


def reports(
    folder, plan, applied, *, source_api=API, source_id_key="solution_id", title="Solution"
):
    folder.mkdir(parents=True, exist_ok=True)
    for item in plan["records"]:
        state = "preview"
        if applied:
            state = (
                "changed locally"
                if item["before_sha256"] != item["after_sha256"]
                else "reviewed; unchanged"
            )
        lines = [
            f"# {title} Concentration Review: {item['name'].strip()}",
            "",
            f"- Record: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: `{plan['commit']}`",
            f"- Before SHA256: `{item['before_sha256']}`",
            f"- Proposed/result SHA256: `{item['after_sha256']}`",
            f"- Source: {source_api}{item[source_id_key]}",
            f"- Source SHA256: {item['source_sha256']}",
            f"- Retrieved: {item.get('source_accessed_at', 'unknown')}",
            "- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.",
            f"- State: {state}; unresolved claims remain unchanged.",
            f"- Baseline schema errors: {len(item['baseline_errors'])}; proposed schema errors: {len(item['post_errors'])}.",
            f"- Operational failure: {item['failure'] or 'none'}",
            "",
            "Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. "
            "This is not a claim of manual inspection of every source sentence or automated reference-validator success. "
            "Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.",
            "",
            "| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in item["claims"]:
            action = (
                "unchanged"
                if c["status"] not in SUPPORTED
                else "applied" if applied else "proposed"
            )
            lines.append(
                f"| `{c['field']}` | "
                + " | ".join(
                    cell(c[k])
                    for k in (
                        "ingredient",
                        "old",
                        "new",
                        "status",
                        "reference",
                        "snippet",
                        "locator",
                        "explanation",
                    )
                )
                + f" | {action} |"
            )
        output = folder / (item["path"].removeprefix("data/normalized_yaml/") + ".md")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("\n".join(lines) + "\n")
    (folder / "summary.json").write_text(json.dumps(summary(plan), indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
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
    require(
        not args.followup_plan or (args.verify and not args.reports),
        "Follow-ups require verification without report rewriting",
    )
    successors = [r for p in args.followup_plan for r in json.loads(p.read_text())["records"]]
    if args.apply or args.verify:
        plan = json.loads(args.plan.read_text())
        outcome = (
            apply(ROOT, plan, args.cache)
            if args.apply
            else verify(ROOT, plan, args.cache, successors)
        )
        if args.reports:
            reports(args.reports, plan, True)
        print(json.dumps({**summary(plan), **outcome}), flush=True)
    else:
        require(args.inventory is not None, "Preview requires --inventory")
        require(not args.plan.exists(), "Do not overwrite a reviewed plan")
        manifest = json.loads(args.inventory.read_text())
        records = select(manifest, args.offset, args.limit)
        plan = preview(ROOT, records, args.cache, manifest["commit"])
        args.plan.parent.mkdir(parents=True, exist_ok=True)
        args.plan.write_text(json.dumps(plan, indent=2) + "\n")
        if args.reports:
            reports(args.reports, plan, False)
        print(json.dumps(summary(plan)), flush=True)
    return 1 if summary(plan)["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
