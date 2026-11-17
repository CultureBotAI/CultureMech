# Source and formulation review: 892 (CultureMech:007502)

- Review: 20261021T085617Z-culturemech-007502-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:49:01Z
- Finished UTC: 2026-10-21T08:56:17Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

This stable record denotes NBRC 891 Soybean Casein Digest Agar, as shown by its import provenance, recovered owner and exact repair writer. The generated 892 target remains a collapsed table plus an empty ingredient, losing five source rows, the official title/accession, pH 7.1–7.5 and source-specific owner preparation. The owner retains two noncanonical FoodOn labels for broader protein-hydrolysate classes. The target’s autoclaving fallback lacks source support and has action DISSOLVE. All four diagnostics pass despite these semantic defects.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 118; batch 012 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eleven task batches contain 110 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 112 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007502 | data/merge_yaml/merged/892.yaml | generated | 892 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007502 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007502 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch012/118/strict.tsv |
| validate-terms | passed | True | CultureMech:007502 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007502 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007502 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped history timestamp syntax and timezone check | passed | False | CultureMech:007502 | 14 timestamp instances inspected; 0 malformed or timezone-naive instances. Existing provenance is preserved; no timestamps were rewritten. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007502.

The four documented recipes completed; interpret the scope of each separately.

### NBRC 891 provenance despite local 892 label

identity: supported. Targets: CultureMech:007502.

The stable CultureMech ID, merge source basename, import-history accession 891, maintained owner source term and captured primary page resolve one medium. The local name 892 does not license substitution of actual NBRC 892; that different source is only an identity countercheck. The legacy HTTP import URL was read as provenance, not represented as a newly retrieved response.

### Every target row and every recovered source amount

quantity: concern. Targets: CultureMech:007502.

The target has two malformed direct ingredient rows: one collapsed table at VARIABLE and an empty name with 'Casein peptone' as its g/L value. The 5 separate owner rows preserve the inspected source amounts and units as itemized. Solid masses expressed by the owner per liter are interpreted on the nominal listed recipe basis, without claiming that a source water amount establishes measured final volume.

[{"owner_field": "ingredients[0].concentration", "name": "Casein peptone", "owner_value": "15", "owner_unit": "G_PER_L", "source_amount": "15", "source_unit": "g", "source_quote": "Casein peptone 15 g", "source_locator": "Medium Composition quantified row 1", "condition": "Source-specific casein hydrolysate identity retained; not a pure defined molecule.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-1"}, {"owner_field": "ingredients[1].concentration", "name": "Soybean peptone", "owner_value": "5", "owner_unit": "G_PER_L", "source_amount": "5", "source_unit": "g", "source_quote": "Soybean peptone 5 g", "source_locator": "Medium Composition quantified row 2", "condition": "Source-specific soybean hydrolysate identity retained; not interchangeable with an arbitrary plant hydrolysate.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-2"}, {"owner_field": "ingredients[2].concentration", "name": "NaCl", "owner_value": "5", "owner_unit": "G_PER_L", "source_amount": "5", "source_unit": "g", "source_quote": "NaCl 5 g", "source_locator": "Medium Composition quantified row 3", "condition": "Source sodium chloride mass; no hydration form is additionally asserted.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-3"}, {"owner_field": "ingredients[3].concentration", "name": "Agar", "owner_value": "15", "owner_unit": "G_PER_L", "source_amount": "15", "source_unit": "g", "source_quote": "Agar 15 g", "source_locator": "Medium Composition quantified row 4", "condition": "Agar is listed without an optional condition in this exact recipe.", "decision": "verified", "decision_rationale": "Source amount verified on the nominal batch basis; final volume is not independently established.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-4"}, {"owner_field": "ingredients[4].concentration", "name": "Distilled water", "owner_value": "1", "owner_unit": "L", "source_amount": "1", "source_unit": "L", "source_quote": "Distilled water 1 L", "source_locator": "Medium Composition quantified row 5", "condition": "Literal solvent amount; not a gram or independently verified final-volume instruction.", "decision": "verified", "decision_rationale": "Literal liquid amount verified; no mass conversion is asserted.", "target_correspondence": "Embedded text only; no equivalent usable direct ingredient row", "evidence_id": "amount-5"}]

### All asserted primary IDs, canonical labels and current secondary keys

grounding: concern. Targets: CultureMech:007502.

The generated target has 0/2 primary ontology links and 0/2 secondary links. The owner has 5/5 primary ontology links, including 3 CHEBI instances, and 3/5 verified secondary links. 2 owner primary labels differ from canonical labels. These are separate layer-specific linkage denominators on a 0–100 scale, not scientific accuracy scores. No secondary denominator of zero is invented when no keys are asserted.

