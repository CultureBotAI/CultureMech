# Source and formulation review: 948 (CultureMech:007507)

- Review: 20261021T091731Z-culturemech-007507-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:12:03Z
- Finished UTC: 2026-10-21T09:17:31Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

NBRC Medium 947 is resolved despite the generated name 948. The target retains two unusable collapsed ingredient rows, generic preparation inconsistent with separate methanol filtration and unadjusted pH, and an unsupported DEFINED classification. Its maintained owner has all four source rows and the filtration instruction, but still needs classification, optional-agar scope and two canonical-label corrections before regeneration. All four canonical diagnostics pass; these are source-supported semantic findings.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 121; batch 013 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twelve task batches contain 120 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 122 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007507 | data/merge_yaml/merged/948.yaml | generated | 948 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007507 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007507 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/121/strict.tsv |
| validate-terms | passed | True | CultureMech:007507 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007507 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007507 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped history timestamp syntax and timezone check | passed | False | CultureMech:007507 | 14 timestamp instances inspected; 0 malformed or timezone-naive instances. Existing provenance is preserved; no timestamps were rewritten. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007507.

The four documented recipes completed; interpret the scope of each separately.

### NBRC 947 provenance despite local 948 label

identity: supported. Targets: CultureMech:007507.

The stable CultureMech ID, merge source basename, import-history accession 947, maintained owner source term and captured primary page resolve one medium. The local name 948 does not license substitution of actual NBRC 948; that different source is only an identity countercheck. The legacy HTTP import URL was read as provenance, not represented as a newly retrieved response.

### Every target row and every recovered source amount

quantity: concern. Targets: CultureMech:007507.

The target has two malformed direct ingredient rows: one collapsed table at VARIABLE and an empty name with 'Bacto Marine Broth 2216 (Difco)' as its g/L value. The 4 separate owner rows preserve the inspected source amounts and units as itemized. Solid masses expressed by the owner per liter are interpreted on the nominal listed recipe basis, without claiming that a source water amount establishes measured final volume.

{"recovered_source_amounts": [{"owner_field": "ingredients[0].concentration", "name": "Bacto Marine Broth 2216 (Difco)", "owner_value": "37.4", "owner_unit": "G_PER_L", "source_amount": "37.4", "source_unit": "g", "source_quote": "Bacto Marine Broth 2216 (Difco) 37.4 g", "source_locator": "Medium Composition quantified row 1", "condition": "Named commercial broth; literal dry mass on the listed recipe basis.", "decision": "evidence_only", "decision_rationale": "Literal source amount is supported; ingredient-level evidence is absent from the owner. Source masses use the nominal listed recipe basis, not independently measured final volume.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-1"}, {"owner_field": "ingredients[1].concentration", "name": "Methanol*", "owner_value": "5", "owner_unit": "ML_PER_L", "source_amount": "5", "source_unit": "ml", "source_quote": "Methanol* 5 ml", "source_locator": "Medium Composition quantified row 2", "condition": "Separate filtration is explicit; this is a liquid dose, not a mass and not a measured final concentration.", "decision": "evidence_only", "decision_rationale": "Literal liquid amount is supported but lacks ingredient-level source evidence; no mass conversion is asserted.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-2"}, {"owner_field": "ingredients[2].concentration", "name": "Agar (if needed)", "owner_value": "15", "owner_unit": "G_PER_L", "source_amount": "15", "source_unit": "g", "source_quote": "Agar (if needed) 15 g", "source_locator": "Medium Composition quantified row 3", "condition": "Optional solidification branch must remain conditional.", "decision": "evidence_only", "decision_rationale": "Literal source amount is supported; ingredient-level evidence is absent from the owner. Source masses use the nominal listed recipe basis, not independently measured final volume.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-3"}, {"owner_field": "ingredients[3].concentration", "name": "Distilled water", "owner_value": "1", "owner_unit": "L", "source_amount": "1", "source_unit": "L", "source_quote": "Distilled water 1 L", "source_locator": "Medium Composition quantified row 4", "condition": "Literal source water volume; no density conversion or final-volume inference.", "decision": "evidence_only", "decision_rationale": "Literal liquid amount is supported but lacks ingredient-level source evidence; no mass conversion is asserted.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-4"}], "target_malformed_claims": [{"field_path": "ingredients[0].concentration", "current": {"value": "variable", "unit": "VARIABLE"}, "decision": "unsupported", "source_quote": "Bacto Marine Broth 2216 (Difco) 37.4 g", "source_locator": "Medium Composition quantified row 1", "evidence_ids": ["nbrc947", "amount-1"], "rationale": "A collapsed multi-ingredient string or empty ingredient cannot be assigned one source concentration. Recover all explicit source rows rather than treating this malformed claim as a number."}, {"field_path": "ingredients[1].concentration", "current": {"value": "Bacto Marine Broth 2216 (Difco)", "unit": "G_PER_L"}, "decision": "unsupported", "source_quote": "Bacto Marine Broth 2216 (Difco) 37.4 g", "source_locator": "Medium Composition quantified row 1", "evidence_ids": ["nbrc947", "amount-1"], "rationale": "A collapsed multi-ingredient string or empty ingredient cannot be assigned one source concentration. Recover all explicit source rows rather than treating this malformed claim as a number."}]}

### All asserted primary IDs, canonical labels and current secondary keys

grounding: concern. Targets: CultureMech:007507.

The generated target has 0/2 primary ontology links and 0/2 verified secondary links. The owner has 3/4 primary ontology links, including 3 CHEBI instances, and 0/4 verified secondary links. 2 owner primary labels differ from canonical labels. These are separate layer-specific linkage denominators on a 0–100 scale, not scientific accuracy scores. No secondary denominator of zero is invented when no keys are asserted.

