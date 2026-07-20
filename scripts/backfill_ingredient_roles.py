"""Propose faceted ingredient-role assignments from CHEBI has_role axioms.

Mechanistic lane of the Step 7 backfill. For each `IngredientDescriptor`
in the normalized-YAML corpus:

  1. Resolve the ingredient's CHEBI id (from `term.id`, `chebi_term.id`,
     or `mediaingredientmech_chebi_term.id`).
  2. Query OAK (`sqlite:obo:chebi`) for `has_role` axioms on that CHEBI id.
  3. For each role hit — DIRECT ONLY, no ancestor walk — match against the
     `meaning:` / `mappings:` CURIEs declared on the three facet enums in
     `src/culturemech/schema/mim_roles.yaml`.
  4. Emit a JSON proposal file:
       { proposals: [ { file, ingredient_index, ingredient_name, chebi_id,
                        proposed_slots: { nutritional_roles: [...], ... },
                        evidence: [ { source_type: "ontology",
                                       source_id: "chebi:has_role:<role_id>",
                                       chebi_role_label: "...", confidence: "chebi-axiom" } ] } ] }

The script COMMITS NOTHING and does not modify any YAML file. Curator
runs the audit → runs the backfill in dry-run → reviews the JSON diff →
applies with a separate curator-controlled tool.

Complements `scripts/audit_missing_roles.py` (identifies WHERE to look)
by proposing WHAT to write. The two are the mechanistic + evidence-blind
lane of the ingredient-roles migration; Step 7b (Edison literature) is
the complementary evidence-bearing lane.

Design notes:

- CHEBI has clean has-role coverage for **physicochemical** roles (BUFFER,
  CHELATOR, SURFACTANT, REDUCING_AGENT, OXIDIZING_AGENT, PH_INDICATOR,
  ANTIFOAM) and some **cellular-metabolic** roles (COFACTOR, INHIBITOR,
  ELECTRON_DONOR, ELECTRON_ACCEPTOR — where asserted). Coverage of the
  **nutritional** facet (CARBON_SOURCE, NITROGEN_SOURCE, …) is thin —
  CHEBI has no "carbon source" role class — so the mechanistic lane
  will typically populate 0-2 facets per ingredient, and Step 7b Edison
  is expected to fill in nutritional/conditional assignments.

- Direct-hit matching only. An is-a ancestor walk over CHEBI's role subtree
  is tempting (L-cysteine has_role `EC-4.3.1.3-inhibitor`, which is-a
  `inhibitor`) but produces semantic false positives — L-cysteine is not a
  general growth inhibitor in the culture-media sense. Any facet assignment
  that requires interpreting a specific-role subclass belongs on the
  Step 7b literature lane, not here.

- Deduplication: proposals are computed per unique CHEBI id (there are
  ~3100 unique CHEBI ids in the corpus vs 171,458 ingredient records),
  then fanned out to every ingredient occurrence.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Iterator, Optional

import yaml

logger = logging.getLogger(__name__)

FACET_SLOTS = ("nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles")

CHEBI_ID_PATHS = (
    ("term", "id"),
    ("chebi_term", "id"),
    ("mediaingredientmech_chebi_term", "id"),
)

# CHEBI has_role predicate — the Relation Ontology `RO:0000087` object
# property. Live sqlite:obo:chebi emits triples under this predicate id
# only (verified 2026-07-20).
HAS_ROLE_PREDICATES = frozenset({"RO:0000087"})

# The root of CHEBI's role subtree. Walking is-a ancestors of a has_role
# target and stopping when we hit this class (or its subclass we've mapped)
# keeps ancestor-walks bounded.
CHEBI_ROLE_ROOT = "CHEBI:50906"


def _get_nested(record: dict, path: tuple[str, ...]) -> Optional[str]:
    current: object = record
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current if isinstance(current, str) else None


def ingredient_chebi_id(ing: dict) -> Optional[str]:
    for path in CHEBI_ID_PATHS:
        value = _get_nested(ing, path)
        if value and value.startswith("CHEBI:"):
            return value
    return None


def load_role_curie_index(mim_roles_path: Path) -> dict[str, list[tuple[str, str]]]:
    """Return `{chebi_role_curie: [(facet_slot, enum_value), ...]}`.

    Builds the lookup that maps a CHEBI role class to the facet-slot
    enum values it should trigger. Sourced from `mim_roles.yaml`'s
    `meaning:` (primary) and `mappings:` (secondary) blocks on each
    permissible value. A single CHEBI CURIE may map to multiple
    (slot, enum) pairs when the same term is legitimately used across
    facets (e.g., `CHEBI:23357` covers both nutritional COFACTOR_PROVIDER
    and cellular-metabolic COFACTOR).
    """
    doc = yaml.safe_load(mim_roles_path.read_text())
    enums = doc.get("enums") or {}
    enum_to_slot = {
        "NutritionalRoleEnum":       "nutritional_roles",
        "PhysicochemicalRoleEnum":   "physicochemical_roles",
        "CellularMetabolicRoleEnum": "cellular_metabolic_roles",
    }
    index: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for enum_name, slot in enum_to_slot.items():
        pvs = (enums.get(enum_name) or {}).get("permissible_values") or {}
        for value_name, value_def in pvs.items():
            if not isinstance(value_def, dict):
                continue
            meaning = value_def.get("meaning")
            if isinstance(meaning, str) and meaning.startswith("CHEBI:"):
                index[meaning].append((slot, value_name))
            for mapped in (value_def.get("mappings") or []):
                if isinstance(mapped, str) and mapped.startswith("CHEBI:"):
                    index[mapped].append((slot, value_name))
    return dict(index)


class ChebiRoleResolver:
    """Cache CHEBI direct-has_role lookups against a single adapter."""

    def __init__(self, adapter, role_curie_index: dict[str, list[tuple[str, str]]]):
        self._adapter = adapter
        self._role_curie_index = role_curie_index
        # Cache per compound CHEBI id → list of (slot, value, evidence-role-curie).
        self._compound_cache: dict[str, list[tuple[str, str, str]]] = {}
        # Cache CHEBI id → label for evidence strings.
        self._label_cache: dict[str, str] = {}

    def label(self, curie: str) -> str:
        if curie in self._label_cache:
            return self._label_cache[curie]
        try:
            label = self._adapter.label(curie) or curie
        except Exception:
            label = curie
        self._label_cache[curie] = label
        return label

    def facets_for(self, chebi_id: str) -> list[tuple[str, str, str]]:
        """Return [(slot, enum_value, evidence_role_curie), ...] for `chebi_id`.

        Direct has_role matches only — the role class asserted on the compound
        must appear verbatim in the facet-enum index. Ancestor walks were
        removed after L-cysteine → INHIBITOR false positives (specific-enzyme
        inhibitor role is-a general inhibitor role → misleading in a
        culture-media context). Speculative facet assignments belong on
        the Step 7b literature lane.
        """
        if chebi_id in self._compound_cache:
            return self._compound_cache[chebi_id]

        hits: list[tuple[str, str, str]] = []
        seen_slot_value: set[tuple[str, str]] = set()

        try:
            rels = list(self._adapter.relationships(subjects=[chebi_id]))
        except Exception as exc:
            logger.debug("relationships(%s) failed: %r", chebi_id, exc)
            rels = []

        for triple in rels:
            if not isinstance(triple, tuple) or len(triple) < 3:
                continue
            _subject, predicate, obj = triple[0], triple[1], triple[2]
            if predicate not in HAS_ROLE_PREDICATES:
                continue
            if not isinstance(obj, str) or not obj.startswith("CHEBI:"):
                continue
            for slot, value in self._role_curie_index.get(obj, []):
                key = (slot, value)
                if key in seen_slot_value:
                    continue
                seen_slot_value.add(key)
                hits.append((slot, value, obj))

        self._compound_cache[chebi_id] = hits
        return hits


def iter_ingredients(yaml_root: Path) -> Iterator[tuple[Path, int, dict]]:
    """Yield (recipe_file, ingredient_index, ingredient_dict)."""
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
        for idx, ing in enumerate(ingredients):
            if isinstance(ing, dict):
                yield path, idx, ing


def has_any_facet_role(ing: dict) -> bool:
    return any((ing.get(slot) or []) for slot in FACET_SLOTS)


def build_proposal(
    path: Path,
    idx: int,
    ing: dict,
    chebi_id: str,
    facet_hits: list[tuple[str, str, str]],
    role_labels: dict[str, str],
    yaml_root: Path,
) -> Optional[dict]:
    if not facet_hits:
        return None
    proposed_slots: dict[str, list[str]] = defaultdict(list)
    evidence: list[dict] = []
    seen_evidence: set[str] = set()
    for slot, value, evidence_role_curie in facet_hits:
        if value not in proposed_slots[slot]:
            proposed_slots[slot].append(value)
        if evidence_role_curie in seen_evidence:
            continue
        seen_evidence.add(evidence_role_curie)
        evidence.append({
            "source_type": "ontology",
            "source_id": f"chebi:has_role:{evidence_role_curie}",
            "chebi_role_label": role_labels.get(evidence_role_curie, evidence_role_curie),
            "confidence": "chebi-axiom",
        })
    try:
        file_display = path.relative_to(yaml_root.parent).as_posix()
    except ValueError:
        file_display = path.as_posix()
    existing_slots = {
        slot: list(ing.get(slot) or [])
        for slot in FACET_SLOTS
        if ing.get(slot)
    }
    proposal: dict = {
        "file": file_display,
        "ingredient_index": idx,
        "ingredient_name": (ing.get("preferred_term") or "").strip() or None,
        "chebi_id": chebi_id,
        "proposed_slots": dict(proposed_slots),
        "evidence": evidence,
    }
    if existing_slots:
        # Under --include-populated the caller wants to see proposals for
        # already-populated ingredients; expose the existing state so an
        # applier can compute per-facet adds without re-loading the YAML.
        proposal["existing_slots"] = existing_slots
    return proposal


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--yaml-dir",
        type=Path,
        default=Path("data/normalized_yaml"),
        help="Root of the normalized-YAML corpus.",
    )
    parser.add_argument(
        "--mim-roles",
        type=Path,
        default=Path("src/culturemech/schema/mim_roles.yaml"),
        help="Path to the vendored MIM role-facet enums schema module.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("reports/mechanistic_role_backfill_proposals.json"),
        help="Output JSON path for the proposals file.",
    )
    parser.add_argument(
        "--limit-ingredients",
        type=int,
        default=None,
        help="Cap total ingredients processed (for smoke tests / partial runs).",
    )
    parser.add_argument(
        "--only-chebi",
        action="append",
        default=[],
        help="Restrict processing to specific CHEBI ids (repeatable). Useful for spot-checks.",
    )
    parser.add_argument(
        "--include-populated",
        action="store_true",
        help="Also propose for ingredients that already have some facet slot set (default: skip them).",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(message)s")

    if not args.mim_roles.exists():
        print(f"error: mim_roles.yaml not found at {args.mim_roles}", file=sys.stderr)
        return 2

    role_curie_index = load_role_curie_index(args.mim_roles)
    logger.info(
        "loaded %d CHEBI role CURIEs across the three facet enums",
        len(role_curie_index),
    )

    # Lazy OAK adapter — we only need it when we hit the first ingredient
    # with a CHEBI id.
    resolver: Optional[ChebiRoleResolver] = None

    proposals: list[dict] = []
    seen_ingredients = 0
    skipped_populated = 0
    without_chebi = 0
    unique_chebi_processed: set[str] = set()

    only_chebi_set = set(args.only_chebi) if args.only_chebi else None

    for path, idx, ing in iter_ingredients(args.yaml_dir):
        if args.limit_ingredients is not None and seen_ingredients >= args.limit_ingredients:
            break
        seen_ingredients += 1

        chebi_id = ingredient_chebi_id(ing)
        if not chebi_id:
            without_chebi += 1
            continue
        if only_chebi_set is not None and chebi_id not in only_chebi_set:
            continue
        if not args.include_populated and has_any_facet_role(ing):
            skipped_populated += 1
            continue

        if resolver is None:
            from culturemech.ontology.oak_client import OAKClient

            client = OAKClient()
            adapter = client.get_adapter("chebi")
            if adapter is None:
                print(
                    "error: OAK adapter for chebi could not be initialized (see logs)",
                    file=sys.stderr,
                )
                return 2
            resolver = ChebiRoleResolver(adapter, role_curie_index)

        facet_hits = resolver.facets_for(chebi_id)
        unique_chebi_processed.add(chebi_id)
        if not facet_hits:
            continue
        # Preload labels for the evidence-role CURIEs.
        role_labels: dict[str, str] = {}
        for _slot, _value, role_curie in facet_hits:
            role_labels[role_curie] = resolver.label(role_curie)
        proposal = build_proposal(
            path=path,
            idx=idx,
            ing=ing,
            chebi_id=chebi_id,
            facet_hits=facet_hits,
            role_labels=role_labels,
            yaml_root=args.yaml_dir,
        )
        if proposal is not None:
            proposals.append(proposal)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps({"proposals": proposals}, indent=2, sort_keys=False))

    # stdout summary — machine-readable + curator-facing.
    print(f"# Mechanistic role backfill — dry-run proposals")
    print()
    print(f"- Ingredient records scanned: **{seen_ingredients}**")
    print(f"- Without a CHEBI id: {without_chebi}")
    print(f"- Skipped because a facet slot was already populated: {skipped_populated}")
    print(f"- Unique CHEBI ids resolved via OAK: **{len(unique_chebi_processed)}**")
    print(f"- Proposals emitted: **{len(proposals)}** → `{args.out}`")

    # Facet-slot distribution.
    slot_counts: dict[str, int] = defaultdict(int)
    for prop in proposals:
        for slot in prop["proposed_slots"]:
            slot_counts[slot] += 1
    print()
    print("## Proposals by facet slot")
    print()
    for slot in FACET_SLOTS:
        print(f"- `{slot}`: {slot_counts.get(slot, 0)} proposals")

    return 0


if __name__ == "__main__":
    sys.exit(main())
