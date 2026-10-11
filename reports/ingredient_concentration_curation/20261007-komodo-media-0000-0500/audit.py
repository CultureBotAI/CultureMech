"""Independently invert every proposed/persisted change and recheck source arithmetic."""

import argparse
import copy
import hashlib
import json
import subprocess
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import review_komodo_concentration_evidence as komodo  # noqa: E402


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def check(cache, mapping_path, applied, folder=Path(__file__).parent, expected_records=500):
    assert expected_records > 0
    plan = json.loads((folder / "plan.json").read_text())
    assert len(plan["records"]) == expected_records
    mapping = mapping_path.read_bytes()
    assert digest(mapping) == plan["mapping_source"]["sha256"]
    komodo.check_mapping_title(mapping_path, plan)
    counts = Counter(
        records=0,
        changed=0,
        concentration_evidence=0,
        mapping_evidence=0,
        new_evidence=0,
        new_references=0,
        new_curation_history=0,
    )
    snapshots = {
        i["path"]: i for i in json.loads((folder / "inspected-candidate-context.json").read_text())
    }
    source_meta = json.loads((folder / "source-captures.json").read_text())["sources"]
    reviewer = komodo.adapter(
        plan["records"], plan["mapping_source"], plan["withholdings"], plan.get("mapping_title")
    )
    requests = "".join(f"{plan['commit']}:{r['path']}\n" for r in plan["records"])
    baselines = subprocess.check_output(
        ["git", "cat-file", "--batch"], input=requests.encode(), cwd=ROOT
    )
    cursor = 0
    for item in plan["records"]:
        end = baselines.index(b"\n", cursor)
        _, kind, size = baselines[cursor:end].split()
        assert kind == b"blob"
        length = int(size)
        before = baselines[end + 1 : end + 1 + length]
        assert baselines[end + 1 + length : end + 2 + length] == b"\n"
        cursor = end + 2 + length
        assert digest(before) == item["before_sha256"], item["path"]
        original = yaml.load(before, Loader=yaml.CSafeLoader)
        current = (ROOT / item["path"]).read_bytes()
        assert digest(current) == item["after_sha256" if applied else "before_sha256"]
        source, meta = komodo.read_source(cache, item["medium_id"])
        assert meta == source_meta[item["medium_id"]]
        assert (
            meta["sha256"] == item["source_sha256"]
            and meta["accessed_at"] == item["source_accessed_at"]
        )
        assert not item["failure"] and not item["baseline_errors"] and not item["post_errors"]
        if applied:
            result = yaml.load(current, Loader=yaml.CSafeLoader)
        else:
            result, claims = reviewer.reviewer(original, source, meta, plan["created_at"])
            assert claims == item["claims"]
            encoded = (
                komodo.runner.render(before.decode(), result) if result != original else before
            )
            assert digest(encoded) == item["after_sha256"]
        restored = copy.deepcopy(result)
        accepted = [c for c in item["claims"] if c["status"] in komodo.runner.SUPPORTED]
        assert bool(accepted) == (item["before_sha256"] != item["after_sha256"])
        for claim in accepted:
            assert claim["status"] == "evidence_only" and claim["new"] == claim["old"]
            assert item["komodo_id"] == item["medium_id"]
            assert meta["http_status"] == 200
            assert claim["pointer"][0] == "ingredients" and len(claim["pointer"]) == 2
            node = restored["ingredients"][claim["pointer"][1]]
            old_node = original["ingredients"][claim["pointer"][1]]
            assert node["concentration"] == old_node["concentration"] == claim["old"]
            row = json.loads(claim["snippet"])
            assert claim["snippet"] in source
            data = json.loads(source)["data"]
            assert data["medium"]["source"] == "DSMZ"
            assert data["medium"]["link"] == item["mapping"]["original_recipe"]
            assert len(data["solutions"]) == 1
            assert row in data["solutions"][0]["recipe"]
            assert row["compound"] == node["preferred_term"] == claim["ingredient"]
            assert row["optional"] == 0 and not row.get("attribute")
            assert row.get("solution_id") is None
            if row.get("condition"):
                assert (
                    row["condition"] == "for solid medium"
                    and original["physical_state"] == "SOLID_AGAR"
                )
            volume = Decimal(str(data["solutions"][0]["volume"]))
            unit = row["unit"]
            scales = {"g": "1", "mg": "0.001", "\u00b5g": "0.000001", "g/l": "1", "mg/l": "0.001"}
            amount = Decimal(str(row["amount"])) * Decimal(scales[unit])
            calculated = amount if unit.endswith("/l") else amount / (volume / 1000)
            reported = Decimal(str(row["g_l"]))
            assert (
                abs(calculated - reported)
                <= Decimal("0.5") * Decimal(10) ** reported.as_tuple().exponent
            )
            assert node["concentration"]["unit"] == "G_PER_L"
            assert Decimal(node["concentration"]["value"]) == reported
            evidence = node["evidence"].pop()
            assert evidence["reference"] == claim["reference"] == meta["url"]
            assert evidence["snippet"] == claim["snippet"] and evidence["supports"] == "SUPPORT"
            assert (
                claim["field"] in evidence["explanation"]
                and meta["sha256"] in evidence["explanation"]
            )
            if "evidence" not in old_node:
                assert not node.pop("evidence")
        if accepted:
            assert snapshots[item["path"]]["local"] == original
            assert snapshots[item["path"]]["source"] == json.loads(source)["data"]
            evidence = restored["evidence"].pop()
            assert evidence["reference"] == komodo.MAPPING_URL
            assert evidence["snippet"] == item["mapping"]["snippet"]
            assert evidence["snippet"] in mapping.decode()
            assert "Source identity only" in evidence["explanation"]
            assert plan["mapping_source"]["sha256"] in evidence["explanation"]
            if "evidence" not in original:
                assert not restored.pop("evidence")
            refs = restored["references"][-2:]
            assert [r["reference"] for r in refs] == [meta["url"], komodo.MAPPING_URL]
            if "mapping_title" in plan:
                assert refs[1]["title"] == plan["mapping_title"]
            assert (
                meta["sha256"] in refs[0]["notes"]
                and plan["mapping_source"]["sha256"] in refs[1]["notes"]
            )
            del restored["references"][-2:]
            if "references" not in original:
                assert not restored.pop("references")
            event = restored["curation_history"].pop()
            assert event["action"] == komodo.ACTION and event["curator"] == "codex"
            assert event["timestamp"] == plan["created_at"]
            if "curation_history" not in original:
                assert not restored.pop("curation_history")
        assert restored == original, item["path"]
        counts.update(
            records=1,
            changed=bool(accepted),
            concentration_evidence=len(accepted),
            mapping_evidence=bool(accepted),
            new_evidence=len(accepted) + bool(accepted),
            new_references=2 * bool(accepted),
            new_curation_history=bool(accepted),
        )
    assert cursor == len(baselines)
    assert counts["records"] == expected_records
    return {
        **counts,
        "only_provenance_appended": True,
        "unsupported_claims_unchanged": True,
        "quantities_and_formulation_unchanged": True,
        "stage": "applied" if applied else "preflight",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--folder", type=Path, default=Path(__file__).parent)
    parser.add_argument("--expected-records", type=int, default=500)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    result = check(args.cache, args.mapping, args.applied, args.folder, args.expected_records)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)