{"counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances": 0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent": 0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 4, "primary_ontology_instances": 3, "primary_CHEBI_instances": 3, "canonical_primary_label_instances": 1, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 75.0, "primary_CHEBI_percent": 75.0, "secondary_verified_percent": 0.0}}, "label_drift": [{"field_path": "ingredients[1].term.label", "id": "CHEBI:17790", "asserted_label": "Methanol", "canonical_label": "methanol", "source_key": "chebi17790"}, {"field_path": "ingredients[2].term.label", "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "source_key": "chebi2509"}], "instances": [{"layer": "target", "path": "data/merge_yaml/merged/948.yaml", "field": "ingredients[0]", "preferred_term": "Bacto Marine Broth 2216 (Difco)37.4gMethanol*5mlAgar (if needed)15gDistilled water1LpH unadjusted*Sterilize separately by filtration."}, {"layer": "target", "path": "data/merge_yaml/merged/948.yaml", "field": "ingredients[1]", "preferred_term": ""}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "ingredients[0]", "preferred_term": "Bacto Marine Broth 2216 (Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "ingredients[1]", "preferred_term": "Methanol*", "primary_id": "CHEBI:17790", "asserted_label": "Methanol", "canonical_label": "methanol", "label_equal": false, "source_key": "chebi17790", "description": ["The primary alcohol that is the simplest aliphatic alcohol, comprising a methyl and an alcohol group."], "synonyms": ["CH3OH", "METHANOL", "METHANOL", "MeOH", "Methanol", "Methanol", "Methyl alcohol", "Methylalkohol", "carbinol", "methanol", "methanol", "spirit of wood", "wood alcohol", "wood naphtha", "wood spirit"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:67-56-1", "gmelin:449", "hmdb:HMDB0001875", "kegg.compound:C00132", "kegg.drug:D02309", "metacyc.compound:METOH", "pdb-ccd:MOH", "pubmed:11141607", "pubmed:11430978", "pubmed:11489599", "pubmed:11680737", "pubmed:11684179", "pubmed:14012711", "pubmed:14678513", "pubmed:14760634", "pubmed:15172721", "pubmed:15906011", "pubmed:16705261", "pubmed:17451998", "pubmed:17733096", "pubmed:19064074", "pubmed:19850112", "pubmed:20314698", "reaxys:1098229", "umbbd.compound:c0132", "wikipedia.en:Methanol"], "generalized_empirical_formula": ["CH4O"], "has_alternative_id": ["CHEBI:14588", "CHEBI:25227", "CHEBI:44080", "CHEBI:44553", "CHEBI:6816"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17790"], "inchi_key_string": ["OKKJLVBELUTLKV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/CH4O/c1-2/h2H,1H3"], "mass": ["32.042"], "monoisotopic_mass": ["32.02621"], "smiles_string": ["CO"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "ingredients[2]", "preferred_term": "Agar (if needed)", "primary_id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "label_equal": false, "source_key": "chebi2509", "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "synonyms": [], "form_annotations": {"database_cross_reference": ["cas:9002-18-0", "kegg.compound:C08815", "pubmed:25603143", "pubmed:25842535", "pubmed:25959629", "pubmed:26043937", "pubmed:26050892", "pubmed:26116384", "reaxys:8538728", "wikipedia.en:Agar"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:2509"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "ingredients[3]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_equal": true, "source_key": "chebi15377", "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]}}]}

### Source ingredient identities, mixtures and exact chemical forms

grounding: supported. Targets: CultureMech:007507.

CHEBI:17790 is neutral methanol with matching formula and structural annotation; its source dose remains 5 mL. CHEBI:2509 denotes the agar mixture, and CHEBI:15377 denotes water. Methanol and Agar are literal label differences, not wrong-ID findings. The commercial broth remains ungrounded rather than receiving an invented molecular identifier.

### Preparation, pH and physical-state conditions

consistency: concern. Targets: CultureMech:007507.

The owner retains the source-specific methanol filtration step and unadjusted-pH note. The target instead has generic dissolve, adjust-pH and autoclaving prose, with the last action misclassified as DISSOLVE. Its collapsed text contains the filtration footnote but does not preserve it as an operative preparation step. The source supplies no numeric pH and no autoclaving instruction for the whole formulation.

### Classification and bounded biological claims

scope: concern. Targets: CultureMech:007507.

Both layers assert DEFINED/DEFINED despite the named commercial broth. Its constituent chemical composition is not defined by this source. Both also assert SOLID_AGAR while preserving optional agar without documenting branch selection; a solid formulation is supported only if agar is used. Neither target nor owner asserts organisms, strains, taxon IDs, assemblies, DOI/PMID papers, growth outcomes, parent media or variants. Source catalogue scope is not experimental growth evidence. Optional omissions are not populated with invented organisms.

### Maintained recovery versus generated representation

ownership: concern. Targets: CultureMech:007507.

The generated August merge precedes later owner recovery and source metadata. The owner now contains 4 explicit source rows and an official source term/reference; the target retains two collapsed rows and no structured source term/reference. Owner label differences must be corrected before regeneration.

### Claim-level amount evidence and checked reference scope

evidence: concern. Targets: CultureMech:007507.

Each source amount is traced to an exact table row above. The owner has the official recipe reference but lacks ingredient-level amount evidence; the target has no structured reference and its reference checker checked zero entries. Add scoped amount evidence while recovering the structured formulation, retaining source batch and condition qualifiers. Ontology citations verify identities and labels rather than recipe amounts. No separate paper was asserted or required to identify this catalogue recipe.

### Append-only event history and timestamp interpretation

provenance: supported. Targets: CultureMech:007507.

All 14 scoped timestamps were checked for ISO syntax and timezone. Every instance parses and has an explicit timezone. Curation events are process provenance rather than independent confirmation of recipe correctness.

[]

## Findings

### f1: Generated target loses the recovered four-row NBRC 947 formula

blocker / open / confirmed; issue key: cm007507-stale-collapsed-source947-formula.

The whole-table string at VARIABLE and an empty ingredient whose g/L value is a product name do not encode a usable named formulation. The owner has the four explicit source rows and official source reference. Optional agar remains conditional, yet neither layer documents choosing the solid branch. Native P1 reflects unusable scientific representation; this is not P1.1 or a reported schema-validation failure.

### f2: Generated preparation loses methanol filtration and unadjusted pH

major / open / confirmed; issue key: cm007507-source-preparation-conflict.

The source requires separate filtration of Methanol* and says pH unadjusted. The target instead presents generic pH adjustment and autoclaving, with autoclaving tagged DISSOLVE. A footnote buried inside one malformed ingredient string is insufficient to preserve the preparation boundary. The maintained owner already supplies the filtration instruction and source pH note. Following the generated procedure could change the source preparation.

### f3: Defined classification lacks source support

major / open / confirmed; issue key: cm007507-unsupported-defined-classification.

Both maintained and generated layers declare medium_type DEFINED and composition_type DEFINED. The exact source names a commercial marine broth without its full constituent specification. The inspected evidence therefore cannot verify the defined-composition assertions; the commercial product name alone also does not establish the replacement classification. This concerns formulation classification, not bacterial-folder mismatch under P2.4.

### f4: Two maintained owner labels differ from canonical labels

minor / open / confirmed; issue key: cm007507-owner-canonical-label-drift.

[{"field_path": "ingredients[1].term.label", "id": "CHEBI:17790", "asserted_label": "Methanol", "canonical_label": "methanol", "source_key": "chebi17790"}, {"field_path": "ingredients[2].term.label", "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "source_key": "chebi2509"}] These label differences do not by themselves imply wrong chemical identifiers.

## Recommended Actions And Acceptance Checks

### a1

Verify and retain all four maintained rows with exact source units, add their scoped evidence, explicitly qualify optional agar, resolve the owner issues below, and regenerate the derived record with its stable ID and exact NBRC 947 identity.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve separate methanol filtration and unadjusted pH in the maintained preparation representation, and regenerate without unsupported whole-medium autoclaving. Retain unknown filtration pore size, base sterilization parameters and final volume rather than inventing them.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Verify the exact commercial product specification and reassess the maintained classification against its documented composition before regeneration. Retain the uncertainty if that specification is unavailable, and verify that any evidence-supported classification survives record/type export. Do not infer an undisclosed composition or mandate COMPLEX from the product name alone.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Use the verified canonical labels for the existing IDs while retaining Methanol* and Agar (if needed) as source preferred terms; preserve dose, filtration and optionality.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/948.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_948.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/948.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/948.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch013/121/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/121/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/948.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/948.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| source-catalog | /private/tmp/culturemech-review-work-batch013/source-preflight-bound/121/source-catalog.json; All bound per-record source metadata, successful captures and retained failed attempts | context_only | [{"key": "chebi15377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377", "status": 200, "accessed_at": "2026-10-21T08:17:26.097802Z", "sha256": "de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b", "metadata_sha256": "2c0ebbd7fde625475a4ba4fbef85146d2fbcc07efb94eb3c832f6b1db4cdf5b7", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/117/chebi15377.json", "content_limit": null, "error": null}, {"key": "chebi17790", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17790", "status": 200, "accessed_at": "2026-10-21T08:00:47.448030Z", "sha256": "9954cafff5982d415d5fbed82fa4630ac9958247ed636b3c770976752ebd50de", "metadata_sha256": "8c0e3fa4c3a8156e35e88f3d04df6add920aeec41ce7739c1290fb8b7e1e68c3", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch010/093/chebi17790.json", "content_limit": null, "error": null}, {"key": "chebi2509", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509", "status": 200, "accessed_at": "2026-10-21T08:17:27.847373Z", "sha256": "8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a", "metadata_sha256": "a98ff777bd7cbd2d7dc4e6586a909b7e31d41144ed7978db3f48cc048aca624c", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/117/chebi2509.json", "content_limit": null, "error": null}, {"key": "nbrc947_attempt1_sandbox", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947", "status": null, "accessed_at": "2026-10-21T08:59:42.087852Z", "sha256": null, "metadata_sha256": "c0d5caa6018b3eedb62f618b40e332c9a5ede3e3aa4ce9fa90eb7100fd58dfd6", "reused_capture_from": null, "content_limit": "Failed transport attempt; no source content retrieved.", "error": "&lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt;"}, {"key": "nbrc948_attempt1_sandbox", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=948", "status": null, "accessed_at": "2026-10-21T08:59:42.113852Z", "sha256": null, "metadata_sha256": "ba349300b6ee07e6ae049b0323f9796b73ecaba541380de7f6d69d9498c31895", "reused_capture_from": null, "content_limit": "Failed transport attempt; no source content retrieved.", "error": "&lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt;"}, {"key": "nbrc947", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947", "status": 200, "accessed_at": "2026-10-21T09:00:09.929582Z", "sha256": "1812da0ace3aa9aaac3fc7abd785024606652b05e847229dd8bc1bcd37418b9e", "metadata_sha256": "ada80b94fc76bad51653280a629745724a00330191d498e74fc3c1d8cb80aef9", "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "nbrc948", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=948", "status": 200, "accessed_at": "2026-10-21T09:00:09.930200Z", "sha256": "b255d9a31c2518964dc1fc73631d2f14eb40dd99d252f86c862e7108900516ce", "metadata_sha256": "7637b8cf6399a2ad76ba6e72f57f9c2dc8150f8edfd770f6f6c9d520062515f2", "reused_capture_from": null, "content_limit": null, "error": null}] |
| nbrc947 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947; Medium No. header; complete Medium Composition table, footnotes and Comment section | supports | Official NBRC 947 gives four quantified rows, unadjusted pH and separate methanol filtration. The full composition and comment fields were inspected. |
| nbrc948 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=948; Medium No. header, complete composition and preparation; identity countercheck only | context_only | Actual NBRC 948 is YSG Medium, with separately sterilized solutions A and B. Its composition and preparation are not the source of this record. |
| amount-1 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947; Medium Composition table, quantified row 1: Bacto Marine Broth 2216 (Difco) | supports | Exact source amount for owner ingredients[0].concentration; Named commercial broth; literal dry mass on the listed recipe basis. Source value and unit are 37.4 g. The target retains this only inside its collapsed table string. |
| amount-2 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947; Medium Composition table, quantified row 2: Methanol* | supports | Exact source amount for owner ingredients[1].concentration; Separate filtration is explicit; this is a liquid dose, not a mass and not a measured final concentration. Source value and unit are 5 ml. The target retains this only inside its collapsed table string. |
| amount-3 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947; Medium Composition table, quantified row 3: Agar (if needed) | supports | Exact source amount for owner ingredients[2].concentration; Optional solidification branch must remain conditional. Source value and unit are 15 g. The target retains this only inside its collapsed table string. |
| amount-4 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947; Medium Composition table, quantified row 4: Distilled water | supports | Exact source amount for owner ingredients[3].concentration; Literal source water volume; no density conversion or final-volume inference. Source value and unit are 1 L. The target retains this only inside its collapsed table string. |
| chebi17790 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17790; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:17790 resolves to canonical label methanol and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:2509 resolves to canonical label agar and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:15377 resolves to canonical label water and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact MAPPED/preferred_term rows for each asserted secondary key; adjacent pinned metadata | supports | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances": 0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent": 0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 4, "primary_ontology_instances": 3, "primary_CHEBI_instances": 3, "canonical_primary_label_instances": 1, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 75.0, "primary_CHEBI_percent": 75.0, "secondary_verified_percent": 0.0}}, "secondary_instances": []} |
| importer | src/culturemech/import/nbrc_importer.py; _map_ingredients; _map_preparation_steps; _infer_medium_type | context_only | Current importer maps quantities mechanically and creates generic dissolve, adjust-pH and autoclaving prose when preparation text is absent. Its action test uses the substring autoclave, which is not present in autoclaving, explaining the generated DISSOLVE action. The classification heuristic can use parentheses as a defined-medium hint. Code inspection is not a historical execution replay. |
| recovery | scripts/recover_nbrc_composition.py; parse_composition; recover | context_only | Current recovery code parses explicit composition rows and separate footnote stock sections from #medium-comp and records recovery history. Its presence and later owner data do not prove the generated merged record was regenerated. |
| exporter | src/culturemech/export/kgx_export.py; transform; medium_to_ingredient_edge; _resolved_ingredient_id; nodes | context_only | The current exporter walks structured ingredient rows and uses a MIM resolver before local identity fallback; it returns no ingredient edge if resolution yields no identity. A missing explicit term alone does not establish a zero-edge export. No export was executed or edge count asserted. The record type is also consumed for node/type semantics, so source-unsupported classification is consequential. |
| history | data/merge_yaml/merged/948.yaml; Every timestamp in target, owner and explicitly listed contextual dependencies | supports | [{"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[0].timestamp", "value": "2026-02-20T00:22:35.997170Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T03:08:43.445251Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:49.291053Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[4].timestamp", "value": "2026-05-16T09:03:06.754368+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[5].timestamp", "value": "2026-08-06T03:05:04.701669+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[0].timestamp", "value": "2026-02-20T00:22:35.997170Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T03:08:43.445251Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:49.291053Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[4].timestamp", "value": "2026-05-16T09:03:06.754368+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[5].timestamp", "value": "2026-08-19T21:54:23.090770+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[6].timestamp", "value": "2026-08-20T19:01:16.174901+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[7].timestamp", "value": "2026-09-07T00:00:00-07:00", "valid_ISO_datetime": true, "timezone_aware": true}] |
| methanol-preparation | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947; Composition footnote attached to Methanol* | supports | The asterisk attaches separate filtration to the methanol addition; it does not prescribe whole-medium autoclaving. |
| source-ph | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947; Composition text after the water row | supports | The source explicitly retains unadjusted pH, not a missing numeric pH to fill from a neighboring medium. |

