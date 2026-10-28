# Non-operational review: CMM

- Review: 20261028T110926Z-culturemech-007191-nonoperational-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T10:59:48.954849Z
- Finished UTC: 2026-10-28T11:09:26.028984Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Partial non-operational identity, bibliography, provenance and structural review. The generated CMM target omits its maintained owner’s explicit bibliographic-only update; no operational repair or source-to-formulation certification is proposed.

## Scope And Provenance

Non-operational identity/bibliography/provenance/schema only. Existing operational fields remain unassessed.

Selection: Authoritative batch064 selection index10
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007191 | data/merge_yaml/merged/CMM.yaml | generated | cmm |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:007191 | Actual exit0; no formal review validate/save run by this author. |
| Canonical strict | passed | True | CultureMech:007191 | Actual exit0; no formal review validate/save run by this author. |
| Canonical terms | passed | True | CultureMech:007191 | Actual exit0; no formal review validate/save run by this author. |
| Canonical references | passed | True | CultureMech:007191 | Actual exit0; no formal review validate/save run by this author. |

## Scientific And Domain Assessments

### Exact stable record and bibliographic identity

identity: supported. Targets: CultureMech:007191.

The selected CM007191 target and its single MEDIADB290 owner are resolved by exact identity/provenance. The named publication is bibliographically authenticated; its title-level organism mention does not establish exact formulation correspondence or a strain-growth assertion.

### Existing source update and historical scope

provenance: concern. Targets: CultureMech:007191.

The owner’s October14 bibliographic-only citation is credited, while the generated target is stale. Two October5 report headers describe incomplete source review and are not promoted into fresh science. Current importer/merger observations are not claims of historical execution; the owner’s original archived-paper/source-to-owner join was not recovered by this review.

### Restricted non-operational boundary

scope: not_applicable. Targets: CultureMech:007191.

The title explicitly concerns M. tuberculosis pathogenicity. This partial review is limited to bibliography, identity, provenance and schema. Formulation, culture conditions, experimental outcome, virulence and source operational content are excluded.

### Private unchanged structural census

quantity: not_applicable. Targets: CultureMech:007191.

50 existing concentration fields are inventoried privately and marked not_assessed. No operational values, calculations, source-derived amounts or corrections are reproduced or certified in the review.

### Identifier preservation without chemical assessment

grounding: unknown. Targets: CultureMech:007191.

Existing ontology and legacy MIM identifiers are preserved structurally with exact current packaged-row membership. No fresh ingredient ontology/form verification or replacement is performed for this restricted record. Current MIM matches, absences and native term success are not chemical validity or historical-ID certification.

### Original canonical diagnostics

schema: supported. Targets: CultureMech:007191.

All four canonical diagnostics passed once, with strict zero errors and references zero checks. Their complete original streams are retained; they do not certify the excluded scientific content.

## Findings

### f1: Generated target omits the maintained bibliographic-only update

major / open / confirmed; issue key: culturemech-007191-generated-bibliographic-staleness.

The maintained MEDIADB290 owner contains the October14 PMID10792526 citation and an explicit non-operational scope note. The generated target lacks that reference and its history event. Fresh PubMed and Crossref agree on James, Williams and Marsh, the 2000 article title and DOI. Preserve the historical Mazumdar2014 import note as database provenance, distinguishing it from the experiment-paper citation. No owner ingredient, quantity, preparation or chemical changes are assessed or authorized for propagation.

## Recommended Actions And Acceptance Checks

### a1

Reconcile only the existing bibliographic citation and its explicit non-operational boundary into generated metadata, preserving the original history and adding an actual new observation if needed. Use a narrowly reviewed metadata-only path; do not blanket-regenerate operational owner differences or certify recipe equivalence from a title/DOI match.

