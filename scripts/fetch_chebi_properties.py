#!/usr/bin/env python3
"""Build the packaged ChEBI structure table the media pages render from.

The ingredient tables carried no chemical information at all: `chemical_formula`
and `molecular_weight` are on `IngredientDescriptor` but are populated on 0 of
170,007 ingredients. Meanwhile 144,092 of those ingredients (85%) already carry
a ChEBI id, and those ids collapse to just **640 distinct terms**.

So the formula is not recipe data — it is a property of the ChEBI term, shared
by every recipe that cites it. Writing it into 144,092 record entries would
denormalize one fact into thousands of copies that then drift. This builds a
single 640-row lookup instead, packaged next to the MIM label index, and the
renderer joins against it.

Source is the EBI OLS4 API over the current ChEBI release. Only what ChEBI
actually asserts is recorded: `generalized_empirical_formula`, `mass`, and
`charge`. A term with no formula gets an empty cell rather than a guess.

Preview by default. `--apply` writes the table.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RECORDS = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_OUT = REPO_ROOT / "src" / "culturemech" / "data" / "chebi" / "structure_index.csv"
METADATA = "structure_index.meta.json"

OLS4 = "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms"
IRI = "http://purl.obolibrary.org/obo/CHEBI_{}"
HEADER = ["chebi_id", "label", "formula", "molecular_weight", "charge"]

USER_AGENT = "CultureMech/1.0 (https://github.com/CultureBotAI/CultureMech)"


def cited_chebi_ids(records_dir: Path) -> list[str]:
    """Every distinct CHEBI id cited by an ingredient or solution component."""
    found: set[str] = set()

    def walk(items) -> None:
        for item in items or []:
            if not isinstance(item, dict):
                continue
            identifier = (item.get("term") or {}).get("id")
            if isinstance(identifier, str) and identifier.startswith("CHEBI:"):
                found.add(identifier)
            walk(item.get("composition"))

    for path in sorted(records_dir.glob("*/*.yaml")):
        record = yaml.safe_load(path.read_text())
        if not isinstance(record, dict):
            continue
        walk(record.get("ingredients"))
        walk(record.get("solutions"))
    return sorted(found, key=lambda c: int(c.split(":")[1]))


def fetch(chebi_id: str, timeout: float = 30.0) -> dict[str, str] | None:
    """One term from OLS4, or None when it does not resolve."""
    local = chebi_id.split(":", 1)[1]
    query = urllib.parse.urlencode({"iri": IRI.format(local)})
    request = urllib.request.Request(
        f"{OLS4}?{query}", headers={"User-Agent": USER_AGENT, "Accept": "application/json"}
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310
        payload = json.load(response)

    terms = (payload.get("_embedded") or {}).get("terms") or []
    if not terms:
        return None
    term = terms[0]
    annotation = term.get("annotation") or {}

    def first(key: str) -> str:
        values = annotation.get(key) or []
        if not values:
            return ""
        value = values[0]
        # OLS4 returns charge as a float; 0.0 is a real charge, not a blank.
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value).strip()

    return {
        "chebi_id": chebi_id,
        "label": (term.get("label") or "").strip(),
        "formula": first("generalized_empirical_formula"),
        "molecular_weight": first("mass"),
        "charge": first("charge"),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--records-dir", type=Path, default=DEFAULT_RECORDS)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--apply", action="store_true", help="Write. Default is preview.")
    parser.add_argument("--limit", type=int, default=0, help="Fetch at most N terms.")
    parser.add_argument("--rate-limit", type=float, default=0.15, help="Seconds between calls.")
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    ids = cited_chebi_ids(args.records_dir)
    if args.limit:
        ids = ids[: args.limit]
    print(f"{len(ids)} distinct CHEBI ids cited by the corpus")

    rows: list[dict[str, str]] = []
    stats: Counter = Counter()
    failures: list[tuple[str, str]] = []

    for index, chebi_id in enumerate(ids, 1):
        try:
            row = fetch(chebi_id)
        except Exception as error:  # noqa: BLE001 - reported, not swallowed
            failures.append((chebi_id, f"{type(error).__name__}: {error}"))
            stats["errored"] += 1
        else:
            if row is None:
                failures.append((chebi_id, "not found in the current ChEBI release"))
                stats["unresolved"] += 1
            else:
                rows.append(row)
                stats["resolved"] += 1
                stats["with_formula"] += bool(row["formula"])
                stats["with_mass"] += bool(row["molecular_weight"])
        if index % 50 == 0:
            print(f"  {index}/{len(ids)}")
        time.sleep(args.rate_limit)

    print(f"\n{'Wrote' if args.apply else 'Would write'} {len(rows)} rows to {args.out}")
    for key in sorted(stats):
        print(f"  {key}: {stats[key]}")
    if failures:
        print(f"\n{len(failures)} id(s) not recorded:")
        for chebi_id, reason in failures[:20]:
            print(f"  {chebi_id}: {reason}")

    if args.apply:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=HEADER)
            writer.writeheader()
            writer.writerows(rows)
        (args.out.parent / METADATA).write_text(
            json.dumps(
                {
                    "source": OLS4,
                    "ontology": "chebi",
                    "fetched": datetime.now(UTC).isoformat(),
                    "row_count": len(rows),
                    "ids_requested": len(ids),
                    "fields": HEADER,
                    "note": (
                        "Only properties ChEBI asserts are recorded. An empty formula "
                        "means ChEBI states none for that term, not that lookup failed; "
                        "terms that failed to resolve are absent from the table."
                    ),
                },
                indent=2,
            )
            + "\n"
        )
    else:
        print("\nPreview only. Re-run with --apply to write.")

    # Missing rows would silently blank a column on the pages.
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
