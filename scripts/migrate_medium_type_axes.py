"""Backfill the multi-axis media-type vocabulary from the single-valued medium_type slot.

medium_type (MediumTypeEnum) conflated three orthogonal properties into one
single-valued slot. This migration derives the new axis slots from it without
removing medium_type (kept for backward compatibility):

    medium_type        -> new axis slot
    -----------        -------------------------------------
    DEFINED            composition_type: DEFINED
    COMPLEX            composition_type: UNDEFINED
    MINIMAL            nutritional_class: MINIMAL
    SELECTIVE          functional_role: [SELECTIVE]
    DIFFERENTIAL       functional_role: [DIFFERENTIAL]
    ENRICHMENT         functional_role: [ENRICHMENT]
    BUFFER             (no axis mapping — not a growth medium; left as-is)
    NEGATIVE_CONTROL   (no axis mapping — left as-is)

Only deterministic, source-faithful mappings are applied. Nutritional level
(RICH vs GENERAL_PURPOSE) and most functional roles cannot be inferred from
medium_type alone and are left for curators. Records with no medium_type are
reported but not modified.

Idempotent: an axis slot is only written if absent; medium_type is never changed.
New slots are inserted right after medium_type to match schema field order.

Dry-run by default. Examples:
    python scripts/migrate_medium_type_axes.py                 # whole corpus, dry-run
    python scripts/migrate_medium_type_axes.py --apply         # write changes
    python scripts/migrate_medium_type_axes.py --apply \
        data/normalized_yaml/bacterial/r2a_medium.yaml ...     # restrict to paths
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml as pyyaml

try:
    from ruamel.yaml import YAML as RuamelYAML
except ImportError:  # pragma: no cover
    RuamelYAML = None

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
from culturemech.curate.curation_event import record_curation_event  # noqa: E402

ROUND_TRIP_YAML = RuamelYAML() if RuamelYAML else None
if ROUND_TRIP_YAML:
    ROUND_TRIP_YAML.default_flow_style = False
    ROUND_TRIP_YAML.preserve_quotes = True

DATA_ROOT = REPO_ROOT / "data" / "normalized_yaml"
CURATOR = "medium-type-axis-migration-v1.0"

# medium_type value -> (axis_slot, value). functional_role values are wrapped in a list.
COMPOSITION = {"DEFINED": "DEFINED", "COMPLEX": "UNDEFINED"}
NUTRITIONAL = {"MINIMAL": "MINIMAL", "RICH": "RICH"}
FUNCTIONAL = {"SELECTIVE": "SELECTIVE", "DIFFERENTIAL": "DIFFERENTIAL", "ENRICHMENT": "ENRICHMENT"}
# BUFFER / NEGATIVE_CONTROL intentionally have no axis mapping.


def load_yaml(path: Path) -> dict[str, Any]:
    data = ROUND_TRIP_YAML.load(path) if ROUND_TRIP_YAML else pyyaml.safe_load(path.read_text())
    return data or {}


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    """Round-trip write. Refuses to write at all without ruamel (#153).

    The old fallback here was `pyyaml.safe_dump`, which reflows the whole record
    and drops comments — measured at a 37-line diff on a 164-line record where
    ruamel produces 1. Reached only via a bare `except ImportError`, that turned
    a missing transitive dependency into silent corpus-wide churn, which is the
    failure #141 describes. Refusing is the safe direction: the caller loses a
    write, not the provenance in the file.
    """
    if not ROUND_TRIP_YAML:
        raise RuntimeError(
            f"refusing to write {path}: ruamel.yaml is unavailable, and the pyyaml "
            "fallback reflows records and strips comments. Install it "
            "(`uv sync`) — it is a declared dependency — or use --text, which "
            "splices lines in without a YAML writer."
        )
    with path.open("w") as handle:
        ROUND_TRIP_YAML.dump(data, handle)
    path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")


def _set_after(doc: dict[str, Any], anchor: str, key: str, value: Any) -> None:
    """Insert key=value immediately after `anchor` when possible (ruamel), else append."""
    if hasattr(doc, "insert") and anchor in doc:
        keys = list(doc.keys())
        doc.insert(keys.index(anchor) + 1, key, value)
    else:
        doc[key] = value


def plan_record(doc: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    """Return (additions, change_notes) derivable from medium_type. Non-mutating."""
    medium_type = doc.get("medium_type")
    additions: dict[str, Any] = {}
    notes: list[str] = []
    if not medium_type:
        return additions, notes
    if medium_type in COMPOSITION and "composition_type" not in doc:
        additions["composition_type"] = COMPOSITION[medium_type]
        notes.append(f"composition_type={COMPOSITION[medium_type]}")
    if medium_type in NUTRITIONAL and "nutritional_class" not in doc:
        additions["nutritional_class"] = NUTRITIONAL[medium_type]
        notes.append(f"nutritional_class={NUTRITIONAL[medium_type]}")
    if medium_type in FUNCTIONAL and "functional_role" not in doc:
        additions["functional_role"] = [FUNCTIONAL[medium_type]]
        notes.append(f"functional_role=[{FUNCTIONAL[medium_type]}]")
    return additions, notes


def apply_additions(doc: dict[str, Any], additions: dict[str, Any]) -> None:
    # Insert in schema order: composition_type, nutritional_class, functional_role after medium_type.
    anchor = "medium_type"
    for key in ("composition_type", "nutritional_class", "functional_role"):
        if key in additions:
            _set_after(doc, anchor, key, additions[key])
            anchor = key


def _additions_as_lines(additions: dict[str, Any]) -> list[str]:
    """Render additions as top-level YAML lines, in schema order."""
    out: list[str] = []
    for key in ("composition_type", "nutritional_class", "functional_role"):
        if key not in additions:
            continue
        value = additions[key]
        if isinstance(value, list):
            out.append(f"{key}:")
            out.extend(f"- {item}" for item in value)
        else:
            out.append(f"{key}: {value}")
    return out


def apply_additions_text(path: Path, additions: dict[str, Any]) -> bool:
    """Insert axis lines right after the top-level `medium_type:` line, no reformatting.

    Returns False (and leaves the file untouched) if no top-level medium_type line is
    found. Avoids the line-rewrapping churn a full ruamel round-trip would introduce
    across the corpus; provenance for the bulk pass lives in the commit, not a per-record
    curation event.
    """
    text = path.read_text()
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("medium_type:") and not line[:1].isspace():
            insert = _additions_as_lines(additions)
            lines[i + 1 : i + 1] = insert
            path.write_text("\n".join(lines))
            return True
    return False


def iter_paths(args_paths: list[str]) -> list[Path]:
    if args_paths:
        return [REPO_ROOT / p if not Path(p).is_absolute() else Path(p) for p in args_paths]
    return sorted(DATA_ROOT.rglob("*.yaml"))


def parse_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", help="Specific YAML files (default: whole corpus).")
    ap.add_argument("--apply", action="store_true", help="Write changes (default: dry-run).")
    ap.add_argument("--text", action="store_true",
                    help="Churn-free line insertion (no reformat, no per-record curation "
                         "event). Recommended for the bulk corpus pass; provenance lives in "
                         "the commit. Without it, a ruamel round-trip rewrites the whole file "
                         "and records a curation event (use for small, targeted runs).")
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    src_counts: Counter[str] = Counter()
    add_counts: Counter[str] = Counter()
    changed = 0
    no_medium_type = 0
    unmapped: Counter[str] = Counter()
    scanned = 0

    for path in iter_paths(args.paths):
        try:
            # Text mode only needs a read-only parse to plan; fast pyyaml avoids the
            # ruamel load cost and any reformatting on read.
            doc = pyyaml.safe_load(path.read_text()) if args.text else load_yaml(path)
        except Exception as exc:  # noqa: BLE001
            print(f"  SKIP (parse error) {path}: {exc}", file=sys.stderr)
            continue
        if not isinstance(doc, dict):
            continue
        scanned += 1
        mt = doc.get("medium_type")
        if not mt:
            no_medium_type += 1
            continue
        src_counts[mt] += 1
        additions, notes = plan_record(doc)
        if mt not in COMPOSITION and mt not in NUTRITIONAL and mt not in FUNCTIONAL:
            unmapped[mt] += 1
        if not additions:
            continue
        if args.apply:
            if args.text:
                if not apply_additions_text(path, additions):
                    print(f"  SKIP (no top-level medium_type line) {path}", file=sys.stderr)
                    continue
            else:
                apply_additions(doc, additions)
                record_curation_event(
                    doc,
                    curator=CURATOR,
                    action="Backfilled multi-axis media type",
                    notes="Derived " + "; ".join(notes) + " from medium_type="
                    + str(mt) + ".",
                )
                write_yaml(path, doc)
        for key in additions:
            add_counts[key] += 1
        changed += 1

    verb = "Applied" if args.apply else "Would apply (dry-run)"
    print(f"Scanned: {scanned}")
    print(f"medium_type present: {sum(src_counts.values())} | missing: {no_medium_type}")
    print("Source medium_type distribution:")
    for k, v in src_counts.most_common():
        print(f"  {k:16} {v}")
    print(f"{verb} axis backfill to {changed} record(s). New slot writes:")
    for k, v in add_counts.most_common():
        print(f"  {k:18} {v}")
    if unmapped:
        print("medium_type values with no axis mapping (left as-is):")
        for k, v in unmapped.most_common():
            print(f"  {k:16} {v}")
    if not args.apply:
        print("\nDry-run only. Re-run with --apply to write.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
