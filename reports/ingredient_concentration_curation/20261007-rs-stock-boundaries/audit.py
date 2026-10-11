"""Independent source arithmetic, whole-record inversion and merge retention for P4/P5."""

import argparse
import collections
import copy
import hashlib
import importlib.util
import json
import re
from decimal import Decimal
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ACTION = "RESTORED_RS_STOCK_BOUNDARIES_CARRIERS_AND_SOURCE_CONFLICTS"
NNM = "RS Medium - Non-Nutrient Medium (NNM) Component"
NNM_TERM = {"id": "CultureMech:010434", "label": NNM}
SNAPSHOT = HERE.parent / "20261007-public-medium-source-pages.json"


def get(node, pointer):
    for key in pointer:
        if node is None:
            return None
        node = node[key] if isinstance(node, list) else node.get(key)
    return node


def strip_evidence(node, reference):
    count = 0
    if isinstance(node, dict):
        evidence = node.pop("evidence", [])
        assert len(evidence) <= 1
        for e in evidence:
            assert e["reference"] == reference and e["supports"] == "SUPPORT"
            assert e["snippet"] and e["explanation"]
        count += len(evidence)
        for value in node.values():
            count += strip_evidence(value, reference)
    elif isinstance(node, list):
        for value in node:
            count += strip_evidence(value, reference)
    return count


def fingerprint_delta(before, after):
    from culturemech.merge.fingerprint import RecipeFingerprinter

    printer = RecipeFingerprinter()
    old, new = [set(map(str, printer._extract_signatures(n))) for n in (before, after)]
    expected = {"water", "purified water"} if before["id"].endswith("434") else {"purified water"}
    assert not old - new and new - old == expected, (old - new, new - old)
    return {
        "before": printer.fingerprint(before),
        "after": printer.fingerprint(after),
        "added_identifiers": sorted(new - old),
        "removed_identifiers": [],
    }


