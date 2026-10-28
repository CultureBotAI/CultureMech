# Non-operational review of cultivation medium for Chlamydophila pecorum

- Review: 20261028T124041Z-culturemech-000973-nonoperational-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T12:37:00.077237Z
- Finished UTC: 2026-10-28T12:40:41.510840Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Partial non-operational review of exact local identity, taxonomic synonym and source lineage. A bibliographic staleness gap requires metadata-only follow-up. All formulation, preparation, growth and chemical-form assertions remain unchanged and unassessed.

## Scope And Provenance

Non-operational identity, taxonomy, bibliography, provenance and schema only.

Selection: Authoritative batch067 selection index05
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000973 | data/merge_yaml/merged/CULTIVATION_MEDIUM_FOR_CHLAMYDOPHILA_PECORUM.yaml | generated | cultivation_medium_for_chlamydophila_pecorum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000973 | Exit 0; original streams retained. Strict check reports zero errors; reference check reports zero checks. |
| validate-strict | passed | True | CultureMech:000973 | Exit 0; original streams retained. Strict check reports zero errors; reference check reports zero checks. |
| validate-terms | passed | True | CultureMech:000973 | Exit 0; original streams retained. Strict check reports zero errors; reference check reports zero checks. |
| validate-references | passed | True | CultureMech:000973 | Exit 0; original streams retained. Strict check reports zero errors; reference check reports zero checks. |

## Scientific And Domain Assessments

### Exact local identity and current taxonomic synonym

identity: supported. Targets: CultureMech:000973.

The selected generated record and its sole maintained owner share CultureMech:000973 and the recorded DSMZ1503 medium accession. NCBI85991 identifies Chlamydia pecorum and lists Chlamydophila pecorum as a synonym. The original medium title is preserved; no strain, growth or formulation equivalence is inferred.

### Bounded source lineage and historical metadata

provenance: concern. Targets: CultureMech:000973.

The September owner update and its PDF reference are preserved as recorded provenance, while the generated bibliographic surface predates them. Three exact historical report identity/provenance headers were read; their operational tables and recommendations are excluded. No historical recipe payload or operational excerpt is authenticated here.

### Unchanged private quantity census

quantity: not_applicable. Targets: CultureMech:000973.

6 existing concentration fields are retained unchanged with not_assessed decisions. Private exact locators, stored values and types support integrity only; no public operational values or replacements are supplied.

### Structural identifier membership

grounding: unknown. Targets: CultureMech:000973.

Existing identifiers and their exact current packaged MIM membership are inventoried only. Chemical correctness, supplied forms, historical identifier validity and replacement mappings are unassessed.

### Non-operational review boundary

scope: not_applicable. Targets: CultureMech:000973.

Only identity, taxonomy, bibliography, provenance and schema are assessed. Formulation, stock stages, preparation, growth conditions and optimization remain unassessed. The explicit selected organism identity and authority metadata determine this boundary.

### Original native structural diagnostics

schema: supported. Targets: CultureMech:000973.

All four canonical diagnostics passed once on the selected target. Strict validation scanned one file with zero errors; reference validation performed zero checks. The additional inspection only extends input provenance and does not rerun these checks or certify cultivation content.

## Findings

### f1: Generated bibliographic attribution predates the maintained owner update

minor / open / confirmed; issue key: culturemech-000973-stale-bibliographic-provenance.

The generated target ends at its August merge event and has no references section. Its exact maintained owner records a September source repair and a DSMZ1503 PDF reference. This establishes a bibliographic/provenance difference only. The later operational edits and source text are not authenticated or recommended for transfer here.

## Recommended Actions And Acceptance Checks

### action1

Reconcile the recorded source identity and bibliographic lineage in a metadata-only follow-up. Preserve the original organism-labelled source title, stable record ID and all historical events; append a current verified provenance clarification where needed. Do not transfer or regenerate operational content as part of this action.

