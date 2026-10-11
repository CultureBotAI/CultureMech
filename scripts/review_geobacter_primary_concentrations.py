"""Guarded primary-source curation of the 56 MediaDB freshwater variants."""

import argparse
import collections
import copy
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner

from culturemech.curate.curation_event import now_iso, record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-geobacter-primary"
PLAN = HERE / "plan-v2.json"
SOURCE_SHA = "321fcc92d528810d137f4bd0c83b97506ab5012562ebdf6821332dd9660b292b"
ACTION = "CURATED_GEOBACTER_PRIMARY_BASAL_INPUTS_AND_DONOR_EVIDENCE"
KEYS = {str(n) for n in range(416, 472)}
LIMITS = [
    "Only the stated basal inputs, routine acetate input, acetate salt identity, exact "
    "single-valued donor amounts and autoclaving are curated. The full formulations "
    "are not certified. The four acetate endpoint quantities remain unsupported.",
    "Calcium combines basal and possible trace-stock contributions; acceptor-dependent "
    "omissions require stage-specific reconstruction, not wholesale deletion.",
    "Trace/vitamin final doses, hydrate mismatches, cobalt-source variants, iron basis, "
    "citrate stoichiometry and database-selected range endpoints remain unresolved.",
    "No organism-growth assertions, new records, classifications or variant links are changed. "
    "Historical database names and evidence are retained as source provenance.",
]
VITAMINS = {
    "Nicotinate",
    "Lipoate",
    "4-Aminobenzoate",
    "Vitamin B12",
    "Thiamine HCl",
    "Riboflavin",
    "Folate",
    "Calcium pantothenate",
    "Biotin",
    "Pyridoxine HCl",
}
TRACES = {
    "Zinc sulfate",
    "Cupric sulfate",
    "Nitrilotriacetic acid",
    "Sodium chloride",
    "Sodium molybdate",
    "Magnesium sulfate",
    "Ferrous sulfate",
    "Manganese sulfate",
    "Aluminum potassium sulfate",
    "Boric acid",
    "Cobaltous sulfate",
    "Cobalt chloride",
    "Nickel chloride",
}


def sources():
    raw = (HERE / "source-review.json").read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Source review changed"
    source = json.loads(raw)
    records = {r["key"]: r for r in source["records"]}
    assert set(records) == KEYS and len(source["records"]) == 56
    return source, records


def bibliography(source, base=False):
    item = source["base" if base else "primary"]
    result = {k: item[k] for k in ("reference", "title", "authors", "year")}
    result["notes"] = (
        "source_type=journal_article; discovery_mode=cross_reference; "
        f"accessed_on={source['accessed_on']}; "
        + (
            f"{item['doi']}; locator={item['locator']}; visually inspected PMC scan. "
            "Used only for the sodium-acetate chemical form in the explicit 1993 methods "
            "cross-reference, not for importing its different iron dose or other conditions."
            if base
            else f"PMID:{item['pmid']}; inspected scan={item['url']}; "
            "locators=printed pages 337 and 339, Methods and Table 2; "
            f"pdf_sha256={source['capture_sha256']['Geobacter1993.pdf']}. "
            "Partial ingredient/preparation support, not approval of every database variant."
        )
    )
    return result


def proof(
    source, record, index, snippet, explanation, *, base=False, locator=None, field="concentration"
):
    item = source["base" if base else "primary"]
    return {
        "reference": item["reference"],
        "supports": "SUPPORT",
        "snippet": snippet,
        "explanation": f"ingredients[{index}].{field} in {record['source_term']}. "
        f"Locator: {locator or source['basal_locator']}. {explanation} "
        f"{source['transcription']} Inspected {source['accessed_on']}. "
        "This does not certify other ingredient quantities, the entire cobalt variant, "
        "or organism growth. Earlier database evidence remains historical database support.",
    }