{"counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances": 0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent": 0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 5, "primary_ontology_instances": 5, "primary_CHEBI_instances": 3, "canonical_primary_label_instances": 3, "secondary_asserted_instances": 3, "secondary_verified_instances": 3, "primary_ontology_percent": 100.0, "primary_CHEBI_percent": 60.0, "secondary_verified_percent": 60.0}}, "label_drift": [{"field_path": "ingredients[0].term.label", "id": "FOODON:03315719", "asserted_label": "Casein peptone", "canonical_label": "mammalian milk protein (hydrolyzed)", "source_key": "foodon03315719"}, {"field_path": "ingredients[1].term.label", "id": "FOODON:03315720", "asserted_label": "Soy peptone", "canonical_label": "vegetable protein, hydrolyzed", "source_key": "foodon03315720"}], "instances": [{"layer": "target", "path": "data/merge_yaml/merged/892.yaml", "field": "ingredients[0]", "preferred_term": "Casein peptone15gSoybean peptone5gNaCl5gAgar15gDistilled water1LpH 7.1-7.5"}, {"layer": "target", "path": "data/merge_yaml/merged/892.yaml", "field": "ingredients[1]", "preferred_term": ""}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "ingredients[0]", "preferred_term": "Casein peptone", "primary_id": "FOODON:03315719", "asserted_label": "Casein peptone", "canonical_label": "mammalian milk protein (hydrolyzed)", "label_equal": false, "source_key": "foodon03315719", "description": ["SIREN DB annotation:\n* casein FOODON:03420180\n* food hydrolyzation process FOODON:03460277"], "synonyms": [], "form_annotations": {"database_cross_reference": ["https://bioregistry.io/reference/siren:F15719"], "has curation status": ["http://purl.obolibrary.org/obo/IAO_0000428"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "ingredients[1]", "preferred_term": "Soybean peptone", "primary_id": "FOODON:03315720", "asserted_label": "Soy peptone", "canonical_label": "vegetable protein, hydrolyzed", "label_equal": false, "source_key": "foodon03315720", "description": ["SIREN DB annotation:\n* protein extract, concentrate or isolate FOODON:03420236\n* food hydrolyzation process FOODON:03460277"], "synonyms": [], "form_annotations": {"database_cross_reference": ["https://bioregistry.io/reference/siren:F15720"], "has curation status": ["http://purl.obolibrary.org/obo/IAO_0000428"]}}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "ingredients[2]", "preferred_term": "NaCl", "primary_id": "CHEBI:26710", "asserted_label": "sodium chloride", "canonical_label": "sodium chloride", "label_equal": true, "source_key": "chebi26710", "description": ["An inorganic chloride salt having sodium(1+) as the counterion."], "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}, "secondary_id": "CHEBI:26710", "secondary_asserted_label": "sodium chloride", "secondary_index_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "ingredients[3]", "preferred_term": "Agar", "primary_id": "CHEBI:2509", "asserted_label": "agar", "canonical_label": "agar", "label_equal": true, "source_key": "chebi2509", "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "synonyms": [], "form_annotations": {"database_cross_reference": ["cas:9002-18-0", "kegg.compound:C08815", "pubmed:25603143", "pubmed:25842535", "pubmed:25959629", "pubmed:26043937", "pubmed:26050892", "pubmed:26116384", "reaxys:8538728", "wikipedia.en:Agar"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:2509"]}, "secondary_id": "CHEBI:2509", "secondary_asserted_label": "agar", "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "ingredients[4]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_equal": true, "source_key": "chebi15377", "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]}, "secondary_id": "CHEBI:15377", "secondary_asserted_label": "water", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}]}

### Source ingredient identities, mixtures and exact chemical forms

grounding: supported. Targets: CultureMech:007502.

CHEBI identifies sodium chloride, agar and water consistently with the source, and all three asserted secondary keys have exact MAPPED/preferred_term rows in the pinned MIM index. FoodOn 03315719 is mammalian milk protein (hydrolyzed), whose description includes casein; FoodOn 03315720 is the broader vegetable protein, hydrolyzed class. These support class-level hydrolysate context rather than supplier-specific formulations. Their owner term labels are not canonical and must be distinguished from the source-specific preferred terms. No wrong-ID or exact peptone-equivalence claim is inferred solely from these broader labels.

### Preparation, pH and physical-state conditions

consistency: concern. Targets: CultureMech:007502.

Source pH 7.1–7.5 is correctly structured in the owner and missing in the target. Owner preparation identifies the exact ingredient set and adjustment to this range; it does not claim a sterilization protocol. The target instead has generic steps and unsupported Sterilize by autoclaving with action DISSOLVE. Source agar is unconditional, supporting the solid recipe.

### Classification and bounded biological claims

scope: supported. Targets: CultureMech:007502.

COMPLEX/UNDEFINED and SOLID_AGAR agree with the two peptones and the stated 15 g agar. No chemically defined interpretation is implied by ontology links to broad hydrolysate classes. Neither target nor owner asserts organisms, strains, taxon IDs, assemblies, DOI/PMID papers, growth outcomes, parent media or variants. Source catalogue scope is not experimental growth evidence. Optional omissions are not populated with invented organisms.

### Maintained recovery versus generated representation

ownership: concern. Targets: CultureMech:007502.

The generated August merge precedes later owner recovery and source metadata. The owner now contains 5 explicit source rows and an official source term/reference; the target retains two collapsed rows and no structured source term/reference. Owner label differences must be corrected before regeneration. The exact maintained repair writer pins CultureMech:007502 at NBRC_892.yaml to NBRC source 891 and adds the official title, source term, pH range, canonical CHEBI links and source-specific preparation. Its FoodOn labels still require the reported correction.

### Claim-level amount evidence and checked reference scope

evidence: concern. Targets: CultureMech:007502.

Each source amount is traced to an exact table row above. The owner has the official recipe reference but lacks ingredient-level amount evidence; the target has no structured reference and its reference checker checked zero entries. Add scoped amount evidence while recovering the structured formulation, retaining source batch and condition qualifiers. Ontology citations verify identities and labels rather than recipe amounts. No separate paper was asserted or required to identify this catalogue recipe.

### Append-only event history and timestamp interpretation

provenance: supported. Targets: CultureMech:007502.

All 14 scoped timestamps were checked for ISO syntax and timezone. Every instance parses and has an explicit timezone. Curation events are process provenance rather than independent confirmation of recipe correctness.

[]

## Findings

### f1: Generated target loses the recovered 5-row NBRC 891 formula

blocker / open / confirmed; issue key: cm007502-stale-collapsed-source891-formula.

The whole-table ingredient string at VARIABLE and the empty ingredient with a reagent name as a g/L value cannot represent a usable named formulation. The owner already has 5 explicit source rows and the official source accession/reference, with source conditions where stated. This prevents faithful scientific use of the generated formulation despite all four documented checks passing. Native P1 reflects unusable identity/representation; this is not P1.1 and is not a reported schema-validator failure.

### f2: Generated autoclaving is unsupported and action-mismatched

major / open / confirmed; issue key: cm007502-unsupported-default-autoclave.

The inspected exact NBRC 891 page does not provide a sterilization protocol. The target nevertheless states Sterilize by autoclaving with action DISSOLVE, matching the importer fallback and keyword mismatch. The current owner has already removed that generic autoclaving instruction; the stale generated instruction should not be reintroduced as primary-source evidence. Neither a neighboring accession nor a routine laboratory convention supplies missing source-specific support.

### f3: Maintained owner labels differ from canonical ontology labels

minor / open / confirmed; issue key: cm007502-owner-canonical-label-drift.

[{"field_path": "ingredients[0].term.label", "id": "FOODON:03315719", "asserted_label": "Casein peptone", "canonical_label": "mammalian milk protein (hydrolyzed)", "source_key": "foodon03315719"}, {"field_path": "ingredients[1].term.label", "id": "FOODON:03315720", "asserted_label": "Soy peptone", "canonical_label": "vegetable protein, hydrolyzed", "source_key": "foodon03315720"}] These are literal label differences in the maintained input and would propagate on regeneration. They do not by themselves prove that the asserted ontology IDs identify the wrong substances; preserve supplier/source names in preferred_term and exact recipe forms separately.

## Recommended Actions And Acceptance Checks

### a1

Verify the maintained source rows and their exact forms/units against the bound primary page, correct owner label or classification issues listed separately, add scoped amount evidence, and regenerate derived records while retaining the same stable ID and source accession.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain supported source pH/formulation details and regenerate from the verified owner without the unsupported default. Any later sterilization instruction needs exact source support and a corresponding action; keep unknown time, temperature and procedure explicit.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Update only the canonical term labels after verifying the same IDs and source-specific ingredient identities. Preserve source names, brands, supplied hydration forms and amounts, then ensure regeneration keeps both canonical labels and preferred terms. Run the documented ID-label correspondence check on the authorized correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/892.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_892.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/892.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/892.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch012/118/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch012/118/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/892.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/892.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| nbrc891 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891; Medium No. header; complete Medium Composition table, footnotes and Comment section | supports | Read the full official NBRC 891 Soybean Casein Digest Agar page: casein peptone 15 g, soybean peptone 5 g, NaCl 5 g, agar 15 g and distilled water 1 L; pH 7.1–7.5. The page contains no detailed sterilization instructions. |
| nbrc892 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=892; Medium No. header, complete composition and preparation; identity countercheck only | context_only | Actual NBRC 892 is Soybean Casein Digest Broth: casein/soybean peptones 17/3 g with K2HPO4 and glucose each 2.5 g, NaCl 5 g and water 1 L. It lacks the target source’s agar and is not a replacement formula for source 891. |
| amount-1 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891; Medium Composition table, quantified row 1: Casein peptone | supports | Exact source amount for owner ingredients[0].concentration; Source-specific casein hydrolysate identity retained; not a pure defined molecule. Source value and unit are 15 g. The target retains this only inside its collapsed table string. |
| amount-2 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891; Medium Composition table, quantified row 2: Soybean peptone | supports | Exact source amount for owner ingredients[1].concentration; Source-specific soybean hydrolysate identity retained; not interchangeable with an arbitrary plant hydrolysate. Source value and unit are 5 g. The target retains this only inside its collapsed table string. |
| amount-3 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891; Medium Composition table, quantified row 3: NaCl | supports | Exact source amount for owner ingredients[2].concentration; Source sodium chloride mass; no hydration form is additionally asserted. Source value and unit are 5 g. The target retains this only inside its collapsed table string. |
| amount-4 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891; Medium Composition table, quantified row 4: Agar | supports | Exact source amount for owner ingredients[3].concentration; Agar is listed without an optional condition in this exact recipe. Source value and unit are 15 g. The target retains this only inside its collapsed table string. |
| amount-5 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891; Medium Composition table, quantified row 5: Distilled water | supports | Exact source amount for owner ingredients[4].concentration; Literal solvent amount; not a gram or independently verified final-volume instruction. Source value and unit are 1 L. The target retains this only inside its collapsed table string. |
| foodon03315719 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315719; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | FOODON:03315719 resolves to canonical label mammalian milk protein (hydrolyzed) and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| foodon03315720 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315720; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | FOODON:03315720 resolves to canonical label vegetable protein, hydrolyzed and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:26710 resolves to canonical label sodium chloride and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:2509 resolves to canonical label agar and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms and annotation | supports | CHEBI:15377 resolves to canonical label water and is not obsolete. The complete response, including available formula, hydration, structure, synonyms and definitions, was inspected. Literal owner-label equality is assessed separately; ontology descriptions do not establish recipe quantities. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact MAPPED/preferred_term rows for each asserted secondary key; adjacent pinned metadata | supports | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances": 0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances": 0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent": 0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 5, "primary_ontology_instances": 5, "primary_CHEBI_instances": 3, "canonical_primary_label_instances": 3, "secondary_asserted_instances": 3, "secondary_verified_instances": 3, "primary_ontology_percent": 100.0, "primary_CHEBI_percent": 60.0, "secondary_verified_percent": 60.0}}, "secondary_instances": [{"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "ingredients[2]", "preferred_term": "NaCl", "primary_id": "CHEBI:26710", "asserted_label": "sodium chloride", "canonical_label": "sodium chloride", "label_equal": true, "source_key": "chebi26710", "description": ["An inorganic chloride salt having sodium(1+) as the counterion."], "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}, "secondary_id": "CHEBI:26710", "secondary_asserted_label": "sodium chloride", "secondary_index_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "ingredients[3]", "preferred_term": "Agar", "primary_id": "CHEBI:2509", "asserted_label": "agar", "canonical_label": "agar", "label_equal": true, "source_key": "chebi2509", "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "synonyms": [], "form_annotations": {"database_cross_reference": ["cas:9002-18-0", "kegg.compound:C08815", "pubmed:25603143", "pubmed:25842535", "pubmed:25959629", "pubmed:26043937", "pubmed:26050892", "pubmed:26116384", "reaxys:8538728", "wikipedia.en:Agar"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:2509"]}, "secondary_id": "CHEBI:2509", "secondary_asserted_label": "agar", "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "ingredients[4]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_equal": true, "source_key": "chebi15377", "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]}, "secondary_id": "CHEBI:15377", "secondary_asserted_label": "water", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}]} |
| importer | src/culturemech/import/nbrc_importer.py; _map_ingredients; _map_preparation_steps; _infer_medium_type | context_only | Current importer maps quantities mechanically and creates generic dissolve, adjust-pH and autoclaving prose when preparation text is absent. Its action test uses the substring autoclave, which is not present in autoclaving, explaining the generated DISSOLVE action. The classification heuristic can use parentheses as a defined-medium hint. Code inspection is not a historical execution replay. |
| recovery | scripts/recover_nbrc_composition.py; parse_composition; recover | context_only | Current recovery code parses explicit composition rows and separate footnote stock sections from #medium-comp and records recovery history. Its presence and later owner data do not prove the generated merged record was regenerated. |
| exporter | src/culturemech/export/kgx_export.py; transform; medium_to_ingredient_edge; _resolved_ingredient_id; nodes | context_only | The current exporter walks structured ingredient rows and uses a MIM resolver before local identity fallback; it returns no ingredient edge if resolution yields no identity. A missing explicit term alone does not establish a zero-edge export. No export was executed or edge count asserted. The record type is also consumed for node/type semantics, so source-unsupported classification is consequential. |
| history | data/merge_yaml/merged/892.yaml; Every timestamp in target, owner and explicitly listed contextual dependencies | supports | [{"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[0].timestamp", "value": "2026-02-20T00:22:35.982294Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T03:09:04.524269Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:49.275698Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[4].timestamp", "value": "2026-05-16T09:03:06.738496+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[5].timestamp", "value": "2026-08-06T03:05:04.694626+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[0].timestamp", "value": "2026-02-20T00:22:35.982294Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T03:09:04.524269Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:49.275698Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[4].timestamp", "value": "2026-05-16T09:03:06.738496+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[5].timestamp", "value": "2026-08-19T21:54:23.036626+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[6].timestamp", "value": "2026-08-20T19:01:16.117092+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[7].timestamp", "value": "2026-09-11T00:00:00-07:00", "valid_ISO_datetime": true, "timezone_aware": true}] |
| repair | scripts/repair_nbrc_892_score15.py; TARGET_ID; TARGET_PATH; NBRC_URL; GROUNDINGS; PREPARATION_STEPS; repair_document | context_only | This exact writer pins CultureMech:007502 to NBRC_892.yaml while explicitly selecting source 891 and Soybean Casein Digest Agar. Its five-row signature and pH range match the bound primary page. It removes generic sterilization and replaces preparation; the two FoodOn labels written by GROUNDINGS differ from the captured canonical labels. The writer was read, not executed. |

