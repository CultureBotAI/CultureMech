# Source and formulation review: 5_x_r2a_agar (CultureMech:007685)

- Review: 20261021T084044Z-culturemech-007685-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:29:17Z
- Finished UTC: 2026-10-21T08:40:44Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact TOGO M1161/JCM1091 sources support all nine ingredients specified by mass and the fivefold relationship to the stated M341/JCM346 parent, with agar unchanged. Both local layers incorrectly encode1 L water as 1 g/L and omit source pH 7.2/preparation. Their parent note also calls both recipes NBRC despite exact JCM provenance. Primary and secondary chemical identifiers resolve within the stated linkage denominators. All four documented diagnostics pass; source quantities and preparation were assessed separately.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 110; batch 011 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding ten task batches contain 100 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 102 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007685 | data/merge_yaml/merged/5_x_R2A_Agar.yaml | generated | 5_x_r2a_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007685 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007685 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch011/110/strict.tsv |
| validate-terms | passed | True | CultureMech:007685 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007685 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007685 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped history timestamp syntax and timezone check | passed | False | CultureMech:007685 | 25 timestamp instances inspected; 0 malformed or timezone-naive instances. Existing provenance is preserved; no timestamps were rewritten. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007685.

The four documented recipes completed; interpret the scope of each separately.

### Exact JCM child and reciprocal parent relation

identity: supported. Targets: CultureMech:007685.

Stable child identity and TOGO M1161/JCM1091 agree. The parent path and ID resolve to M341/JCM346 and the reciprocal child link is present. This source identity is distinct from the inaccurate NBRC wording in the relation note.

### All ten direct rows and explicit water form

quantity: concern. Targets: CultureMech:007685.

All nine dry ingredient quantities agree with primary source masses and provider g/L on its declared 1000 mL basis. The single water row is dimensionally wrong: source 1 L has become 1 G_PER_L in both layers. No stock additions or nested stock quantities are present. Product qualifiers, magnesium sulfate heptahydrate and generic glucose remain source-scoped.

[{"field": "ingredients[0].concentration", "ingredient": "Distilled water", "value": "1", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[0]", "primary_source_key": "jcm1091", "source_amount": "1", "source_unit": "L", "decision": "correct: restore1L solvent volume, no mass conversion", "calculation": "not applicable: volume is not mass"}, {"field": "ingredients[1].concentration", "ingredient": "MgSO4・7H2O", "value": "0.25", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[1]", "primary_source_key": "jcm1091", "source_amount": "0.25", "source_unit": "g", "decision": "verified provider-normalized concentration and primary recipe mass", "calculation": "0.25 g / provider-declared1L = 0.25 g/L"}, {"field": "ingredients[2].concentration", "ingredient": "K2HPO4", "value": "1.5", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[2]", "primary_source_key": "jcm1091", "source_amount": "1.5", "source_unit": "g", "decision": "verified provider-normalized concentration and primary recipe mass", "calculation": "1.5 g / provider-declared1L = 1.5 g/L"}, {"field": "ingredients[3].concentration", "ingredient": "Sodium pyruvate", "value": "1.5", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[3]", "primary_source_key": "jcm1091", "source_amount": "1.5", "source_unit": "g", "decision": "verified provider-normalized concentration and primary recipe mass", "calculation": "1.5 g / provider-declared1L = 1.5 g/L"}, {"field": "ingredients[4].concentration", "ingredient": "Glucose", "value": "2.5", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[4]", "primary_source_key": "jcm1091", "source_amount": "2.5", "source_unit": "g", "decision": "verified provider-normalized concentration and primary recipe mass", "calculation": "2.5 g / provider-declared1L = 2.5 g/L"}, {"field": "ingredients[5].concentration", "ingredient": "Soluble starch", "value": "2.5", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[5]", "primary_source_key": "jcm1091", "source_amount": "2.5", "source_unit": "g", "decision": "verified provider-normalized concentration and primary recipe mass", "calculation": "2.5 g / provider-declared1L = 2.5 g/L"}, {"field": "ingredients[6].concentration", "ingredient": "Agar", "value": "15", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[6]", "primary_source_key": "jcm1091", "source_amount": "15", "source_unit": "g", "decision": "verified provider-normalized concentration and primary recipe mass", "calculation": "15 g / provider-declared1L = 15 g/L"}, {"field": "ingredients[7].concentration", "ingredient": "Yeast extract (BD--Difco)", "value": "2.5", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[7]", "primary_source_key": "jcm1091", "source_amount": "2.5", "source_unit": "g", "decision": "verified provider-normalized concentration and primary recipe mass", "calculation": "2.5 g / provider-declared1L = 2.5 g/L"}, {"field": "ingredients[8].concentration", "ingredient": "Proteose peptone No. 3 (BD--Difco)", "value": "2.5", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[8]", "primary_source_key": "jcm1091", "source_amount": "2.5", "source_unit": "g", "decision": "verified provider-normalized concentration and primary recipe mass", "calculation": "2.5 g / provider-declared1L = 2.5 g/L"}, {"field": "ingredients[9].concentration", "ingredient": "Casamino acids (BD--Difco)", "value": "2.5", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[9]", "primary_source_key": "jcm1091", "source_amount": "2.5", "source_unit": "g", "decision": "verified provider-normalized concentration and primary recipe mass", "calculation": "2.5 g / provider-declared1L = 2.5 g/L"}]

### Every asserted primary label, chemical form and secondary key

grounding: supported. Targets: CultureMech:007685.

Primary IDs are checked against the exact OLS responses, including available chemical-form annotations; current secondary keys are checked against the pinned packaged index. Ingredient-instance denominators include direct and nested stock composition rows, exclude stock-addition doses, and remain separate for generated target, owner and contextual records. These 0–100 percentages measure linkage, not scientific correctness. Undefined mixtures are not assigned invented pure compounds.

{"counts": {"target": {"ingredient_instances": 10, "primary_ontology_instances": 7, "primary_CHEBI_instances": 7, "secondary_asserted_instances": 5, "secondary_verified_instances": 5, "primary_ontology_percent": 70.0, "secondary_verified_percent": 50.0}, "owner": {"ingredient_instances": 10, "primary_ontology_instances": 7, "primary_CHEBI_instances": 7, "secondary_asserted_instances": 5, "secondary_verified_instances": 5, "primary_ontology_percent": 70.0, "secondary_verified_percent": 50.0}, "parent-context": {"ingredient_instances": 10, "primary_ontology_instances": 7, "primary_CHEBI_instances": 7, "secondary_asserted_instances": 5, "secondary_verified_instances": 5, "primary_ontology_percent": 70.0, "secondary_verified_percent": 50.0}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527", "canonical_label": "dipotassium hydrogen phosphate", "source_key": "chebi131527", "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "form_annotations": {"generalized_empirical_formula": ["HO4P.2K"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id": "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[3]", "preferred_term": "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label": "sodium pyruvate", "source_key": "chebi50144", "synonyms": ["Natriumpyruvat", "pyruvic acid, sodium salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"], "form_annotations": {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string": ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"], "mass": ["110.044"], "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description": [], "secondary_id": "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234", "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose", "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose", "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"], "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017", "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke", "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most important reserve polysaccharide found in plants. It is a glucan consisting of amylose and amylopectin."]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509", "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations": {}, "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509", "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[7]", "preferred_term": "Yeast extract (BD--Difco)"}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[8]", "preferred_term": "Proteose peptone No. 3 (BD--Difco)"}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[9]", "preferred_term": "Casamino acids (BD--Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527", "canonical_label": "dipotassium hydrogen phosphate", "source_key": "chebi131527", "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "form_annotations": {"generalized_empirical_formula": ["HO4P.2K"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id": "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[3]", "preferred_term": "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label": "sodium pyruvate", "source_key": "chebi50144", "synonyms": ["Natriumpyruvat", "pyruvic acid, sodium salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"], "form_annotations": {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string": ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"], "mass": ["110.044"], "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description": [], "secondary_id": "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234", "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose", "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose", "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"], "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017", "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke", "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most important reserve polysaccharide found in plants. It is a glucan consisting of amylose and amylopectin."]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509", "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations": {}, "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509", "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[7]", "preferred_term": "Yeast extract (BD--Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[8]", "preferred_term": "Proteose peptone No. 3 (BD--Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[9]", "preferred_term": "Casamino acids (BD--Difco)"}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527", "canonical_label": "dipotassium hydrogen phosphate", "source_key": "chebi131527", "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "form_annotations": {"generalized_empirical_formula": ["HO4P.2K"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id": "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[3]", "preferred_term": "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label": "sodium pyruvate", "source_key": "chebi50144", "synonyms": ["Natriumpyruvat", "pyruvic acid, sodium salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"], "form_annotations": {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string": ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"], "mass": ["110.044"], "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description": [], "secondary_id": "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234", "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose", "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose", "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"], "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017", "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke", "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most important reserve polysaccharide found in plants. It is a glucan consisting of amylose and amylopectin."]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509", "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations": {}, "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509", "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[7]", "preferred_term": "Yeast extract (BD-Difco)"}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[8]", "preferred_term": "Proteose peptone No. 3 (BD-Difco)"}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[9]", "preferred_term": "Casamino acids (BD-Difco)"}]}

