# Solution Concentration Review: Vitamin B12 solution

- Record: data/normalized_yaml/bacterial/mediadive_3546_Vitamin_B12_solution.yaml
- ID: CultureMech:012648
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bb15e5dac755eb253ab4428d39abceb21357020663c261023befed2392d753aa`
- Proposed/result SHA256: `77e0be74586c3f2263bc33f8b33c40f13abd9310957842982de38c787c060c95`
- Source: https://mediadive.dsmz.de/rest/solution/3546
- Source SHA256: f90d88ad5bc31e12635c63a3d6c57e360a0720c83238b8cc133dfc1c613ea285
- Retrieved: 2026-10-07T09:22:25.448079+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Cyanocobalamine | {"unit": "G_PER_L", "value": "0.05"} | {"unit": "G_PER_L", "value": "0.05"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3546 | {<br>                "recipe_order": 1,<br>                "compound": "Cyanocobalamine",<br>                "compound_id": 847,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.5,<br>                "unit": "mg",<br>                "g_l": 0.05,<br>                "mmol_l": 0.0368895,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=847) | Provider explicitly reports g_l=0.05. Arithmetic check: 2.5 mg * 0.001 g/mg / (50 ml / 1000 ml per L) = 0.05 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3546 | {<br>                "recipe_order": 2,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "mL",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
