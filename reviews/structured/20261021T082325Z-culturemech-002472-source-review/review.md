# Source and formulation review: 3_8m_characterization_medium_no_1 (CultureMech:002472)

- Review: 20261021T082325Z-culturemech-002472-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:09:16Z
- Finished UTC: 2026-10-21T08:23:25Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact J1309 provider record supports the medium identity but exposes major stock-stage and unit errors in all local layers: eight volume additions are labelled g/L, the saltwater/vitamin/trace stock compositions are flattened into final-medium ingredients, preparation boundaries are lost, nickel chloride hexahydrate is grounded to anhydrous nickel dichloride, and source DL-calcium pantothenate is assigned a stereospecific D-calcium pantothenate structure. The live JCM1309 endpoint returned no formulation, so this is a partial source review using explicitly identified MediaDive API/PDF evidence; four documented diagnostics pass.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 96; batch 010 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding nine task batches contain 90 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 92 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002472 | data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml | generated | 3_8m_characterization_medium_no_1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002472 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002472 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch010/096/strict.tsv |
| validate-terms | passed | True | CultureMech:002472 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002472 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002472 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact current JCM1309 primary formulation | unavailable | True | CultureMech:002472 | Live query contains Nothing found; static PDF candidate404. Exact providerAPI/PDF support bounded assessment, but current primary reconciliation remains unavailable. |
| Target and owner timestamp syntax and timezone scope | passed | False | CultureMech:002472 | All 13 target/owner history timestamps parse with explicit timezones; no chronology or scientific correctness is inferred from timestamp syntax. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002472.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:002472.

24 primary CHEBI identities resolve with matching labels; 24 of 24 current secondary keys have live pinned-index rows. Unresolved keys: [].