def ingredient_review(node, index, source, record):
    new = copy.deepcopy(node)
    name = node["preferred_term"]
    quantity = node["concentration"]
    assert set(quantity) == {"value", "unit"} and quantity["unit"] == "MILLIMOLAR"
    evidence, status, reason = [], "unsupported", ""
    if name in source["basal"]:
        row = source["basal"][name]
        assert Decimal(quantity["value"]) == Decimal(row["old_millimolar"])
        new["concentration"] = {"value": row["g_per_l"], "unit": "G_PER_L"}
        if "new_label" in row:
            new["preferred_term"] = row["new_label"]
            for field in ("term", "mediaingredientmech_chebi_term"):
                if field in node:
                    new[field] = copy.deepcopy(source["terms"][row["new_label"]])
        status = "correct"
        reason = (
            f"Restore the directly reported {row['g_per_l']} g/L input under the separate "
            f"heading '{source['basal_basis_snippet']}'. No molecular-weight conversion or "
            "new final-volume assumption. The phosphate is explicitly the monohydrate; "
            "unchanged salt identities are not broadened."
        )
        evidence.append(proof(source, record, index, row["snippet"], reason))
    elif name == "Acetate":
        assert Decimal(quantity["value"]) in {Decimal("113.2"), Decimal("10"), Decimal("50")}
        new["preferred_term"] = "Sodium acetate"
        for field in ("term", "mediaingredientmech_chebi_term"):
            if field in node:
                new[field] = copy.deepcopy(source["terms"]["Na-acetate"])
        routine = Decimal(quantity["value"]) == Decimal("113.2")
        if routine:
            new["concentration"] = {"value": "6.8", "unit": "G_PER_L"}
            status = "correct"
        reason = (
            "Replace the database's 113.2 mM by the 1993 routine carbon input, 6.8 g/L. "
            if routine
            else "Correct only the supplied acetate salt identity, not its concentration. "
            "Table 2 reports acetate at 10-50 mM, not a separately specified recipe for "
            "this database-selected endpoint. The existing endpoint quantity remains "
            "unsupported and unchanged; these identity snippets do not verify it. "
        ) + (
            "The sodium salt follows the explicitly cited 1988 FWA-Fe(III) basal recipe, "
            "which prints NaCH3COO. This chemical-form inference applies to the acetate "
            "input of that basal formulation, separately from its amount. The 1993 "
            "Methods cites the 1988 procedure; its donor table varies acetate amount "
            "without specifying a different supplied salt. Hydration/purity is not "
            "established; no new molarity or molecular weight is asserted. The original "
            "database name is historical provenance."
        )
        field = (
            "concentration"
            if routine
            else "term, preferred_term and mediaingredientmech_chebi_term"
        )
        snippet = (
            source["acetate_snippet"]
            if routine
            else ("as previously described (Lovley and Phillips 1988 b).")
        )
        evidence.append(proof(source, record, index, snippet, reason, field=field))
        evidence.append(
            proof(
                source,
                record,
                index,
                source["base"]["acetate_snippet"],
                reason
                + f" The older paragraph's separate unit heading is '{source['base']['basis_snippet']}'.",
                base=True,
                locator=source["base"]["locator"],
                field="term, preferred_term and mediaingredientmech_chebi_term",
            )
        )
    elif name in source["donors"]:
        amount, snippet = source["donors"][name]
        assert Decimal(quantity["value"]) == Decimal(amount)
        assert any(
            n["preferred_term"] == "Ferric oxide"
            for n in runner.load_yaml(record["before_text"])["ingredients"]
        )
        status = "evidence_only"
        reason = (
            f"Table 2 directly gives the nominal donor amount {amount} mM, equal to "
            f"the existing {quantity['value']} MILLIMOLAR; no conversion. Table context "
            "is poorly crystalline Fe(III) oxide. This amount evidence does not independently "
            "certify the pre-existing ionization, supplied salt, stereochemistry or ontology ID."
        )
        evidence.append(
            proof(source, record, index, snippet, reason, locator=source["donor_locator"])
        )
    elif name in VITAMINS or name in TRACES:
        status = "conflict" if name == "Cobaltous sulfate" else "unsupported"
        reason = (
            "Stock recipe and final-medium dilution are separate claims. The 1993 to 1988 "
            "to 1984 to 1979 source chain was inspected, but this exact final dose, supplied "
            "chemical form and preparation boundary are not established for this variant. "
            "Do not import 1% from another medium without an explicit applicability decision. "
            "The 1984 molybdate/nickel modifications supersede the older stock amounts. "
            "The inspected stock names cobalt chloride hexahydrate, not cobalt sulfate. "
            "Keep existing data and earlier database evidence unchanged pending reconstruction."
        )
    elif name == "Calcium chloride anhydrous":
        status = "conflict"
        reason = (
            "The source names calcium chloride dihydrate in the basal recipe and omits "
            "that basal input for specified nitrate/citrate conditions. The trace stock "
            "also contains calcium. Reconstruct both contributions and source scope before "
            "replacing 0.687 mM or deleting this combined node."
        )
    elif name == "Ferric oxide":
        status = "conflict"
        reason = (
            "The source describes approximate poorly crystalline Fe(III) oxide and a "
            "100-250 mmol/L range. Iron-atom basis is not interchangeable with pure Fe2O3 "
            "formula-unit molarity. Citrate conditions also require an omission decision."
        )
    elif name == "Fe(III)dicitrate":
        status = "conflict"
        reason = (
            "Methods specifies Fe(III)-citrate at 50 mM, while Table 1 gives 20-50 mmol/L. "
            "The database's dicitrate stoichiometry and exact range-endpoint formulation "
            "are not established; retain pending chemical/condition reconciliation."
        )
    elif name in {"Toluene", "Nitrate"}:
        reason = (
            "The primary table reports a range, whereas this database record selects an "
            "endpoint. Preserve the distinct database condition without treating range "
            "membership as proof of its exact recipe or collapsing both variants into one."
        )
    elif name == "Manganese(IV) oxide":
        reason = (
            "Table 1 gives 15 mmol/L Mn(IV) oxide (birnessite); its nominal metal amount, "
            "material composition, and the receiving-medium omissions need explicit "
            "reconciliation before certifying this encoded formula-unit concentration."
        )
    else:
        raise AssertionError(f"Unreviewed ingredient: {name}")
    if evidence:
        old_refs = {e["reference"] for e in node.get("evidence", [])}
        assert not old_refs.intersection(e["reference"] for e in evidence)
        new.setdefault("evidence", []).extend(evidence)
    claim = {
        "pointer": ["ingredients", index, "concentration"],
        "ingredient": name,
        "identity": node.get("term"),
        "old": quantity,
        "proposed": new["concentration"],
        "proposed_identity": new.get("term"),
        "proposed_ingredient": new["preferred_term"],
        "status": status,
        "identity_status": "correct" if node.get("term") != new.get("term") else "unchanged",
        "evidence": evidence,
        "explanation": reason,
        "action": (
            "Retain unsupported quantity; correct chemical form only"
            if name == "Acetate" and status == "unsupported"
            else "Apply supported claim" if evidence else "Retain unresolved claim unchanged"
        ),
    }
    return new, claim


