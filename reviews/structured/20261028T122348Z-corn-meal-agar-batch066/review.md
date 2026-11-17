# Scientific review of corn_meal_agar

- Review: 20261028T122348Z-corn-meal-agar-batch066
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T12:04:49.471399Z
- Finished UTC: 2026-10-28T12:23:48.424210Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The basal source supports an extraction-based Corn Meal Agar recipe, but the generated target loses that stage and current preparation. Two methanogen strain wrappers remain unverified pH variants, and the KG link points to Soil Extract Medium. Maintain source and variant separation before regeneration.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch066 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004218 | data/merge_yaml/merged/CORN_MEAL_AGAR.yaml | generated | corn_meal_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:004218 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:004218 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:004218 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:004218 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Basal identity and independent strain wrappers

identity: concern. Targets: CultureMech:004218.

The exact DSM 191 primary/API identify Corn Meal Agar. JCM 15416 maps DSM 25939 to Methanobacterium flexile GH, and JCM 15415 maps DSM 25945 to M. movens TS-2; NCBI 490098/493461 confirm archaeal species lineages. Their collection media differ from the local corn-meal wrapper identity. This establishes a material identity/variant review requirement, not a claim that experimental growth on corn meal is impossible. No collection condition or unrelated recipe is transferred.

### Classification, atmosphere and formulation references

consistency: concern. Targets: CultureMech:004218.

Basal complex/undefined agar classification is consistent with the source. The target Aerobic:No note lacks explicit primary support. The bacterial category on the strain wrappers is inconsistent with their independently resolved archaeal identities, while the generic basal medium is not recategorized solely from those wrappers. mediadive.medium:12 resolves to Soil Extract Medium rather than Corn Meal Agar.

### Agar and provider compound identity

grounding: supported. Targets: CultureMech:004218.

All ten selected agar primary/secondary slots match current CHEBI:2509 and exact MIM CSV rows. The four owner corn-meal mediadive.compound:2087 slots exactly match API 191; the target has no corn-meal term. This provider identifier is not misrepresented as CHEBI or a pure-compound identity. No numeric legacy MIM identifiers occur.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:004218.

All 11 exact selected-name reports were read, including two namesake commercial-media reports as explicitly excluded comparison context. Current API 191 raw bytes authenticate matching historical objects, not separate KOMODO catalogue bytes or access times. No selected layer has attached formulation evidence. The current corn-meal repair hardcodes variant pH/classification and replaces matching history events; its existing behavior is not permission to rewrite history or apply its unselected sibling plan. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:004218.

All 10 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:004218", "selected_concentration_field_count": 10, "selected_concentration_fields_covered": 10, "decisions": [{"decision_id": "q1", "subject": "Corn meal extraction input in generated target", "local_fields": [{"record_path": "data/merge_yaml/merged/CORN_MEAL_AGAR.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "50", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "Raw extraction input, not retained solute mass", "interpretation": "The primary uses 50 g raw corn meal, then filters the extract before making up to 1 L. The target drops the extraction/filtering context and presents 50 G_PER_L as an ordinary final ingredient. Preserve the raw-input basis and filtrate stage; the retained corn-meal mass is not quantified.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Corn meal\",\n                        \"compound_id\": 2087,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-5", "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator.\nHeat at 60C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "Corn meal input in repaired basal owners", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "50.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "50.0", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Raw material per litre of prepared extract", "interpretation": "Both current basal owners explicitly retain the extraction/filter/make-up notes. Their 50 G_PER_L is supportable only as raw input per litre of extract, not retained solid or dissolved corn-meal concentration. No attached claim-level evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Corn meal\",\n                        \"compound_id\": 2087,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-5", "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator.\nHeat at 60C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "Agar in basal recipe", "local_fields": [{"record_path": "data/merge_yaml/merged/CORN_MEAL_AGAR.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "10.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "10.0", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "Added after extract is made up to 1 L", "interpretation": "The primary adds 10 g agar after the filtrate is made up to 1 L; API g_l = 10 supplies the corresponding nominal formulation basis. Retain 10 with this stage, without claiming a separately measured volume after agar dissolution. The historical blanket unsupported decisions do not negate this direct support.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 29.7327,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Heat at 60C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "Unresolved strain-wrapper Corn meal", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "50.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "50.0", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Unverified variant/source identity", "interpretation": "The copied numbers reproduce the basal recipe, but current JCM identities resolve DSM 25939 and DSM 25945 to different methanogen species and neither catalogue supports these corn-meal variants. Exact KOMODO routes returned 403. Basal agreement does not authenticate a strain-specific formulation or its pH; no replacement recipe is proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Corn meal\",\n                        \"compound_id\": 2087,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "Unresolved strain-wrapper Agar", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "10.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "10.0", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "Unverified variant/source identity", "interpretation": "The copied numbers reproduce the basal recipe, but current JCM identities resolve DSM 25939 and DSM 25945 to different methanogen species and neither catalogue supports these corn-meal variants. Exact KOMODO routes returned 403. Basal agreement does not authenticate a strain-specific formulation or its pH; no replacement recipe is proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 29.7327,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "Initial extraction water and overnight holding", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml", "field_path": "preparation_steps[0].description", "original": "Blend 50.0 g corn meal in 800 ml distilled water and leave overnight in the refrigerator."}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "field_path": "preparation_steps[0].description", "original": "Blend 50.0 g corn meal in 800 ml distilled water and leave overnight in the refrigerator."}], "decision": "evidence_only", "stage": "Initial extraction, before filtering/make-up", "interpretation": "The current basal owners retain the exact initial 800 ml and overnight refrigerator step; the generated target omits it. The primary gives no numerical refrigerator temperature or overnight duration. Do not replace this with1000 ml added at the start merely because API lists total water 1000 ml.", "sources": [{"locator": "extracted-text lines 4-4", "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[1]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "Extraction heating", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml", "field_path": "preparation_steps[1].description", "original": "Heat at 60 C for one hour."}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "field_path": "preparation_steps[1].description", "original": "Heat at 60 C for one hour."}], "decision": "evidence_only", "stage": "Before filtration", "interpretation": "Retain the source 60 degrees C for one hour already in the basal owners; missing from generated target. These are extraction conditions, not organism growth claims.", "sources": [{"locator": "extracted-text lines 5-5", "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Heat at 60C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "Filtration and make-up", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml", "field_path": "preparation_steps[2].description", "original": "Filter and bring the volume to 1 L."}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "field_path": "preparation_steps[2].description", "original": "Filter and bring the volume to 1 L."}], "decision": "evidence_only", "stage": "Filtered extract volume", "interpretation": "Explicit make-up to 1 L supports the extract-volume basis. It does not establish complete retention of the starting 50 g corn meal.", "sources": [{"locator": "extracted-text lines 5-5", "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Heat at 60C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "Agar dissolution and autoclaving", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml", "field_path": "preparation_steps[3].description", "original": "Add 10.0 g agar and heat to dissolve."}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "field_path": "preparation_steps[3].description", "original": "Add 10.0 g agar and heat to dissolve."}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml", "field_path": "preparation_steps[4].description", "original": "Autoclave the completed corn meal agar."}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "field_path": "preparation_steps[4].description", "original": "Autoclave the completed corn meal agar."}], "decision": "evidence_only", "stage": "After extract make-up", "interpretation": "Current basal owners retain the correct ordering and general autoclaving. The primary gives no sterilization temperature or duration; API adds 121 degrees C / 15 minutes. Those additional provider controls may be recorded only with their distinct source attribution, not quoted as primary PDF text.", "sources": [{"locator": "extracted-text lines 5-5", "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Heat at 60C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to", "quote_representation": "captured extracted text"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "dissolve, then autoclave.", "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"step\": \"Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator. Heat at 60\\u00b0C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\\u00b0C for 15 minutes. pH 6.0.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "Basal pH", "local_fields": [{"record_path": "data/merge_yaml/merged/CORN_MEAL_AGAR.yaml", "field_path": "ph_value", "original": 6.0}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml", "field_path": "ph_value", "original": 6.0}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "field_path": "ph_value", "original": 6.0}], "decision": "evidence_only", "stage": "Provider metadata/control", "interpretation": "Target and basal owners pH6 agree with current API min_pH/max_pH and preparation, while the PDF does not specify pH. Retain provider-scoped evidence rather than claiming PDF support.", "sources": [{"locator": "$.data.medium", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n            \"id\": 191,\n            \"name\": \"CORN MEAL AGAR\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 6,\n            \"max_pH\": 6,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf\"\n        }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"step\": \"Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator. Heat at 60\\u00b0C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\\u00b0C for 15 minutes. pH 6.0.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "Wrapper pH and preparation scope", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml", "field_path": "ph_value", "original": 7.2}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml", "field_path": "preparation_steps[0].description", "original": "Blend 50.0 g corn meal in 800 ml distilled water and leave overnight in the refrigerator."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml", "field_path": "preparation_steps[1].description", "original": "Heat at 60 C for one hour."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml", "field_path": "preparation_steps[2].description", "original": "Filter and bring the volume to 1 L."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml", "field_path": "preparation_steps[3].description", "original": "Add 10.0 g agar and heat to dissolve."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml", "field_path": "preparation_steps[4].description", "original": "Autoclave the completed corn meal agar."}], "decision": "unsupported", "stage": "Variant identity unresolved", "interpretation": "The old catalogue excerpt reports this pH and the current repair copies basal preparation. Those derivative rows and copied steps do not independently authenticate use of corn-meal agar for the exact methanogen strain. Retain unresolved claims without transferring collection growth conditions or supplying a replacement formulation.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"step\": \"Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator. Heat at 60\\u00b0C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\\u00b0C for 15 minutes. pH 6.0.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "Wrapper pH and preparation scope", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml", "field_path": "ph_value", "original": 7.4}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml", "field_path": "preparation_steps[0].description", "original": "Blend 50.0 g corn meal in 800 ml distilled water and leave overnight in the refrigerator."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml", "field_path": "preparation_steps[1].description", "original": "Heat at 60 C for one hour."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml", "field_path": "preparation_steps[2].description", "original": "Filter and bring the volume to 1 L."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml", "field_path": "preparation_steps[3].description", "original": "Add 10.0 g agar and heat to dissolve."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml", "field_path": "preparation_steps[4].description", "original": "Autoclave the completed corn meal agar."}], "decision": "unsupported", "stage": "Variant identity unresolved", "interpretation": "The old catalogue excerpt reports this pH and the current repair copies basal preparation. Those derivative rows and copied steps do not independently authenticate use of corn-meal agar for the exact methanogen strain. Retain unresolved claims without transferring collection growth conditions or supplying a replacement formulation.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"step\": \"Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator. Heat at 60\\u00b0C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\\u00b0C for 15 minutes. pH 6.0.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q13", "subject": "Provider-only sterilization settings", "local_fields": [], "decision": "evidence_only", "stage": "Additional provider preparation context", "interpretation": "The API explicitly adds 121 degrees C for 15 minutes; the primary says only autoclave. This source difference must remain visible and is not a silently inferred primary prescription.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"step\": \"Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator. Heat at 60\\u00b0C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\\u00b0C for 15 minutes. pH 6.0.\"\n                    }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch066/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: supported. Targets: CultureMech:004218.

