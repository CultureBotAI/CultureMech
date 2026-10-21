# Source and formulation review: 5_salt_water_growth_medium (CultureMech:010360)

- Review: 20261021T084040Z-culturemech-010360-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:29:15Z
- Finished UTC: 2026-10-21T08:40:40Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact TOGO M938/JCM897 identity is supported. The generated target retains a 100 g/L empty MDS-stock placeholder and 500 g/L water, omitting the stock composition, pH and source references already recovered in its normalized owner. The owner repair preserves literal batch amounts but still labels them per liter: the exact provider declares a 600 mL main batch, giving peptone 5 g/L and yeast extract 1 g/L. The stock itself is explicitly brought to 1 L and must remain separate. All four documented diagnostics pass.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 107; batch 011 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding ten task batches contain 100 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 102 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010360 | data/merge_yaml/merged/5_salt_water_growth_medium.yaml | generated | 5_salt_water_growth_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010360 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010360 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch011/107/strict.tsv |
| validate-terms | passed | True | CultureMech:010360 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010360 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010360 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped history timestamp syntax and timezone check | passed | False | CultureMech:010360 | 22 timestamp instances inspected; 0 malformed or timezone-naive instances. Existing provenance is preserved; no timestamps were rewritten. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010360.

The four documented recipes completed; interpret the scope of each separately.

### Exact receiving medium and stock source identity

identity: supported. Targets: CultureMech:010360.

M938, JCM897 and the stable record ID agree. The M578/JCM574 cross-reference is to its MDS subsection. Exact provider stock 4404 and local helper CM013393 corroborate that subsection; no whole-medium substitution or missing ID is assumed.

### All four target ingredients and the stock addition

quantity: concern. Targets: CultureMech:010360.

Every direct target row and stock dose is itemized. Primary batch literals are supported, but target water/stock units are dimensionally wrong and owner per-liter values retain a 600 mL batch’s literals. Provider volume 600 mL supports peptone 5 g/L, yeast extract 1 g/L and stock 166.666667 mL/L; retain the source batch if a final-volume representation cannot be expressed faithfully. Tris dose remains unquantified.

[{"target_field": "ingredients[0].concentration", "owner_field": "ingredients[0].concentration", "name": "Distilled water", "target": "500 G_PER_L", "owner": "500 ML_PER_L", "source": "500 mL in main recipe", "source_key": "jcm897", "decision": "correct target dimension; preserve literal 500 mL batch solvent or normalize only on explicit 600 mL provider basis", "calculation": "500 / 0.6 = 833.333333 mL/L on provider basis; no mass conversion"}, {"target_field": "ingredients[1].concentration", "owner_field": "ingredients[1].concentration", "name": "Yeast extract (BD-Difco)", "target": "0.6 G_PER_L", "owner": "0.6 G_PER_L", "source": "0.6 g in main recipe", "source_key": "mediadiveJ897api", "locator": "$.data.solutions[0].recipe[1]", "decision": "correct per-liter basis", "calculation": "0.6 g / 0.6 L = 1 g/L, matching provider g_l"}, {"target_field": "ingredients[2].concentration", "owner_field": "ingredients[2].concentration", "name": "Peptone (Oxoid)", "target": "3 G_PER_L", "owner": "3 G_PER_L", "source": "3 g in main recipe", "source_key": "mediadiveJ897api", "locator": "$.data.solutions[0].recipe[0]", "decision": "correct per-liter basis", "calculation": "3 g / 0.6 L = 5 g/L, matching provider g_l"}, {"target_field": "ingredients[3].concentration", "owner_field": "preparation_steps[1].description", "name": "Tris base", "target": "variable VARIABLE", "owner": "adjust pH7.5 with1M Tris", "source": "1 M Tris base used for pH adjustment; no addition volume", "source_key": "jcm897", "decision": "not_quantified final dose; preserve adjustment-stock strength and pH, do not assert 1 M final concentration"}, {"target_field": "solutions[0].concentration", "owner_field": "solutions[0].concentration", "name": "MDS salt water", "target": "100 G_PER_L", "owner": "100 ML_PER_L", "source": "100 mL in main recipe", "source_key": "mediadiveJ897api", "locator": "$.data.solutions[0].recipe[2]", "decision": "correct target dimension and both layers’ receiving-medium basis", "calculation": "100 mL / 0.6 L = 166.666667 mL/L conditionally on provider main volume"}]

### Every nested MDS stock row and conditional delivered contribution

quantity: concern. Targets: CultureMech:010360.

The six owner/helper composition rows are assessed at the explicitly final 1 L MDS stock stage. Their water row/note lists 1 L water, while the preparation text correctly says bring to final 1 L; preserve that final-volume meaning rather than adding an extra literal liter of water. The generated target instead has an empty composition and Unknown solution name. On the provider 600 mL receiving basis, 100 mL stock contributes NaCl 40 g/L, MgCl2·6H2O 5 g/L, MgSO4·7H2O 5.833333 g/L, KCl 1.166667 g/L and CaCl2 0.833333 mmol/L. These calculations do not replace stock concentrations or add duplicate direct ingredients.

{"stock_rows": [{"owner_field": "solutions[0].composition[0].concentration", "helper_field": "composition[0].concentration", "name": "NaCl", "value": "240.0", "unit": "G_PER_L", "source_key": "jcm574", "locator": "MDS salt water subsection", "decision": "verified at explicitly final 1 L stock stage; absent from target", "qualification": "Exact hydrate/form and mass retained"}, {"owner_field": "solutions[0].composition[1].concentration", "helper_field": "composition[1].concentration", "name": "MgCl2 x 6H2O", "value": "30.0", "unit": "G_PER_L", "source_key": "jcm574", "locator": "MDS salt water subsection", "decision": "verified at explicitly final 1 L stock stage; absent from target", "qualification": "Exact hydrate/form and mass retained"}, {"owner_field": "solutions[0].composition[2].concentration", "helper_field": "composition[2].concentration", "name": "MgSO4 x 7H2O", "value": "35.0", "unit": "G_PER_L", "source_key": "jcm574", "locator": "MDS salt water subsection", "decision": "verified at explicitly final 1 L stock stage; absent from target", "qualification": "Exact hydrate/form and mass retained"}, {"owner_field": "solutions[0].composition[3].concentration", "helper_field": "composition[3].concentration", "name": "KCl", "value": "7.0", "unit": "G_PER_L", "source_key": "jcm574", "locator": "MDS salt water subsection", "decision": "verified at explicitly final 1 L stock stage; absent from target", "qualification": "Exact hydrate/form and mass retained"}, {"owner_field": "solutions[0].composition[4].concentration", "helper_field": "composition[4].concentration", "name": "1 M CaCl2 solution", "value": "5.0", "unit": "ML_PER_L", "source_key": "jcm574", "locator": "MDS salt water subsection", "decision": "verified at explicitly final 1 L stock stage; absent from target", "qualification": "CaCl2 row is 5 mL of 1 M solution, not 5 g"}, {"owner_field": "solutions[0].composition[5].concentration", "helper_field": "composition[5].concentration", "name": "Distilled water", "value": "1.0", "unit": "L", "source_key": "jcm574", "locator": "MDS salt water subsection", "decision": "verified at explicitly final 1 L stock stage; absent from target", "qualification": "Water denotes bring-to-final-volume context, not an instruction to add an extra literal 1 L after all other liquids"}], "math": {"basis": "Conditional on MediaDive J897 declared 600 mL main volume and JCM574 explicitly final 1 L stock", "main_liquid_additions_mL": [100, 500], "peptone_g_per_L": "3 / 0.6 = 5", "yeast_extract_g_per_L": "0.6 / 0.6 = 1", "MDS_dose_mL_per_L": "100 / 0.6 = 166.6666667", "stock_contributions_g_per_L": {"NaCl": "240 * 0.1 / 0.6 = 40", "MgCl2·6H2O": "30 * 0.1 / 0.6 = 5", "MgSO4·7H2O": "35 * 0.1 / 0.6 = 5.833333333", "KCl": "7 * 0.1 / 0.6 = 1.166666667"}, "CaCl2_mmol_per_L": "1 mol/L * 0.005 L * 1000 mmol/mol / 1 L stock * 0.1 L stock / 0.6 L main = 0.833333333", "Tris": "1 M adjustment solution; dispensed amount and final concentration unspecified"}}

### Every asserted primary label, chemical form and secondary key

grounding: supported. Targets: CultureMech:010360.

Primary IDs are checked against the exact OLS responses, including available chemical-form annotations; current secondary keys are checked against the pinned packaged index. Ingredient-instance denominators include direct and nested stock composition rows, exclude stock-addition doses, and remain separate for generated target, owner and contextual records. These 0–100 percentages measure linkage, not scientific correctness. Undefined mixtures are not assigned invented pure compounds.