### Fivefold nutrient/salt claim and unchanged agar

consistency: supported. Targets: CultureMech:007685.

All ten source rows were compared by exact provider compound ID. Eight non-agar solute masses increase fivefold; agar remains 15 g and water remains 1 L. Both providers declare 1000 mL, and both primaries specify pH 7.2. The existing CONCENTRATION_VARIANT claim is supported without equating all R2A media or treating the parent commercial premix comment as a child component.

[{"ingredient": "Yeast extract", "compound_id": 16, "child_amount": 2.5, "parent_amount": 0.5, "unit": "g", "ratio": "5"}, {"ingredient": "Proteose peptone no. 3", "compound_id": 316, "child_amount": 2.5, "parent_amount": 0.5, "unit": "g", "ratio": "5"}, {"ingredient": "Casamino acids", "compound_id": 101, "child_amount": 2.5, "parent_amount": 0.5, "unit": "g", "ratio": "5"}, {"ingredient": "Glucose", "compound_id": 5, "child_amount": 2.5, "parent_amount": 0.5, "unit": "g", "ratio": "5"}, {"ingredient": "Starch", "compound_id": 199, "child_amount": 2.5, "parent_amount": 0.5, "unit": "g", "ratio": "5"}, {"ingredient": "Sodium pyruvate", "compound_id": 438, "child_amount": 1.5, "parent_amount": 0.3, "unit": "g", "ratio": "5"}, {"ingredient": "K2HPO4", "compound_id": 10, "child_amount": 1.5, "parent_amount": 0.3, "unit": "g", "ratio": "5"}, {"ingredient": "MgSO4 x 7 H2O", "compound_id": 8, "child_amount": 0.25, "parent_amount": 0.05, "unit": "g", "ratio": "5"}, {"ingredient": "Agar", "compound_id": 3, "child_amount": 15, "parent_amount": 15, "unit": "g", "ratio": "1"}, {"ingredient": "Distilled water", "compound_id": 4, "child_amount": 1000, "parent_amount": 1000, "unit": "ml", "ratio": "1"}]

### Source pH and sterilization scope

consistency: concern. Targets: CultureMech:007685.

Both local layers lack pH 7.2 and preparation steps despite exact child-source pH instruction and current JCM page-wide 121 °C 15 min default. These are recoverable protocol omissions. No incubation, atmosphere, vessel or source-specific post-sterilization addition is supplied or inferred.

### Classification, applications and bounded biological evidence

scope: supported. Targets: CultureMech:007685.

The source recipe contains complex biological mixtures and agar where asserted, supporting COMPLEX/UNDEFINED and the specified liquid or agar formulation. Bacterial filing and generic microbial-cultivation application are catalogue scope. Neither target nor normalized owner asserts target organisms, strains, taxa, genomes, DOI/PMID claims or growth outcomes; no species-level growth claim is inferred from recipe names, source catalogue membership or ontology labels. Empty optional organism fields are not treated as a source contradiction.

### Source provenance, references and narrow amount evidence

evidence: concern. Targets: CultureMech:007685.

Source notes correctly retain JCM accessions and URLs, while the parent relationship note incorrectly says TOGO/NBRC. Root references and ingredient concentration evidence are absent from both child layers. Use exact child and parent source citations with separate roles; do not invent a publication, year or species-level growth claim.

### Maintained owner and generated formulation

ownership: supported. Targets: CultureMech:007685.

The sole child owner has the same formulation and source omissions as the generated target; the latter adds merge metadata. The parent is a contextual relationship dependency. Correct the maintained child/source writer and verify reciprocal links before separately authorized regeneration.

### Append-only event history and timestamp interpretation

provenance: supported. Targets: CultureMech:007685.

All 25 scoped timestamps were checked for ISO syntax and timezone. Every instance parses and has an explicit timezone. Curation events are process provenance rather than independent confirmation of recipe correctness.

[]

## Findings

### f1: Source water volume is represented as mass concentration

major / open / confirmed; issue key: cm007685-water-volume-as-mass.

Both target and child owner encode distilled water 1 G_PER_L, whereas JCM1091 and TOGO M1161 explicitly list 1 L. No source density or mass conversion supports this representation. All nine ingredient amounts remain separately supported.

### f2: Source pH and preparation instructions are omitted

major / open / confirmed; issue key: cm007685-source-ph-preparation-omitted.

The exact child source says adjust pH to 7.2 and its current page-wide default specifies 121 °C 15 min autoclaving; both child layers lack these instructions. Omitting that exact sterilization method, temperature and duration materially limits reproducibility. This does not support guessing other growth conditions.

### f3: Parent relation note names the wrong source collection

minor / open / confirmed; issue key: cm007685-parent-collection-provenance.

The note says both records are TOGO/NBRC formulations. Exact child and parent metadata identify JCM_M1091 and JCM_M346, corroborated by both JCM pages and existing source notes. The fivefold relationship itself remains supported.

### f4: Ingredient amounts lack narrow references and evidence

minor / open / confirmed; issue key: cm007685-amount-evidence-placement.

Notes provide recoverable source URLs but neither child layer has structured references or per-ingredient concentration evidence for the nine unchanged mass values and corrected solvent volume. Parent comparison needs its own explicit source scope.

## Recommended Actions And Acceptance Checks

### a1

