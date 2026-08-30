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
from collections.abc import Iterable, Mapping

# `timezone.utc`, not `datetime.UTC`: the latter is 3.11+ and this project
# supports >=3.10. The rest of scripts/ already uses timezone.utc.
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RECORDS = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_OUT = REPO_ROOT / "src" / "culturemech" / "data" / "chebi" / "structure_index.csv"
METADATA = "structure_index.meta.json"

OLS4 = "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms"
IRI = "http://purl.obolibrary.org/obo/CHEBI_{}"
HEADER = ["chebi_id", "label", "formula", "molecular_weight", "charge"]

USER_AGENT = "CultureMech/1.0 (https://github.com/CultureBotAI/CultureMech)"


def _collect(items, found: set[str]) -> None:
    for item in items or []:
        if not isinstance(item, dict):
            continue
        identifier = (item.get("term") or {}).get("id")
        if isinstance(identifier, str) and identifier.startswith("CHEBI:"):
            found.add(identifier)
        _collect(item.get("composition"), found)


def cited_chebi_ids_from_records(records: Iterable[Mapping[str, Any]]) -> list[str]:
    """Every distinct CHEBI id cited by already-parsed records.

    Split out from `cited_chebi_ids` so the test can reuse conftest's
    session-scoped `corpus` fixture. Re-walking `data/normalized_yaml` from the
    test took 484s in CI and tripped the 120s slow-test budget.
    """
    found: set[str] = set()
    for record in records:
        if not isinstance(record, Mapping):
            continue
        _collect(record.get("ingredients"), found)
        _collect(record.get("solutions"), found)
    return sorted(found, key=lambda c: int(c.split(":")[1]))


def cited_chebi_ids(records_dir: Path) -> list[str]:
    """Every distinct CHEBI id cited by the corpus on disk."""

    def parsed():
        for path in sorted(records_dir.glob("*/*.yaml")):
            record = yaml.safe_load(path.read_text())
            if isinstance(record, dict):
                yield record

    return cited_chebi_ids_from_records(parsed())


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


def check(records_dir: Path | None, out: Path, cited: Iterable[str] | None = None) -> int:
    """Verify the packaged table against its metadata and the corpus. Offline.

    A stale or truncated table fails quietly — `structure_for` returns None for
    an unknown id, which is right at render time and wrong as the only line of
    defence. This is the loud check.
    """
    problems: list[str] = []

    if not out.exists():
        print(f"{out} is missing. Build it with --apply.", file=sys.stderr)
        return 1
    meta_path = out.parent / METADATA
    if not meta_path.exists():
        problems.append(f"{meta_path.name} is missing")
        metadata = {}
    else:
        metadata = json.loads(meta_path.read_text())

    with out.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != HEADER:
            problems.append(f"header is {reader.fieldnames}, expected {HEADER}")
        rows = list(reader)

    if metadata.get("fields") not in (None, HEADER):
        problems.append(f"metadata fields {metadata.get('fields')} do not match {HEADER}")
    recorded = metadata.get("row_count")
    if recorded is not None and recorded != len(rows):
        problems.append(f"metadata says {recorded} rows, file holds {len(rows)}")

    identifiers = [r["chebi_id"] for r in rows]
    if len(set(identifiers)) != len(identifiers):
        problems.append("the table has duplicate chebi_id rows")
    if identifiers != sorted(identifiers, key=lambda c: int(c.split(":")[1])):
        problems.append("rows are not in ascending CHEBI id order")

    if cited is None:
        if records_dir is None:
            raise ValueError("check() needs either records_dir or cited")
        cited = cited_chebi_ids(records_dir)
    cited = set(cited)
    missing = sorted(cited - set(identifiers), key=lambda c: int(c.split(":")[1]))
    if missing:
        problems.append(
            f"{len(missing)} CHEBI id(s) cited by the corpus are absent from the "
            f"table, so those rows render without a formula: "
            f"{', '.join(missing[:10])}{' ...' if len(missing) > 10 else ''}"
        )

    print(f"{out.relative_to(REPO_ROOT)}: {len(rows)} rows, {len(cited)} cited by the corpus")
    if problems:
        print(f"\n{len(problems)} problem(s):", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        print("\nRebuild with: just fetch-chebi-properties --apply", file=sys.stderr)
        return 1
    print("✓ packaged, complete for every cited id, and consistent with its metadata")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--records-dir", type=Path, default=DEFAULT_RECORDS)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--apply", action="store_true", help="Write. Default is preview.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify the packaged table offline. No network, no writes.",
    )
    parser.add_argument("--limit", type=int, default=0, help="Fetch at most N terms.")
    parser.add_argument("--rate-limit", type=float, default=0.15, help="Seconds between calls.")
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    if args.check:
        return check(args.records_dir, args.out)

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
                    "fetched": datetime.now(timezone.utc).isoformat(),
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
