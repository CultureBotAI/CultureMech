# Media Content Review Remediation

- **Baseline review:** 2026-08-24
- **Remediation date:** 2026-08-25
- **Scope:** All records under `data/normalized_yaml/` and directly affected derived artifacts
- **Mode:** Source-backed corpus remediation and audit hardening

## Executive Summary

The remediation covered all 15,877 normalized YAML records: 10,891 media and
4,986 standalone solutions. All records load successfully. The repaired corpus
contains 209,656 authoritative component entries, up from 208,591 because
previously omitted source compositions were restored.

The blocking media count fell from 256 to 150. Specifically, 74 missing recipes
were recovered from authoritative source material, all 32 unnamed components
were repaired, all 64 unparsed/prose-as-ingredient findings were cleared, and all
46 composition-type contradictions were adjudicated. Source-backed concentration
repairs removed 69 plausibility findings and three flattened-stock-cocktail
records without guessing unresolved quantities.

Ingredient identity was reconciled against MediaIngredientMech's primary SSSOM
(`mapping_set_version: 2026-08-18`) and real ChEBI content. Guarded migrations
corrected 10,874 serialized wrong-ID references, and 187 previously bare exact-MIM
groundings were adopted. The exact-name grounding-consistency backlog fell from
44 names / 3,932 rows to 28 names / 764 rows. Ambiguous residuals remain visible
rather than being resolved by majority vote.

The same MIM-verified correction table was replayed into the derived merged
corpus, correcting 5,312 stale term references in 1,866 records. This restored
the invariant that every merged `(ingredient name, term.id)` pair must still be
present upstream in normalized YAML.

The complete record-level outcome is in
[the master manifest](media_content_review_manifest.tsv).

## Baseline Versus Current

| Check | 2026-08-24 baseline | 2026-08-25 current |
|---|---:|---:|
| YAML records loaded | 15,877 | 15,877 |
| Authoritative component entries | 208,591 | 209,656 |
| Media status `BLOCKING` | 256 | 150 |
| Media status `NEEDS_REVIEW` | 2,045 | 2,084 |
| Media status `PASS` | 8,590 | 8,657 |
| Media with no usable composition | 224 | 150 |
| Components missing `preferred_term` | 32 | 0 |
| Unparsed/prose composition findings | 64 | 0 |
| Composition-type conflicts | 46 | 0 |
| Concentration-plausibility findings | 9,757 | 9,688 |
| Flattened stock cocktails | 186 | 183 |
| Review-need ranked records | 2,183 | 2,164 |
| Exact-name grounding splits | 44 names / 3,932 rows | 28 names / 764 rows |
| MIM SSSOM audit findings | 85 findings / 8,752 rows | 53 findings / 2,450 rows |
| Name/term element mismatches | 3 pairs / 1,307 rows | 4 pairs / 1,305 rows |
| Selective-agent mismatches | 0 | 0 |

`NEEDS_REVIEW` rose because repaired blocking records can become valid records
with non-blocking variable-concentration signals. It does not represent a new
structural defect. Likewise, restored compositions increased variable entries
from 4,429 to 4,516 while improving completeness.

## Current Required Checks

| Check | Current result |
|---|---:|
| Media missing `name` | 0 |
| Media with no usable ingredients or solutions | 150 |
| Components missing `preferred_term` | 0 |
| Component entries missing a concentration object | 205 |
| Components with malformed concentration objects | 0 |
| Components missing a concentration value | 0 |
| Components missing a concentration unit | 0 |
| Components using a non-schema concentration unit | 0 |
| `VARIABLE` or otherwise unspecified concentration entries | 4,516 |

The 205 absent concentration objects remain one direct water ingredient and 204
stock-solution additions. Of those stock additions, 140 carry non-asserted
candidates and 64 have no candidate. These require source evidence; candidates
were not promoted to assertions merely to clear a check.

## Composition Remediation

The missing-composition worklist now contains 150 genuinely empty media: 125
KOMODO ModelSEED records and 25 records from other or absent provenance. All now
have no ingredients and no solutions; placeholder pseudo-ingredients have been
removed. Thirty-six names cite a medium present in the tracked MediaDive index,
but that reference identifies the whole medium containing a named stock solution,
not the stock's subrecipe. Copying the whole formula would create plausible but
false chemistry, so those records remain blocked.