## Limits And Additional Notes

- The source lists 1 L water plus 5 mL methanol; it does not give a measured final volume. The source title says 0.5% Methanol, but no new exact final-volume percentage or mass concentration is derived.
- Bacto Marine Broth 2216 (Difco) remains an opaque commercial mixture. No constituent composition, manufacturer lot specification or invented pure-chemical grounding is supplied.
- Agar is optional. Neither layer documents selecting the solid branch. No liquid/solid variant record was created.
- The primary source specifies methanol filtration but gives no membrane size, base-medium autoclave cycle, incubation, storage or organism-specific growth evidence. Such details remain unknown.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091731Z-culturemech-007507-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 948 (CultureMech:007507)'
started_at: '2026-10-21T09:12:03Z'
finished_at: '2026-10-21T09:17:31Z'
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
summary: NBRC Medium 947 is resolved despite the generated name 948. The target retains
  two unusable collapsed ingredient rows, generic preparation inconsistent with separate
  methanol filtration and unadjusted pH, and an unsupported DEFINED classification.
  Its maintained owner has all four source rows and the filtration instruction, but
  still needs classification, optional-agar scope and two canonical-label corrections
  before regeneration. All four canonical diagnostics pass; these are source-supported
  semantic findings.
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
  - path: data/merge_yaml/merged/948.yaml
    sha256: bba74008b1e3602f8892b8c1da6e3b04e4badb152b617c4fd965ec5f0550627d
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_948.yaml
    sha256: ffce8cd61a1ef0035e0ed0a86b3a2114380251f9c5db64ca7c0228319f25dded
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
  selection: Task review 121; batch 013 item 1 of 10, selected in Python lexicographic
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
  - CultureMech:007507