- Exact PMID/DOI/title/author/year and existing bibliography-only restrictions remain faithful to the metadata sources.
- All ingredients, quantities, stock stages, chemical IDs, preparation, growth and pathogenicity-related assertions remain unchanged and unassessed; no operational owner repair is transferred.
- Preserve history append-only, retain inspected provenance, and recheck only separately authorized metadata changes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/merge_yaml/merged/CMM.yaml; Complete exact file | context_only | Complete generated target read for identity and structural preservation; operational content excluded from assessment. |
| owner | data/normalized_yaml/bacterial/cmm.yaml; Complete exact file | context_only | Complete exact maintained MEDIADB290 contributor read; its bibliographic-only scope is credited and retained. |
| quantities | REVIEW_WORK/batch064/record10/quantity-inventory.json; Complete exact file | context_only | Private exact structural/provenance inventory; operational fields unchanged and unassessed. |
| scalars | REVIEW_WORK/batch064/record10/field-census.json; Complete exact file | context_only | Private exact structural/provenance inventory; operational fields unchanged and unassessed. |
| numeric | REVIEW_WORK/batch064/record10/numeric-field-census.json; Complete exact file | context_only | Private exact structural/provenance inventory; operational fields unchanged and unassessed. |
| groundings | REVIEW_WORK/batch064/record10/grounding-inventory.json; Complete exact file | context_only | Private exact structural/provenance inventory; operational fields unchanged and unassessed. |
| history | REVIEW_WORK/batch064/record10/history-inventory.json; Complete exact file | context_only | Private exact structural/provenance inventory; operational fields unchanged and unassessed. |
| old-reports | REVIEW_WORK/batch064/record10/historical-report-scope.json; Complete exact file | context_only | Private exact structural/provenance inventory; operational fields unchanged and unassessed. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Matching rows in private inventory | context_only | Exact current packaged ID-row membership only. No chemical correctness or source validation. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete metadata | context_only | Packaged snapshot checksum, commit and row count verified. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current singleton merge copies its maintained owner, so a blanket regeneration could transfer operational differences. This review authorizes metadata-only reconciliation and no such automatic transfer. |
| writer-formulation | src/culturemech/merge/formulation.py; Complete file | context_only | Current conservative scientific-field equality is a grouping condition, not proof that a recipe is valid. |
| writer-mediadb | src/culturemech/import/mediadb_importer.py; _create_notes, _create_curation_history | context_only | Current _create_curation_history uses the generic Mazumdar2014 database publication; _create_notes supplies database provenance. These are not experimental-paper identity authentication or historical execution proof. |
| pubmed10792526 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&amp;id=10792526&amp;retmode=json; Exact bibliographic title/authors/year/journal/DOI fields only; abstract and experimental content excluded | supports | Fresh bibliographic metadata only; no full paper, operational recipe, Methods, growth or pathogenicity result assessed. |
| crossref10792526 | https://api.crossref.org/works/10.1046%2Fj.1365-2672.2000.01020.x; Exact bibliographic title/authors/year/journal/DOI fields only; abstract and experimental content excluded | supports | Fresh bibliographic metadata only; no full paper, operational recipe, Methods, growth or pathogenicity result assessed. |
| bibliography | REVIEW_WORK/batch064/record10/bibliographic-identity.json; Complete exact file | context_only | Exact primary bibliographic metadata joins; not formulation or experimental authentication. |
| check-schema | REVIEW_WORK/batch064/record10/schema-result.json | supports | Once-only canonical diagnostic with actual argv, times and full streams. Reference count zero does not authenticate scientific claims. |
| check-strict | REVIEW_WORK/batch064/record10/strict-result.json | supports | Once-only canonical diagnostic with actual argv, times and full streams. Reference count zero does not authenticate scientific claims. |
| check-terms | REVIEW_WORK/batch064/record10/terms-result.json | supports | Once-only canonical diagnostic with actual argv, times and full streams. Reference count zero does not authenticate scientific claims. |
| check-references | REVIEW_WORK/batch064/record10/references-result.json | supports | Once-only canonical diagnostic with actual argv, times and full streams. Reference count zero does not authenticate scientific claims. |

## Limits And Additional Notes