data/merge_yaml/merged/CORN_MEAL_AGAR.yaml: primary 1/2, secondary 1/2; data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml: primary 2/2, secondary 1/2; data/normalized_yaml/bacterial/corn_meal_agar.yaml: primary 2/2, secondary 1/2; data/normalized_yaml/bacterial/for_dsm_25939.yaml: primary 2/2, secondary 1/2; data/normalized_yaml/bacterial/for_dsm_25945.yaml: primary 2/2, secondary 1/2. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:004218.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:004218.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Corn-meal extraction and preparation context are missing from generated content

major / open / confirmed; issue key: culturemech-004218-extraction-stage-and-generated-preparation-loss.

The target lists 50 G_PER_L corn meal without the extraction/filter stage and omits all five preparation steps now retained by its basal owners. 50 g is raw extraction input; recovered solute/solid mass is unquantified. The agar rate is supported on the defined extract basis. Current repaired owners and conservative merge safeguards are credited; this old target is stale.

### f2: Named strain wrappers are not authenticated corn-meal pH variants

major / open / confirmed; issue key: culturemech-004218-unverified-methanogen-wrapper-identity.

The two selected wrappers resolve to distinct Methanobacterium species. Their copied basal formulation and pH values are not established by the generic DSM 191 source. The generated target still merges them as SOURCE_DUPLICATE although the maintained repair labels them PH_VARIANT. Both relationship claims need exact variant evidence, and wrapper bacterial categories require reconsideration against their archaeal identities.

### f3: The KG medium link resolves to a different recipe identity

major / open / confirmed; issue key: culturemech-004218-kg-reference-points-to-soil-extract.

All five selected documents assert mediadive.medium:12, which current MediaDive identifies as SOIL EXTRACT MEDIUM. The selected basal identity is DSM 191. The current KG matcher compares ingredient identifier sets and cannot establish recipe identity; no automatic replacement is inferred for the unresolved strain wrappers.

### f4: Imported atmosphere and history require bounded provenance repair

minor / open / confirmed; issue key: culturemech-004218-import-provenance-and-unsupported-atmosphere.

The target retains Aerobic:No without explicit primary support; the repaired owners already omit that inherited note. Target and KOMODO-derived owners preserve malformed literal .fZ import times and naive resolver times. Current importer formatting and resolver behavior explain present risks, not authenticated historical execution.

## Recommended Actions And Acceptance Checks

### action1