targets:
- target_id: CultureMech:007507
  path: data/merge_yaml/merged/948.yaml
  label: '948'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_948.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/948.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/948.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch013/121/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/121/strict.tsv"
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/948.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/948.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007507
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
  - CultureMech:007507
- check_id: scoped-history-timestamps
  name: Scoped history timestamp syntax and timezone check
  required: false
  status: passed
  summary: 14 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Existing provenance is preserved; no timestamps were rewritten.
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/948.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T09:17:31Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_948.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T09:17:31Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/948.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:12:41.401579Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/948.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch013/121/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:12:42.941445Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/121/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/948.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:12:45.308426Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/948.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:12:46.427644Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: source-catalog
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch013/source-preflight-bound/121/source-catalog.json
  locator: All bound per-record source metadata, successful captures and retained
    failed attempts
  accessed_at: '2026-10-21T09:17:31Z'
  support: context_only
  summary: '[{"key": "chebi15377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377",
    "status": 200, "accessed_at": "2026-10-21T08:17:26.097802Z", "sha256": "de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b",
    "metadata_sha256": "2c0ebbd7fde625475a4ba4fbef85146d2fbcc07efb94eb3c832f6b1db4cdf5b7",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/117/chebi15377.json",
    "content_limit": null, "error": null}, {"key": "chebi17790", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17790",
    "status": 200, "accessed_at": "2026-10-21T08:00:47.448030Z", "sha256": "9954cafff5982d415d5fbed82fa4630ac9958247ed636b3c770976752ebd50de",
    "metadata_sha256": "8c0e3fa4c3a8156e35e88f3d04df6add920aeec41ce7739c1290fb8b7e1e68c3",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch010/093/chebi17790.json",
    "content_limit": null, "error": null}, {"key": "chebi2509", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509",
    "status": 200, "accessed_at": "2026-10-21T08:17:27.847373Z", "sha256": "8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a",
    "metadata_sha256": "a98ff777bd7cbd2d7dc4e6586a909b7e31d41144ed7978db3f48cc048aca624c",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/117/chebi2509.json",
    "content_limit": null, "error": null}, {"key": "nbrc947_attempt1_sandbox", "url":
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947", "status":
    null, "accessed_at": "2026-10-21T08:59:42.087852Z", "sha256": null, "metadata_sha256":
    "c0d5caa6018b3eedb62f618b40e332c9a5ede3e3aa4ce9fa90eb7100fd58dfd6", "reused_capture_from":
    null, "content_limit": "Failed transport attempt; no source content retrieved.",
    "error": "<urlopen error [Errno 8] nodename nor servname provided, or not known>"},
    {"key": "nbrc948_attempt1_sandbox", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=948",
    "status": null, "accessed_at": "2026-10-21T08:59:42.113852Z", "sha256": null,
    "metadata_sha256": "ba349300b6ee07e6ae049b0323f9796b73ecaba541380de7f6d69d9498c31895",
    "reused_capture_from": null, "content_limit": "Failed transport attempt; no source
    content retrieved.", "error": "<urlopen error [Errno 8] nodename nor servname
    provided, or not known>"}, {"key": "nbrc947", "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947",
    "status": 200, "accessed_at": "2026-10-21T09:00:09.929582Z", "sha256": "1812da0ace3aa9aaac3fc7abd785024606652b05e847229dd8bc1bcd37418b9e",
    "metadata_sha256": "ada80b94fc76bad51653280a629745724a00330191d498e74fc3c1d8cb80aef9",
    "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "nbrc948",
    "url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=948",
    "status": 200, "accessed_at": "2026-10-21T09:00:09.930200Z", "sha256": "b255d9a31c2518964dc1fc73631d2f14eb40dd99d252f86c862e7108900516ce",
    "metadata_sha256": "7637b8cf6399a2ad76ba6e72f57f9c2dc8150f8edfd770f6f6c9d520062515f2",
    "reused_capture_from": null, "content_limit": null, "error": null}]'
  snapshot_sha256: 68f03d0266c85ee84bbcf96d852064f1547e365fdf879c03ed4782f60a946c0a