def check(before, after, item):
    mid = item["medium_id"]
    assert mid in {"P4", "P5"} and item["action"] == ACTION
    assert before["id"] == after["id"] == item["id"]
    assert before["id"] == ("CultureMech:010434" if mid == "P4" else "CultureMech:010435")
    raw = SNAPSHOT.read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "9b1238f4c428109f538a733605e34f22b9b3e577f065cac40f6f417f54605078"
    )
    source = next(r for r in json.loads(raw)["records"] if r["medium_id"] == mid)
    rows = source["recipe_tables"][0]["rows"]
    blocks = [" ".join(r["cells"]) for r in rows]
    ingredients = [r["cells"] for r in rows if "id" in r["attributes"]]
    steps = {
        int(r["cells"][0].split()[0]): r["cells"][0]
        for r in rows
        if r["attributes"].get("class") == "step-row"
    }
    reference = "https://mediadive.dsmz.de/medium/" + mid
    for c in item["claims"]:
        assert (get(before, c["old_pointer"]) if c["old_pointer"] is not None else None) == c["old"]
        assert get(after, c["pointer"]) == c["new"]
        entries = get(after, c["evidence_pointer"])["evidence"]
        assert len(entries) == 1 and entries[0]["reference"] == c["reference"] == reference
        entry = entries[0]
        assert c["field"] in entry["explanation"]
        for quote in [c, *c["extra_excerpts"]]:
            assert any(quote["snippet"] in text for text in blocks), quote
            assert quote["snippet"] in entry["explanation"]
            assert quote["locator"] in entry["explanation"]
    restored = copy.deepcopy(after)
    count = collections.Counter(
        new_evidence=strip_evidence(restored, reference), new_references=1, new_curation_history=1
    )
    assert strip_evidence(copy.deepcopy(before), reference) == 0
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    ref = restored["references"].pop()
    assert ref["reference"] == reference and ref["year"] == 2023
    assert ref["authors"] == "Cristiana Sigona, Daniel J. Richter" and ref["title"]
    assert all(
        token in ref["notes"]
        for token in [
            "source_type=user_contributed_dataset_page",
            "discovery_mode=existing_record_reference",
            "not curated/tested",
            "no valid reference",
        ]
    )
    assert restored["notes"] and restored["notes"] != before["notes"]
    restored["notes"] = before["notes"]
    count["recipe_context_notes_corrected"] = 1

    def amount(node, value, unit):
        assert set(node["concentration"]) == {"value", "unit"}
        assert Decimal(node["concentration"]["value"]) == Decimal(value)
        assert node["concentration"]["unit"] == unit

    def carrier(node, label):
        assert set(node) == {"preferred_term", "source", "notes"} | (
            {"culturemech_term"} if label == NNM else set()
        )
        assert node["preferred_term"] == label and node["notes"]
        assert node["source"] == "MediaDive public Medium " + mid
        if label == NNM:
            assert node["culturemech_term"] == NNM_TERM
        count["unquantified_carrier_nodes_added"] += 1

    def restore_solute(node, old, conflict=False):
        assert node.get("notes")
        for key in ("concentration", "notes") + (("data_quality_flags",) if conflict else ()):
            if key in old:
                node[key] = copy.deepcopy(old[key])
            else:
                node.pop(key, None)
        assert node == old, "Identity, grounding, source or unrelated ingredient metadata changed"
        return node

    if mid == "P4":
        assert len(restored["ingredients"]) == 10 and len(restored["solutions"]) == 23
        assert "Fill to a total volume of 1 liter with purified H2O." in steps[4]
        assert "prepare stock solutions in H2O at the specified concentration" in steps[2]
        carrier(restored["ingredients"].pop(), "Purified water")
        direct = {n["preferred_term"]: n for n in restored["ingredients"]}
        stocks = {s["composition"][0]["preferred_term"]: s for s in restored["solutions"]}
        assert len(direct) == 9 and len(stocks) == 23
        rebuilt = []
        for old in before["ingredients"]:
            name = old["preferred_term"]
            row = next(r for r in ingredients if r[0].split(" (Stock solution")[0] == name)
            if row[2] == "g/l":
                node = direct.pop(name)
                amount(node, row[1], "G_PER_L")
                assert node == old
            else:
                stock = stocks.pop(name)
                assert set(stock) == {"preferred_term", "concentration", "notes", "composition"}
                assert row[0] in stock["notes"] and stock["preferred_term"] == name + " stock"
                assert len(stock["composition"]) == 2
                dose = Decimal(row[1]) * (Decimal(1) if row[2] == "ml/l" else Decimal("0.001"))
                amount(stock, dose, "ML_PER_L")
                node = stock["composition"][0]
                carrier(stock["composition"][1], "Water")
                if name == "TiCl3":
                    assert (
                        "concentration" not in node and "10-15%" in row[0] and "1:1000000" in row[0]
                    )
                    assert stock["concentration"] == old["concentration"]
                    count["ingredient_doses_relocated_to_stock"] += 1
                else:
                    strength = row[0].split("Stock solution ", 1)[1].split(")", 1)[0]
                    mass, volume = strength.lower().split("/")
                    factor = Decimal(1) if mass.endswith("mg") else Decimal(1000)
                    assert "ml" in volume
                    rate = (
                        Decimal(mass.removesuffix("mg").removesuffix("g"))
                        * factor
                        / Decimal(volume.split("ml", 1)[0] or "1")
                    )
                    amount(node, rate, "G_PER_L")
                    old_rate = (
                        Decimal(old["concentration"]["value"])
                        * {
                            "G_PER_L": Decimal(1),
                            "MG_PER_L": Decimal("0.001"),
                            "MICROG_PER_L": Decimal("0.000001"),
                        }[old["concentration"]["unit"]]
                    )
                    assert old_rate == rate * dose / 1000
                    count["stock_stage_concentrations_rebased"] += 1
                    count["new_quantity_slots"] += 1
                node = restore_solute(node, old)
                count["stock_nodes_relocated"] += 1
            rebuilt.append(node)
        assert not direct and not stocks and count["new_evidence"] == 57
        restored["ingredients"] = rebuilt
        restored.pop("solutions")
        count["stock_descriptors_added"] = 23
    else:
        assert restored["ingredients"] == [] and len(restored["solutions"]) == 6
        assert "Fill to 150 ml with NNM." in steps[10]
        doses = [Decimal(v) / 1000 for v in ("4", "30", "10.7", "10.9", "10.7")]
        expected_stocks = (3, 4, 10, 3, 17)
        for mi, old_mix in enumerate(before["solutions"][:5]):
            mix = restored["solutions"][mi]
            amount(mix, doses[mi], "L")
            assert "50 ml" in mix["notes"] and "150 ml" in mix["notes"]
            assert "Fill to 50 ml with NNM." in steps[mi + 5]
            assert len(mix["solutions"]) == expected_stocks[mi]
            moved = {}
            for si, stock in enumerate(mix["solutions"]):
                assert set(stock) == {"preferred_term", "concentration", "notes", "composition"}
                dose = (
                    Decimal("0.0000045")
                    if mi == 2
                    else Decimal("0.00225") if mi == 3 and si == 0 else Decimal("0.00227")
                )
                amount(stock, dose, "L")
                assert "not L/L" in stock["notes"]
                if mi == 3 and si < 2:
                    assert (
                        stock["preferred_term"]
                        == f"MEM {50 if si == 0 else 100}X Amino Acids solution (Sigma)"
                    )
                    assert len(stock["composition"]) == (12 if si == 0 else 7)
                    assert "solvent" in stock["notes"]
                    solutes = stock["composition"]
                else:
                    assert len(stock["composition"]) == 2
                    solutes = stock["composition"][:1]
                    name = solutes[0]["preferred_term"]
                    row = next(r for r in ingredients if r[0].startswith(name + " ("))
                    assert row[0] in stock["notes"]
                    solvent = NNM if "Single stock in NNM." in row[0] else "Purified water"
                    if "Single stock in H2O." not in row[0] and solvent != NNM:
                        assert name in {"Methyl-cellulose", "Pectin"}
                        assert (
                            "prepare the single stock in H2O."
                            in steps[3 if name == "Methyl-cellulose" else 4]
                        )
                    carrier(stock["composition"][1], solvent)
                for node in solutes:
                    name = node["preferred_term"]
                    assert name not in moved
                    if mi == 3 and si < 2:
                        match = re.search(re.escape(name) + r" \(([0-9.]+) g/L\)", steps[8])
                        assert match is not None
                        rate = Decimal(match[1])
                    else:
                        assert row[2] in {"g/ml", "g/50ml"}
                        rate = Decimal(row[1]) * (1000 if row[2] == "g/ml" else 20)
                    amount(node, rate, "G_PER_L")
                    moved[name] = (node, rate * dose / Decimal("0.05"))
                count["new_quantity_slots"] += 1
                count["stock_descriptors_added"] += 1
            direct = {n["preferred_term"]: n for n in mix["composition"]}
            assert len(direct) == (4 if mi == 4 else 1)
            rebuilt = []
            for old in old_mix["composition"]:
                name = old["preferred_term"]
                if name in moved:
                    node, legacy = moved.pop(name)
                    amount(old, legacy, "G_PER_L")
                    restore_solute(node, old)
                    count["stock_nodes_relocated"] += 1
                    count["stock_stage_concentrations_rebased"] += 1
                else:
                    node = direct.pop(name)
                    if name == "Glycerol":
                        assert "45 \u00b5l" in steps[9] and "1.26 g/mL" in steps[9]
                        amount(
                            node, Decimal("0.045") * Decimal("1.26") / Decimal("0.05"), "G_PER_L"
                        )
                        assert node == old
                    else:
                        assert "concentration" not in node
                        if name == NNM:
                            assert node["culturemech_term"] == NNM_TERM and "50 ml" in node["notes"]
                        else:
                            other = {"D-Mannose": "L-mannose", "D-Xylose": "Xylan"}[name]
                            assert other in steps[9] and other in node["notes"]
                            assert "not confirmed presence" in node["notes"]
                            assert node["data_quality_flags"] == ["source_identity_conflict"]
                            count["identity_conflicts_retained_unquantified"] += 1
                        restore_solute(node, old, conflict=name != NNM)
                        count["unsupported_quantity_slots_removed"] += 1
                rebuilt.append(node)
            assert not direct and not moved
            mix["composition"] = rebuilt
            mix.pop("solutions")
            mix["concentration"] = copy.deepcopy(old_mix["concentration"])
            mix["notes"] = old_mix["notes"]
            assert mix == old_mix
        makeup = restored["solutions"][5]
        assert "concentration" not in makeup and "150 ml" in makeup["notes"]
        restore_solute(makeup, before["solutions"][5])
        count.update(
            quantity_corrections=5,
            stock_dose_basis_corrections=5,
            unsupported_quantity_slots_removed=1,
        )
        assert count["new_evidence"] == 98
    assert restored == before, "Unrelated scientific or historical edit"
    fingerprint_delta(before, after)
    return count