- Explicitly partial non-operational review with scientific_review:false. All operational formulation, supplied forms, concentrations, stock stages, preparation, culture and experimental assertions remain unchanged and unassessed.
- Full selected target and maintained owner bytes/history were read for identity and scope. The two prior report headers and provenance metadata were read; their operational tables and recommendations were deliberately not assessed or adopted.
- Fresh PubMed ESummary and Crossref were used only for title/authors/year/journal/DOI correspondence. No full article, operational MediaDB recipe/export, Methods or ingredient-repair sources were requested for this record.
- The owner’s NCBITaxon1773 note is retained as an existing bibliographic note; no fresh taxonomy authority check, target_organisms assertion, strain identity or growth association is made. Bibliographic identity does not authenticate the original source-to-owner formulation join.
- The packaged MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9. Exact local membership/absence is not historical catalog validation, supplied-form correctness or permission to repair legacy operational IDs.
- No formal validate/save, source edits, Git mutation or publication was performed. Current diagnostics are structural only and the reference validator examined zero references.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T110926Z-culturemech-007191-nonoperational-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Non-operational review: CMM'
started_at: '2026-10-28T10:59:48.954849Z'
finished_at: '2026-10-28T11:09:26.028984Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Independent exact provenance/metadata review and original diagnostic
    reading; operational scientific claims deliberately excluded.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: Partial non-operational identity, bibliography, provenance and structural
  review. The generated CMM target omits its maintained owner’s explicit bibliographic-only
  update; no operational repair or source-to-formulation certification is proposed.
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
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CMM.yaml
    sha256: 9cfe9e29bb86307f104a732e2e9d43eb48b91a5a869ea357533e4f918c4fdb9f
    role: target
  - path: data/normalized_yaml/bacterial/cmm.yaml
    sha256: 0149bfe6689b5477986ad43ab5300000e9a7ada548dbd415a4d8954ba4c55a87
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CMM.md
    sha256: f161742169d7f9bc04029bb25629bd27304a0bfb2e005ee651530d1c4affc7b8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cmm.md
    sha256: c2fd3c3cbb375260a75061a381ebd0b57195705e17161088d4bf42d32ac2c350
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/assign_culturemech_ids.py
    sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/enrich_with_mediaingredientmech.py
    sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
    role: context
  - path: scripts/fix_mediadb_leading_compounds.py
    sha256: 2b3b6adfdb298b51b6d87a30151b4f530ac5cd1726fb3763ce7c9fe07cfec729
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
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_ccap_duplicate_compositions.py
    sha256: d6ce21d516f227305d30631f8b04af781946cb40bb87aa8fd0fc47aa5a8caa0c
    role: context
  - path: scripts/repair_ccap_instruction_rows.py
    sha256: eb1a4c8c46eb45dcdde6a5d2f0f6833792dd0802c45603eefa1b63a3ff96fca5
    role: context
  - path: scripts/repair_ccap_missing_compositions.py
    sha256: 84d1ae3d91568fbffc850e88080bdf96fbaad277c3aa61eb371c0da0fc5a2be7
    role: context
  - path: scripts/repair_ccap_sources_score10.py
    sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
    role: context
  - path: scripts/repair_mediadb_names.py
    sha256: 56ad322b70927ac6dff2de12c63d7bfc640d72a6c2521b55293a788ac3cca4c5
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/ccap_importer.py
    sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
    role: context
  - path: src/culturemech/import/mediadb_importer.py
    sha256: 5c2d98caf450ee8bb2f73f112e4edab7c3e0f2fa5f2aa7bd2a34e6fd2fdfd4d0
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
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
  description: Non-operational identity/bibliography/provenance/schema only. Existing
    operational fields remain unassessed.
  selection: Authoritative batch064 selection index10
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007191
targets:
- target_id: CultureMech:007191
  path: data/merge_yaml/merged/CMM.yaml
  label: cmm
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cmm.yaml
    role: maintained source
  ownership_note: Exact declared maintained contributors resolved against stable identity;
    stocks and other source variants remain scoped comparisons.
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit0; no formal review validate/save run by this author.
  target_ids:
  - CultureMech:007191
  command: just validate-schema data/merge_yaml/merged/CMM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
- check_id: strict
  name: Canonical strict
  status: passed
  required: true
  summary: Actual exit0; no formal review validate/save run by this author.
  target_ids:
  - CultureMech:007191
  command: just validate-strict data/merge_yaml/merged/CMM.yaml --out REVIEW_WORK/batch064/record10/strict.tsv
    --workers 1 --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
- check_id: terms
  name: Canonical terms
  status: passed
  required: true
  summary: Actual exit0; no formal review validate/save run by this author.
  target_ids:
  - CultureMech:007191
  command: just validate-terms data/merge_yaml/merged/CMM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-terms
