"""Check amount and mapping provenance in actual current merge groups."""

import argparse
import json
from collections import Counter
from pathlib import Path

import yaml

from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger

ROOT = Path(__file__).resolve().parents[3]


def check(folder=Path(__file__).parent):
    plan = json.loads((folder / "plan.json").read_text())
    targets = {
        ROOT / r["path"]: r for r in plan["records"] if r["before_sha256"] != r["after_sha256"]
    }
    matcher, merger = RecipeMatcher(), RecipeMerger()
    groups = matcher.group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    results, counts = [], Counter()
    for fp, paths in groups.items():
        relevant = [p for p in paths if p in targets]
        if not relevant:
            continue
        merged = merger.merge_group(paths, fingerprint=fp)
        for path in relevant:
            item = targets[path]
            doc = yaml.load(path.read_bytes(), Loader=yaml.CSafeLoader)
            accepted = [c for c in item["claims"] if c["status"] == "evidence_only"]
            retained = 0
            amount_quotes = 0
            for claim in accepted:
                node = doc["ingredients"][claim["pointer"][1]]
                evidence = next(e for e in node["evidence"] if e["reference"] == claim["reference"])
                matches = [
                    n
                    for n in merged.get("ingredients", [])
                    if n["preferred_term"] == claim["ingredient"]
                    and n.get("concentration") == claim["new"]
                    and evidence in n.get("evidence", [])
                ]
                retained += len(matches) == 1
                quote_matches = [
                    e
                    for n in merged.get("ingredients", [])
                    if n["preferred_term"] == claim["ingredient"]
                    and n.get("concentration") == claim["new"]
                    for e in n.get("evidence", [])
                    if e.get("reference") == claim["reference"]
                    and e.get("snippet") == claim["snippet"]
                    and e.get("supports") == "SUPPORT"
                    and claim["field"] in e.get("explanation", "")
                ]
                amount_quotes += len(quote_matches) == 1
            mapping_retained = doc["evidence"][-1] in merged.get("evidence", [])
            references_retained = all(
                r in merged.get("references", []) for r in doc["references"][-2:]
            )
            event_retained = doc["curation_history"][-1] in merged.get("curation_history", [])
            result = {
                "path": item["path"],
                "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                "fingerprint": fp,
                "accepted_claims": len(accepted),
                "retained_full_entries": retained,
                "retained_amount_quotes": amount_quotes,
                "mapping_retained": mapping_retained,
                "references_retained": references_retained,
                "event_retained": event_retained,
            }
            results.append(result)
            counts.update(
                accepted_claims=len(accepted),
                retained_full_entries=retained,
                retained_amount_quotes=amount_quotes,
                records_with_full_entry_loss=retained != len(accepted),
                records_with_amount_quote_loss=amount_quotes != len(accepted),
                records_with_mapping_loss=not mapping_retained,
                records_with_reference_loss=not references_retained,
                records_with_event_loss=not event_retained,
            )
    assert {r["path"] for r in results} == {r["path"] for r in targets.values()}
    return {
        "records": len(results),
        **counts,
        "scope": "Full entries require exact explanation retention; amount quotes require exact ingredient, quantity, reference, SUPPORT, snippet and field scope. Neither alone proves exact formulation equivalence of a concentration-independent group.",
        "details": results,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--folder", type=Path, default=Path(__file__).parent)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    result = check(args.folder)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "details"}), flush=True)
    raise SystemExit(int(any(v for k, v in result.items() if k.startswith("records_with_"))))
