# Water Input Follow-up: CultureMech:012540

- Follow-up target: data/normalized_yaml/bacterial/mediadive_33_Trace_element_solution_SL-12_B.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: ecfa5f6538b1cb26e2eb1fd2ef7110adc2637795f1258b2272c2177288e5439d
- Result SHA256: e43b7120771253b647527e8fdaf3bd061b58c614423633c06e5ebb5591c6039a
- Source SHA256: 00943ba24b7945caa7b4d9ce1748a3fb5bf9e52ac2b2a2790633784f30b1bfb3
- Source accessed: 2026-10-07T08:19:32.422759+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[9].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/33 | {<br>                "recipe_order": 10,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[9] (compound_id=4) | Concentration evidence for composition[9].concentration (Distilled water) in MediaDive solution 33; locator=$.data.recipe[9] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:19:32.422759+00:00; response SHA256=00943ba24b7945caa7b4d9ce1748a3fb5bf9e52ac2b2a2790633784f30b1bfb3. |
