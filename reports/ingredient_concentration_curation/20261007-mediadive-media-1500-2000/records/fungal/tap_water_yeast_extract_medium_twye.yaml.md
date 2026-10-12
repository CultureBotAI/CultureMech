# Medium Concentration Review: TAP WATER YEAST EXTRACT MEDIUM (TWYE)

- Record: data/normalized_yaml/fungal/tap_water_yeast_extract_medium_twye.yaml
- ID: CultureMech:010456
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6c0e6a688ce1572cf5b1126bc8314205ff792979a0b15b7719e02dc8f4458419`
- Proposed/result SHA256: `6c0e6a688ce1572cf5b1126bc8314205ff792979a0b15b7719e02dc8f4458419`
- Source: https://mediadive.dsmz.de/rest/medium/1625
- Source SHA256: 10f0575b6d1496cc2ba273e30ff9d49aab21d72cb29aa5ed878523fd725ced22
- Retrieved: 2026-10-07T13:44:32.965252+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.25"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "18"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Tap water | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1625 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1625 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 0.25,<br>                        "unit": "g",<br>                        "g_l": 0.25,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | K2HPO4 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1625 | {<br>                        "recipe_order": 2,<br>                        "compound": "K2HPO4",<br>                        "compound_id": 10,<br>                        "amount": 0.5,<br>                        "unit": "g",<br>                        "g_l": 0.5,<br>                        "mmol_l": 2.87066,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1625 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 18,<br>                        "unit": "g",<br>                        "g_l": 18,<br>                        "mmol_l": 53.5189,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Tap water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1625 | {<br>                        "recipe_order": 4,<br>                        "compound": "Tap water",<br>                        "compound_id": 322,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
