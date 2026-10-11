# Solution Concentration Review: 30 mM CaCl2 x 2 H2O

- Record: data/normalized_yaml/bacterial/mediadive_2506_30_mM_CaCl2_x_2_H2O.yaml
- ID: CultureMech:011869
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `513695cf2abb3587ace244424d16a753edb7e57c715ad289677853ce287b61e3`
- Proposed/result SHA256: `fd03db8e77c1c7be36a0e4f54731b452582b4e39a39439dd3837de896469866c`
- Source: https://mediadive.dsmz.de/rest/solution/2506
- Source SHA256: eed315fc42e0f08ea8910af5d080aa78013eb4c9a941f346685b5010168244cc
- Retrieved: 2026-10-07T09:13:16.508161+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | H2O | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2506 | {<br>                "recipe_order": 1,<br>                "compound": "H2O",<br>                "compound_id": 56,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=56) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "4.4"} | {"unit": "G_PER_L", "value": "4.4"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2506 | {<br>                "recipe_order": 2,<br>                "compound": "CaCl2 x 2 H2O",<br>                "compound_id": 7,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.44,<br>                "unit": "g",<br>                "g_l": 4.4,<br>                "mmol_l": 29.9289,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=7) | Provider explicitly reports g_l=4.4. Arithmetic check: 0.44 g * 1 g/g / (100 ml / 1000 ml per L) = 4.4 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
