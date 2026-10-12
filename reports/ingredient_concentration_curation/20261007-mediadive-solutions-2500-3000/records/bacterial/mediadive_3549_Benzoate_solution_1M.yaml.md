# Solution Concentration Review: Benzoate solution (1M)

- Record: data/normalized_yaml/bacterial/mediadive_3549_Benzoate_solution_1M.yaml
- ID: CultureMech:012651
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2999962fc52294e8a7cd1684034c4828e4bb1e0f65703a9d2e0b8d1ea0cbb739`
- Proposed/result SHA256: `2e22f125e411967d2a3a4434d9b278a5360c8da553805914af68cfcd42ad2dba`
- Source: https://mediadive.dsmz.de/rest/solution/3549
- Source SHA256: 5e1a34bd530c54caedbb2fe0868f03ff29ad8a3c8f2ef9a948e78cf2dc1d61db
- Retrieved: 2026-10-07T09:22:27.797526+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodiumbenzoate | {"unit": "G_PER_L", "value": "144"} | {"unit": "G_PER_L", "value": "144"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3549 | {<br>                "recipe_order": 1,<br>                "compound": "Sodiumbenzoate",<br>                "compound_id": 1562,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 14.4,<br>                "unit": "g",<br>                "g_l": 144,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1562) | Provider explicitly reports g_l=144. Arithmetic check: 14.4 g * 1 g/g / (100 ml / 1000 ml per L) = 144 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3549 | {<br>                "recipe_order": 2,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "mL",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
