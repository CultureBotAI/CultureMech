#!/usr/bin/env python3
"""Backfill organism_culture_type on records that name target_organisms (#142).

`organism_culture_type` distinguishes a pure-isolate medium (`isolate`) from one
targeting a mixed community (`community`). It is `recommended:`, not `required:`,
so `validate-strict` never flags its absence — and it is unset on 40 of the 50
records that name a target organism.

## Why it is inferable, and where the line is

The enum defines `isolate` as "Pure culture of one or more specific strains" and
`community` as a "Mixed/consortium culture of multiple organisms". The distinction
is the NATURE of the target, not the count: a record naming seven specific gut
strains is still an isolate medium (each grown as a pure culture), while a record
targeting an unnamed consortium/enrichment is a community. So a record whose
target_organisms are specific named strains/species is `isolate`; only a
consortium/community/enrichment descriptor is `community`.

This pass sets `isolate` on records whose targets are specific strains and carry
no community/consortium signal. A record with such a signal is **left for a
curator**, not guessed — the enum's `community` value should be a read assertion,
not an inference from a keyword. (As of #142 no such record exists among the 40,
so every one is set to `isolate`; the guard is for future imports.)

## What this does NOT change

`kgx_export` does not currently read this slot — it emits one `grows_in_medium`
edge per organism regardless (see kgx_export.py). Populating the slot is correct
curation data (yaml_updater already writes it, and it is the natural qualifier a
future organism↔medium edge would carry), but it does not by itself alter the
exported graph today. The issue's claim that isolate and community media "export
identically" is aspirational, not current behaviour.

Report-only by default; `--apply` writes via record_io (minimal diff) and records
a curation event.

Usage::

    just curate-organism-culture-type            # report
    just curate-organism-culture-type --apply     # stamp `isolate`
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import write_record  # noqa: E402

from culturemech.curate.curation_event import record_curation_event  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
SCHEMA = REPO / "src" / "culturemech" / "schema" / "culturemech.yaml"

# A target described as a mixed/consortium/environmental culture rather than a
# specific strain. Such a record is reported for a curator, never auto-set: the
# `community` value must be asserted, not guessed from a keyword. The `[\s_-]?`
# between words matters — record names are slugged with underscores, so a
# `co_culture` medium would slip past a plain `co-?culture` (as one did in #142).
_SEP = r"[\s_-]?"
COMMUNITY_SIGNAL = re.compile(
    r"consorti|communit|microbiom|microbiota|\bsludge\b|metagenom|"
    # `co` + sep + `cult` catches co-culture AND co-cultivation, in either the
    # spaced, hyphenated or underscored (slugged name) form — the separator was
    # the #142 slip, and the stem must not exclude co-cultivation.
    rf"co{_SEP}cult|mixed{_SEP}cultur|enrichment{_SEP}cultur|"
    rf"environmental{_SEP}sample|\brumen\b",
    re.I,
)


def organism_names(doc: dict[str, Any]) -> list[str]:
    """Every human-readable name in target_organisms.

    Each entry is either a bare string or a dict carrying `preferred_term` /
    `name` (the evidence-bearing form). Both shapes appear in the corpus.
    """
    names: list[str] = []
    for org in doc.get("target_organisms") or []:
        if isinstance(org, dict):
            names.append(str(org.get("preferred_term") or org.get("name") or ""))
        else:
            names.append(str(org))
    return names


def classify(doc: dict[str, Any]) -> tuple[str | None, str]:
    """Return (value_to_set, reason). value is None when the record should be
    left untouched — already set, no target_organisms, or a community signal a
    curator must resolve."""
    if not doc.get("target_organisms"):
        return None, "no target_organisms"
    if doc.get("organism_culture_type"):
        return None, "already set"
    names = organism_names(doc)
    blob = " ".join(names) + " " + str(doc.get("name", ""))
    if COMMUNITY_SIGNAL.search(blob):
        return None, "community/consortium signal — leave for a curator"
    n = len([x for x in names if x])
    if n == 0:
        # Entries present but none carry a name — `isolate` would be a guess about
        # a record we cannot actually read. Leave it for a curator.
        return None, "target_organisms present but no organism name — leave for a curator"
    return "isolate", f"{n} specific strain(s) named; no community signal"


def _set_before(doc: dict[str, Any], key: str, value: Any, before: str) -> dict[str, Any]:
    """Return a new dict with `key: value` inserted immediately before `before`,
    preserving order otherwise, so the diff places the slot next to the organisms
    it describes rather than appending it after the curation history."""
    out: dict[str, Any] = {}
    for k, v in doc.items():
        if k == before:
            out[key] = value
        if k != key:
            out[k] = v
    if key not in out:  # `before` absent for some reason: fall back to append
        out[key] = value
    return out


def scan_parsed(records) -> list[tuple[Path, dict[str, Any], str]]:
    """Records needing a value, from already-parsed (path, doc) pairs. Split out so
    the corpus test can reuse a session-scoped fixture instead of re-parsing ~15.9k
    files (#191)."""
    out = []
    for path, doc in records:
        if not isinstance(doc, dict):
            continue
        value, _reason = classify(doc)
        if value is not None:
            out.append((path, doc, value))
    return out


def community_signal_records(records) -> list[tuple[Path, list[str]]]:
    """Records with target_organisms, no culture type, and a community signal —
    the ones this script deliberately does not touch."""
    out = []
    for path, doc in records:
        if not isinstance(doc, dict):
            continue
        value, reason = classify(doc)
        if value is None and reason.startswith("community"):
            out.append((path, organism_names(doc)))
    return out


def scan(normalized: Path) -> tuple[list, list]:
    records = []
    for path in sorted(normalized.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        records.append((path, doc))
    return scan_parsed(records), community_signal_records(records)


def apply_value(path: Path, doc: dict[str, Any], value: str) -> bool:
    """Stamp the slot next to target_organisms, record a curation event, write."""
    n = len([x for x in organism_names(doc) if x])
    doc = _set_before(doc, "organism_culture_type", value, before="target_organisms")
    record_curation_event(
        doc,
        curator="curate_organism_culture_type.py",
        action="SET_ORGANISM_CULTURE_TYPE",
        notes=f"Inferred {value}: {n} specific strain(s) named, no community signal (#142)",
        changes=f"Set organism_culture_type={value} (was unset)",
    )
    return write_record(path, doc)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--apply", action="store_true",
                    help="Write the inferred value. Default is report-only.")
    args = ap.parse_args(argv)

    to_set, community = scan(args.normalized_dir)

    print(f"{len(to_set)} record(s) with target_organisms but no organism_culture_type "
          f"are inferable as `isolate`:")
    for path, _doc, value in to_set[:60]:
        print(f"  {str(path.relative_to(args.normalized_dir))[:56]:58s} -> {value}")
    if len(to_set) > 60:
        print(f"  ... and {len(to_set) - 60} more")

    if community:
        print(f"\n{len(community)} record(s) carry a community/consortium signal and are "
              f"LEFT for a curator (not guessed):")
        for path, names in community:
            print(f"  {str(path.relative_to(args.normalized_dir))[:56]:58s} {names}")

    if not args.apply:
        print("\nReport only. Re-run with --apply to stamp `isolate`.")
        return 0

    written = 0
    for path, doc, value in to_set:
        if apply_value(path, doc, value):
            written += 1
    print(f"\nStamped {written} record(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
