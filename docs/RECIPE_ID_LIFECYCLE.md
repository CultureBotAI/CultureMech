# CultureMech recipe ID lifecycle

This is the producer and consumer contract for durable references to CultureMech
media and stock-solution records.

## Canonical identifier

The top-level `id` field is the canonical external identifier for both
`MediaRecipe` and `SolutionRecipe`. Its serialized form is exactly
`CultureMech:NNNNNN`, from `CultureMech:000001` through
`CultureMech:999999`. Names, filenames, category paths,
upstream database identifiers, and merged-recipe filenames are not stable
external identifiers.

An issued ID is unique, immutable, and never reused. Renaming a recipe or moving
its YAML file preserves the ID. A substantive replacement that is not known to
be the same recipe receives a new ID; the old ID becomes a tombstone. CI binds
each live ID to an immutable lineage signature derived from its ID-assignment
event. The small legacy cohort that predates those events carries an internal
`id_lineage_token`; it is not an external identifier and must never be changed
or copied to another record.

## Published catalog

[`data/culturemech_recipe_catalog.tsv`](../data/culturemech_recipe_catalog.tsv)
is the versioned, machine-readable resolution surface. It combines current
records with the append-only retired-ID ledger in
[`data/culturemech_id_tombstones.tsv`](../data/culturemech_id_tombstones.tsv).
The catalog has these columns:

| Column | Meaning |
| --- | --- |
| `culturemech_id` | Canonical `CultureMech:NNNNNN` ID |
| `lineage_signature` | Immutable internal witness used by CI to reject reassignment; not a consumer identifier |
| `file_path` | Current repository-relative path; empty for retired IDs |
| `display_name` | Current name, or the last known name for a retired ID |
| `lifecycle_status` | `ACTIVE`, `DELETED`, `MERGED`, or `SPLIT` |
| `successor_ids` | Semicolon-delimited successor IDs when the transition establishes them |
| `lifecycle_note` | Curator rationale for a retired ID |
| `catalog_schema_version` | Serialization contract version; currently `1` |

The two-column `data/culturemech_id_registry.tsv` remains an active-record
compatibility index. It is not the lifecycle authority because it intentionally
contains no retired IDs.

## Lifecycle transitions

- `ACTIVE`: exactly one current YAML record carries the ID. Its catalog name and
  path must match that record.
- `DELETED`: the record no longer exists and has no asserted successor. Consumers
  must retain the reference as unresolved historical provenance, not redirect it
  by label similarity.
- `MERGED`: the retired ID has exactly one curator-established successor. A
  consumer may follow the redirect while retaining the original ID as provenance.
- `SPLIT`: the retired ID has at least two successors. There is deliberately no
  automatic single redirect; consumers must choose using domain context or retain
  the historical ID.

For a split where one record clearly continues the old identity, keep the old ID
on that record and mint new IDs for the newly separated records. Use `SPLIT` only
when no single continuation is defensible. Never infer a successor from a shared
name, filename, or fuzzy match.

Before removing an active YAML record, add its ID, current lineage signature,
and reviewed lifecycle decision to `data/culturemech_id_tombstones.tsv` in the
same change. `MERGED` and `SPLIT` successors must already exist in the corpus or
tombstone graph. Cycles, dangling or duplicate successors, malformed IDs, reuse,
duplicate live IDs, changed lineage bindings, and unrecorded gaps are rejected.

## Producer workflow

Mint IDs only with the allocator; it reserves every ID in the active registry,
published catalog, and tombstone ledger and starts above the all-time high-water
mark.

```bash
just assign-ids --dry-run
just assign-ids
just refresh-id-registry
just refresh-id-catalog
just assign-ids-check
just check-id-catalog
```

The catalog is generated, not hand-edited. The tombstone ledger is curator-owned
and append-only: a published row cannot later change its status, successors,
display name, lineage signature, or reason. A name or path move needs only a
catalog refresh; it must not mint a replacement ID.

## Consumer pinning and resolution

Consumers must record both `catalog_schema_version` and an immutable CultureMech
Git commit SHA (or a release tag resolving to one) for the catalog they used.
Branch names and raw `main` URLs are not reproducible pins.

To resolve a reference, look up the exact ID in the pinned catalog, then:

1. read the current record at `file_path` for `ACTIVE`;
2. follow the sole successor for `MERGED`, retaining the source ID as provenance;
3. preserve `DELETED` as an unresolved historical reference; or
4. preserve all candidate successors for `SPLIT` until domain context selects one.

Do not fall back to display names or paths when an ID is absent. An absent ID means
the producer/catalog versions are inconsistent and should be surfaced as an
integrity error.