- evidence_id: nbrc947
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947
  locator: Medium No. header; complete Medium Composition table, footnotes and Comment
    section
  accessed_at: '2026-10-21T09:00:09.929582Z'
  support: supports
  summary: Official NBRC 947 gives four quantified rows, unadjusted pH and separate
    methanol filtration. The full composition and comment fields were inspected.
  snapshot_sha256: 1812da0ace3aa9aaac3fc7abd785024606652b05e847229dd8bc1bcd37418b9e
- evidence_id: nbrc948
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=948
  locator: Medium No. header, complete composition and preparation; identity countercheck
    only
  accessed_at: '2026-10-21T09:00:09.930200Z'
  support: context_only
  summary: Actual NBRC 948 is YSG Medium, with separately sterilized solutions A and
    B. Its composition and preparation are not the source of this record.
  snapshot_sha256: b255d9a31c2518964dc1fc73631d2f14eb40dd99d252f86c862e7108900516ce
- evidence_id: amount-1
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947
  locator: 'Medium Composition table, quantified row 1: Bacto Marine Broth 2216 (Difco)'
  accessed_at: '2026-10-21T09:00:09.929582Z'
  support: supports
  summary: Exact source amount for owner ingredients[0].concentration; Named commercial
    broth; literal dry mass on the listed recipe basis. Source value and unit are
    37.4 g. The target retains this only inside its collapsed table string.
  quote: Bacto Marine Broth 2216 (Difco) 37.4 g
  snapshot_sha256: 1812da0ace3aa9aaac3fc7abd785024606652b05e847229dd8bc1bcd37418b9e
- evidence_id: amount-2
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947
  locator: 'Medium Composition table, quantified row 2: Methanol*'
  accessed_at: '2026-10-21T09:00:09.929582Z'
  support: supports
  summary: Exact source amount for owner ingredients[1].concentration; Separate filtration
    is explicit; this is a liquid dose, not a mass and not a measured final concentration.
    Source value and unit are 5 ml. The target retains this only inside its collapsed
    table string.
  quote: Methanol* 5 ml
  snapshot_sha256: 1812da0ace3aa9aaac3fc7abd785024606652b05e847229dd8bc1bcd37418b9e
- evidence_id: amount-3
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947
  locator: 'Medium Composition table, quantified row 3: Agar (if needed)'
  accessed_at: '2026-10-21T09:00:09.929582Z'
  support: supports
  summary: Exact source amount for owner ingredients[2].concentration; Optional solidification
    branch must remain conditional. Source value and unit are 15 g. The target retains
    this only inside its collapsed table string.
  quote: Agar (if needed) 15 g
  snapshot_sha256: 1812da0ace3aa9aaac3fc7abd785024606652b05e847229dd8bc1bcd37418b9e
- evidence_id: amount-4
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947
  locator: 'Medium Composition table, quantified row 4: Distilled water'
  accessed_at: '2026-10-21T09:00:09.929582Z'
  support: supports
  summary: Exact source amount for owner ingredients[3].concentration; Literal source
    water volume; no density conversion or final-volume inference. Source value and
    unit are 1 L. The target retains this only inside its collapsed table string.
  quote: Distilled water 1 L
  snapshot_sha256: 1812da0ace3aa9aaac3fc7abd785024606652b05e847229dd8bc1bcd37418b9e
- evidence_id: chebi17790
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17790
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:00:47.448030Z'
  support: supports
  summary: CHEBI:17790 resolves to canonical label methanol and is not obsolete. The
    complete response, including available formula, hydration, structure, synonyms
    and definitions, was inspected. Literal owner-label equality is assessed separately;
    ontology descriptions do not establish recipe quantities.
  snapshot_sha256: 9954cafff5982d415d5fbed82fa4630ac9958247ed636b3c770976752ebd50de
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
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to canonical label water and is not obsolete. The
    complete response, including available formula, hydration, structure, synonyms
    and definitions, was inspected. Literal owner-label equality is assessed separately;
    ontology descriptions do not establish recipe quantities.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact MAPPED/preferred_term rows for each asserted secondary key; adjacent
    pinned metadata
  accessed_at: '2026-10-21T09:17:31Z'
  support: supports
  summary: '{"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count":
    9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id",
    "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech",
    "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"},
    "counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances":
    0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances":
    0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent":
    0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 4,
    "primary_ontology_instances": 3, "primary_CHEBI_instances": 3, "canonical_primary_label_instances":
    1, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent":
    75.0, "primary_CHEBI_percent": 75.0, "secondary_verified_percent": 0.0}}, "secondary_instances":
    []}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: _map_ingredients; _map_preparation_steps; _infer_medium_type
  accessed_at: '2026-10-21T09:17:31Z'
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
  accessed_at: '2026-10-21T09:17:31Z'
  support: context_only
  summary: 'Current recovery code parses explicit composition rows and separate footnote
    stock sections from #medium-comp and records recovery history. Its presence and
    later owner data do not prove the generated merged record was regenerated.'
