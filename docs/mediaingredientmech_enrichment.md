# MediaIngredientMech ingredient identity resolution

CultureMech publishes ingredient identities through MediaIngredientMech's
per-label resolution artifact. Runtime resolution is deterministic and offline:
the exact MIM artifact revision is vendored inside the CultureMech package.

This is a publication-time decision. It does not rewrite curated recipe YAML,
and it does not change which recipe contains an ingredient.

## Pinned dependency

The packaged files are:

- `src/culturemech/data/mediaingredientmech/label_index.csv`
- `src/culturemech/data/mediaingredientmech/label_index.metadata.json`

The current pin is MIM commit
`9f09e4fb97fb0e6cbbd6f25baca40b36512adb88`: 9,876 data rows, 922,191
bytes, SHA-256
`a36cd4683feb89e2fc2a1721dc15008d1e10c12044e89a36c27b6621a8aaf262`.
Metadata also fixes the repository, source path, seven-column header, row count,
and consumer-contract version. There is no moving-branch lookup in a normal
build.

Verify the dependency without network access:

```bash
just check-mim-label-index
```

The check rejects hash, size, header, enum, row-count, label-contiguity,
group-ambiguity, and merge-tombstone drift.

## Resolution contract

`culturemech.ingredients.mim_label_index` returns a structured
`GroundingDecision`. Its `identifier` is the semantic identity selected for KG
publication; `ontology_id` is retained only as diagnostic publisher data.

Resolution order is:

1. Match a trimmed, Unicode-normalized, case-insensitive exact label group.
2. If absent, try a conservative fallback that collapses whitespace, ASCII
   hyphen, and underscore only. Digits and chemical punctuation remain intact.
3. Trust MIM's first row only when `ambiguity` is `unique`,
   `resolved:owned`, or `agree:same_substance`.
4. Refuse `conflict:different_substances`,
   `unresolved:partial_chemistry`, and `unresolved:no_chemistry`.
5. Treat `UNMAPPED` as an authoritative absence, suppressing a conflicting
   local term.
6. Follow a `REJECTED` merge tombstone only when a live `MAPPED` row holds its
   identifier. `UNMAPPED_NNNN` is the valid invalid-retirement exception; a
   dangling ontology or registry identifier makes the artifact invalid.

There is no fuzzy matching. In particular, hydrate counts and formula
punctuation are never discarded: an anhydrous ingredient and its hydrate are
different ordered substances.

MIM `identifier` values are not CHEBI-only. FOODON, BTO, NCIT, CAS, MeSH, and
curated local identities can be legitimate answers and are retained.

## Local fallback and source identity

When MIM has no usable verdict, the resolver prefers:

1. `chebi_term.id`
2. a non-`mediadive.compound:*` `term.id`

A MediaDive compound identifier is preserved separately as
`source_compound_id`; it is not promoted to semantic identity. An unsafe MIM
ambiguity may retain a local identity only as the explicitly labelled
`ambiguous_local_fallback` result. An explicit MIM `UNMAPPED` verdict never
falls back locally.

Examples pinned by tests:

| recipe label | local value | publication decision |
|---|---|---|
| `EDTA` | `CHEBI:64755` EDTA(2−) | `CHEBI:4735` free acid |
| `Beef heart` | `UBERON:0000948` organ | `FOODON:00004410` food product |
| `Calf brains` | `UBERON:0000955` organ | no identity; MIM explicitly unmapped |
| `Infusion from Potatoes` | unrelated FOODON term | no identity; MIM explicitly unmapped |

## Consumers

KGX is the first production consumer. Direct medium ingredients and ingredients
inside a referenced solution are resolved through this shared code before a
`biolink:has_part` edge is emitted. An explicit authoritative-unmapped result
omits the ingredient edge.

The resolver is injectable into the pure `transform()` function for isolated
tests. Koza uses the verified packaged default lazily. A wheel smoke test loads
it from `/tmp`, proving an installed distribution does not rely on the source
checkout.

The ingredient-occurrence pipeline imports this same resolver and partitions
its structured decisions without reinterpreting CURIE syntax:

- `mim_exact`, `mim_normalized`, `local_fallback`, and
  `ambiguous_local_fallback` are mapped because `GroundingDecision.identifier`
  is present.
- `authoritative_unmapped`, `ambiguous`, and `not_found` are unmapped because
  the decision has no selected identifier.

The selected value is exported as `resolved_identifier`. The accompanying
`mim_ontology_id_diagnostic` is publisher metadata only. Likewise,
`mediadive.compound:*` remains `source_compound_id`; a colon in an upstream ID
does not make it an ontology grounding. `local_identifier`, MIM match/status/
ambiguity fields, and `grounding_reason` remain available for audit.

### Direct occurrence contract

Occurrence extraction follows the root record's schema shape:

- a MediaRecipe-shaped root contributes `ingredients`;
- a SolutionRecipe-shaped root contributes `composition`.

The fields are alternatives, not lists to concatenate. A solution's legacy
`ingredients: [{preferred_term: See source for composition}]` stub is therefore
not an occurrence, and nested `solutions[].composition` is not expanded once
per referencing medium. The pipeline records direct containment only.

Every occurrence carries the stable coordinate
`(recipe_id, component_field, component_index)`, where `recipe_id` is the root
`CultureMech:NNNNNN` identifier. Recipe labels are display metadata and are
never used for identity or distinct-recipe counts.

The canonical TSV is complete and uncapped. `occurrence_count` is the number of
its rows in a group, while `distinct_recipe_count` is the number of unique
`recipe_id` values. Summary YAML may retain convenient display fields, but no
count is derived from an example sample.

Input paths and occurrence coordinates are sorted before serialization. The
outputs deliberately omit a wall-clock `generation_date`, use LF line endings,
and atomically replace each destination from a fully staged publication set, so
rerunning against identical recipe data and the same pinned MIM index is
byte-identical. YAML/shape failures are always written
to the machine-readable error TSV; `--verbose` affects progress only. Any such
failure exits nonzero and leaves the last successful artifacts intact; a later
replacement error rolls already-replaced members of the set back in-process.

## Refreshing the pin

A refresh is an explicit dependency review. A full lowercase 40-character MIM
commit SHA is required; branch names and short SHAs are rejected.

```bash
# Preview only (default): download, validate, and report answer changes
just refresh-mim-label-index <full-mim-sha>

# Apply after reviewing added, removed, and changed labels
just refresh-mim-label-index <full-mim-sha> --apply
```

The metadata is deterministic and intentionally has no retrieval timestamp.
Both files must be committed together.

## Legacy enrichment tools

`MediaIngredientMechLoader`, `MediaIngredientMechLinker`, and
`scripts/enrich_with_mediaingredientmech.py` remain temporarily for legacy
migrations. They are not the publication authority: they can read a moving
checkout, use first-wins synonym and fuzzy matching, and can materialize answers
into recipe YAML. Do not extend or advertise that path for new exports.

Similarly, `audit_mim_sssom_divergence.py` remains useful as a historical
CHEBI-only diagnostic. Its exactMatch-only sibling-checkout input is not a
substitute for the pinned label resolver.
