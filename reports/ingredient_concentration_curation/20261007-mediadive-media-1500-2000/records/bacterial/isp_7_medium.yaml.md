# Medium Concentration Review: ISP 7 MEDIUM

- Record: data/normalized_yaml/bacterial/isp_7_medium.yaml
- ID: CultureMech:001099
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0baff82eba6ee2c9318db2a4104840352d13e490992ca3f8da1507c09a303672`
- Proposed/result SHA256: `0baff82eba6ee2c9318db2a4104840352d13e490992ca3f8da1507c09a303672`
- Source: https://mediadive.dsmz.de/rest/medium/1619
- Source SHA256: 9ab64cba0c4f8aefb87f3840106805fafb9fc34685a48c8d47f2226d56ad7a51
- Retrieved: 2026-10-07T13:44:27.560083+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | ISP 7 Medium (Himedia) | {"unit": "G_PER_L", "value": "23.74"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1619 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Glycerol | {"unit": "ML_PER_L", "value": "15.00"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1619 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000.00"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1619 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | ISP 7 Medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1619 | {<br>                        "recipe_order": 1,<br>                        "compound": "ISP 7 Medium",<br>                        "compound_id": 1467,<br>                        "attribute": "Himedia",<br>                        "amount": 23.74,<br>                        "unit": "g",<br>                        "g_l": 23.74,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Glycerol | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1619 | {<br>                        "recipe_order": 2,<br>                        "compound": "Glycerol",<br>                        "compound_id": 72,<br>                        "amount": 15,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1619 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
