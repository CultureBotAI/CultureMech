"""Report IngredientDescriptors that map to a MIM ingredient but carry no faceted role assignments.

Complements `scripts/audit_schema.py` (schema-shape probes) with an
instance-shape probe: it walks the normalized-YAML corpus, resolves each
ingredient to a MIM subject id via the SSSOM
(`../MediaIngredientMech/mappings/ingredient_mappings.sssom.tsv`), and
flags ingredients that have a MIM identity anchor but no
`nutritional_roles` / `physicochemical_roles` / `cellular_metabolic_roles`
population.

Serves two downstream lanes of the ingredient-role migration:
  - Step 7 mechanistic backfill (`backfill_ingredient_roles.py`) can prioritize
    ingredients on this report that MIM already has a CHEBI mapping for.
  - Step 7b Edison literature backfill (planned) can prioritize the residue
    — ingredients that need cited evidence rather than an ontology walk.

Follows `audit_schema.py`'s inline-probe pattern: `report_section(title)` +
markdown bullets on stdout. Pipe to `reports/missing_roles_audit.md`.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Iterator, Optional

import yaml

FACET_SLOTS = ("nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles")

# CHEBI id lives at any of these paths on an ingredient dict; the backfill
# scripts on the CultureMech side accept CHEBI identity from either the primary
# term or a MIM-mapped sibling.
CHEBI_ID_PATHS = (
    ("term", "id"),
    ("chebi_term", "id"),
    ("mediaingredientmech_chebi_term", "id"),
)


def report_section(title: str) -> None:
    print()
    print(f"## {title}")
    print()


def _get_nested(record: dict, path: tuple[str, ...]) -> Optional[str]:
    current: object = record
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current if isinstance(current, str) else None


def ingredient_chebi_id(ing: dict) -> Optional[str]:
    """Return the ingredient's CHEBI id from whichever nested path carries it."""
    for path in CHEBI_ID_PATHS:
        value = _get_nested(ing, path)
        if value and value.startswith("CHEBI:"):
            return value
    return None


def load_sssom_chebi_to_mim(sssom_path: Path) -> dict[str, list[tuple[str, str, float]]]:
    """Return `{chebi_id: [(mim_subject, predicate, confidence), ...]}`.

    One CHEBI id may map to multiple MIM subjects (variant forms, hydrates,
    close-match salts). Callers should prefer skos:exactMatch over
    skos:closeMatch when picking a canonical mapping.
    """
    if not sssom_path.exists():
        raise FileNotFoundError(f"MIM SSSOM not found at {sssom_path}")

    chebi_to_mim: dict[str, list[tuple[str, str, float]]] = defaultdict(list)
    with sssom_path.open() as fh:
        # Skip the leading comment block (`# ...`) that precedes the header.
        reader = csv.DictReader(
            (line for line in fh if not line.startswith("#")),
            delimiter="\t",
        )
        for row in reader:
            subject = (row.get("subject_id") or "").strip()
            obj = (row.get("object_id") or "").strip()
            predicate = (row.get("predicate_id") or "").strip()
            if not subject.startswith("MIM:") or not obj.startswith("CHEBI:"):
                continue
            try:
                conf = float(row.get("confidence") or 0.0)
            except ValueError:
                conf = 0.0
            chebi_to_mim[obj].append((subject, predicate, conf))
    return dict(chebi_to_mim)