- evidence_id: exporter
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: transform; medium_to_ingredient_edge; _resolved_ingredient_id; nodes
  accessed_at: '2026-10-21T09:17:31Z'
  support: context_only
  summary: The current exporter walks structured ingredient rows and uses a MIM resolver
    before local identity fallback; it returns no ingredient edge if resolution yields
    no identity. A missing explicit term alone does not establish a zero-edge export.
    No export was executed or edge count asserted. The record type is also consumed
    for node/type semantics, so source-unsupported classification is consequential.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/948.yaml
  locator: Every timestamp in target, owner and explicitly listed contextual dependencies
  accessed_at: '2026-10-21T09:17:31Z'
  support: supports
  summary: '[{"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-02-20T00:22:35.997170Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[1].timestamp",
    "value": "2026-03-13T03:08:43.445251Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[2].timestamp",
    "value": "2026-03-13T06:19:49.291053Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-05-16T09:03:06.754368+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/948.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-08-06T03:05:04.701669+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-02-20T00:22:35.997170Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[1].timestamp",
    "value": "2026-03-13T03:08:43.445251Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[2].timestamp",
    "value": "2026-03-13T06:19:49.291053Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-05-16T09:03:06.754368+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-08-19T21:54:23.090770+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[6].timestamp",
    "value": "2026-08-20T19:01:16.174901+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field": "curation_history[7].timestamp",
    "value": "2026-09-07T00:00:00-07:00", "valid_ISO_datetime": true, "timezone_aware":
    true}]'
- evidence_id: methanol-preparation
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947
  locator: Composition footnote attached to Methanol*
  accessed_at: '2026-10-21T09:00:09.929582Z'
  support: supports
  summary: The asterisk attaches separate filtration to the methanol addition; it
    does not prescribe whole-medium autoclaving.
  quote: '*Sterilize separately by filtration.'
  snapshot_sha256: 1812da0ace3aa9aaac3fc7abd785024606652b05e847229dd8bc1bcd37418b9e
- evidence_id: source-ph
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=947
  locator: Composition text after the water row
  accessed_at: '2026-10-21T09:00:09.929582Z'
  support: supports
  summary: The source explicitly retains unadjusted pH, not a missing numeric pH to
    fill from a neighboring medium.
  quote: pH unadjusted
  snapshot_sha256: 1812da0ace3aa9aaac3fc7abd785024606652b05e847229dd8bc1bcd37418b9e
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: NBRC 947 provenance despite local 948 label
  outcome: supported
  summary: The stable CultureMech ID, merge source basename, import-history accession
    947, maintained owner source term and captured primary page resolve one medium.
    The local name 948 does not license substitution of actual NBRC 948; that different
    source is only an identity countercheck. The legacy HTTP import URL was read as
    provenance, not represented as a newly retrieved response.
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - record
  - owner-0
  - nbrc947
  - nbrc948
