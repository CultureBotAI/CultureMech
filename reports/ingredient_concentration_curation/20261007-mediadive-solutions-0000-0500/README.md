# MediaDive Solution Evidence: Records 0-499

Status: **applied locally; all-record curation remains incomplete**.

This batch processes the first 500 records in the frozen
[source inventory](../20261007-source-inventory.json), sorted by exact upstream
solution ID and git path. The inventory contains 4,770 pending solution records
plus the five previously curated stocks, within 15,910 normalized records.
This batch spans solution IDs 1 through 670, with gaps; it is not the integer
range 1-500. It does not replace the goal's other media, stocks, or variants.

Baseline: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`, freshly fetched before work.
Only authoritative normalized YAML was edited. No IDs, ingredient identities,
membership, roles, growth associations, prior evidence, or prior history were
rewritten; new provenance was appended.

## Results

| Result | Count |
| --- | ---: |
| Exact records processed, with one report each | 500 |
| Records changed | 442 |
| Records unchanged | 58 |
| Operational failures / schema-blocked records | 0 / 0 |
| Water quantity/unit corrections | 189 |
| Unchanged mass concentrations receiving evidence | 2,133 |
| New ingredient-level evidence entries | 2,322 |
| Unsupported claim rows retained | 1,674 |
| Conflicting claim rows retained | 200 |

The [pinned plan](plan.json) contains every exact path, stable ID, original and
proposed quantity, source response hash, literal source excerpt, locator,
decision, and before/after record hash. [Per-record reports](records/) cover all
stored concentration objects, missing direct ingredient amounts, and detected
source-only ingredients/stock additions. Each report has exactly one `- Record:`
line. These reports are not assertions that every claim in a processed record is
verified. There are 4,196 decision rows, including 325 source-only rows.

The 189 corrections replace the importer's mislabeled volume percentages with
the source's water addition in liters per prepared batch. For example, solution
18's 500 ml water addition becomes 0.5 L, not 1 L or 1000 percent. No final volume
or liquid density is inferred. Automatic water correction is refused when source
preparation steps, local preparation notes, stock attributes, or conditional rows
require interpretation.

The mass values did not change. Their evidence supports explicit provider `g_l`
values, cross-checked against amount, mass unit, and provider-declared solution
volume. Rounding is bounded by both reported precision and a small relative
tolerance; unit-scale differences fail. These are provider-declared solution
concentrations, not measured final concentrations in a receiving medium.

Each accepted claim has its own official institutional URL, exact JSON snippet,
field path, arithmetic explanation, retrieval timestamp, and response hash in
the YAML. Bibliographies identify the dataset, title, discovery mode, source
organization, and access date. Individual authors and publication year are absent
from these 500 source responses and were not invented. No DOI was invented.

## Unresolved Decisions

The remaining 1,874 rows include different kinds of scientific and structural
work, not 1,874 independent missing recipes:

- 499 legacy placeholder/other out-of-scope-context rows.
- 447 rows with source attributes such as stock strength or material grade.
- 325 source-only ingredients or nested stock additions needing structural curation.
- 265 water rows requiring interpretation of preparation steps.
- 189 source arithmetic inconsistencies between `g_l`, amount, unit, and volume.
- 73 other unit/liquid contexts and 50 optional/conditional rows.
- 13 missing numeric inputs, 9 ingredient-inventory conflict rows, 2 ambiguous
  compound matches, and 2 source zero amounts requiring preparation context.

None of these rows was promoted to SUPPORT evidence or assigned an inferred
quantity. Source zeros are not silently treated as fixed concentrations. The
old values remain visible alongside the exact source and decision in the reports.

## Verification

- Official source retrieval: 500/500 successful HTTPS responses, fetched serially
  with rate limiting. Response status, returned ID, origin URL, timestamp, and
  bytes are checked; raw response caches remain outside the repository.
- Preview: all 500 baseline and proposed records passed closed-schema validation.
- Full `just validate-strict --workers 1`: **15,910 records, zero errors**, both
  before and after applying the batch.
- Write-time validation reran before any writes; the whole batch was preflighted
  against record/source hashes and the reviewed plan.
- Read-back: all 500 result hashes matched; **2,322/2,322 new snippets** match
  their source responses exactly and are attached to the intended quantities.
- A second apply changed zero records and recognized all 442 applied results.
- Combined regression selection: **162 passed**. The subsequently expanded
  reviewer and offline batch-integrity selection passed **32 tests**; the suites
  overlap and should not be added as independent totals.
- Ruff, Black, and `git diff --check`: passed.
- Full `just assign-ids-check` baseline passed. An independent semantic diff
  audit of all 450 currently edited records proved IDs, names, ingredient
  membership, and all other fields unchanged except quantity objects and appended
  evidence, bibliography, and curation-history entries.
- `just validate-products` baseline could not perform ontology validation because
  `oaklib` is absent from the isolated runtime. Its adapter failures are not
  evidence of new data defects; no ontology IDs or labels changed.
- `just validate-references` could not spawn `linkml-reference-validator` in that
  runtime. The verified source retrieval and substring/arithmetic checks above
  are separate from this unavailable validator.
- The current merger does not include these standalone compositions: all changed
  solution fingerprints were unchanged, and no processable media input changed
  in this batch. The preceding full merge gates already recorded existing name,
  fingerprint, and freshness failures. They were not rerun for this excluded
  solution-only batch; no generated merges or pages were patched.

Validation used the isolated Python 3.11 runtime with the current repository
schema/source and PyYAML's native safe parser. Source verification is automated
exact-ID/label/arithmetic checking of retrieved structured records, supplemented
by manual inspection of representative sources and conflict cases; it is not a
claim of manual reading of every sentence in 500 source records.

## Reproduction And Continuation

The maintained tools are
[`fetch_solution_concentration_sources.py`](../../../scripts/fetch_solution_concentration_sources.py)
and [`review_solution_concentration_evidence.py`](../../../scripts/review_solution_concentration_evidence.py).
The original scoped five-stock mutator supplies shared snippet and presentation
helpers and remains unchanged.

With a configured project runtime and a local cache directory:

```bash
PYTHONPATH=src uv run python scripts/fetch_solution_concentration_sources.py \
  --inventory reports/ingredient_concentration_curation/20261007-source-inventory.json \
  --cache <cache-directory> --offset 0 --limit 500
PYTHONPATH=src uv run python scripts/review_solution_concentration_evidence.py \
  --cache <cache-directory> \
  --plan reports/ingredient_concentration_curation/20261007-mediadive-solutions-0000-0500/plan.json \
  --verify
```

This plan can be reapplied idempotently with `--apply`. Changed source bytes or
concurrent record edits are refused; create a fresh review rather than bypassing
those guards. Missing/failed source captures never count as successful coverage.

The next unprocessed slice of this frozen inventory starts at **offset 500**:
`data/normalized_yaml/bacterial/mediadive_672_Solution_A.yaml`,
`CultureMech:015080`, upstream solution 672. Fetch with `--offset 500 --limit 500`,
then preview using the same slice and a new `--plan` path before any apply.
There are 4,270 further records in this inventory, plus unresolved rows in the
already processed records. The remaining normalized corpus, variants, and derived
merge reconciliation remain part of the full objective.
