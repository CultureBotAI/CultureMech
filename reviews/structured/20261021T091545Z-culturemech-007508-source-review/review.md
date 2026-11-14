# Source and formulation review: 960 (CultureMech:007508)

- Review: 20261021T091545Z-culturemech-007508-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:12:05Z
- Finished UTC: 2026-10-21T09:15:45Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact source is NBRC 959 medium-H despite the generated name 960. The target has two unusable collapsed ingredient rows and generic preparation that substitutes distilled water for source seawater and adds unsupported autoclaving. The maintained owner has all five source rows and the correct source reference, but four labels differ from canonical labels and optional agar has not been reconciled with unconditional SOLID_AGAR. All four canonical diagnostics pass; direct source comparison establishes these semantic defects.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 123; batch 013 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twelve task batches contain 120 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 122 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007508 | data/merge_yaml/merged/960.yaml | generated | 960 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007508 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007508 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/123/strict.tsv |
| validate-terms | passed | True | CultureMech:007508 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007508 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007508 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped history timestamp syntax and timezone check | passed | False | CultureMech:007508 | 14 timestamp instances inspected; 0 malformed or timezone-naive instances. Existing provenance is preserved; no timestamps were rewritten. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007508.

The four documented recipes completed; interpret the scope of each separately.

### NBRC 959 provenance despite local 960 label

identity: supported. Targets: CultureMech:007508.

The stable CultureMech ID, merge source basename, import-history accession 959, maintained owner source term and captured primary page resolve one medium. The local name 960 does not license substitution of actual NBRC 960; that different source is only an identity countercheck. The legacy HTTP import URL was read as provenance, not represented as a newly retrieved response.

### Every target row and every recovered source amount

quantity: concern. Targets: CultureMech:007508.

The target has two malformed direct ingredient rows: one collapsed table at VARIABLE and an empty name with 'Glucose' as its g/L value. The 5 separate owner rows preserve the inspected source amounts and units as itemized. Solid masses expressed by the owner per liter are interpreted on the nominal listed recipe basis, without claiming that a source water amount establishes measured final volume.

{"recovered_source_amounts": [{"owner_field": "ingredients[0].concentration", "name": "Glucose", "owner_value": "2", "owner_unit": "G_PER_L", "source_amount": "2", "source_unit": "g", "source_quote": "Glucose 2 g", "source_locator": "Medium Composition quantified row 1", "condition": "Generic glucose; no stereochemistry or hydrate inferred.", "decision": "evidence_only", "decision_rationale": "Literal source amount is supported; ingredient-level evidence is absent from the owner. Source masses use the nominal listed recipe basis, not independently measured final volume.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-1"}, {"owner_field": "ingredients[1].concentration", "name": "Yeast extract", "owner_value": "0.2", "owner_unit": "G_PER_L", "source_amount": "0.2", "source_unit": "g", "source_quote": "Yeast extract 0.2 g", "source_locator": "Medium Composition quantified row 2", "condition": "Complex extract; literal mass rather than a molecular concentration.", "decision": "evidence_only", "decision_rationale": "Literal source amount is supported; ingredient-level evidence is absent from the owner. Source masses use the nominal listed recipe basis, not independently measured final volume.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-2"}, {"owner_field": "ingredients[2].concentration", "name": "Monosodium glutamate", "owner_value": "0.5", "owner_unit": "G_PER_L", "source_amount": "0.5", "source_unit": "g", "source_quote": "Monosodium glutamate 0.5 g", "source_locator": "Medium Composition quantified row 3", "condition": "Generic monosodium salt; source does not specify stereochemistry.", "decision": "evidence_only", "decision_rationale": "Literal source amount is supported; ingredient-level evidence is absent from the owner. Source masses use the nominal listed recipe basis, not independently measured final volume.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-3"}, {"owner_field": "ingredients[3].concentration", "name": "Agar (if needed)", "owner_value": "12", "owner_unit": "G_PER_L", "source_amount": "12", "source_unit": "g", "source_quote": "Agar (if needed) 12 g", "source_locator": "Medium Composition quantified row 4", "condition": "Conditional solidification branch.", "decision": "evidence_only", "decision_rationale": "Literal source amount is supported; ingredient-level evidence is absent from the owner. Source masses use the nominal listed recipe basis, not independently measured final volume.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-4"}, {"owner_field": "ingredients[4].concentration", "name": "Seawater", "owner_value": "1", "owner_unit": "L", "source_amount": "1", "source_unit": "L", "source_quote": "Seawater 1 L", "source_locator": "Medium Composition quantified row 5", "condition": "Literal natural seawater volume, not distilled water and not a water-density conversion.", "decision": "evidence_only", "decision_rationale": "Literal liquid amount is supported but lacks ingredient-level source evidence; no mass conversion is asserted.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-5"}], "target_malformed_claims": [{"field_path": "ingredients[0].concentration", "current": {"value": "variable", "unit": "VARIABLE"}, "decision": "unsupported", "source_quote": "Glucose 2 g", "source_locator": "Medium Composition quantified row 1", "evidence_ids": ["nbrc959", "amount-1"], "rationale": "A collapsed multi-ingredient string or empty ingredient cannot be assigned one source concentration. Recover all explicit source rows rather than treating this malformed claim as a number."}, {"field_path": "ingredients[1].concentration", "current": {"value": "Glucose", "unit": "G_PER_L"}, "decision": "unsupported", "source_quote": "Glucose 2 g", "source_locator": "Medium Composition quantified row 1", "evidence_ids": ["nbrc959", "amount-1"], "rationale": "A collapsed multi-ingredient string or empty ingredient cannot be assigned one source concentration. Recover all explicit source rows rather than treating this malformed claim as a number."}]}

### All asserted primary IDs, canonical labels and current secondary keys

grounding: concern. Targets: CultureMech:007508.

The generated target has 0/2 primary ontology links and 0/2 verified secondary links. The owner has 5/5 primary ontology links, including 3 CHEBI instances, and 0/5 verified secondary links. 4 owner primary labels differ from canonical labels. These are separate layer-specific linkage denominators on a 0–100 scale, not scientific accuracy scores. No secondary denominator of zero is invented when no keys are asserted.