- check_id: references
  name: Canonical references
  status: passed
  required: true
  summary: Actual exit0; no formal review validate/save run by this author.
  target_ids:
  - CultureMech:007191
  command: just validate-references data/merge_yaml/merged/CMM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CMM.yaml
  locator: Complete exact file
  accessed_at: '2026-10-28T11:09:26.026543Z'
  support: context_only
  summary: Complete generated target read for identity and structural preservation;
    operational content excluded from assessment.
  snapshot_sha256: 9cfe9e29bb86307f104a732e2e9d43eb48b91a5a869ea357533e4f918c4fdb9f
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/cmm.yaml
  locator: Complete exact file
  accessed_at: '2026-10-28T11:09:26.026720Z'
  support: context_only
  summary: Complete exact maintained MEDIADB290 contributor read; its bibliographic-only
    scope is credited and retained.
  snapshot_sha256: 0149bfe6689b5477986ad43ab5300000e9a7ada548dbd415a4d8954ba4c55a87
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch064/record10/quantity-inventory.json
  locator: Complete exact file
  accessed_at: '2026-10-28T11:09:26.026755Z'
  support: context_only
  summary: Private exact structural/provenance inventory; operational fields unchanged
    and unassessed.
  snapshot_sha256: 01e361500db9e8ed9b3b06bafb09e8f0304cb24cc8f381bd5f85a49dc0141fe5
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch064/record10/field-census.json
  locator: Complete exact file
  accessed_at: '2026-10-28T11:09:26.026789Z'
  support: context_only
  summary: Private exact structural/provenance inventory; operational fields unchanged
    and unassessed.
  snapshot_sha256: 6b463cbdc73b99985387c24536dedcb1ef9a06c43cebeaa22cc3a0c7d7b215af
- evidence_id: numeric
  kind: record_content
  reference: REVIEW_WORK/batch064/record10/numeric-field-census.json
  locator: Complete exact file
  accessed_at: '2026-10-28T11:09:26.026837Z'
  support: context_only
  summary: Private exact structural/provenance inventory; operational fields unchanged
    and unassessed.
  snapshot_sha256: 4fede0753586b1ad1b957b2c586bcdd1e3f9a098716722c6bdfcb1ef7b827ffe
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch064/record10/grounding-inventory.json
  locator: Complete exact file
  accessed_at: '2026-10-28T11:09:26.026871Z'
  support: context_only
  summary: Private exact structural/provenance inventory; operational fields unchanged
    and unassessed.
  snapshot_sha256: 5f472c60481bc6c571552052cc8c5604426a62f6e3b8a99b11ad1abbdc290bb0
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch064/record10/history-inventory.json
  locator: Complete exact file
  accessed_at: '2026-10-28T11:09:26.026943Z'
  support: context_only
  summary: Private exact structural/provenance inventory; operational fields unchanged
    and unassessed.
  snapshot_sha256: e4994c999cc7bc05e6a7d504822cb58c81960c893e594bb251c9bccc8817f3d5
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch064/record10/historical-report-scope.json
  locator: Complete exact file
  accessed_at: '2026-10-28T11:09:26.026966Z'
  support: context_only
  summary: Private exact structural/provenance inventory; operational fields unchanged
    and unassessed.
  snapshot_sha256: 562790deecafc2c9cd59fb93dcf35b04df7b7fdb245ac66ac21635748f1c0f91
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Matching rows in private inventory
  accessed_at: '2026-10-28T11:09:26.026985Z'
  support: context_only
  summary: Exact current packaged ID-row membership only. No chemical correctness
    or source validation.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete metadata
  accessed_at: '2026-10-28T11:09:26.027297Z'
  support: context_only
  summary: Packaged snapshot checksum, commit and row count verified.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T11:09:26.027320Z'
  support: context_only
  summary: Current singleton merge copies its maintained owner, so a blanket regeneration
    could transfer operational differences. This review authorizes metadata-only reconciliation
    and no such automatic transfer.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Complete file
  accessed_at: '2026-10-28T11:09:26.027345Z'
  support: context_only
  summary: Current conservative scientific-field equality is a grouping condition,
    not proof that a recipe is valid.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-mediadb
  kind: record_content
  reference: src/culturemech/import/mediadb_importer.py
  locator: _create_notes, _create_curation_history
  accessed_at: '2026-10-28T11:09:26.027365Z'
  support: context_only
  summary: Current _create_curation_history uses the generic Mazumdar2014 database
    publication; _create_notes supplies database provenance. These are not experimental-paper
    identity authentication or historical execution proof.
  snapshot_sha256: 5c2d98caf450ee8bb2f73f112e4edab7c3e0f2fa5f2aa7bd2a34e6fd2fdfd4d0
