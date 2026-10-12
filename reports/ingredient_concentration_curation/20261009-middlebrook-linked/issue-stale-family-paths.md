# Report and Repair Stale Exact Family Paths

Status: open local issue draft. No GitHub issue was created. An ignored-inclusive
search of existing curation `issue*.md` files found no matching stale-family-path
issue before this draft was added.

The [ID-resolved inventory](next-acid-family-inventory-resolved.json) parses
all 15,910 current normalized YAMLs and compares their tracked paths with an
ignored-inclusive filesystem inventory. The 76 acid-name candidates belong
to 41 ID-resolved family components, including one additional neighbor:
`data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml`
(CultureMech:002222). These components contain **21 stale exact path references**.
All 21 resolve by a unique stable ID; they are not missing records or ID changes.

The initial [literal-path-only inventory](next-acid-family-inventory.json)
found 20 bad references in the initial candidates, but split two connected
families and missed that external neighbor. Preserve both receipts: the later
inventory explicitly labels ID fallback and retains every exact-path error.
The neighbor contributes the twenty-first stale reference.

Examples include child links to a bacterial-category KOMODO 119 path whose
current exact path is under `archaea/`, and the reciprocal Methanobacterium
IV/VI links with obsolete bacterial-category paths. Full source field paths,
reference objects, exact current paths and hashes are in the resolved inventory.

## Validator Limitation

`scripts/validate_media_variant_links.py:resolve_ref` accepts a valid stable ID
when a supplied path is not in its index. `validate_links` checks resolution
and reciprocity but does not report that the explicit path is stale. Thus its
zero findings in `corpus.json` are correct for its implemented checks, not
proof that every stored exact path is current. The eleven repaired Middlebrook
records separately passed the stricter path/ID/name audit and are unaffected.

## Required Follow-Up

1. Add a diagnostic for a supplied stale path even when ID resolution succeeds;
   retain the useful ID fallback rather than conflating path drift with an
   absent record. Test stale category paths, case drift, ID/path disagreement,
   missing IDs and reciprocal edges.
2. During the acid-family source reviews, use guarded exact-ID/current-path
   updates on both ends and preserve prior history. Do not renumber records.
3. Include the external JCM-derived VI record when reviewing the IV/VI family.
   Do not treat the graph's current duplicate/variant labels as source proof.
   Ingredient or relationship changes still need exact source-backed evidence.
4. Re-run the exact-path inventory and the semantic/link validators. Do not
   claim this issue is resolved merely because ID-fallback validation passes.
