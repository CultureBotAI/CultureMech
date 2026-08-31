#!/usr/bin/env python3
"""Restore MediaDB ingredient names truncated at a parenthesis (#387).

## What went wrong

`mediadb_fetcher.py` split SQL INSERT rows with `re.findall(r'\\(([^)]+)\\)', ...)`.
`[^)]+` stops at the FIRST closing paren, so

    (16413,NULL,NULL,'Iron(III) chloride','','24380','30808','FeCl3')

parsed as the four fields `16413, NULL, NULL, 'Iron(III` — and that fragment,
leading quote and all, became the ingredient's `preferred_term` in 75 recipes.
Chemical names carry parentheses constantly (oxidation states, stereo
descriptors), so the bug hit precisely the compounds hardest to guess back.

## Why the fragment alone is not enough

`'(S` is `(S)-Malate` in four recipes and `(S)-Lactate` in two others. A global
prefix->name table would silently pick one and be wrong about the rest, so
resolution is per record:

1. the record's `media_term.term.id` gives its MediaDB medium id;
2. `media_compounds` gives that medium's actual compound list;
3. the fragment must prefix exactly one of those compounds' real names;
4. where the fragment still matches more than one, the recorded concentration
   must equal that compound's `Amount_mM` in the dump.

An ingredient that does not resolve to exactly one compound is left untouched
and reported. Names are read through the fixed fetcher rather than a second
parser, so there is one implementation of the SQL grammar, not two.

Preview by default. `--apply` writes.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter

# `timezone.utc`, not `datetime.UTC`: the latter is 3.11+ and this project
# supports >=3.10.
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from record_io import write_record  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
from culturemech.fetch.mediadb_fetcher import MediaDBFetcher  # noqa: E402

DEFAULT_RECORDS = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_DUMP = REPO_ROOT / "data" / "raw" / "mediadb" / "media_database.07Oct2015.sql"

CURATOR = "repair_mediadb_names.py"
ACTION = "REPAIRED_MEDIADB_TRUNCATED_NAME"


def looks_truncated(name: str) -> bool:
    """A `preferred_term` that is a parse fragment rather than a chemical name.

    The tell is the leading apostrophe: it is the SQL string's opening quote,
    kept because the closing one was never reached. Names that merely *end* in
    a prime are real — `Premithramycin A2'`, `Nebramycin factor 5'` — so only
    the leading quote counts.
    """
    return name.startswith("'")


def load_mediadb(
    dump: Path,
) -> tuple[dict[str, dict[str, str]], dict[str, list[tuple[str, str]]], dict[str, str]]:
    """(compounds by id, medium id -> [(compound id, amount_mM)], medium names)."""
    fetcher = MediaDBFetcher(output_dir=dump.parent)
    if not fetcher.parse_sql_dump(dump):
        raise SystemExit(f"Could not parse {dump}")

    compositions: dict[str, list[tuple[str, str]]] = {}
    for medium_id, entries in fetcher.media_compositions.items():
        compositions[medium_id] = [
            (str(entry.get("compound_id") or ""), str(entry.get("concentration") or ""))
            for entry in entries
        ]
    medium_names = {m["id"]: str(m.get("name") or "").strip() for m in fetcher.media}
    return fetcher.compounds, compositions, medium_names


def medium_id(record: dict[str, Any]) -> str | None:
    identifier = ((record.get("media_term") or {}).get("term") or {}).get("id") or ""
    return identifier.split(":", 1)[1] if identifier.startswith("MEDIADB:") else None


def _same_amount(recorded: Any, dump_amount: str) -> bool:
    try:
        return abs(float(recorded) - float(dump_amount)) < 1e-9
    except (TypeError, ValueError):
        return False


def resolve(
    fragment: str,
    concentration: Any,
    pool: list[tuple[str, str]],
    compounds: dict[str, dict[str, str]],
) -> tuple[str | None, str]:
    """The one compound name this fragment can mean, or (None, why not)."""
    prefix = fragment.lstrip("'")
    if not prefix:
        return None, "fragment is only a quote"

    matches = [
        (compound_id, compounds[compound_id]["name"], amount)
        for compound_id, amount in pool
        if compound_id in compounds and compounds[compound_id]["name"].startswith(prefix)
    ]
    if not matches:
        return None, f"no compound in this medium starts with {prefix!r}"

    names = {name for _, name, _ in matches}
    if len(names) == 1:
        return names.pop(), ""

    narrowed = {name for _, name, amount in matches if _same_amount(concentration, amount)}
    if len(narrowed) == 1:
        return narrowed.pop(), ""
    return None, f"{len(names)} candidates at this medium: {sorted(names)[:4]}"


def damaged_medium_name(value: str) -> bool:
    """Whether a stored medium name shows parser damage.

    Two shapes, from the two bugs:

    * a leading quote, from the record splitter stopping at a paren —
      `'Defined freshwater medium (CoSO4`;
    * a glued-on `','...` tail, from the field splitter losing quote tracking
      at an apostrophe — `Spizizen's medium ... Nakano et al','N`.

    Deliberately narrow. The medium's MEDIADB id names its row exactly, so the
    dump value could simply be imposed on every record — but that would also
    overwrite deliberate curation. Only values carrying evidence of damage are
    replaced. A name that differs from the dump only by trailing whitespace
    (`'Supplemented BG11 + Glucose '`) is left alone: that is the dump's own
    value, not damage.
    """
    return value.startswith("'") or "','" in value


def repair_medium_name(record: dict[str, Any], true_name: str) -> list[str]:
    """Restore the medium's own name where the same bug truncated it.

    `media_term.term.label` and `original_name` were written from the truncated
    `media_names` row, so `Defined freshwater medium (CoSO4) + 20 mM Iron
    citrate + 113.2 mM Acetate` became `'Defined freshwater medium (CoSO4`.
    That is not merely ugly: 29 distinct media collapse onto that one string,
    and what the truncation removed is exactly what tells them apart.

    Keyed on the record's MEDIADB id alone, so there is no inference here —
    unlike the ingredient case, the id names the row directly.

    `name` is deliberately left alone. It is the record's slug, used for
    matching and deduplication, and renaming 182 of them is a different change
    with different risks.
    """
    changed = []
    term = (record.get("media_term") or {}).get("term") or {}
    if damaged_medium_name(str(term.get("label", ""))):
        term["label"] = true_name
        changed.append("media_term.term.label")
    if damaged_medium_name(str(record.get("original_name", ""))):
        record["original_name"] = true_name
        changed.append("original_name")
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--records-dir", type=Path, default=DEFAULT_RECORDS)
    parser.add_argument("--dump", type=Path, default=DEFAULT_DUMP)
    parser.add_argument("--apply", action="store_true", help="Write. Default is preview.")
    parser.add_argument("--limit", type=int, default=0, help="Stop after N records (0 = all).")
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    if not args.dump.exists():
        print(
            f"{args.dump} is not present. It is a gitignored raw capture; "
            f"restore it before repairing.",
            file=sys.stderr,
        )
        return 1

    compounds, compositions, medium_names = load_mediadb(args.dump)
    print(f"{len(compounds)} compounds, {len(compositions)} media from {args.dump.name}")

    stats: Counter = Counter()
    renames: Counter = Counter()
    failures: list[tuple[str, str, str]] = []

    for path in sorted(args.records_dir.glob("*/*.yaml")):
        record = yaml.safe_load(path.read_text())
        if not isinstance(record, dict):
            continue

        source_id = medium_id(record)
        true_name = medium_names.get(source_id or "", "")
        name_fields = repair_medium_name(record, true_name) if true_name else []
        if name_fields:
            stats["medium_names_repaired"] += 1
            stats["name_fields_repaired"] += len(name_fields)

        damaged = [
            ingredient
            for ingredient in record.get("ingredients") or []
            if isinstance(ingredient, dict)
            and looks_truncated(str(ingredient.get("preferred_term", "")))
        ]
        if damaged:
            stats["records_with_damaged_ingredients"] += 1

        repaired = 0
        if damaged and not source_id:
            for ingredient in damaged:
                failures.append((path.name, str(ingredient["preferred_term"]), "no MEDIADB:<id>"))
        elif damaged:
            pool = compositions.get(source_id, [])
            for ingredient in damaged:
                fragment = str(ingredient["preferred_term"])
                concentration = (ingredient.get("concentration") or {}).get("value")
                name, reason = resolve(fragment, concentration, pool, compounds)
                if not name:
                    failures.append((path.name, fragment, reason))
                    continue
                ingredient["preferred_term"] = name
                renames[(fragment, name)] += 1
                repaired += 1
        stats["ingredients_repaired"] += repaired

        if not repaired and not name_fields:
            continue

        summary = []
        if repaired:
            summary.append(
                f"{repaired} ingredient name(s), resolved against MEDIADB:{source_id}'s own "
                f"compound list by unique prefix match and, where more than one matched, "
                f"an equal Amount_mM"
            )
        if name_fields:
            summary.append(f"the medium's own name in {', '.join(name_fields)}")
        record.setdefault("curation_history", []).append(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "curator": CURATOR,
                "action": ACTION,
                "notes": (
                    f"Restored {' and '.join(summary)}. The MediaDB SQL parser truncated "
                    f"every value containing a parenthesis at that parenthesis; recovered "
                    f"from {args.dump.name}."
                ),
            }
        )
        stats["records_repaired"] += 1
        if args.apply:
            write_record(path, record)
        if args.limit and stats["records_repaired"] >= args.limit:
            break

    verb = "Repaired" if args.apply else "Would repair"
    print(f"\n{verb} {stats['records_repaired']} records")
    for key in sorted(stats):
        print(f"  {key}: {stats[key]}")
    if renames:
        print("\nresolutions:")
        for (fragment, name), count in renames.most_common():
            print(f"  {count:4d}  {fragment!r} -> {name!r}")
    if failures:
        print(f"\n{len(failures)} left untouched:")
        for name, fragment, reason in failures:
            print(f"  {name}: {fragment!r} — {reason}")
    if not args.apply:
        print("\nPreview only. Re-run with --apply to write.")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