{"counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances": 0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent": 0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 5, "primary_ontology_instances": 5, "primary_CHEBI_instances": 3, "canonical_primary_label_instances": 1, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 100.0, "primary_CHEBI_percent": 60.0, "secondary_verified_percent": 0.0}}, "label_drift": [{"field_path": "ingredients[1].term.label", "id": "FOODON:03315426", "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "source_key": "foodon03315426"}, {"field_path": "ingredients[2].term.label", "id": "CHEBI:64220", "asserted_label": "Na glutamate", "canonical_label": "monosodium glutamate", "source_key": "chebi64220"}, {"field_path": "ingredients[3].term.label", "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "source_key": "chebi2509"}, {"field_path": "ingredients[4].term.label", "id": "ENVO:00002149", "asserted_label": "Seawater", "canonical_label": "sea water", "source_key": "envo00002149"}], "instances": [{"layer": "target", "path": "data/merge_yaml/merged/960.yaml", "field": "ingredients[0]", "preferred_term": "Glucose2gYeast extract0.2gMonosodium glutamate0.5gAgar (if needed)12gSeawater1L"}, {"layer": "target", "path": "data/merge_yaml/merged/960.yaml", "field": "ingredients[1]", "preferred_term": ""}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "ingredients[0]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234", "asserted_label": "glucose", "canonical_label": "glucose", "label_equal": true, "source_key": "chebi17234", "description": ["An aldohexose used as a source of energy and metabolic intermediate."], "synonyms": ["DL-glucose", "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose", "glucose"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:50-99-7", "kegg.compound:C00293", "wikipedia.en:Glucose"], "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:14313", "CHEBI:24277", "CHEBI:33929", "CHEBI:5418"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17234"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "ingredients[1]", "preferred_term": "Yeast extract", "primary_id": "FOODON:03315426", "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "label_equal": false, "source_key": "foodon03315426", "description": ["SIREN DB annotation:\n* not heat-treated FOODON:03440003\n* part of algae or fungus FOODON:03420247"], "synonyms": [], "form_annotations": {"database_cross_reference": ["https://bioregistry.io/reference/siren:F15426"], "has curation status": ["http://purl.obolibrary.org/obo/IAO_0000428"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "ingredients[2]", "preferred_term": "Monosodium glutamate", "primary_id": "CHEBI:64220", "asserted_label": "Na glutamate", "canonical_label": "monosodium glutamate", "label_equal": false, "source_key": "chebi64220", "description": ["An organic sodium salt that is the monosodium salt of glutamic acid."], "synonyms": ["MSG", "sodium 2-ammoniopentanedioate", "sodium 2-azaniumylpentanedioate", "sodium 2-azaniumylpentanedioate", "sodium glutamate"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["pubmed:22293291", "reaxys:17003240"], "generalized_empirical_formula": ["C5H8NO4.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:64220"], "inchi_key_string": ["LPUQAYUQRXPFSQ-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C5H9NO4.Na/c6-3(5(9)10)1-2-4(7)8;/h3H,1-2,6H2,(H,7,8)(H,9,10);/q;+1/p-1"], "mass": ["169.112"], "monoisotopic_mass": ["169.0351"], "smiles_string": ["[NH3+]C(CCC(=O)[O-])C(=O)[O-].[Na+]"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "ingredients[3]", "preferred_term": "Agar (if needed)", "primary_id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "label_equal": false, "source_key": "chebi2509", "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "synonyms": [], "form_annotations": {"database_cross_reference": ["cas:9002-18-0", "kegg.compound:C08815", "pubmed:25603143", "pubmed:25842535", "pubmed:25959629", "pubmed:26043937", "pubmed:26050892", "pubmed:26116384", "reaxys:8538728", "wikipedia.en:Agar"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:2509"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "ingredients[4]", "preferred_term": "Seawater", "primary_id": "ENVO:00002149", "asserted_label": "Seawater", "canonical_label": "sea water", "label_equal": false, "source_key": "envo00002149", "description": ["This definition refers to water that is actually in a sea or ocean. This water may have a wide range of salinity levels.", "Water which has physicochemical properties that have been determined by the processes occuring in a sea or ocean."], "synonyms": ["ocean water", "seawater"], "form_annotations": {"database_cross_reference": ["EcoLexicon:sea_water", "LTER:701", "SWEETRealm:SeaWater", "https://en.wikipedia.org/wiki/Sea_water"], "editor note": ["When we have more classes representing the various processes which make seawater seawater, we can further axiomatise this class."]}}]}

### Source ingredient identities, mixtures and exact chemical forms

grounding: supported. Targets: CultureMech:007508.

Primary IDs denote generic glucose, yeast extract, monosodium glutamate, agar and sea water. CHEBI:64220 has no explicit stereochemical layer in its captured structural annotation, consistent with the generic source wording. ENVO:00002149 has canonical sea water and synonym seawater. Four owner labels differ literally from canonical labels, but these differences do not by themselves prove wrong IDs. No seawater salt profile or reagent-specific molecular conversion is invented.

### Preparation, pH and physical-state conditions

consistency: concern. Targets: CultureMech:007508.

The source specifies seawater. The target instructs dissolving in distilled water and adds generic pH adjustment and autoclaving, with the latter tagged DISSOLVE. The owner has an empty preparation list and correctly preserves seawater. Absence of a source protocol is not permission to invent one. Optional agar remains conditional.

### Classification and bounded biological claims

scope: concern. Targets: CultureMech:007508.

COMPLEX/UNDEFINED agrees with yeast extract and seawater. Both layers assert SOLID_AGAR despite the source and owner retaining Agar (if needed); the record does not document branch selection. Preserve that condition rather than implying every preparation is solid. Neither target nor owner asserts organisms, strains, taxon IDs, assemblies, DOI/PMID papers, growth outcomes, parent media or variants. Source catalogue scope is not experimental growth evidence. Optional omissions are not populated with invented organisms.

### Maintained recovery versus generated representation

ownership: concern. Targets: CultureMech:007508.

The generated August merge precedes later owner recovery and source metadata. The owner now contains 5 explicit source rows and an official source term/reference; the target retains two collapsed rows and no structured source term/reference. Owner label differences must be corrected before regeneration.

### Claim-level amount evidence and checked reference scope

evidence: concern. Targets: CultureMech:007508.

Each source amount is traced to an exact table row above. The owner has the official recipe reference but lacks ingredient-level amount evidence; the target has no structured reference and its reference checker checked zero entries. Add scoped amount evidence while recovering the structured formulation, retaining source batch and condition qualifiers. Ontology citations verify identities and labels rather than recipe amounts. No separate paper was asserted or required to identify this catalogue recipe.

### Append-only event history and timestamp interpretation

provenance: supported. Targets: CultureMech:007508.

All 14 scoped timestamps were checked for ISO syntax and timezone. Every instance parses and has an explicit timezone. Curation events are process provenance rather than independent confirmation of recipe correctness.

[]

## Findings

### f1: Generated target loses the recovered five-row NBRC 959 formula

blocker / open / confirmed; issue key: cm007508-stale-collapsed-source959-formula.

The whole-table string at VARIABLE and an empty ingredient with Glucose as its g/L value do not encode a usable named formulation. The owner has five explicit source rows and the exact source reference. The source agar is optional, yet neither layer documents selecting a solid branch. Native P1 reflects unusable scientific representation rather than a schema-validation failure.

### f2: Generated preparation replaces seawater and invents autoclaving

major / open / confirmed; issue key: cm007508-unsupported-source-preparation.

The exact source requires seawater, whereas target preparation says distilled water. It also asserts autoclaving with action DISSOLVE, although NBRC 959 gives no sterilization protocol. The current owner retains seawater and no fabricated preparation steps. The solvent substitution changes the formulation, while the generic method is unsupported; neither neighbor 960 nor routine practice resolves these discrepancies.

### f3: Four maintained owner labels differ from canonical labels

minor / open / confirmed; issue key: cm007508-owner-canonical-label-drift.

[{"field_path": "ingredients[1].term.label", "id": "FOODON:03315426", "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "source_key": "foodon03315426"}, {"field_path": "ingredients[2].term.label", "id": "CHEBI:64220", "asserted_label": "Na glutamate", "canonical_label": "monosodium glutamate", "source_key": "chebi64220"}, {"field_path": "ingredients[3].term.label", "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "source_key": "chebi2509"}, {"field_path": "ingredients[4].term.label", "id": "ENVO:00002149", "asserted_label": "Seawater", "canonical_label": "sea water", "source_key": "envo00002149"}] Source preferred names should remain while canonical term labels are corrected for the same verified IDs.

## Recommended Actions And Acceptance Checks

### a1

Verify all five maintained rows and source units, correct canonical labels, add scoped amount evidence, explicitly qualify optional agar and regenerate with the stable ID and NBRC 959 accession.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve source seawater and remove unsupported generic preparation through the maintained input and regeneration path. Keep unspecified pH and sterilization details explicit until exact-source evidence exists.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Update the four canonical labels after verifying their existing IDs; preserve the source identities, optional-agar qualifier and all original amounts and units.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/960.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_960.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/960.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/960.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch013/123/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/123/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/960.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/960.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| source-catalog | /private/tmp/culturemech-review-work-batch013/source-preflight-bound/123/source-catalog.json; All bound per-record source metadata, successful captures and retained failed attempts | context_only | [{"key": "chebi17234", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234", "status": 200, "accessed_at": "2026-10-21T08:17:26.738243Z", "sha256": "e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f", "metadata_sha256": "1f7ae4477fc69934e9661df7680d89841c944337c98da538ecf606bbee4d0dca", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi17234.json", "content_limit": null, "error": null}, {"key": "chebi2509", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509", "status": 200, "accessed_at": "2026-10-21T08:17:27.847373Z", "sha256": "8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a", "metadata_sha256": "b948d20f98a26d652f1d59dbe67f94aeb3f9ae77641e503dab273ccef2acb6e6", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/117/chebi2509.json", "content_limit": null, "error": null}, {"key": "chebi64220", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64220", "status": 200, "accessed_at": "2026-10-21T06:49:18.590575Z", "sha256": "f365c8a94dc3b7bb63e10235e8728f2333b34fb60943ea59c357ebd3456fb25b", "metadata_sha256": "d28e9470099f4537ad220993c7e7dc578f46732e28f2eb636d279e6ebf6a9e46", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi64220.json", "content_limit": null, "error": null}, {"key": "envo00002149", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00002149", "status": 200, "accessed_at": "2026-10-21T07:15:14.257665Z", "sha256": "606e3d069458b6f4d637bc9515fdd9947f1a5d2bca36043729825e643d7211d2", "metadata_sha256": "377e3f76f4f183e9696741cc478a5628e6684f08d1ec8d4003b5bb5ebdd2ce4d", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch008/071/envo00002149.json", "content_limit": null, "error": null}, {"key": "foodon03315426", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426", "status": 200, "accessed_at": "2026-10-21T08:00:49.388263Z", "sha256": "cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44", "metadata_sha256": "08b88d5a20203dbab9356d4e24acadd466b8ef2e1f3aa40f433afac40d7c38d7", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/116/foodon03315426.json", "content_limit": null, "error": null}, {"key": "nbrc959_attempt1_sandbox", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959", "status": null, "accessed_at": "2026-10-21T08:59:42.127581Z", "sha256": null, "metadata_sha256": "637bf5802a89812b174f2586b706f5a0a00a0d2dd5429ddfa7a37df028d367f3", "reused_capture_from": null, "content_limit": "Failed transport attempt; no source content retrieved.", "error": "&lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt;"}, {"key": "nbrc960_attempt1_sandbox", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=960", "status": null, "accessed_at": "2026-10-21T08:59:42.146487Z", "sha256": null, "metadata_sha256": "253b732964f5a5b5f4ab5674838b475fb668a4a44a1aa1520ce66ef3d82eaf7a", "reused_capture_from": null, "content_limit": "Failed transport attempt; no source content retrieved.", "error": "&lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt;"}, {"key": "nbrc959", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959", "status": 200, "accessed_at": "2026-10-21T09:00:11.492307Z", "sha256": "f9c6160df6a4ff80275bbb1fdbc9bc8dbc5e4abf7e4dba63c3d1412680699901", "metadata_sha256": "bdd3259893fe0b6bd575b36d96dd5851259c02d6dd5e90a260f63b67d3804354", "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "nbrc960", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=960", "status": 200, "accessed_at": "2026-10-21T09:00:11.492452Z", "sha256": "d5f2cfeceed7907b4991812320fb9d388d0eb56c8f9e38406ec02ac955360b22", "metadata_sha256": "782e67baf7038d9614b73230c1441b3f651af874594d9ad54c9015153c54242d", "reused_capture_from": null, "content_limit": null, "error": null}] |
| nbrc959 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959; Medium No. header; complete Medium Composition table, footnotes and Comment section | supports | Official NBRC 959 medium-H gives five quantified rows, including seawater and optional agar; no numeric pH or preparation protocol is stated. |
| nbrc960 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=960; Medium No. header, complete composition and preparation; identity countercheck only | context_only | Actual NBRC 960 gives agar, distilled water and pH around 5.5. It is a distinct medium and cannot supply a missing pH or preparation for medium-H 959. |
| amount-1 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959; Medium Composition table, quantified row 1: Glucose | supports | Exact source amount for owner ingredients[0].concentration; Generic glucose; no stereochemistry or hydrate inferred. Source value and unit are 2 g. The target retains this only inside its collapsed table string. |
| amount-2 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959; Medium Composition table, quantified row 2: Yeast extract | supports | Exact source amount for owner ingredients[1].concentration; Complex extract; literal mass rather than a molecular concentration. Source value and unit are 0.2 g. The target retains this only inside its collapsed table string. |
| amount-3 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959; Medium Composition table, quantified row 3: Monosodium glutamate | supports | Exact source amount for owner ingredients[2].concentration; Generic monosodium salt; source does not specify stereochemistry. Source value and unit are 0.5 g. The target retains this only inside its collapsed table string. |
| amount-4 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959; Medium Composition table, quantified row 4: Agar (if needed) | supports | Exact source amount for owner ingredients[3].concentration; Conditional solidification branch. Source value and unit are 12 g. The target retains this only inside its collapsed table string. |
| amount-5 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959; Medium Composition table, quantified row 5: Seawater | supports | Exact source amount for owner ingredients[4].concentration; Literal natural seawater volume, not distilled water and not a water-density conversion. Source value and unit are 1 L. The target retains this only inside its collapsed table string. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:17234 resolves to canonical label glucose and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | FOODON:03315426 resolves to canonical label yeast extract and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi64220 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64220; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:64220 resolves to canonical label monosodium glutamate and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:2509 resolves to canonical label agar and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| envo00002149 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00002149; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | ENVO:00002149 resolves to canonical label sea water and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact MAPPED/preferred_term rows for each asserted secondary key; adjacent pinned metadata | supports | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances": 0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent": 0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 5, "primary_ontology_instances": 5, "primary_CHEBI_instances": 3, "canonical_primary_label_instances": 1, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 100.0, "primary_CHEBI_percent": 60.0, "secondary_verified_percent": 0.0}}, "secondary_instances": []} |
| importer | src/culturemech/import/nbrc_importer.py; _map_ingredients; _map_preparation_steps; _infer_medium_type | context_only | Current importer maps quantities mechanically and creates generic dissolve, adjust-pH and autoclaving prose when preparation text is absent. Its action test uses the substring autoclave, which is not present in autoclaving, explaining the generated DISSOLVE action. The classification heuristic can use parentheses as a defined-medium hint. Code inspection is not a historical execution replay. |
| recovery | scripts/recover_nbrc_composition.py; parse_composition; recover | context_only | Current recovery code parses explicit composition rows and separate footnote stock sections from #medium-comp and records recovery history. Its presence and later owner data do not prove the generated merged record was regenerated. |
| exporter | src/culturemech/export/kgx_export.py; transform; medium_to_ingredient_edge; _resolved_ingredient_id; nodes | context_only | The current exporter walks structured ingredient rows and uses a MIM resolver before local identity fallback; it returns no ingredient edge if resolution yields no identity. A missing explicit term alone does not establish a zero-edge export. No export was executed or edge count asserted. The record type is also consumed for node/type semantics, so source-unsupported classification is consequential. |
| history | data/merge_yaml/merged/960.yaml; Every timestamp in target, owner and explicitly listed contextual dependencies | supports | [{"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[0].timestamp", "value": "2026-02-20T00:22:35.998275Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T03:09:12.779352Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:49.293339Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[4].timestamp", "value": "2026-05-16T09:03:06.757252+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[5].timestamp", "value": "2026-08-06T03:05:04.705310+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[0].timestamp", "value": "2026-02-20T00:22:35.998275Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T03:09:12.779352Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:49.293339Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[4].timestamp", "value": "2026-05-16T09:03:06.757252+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[5].timestamp", "value": "2026-08-19T21:54:23.097532+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[6].timestamp", "value": "2026-08-20T19:01:16.179537+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[7].timestamp", "value": "2026-09-07T00:00:00-07:00", "valid_ISO_datetime": true, "timezone_aware": true}] |

## Limits And Additional Notes

- The source gives 1 L seawater with ingredient masses, not a measured final-volume instruction. No seawater density, salinity or chemical composition is assumed.
- Optional agar defines a possible solid branch, but neither layer explicitly selects it. No new variant record is created.
- NBRC 959 supplies no numeric pH, sterilization, incubation, storage or organism-specific growth evidence. Neighbor 960 cannot fill those gaps.
- Generic glucose and monosodium glutamate are retained without adding a stereoisomer or hydrate. Yeast extract remains a mixture.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091545Z-culturemech-007508-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 960 (CultureMech:007508)'
started_at: '2026-10-21T09:12:05Z'
finished_at: '2026-10-21T09:15:45Z'
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
summary: The exact source is NBRC 959 medium-H despite the generated name 960. The
  target has two unusable collapsed ingredient rows and generic preparation that substitutes
  distilled water for source seawater and adds unsupported autoclaving. The maintained
  owner has all five source rows and the correct source reference, but four labels
  differ from canonical labels and optional agar has not been reconciled with unconditional
  SOLID_AGAR. All four canonical diagnostics pass; direct source comparison establishes
  these semantic defects.
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
  - path: data/merge_yaml/merged/960.yaml
    sha256: de51c4d471498ca54b44e2616db0af06de76c5c33f9bdf25d0f562509ac9bd7f
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_960.yaml
    sha256: 34e30bc7fb5910bccf8d7417830766804a55a356f5bf2ca0da604052db238c7a
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/recover_nbrc_composition.py
    sha256: a723e458895350a68ffae3e446006205b2e00cb185bee13976d5047be56405f0
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/nbrc_raw_yaml.py
    sha256: de5654d4eed2e01a2383dcf417b7d8e2779dbb622de9351c28373fb691812ec1
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
  - path: src/culturemech/fetch/nbrc_scraper.py
    sha256: 5c5bbda489abe0b6d000b9318a76913ab5496ee83aff58b530c2b42b5989d1e3
    role: context
  - path: src/culturemech/import/nbrc_importer.py
    sha256: 857b7e0ac88aef783ce4bc9b35c4c6a3d9fc38824a5d463010a6046ac4180924
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
  selection: Task review 123; batch 013 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twelve task batches contain
    120 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 122 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007508
targets:
- target_id: CultureMech:007508
  path: data/merge_yaml/merged/960.yaml
  label: '960'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_960.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/960.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/960.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch013/123/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/123/strict.tsv"
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/960.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/960.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007508
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
  - CultureMech:007508
- check_id: scoped-history-timestamps
  name: Scoped history timestamp syntax and timezone check
  required: false
  status: passed
  summary: 14 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Existing provenance is preserved; no timestamps were rewritten.
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/960.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T09:15:45Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_960.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T09:15:45Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/960.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:12:55.036378Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/960.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch013/123/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:12:56.747646Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/123/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/960.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:12:58.624156Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/960.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:12:59.767418Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: source-catalog
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch013/source-preflight-bound/123/source-catalog.json
  locator: All bound per-record source metadata, successful captures and retained
    failed attempts
  accessed_at: '2026-10-21T09:15:45Z'
  support: context_only
  summary: '[{"key": "chebi17234", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234",
    "status": 200, "accessed_at": "2026-10-21T08:17:26.738243Z", "sha256": "e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f",
    "metadata_sha256": "1f7ae4477fc69934e9661df7680d89841c944337c98da538ecf606bbee4d0dca",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi17234.json",
    "content_limit": null, "error": null}, {"key": "chebi2509", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509",
    "status": 200, "accessed_at": "2026-10-21T08:17:27.847373Z", "sha256": "8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a",
    "metadata_sha256": "b948d20f98a26d652f1d59dbe67f94aeb3f9ae77641e503dab273ccef2acb6e6",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/117/chebi2509.json",
    "content_limit": null, "error": null}, {"key": "chebi64220", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64220",
    "status": 200, "accessed_at": "2026-10-21T06:49:18.590575Z", "sha256": "f365c8a94dc3b7bb63e10235e8728f2333b34fb60943ea59c357ebd3456fb25b",
    "metadata_sha256": "d28e9470099f4537ad220993c7e7dc578f46732e28f2eb636d279e6ebf6a9e46",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi64220.json",
    "content_limit": null, "error": null}, {"key": "envo00002149", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00002149",
    "status": 200, "accessed_at": "2026-10-21T07:15:14.257665Z", "sha256": "606e3d069458b6f4d637bc9515fdd9947f1a5d2bca36043729825e643d7211d2",
    "metadata_sha256": "377e3f76f4f183e9696741cc478a5628e6684f08d1ec8d4003b5bb5ebdd2ce4d",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch008/071/envo00002149.json",
    "content_limit": null, "error": null}, {"key": "foodon03315426", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426",
    "status": 200, "accessed_at": "2026-10-21T08:00:49.388263Z", "sha256": "cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44",
    "metadata_sha256": "08b88d5a20203dbab9356d4e24acadd466b8ef2e1f3aa40f433afac40d7c38d7",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/116/foodon03315426.json",
    "content_limit": null, "error": null}, {"key": "nbrc959_attempt1_sandbox", "url":
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959", "status":
    null, "accessed_at": "2026-10-21T08:59:42.127581Z", "sha256": null, "metadata_sha256":
    "637bf5802a89812b174f2586b706f5a0a00a0d2dd5429ddfa7a37df028d367f3", "reused_capture_from":
    null, "content_limit": "Failed transport attempt; no source content retrieved.",
    "error": "<urlopen error [Errno 8] nodename nor servname provided, or not known>"},
    {"key": "nbrc960_attempt1_sandbox", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=960",
    "status": null, "accessed_at": "2026-10-21T08:59:42.146487Z", "sha256": null,
    "metadata_sha256": "253b732964f5a5b5f4ab5674838b475fb668a4a44a1aa1520ce66ef3d82eaf7a",
    "reused_capture_from": null, "content_limit": "Failed transport attempt; no source
    content retrieved.", "error": "<urlopen error [Errno 8] nodename nor servname
    provided, or not known>"}, {"key": "nbrc959", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959",
    "status": 200, "accessed_at": "2026-10-21T09:00:11.492307Z", "sha256": "f9c6160df6a4ff80275bbb1fdbc9bc8dbc5e4abf7e4dba63c3d1412680699901",
    "metadata_sha256": "bdd3259893fe0b6bd575b36d96dd5851259c02d6dd5e90a260f63b67d3804354",
    "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "nbrc960",
    "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=960",
    "status": 200, "accessed_at": "2026-10-21T09:00:11.492452Z", "sha256": "d5f2cfeceed7907b4991812320fb9d388d0eb56c8f9e38406ec02ac955360b22",
    "metadata_sha256": "782e67baf7038d9614b73230c1441b3f651af874594d9ad54c9015153c54242d",
    "reused_capture_from": null, "content_limit": null, "error": null}]'
  snapshot_sha256: 93ff72f2709cf8b96443c87bf195ab4765103089178fcd83e0801b4ab473caa6
- evidence_id: nbrc959
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959
  locator: Medium No. header; complete Medium Composition table, footnotes and Comment
    section
  accessed_at: '2026-10-21T09:00:11.492307Z'
  support: supports
  summary: Official NBRC 959 medium-H gives five quantified rows, including seawater
    and optional agar; no numeric pH or preparation protocol is stated.
  snapshot_sha256: f9c6160df6a4ff80275bbb1fdbc9bc8dbc5e4abf7e4dba63c3d1412680699901
- evidence_id: nbrc960
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=960
  locator: Medium No. header, complete composition and preparation; identity countercheck
    only
  accessed_at: '2026-10-21T09:00:11.492452Z'
  support: context_only
  summary: Actual NBRC 960 gives agar, distilled water and pH around 5.5. It is a
    distinct medium and cannot supply a missing pH or preparation for medium-H 959.
  snapshot_sha256: d5f2cfeceed7907b4991812320fb9d388d0eb56c8f9e38406ec02ac955360b22
- evidence_id: amount-1
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959
  locator: 'Medium Composition table, quantified row 1: Glucose'
  accessed_at: '2026-10-21T09:00:11.492307Z'
  support: supports
  summary: Exact source amount for owner ingredients[0].concentration; Generic glucose;
    no stereochemistry or hydrate inferred. Source value and unit are 2 g. The target
    retains this only inside its collapsed table string.
  quote: Glucose 2 g
  snapshot_sha256: f9c6160df6a4ff80275bbb1fdbc9bc8dbc5e4abf7e4dba63c3d1412680699901
- evidence_id: amount-2
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959
  locator: 'Medium Composition table, quantified row 2: Yeast extract'
  accessed_at: '2026-10-21T09:00:11.492307Z'
  support: supports
  summary: Exact source amount for owner ingredients[1].concentration; Complex extract;
    literal mass rather than a molecular concentration. Source value and unit are
    0.2 g. The target retains this only inside its collapsed table string.
  quote: Yeast extract 0.2 g
  snapshot_sha256: f9c6160df6a4ff80275bbb1fdbc9bc8dbc5e4abf7e4dba63c3d1412680699901
- evidence_id: amount-3
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959
  locator: 'Medium Composition table, quantified row 3: Monosodium glutamate'
  accessed_at: '2026-10-21T09:00:11.492307Z'
  support: supports
  summary: Exact source amount for owner ingredients[2].concentration; Generic monosodium
    salt; source does not specify stereochemistry. Source value and unit are 0.5 g.
    The target retains this only inside its collapsed table string.
  quote: Monosodium glutamate 0.5 g
  snapshot_sha256: f9c6160df6a4ff80275bbb1fdbc9bc8dbc5e4abf7e4dba63c3d1412680699901
- evidence_id: amount-4
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959
  locator: 'Medium Composition table, quantified row 4: Agar (if needed)'
  accessed_at: '2026-10-21T09:00:11.492307Z'
  support: supports
  summary: Exact source amount for owner ingredients[3].concentration; Conditional
    solidification branch. Source value and unit are 12 g. The target retains this
    only inside its collapsed table string.
  quote: Agar (if needed) 12 g
  snapshot_sha256: f9c6160df6a4ff80275bbb1fdbc9bc8dbc5e4abf7e4dba63c3d1412680699901
- evidence_id: amount-5
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=959
  locator: 'Medium Composition table, quantified row 5: Seawater'
  accessed_at: '2026-10-21T09:00:11.492307Z'
  support: supports
  summary: Exact source amount for owner ingredients[4].concentration; Literal natural
    seawater volume, not distilled water and not a water-density conversion. Source
    value and unit are 1 L. The target retains this only inside its collapsed table
    string.
  quote: Seawater 1 L
  snapshot_sha256: f9c6160df6a4ff80275bbb1fdbc9bc8dbc5e4abf7e4dba63c3d1412680699901
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: CHEBI:17234 resolves to canonical label glucose and is not obsolete. The
    complete response, including available formula, hydration, structure, synonyms
    and definitions, was inspected. Literal owner-label equality is assessed separately;
    ontology descriptions do not establish recipe quantities.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:00:49.388263Z'
  support: supports
  summary: FOODON:03315426 resolves to canonical label yeast extract and is not obsolete.
    The complete response, including available formula, hydration, structure, synonyms
    and definitions, was inspected. Literal owner-label equality is assessed separately;
    ontology descriptions do not establish recipe quantities.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: chebi64220
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64220
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T06:49:18.590575Z'
  support: supports
  summary: CHEBI:64220 resolves to canonical label monosodium glutamate and is not
    obsolete. The complete response, including available formula, hydration, structure,
    synonyms and definitions, was inspected. Literal owner-label equality is assessed
    separately; ontology descriptions do not establish recipe quantities.
  snapshot_sha256: f365c8a94dc3b7bb63e10235e8728f2333b34fb60943ea59c357ebd3456fb25b
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to canonical label agar and is not obsolete. The complete
    response, including available formula, hydration, structure, synonyms and definitions,
    was inspected. Literal owner-label equality is assessed separately; ontology descriptions
    do not establish recipe quantities.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: envo00002149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00002149
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T07:15:14.257665Z'
  support: supports
  summary: ENVO:00002149 resolves to canonical label sea water and is not obsolete.
    The complete response, including available formula, hydration, structure, synonyms
    and definitions, was inspected. Literal owner-label equality is assessed separately;
    ontology descriptions do not establish recipe quantities.
  snapshot_sha256: 606e3d069458b6f4d637bc9515fdd9947f1a5d2bca36043729825e643d7211d2
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact MAPPED/preferred_term rows for each asserted secondary key; adjacent
    pinned metadata
  accessed_at: '2026-10-21T09:15:45Z'
  support: supports
  summary: '{"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count":
    9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id",
    "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech",
    "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"},
    "counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances":
    0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances":
    0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent":
    0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 5,
    "primary_ontology_instances": 5, "primary_CHEBI_instances": 3, "canonical_primary_label_instances":
    1, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent":
    100.0, "primary_CHEBI_percent": 60.0, "secondary_verified_percent": 0.0}}, "secondary_instances":
    []}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: _map_ingredients; _map_preparation_steps; _infer_medium_type
  accessed_at: '2026-10-21T09:15:45Z'
  support: context_only
  summary: Current importer maps quantities mechanically and creates generic dissolve,
    adjust-pH and autoclaving prose when preparation text is absent. Its action test
    uses the substring autoclave, which is not present in autoclaving, explaining
    the generated DISSOLVE action. The classification heuristic can use parentheses
    as a defined-medium hint. Code inspection is not a historical execution replay.
