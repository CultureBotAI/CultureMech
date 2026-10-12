# Solution Concentration Review: Bicarbonate solution (1M)

- Record: data/normalized_yaml/bacterial/mediadive_3547_Bicarbonate_solution_1M.yaml
- ID: CultureMech:012649
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `99c68b8c7bd2a12360af5dce4d5174c4d5ab5efff30d020189e9238a3879f82d`
- Proposed/result SHA256: `f110b765e31687d4b96b8d13395055479058bf9a6b9d68cb07f64a7910b52296`
- Source: https://mediadive.dsmz.de/rest/solution/3547
- Source SHA256: 5fecab918313fa899dbdea08a35dd6a0a6dbe8f06384565d2ad7fce671b20c25
- Retrieved: 2026-10-07T09:22:26.236552+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "84"} | {"unit": "G_PER_L", "value": "84"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3547 | {<br>                "recipe_order": 1,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 84,<br>                "unit": "g",<br>                "g_l": 84,<br>                "mmol_l": 999.917,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Provider explicitly reports g_l=84. Arithmetic check: 84 g * 1 g/g / (1000 ml / 1000 ml per L) = 84 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3547 | {<br>                "recipe_order": 2,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "mL",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