The 74 recovered formulas were limited to cases supported by preserved source
content, including DSMZ, JCM, MediaDB, MediaDive, CCAP, TOGO, SAG, and related
families. Shared-formula repairs were guarded by source IDs and focused tests.
No composition was inferred from a title, neighboring record, or likely recipe.

All composition-type conflicts are now resolved, and both unparsed-composition
reports are empty. This includes empty ingredient names, swapped name/value
fields, concatenated solution tables, and preparation prose stored as a chemical.

## Concentration Status

The current plausibility report contains 9,688 heuristic findings across 3,516
records:

| Finding | Rows |
|---|---:|
| `WATER_AS_VOLUME` | 594 |
| `TRACE_SALT_AS_STOCK` | 4,512 |
| `INDICATOR_UNIT_SLIP` | 4,582 |

There are 183 records with a flattened-stock-cocktail signature. These are still
review worklists, not proof that each value is wrong. Repairs were applied only
when the source supplied the final concentration or the stock addition volume.
Unresolved cocktails need per-record nesting under a stock solution with an
evidenced addition volume.

## Identity Reconciliation

Every exact-MIM correction is validated at runtime against the sibling
`MediaIngredientMech/mappings/ingredient_mappings.sssom.tsv`; corpus writes abort
if the SSSOM target or expected reference count has drifted. ChEBI targets used
for name-settled hydrate, salt, stereochemistry, and unrelated-compound repairs
were checked against the local OAK ChEBI database. The migration is idempotent:
its post-apply dry run reports zero changes.

The current MIM audit reports:

| Finding | Names | Rows |
|---|---:|---:|
| `DIVERGENT` | 5 | 64 |
| `INTERNAL_SPLIT` | 44 | 2,380 |
| `MISSING_GROUNDING` | 4 | 6 |

The six bare rows are under names that also carry multiple forms (`Lactose`,
`maltose`, `MES`, and anhydrous versus pentahydrate `Na2S2O3`). Applying an exact
mapping by normalized name would erase those distinctions, so they remain for
curation. The four element-mismatch pairs are sodium resazurin, disodium
2-oxoglutarate, and disodium glycerophosphate spellings whose current ChEBI terms
lack sodium; they remain explicit because substituting the unsalted species is
not a defensible identity repair.

## Remaining Work

1. Recover the remaining 150 formulas only from authoritative source content.
2. Resolve the 64 stock additions with neither asserted concentrations nor candidates.
3. Curate the 183 flattened cocktails using evidenced stock identities and addition volumes.
4. Adjudicate the remaining MIM divergences and underspecified name splits case by case.
5. Review the 274 filename-collision groups before any move, merge, or deletion.

Filename collisions currently comprise 56 `IDENTICAL`, 12 `EQUIVALENT`, and 206
`DIFFERENT` groups. They were classified only; no path was moved or removed.

## Verification

- Missing-composition ratchet: 150, passed.
- Concentration ratchets: 9,688 total and 183 flattened cocktails, passed.
- Unparsed-composition gates: 0 total and 0 exported, passed.
- MIM SSSOM ratchets: 5 divergent and 44 internally split names, passed.
- Grounding migration idempotence: 0 pending references, passed.
- Affected unit/integration suite: 414 passed.
- Full repository suite: 1,639 passed and 2 skipped.
- Closed LinkML schema validation: 15,877 files, 0 error files, 0 error rows.
- Scoped Ruff and code/test/report whitespace checks: passed.
- Derived-artifact freshness: all 9 checkable current-view audit artifacts
  byte-match fresh regeneration; all 12 recipe index/statistics artifacts were
  regenerated and pass field-level freshness checks.
- Normalized-to-merged grounding agreement: 0 stale `(name, term.id)` pairs.

The canonical artifacts are:

- [Master review manifest](media_content_review_manifest.tsv)
- [Missing compositions](../data/import_tracking/reports/missing_compositions.tsv)
- [Concentration plausibility](../data/import_tracking/reports/concentration_plausibility.tsv)
- [Composition-type conflicts](../data/import_tracking/reports/composition_type_conflicts.tsv)
- [Unparsed composition](../data/import_tracking/reports/unparsed_composition.tsv)
- [Grounding consistency](../data/import_tracking/reports/grounding_consistency.tsv)
- [MIM SSSOM divergence](../data/import_tracking/reports/mim_sssom_divergence.tsv)
- [Name/term element mismatch](../data/import_tracking/reports/name_term_element_mismatch.tsv)
- [Review-need ranking](../data/import_tracking/reports/review_need_ranking.tsv)
