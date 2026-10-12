#!/usr/bin/env python3
"""Apply the source-reviewed 2026-10-07 stock cohort, not a generic reimport.

Preview by default; --apply requires the five inspected, hash-pinned official
REST captures in --source-dir. Sources changing upstream require fresh review.
The all-record ingredient review remains a separate, unfinished objective.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
from collections import Counter
from decimal import Decimal
from pathlib import Path

import yaml
from record_io import DUMP_KWARGS

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
BASE = "f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f"
ACTION = "CURATED_MEDIADIVE_STOCK_CONCENTRATION_EVIDENCE"
DATE = "2026-10-07"
# solution ID, stable ID, exact filename, record SHA256, inspected response SHA256
COHORT = [
    (
        3980,
        "CultureMech:013037",
        "mediadive_3980_Trace_element_solution.yaml",
        "8ae08ecd61bc3ba5f6550f38018ebb2b91ecabaa04d5a8a52e4b326d887c551c",
        "6930d7f4c0bff23677be1bbbf61c580a4682140be0972da54a8203b34f79ed19",
    ),
    (
        3981,
        "CultureMech:013038",
        "mediadive_3981_Se_W_solution.yaml",
        "24e46e9fa96c418fdefcbe483512bbafe36d10af0e5327395c3bd49bcd02bcb5",
        "f31ddb3c46606d262bb9d8fa48f9ea5d4bab81c8917dc35dce7a7f0da6369a23",
    ),
    (
        3861,
        "CultureMech:012935",
        "mediadive_3861_Trace_vitamins.yaml",
        "1d6fbc92ee4ce5c59dd16b6075dc50d287f1b3fe3eaaf407c6c8d33d3e759b43",
        "c6829f83ad6e234909db1d65f45a27c24993e0280ff68c4d7355a8f6344335b9",
    ),
    (
        595,
        "CultureMech:014713",
        "mediadive_595_Trace_element_solution_SL-10.yaml",
        "db9ee9381cce911a78c16d9b8c00946eff42b3c8a46858be606d6836e4b7152d",
        "5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab",
    ),
    (
        5980,
        "CultureMech:014721",
        "mediadive_5980_Wolin_s_vitamin_solution_10x.yaml",
        "8e54f1cdede5cc6eb56616ee7bf066af8ec0dc48e4c7cf3abc14fe30e50e36ab",
        "2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c",
    ),
]
MAKE_UP = {
    3980: "Then add the remaining salts and bring volume to 1.0 L.",
    595: "Finally make up to 1000.00 ml.",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def number(value):
    require(not isinstance(value, bool) and value is not None, "Missing numeric input")
    result = Decimal(str(value))
    require(result.is_finite() and result >= 0, "Invalid numeric input")
    return result


def exact_object(raw, value):
    """Locate a unique parsed JSON object and quote its original bytes as text."""
    decoder = json.JSONDecoder()
    matches = []
    for start, char in enumerate(raw):
        if char != "{":
            continue
        try:
            parsed, end = decoder.raw_decode(raw, start)
        except json.JSONDecodeError:
            continue
        if parsed == value:
            matches.append(raw[start:end])
    require(len(matches) == 1, "Ambiguous or absent exact JSON excerpt")
    return matches[0]


def decide(solution_id, source, row, old):
    """Conservative rules for the inspected cohort; ambiguous strengths stay open."""
    require(row.get("compound_id") is not None, "Nested solution needs separate review")
    require(not row.get("solution_id") and not row.get("solution"), "Not a pure compound row")
    require(row.get("optional") == 0 and not row.get("condition"), "Conditional row")
    if row.get("attribute"):
        require(
            solution_id == 595 and row["compound_id"] == 68 and row["attribute"] == "25%",
            "Unreviewed stock attribute",
        )
        return None, (
            "Unresolved: source stock attribute is '25%' without w/w or w/v basis; "
            "10 ml is a stock dose, not a pure-HCl volume. Provider g_l=2.5 is "
            "not independently justified by the specified inputs. Existing value "
            "retained without new SUPPORT evidence; stock boundary needs review."
        )
    amount = number(row["amount"])
    if row["compound_id"] == 4:
        require(row["compound"] == "Distilled water" and row["unit"] == "ml", "Water identity/unit")
        require(row.get("g_l") is None, "Unexpected water mass conversion")
        require(
            old == {"value": str(row["amount"]), "unit": "PERCENT_V_V"},
            "Unexpected old water quantity",
        )
        if solution_id in MAKE_UP:
            quote = MAKE_UP[solution_id]
            require(quote in source["steps"][0]["step"], "Missing make-up instruction")
            return {"value": "to 1 L final volume", "unit": "VARIABLE"}, (
                f"Additional exact excerpt at $.data.steps[0].step: {quote!r} "
                f"The table lists {amount} ml water; the preparation instruction "
                "specifies make-up to 1 L, not a fixed volume of pure water or a "
                "volume percentage. Preserve that instruction as a variable water "
                "amount. No solvent density or exact delivered water volume assumed."
            )
        require(not source["steps"], "Water preparation needs manual review")
        return {"value": format(amount / 1000, "f"), "unit": "L"}, (
            f"Batch water amount: {amount} ml / 1000 ml per L = {amount / 1000} L. "
            "This is the source's water addition, not a volume percentage or an "
            "independently measured final stock volume."
        )
    require(row["unit"] in {"g", "mg"}, "Unsupported mass unit")
    volume = number(source["volume"])
    require(volume == 1000, "Only the reviewed one-liter stocks are in this batch")
    grams = amount / (1000 if row["unit"] == "mg" else 1)
    concentration = number(row["g_l"])
    require(grams / (volume / 1000) == concentration, "Source concentration/amount conflict")
    require(
        old["unit"] == "G_PER_L" and number(old["value"]) == concentration,
        "Unexpected mass concentration: this batch does not correct mass values",
    )
    require(set(old) == {"value", "unit"}, "Unexpected denominator")
    explanation = (
        f"Source explicitly reports g_l={row['g_l']} for this stock; additional "
        'exact excerpt at $.data.volume: "volume": 1000. '
        f"Cross-check: {amount} {row['unit']} = {grams} g; {grams} g / 1 L = "
        f"{concentration} g/L. This supports the provider-declared stock "
        "concentration, not a concentration in any receiving medium."
    )
    if solution_id in MAKE_UP:
        quote = MAKE_UP[solution_id]
        require(quote in source["steps"][0]["step"], "Missing stock-volume instruction")
        explanation += f" Additional exact excerpt at $.data.steps[0].step: {quote!r}"
    else:
        explanation += (
            " The API normalization is distinguished from the water addition; "
            "the latter alone does not prove a measured final volume."
        )
    return copy.deepcopy(old), explanation


def curate(before, raw, solution_id, stable_id, source_hash, timestamp=None):
    require(sha(raw.encode()) == source_hash, "Source hash changed; re-review required")
    payload = json.loads(raw)
    require(payload["status"] == 200 and payload["count"] == 1, "Source response failed")
    source = payload["data"]
    require(source["id"] == solution_id, "Wrong upstream solution")
    require(before["id"] == stable_id, "Wrong stable record ID")
    require(
        before["term"] == {"id": f"mediadive.solution:{solution_id}", "label": source["name"]},
        "Solution identity mismatch",
    )
    require(before["preferred_term"] == source["name"], "Solution label mismatch")
    require(not before.get("solutions") and not before.get("variants"), "Unreviewed nested content")
    require(not before.get("concentration"), "Unreviewed working concentration")
    rows = source["recipe"]
    require(len(rows) == len(before["composition"]), "Ingredient coverage mismatch")
    require(len({r["compound_id"] for r in rows}) == len(rows), "Duplicate source compound")
    require('"volume": 1000' in raw, "Missing exact volume excerpt")
    after = copy.deepcopy(before)
    reference = f"https://mediadive.dsmz.de/rest/solution/{solution_id}"
    claims = []
    for index, (node, row) in enumerate(zip(after["composition"], rows, strict=True)):
        field = f"composition[{index}].concentration"
        require(
            node["term"]
            == {"id": f"mediadive.compound:{row['compound_id']}", "label": row["compound"]},
            f"Identity mismatch at {field}",
        )
        require(node["preferred_term"] == row["compound"], f"Label mismatch at {field}")
        old = copy.deepcopy(node["concentration"])
        new, explanation = decide(solution_id, source, row, old)
        snippet = exact_object(raw, row)
        locator = f"$.data.recipe[{index}] (compound_id={row['compound_id']})"
        status = "unsupported" if new is None else "evidence_only" if new == old else "correct"
        claims.append(
            {
                "field": field,
                "ingredient": node["preferred_term"],
                "old": old,
                "new": new,
                "status": status,
                "reference": reference,
                "snippet": snippet,
                "locator": locator,
                "explanation": explanation,
            }
        )
        if new is None:
            continue
        require(
            not any(e["reference"] == reference for e in node.get("evidence", [])),
            "Existing source evidence needs reconciliation",
        )
        node["concentration"] = new
        node.setdefault("evidence", []).append(
            {
                "reference": reference,
                "supports": "SUPPORT",
                "snippet": snippet,
                "explanation": f"Concentration evidence for {field} ({node['preferred_term']}) "
                f"in MediaDive solution {solution_id}. Locator: {locator}. {explanation} "
                f"Inspected {DATE}; response SHA256={source_hash}.",
            }
        )
    placeholders = after.get("ingredients", [])
    require(
        placeholders
        == [
            {
                "preferred_term": "See source for composition",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
        "Unexpected legacy ingredient claim",
    )
    claims.append(
        {
            "field": "ingredients[0].concentration",
            "ingredient": placeholders[0]["preferred_term"],
            "old": placeholders[0]["concentration"],
            "new": None,
            "status": "unsupported",
            "reference": None,
            "snippet": None,
            "locator": None,
            "explanation": "Legacy import placeholder, not a source-quantified ingredient. Retained unchanged; not counted as a verified composition claim.",
        }
    )
    require(
        not any(r["reference"] == reference for r in after.get("references", [])),
        "Existing bibliography entry needs reconciliation",
    )
    after.setdefault("references", []).append(
        {
            "reference": reference,
            "title": f"MediaDive solution {solution_id}: {source['name']}",
            "notes": f"source_type=dataset; discovery_mode=existing_record_reference; accessed_on={DATE}; "
            f"source_organization=DSMZ; locator=$.data; response_sha256={source_hash}; "
            "individual authors and publication year not provided by this response. "
            "Ingredient identity matched by upstream solution and compound IDs, labels, and chemical forms. "
            "Provider-reported stock concentrations are not final-medium concentrations.",
        }
    )
    changes = "; ".join(
        f"{c['field']}: {json.dumps(c['old'], sort_keys=True)} -> "
        f"{json.dumps(c['new'], sort_keys=True)} ({c['status']})"
        for c in claims
        if c["new"] is not None
    )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        source=reference,
        notes="Exact source snippets added for supported claims. "
        "Water dose separated from final-volume make-up; unsupported "
        "claims and earlier provenance retained. Arithmetic is in each evidence explanation.",
        changes=changes,
        timestamp=timestamp,
    )
    return after, claims


def preserve_unchanged(before, after):
    """Keep unchanged YAML source spans, including historical line wrapping."""
    replacements = []

    def visit(old_node, new_node, old, new):
        if old == new:
            old_text = before[old_node.start_mark.index : old_node.end_mark.index].rstrip()
            new_text = after[new_node.start_mark.index : new_node.end_mark.index].rstrip()
            replacements.append(
                (new_node.start_mark.index, new_node.start_mark.index + len(new_text), old_text)
            )
        elif isinstance(old_node, yaml.MappingNode) and isinstance(new_node, yaml.MappingNode):
            old_nodes = {k.value: v for k, v in old_node.value}
            new_nodes = {k.value: v for k, v in new_node.value}
            for key in old_nodes.keys() & new_nodes.keys():
                visit(old_nodes[key], new_nodes[key], old[key], new[key])
        elif isinstance(old_node, yaml.SequenceNode) and isinstance(new_node, yaml.SequenceNode):
            for index in range(min(len(old_node.value), len(new_node.value))):
                visit(old_node.value[index], new_node.value[index], old[index], new[index])

    visit(
        yaml.compose(before, Loader=yaml.CSafeLoader),
        yaml.compose(after, Loader=yaml.CSafeLoader),
        yaml.load(before, Loader=yaml.CSafeLoader),
        yaml.load(after, Loader=yaml.CSafeLoader),
    )
    for start, end, value in sorted(replacements, reverse=True):
        after = after[:start] + value + after[end:]
    return after


class EvidenceDumper(yaml.SafeDumper):
    """Use corpus formatting, with readable exact multiline source excerpts."""


def represent_text(dumper, value):
    return dumper.represent_scalar(
        "tag:yaml.org,2002:str", value, style="|" if "\n" in value else None
    )


EvidenceDumper.add_representer(str, represent_text)


def prepare(root, source_dir):
    tracked = set(subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0"))
    plans = []
    for sid, stable_id, filename, baseline_hash, source_hash in COHORT:
        relative = f"data/normalized_yaml/bacterial/{filename}"
        require(relative in tracked, "Target is not an exact tracked path")
        path = root / relative
        baseline_bytes = subprocess.check_output(["git", "show", f"{BASE}:{relative}"], cwd=root)
        require(sha(baseline_bytes) == baseline_hash, "Unexpected baseline")
        baseline = baseline_bytes.decode()
        before = yaml.safe_load(baseline)
        current_bytes = path.read_bytes()
        current = yaml.safe_load(current_bytes)
        timestamp = None
        if current == before:
            require(current_bytes == baseline_bytes, "Concurrent presentation edit refused")
        if current != before:
            last = current.get("curation_history", [{}])[-1]
            require(
                last.get("action") == ACTION and last.get("curator") == "codex",
                "Concurrent edit refused",
            )
            timestamp = last["timestamp"]
        source_path = (
            source_dir / f"ingredient-mediadive-solution-{sid}-{DATE.replace('-', '')}.json"
        )
        raw = source_path.read_bytes().decode()
        after, claims = curate(before, raw, sid, stable_id, source_hash, timestamp)
        require(current in (before, after), f"Concurrent changes refused: {relative}")
        for doc in (before, after):
            require(
                not validate_recipe(doc, target_class="SolutionRecipe"),
                f"Closed-schema failure: {relative}",
            )
        output = preserve_unchanged(
            baseline, yaml.dump(after, Dumper=EvidenceDumper, **DUMP_KWARGS)
        )
        require(yaml.safe_load(output) == after, "Serialization changed content")
        plans.append(
            {
                "path": path,
                "relative": relative,
                "id": stable_id,
                "before": current_bytes,
                "after": output.encode(),
                "claims": claims,
                "source_hash": source_hash,
                "baseline_hash": baseline_hash,
            }
        )
    return plans


def apply(plans):
    # Preflight the entire cohort immediately before the first write.
    for plan in plans:
        require(plan["path"].read_bytes() == plan["before"], "Concurrent edit during preflight")
    changed = 0
    for plan in plans:
        if plan["before"] != plan["after"]:
            plan["path"].write_bytes(plan["after"])
            changed += 1
    return changed


def cell(value):
    if value is None:
        return "unknown / not asserted"
    text = json.dumps(value, sort_keys=True) if isinstance(value, dict) else str(value)
    return text.replace("|", "&#124;").replace("\n", "<br>")


def report(plan, applied):
    lines = [
        f"# Stock Concentration Review: {plan['id']}",
        "",
        f"- Record: {plan['relative']}",
        f"- ID: {plan['id']}",
        f"- Reviewed commit: `{BASE}`",
        "- Kind: SolutionRecipe",
        f"- Baseline SHA256: `{plan['baseline_hash']}`",
        f"- Source response SHA256: `{plan['source_hash']}`",
        f"- Result SHA256: `{sha(plan['after'])}`",
        f"- State: {'applied locally' if applied else 'preview only'}; corpus-wide curation incomplete.",
        "- Baseline and proposed closed-schema validation: passed.",
        "- Scope: every composition concentration and legacy placeholder; no nested solutions, working dose, or variants in this record.",
        "- Source/metadata: official DSMZ MediaDive REST dataset, accessed 2026-10-07; discovery by existing source ID. Individual authors and publication year unknown.",
        "- Evidence check: source inspected manually; exact JSON excerpts and arithmetic checked by the guarded mutator. This is not a linkml-reference-validator result.",
        "",
        "| Field | Ingredient | Old amount/unit/basis | Proposed amount/unit/basis | Status | DOI/PURL | Exact snippet | Locator | Calculation / scope | Action |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for claim in plan["claims"]:
        action = (
            "unchanged; unresolved"
            if claim["new"] is None
            else "applied" if applied else "proposed"
        )
        values = [
            claim[k]
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
        ]
        lines.append(
            f"| `{claim['field']}` | " + " | ".join(cell(v) for v in values) + f" | {action} |"
        )
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    plans = prepare(ROOT, args.source_dir)
    for plan in plans:
        print(report(plan, False))
    counts = Counter(c["status"] for p in plans for c in p["claims"])
    changed = apply(plans) if args.apply else 0
    if args.report_dir:
        args.report_dir.mkdir(parents=True, exist_ok=True)
        for plan in plans:
            (args.report_dir / (plan["path"].stem + ".md")).write_text(report(plan, args.apply))
    print(
        json.dumps(
            {
                "mode": "apply" if args.apply else "preview",
                "records": len(plans),
                "changed": changed,
                "claims": dict(counts),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
