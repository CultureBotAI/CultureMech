# Solution Concentration Review: Pyrrole-2-carboxylic acid solution

- Record: data/normalized_yaml/bacterial/mediadive_5622_Pyrrole-2-carboxylic_acid_solution.yaml
- ID: CultureMech:014497
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2de59f25c6221bcf02886a91bbb6ee3ee4ee9347887ad1ef553fc8aae116ce72`
- Proposed/result SHA256: `2de59f25c6221bcf02886a91bbb6ee3ee4ee9347887ad1ef553fc8aae116ce72`
- Source: https://mediadive.dsmz.de/rest/solution/5622
- Source SHA256: 58c929f638748e05964f9ae72e882443666130040ab570eb5b945f274532c9b3
- Retrieved: 2026-10-07T09:56:42.136688+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Pyrrole-2-carboxylic acid | {"unit": "G_PER_L", "value": "1111"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5622 | {<br>                "recipe_order": 1,<br>                "compound": "Pyrrole-2-carboxylic acid",<br>                "compound_id": 2108,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "M",<br>                "g_l": 1111,<br>                "mmol_l": 10000,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2108) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Potassium phosphate buffer | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5622 | {<br>                "recipe_order": 2,<br>                "compound": "Potassium phosphate buffer",<br>                "compound_id": 275,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "50 mM; pH 7.2",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": 50,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=275) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
