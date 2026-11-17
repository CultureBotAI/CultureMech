# Source and formulation review: acidifferobacter_murciensis_medium (CultureMech:007535)

- Review: 20261021T105912Z-culturemech-007535-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T10:48:44Z
- Finished UTC: 2026-10-21T10:59:12Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact TOGO M1020 formulation identifies JCM970, whose current page contains no recipe. The generated target and sole owner misstate mg/ug and liquid batch amounts as g/L, flatten an iron stock with unresolved delivered concentration, and lose preparation context. Cobalt hydrate grounding and composition/high-metal classifications need source-scoped reassessment.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence. Direct original-collection confirmation is unavailable; scientific assessments are bounded to the complete accessible TOGO representation and captured ontology metadata.

Selection: Task review 164; batch 017 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding sixteen task batches contain 160 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 162 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007535 | data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml | generated | acidifferobacter_murciensis_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007535 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007535 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/164/strict.tsv |
| validate-terms | passed | True | CultureMech:007535 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007535 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007535 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact original JCM970 formulation | unavailable | True | CultureMech:007535 | The exact collection URL returned HTTP200 with Nothing found and no recipe. Provider-supported assessments are retained, but direct original-collection verification is unavailable. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007535.

The four documented recipes completed; interpret the scope of each separately.

### Exact source accession and sole maintained owner

identity: supported. Targets: CultureMech:007535.

The root stable ID, explicit single merge contributor and provider M1020/JCM970 mapping agree. The source and local title both spell Acidifferobacter Murciensis Medium; this is accession identity, not confirmation of organism nomenclature or growth. No similarly titled recipe is substituted for the inaccessible original.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:007535.

13 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 13/14 primary and 6/14 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 14: primary 92.86%; secondary 42.86%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Every source amount, stock strength, pH and sterilization scope

quantity: concern. Targets: CultureMech:007535.

The eighteen-row inventory covers all sixteen component rows and both preparation entries. Ten receiving salts retain mg/ug numerals as g/L; water, stock dose and concentrated-acid volumes also have wrong dimensions or scope. The iron-stock amount must remain separate until actual stock/working-volume bases are established. Neither layer has attached amount evidence; no inventory decision is verified.

