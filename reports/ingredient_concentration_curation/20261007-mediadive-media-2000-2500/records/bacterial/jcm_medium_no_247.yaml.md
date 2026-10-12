# Medium Concentration Review: JCM MEDIUM No. 247

- Record: data/normalized_yaml/bacterial/jcm_medium_no_247.yaml
- ID: CultureMech:002608
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `81eed590822380330098a7e602024b067b4d5593fddb9fdcf79f5f8f9b3daf72`
- Proposed/result SHA256: `81eed590822380330098a7e602024b067b4d5593fddb9fdcf79f5f8f9b3daf72`
- Source: https://mediadive.dsmz.de/rest/medium/J247
- Source SHA256: 12d9048aa043984e074e7b5a1754ef470a0181123c71b0da18a6490f176f25c1
- Retrieved: 2026-10-07T14:03:57.387098+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J247 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Glucose | {"unit": "G_PER_L", "value": "20.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J247 | {<br>                        "recipe_order": 2,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 111.012,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J247 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J247 | {<br>                        "step": "pH 6.8-7.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
