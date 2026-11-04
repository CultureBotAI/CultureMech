# Provenance-only partial review: acanthamoeba_medium (CultureMech:000970)

- Review: 20261021T094507Z-culturemech-000970-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:35:33Z
- Finished UTC: 2026-10-21T09:45:07Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Partial provenance-only review. Exact DSMZ1500/MediaDive1500 identity and the maintained owner resolve, all four diagnostics pass, and asserted ontology metadata resolve. Local multiple-supplier/catalog annotations point to a tertiary page rather than a manufacturer-specific source chain. Supplier access attempts remain bounded failures. Formulation, procedures and biological claims were not reassessed.

## Scope And Provenance

One generated record, assessed only for exact owner/source identity, citation and supplier provenance, identifier/label metadata, field structure and history. Literature support for formulation or biological claims was not reassessed.

Selection: Task review 139; batch 014 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirteen task batches contain 130 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 132 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000970 | data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml | generated | acanthamoeba_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000970 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000970 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch014/139/strict.tsv |
| validate-terms | passed | True | CultureMech:000970 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000970 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000970 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Required formulation and operational scientific assessment | skipped | True | CultureMech:000970 | The record contains infected-Acanthamoeba host-culture and intracellular-bacteria maintenance material. Operational formulation and culture-procedure assessment is deliberately excluded under the agreed safety scope. Ingredient, stock, concentration, preparation, culture-condition and biological-performance assessments were not performed. This is a deliberate scope boundary, not a conclusion that those fields are wrong. |
| Manufacturer-specific historical product/citation identity | unavailable | True | CultureMech:000970 | The local annotation names multiple suppliers and catalogs, but no exact manufacturer-specific source chain to this historical recipe was established. The bounded Sigma PDF request timed out and the BD product request returned403. No manufacturer equivalence, historical identity or composition was inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000970.

The four documented recipes completed; interpret the scope of each separately.

### Operational and biological assessment excluded

scope: unknown. Targets: CultureMech:000970.

The record contains infected-Acanthamoeba host-culture and intracellular-bacteria maintenance material. Operational formulation and culture-procedure assessment is deliberately excluded under the agreed safety scope. No concentration decisions, chemistry corrections or procedural recommendations are supplied; literature support for those claims was not reassessed.

### Exact record, owner and collection accession

identity: supported. Targets: CultureMech:000970.

The target and normalized owner share CultureMech:000970 and identical maintained fields; merge metadata/history trace the single authoritative owner. DSMZ1500 and MediaDive1500 identity metadata agree. This is provenance/representation correspondence, not validation of biological or operational claims.

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:000970.

14 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 15/17 primary and 9/17 secondary instances; all asserted secondary keys have exact pinned MIM rows. This is metadata only: no source-to-ingredient chemical correspondence or replacement is assessed.

Instance coverage on a0–100 percent scale, denominator17: primary88.24%; secondary52.94%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:000970.

17 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Catalog annotations and authoritative source locators

provenance: concern. Targets: CultureMech:000970.

Both layers list multiple suppliers/catalogs and use a Wikipedia URL as product_url, while the notes say composition was researched from a product specification. No manufacturer-specific citation/version or equivalence chain is supplied. The bounded official-URL attempts did not resolve that provenance; no judgment about ingredient amounts or product composition follows.

### Source metadata versus operational field semantics

schema: supported. Targets: CultureMech:000970.

The whole local YAML and all mechanical outputs were inspected. Identity, notes, supplier_catalog and history are readable and traceable to the maintained owner. Passing field/enum validation does not verify preparation action labels, chemical forms, culture procedures, variant assembly or biological suitability; those semantics remain excluded.

### Category and application metadata

scope: unknown. Targets: CultureMech:000970.

Bacterial filing, medium classification and generic application wording are preserved as record metadata. Host-culture context alone does not prove a category error; no organism, taxonomic replacement or growth claim is introduced in this provenance-only review.

## Findings

### f1: Multiple catalog annotations lack an authoritative source chain

