# Solution Concentration Review: Main sol. 1193

- Record: data/normalized_yaml/bacterial/mediadive_2381_Main_sol_1193.yaml
- ID: CultureMech:011760
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `fbb043f9dbf8b7c8e9d1266342e94853fcc652e4dc1eef5dd38599feccbbba5f`
- Proposed/result SHA256: `fbb043f9dbf8b7c8e9d1266342e94853fcc652e4dc1eef5dd38599feccbbba5f`
- Source: https://mediadive.dsmz.de/rest/solution/2381
- Source SHA256: 241f24456316a6cc04535e162ae945f268c028d5edaae24bede6b4ed2ef95730
- Retrieved: 2026-10-07T09:12:01.381281+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | IMDM-Medium | {"unit": "PERCENT_V_V", "value": "900.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2381 | {<br>                "recipe_order": 1,<br>                "compound": "IMDM-Medium",<br>                "compound_id": 1069,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 45,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1069) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Fetal bovine serum | {"unit": "PERCENT_V_V", "value": "100.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2381 | {<br>                "recipe_order": 2,<br>                "compound": "Fetal bovine serum",<br>                "compound_id": 954,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=954) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Aminoacids | {"unit": "PERCENT_V_V", "value": "10.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2381 | {<br>                "recipe_order": 3,<br>                "compound": "Aminoacids",<br>                "compound_id": 1070,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "100 x",<br>                "amount": 0.5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=1070) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
