# Medium Concentration Review: MAIZE MEAL-SARDINE AGAR

- Record: data/normalized_yaml/bacterial/maize_meal_sardine_agar.yaml
- ID: CultureMech:002237
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5cd83d251f986fb951ca510d7918397e6503dcd7c56ce1a24844bb6f35e1d0cd`
- Proposed/result SHA256: `5cd83d251f986fb951ca510d7918397e6503dcd7c56ce1a24844bb6f35e1d0cd`
- Source: https://mediadive.dsmz.de/rest/medium/J1054
- Source SHA256: e086decaca7676cd9c48aa70a3456eec33e55c17ca09121a3698f080534b641b
- Retrieved: 2026-10-07T15:18:40.514707+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Maize meal | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1054 | {<br>                        "recipe_order": 1,<br>                        "compound": "Maize meal",<br>                        "compound_id": 1985,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Small dried sardine | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1054 | {<br>                        "recipe_order": 2,<br>                        "compound": "Small dried sardine",<br>                        "compound_id": 1986,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1054 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 59.4654,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[3].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1054 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1054 | {<br>                        "step": "Boil maize meal and dried sardine with 500 ml of distilled water for 20 min. Filtered through cloth, make up to 1 L, add agar, and boil till dissolved."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