## Limits And Additional Notes

- The exact NBRC 891 page gives ingredient masses and 1 L distilled water, without an independently measured final-volume instruction. Owner g/L values retain the nominal catalogue recipe basis.
- FoodOn hydrolysate classes do not identify a supplier-specific casein or soybean peptone formulation. Source ingredient names and amounts must remain explicit even after canonical labels are corrected.
- Actual NBRC 892 is a different broth formulation. Its peptone ratio, phosphate and glucose are excluded from the source 891 agar recipe.
- The exact source provides pH but no detailed sterilization protocol. No temperature, time, organism or storage claim is inferred from routine laboratory practice.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T085617Z-culturemech-007502-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 892 (CultureMech:007502)'
started_at: '2026-10-21T08:49:01Z'
finished_at: '2026-10-21T08:56:17Z'
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
summary: This stable record denotes NBRC 891 Soybean Casein Digest Agar, as shown
  by its import provenance, recovered owner and exact repair writer. The generated
  892 target remains a collapsed table plus an empty ingredient, losing five source
  rows, the official title/accession, pH 7.1–7.5 and source-specific owner preparation.
  The owner retains two noncanonical FoodOn labels for broader protein-hydrolysate
  classes. The target’s autoclaving fallback lacks source support and has action DISSOLVE.
  All four diagnostics pass despite these semantic defects.
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
  - path: data/merge_yaml/merged/892.yaml
    sha256: 4643e7851a7e062a49652acda50bbd6dfb8ec4e289d44701ec8478ae279b0e51
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_892.yaml
    sha256: bf5e6865a1f46df6e160883b8320734edd956b4722bc7359d327b8f3f6239619
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
  - path: scripts/repair_nbrc_892_score15.py
    sha256: 06708fcaa578639e3d7bbfed83152e06e1c984426274bb5af073fcdc5dc78bb5
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
  selection: Task review 118; batch 012 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eleven task batches contain
    110 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 112 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007502