Restore the exact source solvent-volume/preparation basis in supported fields and attach narrow evidence. Preserve provider-declared normalization for ingredients specified by mass without asserting independently measured final volume; regenerate from corrected owner.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the explicit pH and verified source-version sterilization default with accurate action and source evidence, without adding unrelated R2A procedures.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Correct the maintained relation’s collection wording to exact TOGO/JCM provenance while preserving parent IDs, paths, reciprocal link and the supported concentration-variant relationship.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add source metadata and exact row-level amount/form support using existing evidence fields; distinguish primary recipe quantities, provider-declared concentrations and parent comparison. Preserve source-exact product qualifiers.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/5_x_R2A_Agar.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/5_x_R2A_Agar.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/5_x_R2A_Agar.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch011/110/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch011/110/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/5_x_R2A_Agar.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/5_x_R2A_Agar.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| jcm1091 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1091; Medium1091 title, ten-row recipe, pH sentence and page-wide default sterilization | supports | Read the entire JCM1091 recipe: five components each2.5 g (yeast extract, proteose peptone No.3, casamino acids, glucose, soluble starch); pyruvate and K2HPO4 each1.5 g; MgSO4·7H2O 0.25 g; agar 15 g; water 1 L. Adjust pH to 7.2. Current page default is 121 °C 15 min unless otherwise stated. |
| togoM1161 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1161; $.meta; $.components[0].items[0:10]; $.comments[0] | supports | Exact child M1161 identifies JCM_M1091, retains all ten source rows with units and the pH 7.2 comment. Water has volume 1 and unit L. |
| jcm346 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346; Medium346 title, ten-row recipe, pH instruction and comment | supports | Exact parent JCM346 lists the same eight non-agar solutes at one-fifth child mass, agar 15 g and water 1 L unchanged, and pH 7.2. Its commercial Difco premix comment is parent-source context. |
| togoM341 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M341; $.meta; $.components[0].items; $.comments | supports | M341 metadata explicitly identifies JCM_M346 and matches the parent stable record/source notes. It is not an NBRC accession. |
| mediadiveJ1091api | https://mediadive.dsmz.de/rest/medium/J1091; $.data.medium; $.data.solutions[0] | supports | Provider main solution 5162 declares 1000 mL and the same nine ingredient g_l values; exact salt hydrate and product attributes remain distinguishable. |
| mediadiveJ346api | https://mediadive.dsmz.de/rest/medium/J346; $.data.medium; $.data.solutions[0] | supports | Provider parent solution 4066 also declares 1000 mL. Its corresponding compound IDs and amounts establish the bounded eight-solute fivefold comparison, with agar and water unchanged. |
| parent | data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml; Entire parent YAML and reciprocal child relation | context_only | Read the full parent and verified stable ID, path, JCM_M346 source, ten ingredient rows and reciprocal child reference. This is exact relational context, not a new review target. |
| togo-writer | src/culturemech/import/togo_importer.py; _ingredient_from_item, _parse_unit, _extract_preparation_steps and _extract_ph | context_only | Current importer maps L to L and extracts pH/comments. These current capabilities do not justify the older owner/target water-unit and preparation omissions; the importer was not executed. |
| variant-writer | scripts/apply_media_variant_links.py; Manifest-driven link application | context_only | Generic current variant writer is pinned only as context. No exact hard-coded child/parent row was located in the bounded preflight search; it is not asserted to be the historical author of this particular note. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:15377 resolves to the asserted canonical label water and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:31795 resolves to the asserted canonical label magnesium sulfate heptahydrate and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:131527 resolves to the asserted canonical label dipotassium hydrogen phosphate and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:50144 resolves to the asserted canonical label sodium pyruvate and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:17234 resolves to the asserted canonical label glucose and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:28017 resolves to the asserted canonical label starch and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:2509 resolves to the asserted canonical label agar and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact MAPPED/preferred_term rows for every asserted secondary key; adjacent pinned metadata | supports | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527", "canonical_label": "dipotassium hydrogen phosphate", "source_key": "chebi131527", "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "form_annotations": {"generalized_empirical_formula": ["HO4P.2K"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id": "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[3]", "preferred_term": "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label": "sodium pyruvate", "source_key": "chebi50144", "synonyms": ["Natriumpyruvat", "pyruvic acid, sodium salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"], "form_annotations": {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string": ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"], "mass": ["110.044"], "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description": [], "secondary_id": "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234", "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose", "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose", "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"], "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017", "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke", "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most important reserve polysaccharide found in plants. It is a glucan consisting of amylose and amylopectin."]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509", "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations": {}, "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509", "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[7]", "preferred_term": "Yeast extract (BD--Difco)"}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[8]", "preferred_term": "Proteose peptone No. 3 (BD--Difco)"}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[9]", "preferred_term": "Casamino acids (BD--Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527", "canonical_label": "dipotassium hydrogen phosphate", "source_key": "chebi131527", "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "form_annotations": {"generalized_empirical_formula": ["HO4P.2K"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id": "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[3]", "preferred_term": "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label": "sodium pyruvate", "source_key": "chebi50144", "synonyms": ["Natriumpyruvat", "pyruvic acid, sodium salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"], "form_annotations": {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string": ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"], "mass": ["110.044"], "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description": [], "secondary_id": "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234", "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose", "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose", "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"], "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017", "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke", "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most important reserve polysaccharide found in plants. It is a glucan consisting of amylose and amylopectin."]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509", "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations": {}, "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509", "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[7]", "preferred_term": "Yeast extract (BD--Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[8]", "preferred_term": "Proteose peptone No. 3 (BD--Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[9]", "preferred_term": "Casamino acids (BD--Difco)"}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527", "canonical_label": "dipotassium hydrogen phosphate", "source_key": "chebi131527", "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "form_annotations": {"generalized_empirical_formula": ["HO4P.2K"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id": "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[3]", "preferred_term": "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label": "sodium pyruvate", "source_key": "chebi50144", "synonyms": ["Natriumpyruvat", "pyruvic acid, sodium salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"], "form_annotations": {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string": ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"], "mass": ["110.044"], "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description": [], "secondary_id": "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234", "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose", "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose", "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"], "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017", "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke", "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most important reserve polysaccharide found in plants. It is a glucan consisting of amylose and amylopectin."]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509", "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations": {}, "description": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509", "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[7]", "preferred_term": "Yeast extract (BD-Difco)"}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[8]", "preferred_term": "Proteose peptone No. 3 (BD-Difco)"}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[9]", "preferred_term": "Casamino acids (BD-Difco)"}]} |
| history | data/merge_yaml/merged/5_x_R2A_Agar.yaml; Every timestamp in target, owner and explicitly listed contextual dependencies | supports | [{"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-27T06:35:54.034591Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[1].timestamp", "value": "2026-01-28T19:48:18.491887Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:50.603810Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-17T06:30:04.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[4].timestamp", "value": "2026-03-17T19:46:09.002857+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[5].timestamp", "value": "2026-06-05T07:40:30.911324+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[6].timestamp", "value": "2026-06-10T06:57:21.582179+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[7].timestamp", "value": "2026-06-10T07:46:47.074462+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[8].timestamp", "value": "2026-08-06T03:05:06.217348+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-27T06:35:54.034591Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "curation_history[1].timestamp", "value": "2026-01-28T19:48:18.491887Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:50.603810Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-17T06:30:04.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "curation_history[4].timestamp", "value": "2026-03-17T19:46:09.002857+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "curation_history[5].timestamp", "value": "2026-06-05T07:40:30.911324+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "curation_history[6].timestamp", "value": "2026-06-10T06:57:21.582179+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "curation_history[7].timestamp", "value": "2026-06-10T07:46:47.074462+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-27T06:35:54.876871Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "curation_history[1].timestamp", "value": "2026-01-28T19:48:28.398831Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:20:08.352585Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-17T06:30:25.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "curation_history[4].timestamp", "value": "2026-03-17T19:46:27.342611+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "curation_history[5].timestamp", "value": "2026-06-05T07:40:40.556241+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "curation_history[6].timestamp", "value": "2026-06-10T06:57:29.886165+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "curation_history[7].timestamp", "value": "2026-06-10T07:46:50.358709+00:00", "valid_ISO_datetime": true, "timezone_aware": true}] |

## Limits And Additional Notes