minor / open / confirmed; issue key: CM000970-manufacturer-citation-provenance.

The target and owner identify multiple suppliers/catalogs but use a tertiary Wikipedia page as product_url and provide no manufacturer-specific document/version locator or evidence connecting those products to this source record. Official-URL retrieval was unsuccessful in the bounded attempts. This is a metadata traceability gap, not a formulation or supplier-equivalence finding.

## Recommended Actions And Acceptance Checks

### a1

Clarify the maintained supplier/citation metadata so verified collection identity, asserted catalogs, attempted access and unresolved historical-product linkage are distinct. Add an authoritative exact product/version locator only if actually established; otherwise retain the uncertainty. Do not transfer a supplier formulation, correct quantities or provide culture-procedure guidance.

- Limit follow-up to accession, supplier/citation identity, exact document/version locator and honest provenance wording; no operational or formulation edits under this review.
- Preserve prior history; append an accurate metadata clarification only after a separately authorized maintained-input change.
- After an authorized metadata change, run the four documented target validators and applicable merge checks if regeneration is authorized; mechanical passes do not certify scientific validity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Entire local YAML read for record/owner identity, provenance and field structure. Operational content was not assessed or reproduced in this review. |
| owner-0 | data/normalized_yaml/bacterial/acanthamoeba_medium.yaml; Entire maintained YAML | context_only | Entire local YAML read for record/owner identity, provenance and field structure. Operational content was not assessed or reproduced in this review. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch014/139/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch014/139/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml:1:id: CultureMech:000970<br>./data/normalized_yaml/bacterial/acanthamoeba_medium.yaml:1:id: CultureMech:000970<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch014/source-preflight-bound/139/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 18 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| scope-contract | docs/record-reviews.md; Verdict And Severity; provenance-only inspection and scientific_review flag | supports | The native contract separates provenance-only inspection from scientific review and requires literature support not reassessed to be explicit. |
| collection-identity | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1500.pdf; Document accession/title and collection attribution only | supports | Official collection capture identifies DSMZ1500 ACANTHAMOEBA MEDIUM. Operational text and formulation are outside this assessment. |
| provider-identity | https://mediadive.dsmz.de/rest/medium/1500; $.data.medium.id, name, source, link only | supports | MediaDive medium metadata identifies accession1500, DSMZ and the same official recipe URL. This verifies citation identity only; no provider formulation, culture condition or procedure was assessed. |
| access-sigma22092 | https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/product/documents/288/904/22092dat.pdf; Bounded retrieval attempt metadata only | context_only | The exact official supplier URL did not yield usable source content: status=None, error=The read operation timed out. The attempt and its actual access time are preserved; this is not evidence that the product or its documentation does not exist. |
| access-bd211825 | https://www.bd.com/en-us/products-and-solutions/products/product-page.211825; Bounded retrieval attempt metadata only | context_only | The exact official supplier URL did not yield usable source content: status=403, error=HTTP Error 403: Forbidden. The attempt and its actual access time are preserved; this is not evidence that the product or its documentation does not exist. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17992 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:17992 resolves to sucrose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi18237 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18237; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:18237 resolves to glutamic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32142 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32142; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:32142 resolves to sodium citrate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76181 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76181; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:76181 resolves to ferrous ammonium sulfate hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | CHEBI:91258 resolves to disodium hydrogenphosphate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| foodon03315720 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315720; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | FOODON:03315720 resolves to vegetable protein, hydrolyzed. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| micro0000182 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182; Exact OLS obo_id, canonical label, obsolete flag only; source forms not assessed | supports | MICRO:0000182 resolves to tryptone. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17992": [{"label": "Sucrose", "match_type": "preferred_term", "identifier": "CHEBI:17992", "preferred_term": "Sucrose", "ontology_id": "CHEBI:17992", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:18237": [{"label": "Glutamic acid", "match_type": "preferred_term", "identifier": "CHEBI:18237", "preferred_term": "Glutamic acid", "ontology_id": "CHEBI:18237", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32142": [{"label": "Na3-citrate x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32142", "preferred_term": "Na3-citrate x 2 H2O", "ontology_id": "CHEBI:32142", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34683": [{"label": "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76181": [{"label": "Fe(NH4)2(SO4)2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76181", "preferred_term": "Fe(NH4)2(SO4)2 x 6 H2O", "ontology_id": "CHEBI:76181", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml; data/normalized_yaml/bacterial/acanthamoeba_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/acanthamoeba_medium.yaml", "events": 8, "timestamp_issues": []}] |