- evidence_id: recovery
  kind: record_content
  reference: scripts/recover_nbrc_composition.py
  locator: parse_composition; recover
  accessed_at: '2026-10-21T09:15:45Z'
  support: context_only
  summary: 'Current recovery code parses explicit composition rows and separate footnote
    stock sections from #medium-comp and records recovery history. Its presence and
    later owner data do not prove the generated merged record was regenerated.'
- evidence_id: exporter
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: transform; medium_to_ingredient_edge; _resolved_ingredient_id; nodes
  accessed_at: '2026-10-21T09:15:45Z'
  support: context_only
  summary: The current exporter walks structured ingredient rows and uses a MIM resolver
    before local identity fallback; it returns no ingredient edge if resolution yields
    no identity. A missing explicit term alone does not establish a zero-edge export.
    No export was executed or edge count asserted. The record type is also consumed
    for node/type semantics, so source-unsupported classification is consequential.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/960.yaml
  locator: Every timestamp in target, owner and explicitly listed contextual dependencies
  accessed_at: '2026-10-21T09:15:45Z'
  support: supports
  summary: '[{"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-02-20T00:22:35.998275Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[1].timestamp",
    "value": "2026-03-13T03:09:12.779352Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[2].timestamp",
    "value": "2026-03-13T06:19:49.293339Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-05-16T09:03:06.757252+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/960.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-08-06T03:05:04.705310+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-02-20T00:22:35.998275Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[1].timestamp",
    "value": "2026-03-13T03:09:12.779352Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[2].timestamp",
    "value": "2026-03-13T06:19:49.293339Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-05-16T09:03:06.757252+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-08-19T21:54:23.097532+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[6].timestamp",
    "value": "2026-08-20T19:01:16.179537+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "curation_history[7].timestamp",
    "value": "2026-09-07T00:00:00-07:00", "valid_ISO_datetime": true, "timezone_aware":
    true}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: NBRC 959 provenance despite local 960 label
  outcome: supported
  summary: The stable CultureMech ID, merge source basename, import-history accession
    959, maintained owner source term and captured primary page resolve one medium.
    The local name 960 does not license substitution of actual NBRC 960; that different
    source is only an identity countercheck. The legacy HTTP import URL was read as
    provenance, not represented as a newly retrieved response.
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - record
  - owner-0
  - nbrc959
  - nbrc960