targets:
- target_id: CultureMech:007502
  path: data/merge_yaml/merged/892.yaml
  label: '892'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_892.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/892.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/892.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch012/118/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch012/118/strict.tsv"
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/892.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/892.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007502
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
  - CultureMech:007502
- check_id: scoped-history-timestamps
  name: Scoped history timestamp syntax and timezone check
  required: false
  status: passed
  summary: 14 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Existing provenance is preserved; no timestamps were rewritten.
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/892.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:56:17Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_892.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:56:17Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/892.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:44.250499Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/892.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch012/118/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:45.928485Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch012/118/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/892.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:47.607082Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/892.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:48.565223Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: nbrc891
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891
  locator: Medium No. header; complete Medium Composition table, footnotes and Comment
    section
  accessed_at: '2026-10-21T08:42:35.256437Z'
  support: supports
  summary: 'Read the full official NBRC 891 Soybean Casein Digest Agar page: casein
    peptone 15 g, soybean peptone 5 g, NaCl 5 g, agar 15 g and distilled water 1 L;
    pH 7.1–7.5. The page contains no detailed sterilization instructions.'
  snapshot_sha256: 5cfee8fde0da887bd48754bd05600c682f84e6354f938e5ac91d49a30b64def2
- evidence_id: nbrc892
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=892
  locator: Medium No. header, complete composition and preparation; identity countercheck
    only
  accessed_at: '2026-10-21T08:42:35.855353Z'
  support: context_only
  summary: 'Actual NBRC 892 is Soybean Casein Digest Broth: casein/soybean peptones
    17/3 g with K2HPO4 and glucose each 2.5 g, NaCl 5 g and water 1 L. It lacks the
    target source’s agar and is not a replacement formula for source 891.'
  snapshot_sha256: 5fc62624f809f5ae3b78d2279233423510a452639575fa72a90ce54f3c4e7948
- evidence_id: amount-1
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891
  locator: 'Medium Composition table, quantified row 1: Casein peptone'
  accessed_at: '2026-10-21T08:42:35.256437Z'
  support: supports
  summary: Exact source amount for owner ingredients[0].concentration; Source-specific
    casein hydrolysate identity retained; not a pure defined molecule. Source value
    and unit are 15 g. The target retains this only inside its collapsed table string.
  quote: Casein peptone 15 g
  snapshot_sha256: 5cfee8fde0da887bd48754bd05600c682f84e6354f938e5ac91d49a30b64def2
- evidence_id: amount-2
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891
  locator: 'Medium Composition table, quantified row 2: Soybean peptone'
  accessed_at: '2026-10-21T08:42:35.256437Z'
  support: supports
  summary: Exact source amount for owner ingredients[1].concentration; Source-specific
    soybean hydrolysate identity retained; not interchangeable with an arbitrary plant
    hydrolysate. Source value and unit are 5 g. The target retains this only inside
    its collapsed table string.
  quote: Soybean peptone 5 g
  snapshot_sha256: 5cfee8fde0da887bd48754bd05600c682f84e6354f938e5ac91d49a30b64def2