## Limits And Additional Notes

- The record contains infected-Acanthamoeba host-culture and intracellular-bacteria maintenance material. Operational formulation and culture-procedure assessment is deliberately excluded under the agreed safety scope.
- This is not a complete scientific assessment. Required operational review is explicitly skipped, not implicitly passed. Partial completion does not certify the formulation, procedures or performance.
- The reference command inspected0 excerpts; its pass verifies no supplier identity, recipe claim or biological assertion. Ontology metadata checks do not assess source chemical-form correspondence.
- No corpus, history, source cache, saved review or scientific status was changed. No new cultivation advice, formulation correction or experiment is proposed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094507Z-culturemech-000970-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Provenance-only partial review: acanthamoeba_medium (CultureMech:000970)'
started_at: '2026-10-21T09:35:33Z'
finished_at: '2026-10-21T09:45:07Z'
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
scientific_review: false
summary: Partial provenance-only review. Exact DSMZ1500/MediaDive1500 identity and
  the maintained owner resolve, all four diagnostics pass, and asserted ontology metadata
  resolve. Local multiple-supplier/catalog annotations point to a tertiary page rather
  than a manufacturer-specific source chain. Supplier access attempts remain bounded
  failures. Formulation, procedures and biological claims were not reassessed.
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
  - path: data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
    sha256: c002b915067723463f88b75c270cbfcb22cf20c3d2614c3efc05486127db7554
    role: target
  - path: data/normalized_yaml/bacterial/acanthamoeba_medium.yaml
    sha256: 31260668e9e8c78ea4fa4d14d7bbf6d1f53f1636c3386bfa849100a6c2a77d24
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
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
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
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  description: One generated record, assessed only for exact owner/source identity,
    citation and supplier provenance, identifier/label metadata, field structure and
    history. Literature support for formulation or biological claims was not reassessed.
  selection: Task review 139; batch 014 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirteen task batches
    contain 130 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 132 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000970
  exclusions:
  - target: CultureMech:000970
    reason: 'The record contains infected-Acanthamoeba host-culture and intracellular-bacteria
      maintenance material. Operational formulation and culture-procedure assessment
      is deliberately excluded under the agreed safety scope. Excluded: ingredient
      or chemical-form corrections, concentrations, stock arithmetic, preparation,
      cultivation/maintenance/storage procedures, culture conditions and biological-performance
      claims.'
targets:
- target_id: CultureMech:000970
  path: data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
  label: acanthamoeba_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acanthamoeba_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch014/139/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch014/139/strict.tsv"
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000970
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
  - CultureMech:000970
- check_id: operational-formulation-review
  name: Required formulation and operational scientific assessment
  required: true
  status: skipped
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - record
  - scope-contract
  summary: The record contains infected-Acanthamoeba host-culture and intracellular-bacteria
    maintenance material. Operational formulation and culture-procedure assessment
    is deliberately excluded under the agreed safety scope. Ingredient, stock, concentration,
    preparation, culture-condition and biological-performance assessments were not
    performed. This is a deliberate scope boundary, not a conclusion that those fields
    are wrong.