- evidence_id: pubmed10792526
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=10792526&retmode=json
  locator: Exact bibliographic title/authors/year/journal/DOI fields only; abstract
    and experimental content excluded
  accessed_at: '2026-10-28T11:00:16.669359Z'
  support: supports
  summary: Fresh bibliographic metadata only; no full paper, operational recipe, Methods,
    growth or pathogenicity result assessed.
  snapshot_sha256: 91386e8553dd56bb636b0ac89dee0ef8defe8c7b25ad12262040061028b473fb
- evidence_id: crossref10792526
  kind: authority
  reference: https://api.crossref.org/works/10.1046%2Fj.1365-2672.2000.01020.x
  locator: Exact bibliographic title/authors/year/journal/DOI fields only; abstract
    and experimental content excluded
  accessed_at: '2026-10-28T11:00:16.805496Z'
  support: supports
  summary: Fresh bibliographic metadata only; no full paper, operational recipe, Methods,
    growth or pathogenicity result assessed.
  snapshot_sha256: 5e5a0bdb008563f4050dcb2ecdbe0e1685f589cb76b5e27f857a84866a3b670b
- evidence_id: bibliography
  kind: record_content
  reference: REVIEW_WORK/batch064/record10/bibliographic-identity.json
  locator: Complete exact file
  accessed_at: '2026-10-28T11:09:26.028292Z'
  support: context_only
  summary: Exact primary bibliographic metadata joins; not formulation or experimental
    authentication.
  snapshot_sha256: 8a7b501598f3520175af548dd49f2f7f501a8f89a0992c0b0284d14e4da438b9
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch064/record10/schema-result.json
  accessed_at: '2026-10-28T10:59:49.968835Z'
  support: supports
  summary: Once-only canonical diagnostic with actual argv, times and full streams.
    Reference count zero does not authenticate scientific claims.
  snapshot_sha256: dffa049fd89017abb3cc727116f6d137cd5a37c546475bab9ca70672eb7e3a1b
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch064/record10/strict-result.json
  accessed_at: '2026-10-28T10:59:50.900353Z'
  support: supports
  summary: Once-only canonical diagnostic with actual argv, times and full streams.
    Reference count zero does not authenticate scientific claims.
  snapshot_sha256: 763fe17e387e7c3718ac2488d7632050daf6ae22d81df23a933b5e386f8ef900
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch064/record10/terms-result.json
  accessed_at: '2026-10-28T10:59:51.916490Z'
  support: supports
  summary: Once-only canonical diagnostic with actual argv, times and full streams.
    Reference count zero does not authenticate scientific claims.
  snapshot_sha256: 0973fdde0fd8a3250ccb23834f15d71a56337b14d5bddb85a4b93e43e6ded691
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch064/record10/references-result.json
  accessed_at: '2026-10-28T10:59:52.623939Z'
  support: supports
  summary: Once-only canonical diagnostic with actual argv, times and full streams.
    Reference count zero does not authenticate scientific claims.
  snapshot_sha256: 8417c0fabaa20595052ff1ee4897468019c77dd1f5590551237af24ddfdaac6d
assessments:
- assessment_id: identity
  area: identity
  topic: Exact stable record and bibliographic identity
  outcome: supported
  summary: The selected CM007191 target and its single MEDIADB290 owner are resolved
    by exact identity/provenance. The named publication is bibliographically authenticated;
    its title-level organism mention does not establish exact formulation correspondence
    or a strain-growth assertion.
  target_ids:
  - CultureMech:007191
  evidence_ids:
  - target
  - owner
  - bibliography
- assessment_id: history
  area: provenance
  topic: Existing source update and historical scope
  outcome: concern
  summary: The owner’s October14 bibliographic-only citation is credited, while the
    generated target is stale. Two October5 report headers describe incomplete source
    review and are not promoted into fresh science. Current importer/merger observations
    are not claims of historical execution; the owner’s original archived-paper/source-to-owner
    join was not recovered by this review.
  target_ids:
  - CultureMech:007191
  evidence_ids:
  - history
  - old-reports
  - target
  - owner
  - writer-mediadb
  - writer-merger
- assessment_id: scope
  area: scope
  topic: Restricted non-operational boundary
  outcome: not_applicable
  summary: The title explicitly concerns M. tuberculosis pathogenicity. This partial
    review is limited to bibliography, identity, provenance and schema. Formulation,
    culture conditions, experimental outcome, virulence and source operational content
    are excluded.
  target_ids:
  - CultureMech:007191
  evidence_ids:
  - bibliography
  - owner