- assessment_id: amounts
  area: quantity
  topic: Every target row and every recovered source amount
  outcome: concern
  summary: 'The target has two malformed direct ingredient rows: one collapsed table
    at VARIABLE and an empty name with ''Bacto Marine Broth 2216 (Difco)'' as its
    g/L value. The 4 separate owner rows preserve the inspected source amounts and
    units as itemized. Solid masses expressed by the owner per liter are interpreted
    on the nominal listed recipe basis, without claiming that a source water amount
    establishes measured final volume.'
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - record
  - owner-0
  - nbrc947
  - amount-1
  - amount-2
  - amount-3
  - amount-4
  details: '{"recovered_source_amounts": [{"owner_field": "ingredients[0].concentration",
    "name": "Bacto Marine Broth 2216 (Difco)", "owner_value": "37.4", "owner_unit":
    "G_PER_L", "source_amount": "37.4", "source_unit": "g", "source_quote": "Bacto
    Marine Broth 2216 (Difco) 37.4 g", "source_locator": "Medium Composition quantified
    row 1", "condition": "Named commercial broth; literal dry mass on the listed recipe
    basis.", "decision": "evidence_only", "decision_rationale": "Literal source amount
    is supported; ingredient-level evidence is absent from the owner. Source masses
    use the nominal listed recipe basis, not independently measured final volume.",
    "target_correspondence": "Embedded text only; no equivalent usable direct ingredient
    row", "evidence_id": "amount-1"}, {"owner_field": "ingredients[1].concentration",
    "name": "Methanol*", "owner_value": "5", "owner_unit": "ML_PER_L", "source_amount":
    "5", "source_unit": "ml", "source_quote": "Methanol* 5 ml", "source_locator":
    "Medium Composition quantified row 2", "condition": "Separate filtration is explicit;
    this is a liquid dose, not a mass and not a measured final concentration.", "decision":
    "evidence_only", "decision_rationale": "Literal liquid amount is supported but
    lacks ingredient-level source evidence; no mass conversion is asserted.", "target_correspondence":
    "Embedded text only; no equivalent usable direct ingredient row", "evidence_id":
    "amount-2"}, {"owner_field": "ingredients[2].concentration", "name": "Agar (if
    needed)", "owner_value": "15", "owner_unit": "G_PER_L", "source_amount": "15",
    "source_unit": "g", "source_quote": "Agar (if needed) 15 g", "source_locator":
    "Medium Composition quantified row 3", "condition": "Optional solidification branch
    must remain conditional.", "decision": "evidence_only", "decision_rationale":
    "Literal source amount is supported; ingredient-level evidence is absent from
    the owner. Source masses use the nominal listed recipe basis, not independently
    measured final volume.", "target_correspondence": "Embedded text only; no equivalent
    usable direct ingredient row", "evidence_id": "amount-3"}, {"owner_field": "ingredients[3].concentration",
    "name": "Distilled water", "owner_value": "1", "owner_unit": "L", "source_amount":
    "1", "source_unit": "L", "source_quote": "Distilled water 1 L", "source_locator":
    "Medium Composition quantified row 4", "condition": "Literal source water volume;
    no density conversion or final-volume inference.", "decision": "evidence_only",
    "decision_rationale": "Literal liquid amount is supported but lacks ingredient-level
    source evidence; no mass conversion is asserted.", "target_correspondence": "Embedded
    text only; no equivalent usable direct ingredient row", "evidence_id": "amount-4"}],
    "target_malformed_claims": [{"field_path": "ingredients[0].concentration", "current":
    {"value": "variable", "unit": "VARIABLE"}, "decision": "unsupported", "source_quote":
    "Bacto Marine Broth 2216 (Difco) 37.4 g", "source_locator": "Medium Composition
    quantified row 1", "evidence_ids": ["nbrc947", "amount-1"], "rationale": "A collapsed
    multi-ingredient string or empty ingredient cannot be assigned one source concentration.
    Recover all explicit source rows rather than treating this malformed claim as
    a number."}, {"field_path": "ingredients[1].concentration", "current": {"value":
    "Bacto Marine Broth 2216 (Difco)", "unit": "G_PER_L"}, "decision": "unsupported",
    "source_quote": "Bacto Marine Broth 2216 (Difco) 37.4 g", "source_locator": "Medium
    Composition quantified row 1", "evidence_ids": ["nbrc947", "amount-1"], "rationale":
    "A collapsed multi-ingredient string or empty ingredient cannot be assigned one
    source concentration. Recover all explicit source rows rather than treating this
    malformed claim as a number."}]}'
- assessment_id: grounding
  area: grounding
  topic: All asserted primary IDs, canonical labels and current secondary keys
  outcome: concern
  summary: The generated target has 0/2 primary ontology links and 0/2 verified secondary
    links. The owner has 3/4 primary ontology links, including 3 CHEBI instances,
    and 0/4 verified secondary links. 2 owner primary labels differ from canonical
    labels. These are separate layer-specific linkage denominators on a 0–100 scale,
    not scientific accuracy scores. No secondary denominator of zero is invented when
    no keys are asserted.
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi17790
  - chebi2509
  - chebi15377
  details: '{"counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances":
    0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances":
    0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent":
    0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 4,
    "primary_ontology_instances": 3, "primary_CHEBI_instances": 3, "canonical_primary_label_instances":
    1, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent":
    75.0, "primary_CHEBI_percent": 75.0, "secondary_verified_percent": 0.0}}, "label_drift":
    [{"field_path": "ingredients[1].term.label", "id": "CHEBI:17790", "asserted_label":
    "Methanol", "canonical_label": "methanol", "source_key": "chebi17790"}, {"field_path":
    "ingredients[2].term.label", "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label":
    "agar", "source_key": "chebi2509"}], "instances": [{"layer": "target", "path":
    "data/merge_yaml/merged/948.yaml", "field": "ingredients[0]", "preferred_term":
    "Bacto Marine Broth 2216 (Difco)37.4gMethanol*5mlAgar (if needed)15gDistilled
    water1LpH unadjusted*Sterilize separately by filtration."}, {"layer": "target",
    "path": "data/merge_yaml/merged/948.yaml", "field": "ingredients[1]", "preferred_term":
    ""}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_948.yaml",
    "field": "ingredients[0]", "preferred_term": "Bacto Marine Broth 2216 (Difco)"},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field":
    "ingredients[1]", "preferred_term": "Methanol*", "primary_id": "CHEBI:17790",
    "asserted_label": "Methanol", "canonical_label": "methanol", "label_equal": false,
    "source_key": "chebi17790", "description": ["The primary alcohol that is the simplest
    aliphatic alcohol, comprising a methyl and an alcohol group."], "synonyms": ["CH3OH",
    "METHANOL", "METHANOL", "MeOH", "Methanol", "Methanol", "Methyl alcohol", "Methylalkohol",
    "carbinol", "methanol", "methanol", "spirit of wood", "wood alcohol", "wood naphtha",
    "wood spirit"], "form_annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:67-56-1", "gmelin:449", "hmdb:HMDB0001875", "kegg.compound:C00132", "kegg.drug:D02309",
    "metacyc.compound:METOH", "pdb-ccd:MOH", "pubmed:11141607", "pubmed:11430978",
    "pubmed:11489599", "pubmed:11680737", "pubmed:11684179", "pubmed:14012711", "pubmed:14678513",
    "pubmed:14760634", "pubmed:15172721", "pubmed:15906011", "pubmed:16705261", "pubmed:17451998",
    "pubmed:17733096", "pubmed:19064074", "pubmed:19850112", "pubmed:20314698", "reaxys:1098229",
    "umbbd.compound:c0132", "wikipedia.en:Methanol"], "generalized_empirical_formula":
    ["CH4O"], "has_alternative_id": ["CHEBI:14588", "CHEBI:25227", "CHEBI:44080",
    "CHEBI:44553", "CHEBI:6816"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17790"],
    "inchi_key_string": ["OKKJLVBELUTLKV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/CH4O/c1-2/h2H,1H3"],
    "mass": ["32.042"], "monoisotopic_mass": ["32.02621"], "smiles_string": ["CO"]}},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_948.yaml", "field":
    "ingredients[2]", "preferred_term": "Agar (if needed)", "primary_id": "CHEBI:2509",
    "asserted_label": "Agar", "canonical_label": "agar", "label_equal": false, "source_key":
    "chebi2509", "description": ["A complex mixture of polysaccharides extracted from
    species of red algae. Its two main components are agarose and agaropectin. Agarose
    is the component responsible for the high-strength gelling properties of agar,
    while agaropectin provides the viscous properties."], "synonyms": [], "form_annotations":
    {"database_cross_reference": ["cas:9002-18-0", "kegg.compound:C08815", "pubmed:25603143",
    "pubmed:25842535", "pubmed:25959629", "pubmed:26043937", "pubmed:26050892", "pubmed:26116384",
    "reaxys:8538728", "wikipedia.en:Agar"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:2509"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_948.yaml",
    "field": "ingredients[3]", "preferred_term": "Distilled water", "primary_id":
    "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_equal":
    true, "source_key": "chebi15377", "description": ["An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms"], "synonyms":
    ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water",
    "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau",
    "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117",
    "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER",
    "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula":
    ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043",
    "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string":
    ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass":
    ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]}}]}'
- assessment_id: forms
  area: grounding
  topic: Source ingredient identities, mixtures and exact chemical forms
  outcome: supported
  summary: CHEBI:17790 is neutral methanol with matching formula and structural annotation;
    its source dose remains 5 mL. CHEBI:2509 denotes the agar mixture, and CHEBI:15377
    denotes water. Methanol and Agar are literal label differences, not wrong-ID findings.
    The commercial broth remains ungrounded rather than receiving an invented molecular
    identifier.
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - record
  - owner-0
  - nbrc947
  - chebi17790
  - chebi2509
  - chebi15377
