# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_2278_Solution_B.yaml
- ID: CultureMech:011662
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `49430b6bf99b239c775dbeb7b6aff3c91f0641836d6e55cb0ececbd166339799`
- Proposed/result SHA256: `49430b6bf99b239c775dbeb7b6aff3c91f0641836d6e55cb0ececbd166339799`
- Source: https://mediadive.dsmz.de/rest/solution/2278
- Source SHA256: 4eeeaf1339a72d1294db00d5d02f5abfdea51707e38248b2a6c0db89a5ba4ea4
- Retrieved: 2026-10-07T09:10:53.632660+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2278 | {<br>                "recipe_order": 1,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "washed agar with double distilled water",<br>                "amount": 1.5,<br>                "unit": "%",<br>                "g_l": 15,<br>                "mmol_l": 44.5991,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=3) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2278 | {<br>                "recipe_order": 2,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
