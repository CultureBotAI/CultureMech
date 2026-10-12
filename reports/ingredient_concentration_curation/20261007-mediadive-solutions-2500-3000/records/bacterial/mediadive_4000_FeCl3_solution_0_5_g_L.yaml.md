# Solution Concentration Review: FeCl3 solution 0.5 g/L

- Record: data/normalized_yaml/bacterial/mediadive_4000_FeCl3_solution_0_5_g_L.yaml
- ID: CultureMech:013060
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b4bc04629974ab05dbb2169cdd3d8b8c071b6bb5d3a72a30552ae2fad0c9203e`
- Proposed/result SHA256: `d3cc8f6494e8f3c67cca16da1667aaec53ac99e3a01f82a33a7d17998c53432f`
- Source: https://mediadive.dsmz.de/rest/solution/4000
- Source SHA256: 8ef052cd6013d5b44cdedc55c72c108c0505b43a78a63a5ab7974954f950cae7
- Retrieved: 2026-10-07T09:27:21.442534+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeCl3 x 6 H2O | {"unit": "G_PER_L", "value": "0.5"} | {"unit": "G_PER_L", "value": "0.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4000 | {<br>                "recipe_order": 1,<br>                "compound": "FeCl3 x 6 H2O",<br>                "compound_id": 82,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.15,<br>                "unit": "g",<br>                "g_l": 0.5,<br>                "mmol_l": 1.84982,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=82) | Provider explicitly reports g_l=0.5. Arithmetic check: 0.15 g * 1 g/g / (300 ml / 1000 ml per L) = 0.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 300. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4000 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 300,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