def preparation_proof(source, record):
    return {
        "reference": source["primary"]["reference"],
        "supports": "SUPPORT",
        "snippet": source["preparation_snippet"],
        "explanation": f"preparation_steps[2] in {record['source_term']}; "
        f"{source['preparation_locator']}. Replace the imported 0.22 micrometer filtration "
        "instruction by the directly stated autoclaving of the medium. Temperature, "
        "duration and pressure are not specified here and are not invented. "
        f"{source['transcription']} This is not a complete preparation or growth review.",
    }


def transform(before, source, record, timestamp):
    after = copy.deepcopy(before)
    assert not before.get("solutions") and not before.get("composition")
    claims = []
    for index, node in enumerate(before["ingredients"]):
        new, claim = ingredient_review(node, index, source, record)
        after["ingredients"][index] = new
        claims.append(claim)
    old_step = before["preparation_steps"][2]
    assert old_step["action"] == "FILTER_STERILIZE" and old_step["step_number"] == 3
    after["preparation_steps"][2] = {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Sterilize the medium by autoclaving; the cited Methods does not specify a temperature or duration.",
    }
    root_proof = preparation_proof(source, record)
    assert root_proof["reference"] not in {e["reference"] for e in before.get("evidence", [])}
    after.setdefault("evidence", []).append(root_proof)
    for reference in [bibliography(source)] + (
        [bibliography(source, True)] if any(c["ingredient"] == "Acetate" for c in claims) else []
    ):
        assert reference["reference"] not in {r["reference"] for r in before.get("references", [])}
        after.setdefault("references", []).append(reference)
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        source=source["primary"]["reference"],
        timestamp=timestamp,
        notes=" ".join(LIMITS),
        changes=json.dumps(
            {
                "ingredient_changes": [
                    {
                        k: c[k]
                        for k in (
                            "pointer",
                            "ingredient",
                            "old",
                            "proposed",
                            "proposed_ingredient",
                            "status",
                            "identity_status",
                            "identity",
                            "proposed_identity",
                        )
                    }
                    for c in claims
                    if c["evidence"]
                ],
                "sterilization": {"old": old_step, "new": after["preparation_steps"][2]},
            },
            sort_keys=True,
        ),
    )
    return after, claims


def check(before, after, item):
    source, records = sources()
    record = records[item["key"]]
    assert item["action"] == ACTION and item["target_class"] == "MediaRecipe"
    assert item["path"] == record["path"] and item["unresolved"] == LIMITS
    assert item["id"] == before["id"] == after["id"] == record["id"]
    assert item["before_text"] == record["before_text"]
    assert (
        runner.sha(item["before_text"].encode()) == item["before_sha256"] == record["before_sha256"]
    )
    assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
    assert before == runner.load_yaml(item["before_text"])
    assert after == runner.load_yaml(item["after_text"])
    assert before["media_term"]["term"]["id"] == record["source_term"]
    expected, claims = transform(before, source, record, after["curation_history"][-1]["timestamp"])
    assert item["claims"] == claims and after == expected, "Unreviewed semantic change"
    counts = collections.Counter(
        new_evidence=sum(len(c["evidence"]) for c in claims) + 1,
        new_references=len(after["references"]) - len(before.get("references", [])),
        new_curation_history=1,
        preparation_actions_corrected=1,
        preparation_descriptions_corrected=1,
        quantity_corrections=sum(c["old"] != c["proposed"] for c in claims),
        supplied_hydrate_identities_corrected=1,
    )
    if any(c["ingredient"] == "Acetate" for c in claims):
        counts["ingredient_labels_corrected"] = 1
    return counts