- Verify exact source identifier, bibliographic reference and owner provenance while retaining every operational field unchanged.
- Keep formulation, preparation, growth and chemical mappings unassessed; preserve original history append-only.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CULTIVATION_MEDIUM_FOR_CHLAMYDOPHILA_PECORUM.yaml; Exact metadata scope | context_only | Complete document bytes inventoried unchanged; identity and provenance metadata read. Operational fields and historical operational assertions remain unassessed. |
| local1 | data/normalized_yaml/bacterial/cultivation_medium_for_chlamydophila_pecorum.yaml; Exact metadata scope | context_only | Complete document bytes inventoried unchanged; identity and provenance metadata read. Operational fields and historical operational assertions remain unassessed. |
| quantities | REVIEW_WORK/batch067/record05/quantity-inventory.json; Exact metadata scope | context_only | Private exact structural or metadata inventory; existing operational content is not reproduced or endorsed in this review. |
| fields | REVIEW_WORK/batch067/record05/field-census.json; Exact metadata scope | context_only | Private exact structural or metadata inventory; existing operational content is not reproduced or endorsed in this review. |
| numeric | REVIEW_WORK/batch067/record05/numeric-field-census.json; Exact metadata scope | context_only | Private exact structural or metadata inventory; existing operational content is not reproduced or endorsed in this review. |
| grounding | REVIEW_WORK/batch067/record05/grounding-inventory.json; Exact metadata scope | context_only | Private exact structural or metadata inventory; existing operational content is not reproduced or endorsed in this review. |
| metadata | REVIEW_WORK/batch067/record05/metadata-reader.json; Exact metadata scope | context_only | Private exact structural or metadata inventory; existing operational content is not reproduced or endorsed in this review. |
| history | REVIEW_WORK/batch067/record05/historical-report-scope.json; Exact metadata scope | context_only | Private exact structural or metadata inventory; existing operational content is not reproduced or endorsed in this review. |
| links | REVIEW_WORK/batch067/record05/internal-reference-joins.json; Exact metadata scope | context_only | Private exact structural or metadata inventory; existing operational content is not reproduced or endorsed in this review. |
| boundary | REVIEW_WORK/batch067/record05/identity-and-scope.json; Exact metadata scope | context_only | Private exact structural or metadata inventory; existing operational content is not reproduced or endorsed in this review. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact identifier joins in grounding-inventory.json | context_only | Pinned current identifier membership only, not chemical correctness. |
| addendum | REVIEW_WORK/batch067/record05/inspection-addendum-context/lineage.json; original and effective source pins | context_only | Original inspection and four canonical checks preserved; additional history-named writer hashed for lineage only, with no assessment of its cultivation implementation. |
| identity0 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=85991&amp;retmode=xml; extracted-text lines 5-5 | supports | Taxonomic identity or recorded biosafety metadata only; no medium suitability or operational claim. |
| identity1 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=85991&amp;retmode=xml; extracted-text lines 7-7 | supports | Taxonomic identity or recorded biosafety metadata only; no medium suitability or operational claim. |
| identity2 | https://lpsn.dsmz.de/species/chlamydia-pecorum; extracted-text lines 199-199 | supports | Taxonomic identity or recorded biosafety metadata only; no medium suitability or operational claim. |
| validate-schema | REVIEW_WORK/batch067/record05/validate-schema-result.json; argv, times, exit code, complete stdout/stderr | supports | Original structural diagnostic passed; this is not scientific or operational approval. |
| validate-strict | REVIEW_WORK/batch067/record05/validate-strict-result.json; argv, times, exit code, complete stdout/stderr | supports | Original structural diagnostic passed; this is not scientific or operational approval. |
| validate-terms | REVIEW_WORK/batch067/record05/validate-terms-result.json; argv, times, exit code, complete stdout/stderr | supports | Original structural diagnostic passed; this is not scientific or operational approval. |
| validate-references | REVIEW_WORK/batch067/record05/validate-references-result.json; argv, times, exit code, complete stdout/stderr | supports | Original structural diagnostic passed; this is not scientific or operational approval. |

## Limits And Additional Notes

- Scientific review is false and completion/scope are partial. All cultivation, formulation, preparation and chemical-form content is outside the assessed scope.
- Complete local bytes and private structural fields were inventoried unchanged. Metadata was read separately; this does not claim scientific review of those fields.
- No DSM1503 primary recipe/API or external chemical ontology capture was requested. Existing operational snippets and historical raw hashes remain unauthenticated here.
- The history-named repair script is input-pinned for lineage only; its operational implementation is not assessed, endorsed or proposed for execution.
- NCBI and LPSN support identity/synonym metadata, not source formulation suitability. The source-specific historical title is retained.
- Packaged MIM membership describes current snapshot 6643131b0f12ab40b66f98135245fca04027e0e9 only; it does not establish chemical correctness or historical validity.
- No source edits, native formal validation/save, Git mutation or publication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T124041Z-culturemech-000973-nonoperational-review
kind: record
repository: CultureBotAI/CultureMech
title: Non-operational review of cultivation medium for Chlamydophila pecorum
started_at: '2026-10-28T12:37:00.077237Z'
finished_at: '2026-10-28T12:40:41.510840Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Read-only metadata and structural review of unchanged existing
    records; reviewer did not author or curate the target or maintained owner.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: false
