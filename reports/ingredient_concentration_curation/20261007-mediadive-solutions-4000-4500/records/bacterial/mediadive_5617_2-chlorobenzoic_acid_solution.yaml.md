# Solution Concentration Review: 2-chlorobenzoic acid solution

- Record: data/normalized_yaml/bacterial/mediadive_5617_2-chlorobenzoic_acid_solution.yaml
- ID: CultureMech:014492
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `49d6063d2c373c07041b1af0140bb6f051f6c213444241cfd883f1e61f235bf9`
- Proposed/result SHA256: `49d6063d2c373c07041b1af0140bb6f051f6c213444241cfd883f1e61f235bf9`
- Source: https://mediadive.dsmz.de/rest/solution/5617
- Source SHA256: 98610de14286d7407fb85bafa5324eaf6d3910fb3c1bdc56b79a2106b46d269f
- Retrieved: 2026-10-07T09:56:39.008599+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 2-Chlorobenzoic acid | {"unit": "G_PER_L", "value": "78.3"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5617 | {<br>                "recipe_order": 1,<br>                "compound": "2-Chlorobenzoic acid",<br>                "compound_id": 2103,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 78.3,<br>                "unit": "g/l",<br>                "g_l": 78.3,<br>                "mmol_l": 500.096,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2103) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5617 | {<br>                "recipe_order": 2,<br>                "compound": "Water",<br>                "compound_id": 754,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=754) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
