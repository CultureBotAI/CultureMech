# Solution Concentration Review: Ascorbate solution (1M)

- Record: data/normalized_yaml/bacterial/mediadive_3548_Ascorbate_solution_1M.yaml
- ID: CultureMech:012650
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `590d9d51673b0d962a29779b0ad32bfb5dc5797bb63527906c9341eaba5e2f6d`
- Proposed/result SHA256: `4c6eb66323cbbd6db06fea4ef38bfbcf5396f1b1ce5f15155a3ccdfd8952f36d`
- Source: https://mediadive.dsmz.de/rest/solution/3548
- Source SHA256: 963aa7f6aff071b1e7d58b274ad1fe2f0fe830be8cdc0ff2c35e00022958a796
- Retrieved: 2026-10-07T09:22:27.013720+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Ascorbic acid | {"unit": "G_PER_L", "value": "176"} | {"unit": "G_PER_L", "value": "176"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3548 | {<br>                "recipe_order": 1,<br>                "compound": "Ascorbic acid",<br>                "compound_id": 112,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 17.6,<br>                "unit": "g",<br>                "g_l": 176,<br>                "mmol_l": 999.319,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=112) | Provider explicitly reports g_l=176. Arithmetic check: 17.6 g * 1 g/g / (100 ml / 1000 ml per L) = 176 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3548 | {<br>                "recipe_order": 2,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "mL",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