def audit():
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        assert hashlib.sha256(item["before_text"].encode()).hexdigest() == item["before_sha256"]
        counts.update(check(yaml.safe_load(item["before_text"]), yaml.safe_load(raw), item))
    counts["edited_records"] = len(plan["records"])
    assert counts["edited_records"] == 2 and counts["new_evidence"] == 155
    return dict(counts)


def retention():
    from culturemech.merge.matcher import RecipeMatcher
    from culturemech.merge.merge_recipes import find_all_recipes
    from culturemech.merge.merger import RecipeMerger

    audit()
    spec = importlib.util.spec_from_file_location(
        "retention_fields", HERE.parent / "20261007-komodo12-extraction/check_retention.py"
    )
    shared = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(shared)
    groups = RecipeMatcher().group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    rows = []
    for item in json.loads((HERE / "plan.json").read_text())["records"]:
        target = ROOT / item["path"]
        matches = [(f, paths) for f, paths in groups.items() if target in paths]
        assert len(matches) == 1
        fingerprint, paths = matches[0]
        merged = RecipeMerger().merge_group(paths, fingerprint=fingerprint)
        source = yaml.safe_load(target.read_bytes())
        fields = shared.retention(merged, source)
        fields.update(
            {key: merged.get(key) == source.get(key) for key in ("notes", "curation_history")}
        )
        rows.append(
            {
                "path": item["path"],
                "fingerprint": fingerprint,
                "fingerprint_change": fingerprint_delta(
                    yaml.safe_load(item["before_text"]), source
                ),
                "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                "merged_id": merged["id"],
                "field_retention": fields,
                "all_checked_fields_retained": all(fields.values()),
            }
        )
    return {
        "records": rows,
        "retained": sum(r["all_checked_fields_retained"] for r in rows),
        "all_retained": all(r["all_checked_fields_retained"] for r in rows),
        "scope": "Actual complete corpus groups, including water membership changes. No generated merge published.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--retention", action="store_true")
    args = parser.parse_args()
    assert not args.out.exists(), args.out
    result = retention() if args.retention else audit()
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)
    raise SystemExit(1 if result.get("all_retained") is False else 0)
