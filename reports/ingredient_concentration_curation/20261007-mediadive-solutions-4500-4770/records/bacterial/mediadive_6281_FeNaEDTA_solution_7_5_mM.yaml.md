# Solution Concentration Review: FeNaEDTA solution (7.5 mM)

- Record: data/normalized_yaml/bacterial/mediadive_6281_FeNaEDTA_solution_7_5_mM.yaml
- ID: CultureMech:014962
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a64936328247462bdd0b27dfbf3fd6b518cf9acf83bad303502ca3486b537c62`
- Proposed/result SHA256: `ef666cfceedb2ecb494e9e0c4c7b091f193cd1a4cd5fb5434106e674f2ca4526`
- Source: https://mediadive.dsmz.de/rest/solution/6281
- Source SHA256: 659e14b74954cf589a79562f7773ea4e4ca0cfb2912431212e02105466cb8b0f
- Retrieved: 2026-10-07T10:01:58.226597+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeNa-EDTA | {"unit": "G_PER_L", "value": "2.753"} | {"unit": "G_PER_L", "value": "2.753"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6281 | {<br>                "recipe_order": 2,<br>                "compound": "FeNa-EDTA",<br>                "compound_id": 1230,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2753,<br>                "unit": "mg",<br>                "g_l": 2.753,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1230) | Provider explicitly reports g_l=2.753. Arithmetic check: 2753 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 2.753 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6281 | {<br>                "recipe_order": 3,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
