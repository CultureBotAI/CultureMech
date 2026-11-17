# CultureMech ingredient inventory and integrated mapping release

CultureMech supplies recipe occurrences, MIM curates ingredient identity and
mapping evidence, and KG-Microbe (KGM) admits the reviewed mapping products into
its transforms. This guide connects those existing responsibilities. Completing
an inventory does not complete the integrated release.

## What the catalog-wide list covers

The authoritative input is every `*.yaml` beneath `data/normalized_yaml/`,
including standalone solutions and separately modeled variant recipes. The
native occurrence scanner validates each record and collects root `ingredients`
or `composition`, plus recursively nested inline-stock composition. A referenced
stock already present in the scan contributes its own components once; the list
does not expand it into every referring medium.

Reviewed `variants[].ingredient_changes[]` contribute scoped occurrences for
`ADD`, `SET_CONCENTRATION`, `SET_AMOUNT`, and the introduced side of `REPLACE`. The complete
change ledger also retains `REMOVE` and the displaced side of `REPLACE`, which
never enter positive ingredient counts. Each change retains its variant,
experimental stage, source modification and evidence. The scanner does not apply
these operations to the parent or compute a final variant formulation.

Unresolved named claims belong in `variants[].ingredient_mentions[]` and the
separate hold ledger. Each retains a verbatim label, source text, variant, stage,
reported operation and the unresolved fields: source claim, identity/form,
quantity, operation or stage. These rows do not assert positive presence or an
ontology identity. A quantity hold does not invalidate a separately supported
ingredient identity. Text not yet curated into either structured collection,
including other notes and protocol prose, remains outside this extraction.
Inline copies with extra content beyond
their referenced stock are also outside its direct-containment contract; see
[the occurrence guide](unmapped_ingredients_guide.md). These limitations remain
visible curation work. Do not turn a prose mention or a name match into an
identity assertion merely to claim complete chemical coverage.