def preview(root=ROOT):
    source, records = sources()
    plan = {
        "version": 1,
        "action": ACTION,
        "source_sha256": SOURCE_SHA,
        "created_at": now_iso(),
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip(),
        "records": [],
    }
    for key, record in records.items():
        raw = (root / record["path"]).read_bytes()
        assert runner.sha(raw) == record["before_sha256"], "Record drift"
        before = runner.load_yaml(raw)
        assert not validate_recipe(before, target_class="MediaRecipe")
        after, claims = transform(before, source, record, plan["created_at"])
        assert not validate_recipe(after, target_class="MediaRecipe")
        output = runner.render(raw.decode(), after)
        assert "&id" not in output.decode() and "*id" not in output.decode()
        item = {
            "key": key,
            "id": record["id"],
            "path": record["path"],
            "target_class": "MediaRecipe",
            "action": ACTION,
            "before_text": raw.decode(),
            "after_text": output.decode(),
            "before_sha256": runner.sha(raw),
            "after_sha256": runner.sha(output),
            "claims": claims,
            "unresolved": LIMITS,
        }
        item["counts"] = dict(check(before, after, item))
        plan["records"].append(item)
    runner.safe_targets(root, plan)
    check_variant_identities(plan)
    return plan


def check_variant_identities(plan):
    """Keep this cohort's existing identical-ingredient relationship claims true."""

    def identity(node):
        return (
            node["preferred_term"],
            node.get("term", {}).get("id"),
            node.get("mediaingredientmech_chebi_term", {}).get("id"),
        )

    docs = {r["path"]: runner.load_yaml(r["after_text"]) for r in plan["records"]}
    checked = []
    for path, parent in docs.items():
        for link in parent.get("variant_children", []):
            assert link["relationship"] == "CONCENTRATION_VARIANT"
            child = docs[link["path"]]
            assert child["id"] == link["id"]
            assert child["parent_media"]["path"] == path
            assert child["parent_media"]["id"] == parent["id"]
            assert child["parent_media"]["relationship"] == "CONCENTRATION_VARIANT"
            identities = [
                collections.Counter(identity(n) for n in doc["ingredients"])
                for doc in (parent, child)
            ]
            assert identities[0] == identities[1], "Variant ingredient identities diverge"
            amounts = [
                {identity(n): n["concentration"] for n in doc["ingredients"]}
                for doc in (parent, child)
            ]
            assert amounts[0] != amounts[1], "Concentration variant amounts are identical"
            checked.append([path, link["path"]])
    assert len(checked) == 10
    return checked


def safe_path(root, path):
    target = root / path
    parts = Path(path).parts
    assert target.resolve().is_relative_to(root / "data/normalized_yaml")
    assert not any(root.joinpath(*parts[:i]).is_symlink() for i in range(1, len(parts) + 1))
    return target


def apply(plan, root=ROOT, *, verify=False):
    root = root.resolve()
    assert plan["action"] == ACTION and plan["source_sha256"] == SOURCE_SHA
    assert len(plan["records"]) == 56 and {r["key"] for r in plan["records"]} == KEYS
    runner.safe_targets(root, plan)
    check_variant_identities(plan)
    pending = []
    for item in plan["records"]:
        before, after = (runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
        assert dict(check(before, after, item)) == item["counts"]
        assert not validate_recipe(after, target_class="MediaRecipe")
        target = safe_path(root, item["path"])
        raw = target.read_bytes()
        if runner.sha(raw) == item["after_sha256"]:
            continue
        assert not verify and runner.sha(raw) == item["before_sha256"], "Concurrent record edit"
        pending.append((target, raw, item["after_text"].encode()))
    for target, before, _ in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == before, "Concurrent edit during preflight"
    for target, before, after in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == before, "Concurrent edit during write"
        target.write_bytes(after)
        assert target.read_bytes() == after
    return {"changed": len(pending), "already_applied": 56 - len(pending)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=PLAN)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.apply or args.verify:
        print(json.dumps(apply(json.loads(args.plan.read_text()), verify=args.verify)))
    else:
        assert not args.plan.exists(), "Refuse to overwrite plan"
        plan = preview()
        with args.plan.open("x") as stream:
            json.dump(plan, stream, indent=2)
            stream.write("\n")
        counts = collections.Counter()
        for item in plan["records"]:
            counts.update(item["counts"])
        print(json.dumps({"records_previewed": 56, "records_edited": 0, "proposed": dict(counts)}))


if __name__ == "__main__":
    main()
