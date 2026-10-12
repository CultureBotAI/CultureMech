# Medium Concentration Review: TRYPTICASE SOY AGAR WITH 1% GLUCOSE

- Record: data/normalized_yaml/bacterial/trypticase_soy_agar_with_1_glucose.yaml
- ID: CultureMech:003025
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5839901b5f57e0b61a5432d0b89abb7a186080f943c5ced3d25c98073f4a6254`
- Proposed/result SHA256: `5839901b5f57e0b61a5432d0b89abb7a186080f943c5ced3d25c98073f4a6254`
- Source: https://mediadive.dsmz.de/rest/medium/J67
- Source SHA256: 6a86ca891fdb306e66e73c94b1161f840de404cdf64a1b3aa50bdfd2885c181b
- Retrieved: 2026-10-07T14:01:36.507165+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Pancreatic digest of casein | {"unit": "G_PER_L", "value": "17.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J67 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Peptic digest of soybean meal | {"unit": "G_PER_L", "value": "3.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J67 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Glucose | {"unit": "G_PER_L", "value": "2.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J67 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Sodium chloride | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J67 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Dipotassium phosphate | {"unit": "G_PER_L", "value": "2.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J67 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J67 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | Glucose | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J67 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Trypticase soy agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J67 | {<br>                        "recipe_order": 1,<br>                        "compound": "Trypticase soy agar",<br>                        "compound_id": 1617,<br>                        "attribute": "see Medium No. 75",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J67 | {<br>                        "recipe_order": 2,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "mmol_l": 55.5062,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