[{"field_path": "ingredients[0].concentration (receiving-batch water)", "decision": "correct", "current": {"value": "1000.0", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[0]", "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The source specifies 900 ml receiving-batch water. Local 1000 G_PER_L sums this with 100 ml water used to prepare the separate stock, crosses stages and changes volume to mass concentration. Restore both solvent amounts at their own stages; do not infer density, final volume, or that every milliliter of stock water is delivered by the 100 ml stock aliquot.", "source_original_amount": 900, "source_original_unit": "ml"}, {"field_path": "ingredients[1].concentration", "decision": "correct", "current": {"value": "147", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[1]", "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 147,\n          \"unit\": \"mg\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider specifies 147 mg for the receiving batch, equal to 0.147 g of this source material. Local 147 G_PER_L copies the numeral while changing the unit and adding a per-liter basis. Restore the exact batch amount and unit; this conversion is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate molecular-weight conversion is made.", "source_original_amount": 147, "source_original_unit": "mg"}, {"field_path": "ingredients[2].concentration", "decision": "correct", "current": {"value": "27.2", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[2]", "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 27.2,\n          \"unit\": \"mg\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider specifies 27.2 mg for the receiving batch, equal to 0.0272 g of this source material. Local 27.2 G_PER_L copies the numeral while changing the unit and adding a per-liter basis. Restore the exact batch amount and unit; this conversion is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate molecular-weight conversion is made.", "source_original_amount": 27.2, "source_original_unit": "mg"}, {"field_path": "ingredients[3].concentration", "decision": "correct", "current": {"value": "12.1", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[3]", "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 12.1,\n          \"unit\": \"ug\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider specifies 12.1 ug for the receiving batch, equal to 0.0000121 g of this source material. Local 12.1 G_PER_L copies the numeral while changing the unit and adding a per-liter basis. Restore the exact batch amount and unit; this conversion is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate molecular-weight conversion is made.", "source_original_amount": 12.1, "source_original_unit": "ug"}, {"field_path": "ingredients[4].concentration", "decision": "correct", "current": {"value": "25.4", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[4]", "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 25.4,\n          \"unit\": \"mg\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider specifies 25.4 mg for the receiving batch, equal to 0.0254 g of this source material. Local 25.4 G_PER_L copies the numeral while changing the unit and adding a per-liter basis. Restore the exact batch amount and unit; this conversion is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate molecular-weight conversion is made.", "source_original_amount": 25.4, "source_original_unit": "mg"}, {"field_path": "ingredients[5].concentration", "decision": "correct", "current": {"value": "31", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[5]", "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 31,\n          \"unit\": \"ug\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider specifies 31 ug for the receiving batch, equal to 0.000031 g of this source material. Local 31 G_PER_L copies the numeral while changing the unit and adding a per-liter basis. Restore the exact batch amount and unit; this conversion is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate molecular-weight conversion is made.", "source_original_amount": 31, "source_original_unit": "ug"}, {"field_path": "ingredients[6].concentration", "decision": "correct", "current": {"value": "120", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[6]", "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 120,\n          \"unit\": \"ug\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider specifies 120 ug for the receiving batch, equal to 0.000120 g of this source material. Local 120 G_PER_L copies the numeral while changing the unit and adding a per-liter basis. Restore the exact batch amount and unit; this conversion is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate molecular-weight conversion is made.", "source_original_amount": 120, "source_original_unit": "ug"}, {"field_path": "ingredients[7].concentration", "decision": "correct", "current": {"value": "120", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[7]", "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 120,\n          \"unit\": \"ug\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider specifies 120 ug for the receiving batch, equal to 0.000120 g of this source material. Local 120 G_PER_L copies the numeral while changing the unit and adding a per-liter basis. Restore the exact batch amount and unit; this conversion is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate molecular-weight conversion is made.", "source_original_amount": 120, "source_original_unit": "ug"}, {"field_path": "ingredients[8].concentration", "decision": "correct", "current": {"value": "85.2", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[8]", "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 85.2,\n          \"unit\": \"ug\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider specifies 85.2 ug for the receiving batch, equal to 0.0000852 g of this source material. Local 85.2 G_PER_L copies the numeral while changing the unit and adding a per-liter basis. Restore the exact batch amount and unit; this conversion is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate molecular-weight conversion is made.", "source_original_amount": 85.2, "source_original_unit": "ug"}, {"field_path": "ingredients[9].concentration", "decision": "correct", "current": {"value": "132.2", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[9]", "exact_source_quote": "\"component_name\": \"(NH4)2SO4\",\n          \"volume\": 132.2,\n          \"unit\": \"mg\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider specifies 132.2 mg for the receiving batch, equal to 0.1322 g of this source material. Local 132.2 G_PER_L copies the numeral while changing the unit and adding a per-liter basis. Restore the exact batch amount and unit; this conversion is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate molecular-weight conversion is made.", "source_original_amount": 132.2, "source_original_unit": "mg"}, {"field_path": "ingredients[10].concentration", "decision": "correct", "current": {"value": "70", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[10]", "exact_source_quote": "\"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"ug\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider specifies 70 ug for the receiving batch, equal to 0.000070 g of this source material. Local 70 G_PER_L copies the numeral while changing the unit and adding a per-liter basis. Restore the exact batch amount and unit; this conversion is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate molecular-weight conversion is made.", "source_original_amount": 70, "source_original_unit": "ug"}, {"field_path": "solutions[0].concentration and composition", "decision": "correct", "current": {"preferred_term": "Iron(II) sulfate solution", "composition": [], "concentration": {"value": "100", "unit": "G_PER_L"}, "name": "Unknown solution"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[11]", "exact_source_quote": "\"component_name\": \"Iron(II) sulfate solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The receiving batch adds 100 ml of the locally specified iron stock; local 100 G_PER_L is the wrong dimension and its empty composition loses the explicit stock definition. Resolve the same-record section by its exact name, retain its separate preparation, and preserve the dose as volume. The source supplies no measured final stock volume and does not prove that this aliquot transfers all 20 g of stock iron salt.", "source_original_amount": 100, "source_original_unit": "ml"}, {"field_path": "ingredients[11].concentration and preparation_steps (acid stock strength)", "decision": "not_quantified", "current": {"value": "variable", "unit": "VARIABLE"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "not_quantified"}, "source_stage": "receiving batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[0].items[12]", "exact_source_quote": "\"component_name\": \"H2SO4\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"N\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The provider identifies a 10 N acid stock for adjustment to pH 2.0 but supplies no addition amount. VARIABLE correctly avoids a fixed working dose; recover the missing stock normality and purpose with evidence. Neither 10 N nor variable is a final-medium concentration, and the unquantified addition must not be set to zero.", "source_original_stock_strength": 10, "source_original_strength_unit": "N"}, {"field_path": "ingredients[0].concentration (iron-stock water)", "decision": "correct", "current": {"value": "1000.0", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "separate iron-stock batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[1].items[0]", "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The source uses 100 ml water to prepare the iron stock. It is not an additional independent receiving-medium water row and not a declaration of final stock volume: 20 g iron salt and 2 ml concentrated acid are also added. Keep the stock solvent separate from the 900 ml receiving-batch water; do not sum either 100+2 ml or 900+100 ml into an asserted measured final volume.", "source_original_amount": 100, "source_original_unit": "ml"}, {"field_path": "ingredients[12].concentration", "decision": "correct", "current": {"value": "20", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "separate iron-stock batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[1].items[1]", "exact_source_quote": "\"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 20,\n          \"unit\": \"g\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The 20 g iron(II) sulfate heptahydrate belongs to the separately prepared stock batch. Local 20 G_PER_L at root has an unsupported final-medium scope. Source stock water is 100 ml, but the prepared stock volume is unstated; its 100 ml dose therefore does not establish the transferred iron amount. Preserve 20 g in the stock definition without assigning 200 g/L stock or 20 g/L working concentration.", "source_original_amount": 20, "source_original_unit": "g"}, {"field_path": "ingredients[13].concentration", "decision": "correct", "current": {"value": "2", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "correct"}, "source_stage": "separate iron-stock batch", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.components[1].items[2]", "exact_source_quote": "\"component_name\": \"H2SO4 (concentrated)\",\n          \"volume\": 2,\n          \"unit\": \"ml\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The iron stock uses 2 ml concentrated sulfuric acid. Local 2 G_PER_L changes a stock-batch liquid amount into a root mass concentration. No numeric purity, density or molarity is supplied; restore original volume and concentrated qualifier in the stock, without a typical-strength conversion or final-medium acid dose.", "source_original_amount": 2, "source_original_unit": "ml"}, {"field_path": "ph_value and preparation_steps (receiving-batch pH)", "decision": "add", "current": null, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "add"}, "source_stage": "receiving-batch adjustment before autoclaving", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.comments[0].comment", "exact_source_quote": "Adjust pH to 2.0 with 10 N H2SO4 and autoclave.", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The source pH target and titrant context are missing in both layers. Add pH 2.0 and its preparation scope with the exact provider excerpt; it is not an organism-growth optimum or a quantified acid dose."}, {"field_path": "preparation_steps (separate autoclaving; cycle numbers)", "decision": "not_quantified", "current": null, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml": "not_quantified"}, "source_stage": "receiving batch and separately sterilized iron stock", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020", "source_locator": "$.comments[0].comment", "exact_source_quote": "Adjust pH to 2.0 with 10 N H2SO4 and autoclave. After autoclaving, add the following solution (separately autoclaved):", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation": "The operation and order are supplied: adjust/autoclave the receiving batch, then add the separately autoclaved iron solution. Recover that missing procedure, while retaining temperature and duration as not quantified. The unavailable JCM970 page cannot supply a numeric collection default."}]

### Hydrate and reagent-form correspondence

grounding: concern. Targets: CultureMech:007535.

The provider specifies CoCl2・6H2O, while CHEBI:35696 denotes cobalt dichloride with formula 2Cl.Co and no water components. This is a source-form mismatch despite valid canonical metadata. Other explicit salt hydrate formulas agree with their captured terms. Sulfuric-acid ontology identity does not specify the 10 N adjustment stock or the concentrated stock reagent; their strengths/doses remain separately scoped.

### pH, ordered separate sterilization and stock identity

completeness: concern. Targets: CultureMech:007535.

Both layers omit preparation_steps and ph_value despite the complete provider comment. The stock preferred_term names the exact source section, while name=Unknown solution and composition=[] are placeholders. Recover the same-record definition and distinct stock treatment; do not infer autoclave cycle numbers, gas conditions, incubation or organism growth.

### Composition and high-metal flag support

scope: concern. Targets: CultureMech:007535.

The complete accessible formulation contains specified inorganic salts, water and sulfuric-acid reagents; it supplies no compositionally undefined nutrient mixture supporting COMPLEX/UNDEFINED. DEFINED is the composition direction, with exact-quantity/stock-volume gaps still explicit. The iron stock supports substantial iron loading, but not the schema-defined high_metal=true threshold: the full stock batch contains 20 g FeSO4·7H2O, while the fraction delivered by its 100 ml dose and final volume remain unresolved. Do not assert false merely because other units are wrong. Reassess or withdraw the unsupported true assertion using correct stage-aware molar calculations. LIQUID is consistent with the water-based provider inventory.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007535.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Growth, category and literature limits

scope: supported. Targets: CultureMech:007535.

The title, bacterial folder and generic cultivation application are not strain-level growth evidence. No target organism, taxon identifier, incubation optimum or literature-supported biological phenotype is asserted. The review assesses the exact medium representation without adding such claims.

## Findings

### f1: Mass units and stock boundaries are scientifically unsafe

blocker / open / confirmed; issue key: m1020-unit-and-stock-scope.

Both local layers turn ten mg/ug batch amounts into the same numerals in g/L, sum water across receiving and stock stages, store the 100 ml stock dose as 100 g/L, and flatten stock iron/concentrated acid into the receiving-medium list. The source does not establish a final stock volume or the iron mass delivered by that aliquot. Passing structural checks do not make these quantities usable.

### f2: Cobalt chloride hexahydrate is linked to a different supplied form

major / open / confirmed; issue key: m1020-cobalt-hydrate.

The exact provider names the hexahydrate, whereas asserted CHEBI:35696 represents cobalt dichloride without waters. Canonical label resolution and numerical amount recovery cannot validate that hydrate correspondence.

### f3: Source preparation and useful stock identity are missing

major / open / confirmed; issue key: m1020-preparation-source-evidence.

Both layers lack the provider pH and separately ordered autoclaving procedure, any attached amount evidence, and the full iron-stock definition; its name remains Unknown solution despite an exact matching source-section name. The original collection recipe is currently unavailable, so provider support must remain explicitly qualified.

### f4: Composition defaults and the high-metal assertion lack source support

major / open / confirmed; issue key: m1020-composition-metal-classification.

COMPLEX/UNDEFINED are inconsistent with the inspected chemically specified inorganic inventory. high_metal=true is a separate threshold assertion: substantial iron loading alone does not establish total metal at least 1049.84 mM, and current automated mass/stock handling cannot supply independent support. The exact iron delivered from the source stock is unresolved.

## Recommended Actions And Acceptance Checks

### a1

Restore exact native receiving-batch units, solvent context, stock definition and stock dose in the maintained owner using the complete field inventory. Remove unsupported root stock contributions; retain unresolved delivered concentrations rather than guessing volume or density. Attach claim-level source evidence, and inspect current importer unit/basis behavior before any separately authorized reimport. Regenerate only after source-scoped correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve and correct the supplied cobalt-chloride hydrate identity in the maintained owner with authoritative term/form evidence; preserve the original 120 ug batch mass. Do not infer a replacement ID or perform an anhydrous mass conversion from this review alone.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add exact provider citations and literal claim-level excerpts; recover pH 2.0, 10 N titrant with unknown dose, receiving-medium autoclaving and subsequent separately autoclaved stock addition. Use the exact source stock name and preserve all stock source quantities. Seek the original JCM970 recipe without substituting another medium, and leave cycle temperature/time unquantified until sourced.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Reassess composition against the complete source inventory, using DEFINED as the supported direction while explicitly retaining exact-quantity limitations. Recalculate threshold support only with verified units, supplied forms, stock dilution and valid molar arithmetic; withdraw or qualify unsupported high_metal=true rather than automatically replacing it with false. Preserve the source iron-stock facts and append provenance for authorized changes.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch017/164/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/164/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml:1:id: CultureMech:007535<br>./data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml:1:id: CultureMech:007535<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch017/source-preflight-bound/164/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 15 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020; Complete meta, components[0:2] and comments[0] | supports | Exact TOGO M1020 provider record identifies JCM970 and preserves thirteen receiving-batch rows, three iron-stock rows, pH, adjustment-stock normality and separate autoclaving. The source units/stages are explicit; neither measured final volume nor final iron-stock volume is supplied. |
| primary-unavailable | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=970; Entire exact GRMD970 response | context_only | HTTP200 is not successful formulation retrieval: the exact collection page says Nothing found. This capture supplies no recipe, collection sterilization default or source chronology. The accessible TOGO representation remains secondary evidence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| quantity-inventory | /private/tmp/culturemech-review-work-batch017/164/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| classification-schema | src/culturemech/schema/culturemech.yaml; MediaRecipe.high_metal and MediumCompositionTypeEnum | context_only | high_metal refers to total enumerated metal concentration at or above 1049.84 mM. UNDEFINED means a chemically undefined component; DEFINED also requires known exact quantities. These native definitions are applied separately from the current data errors. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read, not executed or historically replayed. TOGO now separates named primary/stock sections and preserves comment prose, but its local stock basis accepts a dose equal to a water row even with another liquid present; that is not measured final stock volume. Its unit map recognizes mg but bare ug and N fall back to G_PER_L; concentration-only H2SO4 can reach final-concentration handling. Current COMPLEX is a default, not source evidence. Metal analysis sums approximate mass/native-unit values as mM, does not account for stock delivery or molar stoichiometry, and its flag writer consumes prior computed membership. Current single-owner merger returns owner content. These observations guide bounded follow-up and do not prove the historical sequence or endorse blind reimport. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read, not executed or historically replayed. TOGO now separates named primary/stock sections and preserves comment prose, but its local stock basis accepts a dose equal to a water row even with another liquid present; that is not measured final stock volume. Its unit map recognizes mg but bare ug and N fall back to G_PER_L; concentration-only H2SO4 can reach final-concentration handling. Current COMPLEX is a default, not source evidence. Metal analysis sums approximate mass/native-unit values as mM, does not account for stock delivery or molar stoichiometry, and its flag writer consumes prior computed membership. Current single-owner merger returns owner content. These observations guide bounded follow-up and do not prove the historical sequence or endorse blind reimport. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read, not executed or historically replayed. TOGO now separates named primary/stock sections and preserves comment prose, but its local stock basis accepts a dose equal to a water row even with another liquid present; that is not measured final stock volume. Its unit map recognizes mg but bare ug and N fall back to G_PER_L; concentration-only H2SO4 can reach final-concentration handling. Current COMPLEX is a default, not source evidence. Metal analysis sums approximate mass/native-unit values as mM, does not account for stock delivery or molar stoichiometry, and its flag writer consumes prior computed membership. Current single-owner merger returns owner content. These observations guide bounded follow-up and do not prove the historical sequence or endorse blind reimport. |
| writer-3 | scripts/analyze_metal_concentrations.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read, not executed or historically replayed. TOGO now separates named primary/stock sections and preserves comment prose, but its local stock basis accepts a dose equal to a water row even with another liquid present; that is not measured final stock volume. Its unit map recognizes mg but bare ug and N fall back to G_PER_L; concentration-only H2SO4 can reach final-concentration handling. Current COMPLEX is a default, not source evidence. Metal analysis sums approximate mass/native-unit values as mM, does not account for stock delivery or molar stoichiometry, and its flag writer consumes prior computed membership. Current single-owner merger returns owner content. These observations guide bounded follow-up and do not prove the historical sequence or endorse blind reimport. |
| writer-4 | scripts/add_metal_ree_labels.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read, not executed or historically replayed. TOGO now separates named primary/stock sections and preserves comment prose, but its local stock basis accepts a dose equal to a water row even with another liquid present; that is not measured final stock volume. Its unit map recognizes mg but bare ug and N fall back to G_PER_L; concentration-only H2SO4 can reach final-concentration handling. Current COMPLEX is a default, not source evidence. Metal analysis sums approximate mass/native-unit values as mM, does not account for stock delivery or molar stoichiometry, and its flag writer consumes prior computed membership. Current single-owner merger returns owner content. These observations guide bounded follow-up and do not prove the historical sequence or endorse blind reimport. |
| history-metadata | data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml", "events": 12, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Partial completion is required because the exact JCM970 collection page provides no recipe. Scientific findings are bounded to the complete accessible TOGO M1020 representation and captured ontology metadata.
- The iron stock has no stated measured final volume, the 100 ml aliquot does not prove complete transfer of its 20 g iron salt, and the receiving medium has no measured final volume. No final iron/acid concentration or high_metal=false value is inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T105912Z-culturemech-007535-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidifferobacter_murciensis_medium (CultureMech:007535)'
started_at: '2026-10-21T10:48:44Z'
finished_at: '2026-10-21T10:59:12Z'
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
summary: The exact TOGO M1020 formulation identifies JCM970, whose current page contains
  no recipe. The generated target and sole owner misstate mg/ug and liquid batch amounts
  as g/L, flatten an iron stock with unresolved delivered concentration, and lose
  preparation context. Cobalt hydrate grounding and composition/high-metal classifications
  need source-scoped reassessment.
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
  - path: data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
    sha256: 13db535f18bd43cb097ab7932f1a4d8f10e8ca7c565cc63e820439a1d2538e28
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
    sha256: 0fc2424806d9b4c59cc5de3f3ef6bb6e53ff7ea4903a9b0d704e6e7753e9089c
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
  - path: scripts/add_metal_ree_labels.py
    sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
    role: context
  - path: scripts/analyze_metal_concentrations.py
    sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
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
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
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
    provenance, and maintained-input correspondence. Direct original-collection confirmation
    is unavailable; scientific assessments are bounded to the complete accessible
    TOGO representation and captured ontology metadata.
  selection: Task review 164; batch 017 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding sixteen task batches
    contain 160 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 162 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007535
targets:
- target_id: CultureMech:007535
  path: data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
  label: acidifferobacter_murciensis_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch017/164/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/164/strict.tsv"
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007535
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
  - CultureMech:007535
- check_id: jcm970-formulation
  name: Exact original JCM970 formulation
  required: true
  status: unavailable
  summary: The exact collection URL returned HTTP200 with Nothing found and no recipe.
    Provider-supported assessments are retained, but direct original-collection verification
    is unavailable.
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - primary-unavailable
  - provider
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:59:10Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:59:10Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:19.179546Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch017/164/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:20.581895Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/164/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:22.339258Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:23.347789Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T10:59:10Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml:1:id:
    CultureMech:007535

    ./data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml:1:id:
    CultureMech:007535

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/source-preflight-bound/164/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T10:59:10Z'
  support: supports
  summary: 15 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 93baa1131e73deb367d770a17683f4c6ce5a4971db82aafb4bc43a641dd85604
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020
  locator: Complete meta, components[0:2] and comments[0]
  accessed_at: '2026-10-21T10:33:38.860616Z'
  support: supports
  summary: Exact TOGO M1020 provider record identifies JCM970 and preserves thirteen
    receiving-batch rows, three iron-stock rows, pH, adjustment-stock normality and
    separate autoclaving. The source units/stages are explicit; neither measured final
    volume nor final iron-stock volume is supplied.
  snapshot_sha256: 21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e
- evidence_id: primary-unavailable
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=970
  locator: Entire exact GRMD970 response
  accessed_at: '2026-10-21T10:33:41.836244Z'
  support: context_only
  summary: 'HTTP200 is not successful formulation retrieval: the exact collection
    page says Nothing found. This capture supplies no recipe, collection sterilization
    default or source chronology. The accessible TOGO representation remains secondary
    evidence.'
  quote: Nothing found
  snapshot_sha256: db773d7e86f547617d21cb88947756c91b13a1f2e84a73136424652f4513aab2
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T10:59:10Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id":
    "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
    [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label":
    "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/164/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T10:59:10Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: b767edb923bbf3aef1923c87ae3d729445ae37e8c484b1d5637f0a56a4a0419f
- evidence_id: classification-schema
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  locator: MediaRecipe.high_metal and MediumCompositionTypeEnum
  accessed_at: '2026-10-21T10:59:10Z'
  support: context_only
  summary: high_metal refers to total enumerated metal concentration at or above 1049.84
    mM. UNDEFINED means a chemically undefined component; DEFINED also requires known
    exact quantities. These native definitions are applied separately from the current
    data errors.
  snapshot_sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:59:10Z'
  support: context_only
  summary: Current code was read, not executed or historically replayed. TOGO now
    separates named primary/stock sections and preserves comment prose, but its local
    stock basis accepts a dose equal to a water row even with another liquid present;
    that is not measured final stock volume. Its unit map recognizes mg but bare ug
    and N fall back to G_PER_L; concentration-only H2SO4 can reach final-concentration
    handling. Current COMPLEX is a default, not source evidence. Metal analysis sums
    approximate mass/native-unit values as mM, does not account for stock delivery
    or molar stoichiometry, and its flag writer consumes prior computed membership.
    Current single-owner merger returns owner content. These observations guide bounded
    follow-up and do not prove the historical sequence or endorse blind reimport.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:59:10Z'
  support: context_only
  summary: Current code was read, not executed or historically replayed. TOGO now
    separates named primary/stock sections and preserves comment prose, but its local
    stock basis accepts a dose equal to a water row even with another liquid present;
    that is not measured final stock volume. Its unit map recognizes mg but bare ug
    and N fall back to G_PER_L; concentration-only H2SO4 can reach final-concentration
    handling. Current COMPLEX is a default, not source evidence. Metal analysis sums
    approximate mass/native-unit values as mM, does not account for stock delivery
    or molar stoichiometry, and its flag writer consumes prior computed membership.
    Current single-owner merger returns owner content. These observations guide bounded
    follow-up and do not prove the historical sequence or endorse blind reimport.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:59:10Z'
  support: context_only
  summary: Current code was read, not executed or historically replayed. TOGO now
    separates named primary/stock sections and preserves comment prose, but its local
    stock basis accepts a dose equal to a water row even with another liquid present;
    that is not measured final stock volume. Its unit map recognizes mg but bare ug
    and N fall back to G_PER_L; concentration-only H2SO4 can reach final-concentration
    handling. Current COMPLEX is a default, not source evidence. Metal analysis sums
    approximate mass/native-unit values as mM, does not account for stock delivery
    or molar stoichiometry, and its flag writer consumes prior computed membership.
    Current single-owner merger returns owner content. These observations guide bounded
    follow-up and do not prove the historical sequence or endorse blind reimport.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-3
  kind: record_content
  reference: scripts/analyze_metal_concentrations.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:59:10Z'
  support: context_only
  summary: Current code was read, not executed or historically replayed. TOGO now
    separates named primary/stock sections and preserves comment prose, but its local
    stock basis accepts a dose equal to a water row even with another liquid present;
    that is not measured final stock volume. Its unit map recognizes mg but bare ug
    and N fall back to G_PER_L; concentration-only H2SO4 can reach final-concentration
    handling. Current COMPLEX is a default, not source evidence. Metal analysis sums
    approximate mass/native-unit values as mM, does not account for stock delivery
    or molar stoichiometry, and its flag writer consumes prior computed membership.
    Current single-owner merger returns owner content. These observations guide bounded
    follow-up and do not prove the historical sequence or endorse blind reimport.
  snapshot_sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
- evidence_id: writer-4
  kind: record_content
  reference: scripts/add_metal_ree_labels.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:59:10Z'
  support: context_only
  summary: Current code was read, not executed or historically replayed. TOGO now
    separates named primary/stock sections and preserves comment prose, but its local
    stock basis accepts a dose equal to a water row even with another liquid present;
    that is not measured final stock volume. Its unit map recognizes mg but bare ug
    and N fall back to G_PER_L; concentration-only H2SO4 can reach final-concentration
    handling. Current COMPLEX is a default, not source evidence. Metal analysis sums
    approximate mass/native-unit values as mM, does not account for stock delivery
    or molar stoichiometry, and its flag writer consumes prior computed membership.
    Current single-owner merger returns owner content. These observations guide bounded
    follow-up and do not prove the historical sequence or endorse blind reimport.
  snapshot_sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIFFEROBACTER_MURCIENSIS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T10:59:10Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml",
    "events": 12, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source accession and sole maintained owner
  outcome: supported
  summary: The root stable ID, explicit single merge contributor and provider M1020/JCM970
    mapping agree. The source and local title both spell Acidifferobacter Murciensis
    Medium; this is accession identity, not confirmation of organism nomenclature
    or growth. No similarly titled recipe is substituted for the inaccessible original.
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - record
  - owner-0
  - id-search
  - provider
  - primary-unavailable
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '13 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 13/14 primary and 6/14 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    mismatch is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi26836
  - chebi33118
  - chebi35696
  - chebi49976
  - chebi62946
  - chebi63036
  - chebi75213
  - chebi75836
  - chebi86158
  - chebi86318
  - chebi86345
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 14: primary 92.86%;
    secondary 42.86%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Every source amount, stock strength, pH and sterilization scope
  outcome: concern
  summary: The eighteen-row inventory covers all sixteen component rows and both preparation
    entries. Ten receiving salts retain mg/ug numerals as g/L; water, stock dose and
    concentrated-acid volumes also have wrong dimensions or scope. The iron-stock
    amount must remain separate until actual stock/working-volume bases are established.
    Neither layer has attached amount evidence; no inventory decision is verified.
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - record
  - owner-0
  - provider
  - quantity-inventory
  details: '[{"field_path": "ingredients[0].concentration (receiving-batch water)",
    "decision": "correct", "current": {"value": "1000.0", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[0]", "exact_source_quote": "\"component_name\":
    \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
    "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}],
    "explanation": "The source specifies 900 ml receiving-batch water. Local 1000
    G_PER_L sums this with 100 ml water used to prepare the separate stock, crosses
    stages and changes volume to mass concentration. Restore both solvent amounts
    at their own stages; do not infer density, final volume, or that every milliliter
    of stock water is delivered by the 100 ml stock aliquot.", "source_original_amount":
    900, "source_original_unit": "ml"}, {"field_path": "ingredients[1].concentration",
    "decision": "correct", "current": {"value": "147", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[1]", "exact_source_quote": "\"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 147,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider specifies 147 mg for the receiving batch, equal to 0.147 g of this
    source material. Local 147 G_PER_L copies the numeral while changing the unit
    and adding a per-liter basis. Restore the exact batch amount and unit; this conversion
    is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate
    molecular-weight conversion is made.", "source_original_amount": 147, "source_original_unit":
    "mg"}, {"field_path": "ingredients[2].concentration", "decision": "correct", "current":
    {"value": "27.2", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[2]", "exact_source_quote": "\"component_name\":
    \"KH2PO4\",\n          \"volume\": 27.2,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider specifies 27.2 mg for the receiving batch, equal to 0.0272 g of
    this source material. Local 27.2 G_PER_L copies the numeral while changing the
    unit and adding a per-liter basis. Restore the exact batch amount and unit; this
    conversion is mass-only arithmetic, not a verified final-medium g/L concentration.
    No hydrate molecular-weight conversion is made.", "source_original_amount": 27.2,
    "source_original_unit": "mg"}, {"field_path": "ingredients[3].concentration",
    "decision": "correct", "current": {"value": "12.1", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[3]", "exact_source_quote": "\"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 12.1,\n          \"unit\": \"ug\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider specifies 12.1 ug for the receiving batch, equal to 0.0000121 g
    of this source material. Local 12.1 G_PER_L copies the numeral while changing
    the unit and adding a per-liter basis. Restore the exact batch amount and unit;
    this conversion is mass-only arithmetic, not a verified final-medium g/L concentration.
    No hydrate molecular-weight conversion is made.", "source_original_amount": 12.1,
    "source_original_unit": "ug"}, {"field_path": "ingredients[4].concentration",
    "decision": "correct", "current": {"value": "25.4", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[4]", "exact_source_quote": "\"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 25.4,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider specifies 25.4 mg for the receiving batch, equal to 0.0254 g of
    this source material. Local 25.4 G_PER_L copies the numeral while changing the
    unit and adding a per-liter basis. Restore the exact batch amount and unit; this
    conversion is mass-only arithmetic, not a verified final-medium g/L concentration.
    No hydrate molecular-weight conversion is made.", "source_original_amount": 25.4,
    "source_original_unit": "mg"}, {"field_path": "ingredients[5].concentration",
    "decision": "correct", "current": {"value": "31", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[5]", "exact_source_quote": "\"component_name\":
    \"H3BO3\",\n          \"volume\": 31,\n          \"unit\": \"ug\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider specifies 31 ug for the receiving batch, equal to 0.000031 g of
    this source material. Local 31 G_PER_L copies the numeral while changing the unit
    and adding a per-liter basis. Restore the exact batch amount and unit; this conversion
    is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate
    molecular-weight conversion is made.", "source_original_amount": 31, "source_original_unit":
    "ug"}, {"field_path": "ingredients[6].concentration", "decision": "correct", "current":
    {"value": "120", "unit": "G_PER_L"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[6]", "exact_source_quote": "\"component_name\":
    \"MnCl2・4H2O\",\n          \"volume\": 120,\n          \"unit\": \"ug\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider specifies 120 ug for the receiving batch, equal to 0.000120 g of
    this source material. Local 120 G_PER_L copies the numeral while changing the
    unit and adding a per-liter basis. Restore the exact batch amount and unit; this
    conversion is mass-only arithmetic, not a verified final-medium g/L concentration.
    No hydrate molecular-weight conversion is made.", "source_original_amount": 120,
    "source_original_unit": "ug"}, {"field_path": "ingredients[7].concentration",
    "decision": "correct", "current": {"value": "120", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[7]", "exact_source_quote": "\"component_name\":
    \"CoCl2・6H2O\",\n          \"volume\": 120,\n          \"unit\": \"ug\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider specifies 120 ug for the receiving batch, equal to 0.000120 g of
    this source material. Local 120 G_PER_L copies the numeral while changing the
    unit and adding a per-liter basis. Restore the exact batch amount and unit; this
    conversion is mass-only arithmetic, not a verified final-medium g/L concentration.
    No hydrate molecular-weight conversion is made.", "source_original_amount": 120,
    "source_original_unit": "ug"}, {"field_path": "ingredients[8].concentration",
    "decision": "correct", "current": {"value": "85.2", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[8]", "exact_source_quote": "\"component_name\":
    \"CuCl2・2H2O\",\n          \"volume\": 85.2,\n          \"unit\": \"ug\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider specifies 85.2 ug for the receiving batch, equal to 0.0000852 g
    of this source material. Local 85.2 G_PER_L copies the numeral while changing
    the unit and adding a per-liter basis. Restore the exact batch amount and unit;
    this conversion is mass-only arithmetic, not a verified final-medium g/L concentration.
    No hydrate molecular-weight conversion is made.", "source_original_amount": 85.2,
    "source_original_unit": "ug"}, {"field_path": "ingredients[9].concentration",
    "decision": "correct", "current": {"value": "132.2", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[9]", "exact_source_quote": "\"component_name\":
    \"(NH4)2SO4\",\n          \"volume\": 132.2,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider specifies 132.2 mg for the receiving batch, equal to 0.1322 g of
    this source material. Local 132.2 G_PER_L copies the numeral while changing the
    unit and adding a per-liter basis. Restore the exact batch amount and unit; this
    conversion is mass-only arithmetic, not a verified final-medium g/L concentration.
    No hydrate molecular-weight conversion is made.", "source_original_amount": 132.2,
    "source_original_unit": "mg"}, {"field_path": "ingredients[10].concentration",
    "decision": "correct", "current": {"value": "70", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[10]", "exact_source_quote": "\"component_name\":
    \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"ug\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider specifies 70 ug for the receiving batch, equal to 0.000070 g of
    this source material. Local 70 G_PER_L copies the numeral while changing the unit
    and adding a per-liter basis. Restore the exact batch amount and unit; this conversion
    is mass-only arithmetic, not a verified final-medium g/L concentration. No hydrate
    molecular-weight conversion is made.", "source_original_amount": 70, "source_original_unit":
    "ug"}, {"field_path": "solutions[0].concentration and composition", "decision":
    "correct", "current": {"preferred_term": "Iron(II) sulfate solution", "composition":
    [], "concentration": {"value": "100", "unit": "G_PER_L"}, "name": "Unknown solution"},
    "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[11]", "exact_source_quote": "\"component_name\":
    \"Iron(II) sulfate solution\",\n          \"volume\": 100,\n          \"unit\":
    \"ml\"", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}],
    "explanation": "The receiving batch adds 100 ml of the locally specified iron
    stock; local 100 G_PER_L is the wrong dimension and its empty composition loses
    the explicit stock definition. Resolve the same-record section by its exact name,
    retain its separate preparation, and preserve the dose as volume. The source supplies
    no measured final stock volume and does not prove that this aliquot transfers
    all 20 g of stock iron salt.", "source_original_amount": 100, "source_original_unit":
    "ml"}, {"field_path": "ingredients[11].concentration and preparation_steps (acid
    stock strength)", "decision": "not_quantified", "current": {"value": "variable",
    "unit": "VARIABLE"}, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "not_quantified"}, "source_stage": "receiving batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[0].items[12]", "exact_source_quote": "\"component_name\":
    \"H2SO4\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"N\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The provider identifies a 10 N acid stock for adjustment to pH 2.0 but supplies
    no addition amount. VARIABLE correctly avoids a fixed working dose; recover the
    missing stock normality and purpose with evidence. Neither 10 N nor variable is
    a final-medium concentration, and the unquantified addition must not be set to
    zero.", "source_original_stock_strength": 10, "source_original_strength_unit":
    "N"}, {"field_path": "ingredients[0].concentration (iron-stock water)", "decision":
    "correct", "current": {"value": "1000.0", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "separate iron-stock batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[1].items[0]", "exact_source_quote": "\"component_name\":
    \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
    "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}],
    "explanation": "The source uses 100 ml water to prepare the iron stock. It is
    not an additional independent receiving-medium water row and not a declaration
    of final stock volume: 20 g iron salt and 2 ml concentrated acid are also added.
    Keep the stock solvent separate from the 900 ml receiving-batch water; do not
    sum either 100+2 ml or 900+100 ml into an asserted measured final volume.", "source_original_amount":
    100, "source_original_unit": "ml"}, {"field_path": "ingredients[12].concentration",
    "decision": "correct", "current": {"value": "20", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "separate iron-stock batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[1].items[1]", "exact_source_quote": "\"component_name\":
    \"FeSO4・7H2O\",\n          \"volume\": 20,\n          \"unit\": \"g\"", "snapshot_sha256":
    "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}], "explanation":
    "The 20 g iron(II) sulfate heptahydrate belongs to the separately prepared stock
    batch. Local 20 G_PER_L at root has an unsupported final-medium scope. Source
    stock water is 100 ml, but the prepared stock volume is unstated; its 100 ml dose
    therefore does not establish the transferred iron amount. Preserve 20 g in the
    stock definition without assigning 200 g/L stock or 20 g/L working concentration.",
    "source_original_amount": 20, "source_original_unit": "g"}, {"field_path": "ingredients[13].concentration",
    "decision": "correct", "current": {"value": "2", "unit": "G_PER_L"}, "owner_decisions":
    {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "correct"}, "source_stage": "separate iron-stock batch", "source_snippets": [{"source_key":
    "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.components[1].items[2]", "exact_source_quote": "\"component_name\":
    \"H2SO4 (concentrated)\",\n          \"volume\": 2,\n          \"unit\": \"ml\"",
    "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}],
    "explanation": "The iron stock uses 2 ml concentrated sulfuric acid. Local 2 G_PER_L
    changes a stock-batch liquid amount into a root mass concentration. No numeric
    purity, density or molarity is supplied; restore original volume and concentrated
    qualifier in the stock, without a typical-strength conversion or final-medium
    acid dose.", "source_original_amount": 2, "source_original_unit": "ml"}, {"field_path":
    "ph_value and preparation_steps (receiving-batch pH)", "decision": "add", "current":
    null, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "add"}, "source_stage": "receiving-batch adjustment before autoclaving", "source_snippets":
    [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.comments[0].comment", "exact_source_quote": "Adjust pH to
    2.0 with 10 N H2SO4 and autoclave.", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}],
    "explanation": "The source pH target and titrant context are missing in both layers.
    Add pH 2.0 and its preparation scope with the exact provider excerpt; it is not
    an organism-growth optimum or a quantified acid dose."}, {"field_path": "preparation_steps
    (separate autoclaving; cycle numbers)", "decision": "not_quantified", "current":
    null, "owner_decisions": {"data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml":
    "not_quantified"}, "source_stage": "receiving batch and separately sterilized
    iron stock", "source_snippets": [{"source_key": "togoM1020", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1020",
    "source_locator": "$.comments[0].comment", "exact_source_quote": "Adjust pH to
    2.0 with 10 N H2SO4 and autoclave. After autoclaving, add the following solution
    (separately autoclaved):", "snapshot_sha256": "21c531f45b09a6f7a2d50391079d77301c427d6ea865b003f5de00e8eebb426e"}],
    "explanation": "The operation and order are supplied: adjust/autoclave the receiving
    batch, then add the separately autoclaved iron solution. Recover that missing
    procedure, while retaining temperature and duration as not quantified. The unavailable
    JCM970 page cannot supply a numeric collection default."}]'
- assessment_id: chemical-forms
  area: grounding
  topic: Hydrate and reagent-form correspondence
  outcome: concern
  summary: The provider specifies CoCl2・6H2O, while CHEBI:35696 denotes cobalt dichloride
    with formula 2Cl.Co and no water components. This is a source-form mismatch despite
    valid canonical metadata. Other explicit salt hydrate formulas agree with their
    captured terms. Sulfuric-acid ontology identity does not specify the 10 N adjustment
    stock or the concentrated stock reagent; their strengths/doses remain separately
    scoped.
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - record
  - owner-0
  - provider
  - chebi35696
  - chebi26836
  - chebi75836
  - chebi86158
  - chebi75213
  - chebi86345
  - chebi86368
  - chebi86318
- assessment_id: preparation
  area: completeness
  topic: pH, ordered separate sterilization and stock identity
  outcome: concern
  summary: Both layers omit preparation_steps and ph_value despite the complete provider
    comment. The stock preferred_term names the exact source section, while name=Unknown
    solution and composition=[] are placeholders. Recover the same-record definition
    and distinct stock treatment; do not infer autoclave cycle numbers, gas conditions,
    incubation or organism growth.
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - record
  - owner-0
  - provider
  - quantity-inventory
  - primary-unavailable
- assessment_id: classification
  area: scope
  topic: Composition and high-metal flag support
  outcome: concern
  summary: 'The complete accessible formulation contains specified inorganic salts,
    water and sulfuric-acid reagents; it supplies no compositionally undefined nutrient
    mixture supporting COMPLEX/UNDEFINED. DEFINED is the composition direction, with
    exact-quantity/stock-volume gaps still explicit. The iron stock supports substantial
    iron loading, but not the schema-defined high_metal=true threshold: the full stock
    batch contains 20 g FeSO4·7H2O, while the fraction delivered by its 100 ml dose
    and final volume remain unresolved. Do not assert false merely because other units
    are wrong. Reassess or withdraw the unsupported true assertion using correct stage-aware
    molar calculations. LIQUID is consistent with the water-based provider inventory.'
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - record
  - owner-0
  - provider
  - classification-schema
  - chebi75836
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: biology
  area: scope
  topic: Growth, category and literature limits
  outcome: supported
  summary: The title, bacterial folder and generic cultivation application are not
    strain-level growth evidence. No target organism, taxon identifier, incubation
    optimum or literature-supported biological phenotype is asserted. The review assesses
    the exact medium representation without adding such claims.
  target_ids:
  - CultureMech:007535
  evidence_ids:
  - record
  - provider
findings:
- finding_id: f1
  issue_key: m1020-unit-and-stock-scope
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Mass units and stock boundaries are scientifically unsafe
  description: Both local layers turn ten mg/ug batch amounts into the same numerals
    in g/L, sum water across receiving and stock stages, store the 100 ml stock dose
    as 100 g/L, and flatten stock iron/concentrated acid into the receiving-medium
    list. The source does not establish a final stock volume or the iron mass delivered
    by that aliquot. Passing structural checks do not make these quantities usable.
  target_ids:
  - CultureMech:007535
  field_paths:
  - ingredients[0].concentration
  - ingredients[1:11].concentration
  - ingredients[12:14]
  - solutions[0].concentration
  - solutions[0].composition
  evidence_ids:
  - record
  - owner-0
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: m1020-cobalt-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Cobalt chloride hexahydrate is linked to a different supplied form
  description: The exact provider names the hexahydrate, whereas asserted CHEBI:35696
    represents cobalt dichloride without waters. Canonical label resolution and numerical
    amount recovery cannot validate that hydrate correspondence.
  target_ids:
  - CultureMech:007535
  field_paths:
  - ingredients[7].term
  evidence_ids:
  - record
  - owner-0
  - provider
  - chebi35696
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: m1020-preparation-source-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and useful stock identity are missing
  description: Both layers lack the provider pH and separately ordered autoclaving
    procedure, any attached amount evidence, and the full iron-stock definition; its
    name remains Unknown solution despite an exact matching source-section name. The
    original collection recipe is currently unavailable, so provider support must
    remain explicitly qualified.
  target_ids:
  - CultureMech:007535
  field_paths:
  - ph_value
  - preparation_steps
  - ingredients[*].evidence
  - solutions[0].name
  - solutions[0].composition
  - references
  evidence_ids:
  - record
  - owner-0
  - provider
  - primary-unavailable
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normally maps to minor; major is justified by missing pH,
    separate sterilization order, stock identity and all attached quantity evidence,
    which materially affect reconstruction rather than presentation.
- finding_id: f4
  issue_key: m1020-composition-metal-classification
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Composition defaults and the high-metal assertion lack source support
  description: 'COMPLEX/UNDEFINED are inconsistent with the inspected chemically specified
    inorganic inventory. high_metal=true is a separate threshold assertion: substantial
    iron loading alone does not establish total metal at least 1049.84 mM, and current
    automated mass/stock handling cannot supply independent support. The exact iron
    delivered from the source stock is unresolved.'
  target_ids:
  - CultureMech:007535
  field_paths:
  - medium_type
  - composition_type
  - high_metal
  evidence_ids:
  - record
  - owner-0
  - provider
  - classification-schema
  - chebi75836
  - writer-0
  - writer-3
  - writer-4
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Restore exact native receiving-batch units, solvent context, stock
    definition and stock dose in the maintained owner using the complete field inventory.
    Remove unsupported root stock contributions; retain unresolved delivered concentrations
    rather than guessing volume or density. Attach claim-level source evidence, and
    inspect current importer unit/basis behavior before any separately authorized
    reimport. Regenerate only after source-scoped correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007535
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
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
  description: Resolve and correct the supplied cobalt-chloride hydrate identity in
    the maintained owner with authoritative term/form evidence; preserve the original
    120 ug batch mass. Do not infer a replacement ID or perform an anhydrous mass
    conversion from this review alone.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007535
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
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
  description: Add exact provider citations and literal claim-level excerpts; recover
    pH 2.0, 10 N titrant with unknown dose, receiving-medium autoclaving and subsequent
    separately autoclaved stock addition. Use the exact source stock name and preserve
    all stock source quantities. Seek the original JCM970 recipe without substituting
    another medium, and leave cycle temperature/time unquantified until sourced.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007535
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
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
  description: Reassess composition against the complete source inventory, using DEFINED
    as the supported direction while explicitly retaining exact-quantity limitations.
    Recalculate threshold support only with verified units, supplied forms, stock
    dilution and valid molar arithmetic; withdraw or qualify unsupported high_metal=true
    rather than automatically replacing it with false. Preserve the source iron-stock
    facts and append provenance for authorized changes.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007535
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1020_Acidifferobacter_Murciensis_Medium.yaml
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
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- Partial completion is required because the exact JCM970 collection page provides
  no recipe. Scientific findings are bounded to the complete accessible TOGO M1020
  representation and captured ontology metadata.
- The iron stock has no stated measured final volume, the 100 ml aliquot does not
  prove complete transfer of its 20 g iron salt, and the receiving medium has no measured
  final volume. No final iron/acid concentration or high_metal=false value is inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-017
- generated-medium
```