Preserve the source raw-input and filtered-extract stages, retain the correct basal owner steps and attach narrow ingredient/root evidence. Regenerate only after resolving the strain-wrapper ownership issue; do not infer a retained corn-meal concentration.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Resolve each exact wrapper accession and strain identity independently. Withhold unsupported duplicate/pH-variant and growth claims; do not transplant a methanogen recipe into the basal Corn Meal Agar record. Review the hardcoded current repair and affected relationships before any future regeneration; keep unselected DSM 25720 outside this review.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Reconcile each selected KG link against exact source identity; retain or remove unresolved linkage rather than accepting set similarity as recipe equivalence. Verify the basal 191 candidate separately and avoid transferring it to unverified variants.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Keep original events unchanged. Correct future timestamp formatting and append a verified current-date context event; do not invent historical times. Remove or qualify the unsupported generated atmosphere note while preserving any genuinely supported source claim.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CORN_MEAL_AGAR.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/corn_meal_agar.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local3 | data/normalized_yaml/bacterial/for_dsm_25939.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local4 | data/normalized_yaml/bacterial/for_dsm_25945.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch066/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch066/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch066/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch066/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsmz191 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api191 | https://mediadive.dsmz.de/rest/medium/191; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| api12 | https://mediadive.dsmz.de/rest/medium/12; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Excluded comparison identity: current medium12 is SOIL EXTRACT MEDIUM, not selected DSM191 Corn Meal Agar. No recipe transfer; this resolves only the asserted KG-medium reference. |
| komodo191 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=191; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| komodo191_3 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=191.3; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| komodo191_4 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=191.4; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| strain25939 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=15416; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Official collection catalogue identity, strain aliases, habitat and recommended-medium association read in full. This is collection guidance, not a primary experimental growth measurement or authentication of a different KOMODO recipe. |
| strain25945 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=15415; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Official collection catalogue identity, strain aliases, habitat and recommended-medium association read in full. This is collection guidance, not a primary experimental growth measurement or authentication of a different KOMODO recipe. |
| tax490098 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=490098&amp;retmode=xml; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current NCBI Taxonomy identifier, scientific name, aliases and lineage read; collection aliases are independently joined to the collection authority. No medium or growth assertion follows from taxonomy. |
| tax493461 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=493461&amp;retmode=xml; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current NCBI Taxonomy identifier, scientific name, aliases and lineage read; collection aliases are independently joined to the collection authority. No medium or growth assertion follows from taxonomy. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch066/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/corn_meal_agar.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api191 raw bytes exactly match the cited historical SHA, and 4 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history1 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_25945.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api191 raw bytes exactly match the cited historical SHA, and 4 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api191 raw bytes exactly match the cited historical SHA, and 4 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history3 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_25939.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api191 raw bytes exactly match the cited historical SHA, and 4 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_25945.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_25939.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/corn_meal_agar.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history7 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history8 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/corn_meal_agar__edd1883a.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history9 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/corn_meal_agar__47c378f9.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history10 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CORN_MEAL_AGAR.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch066/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer33 | scripts/apply_mim_groundings.py; target_slot; groundable; apply_to_record | context_only | Current target_slot preserves existing CHEBI assertions; groundable excludes conflicting corpus opinions, and apply_to_record fills ungrounded entries from proposals. This writer does not authenticate source amounts or automatically repair an existing wrong supplied-form ID. |
| writer34 | scripts/assign_culturemech_ids.py; assign_ids; _assign_id_to_file | context_only | Current assign_ids selects records with missing IDs; _assign_id_to_file checks new-ID collisions and appends identifier provenance. Identifier assignment does not authenticate recipe content or demonstrate historical source access. |
| writer35 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer36 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer37 | scripts/enrich_with_chebi.py; RecipeEnricher.enrich_ingredient; enrich_recipe; enrich_file | context_only | Current RecipeEnricher.enrich_ingredient skips already grounded entries and delegates missing-term mapping to ChemicalMapper; enrich_recipe traverses ingredient and solution structure, and enrich_file writes results and history. Only the read wrapper behavior is claimed here; the mapper is not treated as an independent supplied-form authority. |
| writer38 | scripts/enrich_with_mediaingredientmech.py; main | context_only | Current main orchestrates a local or cloned MIM repository, its loader and ingredient linker. The CLI orchestration was read; it does not itself verify source recipe quantities, supplied chemical forms or the validity of historical MIM assertions. Linker internals are not claimed as separately audited scientific evidence. |
| writer39 | scripts/migrate_chebi_regrounding.py; rewrite_entry; migrate_file | context_only | Current rewrite_entry applies configured exact-ID/label remaps across primary and secondary slots; migrate_file records applied changes. A successful current mapping operation does not establish source-specific hydrate or stereochemical equivalence. |
| writer40 | scripts/migrate_legacy_mim_to_chebi.py; _resolve_chebi; _rewrite_entry | context_only | Current _resolve_chebi reuses current primary CHEBI where available and considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry retains unresolved links. Current-row presence is distinct from historical validity and from source-specific supplied-form equivalence. |
| writer41 | scripts/migrate_ph_range.py; parse_ph_range; migrate_one | context_only | Current parse_ph_range retains qualifiers in notes and migrate_one converts only string-valued pH ranges, recording provenance. No particular source range is authenticated by this writer. |
| writer42 | scripts/normalize_media_names_to_snake_case.py; process_file; add_curation_history | context_only | Current process_file preserves the original medium name while normalizing its machine name; add_curation_history appends a naming event. Name normalization does not prove equivalence of differently maintained source branches or recipe variants. |
| writer43 | scripts/refill_term_labels.py; refill_text | context_only | Current refill_text replaces term labels using the current exact identifier lookup while preserving other text. Canonical label correspondence is not an independent choice of the correct chemical form for the supplied source reagent. |
| writer44 | scripts/repair_komodo_corn_meal_score25.py; _corn_meal_recipe; TARGETS; CHILD_LINKS; _ensure_flags; _upsert_history; plan_repairs | context_only | Current _corn_meal_recipe and TARGETS hardcode the basal extraction recipe plus pH values for all five listed records; CHILD_LINKS assigns PH_VARIANT to the two selected strain wrappers. _ensure_flags removes unresolved flags and adds ingredients_curated. _upsert_history replaces a matching curator/action event, while plan_repairs also touches an unselected25720 sibling. This current fixed-input repair has no live strain/source authentication guard and is not safe evidence that the wrapper identities are correct. Review only the selected four owners; do not apply its broader plan automatically. |
| writer45 | scripts/repair_komodo_strain_backlinks.py; PARENTS; CHILDREN; repair_parent; plan_repairs; _upsert_event | context_only | Current repair_parent and plan_repairs target only the explicitly listed 131/777 parents and their two strain children. They do not repair the selected records. _upsert_event replaces a matching curator/action event or appends it; this existing behavior is not permission to rewrite history during this review. |
| writer46 | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS duplicate notes. This bounded repair is not a general solution for product decomposition, stock flattening or differing source formulations. |
| writer47 | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients and solutions, fills pH when absent and copies physical/medium type, but does not copy preparation steps. _add_enrichment_metadata records a naive current timestamp. This explains a present omission risk, not historical execution. |
| writer48 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech constructs source notes and default LIQUID with empty ingredients. Its time.strftime format contains %f, which is unsupported here and is consistent with literal .fZ in stored import events. Current code does not authenticate the original retrieval or justify rewriting historical time. |
| writer49 | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps | context_only | Current _parse_api_composition considers the primary recipe, prefers provider g_l when available and excludes recognized solvents; _is_api_stock_addition distinguishes stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps collects solution prose. These present behaviors do not establish historical execution and cannot justify interpreting flattened stock rates as final-medium concentrations. |
| writer50 | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients; find_matches; find_exact_match | context_only | Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs, find_matches compares set Jaccard and find_exact_match selects the first exact identifier set. Quantities, preparation and ungrounded ingredients are not compared, so an exact set match does not establish formulation identity. |
| writer51 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer52 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer53 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| writer54 | src/culturemech/validation/schema_defaulter.py; apply_defaults; _fix_ingredient; _fix_solution | context_only | Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE amounts and placeholder names for structural completeness. A default is not evidence for a dose, composition, solution identity or denominator; existing default-history events remain contextual. |
| quantity-inventory | REVIEW_WORK/batch066/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- All three exact current KOMODO routes returned HTTP 403; historical catalogue snippets remain derivative, separate from the authenticated API 191 payload.
- DSM 191 PDF and API differ in additional provider pH/sterilization details. Extract make-up to 1 L is explicit; retained corn-meal mass and post-agar measured final volume are not.
- The unselected DSM 25720 sibling and two same-label commercial-media reports are context only; no formulation, category or growth assessment transfers to them. Current collection identity is not an experimental growth claim.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T122348Z-corn-meal-agar-batch066
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of corn_meal_agar
started_at: '2026-10-28T12:04:49.471399Z'
finished_at: '2026-10-28T12:23:48.424210Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh review of existing unchanged repository records; this
    reviewer did not author or curate the selected target/owners. Historical reports
    were independently reassessed against current exact sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The basal source supports an extraction-based Corn Meal Agar recipe, but
  the generated target loses that stage and current preparation. Two methanogen strain
  wrappers remain unverified pH variants, and the KG link points to Soil Extract Medium.
  Maintain source and variant separation before regeneration.
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
  - path: data/merge_yaml/merged/CORN_MEAL_AGAR.yaml
    sha256: c7fc255ccc425575a494b834d7a9fdeb46b1ee706ad254fa8bdb6c95b490e925
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
    sha256: cd4239d4892d37c3b1c8e7a1ee3b310e616bcef37605adeeaadf2e0ed4577a8c
    role: context
  - path: data/normalized_yaml/bacterial/corn_meal_agar.yaml
    sha256: e9d140d6162916195a0764e063c59f700fa9a09f00e4586eac5255bef4642c95
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_25939.yaml
    sha256: b7c8c1e99a8dfc63b105713bad3c72eea91e5121046a26f17b49fee465ccd843
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_25945.yaml
    sha256: b5db1084455f89453854a863497c9f9e8d9bdeae0b7f51a71659005a15b0e53c
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml.md
    sha256: 1f58a4b69dc60da18421cade2720227d15c90c05425346cdcab7a87d461274f3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_25939.yaml.md
    sha256: 34c637dc33b072ee8979da6bc99c7e6e7b37369d3b56f0294a2e7e245feaf971
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_25945.yaml.md
    sha256: 18217b8bd75f92c9af494c382f8ad845a112025cde9b55f85f9f2773287bdcf8
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/corn_meal_agar.yaml.md
    sha256: c56c7427c041169799e00a317297a38a9c9ba8c405eaa49accbcc5d4a66807b6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CORN_MEAL_AGAR.md
    sha256: 190994583b5fffebc231c3a67c91af69d081f435103c306c832f8275672a179a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/corn_meal_agar__47c378f9.md
    sha256: 37c5cd81f166ccb21a9f9f543a573f5b22e49e3aab628c8cf2d954342a9e0463
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/corn_meal_agar__edd1883a.md
    sha256: 630664e4c271af3ca9acd3743a55a71fd992ba4171f09df529316f2371d8bcee
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.md
    sha256: 8b97ef5ac9cc94e8aa85b93f4471d9f7dac9ba608cf028414ce8816d4c35c417
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/corn_meal_agar.md
    sha256: c06e6f3c37c5d1cc81e38cdd7b64cbd0f5b5bb308338e16bddd3bfdbc000ca42
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_25939.md
    sha256: 8d7d832f6036df03208cf682623ce28fc25997ce5b988d6623f3492560d2d4c9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_25945.md
    sha256: 2d2c11dfa4100ff7d1b20e2b8926c07fee632c570842518f1bdfe37cbd2ced22
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
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
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
  - path: scripts/repair_komodo_corn_meal_score25.py
    sha256: 64b5e39d4a5b086147c431846ed0a03a937a6a3c7020e2674cd4ec7a7964c8dd
    role: context
  - path: scripts/repair_komodo_strain_backlinks.py
    sha256: 06d56149f4e8333f31ae6dd7e4b9127881227810bc957429c849ba00de21c963
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
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
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch066 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:004218
targets:
- target_id: CultureMech:004218
  path: data/merge_yaml/merged/CORN_MEAL_AGAR.yaml
  label: corn_meal_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/corn_meal_agar.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25939.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25945.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:004218
  command: just validate-schema data/merge_yaml/merged/CORN_MEAL_AGAR.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:004218
  command: just validate-strict data/merge_yaml/merged/CORN_MEAL_AGAR.yaml --workers
    1 --out REVIEW_WORK/batch066/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:004218
  command: just validate-terms data/merge_yaml/merged/CORN_MEAL_AGAR.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:004218
  command: just validate-references data/merge_yaml/merged/CORN_MEAL_AGAR.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CORN_MEAL_AGAR.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T12:09:39.509290Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: c7fc255ccc425575a494b834d7a9fdeb46b1ee706ad254fa8bdb6c95b490e925
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T12:09:39.509441Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: cd4239d4892d37c3b1c8e7a1ee3b310e616bcef37605adeeaadf2e0ed4577a8c
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/corn_meal_agar.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T12:09:39.509467Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: e9d140d6162916195a0764e063c59f700fa9a09f00e4586eac5255bef4642c95
- evidence_id: local3
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_25939.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T12:09:39.509489Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: b7c8c1e99a8dfc63b105713bad3c72eea91e5121046a26f17b49fee465ccd843
- evidence_id: local4
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_25945.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T12:09:39.509509Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: b5db1084455f89453854a863497c9f9e8d9bdeae0b7f51a71659005a15b0e53c
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch066/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T12:04:50.742267Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 60ba47f11bec7ecd7c1f127fbf365b972a12310318555403ba59613d2c3785a9
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch066/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T12:04:51.677727Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 8c508e78c12d61d8da8514b882f9c79fa58ddb2790b96dd96249b75533640c2d
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch066/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T12:04:53.101639Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 606db255f3eda1430db5dc87fbfd10f962604bd660b4f7acf050339f5cfe71e6
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch066/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T12:04:53.859977Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 439569c19a94433a0e6e048a31b2ae5c75cd30265427d65780b42e3889640f27
- evidence_id: dsmz191
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:05:41.027418Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1
- evidence_id: api191
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/191
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:05:40.935767Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87
- evidence_id: api12
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/12
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:05:40.877736Z'
  support: supports
  summary: 'Excluded comparison identity: current medium12 is SOIL EXTRACT MEDIUM,
    not selected DSM191 Corn Meal Agar. No recipe transfer; this resolves only the
    asserted KG-medium reference.'
  snapshot_sha256: aae1357e31d914ca483bea213eafb7d4a462aa252fc9008b483e42791202bd8b
