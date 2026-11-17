# Variant prose review inventory

The structured ingredient inventory reads reviewed `ingredient_changes`, while
free-text variant modifications remain review inputs.
`scripts/inventory_variant_prose.py` makes that curation gap inspectable without
guessing chemical identities or changing recipes. It scans the entire normalized
catalog and writes a lossless review queue, including variants with no
modification entries as context-only rows. Every row starts `UNREVIEWED`.

## Reproduce the queue

Use the maintained Python environment and committed lock file. Start with a plan:

```bash
uv sync --frozen --extra dev
just plan-variant-prose
```

After changing the producer, copy one real recipe into an isolated input
directory. Run the same build and verify CLI on that one-record canary before
the full catalog. `algae/Bold_Basal_Medium.yaml` exercises several modifications
and source evidence. Verify that the queue exists, preserves the original text,
and has the expected rows; a successful exit alone is insufficient.

```bash
uv run --frozen python scripts/inventory_variant_prose.py \
  --input-dir .temp/variant-canary-input --output-dir output/variant-canary
uv run --frozen python scripts/inventory_variant_prose.py \
  --verify output/variant-canary --input-dir .temp/variant-canary-input

just build-variant-prose output/variant-prose-candidate
just verify-variant-prose output/variant-prose-candidate
shasum -a 256 output/variant-prose-candidate/manifest.json
```

Each destination must be new and outside the input tree. Outputs remain
gitignored. Preserve the bundle, manifest digest and exact committed producer
revision in durable evidence storage. For a downstream handoff, obtain the
manifest digest independently from the reviewed producer receipt and pass it as
`--expected-manifest-sha256`; hashing an untrusted received manifest does not
authenticate its provenance. An unpinned verification establishes local
consistency only.

The manifest binds every scanned YAML input, including records without variants,
and the producer, schema, lock and runtime. Verification checks membership,
source bytes and output content against the current source. A changed corpus or
producer needs a new bundle. Read `review_queue.tsv` with a CSV parser: prose and
JSON cells can contain quoted tabs and newlines.

## Review and scientific disposition

Keep recipe ID, source path and hash, zero-based variant/modification indices and exact
text together. These indices identify locations within one source snapshot;
they are not permanent IDs. Full variant JSON retains evidence and metadata,
and record references provide surrounding provenance. A row is a review unit,
not an ingredient, chemical identity, approved mapping, or growth claim.

Review the cited evidence and experimental context before deciding whether a
modification belongs in a structured recipe, a separate variant record, or an
explicit unresolved/context-only disposition. For example, a stock-culture
amendment and an assay treatment in the same variant description may apply at
different stages. Preserve that distinction and the original dose and units.
Do not infer a universal medium ingredient from either statement.

