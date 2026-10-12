# Medium Concentration Review: NUTRIENT AGAR WITH 0.05% YEAST EXTRACT AND 3% NaCl

- Record: data/normalized_yaml/fungal/nutrient_agar_with_0_05_yeast_extract_and_3_nacl.yaml
- ID: CultureMech:010490
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f1ca09038e7bd51e85af251f18f22793b2bd0cb885a46d5ba4e78eb6690ed9b6`
- Proposed/result SHA256: `f1ca09038e7bd51e85af251f18f22793b2bd0cb885a46d5ba4e78eb6690ed9b6`
- Source: https://mediadive.dsmz.de/rest/medium/J1109
- Source SHA256: 29a7c9313ed4163990bcfff91141b4d1095c62b1b179b4ddad348a981e739fb1
- Retrieved: 2026-10-07T15:19:27.028962+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Agar | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1109 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1109 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | NaCl | {"unit": "G_PER_L", "value": "30"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1109 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1109 | {<br>                        "recipe_order": 1,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "attribute": "see Medium No. 74",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1109 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "BD-Difco",<br>                        "amount": 0.5,<br>                        "unit": "g",<br>                        "g_l": 0.5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1109 | {<br>                        "recipe_order": 3,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 30,<br>                        "unit": "g",<br>                        "g_l": 30,<br>                        "mmol_l": 513.347,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