- evidence_id: komodo191
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=191
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:05:40.804549Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: a3d36fcefda2951fb0291aaa6324fbfedf0c173819f5f693b0d6dda61ae12936
- evidence_id: komodo191_3
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=191.3
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:05:40.698766Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 986e718f92bc0d65eda3ad84d9a8e863d6c0c1eae13745788153356522bb3ab6
- evidence_id: komodo191_4
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=191.4
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:05:40.641090Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 91548054caedcfdea66e479e2e3c67485d3571b2933ca6c723b21410fb82b4d4
- evidence_id: strain25939
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=15416
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:05:40.607127Z'
  support: supports
  summary: Official collection catalogue identity, strain aliases, habitat and recommended-medium
    association read in full. This is collection guidance, not a primary experimental
    growth measurement or authentication of a different KOMODO recipe.
  snapshot_sha256: 75939a6abb71b12ac0af9e203e0bafd7e64f034f392e81633331ef3fcc827489
- evidence_id: strain25945
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=15415
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:05:40.564146Z'
  support: supports
  summary: Official collection catalogue identity, strain aliases, habitat and recommended-medium
    association read in full. This is collection guidance, not a primary experimental
    growth measurement or authentication of a different KOMODO recipe.
  snapshot_sha256: f630ac6bb9e53b01458a73094d84875eddb2574d71906aa42044fef4bb4da3ac
- evidence_id: tax490098
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=490098&retmode=xml
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:05:40.430831Z'
  support: supports
  summary: Current NCBI Taxonomy identifier, scientific name, aliases and lineage
    read; collection aliases are independently joined to the collection authority.
    No medium or growth assertion follows from taxonomy.
  snapshot_sha256: 38725eab1f31703eb8977dba3f6dc8769b09be3fdc28befc94f57cd75bed2f31
- evidence_id: tax493461
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=493461&retmode=xml
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T12:05:40.326885Z'
  support: supports
  summary: Current NCBI Taxonomy identifier, scientific name, aliases and lineage
    read; collection aliases are independently joined to the collection authority.
    No medium or growth assertion follows from taxonomy.
  snapshot_sha256: d211da78db9c56d856984c4880957b590bd6cf0a40c56b3ec9fea31e233d8c57
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T12:05:39.347056Z'
  support: supports
  summary: OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of
    polysaccharides extracted from species of red algae. Its two main components are
    agarose and agaropectin. Agarose is the component responsible for the high-strength
    gelling properties of agar, while agaropectin provides the viscous properties.'];
    formula None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch066/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T12:09:39.511237Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: f38def2feeeb931bebb9972ad4372d60b8b58e5444f0d4d6b05dd0d08cd0d11d
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/corn_meal_agar.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512113Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api191 raw bytes exactly match the cited historical SHA, and 4
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: c56c7427c041169799e00a317297a38a9c9ba8c405eaa49accbcc5d4a66807b6
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_25945.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512135Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api191 raw bytes exactly match the cited historical SHA, and 4
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 18217b8bd75f92c9af494c382f8ad845a112025cde9b55f85f9f2773287bdcf8
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512155Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api191 raw bytes exactly match the cited historical SHA, and 4
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 1f58a4b69dc60da18421cade2720227d15c90c05425346cdcab7a87d461274f3
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/for_dsm_25939.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512174Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api191 raw bytes exactly match the cited historical SHA, and 4
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 34c637dc33b072ee8979da6bc99c7e6e7b37369d3b56f0294a2e7e245feaf971
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_25945.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512192Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 2d2c11dfa4100ff7d1b20e2b8926c07fee632c570842518f1bdfe37cbd2ced22
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_25939.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512210Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 8d7d832f6036df03208cf682623ce28fc25997ce5b988d6623f3492560d2d4c9
- evidence_id: history6
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/corn_meal_agar.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512227Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: c06e6f3c37c5d1cc81e38cdd7b64cbd0f5b5bb308338e16bddd3bfdbc000ca42
- evidence_id: history7
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512244Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 8b97ef5ac9cc94e8aa85b93f4471d9f7dac9ba608cf028414ce8816d4c35c417
- evidence_id: history8
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/corn_meal_agar__edd1883a.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512262Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 630664e4c271af3ca9acd3743a55a71fd992ba4171f09df529316f2371d8bcee
- evidence_id: history9
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/corn_meal_agar__47c378f9.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512279Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 37c5cd81f166ccb21a9f9f543a573f5b22e49e3aab628c8cf2d954342a9e0463
- evidence_id: history10
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CORN_MEAL_AGAR.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T12:09:39.512296Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 190994583b5fffebc231c3a67c91af69d081f435103c306c832f8275672a179a
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch066/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T12:09:39.512316Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 679aa796bcd3eeaabd5e8af8ee86edfeb03246f987d18030dc2197e11b901064
- evidence_id: writer33
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: target_slot; groundable; apply_to_record
  accessed_at: '2026-10-28T12:09:39.512383Z'
  support: context_only
  summary: Current target_slot preserves existing CHEBI assertions; groundable excludes
    conflicting corpus opinions, and apply_to_record fills ungrounded entries from
    proposals. This writer does not authenticate source amounts or automatically repair
    an existing wrong supplied-form ID.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer34
  kind: record_content
  reference: scripts/assign_culturemech_ids.py
  locator: assign_ids; _assign_id_to_file
  accessed_at: '2026-10-28T12:09:39.512407Z'
  support: context_only
  summary: Current assign_ids selects records with missing IDs; _assign_id_to_file
    checks new-ID collisions and appends identifier provenance. Identifier assignment
    does not authenticate recipe content or demonstrate historical source access.
  snapshot_sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
