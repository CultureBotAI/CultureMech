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

- `action`: `ADD`, `REMOVE`, `REPLACE` or `SET_CONCENTRATION`.
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
basis is unspecified, retain the literal quantity in notes rather than invent a
concentration. An unsupported quantity-only operation remains held for review.
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
  --apply --receipt .temp/variant-curation/APPLY-RECEIPT.json
```

The applicator previews by default, prevalidates every selected record, refuses
source drift or overwriting previous different curation, and checks that the
native writer will not reformat unchanged source. Apply uses a staged validated
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
and recipe changes; build a fresh full-catalog version 2 bundle from that clean
revision. Report original queue coverage and remaining holds separately from
ingredient-group and occurrence counts. Hand MIM the exact source revision,
manifest digest, artifacts and contract change for explicit intake adoption;
preserve its running campaign's frozen inputs.