- assessment_id: amounts
  area: quantity
  topic: Every target row and every recovered source amount
  outcome: concern
  summary: 'The target has two malformed direct ingredient rows: one collapsed table
    at VARIABLE and an empty name with ''Glucose'' as its g/L value. The 5 separate
    owner rows preserve the inspected source amounts and units as itemized. Solid
    masses expressed by the owner per liter are interpreted on the nominal listed
    recipe basis, without claiming that a source water amount establishes measured
    final volume.'
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - record
  - owner-0
  - nbrc959
  - amount-1
  - amount-2
  - amount-3
  - amount-4
  - amount-5
  details: '{"recovered_source_amounts": [{"owner_field": "ingredients[0].concentration",
    "name": "Glucose", "owner_value": "2", "owner_unit": "G_PER_L", "source_amount":
    "2", "source_unit": "g", "source_quote": "Glucose 2 g", "source_locator": "Medium
    Composition quantified row 1", "condition": "Generic glucose; no stereochemistry
    or hydrate inferred.", "decision": "evidence_only", "decision_rationale": "Literal
    source amount is supported; ingredient-level evidence is absent from the owner.
    Source masses use the nominal listed recipe basis, not independently measured
    final volume.", "target_correspondence": "Embedded text only; no equivalent usable
    direct ingredient row", "evidence_id": "amount-1"}, {"owner_field": "ingredients[1].concentration",
    "name": "Yeast extract", "owner_value": "0.2", "owner_unit": "G_PER_L", "source_amount":
    "0.2", "source_unit": "g", "source_quote": "Yeast extract 0.2 g", "source_locator":
    "Medium Composition quantified row 2", "condition": "Complex extract; literal
    mass rather than a molecular concentration.", "decision": "evidence_only", "decision_rationale":
    "Literal source amount is supported; ingredient-level evidence is absent from
    the owner. Source masses use the nominal listed recipe basis, not independently
    measured final volume.", "target_correspondence": "Embedded text only; no equivalent
    usable direct ingredient row", "evidence_id": "amount-2"}, {"owner_field": "ingredients[2].concentration",
    "name": "Monosodium glutamate", "owner_value": "0.5", "owner_unit": "G_PER_L",
    "source_amount": "0.5", "source_unit": "g", "source_quote": "Monosodium glutamate
    0.5 g", "source_locator": "Medium Composition quantified row 3", "condition":
    "Generic monosodium salt; source does not specify stereochemistry.", "decision":
    "evidence_only", "decision_rationale": "Literal source amount is supported; ingredient-level
    evidence is absent from the owner. Source masses use the nominal listed recipe
    basis, not independently measured final volume.", "target_correspondence": "Embedded
    text only; no equivalent usable direct ingredient row", "evidence_id": "amount-3"},
    {"owner_field": "ingredients[3].concentration", "name": "Agar (if needed)", "owner_value":
    "12", "owner_unit": "G_PER_L", "source_amount": "12", "source_unit": "g", "source_quote":
    "Agar (if needed) 12 g", "source_locator": "Medium Composition quantified row
    4", "condition": "Conditional solidification branch.", "decision": "evidence_only",
    "decision_rationale": "Literal source amount is supported; ingredient-level evidence
    is absent from the owner. Source masses use the nominal listed recipe basis, not
    independently measured final volume.", "target_correspondence": "Embedded text
    only; no equivalent usable direct ingredient row", "evidence_id": "amount-4"},
    {"owner_field": "ingredients[4].concentration", "name": "Seawater", "owner_value":
    "1", "owner_unit": "L", "source_amount": "1", "source_unit": "L", "source_quote":
    "Seawater 1 L", "source_locator": "Medium Composition quantified row 5", "condition":
    "Literal natural seawater volume, not distilled water and not a water-density
    conversion.", "decision": "evidence_only", "decision_rationale": "Literal liquid
    amount is supported but lacks ingredient-level source evidence; no mass conversion
    is asserted.", "target_correspondence": "Embedded text only; no equivalent usable
    direct ingredient row", "evidence_id": "amount-5"}], "target_malformed_claims":
    [{"field_path": "ingredients[0].concentration", "current": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "unsupported", "source_quote": "Glucose 2 g",
    "source_locator": "Medium Composition quantified row 1", "evidence_ids": ["nbrc959",
    "amount-1"], "rationale": "A collapsed multi-ingredient string or empty ingredient
    cannot be assigned one source concentration. Recover all explicit source rows
    rather than treating this malformed claim as a number."}, {"field_path": "ingredients[1].concentration",
    "current": {"value": "Glucose", "unit": "G_PER_L"}, "decision": "unsupported",
    "source_quote": "Glucose 2 g", "source_locator": "Medium Composition quantified
    row 1", "evidence_ids": ["nbrc959", "amount-1"], "rationale": "A collapsed multi-ingredient
    string or empty ingredient cannot be assigned one source concentration. Recover
    all explicit source rows rather than treating this malformed claim as a number."}]}'
- assessment_id: grounding
  area: grounding
  topic: All asserted primary IDs, canonical labels and current secondary keys
  outcome: concern
  summary: The generated target has 0/2 primary ontology links and 0/2 verified secondary
    links. The owner has 5/5 primary ontology links, including 3 CHEBI instances,
    and 0/5 verified secondary links. 4 owner primary labels differ from canonical
    labels. These are separate layer-specific linkage denominators on a 0–100 scale,
    not scientific accuracy scores. No secondary denominator of zero is invented when
    no keys are asserted.
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi17234
  - foodon03315426
  - chebi64220
  - chebi2509
  - envo00002149
  details: '{"counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances":
    0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances":
    0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent":
    0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 5,
    "primary_ontology_instances": 5, "primary_CHEBI_instances": 3, "canonical_primary_label_instances":
    1, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent":
    100.0, "primary_CHEBI_percent": 60.0, "secondary_verified_percent": 0.0}}, "label_drift":
    [{"field_path": "ingredients[1].term.label", "id": "FOODON:03315426", "asserted_label":
    "Yeast extract", "canonical_label": "yeast extract", "source_key": "foodon03315426"},
    {"field_path": "ingredients[2].term.label", "id": "CHEBI:64220", "asserted_label":
    "Na glutamate", "canonical_label": "monosodium glutamate", "source_key": "chebi64220"},
    {"field_path": "ingredients[3].term.label", "id": "CHEBI:2509", "asserted_label":
    "Agar", "canonical_label": "agar", "source_key": "chebi2509"}, {"field_path":
    "ingredients[4].term.label", "id": "ENVO:00002149", "asserted_label": "Seawater",
    "canonical_label": "sea water", "source_key": "envo00002149"}], "instances": [{"layer":
    "target", "path": "data/merge_yaml/merged/960.yaml", "field": "ingredients[0]",
    "preferred_term": "Glucose2gYeast extract0.2gMonosodium glutamate0.5gAgar (if
    needed)12gSeawater1L"}, {"layer": "target", "path": "data/merge_yaml/merged/960.yaml",
    "field": "ingredients[1]", "preferred_term": ""}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_960.yaml",
    "field": "ingredients[0]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234",
    "asserted_label": "glucose", "canonical_label": "glucose", "label_equal": true,
    "source_key": "chebi17234", "description": ["An aldohexose used as a source of
    energy and metabolic intermediate."], "synonyms": ["DL-glucose", "Glc", "Glucose",
    "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose", "glucose"], "form_annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:50-99-7", "kegg.compound:C00293",
    "wikipedia.en:Glucose"], "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id":
    ["CHEBI:14313", "CHEBI:24277", "CHEBI:33929", "CHEBI:5418"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17234"], "mass": ["180.156"], "monoisotopic_mass":
    ["180.06339"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_960.yaml",
    "field": "ingredients[1]", "preferred_term": "Yeast extract", "primary_id": "FOODON:03315426",
    "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "label_equal":
    false, "source_key": "foodon03315426", "description": ["SIREN DB annotation:\n*
    not heat-treated FOODON:03440003\n* part of algae or fungus FOODON:03420247"],
    "synonyms": [], "form_annotations": {"database_cross_reference": ["https://bioregistry.io/reference/siren:F15426"],
    "has curation status": ["http://purl.obolibrary.org/obo/IAO_0000428"]}}, {"layer":
    "owner", "path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field": "ingredients[2]",
    "preferred_term": "Monosodium glutamate", "primary_id": "CHEBI:64220", "asserted_label":
    "Na glutamate", "canonical_label": "monosodium glutamate", "label_equal": false,
    "source_key": "chebi64220", "description": ["An organic sodium salt that is the
    monosodium salt of glutamic acid."], "synonyms": ["MSG", "sodium 2-ammoniopentanedioate",
    "sodium 2-azaniumylpentanedioate", "sodium 2-azaniumylpentanedioate", "sodium
    glutamate"], "form_annotations": {"charge": [0.0], "database_cross_reference":
    ["pubmed:22293291", "reaxys:17003240"], "generalized_empirical_formula": ["C5H8NO4.Na"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:64220"], "inchi_key_string":
    ["LPUQAYUQRXPFSQ-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C5H9NO4.Na/c6-3(5(9)10)1-2-4(7)8;/h3H,1-2,6H2,(H,7,8)(H,9,10);/q;+1/p-1"],
    "mass": ["169.112"], "monoisotopic_mass": ["169.0351"], "smiles_string": ["[NH3+]C(CCC(=O)[O-])C(=O)[O-].[Na+]"]}},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_960.yaml", "field":
    "ingredients[3]", "preferred_term": "Agar (if needed)", "primary_id": "CHEBI:2509",
    "asserted_label": "Agar", "canonical_label": "agar", "label_equal": false, "source_key":
    "chebi2509", "description": ["A complex mixture of polysaccharides extracted from
    species of red algae. Its two main components are agarose and agaropectin. Agarose
    is the component responsible for the high-strength gelling properties of agar,
    while agaropectin provides the viscous properties."], "synonyms": [], "form_annotations":
    {"database_cross_reference": ["cas:9002-18-0", "kegg.compound:C08815", "pubmed:25603143",
    "pubmed:25842535", "pubmed:25959629", "pubmed:26043937", "pubmed:26050892", "pubmed:26116384",
    "reaxys:8538728", "wikipedia.en:Agar"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:2509"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_960.yaml",
    "field": "ingredients[4]", "preferred_term": "Seawater", "primary_id": "ENVO:00002149",
    "asserted_label": "Seawater", "canonical_label": "sea water", "label_equal": false,
    "source_key": "envo00002149", "description": ["This definition refers to water
    that is actually in a sea or ocean. This water may have a wide range of salinity
    levels.", "Water which has physicochemical properties that have been determined
    by the processes occuring in a sea or ocean."], "synonyms": ["ocean water", "seawater"],
    "form_annotations": {"database_cross_reference": ["EcoLexicon:sea_water", "LTER:701",
    "SWEETRealm:SeaWater", "https://en.wikipedia.org/wiki/Sea_water"], "editor note":
    ["When we have more classes representing the various processes which make seawater
    seawater, we can further axiomatise this class."]}}]}'
- assessment_id: forms
  area: grounding
  topic: Source ingredient identities, mixtures and exact chemical forms
  outcome: supported
  summary: Primary IDs denote generic glucose, yeast extract, monosodium glutamate,
    agar and sea water. CHEBI:64220 has no explicit stereochemical layer in its captured
    structural annotation, consistent with the generic source wording. ENVO:00002149
    has canonical sea water and synonym seawater. Four owner labels differ literally
    from canonical labels, but these differences do not by themselves prove wrong
    IDs. No seawater salt profile or reagent-specific molecular conversion is invented.
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - record
  - owner-0
  - nbrc959
  - chebi17234
  - foodon03315426
  - chebi64220
  - chebi2509
  - envo00002149
- assessment_id: conditions
  area: consistency
  topic: Preparation, pH and physical-state conditions
  outcome: concern
  summary: The source specifies seawater. The target instructs dissolving in distilled
    water and adds generic pH adjustment and autoclaving, with the latter tagged DISSOLVE.
    The owner has an empty preparation list and correctly preserves seawater. Absence
    of a source protocol is not permission to invent one. Optional agar remains conditional.
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - record
  - owner-0
  - nbrc959
  - importer
- assessment_id: classification
  area: scope
  topic: Classification and bounded biological claims
  outcome: concern
  summary: COMPLEX/UNDEFINED agrees with yeast extract and seawater. Both layers assert
    SOLID_AGAR despite the source and owner retaining Agar (if needed); the record
    does not document branch selection. Preserve that condition rather than implying
    every preparation is solid. Neither target nor owner asserts organisms, strains,
    taxon IDs, assemblies, DOI/PMID papers, growth outcomes, parent media or variants.
    Source catalogue scope is not experimental growth evidence. Optional omissions
    are not populated with invented organisms.
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - record
  - owner-0
  - nbrc959
  - nbrc960
  - exporter
- assessment_id: owner-correspondence
  area: ownership
  topic: Maintained recovery versus generated representation
  outcome: concern
  summary: The generated August merge precedes later owner recovery and source metadata.
    The owner now contains 5 explicit source rows and an official source term/reference;
    the target retains two collapsed rows and no structured source term/reference.
    Owner label differences must be corrected before regeneration.
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - record
  - owner-0
  - nbrc959
  - recovery
  - mim
- assessment_id: evidence
  area: evidence
  topic: Claim-level amount evidence and checked reference scope
  outcome: concern
  summary: Each source amount is traced to an exact table row above. The owner has
    the official recipe reference but lacks ingredient-level amount evidence; the
    target has no structured reference and its reference checker checked zero entries.
    Add scoped amount evidence while recovering the structured formulation, retaining
    source batch and condition qualifiers. Ontology citations verify identities and
    labels rather than recipe amounts. No separate paper was asserted or required
    to identify this catalogue recipe.
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - record
  - owner-0
  - nbrc959
  - validate-references
- assessment_id: history
  area: provenance
  topic: Append-only event history and timestamp interpretation
  outcome: supported
  summary: All 14 scoped timestamps were checked for ISO syntax and timezone. Every
    instance parses and has an explicit timezone. Curation events are process provenance
    rather than independent confirmation of recipe correctness.
  target_ids:
  - CultureMech:007508
  evidence_ids:
  - record
  - owner-0
  - history
  details: '[]'
findings:
- finding_id: f1
  issue_key: cm007508-stale-collapsed-source959-formula
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated target loses the recovered five-row NBRC 959 formula
  description: The whole-table string at VARIABLE and an empty ingredient with Glucose
    as its g/L value do not encode a usable named formulation. The owner has five
    explicit source rows and the exact source reference. The source agar is optional,
    yet neither layer documents selecting a solid branch. Native P1 reflects unusable
    scientific representation rather than a schema-validation failure.
  target_ids:
  - CultureMech:007508
  field_paths:
  - ingredients
  - media_term
  - references
  - physical_state
  evidence_ids:
  - record
  - owner-0
  - nbrc959
  - recovery
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_960.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm007508-unsupported-source-preparation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated preparation replaces seawater and invents autoclaving
  description: The exact source requires seawater, whereas target preparation says
    distilled water. It also asserts autoclaving with action DISSOLVE, although NBRC
    959 gives no sterilization protocol. The current owner retains seawater and no
    fabricated preparation steps. The solvent substitution changes the formulation,
    while the generic method is unsupported; neither neighbor 960 nor routine practice
    resolves these discrepancies.
  target_ids:
  - CultureMech:007508
  field_paths:
  - preparation_steps[0].description
  - preparation_steps[2].description
  - preparation_steps[2].action
  evidence_ids:
  - record
  - owner-0
  - nbrc959
  - amount-5
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_960.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: cm007508-owner-canonical-label-drift
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Four maintained owner labels differ from canonical labels
  description: '[{"field_path": "ingredients[1].term.label", "id": "FOODON:03315426",
    "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "source_key":
    "foodon03315426"}, {"field_path": "ingredients[2].term.label", "id": "CHEBI:64220",
    "asserted_label": "Na glutamate", "canonical_label": "monosodium glutamate", "source_key":
    "chebi64220"}, {"field_path": "ingredients[3].term.label", "id": "CHEBI:2509",
    "asserted_label": "Agar", "canonical_label": "agar", "source_key": "chebi2509"},
    {"field_path": "ingredients[4].term.label", "id": "ENVO:00002149", "asserted_label":
    "Seawater", "canonical_label": "sea water", "source_key": "envo00002149"}] Source
    preferred names should remain while canonical term labels are corrected for the
    same verified IDs.'
  target_ids:
  - CultureMech:007508
  field_paths:
  - owner:data/normalized_yaml/bacterial/NBRC_960.yaml:ingredients[1].term.label
  - owner:data/normalized_yaml/bacterial/NBRC_960.yaml:ingredients[2].term.label
  - owner:data/normalized_yaml/bacterial/NBRC_960.yaml:ingredients[3].term.label
  - owner:data/normalized_yaml/bacterial/NBRC_960.yaml:ingredients[4].term.label
  evidence_ids:
  - owner-0
  - foodon03315426
  - chebi64220
  - chebi2509
  - envo00002149
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_960.yaml
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
  description: Verify all five maintained rows and source units, correct canonical
    labels, add scoped amount evidence, explicitly qualify optional agar and regenerate
    with the stable ID and NBRC 959 accession.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007508
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_960.yaml
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
  description: Preserve source seawater and remove unsupported generic preparation
    through the maintained input and regeneration path. Keep unspecified pH and sterilization
    details explicit until exact-source evidence exists.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007508
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_960.yaml
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
  description: Update the four canonical labels after verifying their existing IDs;
    preserve the source identities, optional-agar qualifier and all original amounts
    and units.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007508
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_960.yaml
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
- The source gives 1 L seawater with ingredient masses, not a measured final-volume
  instruction. No seawater density, salinity or chemical composition is assumed.
- Optional agar defines a possible solid branch, but neither layer explicitly selects
  it. No new variant record is created.
- NBRC 959 supplies no numeric pH, sterilization, incubation, storage or organism-specific
  growth evidence. Neighbor 960 cannot fill those gaps.
- Generic glucose and monosodium glutamate are retained without adding a stereoisomer
  or hydrate. Yeast extract remains a mixture.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-013
- generated-medium
```
