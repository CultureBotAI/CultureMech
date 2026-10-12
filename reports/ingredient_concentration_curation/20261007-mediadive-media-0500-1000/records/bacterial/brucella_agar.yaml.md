# Medium Concentration Review: BRUCELLA AGAR

- Record: data/normalized_yaml/bacterial/brucella_agar.yaml
- ID: CultureMech:001710
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c6acdb25379a635738235c5353b191bd7fffade7ecd6699a4bc0489c51b19104`
- Proposed/result SHA256: `c6acdb25379a635738235c5353b191bd7fffade7ecd6699a4bc0489c51b19104`
- Source: https://mediadive.dsmz.de/rest/medium/584
- Source SHA256: 34baa940ed6d75704c2470f5aa0ed3e28137964edf52976bda03afb0987f57ec
- Retrieved: 2026-10-07T12:15:57.932579+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Brucella agar | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/584 | {<br>                        "recipe_order": 1,<br>                        "compound": "Brucella agar",<br>                        "compound_id": 1854,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Sheep blood | {"unit": "ML_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/584 | {<br>                        "recipe_order": 2,<br>                        "compound": "Sheep blood",<br>                        "compound_id": 2047,<br>                        "amount": 100,<br>                        "unit": "ml/l",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/584 | {<br>                        "step": "Prepare Brucella agar (e.g. Merck). Cool to 50\u00b0C after autoclaving, then add 100 ml/l sheep blood."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
