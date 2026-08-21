#!/usr/bin/env python3
"""Set every ingredient's `term.label` to its ontology term's real label (#259).

`term.label` is meant to be the label of the term in `term.id`. Across the corpus it is
mostly the ingredient string from the source recipe instead, so the same id appears under
many different labels and a reviewer cannot tell by eye whether an id is right. That is
not a cosmetic problem: it is why the wrong-compound groundings in #256/#257 went
unnoticed for so long -- `CHEBI:86463` labelled `magnesium sulfate heptahydrate` looks
correct until you learn CHEBI:86463 is potassium aluminium sulfate.

Before this ran, of 145,453 CHEBI-grounded rows:

    62,831  label disagrees with CHEBI
    46,785  correct
    20,505  differs only in case
    15,332  empty

Nothing is lost: the ingredient's own string stays in `preferred_term`, which is where it
belongs. This only overwrites the *ontology's* field with the ontology's value.

ORDER MATTERS, and this is the part worth stating plainly. Refilling labels makes every
label agree with its id -- including the ids that are WRONG. The label/name disagreement
is currently the only visible signal that a grounding is bad, so refilling first would
have silently entrenched every remaining error. Auditing the name-vs-term hydration
mismatch first surfaced 258 more rows to correct (`Na2-EDTA x 2 H2O` grounded to *EDTA
disodium salt (anhydrous)*, and so on); those were fixed BEFORE this ran.

An id the ontology cannot resolve is left completely alone rather than blanked -- an
unresolvable id is a finding, and erasing its label would hide it.

Read-only by default; `--apply` writes.

Usage::

    just refill-term-labels                    # report
    just refill-term-labels --limit 1 --apply  # canary
    just refill-term-labels --apply
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
NORMALIZED = REPO / "data" / "normalized_yaml"

# Ontologies we can resolve offline via oaklib. A prefix absent here is left untouched.
ADAPTERS = {"CHEBI": "sqlite:obo:chebi", "FOODON": "sqlite:obo:foodon",
            "UBERON": "sqlite:obo:uberon", "ENVO": "sqlite:obo:envo"}

ID_LINE = re.compile(r"^(\s*)id:\s*(\S+)\s*$")
LABEL_LINE = re.compile(r"^(\s*)label:\s*(.*)$")
# A YAML key line, used to tell a folded continuation from the next field.
KEY_LINE = re.compile(r"^\s*(?:-\s+)?[\w.-]+:")


def _continuation_span(lines: list[str], start: int, indent: str) -> int:
    """How many lines after `start` belong to the folded scalar opened there.

    PyYAML writes a long label as a folded plain scalar:

        label: (2R,4S,5R,6R)-5-Acetamido-2-[...]oxane-2-carboxylic
          acid

    Replacing only the `label:` line orphaned the continuation, which YAML then
    folded into whatever value preceded it on the next read — so the label gained
    a trailing ` acid`, and every run added another. One record had reached
    `...carboxylic acid acid acid` before this was found (#314). 67 records carry
    a multi-line label and were all corruptible.
    """
    count = 0
    for line in lines[start + 1:]:
        if not line.strip():
            break
        if KEY_LINE.match(line):
            break
        if len(line) - len(line.lstrip()) <= len(indent):
            break
        count += 1
    return count


class Labels:
    """Ontology labels, resolved once per id and cached."""

    def __init__(self) -> None:
        self._adapters: dict[str, object] = {}
        self._cache: dict[str, str | None] = {}

    def _adapter(self, prefix: str):
        if prefix not in self._adapters:
            handle = ADAPTERS.get(prefix)
            try:
                from oaklib import get_adapter
                self._adapters[prefix] = get_adapter(handle) if handle else None
            except Exception:                                    # noqa: BLE001
                self._adapters[prefix] = None
        return self._adapters[prefix]

    def get(self, term_id: str) -> str | None:
        """The real label, or None when it cannot be resolved (leave the row alone)."""
        if term_id not in self._cache:
            prefix = term_id.split(":")[0]
            adapter = self._adapter(prefix)
            try:
                self._cache[term_id] = (adapter.label(term_id) or None) if adapter else None
            except Exception:                                    # noqa: BLE001
                self._cache[term_id] = None
        return self._cache[term_id]


def _label_line(indent: str, value: str) -> str:
    """`<indent>label: <value>` emitted the way record_io would have emitted it.

    Two wrong answers were tried first. `yaml.dump("water")` returns "water\n...\n" --
    the trailing document-end marker corrupts the file, and the run silently rewrites
    nothing because every write fails its own re-parse. `json.dumps` is always valid
    YAML but double-quotes EVERY label, which diverges from the corpus convention and
    breaks test_record_io's byte-identical round-trip check.

    Dumping a one-key mapping with the corpus's own DUMP_KWARGS gets PyYAML to decide
    quoting exactly as `write_record` would: bare when the scalar is plain, quoted only
    when it has to be.
    """
    from record_io import DUMP_KWARGS
    kwargs = {k: v for k, v in DUMP_KWARGS.items() if k != "sort_keys"}
    body = yaml.dump({"label": value}, sort_keys=False, **kwargs).rstrip("\n")
    return "".join(f"{indent}{line}\n" for line in body.splitlines())


def refill_text(text: str, labels: Labels) -> tuple[str, Counter]:
    """Rewrite `label:` lines that follow an `id:` line at the same indent.

    Line-based rather than a YAML round-trip for the reason established in #257:
    re-dumping reflows every long `notes:` string, turning a one-field change into a
    whole-file diff and burying the real edit in review.
    """
    lines = text.splitlines(keepends=True)
    out = list(lines)
    stats: Counter = Counter()
    pending: tuple[str, str] | None = None          # (indent, new_label)
    for n, line in enumerate(lines):
        m = ID_LINE.match(line)
        if m:
            real = labels.get(m.group(2))
            pending = (m.group(1), real) if real else None
            if real is None:
                stats["unresolvable id (left alone)"] += 1
            continue
        if pending:
            ml = LABEL_LINE.match(line)
            if ml and ml.group(1) == pending[0]:
                current = ml.group(2).strip().strip("'\"")
                new = pending[1]
                want = _label_line(pending[0], new)
                # Compare the whole rendered BLOCK, not just the first line: a
                # folded label spans several lines, and comparing one of them to a
                # multi-line `want` never matches, so an already-correct corpus
                # reported every folded label as "corrected" and rewrote it. The
                # output was stable, but the summary a human reads before running
                # --apply was not.
                span = _continuation_span(lines, n, ml.group(1))
                block = "".join(lines[n:n + span + 1])
                # Rendered LINE not stripped VALUE: a correct label quoted
                # differently from the corpus convention still needs rewriting.
                if block == want:
                    stats["already correct"] += 1
                else:
                    stats["empty -> filled" if not current
                          else ("requoted" if current == new else "corrected")] += 1
                    out[n] = want
                    # Blank the folded continuation this label opened; `want`
                    # already carries the full value, correctly re-folded.
                    for extra in range(1, span + 1):
                        out[n + extra] = ""
            pending = None
    return "".join(out), stats


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED)
    args = ap.parse_args(argv)

    labels = Labels()
    totals: Counter = Counter()
    changed = 0
    for path in sorted(args.yaml_dir.resolve().rglob("*.yaml")):
        try:
            text = path.read_text(errors="replace")
        except OSError:
            continue
        if "label:" not in text:
            continue
        new_text, stats = refill_text(text, labels)
        totals.update(stats)
        if new_text == text:
            continue
        try:
            yaml.safe_load(new_text)
        except yaml.YAMLError as exc:
            print(f"  SKIP {path.name} — edit would break YAML: {exc}", file=sys.stderr)
            continue
        changed += 1
        if args.apply:
            path.write_text(new_text)
        if args.limit and changed >= args.limit:
            break

    print(f"{'Rewrote' if args.apply else 'Would rewrite'} labels in {changed} record(s).")
    for k, v in totals.most_common():
        print(f"  {v:8d}  {k}")
    if not args.apply:
        print("\nReport only. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