- check_id: manufacturer-source-identity
  name: Manufacturer-specific historical product/citation identity
  required: true
  status: unavailable
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - record
  - owner-0
  - collection-identity
  - access-sigma22092
  - access-bd211825
  summary: The local annotation names multiple suppliers and catalogs, but no exact
    manufacturer-specific source chain to this historical recipe was established.
    The bounded Sigma PDF request timed out and the BD product request returned403.
    No manufacturer equivalence, historical identity or composition was inferred.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T09:45:06Z'
  support: context_only
  summary: Entire local YAML read for record/owner identity, provenance and field
    structure. Operational content was not assessed or reproduced in this review.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/acanthamoeba_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T09:45:06Z'
  support: context_only
  summary: Entire local YAML read for record/owner identity, provenance and field
    structure. Operational content was not assessed or reproduced in this review.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:37.538212Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch014/139/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:39.558158Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch014/139/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:42.039254Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:43.507783Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T09:45:06Z'
  support: supports
  summary: './data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml:1:id: CultureMech:000970

    ./data/normalized_yaml/bacterial/acanthamoeba_medium.yaml:1:id: CultureMech:000970

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch014/source-preflight-bound/139/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T09:45:06Z'
  support: supports
  summary: 18 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 7dee8c83ec9a3fc411bda4c2e29d7f5d2a821b03475f8ab7728c3099fe2c1cd2
- evidence_id: scope-contract
  kind: record_content
  reference: docs/record-reviews.md
  locator: Verdict And Severity; provenance-only inspection and scientific_review
    flag
  accessed_at: '2026-10-21T09:45:06Z'
  support: supports
  summary: The native contract separates provenance-only inspection from scientific
    review and requires literature support not reassessed to be explicit.
- evidence_id: collection-identity
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1500.pdf
  locator: Document accession/title and collection attribution only
  accessed_at: '2026-10-21T09:28:26.141221Z'
  support: supports
  summary: Official collection capture identifies DSMZ1500 ACANTHAMOEBA MEDIUM. Operational
    text and formulation are outside this assessment.
  quote: ACANTHAMOEBA MEDIUM
  snapshot_sha256: 84c818e0d370fd9085735ef20849ebc5de122ab9156aafc544c1be14f4a846ca
- evidence_id: provider-identity
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1500
  locator: $.data.medium.id, name, source, link only
  accessed_at: '2026-10-21T09:28:24.720382Z'
  support: supports
  summary: MediaDive medium metadata identifies accession1500, DSMZ and the same official
    recipe URL. This verifies citation identity only; no provider formulation, culture
    condition or procedure was assessed.
  snapshot_sha256: df4daf27b8ab3032041f7cbf01dd21f7f6fad7980a9ecbdd3b4d9c7af3c9989b
- evidence_id: access-sigma22092
  kind: database
  reference: https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/product/documents/288/904/22092dat.pdf
  locator: Bounded retrieval attempt metadata only
  accessed_at: '2026-10-21T09:30:02.552939Z'
  support: context_only
  summary: 'The exact official supplier URL did not yield usable source content: status=None,
    error=The read operation timed out. The attempt and its actual access time are
    preserved; this is not evidence that the product or its documentation does not
    exist.'
- evidence_id: access-bd211825
  kind: database
  reference: https://www.bd.com/en-us/products-and-solutions/products/product-page.211825
  locator: Bounded retrieval attempt metadata only
  accessed_at: '2026-10-21T09:30:02.551711Z'
  support: context_only
  summary: 'The exact official supplier URL did not yield usable source content: status=403,
    error=HTTP Error 403: Forbidden. The attempt and its actual access time are preserved;
    this is not evidence that the product or its documentation does not exist.'
  snapshot_sha256: fd8d3405e9f73d7650418e9b05b5a81b627beff09ee5292a8f222bba18b91227
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi17992
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T08:42:31.913996Z'
  support: supports
  summary: CHEBI:17992 resolves to sucrose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 509f9cbc014a0211d3a8e536a2c68048a090719ce68ee80550c8bbf532f150aa
