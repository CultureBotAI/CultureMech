#!/usr/bin/env python3
"""Build the record07 source-location inventory for manual review.

Provenance date: 2026-11-15.
Context: CultureMech #749 (DSMZ876 scientific findings) and #752 (retain the
executed provenance helpers and their historical versions).

Required inputs: no CLI arguments. Read the three YAML paths in PATHS (the
selected generated record and both maintained owners) and the already captured
record07/medium876.json under .temp/batch079-scientific-20261114. Python requires
PyYAML; paths are resolved from this script's checkout root.
Outputs: an exclusively created record07/claim-inventory.json and console rows
showing current ingredients, stock additions and exact-label source candidates.

Replay limits: this is a one-run inventory writer and refuses an existing output.
It does not fetch sources, verify chemical identities, decide source equivalence
or declare quantities scientifically valid. Exact-name candidates can span
multiple source stocks and require manual interpretation. Preserve the original
inventory and the retained pre-format helper bytes instead of overwriting them
or treating a later invocation as the original scientific reading.
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / ".temp" / "batch079-scientific-20261114" / "record07"
PATHS = (
    "data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml",
    "data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml",
    "data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml",
)


def main() -> None:
    source = json.loads((RUN / "medium876.json").read_text())
    by_label = {}
    for solution in source["solutions"]:
        for item in solution["recipe"]:
            if "compound" in item:
                by_label.setdefault(item["compound"], []).append(
                    {
                        "solution_id": solution["id"],
                        "solution": solution["name"],
                        "volume_ml": solution["volume"],
                        **item,
                    }
                )
    result = {}
    for path in PATHS:
        record = yaml.safe_load((ROOT / path).read_text())
        rows = []
        for index, ingredient in enumerate(record["ingredients"]):
            rows.append(
                {
                    "field": f"ingredients[{index}]",
                    "ingredient": ingredient,
                    "source_occurrences": by_label.get(ingredient["preferred_term"], []),
                }
            )
        for si, solution in enumerate(record.get("solutions", [])):
            for index, ingredient in enumerate(solution.get("composition", [])):
                rows.append(
                    {
                        "field": f"solutions[{si}].composition[{index}]",
                        "solution": solution["preferred_term"],
                        "addition": solution.get("concentration"),
                        "addition_candidates": solution.get("concentration_candidates"),
                        "ingredient": ingredient,
                        "source_occurrences": by_label.get(ingredient["preferred_term"], []),
                    }
                )
        result[path] = rows
    output = RUN / "claim-inventory.json"
    with output.open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    for path, rows in result.items():
        print(path)
        for row in rows:
            item = row["ingredient"]
            refs = [
                f"{r['solution_id']}:{r['compound']} {r.get('amount')} {r.get('unit')} "
                f"(g_l={r.get('g_l')}; volume={r['volume_ml']}ml)"
                for r in row["source_occurrences"]
            ]
            print(row["field"], item["preferred_term"], item.get("concentration"), refs)
    print(f"Diagnostic source-location inventory: {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