27 direct ingredient instances; CHEBI-primary instance linkage 24/27 (88.89%), verified secondary coverage 24/27 (88.89%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Exact source accession and generated ownership

identity: supported. Targets: CultureMech:002472.

Stable CM002472, merge-event source basename, maintained owner and exact MediaDive J1309 agree on identity. Provider identifies pH 7.5 and a complex liquid medium; exact primary formulation access remains unavailable.

### Every direct ingredient, nested stock and dose

quantity: concern. Targets: CultureMech:002472.

All 27 direct claims are traced: two retain provider-normalized direct masses; eight misuse volume-dose numerals as g/L; four saltwater rows and thirteen vitamin/trace rows lose their stock stages. Source vitamin 3 mL and trace 5 mL doses are absent as structured solution additions. The main volume additions total 1000 mL, while the provider declares 1005 mL; all numerical final-concentration examples remain conditional and the discrepancy is unresolved.

[{"field": "ingredients[0].concentration", "material": "Salt water", "local": {"value": "830", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[0]", "source_row": {"recipe_order": 1, "compound": "Salt water", "compound_id": 1508, "attribute": "see below, 30%", "amount": 830, "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve source mL addition plus stock strength, not the same numeral in g/L", "calculation": null}, {"field": "ingredients[1].concentration", "material": "Peptone", "local": {"value": "0.0248756", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[1]", "source_row": {"recipe_order": 2, "compound": "Peptone", "compound_id": 1, "attribute": "Oxoid", "amount": 0.025, "unit": "g", "g_l": 0.0248756, "optional": 0}, "decision": "verified provider g/L normalization; original mass is0.025g peptone or5mg yeast per declared1005mL, not independently primary-verified", "calculation": null}, {"field": "ingredients[2].concentration", "material": "Yeast extract", "local": {"value": "0.00497512", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[2]", "source_row": {"recipe_order": 3, "compound": "Yeast extract", "compound_id": 16, "amount": 5, "unit": "mg", "g_l": 0.00497512, "optional": 0}, "decision": "verified provider g/L normalization; original mass is0.025g peptone or5mg yeast per declared1005mL, not independently primary-verified", "calculation": null}, {"field": "ingredients[3].concentration", "material": "NH4Cl", "local": {"value": "5", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[3]", "source_row": {"recipe_order": 4, "compound": "NH4Cl", "compound_id": 42, "attribute": "1M", "amount": 5, "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve source mL addition plus stock strength, not the same numeral in g/L", "calculation": null}, {"field": "ingredients[4].concentration", "material": "K2HPO4", "local": {"value": "2", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[4]", "source_row": {"recipe_order": 5, "compound": "K2HPO4", "compound_id": 10, "attribute": "0.5 M", "amount": 2, "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve source mL addition plus stock strength, not the same numeral in g/L", "calculation": null}, {"field": "ingredients[5].concentration", "material": "FeSO4 x 7 H2O", "local": {"value": "5", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[5]", "source_row": {"recipe_order": 6, "compound": "FeSO4 x 7 H2O", "compound_id": 12, "attribute": "*, 0.15%", "amount": 5, "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve source mL addition plus stock strength, not the same numeral in g/L", "calculation": null}, {"field": "ingredients[6].concentration", "material": "Sodium pyruvate", "local": {"value": "50", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[8]", "source_row": {"recipe_order": 9, "compound": "Sodium pyruvate", "compound_id": 438, "attribute": "1.0 M", "amount": 50, "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve source mL addition plus stock strength, not the same numeral in g/L", "calculation": null}, {"field": "ingredients[7].concentration", "material": "Sodium perchlorate", "local": {"value": "50", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[9]", "source_row": {"recipe_order": 10, "compound": "Sodium perchlorate", "compound_id": 2064, "attribute": "1.0 M", "amount": 50, "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve source mL addition plus stock strength, not the same numeral in g/L", "calculation": null}, {"field": "ingredients[8].concentration", "material": "Sodium Thiosulfate", "local": {"value": "50", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[10]", "source_row": {"recipe_order": 11, "compound": "Sodium Thiosulfate", "compound_id": 1126, "attribute": "1.0 M", "amount": 50, "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve source mL addition plus stock strength, not the same numeral in g/L", "calculation": null}, {"field": "ingredients[9].concentration", "material": "NaCl", "local": {"value": "238.806", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[11]", "source_row": {"recipe_order": 12, "compound": "NaCl", "compound_id": 43, "amount": 240, "unit": "g", "g_l": 238.806, "mmol_l": 4086.34, "optional": 0}, "decision": "correct stage: constituent of separate30% saltwater stock dosed830mL, not an additional neat final-medium mass", "calculation": "If stock is made to1L and receiving volume is1.005L: 240g/L stock ×0.830L/1.005L = 198.2089552238805970149253731g/L; conditional provider interpretation only."}, {"field": "ingredients[10].concentration", "material": "MgCl2 x 6 H2O", "local": {"value": "24.7761", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[12]", "source_row": {"recipe_order": 13, "compound": "MgCl2 x 6 H2O", "compound_id": 79, "amount": 24.9, "unit": "g", "g_l": 24.7761, "mmol_l": 121.868, "optional": 0}, "decision": "correct stage: constituent of separate30% saltwater stock dosed830mL, not an additional neat final-medium mass", "calculation": "If stock is made to1L and receiving volume is1.005L: 24.9g/L stock ×0.830L/1.005L = 20.56417910447761194029850746g/L; conditional provider interpretation only."}, {"field": "ingredients[11].concentration", "material": "MgSO4 x 7 H2O", "local": {"value": "28.8557", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[13]", "source_row": {"recipe_order": 14, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 29, "unit": "g", "g_l": 28.8557, "mmol_l": 117.073, "optional": 0}, "decision": "correct stage: constituent of separate30% saltwater stock dosed830mL, not an additional neat final-medium mass", "calculation": "If stock is made to1L and receiving volume is1.005L: 29g/L stock ×0.830L/1.005L = 23.95024875621890547263681592g/L; conditional provider interpretation only."}, {"field": "ingredients[12].concentration", "material": "KCl", "local": {"value": "6.96517", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[14]", "source_row": {"recipe_order": 15, "compound": "KCl", "compound_id": 61, "amount": 7, "unit": "g", "g_l": 6.96517, "mmol_l": 93.4296, "optional": 0}, "decision": "correct stage: constituent of separate30% saltwater stock dosed830mL, not an additional neat final-medium mass", "calculation": "If stock is made to1L and receiving volume is1.005L: 7g/L stock ×0.830L/1.005L = 5.781094527363184079601990050g/L; conditional provider interpretation only."}, {"field": "ingredients[13].concentration", "material": "CaCl2", "local": {"value": "5", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[15]", "source_row": {"recipe_order": 16, "compound": "CaCl2", "compound_id": 81, "attribute": "1M", "amount": 5, "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve source mL addition plus stock strength, not the same numeral in g/L", "calculation": null}, {"field": "ingredients[14].concentration", "material": "Thiamine HCl", "local": {"value": "0.033", "unit": "G_PER_L"}, "source_solution_id": 5467, "source_locator": "$.data.solutions[1].recipe[0]", "source_row": {"recipe_order": 1, "compound": "Thiamine HCl", "compound_id": 1207, "amount": 33, "unit": "mg", "g_l": 0.033, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.033g/L stock ×0.003L/1.005L = 0.00009850746268656716417910447761g/L on provider nominal1005mL basis."}, {"field": "ingredients[15].concentration", "material": "Riboflavin", "local": {"value": "0.01", "unit": "G_PER_L"}, "source_solution_id": 5467, "source_locator": "$.data.solutions[1].recipe[1]", "source_row": {"recipe_order": 2, "compound": "Riboflavin", "compound_id": 136, "amount": 10, "unit": "mg", "g_l": 0.01, "mmol_l": 0.0265675, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.01g/L stock ×0.003L/1.005L = 0.00002985074626865671641791044776g/L on provider nominal1005mL basis."}, {"field": "ingredients[16].concentration", "material": "Nicotinic acid", "local": {"value": "0.033", "unit": "G_PER_L"}, "source_solution_id": 5467, "source_locator": "$.data.solutions[1].recipe[2]", "source_row": {"recipe_order": 3, "compound": "Nicotinic acid", "compound_id": 139, "amount": 33, "unit": "mg", "g_l": 0.033, "mmol_l": 0.268053, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.033g/L stock ×0.003L/1.005L = 0.00009850746268656716417910447761g/L on provider nominal1005mL basis."}, {"field": "ingredients[17].concentration", "material": "DL-Calcium pantothenate", "local": {"value": "0.017", "unit": "G_PER_L"}, "source_solution_id": 5467, "source_locator": "$.data.solutions[1].recipe[3]", "source_row": {"recipe_order": 4, "compound": "DL-Calcium pantothenate", "compound_id": 1720, "amount": 17, "unit": "mg", "g_l": 0.017, "mmol_l": 0.0356768, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.017g/L stock ×0.003L/1.005L = 0.00005074626865671641791044776119g/L on provider nominal1005mL basis."}, {"field": "ingredients[18].concentration", "material": "Vitamin B12", "local": {"value": "0.017", "unit": "G_PER_L"}, "source_solution_id": 5467, "source_locator": "$.data.solutions[1].recipe[4]", "source_row": {"recipe_order": 5, "compound": "Vitamin B12", "compound_id": 18, "amount": 17, "unit": "mg", "g_l": 0.017, "mmol_l": 0.0125424, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.017g/L stock ×0.003L/1.005L = 0.00005074626865671641791044776119g/L on provider nominal1005mL basis."}, {"field": "ingredients[19].concentration", "material": "p-Aminobenzoic acid", "local": {"value": "0.013", "unit": "G_PER_L"}, "source_solution_id": 5467, "source_locator": "$.data.solutions[1].recipe[5]", "source_row": {"recipe_order": 6, "compound": "p-Aminobenzoic acid", "compound_id": 47, "amount": 13, "unit": "mg", "g_l": 0.013, "mmol_l": 0.0947936, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.013g/L stock ×0.003L/1.005L = 0.00003880597014925373134328358209g/L on provider nominal1005mL basis."}, {"field": "ingredients[20].concentration", "material": "ZnCl2", "local": {"value": "0.07", "unit": "G_PER_L"}, "source_solution_id": 3847, "source_locator": "$.data.solutions[2].recipe[0]", "source_row": {"recipe_order": 1, "compound": "ZnCl2", "compound_id": 64, "amount": 70, "unit": "mg", "g_l": 0.07, "mmol_l": 0.513573, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.07g/L stock ×0.005L/1.005L = 0.0003482587064676616915422885572g/L on provider nominal1005mL basis."}, {"field": "ingredients[21].concentration", "material": "MnCl2 x 4 H2O", "local": {"value": "0.1", "unit": "G_PER_L"}, "source_solution_id": 3847, "source_locator": "$.data.solutions[2].recipe[1]", "source_row": {"recipe_order": 2, "compound": "MnCl2 x 4 H2O", "compound_id": 36, "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l": 0.505293, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.1g/L stock ×0.005L/1.005L = 0.0004975124378109452736318407960g/L on provider nominal1005mL basis."}, {"field": "ingredients[22].concentration", "material": "H3BO3", "local": {"value": "0.006", "unit": "G_PER_L"}, "source_solution_id": 3847, "source_locator": "$.data.solutions[2].recipe[2]", "source_row": {"recipe_order": 3, "compound": "H3BO3", "compound_id": 37, "amount": 6, "unit": "mg", "g_l": 0.006, "mmol_l": 0.0970246, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.006g/L stock ×0.005L/1.005L = 0.00002985074626865671641791044776g/L on provider nominal1005mL basis."}, {"field": "ingredients[23].concentration", "material": "CoCl2 x 6 H2O", "local": {"value": "0.19", "unit": "G_PER_L"}, "source_solution_id": 3847, "source_locator": "$.data.solutions[2].recipe[3]", "source_row": {"recipe_order": 4, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 190, "unit": "mg", "g_l": 0.19, "mmol_l": 1.46335, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.19g/L stock ×0.005L/1.005L = 0.0009452736318407960199004975124g/L on provider nominal1005mL basis."}, {"field": "ingredients[24].concentration", "material": "CuCl2 x 2 H2O", "local": {"value": "0.002", "unit": "G_PER_L"}, "source_solution_id": 3847, "source_locator": "$.data.solutions[2].recipe[4]", "source_row": {"recipe_order": 5, "compound": "CuCl2 x 2 H2O", "compound_id": 39, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l": 0.0117314, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.002g/L stock ×0.005L/1.005L = 0.000009950248756218905472636815920g/L on provider nominal1005mL basis."}, {"field": "ingredients[25].concentration", "material": "NiCl2 x 6 H2O", "local": {"value": "0.024", "unit": "G_PER_L"}, "source_solution_id": 3847, "source_locator": "$.data.solutions[2].recipe[5]", "source_row": {"recipe_order": 6, "compound": "NiCl2 x 6 H2O", "compound_id": 40, "amount": 24, "unit": "mg", "g_l": 0.024, "mmol_l": 0.185187, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.024g/L stock ×0.005L/1.005L = 0.0001194029850746268656716417910g/L on provider nominal1005mL basis."}, {"field": "ingredients[26].concentration", "material": "Na2MoO4 x 2 H2O", "local": {"value": "0.036", "unit": "G_PER_L"}, "source_solution_id": 3847, "source_locator": "$.data.solutions[2].recipe[6]", "source_row": {"recipe_order": 7, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 36, "unit": "mg", "g_l": 0.036, "mmol_l": 0.148791, "optional": 0}, "decision": "correct stock/final-medium confusion: local number equals source stock g/L before its separate dose", "calculation": "0.036g/L stock ×0.005L/1.005L = 0.0001791044776119402985074626866g/L on provider nominal1005mL basis."}]

### All four steps and stage-specific conditions

completeness: concern. Targets: CultureMech:002472.

Step 1 retains a dangling following-solutions reference but loses the ingredients to which it applies and the starred filter-sterilized mapping; step 2 correctly retains 10 mL Balch-tube distribution, butyl stoppers and N2; step 3 is only a saltwater heading; step 4 carries the stock 1 L make-up/pH instruction without explicit stock scope. Global pH 7.5 agrees with provider medium metadata, but stock/receiving-medium contexts must remain explicit. No temperature/time beyond inspected source is invented.

### Current writer versus unchanged normalized content

ownership: concern. Targets: CultureMech:002472.

Generated and maintained ingredient/preparation bytes agree; these defects are not exclusively stale generated output. Curate the normalized owner and review the current importer’s residual molar-stock/subsection handling before regeneration. The existing history records imports and canonicalization, not independent formulation verification.

### Growth, category, variants and annotations

scope: unknown. Targets: CultureMech:002472.

No target organisms, strain accessions, DOI/PMID, parent/child variant or genome claims are present. Complex/undefined liquid status fits the listed mixtures and absence of agar, but no exact organism-category or high_metal threshold is established. The latter should be reassessed once trace doses are corrected. Source absence is not negative growth evidence.

### Source-explicit nickel hydrate

grounding: concern. Targets: CultureMech:002472.

ingredients[25] names nickel chloride hexahydrate but both primary/secondary terms encode Cl2Ni. Other asserted label correspondences are checked separately; no unverified replacement identifier or molar-mass conversion is proposed.

### Source DL reagent versus stereospecific ontology structure

grounding: concern. Targets: CultureMech:002472.

Source vitamin solution 5467 recipe[3] (fourth displayed row) specifies DL-Calcium pantothenate 17 mg per 1 L; ingredients[17] retains that preferred term but both ontology links assert CHEBI31345, whose captured structural annotations and D synonyms do not establish the DL reagent identity. Preserve the 17 mg stock amount and DL form, and leave a replacement identifier unresolved.

### Source provenance and amount evidence

evidence: concern. Targets: CultureMech:002472.

A JCM URL exists in notes and provider accession in media_term; neither local layer has structured references or claim-level ingredient/stock evidence. Preserve exact provider version, primary-access limit, original units and dilution basis while repairing the scientific claims. All target/owner history timestamps were inspected with timezone scope; no events were changed.

## Findings

### f1: Eight stock-volume additions are encoded as g/L

major / open / confirmed; issue key: cm002472-stock-volume-numerals-as-mass.

Saltwater 830 mL, NH4Cl 5 mL(1 M), K2HPO4 2 mL(0.5 M), FeSO4·7H2O5 mL(0.15%), three 50 mL 1 M organic/electron-acceptor stocks, and saltwater CaCl2 5 mL(1 M) have been copied as the same numeralsg/L. These are dimensional and preparation-stage errors in both local layers.

### f2: Saltwater, vitamin and trace stocks are treated as final-medium ingredients

major / open / confirmed; issue key: cm002472-nested-stock-flattening.

Four saltwater and thirteen vitamin/trace concentrations lose their stock context, while structured 830 mL saltwater,3 mL vitamin and 5 mL trace doses are absent. This risks double-counting saltwater and overconcentrating nested supplements. The provider main recipe itself embeds the saltwater section, so source headings must be used rather than treating every primary API row as a neat addition.

### f3: Preparation omits the stock-specific addition and sterilization context

major / open / confirmed; issue key: cm002472-preparation-stage-boundaries.

The four steps preserve fragments but lose which additions follow cooling, which starred stocks are filter sterilized, and that 30% saltwater is separately made to 1 L. A saltwater heading is represented as a standalone MIX step and following-solutions text is disconnected from its doses.

### f4: Nickel chloride hexahydrate is grounded to Cl2Ni

major / open / confirmed; issue key: cm002472-nickel-hydrate-identity.

Source and preferred_term specify NiCl2×6H2O, while CHEBI34887 has formula Cl2Ni. Both primary and secondary links repeat the anhydrous identity; a valid canonical label does not resolve this chemical-form mismatch.

### f5: Source DL-calcium pantothenate is assigned a stereospecific structure

major / open / confirmed; issue key: cm002472-dl-pantothenate-stereospecific-grounding.

ingredients[17] and the source specify DL-Calcium pantothenate,17 mg per vitamin-stock litre. CHEBI31345 has a generic label but the inspected entry specifies stereochemistry and D-calcium pantothenate synonyms. Neither that structure nor label correspondence establishes identity with the source DL reagent. Both primary and secondary links therefore overstate the supported chemical form.

## Recommended Actions And Acceptance Checks

### a1

Restore source-defined stock strengths, mL doses and enclosing batch/stage with bounded evidence. Do not invent percentage basis, density or hydrate molecular weight; retain unresolved current-primary reconciliation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent the source stock hierarchy and dose once; preserve constituent stock recipes and separate any calculated final contributions. Reassesshigh_metal after amounts are corrected.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Restore base, saltwater, vitamin and trace preparation boundaries and attach cooling/sterilization instructions to exact source additions while retaining N2 and tube conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Verify an exact hydrate grounding against the packaged resolver and authoritative ontology; preserve source hydrate and leave unresolved rather than force an unverified identifier.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Verify an exact source-compatible DL grounding or retain the unresolved form explicitly; preserve the 17 mg stock amount and do not replace the source reagent with a D-only preparation or invent a replacement CHEBI identifier.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch010/096/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch010/096/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| provider | https://mediadive.dsmz.de/rest/medium/J1309; $.data.medium; $.data.solutions[0:3] | supports | Exact J1309 identity, pH 7.5, main 5466 nominal 1005 mL, vitamin 5467 per 1000 mL and trace 3847 per 1000 mL were inspected in full. Main volume doses and strength annotations are separate fields; nested g_l values describe stock composition. |
| provider-pdf | https://mediadive.dsmz.de/pdf/J1309; PDF pages1–2 | supports | Read both pages. The provider rendering separates the 30% saltwater heading and vitamin/trace recipes, and marks post-cooling additions and starred filter-sterilized stocks. It credits JCM2022 but is served/generated by MediaDive. |
| primary-unavailable | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1309; Whole returned body | unknown | Exact live JCM1309 query returned no formulation. HTTP 200 is transport success, not primary-source access. |
| primary-pdf-unavailable | https://jcm.brc.riken.jp/en/wp-content/uploads/medium/JCM1309.pdf; HTTP response | unknown | Bounded candidate official static PDF returned HTTP 404. The error response is retained and supplies no formulation. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi132103 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132103; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:132103 resolves to sodium perchlorate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi132112 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132112; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:132112 resolves to sodium thiosulfate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15940 resolves to nicotinic acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17015 resolves to riboflavin and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:176843 resolves to vitamin B12 and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:30753 resolves to 4-aminobenzoic acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31206 resolves to ammonium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31345 resolves to Calcium pantothenate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:33118 resolves to boric acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:3312 resolves to calcium dichloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:34887 resolves to nickel dichloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:49105 resolves to thiamine hydrochloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:49976 resolves to zinc dichloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:50144 resolves to sodium pyruvate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:75213 resolves to sodium molybdate dihydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:132103": [{"label": "Sodium perchlorate", "match_type": "preferred_term", "identifier": "CHEBI:132103", "preferred_term": "Sodium perchlorate", "ontology_id": "CHEBI:132103", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:132112": [{"label": "Na2S2O3", "match_type": "preferred_term", "identifier": "CHEBI:132112", "preferred_term": "Na2S2O3", "ontology_id": "CHEBI:132112", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3312": [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| importer | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit | context_only | Current importer restricts direct ingredients to primary solution, preserves explicit solution_id and percentage-bearing mL stocks, and normalizesml to ML_PER_L. Its stock detector checks percentage annotations but does not generally recognize plain 1 M/0.5 M or g/L stock annotations. The API saltwater subsection is itself embedded inside primary recipe rows, so merely rerunning current code is not proven to repair all stages. Source read only; not executed. |
| nickel-form | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; _embedded.terms[0].label,annotation.generalized_empirical_formula,annotation.mass | supports | OLS exact CHEBI34887 is nickel dichloride, empirical formula Cl2Ni and mass 129.599. It does not encode the six waters explicitly required by source and preferred_term NiCl2×6H2O. Canonical ID/label agreement cannot validate that hydrate identity. |
| pantothenate-form | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; _embedded.terms[0].synonyms, annotation.inchi_string, annotation.smiles_string | supports | The full OLS entry has a generic canonical label but lists D-calcium pantothenate and Calcium pantothenate, d- synonyms. Its InChI specifies stereochemistry with suffix /t2*7-;/m00./s1 and its SMILES gives two [C@@H] moieties. This is a stereospecific structure, while the source explicitly specifies DL-Calcium pantothenate. The exact DL-compatible grounding remains unresolved. |
| history | data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml; Every timestamp in target and sole normalized owner | supports | [{"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-26T17:53:19.390901Z", "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T06:19:13.607219Z", "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-17T06:30:15.000000Z", "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-17T19:45:26.745213+00:00", "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[4].timestamp", "value": "2026-06-05T07:40:15.797629+00:00", "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[5].timestamp", "value": "2026-06-10T07:46:42.545165+00:00", "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[6].timestamp", "value": "2026-08-06T03:04:34.086339+00:00", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-26T17:53:19.390901Z", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T06:19:13.607219Z", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-17T06:30:15.000000Z", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-17T19:45:26.745213+00:00", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[4].timestamp", "value": "2026-06-05T07:40:15.797629+00:00", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml", "field": "curation_history[5].timestamp", "value": "2026-06-10T07:46:42.545165+00:00", "timezone_aware": true}] |

## Limits And Additional Notes

- The current JCM1309 endpoint returned HTTP 200 with Nothing found; a bounded official static-PDF candidate returned 404. The exact MediaDive J1309 API and provider-generated PDF are available, but are secondary source versions rather than recovered current primary text. Final source reconciliation remains open.
- The provider declares a 1005 mL final volume, but the explicit main additions total 1000 mL (830+5+2+5+5+3+50+50+50); the separate saltwater recipe also includes 5 mL calcium stock. The 1000-versus-1005 mL discrepancy remains unresolved, and no causal attribution is made. Numerical dilution examples are conditional on the provider-reported basis, not a validated final volume. Percentage annotations 0.15% and 30% lack an explicit w/v or v/v basis; no density or percentage-basis assumption is used.
- No new organism, strain, taxon, assembly or literature-growth assertion is inferred. The target asserts no organism identifiers. Bacterial filing and high_metal are not independently established by a cultivation experiment; the high_metal tag should be reassessed after the stock-stage corrections.
- Public ontology captures identify the asserted terms; no replacement nickel-hydrate or DL-calcium-pantothenate identifier is proposed without exact verification. The DL reagent remains 17 mg per source vitamin-stock litre; no stereoisomer substitution or altered stock mass is proposed. Undefined peptone and yeast extract remain mixtures.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082325Z-culturemech-002472-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 3_8m_characterization_medium_no_1 (CultureMech:002472)'
started_at: '2026-10-21T08:09:16Z'
finished_at: '2026-10-21T08:23:25Z'
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
scientific_review: true
summary: 'The exact J1309 provider record supports the medium identity but exposes
  major stock-stage and unit errors in all local layers: eight volume additions are
  labelled g/L, the saltwater/vitamin/trace stock compositions are flattened into
  final-medium ingredients, preparation boundaries are lost, nickel chloride hexahydrate
  is grounded to anhydrous nickel dichloride, and source DL-calcium pantothenate is
  assigned a stereospecific D-calcium pantothenate structure. The live JCM1309 endpoint
  returned no formulation, so this is a partial source review using explicitly identified
  MediaDive API/PDF evidence; four documented diagnostics pass.'
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
  - path: data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
    sha256: 0790769e6906cd5393358fdcb21dd33cd81f0829424d10e1a3e41ccedd995b21
    role: target
  - path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
    sha256: b31628f1d0b081562ef8f764338fdb98521bdd52a21f573e2b2fc34c5dcd9a73
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
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/mediadive_raw_yaml.py
    sha256: 70ba720001705c315f2c5bd40871e08f6f429b6229c78255e6c94dfdcc482432
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  selection: Task review 96; batch 010 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding nine task batches contain
    90 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 92 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002472
targets:
- target_id: CultureMech:002472
  path: data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
  label: 3_8m_characterization_medium_no_1
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch010/096/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch010/096/strict.tsv"
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002472
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
  - CultureMech:002472
- check_id: primary-source-access
  name: Exact current JCM1309 primary formulation
  required: true
  status: unavailable
  summary: Live query contains Nothing found; static PDF candidate404. Exact providerAPI/PDF
    support bounded assessment, but current primary reconciliation remains unavailable.
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - primary-unavailable
  - primary-pdf-unavailable
  - provider
  - provider-pdf
- check_id: scoped-history-timestamps
  name: Target and owner timestamp syntax and timezone scope
  required: false
  status: passed
  summary: All 13 target/owner history timestamps parse with explicit timezones; no
    chronology or scientific correctness is inferred from timestamp syntax.
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:23:25Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:23:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:09:46.447253Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch010/096/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:09:56.415417Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch010/096/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:09:59.054812Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:00.289250Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1309
  locator: $.data.medium; $.data.solutions[0:3]
  accessed_at: '2026-10-21T08:04:42.160955Z'
  support: supports
  summary: Exact J1309 identity, pH 7.5, main 5466 nominal 1005 mL, vitamin 5467 per
    1000 mL and trace 3847 per 1000 mL were inspected in full. Main volume doses and
    strength annotations are separate fields; nested g_l values describe stock composition.
  snapshot_sha256: a8d204bd1c4270033b25a5886363e1f50cc0c6b1e696f7f40ae6b3740ff21e3c
- evidence_id: provider-pdf
  kind: database
  reference: https://mediadive.dsmz.de/pdf/J1309
  locator: PDF pages1–2
  accessed_at: '2026-10-21T08:05:44.754321Z'
  support: supports
  summary: Read both pages. The provider rendering separates the 30% saltwater heading
    and vitamin/trace recipes, and marks post-cooling additions and starred filter-sterilized
    stocks. It credits JCM2022 but is served/generated by MediaDive.
  snapshot_sha256: 8a02dc002fe8c5c24418dfc8fe760ce3ee258904c182930010a0dc715b5ed0bc
- evidence_id: primary-unavailable
  kind: search
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1309
  locator: Whole returned body
  accessed_at: '2026-10-21T08:04:45.083635Z'
  support: unknown
  summary: Exact live JCM1309 query returned no formulation. HTTP 200 is transport
    success, not primary-source access.
  quote: Nothing found.
  snapshot_sha256: 0014e1e3dfaed9f1e5976d9d837ee56d32bec66e1dbd901ceac85f3f3cbcac26
  search_scope: Bounded exact public HTTP request to https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1309
    at the recorded access time. The returned body/status is preserved; no neighboring
    accession, inferred formulation, or exhaustive web absence claim is used. This
    is an external endpoint check; ignored local files are not part of this access
    test.
- evidence_id: primary-pdf-unavailable
  kind: search
  reference: https://jcm.brc.riken.jp/en/wp-content/uploads/medium/JCM1309.pdf
  locator: HTTP response
  accessed_at: '2026-10-21T08:05:44.752900Z'
  support: unknown
  summary: Bounded candidate official static PDF returned HTTP 404. The error response
    is retained and supplies no formulation.
  snapshot_sha256: 3b823caf114dbf76ca3f609fc0be6ac2890f5cf3cc549be12bca64b06e6c78ef
  search_scope: Bounded exact public HTTP request to https://jcm.brc.riken.jp/en/wp-content/uploads/medium/JCM1309.pdf
    at the recorded access time. The returned body/status is preserved; no neighboring
    accession, inferred formulation, or exhaustive web absence claim is used. This
    is an external endpoint check; ignored local files are not part of this access
    test.
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:00:46.687620Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi132103
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132103
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:43.190704Z'
  support: supports
  summary: CHEBI:132103 resolves to sodium perchlorate and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 7b8ebe949b186fbff70466c1b70835f03f99c7f1ae6b2aa938bd7f554376ba1d
- evidence_id: chebi132112
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132112
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:43.693201Z'
  support: supports
  summary: CHEBI:132112 resolves to sodium thiosulfate and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: d7212b97722dceb8181a43aa6840a8c7be39f43e1ab9bf8979a93c14b8c2495e
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to riboflavin and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:12.693131Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12 and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:00:48.036367Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to 4-aminobenzoic acid and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:00:48.109537Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 resolves to Calcium pantothenate and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:00:48.145370Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:00.737662Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:02.761234Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi3312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:24.822837Z'
  support: supports
  summary: CHEBI:3312 resolves to calcium dichloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 34ed49d95375c80dcb07576c67d04fa77337bfecf406accb283e8c32253b754b
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to thiamine hydrochloride and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi50144
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:22:07.440767Z'
  support: supports
  summary: CHEBI:50144 resolves to sodium pyruvate and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 resolves to cobalt chloride hexahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:08.404288Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:00:48.784931Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:44.822632Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:54:59.898295Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:45.074853Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate and is not
    obsolete. This verifies the asserted generic chemical identity; no source grade,
    salt, hydrate or stereochemistry beyond the record is inferred.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T08:23:25Z'
  support: supports
  summary: '{"CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier":
    "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836":
    [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type":
    "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate",
    "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:132103": [{"label": "Sodium perchlorate", "match_type": "preferred_term",
    "identifier": "CHEBI:132103", "preferred_term": "Sodium perchlorate", "ontology_id":
    "CHEBI:132103", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:132112":
    [{"label": "Na2S2O3", "match_type": "preferred_term", "identifier": "CHEBI:132112",
    "preferred_term": "Na2S2O3", "ontology_id": "CHEBI:132112", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345":
    [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier":
    "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:3312": [{"label": "CaCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id":
    "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105":
    [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type":
    "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label":
    "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345",
    "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976":
    [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976",
    "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O",
    "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier":
    "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride
    hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label":
    "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit
  accessed_at: '2026-10-21T08:23:25Z'
  support: context_only
  summary: Current importer restricts direct ingredients to primary solution, preserves
    explicit solution_id and percentage-bearing mL stocks, and normalizesml to ML_PER_L.
    Its stock detector checks percentage annotations but does not generally recognize
    plain 1 M/0.5 M or g/L stock annotations. The API saltwater subsection is itself
    embedded inside primary recipe rows, so merely rerunning current code is not proven
    to repair all stages. Source read only; not executed.
- evidence_id: nickel-form
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: _embedded.terms[0].label,annotation.generalized_empirical_formula,annotation.mass
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: OLS exact CHEBI34887 is nickel dichloride, empirical formula Cl2Ni and
    mass 129.599. It does not encode the six waters explicitly required by source
    and preferred_term NiCl2×6H2O. Canonical ID/label agreement cannot validate that
    hydrate identity.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: pantothenate-form
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: _embedded.terms[0].synonyms, annotation.inchi_string, annotation.smiles_string
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: The full OLS entry has a generic canonical label but lists D-calcium pantothenate
    and Calcium pantothenate, d- synonyms. Its InChI specifies stereochemistry with
    suffix /t2*7-;/m00./s1 and its SMILES gives two [C@@H] moieties. This is a stereospecific
    structure, while the source explicitly specifies DL-Calcium pantothenate. The
    exact DL-compatible grounding remains unresolved.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml
  locator: Every timestamp in target and sole normalized owner
  accessed_at: '2026-10-21T08:23:25Z'
  support: supports
  summary: '[{"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[0].timestamp", "value": "2026-01-26T17:53:19.390901Z",
    "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[1].timestamp", "value": "2026-03-13T06:19:13.607219Z",
    "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[2].timestamp", "value": "2026-03-17T06:30:15.000000Z",
    "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[3].timestamp", "value": "2026-03-17T19:45:26.745213+00:00",
    "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[4].timestamp", "value": "2026-06-05T07:40:15.797629+00:00",
    "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[5].timestamp", "value": "2026-06-10T07:46:42.545165+00:00",
    "timezone_aware": true}, {"path": "data/merge_yaml/merged/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[6].timestamp", "value": "2026-08-06T03:04:34.086339+00:00",
    "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[0].timestamp", "value": "2026-01-26T17:53:19.390901Z",
    "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[1].timestamp", "value": "2026-03-13T06:19:13.607219Z",
    "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[2].timestamp", "value": "2026-03-17T06:30:15.000000Z",
    "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[3].timestamp", "value": "2026-03-17T19:45:26.745213+00:00",
    "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[4].timestamp", "value": "2026-06-05T07:40:15.797629+00:00",
    "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml",
    "field": "curation_history[5].timestamp", "value": "2026-06-10T07:46:42.545165+00:00",
    "timezone_aware": true}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '24 primary CHEBI identities resolve with matching labels; 24 of 24 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - record
  - mim
  - chebi131527
  - chebi132103
  - chebi132112
  - chebi15940
  - chebi17015
  - chebi176843
  - chebi26710
  - chebi30753
  - chebi31206
  - chebi31345
  - chebi31795
  - chebi32588
  - chebi33118
  - chebi3312
  - chebi34887
  - chebi49105
  - chebi49976
  - chebi50144
  - chebi53503
  - chebi75213
  - chebi75836
  - chebi86318
  - chebi86345
  - chebi86368
  details: 27 direct ingredient instances; CHEBI-primary instance linkage 24/27 (88.89%),
    verified secondary coverage 24/27 (88.89%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Exact source accession and generated ownership
  outcome: supported
  summary: Stable CM002472, merge-event source basename, maintained owner and exact
    MediaDive J1309 agree on identity. Provider identifies pH 7.5 and a complex liquid
    medium; exact primary formulation access remains unavailable.
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - record
  - owner-0
  - provider
  - primary-unavailable
- assessment_id: all-amounts
  area: quantity
  topic: Every direct ingredient, nested stock and dose
  outcome: concern
  summary: 'All 27 direct claims are traced: two retain provider-normalized direct
    masses; eight misuse volume-dose numerals as g/L; four saltwater rows and thirteen
    vitamin/trace rows lose their stock stages. Source vitamin 3 mL and trace 5 mL
    doses are absent as structured solution additions. The main volume additions total
    1000 mL, while the provider declares 1005 mL; all numerical final-concentration
    examples remain conditional and the discrepancy is unresolved.'
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - record
  - owner-0
  - provider
  - provider-pdf
  details: '[{"field": "ingredients[0].concentration", "material": "Salt water", "local":
    {"value": "830", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator":
    "$.data.solutions[0].recipe[0]", "source_row": {"recipe_order": 1, "compound":
    "Salt water", "compound_id": 1508, "attribute": "see below, 30%", "amount": 830,
    "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve
    source mL addition plus stock strength, not the same numeral in g/L", "calculation":
    null}, {"field": "ingredients[1].concentration", "material": "Peptone", "local":
    {"value": "0.0248756", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator":
    "$.data.solutions[0].recipe[1]", "source_row": {"recipe_order": 2, "compound":
    "Peptone", "compound_id": 1, "attribute": "Oxoid", "amount": 0.025, "unit": "g",
    "g_l": 0.0248756, "optional": 0}, "decision": "verified provider g/L normalization;
    original mass is0.025g peptone or5mg yeast per declared1005mL, not independently
    primary-verified", "calculation": null}, {"field": "ingredients[2].concentration",
    "material": "Yeast extract", "local": {"value": "0.00497512", "unit": "G_PER_L"},
    "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[2]",
    "source_row": {"recipe_order": 3, "compound": "Yeast extract", "compound_id":
    16, "amount": 5, "unit": "mg", "g_l": 0.00497512, "optional": 0}, "decision":
    "verified provider g/L normalization; original mass is0.025g peptone or5mg yeast
    per declared1005mL, not independently primary-verified", "calculation": null},
    {"field": "ingredients[3].concentration", "material": "NH4Cl", "local": {"value":
    "5", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator": "$.data.solutions[0].recipe[3]",
    "source_row": {"recipe_order": 4, "compound": "NH4Cl", "compound_id": 42, "attribute":
    "1M", "amount": 5, "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage
    error: preserve source mL addition plus stock strength, not the same numeral in
    g/L", "calculation": null}, {"field": "ingredients[4].concentration", "material":
    "K2HPO4", "local": {"value": "2", "unit": "G_PER_L"}, "source_solution_id": 5466,
    "source_locator": "$.data.solutions[0].recipe[4]", "source_row": {"recipe_order":
    5, "compound": "K2HPO4", "compound_id": 10, "attribute": "0.5 M", "amount": 2,
    "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve
    source mL addition plus stock strength, not the same numeral in g/L", "calculation":
    null}, {"field": "ingredients[5].concentration", "material": "FeSO4 x 7 H2O",
    "local": {"value": "5", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator":
    "$.data.solutions[0].recipe[5]", "source_row": {"recipe_order": 6, "compound":
    "FeSO4 x 7 H2O", "compound_id": 12, "attribute": "*, 0.15%", "amount": 5, "unit":
    "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve source
    mL addition plus stock strength, not the same numeral in g/L", "calculation":
    null}, {"field": "ingredients[6].concentration", "material": "Sodium pyruvate",
    "local": {"value": "50", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator":
    "$.data.solutions[0].recipe[8]", "source_row": {"recipe_order": 9, "compound":
    "Sodium pyruvate", "compound_id": 438, "attribute": "1.0 M", "amount": 50, "unit":
    "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve source
    mL addition plus stock strength, not the same numeral in g/L", "calculation":
    null}, {"field": "ingredients[7].concentration", "material": "Sodium perchlorate",
    "local": {"value": "50", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator":
    "$.data.solutions[0].recipe[9]", "source_row": {"recipe_order": 10, "compound":
    "Sodium perchlorate", "compound_id": 2064, "attribute": "1.0 M", "amount": 50,
    "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve
    source mL addition plus stock strength, not the same numeral in g/L", "calculation":
    null}, {"field": "ingredients[8].concentration", "material": "Sodium Thiosulfate",
    "local": {"value": "50", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator":
    "$.data.solutions[0].recipe[10]", "source_row": {"recipe_order": 11, "compound":
    "Sodium Thiosulfate", "compound_id": 1126, "attribute": "1.0 M", "amount": 50,
    "unit": "ml", "optional": 0}, "decision": "correct dimensional/stage error: preserve
    source mL addition plus stock strength, not the same numeral in g/L", "calculation":
    null}, {"field": "ingredients[9].concentration", "material": "NaCl", "local":
    {"value": "238.806", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator":
    "$.data.solutions[0].recipe[11]", "source_row": {"recipe_order": 12, "compound":
    "NaCl", "compound_id": 43, "amount": 240, "unit": "g", "g_l": 238.806, "mmol_l":
    4086.34, "optional": 0}, "decision": "correct stage: constituent of separate30%
    saltwater stock dosed830mL, not an additional neat final-medium mass", "calculation":
    "If stock is made to1L and receiving volume is1.005L: 240g/L stock ×0.830L/1.005L
    = 198.2089552238805970149253731g/L; conditional provider interpretation only."},
    {"field": "ingredients[10].concentration", "material": "MgCl2 x 6 H2O", "local":
    {"value": "24.7761", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator":
    "$.data.solutions[0].recipe[12]", "source_row": {"recipe_order": 13, "compound":
    "MgCl2 x 6 H2O", "compound_id": 79, "amount": 24.9, "unit": "g", "g_l": 24.7761,
    "mmol_l": 121.868, "optional": 0}, "decision": "correct stage: constituent of
    separate30% saltwater stock dosed830mL, not an additional neat final-medium mass",
    "calculation": "If stock is made to1L and receiving volume is1.005L: 24.9g/L stock
    ×0.830L/1.005L = 20.56417910447761194029850746g/L; conditional provider interpretation
    only."}, {"field": "ingredients[11].concentration", "material": "MgSO4 x 7 H2O",
    "local": {"value": "28.8557", "unit": "G_PER_L"}, "source_solution_id": 5466,
    "source_locator": "$.data.solutions[0].recipe[13]", "source_row": {"recipe_order":
    14, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 29, "unit": "g",
    "g_l": 28.8557, "mmol_l": 117.073, "optional": 0}, "decision": "correct stage:
    constituent of separate30% saltwater stock dosed830mL, not an additional neat
    final-medium mass", "calculation": "If stock is made to1L and receiving volume
    is1.005L: 29g/L stock ×0.830L/1.005L = 23.95024875621890547263681592g/L; conditional
    provider interpretation only."}, {"field": "ingredients[12].concentration", "material":
    "KCl", "local": {"value": "6.96517", "unit": "G_PER_L"}, "source_solution_id":
    5466, "source_locator": "$.data.solutions[0].recipe[14]", "source_row": {"recipe_order":
    15, "compound": "KCl", "compound_id": 61, "amount": 7, "unit": "g", "g_l": 6.96517,
    "mmol_l": 93.4296, "optional": 0}, "decision": "correct stage: constituent of
    separate30% saltwater stock dosed830mL, not an additional neat final-medium mass",
    "calculation": "If stock is made to1L and receiving volume is1.005L: 7g/L stock
    ×0.830L/1.005L = 5.781094527363184079601990050g/L; conditional provider interpretation
    only."}, {"field": "ingredients[13].concentration", "material": "CaCl2", "local":
    {"value": "5", "unit": "G_PER_L"}, "source_solution_id": 5466, "source_locator":
    "$.data.solutions[0].recipe[15]", "source_row": {"recipe_order": 16, "compound":
    "CaCl2", "compound_id": 81, "attribute": "1M", "amount": 5, "unit": "ml", "optional":
    0}, "decision": "correct dimensional/stage error: preserve source mL addition
    plus stock strength, not the same numeral in g/L", "calculation": null}, {"field":
    "ingredients[14].concentration", "material": "Thiamine HCl", "local": {"value":
    "0.033", "unit": "G_PER_L"}, "source_solution_id": 5467, "source_locator": "$.data.solutions[1].recipe[0]",
    "source_row": {"recipe_order": 1, "compound": "Thiamine HCl", "compound_id": 1207,
    "amount": 33, "unit": "mg", "g_l": 0.033, "optional": 0}, "decision": "correct
    stock/final-medium confusion: local number equals source stock g/L before its
    separate dose", "calculation": "0.033g/L stock ×0.003L/1.005L = 0.00009850746268656716417910447761g/L
    on provider nominal1005mL basis."}, {"field": "ingredients[15].concentration",
    "material": "Riboflavin", "local": {"value": "0.01", "unit": "G_PER_L"}, "source_solution_id":
    5467, "source_locator": "$.data.solutions[1].recipe[1]", "source_row": {"recipe_order":
    2, "compound": "Riboflavin", "compound_id": 136, "amount": 10, "unit": "mg", "g_l":
    0.01, "mmol_l": 0.0265675, "optional": 0}, "decision": "correct stock/final-medium
    confusion: local number equals source stock g/L before its separate dose", "calculation":
    "0.01g/L stock ×0.003L/1.005L = 0.00002985074626865671641791044776g/L on provider
    nominal1005mL basis."}, {"field": "ingredients[16].concentration", "material":
    "Nicotinic acid", "local": {"value": "0.033", "unit": "G_PER_L"}, "source_solution_id":
    5467, "source_locator": "$.data.solutions[1].recipe[2]", "source_row": {"recipe_order":
    3, "compound": "Nicotinic acid", "compound_id": 139, "amount": 33, "unit": "mg",
    "g_l": 0.033, "mmol_l": 0.268053, "optional": 0}, "decision": "correct stock/final-medium
    confusion: local number equals source stock g/L before its separate dose", "calculation":
    "0.033g/L stock ×0.003L/1.005L = 0.00009850746268656716417910447761g/L on provider
    nominal1005mL basis."}, {"field": "ingredients[17].concentration", "material":
    "DL-Calcium pantothenate", "local": {"value": "0.017", "unit": "G_PER_L"}, "source_solution_id":
    5467, "source_locator": "$.data.solutions[1].recipe[3]", "source_row": {"recipe_order":
    4, "compound": "DL-Calcium pantothenate", "compound_id": 1720, "amount": 17, "unit":
    "mg", "g_l": 0.017, "mmol_l": 0.0356768, "optional": 0}, "decision": "correct
    stock/final-medium confusion: local number equals source stock g/L before its
    separate dose", "calculation": "0.017g/L stock ×0.003L/1.005L = 0.00005074626865671641791044776119g/L
    on provider nominal1005mL basis."}, {"field": "ingredients[18].concentration",
    "material": "Vitamin B12", "local": {"value": "0.017", "unit": "G_PER_L"}, "source_solution_id":
    5467, "source_locator": "$.data.solutions[1].recipe[4]", "source_row": {"recipe_order":
    5, "compound": "Vitamin B12", "compound_id": 18, "amount": 17, "unit": "mg", "g_l":
    0.017, "mmol_l": 0.0125424, "optional": 0}, "decision": "correct stock/final-medium
    confusion: local number equals source stock g/L before its separate dose", "calculation":
    "0.017g/L stock ×0.003L/1.005L = 0.00005074626865671641791044776119g/L on provider
    nominal1005mL basis."}, {"field": "ingredients[19].concentration", "material":
    "p-Aminobenzoic acid", "local": {"value": "0.013", "unit": "G_PER_L"}, "source_solution_id":
    5467, "source_locator": "$.data.solutions[1].recipe[5]", "source_row": {"recipe_order":
    6, "compound": "p-Aminobenzoic acid", "compound_id": 47, "amount": 13, "unit":
    "mg", "g_l": 0.013, "mmol_l": 0.0947936, "optional": 0}, "decision": "correct
    stock/final-medium confusion: local number equals source stock g/L before its
    separate dose", "calculation": "0.013g/L stock ×0.003L/1.005L = 0.00003880597014925373134328358209g/L
    on provider nominal1005mL basis."}, {"field": "ingredients[20].concentration",
    "material": "ZnCl2", "local": {"value": "0.07", "unit": "G_PER_L"}, "source_solution_id":
    3847, "source_locator": "$.data.solutions[2].recipe[0]", "source_row": {"recipe_order":
    1, "compound": "ZnCl2", "compound_id": 64, "amount": 70, "unit": "mg", "g_l":
    0.07, "mmol_l": 0.513573, "optional": 0}, "decision": "correct stock/final-medium
    confusion: local number equals source stock g/L before its separate dose", "calculation":
    "0.07g/L stock ×0.005L/1.005L = 0.0003482587064676616915422885572g/L on provider
    nominal1005mL basis."}, {"field": "ingredients[21].concentration", "material":
    "MnCl2 x 4 H2O", "local": {"value": "0.1", "unit": "G_PER_L"}, "source_solution_id":
    3847, "source_locator": "$.data.solutions[2].recipe[1]", "source_row": {"recipe_order":
    2, "compound": "MnCl2 x 4 H2O", "compound_id": 36, "amount": 100, "unit": "mg",
    "g_l": 0.1, "mmol_l": 0.505293, "optional": 0}, "decision": "correct stock/final-medium
    confusion: local number equals source stock g/L before its separate dose", "calculation":
    "0.1g/L stock ×0.005L/1.005L = 0.0004975124378109452736318407960g/L on provider
    nominal1005mL basis."}, {"field": "ingredients[22].concentration", "material":
    "H3BO3", "local": {"value": "0.006", "unit": "G_PER_L"}, "source_solution_id":
    3847, "source_locator": "$.data.solutions[2].recipe[2]", "source_row": {"recipe_order":
    3, "compound": "H3BO3", "compound_id": 37, "amount": 6, "unit": "mg", "g_l": 0.006,
    "mmol_l": 0.0970246, "optional": 0}, "decision": "correct stock/final-medium confusion:
    local number equals source stock g/L before its separate dose", "calculation":
    "0.006g/L stock ×0.005L/1.005L = 0.00002985074626865671641791044776g/L on provider
    nominal1005mL basis."}, {"field": "ingredients[23].concentration", "material":
    "CoCl2 x 6 H2O", "local": {"value": "0.19", "unit": "G_PER_L"}, "source_solution_id":
    3847, "source_locator": "$.data.solutions[2].recipe[3]", "source_row": {"recipe_order":
    4, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 190, "unit": "mg",
    "g_l": 0.19, "mmol_l": 1.46335, "optional": 0}, "decision": "correct stock/final-medium
    confusion: local number equals source stock g/L before its separate dose", "calculation":
    "0.19g/L stock ×0.005L/1.005L = 0.0009452736318407960199004975124g/L on provider
    nominal1005mL basis."}, {"field": "ingredients[24].concentration", "material":
    "CuCl2 x 2 H2O", "local": {"value": "0.002", "unit": "G_PER_L"}, "source_solution_id":
    3847, "source_locator": "$.data.solutions[2].recipe[4]", "source_row": {"recipe_order":
    5, "compound": "CuCl2 x 2 H2O", "compound_id": 39, "amount": 2, "unit": "mg",
    "g_l": 0.002, "mmol_l": 0.0117314, "optional": 0}, "decision": "correct stock/final-medium
    confusion: local number equals source stock g/L before its separate dose", "calculation":
    "0.002g/L stock ×0.005L/1.005L = 0.000009950248756218905472636815920g/L on provider
    nominal1005mL basis."}, {"field": "ingredients[25].concentration", "material":
    "NiCl2 x 6 H2O", "local": {"value": "0.024", "unit": "G_PER_L"}, "source_solution_id":
    3847, "source_locator": "$.data.solutions[2].recipe[5]", "source_row": {"recipe_order":
    6, "compound": "NiCl2 x 6 H2O", "compound_id": 40, "amount": 24, "unit": "mg",
    "g_l": 0.024, "mmol_l": 0.185187, "optional": 0}, "decision": "correct stock/final-medium
    confusion: local number equals source stock g/L before its separate dose", "calculation":
    "0.024g/L stock ×0.005L/1.005L = 0.0001194029850746268656716417910g/L on provider
    nominal1005mL basis."}, {"field": "ingredients[26].concentration", "material":
    "Na2MoO4 x 2 H2O", "local": {"value": "0.036", "unit": "G_PER_L"}, "source_solution_id":
    3847, "source_locator": "$.data.solutions[2].recipe[6]", "source_row": {"recipe_order":
    7, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 36, "unit": "mg",
    "g_l": 0.036, "mmol_l": 0.148791, "optional": 0}, "decision": "correct stock/final-medium
    confusion: local number equals source stock g/L before its separate dose", "calculation":
    "0.036g/L stock ×0.005L/1.005L = 0.0001791044776119402985074626866g/L on provider
    nominal1005mL basis."}]'
- assessment_id: preparation
  area: completeness
  topic: All four steps and stage-specific conditions
  outcome: concern
  summary: Step 1 retains a dangling following-solutions reference but loses the ingredients
    to which it applies and the starred filter-sterilized mapping; step 2 correctly
    retains 10 mL Balch-tube distribution, butyl stoppers and N2; step 3 is only a
    saltwater heading; step 4 carries the stock 1 L make-up/pH instruction without
    explicit stock scope. Global pH 7.5 agrees with provider medium metadata, but
    stock/receiving-medium contexts must remain explicit. No temperature/time beyond
    inspected source is invented.
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - record
  - provider
  - provider-pdf
- assessment_id: ownership
  area: ownership
  topic: Current writer versus unchanged normalized content
  outcome: concern
  summary: Generated and maintained ingredient/preparation bytes agree; these defects
    are not exclusively stale generated output. Curate the normalized owner and review
    the current importer’s residual molar-stock/subsection handling before regeneration.
    The existing history records imports and canonicalization, not independent formulation
    verification.
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - record
  - owner-0
  - importer
- assessment_id: scope
  area: scope
  topic: Growth, category, variants and annotations
  outcome: unknown
  summary: No target organisms, strain accessions, DOI/PMID, parent/child variant
    or genome claims are present. Complex/undefined liquid status fits the listed
    mixtures and absence of agar, but no exact organism-category or high_metal threshold
    is established. The latter should be reassessed once trace doses are corrected.
    Source absence is not negative growth evidence.
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - record
  - owner-0
  - provider
- assessment_id: hydrate
  area: grounding
  topic: Source-explicit nickel hydrate
  outcome: concern
  summary: ingredients[25] names nickel chloride hexahydrate but both primary/secondary
    terms encode Cl2Ni. Other asserted label correspondences are checked separately;
    no unverified replacement identifier or molar-mass conversion is proposed.
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - record
  - provider
  - nickel-form
  - mim
- assessment_id: pantothenate
  area: grounding
  topic: Source DL reagent versus stereospecific ontology structure
  outcome: concern
  summary: Source vitamin solution 5467 recipe[3] (fourth displayed row) specifies
    DL-Calcium pantothenate 17 mg per 1 L; ingredients[17] retains that preferred
    term but both ontology links assert CHEBI31345, whose captured structural annotations
    and D synonyms do not establish the DL reagent identity. Preserve the 17 mg stock
    amount and DL form, and leave a replacement identifier unresolved.
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - record
  - provider
  - pantothenate-form
  - mim
- assessment_id: evidence-placement
  area: evidence
  topic: Source provenance and amount evidence
  outcome: concern
  summary: A JCM URL exists in notes and provider accession in media_term; neither
    local layer has structured references or claim-level ingredient/stock evidence.
    Preserve exact provider version, primary-access limit, original units and dilution
    basis while repairing the scientific claims. All target/owner history timestamps
    were inspected with timezone scope; no events were changed.
  target_ids:
  - CultureMech:002472
  evidence_ids:
  - record
  - owner-0
  - provider
  - primary-unavailable
  - history
findings:
- finding_id: f1
  issue_key: cm002472-stock-volume-numerals-as-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Eight stock-volume additions are encoded as g/L
  description: Saltwater 830 mL, NH4Cl 5 mL(1 M), K2HPO4 2 mL(0.5 M), FeSO4·7H2O5
    mL(0.15%), three 50 mL 1 M organic/electron-acceptor stocks, and saltwater CaCl2
    5 mL(1 M) have been copied as the same numeralsg/L. These are dimensional and
    preparation-stage errors in both local layers.
  target_ids:
  - CultureMech:002472
  field_paths:
  - ingredients[0].concentration
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - ingredients[7].concentration
  - ingredients[8].concentration
  - ingredients[13].concentration
  evidence_ids:
  - record
  - owner-0
  - provider
  - provider-pdf
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
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
  issue_key: cm002472-nested-stock-flattening
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Saltwater, vitamin and trace stocks are treated as final-medium ingredients
  description: Four saltwater and thirteen vitamin/trace concentrations lose their
    stock context, while structured 830 mL saltwater,3 mL vitamin and 5 mL trace doses
    are absent. This risks double-counting saltwater and overconcentrating nested
    supplements. The provider main recipe itself embeds the saltwater section, so
    source headings must be used rather than treating every primary API row as a neat
    addition.
  target_ids:
  - CultureMech:002472
  field_paths:
  - ingredients[9].concentration
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[14].concentration
  - ingredients[15].concentration
  - ingredients[16].concentration
  - ingredients[17].concentration
  - ingredients[18].concentration
  - ingredients[19].concentration
  - ingredients[20].concentration
  - ingredients[21].concentration
  - ingredients[22].concentration
  - ingredients[23].concentration
  - ingredients[24].concentration
  - ingredients[25].concentration
  - ingredients[26].concentration
  - solutions
  - high_metal
  evidence_ids:
  - record
  - owner-0
  - provider
  - provider-pdf
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
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
  issue_key: cm002472-preparation-stage-boundaries
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Preparation omits the stock-specific addition and sterilization context
  description: The four steps preserve fragments but lose which additions follow cooling,
    which starred stocks are filter sterilized, and that 30% saltwater is separately
    made to 1 L. A saltwater heading is represented as a standalone MIX step and following-solutions
    text is disconnected from its doses.
  target_ids:
  - CultureMech:002472
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - provider
  - provider-pdf
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: cm002472-nickel-hydrate-identity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel chloride hexahydrate is grounded to Cl2Ni
  description: Source and preferred_term specify NiCl2×6H2O, while CHEBI34887 has
    formula Cl2Ni. Both primary and secondary links repeat the anhydrous identity;
    a valid canonical label does not resolve this chemical-form mismatch.
  target_ids:
  - CultureMech:002472
  field_paths:
  - ingredients[25].term
  - ingredients[25].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - provider
  - nickel-form
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f5
  issue_key: cm002472-dl-pantothenate-stereospecific-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Source DL-calcium pantothenate is assigned a stereospecific structure
  description: ingredients[17] and the source specify DL-Calcium pantothenate,17 mg
    per vitamin-stock litre. CHEBI31345 has a generic label but the inspected entry
    specifies stereochemistry and D-calcium pantothenate synonyms. Neither that structure
    nor label correspondence establishes identity with the source DL reagent. Both
    primary and secondary links therefore overstate the supported chemical form.
  target_ids:
  - CultureMech:002472
  field_paths:
  - ingredients[17].term
  - ingredients[17].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - provider
  - pantothenate-form
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Restore source-defined stock strengths, mL doses and enclosing batch/stage
    with bounded evidence. Do not invent percentage basis, density or hydrate molecular
    weight; retain unresolved current-primary reconciliation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002472
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
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
  description: Represent the source stock hierarchy and dose once; preserve constituent
    stock recipes and separate any calculated final contributions. Reassesshigh_metal
    after amounts are corrected.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002472
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
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
  description: Restore base, saltwater, vitamin and trace preparation boundaries and
    attach cooling/sterilization instructions to exact source additions while retaining
    N2 and tube conditions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002472
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
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
  description: Verify an exact hydrate grounding against the packaged resolver and
    authoritative ontology; preserve source hydrate and leave unresolved rather than
    force an unverified identifier.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002472
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
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
- action_id: a5
  description: Verify an exact source-compatible DL grounding or retain the unresolved
    form explicitly; preserve the 17 mg stock amount and do not replace the source
    reagent with a D-only preparation or invent a replacement CHEBI identifier.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:002472
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/3_8m_characterization_medium_no_1.yaml
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
- The current JCM1309 endpoint returned HTTP 200 with Nothing found; a bounded official
  static-PDF candidate returned 404. The exact MediaDive J1309 API and provider-generated
  PDF are available, but are secondary source versions rather than recovered current
  primary text. Final source reconciliation remains open.
- The provider declares a 1005 mL final volume, but the explicit main additions total
  1000 mL (830+5+2+5+5+3+50+50+50); the separate saltwater recipe also includes 5
  mL calcium stock. The 1000-versus-1005 mL discrepancy remains unresolved, and no
  causal attribution is made. Numerical dilution examples are conditional on the provider-reported
  basis, not a validated final volume. Percentage annotations 0.15% and 30% lack an
  explicit w/v or v/v basis; no density or percentage-basis assumption is used.
- No new organism, strain, taxon, assembly or literature-growth assertion is inferred.
  The target asserts no organism identifiers. Bacterial filing and high_metal are
  not independently established by a cultivation experiment; the high_metal tag should
  be reassessed after the stock-stage corrections.
- Public ontology captures identify the asserted terms; no replacement nickel-hydrate
  or DL-calcium-pantothenate identifier is proposed without exact verification. The
  DL reagent remains 17 mg per source vitamin-stock litre; no stereoisomer substitution
  or altered stock mass is proposed. Undefined peptone and yeast extract remain mixtures.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-010
- generated-medium
```
