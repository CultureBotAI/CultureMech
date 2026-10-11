# Medium Concentration Review: PBY MEDIUM

- Record: data/normalized_yaml/bacterial/pby_medium.yaml
- ID: CultureMech:002553
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `387c671af4b1f6a9428ec2c83cec84be6baba5a61cc88dccc7a2e68a64596e69`
- Proposed/result SHA256: `387c671af4b1f6a9428ec2c83cec84be6baba5a61cc88dccc7a2e68a64596e69`
- Source: https://mediadive.dsmz.de/rest/medium/J191
- Source SHA256: 4c59c01e3f3d94c41ab18f2fc5051052d8701788b1e739f3d3f4e75c6c8d8932
- Retrieved: 2026-10-07T14:03:12.676129+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Bacto peptone | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J191 | {<br>                        "recipe_order": 1,<br>                        "compound": "Bacto peptone",<br>                        "compound_id": 19,<br>                        "attribute": "BD-Difco",<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[1].concentration` | Beef extract | {"unit": "G_PER_L", "value": "3.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J191 | {<br>                        "recipe_order": 2,<br>                        "compound": "Beef extract",<br>                        "compound_id": 85,<br>                        "attribute": "BD-Difco",<br>                        "amount": 3,<br>                        "unit": "g",<br>                        "g_l": 3,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[2].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J191 | {<br>                        "recipe_order": 3,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "BD-Difco",<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "g_l": 1,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Optional addition or source attribute needs separate formulation/stock-strength review. | unchanged |
| `ingredients[3].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J191 | {<br>                        "recipe_order": 4,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J191 | {<br>                        "step": "Adjust pH to 7.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