summary: Partial non-operational review of exact local identity, taxonomic synonym
  and source lineage. A bibliographic staleness gap requires metadata-only follow-up.
  All formulation, preparation, growth and chemical-form assertions remain unchanged
  and unassessed.
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
  - path: data/merge_yaml/merged/CULTIVATION_MEDIUM_FOR_CHLAMYDOPHILA_PECORUM.yaml
    sha256: 563b2f04fadb7ecadfbc700931797585eb0b0d1432f6dbd4923066f9e3040cb2
    role: target
  - path: data/normalized_yaml/bacterial/cultivation_medium_for_chlamydophila_pecorum.yaml
    sha256: 4aaebea5123937963df89a51b50716aefc25d625db222904faedd3addaadb2ce
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cultivation_medium_for_chlamydophila_pecorum.yaml.md
    sha256: 81e30951931931e6a1dbacc262fd02169f2560fb83ae2b50a85b3d0e452da52b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CULTIVATION_MEDIUM_FOR_CHLAMYDOPHILA_PECORUM.md
    sha256: 9cfdcf22f4dd927368b764349cb1f2055148dec467570275f843f2e8d34ae126
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cultivation_medium_for_chlamydophila_pecorum.md
    sha256: 59725a19fb82d8c4b40061d1b6ea586b7fc9efeaa8becda8abb16c0dd187114f
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
  - path: scripts/fetch_mediadive_solution_volumes.py
    sha256: 408cdfa3f5c446e8f9c32ac98d7ea8a3a36553b23c032f3b7551f6a1661fd39a
    role: context
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/repair_dsmz_host_cell_score25.py
    sha256: 5f438a3145f2c627a7375f600dc9de935b30084e7cf791702835c683ba300dee
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_solution_concentration_evidence.py
    sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
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
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
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
  description: Non-operational identity, taxonomy, bibliography, provenance and schema
    only.
  selection: Authoritative batch067 selection index05
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000973
targets:
- target_id: CultureMech:000973
  path: data/merge_yaml/merged/CULTIVATION_MEDIUM_FOR_CHLAMYDOPHILA_PECORUM.yaml
  label: cultivation_medium_for_chlamydophila_pecorum
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cultivation_medium_for_chlamydophila_pecorum.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original streams retained. Strict check reports zero errors; reference
    check reports zero checks.
  target_ids:
  - CultureMech:000973
  command: just validate-schema data/merge_yaml/merged/CULTIVATION_MEDIUM_FOR_CHLAMYDOPHILA_PECORUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original streams retained. Strict check reports zero errors; reference
    check reports zero checks.
  target_ids:
  - CultureMech:000973
  command: just validate-strict data/merge_yaml/merged/CULTIVATION_MEDIUM_FOR_CHLAMYDOPHILA_PECORUM.yaml
    --workers 1 --out REVIEW_WORK/batch067/record05/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original streams retained. Strict check reports zero errors; reference
    check reports zero checks.
  target_ids:
  - CultureMech:000973
  command: just validate-terms data/merge_yaml/merged/CULTIVATION_MEDIUM_FOR_CHLAMYDOPHILA_PECORUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original streams retained. Strict check reports zero errors; reference
    check reports zero checks.
  target_ids:
  - CultureMech:000973
  command: just validate-references data/merge_yaml/merged/CULTIVATION_MEDIUM_FOR_CHLAMYDOPHILA_PECORUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CULTIVATION_MEDIUM_FOR_CHLAMYDOPHILA_PECORUM.yaml
  locator: Exact metadata scope
  accessed_at: '2026-10-28T12:40:41.509335Z'
  support: context_only
  summary: Complete document bytes inventoried unchanged; identity and provenance
    metadata read. Operational fields and historical operational assertions remain
    unassessed.
  snapshot_sha256: 563b2f04fadb7ecadfbc700931797585eb0b0d1432f6dbd4923066f9e3040cb2
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/cultivation_medium_for_chlamydophila_pecorum.yaml
  locator: Exact metadata scope
  accessed_at: '2026-10-28T12:40:41.509502Z'
  support: context_only
  summary: Complete document bytes inventoried unchanged; identity and provenance
    metadata read. Operational fields and historical operational assertions remain
    unassessed.
  snapshot_sha256: 4aaebea5123937963df89a51b50716aefc25d625db222904faedd3addaadb2ce
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch067/record05/quantity-inventory.json
  locator: Exact metadata scope
  accessed_at: '2026-10-28T12:40:41.509534Z'
  support: context_only
  summary: Private exact structural or metadata inventory; existing operational content
    is not reproduced or endorsed in this review.
  snapshot_sha256: 493e92d78b13f0481e7a9ae15f2f8dc1c39ea45b46770f1e10610e33dc14f871