- evidence_id: amount-3
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891
  locator: 'Medium Composition table, quantified row 3: NaCl'
  accessed_at: '2026-10-21T08:42:35.256437Z'
  support: supports
  summary: Exact source amount for owner ingredients[2].concentration; Source sodium
    chloride mass; no hydration form is additionally asserted. Source value and unit
    are 5 g. The target retains this only inside its collapsed table string.
  quote: NaCl 5 g
  snapshot_sha256: 5cfee8fde0da887bd48754bd05600c682f84e6354f938e5ac91d49a30b64def2
- evidence_id: amount-4
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891
  locator: 'Medium Composition table, quantified row 4: Agar'
  accessed_at: '2026-10-21T08:42:35.256437Z'
  support: supports
  summary: Exact source amount for owner ingredients[3].concentration; Agar is listed
    without an optional condition in this exact recipe. Source value and unit are
    15 g. The target retains this only inside its collapsed table string.
  quote: Agar 15 g
  snapshot_sha256: 5cfee8fde0da887bd48754bd05600c682f84e6354f938e5ac91d49a30b64def2
- evidence_id: amount-5
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=891
  locator: 'Medium Composition table, quantified row 5: Distilled water'
  accessed_at: '2026-10-21T08:42:35.256437Z'
  support: supports
  summary: Exact source amount for owner ingredients[4].concentration; Literal solvent
    amount; not a gram or independently verified final-volume instruction. Source
    value and unit are 1 L. The target retains this only inside its collapsed table
    string.
  quote: Distilled water 1 L
  snapshot_sha256: 5cfee8fde0da887bd48754bd05600c682f84e6354f938e5ac91d49a30b64def2
- evidence_id: foodon03315719
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315719
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:42:32.147808Z'
  support: supports
  summary: FOODON:03315719 resolves to canonical label mammalian milk protein (hydrolyzed)
    and is not obsolete. The complete response, including available formula, hydration,
    structure, synonyms and definitions, was inspected. Literal owner-label equality
    is assessed separately; ontology descriptions do not establish recipe quantities.
  snapshot_sha256: 003d7d18eee340eb5c43ae7608d034459540ad736e2eca09a4c08e70afa766fe
- evidence_id: foodon03315720
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315720
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-20T07:37:22.786983Z'
  support: supports
  summary: FOODON:03315720 resolves to canonical label vegetable protein, hydrolyzed
    and is not obsolete. The complete response, including available formula, hydration,
    structure, synonyms and definitions, was inspected. Literal owner-label equality
    is assessed separately; ontology descriptions do not establish recipe quantities.
  snapshot_sha256: aa063e8b88177611aba640828e84d3982b1b3b1c65b11647d89c9efbf6274c25
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms
    and annotation'
  accessed_at: '2026-10-21T08:17:28.023873Z'
  support: supports
  summary: CHEBI:26710 resolves to canonical label sodium chloride and is not obsolete.
    The complete response, including available formula, hydration, structure, synonyms
    and definitions, was inspected. Literal owner-label equality is assessed separately;
    ontology descriptions do not establish recipe quantities.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
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
  accessed_at: '2026-10-21T08:56:17Z'
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
    3, "secondary_asserted_instances": 3, "secondary_verified_instances": 3, "primary_ontology_percent":
    100.0, "primary_CHEBI_percent": 60.0, "secondary_verified_percent": 60.0}}, "secondary_instances":
    [{"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field":
    "ingredients[2]", "preferred_term": "NaCl", "primary_id": "CHEBI:26710", "asserted_label":
    "sodium chloride", "canonical_label": "sodium chloride", "label_equal": true,
    "source_key": "chebi26710", "description": ["An inorganic chloride salt having
    sodium(1+) as the counterion."], "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid",
    "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum",
    "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "form_annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673",
    "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595",
    "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula":
    ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string":
    ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"],
    "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]},
    "secondary_id": "CHEBI:26710", "secondary_asserted_label": "sodium chloride",
    "secondary_index_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml",
    "field": "ingredients[3]", "preferred_term": "Agar", "primary_id": "CHEBI:2509",
    "asserted_label": "agar", "canonical_label": "agar", "label_equal": true, "source_key":
    "chebi2509", "description": ["A complex mixture of polysaccharides extracted from
    species of red algae. Its two main components are agarose and agaropectin. Agarose
    is the component responsible for the high-strength gelling properties of agar,
    while agaropectin provides the viscous properties."], "synonyms": [], "form_annotations":
    {"database_cross_reference": ["cas:9002-18-0", "kegg.compound:C08815", "pubmed:25603143",
    "pubmed:25842535", "pubmed:25959629", "pubmed:26043937", "pubmed:26050892", "pubmed:26116384",
    "reaxys:8538728", "wikipedia.en:Agar"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:2509"]}, "secondary_id": "CHEBI:2509", "secondary_asserted_label":
    "agar", "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "ingredients[4]", "preferred_term":
    "Distilled water", "primary_id": "CHEBI:15377", "asserted_label": "water", "canonical_label":
    "water", "label_equal": true, "source_key": "chebi15377", "description": ["An
    oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen
    atoms"], "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER",
    "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen",
    "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water",
    "water"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5",
    "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001",
    "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"],
    "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743",
    "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292",
    "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"],
    "smiles_string": ["[H]O[H]"]}, "secondary_id": "CHEBI:15377", "secondary_asserted_label":
    "water", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}]}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: _map_ingredients; _map_preparation_steps; _infer_medium_type
  accessed_at: '2026-10-21T08:56:17Z'
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
  accessed_at: '2026-10-21T08:56:17Z'
  support: context_only
  summary: 'Current recovery code parses explicit composition rows and separate footnote
    stock sections from #medium-comp and records recovery history. Its presence and
    later owner data do not prove the generated merged record was regenerated.'
- evidence_id: exporter
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: transform; medium_to_ingredient_edge; _resolved_ingredient_id; nodes
  accessed_at: '2026-10-21T08:56:17Z'
  support: context_only
  summary: The current exporter walks structured ingredient rows and uses a MIM resolver
    before local identity fallback; it returns no ingredient edge if resolution yields
    no identity. A missing explicit term alone does not establish a zero-edge export.
    No export was executed or edge count asserted. The record type is also consumed
    for node/type semantics, so source-unsupported classification is consequential.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/892.yaml
  locator: Every timestamp in target, owner and explicitly listed contextual dependencies
  accessed_at: '2026-10-21T08:56:17Z'
  support: supports
  summary: '[{"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-02-20T00:22:35.982294Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[1].timestamp",
    "value": "2026-03-13T03:09:04.524269Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[2].timestamp",
    "value": "2026-03-13T06:19:49.275698Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-05-16T09:03:06.738496+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/892.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-08-06T03:05:04.694626+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-02-20T00:22:35.982294Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[1].timestamp",
    "value": "2026-03-13T03:09:04.524269Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[2].timestamp",
    "value": "2026-03-13T06:19:49.275698Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-05-16T09:03:06.738496+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-08-19T21:54:23.036626+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[6].timestamp",
    "value": "2026-08-20T19:01:16.117092+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "curation_history[7].timestamp",
    "value": "2026-09-11T00:00:00-07:00", "valid_ISO_datetime": true, "timezone_aware":
    true}]'
