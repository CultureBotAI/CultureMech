# Solution Concentration Review: Main sol. 448

- Record: data/normalized_yaml/bacterial/mediadive_899_Main_sol_448.yaml
- ID: CultureMech:015255
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f267c982e68c5db824ec1f9e6b36c826f5af0e86f4976f068ff16880956dfcf4`
- Proposed/result SHA256: `f267c982e68c5db824ec1f9e6b36c826f5af0e86f4976f068ff16880956dfcf4`
- Source: https://mediadive.dsmz.de/rest/solution/899
- Source SHA256: 07569065b94446166e8ea6e8d6dda574b2732c6ae1eb9f6fa773c81e030ef257
- Retrieved: 2026-10-07T08:47:36.465770+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Nicotinic acid | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/899 | {<br>                "recipe_order": 2,<br>                "compound": "Nicotinic acid",<br>                "compound_id": 139,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.05,<br>                "unit": "%",<br>                "g_l": 0.5,<br>                "mmol_l": 4.06141,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=139) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 442 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/899 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 442",<br>                "solution_id": 893,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
