# Variant prose review inventory

The structured ingredient inventory excludes free-text variant modifications.
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