- evidence_id: repair
  kind: record_content
  reference: scripts/repair_nbrc_892_score15.py
  locator: TARGET_ID; TARGET_PATH; NBRC_URL; GROUNDINGS; PREPARATION_STEPS; repair_document
  accessed_at: '2026-10-21T08:56:17Z'
  support: context_only
  summary: This exact writer pins CultureMech:007502 to NBRC_892.yaml while explicitly
    selecting source 891 and Soybean Casein Digest Agar. Its five-row signature and
    pH range match the bound primary page. It removes generic sterilization and replaces
    preparation; the two FoodOn labels written by GROUNDINGS differ from the captured
    canonical labels. The writer was read, not executed.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: NBRC 891 provenance despite local 892 label
  outcome: supported
  summary: The stable CultureMech ID, merge source basename, import-history accession
    891, maintained owner source term and captured primary page resolve one medium.
    The local name 892 does not license substitution of actual NBRC 892; that different
    source is only an identity countercheck. The legacy HTTP import URL was read as
    provenance, not represented as a newly retrieved response.
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - record
  - owner-0
  - nbrc891
  - nbrc892
  - repair
- assessment_id: amounts
  area: quantity
  topic: Every target row and every recovered source amount
  outcome: concern
  summary: 'The target has two malformed direct ingredient rows: one collapsed table
    at VARIABLE and an empty name with ''Casein peptone'' as its g/L value. The 5
    separate owner rows preserve the inspected source amounts and units as itemized.
    Solid masses expressed by the owner per liter are interpreted on the nominal listed
    recipe basis, without claiming that a source water amount establishes measured
    final volume.'
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - record
  - owner-0
  - nbrc891
  - amount-1
  - amount-2
  - amount-3
  - amount-4
  - amount-5
  details: '[{"owner_field": "ingredients[0].concentration", "name": "Casein peptone",
    "owner_value": "15", "owner_unit": "G_PER_L", "source_amount": "15", "source_unit":
    "g", "source_quote": "Casein peptone 15 g", "source_locator": "Medium Composition
    quantified row 1", "condition": "Source-specific casein hydrolysate identity retained;
    not a pure defined molecule.", "decision": "verified", "decision_rationale": "Source
    amount verified on the nominal batch basis; final volume is not independently
    established.", "target_correspondence": "Embedded text only; no equivalent usable
    direct ingredient row", "evidence_id": "amount-1"}, {"owner_field": "ingredients[1].concentration",
    "name": "Soybean peptone", "owner_value": "5", "owner_unit": "G_PER_L", "source_amount":
    "5", "source_unit": "g", "source_quote": "Soybean peptone 5 g", "source_locator":
    "Medium Composition quantified row 2", "condition": "Source-specific soybean hydrolysate
    identity retained; not interchangeable with an arbitrary plant hydrolysate.",
    "decision": "verified", "decision_rationale": "Source amount verified on the nominal
    batch basis; final volume is not independently established.", "target_correspondence":
    "Embedded text only; no equivalent usable direct ingredient row", "evidence_id":
    "amount-2"}, {"owner_field": "ingredients[2].concentration", "name": "NaCl", "owner_value":
    "5", "owner_unit": "G_PER_L", "source_amount": "5", "source_unit": "g", "source_quote":
    "NaCl 5 g", "source_locator": "Medium Composition quantified row 3", "condition":
    "Source sodium chloride mass; no hydration form is additionally asserted.", "decision":
    "verified", "decision_rationale": "Source amount verified on the nominal batch
    basis; final volume is not independently established.", "target_correspondence":
    "Embedded text only; no equivalent usable direct ingredient row", "evidence_id":
    "amount-3"}, {"owner_field": "ingredients[3].concentration", "name": "Agar", "owner_value":
    "15", "owner_unit": "G_PER_L", "source_amount": "15", "source_unit": "g", "source_quote":
    "Agar 15 g", "source_locator": "Medium Composition quantified row 4", "condition":
    "Agar is listed without an optional condition in this exact recipe.", "decision":
    "verified", "decision_rationale": "Source amount verified on the nominal batch
    basis; final volume is not independently established.", "target_correspondence":
    "Embedded text only; no equivalent usable direct ingredient row", "evidence_id":
    "amount-4"}, {"owner_field": "ingredients[4].concentration", "name": "Distilled
    water", "owner_value": "1", "owner_unit": "L", "source_amount": "1", "source_unit":
    "L", "source_quote": "Distilled water 1 L", "source_locator": "Medium Composition
    quantified row 5", "condition": "Literal solvent amount; not a gram or independently
    verified final-volume instruction.", "decision": "verified", "decision_rationale":
    "Literal liquid amount verified; no mass conversion is asserted.", "target_correspondence":
    "Embedded text only; no equivalent usable direct ingredient row", "evidence_id":
    "amount-5"}]'
