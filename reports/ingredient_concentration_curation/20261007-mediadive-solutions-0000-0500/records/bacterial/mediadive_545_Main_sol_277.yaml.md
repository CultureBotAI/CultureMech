# Solution Concentration Review: Main sol. 277

- Record: data/normalized_yaml/bacterial/mediadive_545_Main_sol_277.yaml
- ID: CultureMech:014363
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6d0793f35a29cc8da6e5ef5df4416c6b9b1e409717ec5d5326afbb5f14aa84f4`
- Proposed/result SHA256: `c04ceec3f32448d8f7a952cff04b532e91f03858484727f5f66261539954b9a5`
- Source: https://mediadive.dsmz.de/rest/solution/545
- Source SHA256: 34f939a02042bbe9c01137133bfb8daee909e8384c7e80dd0d08fd2e4f39e19b
- Retrieved: 2026-10-07T08:24:26.029980+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Agar | {"unit": "G_PER_L", "value": "20"} | {"unit": "G_PER_L", "value": "20"} | evidence_only | https://mediadive.dsmz.de/rest/solution/545 | {<br>                "recipe_order": 1,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": 20,<br>                "mmol_l": 59.4654,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=3) | Provider explicitly reports g_l=20. Arithmetic check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Water | {"unit": "PERCENT_V_V", "value": "800"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/545 | {<br>                "recipe_order": 2,<br>                "compound": "Water",<br>                "compound_id": 754,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 800,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=754) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[2]` | Cherry extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/545 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Cherry extract",<br>                "solution_id": 5596,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