def iter_ingredients(yaml_root: Path) -> Iterator[tuple[Path, dict]]:
    """Yield (recipe_file, ingredient_dict) for every ingredient in the corpus."""
    for path in sorted(yaml_root.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        ingredients = doc.get("ingredients") or []
        if not isinstance(ingredients, list):
            continue
        for ing in ingredients:
            if isinstance(ing, dict):
                yield path, ing


def has_any_facet_role(ing: dict) -> bool:
    return any((ing.get(slot) or []) for slot in FACET_SLOTS)


def pick_canonical_mim(mim_candidates: list[tuple[str, str, float]]) -> Optional[tuple[str, str]]:
    """Prefer exactMatch > closeMatch > narrowMatch; break ties on higher confidence."""
    if not mim_candidates:
        return None
    predicate_rank = {
        "skos:exactMatch": 3,
        "skos:closeMatch": 2,
        "skos:narrowMatch": 1,
    }
    ranked = sorted(
        mim_candidates,
        key=lambda t: (predicate_rank.get(t[1], 0), t[2]),
        reverse=True,
    )
    subject, predicate, _ = ranked[0]
    return subject, predicate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sssom",
        type=Path,
        default=Path("../MediaIngredientMech/mappings/ingredient_mappings.sssom.tsv"),
        help="Path to the MIM SSSOM TSV (default: sibling MediaIngredientMech checkout).",
    )
    parser.add_argument(
        "--yaml-dir",
        type=Path,
        default=Path("data/normalized_yaml"),
        help="Root of the normalized-YAML corpus (default: data/normalized_yaml).",
    )
    parser.add_argument(
        "--limit-examples",
        type=int,
        default=25,
        help="Cap on example ingredients enumerated per bucket (default: 25).",
    )
    args = parser.parse_args()

    if not args.yaml_dir.exists():
        print(f"# missing-roles audit\n\nYAML root not found: {args.yaml_dir}", file=sys.stderr)
        return 2

    chebi_to_mim = load_sssom_chebi_to_mim(args.sssom)

    total_ingredients = 0
    without_chebi = 0
    with_chebi_no_mim: list[tuple[Path, dict, str]] = []
    with_mim_no_roles: list[tuple[Path, dict, str, str, str]] = []
    with_mim_and_roles = 0
    slot_populated_counts: Counter[str] = Counter()
    facet_populated_ingredients: set[int] = set()
    predicate_used_counts: Counter[str] = Counter()

    for path, ing in iter_ingredients(args.yaml_dir):
        total_ingredients += 1
        chebi_id = ingredient_chebi_id(ing)
        if not chebi_id:
            without_chebi += 1
            continue

        canonical = pick_canonical_mim(chebi_to_mim.get(chebi_id, []))
        for slot in FACET_SLOTS:
            if ing.get(slot):
                slot_populated_counts[slot] += 1
                facet_populated_ingredients.add(id(ing))

        if canonical is None:
            with_chebi_no_mim.append((path, ing, chebi_id))
            continue

        mim_subject, predicate = canonical
        predicate_used_counts[predicate] += 1

        if has_any_facet_role(ing):
            with_mim_and_roles += 1
        else:
            with_mim_no_roles.append((path, ing, chebi_id, mim_subject, predicate))

    print("# Missing-roles audit")
    print()
    print(f"- Corpus root: `{args.yaml_dir}`")
    print(f"- MIM SSSOM: `{args.sssom}` ({sum(len(v) for v in chebi_to_mim.values())} MIM/CHEBI rows across {len(chebi_to_mim)} CHEBI ids)")
    print(f"- Total ingredient descriptors scanned: **{total_ingredients}**")
    print(f"- Ingredients with a CHEBI id: **{total_ingredients - without_chebi}**")
    print(f"  - Resolvable to a MIM subject via SSSOM: **{len(with_mim_no_roles) + with_mim_and_roles}**")
    print(f"    - Already carry at least one facet role: **{with_mim_and_roles}**")
    print(f"    - Missing all three facet roles: **{len(with_mim_no_roles)}**")
    print(f"  - CHEBI id present but no MIM SSSOM row: **{len(with_chebi_no_mim)}**")
    print(f"- Ingredients with no CHEBI id: **{without_chebi}**")

    report_section("Facet-slot population totals")
    print("| Facet slot | Ingredients populated |")
    print("| ---------- | --------------------- |")
    for slot in FACET_SLOTS:
        print(f"| `{slot}` | {slot_populated_counts.get(slot, 0)} |")

    report_section("MIM mapping predicates in use")
    if predicate_used_counts:
        for predicate, count in predicate_used_counts.most_common():
            print(f"- `{predicate}` — {count}")
    else:
        print("(no MIM SSSOM hits — check that the SSSOM path is correct and the corpus has CHEBI-mapped ingredients)")

    report_section("MIM-mapped ingredients missing all faceted role assignments")
    print(
        f"({len(with_mim_no_roles)} ingredients — primary target list for the "
        f"Step 7 mechanistic backfill and Step 7b literature backfill.)"
    )
    print()
    # Deduplicate by (chebi_id, preferred_term) so a compound recurring across
    # many recipes doesn't drown the list. Sort by frequency (most common first).
    dedup: Counter[tuple[str, str]] = Counter()
    example_recipe: dict[tuple[str, str], Path] = {}
    for path, ing, chebi_id, _mim, _pred in with_mim_no_roles:
        key = (chebi_id, (ing.get("preferred_term") or "").strip())
        dedup[key] += 1
        example_recipe.setdefault(key, path)
    for (chebi_id, term), count in dedup.most_common(args.limit_examples):
        recipe = example_recipe[(chebi_id, term)]
        try:
            recipe_display = recipe.relative_to(args.yaml_dir.parent)
        except ValueError:
            recipe_display = recipe
        label = term or "(unlabeled)"
        print(f"- `{chebi_id}` — {label} — appears in {count} recipes (e.g. `{recipe_display}`)")
    if len(dedup) > args.limit_examples:
        print(f"- ... and {len(dedup) - args.limit_examples} more unique ingredients.")

    report_section("CHEBI-mapped ingredients with no MIM SSSOM anchor")
    print(
        f"({len(with_chebi_no_mim)} ingredients — these have a local CHEBI id "
        f"but don't appear in the MIM SSSOM. Candidates for a MIM-side "
        f"ingredient-record proposal or a SSSOM curation pass.)"
    )
    print()
    dedup2: Counter[tuple[str, str]] = Counter()
    example_recipe2: dict[tuple[str, str], Path] = {}
    for path, ing, chebi_id in with_chebi_no_mim:
        key = (chebi_id, (ing.get("preferred_term") or "").strip())
        dedup2[key] += 1
        example_recipe2.setdefault(key, path)
    for (chebi_id, term), count in dedup2.most_common(args.limit_examples):
        recipe = example_recipe2[(chebi_id, term)]
        try:
            recipe_display = recipe.relative_to(args.yaml_dir.parent)
        except ValueError:
            recipe_display = recipe
        label = term or "(unlabeled)"
        print(f"- `{chebi_id}` — {label} — {count} recipes (e.g. `{recipe_display}`)")
    if len(dedup2) > args.limit_examples:
        print(f"- ... and {len(dedup2) - args.limit_examples} more unique ingredients.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
