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
`82694054f5bbf74b5392bf8858c9962c2152a35a`: 9,115 data rows, 854,426
bytes, SHA-256
`7113b90cb82ea6d80c0abdb34b0620b71fe6b02e3000327b14dbf797062728ac`.
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

The occurrence pipeline tracked by #337 must import this same resolver. That
issue owns structural traversal, including the distinction between
`MediaRecipe.ingredients` and root `SolutionRecipe.composition`, stable
occurrence coordinates, placeholder exclusion, uncapped outputs, and parse
errors. #260 deliberately does not conceal the existing root-solution traversal
gap inside KGX.

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
