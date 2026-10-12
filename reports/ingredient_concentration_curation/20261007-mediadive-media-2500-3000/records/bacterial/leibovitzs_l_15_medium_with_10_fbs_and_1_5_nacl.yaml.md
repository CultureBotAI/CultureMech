# Medium Concentration Review: LEIBOVITZ'S L-15 MEDIUM WITH 10% FBS AND 1.5% NaCl

- Record: data/normalized_yaml/bacterial/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml
- ID: CultureMech:003278
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `60d212c13858445c4b511ce5f1beeeff7370d89282c5c29ceed4f681acdcd015`
- Proposed/result SHA256: `60d212c13858445c4b511ce5f1beeeff7370d89282c5c29ceed4f681acdcd015`
- Source: https://mediadive.dsmz.de/rest/medium/J930
- Source SHA256: 332169eb2e5cf3aa4908fcbe8c23dd08e62411e0f34ba46c23928b68ed6d84ac
- Retrieved: 2026-10-07T14:41:28.668407+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Leibovitz's L-15 medium | {"unit": "L", "value": "1.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J930 | {<br>                        "recipe_order": 1,<br>                        "compound": "Leibovitz's L-15 medium",<br>                        "compound_id": 1941,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Fetal bovine serum | {"unit": "ML_PER_L", "value": "100.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J930 | {<br>                        "recipe_order": 2,<br>                        "compound": "Fetal bovine serum",<br>                        "compound_id": 954,<br>                        "amount": 100,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[2].concentration` | NaCl | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J930 | {<br>                        "recipe_order": 3,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 13.6364,<br>                        "mmol_l": 233.34,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `variant_children[0]` | leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl | {"id": "CultureMech:010402", "name": "leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl", "notes": "TOGO M976 imports the same JCM Medium 930 Leibovitz L-15 with 10% FBS and 1.5% NaCl formulation represented by MediaDive J930.", "path": "data/normalized_yaml/bacterial/TOGO_M976_Leibovitz_s_L-15_Medium_With_10_FBS_And_1.5_NaCl.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J930 | {<br>                        "step": "Filter-sterilize with 0.22 \u00ef\u00bf\u00bdm PES filter."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
