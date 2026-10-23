# Source and formulation review: a7_medium (CultureMech:007783)

- Review: 20261021T094154Z-culturemech-007783-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:35:26Z
- Finished UTC: 2026-10-21T09:41:54Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M1252 resolves to JCM 1170 A7 medium. The target and maintained owner flatten a mineral stock into direct ingredients, sum calcium across stages, express solvent and stock volumes as g/L, and change resazurin from 1 mg to 1 g. They omit the exact pH 9.0 and collection sterilization instruction. The generated water value also differs from a later owner repair, which itself did not resolve source stages or units. All four documented diagnostics pass.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 133; batch 014 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirteen task batches contain 130 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 132 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007783 | data/merge_yaml/merged/A7_MEDIUM.yaml | generated | a7_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007783 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007783 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch014/133/strict.tsv |
| validate-terms | passed | True | CultureMech:007783 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007783 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007783 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped timestamp syntax and timezone inspection | passed | False | CultureMech:007783 | 24 timestamps inspected, 0 invalid or timezone-naive; old provenance remains unchanged. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007783.

The four documented recipes completed; interpret the scope of each separately.

### TOGO and collection source identity

identity: supported. Targets: CultureMech:007783.

Stable ID, merge basename, maintained owner, TOGO M1252 metadata and exact JCM 1170 title identify A7. MediaDive J1170 corroborates this same recipe; mineral solution 5281 is subordinate source context, not an asserted local stock identifier.

### Primary labels/forms and pinned secondary correspondence

grounding: supported. Targets: CultureMech:007783.

Layer-specific counts are {"target": {"ingredient_instances": 12, "primary_CHEBI_instances": 11, "secondary_current_asserted_instances": 7, "secondary_current_verified_instances": 7, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 91.67, "secondary_verified_percent": 58.33}, "owner": {"ingredient_instances": 12, "primary_CHEBI_instances": 11, "secondary_current_asserted_instances": 7, "secondary_current_verified_instances": 7, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 91.67, "secondary_verified_percent": 58.33}}. Percentages are 0–100 linkage coverage over direct ingredient instances, not scientific accuracy. The 0 legacy link instances across both layers are unverified by the current CHEBI-keyed snapshot; absence here does not prove historical invalidity. Current secondary keys without a live preferred-term row are []. No secondary linked-set percentage is invented for an empty set.

{"label_drift": [], "legacy": [], "missing_current_secondary": []}

### Supplied forms and source role/property prose

grounding: supported. Targets: CultureMech:007783.

Explicit calcium dihydrate, magnesium hexahydrate, ferrous sulfate heptahydrate and L-cysteine hydrochloride monohydrate agree with the asserted ontology forms. CHEBI:91248 has the shorter label hydrate but its definition and formula explicitly specify one water; it is not a hydrate mismatch. Resazurin is not silently substituted with a sodium salt. Cellobiose, phosphates, urea and sodium carbonate preserve source identities. Yeast extract remains an undefined mixture with the named BD-Difco qualifier. TOGO reproduces the listed ingredient role/property prose; this is imported annotation provenance, not a new experiment.

### Exact pH and source sterilization instruction

consistency: concern. Targets: CultureMech:007783.

Both local layers omit pH and preparation. The exact JCM source says Adjust pH to9.0 and its header states autoclaving at 121°C for 15 min unless otherwise stated; no exception is printed. Mineral-stock preparation must remain separate. Temperature, atmosphere and incubation beyond that source preparation instruction are not invented.

### Medium class and source use

scope: supported. Targets: CultureMech:007783.

COMPLEX/UNDEFINED is consistent with the explicitly undefined yeast extract amid named chemicals, and LIQUID agrees with the absence of a gelling component. Bacterial filing and generic microbial cultivation do not imply any particular strain performance.

### Generated water claim versus repaired owner

ownership: concern. Targets: CultureMech:007783.

Target water 2.0 G_PER_L predates owner water 1.0 G_PER_L and the September repair event. The calcium sum, resazurin scale, stock stub and preparation omissions persist in both. Regenerating from the current owner alone would change water but would not repair source units or stock boundaries.

### Append-only history and timestamp interpretation

provenance: supported. Targets: CultureMech:007783.

24 exact timestamp instances were examined; 0 lack valid syntax or explicit timezone. No local timestamp was assumed UTC or rewritten. Process and confidence annotations are not independent scientific evidence.

[]

### Every stored ingredient/stock quantity and source-stage dependency

quantity: concern. Targets: CultureMech:007783.

All 12 direct ingredient claims and the one stock-addition claim are matched to 15 literal source quantity statements including both water stages and all 3 stock components. Arithmetic retains provider-declared stock and receiving-volume assumptions separately from the exact quotations.

