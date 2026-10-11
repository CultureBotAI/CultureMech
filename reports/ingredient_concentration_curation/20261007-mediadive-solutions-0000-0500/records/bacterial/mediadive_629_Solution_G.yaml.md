# Solution Concentration Review: Solution G

- Record: data/normalized_yaml/bacterial/mediadive_629_Solution_G.yaml
- ID: CultureMech:014976
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6b74566cce9dd63d9c71d23df1fb934b879e85eaf64ba59b434524b291081bb1`
- Proposed/result SHA256: `6b74566cce9dd63d9c71d23df1fb934b879e85eaf64ba59b434524b291081bb1`
- Source: https://mediadive.dsmz.de/rest/solution/629
- Source SHA256: 006f14b9cbe815ff61b048b8f4152ee0f8892ac37d7f82cedaeac9aef31fe9fd
- Retrieved: 2026-10-07T08:25:23.554415+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | L-α-Phosphatidylcholine | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/629 | {<br>                "recipe_order": 1,<br>                "compound": "L-\u03b1-Phosphatidylcholine",<br>                "compound_id": 2082,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "SIGMA P3556",<br>                "amount": 5,<br>                "unit": "mg",<br>                "g_l": 5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2082) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Methanol | {"unit": "G_PER_L", "value": "792"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/629 | {<br>                "recipe_order": 2,<br>                "compound": "Methanol",<br>                "compound_id": 226,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": 792,<br>                "mmol_l": 24717.6,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=226) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