- assessment_id: quantities
  area: quantity
  topic: Private unchanged structural census
  outcome: not_applicable
  summary: 50 existing concentration fields are inventoried privately and marked not_assessed.
    No operational values, calculations, source-derived amounts or corrections are
    reproduced or certified in the review.
  target_ids:
  - CultureMech:007191
  evidence_ids:
  - quantities
  - numeric
- assessment_id: grounding
  area: grounding
  topic: Identifier preservation without chemical assessment
  outcome: unknown
  summary: Existing ontology and legacy MIM identifiers are preserved structurally
    with exact current packaged-row membership. No fresh ingredient ontology/form
    verification or replacement is performed for this restricted record. Current MIM
    matches, absences and native term success are not chemical validity or historical-ID
    certification.
  target_ids:
  - CultureMech:007191
  evidence_ids:
  - groundings
  - mim
  - mim-meta
  - check-terms
- assessment_id: schema
  area: schema
  topic: Original canonical diagnostics
  outcome: supported
  summary: All four canonical diagnostics passed once, with strict zero errors and
    references zero checks. Their complete original streams are retained; they do
    not certify the excluded scientific content.
  target_ids:
  - CultureMech:007191
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
findings:
- finding_id: f1
  issue_key: culturemech-007191-generated-bibliographic-staleness
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Generated target omits the maintained bibliographic-only update
  description: The maintained MEDIADB290 owner contains the October14 PMID10792526
    citation and an explicit non-operational scope note. The generated target lacks
    that reference and its history event. Fresh PubMed and Crossref agree on James,
    Williams and Marsh, the 2000 article title and DOI. Preserve the historical Mazumdar2014
    import note as database provenance, distinguishing it from the experiment-paper
    citation. No owner ingredient, quantity, preparation or chemical changes are assessed
    or authorized for propagation.
  field_paths:
  - references
  - curation_history
  target_ids:
  - CultureMech:007191
  evidence_ids:
  - target
  - owner
  - bibliography
  - pubmed10792526
  - crossref10792526
  - writer-mediadb
  - writer-merger
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cmm.yaml
    role: maintained source
  rule_id: review-yaml-record/bibliographic-provenance
  native_severity: P2
  normalization_reason: Material omission of an already maintained explicit bibliographic
    source and its scope; no operational scientific defect or critical schema failure
    is adjudicated.
actions:
- action_id: a1
  description: Reconcile only the existing bibliographic citation and its explicit
    non-operational boundary into generated metadata, preserving the original history
    and adding an actual new observation if needed. Use a narrowly reviewed metadata-only
    path; do not blanket-regenerate operational owner differences or certify recipe
    equivalence from a title/DOI match.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007191
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cmm.yaml
    role: maintained source
  acceptance_checks:
  - Exact PMID/DOI/title/author/year and existing bibliography-only restrictions remain
    faithful to the metadata sources.
  - All ingredients, quantities, stock stages, chemical IDs, preparation, growth and
    pathogenicity-related assertions remain unchanged and unassessed; no operational
    owner repair is transferred.
  - Preserve history append-only, retain inspected provenance, and recheck only separately
    authorized metadata changes.
  generator: Explicitly scoped metadata-only reconciliation; no whole-recipe regeneration
limitations:
- Explicitly partial non-operational review with scientific_review:false. All operational
  formulation, supplied forms, concentrations, stock stages, preparation, culture
  and experimental assertions remain unchanged and unassessed.
- Full selected target and maintained owner bytes/history were read for identity and
  scope. The two prior report headers and provenance metadata were read; their operational
  tables and recommendations were deliberately not assessed or adopted.
- Fresh PubMed ESummary and Crossref were used only for title/authors/year/journal/DOI
  correspondence. No full article, operational MediaDB recipe/export, Methods or ingredient-repair
  sources were requested for this record.
- The owner’s NCBITaxon1773 note is retained as an existing bibliographic note; no
  fresh taxonomy authority check, target_organisms assertion, strain identity or growth
  association is made. Bibliographic identity does not authenticate the original source-to-owner
  formulation join.
- The packaged MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9. Exact
  local membership/absence is not historical catalog validation, supplied-form correctness
  or permission to repair legacy operational IDs.
- No formal validate/save, source edits, Git mutation or publication was performed.
  Current diagnostics are structural only and the reference validator examined zero
  references.
```