- evidence_id: fields
  kind: record_content
  reference: REVIEW_WORK/batch067/record05/field-census.json
  locator: Exact metadata scope
  accessed_at: '2026-10-28T12:40:41.509566Z'
  support: context_only
  summary: Private exact structural or metadata inventory; existing operational content
    is not reproduced or endorsed in this review.
  snapshot_sha256: 9e6eb5bb309150f82a2192cf827fc5fe206a6052989bd33b48787b8c4482dbb0
- evidence_id: numeric
  kind: record_content
  reference: REVIEW_WORK/batch067/record05/numeric-field-census.json
  locator: Exact metadata scope
  accessed_at: '2026-10-28T12:40:41.509596Z'
  support: context_only
  summary: Private exact structural or metadata inventory; existing operational content
    is not reproduced or endorsed in this review.
  snapshot_sha256: 5db79d567fe246ab1b8bffe05574cf2009c87fcaab40ed58f164675080cb5728
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch067/record05/grounding-inventory.json
  locator: Exact metadata scope
  accessed_at: '2026-10-28T12:40:41.509622Z'
  support: context_only
  summary: Private exact structural or metadata inventory; existing operational content
    is not reproduced or endorsed in this review.
  snapshot_sha256: c363d750ded27d8350a126774d1382ca32460dac991f9acc5bd1aaf2d77b28f4
- evidence_id: metadata
  kind: record_content
  reference: REVIEW_WORK/batch067/record05/metadata-reader.json
  locator: Exact metadata scope
  accessed_at: '2026-10-28T12:40:41.509667Z'
  support: context_only
  summary: Private exact structural or metadata inventory; existing operational content
    is not reproduced or endorsed in this review.
  snapshot_sha256: f7933d3196589f2c2ba12f99fae71cfe6f3b51551a06aa18d08ecd7c367e3705
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch067/record05/historical-report-scope.json
  locator: Exact metadata scope
  accessed_at: '2026-10-28T12:40:41.509700Z'
  support: context_only
  summary: Private exact structural or metadata inventory; existing operational content
    is not reproduced or endorsed in this review.
  snapshot_sha256: cc885f68e65da9c7c2d854b0dcad93819bd43e5cc1b424a0442763f03a6b2a8e
- evidence_id: links
  kind: record_content
  reference: REVIEW_WORK/batch067/record05/internal-reference-joins.json
  locator: Exact metadata scope
  accessed_at: '2026-10-28T12:40:41.509733Z'
  support: context_only
  summary: Private exact structural or metadata inventory; existing operational content
    is not reproduced or endorsed in this review.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: boundary
  kind: record_content
  reference: REVIEW_WORK/batch067/record05/identity-and-scope.json
  locator: Exact metadata scope
  accessed_at: '2026-10-28T12:40:41.509768Z'
  support: context_only
  summary: Private exact structural or metadata inventory; existing operational content
    is not reproduced or endorsed in this review.
  snapshot_sha256: cbfa75fd17fc2b88a3ccffd38bb62384724914031d9b3455b0f27c827c594ed5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact identifier joins in grounding-inventory.json
  accessed_at: '2026-10-28T12:40:41.509796Z'
  support: context_only
  summary: Pinned current identifier membership only, not chemical correctness.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: addendum
  kind: record_content
  reference: REVIEW_WORK/batch067/record05/inspection-addendum-context/lineage.json
  locator: original and effective source pins
  accessed_at: '2026-10-28T12:40:41.510108Z'
  support: context_only
  summary: Original inspection and four canonical checks preserved; additional history-named
    writer hashed for lineage only, with no assessment of its cultivation implementation.
  snapshot_sha256: a355e0356b5f8df202dd57fd1f151a036481cbc9938014eb654a13426850acb8
