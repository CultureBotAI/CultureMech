# Solution Concentration Review: Main sol. 780

- Record: data/normalized_yaml/bacterial/mediadive_1585_Main_sol_780.yaml
- ID: CultureMech:011043
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `085f1e76c221669d9f2322e967adc7186b0f04929174c175d0e67366edc16acb`
- Proposed/result SHA256: `afb853ac0b485059a8565c7866690eac7f1947297daaa958de04ba0082f57204`
- Source: https://mediadive.dsmz.de/rest/solution/1585
- Source SHA256: 0a2950d90c800c72da47beb5e79e97996c0789571b84b0bd0f17669024877fcf
- Retrieved: 2026-10-07T08:54:18.369548+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Mycobactine J | {"unit": "G_PER_L", "value": "0.002"} | {"unit": "G_PER_L", "value": "0.002"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1585 | {<br>                "recipe_order": 1,<br>                "compound": "Mycobactine J",<br>                "compound_id": 2139,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "mg",<br>                "g_l": 0.002,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2139) | Provider explicitly reports g_l=0.002. Arithmetic check: 2 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.002 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Absolute ethanol | {"unit": "PERCENT_V_V", "value": "4"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1585 | {<br>                "recipe_order": 2,<br>                "compound": "Absolute ethanol",<br>                "compound_id": 788,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=788) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[2]` | Main sol. 645 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1585 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 645",<br>                "solution_id": 1369,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
