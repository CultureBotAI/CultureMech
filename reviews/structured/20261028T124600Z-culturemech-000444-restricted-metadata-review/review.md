# Metadata-only review: CRYPTOANAEROBACTER MEDIUM

- Review: 20261028T124600Z-culturemech-000444-restricted-metadata-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T12:36:30.939636Z
- Finished UTC: 2026-10-28T12:46:00.624265Z
- Reviewer: Codex batch006_validation (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Partial metadata-only review of the exact target and maintained owner. Identity and original structural checks are documented; prior source-review claims remain historically bounded. The exact DSM754 supplement association triggers exclusion of formulation, quantities, stocks, preparation and growth-condition assessment. No recipe content or operational recommendation is changed.

## Scope And Provenance

Restricted identity, bibliography/catalogue provenance and schema only; operational content explicitly excluded.

Selection: Authoritative batch067 record03
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000444 | data/merge_yaml/merged/CRYPTOANAEROBACTER_MEDIUM.yaml | generated | cryptoanaerobacter_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:000444 | Actual exit0; structural diagnostics only. |
| Canonical strict | passed | True | CultureMech:000444 | Actual exit0; structural diagnostics only. |
| Canonical terms | passed | True | CultureMech:000444 | Actual exit0; structural diagnostics only. |
| Canonical references | passed | True | CultureMech:000444 | Actual exit0; structural diagnostics only. |

## Scientific And Domain Assessments

### Record and maintained-owner identity

identity: supported. Targets: CultureMech:000444.

The exact target and sole maintained owner share CultureMech:000444, the original record name and MediaDive medium accession1022. The DSM754 supplement reference establishes a restricted source context; no organism-growth claim, recipe equivalence or species rename is inferred.

### Explicit restricted review boundary

scope: supported. Targets: CultureMech:000444.

Review is limited to identity, catalogue cross-references, provenance and schema. All operational formulation, stock, quantity, preparation and growth-condition content remains unchanged and not assessed.

### Original structural diagnostics

schema: supported. Targets: CultureMech:000444.

All four documented canonical commands ran once and exited0; strict reports zero errors and references reports zero checks. These results do not establish scientific adequacy, source authenticity or safety of use.

### Operational quantities excluded

quantity: not_applicable. Targets: CultureMech:000444.

All 62 existing concentration fields are inventoried privately and unchanged/not_assessed. No numeric detail, correction, dilution or source recipe is supplied in this review.

### Chemical grounding excluded

grounding: not_applicable. Targets: CultureMech:000444.

Existing identifier/label slots and packaged snapshot memberships are preserved structurally. Current labels, supplied chemical forms and recipe-stage identities are not scientifically endorsed or corrected.

### Historical claims remain bounded

provenance: concern. Targets: CultureMech:000444.

The selected October reports contain prior source/check assertions, including an unchanged guarded-review event. Their headers and record/hash lineage are identifiable, but historical operational source contents and retrieval events are not independently reauthenticated here. Existing original events are retained; present writer behavior does not prove past execution.

## Findings

### f1: Historical source-review assertions need an explicit scope boundary

minor / open / confirmed; issue key: culturemech-000444-historical-source-scope.

Historical report and curation assertions should remain identified as prior observations, with their original source dates and hashes. This restricted review does not reauthenticate operational source claims or promote the record to scientifically verified. Add metadata-only provenance context by a new event if needed; retain all original events and recipe fields unchanged.

## Recommended Actions And Acceptance Checks

### a1

Retain existing history byte-for-byte and, if needed, append only a metadata event that distinguishes prior report claims from this restricted observation. Do not change recipe content, infer species growth, repair stock/formulation fields or regenerate operational recommendations.

- Original events and all operational fields remain unchanged.
- Any added provenance contains verified original source identity, dates and hashes, with historical claims explicitly labeled as historical.
- The record is not promoted to scientific validation by this metadata review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/merge_yaml/merged/CRYPTOANAEROBACTER_MEDIUM.yaml; Complete scoped metadata | context_only | Exact selected document bytes inspected; metadata assessed, operational contents preserved privately without scientific assessment. |
| owner | data/normalized_yaml/bacterial/cryptoanaerobacter_medium.yaml; Complete scoped metadata | context_only | Exact selected document bytes inspected; metadata assessed, operational contents preserved privately without scientific assessment. |
| dsm754-identity | https://www.dsmz.de/collection/catalogue/details/culture/DSM-754; Catalogue identity heading, collection cross-references, risk-group metadata and BacDive link label only; retained raw/identity-text metadata REVIEW_WORK/batch067/validation-source-supplement/dsm754Identity.json | context_only | Current catalogue heading remains Clostridium sp. for DSM754; its cross-reference link names Paeniclostridium sordellii. These catalogue observations establish the restricted source context, not a species correction or growth claim for the reviewed medium. |
| quantities | REVIEW_WORK/batch067/record03/quantity-inventory.json; Complete scoped metadata | context_only | Private unchanged/not_assessed concentration inventory; values intentionally excluded from public details. |
| census | REVIEW_WORK/batch067/record03/field-census.json; Complete scoped metadata | context_only | Private exact existing scalar inventory; no operational assessment. |
| grounding | REVIEW_WORK/batch067/record03/grounding-inventory.json; Complete scoped metadata | context_only | Existing identifier slots/current MIM memberships only, without chemical validation. |
| history | REVIEW_WORK/batch067/record03/history-inventory.json; Complete scoped metadata | context_only | Complete existing history objects, preserved without retrospective validation. |
| reports | REVIEW_WORK/batch067/record03/historical-reading-metadata-only.json; Complete scoped metadata | context_only | Exact selected historical report headers and archive boundary only; no historical formulation claims adopted. |
| reader | REVIEW_WORK/batch067/record03/complete-document-reader.json; Complete scoped metadata | context_only | Exact identity metadata and original document hashes. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact observed ID rows | context_only | Current packaged rows only; this snapshot cannot establish past identity validity. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Full metadata | context_only | Current packaged version/checksum only. |
| writer-merge | src/culturemech/merge/merger.py; RecipeMerger.merge_group singleton branch | context_only | Current singleton merge copies the owner and adds lineage; present code does not prove the historical merge execution. No regeneration is recommended in this restricted review. |
| writer-enrich | scripts/enrich_with_chebi.py; RecipeEnricher.enrich_ingredient and enrich_file | context_only | Current enrichment skips existing term IDs and appends a history event when writing changes. This is provenance context only, not a chemical endorsement or execution claim. |
| check-schema | REVIEW_WORK/batch067/record03/validate-schema.json | supports | Actual original once-only canonical schema exit0; full argv/time/stdout/stderr retained. Zero reference checks do not authenticate biological or formulation claims. |
| check-strict | REVIEW_WORK/batch067/record03/validate-strict.json | supports | Actual original once-only canonical strict exit0; full argv/time/stdout/stderr retained. Zero reference checks do not authenticate biological or formulation claims. |
| check-terms | REVIEW_WORK/batch067/record03/validate-terms.json | supports | Actual original once-only canonical terms exit0; full argv/time/stdout/stderr retained. Zero reference checks do not authenticate biological or formulation claims. |
| check-references | REVIEW_WORK/batch067/record03/validate-references.json | supports | Actual original once-only canonical references exit0; full argv/time/stdout/stderr retained. Zero reference checks do not authenticate biological or formulation claims. |

## Limits And Additional Notes

- scientific_review is false: this review provides no cultivation, formulation, stock, dose, incubation, optimization or supplement-production correction.
- Current DSM754 heading and linked taxonomic label differ; both are retained as catalogue observations, without asserting that the medium itself targets a particular species.
- No primary recipe PDF, medium API formulation or operational paper section was fetched or extracted after the restricted context was identified.
- Full historical operational tables and source recipe claims were not assessed. Prior report headers and exact local hashes are retained as provenance, not fresh scientific validation.
- All current quantity and numeric preparation fields remain unchanged/not_assessed in private inventories; none is reproduced as public recipe guidance.
- Current MIM membership is a structural observation only; no new operational ontology validation or supplied-form correction was performed.
- The four canonical diagnostics are actual structural results; references checked zero citations and do not authenticate source claims.
- No formal review save, source/recipe edits, Git or STATE mutation, or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T124600Z-culturemech-000444-restricted-metadata-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Metadata-only review: CRYPTOANAEROBACTER MEDIUM'
started_at: '2026-10-28T12:36:30.939636Z'
finished_at: '2026-10-28T12:46:00.624265Z'
reviewer:
  identity: Codex batch006_validation
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Independent read-only metadata assessment; original target/owner
    and source identity metadata examined without operational corrections.
skill: review-yaml-record
completion: partial
verdict: pass_with_limitations
scientific_review: false
summary: Partial metadata-only review of the exact target and maintained owner. Identity
  and original structural checks are documented; prior source-review claims remain
  historically bounded. The exact DSM754 supplement association triggers exclusion
  of formulation, quantities, stocks, preparation and growth-condition assessment.
  No recipe content or operational recommendation is changed.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/SKILL.md
    sha256: a67993ef11cf374ac579c53252bc603f9894ebd69cad711b11f293714c76621e
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
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CRYPTOANAEROBACTER_MEDIUM.yaml
    sha256: f6400643a960312ceae4f477022f53c97c8a49e4d3434d46850b378cd9f5f0bd
    role: target
  - path: data/normalized_yaml/bacterial/cryptoanaerobacter_medium.yaml
    sha256: 28a738f4769a29cd05b54ad467779bfcdd3f11fe8c4c967824eab4de67232e12
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
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
    sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
    sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/cryptoanaerobacter_medium.yaml.md
    sha256: 33e30d9c861af970d9d77d5bbdb3aea52272befffe181ddf9c2f1994bd7c7c51
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CRYPTOANAEROBACTER_MEDIUM.md
    sha256: 9ffe2dff27fcfd19e8430d53dbc150f0e2232cb5c41e300ddf34aa9ae789f705
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cryptoanaerobacter_medium.md
    sha256: 119c93f73040817026085b41516b43badf3687dceaaf5345b0b4f315886d3760
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/validate_media_variant_links.py
    sha256: d18ef71320a0c50abe085e151d0d0d4d963007d1e1c9afbefab97581a983e31e
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: 6116d95493b8f91faed19956301291a73d090a3b83671303650a561798933456
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/ingredients/mim_label_index.py
    sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
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
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Restricted identity, bibliography/catalogue provenance and schema only;
    operational content explicitly excluded.
  selection: Authoritative batch067 record03
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000444
targets:
- target_id: CultureMech:000444
  path: data/merge_yaml/merged/CRYPTOANAEROBACTER_MEDIUM.yaml
  label: cryptoanaerobacter_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cryptoanaerobacter_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  target_ids:
  - CultureMech:000444
  command: just validate-schema data/merge_yaml/merged/CRYPTOANAEROBACTER_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
  summary: Actual exit0; structural diagnostics only.
- check_id: strict
  name: Canonical strict
  status: passed
  required: true
  target_ids:
  - CultureMech:000444
  command: just validate-strict data/merge_yaml/merged/CRYPTOANAEROBACTER_MEDIUM.yaml
    --out REVIEW_WORK/batch067/record03/strict.tsv --workers 1 --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
  summary: Actual exit0; structural diagnostics only.
- check_id: terms
  name: Canonical terms
  status: passed
  required: true
  target_ids:
  - CultureMech:000444
  command: just validate-terms data/merge_yaml/merged/CRYPTOANAEROBACTER_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-terms
  summary: Actual exit0; structural diagnostics only.
- check_id: references
  name: Canonical references
  status: passed
  required: true
  target_ids:
  - CultureMech:000444
  command: just validate-references data/merge_yaml/merged/CRYPTOANAEROBACTER_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
  summary: Actual exit0; structural diagnostics only.
evidence:
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CRYPTOANAEROBACTER_MEDIUM.yaml
  locator: Complete scoped metadata
  accessed_at: '2026-10-28T12:46:00.562047Z'
  support: context_only
  summary: Exact selected document bytes inspected; metadata assessed, operational
    contents preserved privately without scientific assessment.
  snapshot_sha256: f6400643a960312ceae4f477022f53c97c8a49e4d3434d46850b378cd9f5f0bd
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/cryptoanaerobacter_medium.yaml
  locator: Complete scoped metadata
  accessed_at: '2026-10-28T12:46:00.562266Z'
  support: context_only
  summary: Exact selected document bytes inspected; metadata assessed, operational
    contents preserved privately without scientific assessment.
  snapshot_sha256: 28a738f4769a29cd05b54ad467779bfcdd3f11fe8c4c967824eab4de67232e12
- evidence_id: dsm754-identity
  kind: database
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-754
  locator: Catalogue identity heading, collection cross-references, risk-group metadata
    and BacDive link label only; retained raw/identity-text metadata REVIEW_WORK/batch067/validation-source-supplement/dsm754Identity.json
  accessed_at: '2026-10-28T12:40:44.604754Z'
  support: context_only
  summary: Current catalogue heading remains Clostridium sp. for DSM754; its cross-reference
    link names Paeniclostridium sordellii. These catalogue observations establish
    the restricted source context, not a species correction or growth claim for the
    reviewed medium.
  snapshot_sha256: 02c87425ca5e4b06f57eae29c585481d82a95e4ca9a8b3b5269f489a1a7f8b99
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch067/record03/quantity-inventory.json
  locator: Complete scoped metadata
  accessed_at: '2026-10-28T12:46:00.621995Z'
  support: context_only
  summary: Private unchanged/not_assessed concentration inventory; values intentionally
    excluded from public details.
  snapshot_sha256: 207f37fb215b905140c10c02f9b3169c16281ace092dfdb88f918af7f88a3e3b
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch067/record03/field-census.json
  locator: Complete scoped metadata
  accessed_at: '2026-10-28T12:46:00.622063Z'
  support: context_only
  summary: Private exact existing scalar inventory; no operational assessment.
  snapshot_sha256: 966c3b87323afc355be9a2dc3badaabdfc4e78f6ddeb0de9612a5a050f04acf8
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch067/record03/grounding-inventory.json
  locator: Complete scoped metadata
  accessed_at: '2026-10-28T12:46:00.622188Z'
  support: context_only
  summary: Existing identifier slots/current MIM memberships only, without chemical
    validation.
  snapshot_sha256: 0f6c0c03c31368e5494a7ef36b917290af6c4e2045dfffc799e86acd26b265b8
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch067/record03/history-inventory.json
  locator: Complete scoped metadata
  accessed_at: '2026-10-28T12:46:00.622391Z'
  support: context_only
  summary: Complete existing history objects, preserved without retrospective validation.
  snapshot_sha256: fcd8d89c57308b67baea1c036cb6aefffcf96e77d40eb236f49c8d574f3728a6
- evidence_id: reports
  kind: record_content
  reference: REVIEW_WORK/batch067/record03/historical-reading-metadata-only.json
  locator: Complete scoped metadata
  accessed_at: '2026-10-28T12:46:00.622428Z'
  support: context_only
  summary: Exact selected historical report headers and archive boundary only; no
    historical formulation claims adopted.
  snapshot_sha256: de5340e4c31d30fd1fa30989b023ef3ed4b709d9e78d9bc171253d0ed51b62da
- evidence_id: reader
  kind: record_content
  reference: REVIEW_WORK/batch067/record03/complete-document-reader.json
  locator: Complete scoped metadata
  accessed_at: '2026-10-28T12:46:00.622461Z'
  support: context_only
  summary: Exact identity metadata and original document hashes.
  snapshot_sha256: fa1d5ae25e66c85a69198541d639910d20a00b051965eb373cfc71f964c13ede
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact observed ID rows
  accessed_at: '2026-10-28T12:46:00.622492Z'
  support: context_only
  summary: Current packaged rows only; this snapshot cannot establish past identity
    validity.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Full metadata
  accessed_at: '2026-10-28T12:46:00.623065Z'
  support: context_only
  summary: Current packaged version/checksum only.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group singleton branch
  accessed_at: '2026-10-28T12:46:00.623101Z'
  support: context_only
  summary: Current singleton merge copies the owner and adds lineage; present code
    does not prove the historical merge execution. No regeneration is recommended
    in this restricted review.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-enrich
  kind: record_content
  reference: scripts/enrich_with_chebi.py
  locator: RecipeEnricher.enrich_ingredient and enrich_file
  accessed_at: '2026-10-28T12:46:00.623140Z'
  support: context_only
  summary: Current enrichment skips existing term IDs and appends a history event
    when writing changes. This is provenance context only, not a chemical endorsement
    or execution claim.
  snapshot_sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch067/record03/validate-schema.json
  accessed_at: '2026-10-28T12:36:31.965015Z'
  support: supports
  summary: Actual original once-only canonical schema exit0; full argv/time/stdout/stderr
    retained. Zero reference checks do not authenticate biological or formulation
    claims.
  snapshot_sha256: 6430b18f7f3a5913b545981a859ca50c7a5a7bcdbaf7573e5f4d5ae0e33e3a59
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch067/record03/validate-strict.json
  accessed_at: '2026-10-28T12:36:32.881036Z'
  support: supports
  summary: Actual original once-only canonical strict exit0; full argv/time/stdout/stderr
    retained. Zero reference checks do not authenticate biological or formulation
    claims.
  snapshot_sha256: e51e1dda90f558cc0196dfa191fff11758fbb2000a72c082ccb3bd29c37b80e3
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch067/record03/validate-terms.json
  accessed_at: '2026-10-28T12:36:33.920071Z'
  support: supports
  summary: Actual original once-only canonical terms exit0; full argv/time/stdout/stderr
    retained. Zero reference checks do not authenticate biological or formulation
    claims.
  snapshot_sha256: 6bfdc4720b7d837ada6d4c3c4ed9dc5adffa753f7db1171e9cb751b8d1796eb1
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch067/record03/validate-references.json
  accessed_at: '2026-10-28T12:36:34.640726Z'
  support: supports
  summary: Actual original once-only canonical references exit0; full argv/time/stdout/stderr
    retained. Zero reference checks do not authenticate biological or formulation
    claims.
  snapshot_sha256: 37b63909bf619cfea397d22e7588a5c8a70416b7014700ef8c6e11a39d70ddc3
assessments:
- assessment_id: identity
  area: identity
  outcome: supported
  topic: Record and maintained-owner identity
  summary: The exact target and sole maintained owner share CultureMech:000444, the
    original record name and MediaDive medium accession1022. The DSM754 supplement
    reference establishes a restricted source context; no organism-growth claim, recipe
    equivalence or species rename is inferred.
  target_ids:
  - CultureMech:000444
  evidence_ids:
  - target
  - owner
  - reader
  - dsm754-identity
- assessment_id: scope
  area: scope
  outcome: supported
  topic: Explicit restricted review boundary
  summary: Review is limited to identity, catalogue cross-references, provenance and
    schema. All operational formulation, stock, quantity, preparation and growth-condition
    content remains unchanged and not assessed.
  target_ids:
  - CultureMech:000444
  evidence_ids:
  - target
  - owner
  - dsm754-identity
  - quantities
- assessment_id: schema
  area: schema
  outcome: supported
  topic: Original structural diagnostics
  summary: All four documented canonical commands ran once and exited0; strict reports
    zero errors and references reports zero checks. These results do not establish
    scientific adequacy, source authenticity or safety of use.
  target_ids:
  - CultureMech:000444
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  outcome: not_applicable
  topic: Operational quantities excluded
  summary: All 62 existing concentration fields are inventoried privately and unchanged/not_assessed.
    No numeric detail, correction, dilution or source recipe is supplied in this review.
  target_ids:
  - CultureMech:000444
  evidence_ids:
  - quantities
  - census
- assessment_id: grounding
  area: grounding
  outcome: not_applicable
  topic: Chemical grounding excluded
  summary: Existing identifier/label slots and packaged snapshot memberships are preserved
    structurally. Current labels, supplied chemical forms and recipe-stage identities
    are not scientifically endorsed or corrected.
  target_ids:
  - CultureMech:000444
  evidence_ids:
  - grounding
  - mim
  - mim-meta
- assessment_id: provenance
  area: provenance
  outcome: concern
  topic: Historical claims remain bounded
  summary: The selected October reports contain prior source/check assertions, including
    an unchanged guarded-review event. Their headers and record/hash lineage are identifiable,
    but historical operational source contents and retrieval events are not independently
    reauthenticated here. Existing original events are retained; present writer behavior
    does not prove past execution.
  target_ids:
  - CultureMech:000444
  evidence_ids:
  - reports
  - history
  - writer-merge
  - writer-enrich
findings:
- finding_id: f1
  issue_key: culturemech-000444-historical-source-scope
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical source-review assertions need an explicit scope boundary
  description: Historical report and curation assertions should remain identified
    as prior observations, with their original source dates and hashes. This restricted
    review does not reauthenticate operational source claims or promote the record
    to scientifically verified. Add metadata-only provenance context by a new event
    if needed; retain all original events and recipe fields unchanged.
  target_ids:
  - CultureMech:000444
  field_paths:
  - curation_history
  - media_term
  - evidence
  evidence_ids:
  - reports
  - history
  - reader
  rule_id: review-yaml-record/historical-provenance-scope
  native_severity: P3
  normalization_reason: Custom metadata provenance rule, minor P3; no formulation
    error or blocking schema failure is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cryptoanaerobacter_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: Retain existing history byte-for-byte and, if needed, append only a
    metadata event that distinguishes prior report claims from this restricted observation.
    Do not change recipe content, infer species growth, repair stock/formulation fields
    or regenerate operational recommendations.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000444
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cryptoanaerobacter_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Original events and all operational fields remain unchanged.
  - Any added provenance contains verified original source identity, dates and hashes,
    with historical claims explicitly labeled as historical.
  - The record is not promoted to scientific validation by this metadata review.
  generator: Metadata-only provenance follow-up; no operational regeneration proposed
limitations:
- 'scientific_review is false: this review provides no cultivation, formulation, stock,
  dose, incubation, optimization or supplement-production correction.'
- Current DSM754 heading and linked taxonomic label differ; both are retained as catalogue
  observations, without asserting that the medium itself targets a particular species.
- No primary recipe PDF, medium API formulation or operational paper section was fetched
  or extracted after the restricted context was identified.
- Full historical operational tables and source recipe claims were not assessed. Prior
  report headers and exact local hashes are retained as provenance, not fresh scientific
  validation.
- All current quantity and numeric preparation fields remain unchanged/not_assessed
  in private inventories; none is reproduced as public recipe guidance.
- Current MIM membership is a structural observation only; no new operational ontology
  validation or supplied-form correction was performed.
- The four canonical diagnostics are actual structural results; references checked
  zero citations and do not authenticate source claims.
- No formal review save, source/recipe edits, Git or STATE mutation, or publication
  was performed by this author.
```