- evidence_id: writer35
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T12:09:39.512429Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer36
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T12:09:39.512450Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer37
  kind: record_content
  reference: scripts/enrich_with_chebi.py
  locator: RecipeEnricher.enrich_ingredient; enrich_recipe; enrich_file
  accessed_at: '2026-10-28T12:09:39.512470Z'
  support: context_only
  summary: Current RecipeEnricher.enrich_ingredient skips already grounded entries
    and delegates missing-term mapping to ChemicalMapper; enrich_recipe traverses
    ingredient and solution structure, and enrich_file writes results and history.
    Only the read wrapper behavior is claimed here; the mapper is not treated as an
    independent supplied-form authority.
  snapshot_sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
- evidence_id: writer38
  kind: record_content
  reference: scripts/enrich_with_mediaingredientmech.py
  locator: main
  accessed_at: '2026-10-28T12:09:39.512489Z'
  support: context_only
  summary: Current main orchestrates a local or cloned MIM repository, its loader
    and ingredient linker. The CLI orchestration was read; it does not itself verify
    source recipe quantities, supplied chemical forms or the validity of historical
    MIM assertions. Linker internals are not claimed as separately audited scientific
    evidence.
  snapshot_sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
- evidence_id: writer39
  kind: record_content
  reference: scripts/migrate_chebi_regrounding.py
  locator: rewrite_entry; migrate_file
  accessed_at: '2026-10-28T12:09:39.512510Z'
  support: context_only
  summary: Current rewrite_entry applies configured exact-ID/label remaps across primary
    and secondary slots; migrate_file records applied changes. A successful current
    mapping operation does not establish source-specific hydrate or stereochemical
    equivalence.
  snapshot_sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
- evidence_id: writer40
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: _resolve_chebi; _rewrite_entry
  accessed_at: '2026-10-28T12:09:39.512530Z'
  support: context_only
  summary: Current _resolve_chebi reuses current primary CHEBI where available and
    considers bounded exact-name/synonym matches with a stereo-prefix guard; _rewrite_entry
    retains unresolved links. Current-row presence is distinct from historical validity
    and from source-specific supplied-form equivalence.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer41
  kind: record_content
  reference: scripts/migrate_ph_range.py
  locator: parse_ph_range; migrate_one
  accessed_at: '2026-10-28T12:09:39.512548Z'
  support: context_only
  summary: Current parse_ph_range retains qualifiers in notes and migrate_one converts
    only string-valued pH ranges, recording provenance. No particular source range
    is authenticated by this writer.
  snapshot_sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
- evidence_id: writer42
  kind: record_content
  reference: scripts/normalize_media_names_to_snake_case.py
  locator: process_file; add_curation_history
  accessed_at: '2026-10-28T12:09:39.512568Z'
  support: context_only
  summary: Current process_file preserves the original medium name while normalizing
    its machine name; add_curation_history appends a naming event. Name normalization
    does not prove equivalence of differently maintained source branches or recipe
    variants.
  snapshot_sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
- evidence_id: writer43
  kind: record_content
  reference: scripts/refill_term_labels.py
  locator: refill_text
  accessed_at: '2026-10-28T12:09:39.512588Z'
  support: context_only
  summary: Current refill_text replaces term labels using the current exact identifier
    lookup while preserving other text. Canonical label correspondence is not an independent
    choice of the correct chemical form for the supplied source reagent.
  snapshot_sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
- evidence_id: writer44
  kind: record_content
  reference: scripts/repair_komodo_corn_meal_score25.py
  locator: _corn_meal_recipe; TARGETS; CHILD_LINKS; _ensure_flags; _upsert_history;
    plan_repairs
  accessed_at: '2026-10-28T12:09:39.512610Z'
  support: context_only
  summary: Current _corn_meal_recipe and TARGETS hardcode the basal extraction recipe
    plus pH values for all five listed records; CHILD_LINKS assigns PH_VARIANT to
    the two selected strain wrappers. _ensure_flags removes unresolved flags and adds
    ingredients_curated. _upsert_history replaces a matching curator/action event,
    while plan_repairs also touches an unselected25720 sibling. This current fixed-input
    repair has no live strain/source authentication guard and is not safe evidence
    that the wrapper identities are correct. Review only the selected four owners;
    do not apply its broader plan automatically.
  snapshot_sha256: 64b5e39d4a5b086147c431846ed0a03a937a6a3c7020e2674cd4ec7a7964c8dd
- evidence_id: writer45
  kind: record_content
  reference: scripts/repair_komodo_strain_backlinks.py
  locator: PARENTS; CHILDREN; repair_parent; plan_repairs; _upsert_event
  accessed_at: '2026-10-28T12:09:39.512629Z'
  support: context_only
  summary: Current repair_parent and plan_repairs target only the explicitly listed
    131/777 parents and their two strain children. They do not repair the selected
    records. _upsert_event replaces a matching curator/action event or appends it;
    this existing behavior is not permission to rewrite history during this review.
  snapshot_sha256: 06d56149f4e8333f31ae6dd7e4b9127881227810bc957429c849ba00de21c963
- evidence_id: writer46
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T12:09:39.512647Z'
  support: context_only
  summary: Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS
    duplicate notes. This bounded repair is not a general solution for product decomposition,
    stock flattening or differing source formulations.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer47
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition; _is_placeholder; _add_enrichment_metadata
  accessed_at: '2026-10-28T12:09:39.512673Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients and
    solutions, fills pH when absent and copies physical/medium type, but does not
    copy preparation steps. _add_enrichment_metadata records a naive current timestamp.
    This explains a present omission risk, not historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer48
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T12:09:39.512694Z'
  support: context_only
  summary: Current _convert_to_culturemech constructs source notes and default LIQUID
    with empty ingredients. Its time.strftime format contains %f, which is unsupported
    here and is consistent with literal .fZ in stored import events. Current code
    does not authenticate the original retrieval or justify rewriting historical time.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer49
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-28T12:09:39.512724Z'
  support: context_only
  summary: Current _parse_api_composition considers the primary recipe, prefers provider
    g_l when available and excludes recognized solvents; _is_api_stock_addition distinguishes
    stock additions. _parse_api_solutions retains separate stock structure. _parse_preparation_steps
    collects solution prose. These present behaviors do not establish historical execution
    and cannot justify interpreting flattened stock rates as final-medium concentrations.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer50
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients; find_matches; find_exact_match
  accessed_at: '2026-10-28T12:09:39.512748Z'
  support: context_only
  summary: Current extract_recipe_ingredients collects asserted CHEBI/FOODON IDs,
    find_matches compares set Jaccard and find_exact_match selects the first exact
    identifier set. Quantities, preparation and ungrounded ingredients are not compared,
    so an exact set match does not establish formulation identity.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer51
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T12:09:39.512767Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer52
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T12:09:39.512787Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer53
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T12:09:39.512807Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer54
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: apply_defaults; _fix_ingredient; _fix_solution
  accessed_at: '2026-10-28T12:09:39.512829Z'
  support: context_only
  summary: Current apply_defaults, _fix_ingredient and _fix_solution can insert VARIABLE
    amounts and placeholder names for structural completeness. A default is not evidence
    for a dose, composition, solution identity or denominator; existing default-history
    events remain contextual.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch066/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T12:23:48.424210Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: ff41818856ea39ae0ee679ed5cf2bb18c98f401cf1e9a660b04d12bbd107817b
