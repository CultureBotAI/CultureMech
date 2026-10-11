"""Preview and apply six source-pinned MediaDB ingredient repairs."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-mediadb-exceptions"
PLAN = HERE / "plan.json"
SOURCE_SHA = "a8cb05b4aaefa6beac43990330eca3bed8adf4c264700dd03ebb778bc47ce506"
ACTION = "RESTORED_MEDIADB_INGREDIENT_MEMBERSHIP_AND_UNKNOWN_AMOUNTS"
KEYS = {"288", "289", "430", "460", "473", "474"}
LB = {"Tryptone": "10.0", "Yeast extract": "5.0", "Sodium chloride": "10.0"}
UNKNOWN = (
    "MediaDB reports this ingredient with an unavailable amount (None in the live table; "
    "NULL in the 2015-10-07 export). This is not evidence of zero or of a variable dose. "
    "The schema-defaulted VARIABLE concentration has been withdrawn; the original "
    "article's quantity remains unresolved."
)
LIMITS = [
    "Evidence establishes MediaDB's reported amounts for its own compound labels, not an "
    "independent verification of the original articles or existing chemical-form mappings.",
    "Existing preparation, classification, physical-state and organism claims are unchanged "
    "and are not certified by the concentration table.",
    "No mass conversion, final-volume assumption, exact-variant merge or taxa-media association.",
]


def sources():
    raw = (HERE / "source-review.json").read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Source review drift"
    source = json.loads(raw)
    records = {r["source_term"].split(":")[1]: r for r in source["records"]}
    assert set(records) == KEYS
    for mid, record in records.items():
        live = record["live"]
        assert live["url"] == f"https://mediadb.systemsbiology.net/defined_media/media/{mid}/"
        assert live["table"][0] == ["Compound", "Amount (mM)"]
        assert len(live["table"]) - 1 == len(record["rows"])
        for cid, row in record["rows"].items():
            sql = row["source_row"]["values"]
            assert sql["compID"] == cid and sql["medID"] == mid
            assert row["compound_row"]["values"]["compID"] == cid
            assert row["live_cells"] in live["table"][1:]
            assert row["live_cells"][0] == row["compound_row"]["values"]["name"]
            amount = sql["Amount_mM"]
            if amount is None:
                assert row["live_cells"][1] == "None"
            else:
                assert Decimal(amount) == Decimal(row["live_cells"][1])
    return source, records


def rows_by_name(record):
    rows = {r["compound_row"]["values"]["name"]: r for r in record["rows"].values()}
    assert len(rows) == len(record["rows"])
    return rows


def lb_node(node):
    return "LB Medium (Luria-Bertani," in node.get("supplier_catalog", {}).get("supplier_name", "")


def evidence(record, row, index):
    name, amount = row["live_cells"]
    meaning = (
        "The source amount is unavailable, not zero and not a specified variable dose. "
        "Only ingredient membership is supported; the former VARIABLE default is withdrawn."
        if amount == "None"
        else f"The database directly reports {amount} mM for this compound label; no conversion."
    )
    return {
        "reference": record["live"]["url"],
        "supports": "SUPPORT",
        "snippet": row["live_snippet"],
        "explanation": (
            f"ingredients[{index}] ({name}), concentration in {record['source_term']}. "
            f"Locator: compound table, column header 'Amount (mM)'. {meaning} "
            f"Corroborating 2015-10-07 export media_compounds row "
            f"(medcompID, medID, compID, Amount_mM): {row['source_row']['snippet']}. "
            "Evidence concerns the database compound label, not independent validation of "
            "existing ontology mappings, supplied hydrate form, or original-article quantities. "
            f"Accessed {record['live']['accessed_at'][:10]}."
        ),
    }


def membership_evidence(record, removed):
    row = rows_by_name(record)["Sodium chloride"]
    return {
        "reference": record["live"]["url"],
        "supports": "SUPPORT",
        "snippet": row["live_snippet"],
        "explanation": (
            f"Ingredient membership correction for {record['source_term']}: the complete "
            f"{len(record['rows'])}-compound table, corroborated against the versioned export, "
            "does not list Tryptone or Yeast extract and lists sodium chloride only at "
            f"{row['live_cells'][1]} mM under 'Amount (mM)'. Removed the unrelated LB "
            f"product expansion {json.dumps(removed, sort_keys=True)} and its copied root "
            "commercial-product note. The original source note is preserved. This is a "
            "correction to this database formulation, not a general statement about other variants."
        ),
    }


def references(source, record):
    return [
        {
            "reference": record["live"]["url"],
            "title": record["live"]["heading"],
            "notes": (
                "source_type=database_recipe_web_page; discovery_mode=source_accession; "
                f"accessed_on={record['live']['accessed_at'][:10]}; publisher=Institute for "
                f"Systems Biology; raw_html_sha256={record['live']['sha256']}; "
                "locator=Compound / Amount (mM) table; article DOI, individual authors "
                "and page publication year not established for this recipe page."
            ),
        },
        {
            "reference": source["source"]["url"],
            "title": "MediaDB SQL database export, 7 October 2015",
            "year": 2015,
            "notes": (
                "source_type=versioned_database_export; discovery_mode=official_download_page; "
                "accessed_on=2026-10-09; publisher=Institute for Systems Biology; "
                f"uncompressed_sha256={source['source']['sha256']}; "
                "locator=media_names, media_compounds and compounds tables; "
                "the database paper's DOI is not treated as evidence for individual amounts."
            ),
        },
    ]


def claims(before, after, record):
    results = []
    prior = {
        n["preferred_term"]: (i, n) for i, n in enumerate(before["ingredients"]) if not lb_node(n)
    }
    for index, node in enumerate(after["ingredients"]):
        name = node["preferred_term"]
        old_index, old = prior.get(name, (None, {}))
        results.append(
            {
                "pointer": ["ingredients", index],
                "old_pointer": ["ingredients", old_index] if old else None,
                "ingredient": name,
                "old": old.get("concentration"),
                "proposed": node.get("concentration"),
                "status": (
                    "correct" if "concentration" not in node else "evidence_only" if old else "add"
                ),
                "evidence": node["evidence"][-1],
                "calculation": "None; direct database table or unknown amount.",
                "limitations": LIMITS,
            }
        )
    for index, node in enumerate(before["ingredients"]):
        if lb_node(node):
            results.append(
                {
                    "pointer": None,
                    "old_pointer": ["ingredients", index],
                    "ingredient": node["preferred_term"],
                    "old": node["concentration"],
                    "proposed": None,
                    "status": "correct",
                    "evidence": after["evidence"][-1],
                    "calculation": "None; remove unrelated product expansion, not a dose conversion.",
                    "limitations": LIMITS,
                }
            )
    return results


def transform(before, source, record, timestamp):
    after = copy.deepcopy(before)
    removed = []
    retained = []
    for index, node in enumerate(after["ingredients"]):
        if lb_node(node):
            removed.append({"pointer": ["ingredients", index], "node": copy.deepcopy(node)})
        else:
            retained.append(node)
    after["ingredients"] = retained
    source_rows = rows_by_name(record)
    existing = {n["preferred_term"] for n in retained}
    assert len(existing) == len(retained)
    missing = sorted(set(source_rows) - existing)
    assert not existing - set(source_rows)
    for name in missing:
        assert name in {"3-Methylbutanoic acid", "2-methylbutanoic acid"}
        retained.append(
            {
                "preferred_term": name,
                "concentration": {
                    "value": source_rows[name]["source_row"]["values"]["Amount_mM"],
                    "unit": "MILLIMOLAR",
                },
            }
        )
    unknown = []
    for index, node in enumerate(retained):
        row = source_rows[node["preferred_term"]]
        if row["source_row"]["values"]["Amount_mM"] is None:
            assert node.pop("concentration") == {"value": "variable", "unit": "VARIABLE"}
            unknown.append(node["preferred_term"])
            node["notes"] = (node.get("notes", "") + " " + UNKNOWN).strip()
        node.setdefault("evidence", []).append(evidence(record, row, index))
    if removed:
        after["notes"] = before["notes"].split("\n\nCommercial Product:")[0].rstrip()
        assert "Commercial Product:" not in after["notes"]
        after.setdefault("evidence", []).append(membership_evidence(record, removed))
    after.setdefault("references", []).extend(references(source, record))
    changes = {
        "removed_lb_nodes": removed,
        "restored_ingredients": missing,
        "withdrawn_variable_defaults": unknown,
        "concentration_evidence_added": len(retained),
    }
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=record["live"]["url"],
        changes=json.dumps(changes, sort_keys=True),
        notes="Restored the exact MediaDB formulation and distinguished missing from variable "
        "amounts. Every current ingredient has a source-table snippet. " + " ".join(LIMITS),
    )
    return after


def check(before, after, item):
    """Independently invert only the reviewed ingredient/provenance changes."""
    source, records = sources()
    record = records[item["key"]]
    assert item["action"] == ACTION and item["path"] == record["path"]
    assert item["id"] == before["id"] == after["id"] == record["id"]
    assert (
        item["before_sha256"] == record["before_sha256"] == runner.sha(item["before_text"].encode())
    )
    assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
    assert before == runner.load_yaml(item["before_text"])
    assert after == runner.load_yaml(item["after_text"])
    assert item["claims"] == claims(before, after, record), "Claim inventory drift"
    assert before["media_term"]["term"]["id"] == record["source_term"]
    assert (
        before["original_name"].casefold()
        == record["medium_row"]["values"]["Media_name"].casefold()
    )
    rows = rows_by_name(record)
    old_nodes = {n["preferred_term"]: n for n in before["ingredients"] if not lb_node(n)}
    removed = [
        {"pointer": ["ingredients", i], "node": n}
        for i, n in enumerate(before["ingredients"])
        if lb_node(n)
    ]
    assert len(old_nodes) + len(removed) == len(before["ingredients"])
    if item["key"] in {"430", "460", "473", "474"}:
        assert {r["node"]["preferred_term"] for r in removed} == set(LB)
        assert len(removed) == 3
        for removal in removed:
            node = removal["node"]
            assert node["concentration"] == {"value": LB[node["preferred_term"]], "unit": "G_PER_L"}
            assert not node.get("evidence"), "Do not drop previous evidence"
    else:
        assert not removed
    expected_names = list(old_nodes) + sorted(set(rows) - set(old_nodes))
    assert [n["preferred_term"] for n in after["ingredients"]] == expected_names
    counts = collections.Counter()
    for index, node in enumerate(after["ingredients"]):
        name = node["preferred_term"]
        row = rows[name]
        old = old_nodes.get(name)
        reverted = copy.deepcopy(node)
        proof = reverted.pop("evidence")
        assert proof == (old or {}).get("evidence", []) + [evidence(record, row, index)]
        counts["new_evidence"] += 1
        if old and "evidence" in old:
            reverted["evidence"] = old["evidence"]
        amount = row["source_row"]["values"]["Amount_mM"]
        if amount is None:
            assert old and old["concentration"] == {"value": "variable", "unit": "VARIABLE"}
            assert "concentration" not in node
            assert node["notes"] == (old.get("notes", "") + " " + UNKNOWN).strip()
            reverted.pop("notes")
            if "notes" in old:
                reverted["notes"] = old["notes"]
            reverted["concentration"] = old["concentration"]
            counts["unsupported_quantity_slots_removed"] += 1
        else:
            assert set(node["concentration"]) == {"value", "unit"}
            assert node["concentration"]["unit"] == "MILLIMOLAR"
            assert Decimal(node["concentration"]["value"]) == Decimal(amount)
        if old:
            assert reverted == old, (name, "Unreviewed ingredient change")
        else:
            assert name in {"2-methylbutanoic acid", "3-Methylbutanoic acid"}
            assert reverted == {
                "preferred_term": name,
                "concentration": {"value": amount, "unit": "MILLIMOLAR"},
            }
            counts["new_quantity_slots"] += 1
    restored = copy.deepcopy(after)
    restored["ingredients"] = before["ingredients"]
    if removed:
        assert after["evidence"] == before.get("evidence", []) + [
            membership_evidence(record, removed)
        ]
        assert after["notes"] == before["notes"].split("\n\nCommercial Product:")[0].rstrip()
        restored["notes"] = before["notes"]
        restored.pop("evidence")
        if "evidence" in before:
            restored["evidence"] = before["evidence"]
        counts["new_evidence"] += 1
        counts["copied_ingredient_nodes_removed"] += len(removed)
        counts["unsupported_quantity_slots_removed"] += len(removed)
        counts["recipe_context_notes_corrected"] += 1
    assert after["references"] == before.get("references", []) + references(source, record)
    restored.pop("references")
    if "references" in before:
        restored["references"] = before["references"]
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["curator"] == "codex" and event["action"] == ACTION
    expected = transform(before, source, record, event["timestamp"])
    assert event == expected["curation_history"][-1]
    restored["curation_history"].pop()
    assert restored == before, "Unreviewed root field change"
    counts.update(new_references=2, new_curation_history=1)
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
    for mid, record in records.items():
        raw = (root / record["path"]).read_bytes()
        assert runner.sha(raw) == record["before_sha256"], "Record drift; new review required"
        before = runner.load_yaml(raw)
        assert not validate_recipe(before, target_class="MediaRecipe")
        after = transform(before, source, record, plan["created_at"])
        assert not validate_recipe(after, target_class="MediaRecipe")
        output = runner.render(raw.decode(), after)
        item = {
            "key": mid,
            "id": record["id"],
            "path": record["path"],
            "target_class": "MediaRecipe",
            "action": ACTION,
            "before_sha256": runner.sha(raw),
            "after_sha256": runner.sha(output),
            "before_text": raw.decode(),
            "after_text": output.decode(),
            "unresolved": LIMITS,
            "claims": claims(before, after, record),
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
    assert len(plan["records"]) == 6 and {r["key"] for r in plan["records"]} == KEYS
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
        assert target.read_bytes() == after, "Readback mismatch"
    return {"changed": len(pending), "already_applied": 6 - len(pending)}


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
                    "reviewed": 6,
                    "records_edited": 0,
                    "counts": dict(
                        sum(
                            (collections.Counter(r["counts"]) for r in plan["records"]),
                            collections.Counter(),
                        )
                    ),
                }
            )
        )


if __name__ == "__main__":
    main()
