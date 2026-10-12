# Solution Concentration Review: Mail sol. C91

- Record: data/normalized_yaml/bacterial/mediadive_6229_Mail_sol_C91.yaml
- ID: CultureMech:014922
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8387f5f0bbf46878a6484c27a87ae6cb01ab2105f56886ff7d5988d7d00e5dec`
- Proposed/result SHA256: `8387f5f0bbf46878a6484c27a87ae6cb01ab2105f56886ff7d5988d7d00e5dec`
- Source: https://mediadive.dsmz.de/rest/solution/6229
- Source SHA256: d874176393be3f49bf2eb8a8a41f783f7f43aa845d6a36e317c0bb575bcd8201
- Retrieved: 2026-10-07T10:01:30.068355+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Soil | {"unit": "G_PER_L", "value": "159.091"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6229 | {<br>                "recipe_order": 2,<br>                "compound": "Soil",<br>                "compound_id": 2350,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "air\u00addried, sieved",<br>                "amount": 105,<br>                "unit": "g",<br>                "g_l": 159.091,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2350) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6229 | {<br>                "recipe_order": 3,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 660,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