- evidence_id: chebi18237
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18237
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T09:28:26.404771Z'
  support: supports
  summary: CHEBI:18237 resolves to glutamic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: fb5cac52a2eacb0d6479789d2324d7f238b6c742c8543de7c28c54f2a974b7a5
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32142
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32142
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T09:28:26.951076Z'
  support: supports
  summary: CHEBI:32142 resolves to sodium citrate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b4f0ce2cb1b062201417730385f65363b10c4760d65571b0ee77c87c4ac1fb43
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi76181
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76181
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T09:28:27.017914Z'
  support: supports
  summary: CHEBI:76181 resolves to ferrous ammonium sulfate hexahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 1ca5b1ee73ce8d8fd35e60c7f45baacd870b6f5fdce0a02345be62e7622dbaa5
- evidence_id: chebi91258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-21T09:28:27.054091Z'
  support: supports
  summary: CHEBI:91258 resolves to disodium hydrogenphosphate dihydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: f6c74e6e0b876aadf2fe47494521d320abb79244773bf4c44da7b288b1e27319
- evidence_id: foodon03315720
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315720
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-20T07:37:22.786983Z'
  support: supports
  summary: FOODON:03315720 resolves to vegetable protein, hydrolyzed. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: aa063e8b88177611aba640828e84d3982b1b3b1c65b11647d89c9efbf6274c25