The separate [variant prose inventory](variant_prose_inventory.md) produces a
reproducible `UNREVIEWED` queue with exact modification text and evidence.
It supports [source-bound curation](variant_prose_inventory.md#curate-structured-variant-ingredients)
of this gap; queue rows alone are not ingredient occurrences or approved additions
to MIM's frozen intake. A complete disposition ledger can still contain explicit
evidence or representation holds; report those instead of claiming all prose is curated.

`ingredients_list.tsv` is the compact inventory. The lossless exchange surface
is `ingredient_occurrences.tsv`, identified by
`(recipe_id, component_field, component_index)` **within the pinned source
snapshot**. An array index can change between revisions. Keep source paths,
source labels, compound IDs, descriptor JSON and resolution evidence with each
occurrence. Counts of distinct names, resolved identities, review cases, recipes
and occurrences are different measurements.

## Version 3 exchange contract

The manifest contract is `culturemech-direct-ingredients-v3`. The occurrence TSV
keeps its original columns and appends variant context. The new
`variant_ingredient_changes.tsv` contains one descriptor row for each change,
plus a second row for the displaced descriptor of a replacement. It preserves
the complete source change in `change_json`, the descriptor in `ingredient_json`,
and evidence in `evidence_json`.

Version 3 adds `variant_ingredient_holds.tsv` as the seventh product and supports
literal `amount` in the complete change JSON. `SET_AMOUNT` changes a source-stated
batch input without asserting a final concentration. Amounts can also qualify
`ADD` or `REPLACE`. Mass/volume units use `PER_BATCH`; a percentage whose source
does not specify w/v or v/v uses `UNSPECIFIED_PERCENT`. The required basis
statement preserves the source denominator and its limits. Do not fill the
concentration columns from these amounts.

Hold rows carry `held_fields_json`, exact `mention_json`, optional evidence and
reported quantity, `review_status=WITHHELD` and `counts_as_presence=false`.
MIM must retain these rows in its intake even when their labels are absent from
the compact positive inventory. Resolving a held label is distinct from approving
the source assertion or making it present in a base recipe.

`counts_as_presence` is an inventory inclusion flag: true for an introduced,
concentration-target or literal-amount-target descriptor, false for a removal,
displaced descriptor or held mention.
It does not establish a nonzero concentration, an initial dose, or an ingredient
present in every condition. In particular, a concentration set to zero remains
an explicit change target. Consumers must retain the action, stage and quantity
context; neither positive rows nor the compact list are a fully expanded recipe.

Variant occurrence coordinates use `component_field=variants/V/ingredient_changes`
and `component_index=C`, both zero-based. The ledger adds `descriptor_role` to
that key; `descriptor_path` is a JSON pointer such as
`/variants/0/ingredient_changes/1/replaced_ingredient`. Source modification indices
refer to the same pinned recipe bytes. Grouping still uses the existing MIM resolver,
so a known identity gains occurrences and an unresolved label stays visible.

Version 1 and 2 consumers must explicitly adopt this contract. Old bundles remain
verifiable with their pinned archived producer. Consumers must admit the new
columns and companion ledgers, preserve scope, and reject attempts to flatten
negative/context-only mentions into positive medium edges. A new CultureMech
bundle does not authorize replacement of a running MIM campaign's frozen inputs.

## Build and verify one candidate

Use the maintained Python 3.13 environment and the committed lock file:

```bash
uv sync --frozen --extra dev
just check-mim-label-index
just plan-ingredient-release
```

For a first run after changing the producer, copy one actual recipe into an
isolated input directory and run the same build and verify commands below with
`--input-dir`. This exercises schema validation, the real pinned resolver,
artifact persistence and accounting. It does not prove reference handling across
the full corpus or full-catalog completion.

```bash
uv run --frozen python scripts/ingredient_release_bundle.py build \
  --input-dir .temp/ingredient-canary-input \
  --output-dir output/ingredient-canary
uv run --frozen python scripts/ingredient_release_bundle.py verify \
  --input-dir .temp/ingredient-canary-input \
  --bundle-dir output/ingredient-canary

just build-ingredient-release output/ingredient-release-candidate
just verify-ingredient-release output/ingredient-release-candidate
```

The destination must be new. The wrapper uses the existing aggregation and
pinned `culturemech.ingredients.mim_label_index` resolver; it introduces no
second matching algorithm. It stages the list, uncapped occurrence table,
mapped/unmapped YAML views, complete variant change ledger, error report and manifest
together. Input failures
or changed dependencies prevent successful publication. Ordinary aggregation
outputs and another campaign's frozen inputs remain untouched.

The manifest binds actual input membership/content (including records that
contribute no direct occurrences), producer/schema/resolver and lock bytes, the
packaged MIM label-index provenance, runtime, product hashes and parsed counts.
Verification checks the bundle against current inputs and code, not merely its
timestamp. Keep the exact source revision and manifest digest with a handoff;
retain the generated bundle in durable evidence storage. Generated outputs stay
gitignored. A dirty-tree candidate needs its exact changes committed and a fresh
build before it can serve as a release origin.

The producer records `shasum -a 256 BUNDLE/manifest.json` in the reviewed handoff.
The consumer verifies using that independently obtained digest:

```bash
just verify-ingredient-handoff output/ingredient-release-candidate "$EXPECTED_MANIFEST_SHA256"
```

Do not calculate the expected digest from a newly received manifest and treat
that as authentication. Ordinary `verify-ingredient-release` checks local
consistency only; its recorded source revision is not an independent provenance
attestation. A pinned handoff also verifies the exact manifest bytes before and
after checking its inputs and products.

For an identical preserved corpus outside the checkout's default input path,
call the verifier with both `--input-dir` and `--expected-manifest-sha256`.
Its exact membership and bytes must match; the pinned original scope is retained.
Moving a subset into the default directory never makes it a full-catalog origin.

CSV parsing is required: embedded newlines and quoting make physical line counts
unsafe. Require zero input errors, complete occurrence/list accounting, and
explicit mapped/unmapped/ambiguous outcomes. The verifier also reconciles the
positive variant coordinates exactly against eligible change-ledger rows and
requires both descriptors of every replacement. An unresolved row is retained work,
not a dropped observation. Equal hashes establish byte identity, not scientific
approval or an assertion that upstream has not advanced.

## Coordinate CultureMech → MIM → KGM

Use one release ledger (an issue or review record) to record exact revisions,
artifact digests and evidence for each stage:

| Stage | Required evidence | Completion boundary |
| --- | --- | --- |
| CultureMech inventory | Full structured-catalog manifest, verified products, occurrence counts and declared exclusions | Source intake is reproducible; chemical review is still separate. |
| MIM intake and curation | Accepted CultureMech manifest digest, pinned KGM unmatched inputs, original-case accounting, scientific decisions and holds | Every source case is retained or given an explicit reviewed disposition. |
| MIM export | Exact MIM commit, supported SSSOM, withheld SSSOM, dispositions and validated manifest; any scoped identity/occurrence companions | Full export validates against the actual review and source snapshot. A live adoption process is not an export. |
| KGM candidate | Independently reviewed pin, source archive and complete export hashes; candidate delta and runtime tests | Candidate generation succeeds without changing production mappings. |
| KGM integration | Paired mapping installation, affected transforms, source-finalization receipts, consumed-input fingerprints and graph validation | Tested graph output is bound to those exact admitted inputs. |

MIM's native reviewed exporter is
`mediaingredientmech.export.reviewed_sssom`; its `export-reviewed-sssom` and
`qc-reviewed-sssom` recipes describe the selected revision's contract. Check the
active campaign's contract before selecting the recipe: newer stable-ID or
scoped products may require additional reviewed companions. Keep those companions
with the export rather than flattening source-scoped assertions into global
name aliases. Do not promote withheld rows to supported mappings.

KGM already documents its immutable-commit workflow in
[MIM_REVIEWED_RELEASE.md](https://github.com/Knowledge-Graph-Hub/kg-microbe/blob/main/docs/MIM_REVIEWED_RELEASE.md)
and scoped evidence in
[INGREDIENT_BUNDLE.md](https://github.com/Knowledge-Graph-Hub/kg-microbe/blob/main/docs/INGREDIENT_BUNDLE.md).
Read those files at the selected **KGM revision**; links to `main` are navigation,
never release pins. Do not copy a historical example SHA or artifact digest into
a new release. Its candidate command has this shape:

```bash
poetry run python -m scripts.refresh_reviewed_mim \
  --source-archive data/<pinned-MIM-source>.tar.gz \
  --release-directory data/<validated-MIM-export> \
  --output-directory data/<new-candidate>
```

The pin and source archive are checked independently of the producer's manifest.
Review the candidate and quarantine, then install the supported MIM table and
reviewed unified candidate together through the normal PR workflow. A copied
SSSOM alone does not update all consumer lookups. Transform affected sources and
follow KGM's source-finalization and merge contracts; never rehash old output to
make it appear regenerated. Merging remains a separate owner decision.

CultureMech's packaged MIM label index is a separate consumer artifact. Refresh
it from the selected full MIM commit with `just refresh-mim-label-index` (preview
first), verify the resulting pin, and regenerate the inventory as a new snapshot.
Retain the pre-curation inventory and its unresolved cases so the new resolution
cannot erase evidence of what was submitted.

## Pattern for future Mech transforms

Reuse the same boundaries: versioned authoritative sources, a deterministic
producer, a complete input/output manifest, explicit unresolved or withheld
records, independently pinned consumer admission, and exact consumed-input
receipts through graph validation. Each Mech defines its own scientific scope
and identity policy. This first adapter does not create a universal resolver,
automatically authorize releases, or replace KGM's existing transform contracts.
