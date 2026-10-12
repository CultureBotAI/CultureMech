"""Preview and add primary-source evidence to the twelve modified M63 records."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-m63-primary"
PLAN = HERE / "plan-v3.json"
SOURCE_SHA = "f027ea3d56c3b7f52f0f7519548394436250ab9a69ac1d294419306cfdbba9db"
ACTION = "CURATED_M63_PRIMARY_AMOUNTS_AND_CHEMICAL_FORMS"
KEYS = {str(n) for n in range(4, 16)}
CARBON = {"glucose": "D-Glucose", "ectoine": "Ectoine", "hydroxyectoine": "5-Hydroxyectoine"}
LIMITS = [
    "Five base-medium amounts and three chemical forms follow the 1982 M63 definition "
    "explicitly cited as reference 48 by the 2010 Methods. This cross-reference inference "
    "is distinct from the carbon and salt concentrations directly reported in 2010.",
    "KOH at 75 mM is a base-recipe input, not a quantified pH-adjustment dose. "
    "No fixed titration dose is inferred from the separate 2010 pH 7.2 adjustment.",
    "Existing D-glucose stereochemistry and hydroxyectoine positional naming are preserved, "
    "not independently certified by the amount evidence.",
    "No quantity, preparation, classification, growth association or variant-link changes. "
    "These records are not certified as complete primary-source formulations.",
]


def sources():
    raw = (HERE / "source-review-v2.json").read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Source review drift"
    source = json.loads(raw)
    records = {r["key"]: r for r in source["records"]}
    assert set(records) == KEYS and len(source["records"]) == 12
    return source, records


def bibliography(source):
    return {
        "reference": source["reference"],
        "title": source["title"],
        "authors": "; ".join(source["authors"]),
        "year": source["year"],
        "notes": "source_type=journal_article; discovery_mode=cross_reference; "
        f"accessed_on={source['accessed_on']}; MediaDB original-article lead, PMID:20942908; "
        f"inspected full text={source['url']}; locator=Figure 1 caption and Methods / "
        "Bacterial strains, plasmids and growth conditions; "
        f"raw_html_sha256={source['raw_html_sha256']}. Supports the carbon source and NaCl "
        "concentrations; the five base-medium inputs follow its explicit reference 48.",
    }


def base_bibliography(source):
    base = source["base_source"]
    return {k: base[k] for k in ("reference", "title", "authors", "year")} | {
        "notes": f"source_type=journal_article; discovery_mode=cross_reference; "
        f"accessed_on={base['accessed_on']}; {base['doi']}; "
        f"locator={base['locator']}; inspected scan={base['page_image_url']}; "
        f"image_sha256={base['capture_sha256']['PMC220425-p1433.png']}. "
        f"{base['scope']} {base['transcription']}"
    }


def corrected_node(node, source):
    result = copy.deepcopy(node)
    row = source["base_source"]["rows"].get(node["preferred_term"])
    if row and "term" in row:
        result["preferred_term"] = row["proposed_label"]
        result["term"] = copy.deepcopy(row["term"])
        if "mediaingredientmech_chebi_term" in result:
            result["mediaingredientmech_chebi_term"] = copy.deepcopy(row["term"])
    return result


def base_proof(source, record, index, old):
    base = source["base_source"]
    row = base["rows"][old["preferred_term"]]
    calculation = {
        "Potassium hydroxide": "0.075 mol/L * 1000 mmol/mol = 75 mM",
        "Potassium dibasic phosphate": "0.1 mol/L * 1000 mmol/mol = 100 mM",
        "Magnesium sulfate": "0.16 mM is directly reported; no conversion",
        "Ferrous sulfate": "1.8 micromol/L / 1000 micromol/mmol = 0.0018 mM",
        "Ammonium sulfate": "0.015 mol/L * 1000 mmol/mol = 15 mM",
    }[old["preferred_term"]]
    identity = (
        f"Corrected {old['preferred_term']} ({old['term']['id']}) to "
        f"{row['proposed_label']} ({row['term']['id']}) to match the printed chemical form. "
        if "term" in row
        else "Chemical identity retained. "
    )
    return {
        "reference": base["reference"],
        "supports": "SUPPORT",
        "snippet": row["snippet"],
        "explanation": f"ingredients[{index}].concentration ({row['proposed_label']}) in "
        f"{record['source_term']}. Locator: {base['locator']}. {base['scope']} "
        f"Calculation: {calculation}. Numerical value and MILLIMOLAR unit retained. "
        f"{identity}No mass/molecular-weight conversion. "
        "KOH here is a quantified base-recipe input, not the additional pH-adjustment dose. "
        f"{base['transcription']} Inspected {base['accessed_on']}.",
    }


def proof(source, record, index, node):
    name = node["preferred_term"]
    is_salt = name == "Sodium chloride"
    if name in source["base_source"]["rows"]:
        return base_proof(source, record, index, node)
    assert is_salt or name == CARBON[record["carbon"]]
    if is_salt:
        meaning = (
            f"Panel {record['panel']} is {record['salt_molar']} M NaCl; "
            f"{record['salt_molar']} mol/L * 1000 mmol/mol = "
            f"{node['concentration']['value']} mmol/L (MILLIMOLAR). "
            f"Methods separately states: '{source['excerpts']['salt_basis']}' "
            "This is final-medium concentration, not a stock dose."
        )
    else:
        meaning = (
            f"The {record['carbon']} condition reports 20 mM, equivalent to the existing "
            "20.0 MILLIMOLAR, with no mass or volume conversion. Each named carbon source "
            "is a separate condition, not a mixture of all three. "
            "This verifies the amount for the source's carbon-source name, not the "
            "record's pre-existing stereochemical/positional naming or ontology mapping."
        )
    return {
        "reference": source["reference"],
        "supports": "SUPPORT",
        "snippet": source["excerpts"]["salt" if is_salt else "carbon"],
        "explanation": f"ingredients[{index}].concentration ({name}) in {record['source_term']}, "
        f"modified M63 with {record['carbon']} and {record['salt_molar']} M NaCl. "
        f"Locator: {source['figure_locator']}. {meaning} "
        f"Inspected at {source['url']} on {source['accessed_on']}. "
        "Other base-medium amounts and growth performance are not established by this evidence.",
    }


def claims(before, source, record):
    result = []
    for index, node in enumerate(before["ingredients"]):
        proposed = corrected_node(node, source)
        evidence = proof(source, record, index, node)
        identity_change = proposed != node
        result.append(
            {
                "pointer": ["ingredients", index, "concentration"],
                "ingredient": node["preferred_term"],
                "identity": node.get("term"),
                "proposed_ingredient": proposed["preferred_term"],
                "proposed_identity": proposed.get("term"),
                "old": node["concentration"],
                "proposed": node["concentration"],
                "status": "correct" if identity_change else "evidence_only",
                "evidence": evidence,
                "action": (
                    "Correct chemical form and add evidence; preserve amount"
                    if identity_change
                    else "Add evidence; preserve amount and identity"
                ),
                "basis": "Final-medium molarity; base inputs via explicit recipe cross-reference",
                "calculation": evidence["explanation"],
                "unresolved": LIMITS,
            }
        )
    return result


def transform(before, source, record, timestamp):
    after = copy.deepcopy(before)
    supported = []
    for index, old in enumerate(before["ingredients"]):
        node = corrected_node(old, source)
        evidence = proof(source, record, index, old)
        assert evidence["reference"] not in {e["reference"] for e in node.get("evidence", [])}
        node.setdefault("evidence", []).append(evidence)
        after["ingredients"][index] = node
        supported.append(f"ingredients[{index}].concentration")
    assert len(supported) == 7
    for reference in (bibliography(source), base_bibliography(source)):
        assert reference["reference"] not in {r["reference"] for r in after.get("references", [])}
        after.setdefault("references", []).append(reference)
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=source["reference"],
        changes=json.dumps(
            {
                "evidence_added_to": supported,
                "quantity_changes": 0,
                "chemical_forms_corrected": [
                    {"old": n["preferred_term"], "new": corrected_node(n, source)["preferred_term"]}
                    for n in before["ingredients"]
                    if corrected_node(n, source) != n
                ],
            },
            sort_keys=True,
        ),
        notes="Added primary-source concentration snippets and corrected phosphate/sulfate "
        "chemical forms using the explicitly cited M63 definition. " + " ".join(LIMITS),
    )
    return after


def check(before, after, item):
    """Invert reviewed chemical forms and provenance; reject any quantity change."""
    source, records = sources()
    record = records[item["key"]]
    assert item["action"] == ACTION and item["target_class"] == "MediaRecipe"
    assert item["path"] == record["path"] and item["unresolved"] == LIMITS
    assert item["id"] == before["id"] == after["id"] == record["id"]
    assert (
        runner.sha(item["before_text"].encode()) == item["before_sha256"] == record["before_sha256"]
    )
    assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
    assert before == runner.load_yaml(item["before_text"])
    assert after == runner.load_yaml(item["after_text"])
    assert before["media_term"]["term"]["id"] == record["source_term"]
    assert before["ingredients"] == record["ingredients_before"]
    assert len(before["ingredients"]) == len(after["ingredients"]) == 7
    assert item["claims"] == claims(before, source, record)
    reverted = copy.deepcopy(after)
    corrected = 0
    for index, (old, new) in enumerate(
        zip(before["ingredients"], reverted["ingredients"], strict=True)
    ):
        name = old["preferred_term"]
        row = source["base_source"]["rows"].get(name)
        if row:
            amount = Decimal(row["millimolar"])
        else:
            amount = (
                Decimal(record["salt_molar"]) * 1000 if name == "Sodium chloride" else Decimal(20)
            )
        assert set(old["concentration"]) == {"value", "unit"}
        assert old["concentration"]["unit"] == "MILLIMOLAR"
        assert Decimal(old["concentration"]["value"]) == amount
        assert new.pop("evidence") == old.get("evidence", []) + [proof(source, record, index, old)]
        if "evidence" in old:
            new["evidence"] = old["evidence"]
        if row and "term" in row:
            assert new["preferred_term"] == row["proposed_label"] and new["term"] == row["term"]
            new["preferred_term"], new["term"] = old["preferred_term"], old["term"]
            if "mediaingredientmech_chebi_term" in old:
                assert new["mediaingredientmech_chebi_term"] == row["term"]
                new["mediaingredientmech_chebi_term"] = old["mediaingredientmech_chebi_term"]
            corrected += 1
        assert new == old, (index, "Unreviewed ingredient change")
    assert corrected == 3
    assert reverted.pop("references") == before.get("references", []) + [
        bibliography(source),
        base_bibliography(source),
    ]
    if "references" in before:
        reverted["references"] = before["references"]
    event = reverted["curation_history"].pop()
    assert event == transform(before, source, record, event["timestamp"])["curation_history"][-1]
    assert reverted == before, "Unreviewed root field change"
    return collections.Counter(
        new_evidence=7,
        new_references=2,
        new_curation_history=1,
        supplied_hydrate_identities_corrected=2,
        ingredient_labels_corrected=1,
    )


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
        assert runner.sha(raw) == record["before_sha256"], "Record drift; new review required"
        before = runner.load_yaml(raw)
        assert not validate_recipe(before, target_class="MediaRecipe")
        after = transform(before, source, record, plan["created_at"])
        assert not validate_recipe(after, target_class="MediaRecipe")
        output = runner.render(raw.decode(), after)
        item = {
            "key": key,
            "id": record["id"],
            "path": record["path"],
            "target_class": "MediaRecipe",
            "action": ACTION,
            "before_sha256": runner.sha(raw),
            "after_sha256": runner.sha(output),
            "before_text": raw.decode(),
            "after_text": output.decode(),
            "unresolved": LIMITS,
            "claims": claims(before, source, record),
        }
        item["counts"] = dict(check(before, after, item))
        plan["records"].append(item)
    runner.safe_targets(root, plan)
    return plan


def safe_path(root, path):
    target = root / path
    parts = Path(path).parts
    assert target.resolve().is_relative_to(root / "data/normalized_yaml")
    assert not any(root.joinpath(*parts[:i]).is_symlink() for i in range(1, len(parts) + 1))
    return target


def apply(plan, root=ROOT, *, verify=False):
    root = root.resolve()
    assert plan["action"] == ACTION and plan["source_sha256"] == SOURCE_SHA
    assert len(plan["records"]) == 12 and {r["key"] for r in plan["records"]} == KEYS
    runner.safe_targets(root, plan)
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
    return {"changed": len(pending), "already_applied": 12 - len(pending)}


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
        assert not args.plan.exists(), "Refuse to overwrite preview"
        plan = preview()
        with args.plan.open("x") as stream:
            stream.write(json.dumps(plan, indent=2) + "\n")
        print(
            json.dumps(
                {
                    "reviewed": 12,
                    "records_edited": 0,
                    "approved_evidence": 84,
                    "chemical_form_corrections": 36,
                }
            )
        )


if __name__ == "__main__":
    main()