- evidence_id: micro0000182
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182
  locator: Exact OLS obo_id, canonical label, obsolete flag only; source forms not
    assessed
  accessed_at: '2026-10-20T07:37:21.973857Z'
  support: supports
  summary: MICRO:0000182 resolves to tryptone. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 01875997c482a49e4d41eb35c6c697e190afd236a8527625e94b6f96df3872b0
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T09:45:06Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17234":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17992": [{"label": "Sucrose", "match_type": "preferred_term",
    "identifier": "CHEBI:17992", "preferred_term": "Sucrose", "ontology_id": "CHEBI:17992",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:18237": [{"label":
    "Glutamic acid", "match_type": "preferred_term", "identifier": "CHEBI:18237",
    "preferred_term": "Glutamic acid", "ontology_id": "CHEBI:18237", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:31795": [{"label": "MgSO4 x
    7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32142": [{"label": "Na3-citrate x 2
    H2O", "match_type": "preferred_term", "identifier": "CHEBI:32142", "preferred_term":
    "Na3-citrate x 2 H2O", "ontology_id": "CHEBI:32142", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:34683": [{"label": "Na2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:76181": [{"label": "Fe(NH4)2(SO4)2 x 6 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:76181", "preferred_term": "Fe(NH4)2(SO4)2
    x 6 H2O", "ontology_id": "CHEBI:76181", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id":
    "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACANTHAMOEBA_MEDIUM.yaml; data/normalized_yaml/bacterial/acanthamoeba_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T09:45:06Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/acanthamoeba_medium.yaml",
    "events": 8, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: scientific-scope
  area: scope
  topic: Operational and biological assessment excluded
  outcome: unknown
  summary: The record contains infected-Acanthamoeba host-culture and intracellular-bacteria
    maintenance material. Operational formulation and culture-procedure assessment
    is deliberately excluded under the agreed safety scope. No concentration decisions,
    chemistry corrections or procedural recommendations are supplied; literature support
    for those claims was not reassessed.
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - record
  - scope-contract
- assessment_id: identity
  area: identity
  topic: Exact record, owner and collection accession
  outcome: supported
  summary: The target and normalized owner share CultureMech:000970 and identical
    maintained fields; merge metadata/history trace the single authoritative owner.
    DSMZ1500 and MediaDive1500 identity metadata agree. This is provenance/representation
    correspondence, not validation of biological or operational claims.
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - record
  - owner-0
  - id-search
  - collection-identity
  - provider-identity
- assessment_id: ontology-metadata
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '14 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 15/17 primary and 9/17 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. This is metadata
    only: no source-to-ingredient chemical correspondence or replacement is assessed.'
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi17234
  - chebi17992
  - chebi18237
  - chebi2509
  - chebi26710
  - chebi31795
  - chebi32142
  - chebi34683
  - chebi63036
  - chebi76181
  - chebi91258
  - foodon03315720
  - micro0000182
  details: 'Instance coverage on a0–100 percent scale, denominator17: primary88.24%;
    secondary52.94%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 17 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: supplier-provenance
  area: provenance
  topic: Catalog annotations and authoritative source locators
  outcome: concern
  summary: Both layers list multiple suppliers/catalogs and use a Wikipedia URL as
    product_url, while the notes say composition was researched from a product specification.
    No manufacturer-specific citation/version or equivalence chain is supplied. The
    bounded official-URL attempts did not resolve that provenance; no judgment about
    ingredient amounts or product composition follows.
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - record
  - owner-0
  - collection-identity
  - access-sigma22092
  - access-bd211825
- assessment_id: field-structure
  area: schema
  topic: Source metadata versus operational field semantics
  outcome: supported
  summary: The whole local YAML and all mechanical outputs were inspected. Identity,
    notes, supplier_catalog and history are readable and traceable to the maintained
    owner. Passing field/enum validation does not verify preparation action labels,
    chemical forms, culture procedures, variant assembly or biological suitability;
    those semantics remain excluded.
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - record
  - owner-0
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: classification
  area: scope
  topic: Category and application metadata
  outcome: unknown
  summary: Bacterial filing, medium classification and generic application wording
    are preserved as record metadata. Host-culture context alone does not prove a
    category error; no organism, taxonomic replacement or growth claim is introduced
    in this provenance-only review.
  target_ids:
  - CultureMech:000970
  evidence_ids:
  - record
  - owner-0
  - scope-contract
findings:
- finding_id: f1
  issue_key: CM000970-manufacturer-citation-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Multiple catalog annotations lack an authoritative source chain
  description: The target and owner identify multiple suppliers/catalogs but use a
    tertiary Wikipedia page as product_url and provide no manufacturer-specific document/version
    locator or evidence connecting those products to this source record. Official-URL
    retrieval was unsuccessful in the bounded attempts. This is a metadata traceability
    gap, not a formulation or supplier-equivalence finding.
  target_ids:
  - CultureMech:000970
  field_paths:
  - notes
  - ingredients[*].supplier_catalog
  - references
  evidence_ids:
  - record
  - owner-0
  - collection-identity
  - access-sigma22092
  - access-bd211825
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acanthamoeba_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: P3 normalized to minor because this finding is limited to
    catalog/source traceability; no scientific formulation or operational defect is
    asserted.
actions:
- action_id: a1
  description: Clarify the maintained supplier/citation metadata so verified collection
    identity, asserted catalogs, attempted access and unresolved historical-product
    linkage are distinct. Add an authoritative exact product/version locator only
    if actually established; otherwise retain the uncertainty. Do not transfer a supplier
    formulation, correct quantities or provide culture-procedure guidance.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000970
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acanthamoeba_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Limit follow-up to accession, supplier/citation identity, exact document/version
    locator and honest provenance wording; no operational or formulation edits under
    this review.
  - Preserve prior history; append an accurate metadata clarification only after a
    separately authorized maintained-input change.
  - After an authorized metadata change, run the four documented target validators
    and applicable merge checks if regeneration is authorized; mechanical passes do
    not certify scientific validity.
limitations:
- The record contains infected-Acanthamoeba host-culture and intracellular-bacteria
  maintenance material. Operational formulation and culture-procedure assessment is
  deliberately excluded under the agreed safety scope.
- This is not a complete scientific assessment. Required operational review is explicitly
  skipped, not implicitly passed. Partial completion does not certify the formulation,
  procedures or performance.
- The reference command inspected0 excerpts; its pass verifies no supplier identity,
  recipe claim or biological assertion. Ontology metadata checks do not assess source
  chemical-form correspondence.
- No corpus, history, source cache, saved review or scientific status was changed.
  No new cultivation advice, formulation correction or experiment is proposed.
tags:
- unreviewed-records
- batch-014
- generated-medium
```
