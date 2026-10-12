# Formulation-Aware Merge Repair

This is an integration repair for evidence-backed ingredient curation, not an
additional concentration review or a claim that the all-record goal is finished.
No authoritative ingredient amount, snippet, reference or record ID was changed.
Tracked derived YAML has not been regenerated or published.

## Reproduced Defects

Six new regression cases failed against the preceding implementation: four
amount/reference-only-stock merge cases, scoped/root evidence loss, and mutation
of loaded source records. The real M1038/M781/M3009 collision remains a single
ingredient-set candidate group but now produces three separate formulation
groups. The M1038 recipe retains all seven stocks and its source evidence.
The prior [failed retention result](../20261008-togo-methanogens/merge-retention.json)
is preserved as a historical baseline, not overwritten with a passing result.

## Behavior

- `group_recipes`/`find_duplicates` retain broad ingredient-set candidate discovery.
- The CLI uses `group_formulations`. Scientific assertions, amounts, stock
  boundaries and references, conditions, preparation and notes must agree as
  encoded. Different units are not converted; missing amounts are not zero.
- Direct merger calls reject incompatible formulations, including when a caller
  supplies the old ingredient-set fingerprint. Supplied fingerprints are checked.
- Compatible recipes retain all evidence at corresponding ingredient/stock
  locations and all root references, sources and curation events. Distinct
  snippets sharing a URL are not deduplicated into one claim.
- Comparisons retain list order so index-based evidence is not misassigned.
  Hydrate labels and unknown scientific fields remain significant. Copies of
  loaded records are not mutated. Standalone-solution routing remains intact.
- Malformed formulation data or read failures abort grouping before any CLI
  output. Typed empty-composition routing and placeholder exclusions remain
  separate from those failures; candidate discovery keeps its permissive API.
- `merge_fingerprint` keeps its existing ingredient-set schema meaning. The
  formulation hash controls grouping/filename disambiguation; no IDs are minted.

This deliberately does not declare chemical equivalence from names or erase
free-text conflicts. Identical encoded assertions can still be unsupported.
Cross-source identity/variant review and source-backed concentration curation
remain necessary. Scalar provenance that cannot be unioned losslessly remains
part of the comparison, rather than being discarded.

## Validation

The focused run passes 120 tests, including the actual three-record collision,
nested evidence, numeric/unit/basis changes, unknown fields, cycles, malformed
provenance, the CLI and independent-audit mutation probes. Ruff and Black pass on
this repair's Python files. The [final retention audit](retention-strict.json)
passes on all 15,910 tracked normalized paths: 10,783 eligible inputs retain
their checked assertions and provenance across 10,777 closed-schema-valid output
groups. There are six two-record groups. Existing routing exclusions remain:
4,785 standalone solutions, 340 media with empty/unfingerprintable composition,
and two placeholder-only media. These exclusions are not new omissions or
completed concentration reviews. Source byte hashes remain unchanged.

The full suite reports **9,729 passed, 19 skipped and two failures**, both
derived-data freshness checks. After regeneration, the manifest's targeted test
and all 27 recipe-index tests pass; the original full run remains a failed run,
not a green rerun. The fast tier passes **7,858 tests**, with 16 skipped and
1,890 deselected. All [broad checks](validation.json) are terminal. Legacy merge
verification fails with 1,247 name conflicts and 3,287 fingerprint issues. The
temporary freshness rebuild also fails comparison: 6,320 tracked versus 10,777
fresh outputs, with 4,275 tracked-only, 8,732 fresh-only, 2,045 changed shared
paths and none unchanged. These checks used the partial locked Python 3.13
runtime, not full CI. Tracked merge YAML was not replaced by the temporary build.
The [final combined check](final-checks.json) passes **148 tests**, Ruff, Black
and `git diff --check`. It verifies the production-code and normalized-source
hashes against the strict retention audit, the manifest against its preview,
and all eight refreshed indexes against their recorded output hashes.
The first successful [retention run](retention.json) and
[formatted-code run](retention-final.json) remain historical snapshots; the
strict-routing result above binds the final production-code hashes.

The independent [audit](audit.py) uses exact NUL-delimited `git ls-files` paths,
compares every grouped input against its actual output without using the
production projection as its expected answer, checks closed-schema validity,
and verifies that source bytes remain unchanged. The first audit attempt stopped
on Git's quoted Unicode path output; it performed no corpus writes. Inventory
parsing was corrected before the full audit rerun. The final audit also detects
unexpected added assertions and verifies production-code hashes at start/end.

See the [adversarial self-review](review.md) for reproduced findings, fixes and
explicitly unresolved issues. This is not an independent or GitHub review.

## Derived Metadata

The derived-artifact manifest was regenerated with its maintained writer. Its
only content change is one computed writer-attribution cell. A narrowly scoped
Git attribute preserves the empty final TSV column without treating its delimiter
as trailing whitespace. The manifest's exact-content freshness test passes.

The [index refresh plan](index-refresh-plan.json) and
[application result](index-refresh-application.json) record eight generated
index updates covering 66 unique records: 58 ingredient-count and 60 stock-count
fields. IDs, names, paths and source identifiers are unchanged. Preview/source/
target hashes were checked before publication and read back afterward. Generator
outputs differing only in timestamps were not copied. This updates metadata for
earlier ingredient/stock restructuring, not any authoritative quantity or quote.

## Remaining Work

Tracked merge outputs remain stale; the legacy verifier does not establish
formulation equivalence or closed-schema validity. Earlier cohort retention scripts using candidate groups
must use the formulation API when rerun; the DSMZ111 helper exercised by the
regression suite has been updated without altering its historical JSON result.
Then resume the source-backed J985, FeCl2-stock and JCM265 repairs and remaining
record inventory. No commit, push, PR merge or branch deletion is claimed.