- assessment_id: grounding
  area: grounding
  topic: All asserted primary IDs, canonical labels and current secondary keys
  outcome: concern
  summary: The generated target has 0/2 primary ontology links and 0/2 secondary links.
    The owner has 5/5 primary ontology links, including 3 CHEBI instances, and 3/5
    verified secondary links. 2 owner primary labels differ from canonical labels.
    These are separate layer-specific linkage denominators on a 0–100 scale, not scientific
    accuracy scores. No secondary denominator of zero is invented when no keys are
    asserted.
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - record
  - owner-0
  - mim
  - foodon03315719
  - foodon03315720
  - chebi26710
  - chebi2509
  - chebi15377
  details: '{"counts": {"target": {"ingredient_instances": 2, "primary_ontology_instances":
    0, "primary_CHEBI_instances": 0, "canonical_primary_label_instances": 0, "secondary_asserted_instances":
    0, "secondary_verified_instances": 0, "primary_ontology_percent": 0.0, "primary_CHEBI_percent":
    0.0, "secondary_verified_percent": 0.0}, "owner": {"ingredient_instances": 5,
    "primary_ontology_instances": 5, "primary_CHEBI_instances": 3, "canonical_primary_label_instances":
    3, "secondary_asserted_instances": 3, "secondary_verified_instances": 3, "primary_ontology_percent":
    100.0, "primary_CHEBI_percent": 60.0, "secondary_verified_percent": 60.0}}, "label_drift":
    [{"field_path": "ingredients[0].term.label", "id": "FOODON:03315719", "asserted_label":
    "Casein peptone", "canonical_label": "mammalian milk protein (hydrolyzed)", "source_key":
    "foodon03315719"}, {"field_path": "ingredients[1].term.label", "id": "FOODON:03315720",
    "asserted_label": "Soy peptone", "canonical_label": "vegetable protein, hydrolyzed",
    "source_key": "foodon03315720"}], "instances": [{"layer": "target", "path": "data/merge_yaml/merged/892.yaml",
    "field": "ingredients[0]", "preferred_term": "Casein peptone15gSoybean peptone5gNaCl5gAgar15gDistilled
    water1LpH 7.1-7.5"}, {"layer": "target", "path": "data/merge_yaml/merged/892.yaml",
    "field": "ingredients[1]", "preferred_term": ""}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml",
    "field": "ingredients[0]", "preferred_term": "Casein peptone", "primary_id": "FOODON:03315719",
    "asserted_label": "Casein peptone", "canonical_label": "mammalian milk protein
    (hydrolyzed)", "label_equal": false, "source_key": "foodon03315719", "description":
    ["SIREN DB annotation:\n* casein FOODON:03420180\n* food hydrolyzation process
    FOODON:03460277"], "synonyms": [], "form_annotations": {"database_cross_reference":
    ["https://bioregistry.io/reference/siren:F15719"], "has curation status": ["http://purl.obolibrary.org/obo/IAO_0000428"]}},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field":
    "ingredients[1]", "preferred_term": "Soybean peptone", "primary_id": "FOODON:03315720",
    "asserted_label": "Soy peptone", "canonical_label": "vegetable protein, hydrolyzed",
    "label_equal": false, "source_key": "foodon03315720", "description": ["SIREN DB
    annotation:\n* protein extract, concentrate or isolate FOODON:03420236\n* food
    hydrolyzation process FOODON:03460277"], "synonyms": [], "form_annotations": {"database_cross_reference":
    ["https://bioregistry.io/reference/siren:F15720"], "has curation status": ["http://purl.obolibrary.org/obo/IAO_0000428"]}},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml", "field":
    "ingredients[2]", "preferred_term": "NaCl", "primary_id": "CHEBI:26710", "asserted_label":
    "sodium chloride", "canonical_label": "sodium chloride", "label_equal": true,
    "source_key": "chebi26710", "description": ["An inorganic chloride salt having
    sodium(1+) as the counterion."], "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid",
    "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum",
    "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "form_annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673",
    "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595",
    "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula":
    ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string":
    ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"],
    "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]},
    "secondary_id": "CHEBI:26710", "secondary_asserted_label": "sodium chloride",
    "secondary_index_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/NBRC_892.yaml",
    "field": "ingredients[3]", "preferred_term": "Agar", "primary_id": "CHEBI:2509",
    "asserted_label": "agar", "canonical_label": "agar", "label_equal": true, "source_key":
    "chebi2509", "description": ["A complex mixture of polysaccharides extracted from
    species of red algae. Its two main components are agarose and agaropectin. Agarose
    is the component responsible for the high-strength gelling properties of agar,
    while agaropectin provides the viscous properties."], "synonyms": [], "form_annotations":
    {"database_cross_reference": ["cas:9002-18-0", "kegg.compound:C08815", "pubmed:25603143",
    "pubmed:25842535", "pubmed:25959629", "pubmed:26043937", "pubmed:26050892", "pubmed:26116384",
    "reaxys:8538728", "wikipedia.en:Agar"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:2509"]}, "secondary_id": "CHEBI:2509", "secondary_asserted_label":
    "agar", "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/NBRC_892.yaml", "field": "ingredients[4]", "preferred_term":
    "Distilled water", "primary_id": "CHEBI:15377", "asserted_label": "water", "canonical_label":
    "water", "label_equal": true, "source_key": "chebi15377", "description": ["An
    oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen
    atoms"], "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER",
    "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen",
    "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water",
    "water"], "form_annotations": {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5",
    "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001",
    "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"],
    "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743",
    "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292",
    "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"],
    "smiles_string": ["[H]O[H]"]}, "secondary_id": "CHEBI:15377", "secondary_asserted_label":
    "water", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}]}'
- assessment_id: forms
  area: grounding
  topic: Source ingredient identities, mixtures and exact chemical forms
  outcome: supported
  summary: CHEBI identifies sodium chloride, agar and water consistently with the
    source, and all three asserted secondary keys have exact MAPPED/preferred_term
    rows in the pinned MIM index. FoodOn 03315719 is mammalian milk protein (hydrolyzed),
    whose description includes casein; FoodOn 03315720 is the broader vegetable protein,
    hydrolyzed class. These support class-level hydrolysate context rather than supplier-specific
    formulations. Their owner term labels are not canonical and must be distinguished
    from the source-specific preferred terms. No wrong-ID or exact peptone-equivalence
    claim is inferred solely from these broader labels.
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - record
  - owner-0
  - nbrc891
  - foodon03315719
  - foodon03315720
  - chebi26710
  - chebi2509
  - chebi15377