- evidence_id: identity0
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=85991&retmode=xml
  locator: extracted-text lines 5-5
  quote: <ScientificName>Chlamydia pecorum</ScientificName>
  accessed_at: '2026-10-28T12:37:44.090618Z'
  support: supports
  summary: Taxonomic identity or recorded biosafety metadata only; no medium suitability
    or operational claim.
  snapshot_sha256: 90db19d1dba93207704840ce6eefa995bdcc10fc45393c13a0f04d76a3f30f23
- evidence_id: identity1
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=85991&retmode=xml
  locator: extracted-text lines 7-7
  quote: <Synonym>Chlamydophila pecorum</Synonym>
  accessed_at: '2026-10-28T12:37:44.090618Z'
  support: supports
  summary: Taxonomic identity or recorded biosafety metadata only; no medium suitability
    or operational claim.
  snapshot_sha256: 90db19d1dba93207704840ce6eefa995bdcc10fc45393c13a0f04d76a3f30f23
- evidence_id: identity2
  kind: authority
  reference: https://lpsn.dsmz.de/species/chlamydia-pecorum
  locator: extracted-text lines 199-199
  quote: 'animal pathogen - biological class of risk animal: 2'
  accessed_at: '2026-10-28T12:37:43.951856Z'
  support: supports
  summary: Taxonomic identity or recorded biosafety metadata only; no medium suitability
    or operational claim.
  snapshot_sha256: 5c3aae957bfb0071b18876c514f97b307cc30195d786112b07e29b12ad681508
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch067/record05/validate-schema-result.json
  locator: argv, times, exit code, complete stdout/stderr
  accessed_at: '2026-10-28T12:37:01.122104Z'
  support: supports
  summary: Original structural diagnostic passed; this is not scientific or operational
    approval.
  snapshot_sha256: d6ec1b94e8133f02b6d37f06ffb269803c51ca99f69eae3e1396d9dfb19f084f
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch067/record05/validate-strict-result.json
  locator: argv, times, exit code, complete stdout/stderr
  accessed_at: '2026-10-28T12:37:02.049142Z'
  support: supports
  summary: Original structural diagnostic passed; this is not scientific or operational
    approval.
  snapshot_sha256: 34bf615b96699451c3b242cea9a80f68c0437fc2c3e96bab7cec485a1bdcc984
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch067/record05/validate-terms-result.json
  locator: argv, times, exit code, complete stdout/stderr
  accessed_at: '2026-10-28T12:37:03.038150Z'
  support: supports
  summary: Original structural diagnostic passed; this is not scientific or operational
    approval.
  snapshot_sha256: e070c8ac8f66a571f5e84370499df42cad58d44e197fb4b7179342dee20a0056
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch067/record05/validate-references-result.json
  locator: argv, times, exit code, complete stdout/stderr
  accessed_at: '2026-10-28T12:37:03.667321Z'
  support: supports
  summary: Original structural diagnostic passed; this is not scientific or operational
    approval.
  snapshot_sha256: 3e171b7156c47bb005df216bb427845a8a0723a09fee705aa347faebdeb2c8f7
assessments:
- assessment_id: a1
  area: identity
  topic: Exact local identity and current taxonomic synonym
  outcome: supported
  summary: The selected generated record and its sole maintained owner share CultureMech:000973
    and the recorded DSMZ1503 medium accession. NCBI85991 identifies Chlamydia pecorum
    and lists Chlamydophila pecorum as a synonym. The original medium title is preserved;
    no strain, growth or formulation equivalence is inferred.
  target_ids:
  - CultureMech:000973
  evidence_ids:
  - local0
  - local1
  - identity0
  - identity1
- assessment_id: a2
  area: provenance
  topic: Bounded source lineage and historical metadata
  outcome: concern
  summary: The September owner update and its PDF reference are preserved as recorded
    provenance, while the generated bibliographic surface predates them. Three exact
    historical report identity/provenance headers were read; their operational tables
    and recommendations are excluded. No historical recipe payload or operational
    excerpt is authenticated here.
  target_ids:
  - CultureMech:000973
  evidence_ids:
  - metadata
  - history
  - addendum