- Both primary recipes specify1 L water, while the provider independently declares 1000 mL. Calculated g/L values and parent ratios below retain the provider-declared basis rather than claiming measured post-addition final volume.
- The primary source says glucose generically, and CHEBI17234 is the generic glucose term. No D/L substitution or stereospecific amount was invented. MgSO4·7H2O is explicitly a heptahydrate and its term/form were checked.
- Parent M341 was read in full as a relational dependency. This is not a separate comprehensive review of that parent or every other R2A record.
- The exact source gives no organism, genome, incubation condition or experimental growth claim. The commercial premix comment belongs to JCM346 and is not transferred into the child recipe as an ingredient.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084044Z-culturemech-007685-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 5_x_r2a_agar (CultureMech:007685)'
started_at: '2026-10-21T08:29:17Z'
finished_at: '2026-10-21T08:40:44Z'
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
summary: Exact TOGO M1161/JCM1091 sources support all nine ingredients specified by
  mass and the fivefold relationship to the stated M341/JCM346 parent, with agar unchanged.
  Both local layers incorrectly encode1 L water as 1 g/L and omit source pH 7.2/preparation.
  Their parent note also calls both recipes NBRC despite exact JCM provenance. Primary
  and secondary chemical identifiers resolve within the stated linkage denominators.
  All four documented diagnostics pass; source quantities and preparation were assessed
  separately.
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
  - path: data/merge_yaml/merged/5_x_R2A_Agar.yaml
    sha256: 5dce64dea3102709ae4ea7683beb9ccd872e6deae1bd78708974d64fd7329828
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
    sha256: ba6c80d033eb2b2c858523353e4076e881e24f6b86253ae0a7359a0a1088e45c
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml
    sha256: 0b3e81644edeccd379bcb782e97434598aeb0a3775e629d2a2a4da48d85e4590
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
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
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
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
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
  selection: Task review 110; batch 011 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding ten task batches contain
    100 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 102 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007685
targets:
- target_id: CultureMech:007685
  path: data/merge_yaml/merged/5_x_R2A_Agar.yaml
  label: 5_x_r2a_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/5_x_R2A_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/5_x_R2A_Agar.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch011/110/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch011/110/strict.tsv"
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/5_x_R2A_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/5_x_R2A_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007685
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
  - CultureMech:007685
- check_id: scoped-history-timestamps
  name: Scoped history timestamp syntax and timezone check
  required: false
  status: passed
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Existing provenance is preserved; no timestamps were rewritten.
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/5_x_R2A_Agar.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:40:44Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:40:44Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/5_x_R2A_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:31:32.974752Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/5_x_R2A_Agar.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch011/110/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:31:47.086901Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch011/110/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/5_x_R2A_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:31:58.693215Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/5_x_R2A_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:32:02.399488Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: jcm1091
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1091
  locator: Medium1091 title, ten-row recipe, pH sentence and page-wide default sterilization
  accessed_at: '2026-10-21T08:23:35.486385Z'
  support: supports
  summary: 'Read the entire JCM1091 recipe: five components each2.5 g (yeast extract,
    proteose peptone No.3, casamino acids, glucose, soluble starch); pyruvate and
    K2HPO4 each1.5 g; MgSO4·7H2O 0.25 g; agar 15 g; water 1 L. Adjust pH to 7.2. Current
    page default is 121 °C 15 min unless otherwise stated.'
  snapshot_sha256: 3335c9e28273375ce3f454927ff1ed7d233af7b50869fb9f758d0e5451a944f5
- evidence_id: togoM1161
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1161
  locator: $.meta; $.components[0].items[0:10]; $.comments[0]
  accessed_at: '2026-10-21T08:23:34.139808Z'
  support: supports
  summary: Exact child M1161 identifies JCM_M1091, retains all ten source rows with
    units and the pH 7.2 comment. Water has volume 1 and unit L.
  snapshot_sha256: a318c4043551d9e4edd9829bc1ec37e1fb8154dd0f7324e8654f977421f8422b
- evidence_id: jcm346
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=346
  locator: Medium346 title, ten-row recipe, pH instruction and comment
  accessed_at: '2026-10-21T08:23:35.784072Z'
  support: supports
  summary: Exact parent JCM346 lists the same eight non-agar solutes at one-fifth
    child mass, agar 15 g and water 1 L unchanged, and pH 7.2. Its commercial Difco
    premix comment is parent-source context.
  snapshot_sha256: 63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb
- evidence_id: togoM341
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M341
  locator: $.meta; $.components[0].items; $.comments
  accessed_at: '2026-10-21T08:23:34.145536Z'
  support: supports
  summary: M341 metadata explicitly identifies JCM_M346 and matches the parent stable
    record/source notes. It is not an NBRC accession.
  snapshot_sha256: 7c5b6b04a9e45e5a61a3784b0765d8e068d539235cb246d934d61b4b0767448c
- evidence_id: mediadiveJ1091api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1091
  locator: $.data.medium; $.data.solutions[0]
  accessed_at: '2026-10-21T08:23:33.417077Z'
  support: supports
  summary: Provider main solution 5162 declares 1000 mL and the same nine ingredient
    g_l values; exact salt hydrate and product attributes remain distinguishable.
  snapshot_sha256: d06452885eba52036da8902317a36ede91a36b2d9a2b48a516316d8598546a6d
- evidence_id: mediadiveJ346api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J346
  locator: $.data.medium; $.data.solutions[0]
  accessed_at: '2026-10-21T08:23:33.418631Z'
  support: supports
  summary: Provider parent solution 4066 also declares 1000 mL. Its corresponding
    compound IDs and amounts establish the bounded eight-solute fivefold comparison,
    with agar and water unchanged.
  snapshot_sha256: b0e0da4ff4a646441317c0fa7aef68eb8c0a08ad2e576063119af8ba09ae43fb
- evidence_id: parent
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml
  locator: Entire parent YAML and reciprocal child relation
  accessed_at: '2026-10-21T08:40:44Z'
  support: context_only
  summary: Read the full parent and verified stable ID, path, JCM_M346 source, ten
    ingredient rows and reciprocal child reference. This is exact relational context,
    not a new review target.
- evidence_id: togo-writer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _parse_unit, _extract_preparation_steps and _extract_ph
  accessed_at: '2026-10-21T08:40:44Z'
  support: context_only
  summary: Current importer maps L to L and extracts pH/comments. These current capabilities
    do not justify the older owner/target water-unit and preparation omissions; the
    importer was not executed.
