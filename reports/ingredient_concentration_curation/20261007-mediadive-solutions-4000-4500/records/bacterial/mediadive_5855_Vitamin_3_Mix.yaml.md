# Solution Concentration Review: Vitamin 3 Mix

- Record: data/normalized_yaml/bacterial/mediadive_5855_Vitamin_3_Mix.yaml
- ID: CultureMech:014672
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5571d165e3c74b50093e42593cf498d7c0741f65dfefd9e205a9fe1a8e742132`
- Proposed/result SHA256: `5571d165e3c74b50093e42593cf498d7c0741f65dfefd9e205a9fe1a8e742132`
- Source: https://mediadive.dsmz.de/rest/solution/5855
- Source SHA256: e361a0b564da738ae6197d52c460ea46550f2bd4b88ee87d4e8ed664f02fc11b
- Retrieved: 2026-10-07T09:58:42.609980+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Thiamine HCl | {"unit": "PERCENT_V_V", "value": "10.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5855 | {<br>                "recipe_order": 1,<br>                "compound": "Thiamine HCl",<br>                "compound_id": 1207,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10 g/l stock solution",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1207) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | D-Biotin | {"unit": "PERCENT_V_V", "value": "1.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5855 | {<br>                "recipe_order": 2,<br>                "compound": "D-Biotin",<br>                "compound_id": 879,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.5 g/l stock solution",<br>                "amount": 0.1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=879) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Vitamin B12 | {"unit": "PERCENT_V_V", "value": "2.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5855 | {<br>                "recipe_order": 3,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "",<br>                "attribute": "0.2 g/l stock solution",<br>                "amount": 0.25,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=18) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