- assessment_id: a3
  area: quantity
  topic: Unchanged private quantity census
  outcome: not_applicable
  summary: 6 existing concentration fields are retained unchanged with not_assessed
    decisions. Private exact locators, stored values and types support integrity only;
    no public operational values or replacements are supplied.
  target_ids:
  - CultureMech:000973
  evidence_ids:
  - quantities
  - numeric
- assessment_id: a4
  area: grounding
  topic: Structural identifier membership
  outcome: unknown
  summary: Existing identifiers and their exact current packaged MIM membership are
    inventoried only. Chemical correctness, supplied forms, historical identifier
    validity and replacement mappings are unassessed.
  target_ids:
  - CultureMech:000973
  evidence_ids:
  - grounding
  - mim
  - validate-terms
- assessment_id: a5
  area: scope
  topic: Non-operational review boundary
  outcome: not_applicable
  summary: Only identity, taxonomy, bibliography, provenance and schema are assessed.
    Formulation, stock stages, preparation, growth conditions and optimization remain
    unassessed. The explicit selected organism identity and authority metadata determine
    this boundary.
  target_ids:
  - CultureMech:000973
  evidence_ids:
  - boundary
  - identity0
  - identity1
  - identity2
- assessment_id: a6
  area: schema
  topic: Original native structural diagnostics
  outcome: supported
  summary: All four canonical diagnostics passed once on the selected target. Strict
    validation scanned one file with zero errors; reference validation performed zero
    checks. The additional inspection only extends input provenance and does not rerun
    these checks or certify cultivation content.
  target_ids:
  - CultureMech:000973
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
  - addendum
findings:
- finding_id: f1
  issue_key: culturemech-000973-stale-bibliographic-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated bibliographic attribution predates the maintained owner update
  description: The generated target ends at its August merge event and has no references
    section. Its exact maintained owner records a September source repair and a DSMZ1503
    PDF reference. This establishes a bibliographic/provenance difference only. The
    later operational edits and source text are not authenticated or recommended for
    transfer here.
  field_paths:
  - references
  - curation_history
  - data/normalized_yaml/bacterial/cultivation_medium_for_chlamydophila_pecorum.yaml::curation_history[3]
  target_ids:
  - CultureMech:000973
  evidence_ids:
  - local0
  - local1
  - metadata
  - history
  - addendum
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cultivation_medium_for_chlamydophila_pecorum.yaml
    role: maintained normalized contributor
  rule_id: review-yaml-record/nonoperational-bibliographic-provenance
  native_severity: P3
  normalization_reason: P3 normalized to minor for a bounded bibliographic traceability
    gap. Formulation and cultivation correctness remain unassessed.
actions:
- action_id: action1
  description: Reconcile the recorded source identity and bibliographic lineage in
    a metadata-only follow-up. Preserve the original organism-labelled source title,
    stable record ID and all historical events; append a current verified provenance
    clarification where needed. Do not transfer or regenerate operational content
    as part of this action.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000973
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cultivation_medium_for_chlamydophila_pecorum.yaml
    role: maintained normalized contributor
  generator: Metadata-only follow-up; no operational writer execution or whole-recipe
    regeneration.
  acceptance_checks:
  - Verify exact source identifier, bibliographic reference and owner provenance while
    retaining every operational field unchanged.
  - Keep formulation, preparation, growth and chemical mappings unassessed; preserve
    original history append-only.
limitations:
- Scientific review is false and completion/scope are partial. All cultivation, formulation,
  preparation and chemical-form content is outside the assessed scope.
- Complete local bytes and private structural fields were inventoried unchanged. Metadata
  was read separately; this does not claim scientific review of those fields.
- No DSM1503 primary recipe/API or external chemical ontology capture was requested.
  Existing operational snippets and historical raw hashes remain unauthenticated here.
- The history-named repair script is input-pinned for lineage only; its operational
  implementation is not assessed, endorsed or proposed for execution.
- NCBI and LPSN support identity/synonym metadata, not source formulation suitability.
  The source-specific historical title is retained.
- Packaged MIM membership describes current snapshot 6643131b0f12ab40b66f98135245fca04027e0e9
  only; it does not establish chemical correctness or historical validity.
- No source edits, native formal validation/save, Git mutation or publication.
```
