#!/usr/bin/env python3
"""Review exact MediaDive medium sources with guarded, explicit evidence-only/add edits.

All selected records receive results, including stock boundaries, source-only
ingredients, preparation context, and variants. Complex stock topology is an
unresolved curation task, not permission to endorse flattened concentrations.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
from decimal import Decimal
from functools import partial
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import review_solution_concentration_evidence as runner
from fetch_medium_concentration_sources import API, read_capture
from fetch_solution_concentration_sources import select

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
ACTION = "CURATED_MEDIUM_CONCENTRATION_SOURCE_EVIDENCE"
MASS_CONCENTRATIONS = {
    "G_PER_L": Decimal(1),
    "MG_PER_L": Decimal("0.001"),
    "MICROG_PER_L": Decimal("0.000001"),
    "MG_PER_ML": Decimal(1),
}
SOURCE_RATES = {"g/l": Decimal(1), "mg/l": Decimal("0.001")}


def json_excerpt(raw, pointer):
    """Find a literal JSON value by path, even when equal objects occur elsewhere."""
    decoder = json.JSONDecoder()

    def skip(start):
        while start < len(raw) and raw[start].isspace():
            start += 1
        return start

    def locate(start, path):
        start = skip(start)
        value, end = decoder.raw_decode(raw, start)
        if not path:
            return raw[start:end]
        key, *rest = path
        if isinstance(value, dict) and isinstance(key, str):
            cursor = skip(start + 1)
            while raw[cursor] != "}":
                member, cursor = decoder.raw_decode(raw, cursor)
                cursor = skip(cursor)
                runner.require(raw[cursor] == ":", "Malformed JSON object")
                cursor = skip(cursor + 1)
                if member == key:
                    return locate(cursor, rest)
                _, cursor = decoder.raw_decode(raw, cursor)
                cursor = skip(cursor)
                if raw[cursor] == ",":
                    cursor = skip(cursor + 1)
        elif isinstance(value, list) and isinstance(key, int) and 0 <= key < len(value):
            cursor = skip(start + 1)
            for _ in range(key):
                _, cursor = decoder.raw_decode(raw, cursor)
                cursor = skip(cursor)
                runner.require(raw[cursor] == ",", "Malformed JSON array")
                cursor = skip(cursor + 1)
            return locate(cursor, rest)
        raise ValueError(f"Missing JSON excerpt path: {pointer}")

    result = locate(0, pointer)
    runner.require(json.loads(result) == runner.get_node(json.loads(raw), pointer), "Wrong excerpt")
    return result


def gap(
    field,
    ingredient,
    explanation,
    *,
    old=None,
    reference=None,
    snippet=None,
    locator=None,
):
    return {
        "pointer": None,
        "field": field,
        "ingredient": ingredient,
        "old": old,
        "new": None,
        "status": "unsupported",
        "reference": reference,
        "snippet": snippet,
        "locator": locator,
        "explanation": explanation,
    }


def collect_claims(doc):
    claims = runner.all_claims(doc)

    def stocks(node, pointer):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "solutions":
                    for index, stock in enumerate(value):
                        path = pointer + [key, index]
                        if "concentration" not in stock:
                            claim = gap(
                                runner.field_name(path + ["concentration"]),
                                stock.get("preferred_term", "working stock dose"),
                                "Working stock dose is missing; unasserted candidates cannot establish an amount.",
                            )
                            claim["pointer"] = path
                            claims.append(claim)
                        if stock.get("concentration_candidates"):
                            claims.append(
                                gap(
                                    runner.field_name(path + ["concentration_candidates"]),
                                    stock.get("preferred_term", "working stock dose"),
                                    "Existing candidates are proposals, not verified quantities; no promotion from other media or typical values.",
                                    old=copy.deepcopy(stock["concentration_candidates"]),
                                )
                            )
                if key not in {"evidence", "references", "curation_history"}:
                    stocks(value, pointer + [key])
        elif isinstance(node, list):
            for index, value in enumerate(node):
                stocks(value, pointer + [index])

    stocks(doc, [])
    for key in ("variants", "variant_children", "parent_media"):
        value = doc.get(key)
        if not value:
            continue
        entries = value if isinstance(value, list) else [value]
        for index, item in enumerate(entries):
            claims.append(
                gap(
                    f"{key}[{index}]" if isinstance(value, list) else key,
                    (
                        item.get("name", "variant relationship")
                        if isinstance(item, dict)
                        else "variant relationship"
                    ),
                    "Variant formulation/relationship requires its own exact source; parent evidence is not propagated.",
                    old=copy.deepcopy(item),
                )
            )
    return claims


def identity_problem(doc, data):
    medium = data["medium"]
    mid = str(medium["id"])
    if (
        doc.get("media_term", {}).get("term")
        != {"id": f"mediadive.medium:{mid}", "label": medium["name"]}
        or doc.get("original_name") != medium["name"]
    ):
        return "Exact medium accession/name mismatch; no name-based substitution."
    # Establish the collection and original recipe link independently of the title.
    context = json.dumps({k: doc.get(k) for k in ("notes", "references", "curation_history")})
    collection = medium.get("source")
    if collection not in {"DSMZ", "JCM"} or not medium.get("link") or medium["link"] not in context:
        return "Original collection/link is not established in this record; separate source review required."
    if collection == "JCM":
        try:
            link = urlsplit(medium["link"])
            valid_link = (
                re.fullmatch(r"J[1-9]\d*", mid)
                and link.scheme == "https"
                and link.netloc == "www.jcm.riken.jp"
                and link.path == "/cgi-bin/jcm/jcm_grmd"
                and not link.fragment
                and parse_qs(link.query, keep_blank_values=True, strict_parsing=True)
                == {"GRMD": [mid[1:]]}
            )
        except ValueError:
            valid_link = False
        if not valid_link:
            return "JCM accession does not match its official recipe endpoint; collection-specific source review required."
    return formulation_problem(doc, data)


def formulation_problem(doc, data):
    """Shared formulation checks after collection-specific source identity is established."""
    mid = str(data["medium"]["id"])
    solutions = data["solutions"]
    if not solutions or solutions[0].get("name") != f"Main sol. {mid}":
        return (
            "Unresolved main-solution identity; do not treat the first named stock as the medium."
        )
    if (
        len(solutions) != 1
        or doc.get("solutions")
        or any(r.get("solution_id") is not None for r in solutions[0].get("recipe", []))
    ):
        return "Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values."
    main = solutions[0]
    if not isinstance(main.get("recipe"), list) or not isinstance(main.get("steps"), list):
        return "Missing source ingredient/preparation inventory."
    preparation = " ".join(
        step["step"]
        for step in main["steps"]
        if isinstance(step, dict) and isinstance(step.get("step"), str)
    )
    if re.search(
        r"\bas\s+energy\s+source\s+add\s+either\b|\bdo\s+not\s+combine\s+both\b|"
        r"\bfor\s+\S+\s+add\s+instead\s+of\b",
        preparation,
        re.I,
    ):
        return (
            "Mutually exclusive ingredient branches require variant-specific source review; "
            "the combined source table cannot support one main-medium formulation."
        )
    if re.search(
        r"\b(?:add|mix)\s+\d+(?:\.\d+)?\s*ml\s+(?:of\s+)?stock\s+solution\s+"
        r"(?:per|to|with)\s+\d+(?:\.\d+)?\s*ml\s+(?:of\s+)?(?:basal\s+)?medium\b",
        preparation,
        re.I,
    ):
        return (
            "Explicit stock-to-medium mixing ratio requires preparation-stage review; "
            "table concentrations cannot automatically establish both base and complete-medium amounts."
        )
    if doc.get("physical_state") == "SOLID_AGAR" and re.search(
        r"\bfor\s+agar\s+media\s*,?\s*do\s+not\s+add\b|"
        r"\bagar\s*(?:\([^)]*\)\s*)?medium\s+should\s+be\s+prepared\s+without\b",
        preparation,
        re.I,
    ):
        return (
            "Agar-specific ingredient omission or replacement requires formulation review; "
            "liquid-table amounts cannot automatically support the solid medium."
        )
    if re.search(
        r"\b\d+(?:\.\d+)?\s*ml\s*/\s*l\s+\d+(?:\.\d+)?\s*M\b",
        preparation,
        re.I,
    ):
        return (
            "Molar-stock doses in preparation text require stock and volume-basis review; "
            "the main table alone does not establish complete-medium concentrations."
        )
    rows = main["recipe"]
    if any(r.get("compound_id") is None or not r.get("compound") for r in rows):
        return "Unresolved compound-versus-stock source row."
    labels = [r["compound"] for r in rows]
    local = [n["preferred_term"] for n in doc.get("ingredients", [])]
    if len(labels) != len(set(labels)) or len(local) != len(set(local)):
        return "Duplicate ingredient labels require row-specific identity review."
    missing = set(local) - set(labels)
    for row in rows:
        if row["compound"] in local:
            continue
        water = row["compound_id"] == 4 and row["compound"] == "Distilled water"
        alternate = row.get("optional") == 1 or (
            row.get("condition") == "for solid medium" and doc.get("physical_state") == "LIQUID"
        )
        if not water and not alternate:
            missing.add(row["compound"])
    if missing:
        return (
            "Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): "
            + ", ".join(sorted(missing))
        )
    # A branded mixture can share an erroneous local ID with a pure ingredient.
    # Restrict this warning to rows otherwise eligible for unconditional support.
    unconditional = {
        row["compound"]
        for row in rows
        if row.get("optional") == 0 and not row.get("attribute") and not row.get("condition")
    }
    terms = [
        node["term"]["id"]
        for node in doc.get("ingredients", [])
        if node["preferred_term"] in unconditional and node.get("term", {}).get("id")
    ]
    if len(terms) != len(set(terms)):
        return (
            "Multiple unconditional ingredient rows share a local chemical identifier; "
            "resolve possible aliases or grounding errors before supporting a combined amount."
        )
    return None


def decide(doc, main, row, node):
    old = node.get("concentration")
    preparation = " ".join(step.get("step", "") for step in main.get("steps", []))
    if re.search(r"\b(?:soil|manure)\b", row["compound"], re.I) and re.search(
        r"supernatant|decant|cheesecloth|through (?:filter )?paper|centrifug",
        preparation,
        re.I,
    ):
        return (
            None,
            "unsupported",
            "Extraction input and recovered medium are different preparation stages. "
            "Source g_l alone cannot establish retained solids or extract yield; "
            "explicit input-loading evidence and stock-boundary review are required.",
        )
    if row.get("optional") != 0 or row.get("attribute"):
        return (
            None,
            "unsupported",
            "Optional addition or source attribute needs separate formulation/stock-strength review.",
        )
    condition = row.get("condition")
    if condition and not (
        condition == "for solid medium" and doc.get("physical_state") == "SOLID_AGAR"
    ):
        return (
            None,
            "unsupported",
            "Conditional source row is not established for this physical state/formulation.",
        )
    if node.get("modifier") or node.get("culturemech_term"):
        return (
            None,
            "unsupported",
            "Local variant/base-medium context requires separate review.",
        )
    notes = (node.get("notes") or "").strip()
    if notes and notes not in {condition, f"({condition})" if condition else ""}:
        return (
            None,
            "unsupported",
            "Local ingredient preparation notes need reconciliation before attaching concentration support.",
        )
    try:
        amount = runner.number(row.get("amount"))
        volume = runner.number(main.get("volume"))
        runner.require(
            amount > 0 and volume > 0,
            "Zero/unquantified amount or missing positive provider volume",
        )
        if old is not None:
            runner.require(
                set(old) == {"value", "unit"},
                "Existing denominator/quantity metadata requires review",
            )
        unit = row.get("unit")
        if unit in runner.MASS:
            computed = amount * runner.MASS[unit] / (volume / 1000)
            calculation = f"{amount} {unit} * {runner.MASS[unit]} g/{unit} / ({volume} ml / 1000 ml per L) = {computed} g/L"
        elif unit in SOURCE_RATES:
            computed = amount * SOURCE_RATES[unit]
            calculation = f"{amount} {unit} * {SOURCE_RATES[unit]} = {computed} g/L; the source already gives a rate, so it is not divided by volume again"
        else:
            return (
                None,
                "unsupported",
                "Liquid dose, percent basis, molar conversion, or other unit needs source-specific review; no water-based final volume is inferred.",
            )
        reported = runner.number(row.get("g_l"))
        if not runner.rounded_equal(computed, reported):
            return (
                None,
                "conflict",
                "Source g_l disagrees with its amount/unit/provider-volume arithmetic.",
            )
        new = {"value": str(row["g_l"]), "unit": "G_PER_L"}
        if old is not None:
            factor = MASS_CONCENTRATIONS.get(old["unit"])
            if factor is None or runner.number(old["value"]) * factor != reported:
                return (
                    None,
                    "conflict",
                    "Existing concentration conflicts with the source; preserved pending source-specific correction.",
                )
            new = copy.deepcopy(old)
        explanation = (
            f"Provider explicitly reports g_l={row['g_l']}; check: {calculation}. "
            "This supports the provider-declared main-recipe concentration, not an independently measured final volume, "
            "a stock composition, or a downstream assay dilution. Water alone does not establish final volume. "
            "Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence."
        )
        if condition:
            explanation += (
                f" Source condition {condition!r} matches local physical_state=SOLID_AGAR."
            )
        return new, "add" if old is None else "evidence_only", explanation
    except (ValueError, ArithmeticError, KeyError, TypeError) as exc:
        return None, "unsupported", str(exc)


def withheld_claims(doc, raw, meta, decisions):
    """Validate source-pinned manual vetoes; they can never authorize a value."""
    result = {}
    fields = {c["field"] for c in collect_claims(doc) if c["pointer"] is not None}
    mid = str(json.loads(raw)["data"]["medium"]["id"])
    keys = {
        "id",
        "medium_id",
        "fields",
        "reference",
        "source_sha256",
        "source_pointer",
        "snippet",
        "reason",
    }
    for decision in decisions:
        runner.require(
            isinstance(decision, dict) and set(decision) == keys,
            "Invalid withholding keys",
        )
        if decision["id"] != doc["id"]:
            continue
        runner.require(decision["medium_id"] == mid, "Withholding medium mismatch")
        runner.require(decision["reference"] == API + mid, "Withholding source reference mismatch")
        runner.require(
            decision["source_sha256"] == meta["sha256"] == runner.sha(raw.encode()),
            "Withholding source hash mismatch",
        )
        pointer = decision["source_pointer"]
        runner.require(
            isinstance(pointer, list)
            and bool(pointer)
            and all(type(k) in (str, int) and (not isinstance(k, int) or k >= 0) for k in pointer),
            "Invalid withholding source pointer",
        )
        fragment = json_excerpt(raw, pointer)
        value = json.loads(fragment)
        snippet = decision["snippet"]
        runner.require(
            isinstance(snippet, str)
            and bool(snippet.strip())
            and (snippet in value if isinstance(value, str) else snippet == fragment),
            "Withholding snippet does not match its source locator",
        )
        runner.require(
            isinstance(decision["reason"], str) and bool(decision["reason"].strip()),
            "Missing withholding reason",
        )
        selected = decision["fields"]
        runner.require(
            isinstance(selected, list)
            and bool(selected)
            and all(isinstance(f, str) for f in selected)
            and len(selected) == len(set(selected)),
            "Invalid withholding fields",
        )
        selected = fields if selected == ["*"] else set(selected)
        runner.require(bool(selected) and selected <= fields, "Unknown withholding field")
        runner.require(not result.keys() & selected, "Overlapping withholdings")
        result.update(dict.fromkeys(selected, decision))
    return result


def check_withholdings(root, records, cache, decisions, successors=()):
    runner.require(isinstance(decisions, list), "Withholdings must be a list")
    for decision in decisions:
        runner.require(isinstance(decision, dict), "Invalid withholding")
        targets = [
            r
            for r in records
            if r["id"] == decision.get("id") and r["medium_id"] == decision.get("medium_id")
        ]
        runner.require(len(targets) == 1, "Withholding must target exactly one selected record")
        item = targets[0]
        raw, meta = read_capture(cache, item["medium_id"])
        chain = runner.followup_chain(item, successors) if successors else []
        historical = chain[0]["before_text"] if chain else (root / item["path"]).read_bytes()
        doc = runner.load_yaml(historical)
        runner.require(doc["id"] == item["id"], "Withholding record ID mismatch")
        withheld_claims(doc, raw, meta, decisions)


def review(doc, raw, meta, timestamp, *, withholdings=(), identity_checker=None, action=None):
    data = json.loads(raw)["data"]
    medium = data["medium"]
    mid = str(medium["id"])
    reference = API + mid
    claims = collect_claims(doc)
    withheld = withheld_claims(doc, raw, meta, withholdings)
    after = copy.deepcopy(doc)
    reason = (identity_checker or identity_problem)(doc, data)
    rows = data["solutions"][0].get("recipe", []) if data["solutions"] else []
    by_label = {row.get("compound"): (i, row) for i, row in enumerate(rows)}
    matched = set()
    for claim in claims:
        pointer = claim["pointer"]
        if pointer is None:
            continue
        if claim["field"] in withheld:
            decision = withheld[claim["field"]]
            claim.update(
                status="conflict",
                new=None,
                reference=decision["reference"],
                snippet=decision["snippet"],
                locator="$." + runner.field_name(decision["source_pointer"]),
                explanation="Manual source review withheld support: " + decision["reason"],
            )
            continue
        if reason:
            claim.update(status="conflict", reference=reference, explanation=reason)
            continue
        if len(pointer) != 2 or pointer[0] != "ingredients":
            claim["explanation"] = (
                "Nested, stock-dose, or variant concentration needs its own formulation context."
            )
            continue
        node = runner.get_node(after, pointer)
        index, row = by_label[node["preferred_term"]]
        source_pointer = ["data", "solutions", 0, "recipe", index]
        snippet = json_excerpt(raw, source_pointer)
        locator = "$." + runner.field_name(source_pointer)
        claim.update(reference=reference, snippet=snippet, locator=locator)
        matched.add((0, index))
        tid = node.get("term", {}).get("id", "")
        if (
            tid.startswith("mediadive.compound:")
            and tid != f"mediadive.compound:{row['compound_id']}"
        ):
            claim.update(
                status="conflict",
                explanation="Source compound ID disagrees with local upstream ID.",
            )
            continue
        if any(e.get("reference") == reference for e in node.get("evidence", [])):
            claim["explanation"] = (
                "Existing same-source evidence retained; reconcile its scope without duplicating or replacing it."
            )
            continue
        proposed, status, explanation = decide(doc, data["solutions"][0], row, node)
        claim.update(new=proposed, status=status, explanation=explanation)
        if proposed is None:
            continue
        volume_quote = json_excerpt(raw, ["data", "solutions", 0, "volume"])
        explanation += (
            f" Additional exact value at $.data.solutions[0].volume (ml): {volume_quote}."
        )
        claim["explanation"] = explanation
        node["concentration"] = proposed
        node.setdefault("evidence", []).append(
            {
                "reference": reference,
                "supports": "SUPPORT",
                "snippet": snippet,
                "explanation": f"Concentration evidence for {claim['field']} ({node['preferred_term']}) in MediaDive medium {mid}; "
                f"locator={locator}. {explanation} Retrieved {meta['accessed_at']}; response SHA256={meta['sha256']}.",
            }
        )
    for si, solution in enumerate(data["solutions"]):
        for ri, row in enumerate(solution.get("recipe", [])):
            if (si, ri) in matched:
                continue
            pointer = ["data", "solutions", si, "recipe", ri]
            claims.append(
                gap(
                    "source." + runner.field_name(pointer),
                    row.get("compound") or row.get("solution") or "unresolved source row",
                    "Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded.",
                    reference=reference,
                    snippet=json_excerpt(raw, pointer),
                    locator="$." + runner.field_name(pointer),
                )
            )
        for pi, _step in enumerate(solution.get("steps", [])):
            pointer = ["data", "solutions", si, "steps", pi]
            claims.append(
                gap(
                    "source." + runner.field_name(pointer),
                    "preparation context",
                    "Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose.",
                    reference=reference,
                    snippet=json_excerpt(raw, pointer),
                    locator="$." + runner.field_name(pointer),
                )
            )
    changed = [c for c in claims if c["status"] in runner.SUPPORTED]
    if changed:
        refs = after.setdefault("references", [])
        if not any(r["reference"] == reference for r in refs):
            refs.append(
                {
                    "reference": reference,
                    "title": f"MediaDive medium {mid}: {medium['name']}",
                    "notes": f"source_type=dataset; discovery_mode=existing_record_reference; source_organization=DSMZ; "
                    f"accessed_on={meta['accessed_at'][:10]}; locator=$.data.solutions[0]; response_sha256={meta['sha256']}; "
                    f"original_recipe={medium['link']}; individual authors and publication year not supplied. Provider-declared main-recipe amounts only.",
                }
            )
            if medium["source"] == "JCM":
                refs[-1]["notes"] += (
                    f" Original recipe collection=JCM; GRMD accession={mid[1:]}; "
                    "DSMZ is the MediaDive dataset provider, not the original recipe collection."
                )
        record_curation_event(
            after,
            curator="codex",
            action=action or ACTION,
            source=reference,
            timestamp=timestamp,
            notes="Exact medium/source membership, ingredient inventory/forms, physical-state conditions, literal snippets, and arithmetic checked. "
            "Stock boundaries, source-only rows, preparation context, and variants remain explicit follow-up tasks; secondary chemical mappings unchanged.",
            changes="; ".join(
                f"{c['field']}: {json.dumps(c['old'], sort_keys=True)} -> {json.dumps(c['new'], sort_keys=True)} ({c['status']})"
                for c in changed
            ),
        )
    return after, claims


def adapter(withholdings=()):
    return runner.ReviewAdapter(
        "medium_id",
        "MediaRecipe",
        read_capture,
        partial(review, withholdings=withholdings),
        collect_claims,
        ("solutions", "variants", "variant_children"),
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    parser.add_argument(
        "--withholdings",
        type=Path,
        help="Source-pinned manual vetoes; preview only, frozen into the plan",
    )
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
        not args.withholdings or not (args.apply or args.verify),
        "Withholdings are preview-only; apply/verify use the frozen plan",
    )
    runner.require(
        not args.followup_plan or (args.verify and not args.reports),
        "Follow-ups require verification without report rewriting",
    )
    successors = [r for p in args.followup_plan for r in json.loads(p.read_text())["records"]]
    if args.apply or args.verify:
        plan = json.loads(args.plan.read_text())
        decisions = plan.get("withholdings", [])
        check_withholdings(ROOT, plan["records"], args.cache, decisions, successors)
        outcome = (
            runner.apply(ROOT, plan, args.cache, adapter=adapter(decisions))
            if args.apply
            else runner.verify(ROOT, plan, args.cache, successors, adapter=adapter(decisions))
        )
    else:
        runner.require(
            args.inventory is not None and not args.plan.exists(),
            "Preview requires inventory and a new plan path",
        )
        manifest = json.loads(args.inventory.read_text())
        selected = select(manifest, args.offset, args.limit)
        decisions = json.loads(args.withholdings.read_text()) if args.withholdings else []
        check_withholdings(ROOT, selected, args.cache, decisions)
        plan = runner.preview(
            ROOT,
            selected,
            args.cache,
            manifest["commit"],
            adapter=adapter(decisions),
        )
        if decisions:
            plan["withholdings"] = decisions
        args.plan.parent.mkdir(parents=True, exist_ok=True)
        args.plan.write_text(json.dumps(plan, indent=2) + "\n")
        outcome = {}
    if args.reports:
        runner.reports(
            args.reports,
            plan,
            args.apply or args.verify,
            source_api=API,
            source_id_key="medium_id",
            title="Medium",
        )
    print(json.dumps({**runner.summary(plan), **outcome}), flush=True)
    return 1 if runner.summary(plan)["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