assessments:
- assessment_id: a1
  area: identity
  topic: Basal identity and independent strain wrappers
  outcome: concern
  summary: The exact DSM 191 primary/API identify Corn Meal Agar. JCM 15416 maps DSM
    25939 to Methanobacterium flexile GH, and JCM 15415 maps DSM 25945 to M. movens
    TS-2; NCBI 490098/493461 confirm archaeal species lineages. Their collection media
    differ from the local corn-meal wrapper identity. This establishes a material
    identity/variant review requirement, not a claim that experimental growth on corn
    meal is impossible. No collection condition or unrelated recipe is transferred.
  target_ids:
  - CultureMech:004218
  evidence_ids:
  - local0
  - dsmz191
  - api191
  - strain25939
  - strain25945
  - tax490098
  - tax493461
- assessment_id: a2
  area: consistency
  topic: Classification, atmosphere and formulation references
  outcome: concern
  summary: Basal complex/undefined agar classification is consistent with the source.
    The target Aerobic:No note lacks explicit primary support. The bacterial category
    on the strain wrappers is inconsistent with their independently resolved archaeal
    identities, while the generic basal medium is not recategorized solely from those
    wrappers. mediadive.medium:12 resolves to Soil Extract Medium rather than Corn
    Meal Agar.
  target_ids:
  - CultureMech:004218
  evidence_ids:
  - local0
  - api12
  - dsmz191
  - tax490098
  - tax493461
- assessment_id: a3
  area: grounding
  topic: Agar and provider compound identity
  outcome: supported
  summary: All ten selected agar primary/secondary slots match current CHEBI:2509
    and exact MIM CSV rows. The four owner corn-meal mediadive.compound:2087 slots
    exactly match API 191; the target has no corn-meal term. This provider identifier
    is not misrepresented as CHEBI or a pure-compound identity. No numeric legacy
    MIM identifiers occur.
  target_ids:
  - CultureMech:004218
  evidence_ids:
  - grounding
  - chebi2509
  - api191
