#!/usr/bin/env python3
"""Keep `medium_type` populated and derived from `composition_type` (#165).

`medium_type` is a MAINTAINED compatibility axis, not a vestige. `kgx_export`
emits one edge per record from it (`medium_to_type_edge`), so a record missing the
slot silently contributes no type edge to the knowledge graph — no error, no
warning, just an absent edge among ~11,092. `browser_export` publishes it as a
field. Keeping it correct is therefore curation work, not tidying.

## The derivation

The mapping is READ FROM THE SCHEMA, not hardcoded here. Each `MediumTypeEnum`
value documents its own relationship to the composition axis ("Migrates to
composition_type=UNDEFINED"), and this script inverts that:

    composition_type=DEFINED       -> medium_type=DEFINED
    composition_type=UNDEFINED     -> medium_type=COMPLEX
    composition_type=SEMI_DEFINED  -> medium_type=COMPLEX

SEMI_DEFINED is #171's refinement of UNDEFINED; the single-valued slot cannot
express it, so it collapses to COMPLEX. That is a real loss of resolution, and it
is the reason composition_type — not this slot — is the primary axis for curation.

## What is NOT derived

`BUFFER` and `NEGATIVE_CONTROL` have no composition_type counterpart:
`specialized/pbs.yaml` and `specialized/water.yaml` carry no composition_type at
all, and MediumFunctionalRoleEnum has no such values. They are curated directly
and this script leaves them alone. Deriving over them would erase the only
classification those records have.

Report-only by default. `--apply` writes, and only ever writes the derived value
onto records that are missing it or contradict the schema mapping.

Usage::

    just curate-medium-type              # report drift
    just curate-medium-type --apply      # stamp it
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
from record_kinds import is_solution_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
SCHEMA = REPO / "src" / "culturemech" / "schema" / "culturemech.yaml"

# Values curated directly rather than derived — they describe what the record is
# FOR, which the composition axis does not capture.
DIRECTLY_CURATED = frozenset({"BUFFER", "NEGATIVE_CONTROL"})


def schema_mapping(schema_path: Path = SCHEMA) -> dict[str, str]:
    """medium_type -> composition_type, parsed from the schema's own prose."""
    doc = yaml.safe_load(schema_path.read_text())
    pv = doc["enums"]["MediumTypeEnum"]["permissible_values"]
    out: dict[str, str] = {}
    for name, body in pv.items():
        m = re.search(r"Migrates to composition_type=(\w+)",
                      str((body or {}).get("description") or ""))
        if m:
            out[name] = m.group(1)
    return out


def inverse_mapping(mapping: dict[str, str]) -> dict[str, str]:
    """composition_type -> the medium_type to stamp.

    Several composition values collapse onto one medium_type (UNDEFINED and
    SEMI_DEFINED both give COMPLEX), so the inverse is many-to-one. SEMI_DEFINED is
    added explicitly because the schema does not state it: it postdates this enum.
    """
    inv = {v: k for k, v in mapping.items()}
    if "UNDEFINED" in inv:
        inv.setdefault("SEMI_DEFINED", inv["UNDEFINED"])
    return inv


def expected_medium_type(doc: dict[str, Any], inv: dict[str, str]) -> str | None:
    ct = doc.get("composition_type")
    return inv.get(str(ct)) if ct else None


def assess(doc: dict[str, Any], mapping: dict[str, str], inv: dict[str, str]) -> str | None:
    """Return the reason this record needs stamping, or None when it is correct."""
    current = doc.get("medium_type")
    if current is not None and str(current) in DIRECTLY_CURATED:
        return None
    want = expected_medium_type(doc, inv)
    if want is None:
        # No composition_type to derive from. Only a problem if the slot is empty
        # too — otherwise the record is curated directly, like pbs/water.
        return "no composition_type and no medium_type" if current is None else None
    if current is None:
        return f"missing; composition_type={doc.get('composition_type')} -> {want}"
    expected_composition = mapping.get(str(current))
    ct = str(doc.get("composition_type"))
    if expected_composition is None:
        return None
    if ct == expected_composition or (expected_composition == "UNDEFINED"
                                      and ct == "SEMI_DEFINED"):
        return None
    return f"{current} contradicts composition_type={ct} -> {want}"


def scan_parsed(records, mapping: dict[str, str], inv: dict[str, str]
                ) -> list[tuple[Path, dict[str, Any], str, str | None]]:
    """Drift among already-parsed records.

    Split out so the corpus guard can use the session-scoped fixture rather than
    re-parsing all ~15,900 files, which cost 328s (#191).
    """
    out = []
    for path, doc in records:
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        reason = assess(doc, mapping, inv)
        if reason:
            out.append((path, doc, reason, expected_medium_type(doc, inv)))
    return out


def scan(normalized: Path, mapping: dict[str, str], inv: dict[str, str]
         ) -> list[tuple[Path, dict[str, Any], str, str | None]]:
    records = []
    for path in sorted(normalized.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        records.append((path, doc))
    return scan_parsed(records, mapping, inv)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--schema", type=Path, default=SCHEMA)
    ap.add_argument("--apply", action="store_true",
                    help="Write the derived medium_type. Default is report-only.")
    args = ap.parse_args(argv)

    mapping = schema_mapping(args.schema)
    if not mapping:
        print("No 'Migrates to composition_type=' found in the schema; refusing to "
              "guess a mapping.", file=sys.stderr)
        return 1
    inv = inverse_mapping(mapping)
    print(f"Derivation (from the schema): "
          f"{', '.join(f'{k}->{v}' for k, v in sorted(inv.items()))}")
    print(f"Curated directly, never derived: {', '.join(sorted(DIRECTLY_CURATED))}\n")

    drift = scan(args.normalized_dir, mapping, inv)
    if not drift:
        print("All records populated and consistent with composition_type.")
        return 0

    print(f"{len(drift)} record(s) need attention:")
    for path, _doc, reason, _want in drift[:40]:
        print(f"  {str(path.relative_to(args.normalized_dir))[:52]:54s} {reason}")
    if len(drift) > 40:
        print(f"  ... and {len(drift) - 40} more")

    if not args.apply:
        print("\nReport only. Re-run with --apply to stamp the derived value.")
        return 0

    written = 0
    for path, _doc, _reason, want in drift:
        if want is None:
            continue  # nothing to derive from; needs a curator, not a script
        text = path.read_text()
        if re.search(r"^medium_type:.*$", text, re.M):
            new = re.sub(r"^medium_type:.*$", f"medium_type: {want}", text, count=1, flags=re.M)
        else:
            # Insert after composition_type so the two axes read together.
            new, n = re.subn(r"^(composition_type:.*)$", rf"\1\nmedium_type: {want}",
                             text, count=1, flags=re.M)
            if not n:
                print(f"  SKIP {path.name}: no anchor to insert after", file=sys.stderr)
                continue
        if new != text:
            path.write_text(new)
            written += 1
    print(f"\nStamped {written} record(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
