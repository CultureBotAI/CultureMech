# Source and formulation review: 2x_yeast_extract_tryptone_2xyt (CultureMech:009454)

- Review: 20261021T081143Z-culturemech-009454-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:09:07Z
- Finished UTC: 2026-10-21T08:11:43Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M2919 identifies one opaque 2xYT component with a volume of 1 L. The generated target instead records 1 G_PER_L; the later owner records 1000 ML_PER_L, which adds a final-volume denominator not supplied by the provider. The owner also combines the separate 20 mL culture comment and one-liter component row into an unsupported transfer narrative. The generated target itself contains only a source URL in notes and does not assert that transfer. Owner corrections, field-linked evidence, and subsequent regeneration are needed. Completion is partial because the exact upstream primary formulation and internal product composition are not available from the source-less TOGO response.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 91; batch 010 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding nine task batches contain 90 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 92 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009454 | data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml | generated | 2x_yeast_extract_tryptone_2xyt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009454 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009454 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch010/091/strict.tsv |
| validate-terms | passed | True | CultureMech:009454 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009454 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009454 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Primary formulation and product provenance beyond TOGO M2919 | unavailable | True | CultureMech:009454 | The fully inspected exact provider response has empty src_url and no original_media_id. Original primary formulation/product identity remains unavailable; the exact TOGO identity and one-liter component row are independently resolved. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009454.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:009454.

0 primary CHEBI identities resolve with matching labels; 0 of 0 current secondary keys have live pinned-index rows. Unresolved keys: [].