- assessment_id: conditions
  area: consistency
  topic: Preparation, pH and physical-state conditions
  outcome: concern
  summary: The owner retains the source-specific methanol filtration step and unadjusted-pH
    note. The target instead has generic dissolve, adjust-pH and autoclaving prose,
    with the last action misclassified as DISSOLVE. Its collapsed text contains the
    filtration footnote but does not preserve it as an operative preparation step.
    The source supplies no numeric pH and no autoclaving instruction for the whole
    formulation.
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - record
  - owner-0
  - nbrc947
  - importer
- assessment_id: classification
  area: scope
  topic: Classification and bounded biological claims
  outcome: concern
  summary: Both layers assert DEFINED/DEFINED despite the named commercial broth.
    Its constituent chemical composition is not defined by this source. Both also
    assert SOLID_AGAR while preserving optional agar without documenting branch selection;
    a solid formulation is supported only if agar is used. Neither target nor owner
    asserts organisms, strains, taxon IDs, assemblies, DOI/PMID papers, growth outcomes,
    parent media or variants. Source catalogue scope is not experimental growth evidence.
    Optional omissions are not populated with invented organisms.
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - record
  - owner-0
  - nbrc947
  - nbrc948
  - exporter
- assessment_id: owner-correspondence
  area: ownership
  topic: Maintained recovery versus generated representation
  outcome: concern
  summary: The generated August merge precedes later owner recovery and source metadata.
    The owner now contains 4 explicit source rows and an official source term/reference;
    the target retains two collapsed rows and no structured source term/reference.
    Owner label differences must be corrected before regeneration.
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - record
  - owner-0
  - nbrc947
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
  - CultureMech:007507
  evidence_ids:
  - record
  - owner-0
  - nbrc947
  - validate-references
- assessment_id: history
  area: provenance
  topic: Append-only event history and timestamp interpretation
  outcome: supported
  summary: All 14 scoped timestamps were checked for ISO syntax and timezone. Every
    instance parses and has an explicit timezone. Curation events are process provenance
    rather than independent confirmation of recipe correctness.
  target_ids:
  - CultureMech:007507
  evidence_ids:
  - record
  - owner-0
  - history
  details: '[]'
findings:
- finding_id: f1
  issue_key: cm007507-stale-collapsed-source947-formula
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated target loses the recovered four-row NBRC 947 formula
  description: The whole-table string at VARIABLE and an empty ingredient whose g/L
    value is a product name do not encode a usable named formulation. The owner has
    the four explicit source rows and official source reference. Optional agar remains
    conditional, yet neither layer documents choosing the solid branch. Native P1
    reflects unusable scientific representation; this is not P1.1 or a reported schema-validation
    failure.
  target_ids:
  - CultureMech:007507
  field_paths:
  - ingredients
  - media_term
  - references
  - physical_state
  evidence_ids:
  - record
  - owner-0
  - nbrc947
  - recovery
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_948.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm007507-source-preparation-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated preparation loses methanol filtration and unadjusted pH
  description: The source requires separate filtration of Methanol* and says pH unadjusted.
    The target instead presents generic pH adjustment and autoclaving, with autoclaving
    tagged DISSOLVE. A footnote buried inside one malformed ingredient string is insufficient
    to preserve the preparation boundary. The maintained owner already supplies the
    filtration instruction and source pH note. Following the generated procedure could
    change the source preparation.
  target_ids:
  - CultureMech:007507
  field_paths:
  - preparation_steps
  - ingredients[0].preferred_term
  evidence_ids:
  - record
  - owner-0
  - nbrc947
  - methanol-preparation
  - source-ph
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_948.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: cm007507-unsupported-defined-classification
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Defined classification lacks source support
  description: Both maintained and generated layers declare medium_type DEFINED and
    composition_type DEFINED. The exact source names a commercial marine broth without
    its full constituent specification. The inspected evidence therefore cannot verify
    the defined-composition assertions; the commercial product name alone also does
    not establish the replacement classification. This concerns formulation classification,
    not bacterial-folder mismatch under P2.4.
  target_ids:
  - CultureMech:007507
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - nbrc947
  - importer
  - exporter
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_948.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: cm007507-owner-canonical-label-drift
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Two maintained owner labels differ from canonical labels
  description: '[{"field_path": "ingredients[1].term.label", "id": "CHEBI:17790",
    "asserted_label": "Methanol", "canonical_label": "methanol", "source_key": "chebi17790"},
    {"field_path": "ingredients[2].term.label", "id": "CHEBI:2509", "asserted_label":
    "Agar", "canonical_label": "agar", "source_key": "chebi2509"}] These label differences
    do not by themselves imply wrong chemical identifiers.'
  target_ids:
  - CultureMech:007507
  field_paths:
  - owner:data/normalized_yaml/bacterial/NBRC_948.yaml:ingredients[1].term.label
  - owner:data/normalized_yaml/bacterial/NBRC_948.yaml:ingredients[2].term.label
  evidence_ids:
  - owner-0
  - chebi17790
  - chebi2509
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_948.yaml
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
  description: Verify and retain all four maintained rows with exact source units,
    add their scoped evidence, explicitly qualify optional agar, resolve the owner
    issues below, and regenerate the derived record with its stable ID and exact NBRC
    947 identity.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007507
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_948.yaml
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
  description: Preserve separate methanol filtration and unadjusted pH in the maintained
    preparation representation, and regenerate without unsupported whole-medium autoclaving.
    Retain unknown filtration pore size, base sterilization parameters and final volume
    rather than inventing them.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007507
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_948.yaml
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
  description: Verify the exact commercial product specification and reassess the
    maintained classification against its documented composition before regeneration.
    Retain the uncertainty if that specification is unavailable, and verify that any
    evidence-supported classification survives record/type export. Do not infer an
    undisclosed composition or mandate COMPLEX from the product name alone.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007507
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_948.yaml
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
  description: Use the verified canonical labels for the existing IDs while retaining
    Methanol* and Agar (if needed) as source preferred terms; preserve dose, filtration
    and optionality.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007507
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_948.yaml
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
- The source lists 1 L water plus 5 mL methanol; it does not give a measured final
  volume. The source title says 0.5% Methanol, but no new exact final-volume percentage
  or mass concentration is derived.
- Bacto Marine Broth 2216 (Difco) remains an opaque commercial mixture. No constituent
  composition, manufacturer lot specification or invented pure-chemical grounding
  is supplied.
- Agar is optional. Neither layer documents selecting the solid branch. No liquid/solid
  variant record was created.
- The primary source specifies methanol filtration but gives no membrane size, base-medium
  autoclave cycle, incubation, storage or organism-specific growth evidence. Such
  details remain unknown.
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