[{"field_path": "ingredients[3].concentration", "name": "K2HPO4", "current": {"value": "2.9", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "jcm1170", "source_quote": "K 2 HPO 4 2.9 g", "source_locator": "A7 main recipe row 1", "preparation_stage": "main direct addition", "decision_rationale": "The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-1"}, {"field_path": "ingredients[2].concentration", "name": "KH2PO4", "current": {"value": "1.5", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "jcm1170", "source_quote": "KH 2 PO 4 1.5 g", "source_locator": "A7 main recipe row 2", "preparation_stage": "main direct addition", "decision_rationale": "The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-2"}, {"field_path": "ingredients[8].concentration", "name": "Urea", "current": {"value": "2.1", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "jcm1170", "source_quote": "Urea 2.1 g", "source_locator": "A7 main recipe row 3", "preparation_stage": "main direct addition", "decision_rationale": "The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-3"}, {"field_path": "ingredients[7].concentration", "name": "Yeast extract (BD-Difco)", "current": {"value": "6", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "jcm1170", "source_quote": "Yeast extract (BD-Difco) 6.0 g", "source_locator": "A7 main recipe row 4", "preparation_stage": "main direct addition", "decision_rationale": "The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-4"}, {"field_path": "ingredients[1].concentration", "name": "CaCl2・2H2O", "current": {"value": "37.51", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170", "source_quote": "CaCl 2 ·2H 2 O 0.01 g", "source_locator": "A7 main recipe row 5", "preparation_stage": "main direct addition", "decision_rationale": "Direct calcium is 0.01 g; stored 37.51 g/L sums it with the separate stock 37.5 g. Restore stage boundaries before any concentration calculation.", "evidence_id": "quantity-5"}, {"field_path": "ingredients[5].concentration", "name": "Na2CO3", "current": {"value": "4", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "jcm1170", "source_quote": "Na 2 CO 3 4.0 g", "source_locator": "A7 main recipe row 6", "preparation_stage": "main direct addition", "decision_rationale": "The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-6"}, {"field_path": "ingredients[9].concentration", "name": "L-Cysteine・HCl・H2O", "current": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "jcm1170", "source_quote": "L-Cysteine·HCl·H 2 O 0.5 g", "source_locator": "A7 main recipe row 7", "preparation_stage": "main direct addition", "decision_rationale": "The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-7"}, {"field_path": "ingredients[4].concentration", "name": "Resazurin", "current": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170", "source_quote": "Resazurin 1.0 mg", "source_locator": "A7 main recipe row 8", "preparation_stage": "main direct addition", "decision_rationale": "Primary and TOGO source specify 1 mg; provider g_l=0.001. Stored 1 G_PER_L loses the milligram scale and is 1000-fold the provider-normalized value.", "evidence_id": "quantity-8"}, {"field_path": "ingredients[6].concentration", "name": "Cellobiose", "current": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "jcm1170", "source_quote": "Cellobiose 10.0 g", "source_locator": "A7 main recipe row 9", "preparation_stage": "main direct addition", "decision_rationale": "The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-9"}, {"field_path": "solutions[0].concentration", "name": "Mineral solution", "current": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170", "source_quote": "Mineral solution (see below) 0.2 ml", "source_locator": "A7 main recipe row 10", "preparation_stage": "stock addition", "decision_rationale": "The source dose is 0.2 mL, not 0.2 g/L. The empty composition and Unknown solution name obscure the source-defined mineral preparation; no broken external ID is asserted because the stub has no term ID.", "evidence_id": "quantity-10"}, {"field_path": "ingredients[0].concentration", "name": "Distilled water", "current": {"value": "2.0", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170", "source_quote": "Distilled water 1.0 L", "source_locator": "Main final row", "preparation_stage": "main", "decision_rationale": "Two separately scoped source solvent volumes were numerically merged as 2 G_PER_L. The owner later collapsed this to 1 G_PER_L, but neither is a valid mass representation of either source volume. Preserve each stage separately and avoid an assumed water-density conversion.", "evidence_id": "quantity-11"}, {"field_path": "stock water (unrepresented separately)", "name": "Distilled water", "current": {"value": "2.0", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170", "source_quote": "Distilled water 1.0 L", "source_locator": "Mineral solution final row", "preparation_stage": "mineral stock", "decision_rationale": "Two separately scoped source solvent volumes were numerically merged as 2 G_PER_L. The owner later collapsed this to 1 G_PER_L, but neither is a valid mass representation of either source volume. Preserve each stage separately and avoid an assumed water-density conversion.", "evidence_id": "quantity-12"}, {"field_path": "ingredients[10].concentration", "name": "MgCl2・6H2O", "current": {"value": "25", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170", "source_quote": "MgCl 2 ·6H 2 O 25.0 g", "source_locator": "Mineral solution row 1", "preparation_stage": "mineral stock", "decision_rationale": "This quantity belongs to the stock, whose 0.2 mL aliquot enters the main medium. It is not a direct undiluted medium concentration.", "evidence_id": "quantity-13", "arithmetic_separate_from_quote": "Only on provider-declared 1 L stock and 1 L receiving bases: 25×0.0002=0.005g/L. These conditional calculations are separate from the source quotation and are not asserted replacements into the record."}, {"field_path": "ingredients[1].concentration", "name": "CaCl2・2H2O", "current": {"value": "37.51", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170", "source_quote": "CaCl 2 ·2H 2 O 37.5 g", "source_locator": "Mineral solution row 2", "preparation_stage": "mineral stock", "decision_rationale": "This quantity belongs to the stock, whose 0.2 mL aliquot enters the main medium. It is not a direct undiluted medium concentration.", "evidence_id": "quantity-14", "arithmetic_separate_from_quote": "Only on provider-declared 1 L stock and 1 L receiving bases: 37.5×0.0002=0.0075g/L from stock; with0.01g/L direct calcium,total0.0175g/L. These conditional calculations are separate from the source quotation and are not asserted replacements into the record."}, {"field_path": "ingredients[11].concentration", "name": "FeSO4・7H2O", "current": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170", "source_quote": "FeSO 4 ·7H 2 O 0.3 g", "source_locator": "Mineral solution row 3", "preparation_stage": "mineral stock", "decision_rationale": "This quantity belongs to the stock, whose 0.2 mL aliquot enters the main medium. It is not a direct undiluted medium concentration.", "evidence_id": "quantity-15", "arithmetic_separate_from_quote": "Only on provider-declared 1 L stock and 1 L receiving bases: 0.3×0.0002=0.00006g/L. These conditional calculations are separate from the source quotation and are not asserted replacements into the record."}]

### Claim-level evidence and reference diagnostic coverage

evidence: concern. Targets: CultureMech:007783.

Source citations/notes identify provenance but do not place exact quantity evidence on the local ingredient or stock claims. The reference validator actually checked zero evidence references; its passing result does not authenticate source amounts. This review provides literal snippets and locators for all assessed quantities. Follow-up should attach narrow amount evidence and source metadata without inventing new schema slots.

### Bounded biological claims and absent optional entities

scope: not_applicable. Targets: CultureMech:007783.

Neither reviewed layer asserts organism/strain identifiers, assemblies, DOI/PMID citations, growth outcomes, variants, parent-media relationships or KG-Microbe matches. Catalogue use and generic applications do not establish strain-specific growth or optimal conditions. No organisms or variants are added merely to fill optional slots.

## Findings

### f1: Mineral stock and solvent volumes lose their source stages

major / open / confirmed; issue key: cm007783-mineral-stock-stage-and-unit-collapse.

Stock MgCl2·6H2O 25 g, CaCl2·2H2O 37.5 g and FeSO4·7H2O 0.3 g are represented as direct medium g/L, while calcium is summed with the separate 0.01 g main addition. The 0.2 mL stock dose and source water volumes become g/L. This materially changes the recipe; the stock stub has no composition.

### f2: Resazurin is stored at a thousandfold provider-normalized amount

major / open / confirmed; issue key: cm007783-resazurin-milligram-scale.

JCM 1170 and TOGO specify 1 mg resazurin; exact MediaDive J1170 gives g_l 0.001. Both local layers instead store 1 G_PER_L. This is a source unit-scale loss, independently of the stock reconstruction.

### f3: Exact pH and sterilization instructions are omitted

major / open / confirmed; issue key: cm007783-source-preparation-omitted.

Neither layer records source pH 9.0 or JCM default 121°C for 15 min. Their omission prevents faithful source preparation, particularly when combined with missing stock boundaries. Native P3.5 is normalized to major because a concrete available source protocol is lost, not because a generic sterilization recommendation is desired; P3.4 is the related missing-preparation rule.

### f4: Generated water differs from its later maintained owner

minor / open / confirmed; issue key: cm007783-generated-water-stale-after-owner-repair.

The generated water value 2.0 remains after the owner-only repair to 1.0; both retain G_PER_L. This is a confirmed generated/owner mismatch, not proof that the owner quantity is scientifically correct.

## Recommended Actions And Acceptance Checks

### a1

Restore the source-defined stock and 0.2 mL addition, separate source water contexts and direct calcium, and attach stage-specific evidence. Preserve final-volume limits and avoid inventing a reference ID for the empty stub.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct the maintained resazurin amount/unit using the literal 1 mg source statement and explicit receiving-basis evidence; retain the generic source form and add narrow quantity evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Restore the exact source pH and scoped sterilization instruction, together with separate stock preparation. Add no unstated atmosphere, incubation or storage details.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

After fixing source stages/units in the maintained owner, regenerate and check merge freshness so the assessed correction survives. Do not merely copy the owner 1.0 G_PER_L value into generated data.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/A7_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/A7_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/A7_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch014/133/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch014/133/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/A7_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/A7_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| source-catalog | /private/tmp/culturemech-review-work-batch014/source-preflight-bound/133/source-catalog.json; Complete bound per-record catalog, raw/text/metadata hashes and actual original capture times | context_only | [{"key": "togoM1252", "url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1252", "status": 200, "accessed_at": "2026-10-21T09:27:38.289987Z", "sha256": "2e640fc19cf88ade87d88cf45f9d17390bb81103927456c37a6e8528d56f60b0", "metadata_sha256": "053b1b2288da96adf2c86154b8029803b0f3887529640ff7164ac62e4014e7df", "content_limit": null, "reused_capture_from": null}, {"key": "jcm1170", "url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170", "status": 200, "accessed_at": "2026-10-21T09:27:41.909576Z", "sha256": "169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473", "metadata_sha256": "8659ce8d2cd9153bf048260aa4eb51c96c98332b19ee79d5f4c81ecbb7c3215e", "content_limit": null, "reused_capture_from": null}, {"key": "mediadiveJ1170api", "url": "https://mediadive.dsmz.de/rest/medium/J1170", "status": 200, "accessed_at": "2026-10-21T09:27:37.342050Z", "sha256": "b350cf0402d3cd15f663eda2fc1a592d78657c2a96319b31653031f04b2a18ce", "metadata_sha256": "e1b3baadf9a156bad414725d716b8392b94483730d9e175c95de260ff44a55a0", "content_limit": null, "reused_capture_from": null}, {"key": "chebi131527", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527", "status": 200, "accessed_at": "2026-10-20T07:22:08.349487Z", "sha256": "349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3", "metadata_sha256": "c41119d09143e5f6fc0daade670cc7a5b6548f4d2a67875be803bc60bf870e00", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/128/chebi131527.json"}, {"key": "chebi15377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377", "status": 200, "accessed_at": "2026-10-21T08:17:26.097802Z", "sha256": "de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b", "metadata_sha256": "fe445adf8b97909a9194a7c110c73e7869942b205555a93954317531b9f99891", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/128/chebi15377.json"}, {"key": "chebi16199", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16199", "status": 200, "accessed_at": "2026-10-21T09:27:39.323287Z", "sha256": "5298ca6b7d402b8a6e2091f03adf139a2d777c9614d760976b3953bc88bd862e", "metadata_sha256": "eb4004c154dd3dcd9f9f997f5f59895054624ba37ab49dc5f2005a84044f9f3e", "content_limit": null, "reused_capture_from": null}, {"key": "chebi17057", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057", "status": 200, "accessed_at": "2026-10-21T09:27:39.796651Z", "sha256": "3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06", "metadata_sha256": "8d6c6877b9fb6e8fff0dbb111f4c187c4edb6a6c34ef757d588df42a4b9cef8e", "content_limit": null, "reused_capture_from": null}, {"key": "chebi29377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377", "status": 200, "accessed_at": "2026-10-21T07:31:16.500548Z", "sha256": "21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1", "metadata_sha256": "8608e6858d72ed15b530de6d9530e6c16894d1c77b4293bda918c96d3638bb0e", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi29377.json"}, {"key": "chebi63036", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036", "status": 200, "accessed_at": "2026-10-21T08:17:29.666916Z", "sha256": "48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3", "metadata_sha256": "7e2ba4fce0e5497d8cc182759f23196a207db333e6f86cf42d00cce9f9fdf74b", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi63036.json"}, {"key": "chebi75836", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836", "status": 200, "accessed_at": "2026-10-20T06:55:07.038393Z", "sha256": "14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525", "metadata_sha256": "53b6c7602cac632af1a89696eefaea6c54dc263513bd7075acaf97eb03a2c691", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi75836.json"}, {"key": "chebi86158", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158", "status": 200, "accessed_at": "2026-10-21T08:17:30.011607Z", "sha256": "b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61", "metadata_sha256": "63bf1709f314b8c80be487ef789830053b84018014531540454d6ff21f99ab64", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi86158.json"}, {"key": "chebi86345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345", "status": 200, "accessed_at": "2026-10-21T08:17:30.382026Z", "sha256": "08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133", "metadata_sha256": "71754d7feafd2625264172c5d61d4ba5ea54d52754b6c6f39a1a27b8c97dbda1", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi86345.json"}, {"key": "chebi8806", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806", "status": 200, "accessed_at": "2026-10-21T08:17:30.774007Z", "sha256": "e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5", "metadata_sha256": "de7e292c7dc9c7858e8fbcf4df8d5b2f8d492148c84d2036bf7d700de5fa2130", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi8806.json"}, {"key": "chebi91248", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248", "status": 200, "accessed_at": "2026-10-21T08:42:32.136441Z", "sha256": "7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683", "metadata_sha256": "644bf4bafd29651baa8c7f1d8eeb04bb2c0110f27ede8cf704b2abe256ae21c6", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi91248.json"}] |
| jcm1170 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; header default; complete A7 and Mineral solution sections | supports | Entire exact JCM 1170 source: main recipe, pH 9.0, mineral stock and explicit collection-wide default 121°C for 15 min applying unless otherwise stated. No exception is printed for this recipe. |
| togoM1252 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1252; $.meta; $.components[0:2]; $.comments | supports | Exact M1252 meta links to JCM 1170, preserves separate main and mineral components, pH and ingredient roles/properties. |
| mediadiveJ1170api | https://mediadive.dsmz.de/rest/medium/J1170; $.data.medium; $.data.solutions[0:2] | supports | Exact J1170 provider retains main 5280 and mineral 5281, each declaring1000 mL; resazurin 1 mg and the 0.2 mL dose remain explicit. |
| quantity-1 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; A7 main recipe row 1 | supports | The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred. |
| quantity-2 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; A7 main recipe row 2 | supports | The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred. |
| quantity-3 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; A7 main recipe row 3 | supports | The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred. |
| quantity-4 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; A7 main recipe row 4 | supports | The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred. |
| quantity-5 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; A7 main recipe row 5 | context_only | Direct calcium is 0.01 g; stored 37.51 g/L sums it with the separate stock 37.5 g. Restore stage boundaries before any concentration calculation. |
| quantity-6 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; A7 main recipe row 6 | supports | The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred. |
| quantity-7 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; A7 main recipe row 7 | supports | The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred. |
| quantity-8 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; A7 main recipe row 8 | context_only | Primary and TOGO source specify 1 mg; provider g_l=0.001. Stored 1 G_PER_L loses the milligram scale and is 1000-fold the provider-normalized value. |
| quantity-9 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; A7 main recipe row 9 | supports | The literal main-recipe mass and form are supported. The stored g/L number agrees on the nominal source/provider recipe basis, but ingredient-level amount evidence is absent; measured final receiving volume is not inferred. |
| quantity-10 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; A7 main recipe row 10 | context_only | The source dose is 0.2 mL, not 0.2 g/L. The empty composition and Unknown solution name obscure the source-defined mineral preparation; no broken external ID is asserted because the stub has no term ID. |
| quantity-11 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; Main final row | context_only | Two separately scoped source solvent volumes were numerically merged as 2 G_PER_L. The owner later collapsed this to 1 G_PER_L, but neither is a valid mass representation of either source volume. Preserve each stage separately and avoid an assumed water-density conversion. |
| quantity-12 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; Mineral solution final row | context_only | Two separately scoped source solvent volumes were numerically merged as 2 G_PER_L. The owner later collapsed this to 1 G_PER_L, but neither is a valid mass representation of either source volume. Preserve each stage separately and avoid an assumed water-density conversion. |
| quantity-13 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; Mineral solution row 1 | context_only | This quantity belongs to the stock, whose 0.2 mL aliquot enters the main medium. It is not a direct undiluted medium concentration. |
| quantity-14 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; Mineral solution row 2 | context_only | This quantity belongs to the stock, whose 0.2 mL aliquot enters the main medium. It is not a direct undiluted medium concentration. |
| quantity-15 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170; Mineral solution row 3 | context_only | This quantity belongs to the stock, whose 0.2 mL aliquot enters the main medium. It is not a direct undiluted medium concentration. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0] | supports | CHEBI:15377 resolves to water and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0] | supports | CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0] | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0] | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0] | supports | CHEBI:8806 resolves to Resazurin and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; $._embedded.terms[0] | supports | CHEBI:29377 resolves to sodium carbonate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi17057 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057; $._embedded.terms[0] | supports | CHEBI:17057 resolves to cellobiose and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi16199 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16199; $._embedded.terms[0] | supports | CHEBI:16199 resolves to urea and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; $._embedded.terms[0] | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0] | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0] | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned snapshot; exact MAPPED/preferred_term rows for asserted CHEBI keys and exact legacy-key lookup | supports | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "counts": {"target": {"ingredient_instances": 12, "primary_CHEBI_instances": 11, "secondary_current_asserted_instances": 7, "secondary_current_verified_instances": 7, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 91.67, "secondary_verified_percent": 58.33}, "owner": {"ingredient_instances": 12, "primary_CHEBI_instances": 11, "secondary_current_asserted_instances": 7, "secondary_current_verified_instances": 7, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 91.67, "secondary_verified_percent": 58.33}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[0]", "name": "Distilled water", "primary": {"id": "CHEBI:15377", "label": "water"}, "canonical_label": "water", "label_equal": true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]}, "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "secondary": {"asserted": {"id": "CHEBI:15377", "label": "water"}, "exact_current_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[1]", "name": "CaCl2・2H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O", "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)", "calcium chloride--water (1/2)", "calcium dichloride dihydrate"]}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[2]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}, "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate", "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid, monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid, potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate", "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium phosphate", "Sorensen's potassium phosphate", "potassium dihydrogen phosphate", "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[3]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen phosphate", "label_equal": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433", "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula": ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[4]", "name": "Resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}, "synonyms": ["Resazurin"], "secondary": {"asserted": {"id": "CHEBI:8806", "label": "Resazurin"}, "exact_current_rows": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[5]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "canonical_label": "sodium carbonate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass": ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate", "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary": {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[6]", "name": "Cellobiose", "primary": {"id": "CHEBI:17057", "label": "cellobiose"}, "canonical_label": "cellobiose", "label_equal": true, "definition": ["A glycosylglucose consisting of two glucose units linked via a β(1→4) bond."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1292744", "cas:528-50-7", "drugbank:DB02061", "kegg.compound:C00185", "knapsack:C00001134", "pubmed:19669625", "pubmed:19968554", "wikipedia.en:Cellobiose"], "generalized_empirical_formula": ["C12H22O11"], "has_alternative_id": ["CHEBI:13952", "CHEBI:23061", "CHEBI:28108", "CHEBI:3522"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17057"], "inchi_key_string": ["GUBGYTABKSRVRQ-CUHNMECISA-N"], "inchi_string": ["InChI=1S/C12H22O11/c13-1-3-5(15)6(16)9(19)12(22-3)23-10-4(2-14)21-11(20)8(18)7(10)17/h3-20H,1-2H2/t3-,4-,5-,6+,7-,8-,9-,10-,11?,12+/m1/s1"], "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@H](O[C@H]2[C@H](O)[C@@H](O)C(O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O"], "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1x_1-5][a2122h-1b_1-5]/1-2/a4-b1"]}, "synonyms": ["1-beta-D-Glucopyranosyl-4-D-glucopyranose", "4-(beta-D-glucosido)-D-glucose", "4-O-beta-D-glucopyranosyl-D-glucopyranose", "4-beta-D-glucopyranosyl-D-glucopyranose", "Cellobiose", "D-(+)-cellobiose", "D-celiobiose", "D-cellobiose", "D-glucosyl-beta-(1-4)-D-glucose", "beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose", "beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose", "cellose"], "secondary": {"asserted": {"id": "CHEBI:17057", "label": "cellobiose"}, "exact_current_rows": [{"label": "Cellobiose", "match_type": "preferred_term", "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[7]", "name": "Yeast extract (BD-Difco)"}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[8]", "name": "Urea", "primary": {"id": "CHEBI:16199", "label": "urea"}, "canonical_label": "urea", "label_equal": true, "definition": ["A carbonyl group with two C-bound amine groups. The commercially available fertilizer has an analysis of 46-0-0 (N-P2O5-K2O)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:57-13-6", "drugbank:DB03904", "drugcentral:4264", "ecmdb:ECMDB04172", "gmelin:1378", "hmdb:HMDB0000294", "kegg.compound:C00086", "kegg.drug:D00023", "knapsack:C00007314", "metacyc.compound:UREA", "pdb-ccd:URE", "ppdb:1728", "pubmed:18037357", "pubmed:22770225", "reaxys:635724", "umbbd.compound:c0165", "wikipedia.en:Urea", "ymdb:YMDB00003"], "generalized_empirical_formula": ["CH4N2O"], "has_alternative_id": ["CHEBI:15292", "CHEBI:27218", "CHEBI:46379", "CHEBI:9888"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16199"], "inchi_key_string": ["XSQUKJJJFZCRTK-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/CH4N2O/c2-1(3)4/h(H4,2,3,4)"], "mass": ["60.056"], "monoisotopic_mass": ["60.03236"], "smiles_string": ["NC(N)=O"]}, "synonyms": ["1728", "Carbamide", "E927b", "H2NC(O)NH2", "Harnstoff", "Karbamid", "UREA", "UREA", "Urea", "Urea", "carbamide", "carbonyldiamide", "ur", "urea", "urea", "uree"], "secondary": {"asserted": {"id": "CHEBI:16199", "label": "urea"}, "exact_current_rows": [{"label": "Urea", "match_type": "preferred_term", "identifier": "CHEBI:16199", "preferred_term": "Urea", "ontology_id": "CHEBI:16199", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[9]", "name": "L-Cysteine・HCl・H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}, "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water (1/1)", "L-cysteine hydrochloride--water (1/1)"]}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[10]", "name": "MgCl2・6H2O", "primary": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "canonical_label": "magnesium dichloride hexahydrate", "label_equal": true, "definition": ["A hydrate that is the hexahydrate form of magnesium dichloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969", "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate", "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"]}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[11]", "name": "FeSO4・7H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}, "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[0]", "name": "Distilled water", "primary": {"id": "CHEBI:15377", "label": "water"}, "canonical_label": "water", "label_equal": true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]}, "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "secondary": {"asserted": {"id": "CHEBI:15377", "label": "water"}, "exact_current_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[1]", "name": "CaCl2・2H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O", "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)", "calcium chloride--water (1/2)", "calcium dichloride dihydrate"]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[2]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}, "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate", "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid, monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid, potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate", "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium phosphate", "Sorensen's potassium phosphate", "potassium dihydrogen phosphate", "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[3]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen phosphate", "label_equal": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433", "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula": ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[4]", "name": "Resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}, "synonyms": ["Resazurin"], "secondary": {"asserted": {"id": "CHEBI:8806", "label": "Resazurin"}, "exact_current_rows": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[5]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "canonical_label": "sodium carbonate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass": ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate", "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary": {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[6]", "name": "Cellobiose", "primary": {"id": "CHEBI:17057", "label": "cellobiose"}, "canonical_label": "cellobiose", "label_equal": true, "definition": ["A glycosylglucose consisting of two glucose units linked via a β(1→4) bond."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1292744", "cas:528-50-7", "drugbank:DB02061", "kegg.compound:C00185", "knapsack:C00001134", "pubmed:19669625", "pubmed:19968554", "wikipedia.en:Cellobiose"], "generalized_empirical_formula": ["C12H22O11"], "has_alternative_id": ["CHEBI:13952", "CHEBI:23061", "CHEBI:28108", "CHEBI:3522"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17057"], "inchi_key_string": ["GUBGYTABKSRVRQ-CUHNMECISA-N"], "inchi_string": ["InChI=1S/C12H22O11/c13-1-3-5(15)6(16)9(19)12(22-3)23-10-4(2-14)21-11(20)8(18)7(10)17/h3-20H,1-2H2/t3-,4-,5-,6+,7-,8-,9-,10-,11?,12+/m1/s1"], "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@H](O[C@H]2[C@H](O)[C@@H](O)C(O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O"], "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1x_1-5][a2122h-1b_1-5]/1-2/a4-b1"]}, "synonyms": ["1-beta-D-Glucopyranosyl-4-D-glucopyranose", "4-(beta-D-glucosido)-D-glucose", "4-O-beta-D-glucopyranosyl-D-glucopyranose", "4-beta-D-glucopyranosyl-D-glucopyranose", "Cellobiose", "D-(+)-cellobiose", "D-celiobiose", "D-cellobiose", "D-glucosyl-beta-(1-4)-D-glucose", "beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose", "beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose", "cellose"], "secondary": {"asserted": {"id": "CHEBI:17057", "label": "cellobiose"}, "exact_current_rows": [{"label": "Cellobiose", "match_type": "preferred_term", "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[7]", "name": "Yeast extract (BD-Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[8]", "name": "Urea", "primary": {"id": "CHEBI:16199", "label": "urea"}, "canonical_label": "urea", "label_equal": true, "definition": ["A carbonyl group with two C-bound amine groups. The commercially available fertilizer has an analysis of 46-0-0 (N-P2O5-K2O)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:57-13-6", "drugbank:DB03904", "drugcentral:4264", "ecmdb:ECMDB04172", "gmelin:1378", "hmdb:HMDB0000294", "kegg.compound:C00086", "kegg.drug:D00023", "knapsack:C00007314", "metacyc.compound:UREA", "pdb-ccd:URE", "ppdb:1728", "pubmed:18037357", "pubmed:22770225", "reaxys:635724", "umbbd.compound:c0165", "wikipedia.en:Urea", "ymdb:YMDB00003"], "generalized_empirical_formula": ["CH4N2O"], "has_alternative_id": ["CHEBI:15292", "CHEBI:27218", "CHEBI:46379", "CHEBI:9888"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16199"], "inchi_key_string": ["XSQUKJJJFZCRTK-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/CH4N2O/c2-1(3)4/h(H4,2,3,4)"], "mass": ["60.056"], "monoisotopic_mass": ["60.03236"], "smiles_string": ["NC(N)=O"]}, "synonyms": ["1728", "Carbamide", "E927b", "H2NC(O)NH2", "Harnstoff", "Karbamid", "UREA", "UREA", "Urea", "Urea", "carbamide", "carbonyldiamide", "ur", "urea", "urea", "uree"], "secondary": {"asserted": {"id": "CHEBI:16199", "label": "urea"}, "exact_current_rows": [{"label": "Urea", "match_type": "preferred_term", "identifier": "CHEBI:16199", "preferred_term": "Urea", "ontology_id": "CHEBI:16199", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[9]", "name": "L-Cysteine・HCl・H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}, "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water (1/1)", "L-cysteine hydrochloride--water (1/1)"]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[10]", "name": "MgCl2・6H2O", "primary": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "canonical_label": "magnesium dichloride hexahydrate", "label_equal": true, "definition": ["A hydrate that is the hexahydrate form of magnesium dichloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969", "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate", "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[11]", "name": "FeSO4・7H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}, "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"]}], "legacy": []} |
| importer | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _local_batch_volume_ml; _parse_unit; _extract_ph | context_only | Current importer separates primary/stock sections and uses restricted volume corroboration. It does not prove that old flattened rows are correct. _extract_ph reads outer ph whereas this actual payload provides meta.ph=9.0; no current code was run. |
| migrator | scripts/migrate_solutions_from_ingredients.py; _resolve_solution | context_only | Legacy solution migration can retain an unmatched name as an empty stub and copy its concentration; this does not verify the source dose or stock content. |
| repair | scripts/repair_merged_duplicates.py; repair_record; identical-value repair logic | context_only | Current repair collapses duplicate equal values and leaves unequal summed components unresolved. The owner September event repairs only water 1.0+1.0 to 1.0; it neither re-establishes separate main/stock stages nor changes the G_PER_L unit. |
| history | data/merge_yaml/merged/A7_MEDIUM.yaml; All target/owner history and ingredient curation timestamps | supports | [{"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-27T06:35:54.223556Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-01-28T19:48:35.025492Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[2].timestamp", "value": "2026-03-09T08:04:58.180895+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:29.829902Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:51.428798Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[5].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[6].timestamp", "value": "2026-03-17T06:30:39.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[7].timestamp", "value": "2026-03-17T19:46:09.852717+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[8].timestamp", "value": "2026-05-16T09:03:08.856012+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[9].timestamp", "value": "2026-06-05T07:40:31.767104+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[10].timestamp", "value": "2026-06-10T07:46:47.392256+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[11].timestamp", "value": "2026-08-06T03:05:07.150247+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-27T06:35:54.223556Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-01-28T19:48:35.025492Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[2].timestamp", "value": "2026-03-09T08:04:58.180895+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:29.829902Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:51.428798Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[5].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[6].timestamp", "value": "2026-03-17T06:30:39.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[7].timestamp", "value": "2026-03-17T19:46:09.852717+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[8].timestamp", "value": "2026-05-16T09:03:08.856012+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[9].timestamp", "value": "2026-06-05T07:40:31.767104+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[10].timestamp", "value": "2026-06-10T07:46:47.392256+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path": "curation_history[11].timestamp", "value": "2026-09-02T07:37:43.584161+00:00", "valid_ISO_datetime": true, "timezone_aware": true}] |
| merge | src/culturemech/merge/merger.py; RecipeMerger and merge record construction | context_only | The target is a generated merge with the exact normalized owner declared in the inspection. Merge fingerprints are ingredient-identity sets, not concentration or source-recipe equivalence. Fix maintained inputs and regenerate only with separate authorization. |
| exporter | src/culturemech/export/kgx_export.py; medium_to_ingredient_edge; medium_to_solution_edge; _resolved_ingredient_id; _quantity | context_only | Current export consumes structured ingredient, solution, type and stored-quantity claims and resolves ingredients through the pinned MIM index before fallback. It does not independently recover omitted source stages or prove final-volume basis. No export was run and no resulting edge count is asserted. |