- evidence_id: variant-writer
  kind: record_content
  reference: scripts/apply_media_variant_links.py
  locator: Manifest-driven link application
  accessed_at: '2026-10-21T08:40:44Z'
  support: context_only
  summary: Generic current variant writer is pinned only as context. No exact hard-coded
    child/parent row was located in the bounded preflight search; it is not asserted
    to be the historical author of this particular note.
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to the asserted canonical label water and is not obsolete.
    Complete response including available form, formula, synonym and structure annotations
    was inspected; recipe-specific grade and amount are separate claims.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T08:17:28.683169Z'
  support: supports
  summary: CHEBI:31795 resolves to the asserted canonical label magnesium sulfate
    heptahydrate and is not obsolete. Complete response including available form,
    formula, synonym and structure annotations was inspected; recipe-specific grade
    and amount are separate claims.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to the asserted canonical label dipotassium hydrogen
    phosphate and is not obsolete. Complete response including available form, formula,
    synonym and structure annotations was inspected; recipe-specific grade and amount
    are separate claims.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi50144
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-20T07:22:07.440767Z'
  support: supports
  summary: CHEBI:50144 resolves to the asserted canonical label sodium pyruvate and
    is not obsolete. Complete response including available form, formula, synonym
    and structure annotations was inspected; recipe-specific grade and amount are
    separate claims.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: CHEBI:17234 resolves to the asserted canonical label glucose and is not
    obsolete. Complete response including available form, formula, synonym and structure
    annotations was inspected; recipe-specific grade and amount are separate claims.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi28017
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T06:57:46.408993Z'
  support: supports
  summary: CHEBI:28017 resolves to the asserted canonical label starch and is not
    obsolete. Complete response including available form, formula, synonym and structure
    annotations was inspected; recipe-specific grade and amount are separate claims.
  snapshot_sha256: 959b4330165a7ff12d2e464f4a7b44e148376624d04cf7764b6a8671c1c99204
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to the asserted canonical label agar and is not obsolete.
    Complete response including available form, formula, synonym and structure annotations
    was inspected; recipe-specific grade and amount are separate claims.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact MAPPED/preferred_term rows for every asserted secondary key; adjacent
    pinned metadata
  accessed_at: '2026-10-21T08:40:44Z'
  support: supports
  summary: '{"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count":
    9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id",
    "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech",
    "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"},
    "instances": [{"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id":
    "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms":
    ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water",
    "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau",
    "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations":
    {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"],
    "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen
    hydride consisting of an oxygen atom that is covalently bonded to two hydrogen
    atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled
    water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795",
    "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795",
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]},
    {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field":
    "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527", "canonical_label":
    "dipotassium hydrogen phosphate", "source_key": "chebi131527", "synonyms": ["Dibasic
    potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen
    phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium
    phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium
    salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium
    monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic",
    "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium
    hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "form_annotations":
    {"generalized_empirical_formula": ["HO4P.2K"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description":
    ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id":
    "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path":
    "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[3]", "preferred_term":
    "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label": "sodium pyruvate",
    "source_key": "chebi50144", "synonyms": ["Natriumpyruvat", "pyruvic acid, sodium
    salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"], "form_annotations":
    {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string": ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"],
    "mass": ["110.044"], "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description":
    [], "secondary_id": "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate",
    "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term":
    "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234",
    "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose",
    "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose",
    "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"],
    "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy
    and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017",
    "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke",
    "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most
    important reserve polysaccharide found in plants. It is a glucan consisting of
    amylose and amylopectin."]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509",
    "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations":
    {}, "description": ["A complex mixture of polysaccharides extracted from species
    of red algae. Its two main components are agarose and agaropectin. Agarose is
    the component responsible for the high-strength gelling properties of agar, while
    agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509",
    "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[7]", "preferred_term": "Yeast extract (BD--Difco)"}, {"layer":
    "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[8]",
    "preferred_term": "Proteose peptone No. 3 (BD--Difco)"}, {"layer": "target", "path":
    "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[9]", "preferred_term":
    "Casamino acids (BD--Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id":
    "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms":
    ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water",
    "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau",
    "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations":
    {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"],
    "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen
    hydride consisting of an oxygen atom that is covalently bonded to two hydrogen
    atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled
    water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795",
    "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795",
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527",
    "canonical_label": "dipotassium hydrogen phosphate", "source_key": "chebi131527",
    "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate",
    "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium
    orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4",
    "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium
    monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)",
    "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium
    hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate
    trihydrate"], "form_annotations": {"generalized_empirical_formula": ["HO4P.2K"],
    "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description":
    ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id":
    "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[3]",
    "preferred_term": "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label":
    "sodium pyruvate", "source_key": "chebi50144", "synonyms": ["Natriumpyruvat",
    "pyruvic acid, sodium salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"],
    "form_annotations": {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string":
    ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"], "mass": ["110.044"],
    "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description": [], "secondary_id":
    "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate", "match_type":
    "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate",
    "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234",
    "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose",
    "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose",
    "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"],
    "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy
    and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017",
    "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke",
    "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most
    important reserve polysaccharide found in plants. It is a glucan consisting of
    amylose and amylopectin."]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509",
    "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations":
    {}, "description": ["A complex mixture of polysaccharides extracted from species
    of red algae. Its two main components are agarose and agaropectin. Agarose is
    the component responsible for the high-strength gelling properties of agar, while
    agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509",
    "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[7]", "preferred_term": "Yeast extract (BD--Difco)"}, {"layer":
    "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[8]", "preferred_term": "Proteose peptone No. 3 (BD--Difco)"},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[9]", "preferred_term": "Casamino acids (BD--Difco)"}, {"layer":
    "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id":
    "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms":
    ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water",
    "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau",
    "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations":
    {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"],
    "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen
    hydride consisting of an oxygen atom that is covalently bonded to two hydrogen
    atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled
    water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795",
    "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795",
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]},
    {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527",
    "canonical_label": "dipotassium hydrogen phosphate", "source_key": "chebi131527",
    "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate",
    "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium
    orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4",
    "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium
    monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)",
    "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium
    hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate
    trihydrate"], "form_annotations": {"generalized_empirical_formula": ["HO4P.2K"],
    "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description":
    ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id":
    "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context",
    "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[3]",
    "preferred_term": "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label":
    "sodium pyruvate", "source_key": "chebi50144", "synonyms": ["Natriumpyruvat",
    "pyruvic acid, sodium salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"],
    "form_annotations": {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string":
    ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"], "mass": ["110.044"],
    "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description": [], "secondary_id":
    "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate", "match_type":
    "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate",
    "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]},
    {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234",
    "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose",
    "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose",
    "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"],
    "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy
    and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017",
    "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke",
    "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most
    important reserve polysaccharide found in plants. It is a glucan consisting of
    amylose and amylopectin."]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509",
    "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations":
    {}, "description": ["A complex mixture of polysaccharides extracted from species
    of red algae. Its two main components are agarose and agaropectin. Agarose is
    the component responsible for the high-strength gelling properties of agar, while
    agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509",
    "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[7]", "preferred_term": "Yeast extract (BD-Difco)"}, {"layer":
    "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[8]", "preferred_term": "Proteose peptone No. 3 (BD-Difco)"},
    {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[9]", "preferred_term": "Casamino acids (BD-Difco)"}]}'
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/5_x_R2A_Agar.yaml
  locator: Every timestamp in target, owner and explicitly listed contextual dependencies
  accessed_at: '2026-10-21T08:40:44Z'
  support: supports
  summary: '[{"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-01-27T06:35:54.034591Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[1].timestamp",
    "value": "2026-01-28T19:48:18.491887Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[2].timestamp",
    "value": "2026-03-13T06:19:50.603810Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-17T06:30:04.000000Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-03-17T19:46:09.002857+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-06-05T07:40:30.911324+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[6].timestamp",
    "value": "2026-06-10T06:57:21.582179+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[7].timestamp",
    "value": "2026-06-10T07:46:47.074462+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "curation_history[8].timestamp",
    "value": "2026-08-06T03:05:06.217348+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "curation_history[0].timestamp", "value": "2026-01-27T06:35:54.034591Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "curation_history[1].timestamp", "value": "2026-01-28T19:48:18.491887Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:50.603810Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "curation_history[3].timestamp", "value": "2026-03-17T06:30:04.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "curation_history[4].timestamp", "value": "2026-03-17T19:46:09.002857+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "curation_history[5].timestamp", "value": "2026-06-05T07:40:30.911324+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "curation_history[6].timestamp", "value": "2026-06-10T06:57:21.582179+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "curation_history[7].timestamp", "value": "2026-06-10T07:46:47.074462+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "curation_history[0].timestamp", "value": "2026-01-27T06:35:54.876871Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "curation_history[1].timestamp", "value": "2026-01-28T19:48:28.398831Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "curation_history[2].timestamp", "value": "2026-03-13T06:20:08.352585Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "curation_history[3].timestamp", "value": "2026-03-17T06:30:25.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "curation_history[4].timestamp", "value": "2026-03-17T19:46:27.342611+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "curation_history[5].timestamp", "value": "2026-06-05T07:40:40.556241+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "curation_history[6].timestamp", "value": "2026-06-10T06:57:29.886165+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "curation_history[7].timestamp", "value": "2026-06-10T07:46:50.358709+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact JCM child and reciprocal parent relation
  outcome: supported
  summary: Stable child identity and TOGO M1161/JCM1091 agree. The parent path and
    ID resolve to M341/JCM346 and the reciprocal child link is present. This source
    identity is distinct from the inaccurate NBRC wording in the relation note.
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - record
  - owner-0
  - parent
  - jcm1091
  - togoM1161
  - jcm346
  - togoM341
- assessment_id: amounts
  area: quantity
  topic: All ten direct rows and explicit water form
  outcome: concern
  summary: 'All nine dry ingredient quantities agree with primary source masses and
    provider g/L on its declared 1000 mL basis. The single water row is dimensionally
    wrong: source 1 L has become 1 G_PER_L in both layers. No stock additions or nested
    stock quantities are present. Product qualifiers, magnesium sulfate heptahydrate
    and generic glucose remain source-scoped.'
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - record
  - owner-0
  - jcm1091
  - togoM1161
  - mediadiveJ1091api
  details: '[{"field": "ingredients[0].concentration", "ingredient": "Distilled water",
    "value": "1", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[0]",
    "primary_source_key": "jcm1091", "source_amount": "1", "source_unit": "L", "decision":
    "correct: restore1L solvent volume, no mass conversion", "calculation": "not applicable:
    volume is not mass"}, {"field": "ingredients[1].concentration", "ingredient":
    "MgSO4・7H2O", "value": "0.25", "unit": "G_PER_L", "source_key": "togoM1161", "locator":
    "$.components[0].items[1]", "primary_source_key": "jcm1091", "source_amount":
    "0.25", "source_unit": "g", "decision": "verified provider-normalized concentration
    and primary recipe mass", "calculation": "0.25 g / provider-declared1L = 0.25
    g/L"}, {"field": "ingredients[2].concentration", "ingredient": "K2HPO4", "value":
    "1.5", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[2]",
    "primary_source_key": "jcm1091", "source_amount": "1.5", "source_unit": "g", "decision":
    "verified provider-normalized concentration and primary recipe mass", "calculation":
    "1.5 g / provider-declared1L = 1.5 g/L"}, {"field": "ingredients[3].concentration",
    "ingredient": "Sodium pyruvate", "value": "1.5", "unit": "G_PER_L", "source_key":
    "togoM1161", "locator": "$.components[0].items[3]", "primary_source_key": "jcm1091",
    "source_amount": "1.5", "source_unit": "g", "decision": "verified provider-normalized
    concentration and primary recipe mass", "calculation": "1.5 g / provider-declared1L
    = 1.5 g/L"}, {"field": "ingredients[4].concentration", "ingredient": "Glucose",
    "value": "2.5", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[4]",
    "primary_source_key": "jcm1091", "source_amount": "2.5", "source_unit": "g", "decision":
    "verified provider-normalized concentration and primary recipe mass", "calculation":
    "2.5 g / provider-declared1L = 2.5 g/L"}, {"field": "ingredients[5].concentration",
    "ingredient": "Soluble starch", "value": "2.5", "unit": "G_PER_L", "source_key":
    "togoM1161", "locator": "$.components[0].items[5]", "primary_source_key": "jcm1091",
    "source_amount": "2.5", "source_unit": "g", "decision": "verified provider-normalized
    concentration and primary recipe mass", "calculation": "2.5 g / provider-declared1L
    = 2.5 g/L"}, {"field": "ingredients[6].concentration", "ingredient": "Agar", "value":
    "15", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[6]",
    "primary_source_key": "jcm1091", "source_amount": "15", "source_unit": "g", "decision":
    "verified provider-normalized concentration and primary recipe mass", "calculation":
    "15 g / provider-declared1L = 15 g/L"}, {"field": "ingredients[7].concentration",
    "ingredient": "Yeast extract (BD--Difco)", "value": "2.5", "unit": "G_PER_L",
    "source_key": "togoM1161", "locator": "$.components[0].items[7]", "primary_source_key":
    "jcm1091", "source_amount": "2.5", "source_unit": "g", "decision": "verified provider-normalized
    concentration and primary recipe mass", "calculation": "2.5 g / provider-declared1L
    = 2.5 g/L"}, {"field": "ingredients[8].concentration", "ingredient": "Proteose
    peptone No. 3 (BD--Difco)", "value": "2.5", "unit": "G_PER_L", "source_key": "togoM1161",
    "locator": "$.components[0].items[8]", "primary_source_key": "jcm1091", "source_amount":
    "2.5", "source_unit": "g", "decision": "verified provider-normalized concentration
    and primary recipe mass", "calculation": "2.5 g / provider-declared1L = 2.5 g/L"},
    {"field": "ingredients[9].concentration", "ingredient": "Casamino acids (BD--Difco)",
    "value": "2.5", "unit": "G_PER_L", "source_key": "togoM1161", "locator": "$.components[0].items[9]",
    "primary_source_key": "jcm1091", "source_amount": "2.5", "source_unit": "g", "decision":
    "verified provider-normalized concentration and primary recipe mass", "calculation":
    "2.5 g / provider-declared1L = 2.5 g/L"}]'
- assessment_id: grounding
  area: grounding
  topic: Every asserted primary label, chemical form and secondary key
  outcome: supported
  summary: Primary IDs are checked against the exact OLS responses, including available
    chemical-form annotations; current secondary keys are checked against the pinned
    packaged index. Ingredient-instance denominators include direct and nested stock
    composition rows, exclude stock-addition doses, and remain separate for generated
    target, owner and contextual records. These 0–100 percentages measure linkage,
    not scientific correctness. Undefined mixtures are not assigned invented pure
    compounds.
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi15377
  - chebi31795
  - chebi131527
  - chebi50144
  - chebi17234
  - chebi28017
  - chebi2509
  details: '{"counts": {"target": {"ingredient_instances": 10, "primary_ontology_instances":
    7, "primary_CHEBI_instances": 7, "secondary_asserted_instances": 5, "secondary_verified_instances":
    5, "primary_ontology_percent": 70.0, "secondary_verified_percent": 50.0}, "owner":
    {"ingredient_instances": 10, "primary_ontology_instances": 7, "primary_CHEBI_instances":
    7, "secondary_asserted_instances": 5, "secondary_verified_instances": 5, "primary_ontology_percent":
    70.0, "secondary_verified_percent": 50.0}, "parent-context": {"ingredient_instances":
    10, "primary_ontology_instances": 7, "primary_CHEBI_instances": 7, "secondary_asserted_instances":
    5, "secondary_verified_instances": 5, "primary_ontology_percent": 70.0, "secondary_verified_percent":
    50.0}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id":
    "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms":
    ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water",
    "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau",
    "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations":
    {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"],
    "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen
    hydride consisting of an oxygen atom that is covalently bonded to two hydrogen
    atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled
    water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795",
    "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795",
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]},
    {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field":
    "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527", "canonical_label":
    "dipotassium hydrogen phosphate", "source_key": "chebi131527", "synonyms": ["Dibasic
    potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen
    phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium
    phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium
    salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium
    monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic",
    "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium
    hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "form_annotations":
    {"generalized_empirical_formula": ["HO4P.2K"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description":
    ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id":
    "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path":
    "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[3]", "preferred_term":
    "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label": "sodium pyruvate",
    "source_key": "chebi50144", "synonyms": ["Natriumpyruvat", "pyruvic acid, sodium
    salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"], "form_annotations":
    {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string": ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"],
    "mass": ["110.044"], "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description":
    [], "secondary_id": "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate",
    "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term":
    "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234",
    "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose",
    "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose",
    "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"],
    "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy
    and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017",
    "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke",
    "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most
    important reserve polysaccharide found in plants. It is a glucan consisting of
    amylose and amylopectin."]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509",
    "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations":
    {}, "description": ["A complex mixture of polysaccharides extracted from species
    of red algae. Its two main components are agarose and agaropectin. Agarose is
    the component responsible for the high-strength gelling properties of agar, while
    agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509",
    "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml",
    "field": "ingredients[7]", "preferred_term": "Yeast extract (BD--Difco)"}, {"layer":
    "target", "path": "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[8]",
    "preferred_term": "Proteose peptone No. 3 (BD--Difco)"}, {"layer": "target", "path":
    "data/merge_yaml/merged/5_x_R2A_Agar.yaml", "field": "ingredients[9]", "preferred_term":
    "Casamino acids (BD--Difco)"}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id":
    "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms":
    ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water",
    "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau",
    "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations":
    {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"],
    "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen
    hydride consisting of an oxygen atom that is covalently bonded to two hydrogen
    atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled
    water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795",
    "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795",
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527",
    "canonical_label": "dipotassium hydrogen phosphate", "source_key": "chebi131527",
    "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate",
    "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium
    orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4",
    "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium
    monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)",
    "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium
    hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate
    trihydrate"], "form_annotations": {"generalized_empirical_formula": ["HO4P.2K"],
    "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description":
    ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id":
    "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml", "field": "ingredients[3]",
    "preferred_term": "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label":
    "sodium pyruvate", "source_key": "chebi50144", "synonyms": ["Natriumpyruvat",
    "pyruvic acid, sodium salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"],
    "form_annotations": {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string":
    ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"], "mass": ["110.044"],
    "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description": [], "secondary_id":
    "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate", "match_type":
    "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate",
    "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234",
    "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose",
    "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose",
    "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"],
    "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy
    and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017",
    "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke",
    "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most
    important reserve polysaccharide found in plants. It is a glucan consisting of
    amylose and amylopectin."]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509",
    "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations":
    {}, "description": ["A complex mixture of polysaccharides extracted from species
    of red algae. Its two main components are agarose and agaropectin. Agarose is
    the component responsible for the high-strength gelling properties of agar, while
    agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509",
    "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[7]", "preferred_term": "Yeast extract (BD--Difco)"}, {"layer":
    "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[8]", "preferred_term": "Proteose peptone No. 3 (BD--Difco)"},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml",
    "field": "ingredients[9]", "preferred_term": "Casamino acids (BD--Difco)"}, {"layer":
    "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id":
    "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms":
    ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water",
    "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau",
    "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations":
    {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"],
    "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen
    hydride consisting of an oxygen atom that is covalently bonded to two hydrogen
    atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled
    water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[1]", "preferred_term": "MgSO4・7H2O", "primary_id": "CHEBI:31795",
    "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795",
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."]},
    {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[2]", "preferred_term": "K2HPO4", "primary_id": "CHEBI:131527",
    "canonical_label": "dipotassium hydrogen phosphate", "source_key": "chebi131527",
    "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate",
    "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium
    orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4",
    "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium
    monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)",
    "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium
    hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate
    trihydrate"], "form_annotations": {"generalized_empirical_formula": ["HO4P.2K"],
    "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "description":
    ["A potassium salt that is the dipotassium salt of phosphoric acid."], "secondary_id":
    "CHEBI:131527", "secondary_index_rows": [{"label": "K2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context",
    "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml", "field": "ingredients[3]",
    "preferred_term": "Sodium pyruvate", "primary_id": "CHEBI:50144", "canonical_label":
    "sodium pyruvate", "source_key": "chebi50144", "synonyms": ["Natriumpyruvat",
    "pyruvic acid, sodium salt", "sodium 2-oxopropanoate", "sodium 2-oxopropanoate"],
    "form_annotations": {"generalized_empirical_formula": ["C3H3O3.Na"], "inchi_string":
    ["InChI=1S/C3H4O3.Na/c1-2(4)3(5)6;/h1H3,(H,5,6);/q;+1/p-1"], "mass": ["110.044"],
    "smiles_string": ["CC(=O)C(=O)[O-].[Na+]"]}, "description": [], "secondary_id":
    "CHEBI:50144", "secondary_index_rows": [{"label": "Na-pyruvate", "match_type":
    "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate",
    "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]},
    {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[4]", "preferred_term": "Glucose", "primary_id": "CHEBI:17234",
    "canonical_label": "glucose", "source_key": "chebi17234", "synonyms": ["DL-glucose",
    "Glc", "Glucose", "Glucose", "Glukose", "gluco-hexose", "gluco-hexose", "glucose",
    "glucose"], "form_annotations": {"generalized_empirical_formula": ["C6H12O6"],
    "mass": ["180.156"]}, "description": ["An aldohexose used as a source of energy
    and metabolic intermediate."], "secondary_id": "CHEBI:17234", "secondary_index_rows":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[5]", "preferred_term": "Soluble starch", "primary_id": "CHEBI:28017",
    "canonical_label": "starch", "source_key": "chebi28017", "synonyms": ["Staerke",
    "Starch", "amidon", "amylum"], "form_annotations": {}, "description": ["The most
    important reserve polysaccharide found in plants. It is a glucan consisting of
    amylose and amylopectin."]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[6]", "preferred_term": "Agar", "primary_id": "CHEBI:2509",
    "canonical_label": "agar", "source_key": "chebi2509", "synonyms": [], "form_annotations":
    {}, "description": ["A complex mixture of polysaccharides extracted from species
    of red algae. Its two main components are agarose and agaropectin. Agarose is
    the component responsible for the high-strength gelling properties of agar, while
    agaropectin provides the viscous properties."], "secondary_id": "CHEBI:2509",
    "secondary_index_rows": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[7]", "preferred_term": "Yeast extract (BD-Difco)"}, {"layer":
    "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[8]", "preferred_term": "Proteose peptone No. 3 (BD-Difco)"},
    {"layer": "parent-context", "path": "data/normalized_yaml/bacterial/TOGO_M341_R2A_Agar.yaml",
    "field": "ingredients[9]", "preferred_term": "Casamino acids (BD-Difco)"}]}'
- assessment_id: variant
  area: consistency
  topic: Fivefold nutrient/salt claim and unchanged agar
  outcome: supported
  summary: All ten source rows were compared by exact provider compound ID. Eight
    non-agar solute masses increase fivefold; agar remains 15 g and water remains
    1 L. Both providers declare 1000 mL, and both primaries specify pH 7.2. The existing
    CONCENTRATION_VARIANT claim is supported without equating all R2A media or treating
    the parent commercial premix comment as a child component.
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - record
  - owner-0
  - parent
  - jcm1091
  - jcm346
  - mediadiveJ1091api
  - mediadiveJ346api
  details: '[{"ingredient": "Yeast extract", "compound_id": 16, "child_amount": 2.5,
    "parent_amount": 0.5, "unit": "g", "ratio": "5"}, {"ingredient": "Proteose peptone
    no. 3", "compound_id": 316, "child_amount": 2.5, "parent_amount": 0.5, "unit":
    "g", "ratio": "5"}, {"ingredient": "Casamino acids", "compound_id": 101, "child_amount":
    2.5, "parent_amount": 0.5, "unit": "g", "ratio": "5"}, {"ingredient": "Glucose",
    "compound_id": 5, "child_amount": 2.5, "parent_amount": 0.5, "unit": "g", "ratio":
    "5"}, {"ingredient": "Starch", "compound_id": 199, "child_amount": 2.5, "parent_amount":
    0.5, "unit": "g", "ratio": "5"}, {"ingredient": "Sodium pyruvate", "compound_id":
    438, "child_amount": 1.5, "parent_amount": 0.3, "unit": "g", "ratio": "5"}, {"ingredient":
    "K2HPO4", "compound_id": 10, "child_amount": 1.5, "parent_amount": 0.3, "unit":
    "g", "ratio": "5"}, {"ingredient": "MgSO4 x 7 H2O", "compound_id": 8, "child_amount":
    0.25, "parent_amount": 0.05, "unit": "g", "ratio": "5"}, {"ingredient": "Agar",
    "compound_id": 3, "child_amount": 15, "parent_amount": 15, "unit": "g", "ratio":
    "1"}, {"ingredient": "Distilled water", "compound_id": 4, "child_amount": 1000,
    "parent_amount": 1000, "unit": "ml", "ratio": "1"}]'
- assessment_id: preparation
  area: consistency
  topic: Source pH and sterilization scope
  outcome: concern
  summary: Both local layers lack pH 7.2 and preparation steps despite exact child-source
    pH instruction and current JCM page-wide 121 °C 15 min default. These are recoverable
    protocol omissions. No incubation, atmosphere, vessel or source-specific post-sterilization
    addition is supplied or inferred.
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - record
  - owner-0
  - jcm1091
  - togoM1161
  - togo-writer
- assessment_id: biological-scope
  area: scope
  topic: Classification, applications and bounded biological evidence
  outcome: supported
  summary: The source recipe contains complex biological mixtures and agar where asserted,
    supporting COMPLEX/UNDEFINED and the specified liquid or agar formulation. Bacterial
    filing and generic microbial-cultivation application are catalogue scope. Neither
    target nor normalized owner asserts target organisms, strains, taxa, genomes,
    DOI/PMID claims or growth outcomes; no species-level growth claim is inferred
    from recipe names, source catalogue membership or ontology labels. Empty optional
    organism fields are not treated as a source contradiction.
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - record
  - owner-0
  - jcm1091
- assessment_id: evidence
  area: evidence
  topic: Source provenance, references and narrow amount evidence
  outcome: concern
  summary: Source notes correctly retain JCM accessions and URLs, while the parent
    relationship note incorrectly says TOGO/NBRC. Root references and ingredient concentration
    evidence are absent from both child layers. Use exact child and parent source
    citations with separate roles; do not invent a publication, year or species-level
    growth claim.
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - record
  - owner-0
  - parent
  - jcm1091
  - togoM1161
  - jcm346
  - togoM341
- assessment_id: ownership
  area: ownership
  topic: Maintained owner and generated formulation
  outcome: supported
  summary: The sole child owner has the same formulation and source omissions as the
    generated target; the latter adds merge metadata. The parent is a contextual relationship
    dependency. Correct the maintained child/source writer and verify reciprocal links
    before separately authorized regeneration.
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - record
  - owner-0
  - parent
  - togo-writer
  - variant-writer
- assessment_id: history
  area: provenance
  topic: Append-only event history and timestamp interpretation
  outcome: supported
  summary: All 25 scoped timestamps were checked for ISO syntax and timezone. Every
    instance parses and has an explicit timezone. Curation events are process provenance
    rather than independent confirmation of recipe correctness.
  target_ids:
  - CultureMech:007685
  evidence_ids:
  - record
  - owner-0
  - history
  details: '[]'
findings:
- finding_id: f1
  issue_key: cm007685-water-volume-as-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source water volume is represented as mass concentration
  description: Both target and child owner encode distilled water 1 G_PER_L, whereas
    JCM1091 and TOGO M1161 explicitly list 1 L. No source density or mass conversion
    supports this representation. All nine ingredient amounts remain separately supported.
  target_ids:
  - CultureMech:007685
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm1091
  - togoM1161
  - mediadiveJ1091api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
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
  issue_key: cm007685-source-ph-preparation-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH and preparation instructions are omitted
  description: The exact child source says adjust pH to 7.2 and its current page-wide
    default specifies 121 °C 15 min autoclaving; both child layers lack these instructions.
    Omitting that exact sterilization method, temperature and duration materially
    limits reproducibility. This does not support guessing other growth conditions.
  target_ids:
  - CultureMech:007685
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm1091
  - togoM1161
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: Native P3.5 normally maps to minor; this omission is normalized
    to major because source-specific sterilization method, temperature and duration
    are omitted from both local layers, materially limiting reproducibility. The source
    pH/preparation omission also relates to P3.4.
- finding_id: f3
  issue_key: cm007685-parent-collection-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Parent relation note names the wrong source collection
  description: The note says both records are TOGO/NBRC formulations. Exact child
    and parent metadata identify JCM_M1091 and JCM_M346, corroborated by both JCM
    pages and existing source notes. The fivefold relationship itself remains supported.
  target_ids:
  - CultureMech:007685
  field_paths:
  - parent_media.notes
  evidence_ids:
  - record
  - owner-0
  - parent
  - togoM1161
  - togoM341
  - jcm1091
  - jcm346
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: cm007685-amount-evidence-placement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Ingredient amounts lack narrow references and evidence
  description: Notes provide recoverable source URLs but neither child layer has structured
    references or per-ingredient concentration evidence for the nine unchanged mass
    values and corrected solvent volume. Parent comparison needs its own explicit
    source scope.
  target_ids:
  - CultureMech:007685
  field_paths:
  - references
  - ingredients[*].evidence
  evidence_ids:
  - record
  - owner-0
  - jcm1091
  - togoM1161
  - mediadiveJ1091api
  - jcm346
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Restore the exact source solvent-volume/preparation basis in supported
    fields and attach narrow evidence. Preserve provider-declared normalization for
    ingredients specified by mass without asserting independently measured final volume;
    regenerate from corrected owner.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007685
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
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
  description: Preserve the explicit pH and verified source-version sterilization
    default with accurate action and source evidence, without adding unrelated R2A
    procedures.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007685
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
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
  description: Correct the maintained relation’s collection wording to exact TOGO/JCM
    provenance while preserving parent IDs, paths, reciprocal link and the supported
    concentration-variant relationship.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007685
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
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
  description: Add source metadata and exact row-level amount/form support using existing
    evidence fields; distinguish primary recipe quantities, provider-declared concentrations
    and parent comparison. Preserve source-exact product qualifiers.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007685
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1161_5_x_R2A_Agar.yaml
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
- Both primary recipes specify1 L water, while the provider independently declares
  1000 mL. Calculated g/L values and parent ratios below retain the provider-declared
  basis rather than claiming measured post-addition final volume.
- The primary source says glucose generically, and CHEBI17234 is the generic glucose
  term. No D/L substitution or stereospecific amount was invented. MgSO4·7H2O is explicitly
  a heptahydrate and its term/form were checked.
- Parent M341 was read in full as a relational dependency. This is not a separate
  comprehensive review of that parent or every other R2A record.
- The exact source gives no organism, genome, incubation condition or experimental
  growth claim. The commercial premix comment belongs to JCM346 and is not transferred
  into the child recipe as an ingredient.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-011
- generated-medium
```
