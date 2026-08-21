#!/usr/bin/env python3
"""Adopt MIM's published grounding where we have none (#308, #256).

`just audit-mim-sssom` reports three things; this applies only the cheapest one,
`MISSING_GROUNDING` — a name MediaIngredientMech has already mapped `exactMatch`
to a CHEBI term and we left bare. There is nothing to reconcile: MIM decided, the
mapping is published, and we are simply not carrying it.

It deliberately does NOT touch the other two findings. `DIVERGENT` runs both ways
— #256 records cases where our hydrate is the better term and cases where MIM's
neutral acid is — and `INTERNAL_SPLIT` needs someone to pick which of our own ids
is right. Both are curation, not application.

## Why this matters beyond tidiness

`kgx_export` resolves an ingredient with `_get_term_id(ingredient, ["term","id"])`
and returns `None` without it, so an ungrounded ingredient produces **no edge at
all**. The 62 media whose compositions were recovered in #299 currently
contribute their medium node and nothing about what is in them.

## Which slot gets written

Two shapes exist in the corpus and the difference is load-bearing:

    no `term`, no `chebi_term`   ->  write `term`      (812 rows)
    `term: mediadive.compound:N` ->  write `chebi_term` (11 rows)

MediaDive-derived records keep the source's own id in `term` and the ontology
grounding in `chebi_term`; overwriting `term` there would destroy the provenance
link. Writing `chebi_term` matches how those records already carry CHEBI.

A row that already has a CHEBI in either slot is never touched, whatever MIM
says — that is `DIVERGENT`, and it is not this script's decision to make.

`term.label` is MIM's `object_label`, i.e. the ONTOLOGY label, not the ingredient
string. `just check-id-labels` is what adjudicates labels, and seeding it with the
ingredient name is the drift #256 records.

Dry-run by default. Usage::

    just apply-mim-groundings              # show what would change
    just apply-mim-groundings --limit 1    # canary one record
    just apply-mim-groundings --apply
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_mim_sssom_divergence import (  # noqa: E402
    DEFAULT_SSSOM,
    NORMALIZED,
    load_sssom,
    normalize_name,
    our_chebi,
    reagent_rows,
)
from record_io import write_record  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
CURATOR = "apply_mim_groundings.py"


def target_slot(row: dict[str, Any]) -> str | None:
    """Which slot to write, or None when this row must be left alone."""
    if our_chebi(row)[0]:
        return None  # already grounded; a disagreement is DIVERGENT, not ours
    term = row.get("term")
    if isinstance(term, dict) and term.get("id"):
        # A non-CHEBI id is a source anchor (mediadive.compound:N). Keep it and
        # put the ontology grounding beside it, as those records already do.
        return "chebi_term"
    return "term"


def corpus_opinions(normalized_dir: Path) -> dict[str, set[str]]:
    """``{normalized name: every CHEBI id we already use for it}``.

    Needed because a name can be grounded on some rows and bare on others, and a
    per-row view cannot see that. Grounding `maltose`'s bare rows to MIM's
    CHEBI:17306 while 40 rows already said CHEBI:18167 turned a clean
    disagreement into an INTERNAL_SPLIT — filling gaps must not manufacture one.
    """
    opinions: dict[str, set[str]] = {}
    for path in sorted(normalized_dir.glob("*/*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            continue
        if not isinstance(doc, dict):
            continue
        for _location, row in reagent_rows(doc):
            name = row.get("preferred_term")
            if not isinstance(name, str) or not name.strip():
                continue
            chebi, _label = our_chebi(row)
            if chebi:
                opinions.setdefault(normalize_name(name), set()).add(chebi)
    return opinions


def groundable(mim: dict[str, tuple[str, str]],
               opinions: dict[str, set[str]]) -> dict[str, tuple[str, str]]:
    """MIM mappings safe to apply: we hold no conflicting opinion on the name.

    Skipped are names where the corpus already grounds to something MIM does not
    say. That is DIVERGENT — #256 records that it runs both ways, so it is a
    curation call and adopting MIM by default would quietly overrule us.
    """
    return {
        name: entry for name, entry in mim.items()
        if not (opinions.get(name, set()) - {entry[0]})
    }


def apply_to_record(doc: dict[str, Any], mim: dict[str, tuple[str, str]]
                    ) -> list[tuple[str, str, str]]:
    """Ground what we can in one record. Returns (name, chebi, slot) per change."""
    changes: list[tuple[str, str, str]] = []
    for _location, row in reagent_rows(doc):
        name = row.get("preferred_term")
        if not isinstance(name, str) or not name.strip():
            continue
        entry = mim.get(normalize_name(name))
        if not entry:
            continue
        slot = target_slot(row)
        if slot is None:
            continue
        chebi_id, chebi_label = entry
        row[slot] = {"id": chebi_id, "label": chebi_label}
        _drop_stale_no_mapping_note(row)
        changes.append((name.strip(), chebi_id, slot))
    return changes


# Two rows carry a note that the grounding makes false. Left alone it would sit
# directly beside the term it denies.
_STALE_NOTE = "Ontology mapping not yet available"


def _drop_stale_no_mapping_note(row: dict[str, Any]) -> None:
    """Remove the "no mapping yet" clause once a mapping is written.

    Only that clause: these notes are semicolon-joined and the rest ("From CCAP
    Medium MR_MHY.pdf", "Curated from ...") is provenance worth keeping.
    """
    note = row.get("notes")
    if not isinstance(note, str) or _STALE_NOTE.lower() not in note.lower():
        return
    kept = [part.strip() for part in note.split(";")
            if _STALE_NOTE.lower() not in part.strip().lower()]
    remainder = "; ".join(part for part in kept if part)
    if remainder:
        row["notes"] = remainder
    else:
        del row["notes"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--sssom", type=Path, default=DEFAULT_SSSOM)
    parser.add_argument("--limit", type=int, default=0,
                        help="Stop after N records. Use 1 to canary.")
    parser.add_argument("--apply", action="store_true",
                        help="Write the records. Without this, nothing changes.")
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    mim, version = load_sssom(args.sssom)
    opinions = corpus_opinions(args.normalized_dir)
    safe = groundable(mim, opinions)
    skipped = len(mim) - len(safe)
    print(f"MIM SSSOM mapping_set_version: {version}")
    print(f"  {len(safe)} mapping(s) safe to apply; {skipped} skipped because the "
          f"corpus already grounds that name differently (DIVERGENT — curation)\n")
    mim = safe

    records = rows = 0
    slots: Counter = Counter()
    names: Counter = Counter()
    for path in sorted(args.normalized_dir.glob("*/*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            continue
        if not isinstance(doc, dict):
            continue

        changes = apply_to_record(doc, mim)
        if not changes:
            continue

        records += 1
        rows += len(changes)
        for name, _chebi, slot in changes:
            slots[slot] += 1
            names[name] += 1

        doc.setdefault("curation_history", []).append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "curator": CURATOR,
            "action": "Adopted MIM published grounding",
            "notes": (f"Grounded {len(changes)} ingredient(s) from MIM's "
                      f"ingredient_mappings.sssom.tsv ({version}), exactMatch only, "
                      f"where this record carried no CHEBI term (#308)."),
        })
        print(f"  {path.name:<44} +{len(changes)}")
        if args.apply:
            write_record(path, doc)
        if args.limit and records >= args.limit:
            break

    verb = "Grounded" if args.apply else "Would ground"
    print(f"\n{verb} {rows} row(s) across {records} record(s), "
          f"{len(names)} distinct ingredient name(s).")
    print(f"  slots written: {dict(slots)}")
    if not args.apply:
        print("Dry run — nothing written. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