## Limits And Additional Notes

- JCM lists 1 L water separately for the main medium and stock. MediaDive declares each solution volume 1000 mL; conditional calculations use those declared bases, without claiming independently measured final volumes.
- The source gives no atmosphere, incubation temperature, storage or strain-specific growth evidence. No generic anaerobic protocol is inferred from cysteine or resazurin.
- Current writer and repair code is explanatory context, not a replay of historical imports. The later owner water repair is not scientific confirmation of its remaining mass unit.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094154Z-culturemech-007783-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: a7_medium (CultureMech:007783)'
started_at: '2026-10-21T09:35:26Z'
finished_at: '2026-10-21T09:41:54Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: TOGO M1252 resolves to JCM 1170 A7 medium. The target and maintained owner
  flatten a mineral stock into direct ingredients, sum calcium across stages, express
  solvent and stock volumes as g/L, and change resazurin from 1 mg to 1 g. They omit
  the exact pH 9.0 and collection sterilization instruction. The generated water value
  also differs from a later owner repair, which itself did not resolve source stages
  or units. All four documented diagnostics pass.
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
  - path: data/merge_yaml/merged/A7_MEDIUM.yaml
    sha256: 6e5734a2ea404962ee5dd9c18b8d8979e5bc827361b59b550c20a7cf1e8258f7
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
    sha256: 181bb36fb330944600605498086a68535b42b52098a7220265c09bae3cdb5731
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
  - path: scripts/audit_merged_duplicates.py
    sha256: f98dd2c9772d8b2f36659ec5ead5a82ff1d00c283c3357de62c32df408e3c913
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/mediadive_raw_yaml.py
    sha256: 70ba720001705c315f2c5bd40871e08f6f429b6229c78255e6c94dfdcc482432
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
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
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
  selection: Task review 133; batch 014 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirteen task batches
    contain 130 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 132 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007783