{"counts": {"target": {"ingredient_instances": 4, "primary_ontology_instances": 2, "primary_CHEBI_instances": 2, "secondary_asserted_instances": 2, "secondary_verified_instances": 2, "primary_ontology_percent": 50.0, "secondary_verified_percent": 50.0}, "owner": {"ingredient_instances": 9, "primary_ontology_instances": 9, "primary_CHEBI_instances": 7, "secondary_asserted_instances": 7, "secondary_verified_instances": 7, "primary_ontology_percent": 100.0, "secondary_verified_percent": 77.78}, "MDS-helper": {"ingredient_instances": 6, "primary_ontology_instances": 6, "primary_CHEBI_instances": 6, "secondary_asserted_instances": 6, "secondary_verified_instances": 6, "primary_ontology_percent": 100.0, "secondary_verified_percent": 100.0}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "ingredients[1]", "preferred_term": "Yeast extract (BD-Difco)"}, {"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "ingredients[2]", "preferred_term": "Peptone (Oxoid)"}, {"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "ingredients[3]", "preferred_term": "Tris base", "primary_id": "CHEBI:9754", "canonical_label": "tris", "source_key": "chebi9754", "synonyms": ["1,1,1-tris(hydroxymethyl)methanamine", "2-Amino-2-(hydroxymethyl)-1,3-propanediol", "2-amino-2-(hydroxymethyl)propane-1,3-diol", "2-amino-2-(hydroxymethyl)propane-1,3-diol", "THAM", "Tris amino", "Tris base", "Tris buffer", "Tris", "Tris-base", "Trizma", "Trometamol", "Tromethamine", "aminotris(hydroxymethyl)methane", "tris(hydroxymethyl)aminomethane"], "form_annotations": {"generalized_empirical_formula": ["C4H11NO3"], "inchi_string": ["InChI=1S/C4H11NO3/c5-4(1-6,2-7)3-8/h6-8H,1-3,5H2"], "mass": ["121.136"], "smiles_string": ["NC(CO)(CO)CO"]}, "description": ["A primary amino compound that is &lt;em&gt;tert&lt;/em&gt;-butylamine in which one hydrogen attached to each methyl group is replaced by a hydroxy group. A compound widely used as a biological buffer substance in the pH range 7—9; p&lt;em&gt;K&lt;/em&gt;&lt;small&gt;&lt;sub&gt;a&lt;/sub&gt;&lt;/small&gt; = 8.3 at 20 °C; p&lt;em&gt;K&lt;/em&gt;&lt;small&gt;&lt;sub&gt;a&lt;/sub&gt;&lt;/small&gt; = 7.82 at 37 °C."], "secondary_id": "CHEBI:9754", "secondary_index_rows": [{"label": "Tris base", "match_type": "preferred_term", "identifier": "CHEBI:9754", "preferred_term": "Tris base", "ontology_id": "CHEBI:9754", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "ingredients[1]", "preferred_term": "Yeast extract (BD-Difco)", "primary_id": "FOODON:03315426", "canonical_label": "yeast extract", "source_key": "foodon03315426", "synonyms": [], "form_annotations": {}, "description": ["SIREN DB annotation:\n* not heat-treated FOODON:03440003\n* part of algae or fungus FOODON:03420247"]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "ingredients[2]", "preferred_term": "Peptone (Oxoid)", "primary_id": "MICRO:0000178", "canonical_label": "peptone", "source_key": "micro0000178", "synonyms": [], "form_annotations": {}, "description": []}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[0]", "preferred_term": "NaCl", "primary_id": "CHEBI:26710", "canonical_label": "sodium chloride", "source_key": "chebi26710", "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "form_annotations": {"generalized_empirical_formula": ["Cl.Na"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "smiles_string": ["[Cl-].[Na+]"]}, "description": ["An inorganic chloride salt having sodium(1+) as the counterion."], "secondary_id": "CHEBI:26710", "secondary_index_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[1]", "preferred_term": "MgCl2 x 6H2O", "primary_id": "CHEBI:86345", "canonical_label": "magnesium dichloride hexahydrate", "source_key": "chebi86345", "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate", "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "form_annotations": {"generalized_empirical_formula": ["2Cl.6H2O.Mg"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "description": ["A hydrate that is the hexahydrate form of magnesium dichloride."], "secondary_id": "CHEBI:86345", "secondary_index_rows": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[2]", "preferred_term": "MgSO4 x 7H2O", "primary_id": "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "secondary_id": "CHEBI:31795", "secondary_index_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[3]", "preferred_term": "KCl", "primary_id": "CHEBI:32588", "canonical_label": "potassium chloride", "source_key": "chebi32588", "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride", "sylvite"], "form_annotations": {"generalized_empirical_formula": ["Cl.K"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "smiles_string": ["[Cl-].[K+]"]}, "description": ["A metal chloride salt with a K(+) counterion."], "secondary_id": "CHEBI:32588", "secondary_index_rows": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[4]", "preferred_term": "1 M CaCl2 solution", "primary_id": "CHEBI:3312", "canonical_label": "calcium dichloride", "source_key": "chebi3312", "synonyms": ["CaCl2", "Calcium chloride anhydrous", "[CaCl2]", "calcium chloride anhydrous", "calcium chloride", "calcium chloride", "calcium dichloride", "calcium dichloride"], "form_annotations": {"generalized_empirical_formula": ["Ca.2Cl"], "inchi_string": ["InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2"], "mass": ["110.984"], "smiles_string": ["[Ca+2].[Cl-].[Cl-]"]}, "description": [], "secondary_id": "CHEBI:3312", "secondary_index_rows": [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[5]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[0]", "preferred_term": "NaCl", "primary_id": "CHEBI:26710", "canonical_label": "sodium chloride", "source_key": "chebi26710", "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "form_annotations": {"generalized_empirical_formula": ["Cl.Na"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "smiles_string": ["[Cl-].[Na+]"]}, "description": ["An inorganic chloride salt having sodium(1+) as the counterion."], "secondary_id": "CHEBI:26710", "secondary_index_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[1]", "preferred_term": "MgCl2 x 6H2O", "primary_id": "CHEBI:86345", "canonical_label": "magnesium dichloride hexahydrate", "source_key": "chebi86345", "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate", "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "form_annotations": {"generalized_empirical_formula": ["2Cl.6H2O.Mg"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "description": ["A hydrate that is the hexahydrate form of magnesium dichloride."], "secondary_id": "CHEBI:86345", "secondary_index_rows": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[2]", "preferred_term": "MgSO4 x 7H2O", "primary_id": "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "secondary_id": "CHEBI:31795", "secondary_index_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[3]", "preferred_term": "KCl", "primary_id": "CHEBI:32588", "canonical_label": "potassium chloride", "source_key": "chebi32588", "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride", "sylvite"], "form_annotations": {"generalized_empirical_formula": ["Cl.K"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "smiles_string": ["[Cl-].[K+]"]}, "description": ["A metal chloride salt with a K(+) counterion."], "secondary_id": "CHEBI:32588", "secondary_index_rows": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[4]", "preferred_term": "1 M CaCl2 solution", "primary_id": "CHEBI:3312", "canonical_label": "calcium dichloride", "source_key": "chebi3312", "synonyms": ["CaCl2", "Calcium chloride anhydrous", "[CaCl2]", "calcium chloride anhydrous", "calcium chloride", "calcium chloride", "calcium dichloride", "calcium dichloride"], "form_annotations": {"generalized_empirical_formula": ["Ca.2Cl"], "inchi_string": ["InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2"], "mass": ["110.984"], "smiles_string": ["[Ca+2].[Cl-].[Cl-]"]}, "description": [], "secondary_id": "CHEBI:3312", "secondary_index_rows": [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[5]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}]}

### Stock preparation, receiving pH and sterilization

consistency: concern. Targets: CultureMech:010360.

JCM574 explicitly brings MDS stock to 1 L and adjusts it to pH 7.5; JCM897 independently adjusts the receiving medium to pH 7.5 with 1 M Tris. Owner preserves these separate pH contexts and mixing steps; target lacks them. Current JCM page-wide 121 °C 15 min default is absent from both. Source instructions do not specify a fixed Tris dose or any growth atmosphere.

### Classification, applications and bounded biological evidence

scope: supported. Targets: CultureMech:010360.

The source recipe contains complex biological mixtures and agar where asserted, supporting COMPLEX/UNDEFINED and the specified liquid or agar formulation. Bacterial filing and generic microbial-cultivation application are catalogue scope. Neither target nor normalized owner asserts target organisms, strains, taxa, genomes, DOI/PMID claims or growth outcomes; no species-level growth claim is inferred from recipe names, source catalogue membership or ontology labels. Empty optional organism fields are not treated as a source contradiction.

### September repaired owner versus August generated target

ownership: concern. Targets: CultureMech:010360.

The generated target omits the repaired six-row stock composition, volume unit repairs, pH, yeast-extract and peptone primary terms, preparation, references and flags. Regenerating blindly would retain the owner’s per-liter normalization issue. Verify and correct the maintained basis first, preserve recovered content, then regenerate.

### Reference placement and formulation evidence

evidence: concern. Targets: CultureMech:010360.

Generated notes retain source URLs; owner has four exact references and row source notes. Neither source strings nor the September repair event substitutes for narrow concentration evidence. Main-batch literals, normalized provider amounts and the separate stock recipe need explicitly scoped supporting snippets.

### Append-only event history and timestamp interpretation

provenance: supported. Targets: CultureMech:010360.

All 22 scoped timestamps were checked for ISO syntax and timezone. Every instance parses and has an explicit timezone. Curation events are process provenance rather than independent confirmation of recipe correctness.

[]

## Findings

### f1: Main-batch literals are presented with incorrect mass or per-liter units

major / open / confirmed; issue key: cm010360-main-batch-units-and-volume-basis.

The target reports water 500 g/L and stock 100 g/L although both are liquid additions. Its owner changes these to 500 mL/L and 100 mL/L but retains yeast 0.6 g/L and peptone 3 g/L. JCM897 lists these as a batch with 100 mL stock plus 500 mL water; exact MediaDive declares 600 mL and g_l 1 and 5 for yeast and peptone. Neither a hidden one-liter denominator nor a mass-density conversion is supported.

### f2: Generated medium omits the recovered salt-stock composition and pH

major / open / confirmed; issue key: cm010360-generated-stock-repair-missing.

The target’s empty MDS composition and Unknown solution name omit the actual salt constituents, nested 1 M CaCl2 dose and stock/receiving pH instructions. The maintained owner and existing helper already recover these exact-source details. This is incomplete generated representation, not evidence that the stock does not exist or a broken asserted CultureMech ID.

### f3: Stock and main-recipe amount claims lack narrow evidence

minor / open / confirmed; issue key: cm010360-amount-evidence-placement.

Owner references and source notes correctly identify the sources, but per-field ingredient amounts and stock-addition doses lack concentration evidence that states their separate batch bases.

## Recommended Actions And Acceptance Checks

### a1

Preserve source batch amounts and explicit receiving-volume basis, or normalize consistently on the provider 600 mL basis with clear attribution. Retain stock concentrations at the separate 1 L stock stage and Tris as an unquantified adjustment dose; correct owner before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

After correcting receiving-volume semantics, regenerate from the verified owner and retain all six stock rows, separate stock/receiving pH, primary terms and existing references. Preserve the exact JCM source default sterilization with version scope rather than inventing a protocol.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach ingredient evidence for source masses and stock composition; use root evidence for stock-addition and nested liquid-dose claims with exact field paths, source snippets and explicit volume arithmetic.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/5_salt_water_growth_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/5_salt_water_growth_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/5_salt_water_growth_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch011/107/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch011/107/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/5_salt_water_growth_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/5_salt_water_growth_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| jcm897 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=897; Medium897, four-row main recipe, linked Medium574, pH instruction and page-wide default | supports | Read the entire primary JCM897 page: peptone (Oxoid) 3 g, yeast extract (BD-Difco) 0.6 g, MDS salt water from JCM574 100 mL and distilled water 500 mL. Adjust pH to 7.5 with 1 M Tris base. Current page-wide default sterilization is 121 °C for 15 min unless otherwise stated. |
| togoM938 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M938; $.meta; $.components[0].items[0:5]; $.comments[0] | supports | Exact M938 metadata identifies JCM_M897. Main rows retain the same batch masses and liquid volumes; MDS references M578 and Tris has conc_value=1, conc_unit=M without a dispensed amount. |
| jcm574 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=574; MDS salt water subsection and following bring-to-volume/pH sentence | supports | Read the whole page and isolate its MDS salt-water subsection: NaCl 240 g, MgCl2·6H2O 30 g, MgSO4·7H2O 35 g, KCl 7 g and 5 mL 1 M CaCl2, brought to 1 L and pH 7.5 with 1 M Tris. The parent medium and its other stock recipes remain outside the receiving formulation. |
| togoM578 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M578; $.meta; $.components[2] (paragraph_index7); $.comments[4] (paragraph_index8) | supports | M578 identifies JCM_M574. Paragraph7 is the MDS salt-water stock; paragraph 8 instructs final 1 L and pH 7.5. Other sections belong to the full DB Characterization Medium No.2, not JCM897. |
| mediadiveJ897api | https://mediadive.dsmz.de/rest/medium/J897; $.data.medium; $.data.solutions[0:2] | supports | Provider declares main solution 4891 volume 600 mL, peptone g_l 5 and yeast extract g_l 1. Its MDS stock 4404 has volume 1000 mL, the four salt mass rows and a 5 mL 1 M CaCl2 row. |
| mediadiveJ574api | https://mediadive.dsmz.de/rest/medium/J574; $.data.solutions[2] (id4404) | context_only | The exact parent provider record also defines MDS solution 4404 with the same recipe and explicit final 1 L instruction. It is used only to cross-check the stock, not to add other J574 stocks to this medium. |
| repair | scripts/repair_togo_m938_score15.py; _mds_composition, _mds_salt_water, repair_m938, repair_mds_helper | context_only | September repair pins exact owner and helper IDs, recovers the six stock rows and pH/reference context, and writes 3 g/L peptone, 0.6 g/L yeast extract, 500 mL/L water and 100 mL/L stock from source batch literals. The recovery is real but does not establish a correct one-liter receiving-medium basis. |
| togo-writer | src/culturemech/import/togo_importer.py; _ingredient_from_item, _parse_unit, _solution_from_item and _extract_preparation_steps | context_only | Current importer distinguishes liquid units and stock rows and extracts comments. Source-specific final-volume meaning still requires checking; current writer code is not evidence that the older owner or generated quantities are correct. |
| stock-helper | data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml; Entire YAML; stable CM013393, mediadive.solution4404 and six composition rows | context_only | Read the maintained helper in full and verified the exact stock identity and equality of its six composition rows to the normalized owner. It is a dependency context rather than a merge contributor. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:15377 resolves to the asserted canonical label water and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi9754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:9754 resolves to the asserted canonical label tris and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | FOODON:03315426 resolves to the asserted canonical label yeast extract and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| micro0000178 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | MICRO:0000178 resolves to the asserted canonical label peptone and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:26710 resolves to the asserted canonical label sodium chloride and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:86345 resolves to the asserted canonical label magnesium dichloride hexahydrate and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:31795 resolves to the asserted canonical label magnesium sulfate heptahydrate and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:32588 resolves to the asserted canonical label potassium chloride and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312; $._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms, annotation | supports | CHEBI:3312 resolves to the asserted canonical label calcium dichloride and is not obsolete. Complete response including available form, formula, synonym and structure annotations was inspected; recipe-specific grade and amount are separate claims. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact MAPPED/preferred_term rows for every asserted secondary key; adjacent pinned metadata | supports | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "ingredients[1]", "preferred_term": "Yeast extract (BD-Difco)"}, {"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "ingredients[2]", "preferred_term": "Peptone (Oxoid)"}, {"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "ingredients[3]", "preferred_term": "Tris base", "primary_id": "CHEBI:9754", "canonical_label": "tris", "source_key": "chebi9754", "synonyms": ["1,1,1-tris(hydroxymethyl)methanamine", "2-Amino-2-(hydroxymethyl)-1,3-propanediol", "2-amino-2-(hydroxymethyl)propane-1,3-diol", "2-amino-2-(hydroxymethyl)propane-1,3-diol", "THAM", "Tris amino", "Tris base", "Tris buffer", "Tris", "Tris-base", "Trizma", "Trometamol", "Tromethamine", "aminotris(hydroxymethyl)methane", "tris(hydroxymethyl)aminomethane"], "form_annotations": {"generalized_empirical_formula": ["C4H11NO3"], "inchi_string": ["InChI=1S/C4H11NO3/c5-4(1-6,2-7)3-8/h6-8H,1-3,5H2"], "mass": ["121.136"], "smiles_string": ["NC(CO)(CO)CO"]}, "description": ["A primary amino compound that is &lt;em&gt;tert&lt;/em&gt;-butylamine in which one hydrogen attached to each methyl group is replaced by a hydroxy group. A compound widely used as a biological buffer substance in the pH range 7—9; p&lt;em&gt;K&lt;/em&gt;&lt;small&gt;&lt;sub&gt;a&lt;/sub&gt;&lt;/small&gt; = 8.3 at 20 °C; p&lt;em&gt;K&lt;/em&gt;&lt;small&gt;&lt;sub&gt;a&lt;/sub&gt;&lt;/small&gt; = 7.82 at 37 °C."], "secondary_id": "CHEBI:9754", "secondary_index_rows": [{"label": "Tris base", "match_type": "preferred_term", "identifier": "CHEBI:9754", "preferred_term": "Tris base", "ontology_id": "CHEBI:9754", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "ingredients[1]", "preferred_term": "Yeast extract (BD-Difco)", "primary_id": "FOODON:03315426", "canonical_label": "yeast extract", "source_key": "foodon03315426", "synonyms": [], "form_annotations": {}, "description": ["SIREN DB annotation:\n* not heat-treated FOODON:03440003\n* part of algae or fungus FOODON:03420247"]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "ingredients[2]", "preferred_term": "Peptone (Oxoid)", "primary_id": "MICRO:0000178", "canonical_label": "peptone", "source_key": "micro0000178", "synonyms": [], "form_annotations": {}, "description": []}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[0]", "preferred_term": "NaCl", "primary_id": "CHEBI:26710", "canonical_label": "sodium chloride", "source_key": "chebi26710", "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "form_annotations": {"generalized_empirical_formula": ["Cl.Na"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "smiles_string": ["[Cl-].[Na+]"]}, "description": ["An inorganic chloride salt having sodium(1+) as the counterion."], "secondary_id": "CHEBI:26710", "secondary_index_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[1]", "preferred_term": "MgCl2 x 6H2O", "primary_id": "CHEBI:86345", "canonical_label": "magnesium dichloride hexahydrate", "source_key": "chebi86345", "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate", "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "form_annotations": {"generalized_empirical_formula": ["2Cl.6H2O.Mg"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "description": ["A hydrate that is the hexahydrate form of magnesium dichloride."], "secondary_id": "CHEBI:86345", "secondary_index_rows": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[2]", "preferred_term": "MgSO4 x 7H2O", "primary_id": "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "secondary_id": "CHEBI:31795", "secondary_index_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[3]", "preferred_term": "KCl", "primary_id": "CHEBI:32588", "canonical_label": "potassium chloride", "source_key": "chebi32588", "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride", "sylvite"], "form_annotations": {"generalized_empirical_formula": ["Cl.K"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "smiles_string": ["[Cl-].[K+]"]}, "description": ["A metal chloride salt with a K(+) counterion."], "secondary_id": "CHEBI:32588", "secondary_index_rows": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[4]", "preferred_term": "1 M CaCl2 solution", "primary_id": "CHEBI:3312", "canonical_label": "calcium dichloride", "source_key": "chebi3312", "synonyms": ["CaCl2", "Calcium chloride anhydrous", "[CaCl2]", "calcium chloride anhydrous", "calcium chloride", "calcium chloride", "calcium dichloride", "calcium dichloride"], "form_annotations": {"generalized_empirical_formula": ["Ca.2Cl"], "inchi_string": ["InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2"], "mass": ["110.984"], "smiles_string": ["[Ca+2].[Cl-].[Cl-]"]}, "description": [], "secondary_id": "CHEBI:3312", "secondary_index_rows": [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "solutions[0].composition[5]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[0]", "preferred_term": "NaCl", "primary_id": "CHEBI:26710", "canonical_label": "sodium chloride", "source_key": "chebi26710", "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "form_annotations": {"generalized_empirical_formula": ["Cl.Na"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "smiles_string": ["[Cl-].[Na+]"]}, "description": ["An inorganic chloride salt having sodium(1+) as the counterion."], "secondary_id": "CHEBI:26710", "secondary_index_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[1]", "preferred_term": "MgCl2 x 6H2O", "primary_id": "CHEBI:86345", "canonical_label": "magnesium dichloride hexahydrate", "source_key": "chebi86345", "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate", "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "form_annotations": {"generalized_empirical_formula": ["2Cl.6H2O.Mg"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "description": ["A hydrate that is the hexahydrate form of magnesium dichloride."], "secondary_id": "CHEBI:86345", "secondary_index_rows": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[2]", "preferred_term": "MgSO4 x 7H2O", "primary_id": "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "secondary_id": "CHEBI:31795", "secondary_index_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[3]", "preferred_term": "KCl", "primary_id": "CHEBI:32588", "canonical_label": "potassium chloride", "source_key": "chebi32588", "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride", "sylvite"], "form_annotations": {"generalized_empirical_formula": ["Cl.K"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "smiles_string": ["[Cl-].[K+]"]}, "description": ["A metal chloride salt with a K(+) counterion."], "secondary_id": "CHEBI:32588", "secondary_index_rows": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[4]", "preferred_term": "1 M CaCl2 solution", "primary_id": "CHEBI:3312", "canonical_label": "calcium dichloride", "source_key": "chebi3312", "synonyms": ["CaCl2", "Calcium chloride anhydrous", "[CaCl2]", "calcium chloride anhydrous", "calcium chloride", "calcium chloride", "calcium dichloride", "calcium dichloride"], "form_annotations": {"generalized_empirical_formula": ["Ca.2Cl"], "inchi_string": ["InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2"], "mass": ["110.984"], "smiles_string": ["[Ca+2].[Cl-].[Cl-]"]}, "description": [], "secondary_id": "CHEBI:3312", "secondary_index_rows": [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field": "composition[5]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377", "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER", "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]", "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377", "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}]} |
| history | data/merge_yaml/merged/5_salt_water_growth_medium.yaml; Every timestamp in target, owner and explicitly listed contextual dependencies | supports | [{"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-27T06:35:55.994036Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[1].timestamp", "value": "2026-01-28T19:48:16.339601Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[2].timestamp", "value": "2026-02-03T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-09T08:04:26.968063+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[4].timestamp", "value": "2026-03-13T06:20:13.259357Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[5].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[6].timestamp", "value": "2026-03-17T06:30:00.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[7].timestamp", "value": "2026-03-17T19:46:32.238153+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[8].timestamp", "value": "2026-05-16T09:03:22.160119+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[9].timestamp", "value": "2026-06-05T07:40:45.844875+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "curation_history[10].timestamp", "value": "2026-08-06T03:05:20.633441+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-27T06:35:55.994036Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[1].timestamp", "value": "2026-01-28T19:48:16.339601Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[2].timestamp", "value": "2026-02-03T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-09T08:04:26.968063+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[4].timestamp", "value": "2026-03-13T06:20:13.259357Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[5].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[6].timestamp", "value": "2026-03-17T06:30:00.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[7].timestamp", "value": "2026-03-17T19:46:32.238153+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[8].timestamp", "value": "2026-05-16T09:03:22.160119+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[9].timestamp", "value": "2026-06-05T07:40:45.844875+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field": "curation_history[10].timestamp", "value": "2026-09-11T00:00:00-07:00", "valid_ISO_datetime": true, "timezone_aware": true}] |

## Limits And Additional Notes

- JCM897 lists 100 mL MDS stock and 500 mL water; MediaDive explicitly declares a 600 mL main volume. Per-liter calculations below are conditional on that provider-declared basis, not an independently measured final volume after solids or pH titration.
- JCM574 is a different full medium. Only its named MDS salt-water subsection defines the stock used here; its vitamins, phosphate buffer and other stock additions are not ingredients of JCM897.
- The normalized MDS helper CM013393 is contextual support for stock identity, not an ID explicitly asserted by the generated target. No broken CultureMech solution reference is invented.
- The 1 M Tris concentration describes the pH-adjustment solution. Its dispensed volume and final medium concentration are unspecified.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084040Z-culturemech-010360-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 5_salt_water_growth_medium (CultureMech:010360)'
started_at: '2026-10-21T08:29:15Z'
finished_at: '2026-10-21T08:40:40Z'
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
summary: 'Exact TOGO M938/JCM897 identity is supported. The generated target retains
  a 100 g/L empty MDS-stock placeholder and 500 g/L water, omitting the stock composition,
  pH and source references already recovered in its normalized owner. The owner repair
  preserves literal batch amounts but still labels them per liter: the exact provider
  declares a 600 mL main batch, giving peptone 5 g/L and yeast extract 1 g/L. The
  stock itself is explicitly brought to 1 L and must remain separate. All four documented
  diagnostics pass.'
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
  - path: data/merge_yaml/merged/5_salt_water_growth_medium.yaml
    sha256: 9dc2e34c42aa16fd721dda5a986cd79b968204a5195a9f97b4330b9212479072
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M578_DB_Characterization_Medium_NO._2.yaml
    sha256: 6fa9484819e533b7c47f5fc98308da6af89097fe123659223328b19871c109d4
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml
    sha256: f28ce669f44022e2b9868a1e69d8140b338c6b1218b8a994a39510f79b1adb41
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml
    sha256: 041e240b0c7b7e7e06eccc8b43903615ce3204f0e110a6bdc1a05224c9b09ab3
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
  - path: scripts/repair_togo_m938_score15.py
    sha256: c5589cb4cf3e2940ef3ce0e0c49fcddfd83167392d28cb9c5510b6e2becfbce9
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
  selection: Task review 107; batch 011 item 7 of 10, selected in Python lexicographic
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
  - CultureMech:010360
targets:
- target_id: CultureMech:010360
  path: data/merge_yaml/merged/5_salt_water_growth_medium.yaml
  label: 5_salt_water_growth_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/5_salt_water_growth_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/5_salt_water_growth_medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch011/107/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch011/107/strict.tsv"
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/5_salt_water_growth_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/5_salt_water_growth_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010360
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
  - CultureMech:010360
- check_id: scoped-history-timestamps
  name: Scoped history timestamp syntax and timezone check
  required: false
  status: passed
  summary: 22 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Existing provenance is preserved; no timestamps were rewritten.
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/5_salt_water_growth_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:40:40Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:40:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/5_salt_water_growth_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:30:24.377366Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/5_salt_water_growth_medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch011/107/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:30:28.673138Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch011/107/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/5_salt_water_growth_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:30:35.575015Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/5_salt_water_growth_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:30:41.189032Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: jcm897
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=897
  locator: Medium897, four-row main recipe, linked Medium574, pH instruction and page-wide
    default
  accessed_at: '2026-10-21T08:23:36.048679Z'
  support: supports
  summary: 'Read the entire primary JCM897 page: peptone (Oxoid) 3 g, yeast extract
    (BD-Difco) 0.6 g, MDS salt water from JCM574 100 mL and distilled water 500 mL.
    Adjust pH to 7.5 with 1 M Tris base. Current page-wide default sterilization is
    121 °C for 15 min unless otherwise stated.'
  snapshot_sha256: 07ff8fd55f3dd14c7529f03e018bdc497445b23135b981406f4a4f439e47e795
- evidence_id: togoM938
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M938
  locator: $.meta; $.components[0].items[0:5]; $.comments[0]
  accessed_at: '2026-10-21T08:23:34.844880Z'
  support: supports
  summary: Exact M938 metadata identifies JCM_M897. Main rows retain the same batch
    masses and liquid volumes; MDS references M578 and Tris has conc_value=1, conc_unit=M
    without a dispensed amount.
  snapshot_sha256: 52a62ce686524732fe5fcb7e04862de9e8e316046664c4ba61f5fbc26138ed2e
- evidence_id: jcm574
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=574
  locator: MDS salt water subsection and following bring-to-volume/pH sentence
  accessed_at: '2026-10-21T08:23:35.914237Z'
  support: supports
  summary: 'Read the whole page and isolate its MDS salt-water subsection: NaCl 240
    g, MgCl2·6H2O 30 g, MgSO4·7H2O 35 g, KCl 7 g and 5 mL 1 M CaCl2, brought to 1
    L and pH 7.5 with 1 M Tris. The parent medium and its other stock recipes remain
    outside the receiving formulation.'
  snapshot_sha256: c94fcb12b856675574dd0b1766493de62e18406b29e208285c340a72edfffb63
- evidence_id: togoM578
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M578
  locator: $.meta; $.components[2] (paragraph_index7); $.comments[4] (paragraph_index8)
  accessed_at: '2026-10-21T08:23:34.710370Z'
  support: supports
  summary: M578 identifies JCM_M574. Paragraph7 is the MDS salt-water stock; paragraph
    8 instructs final 1 L and pH 7.5. Other sections belong to the full DB Characterization
    Medium No.2, not JCM897.
  snapshot_sha256: 1b101f2be3f12a6b88b284df90b3369c5b359d83517fefe582bcb42c0ae904e6
- evidence_id: mediadiveJ897api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J897
  locator: $.data.medium; $.data.solutions[0:2]
  accessed_at: '2026-10-21T08:23:34.137064Z'
  support: supports
  summary: Provider declares main solution 4891 volume 600 mL, peptone g_l 5 and yeast
    extract g_l 1. Its MDS stock 4404 has volume 1000 mL, the four salt mass rows
    and a 5 mL 1 M CaCl2 row.
  snapshot_sha256: be23e191389218e7173c24a0b661bc1454de0281f452052fc170d84174d43d30
- evidence_id: mediadiveJ574api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J574
  locator: $.data.solutions[2] (id4404)
  accessed_at: '2026-10-21T08:23:33.420979Z'
  support: context_only
  summary: The exact parent provider record also defines MDS solution 4404 with the
    same recipe and explicit final 1 L instruction. It is used only to cross-check
    the stock, not to add other J574 stocks to this medium.
  snapshot_sha256: 186c5383b696eb915c015a43a3111e73ec6927c33e14867005973a01af0e9145
- evidence_id: repair
  kind: record_content
  reference: scripts/repair_togo_m938_score15.py
  locator: _mds_composition, _mds_salt_water, repair_m938, repair_mds_helper
  accessed_at: '2026-10-21T08:40:40Z'
  support: context_only
  summary: September repair pins exact owner and helper IDs, recovers the six stock
    rows and pH/reference context, and writes 3 g/L peptone, 0.6 g/L yeast extract,
    500 mL/L water and 100 mL/L stock from source batch literals. The recovery is
    real but does not establish a correct one-liter receiving-medium basis.
- evidence_id: togo-writer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _parse_unit, _solution_from_item and _extract_preparation_steps
  accessed_at: '2026-10-21T08:40:40Z'
  support: context_only
  summary: Current importer distinguishes liquid units and stock rows and extracts
    comments. Source-specific final-volume meaning still requires checking; current
    writer code is not evidence that the older owner or generated quantities are correct.
- evidence_id: stock-helper
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml
  locator: Entire YAML; stable CM013393, mediadive.solution4404 and six composition
    rows
  accessed_at: '2026-10-21T08:40:40Z'
  support: context_only
  summary: Read the maintained helper in full and verified the exact stock identity
    and equality of its six composition rows to the normalized owner. It is a dependency
    context rather than a merge contributor.
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
- evidence_id: chebi9754
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T08:23:35.430164Z'
  support: supports
  summary: CHEBI:9754 resolves to the asserted canonical label tris and is not obsolete.
    Complete response including available form, formula, synonym and structure annotations
    was inspected; recipe-specific grade and amount are separate claims.
  snapshot_sha256: b9f921dfa34f343d4ef51ee217fc47702a8f03e2b9a8353effa10de89e9c6659
- evidence_id: foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T08:00:49.388263Z'
  support: supports
  summary: FOODON:03315426 resolves to the asserted canonical label yeast extract
    and is not obsolete. Complete response including available form, formula, synonym
    and structure annotations was inspected; recipe-specific grade and amount are
    separate claims.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: micro0000178
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T08:00:49.423450Z'
  support: supports
  summary: MICRO:0000178 resolves to the asserted canonical label peptone and is not
    obsolete. Complete response including available form, formula, synonym and structure
    annotations was inspected; recipe-specific grade and amount are separate claims.
  snapshot_sha256: ef45aa186438f91d015280171fde8ccb25740a50cc6f2c6e848de6aad3339b31
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T08:17:28.023873Z'
  support: supports
  summary: CHEBI:26710 resolves to the asserted canonical label sodium chloride and
    is not obsolete. Complete response including available form, formula, synonym
    and structure annotations was inspected; recipe-specific grade and amount are
    separate claims.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to the asserted canonical label magnesium dichloride
    hexahydrate and is not obsolete. Complete response including available form, formula,
    synonym and structure annotations was inspected; recipe-specific grade and amount
    are separate claims.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
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
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to the asserted canonical label potassium chloride
    and is not obsolete. Complete response including available form, formula, synonym
    and structure annotations was inspected; recipe-specific grade and amount are
    separate claims.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi3312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312
  locator: '$._embedded.terms[0]: obo_id, label, is_obsolete, description, synonyms,
    annotation'
  accessed_at: '2026-10-21T07:16:24.822837Z'
  support: supports
  summary: CHEBI:3312 resolves to the asserted canonical label calcium dichloride
    and is not obsolete. Complete response including available form, formula, synonym
    and structure annotations was inspected; recipe-specific grade and amount are
    separate claims.
  snapshot_sha256: 34ed49d95375c80dcb07576c67d04fa77337bfecf406accb283e8c32253b754b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact MAPPED/preferred_term rows for every asserted secondary key; adjacent
    pinned metadata
  accessed_at: '2026-10-21T08:40:40Z'
  support: supports
  summary: '{"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count":
    9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id",
    "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech",
    "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"},
    "instances": [{"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
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
    "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "ingredients[1]", "preferred_term": "Yeast extract (BD-Difco)"}, {"layer":
    "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field":
    "ingredients[2]", "preferred_term": "Peptone (Oxoid)"}, {"layer": "target", "path":
    "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "ingredients[3]",
    "preferred_term": "Tris base", "primary_id": "CHEBI:9754", "canonical_label":
    "tris", "source_key": "chebi9754", "synonyms": ["1,1,1-tris(hydroxymethyl)methanamine",
    "2-Amino-2-(hydroxymethyl)-1,3-propanediol", "2-amino-2-(hydroxymethyl)propane-1,3-diol",
    "2-amino-2-(hydroxymethyl)propane-1,3-diol", "THAM", "Tris amino", "Tris base",
    "Tris buffer", "Tris", "Tris-base", "Trizma", "Trometamol", "Tromethamine", "aminotris(hydroxymethyl)methane",
    "tris(hydroxymethyl)aminomethane"], "form_annotations": {"generalized_empirical_formula":
    ["C4H11NO3"], "inchi_string": ["InChI=1S/C4H11NO3/c5-4(1-6,2-7)3-8/h6-8H,1-3,5H2"],
    "mass": ["121.136"], "smiles_string": ["NC(CO)(CO)CO"]}, "description": ["A primary
    amino compound that is <em>tert</em>-butylamine in which one hydrogen attached
    to each methyl group is replaced by a hydroxy group. A compound widely used as
    a biological buffer substance in the pH range 7—9; p<em>K</em><small><sub>a</sub></small>
    = 8.3 at 20 °C; p<em>K</em><small><sub>a</sub></small> = 7.82 at 37 °C."], "secondary_id":
    "CHEBI:9754", "secondary_index_rows": [{"label": "Tris base", "match_type": "preferred_term",
    "identifier": "CHEBI:9754", "preferred_term": "Tris base", "ontology_id": "CHEBI:9754",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field":
    "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377",
    "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER",
    "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]",
    "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen
    hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula":
    ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string":
    ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom
    that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377",
    "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer":
    "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "ingredients[1]", "preferred_term": "Yeast extract (BD-Difco)", "primary_id":
    "FOODON:03315426", "canonical_label": "yeast extract", "source_key": "foodon03315426",
    "synonyms": [], "form_annotations": {}, "description": ["SIREN DB annotation:\n*
    not heat-treated FOODON:03440003\n* part of algae or fungus FOODON:03420247"]},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "ingredients[2]", "preferred_term": "Peptone (Oxoid)", "primary_id":
    "MICRO:0000178", "canonical_label": "peptone", "source_key": "micro0000178", "synonyms":
    [], "form_annotations": {}, "description": []}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "solutions[0].composition[0]", "preferred_term": "NaCl", "primary_id":
    "CHEBI:26710", "canonical_label": "sodium chloride", "source_key": "chebi26710",
    "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro
    sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium
    chloride", "sodium chloride", "table salt"], "form_annotations": {"generalized_empirical_formula":
    ["Cl.Na"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"],
    "smiles_string": ["[Cl-].[Na+]"]}, "description": ["An inorganic chloride salt
    having sodium(1+) as the counterion."], "secondary_id": "CHEBI:26710", "secondary_index_rows":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "solutions[0].composition[1]", "preferred_term": "MgCl2 x 6H2O", "primary_id":
    "CHEBI:86345", "canonical_label": "magnesium dichloride hexahydrate", "source_key":
    "chebi86345", "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium
    chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate",
    "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "form_annotations":
    {"generalized_empirical_formula": ["2Cl.6H2O.Mg"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"],
    "mass": ["203.301"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "description":
    ["A hydrate that is the hexahydrate form of magnesium dichloride."], "secondary_id":
    "CHEBI:86345", "secondary_index_rows": [{"label": "Magnesium chloride", "match_type":
    "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride",
    "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "solutions[0].composition[2]", "preferred_term": "MgSO4 x 7H2O", "primary_id":
    "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key":
    "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter
    salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium
    sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water
    (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."],
    "secondary_id": "CHEBI:31795", "secondary_index_rows": [{"label": "MgSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "solutions[0].composition[3]", "preferred_term": "KCl", "primary_id":
    "CHEBI:32588", "canonical_label": "potassium chloride", "source_key": "chebi32588",
    "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium
    chloride", "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride",
    "sylvite"], "form_annotations": {"generalized_empirical_formula": ["Cl.K"], "inchi_string":
    ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "smiles_string": ["[Cl-].[K+]"]},
    "description": ["A metal chloride salt with a K(+) counterion."], "secondary_id":
    "CHEBI:32588", "secondary_index_rows": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field":
    "solutions[0].composition[4]", "preferred_term": "1 M CaCl2 solution", "primary_id":
    "CHEBI:3312", "canonical_label": "calcium dichloride", "source_key": "chebi3312",
    "synonyms": ["CaCl2", "Calcium chloride anhydrous", "[CaCl2]", "calcium chloride
    anhydrous", "calcium chloride", "calcium chloride", "calcium dichloride", "calcium
    dichloride"], "form_annotations": {"generalized_empirical_formula": ["Ca.2Cl"],
    "inchi_string": ["InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2"], "mass": ["110.984"], "smiles_string":
    ["[Ca+2].[Cl-].[Cl-]"]}, "description": [], "secondary_id": "CHEBI:3312", "secondary_index_rows":
    [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312",
    "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "solutions[0].composition[5]", "preferred_term": "Distilled water", "primary_id":
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
    "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml",
    "field": "composition[0]", "preferred_term": "NaCl", "primary_id": "CHEBI:26710",
    "canonical_label": "sodium chloride", "source_key": "chebi26710", "synonyms":
    ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico",
    "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride",
    "sodium chloride", "table salt"], "form_annotations": {"generalized_empirical_formula":
    ["Cl.Na"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"],
    "smiles_string": ["[Cl-].[Na+]"]}, "description": ["An inorganic chloride salt
    having sodium(1+) as the counterion."], "secondary_id": "CHEBI:26710", "secondary_index_rows":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml",
    "field": "composition[1]", "preferred_term": "MgCl2 x 6H2O", "primary_id": "CHEBI:86345",
    "canonical_label": "magnesium dichloride hexahydrate", "source_key": "chebi86345",
    "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride
    hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate",
    "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "form_annotations":
    {"generalized_empirical_formula": ["2Cl.6H2O.Mg"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"],
    "mass": ["203.301"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "description":
    ["A hydrate that is the hexahydrate form of magnesium dichloride."], "secondary_id":
    "CHEBI:86345", "secondary_index_rows": [{"label": "Magnesium chloride", "match_type":
    "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride",
    "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml",
    "field": "composition[2]", "preferred_term": "MgSO4 x 7H2O", "primary_id": "CHEBI:31795",
    "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795",
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."],
    "secondary_id": "CHEBI:31795", "secondary_index_rows": [{"label": "MgSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml",
    "field": "composition[3]", "preferred_term": "KCl", "primary_id": "CHEBI:32588",
    "canonical_label": "potassium chloride", "source_key": "chebi32588", "synonyms":
    ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium chloride",
    "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride", "sylvite"],
    "form_annotations": {"generalized_empirical_formula": ["Cl.K"], "inchi_string":
    ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "smiles_string": ["[Cl-].[K+]"]},
    "description": ["A metal chloride salt with a K(+) counterion."], "secondary_id":
    "CHEBI:32588", "secondary_index_rows": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper",
    "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field":
    "composition[4]", "preferred_term": "1 M CaCl2 solution", "primary_id": "CHEBI:3312",
    "canonical_label": "calcium dichloride", "source_key": "chebi3312", "synonyms":
    ["CaCl2", "Calcium chloride anhydrous", "[CaCl2]", "calcium chloride anhydrous",
    "calcium chloride", "calcium chloride", "calcium dichloride", "calcium dichloride"],
    "form_annotations": {"generalized_empirical_formula": ["Ca.2Cl"], "inchi_string":
    ["InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2"], "mass": ["110.984"], "smiles_string": ["[Ca+2].[Cl-].[Cl-]"]},
    "description": [], "secondary_id": "CHEBI:3312", "secondary_index_rows": [{"label":
    "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term":
    "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml",
    "field": "composition[5]", "preferred_term": "Distilled water", "primary_id":
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
    "unique"}]}]}'
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/5_salt_water_growth_medium.yaml
  locator: Every timestamp in target, owner and explicitly listed contextual dependencies
  accessed_at: '2026-10-21T08:40:40Z'
  support: supports
  summary: '[{"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field":
    "curation_history[0].timestamp", "value": "2026-01-27T06:35:55.994036Z", "valid_ISO_datetime":
    true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "curation_history[1].timestamp", "value": "2026-01-28T19:48:16.339601Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "curation_history[2].timestamp", "value": "2026-02-03T00:00:00+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "curation_history[3].timestamp", "value": "2026-03-09T08:04:26.968063+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "curation_history[4].timestamp", "value": "2026-03-13T06:20:13.259357Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "curation_history[5].timestamp", "value": "2026-03-14T00:00:00+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "curation_history[6].timestamp", "value": "2026-03-17T06:30:00.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "curation_history[7].timestamp", "value": "2026-03-17T19:46:32.238153+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "curation_history[8].timestamp", "value": "2026-05-16T09:03:22.160119+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "curation_history[9].timestamp", "value": "2026-06-05T07:40:45.844875+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "curation_history[10].timestamp", "value": "2026-08-06T03:05:20.633441+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[0].timestamp", "value": "2026-01-27T06:35:55.994036Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[1].timestamp", "value": "2026-01-28T19:48:16.339601Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[2].timestamp", "value": "2026-02-03T00:00:00+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[3].timestamp", "value": "2026-03-09T08:04:26.968063+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[4].timestamp", "value": "2026-03-13T06:20:13.259357Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[5].timestamp", "value": "2026-03-14T00:00:00+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[6].timestamp", "value": "2026-03-17T06:30:00.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[7].timestamp", "value": "2026-03-17T19:46:32.238153+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[8].timestamp", "value": "2026-05-16T09:03:22.160119+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[9].timestamp", "value": "2026-06-05T07:40:45.844875+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "curation_history[10].timestamp", "value": "2026-09-11T00:00:00-07:00",
    "valid_ISO_datetime": true, "timezone_aware": true}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact receiving medium and stock source identity
  outcome: supported
  summary: M938, JCM897 and the stable record ID agree. The M578/JCM574 cross-reference
    is to its MDS subsection. Exact provider stock 4404 and local helper CM013393
    corroborate that subsection; no whole-medium substitution or missing ID is assumed.
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - record
  - owner-0
  - jcm897
  - togoM938
  - jcm574
  - togoM578
  - mediadiveJ897api
  - stock-helper
- assessment_id: main-amounts
  area: quantity
  topic: All four target ingredients and the stock addition
  outcome: concern
  summary: Every direct target row and stock dose is itemized. Primary batch literals
    are supported, but target water/stock units are dimensionally wrong and owner
    per-liter values retain a 600 mL batch’s literals. Provider volume 600 mL supports
    peptone 5 g/L, yeast extract 1 g/L and stock 166.666667 mL/L; retain the source
    batch if a final-volume representation cannot be expressed faithfully. Tris dose
    remains unquantified.
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - record
  - owner-0
  - jcm897
  - togoM938
  - mediadiveJ897api
  details: '[{"target_field": "ingredients[0].concentration", "owner_field": "ingredients[0].concentration",
    "name": "Distilled water", "target": "500 G_PER_L", "owner": "500 ML_PER_L", "source":
    "500 mL in main recipe", "source_key": "jcm897", "decision": "correct target dimension;
    preserve literal 500 mL batch solvent or normalize only on explicit 600 mL provider
    basis", "calculation": "500 / 0.6 = 833.333333 mL/L on provider basis; no mass
    conversion"}, {"target_field": "ingredients[1].concentration", "owner_field":
    "ingredients[1].concentration", "name": "Yeast extract (BD-Difco)", "target":
    "0.6 G_PER_L", "owner": "0.6 G_PER_L", "source": "0.6 g in main recipe", "source_key":
    "mediadiveJ897api", "locator": "$.data.solutions[0].recipe[1]", "decision": "correct
    per-liter basis", "calculation": "0.6 g / 0.6 L = 1 g/L, matching provider g_l"},
    {"target_field": "ingredients[2].concentration", "owner_field": "ingredients[2].concentration",
    "name": "Peptone (Oxoid)", "target": "3 G_PER_L", "owner": "3 G_PER_L", "source":
    "3 g in main recipe", "source_key": "mediadiveJ897api", "locator": "$.data.solutions[0].recipe[0]",
    "decision": "correct per-liter basis", "calculation": "3 g / 0.6 L = 5 g/L, matching
    provider g_l"}, {"target_field": "ingredients[3].concentration", "owner_field":
    "preparation_steps[1].description", "name": "Tris base", "target": "variable VARIABLE",
    "owner": "adjust pH7.5 with1M Tris", "source": "1 M Tris base used for pH adjustment;
    no addition volume", "source_key": "jcm897", "decision": "not_quantified final
    dose; preserve adjustment-stock strength and pH, do not assert 1 M final concentration"},
    {"target_field": "solutions[0].concentration", "owner_field": "solutions[0].concentration",
    "name": "MDS salt water", "target": "100 G_PER_L", "owner": "100 ML_PER_L", "source":
    "100 mL in main recipe", "source_key": "mediadiveJ897api", "locator": "$.data.solutions[0].recipe[2]",
    "decision": "correct target dimension and both layers’ receiving-medium basis",
    "calculation": "100 mL / 0.6 L = 166.666667 mL/L conditionally on provider main
    volume"}]'
- assessment_id: stock-amounts
  area: quantity
  topic: Every nested MDS stock row and conditional delivered contribution
  outcome: concern
  summary: The six owner/helper composition rows are assessed at the explicitly final
    1 L MDS stock stage. Their water row/note lists 1 L water, while the preparation
    text correctly says bring to final 1 L; preserve that final-volume meaning rather
    than adding an extra literal liter of water. The generated target instead has
    an empty composition and Unknown solution name. On the provider 600 mL receiving
    basis, 100 mL stock contributes NaCl 40 g/L, MgCl2·6H2O 5 g/L, MgSO4·7H2O 5.833333
    g/L, KCl 1.166667 g/L and CaCl2 0.833333 mmol/L. These calculations do not replace
    stock concentrations or add duplicate direct ingredients.
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - record
  - owner-0
  - jcm574
  - togoM578
  - mediadiveJ897api
  - mediadiveJ574api
  - stock-helper
  details: '{"stock_rows": [{"owner_field": "solutions[0].composition[0].concentration",
    "helper_field": "composition[0].concentration", "name": "NaCl", "value": "240.0",
    "unit": "G_PER_L", "source_key": "jcm574", "locator": "MDS salt water subsection",
    "decision": "verified at explicitly final 1 L stock stage; absent from target",
    "qualification": "Exact hydrate/form and mass retained"}, {"owner_field": "solutions[0].composition[1].concentration",
    "helper_field": "composition[1].concentration", "name": "MgCl2 x 6H2O", "value":
    "30.0", "unit": "G_PER_L", "source_key": "jcm574", "locator": "MDS salt water
    subsection", "decision": "verified at explicitly final 1 L stock stage; absent
    from target", "qualification": "Exact hydrate/form and mass retained"}, {"owner_field":
    "solutions[0].composition[2].concentration", "helper_field": "composition[2].concentration",
    "name": "MgSO4 x 7H2O", "value": "35.0", "unit": "G_PER_L", "source_key": "jcm574",
    "locator": "MDS salt water subsection", "decision": "verified at explicitly final
    1 L stock stage; absent from target", "qualification": "Exact hydrate/form and
    mass retained"}, {"owner_field": "solutions[0].composition[3].concentration",
    "helper_field": "composition[3].concentration", "name": "KCl", "value": "7.0",
    "unit": "G_PER_L", "source_key": "jcm574", "locator": "MDS salt water subsection",
    "decision": "verified at explicitly final 1 L stock stage; absent from target",
    "qualification": "Exact hydrate/form and mass retained"}, {"owner_field": "solutions[0].composition[4].concentration",
    "helper_field": "composition[4].concentration", "name": "1 M CaCl2 solution",
    "value": "5.0", "unit": "ML_PER_L", "source_key": "jcm574", "locator": "MDS salt
    water subsection", "decision": "verified at explicitly final 1 L stock stage;
    absent from target", "qualification": "CaCl2 row is 5 mL of 1 M solution, not
    5 g"}, {"owner_field": "solutions[0].composition[5].concentration", "helper_field":
    "composition[5].concentration", "name": "Distilled water", "value": "1.0", "unit":
    "L", "source_key": "jcm574", "locator": "MDS salt water subsection", "decision":
    "verified at explicitly final 1 L stock stage; absent from target", "qualification":
    "Water denotes bring-to-final-volume context, not an instruction to add an extra
    literal 1 L after all other liquids"}], "math": {"basis": "Conditional on MediaDive
    J897 declared 600 mL main volume and JCM574 explicitly final 1 L stock", "main_liquid_additions_mL":
    [100, 500], "peptone_g_per_L": "3 / 0.6 = 5", "yeast_extract_g_per_L": "0.6 /
    0.6 = 1", "MDS_dose_mL_per_L": "100 / 0.6 = 166.6666667", "stock_contributions_g_per_L":
    {"NaCl": "240 * 0.1 / 0.6 = 40", "MgCl2·6H2O": "30 * 0.1 / 0.6 = 5", "MgSO4·7H2O":
    "35 * 0.1 / 0.6 = 5.833333333", "KCl": "7 * 0.1 / 0.6 = 1.166666667"}, "CaCl2_mmol_per_L":
    "1 mol/L * 0.005 L * 1000 mmol/mol / 1 L stock * 0.1 L stock / 0.6 L main = 0.833333333",
    "Tris": "1 M adjustment solution; dispensed amount and final concentration unspecified"}}'
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
  - CultureMech:010360
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi15377
  - chebi9754
  - foodon03315426
  - micro0000178
  - chebi26710
  - chebi86345
  - chebi31795
  - chebi32588
  - chebi3312
  details: '{"counts": {"target": {"ingredient_instances": 4, "primary_ontology_instances":
    2, "primary_CHEBI_instances": 2, "secondary_asserted_instances": 2, "secondary_verified_instances":
    2, "primary_ontology_percent": 50.0, "secondary_verified_percent": 50.0}, "owner":
    {"ingredient_instances": 9, "primary_ontology_instances": 9, "primary_CHEBI_instances":
    7, "secondary_asserted_instances": 7, "secondary_verified_instances": 7, "primary_ontology_percent":
    100.0, "secondary_verified_percent": 77.78}, "MDS-helper": {"ingredient_instances":
    6, "primary_ontology_instances": 6, "primary_CHEBI_instances": 6, "secondary_asserted_instances":
    6, "secondary_verified_instances": 6, "primary_ontology_percent": 100.0, "secondary_verified_percent":
    100.0}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
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
    "unique"}]}, {"layer": "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml",
    "field": "ingredients[1]", "preferred_term": "Yeast extract (BD-Difco)"}, {"layer":
    "target", "path": "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field":
    "ingredients[2]", "preferred_term": "Peptone (Oxoid)"}, {"layer": "target", "path":
    "data/merge_yaml/merged/5_salt_water_growth_medium.yaml", "field": "ingredients[3]",
    "preferred_term": "Tris base", "primary_id": "CHEBI:9754", "canonical_label":
    "tris", "source_key": "chebi9754", "synonyms": ["1,1,1-tris(hydroxymethyl)methanamine",
    "2-Amino-2-(hydroxymethyl)-1,3-propanediol", "2-amino-2-(hydroxymethyl)propane-1,3-diol",
    "2-amino-2-(hydroxymethyl)propane-1,3-diol", "THAM", "Tris amino", "Tris base",
    "Tris buffer", "Tris", "Tris-base", "Trizma", "Trometamol", "Tromethamine", "aminotris(hydroxymethyl)methane",
    "tris(hydroxymethyl)aminomethane"], "form_annotations": {"generalized_empirical_formula":
    ["C4H11NO3"], "inchi_string": ["InChI=1S/C4H11NO3/c5-4(1-6,2-7)3-8/h6-8H,1-3,5H2"],
    "mass": ["121.136"], "smiles_string": ["NC(CO)(CO)CO"]}, "description": ["A primary
    amino compound that is <em>tert</em>-butylamine in which one hydrogen attached
    to each methyl group is replaced by a hydroxy group. A compound widely used as
    a biological buffer substance in the pH range 7—9; p<em>K</em><small><sub>a</sub></small>
    = 8.3 at 20 °C; p<em>K</em><small><sub>a</sub></small> = 7.82 at 37 °C."], "secondary_id":
    "CHEBI:9754", "secondary_index_rows": [{"label": "Tris base", "match_type": "preferred_term",
    "identifier": "CHEBI:9754", "preferred_term": "Tris base", "ontology_id": "CHEBI:9754",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field":
    "ingredients[0]", "preferred_term": "Distilled water", "primary_id": "CHEBI:15377",
    "canonical_label": "water", "source_key": "chebi15377", "synonyms": ["BOUND WATER",
    "H(2)O", "H2O", "HOH", "WATER", "WATER", "Wasser", "Water", "Water", "[OH2]",
    "acqua", "agua", "aqua", "dihydridooxygen", "dihydrogen oxide", "eau", "hydrogen
    hydroxide", "oxidane", "oxidane", "water", "water"], "form_annotations": {"generalized_empirical_formula":
    ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string":
    ["[H]O[H]"]}, "description": ["An oxygen hydride consisting of an oxygen atom
    that is covalently bonded to two hydrogen atoms"], "secondary_id": "CHEBI:15377",
    "secondary_index_rows": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer":
    "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "ingredients[1]", "preferred_term": "Yeast extract (BD-Difco)", "primary_id":
    "FOODON:03315426", "canonical_label": "yeast extract", "source_key": "foodon03315426",
    "synonyms": [], "form_annotations": {}, "description": ["SIREN DB annotation:\n*
    not heat-treated FOODON:03440003\n* part of algae or fungus FOODON:03420247"]},
    {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "ingredients[2]", "preferred_term": "Peptone (Oxoid)", "primary_id":
    "MICRO:0000178", "canonical_label": "peptone", "source_key": "micro0000178", "synonyms":
    [], "form_annotations": {}, "description": []}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "solutions[0].composition[0]", "preferred_term": "NaCl", "primary_id":
    "CHEBI:26710", "canonical_label": "sodium chloride", "source_key": "chebi26710",
    "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro
    sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium
    chloride", "sodium chloride", "table salt"], "form_annotations": {"generalized_empirical_formula":
    ["Cl.Na"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"],
    "smiles_string": ["[Cl-].[Na+]"]}, "description": ["An inorganic chloride salt
    having sodium(1+) as the counterion."], "secondary_id": "CHEBI:26710", "secondary_index_rows":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "solutions[0].composition[1]", "preferred_term": "MgCl2 x 6H2O", "primary_id":
    "CHEBI:86345", "canonical_label": "magnesium dichloride hexahydrate", "source_key":
    "chebi86345", "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium
    chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate",
    "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "form_annotations":
    {"generalized_empirical_formula": ["2Cl.6H2O.Mg"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"],
    "mass": ["203.301"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "description":
    ["A hydrate that is the hexahydrate form of magnesium dichloride."], "secondary_id":
    "CHEBI:86345", "secondary_index_rows": [{"label": "Magnesium chloride", "match_type":
    "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride",
    "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "solutions[0].composition[2]", "preferred_term": "MgSO4 x 7H2O", "primary_id":
    "CHEBI:31795", "canonical_label": "magnesium sulfate heptahydrate", "source_key":
    "chebi31795", "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter
    salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium
    sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water
    (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."],
    "secondary_id": "CHEBI:31795", "secondary_index_rows": [{"label": "MgSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "solutions[0].composition[3]", "preferred_term": "KCl", "primary_id":
    "CHEBI:32588", "canonical_label": "potassium chloride", "source_key": "chebi32588",
    "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium
    chloride", "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride",
    "sylvite"], "form_annotations": {"generalized_empirical_formula": ["Cl.K"], "inchi_string":
    ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "smiles_string": ["[Cl-].[K+]"]},
    "description": ["A metal chloride salt with a K(+) counterion."], "secondary_id":
    "CHEBI:32588", "secondary_index_rows": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "owner", "path":
    "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml", "field":
    "solutions[0].composition[4]", "preferred_term": "1 M CaCl2 solution", "primary_id":
    "CHEBI:3312", "canonical_label": "calcium dichloride", "source_key": "chebi3312",
    "synonyms": ["CaCl2", "Calcium chloride anhydrous", "[CaCl2]", "calcium chloride
    anhydrous", "calcium chloride", "calcium chloride", "calcium dichloride", "calcium
    dichloride"], "form_annotations": {"generalized_empirical_formula": ["Ca.2Cl"],
    "inchi_string": ["InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2"], "mass": ["110.984"], "smiles_string":
    ["[Ca+2].[Cl-].[Cl-]"]}, "description": [], "secondary_id": "CHEBI:3312", "secondary_index_rows":
    [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312",
    "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "owner", "path": "data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml",
    "field": "solutions[0].composition[5]", "preferred_term": "Distilled water", "primary_id":
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
    "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml",
    "field": "composition[0]", "preferred_term": "NaCl", "primary_id": "CHEBI:26710",
    "canonical_label": "sodium chloride", "source_key": "chebi26710", "synonyms":
    ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico",
    "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride",
    "sodium chloride", "table salt"], "form_annotations": {"generalized_empirical_formula":
    ["Cl.Na"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"],
    "smiles_string": ["[Cl-].[Na+]"]}, "description": ["An inorganic chloride salt
    having sodium(1+) as the counterion."], "secondary_id": "CHEBI:26710", "secondary_index_rows":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml",
    "field": "composition[1]", "preferred_term": "MgCl2 x 6H2O", "primary_id": "CHEBI:86345",
    "canonical_label": "magnesium dichloride hexahydrate", "source_key": "chebi86345",
    "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride
    hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate",
    "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "form_annotations":
    {"generalized_empirical_formula": ["2Cl.6H2O.Mg"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"],
    "mass": ["203.301"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "description":
    ["A hydrate that is the hexahydrate form of magnesium dichloride."], "secondary_id":
    "CHEBI:86345", "secondary_index_rows": [{"label": "Magnesium chloride", "match_type":
    "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride",
    "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml",
    "field": "composition[2]", "preferred_term": "MgSO4 x 7H2O", "primary_id": "CHEBI:31795",
    "canonical_label": "magnesium sulfate heptahydrate", "source_key": "chebi31795",
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "form_annotations": {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "description": ["A hydrate that is the heptahydrate form of magnesium sulfate."],
    "secondary_id": "CHEBI:31795", "secondary_index_rows": [{"label": "MgSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml",
    "field": "composition[3]", "preferred_term": "KCl", "primary_id": "CHEBI:32588",
    "canonical_label": "potassium chloride", "source_key": "chebi32588", "synonyms":
    ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium chloride",
    "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride", "sylvite"],
    "form_annotations": {"generalized_empirical_formula": ["Cl.K"], "inchi_string":
    ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "smiles_string": ["[Cl-].[K+]"]},
    "description": ["A metal chloride salt with a K(+) counterion."], "secondary_id":
    "CHEBI:32588", "secondary_index_rows": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}, {"layer": "MDS-helper",
    "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml", "field":
    "composition[4]", "preferred_term": "1 M CaCl2 solution", "primary_id": "CHEBI:3312",
    "canonical_label": "calcium dichloride", "source_key": "chebi3312", "synonyms":
    ["CaCl2", "Calcium chloride anhydrous", "[CaCl2]", "calcium chloride anhydrous",
    "calcium chloride", "calcium chloride", "calcium dichloride", "calcium dichloride"],
    "form_annotations": {"generalized_empirical_formula": ["Ca.2Cl"], "inchi_string":
    ["InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2"], "mass": ["110.984"], "smiles_string": ["[Ca+2].[Cl-].[Cl-]"]},
    "description": [], "secondary_id": "CHEBI:3312", "secondary_index_rows": [{"label":
    "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term":
    "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, {"layer": "MDS-helper", "path": "data/normalized_yaml/bacterial/mediadive_4404_MDS_salt_water.yaml",
    "field": "composition[5]", "preferred_term": "Distilled water", "primary_id":
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
    "unique"}]}]}'
- assessment_id: preparation
  area: consistency
  topic: Stock preparation, receiving pH and sterilization
  outcome: concern
  summary: JCM574 explicitly brings MDS stock to 1 L and adjusts it to pH 7.5; JCM897
    independently adjusts the receiving medium to pH 7.5 with 1 M Tris. Owner preserves
    these separate pH contexts and mixing steps; target lacks them. Current JCM page-wide
    121 °C 15 min default is absent from both. Source instructions do not specify
    a fixed Tris dose or any growth atmosphere.
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - record
  - owner-0
  - jcm897
  - jcm574
  - repair
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
  - CultureMech:010360
  evidence_ids:
  - record
  - owner-0
  - jcm897
  - jcm574
- assessment_id: ownership
  area: ownership
  topic: September repaired owner versus August generated target
  outcome: concern
  summary: The generated target omits the repaired six-row stock composition, volume
    unit repairs, pH, yeast-extract and peptone primary terms, preparation, references
    and flags. Regenerating blindly would retain the owner’s per-liter normalization
    issue. Verify and correct the maintained basis first, preserve recovered content,
    then regenerate.
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - record
  - owner-0
  - repair
  - togo-writer
  - stock-helper
- assessment_id: evidence
  area: evidence
  topic: Reference placement and formulation evidence
  outcome: concern
  summary: Generated notes retain source URLs; owner has four exact references and
    row source notes. Neither source strings nor the September repair event substitutes
    for narrow concentration evidence. Main-batch literals, normalized provider amounts
    and the separate stock recipe need explicitly scoped supporting snippets.
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - record
  - owner-0
  - jcm897
  - togoM938
  - jcm574
  - mediadiveJ897api
- assessment_id: history
  area: provenance
  topic: Append-only event history and timestamp interpretation
  outcome: supported
  summary: All 22 scoped timestamps were checked for ISO syntax and timezone. Every
    instance parses and has an explicit timezone. Curation events are process provenance
    rather than independent confirmation of recipe correctness.
  target_ids:
  - CultureMech:010360
  evidence_ids:
  - record
  - owner-0
  - history
  details: '[]'
findings:
- finding_id: f1
  issue_key: cm010360-main-batch-units-and-volume-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Main-batch literals are presented with incorrect mass or per-liter units
  description: The target reports water 500 g/L and stock 100 g/L although both are
    liquid additions. Its owner changes these to 500 mL/L and 100 mL/L but retains
    yeast 0.6 g/L and peptone 3 g/L. JCM897 lists these as a batch with 100 mL stock
    plus 500 mL water; exact MediaDive declares 600 mL and g_l 1 and 5 for yeast and
    peptone. Neither a hidden one-liter denominator nor a mass-density conversion
    is supported.
  target_ids:
  - CultureMech:010360
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[2].concentration
  - solutions[0].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm897
  - togoM938
  - mediadiveJ897api
  - repair
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml
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
  issue_key: cm010360-generated-stock-repair-missing
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Generated medium omits the recovered salt-stock composition and pH
  description: The target’s empty MDS composition and Unknown solution name omit the
    actual salt constituents, nested 1 M CaCl2 dose and stock/receiving pH instructions.
    The maintained owner and existing helper already recover these exact-source details.
    This is incomplete generated representation, not evidence that the stock does
    not exist or a broken asserted CultureMech ID.
  target_ids:
  - CultureMech:010360
  field_paths:
  - solutions[0].composition
  - solutions[0].name
  - solutions[0].preparation_notes
  - ph_value
  - preparation_steps
  - references
  evidence_ids:
  - record
  - owner-0
  - jcm897
  - jcm574
  - repair
  - stock-helper
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: cm010360-amount-evidence-placement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Stock and main-recipe amount claims lack narrow evidence
  description: Owner references and source notes correctly identify the sources, but
    per-field ingredient amounts and stock-addition doses lack concentration evidence
    that states their separate batch bases.
  target_ids:
  - CultureMech:010360
  field_paths:
  - ingredients[*].evidence
  - solutions[0].composition[*].evidence
  - evidence
  evidence_ids:
  - record
  - owner-0
  - jcm897
  - jcm574
  - mediadiveJ897api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml
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
  description: Preserve source batch amounts and explicit receiving-volume basis,
    or normalize consistently on the provider 600 mL basis with clear attribution.
    Retain stock concentrations at the separate 1 L stock stage and Tris as an unquantified
    adjustment dose; correct owner before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010360
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml
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
  description: After correcting receiving-volume semantics, regenerate from the verified
    owner and retain all six stock rows, separate stock/receiving pH, primary terms
    and existing references. Preserve the exact JCM source default sterilization with
    version scope rather than inventing a protocol.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010360
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml
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
  description: Attach ingredient evidence for source masses and stock composition;
    use root evidence for stock-addition and nested liquid-dose claims with exact
    field paths, source snippets and explicit volume arithmetic.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010360
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml
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
- JCM897 lists 100 mL MDS stock and 500 mL water; MediaDive explicitly declares a
  600 mL main volume. Per-liter calculations below are conditional on that provider-declared
  basis, not an independently measured final volume after solids or pH titration.
- JCM574 is a different full medium. Only its named MDS salt-water subsection defines
  the stock used here; its vitamins, phosphate buffer and other stock additions are
  not ingredients of JCM897.
- The normalized MDS helper CM013393 is contextual support for stock identity, not
  an ID explicitly asserted by the generated target. No broken CultureMech solution
  reference is invented.
- The 1 M Tris concentration describes the pH-adjustment solution. Its dispensed volume
  and final medium concentration are unspecified.
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