Apply any resulting scientific changes through the normal record-curation and
validation workflow. Regenerate the structured ingredient bundle only after
those changes are reviewed. Queue generation alone does not close #683 and
does not enlarge the running MIM campaign's frozen input scope. Record any
later accepted additions or holds in the integrated release ledger (#687).

This queue covers `variants[].modifications` and variant context. It is not an
inventory of all ingredient mentions in every notes, protocol, or prose field.

## Curate structured variant ingredients

Use the repository's `curate-yaml-record`, `review-ingredient-concentrations`
and structured record-review workflow for scientific decisions. The queue is a
complete accounting surface for the selected snapshot; one row can contain zero,
one or several ingredient assertions. Give every row a disposition, including
condition-only text, already represented claims and explicit evidence/model holds.

The maintained model is `MediaVariant.ingredient_changes`. Each change requires:

- `action`: `ADD`, `REMOVE`, `REPLACE`, `SET_CONCENTRATION` or `SET_AMOUNT`.
- `ingredient`: the introduced, removed or concentration-target descriptor;
  retain an explicit source label when ontology identity is unresolved.
- `stage`: the experimental/preparation stage, including alternative routes.
- `source_modification_index` and `source_text`: exact zero-based location and
  unchanged text from this variant's `modifications` array.
- `evidence`: nonempty SUPPORT evidence with reference, short source snippet
  and an explanation of the supported assertion and its limits.

`REPLACE` additionally requires `replaced_ingredient`; other actions forbid it.
`SET_CONCENTRATION` requires an asserted descriptor concentration. Preserve stock
strength, addition volume, final concentration, discrete treatments, isotope and
hydrate distinctions. Where an input is a batch mass/volume or the percentage
basis is unspecified, use a literal `amount` with its explicit `basis_statement`
rather than invent a concentration. `SET_AMOUNT` requires that amount; `ADD` and
`REPLACE` can also carry it. An amount and descriptor concentration cannot coexist
on the same change. Unsupported quantity claims remain explicitly held.
These changes do not apply themselves to the base recipe or establish its complete
equivalence to the study formulation.

Prepare explicit decisions using the shape in
`conf/variant_ingredient_curation/bbm-canary-683.json`. Bind each record to its
path, stable ID and preimage SHA256, each selected variant to its index/name, and
every change to exact source prose. Save the claim review against those inputs
before applying it. The public primary evidence, reviewed proposal and scripts
are the reproducible method; an LLM response alone is not a curation receipt.

```bash
just preview-variant-ingredients conf/variant_ingredient_curation/bbm-canary-683.json
uv run --frozen python scripts/curate_variant_ingredients.py DECISIONS.json \
  --only-record data/normalized_yaml/CATEGORY/RECORD.yaml \
  --apply --receipt .temp/variant-curation/CANARY-RECEIPT.json
uv run --frozen python scripts/curate_variant_ingredients.py DECISIONS.json \
  --apply --receipt .temp/variant-curation/APPLY-RECEIPT.json
```

The applicator previews by default, prevalidates every selected record, refuses
source drift or overwriting previous different curation, and inserts only new
fields at parsed YAML block boundaries. Existing scalar spelling, comments and
wrapping remain intact. It requires the entire parsed result to equal the native
validated proposal and refuses unsupported layouts. Apply uses a staged validated
write and atomic replacement. It persists a receipt before the first mutation and
before/after each record. An interrupted batch reports observed per-record hashes;
inspect the receipt rather than assuming all-or-nothing rollback. Replaying an
already identical decision is a no-op, with no new history event.

Run one actual record end to end before a batch. Verify unchanged base ingredients
and original prose, actual YAML persistence, native validation, the new occurrences
and the complete change ledger through the same bundle CLI. The BBM canary separates
assay estradiol from earlier NH4Cl stock culture; it does not establish coverage
of other source families. Independently review subsequent bounded source families.

After applying reviewed decisions, run the native schema, strict, ID and product
checks and relevant export tests. Commit the producer, source decisions, reviews
and recipe changes; build a fresh full-catalog version 3 bundle from that clean
revision. Report original queue coverage and remaining holds separately from
ingredient-group and occurrence counts. Hand MIM the exact source revision,
manifest digest, artifacts and contract change for explicit intake adoption;
preserve its running campaign's frozen inputs.

### Correct source claims and retain unresolved names

Use `curate_variant_completeness.py` for reviewed follow-ups. Its proposal records
use the same path, ID and byte hash guard, with `append_changes`, `append_mentions`,
`replace_changes` and `replace_modifications` inside each selected variant.
Replacements require the entire exact previous value and an explicit replacement.
The bounded `field_replacements` operation can correct variant descriptions,
purposes and evidence, or remove one exactly identified unsupported growth
descriptor. Other record fields remain outside this tool's mutation scope.

An unresolved mention retains a verbatim `source_label`, exact source index/text,
reported action, stage, reason and nonempty `held_fields`. Use `SOURCE_CLAIM`,
`IDENTITY_FORM`, `QUANTITY`, `OPERATION` or `STAGE` to distinguish the uncertainty.
Optional evidence and `reported_quantity` remain uninterpreted. No ontology ID or
positive-presence assertion belongs in this collection. A known ingredient can
have a supported event and a separate quantity/form hold.

When reviewed cohorts overlap the same recipe, merge them before applying;
separate applies would invalidate each other's source hashes. The maintained
`scripts/adhoc/audit_variant_completeness_683.py merge` validates each independently
pinned cohort and the combined native recipe, retaining disposition-only rows
without creating empty history events. Save independent scientific reviews before
the authoritative apply.

```bash
uv run --frozen python scripts/curate_variant_completeness.py DECISIONS.json \
  --receipt .temp/variant-curation/PREVIEW.json
uv run --frozen python scripts/curate_variant_completeness.py DECISIONS.json \
  --only-record data/normalized_yaml/CATEGORY/RECORD.yaml \
  --apply --receipt .temp/variant-curation/CANARY.json
```

Run the same native bundle build/verify path on the persisted canary and check the
positive, complete-change and hold ledgers. Only then apply the whole proposal,
supplying `--completed-receipt CANARY.json` and
`--expected-completed-receipt-sha256 PIN` to retain the verified canary unchanged.
The receipt records exact before/after bytes and the decision digest. Replays
require both the unchanged proposal and independently pinned successful receipt.
An incomplete receipt is evidence of partial progress, not permission to retry
blindly against changed files.

The original queue is immutable even when a source correction changes current
prose. The completeness audit joins original coordinates to corrected text and
counts supported events and retained holds separately. Its registered successor
capsule proves each exact recipe/history change and restores the earlier source
for historical audits, surviving squash merges and branch deletion. It does not
replace the scientific claim review. Deliver the resulting seven-product bundle
and complete coverage ledger to a separate MIM intake.