targets:
- target_id: CultureMech:007783
  path: data/merge_yaml/merged/A7_MEDIUM.yaml
  label: a7_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/A7_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/A7_MEDIUM.yaml --workers 1
    --out /private/tmp/culturemech-review-work-batch014/133/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch014/133/strict.tsv"
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/A7_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/A7_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007783
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
  - CultureMech:007783
- check_id: scoped-history
  name: Scoped timestamp syntax and timezone inspection
  required: false
  status: passed
  summary: 24 timestamps inspected, 0 invalid or timezone-naive; old provenance remains
    unchanged.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/A7_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T09:41:54Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T09:41:54Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/A7_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:31.617762Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/A7_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch014/133/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:33.652122Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch014/133/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/A7_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:36.073317Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/A7_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:37.619395Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: source-catalog
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch014/source-preflight-bound/133/source-catalog.json
  locator: Complete bound per-record catalog, raw/text/metadata hashes and actual
    original capture times
  accessed_at: '2026-10-21T09:41:54Z'
  support: context_only
  summary: '[{"key": "togoM1252", "url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1252",
    "status": 200, "accessed_at": "2026-10-21T09:27:38.289987Z", "sha256": "2e640fc19cf88ade87d88cf45f9d17390bb81103927456c37a6e8528d56f60b0",
    "metadata_sha256": "053b1b2288da96adf2c86154b8029803b0f3887529640ff7164ac62e4014e7df",
    "content_limit": null, "reused_capture_from": null}, {"key": "jcm1170", "url":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170", "status": 200, "accessed_at":
    "2026-10-21T09:27:41.909576Z", "sha256": "169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473",
    "metadata_sha256": "8659ce8d2cd9153bf048260aa4eb51c96c98332b19ee79d5f4c81ecbb7c3215e",
    "content_limit": null, "reused_capture_from": null}, {"key": "mediadiveJ1170api",
    "url": "https://mediadive.dsmz.de/rest/medium/J1170", "status": 200, "accessed_at":
    "2026-10-21T09:27:37.342050Z", "sha256": "b350cf0402d3cd15f663eda2fc1a592d78657c2a96319b31653031f04b2a18ce",
    "metadata_sha256": "e1b3baadf9a156bad414725d716b8392b94483730d9e175c95de260ff44a55a0",
    "content_limit": null, "reused_capture_from": null}, {"key": "chebi131527", "url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527",
    "status": 200, "accessed_at": "2026-10-20T07:22:08.349487Z", "sha256": "349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3",
    "metadata_sha256": "c41119d09143e5f6fc0daade670cc7a5b6548f4d2a67875be803bc60bf870e00",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/128/chebi131527.json"},
    {"key": "chebi15377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377",
    "status": 200, "accessed_at": "2026-10-21T08:17:26.097802Z", "sha256": "de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b",
    "metadata_sha256": "fe445adf8b97909a9194a7c110c73e7869942b205555a93954317531b9f99891",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/128/chebi15377.json"},
    {"key": "chebi16199", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16199",
    "status": 200, "accessed_at": "2026-10-21T09:27:39.323287Z", "sha256": "5298ca6b7d402b8a6e2091f03adf139a2d777c9614d760976b3953bc88bd862e",
    "metadata_sha256": "eb4004c154dd3dcd9f9f997f5f59895054624ba37ab49dc5f2005a84044f9f3e",
    "content_limit": null, "reused_capture_from": null}, {"key": "chebi17057", "url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057",
    "status": 200, "accessed_at": "2026-10-21T09:27:39.796651Z", "sha256": "3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06",
    "metadata_sha256": "8d6c6877b9fb6e8fff0dbb111f4c187c4edb6a6c34ef757d588df42a4b9cef8e",
    "content_limit": null, "reused_capture_from": null}, {"key": "chebi29377", "url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377",
    "status": 200, "accessed_at": "2026-10-21T07:31:16.500548Z", "sha256": "21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1",
    "metadata_sha256": "8608e6858d72ed15b530de6d9530e6c16894d1c77b4293bda918c96d3638bb0e",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi29377.json"},
    {"key": "chebi63036", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.666916Z", "sha256": "48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3",
    "metadata_sha256": "7e2ba4fce0e5497d8cc182759f23196a207db333e6f86cf42d00cce9f9fdf74b",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi63036.json"},
    {"key": "chebi75836", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836",
    "status": 200, "accessed_at": "2026-10-20T06:55:07.038393Z", "sha256": "14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525",
    "metadata_sha256": "53b6c7602cac632af1a89696eefaea6c54dc263513bd7075acaf97eb03a2c691",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi75836.json"},
    {"key": "chebi86158", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.011607Z", "sha256": "b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61",
    "metadata_sha256": "63bf1709f314b8c80be487ef789830053b84018014531540454d6ff21f99ab64",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi86158.json"},
    {"key": "chebi86345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.382026Z", "sha256": "08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133",
    "metadata_sha256": "71754d7feafd2625264172c5d61d4ba5ea54d52754b6c6f39a1a27b8c97dbda1",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi86345.json"},
    {"key": "chebi8806", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.774007Z", "sha256": "e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5",
    "metadata_sha256": "de7e292c7dc9c7858e8fbcf4df8d5b2f8d492148c84d2036bf7d700de5fa2130",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi8806.json"},
    {"key": "chebi91248", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248",
    "status": 200, "accessed_at": "2026-10-21T08:42:32.136441Z", "sha256": "7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683",
    "metadata_sha256": "644bf4bafd29651baa8c7f1d8eeb04bb2c0110f27ede8cf704b2abe256ae21c6",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi91248.json"}]'
  snapshot_sha256: 33e6e5aa5aa7ea3b31fc869e9ca714abb850f4895e4d088368c4a8595cf74424
- evidence_id: jcm1170
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: header default; complete A7 and Mineral solution sections
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: supports
  summary: 'Entire exact JCM 1170 source: main recipe, pH 9.0, mineral stock and explicit
    collection-wide default 121°C for 15 min applying unless otherwise stated. No
    exception is printed for this recipe.'
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: togoM1252
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1252
  locator: $.meta; $.components[0:2]; $.comments
  accessed_at: '2026-10-21T09:27:38.289987Z'
  support: supports
  summary: Exact M1252 meta links to JCM 1170, preserves separate main and mineral
    components, pH and ingredient roles/properties.
  snapshot_sha256: 2e640fc19cf88ade87d88cf45f9d17390bb81103927456c37a6e8528d56f60b0
- evidence_id: mediadiveJ1170api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1170
  locator: $.data.medium; $.data.solutions[0:2]
  accessed_at: '2026-10-21T09:27:37.342050Z'
  support: supports
  summary: Exact J1170 provider retains main 5280 and mineral 5281, each declaring1000
    mL; resazurin 1 mg and the 0.2 mL dose remain explicit.
  snapshot_sha256: b350cf0402d3cd15f663eda2fc1a592d78657c2a96319b31653031f04b2a18ce
- evidence_id: quantity-1
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: A7 main recipe row 1
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: supports
  summary: The literal main-recipe mass and form are supported. The stored g/L number
    agrees on the nominal source/provider recipe basis, but ingredient-level amount
    evidence is absent; measured final receiving volume is not inferred.
  quote: K 2 HPO 4 2.9 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-2
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: A7 main recipe row 2
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: supports
  summary: The literal main-recipe mass and form are supported. The stored g/L number
    agrees on the nominal source/provider recipe basis, but ingredient-level amount
    evidence is absent; measured final receiving volume is not inferred.
  quote: KH 2 PO 4 1.5 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-3
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: A7 main recipe row 3
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: supports
  summary: The literal main-recipe mass and form are supported. The stored g/L number
    agrees on the nominal source/provider recipe basis, but ingredient-level amount
    evidence is absent; measured final receiving volume is not inferred.
  quote: Urea 2.1 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-4
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: A7 main recipe row 4
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: supports
  summary: The literal main-recipe mass and form are supported. The stored g/L number
    agrees on the nominal source/provider recipe basis, but ingredient-level amount
    evidence is absent; measured final receiving volume is not inferred.
  quote: Yeast extract (BD-Difco) 6.0 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-5
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: A7 main recipe row 5
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: context_only
  summary: Direct calcium is 0.01 g; stored 37.51 g/L sums it with the separate stock
    37.5 g. Restore stage boundaries before any concentration calculation.
  quote: CaCl 2 ·2H 2 O 0.01 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-6
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: A7 main recipe row 6
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: supports
  summary: The literal main-recipe mass and form are supported. The stored g/L number
    agrees on the nominal source/provider recipe basis, but ingredient-level amount
    evidence is absent; measured final receiving volume is not inferred.
  quote: Na 2 CO 3 4.0 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-7
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: A7 main recipe row 7
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: supports
  summary: The literal main-recipe mass and form are supported. The stored g/L number
    agrees on the nominal source/provider recipe basis, but ingredient-level amount
    evidence is absent; measured final receiving volume is not inferred.
  quote: L-Cysteine·HCl·H 2 O 0.5 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-8
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: A7 main recipe row 8
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: context_only
  summary: Primary and TOGO source specify 1 mg; provider g_l=0.001. Stored 1 G_PER_L
    loses the milligram scale and is 1000-fold the provider-normalized value.
  quote: Resazurin 1.0 mg
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-9
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: A7 main recipe row 9
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: supports
  summary: The literal main-recipe mass and form are supported. The stored g/L number
    agrees on the nominal source/provider recipe basis, but ingredient-level amount
    evidence is absent; measured final receiving volume is not inferred.
  quote: Cellobiose 10.0 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-10
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: A7 main recipe row 10
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: context_only
  summary: The source dose is 0.2 mL, not 0.2 g/L. The empty composition and Unknown
    solution name obscure the source-defined mineral preparation; no broken external
    ID is asserted because the stub has no term ID.
  quote: Mineral solution (see below) 0.2 ml
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-11
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: Main final row
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: context_only
  summary: Two separately scoped source solvent volumes were numerically merged as
    2 G_PER_L. The owner later collapsed this to 1 G_PER_L, but neither is a valid
    mass representation of either source volume. Preserve each stage separately and
    avoid an assumed water-density conversion.
  quote: Distilled water 1.0 L
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-12
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: Mineral solution final row
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: context_only
  summary: Two separately scoped source solvent volumes were numerically merged as
    2 G_PER_L. The owner later collapsed this to 1 G_PER_L, but neither is a valid
    mass representation of either source volume. Preserve each stage separately and
    avoid an assumed water-density conversion.
  quote: Distilled water 1.0 L
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-13
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: Mineral solution row 1
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: context_only
  summary: This quantity belongs to the stock, whose 0.2 mL aliquot enters the main
    medium. It is not a direct undiluted medium concentration.
  quote: MgCl 2 ·6H 2 O 25.0 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-14
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: Mineral solution row 2
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: context_only
  summary: This quantity belongs to the stock, whose 0.2 mL aliquot enters the main
    medium. It is not a direct undiluted medium concentration.
  quote: CaCl 2 ·2H 2 O 37.5 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: quantity-15
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1170
  locator: Mineral solution row 3
  accessed_at: '2026-10-21T09:27:41.909576Z'
  support: context_only
  summary: This quantity belongs to the stock, whose 0.2 mL aliquot enters the main
    medium. It is not a direct undiluted medium concentration.
  quote: FeSO 4 ·7H 2 O 0.3 g
  snapshot_sha256: 169de03ce8550b598efdf060b122eb2de804eb09b143f29a30c74222fa56e473
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi29377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:31:16.500548Z'
  support: supports
  summary: CHEBI:29377 resolves to sodium carbonate and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi17057
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T09:27:39.796651Z'
  support: supports
  summary: CHEBI:17057 resolves to cellobiose and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: 3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06
- evidence_id: chebi16199
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16199
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T09:27:39.323287Z'
  support: supports
  summary: CHEBI:16199 resolves to urea and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: 5298ca6b7d402b8a6e2091f03adf139a2d777c9614d760976b3953bc88bd862e
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: CHEBI:91248 resolves to L-cysteine hydrochloride hydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned snapshot; exact MAPPED/preferred_term rows for asserted CHEBI
    keys and exact legacy-key lookup
  accessed_at: '2026-10-21T09:41:54Z'
  support: supports
  summary: '{"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count":
    9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id",
    "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech",
    "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"},
    "counts": {"target": {"ingredient_instances": 12, "primary_CHEBI_instances": 11,
    "secondary_current_asserted_instances": 7, "secondary_current_verified_instances":
    7, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 91.67, "secondary_verified_percent":
    58.33}, "owner": {"ingredient_instances": 12, "primary_CHEBI_instances": 11, "secondary_current_asserted_instances":
    7, "secondary_current_verified_instances": 7, "legacy_secondary_instances": 0,
    "primary_CHEBI_percent": 91.67, "secondary_verified_percent": 58.33}}, "instances":
    [{"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field":
    "ingredients[0]", "name": "Distilled water", "primary": {"id": "CHEBI:15377",
    "label": "water"}, "canonical_label": "water", "label_equal": true, "definition":
    ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to
    two hydrogen atoms"], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7732-18-5", "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001",
    "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"],
    "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743",
    "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292",
    "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"],
    "smiles_string": ["[H]O[H]"]}, "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH",
    "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua",
    "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane",
    "oxidane", "water", "water"], "secondary": {"asserted": {"id": "CHEBI:15377",
    "label": "water"}, "exact_current_rows": [{"label": "Distilled water", "match_type":
    "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water",
    "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field":
    "ingredients[1]", "name": "CaCl2・2H2O", "primary": {"id": "CHEBI:86158", "label":
    "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium
    chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8",
    "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"],
    "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass":
    ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O",
    "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)",
    "calcium chloride--water (1/2)", "calcium dichloride dihydrate"]}, {"layer": "target",
    "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[2]", "name":
    "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"},
    "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition":
    ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014",
    "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"],
    "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"],
    "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]},
    "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate",
    "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid,
    monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid,
    potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate",
    "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium
    phosphate", "Sorensen''s potassium phosphate", "potassium dihydrogen phosphate",
    "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036",
    "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4",
    "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml",
    "field": "ingredients[3]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527",
    "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen
    phosphate", "label_equal": true, "definition": ["A potassium salt that is the
    dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433",
    "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula":
    ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"],
    "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]},
    "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate",
    "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium
    orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4",
    "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium
    monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)",
    "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium
    hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate
    trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium
    hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[4]",
    "name": "Resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label":
    "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula":
    ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string":
    ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]},
    "synonyms": ["Resazurin"], "secondary": {"asserted": {"id": "CHEBI:8806", "label":
    "Resazurin"}, "exact_current_rows": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path":
    "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[5]", "name": "Na2CO3",
    "primary": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "canonical_label":
    "sodium carbonate", "label_equal": true, "definition": [], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula":
    ["CO3.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string":
    ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"],
    "mass": ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate",
    "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary":
    {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows":
    [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[6]",
    "name": "Cellobiose", "primary": {"id": "CHEBI:17057", "label": "cellobiose"},
    "canonical_label": "cellobiose", "label_equal": true, "definition": ["A glycosylglucose
    consisting of two glucose units linked via a β(1→4) bond."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["beilstein:1292744", "cas:528-50-7", "drugbank:DB02061",
    "kegg.compound:C00185", "knapsack:C00001134", "pubmed:19669625", "pubmed:19968554",
    "wikipedia.en:Cellobiose"], "generalized_empirical_formula": ["C12H22O11"], "has_alternative_id":
    ["CHEBI:13952", "CHEBI:23061", "CHEBI:28108", "CHEBI:3522"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17057"], "inchi_key_string": ["GUBGYTABKSRVRQ-CUHNMECISA-N"],
    "inchi_string": ["InChI=1S/C12H22O11/c13-1-3-5(15)6(16)9(19)12(22-3)23-10-4(2-14)21-11(20)8(18)7(10)17/h3-20H,1-2H2/t3-,4-,5-,6+,7-,8-,9-,10-,11?,12+/m1/s1"],
    "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@H](O[C@H]2[C@H](O)[C@@H](O)C(O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O"],
    "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1x_1-5][a2122h-1b_1-5]/1-2/a4-b1"]},
    "synonyms": ["1-beta-D-Glucopyranosyl-4-D-glucopyranose", "4-(beta-D-glucosido)-D-glucose",
    "4-O-beta-D-glucopyranosyl-D-glucopyranose", "4-beta-D-glucopyranosyl-D-glucopyranose",
    "Cellobiose", "D-(+)-cellobiose", "D-celiobiose", "D-cellobiose", "D-glucosyl-beta-(1-4)-D-glucose",
    "beta-D-glucopyranosyl-(1->4)-D-glucopyranose", "beta-D-glucopyranosyl-(1->4)-D-glucopyranose",
    "cellose"], "secondary": {"asserted": {"id": "CHEBI:17057", "label": "cellobiose"},
    "exact_current_rows": [{"label": "Cellobiose", "match_type": "preferred_term",
    "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path":
    "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[7]", "name": "Yeast
    extract (BD-Difco)"}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml",
    "field": "ingredients[8]", "name": "Urea", "primary": {"id": "CHEBI:16199", "label":
    "urea"}, "canonical_label": "urea", "label_equal": true, "definition": ["A carbonyl
    group with two C-bound amine groups. The commercially available fertilizer has
    an analysis of 46-0-0 (N-P2O5-K2O)."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:57-13-6", "drugbank:DB03904", "drugcentral:4264", "ecmdb:ECMDB04172", "gmelin:1378",
    "hmdb:HMDB0000294", "kegg.compound:C00086", "kegg.drug:D00023", "knapsack:C00007314",
    "metacyc.compound:UREA", "pdb-ccd:URE", "ppdb:1728", "pubmed:18037357", "pubmed:22770225",
    "reaxys:635724", "umbbd.compound:c0165", "wikipedia.en:Urea", "ymdb:YMDB00003"],
    "generalized_empirical_formula": ["CH4N2O"], "has_alternative_id": ["CHEBI:15292",
    "CHEBI:27218", "CHEBI:46379", "CHEBI:9888"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:16199"], "inchi_key_string": ["XSQUKJJJFZCRTK-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/CH4N2O/c2-1(3)4/h(H4,2,3,4)"], "mass": ["60.056"], "monoisotopic_mass":
    ["60.03236"], "smiles_string": ["NC(N)=O"]}, "synonyms": ["1728", "Carbamide",
    "E927b", "H2NC(O)NH2", "Harnstoff", "Karbamid", "UREA", "UREA", "Urea", "Urea",
    "carbamide", "carbonyldiamide", "ur", "urea", "urea", "uree"], "secondary": {"asserted":
    {"id": "CHEBI:16199", "label": "urea"}, "exact_current_rows": [{"label": "Urea",
    "match_type": "preferred_term", "identifier": "CHEBI:16199", "preferred_term":
    "Urea", "ontology_id": "CHEBI:16199", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml",
    "field": "ingredients[9]", "name": "L-Cysteine・HCl・H2O", "primary": {"id": "CHEBI:91248",
    "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride
    hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate
    form of <small>L</small>-cysteine hydrochloride."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326",
    "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string":
    ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"],
    "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]},
    "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)",
    "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic
    acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate
    monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water
    (1/1)", "L-cysteine hydrochloride--water (1/1)"]}, {"layer": "target", "path":
    "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[10]", "name": "MgCl2・6H2O",
    "primary": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"},
    "canonical_label": "magnesium dichloride hexahydrate", "label_equal": true, "definition":
    ["A hydrate that is the hexahydrate form of magnesium dichloride."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7791-18-6", "kegg.drug:D04834",
    "pubmed:24831644", "pubmed:25148974", "pubmed:25430969", "reaxys:11343754"], "generalized_empirical_formula":
    ["2Cl.6H2O.Mg"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86345"],
    "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"],
    "mass": ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]},
    "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride
    hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate",
    "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"]}, {"layer":
    "target", "path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field": "ingredients[11]",
    "name": "FeSO4・7H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate
    heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal":
    true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate.
    It is used as a source of iron in the treatment of iron-deficiency anaemia (generally
    in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally
    used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0",
    "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"],
    "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string":
    ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]},
    "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous
    sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol",
    "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O",
    "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"]}, {"layer": "owner",
    "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[0]",
    "name": "Distilled water", "primary": {"id": "CHEBI:15377", "label": "water"},
    "canonical_label": "water", "label_equal": true, "definition": ["An oxygen hydride
    consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"],
    "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5",
    "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001",
    "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"],
    "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743",
    "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292",
    "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"],
    "smiles_string": ["[H]O[H]"]}, "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH",
    "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua",
    "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane",
    "oxidane", "water", "water"], "secondary": {"asserted": {"id": "CHEBI:15377",
    "label": "water"}, "exact_current_rows": [{"label": "Distilled water", "match_type":
    "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water",
    "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field": "ingredients[1]", "name": "CaCl2・2H2O", "primary": {"id": "CHEBI:86158",
    "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium
    chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8",
    "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"],
    "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass":
    ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O",
    "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)",
    "calcium chloride--water (1/2)", "calcium dichloride dihydrate"]}, {"layer": "owner",
    "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[2]",
    "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen
    phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal":
    true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the
    counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0",
    "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"],
    "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"],
    "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]},
    "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate",
    "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid,
    monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid,
    potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate",
    "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium
    phosphate", "Sorensen''s potassium phosphate", "potassium dihydrogen phosphate",
    "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036",
    "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4",
    "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field": "ingredients[3]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527",
    "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen
    phosphate", "label_equal": true, "definition": ["A potassium salt that is the
    dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433",
    "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula":
    ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"],
    "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]},
    "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate",
    "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium
    orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4",
    "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium
    monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)",
    "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium
    hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate
    trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium
    hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field":
    "ingredients[4]", "name": "Resazurin", "primary": {"id": "CHEBI:8806", "label":
    "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition":
    [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3",
    "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]},
    "synonyms": ["Resazurin"], "secondary": {"asserted": {"id": "CHEBI:8806", "label":
    "Resazurin"}, "exact_current_rows": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[5]",
    "name": "Na2CO3", "primary": {"id": "CHEBI:29377", "label": "sodium carbonate"},
    "canonical_label": "sodium carbonate", "label_equal": true, "definition": [],
    "annotations": {"charge": [0.0], "database_cross_reference": ["cas:497-19-8",
    "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"],
    "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass":
    ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate",
    "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary":
    {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows":
    [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field":
    "ingredients[6]", "name": "Cellobiose", "primary": {"id": "CHEBI:17057", "label":
    "cellobiose"}, "canonical_label": "cellobiose", "label_equal": true, "definition":
    ["A glycosylglucose consisting of two glucose units linked via a β(1→4) bond."],
    "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1292744",
    "cas:528-50-7", "drugbank:DB02061", "kegg.compound:C00185", "knapsack:C00001134",
    "pubmed:19669625", "pubmed:19968554", "wikipedia.en:Cellobiose"], "generalized_empirical_formula":
    ["C12H22O11"], "has_alternative_id": ["CHEBI:13952", "CHEBI:23061", "CHEBI:28108",
    "CHEBI:3522"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17057"],
    "inchi_key_string": ["GUBGYTABKSRVRQ-CUHNMECISA-N"], "inchi_string": ["InChI=1S/C12H22O11/c13-1-3-5(15)6(16)9(19)12(22-3)23-10-4(2-14)21-11(20)8(18)7(10)17/h3-20H,1-2H2/t3-,4-,5-,6+,7-,8-,9-,10-,11?,12+/m1/s1"],
    "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@H](O[C@H]2[C@H](O)[C@@H](O)C(O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O"],
    "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1x_1-5][a2122h-1b_1-5]/1-2/a4-b1"]},
    "synonyms": ["1-beta-D-Glucopyranosyl-4-D-glucopyranose", "4-(beta-D-glucosido)-D-glucose",
    "4-O-beta-D-glucopyranosyl-D-glucopyranose", "4-beta-D-glucopyranosyl-D-glucopyranose",
    "Cellobiose", "D-(+)-cellobiose", "D-celiobiose", "D-cellobiose", "D-glucosyl-beta-(1-4)-D-glucose",
    "beta-D-glucopyranosyl-(1->4)-D-glucopyranose", "beta-D-glucopyranosyl-(1->4)-D-glucopyranose",
    "cellose"], "secondary": {"asserted": {"id": "CHEBI:17057", "label": "cellobiose"},
    "exact_current_rows": [{"label": "Cellobiose", "match_type": "preferred_term",
    "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[7]",
    "name": "Yeast extract (BD-Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field": "ingredients[8]", "name": "Urea", "primary": {"id": "CHEBI:16199", "label":
    "urea"}, "canonical_label": "urea", "label_equal": true, "definition": ["A carbonyl
    group with two C-bound amine groups. The commercially available fertilizer has
    an analysis of 46-0-0 (N-P2O5-K2O)."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:57-13-6", "drugbank:DB03904", "drugcentral:4264", "ecmdb:ECMDB04172", "gmelin:1378",
    "hmdb:HMDB0000294", "kegg.compound:C00086", "kegg.drug:D00023", "knapsack:C00007314",
    "metacyc.compound:UREA", "pdb-ccd:URE", "ppdb:1728", "pubmed:18037357", "pubmed:22770225",
    "reaxys:635724", "umbbd.compound:c0165", "wikipedia.en:Urea", "ymdb:YMDB00003"],
    "generalized_empirical_formula": ["CH4N2O"], "has_alternative_id": ["CHEBI:15292",
    "CHEBI:27218", "CHEBI:46379", "CHEBI:9888"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:16199"], "inchi_key_string": ["XSQUKJJJFZCRTK-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/CH4N2O/c2-1(3)4/h(H4,2,3,4)"], "mass": ["60.056"], "monoisotopic_mass":
    ["60.03236"], "smiles_string": ["NC(N)=O"]}, "synonyms": ["1728", "Carbamide",
    "E927b", "H2NC(O)NH2", "Harnstoff", "Karbamid", "UREA", "UREA", "Urea", "Urea",
    "carbamide", "carbonyldiamide", "ur", "urea", "urea", "uree"], "secondary": {"asserted":
    {"id": "CHEBI:16199", "label": "urea"}, "exact_current_rows": [{"label": "Urea",
    "match_type": "preferred_term", "identifier": "CHEBI:16199", "preferred_term":
    "Urea", "ontology_id": "CHEBI:16199", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field": "ingredients[9]", "name": "L-Cysteine・HCl・H2O", "primary": {"id": "CHEBI:91248",
    "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride
    hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate
    form of <small>L</small>-cysteine hydrochloride."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326",
    "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string":
    ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"],
    "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]},
    "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)",
    "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic
    acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate
    monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water
    (1/1)", "L-cysteine hydrochloride--water (1/1)"]}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[10]",
    "name": "MgCl2・6H2O", "primary": {"id": "CHEBI:86345", "label": "magnesium dichloride
    hexahydrate"}, "canonical_label": "magnesium dichloride hexahydrate", "label_equal":
    true, "definition": ["A hydrate that is the hexahydrate form of magnesium dichloride."],
    "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7791-18-6",
    "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969", "reaxys:11343754"],
    "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "monoisotopic_mass":
    ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "synonyms":
    ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride hydrate",
    "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate", "magnesium
    dichloride--water (1/6)", "magnesium dichloride--water (1/6)"]}, {"layer": "owner",
    "path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field": "ingredients[11]",
    "name": "FeSO4・7H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate
    heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal":
    true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate.
    It is used as a source of iron in the treatment of iron-deficiency anaemia (generally
    in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally
    used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0",
    "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"],
    "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string":
    ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]},
    "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous
    sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol",
    "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O",
    "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"]}], "legacy": []}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _local_batch_volume_ml;
    _parse_unit; _extract_ph
  accessed_at: '2026-10-21T09:41:54Z'
  support: context_only
  summary: Current importer separates primary/stock sections and uses restricted volume
    corroboration. It does not prove that old flattened rows are correct. _extract_ph
    reads outer ph whereas this actual payload provides meta.ph=9.0; no current code
    was run.
- evidence_id: migrator
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _resolve_solution
  accessed_at: '2026-10-21T09:41:54Z'
  support: context_only
  summary: Legacy solution migration can retain an unmatched name as an empty stub
    and copy its concentration; this does not verify the source dose or stock content.
- evidence_id: repair
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_record; identical-value repair logic
  accessed_at: '2026-10-21T09:41:54Z'
  support: context_only
  summary: Current repair collapses duplicate equal values and leaves unequal summed
    components unresolved. The owner September event repairs only water 1.0+1.0 to
    1.0; it neither re-establishes separate main/stock stages nor changes the G_PER_L
    unit.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/A7_MEDIUM.yaml
  locator: All target/owner history and ingredient curation timestamps
  accessed_at: '2026-10-21T09:41:54Z'
  support: supports
  summary: '[{"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[0].timestamp",
    "value": "2026-01-27T06:35:54.223556Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[1].timestamp",
    "value": "2026-01-28T19:48:35.025492Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[2].timestamp",
    "value": "2026-03-09T08:04:58.180895+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[3].timestamp",
    "value": "2026-03-13T03:09:29.829902Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[4].timestamp",
    "value": "2026-03-13T06:19:51.428798Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[5].timestamp",
    "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[6].timestamp",
    "value": "2026-03-17T06:30:39.000000Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[7].timestamp",
    "value": "2026-03-17T19:46:09.852717+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[8].timestamp",
    "value": "2026-05-16T09:03:08.856012+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[9].timestamp",
    "value": "2026-06-05T07:40:31.767104+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[10].timestamp",
    "value": "2026-06-10T07:46:47.392256+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/A7_MEDIUM.yaml", "field_path": "curation_history[11].timestamp",
    "value": "2026-08-06T03:05:07.150247+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml", "field_path":
    "curation_history[0].timestamp", "value": "2026-01-27T06:35:54.223556Z", "valid_ISO_datetime":
    true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-01-28T19:48:35.025492Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[2].timestamp", "value": "2026-03-09T08:04:58.180895+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:29.829902Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:51.428798Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[5].timestamp", "value": "2026-03-14T00:00:00+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[6].timestamp", "value": "2026-03-17T06:30:39.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[7].timestamp", "value": "2026-03-17T19:46:09.852717+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[8].timestamp", "value": "2026-05-16T09:03:08.856012+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[9].timestamp", "value": "2026-06-05T07:40:31.767104+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[10].timestamp", "value": "2026-06-10T07:46:47.392256+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml",
    "field_path": "curation_history[11].timestamp", "value": "2026-09-02T07:37:43.584161+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}]'
- evidence_id: merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger and merge record construction
  accessed_at: '2026-10-21T09:41:54Z'
  support: context_only
  summary: The target is a generated merge with the exact normalized owner declared
    in the inspection. Merge fingerprints are ingredient-identity sets, not concentration
    or source-recipe equivalence. Fix maintained inputs and regenerate only with separate
    authorization.
- evidence_id: exporter
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: medium_to_ingredient_edge; medium_to_solution_edge; _resolved_ingredient_id;
    _quantity
  accessed_at: '2026-10-21T09:41:54Z'
  support: context_only
  summary: Current export consumes structured ingredient, solution, type and stored-quantity
    claims and resolves ingredients through the pinned MIM index before fallback.
    It does not independently recover omitted source stages or prove final-volume
    basis. No export was run and no resulting edge count is asserted.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: TOGO and collection source identity
  outcome: supported
  summary: Stable ID, merge basename, maintained owner, TOGO M1252 metadata and exact
    JCM 1170 title identify A7. MediaDive J1170 corroborates this same recipe; mineral
    solution 5281 is subordinate source context, not an asserted local stock identifier.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - record
  - owner-0
  - jcm1170
  - togoM1252
  - mediadiveJ1170api
- assessment_id: grounding
  area: grounding
  topic: Primary labels/forms and pinned secondary correspondence
  outcome: supported
  summary: 'Layer-specific counts are {"target": {"ingredient_instances": 12, "primary_CHEBI_instances":
    11, "secondary_current_asserted_instances": 7, "secondary_current_verified_instances":
    7, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 91.67, "secondary_verified_percent":
    58.33}, "owner": {"ingredient_instances": 12, "primary_CHEBI_instances": 11, "secondary_current_asserted_instances":
    7, "secondary_current_verified_instances": 7, "legacy_secondary_instances": 0,
    "primary_CHEBI_percent": 91.67, "secondary_verified_percent": 58.33}}. Percentages
    are 0–100 linkage coverage over direct ingredient instances, not scientific accuracy.
    The 0 legacy link instances across both layers are unverified by the current CHEBI-keyed
    snapshot; absence here does not prove historical invalidity. Current secondary
    keys without a live preferred-term row are []. No secondary linked-set percentage
    is invented for an empty set.'
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi15377
  - chebi86158
  - chebi63036
  - chebi131527
  - chebi8806
  - chebi29377
  - chebi17057
  - chebi16199
  - chebi91248
  - chebi86345
  - chebi75836
  details: '{"label_drift": [], "legacy": [], "missing_current_secondary": []}'
- assessment_id: forms
  area: grounding
  topic: Supplied forms and source role/property prose
  outcome: supported
  summary: Explicit calcium dihydrate, magnesium hexahydrate, ferrous sulfate heptahydrate
    and L-cysteine hydrochloride monohydrate agree with the asserted ontology forms.
    CHEBI:91248 has the shorter label hydrate but its definition and formula explicitly
    specify one water; it is not a hydrate mismatch. Resazurin is not silently substituted
    with a sodium salt. Cellobiose, phosphates, urea and sodium carbonate preserve
    source identities. Yeast extract remains an undefined mixture with the named BD-Difco
    qualifier. TOGO reproduces the listed ingredient role/property prose; this is
    imported annotation provenance, not a new experiment.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - record
  - owner-0
  - jcm1170
  - togoM1252
  - chebi15377
  - chebi86158
  - chebi63036
  - chebi131527
  - chebi8806
  - chebi29377
  - chebi17057
  - chebi16199
  - chebi91248
  - chebi86345
  - chebi75836
- assessment_id: preparation
  area: consistency
  topic: Exact pH and source sterilization instruction
  outcome: concern
  summary: Both local layers omit pH and preparation. The exact JCM source says Adjust
    pH to9.0 and its header states autoclaving at 121°C for 15 min unless otherwise
    stated; no exception is printed. Mineral-stock preparation must remain separate.
    Temperature, atmosphere and incubation beyond that source preparation instruction
    are not invented.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - record
  - owner-0
  - jcm1170
  - togoM1252
  - importer
- assessment_id: classification
  area: scope
  topic: Medium class and source use
  outcome: supported
  summary: COMPLEX/UNDEFINED is consistent with the explicitly undefined yeast extract
    amid named chemicals, and LIQUID agrees with the absence of a gelling component.
    Bacterial filing and generic microbial cultivation do not imply any particular
    strain performance.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - record
  - owner-0
  - jcm1170
  - togoM1252
- assessment_id: ownership
  area: ownership
  topic: Generated water claim versus repaired owner
  outcome: concern
  summary: Target water 2.0 G_PER_L predates owner water 1.0 G_PER_L and the September
    repair event. The calcium sum, resazurin scale, stock stub and preparation omissions
    persist in both. Regenerating from the current owner alone would change water
    but would not repair source units or stock boundaries.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - record
  - owner-0
  - repair
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp interpretation
  outcome: supported
  summary: 24 exact timestamp instances were examined; 0 lack valid syntax or explicit
    timezone. No local timestamp was assumed UTC or rewritten. Process and confidence
    annotations are not independent scientific evidence.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - record
  - owner-0
  - history
  details: '[]'
- assessment_id: quantities
  area: quantity
  topic: Every stored ingredient/stock quantity and source-stage dependency
  outcome: concern
  summary: All 12 direct ingredient claims and the one stock-addition claim are matched
    to 15 literal source quantity statements including both water stages and all 3
    stock components. Arithmetic retains provider-declared stock and receiving-volume
    assumptions separately from the exact quotations.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - record
  - owner-0
  - quantity-1
  - quantity-2
  - quantity-3
  - quantity-4
  - quantity-5
  - quantity-6
  - quantity-7
  - quantity-8
  - quantity-9
  - quantity-10
  - quantity-11
  - quantity-12
  - quantity-13
  - quantity-14
  - quantity-15
  details: '[{"field_path": "ingredients[3].concentration", "name": "K2HPO4", "current":
    {"value": "2.9", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key":
    "jcm1170", "source_quote": "K 2 HPO 4 2.9 g", "source_locator": "A7 main recipe
    row 1", "preparation_stage": "main direct addition", "decision_rationale": "The
    literal main-recipe mass and form are supported. The stored g/L number agrees
    on the nominal source/provider recipe basis, but ingredient-level amount evidence
    is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-1"},
    {"field_path": "ingredients[2].concentration", "name": "KH2PO4", "current": {"value":
    "1.5", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "jcm1170",
    "source_quote": "KH 2 PO 4 1.5 g", "source_locator": "A7 main recipe row 2", "preparation_stage":
    "main direct addition", "decision_rationale": "The literal main-recipe mass and
    form are supported. The stored g/L number agrees on the nominal source/provider
    recipe basis, but ingredient-level amount evidence is absent; measured final receiving
    volume is not inferred.", "evidence_id": "quantity-2"}, {"field_path": "ingredients[8].concentration",
    "name": "Urea", "current": {"value": "2.1", "unit": "G_PER_L"}, "decision": "evidence_only",
    "source_key": "jcm1170", "source_quote": "Urea 2.1 g", "source_locator": "A7 main
    recipe row 3", "preparation_stage": "main direct addition", "decision_rationale":
    "The literal main-recipe mass and form are supported. The stored g/L number agrees
    on the nominal source/provider recipe basis, but ingredient-level amount evidence
    is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-3"},
    {"field_path": "ingredients[7].concentration", "name": "Yeast extract (BD-Difco)",
    "current": {"value": "6", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key":
    "jcm1170", "source_quote": "Yeast extract (BD-Difco) 6.0 g", "source_locator":
    "A7 main recipe row 4", "preparation_stage": "main direct addition", "decision_rationale":
    "The literal main-recipe mass and form are supported. The stored g/L number agrees
    on the nominal source/provider recipe basis, but ingredient-level amount evidence
    is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-4"},
    {"field_path": "ingredients[1].concentration", "name": "CaCl2・2H2O", "current":
    {"value": "37.51", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170",
    "source_quote": "CaCl 2 ·2H 2 O 0.01 g", "source_locator": "A7 main recipe row
    5", "preparation_stage": "main direct addition", "decision_rationale": "Direct
    calcium is 0.01 g; stored 37.51 g/L sums it with the separate stock 37.5 g. Restore
    stage boundaries before any concentration calculation.", "evidence_id": "quantity-5"},
    {"field_path": "ingredients[5].concentration", "name": "Na2CO3", "current": {"value":
    "4", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "jcm1170",
    "source_quote": "Na 2 CO 3 4.0 g", "source_locator": "A7 main recipe row 6", "preparation_stage":
    "main direct addition", "decision_rationale": "The literal main-recipe mass and
    form are supported. The stored g/L number agrees on the nominal source/provider
    recipe basis, but ingredient-level amount evidence is absent; measured final receiving
    volume is not inferred.", "evidence_id": "quantity-6"}, {"field_path": "ingredients[9].concentration",
    "name": "L-Cysteine・HCl・H2O", "current": {"value": "0.5", "unit": "G_PER_L"},
    "decision": "evidence_only", "source_key": "jcm1170", "source_quote": "L-Cysteine·HCl·H
    2 O 0.5 g", "source_locator": "A7 main recipe row 7", "preparation_stage": "main
    direct addition", "decision_rationale": "The literal main-recipe mass and form
    are supported. The stored g/L number agrees on the nominal source/provider recipe
    basis, but ingredient-level amount evidence is absent; measured final receiving
    volume is not inferred.", "evidence_id": "quantity-7"}, {"field_path": "ingredients[4].concentration",
    "name": "Resazurin", "current": {"value": "1", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "jcm1170", "source_quote": "Resazurin 1.0 mg", "source_locator":
    "A7 main recipe row 8", "preparation_stage": "main direct addition", "decision_rationale":
    "Primary and TOGO source specify 1 mg; provider g_l=0.001. Stored 1 G_PER_L loses
    the milligram scale and is 1000-fold the provider-normalized value.", "evidence_id":
    "quantity-8"}, {"field_path": "ingredients[6].concentration", "name": "Cellobiose",
    "current": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key":
    "jcm1170", "source_quote": "Cellobiose 10.0 g", "source_locator": "A7 main recipe
    row 9", "preparation_stage": "main direct addition", "decision_rationale": "The
    literal main-recipe mass and form are supported. The stored g/L number agrees
    on the nominal source/provider recipe basis, but ingredient-level amount evidence
    is absent; measured final receiving volume is not inferred.", "evidence_id": "quantity-9"},
    {"field_path": "solutions[0].concentration", "name": "Mineral solution", "current":
    {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170",
    "source_quote": "Mineral solution (see below) 0.2 ml", "source_locator": "A7 main
    recipe row 10", "preparation_stage": "stock addition", "decision_rationale": "The
    source dose is 0.2 mL, not 0.2 g/L. The empty composition and Unknown solution
    name obscure the source-defined mineral preparation; no broken external ID is
    asserted because the stub has no term ID.", "evidence_id": "quantity-10"}, {"field_path":
    "ingredients[0].concentration", "name": "Distilled water", "current": {"value":
    "2.0", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170", "source_quote":
    "Distilled water 1.0 L", "source_locator": "Main final row", "preparation_stage":
    "main", "decision_rationale": "Two separately scoped source solvent volumes were
    numerically merged as 2 G_PER_L. The owner later collapsed this to 1 G_PER_L,
    but neither is a valid mass representation of either source volume. Preserve each
    stage separately and avoid an assumed water-density conversion.", "evidence_id":
    "quantity-11"}, {"field_path": "stock water (unrepresented separately)", "name":
    "Distilled water", "current": {"value": "2.0", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "jcm1170", "source_quote": "Distilled water 1.0 L", "source_locator":
    "Mineral solution final row", "preparation_stage": "mineral stock", "decision_rationale":
    "Two separately scoped source solvent volumes were numerically merged as 2 G_PER_L.
    The owner later collapsed this to 1 G_PER_L, but neither is a valid mass representation
    of either source volume. Preserve each stage separately and avoid an assumed water-density
    conversion.", "evidence_id": "quantity-12"}, {"field_path": "ingredients[10].concentration",
    "name": "MgCl2・6H2O", "current": {"value": "25", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "jcm1170", "source_quote": "MgCl 2 ·6H 2 O 25.0 g", "source_locator":
    "Mineral solution row 1", "preparation_stage": "mineral stock", "decision_rationale":
    "This quantity belongs to the stock, whose 0.2 mL aliquot enters the main medium.
    It is not a direct undiluted medium concentration.", "evidence_id": "quantity-13",
    "arithmetic_separate_from_quote": "Only on provider-declared 1 L stock and 1 L
    receiving bases: 25×0.0002=0.005g/L. These conditional calculations are separate
    from the source quotation and are not asserted replacements into the record."},
    {"field_path": "ingredients[1].concentration", "name": "CaCl2・2H2O", "current":
    {"value": "37.51", "unit": "G_PER_L"}, "decision": "correct", "source_key": "jcm1170",
    "source_quote": "CaCl 2 ·2H 2 O 37.5 g", "source_locator": "Mineral solution row
    2", "preparation_stage": "mineral stock", "decision_rationale": "This quantity
    belongs to the stock, whose 0.2 mL aliquot enters the main medium. It is not a
    direct undiluted medium concentration.", "evidence_id": "quantity-14", "arithmetic_separate_from_quote":
    "Only on provider-declared 1 L stock and 1 L receiving bases: 37.5×0.0002=0.0075g/L
    from stock; with0.01g/L direct calcium,total0.0175g/L. These conditional calculations
    are separate from the source quotation and are not asserted replacements into
    the record."}, {"field_path": "ingredients[11].concentration", "name": "FeSO4・7H2O",
    "current": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "source_key":
    "jcm1170", "source_quote": "FeSO 4 ·7H 2 O 0.3 g", "source_locator": "Mineral
    solution row 3", "preparation_stage": "mineral stock", "decision_rationale": "This
    quantity belongs to the stock, whose 0.2 mL aliquot enters the main medium. It
    is not a direct undiluted medium concentration.", "evidence_id": "quantity-15",
    "arithmetic_separate_from_quote": "Only on provider-declared 1 L stock and 1 L
    receiving bases: 0.3×0.0002=0.00006g/L. These conditional calculations are separate
    from the source quotation and are not asserted replacements into the record."}]'
- assessment_id: evidence
  area: evidence
  topic: Claim-level evidence and reference diagnostic coverage
  outcome: concern
  summary: Source citations/notes identify provenance but do not place exact quantity
    evidence on the local ingredient or stock claims. The reference validator actually
    checked zero evidence references; its passing result does not authenticate source
    amounts. This review provides literal snippets and locators for all assessed quantities.
    Follow-up should attach narrow amount evidence and source metadata without inventing
    new schema slots.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - source-catalog
- assessment_id: organisms
  area: scope
  topic: Bounded biological claims and absent optional entities
  outcome: not_applicable
  summary: Neither reviewed layer asserts organism/strain identifiers, assemblies,
    DOI/PMID citations, growth outcomes, variants, parent-media relationships or KG-Microbe
    matches. Catalogue use and generic applications do not establish strain-specific
    growth or optimal conditions. No organisms or variants are added merely to fill
    optional slots.
  target_ids:
  - CultureMech:007783
  evidence_ids:
  - record
  - owner-0
findings:
- finding_id: f1
  issue_key: cm007783-mineral-stock-stage-and-unit-collapse
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Mineral stock and solvent volumes lose their source stages
  description: Stock MgCl2·6H2O 25 g, CaCl2·2H2O 37.5 g and FeSO4·7H2O 0.3 g are represented
    as direct medium g/L, while calcium is summed with the separate 0.01 g main addition.
    The 0.2 mL stock dose and source water volumes become g/L. This materially changes
    the recipe; the stock stub has no composition.
  target_ids:
  - CultureMech:007783
  field_paths:
  - ingredients[0:2].concentration
  - ingredients[10:12].concentration
  - solutions[0]
  evidence_ids:
  - record
  - owner-0
  - jcm1170
  - togoM1252
  - mediadiveJ1170api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm007783-resazurin-milligram-scale
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Resazurin is stored at a thousandfold provider-normalized amount
  description: JCM 1170 and TOGO specify 1 mg resazurin; exact MediaDive J1170 gives
    g_l 0.001. Both local layers instead store 1 G_PER_L. This is a source unit-scale
    loss, independently of the stock reconstruction.
  target_ids:
  - CultureMech:007783
  field_paths:
  - ingredients[4].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm1170
  - togoM1252
  - mediadiveJ1170api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: cm007783-source-preparation-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Exact pH and sterilization instructions are omitted
  description: Neither layer records source pH 9.0 or JCM default 121°C for 15 min.
    Their omission prevents faithful source preparation, particularly when combined
    with missing stock boundaries. Native P3.5 is normalized to major because a concrete
    available source protocol is lost, not because a generic sterilization recommendation
    is desired; P3.4 is the related missing-preparation rule.
  target_ids:
  - CultureMech:007783
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm1170
  - togoM1252
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3.5 normalized to major because the exact available 121°C/15
    min source preparation is omitted, impairing reproducibility; P3.4 describes the
    related missing preparation. No generic unsourced protocol is proposed.
- finding_id: f4
  issue_key: cm007783-generated-water-stale-after-owner-repair
  category: ownership
  severity: minor
  status: open
  certainty: confirmed
  title: Generated water differs from its later maintained owner
  description: The generated water value 2.0 remains after the owner-only repair to
    1.0; both retain G_PER_L. This is a confirmed generated/owner mismatch, not proof
    that the owner quantity is scientifically correct.
  target_ids:
  - CultureMech:007783
  field_paths:
  - ingredients[0].concentration
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - repair
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Restore the source-defined stock and 0.2 mL addition, separate source
    water contexts and direct calcium, and attach stage-specific evidence. Preserve
    final-volume limits and avoid inventing a reference ID for the empty stub.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007783
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
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
  description: Correct the maintained resazurin amount/unit using the literal 1 mg
    source statement and explicit receiving-basis evidence; retain the generic source
    form and add narrow quantity evidence.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007783
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
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
- action_id: a3
  description: Restore the exact source pH and scoped sterilization instruction, together
    with separate stock preparation. Add no unstated atmosphere, incubation or storage
    details.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007783
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
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
  description: After fixing source stages/units in the maintained owner, regenerate
    and check merge freshness so the assessed correction survives. Do not merely copy
    the owner 1.0 G_PER_L value into generated data.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007783
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1252_A7_Medium.yaml
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
- JCM lists 1 L water separately for the main medium and stock. MediaDive declares
  each solution volume 1000 mL; conditional calculations use those declared bases,
  without claiming independently measured final volumes.
- The source gives no atmosphere, incubation temperature, storage or strain-specific
  growth evidence. No generic anaerobic protocol is inferred from cysteine or resazurin.
- Current writer and repair code is explanatory context, not a replay of historical
  imports. The later owner water repair is not scientific confirmation of its remaining
  mass unit.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-014
- generated-medium
```