- assessment_id: conditions
  area: consistency
  topic: Preparation, pH and physical-state conditions
  outcome: concern
  summary: Source pH 7.1–7.5 is correctly structured in the owner and missing in the
    target. Owner preparation identifies the exact ingredient set and adjustment to
    this range; it does not claim a sterilization protocol. The target instead has
    generic steps and unsupported Sterilize by autoclaving with action DISSOLVE. Source
    agar is unconditional, supporting the solid recipe.
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - record
  - owner-0
  - nbrc891
  - importer
- assessment_id: classification
  area: scope
  topic: Classification and bounded biological claims
  outcome: supported
  summary: COMPLEX/UNDEFINED and SOLID_AGAR agree with the two peptones and the stated
    15 g agar. No chemically defined interpretation is implied by ontology links to
    broad hydrolysate classes. Neither target nor owner asserts organisms, strains,
    taxon IDs, assemblies, DOI/PMID papers, growth outcomes, parent media or variants.
    Source catalogue scope is not experimental growth evidence. Optional omissions
    are not populated with invented organisms.
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - record
  - owner-0
  - nbrc891
  - nbrc892
  - exporter
- assessment_id: owner-correspondence
  area: ownership
  topic: Maintained recovery versus generated representation
  outcome: concern
  summary: The generated August merge precedes later owner recovery and source metadata.
    The owner now contains 5 explicit source rows and an official source term/reference;
    the target retains two collapsed rows and no structured source term/reference.
    Owner label differences must be corrected before regeneration. The exact maintained
    repair writer pins CultureMech:007502 at NBRC_892.yaml to NBRC source 891 and
    adds the official title, source term, pH range, canonical CHEBI links and source-specific
    preparation. Its FoodOn labels still require the reported correction.
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - record
  - owner-0
  - nbrc891
  - recovery
  - mim
  - repair
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
  - CultureMech:007502
  evidence_ids:
  - record
  - owner-0
  - nbrc891
  - validate-references
- assessment_id: history
  area: provenance
  topic: Append-only event history and timestamp interpretation
  outcome: supported
  summary: All 14 scoped timestamps were checked for ISO syntax and timezone. Every
    instance parses and has an explicit timezone. Curation events are process provenance
    rather than independent confirmation of recipe correctness.
  target_ids:
  - CultureMech:007502
  evidence_ids:
  - record
  - owner-0
  - history
  details: '[]'
findings:
- finding_id: f1
  issue_key: cm007502-stale-collapsed-source891-formula
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated target loses the recovered 5-row NBRC 891 formula
  description: The whole-table ingredient string at VARIABLE and the empty ingredient
    with a reagent name as a g/L value cannot represent a usable named formulation.
    The owner already has 5 explicit source rows and the official source accession/reference,
    with source conditions where stated. This prevents faithful scientific use of
    the generated formulation despite all four documented checks passing. Native P1
    reflects unusable identity/representation; this is not P1.1 and is not a reported
    schema-validator failure.
  target_ids:
  - CultureMech:007502
  field_paths:
  - ingredients
  - media_term
  - references
  - name
  - original_name
  - ph_range
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc891
  - recovery
  - repair
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_892.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm007502-unsupported-default-autoclave
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated autoclaving is unsupported and action-mismatched
  description: The inspected exact NBRC 891 page does not provide a sterilization
    protocol. The target nevertheless states Sterilize by autoclaving with action
    DISSOLVE, matching the importer fallback and keyword mismatch. The current owner
    has already removed that generic autoclaving instruction; the stale generated
    instruction should not be reintroduced as primary-source evidence. Neither a neighboring
    accession nor a routine laboratory convention supplies missing source-specific
    support.
  target_ids:
  - CultureMech:007502
  field_paths:
  - preparation_steps[2].description
  - preparation_steps[2].action
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc891
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_892.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: cm007502-owner-canonical-label-drift
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Maintained owner labels differ from canonical ontology labels
  description: '[{"field_path": "ingredients[0].term.label", "id": "FOODON:03315719",
    "asserted_label": "Casein peptone", "canonical_label": "mammalian milk protein
    (hydrolyzed)", "source_key": "foodon03315719"}, {"field_path": "ingredients[1].term.label",
    "id": "FOODON:03315720", "asserted_label": "Soy peptone", "canonical_label": "vegetable
    protein, hydrolyzed", "source_key": "foodon03315720"}] These are literal label
    differences in the maintained input and would propagate on regeneration. They
    do not by themselves prove that the asserted ontology IDs identify the wrong substances;
    preserve supplier/source names in preferred_term and exact recipe forms separately.'
  target_ids:
  - CultureMech:007502
  field_paths:
  - owner:data/normalized_yaml/bacterial/NBRC_892.yaml:ingredients[0].term.label
  - owner:data/normalized_yaml/bacterial/NBRC_892.yaml:ingredients[1].term.label
  evidence_ids:
  - owner-0
  - foodon03315719
  - foodon03315720
  - repair
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_892.yaml
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
  description: Verify the maintained source rows and their exact forms/units against
    the bound primary page, correct owner label or classification issues listed separately,
    add scoped amount evidence, and regenerate derived records while retaining the
    same stable ID and source accession.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007502
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_892.yaml
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
  description: Retain supported source pH/formulation details and regenerate from
    the verified owner without the unsupported default. Any later sterilization instruction
    needs exact source support and a corresponding action; keep unknown time, temperature
    and procedure explicit.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007502
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_892.yaml
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
  description: Update only the canonical term labels after verifying the same IDs
    and source-specific ingredient identities. Preserve source names, brands, supplied
    hydration forms and amounts, then ensure regeneration keeps both canonical labels
    and preferred terms. Run the documented ID-label correspondence check on the authorized
    correction.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007502
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_892.yaml
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
- The exact NBRC 891 page gives ingredient masses and 1 L distilled water, without
  an independently measured final-volume instruction. Owner g/L values retain the
  nominal catalogue recipe basis.
- FoodOn hydrolysate classes do not identify a supplier-specific casein or soybean
  peptone formulation. Source ingredient names and amounts must remain explicit even
  after canonical labels are corrected.
- Actual NBRC 892 is a different broth formulation. Its peptone ratio, phosphate and
  glucose are excluded from the source 891 agar recipe.
- The exact source provides pH but no detailed sterilization protocol. No temperature,
  time, organism or storage claim is inferred from routine laboratory practice.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-012
- generated-medium
```
