#!/usr/bin/env python3
"""Compare our ingredient groundings against MediaIngredientMech's published SSSOM.

#256 established why this matters and cannot be fixed downstream: kg-microbe's
loader resolves an ingredient with
``best_primary([chebi_id, culturemech_term_id, mim_id, ...])``, so
``culturemech_term_id`` — our ``term.id`` — outranks ``mim_id``. When MIM corrects
a mapping, the consumer still picks ours. MIM can only fix rows we have no opinion
on. The disagreement therefore has to surface *here*, at review time.

MIM publishes ``mappings/ingredient_mappings.sssom.tsv``. Before this script the
only consumer in the repo was ``audit_missing_roles.py``, and only for role
coverage — no grounding path read it at all.

Three findings, each a different decision:

  DIVERGENT          We and MIM both ground this name, to different CHEBI ids.
                     Needs curation, not a bulk overwrite: it runs both ways.
                     #256 catalogues cases where ours is better (a hydrate we
                     model and MIM does not) alongside cases where MIM is
                     (``edta`` → the neutral acid as supplied, rather than our
                     EDTA(2-)).

  INTERNAL_SPLIT     One ingredient name carries several CHEBI ids in OUR corpus.
                     Independent of MIM and often unambiguous — ``dipotassium
                     phosphate`` is CHEBI:131527 on 475 rows and CHEBI:63036 on 1.
                     Where MIM has an opinion it is shown, because it adjudicates.

  MISSING_GROUNDING  MIM grounds this name and we left it ungrounded. The cheapest
                     class to act on: nothing to reconcile, only to adopt.

What "our CHEBI" means. Records carry the grounding in one of two slots, and
reading only one of them gets the wrong answer: MediaDive-derived records put the
source's own id in ``term.id`` (``mediadive.compound:5``) and the ontology
grounding in ``chebi_term.id``. Comparing ``term.id`` to MIM makes 24,400 rows
look divergent when they are not — they simply keep CHEBI in the other slot. So
``chebi_term.id`` wins, falling back to ``term.id`` when it is itself a CHEBI id.

Matching is by normalized ingredient name against MIM's ``subject_label``, over
``skos:exactMatch`` rows only. ``narrowMatch``/``broadMatch``/``closeMatch`` are
deliberately excluded: they assert a relationship, not an identity, and treating
them as a grounding verdict would manufacture disagreements. A MIM name mapping to
more than one CHEBI id under exactMatch is skipped rather than guessed at.

The report records the SSSOM's own ``mapping_set_version``, so "which MIM release
did we align to" is answerable from the artifact rather than from memory.

Read-only. Usage::

    just audit-mim-sssom
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
NORMALIZED = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_SSSOM = (
    REPO_ROOT.parent / "MediaIngredientMech" / "mappings" / "ingredient_mappings.sssom.tsv"
)
DEFAULT_OUT = REPO_ROOT / "data" / "import_tracking" / "reports" / "mim_sssom_divergence.tsv"

EXACT_MATCH = "skos:exactMatch"
FINDINGS = ("DIVERGENT", "INTERNAL_SPLIT", "MISSING_GROUNDING")


def normalize_name(value: str) -> str:
    """Fold the differences that are never meaningful in a reagent name.

    Whitespace, hyphen and underscore only. Deliberately NOT stripping
    punctuation or digits: `CaCl2 x 2 H2O` and `CaCl2` are different substances,
    and folding them together would hide exactly the hydrate distinctions #256
    says we sometimes model better than MIM.
    """
    return re.sub(r"[\s\-_]+", " ", value.strip().casefold())


# Tokens in MIM's `other` column that are not synonyms of the ingredient. The
# column mixes three things: CAS registry numbers, genuine aliases, and organism
# trait annotations that leaked in (`carbon source: acetate`, `produces:
# alanosine`, `electron acceptor: ...`). Only the middle group is a name.
_CAS_TOKEN = re.compile(r"^cas\s*:", re.IGNORECASE)
_TRAIT_TOKEN = re.compile(
    r"^(?:produces|degradation|hydrolysis|reduction|oxidation|utilizes"
    r"|electron\s+(?:acceptor|donor)|(?:carbon|nitrogen|sulfur|energy)\s+source"
    r"|aerobic\s+catabolization|anaerobic\s*\w*|fermentation|assimilation"
    r"|respiration)\s*:",
    re.IGNORECASE,
)


def _synonyms(row: dict[str, str]) -> list[str]:
    """The pipe-separated aliases in `other`, minus identifiers and annotations."""
    out = []
    for token in (row.get("other") or "").split("|"):
        token = token.strip()
        if not token or _CAS_TOKEN.match(token) or _TRAIT_TOKEN.match(token):
            continue
        out.append(token)
    return out


def load_sssom(
    path: Path, *, match_synonyms: bool = False
) -> tuple[dict[str, tuple[str, str]], str]:
    """Return ``({normalized_name: (chebi_id, chebi_label)}, mapping_set_version)``.

    Names that exactMatch more than one CHEBI id are dropped: MIM has not settled
    them, so we have nothing to compare against and guessing would invent a
    verdict.

    ``match_synonyms`` also indexes MIM's ``other`` aliases, which roughly doubles
    the share of our ingredient names the audit can see (#304). Two rules keep it
    honest, and both matter:

      * an alias mapping to more than one CHEBI id is dropped, exactly as an
        ambiguous label is — 351 of them;
      * a LABEL always wins over an alias. 56 aliases contradict some row's
        label, e.g. `threonine` is MIM's label for CHEBI:26986 and an alias of
        CHEBI:16857. A label is MIM's primary assertion for that row; an alias is
        secondary, so preferring the label resolves those without guessing.

    It is OPT-IN and should stay that way. Coverage rises from 14.5% to 29.5% of
    names, but the 74 extra DIVERGENT names it produces are almost all noise:

        47 names (3,227 rows)  differ only in hydration state
         3 names   (709 rows)  differ only in stereochemistry
        24 names   (924 rows)  substantive -- and on inspection we are right in
                               nearly all of them, e.g. `Calcium chloride
                               anhydrous` where MIM's alias points at the
                               hexahydrate

    One is a contaminated alias rather than a disagreement: `Potassium dihydrogen
    phosphate` appears in the `other` column of MIM's `CaSO4 x 2 H2O` row and on
    no other, so it is unambiguous and wrong, and 233 of our rows would be told
    they should be calcium sulfate dihydrate. The ambiguity rule cannot catch a
    bad alias that occurs only once.

    So this widens what the audit can SEE, which is useful for investigation, and
    is deliberately not wired into the gate baselines.
    """
    if not path.exists():
        raise SystemExit(
            f"MIM SSSOM not found at {path}\n"
            "Pass --sssom, or check out MediaIngredientMech beside this repo."
        )

    version = "unknown"
    candidates: dict[str, set[tuple[str, str]]] = defaultdict(set)
    aliases: dict[str, set[tuple[str, str]]] = defaultdict(set)
    with path.open(encoding="utf-8") as handle:
        header_lines = []
        for line in handle:
            if not line.startswith("#"):
                data_start = line
                break
            header_lines.append(line)
        else:
            raise SystemExit(f"{path} has no data rows")

        for line in header_lines:
            match = re.search(r'mapping_set_version:\s*"?([^"\s]+)"?', line)
            if match:
                version = match.group(1)

        reader = csv.DictReader([data_start, *handle], delimiter="\t")
        for row in reader:
            if row.get("predicate_id") != EXACT_MATCH:
                continue
            object_id = row.get("object_id") or ""
            label = row.get("subject_label") or ""
            if not object_id.startswith("CHEBI:") or not label:
                continue
            entry = (object_id, row.get("object_label") or "")
            candidates[normalize_name(label)].add(entry)
            if match_synonyms:
                for alias in _synonyms(row):
                    aliases[normalize_name(alias)].add(entry)

    resolved = {name: next(iter(ids)) for name, ids in candidates.items() if len(ids) == 1}
    for name, ids in aliases.items():
        # Label wins, and an ambiguous alias is no verdict at all.
        if name not in candidates and len(ids) == 1:
            resolved[name] = next(iter(ids))
    return resolved, version


def our_chebi(row: dict[str, Any]) -> tuple[str | None, str]:
    """The CHEBI grounding on one ingredient row, and the label it asserts.

    The label is the RECORD's assertion, not an ontology lookup. #256 records
    that some rows carry the ingredient string in `term.label` rather than the
    ontology label, so it is a reading aid for triage and not evidence — which is
    why the column is named `our_label_asserted`. `just check-id-labels` is what
    adjudicates labels.
    """
    for slot in ("chebi_term", "term"):
        candidate = row.get(slot)
        if not isinstance(candidate, dict):
            continue
        value = candidate.get("id")
        if isinstance(value, str) and value.startswith("CHEBI:"):
            return value, str(candidate.get("label") or "")
    return None, ""


def reagent_rows(doc: dict[str, Any]):
    """Every reagent row, from all three places records keep them."""
    for row in doc.get("ingredients") or []:
        if isinstance(row, dict):
            yield "ingredients", row
    for row in doc.get("composition") or []:
        if isinstance(row, dict):
            yield "composition", row
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        for row in solution.get("composition") or []:
            if isinstance(row, dict):
                yield "solutions[].composition", row


def collect(normalized_dir: Path) -> dict[str, Counter]:
    """``{normalized_name: Counter({chebi_id_or_None: rows})}``, plus display names."""
    by_name: dict[str, Counter] = defaultdict(Counter)
    display: dict[str, str] = {}
    labels: dict[str, str] = {}
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
            key = normalize_name(name)
            display.setdefault(key, name.strip())
            chebi, label = our_chebi(row)
            by_name[key][chebi] += 1
            if chebi and label:
                labels.setdefault(chebi, label)
    return by_name, display, labels


def audit(
    normalized_dir: Path, sssom_path: Path, *, match_synonyms: bool = False
) -> tuple[list[dict[str, str]], str, dict[str, int]]:
    """Findings, the SSSOM version, and how much of the corpus was comparable."""
    mim, version = load_sssom(sssom_path, match_synonyms=match_synonyms)
    by_name, display, labels = collect(normalized_dir)

    # Coverage is part of the result, not a footnote. MIM's exactMatch labels
    # reach 517 of our 3,519 distinct names -- 14.7% -- though those are the
    # common reagents and carry 60.6% of rows. A gate that sees a seventh of the
    # names must say so, or a green run reads as "we agree with MIM" when it
    # mostly means "MIM has not looked at these".
    coverage = {
        "our_names": len(by_name),
        "matched_names": sum(1 for name in by_name if name in mim),
        "our_rows": sum(sum(counts.values()) for counts in by_name.values()),
        "matched_rows": sum(
            sum(counts.values()) for name, counts in by_name.items() if name in mim
        ),
    }

    def described(chebi_ids) -> str:
        return "|".join(f"{cid}={labels.get(cid, '?')}" for cid in chebi_ids)

    rows: list[dict[str, str]] = []
    for key, counts in sorted(by_name.items()):
        grounded = {cid: n for cid, n in counts.items() if cid}
        ungrounded = counts.get(None, 0)
        mim_entry = mim.get(key)
        mim_id, mim_label = mim_entry if mim_entry else ("", "")
        base = {
            "ingredient": display[key],
            "mim_id": mim_id,
            "mim_label": mim_label,
            "our_label_asserted": described(sorted(grounded, key=lambda c: -grounded[c])),
        }

        if len(grounded) > 1:
            ours = "|".join(
                f"{cid}={n}" for cid, n in sorted(grounded.items(), key=lambda kv: -kv[1])
            )
            agrees = mim_id in grounded if mim_id else False
            rows.append(
                {
                    **base,
                    "finding": "INTERNAL_SPLIT",
                    "our_ids": ours,
                    "rows": str(sum(grounded.values())),
                    "detail": (
                        f"{len(grounded)} CHEBI ids for one name; "
                        + (
                            "MIM matches one of them"
                            if agrees
                            else "MIM has no opinion" if not mim_id else "MIM matches none of them"
                        )
                    ),
                }
            )

        if mim_id and grounded:
            divergent = {cid: n for cid, n in grounded.items() if cid != mim_id}
            if divergent and len(grounded) == 1:
                cid, n = next(iter(divergent.items()))
                rows.append(
                    {
                        **base,
                        "finding": "DIVERGENT",
                        "our_ids": f"{cid}={n}",
                        "rows": str(n),
                        "detail": "we and MIM both ground this name, to different ids",
                    }
                )

        if mim_id and ungrounded:
            # Deliberately NOT `and not grounded`. 184 names carry some grounded
            # rows and some bare ones, and for 48 of them MIM has an opinion —
            # `Pyrrole-2-carboxylic acid` is grounded on 1 row and bare on 18.
            # Requiring the name to be wholly ungrounded hid 96 rows that are the
            # cheapest possible fix: MIM has already decided, and most rows of the
            # name already agree.
            rows.append(
                {
                    **base,
                    "finding": "MISSING_GROUNDING",
                    "our_ids": "",
                    "rows": str(ungrounded),
                    "detail": (
                        "MIM grounds this name and we do not"
                        if not grounded
                        else f"MIM grounds this name; {ungrounded} row(s) of it "
                        f"are bare while {sum(grounded.values())} are grounded"
                    ),
                }
            )
    return rows, version, coverage


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument(
        "--sssom", type=Path, default=DEFAULT_SSSOM, help="MIM's published ingredient SSSOM"
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--match-synonyms",
        action="store_true",
        help="Also match MIM's `other` aliases, not just subject_label. Roughly "
        "doubles the share of our names the audit can see (#304).",
    )
    parser.add_argument(
        "--max-divergent",
        type=int,
        default=None,
        help="Exit non-zero when more than N ingredient NAMES diverge from MIM. "
        "Counted in names, not rows: one regrounding decision fixes every "
        "row of a name, so names are what a curator actually works through.",
    )
    parser.add_argument(
        "--max-split",
        type=int,
        default=None,
        help="Exit non-zero when more than N names carry several CHEBI ids in our "
        "own corpus. Independent of MIM, and the class most often a plain "
        "mistake.",
    )
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    rows, version, coverage = audit(
        args.normalized_dir, args.sssom, match_synonyms=args.match_synonyms
    )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            delimiter="\t",
            fieldnames=[
                "finding",
                "ingredient",
                "our_ids",
                "our_label_asserted",
                "mim_id",
                "mim_label",
                "rows",
                "detail",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    tally = Counter(row["finding"] for row in rows)
    affected = Counter()
    for row in rows:
        affected[row["finding"]] += int(row["rows"])

    print(f"MIM SSSOM: {args.sssom}")
    print(f"  mapping_set_version: {version}\n")
    for finding in FINDINGS:
        print(
            f"  {finding:18s} {tally.get(finding, 0):4d} names "
            f"({affected.get(finding, 0):,} rows)"
        )

    name_pct = 100 * coverage["matched_names"] / max(coverage["our_names"], 1)
    row_pct = 100 * coverage["matched_rows"] / max(coverage["our_rows"], 1)
    print(
        f"\n  comparable: {coverage['matched_names']:,} of "
        f"{coverage['our_names']:,} names ({name_pct:.1f}%), "
        f"{coverage['matched_rows']:,} of {coverage['our_rows']:,} rows "
        f"({row_pct:.1f}%)"
    )
    print(
        "  the rest are names MIM's exactMatch labels do not cover, so this " "gate cannot see them"
    )

    relative = args.out.relative_to(REPO_ROOT) if args.out.is_relative_to(REPO_ROOT) else args.out
    print(f"\nWrote {relative}")
    print(
        "\nRead-only. Divergence runs BOTH ways — #256 records cases where our "
        "hydrate is the better term and cases where MIM's neutral acid is — so "
        "this reports rather than rewrites."
    )

    failed = False
    if args.max_divergent is not None and tally.get("DIVERGENT", 0) > args.max_divergent:
        print(
            f"\nFAIL: {tally['DIVERGENT']} divergent names > baseline "
            f"{args.max_divergent}. A new grounding disagrees with MIM's "
            f"published SSSOM; reconcile it or agree the change with MIM.",
            file=sys.stderr,
        )
        failed = True
    if args.max_split is not None and tally.get("INTERNAL_SPLIT", 0) > args.max_split:
        print(
            f"\nFAIL: {tally['INTERNAL_SPLIT']} names carry several CHEBI ids > "
            f"baseline {args.max_split}. One name has been grounded two ways "
            f"within our own corpus.",
            file=sys.stderr,
        )
        failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