1 direct ingredient instances; CHEBI-primary instance linkage 0/1 (0.00%), verified secondary coverage 0/1 (0.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Stable ID, exact provider accession and owner

identity: supported. Targets: CultureMech:009454.

CultureMech:009454 resolves to one generated MediaRecipe and its normalized bacterial owner. Original title and TOGO:M2919 match the exact API. The merge source identifies that owner; no synonymous sibling, formula fingerprint, or generic 2xYT name is used to substitute a different formulation.

### The sole component amount in both layers

quantity: concern. Targets: CultureMech:009454.

Provider amount 1 L is a volume-only source statement. Generated 1 G_PER_L changes the physical dimension without support. Owner 1000 ML_PER_L is a volume-per-volume concentration; 1 L equals 1000 mL, but the added final-liter denominator is not supplied. Use the existing volume-only L representation for the source amount, with field evidence. No density, stock strength, or 20 mL-to-1 L ratio is available for another conversion.

{"field_path": "ingredients[0].concentration", "source": {"value": 1, "unit": "L"}, "generated": {"value": "1", "unit": "G_PER_L"}, "owner": {"value": "1000", "unit": "ML_PER_L"}, "concentration_decision": "correct", "proposed_owner": {"value": "1", "unit": "L"}, "basis": "source volume, not final-volume closure", "action_taken": "none"}

### Opaque medium, chemical forms and stock boundaries

representation: unknown. Targets: CultureMech:009454.

The complete provider response has one opaque complex/undefined medium component and no internal ingredient amounts, supplier/catalog identity, nested stocks, solution references, or variants. Both local layers preserve the opaque name. No tryptone, yeast-extract, salt, water, hydrate, or stock quantity can be inferred from the 2xYT label. Its two-fold name is not an evidenced instruction to dilute or multiply this record.

### Separate provider comment versus later owner interpretation

scope: concern. Targets: CultureMech:009454.

The generated target has only the source URL in notes and makes no 20 mL transfer claim. The normalized owner notes and September repair-event notes instead say a 20 mL overnight culture is seeded in one liter. The provider says a single colony seeds the 20 mL culture; the one-liter ingredient is a separately listed row. These cannot be combined into an asserted transfer or inoculum fraction. CB9615 is retained only as an unresolved source token.

### Preparation and conditions

completeness: unknown. Targets: CultureMech:009454.

The owner preparation text says to use one liter, which agrees with the component volume; its MIX action is a local representation rather than a quoted detailed procedure. The source does not give internal product preparation, pH, temperature, atmosphere, sterilization, storage, or a quantitative meaning for overnight. No time, organism taxonomy, growth outcome, or transfer procedure is added. The generated target has no preparation_steps.

### Classification, applications and quality flags

scope: supported. Targets: CultureMech:009454.

COMPLEX/UNDEFINED agrees with the provider component properties; LIQUID is consistent with the liter-denominated medium row. Bacterial category and generic Microbial cultivation are catalog context, not demonstrated species-level growth. The owner has_unmapped_ingredients flag agrees with its ungrounded opaque row; ingredients_curated records curation status and does not prove the volume basis or comment interpretation correct.

### Later maintained repair versus stored generated record

consistency: concern. Targets: CultureMech:009454.

Both files share their first three timezone-aware import/ID/name events. The target records an August 6 merge; the owner records a September 8 repair and now has different concentration, ingredient source/notes, root notes, preparation, quality flags, and a root reference. These current differences establish generated/owner drift. The later owner is not assumed fully correct: its denominator and transfer wording require review before regeneration. Historical events remain append-only.

### Provider reference, claim evidence and unavailable upstream source

provenance: concern. Targets: CultureMech:009454.

The target has a notes URL but no structured reference or claim evidence; its actual reference diagnostic checked zero excerpts. The owner adds one root TOGO reference and an ingredient source string, but no exact amount or comment evidence. The API supplies provider-level support while its original primary source and product identity remain unavailable. Completion is partial for that required provenance gap, not because the provider-to-record dimensional discrepancy is uncertain.

## Findings

### f1: The one-liter opaque component is represented with unsupported concentration units

major / open / confirmed; issue key: CM009454-opaque-product-volume-basis.

The generated ingredients[0].concentration asserts 1 G_PER_L, while TOGO explicitly supplies volume 1 L. The maintained owner changes this to 1000 ML_PER_L, which preserves a volume numerator but adds a final-liter denominator absent from the response. The exact source amount can be represented as 1 L without density, final-volume, stock-dilution, or culture-transfer assumptions. Current importer code already maps l to L.

### f2: The normalized owner joins two source statements into an unsupported culture-transfer narrative

major / open / confirmed; issue key: CM009454-owner-culture-comment-scope.

This is an owner-specific error: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml notes and curation_history[3].notes describe a 20 mL overnight culture seeded in one liter. The source instead says a single colony of CB9615 seeds a 20 mL culture and separately lists one liter of the medium. The generated target notes contain only the source URL and do not make the transfer claim.

### f3: The generated record predates the maintained owner repair and omits its provenance fields

minor / open / confirmed; issue key: CM009454-generated-owner-provenance-drift.

The August merged target omits the September owner repair event and current owner ingredient source/notes, root reference, preparation_steps and data_quality_flags. Its quantity also differs, as assessed separately. The owner itself contains the unsupported denominator and transfer interpretation, so indiscriminately copying the later content would propagate defects.

### f4: Provider statements lack claim-level evidence and original primary provenance is unavailable

minor / open / confirmed; issue key: CM009454-claim-evidence-upstream-provenance.

The owner has one root TOGO URL but no ingredient or root evidence tying the exact volume and separate culture comment to their source fields. The generated target lacks that root reference and its reference diagnostic examined zero excerpts. The full provider API identifies M2919 but contains empty src_url and no original_media_id; no original collection, publication or product formulation was established.

## Recommended Actions And Acceptance Checks

### a1

Correct the normalized owner to the source-faithful value 1 unit L, attach exact amount evidence, and retain the opaque component identity. Regenerate the target only after all owner corrections and verify the volume-only unit survives. Do not expand an assumed standard recipe or infer any dilution from the 2x name or culture comment.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct the editable normalized-owner notes to keep the one-liter formulation row separate from the source culture comment. Preserve the existing repair event verbatim and append a new evidence-backed clarification event; do not rewrite historical notes. Do not add a transfer, inoculum percentage, taxonomy, time/temperature, or growth assertion. Review owner content before propagating it through regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Verify the future owner notes distinguish the single-colony-to-20 mL statement from the separate one-liter component and leave their relationship unresolved.

### a3

After correcting and evidencing the maintained owner, regenerate through the declared merge entrypoint and confirm that its verified source trace, preparation context, flags and append-only history survive. Do not hand-edit the generated YAML or treat the later timestamp as proof of scientific correctness.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Retain the existing owner reference and add narrowly scoped amount/comment evidence with exact snippets, provider API locator, original unit, actual capture date/hash and upstream limitations. Recover an exact original source if possible; if unavailable, preserve that limit. Keep the product opaque and avoid guessed ingredient identities, formula amounts or growth claims.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch010/091/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch010/091/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml:1:id: CultureMech:009454<br>./data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml:1:id: CultureMech:009454<br> |
| togo-source | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2919; $.meta; $.components[0].items[0]; $.comments | supports | Exact provider identity M2919 and original title match both records. One named complex/undefined component is quantified as a volume; no internal solutes, original accession, or upstream source URL are supplied. |
| source-volume | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2919; $.components[0].items[0].volume and unit; component_name supplies the row identity | supports | The only formulation row states one liter of the named opaque 2xYT medium. This is a volume-only amount, not a mass concentration or an explicitly normalized component addition per final liter. |
| source-comment | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2919; $.comments[0].comment, paragraph_index 1; component row is separately paragraph_index 3 | supports | The separate comment says a single colony seeds a 20 mL overnight culture in 2xYT. It does not say that a 20 mL culture is transferred into the separately listed liter. The strain token remains source context; no taxonomic or growth assertion is added. |
| togo-shell | https://togomedium.org/medium/M2919; Complete HTML and extracted page text | supports | The canonical medium URL resolves to an application shell. Its captured HTML supplies no independently inspectable formulation text; the exact API supports the comparison. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {} |
| mim-scope | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Pinned MIM source metadata and complete direct ingredient descriptors | supports | Pinned MIM commit 6643131b0f12ab40b66f98135245fca04027e0e9, index SHA256 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5, 9077 rows. Neither record asserts a primary chemical term or secondary MIM link for its one opaque medium component. Primary and secondary ingredient-instance linkage are each 0/1 (0%) in each layer on a 0–100 scale; this does not establish an erroneous ingredient identity or justify a guessed pure-chemical mapping. |
| importer-current-context | src/culturemech/import/togo_importer.py; _ingredient_from_item lines273–339; ordinary primary-item path lines609–640; _parse_unit lines713–746 | context_only | The inspected current ordinary-item path reads the provider amount/unit and explicitly maps l to the volume-only L enum. It does not support attributing the stored historical 1 G_PER_L to an unchanged current L conversion bug, nor does this static read prove the historical repair execution. |
| converter-current-context | src/culturemech/convert/togo_raw_yaml.py; Complete 55-line mechanical-conversion entrypoint | context_only | The raw-YAML converter declares a direct JSON-to-YAML conversion without normalization and delegates to JSONToRawYAMLConverter. It is not the maintained scientific correction owner and was not executed. |
| historical-repair-search | repository checkout; Exact basename repair_togo_mrs_2xyt_score40.py over ignored-inclusive file inventory | unknown | No current file with the historical repair basename was found. The owner event is retained as historical provenance, not treated as an inspected repair implementation or scientific validation. |
| owner-difference | data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml; All differing top-level nodes; source hashes pinned in source.inputs | supports | {"curation_history": {"generated": [{"timestamp": "2026-01-27T06:35:57.404404Z", "curator": "togo-import", "action": "Imported from TOGO Medium", "notes": "Source: TOGO, ID: M2919"}, {"timestamp": "2026-03-13T06:20:06.244709Z", "curator": "culturemech-id-assigner-v1.0", "action": "Assigned CultureMech ID", "notes": "Assigned stable identifier: CultureMech:009454"}, {"timestamp": "2026-03-17T19:46:25.216600+00:00", "curator": "normalize_media_names_to_snake_case.py", "action": "NAME_NORMALIZED", "notes": "Normalized name from \"2x Yeast Extract Tryptone (2xYT)\" to \"2x_yeast_extract_tryptone_2xyt\" for consistent matching"}, {"timestamp": "2026-08-06T03:04:34.069611+00:00", "curator": "merge_recipes.py", "action": "MERGED_RECIPES", "notes": "merged 1 source recipe(s) on fingerprint 69b8ae2d5ae1aa7966693ad313b2e2d767b26c1fc95c1f52c6f1abe5cf9c9a9e", "source": "2x_yeast_extract_tryptone_2xyt.yaml"}], "owner": [{"timestamp": "2026-01-27T06:35:57.404404Z", "curator": "togo-import", "action": "Imported from TOGO Medium", "notes": "Source: TOGO, ID: M2919"}, {"timestamp": "2026-03-13T06:20:06.244709Z", "curator": "culturemech-id-assigner-v1.0", "action": "Assigned CultureMech ID", "notes": "Assigned stable identifier: CultureMech:009454"}, {"timestamp": "2026-03-17T19:46:25.216600+00:00", "curator": "normalize_media_names_to_snake_case.py", "action": "NAME_NORMALIZED", "notes": "Normalized name from \"2x Yeast Extract Tryptone (2xYT)\" to \"2x_yeast_extract_tryptone_2xyt\" for consistent matching"}, {"timestamp": "2026-09-08T00:00:00-07:00", "curator": "repair_togo_mrs_2xyt_score40.py", "action": "RESOLVED_TOGO_MRS_2XYT_SCORE40", "changes": "Resolved score-40 TOGO MRS/2xYT one-liter product row", "source": "https://togomedium.org/medium/M2919", "notes": "TOGO M2919 records a 20 mL overnight culture seeded in one liter of 2x Yeast Extract Tryptone (2xYT); the source does not disclose the product's internal formulation."}]}, "data_quality_flags": {"generated": null, "owner": ["ingredients_curated", "has_unmapped_ingredients"]}, "ingredients": {"generated": [{"preferred_term": "2x Yeast Extract Tryptone (2xYT)", "concentration": {"value": "1", "unit": "G_PER_L"}, "notes": "Properties: Undefined component, Complex component"}], "owner": [{"preferred_term": "2x Yeast Extract Tryptone (2xYT)", "concentration": {"value": "1000", "unit": "ML_PER_L"}, "source": "TOGO M2919", "notes": "TOGO M2919 records one liter of 2x Yeast Extract Tryptone (2xYT) as an opaque product."}]}, "merge_fingerprint": {"generated": "69b8ae2d5ae1aa7966693ad313b2e2d767b26c1fc95c1f52c6f1abe5cf9c9a9e", "owner": null}, "merged_from": {"generated": ["2x_yeast_extract_tryptone_2xyt"], "owner": null}, "notes": {"generated": "Source: https://togomedium.org/medium/M2919", "owner": "TOGO M2919 records a 20 mL overnight culture seeded in one liter of 2x Yeast Extract Tryptone (2xYT); the source does not disclose the product's internal formulation."}, "preparation_steps": {"generated": null, "owner": [{"step_number": 1, "action": "MIX", "description": "Use one liter of 2x Yeast Extract Tryptone (2xYT)."}]}, "references": {"generated": null, "owner": [{"reference": "https://togomedium.org/medium/M2919"}]}} |

## Limits And Additional Notes

- The exact TOGO API identifies M2919, but src_url is empty and original_media_id is absent. No original publication, collection accession, manufacturer, catalog product, or exact internal formulation is established. Required upstream primary-source corroboration remains unavailable.
- The canonical TOGO page is an HTTP 200 application shell. The scientific comparison uses the captured exact provider API, with its actual access time and byte hash.
- The source lists a one-liter opaque medium component and separately comments on a 20 mL overnight culture seeded by a single colony of CB9615. No transfer between those volumes, dilution ratio, final-volume closure, strain taxonomy, measured growth, or organism-specific recommendation is inferred.
- No generic 2xYT recipe, commercial product formulation, nearby medium record, or standard practice is substituted for the undisclosed source component. Provider GMO properties are reported as source annotations, not independently validated ontology assertions or ingredient groundings.
- The current TOGO importer and mechanical converter were read statically. Current code already preserves the L unit; neither the historical import nor the later repair event was replayed. The named historical repair script was not found in an ignored-inclusive current-checkout file search; that bounded absence does not establish that it never existed.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T081143Z-culturemech-009454-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 2x_yeast_extract_tryptone_2xyt (CultureMech:009454)'
started_at: '2026-10-21T08:09:07Z'
finished_at: '2026-10-21T08:11:43Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: TOGO M2919 identifies one opaque 2xYT component with a volume of 1 L. The
  generated target instead records 1 G_PER_L; the later owner records 1000 ML_PER_L,
  which adds a final-volume denominator not supplied by the provider. The owner also
  combines the separate 20 mL culture comment and one-liter component row into an
  unsupported transfer narrative. The generated target itself contains only a source
  URL in notes and does not assert that transfer. Owner corrections, field-linked
  evidence, and subsequent regeneration are needed. Completion is partial because
  the exact upstream primary formulation and internal product composition are not
  available from the source-less TOGO response.
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
  state: working_tree
  inputs:
  - path: .claude/skills/audit-schema-gaps/SKILL.md
    sha256: 86467f280ecdd2d60531d3b2a9249d7a38efa4cfeab714d55421b9a62cfabb7d
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/linkage-and-duplicates.md
    sha256: e792d47f2b9e169d2306ac920f87aa1ced9b9d07c7650dd7d2feb7aee48c2234
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: e3f1aeccd3d249f78739c902ea8d95052fec26fc5db752b5ca732d96ab37e466
    role: context
  - path: .claude/skills/schema-gap-analysis/SKILL.md
    sha256: 09665fe53584559e776f75ab41dfabd997eff0cac10bafcca0a721b678ccee93
    role: context
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: e35781d4fd66de4289411141b4c8a94189782d864ba6c45e49bf46537c46c5a1
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
    sha256: 9b1102c84782f416ad523d9b10619284a2948937f70aa98199628274bbcbc9ca
    role: target
  - path: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    sha256: 6707e065ffece91b557d2918436592a119cd05fb49d1c99f9820c7c9ed86fa17
    role: context
  - path: docs/DATA_LAYERS.md
    sha256: 381cbb9ad2ba80f2a849507c4ce8b10839546ae4ce2757dad065e86fe381d236
    role: context
  - path: docs/record-review-profile.md
    sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 552166976136ed158a253773f0b763e670d2484e7354b48ec0f9b77b4250da77
    role: context
  - path: project.justfile
    sha256: 3576f5ce2adee0179be4f2d3fd134841249eb9a54a7eed8b388c3b345883a5fe
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/togo_raw_yaml.py
    sha256: ce5e73545c9ecde54724259d2fd475676c0f3cb44dcfd283950e89fd49c10993
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 91; batch 010 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding nine task batches contain
    90 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 92 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009454
targets:
- target_id: CultureMech:009454
  path: data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
  label: 2x_yeast_extract_tryptone_2xyt
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch010/091/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch010/091/strict.tsv"
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - validate-references
- check_id: structured-source-adapter
  name: iModulonDB applicability
  required: false
  status: not_applicable
  summary: The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic
    dataset requiring an iModulonDB cross-check; expression-module membership cannot
    establish this formulation.
  target_ids:
  - CultureMech:009454
- check_id: upstream-primary-formulation
  name: Primary formulation and product provenance beyond TOGO M2919
  required: true
  status: unavailable
  summary: The fully inspected exact provider response has empty src_url and no original_media_id.
    Original primary formulation/product identity remains unavailable; the exact TOGO
    identity and one-liter component row are independently resolved.
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - record
  - owner-0
  - togo-source
  - togo-shell
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:11:42Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:11:42Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:09:41.404310Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch010/091/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:09:51.044824Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch010/091/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:09:58.374639Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:09:59.672999Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T08:11:42Z'
  support: supports
  summary: './data/merge_yaml/merged/2x_yeast_extract_tryptone_2xyt.yaml:1:id: CultureMech:009454

    ./data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml:1:id: CultureMech:009454

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: togo-source
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2919
  locator: $.meta; $.components[0].items[0]; $.comments
  accessed_at: '2026-10-21T08:00:46.677580Z'
  support: supports
  summary: Exact provider identity M2919 and original title match both records. One
    named complex/undefined component is quantified as a volume; no internal solutes,
    original accession, or upstream source URL are supplied.
  snapshot_sha256: 8673138712ded5db403b94f777812b9498feb2a61d6b068e64e8ab54d0b4cf37
- evidence_id: source-volume
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2919
  locator: $.components[0].items[0].volume and unit; component_name supplies the row
    identity
  accessed_at: '2026-10-21T08:00:46.677580Z'
  support: supports
  summary: The only formulation row states one liter of the named opaque 2xYT medium.
    This is a volume-only amount, not a mass concentration or an explicitly normalized
    component addition per final liter.
  quote: "\"volume\": 1,\n          \"unit\": \"L\""
  snapshot_sha256: 8673138712ded5db403b94f777812b9498feb2a61d6b068e64e8ab54d0b4cf37
- evidence_id: source-comment
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2919
  locator: $.comments[0].comment, paragraph_index 1; component row is separately paragraph_index
    3
  accessed_at: '2026-10-21T08:00:46.677580Z'
  support: supports
  summary: The separate comment says a single colony seeds a 20 mL overnight culture
    in 2xYT. It does not say that a 20 mL culture is transferred into the separately
    listed liter. The strain token remains source context; no taxonomic or growth
    assertion is added.
  quote: A single colony of CB9615 was used to seed a 20 mL overnight culture
  snapshot_sha256: 8673138712ded5db403b94f777812b9498feb2a61d6b068e64e8ab54d0b4cf37
- evidence_id: togo-shell
  kind: database
  reference: https://togomedium.org/medium/M2919
  locator: Complete HTML and extracted page text
  accessed_at: '2026-10-21T08:00:46.677079Z'
  support: supports
  summary: The canonical medium URL resolves to an application shell. Its captured
    HTML supplies no independently inspectable formulation text; the exact API supports
    the comparison.
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T08:11:42Z'
  support: supports
  summary: '{}'
- evidence_id: mim-scope
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Pinned MIM source metadata and complete direct ingredient descriptors
  accessed_at: '2026-10-21T08:11:42Z'
  support: supports
  summary: Pinned MIM commit 6643131b0f12ab40b66f98135245fca04027e0e9, index SHA256
    4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5, 9077 rows. Neither
    record asserts a primary chemical term or secondary MIM link for its one opaque
    medium component. Primary and secondary ingredient-instance linkage are each 0/1
    (0%) in each layer on a 0–100 scale; this does not establish an erroneous ingredient
    identity or justify a guessed pure-chemical mapping.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: importer-current-context
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item lines273–339; ordinary primary-item path lines609–640;
    _parse_unit lines713–746
  accessed_at: '2026-10-21T08:11:42Z'
  support: context_only
  summary: The inspected current ordinary-item path reads the provider amount/unit
    and explicitly maps l to the volume-only L enum. It does not support attributing
    the stored historical 1 G_PER_L to an unchanged current L conversion bug, nor
    does this static read prove the historical repair execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: converter-current-context
  kind: record_content
  reference: src/culturemech/convert/togo_raw_yaml.py
  locator: Complete 55-line mechanical-conversion entrypoint
  accessed_at: '2026-10-21T08:11:42Z'
  support: context_only
  summary: The raw-YAML converter declares a direct JSON-to-YAML conversion without
    normalization and delegates to JSONToRawYAMLConverter. It is not the maintained
    scientific correction owner and was not executed.
  snapshot_sha256: ce5e73545c9ecde54724259d2fd475676c0f3cb44dcfd283950e89fd49c10993
- evidence_id: historical-repair-search
  kind: search
  reference: repository checkout
  locator: Exact basename repair_togo_mrs_2xyt_score40.py over ignored-inclusive file
    inventory
  accessed_at: '2026-10-21T08:11:42Z'
  support: unknown
  summary: No current file with the historical repair basename was found. The owner
    event is retained as historical provenance, not treated as an inspected repair
    implementation or scientific validation.
  search_scope: Whole current batch010 checkout with rg --files --no-ignore --hidden,
    exact basename comparison. No all-history or other-checkout absence claim.
- evidence_id: owner-difference
  kind: record_content
  reference: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
  locator: All differing top-level nodes; source hashes pinned in source.inputs
  accessed_at: '2026-10-21T08:11:42Z'
  support: supports
  summary: '{"curation_history": {"generated": [{"timestamp": "2026-01-27T06:35:57.404404Z",
    "curator": "togo-import", "action": "Imported from TOGO Medium", "notes": "Source:
    TOGO, ID: M2919"}, {"timestamp": "2026-03-13T06:20:06.244709Z", "curator": "culturemech-id-assigner-v1.0",
    "action": "Assigned CultureMech ID", "notes": "Assigned stable identifier: CultureMech:009454"},
    {"timestamp": "2026-03-17T19:46:25.216600+00:00", "curator": "normalize_media_names_to_snake_case.py",
    "action": "NAME_NORMALIZED", "notes": "Normalized name from \"2x Yeast Extract
    Tryptone (2xYT)\" to \"2x_yeast_extract_tryptone_2xyt\" for consistent matching"},
    {"timestamp": "2026-08-06T03:04:34.069611+00:00", "curator": "merge_recipes.py",
    "action": "MERGED_RECIPES", "notes": "merged 1 source recipe(s) on fingerprint
    69b8ae2d5ae1aa7966693ad313b2e2d767b26c1fc95c1f52c6f1abe5cf9c9a9e", "source": "2x_yeast_extract_tryptone_2xyt.yaml"}],
    "owner": [{"timestamp": "2026-01-27T06:35:57.404404Z", "curator": "togo-import",
    "action": "Imported from TOGO Medium", "notes": "Source: TOGO, ID: M2919"}, {"timestamp":
    "2026-03-13T06:20:06.244709Z", "curator": "culturemech-id-assigner-v1.0", "action":
    "Assigned CultureMech ID", "notes": "Assigned stable identifier: CultureMech:009454"},
    {"timestamp": "2026-03-17T19:46:25.216600+00:00", "curator": "normalize_media_names_to_snake_case.py",
    "action": "NAME_NORMALIZED", "notes": "Normalized name from \"2x Yeast Extract
    Tryptone (2xYT)\" to \"2x_yeast_extract_tryptone_2xyt\" for consistent matching"},
    {"timestamp": "2026-09-08T00:00:00-07:00", "curator": "repair_togo_mrs_2xyt_score40.py",
    "action": "RESOLVED_TOGO_MRS_2XYT_SCORE40", "changes": "Resolved score-40 TOGO
    MRS/2xYT one-liter product row", "source": "https://togomedium.org/medium/M2919",
    "notes": "TOGO M2919 records a 20 mL overnight culture seeded in one liter of
    2x Yeast Extract Tryptone (2xYT); the source does not disclose the product''s
    internal formulation."}]}, "data_quality_flags": {"generated": null, "owner":
    ["ingredients_curated", "has_unmapped_ingredients"]}, "ingredients": {"generated":
    [{"preferred_term": "2x Yeast Extract Tryptone (2xYT)", "concentration": {"value":
    "1", "unit": "G_PER_L"}, "notes": "Properties: Undefined component, Complex component"}],
    "owner": [{"preferred_term": "2x Yeast Extract Tryptone (2xYT)", "concentration":
    {"value": "1000", "unit": "ML_PER_L"}, "source": "TOGO M2919", "notes": "TOGO
    M2919 records one liter of 2x Yeast Extract Tryptone (2xYT) as an opaque product."}]},
    "merge_fingerprint": {"generated": "69b8ae2d5ae1aa7966693ad313b2e2d767b26c1fc95c1f52c6f1abe5cf9c9a9e",
    "owner": null}, "merged_from": {"generated": ["2x_yeast_extract_tryptone_2xyt"],
    "owner": null}, "notes": {"generated": "Source: https://togomedium.org/medium/M2919",
    "owner": "TOGO M2919 records a 20 mL overnight culture seeded in one liter of
    2x Yeast Extract Tryptone (2xYT); the source does not disclose the product''s
    internal formulation."}, "preparation_steps": {"generated": null, "owner": [{"step_number":
    1, "action": "MIX", "description": "Use one liter of 2x Yeast Extract Tryptone
    (2xYT)."}]}, "references": {"generated": null, "owner": [{"reference": "https://togomedium.org/medium/M2919"}]}}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '0 primary CHEBI identities resolve with matching labels; 0 of 0 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - record
  - mim
  details: 1 direct ingredient instances; CHEBI-primary instance linkage 0/1 (0.00%),
    verified secondary coverage 0/1 (0.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Stable ID, exact provider accession and owner
  outcome: supported
  summary: CultureMech:009454 resolves to one generated MediaRecipe and its normalized
    bacterial owner. Original title and TOGO:M2919 match the exact API. The merge
    source identifies that owner; no synonymous sibling, formula fingerprint, or generic
    2xYT name is used to substitute a different formulation.
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togo-source
- assessment_id: volume
  area: quantity
  topic: The sole component amount in both layers
  outcome: concern
  summary: Provider amount 1 L is a volume-only source statement. Generated 1 G_PER_L
    changes the physical dimension without support. Owner 1000 ML_PER_L is a volume-per-volume
    concentration; 1 L equals 1000 mL, but the added final-liter denominator is not
    supplied. Use the existing volume-only L representation for the source amount,
    with field evidence. No density, stock strength, or 20 mL-to-1 L ratio is available
    for another conversion.
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - record
  - owner-0
  - source-volume
  - source-comment
  - importer-current-context
  details: '{"field_path": "ingredients[0].concentration", "source": {"value": 1,
    "unit": "L"}, "generated": {"value": "1", "unit": "G_PER_L"}, "owner": {"value":
    "1000", "unit": "ML_PER_L"}, "concentration_decision": "correct", "proposed_owner":
    {"value": "1", "unit": "L"}, "basis": "source volume, not final-volume closure",
    "action_taken": "none"}'
- assessment_id: opaque-formulation
  area: representation
  topic: Opaque medium, chemical forms and stock boundaries
  outcome: unknown
  summary: The complete provider response has one opaque complex/undefined medium
    component and no internal ingredient amounts, supplier/catalog identity, nested
    stocks, solution references, or variants. Both local layers preserve the opaque
    name. No tryptone, yeast-extract, salt, water, hydrate, or stock quantity can
    be inferred from the 2xYT label. Its two-fold name is not an evidenced instruction
    to dilute or multiply this record.
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - record
  - owner-0
  - togo-source
  - mim-scope
- assessment_id: comment-scope
  area: scope
  topic: Separate provider comment versus later owner interpretation
  outcome: concern
  summary: The generated target has only the source URL in notes and makes no 20 mL
    transfer claim. The normalized owner notes and September repair-event notes instead
    say a 20 mL overnight culture is seeded in one liter. The provider says a single
    colony seeds the 20 mL culture; the one-liter ingredient is a separately listed
    row. These cannot be combined into an asserted transfer or inoculum fraction.
    CB9615 is retained only as an unresolved source token.
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - record
  - owner-0
  - source-comment
  - source-volume
  - owner-difference
- assessment_id: conditions-preparation
  area: completeness
  topic: Preparation and conditions
  outcome: unknown
  summary: The owner preparation text says to use one liter, which agrees with the
    component volume; its MIX action is a local representation rather than a quoted
    detailed procedure. The source does not give internal product preparation, pH,
    temperature, atmosphere, sterilization, storage, or a quantitative meaning for
    overnight. No time, organism taxonomy, growth outcome, or transfer procedure is
    added. The generated target has no preparation_steps.
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - record
  - owner-0
  - togo-source
  - source-comment
  - owner-difference
- assessment_id: classification-flags
  area: scope
  topic: Classification, applications and quality flags
  outcome: supported
  summary: COMPLEX/UNDEFINED agrees with the provider component properties; LIQUID
    is consistent with the liter-denominated medium row. Bacterial category and generic
    Microbial cultivation are catalog context, not demonstrated species-level growth.
    The owner has_unmapped_ingredients flag agrees with its ungrounded opaque row;
    ingredients_curated records curation status and does not prove the volume basis
    or comment interpretation correct.
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - record
  - owner-0
  - togo-source
  - mim-scope
- assessment_id: history-correspondence
  area: consistency
  topic: Later maintained repair versus stored generated record
  outcome: concern
  summary: 'Both files share their first three timezone-aware import/ID/name events.
    The target records an August 6 merge; the owner records a September 8 repair and
    now has different concentration, ingredient source/notes, root notes, preparation,
    quality flags, and a root reference. These current differences establish generated/owner
    drift. The later owner is not assumed fully correct: its denominator and transfer
    wording require review before regeneration. Historical events remain append-only.'
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - record
  - owner-0
  - owner-difference
  - historical-repair-search
- assessment_id: evidence-provenance
  area: provenance
  topic: Provider reference, claim evidence and unavailable upstream source
  outcome: concern
  summary: The target has a notes URL but no structured reference or claim evidence;
    its actual reference diagnostic checked zero excerpts. The owner adds one root
    TOGO reference and an ingredient source string, but no exact amount or comment
    evidence. The API supplies provider-level support while its original primary source
    and product identity remain unavailable. Completion is partial for that required
    provenance gap, not because the provider-to-record dimensional discrepancy is
    uncertain.
  target_ids:
  - CultureMech:009454
  evidence_ids:
  - record
  - owner-0
  - togo-source
  - togo-shell
  - source-volume
  - source-comment
  - validate-references
findings:
- finding_id: f1
  issue_key: CM009454-opaque-product-volume-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: The one-liter opaque component is represented with unsupported concentration
    units
  description: The generated ingredients[0].concentration asserts 1 G_PER_L, while
    TOGO explicitly supplies volume 1 L. The maintained owner changes this to 1000
    ML_PER_L, which preserves a volume numerator but adds a final-liter denominator
    absent from the response. The exact source amount can be represented as 1 L without
    density, final-volume, stock-dilution, or culture-transfer assumptions. Current
    importer code already maps l to L.
  target_ids:
  - CultureMech:009454
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - source-volume
  - source-comment
  - importer-current-context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM009454-owner-culture-comment-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: The normalized owner joins two source statements into an unsupported culture-transfer
    narrative
  description: 'This is an owner-specific error: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    notes and curation_history[3].notes describe a 20 mL overnight culture seeded
    in one liter. The source instead says a single colony of CB9615 seeds a 20 mL
    culture and separately lists one liter of the medium. The generated target notes
    contain only the source URL and do not make the transfer claim.'
  target_ids:
  - CultureMech:009454
  field_paths:
  - notes
  - curation_history
  evidence_ids:
  - owner-0
  - record
  - source-comment
  - source-volume
  - owner-difference
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM009454-generated-owner-provenance-drift
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: The generated record predates the maintained owner repair and omits its provenance
    fields
  description: The August merged target omits the September owner repair event and
    current owner ingredient source/notes, root reference, preparation_steps and data_quality_flags.
    Its quantity also differs, as assessed separately. The owner itself contains the
    unsupported denominator and transfer interpretation, so indiscriminately copying
    the later content would propagate defects.
  target_ids:
  - CultureMech:009454
  field_paths:
  - curation_history
  - ingredients[0].source
  - ingredients[0].notes
  - references
  - preparation_steps
  - data_quality_flags
  evidence_ids:
  - record
  - owner-0
  - owner-difference
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM009454-claim-evidence-upstream-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Provider statements lack claim-level evidence and original primary provenance
    is unavailable
  description: The owner has one root TOGO URL but no ingredient or root evidence
    tying the exact volume and separate culture comment to their source fields. The
    generated target lacks that root reference and its reference diagnostic examined
    zero excerpts. The full provider API identifies M2919 but contains empty src_url
    and no original_media_id; no original collection, publication or product formulation
    was established.
  target_ids:
  - CultureMech:009454
  field_paths:
  - references
  - evidence
  - ingredients[0].evidence
  - ingredients[0].source
  - notes
  evidence_ids:
  - record
  - owner-0
  - togo-source
  - togo-shell
  - source-volume
  - source-comment
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Correct the normalized owner to the source-faithful value 1 unit L,
    attach exact amount evidence, and retain the opaque component identity. Regenerate
    the target only after all owner corrections and verify the volume-only unit survives.
    Do not expand an assumed standard recipe or infer any dilution from the 2x name
    or culture comment.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009454
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a2
  description: Correct the editable normalized-owner notes to keep the one-liter formulation
    row separate from the source culture comment. Preserve the existing repair event
    verbatim and append a new evidence-backed clarification event; do not rewrite
    historical notes. Do not add a transfer, inoculum percentage, taxonomy, time/temperature,
    or growth assertion. Review owner content before propagating it through regeneration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009454
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
  - Verify the future owner notes distinguish the single-colony-to-20 mL statement
    from the separate one-liter component and leave their relationship unresolved.
- action_id: a3
  description: After correcting and evidencing the maintained owner, regenerate through
    the declared merge entrypoint and confirm that its verified source trace, preparation
    context, flags and append-only history survive. Do not hand-edit the generated
    YAML or treat the later timestamp as proof of scientific correctness.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009454
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a4
  description: Retain the existing owner reference and add narrowly scoped amount/comment
    evidence with exact snippets, provider API locator, original unit, actual capture
    date/hash and upstream limitations. Recover an exact original source if possible;
    if unavailable, preserve that limit. Keep the product opaque and avoid guessed
    ingredient identities, formula amounts or growth claims.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009454
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2x_yeast_extract_tryptone_2xyt.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
limitations:
- The exact TOGO API identifies M2919, but src_url is empty and original_media_id
  is absent. No original publication, collection accession, manufacturer, catalog
  product, or exact internal formulation is established. Required upstream primary-source
  corroboration remains unavailable.
- The canonical TOGO page is an HTTP 200 application shell. The scientific comparison
  uses the captured exact provider API, with its actual access time and byte hash.
- The source lists a one-liter opaque medium component and separately comments on
  a 20 mL overnight culture seeded by a single colony of CB9615. No transfer between
  those volumes, dilution ratio, final-volume closure, strain taxonomy, measured growth,
  or organism-specific recommendation is inferred.
- No generic 2xYT recipe, commercial product formulation, nearby medium record, or
  standard practice is substituted for the undisclosed source component. Provider
  GMO properties are reported as source annotations, not independently validated ontology
  assertions or ingredient groundings.
- The current TOGO importer and mechanical converter were read statically. Current
  code already preserves the L unit; neither the historical import nor the later repair
  event was replayed. The named historical repair script was not found in an ignored-inclusive
  current-checkout file search; that bounded absence does not establish that it never
  existed.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-010
- generated-medium
```