- assessment_id: a4
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: All 11 exact selected-name reports were read, including two namesake commercial-media
    reports as explicitly excluded comparison context. Current API 191 raw bytes authenticate
    matching historical objects, not separate KOMODO catalogue bytes or access times.
    No selected layer has attached formulation evidence. The current corn-meal repair
    hardcodes variant pH/classification and replaces matching history events; its
    existing behavior is not permission to rewrite history or apply its unselected
    sibling plan. Current conservative merging preserves scientific fields and rejects
    incompatible formulations. Inspected writer behavior is described separately by
    exact file and function; it does not prove historical execution.
  target_ids:
  - CultureMech:004218
  evidence_ids:
  - history-auth
  - writer33
  - writer34
  - writer35
  - writer36
  - writer37
  - writer38
  - writer39
  - writer40
  - writer41
  - writer42
  - writer43
  - writer44
  - writer45
  - writer46
  - writer47
  - writer48
  - writer49
  - writer50
  - writer51
  - writer52
  - writer53
  - writer54
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 10 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:004218
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:004218",
    "selected_concentration_field_count": 10, "selected_concentration_fields_covered":
    10, "decisions": [{"decision_id": "q1", "subject": "Corn meal extraction input
    in generated target", "local_fields": [{"record_path": "data/merge_yaml/merged/CORN_MEAL_AGAR.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "50", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "Raw extraction input, not retained
    solute mass", "interpretation": "The primary uses 50 g raw corn meal, then filters
    the extract before making up to 1 L. The target drops the extraction/filtering
    context and presents 50 G_PER_L as an ordinary final ingredient. Preserve the
    raw-input basis and filtrate stage; the retained corn-meal mass is not quantified.",
    "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api191",
    "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256":
    "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256":
    "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at":
    "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Corn meal\",\n                        \"compound_id\":
    2087,\n                        \"amount\": 50,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 4-5", "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf",
    "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1",
    "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de",
    "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Blend 50.0
    g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator.\nHeat
    at 60C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat
    to", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2",
    "subject": "Corn meal input in repaired basal owners", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "50.0", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "50.0", "unit": "G_PER_L"}}],
    "decision": "evidence_only", "stage": "Raw material per litre of prepared extract",
    "interpretation": "Both current basal owners explicitly retain the extraction/filter/make-up
    notes. Their 50 G_PER_L is supportable only as raw input per litre of extract,
    not retained solid or dissolved corn-meal concentration. No attached claim-level
    evidence exists.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256":
    "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256":
    "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at":
    "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Corn meal\",\n                        \"compound_id\":
    2087,\n                        \"amount\": 50,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 4-5", "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf",
    "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1",
    "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de",
    "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Blend 50.0
    g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator.\nHeat
    at 60C for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat
    to", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3",
    "subject": "Agar in basal recipe", "local_fields": [{"record_path": "data/merge_yaml/merged/CORN_MEAL_AGAR.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "10", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "10.0", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "10.0", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "Added after extract is made
    up to 1 L", "interpretation": "The primary adds 10 g agar after the filtrate is
    made up to 1 L; API g_l = 10 supplies the corresponding nominal formulation basis.
    Retain 10 with this stage, without claiming a separately measured volume after
    agar dissolution. The historical blanket unsupported decisions do not negate this
    direct support.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key":
    "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256":
    "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256":
    "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at":
    "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\":
    29.7327,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz191",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf",
    "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1",
    "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de",
    "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Heat at 60C
    for one hour. Filter and make up volume to 1 l. Add 10.0 g agar and heat to",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject":
    "Unresolved strain-wrapper Corn meal", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "50.0", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "50.0", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Unverified variant/source identity",
    "interpretation": "The copied numbers reproduce the basal recipe, but current
    JCM identities resolve DSM 25939 and DSM 25945 to different methanogen species
    and neither catalogue supports these corn-meal variants. Exact KOMODO routes returned
    403. Basal agreement does not authenticate a strain-specific formulation or its
    pH; no replacement recipe is proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191",
    "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Corn meal\",\n                        \"compound_id\":
    2087,\n                        \"amount\": 50,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id":
    "q5", "subject": "Unresolved strain-wrapper Agar", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/for_dsm_25939.yaml", "field_path": "ingredients[1].concentration",
    "original": {"value": "10.0", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "10.0", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "Unverified variant/source identity",
    "interpretation": "The copied numbers reproduce the basal recipe, but current
    JCM identities resolve DSM 25939 and DSM 25945 to different methanogen species
    and neither catalogue supports these corn-meal variants. Exact KOMODO routes returned
    403. Basal agreement does not authenticate a strain-specific formulation or its
    pH; no replacement recipe is proposed.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191",
    "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\":
    29.7327,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q6", "subject": "Initial extraction water
    and overnight holding", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml",
    "field_path": "preparation_steps[0].description", "original": "Blend 50.0 g corn
    meal in 800 ml distilled water and leave overnight in the refrigerator."}, {"record_path":
    "data/normalized_yaml/bacterial/corn_meal_agar.yaml", "field_path": "preparation_steps[0].description",
    "original": "Blend 50.0 g corn meal in 800 ml distilled water and leave overnight
    in the refrigerator."}], "decision": "evidence_only", "stage": "Initial extraction,
    before filtering/make-up", "interpretation": "The current basal owners retain
    the exact initial 800 ml and overnight refrigerator step; the generated target
    omits it. The primary gives no numerical refrigerator temperature or overnight
    duration. Do not replace this with1000 ml added at the start merely because API
    lists total water 1000 ml.", "sources": [{"locator": "extracted-text lines 4-4",
    "source_key": "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf",
    "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1",
    "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de",
    "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Blend 50.0
    g corn meal in 800 ml of distilled water. Leave overnight in the refrigerator.",
    "quote_representation": "captured extracted text"}, {"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191",
    "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q7", "subject": "Extraction heating", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml",
    "field_path": "preparation_steps[1].description", "original": "Heat at 60 C for
    one hour."}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml",
    "field_path": "preparation_steps[1].description", "original": "Heat at 60 C for
    one hour."}], "decision": "evidence_only", "stage": "Before filtration", "interpretation":
    "Retain the source 60 degrees C for one hour already in the basal owners; missing
    from generated target. These are extraction conditions, not organism growth claims.",
    "sources": [{"locator": "extracted-text lines 5-5", "source_key": "dsmz191", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256":
    "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256":
    "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at":
    "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Heat at 60C for one hour.
    Filter and make up volume to 1 l. Add 10.0 g agar and heat to", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q8", "subject": "Filtration and
    make-up", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml",
    "field_path": "preparation_steps[2].description", "original": "Filter and bring
    the volume to 1 L."}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml",
    "field_path": "preparation_steps[2].description", "original": "Filter and bring
    the volume to 1 L."}], "decision": "evidence_only", "stage": "Filtered extract
    volume", "interpretation": "Explicit make-up to 1 L supports the extract-volume
    basis. It does not establish complete retention of the starting 50 g corn meal.",
    "sources": [{"locator": "extracted-text lines 5-5", "source_key": "dsmz191", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256":
    "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256":
    "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at":
    "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Heat at 60C for one hour.
    Filter and make up volume to 1 l. Add 10.0 g agar and heat to", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q9", "subject": "Agar dissolution
    and autoclaving", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml",
    "field_path": "preparation_steps[3].description", "original": "Add 10.0 g agar
    and heat to dissolve."}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml",
    "field_path": "preparation_steps[3].description", "original": "Add 10.0 g agar
    and heat to dissolve."}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml",
    "field_path": "preparation_steps[4].description", "original": "Autoclave the completed
    corn meal agar."}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml",
    "field_path": "preparation_steps[4].description", "original": "Autoclave the completed
    corn meal agar."}], "decision": "evidence_only", "stage": "After extract make-up",
    "interpretation": "Current basal owners retain the correct ordering and general
    autoclaving. The primary gives no sterilization temperature or duration; API adds
    121 degrees C / 15 minutes. Those additional provider controls may be recorded
    only with their distinct source attribution, not quoted as primary PDF text.",
    "sources": [{"locator": "extracted-text lines 5-5", "source_key": "dsmz191", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf", "source_raw_sha256":
    "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1", "source_text_sha256":
    "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de", "accessed_at":
    "2026-10-28T12:05:41.027418Z", "exact_source_quote": "Heat at 60C for one hour.
    Filter and make up volume to 1 l. Add 10.0 g agar and heat to", "quote_representation":
    "captured extracted text"}, {"locator": "extracted-text lines 6-6", "source_key":
    "dsmz191", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf",
    "source_raw_sha256": "61201760e37daa66583e3f95098ff55d274bcd8bd3c8166691ffef2ac60e8ca1",
    "source_text_sha256": "b6a933d64ac8f4c13748e109abba624c5fa5d615395686fafcfdb722d39301de",
    "accessed_at": "2026-10-28T12:05:41.027418Z", "exact_source_quote": "dissolve,
    then autoclave.", "quote_representation": "captured extracted text"}, {"locator":
    "$.data.solutions[0].steps[0]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191",
    "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"step\":
    \"Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the
    refrigerator. Heat at 60\\u00b0C for one hour. Filter and make up volume to 1
    l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\\u00b0C for 15
    minutes. pH 6.0.\"\n                    }", "quote_representation": "raw JSON
    object"}]}, {"decision_id": "q10", "subject": "Basal pH", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CORN_MEAL_AGAR.yaml", "field_path": "ph_value", "original":
    6.0}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml",
    "field_path": "ph_value", "original": 6.0}, {"record_path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml",
    "field_path": "ph_value", "original": 6.0}], "decision": "evidence_only", "stage":
    "Provider metadata/control", "interpretation": "Target and basal owners pH6 agree
    with current API min_pH/max_pH and preparation, while the PDF does not specify
    pH. Retain provider-scoped evidence rather than claiming PDF support.", "sources":
    [{"locator": "$.data.medium", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191",
    "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n            \"id\":
    191,\n            \"name\": \"CORN MEAL AGAR\",\n            \"complex_medium\":
    \"yes\",\n            \"min_pH\": 6,\n            \"max_pH\": 6,\n            \"source\":
    \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf\"\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191",
    "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"step\":
    \"Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the
    refrigerator. Heat at 60\\u00b0C for one hour. Filter and make up volume to 1
    l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\\u00b0C for 15
    minutes. pH 6.0.\"\n                    }", "quote_representation": "raw JSON
    object"}]}, {"decision_id": "q11", "subject": "Wrapper pH and preparation scope",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml",
    "field_path": "ph_value", "original": 7.2}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml",
    "field_path": "preparation_steps[0].description", "original": "Blend 50.0 g corn
    meal in 800 ml distilled water and leave overnight in the refrigerator."}, {"record_path":
    "data/normalized_yaml/bacterial/for_dsm_25939.yaml", "field_path": "preparation_steps[1].description",
    "original": "Heat at 60 C for one hour."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml",
    "field_path": "preparation_steps[2].description", "original": "Filter and bring
    the volume to 1 L."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml",
    "field_path": "preparation_steps[3].description", "original": "Add 10.0 g agar
    and heat to dissolve."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25939.yaml",
    "field_path": "preparation_steps[4].description", "original": "Autoclave the completed
    corn meal agar."}], "decision": "unsupported", "stage": "Variant identity unresolved",
    "interpretation": "The old catalogue excerpt reports this pH and the current repair
    copies basal preparation. Those derivative rows and copied steps do not independently
    authenticate use of corn-meal agar for the exact methanogen strain. Retain unresolved
    claims without transferring collection growth conditions or supplying a replacement
    formulation.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256":
    "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256":
    "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at":
    "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"step\":
    \"Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the
    refrigerator. Heat at 60\\u00b0C for one hour. Filter and make up volume to 1
    l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\\u00b0C for 15
    minutes. pH 6.0.\"\n                    }", "quote_representation": "raw JSON
    object"}]}, {"decision_id": "q12", "subject": "Wrapper pH and preparation scope",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml",
    "field_path": "ph_value", "original": 7.4}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml",
    "field_path": "preparation_steps[0].description", "original": "Blend 50.0 g corn
    meal in 800 ml distilled water and leave overnight in the refrigerator."}, {"record_path":
    "data/normalized_yaml/bacterial/for_dsm_25945.yaml", "field_path": "preparation_steps[1].description",
    "original": "Heat at 60 C for one hour."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml",
    "field_path": "preparation_steps[2].description", "original": "Filter and bring
    the volume to 1 L."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml",
    "field_path": "preparation_steps[3].description", "original": "Add 10.0 g agar
    and heat to dissolve."}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_25945.yaml",
    "field_path": "preparation_steps[4].description", "original": "Autoclave the completed
    corn meal agar."}], "decision": "unsupported", "stage": "Variant identity unresolved",
    "interpretation": "The old catalogue excerpt reports this pH and the current repair
    copies basal preparation. Those derivative rows and copied steps do not independently
    authenticate use of corn-meal agar for the exact methanogen strain. Retain unresolved
    claims without transferring collection growth conditions or supplying a replacement
    formulation.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key":
    "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191", "source_raw_sha256":
    "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "source_text_sha256":
    "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87", "accessed_at":
    "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"step\":
    \"Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the
    refrigerator. Heat at 60\\u00b0C for one hour. Filter and make up volume to 1
    l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\\u00b0C for 15
    minutes. pH 6.0.\"\n                    }", "quote_representation": "raw JSON
    object"}]}, {"decision_id": "q13", "subject": "Provider-only sterilization settings",
    "local_fields": [], "decision": "evidence_only", "stage": "Additional provider
    preparation context", "interpretation": "The API explicitly adds 121 degrees C
    for 15 minutes; the primary says only autoclave. This source difference must remain
    visible and is not a silently inferred primary prescription.", "sources": [{"locator":
    "$.data.solutions[0].steps[0]", "source_key": "api191", "reference": "https://mediadive.dsmz.de/rest/medium/191",
    "source_raw_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "source_text_sha256": "026776f8e80280cead09152fe12fa23f78abb1e4a4b89435e39a74870832ee87",
    "accessed_at": "2026-10-28T12:05:40.935767Z", "exact_source_quote": "{\n                        \"step\":
    \"Blend 50.0 g corn meal in 800 ml of distilled water. Leave overnight in the
    refrigerator. Heat at 60\\u00b0C for one hour. Filter and make up volume to 1
    l. Add 10.0 g agar and heat to dissolve, then autoclave at 121\\u00b0C for 15
    minutes. pH 6.0.\"\n                    }", "quote_representation": "raw JSON
    object"}]}], "local_field_census_reference": "REVIEW_WORK/batch066/record04/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: supported
  summary: 'data/merge_yaml/merged/CORN_MEAL_AGAR.yaml: primary 1/2, secondary 1/2;
    data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml: primary 2/2, secondary
    1/2; data/normalized_yaml/bacterial/corn_meal_agar.yaml: primary 2/2, secondary
    1/2; data/normalized_yaml/bacterial/for_dsm_25939.yaml: primary 2/2, secondary
    1/2; data/normalized_yaml/bacterial/for_dsm_25945.yaml: primary 2/2, secondary
    1/2. These are ingredient-instance linkage fractions, not accuracy scores. Solution
    terms are audited separately. Every actually asserted CHEBI term is joined to
    its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech
    mentions occur across the complete selected documents, with exact locators in
    the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product
    components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:004218
  evidence_ids:
  - grounding
- assessment_id: a7
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and exact maintained owners reviewed. Dependencies
    transfer only their explicitly named stock subsection; unrelated parent media
    and source prescriptions are not growth evidence.
  target_ids:
  - CultureMech:004218
  evidence_ids:
  - local0
- assessment_id: a8
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:004218
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-004218-extraction-stage-and-generated-preparation-loss
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Corn-meal extraction and preparation context are missing from generated content
  description: The target lists 50 G_PER_L corn meal without the extraction/filter
    stage and omits all five preparation steps now retained by its basal owners. 50
    g is raw extraction input; recovered solute/solid mass is unquantified. The agar
    rate is supported on the defined extract basis. Current repaired owners and conservative
    merge safeguards are credited; this old target is stale.
  target_ids:
  - CultureMech:004218
  field_paths:
  - ingredients[0].concentration
  - ingredients[0].notes
  - preparation_steps
  - sterilization
  - evidence
  evidence_ids:
  - dsmz191
  - api191
  - local0
  - local1
  - local2
  rule_id: review-ingredient-concentrations/extraction-stage
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/corn_meal_agar.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25939.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25945.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-004218-unverified-methanogen-wrapper-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Named strain wrappers are not authenticated corn-meal pH variants
  description: The two selected wrappers resolve to distinct Methanobacterium species.
    Their copied basal formulation and pH values are not established by the generic
    DSM 191 source. The generated target still merges them as SOURCE_DUPLICATE although
    the maintained repair labels them PH_VARIANT. Both relationship claims need exact
    variant evidence, and wrapper bacterial categories require reconsideration against
    their archaeal identities.
  target_ids:
  - CultureMech:004218
  field_paths:
  - merged_from
  - synonyms
  - variant_children
  - data/normalized_yaml/bacterial/for_dsm_25939.yaml::parent_media
  - data/normalized_yaml/bacterial/for_dsm_25945.yaml::parent_media
  - data/normalized_yaml/bacterial/for_dsm_25939.yaml::variant_relationship
  - data/normalized_yaml/bacterial/for_dsm_25945.yaml::variant_relationship
  - data/normalized_yaml/bacterial/for_dsm_25939.yaml::category
  - data/normalized_yaml/bacterial/for_dsm_25945.yaml::category
  - data/normalized_yaml/bacterial/for_dsm_25939.yaml::ph_value
  - data/normalized_yaml/bacterial/for_dsm_25945.yaml::ph_value
  evidence_ids:
  - strain25939
  - strain25945
  - tax490098
  - tax493461
  - komodo191_3
  - komodo191_4
  - local3
  - local4
  rule_id: review-yaml-record/source-variant-identity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/corn_meal_agar.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25939.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25945.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-004218-kg-reference-points-to-soil-extract
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The KG medium link resolves to a different recipe identity
  description: All five selected documents assert mediadive.medium:12, which current
    MediaDive identifies as SOIL EXTRACT MEDIUM. The selected basal identity is DSM
    191. The current KG matcher compares ingredient identifier sets and cannot establish
    recipe identity; no automatic replacement is inferred for the unresolved strain
    wrappers.
  target_ids:
  - CultureMech:004218
  field_paths:
  - data/merge_yaml/merged/CORN_MEAL_AGAR.yaml::kg_microbe_match
  - data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml::kg_microbe_match
  - data/normalized_yaml/bacterial/corn_meal_agar.yaml::kg_microbe_match
  - data/normalized_yaml/bacterial/for_dsm_25939.yaml::kg_microbe_match
  - data/normalized_yaml/bacterial/for_dsm_25945.yaml::kg_microbe_match
  evidence_ids:
  - api12
  - api191
  - local0
  rule_id: review-yaml-record/exact-source-reference
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/corn_meal_agar.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25939.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25945.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-004218-import-provenance-and-unsupported-atmosphere
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Imported atmosphere and history require bounded provenance repair
  description: The target retains Aerobic:No without explicit primary support; the
    repaired owners already omit that inherited note. Target and KOMODO-derived owners
    preserve malformed literal .fZ import times and naive resolver times. Current
    importer formatting and resolver behavior explain present risks, not authenticated
    historical execution.
  target_ids:
  - CultureMech:004218
  field_paths:
  - notes
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  - data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_25939.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_25945.yaml::curation_history[0].timestamp
  evidence_ids:
  - local0
  - local1
  - dsmz191
  rule_id: review-yaml-record/provenance-traceability
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/corn_meal_agar.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25939.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25945.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Preserve the source raw-input and filtered-extract stages, retain the
    correct basal owner steps and attach narrow ingredient/root evidence. Regenerate
    only after resolving the strain-wrapper ownership issue; do not infer a retained
    corn-meal concentration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:004218
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/corn_meal_agar.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25939.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25945.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action2
  description: Resolve each exact wrapper accession and strain identity independently.
    Withhold unsupported duplicate/pH-variant and growth claims; do not transplant
    a methanogen recipe into the basal Corn Meal Agar record. Review the hardcoded
    current repair and affected relationships before any future regeneration; keep
    unselected DSM 25720 outside this review.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:004218
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/corn_meal_agar.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25939.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25945.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action3
  description: Reconcile each selected KG link against exact source identity; retain
    or remove unresolved linkage rather than accepting set similarity as recipe equivalence.
    Verify the basal 191 candidate separately and avoid transferring it to unverified
    variants.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:004218
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/corn_meal_agar.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25939.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25945.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action4
  description: Keep original events unchanged. Correct future timestamp formatting
    and append a verified current-date context event; do not invent historical times.
    Remove or qualify the unsupported generated atmosphere note while preserving any
    genuinely supported source claim.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:004218
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/corn_meal_agar.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25939.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_25945.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
limitations:
- All three exact current KOMODO routes returned HTTP 403; historical catalogue snippets
  remain derivative, separate from the authenticated API 191 payload.
- DSM 191 PDF and API differ in additional provider pH/sterilization details. Extract
  make-up to 1 L is explicit; retained corn-meal mass and post-agar measured final
  volume are not.
- The unselected DSM 25720 sibling and two same-label commercial-media reports are
  context only; no formulation, category or growth assessment transfers to them. Current
  collection identity is not an experimental growth claim.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
